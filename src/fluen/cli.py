import click
from pathlib import Path
from typing import Optional
from fluen.config import FluenConfig
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
import asyncio
from fluen.orchestrator import Orchestrator
from fluen.models.scan import ScanSelector, ScanOptions


class FluenContext:
    def __init__(self):
        self.config: Optional[FluenConfig] = None
        self.config_path: Path = Path('fluen_config.yml')
        self.console = Console()
        self.scan_options: Optional[ScanOptions] = None

pass_fluen_context = click.make_pass_decorator(FluenContext, ensure=True)

@click.group()
@click.option('--config', '-c', type=click.Path(exists=False, path_type=Path),
              default='fluen_config.yml', help='Path to configuration file')
@pass_fluen_context
def cli(ctx: FluenContext, config: Path):
    """Fluen - LLM-based code documentation generator."""
    ctx.config_path = config
    ctx.config = FluenConfig.load(config)
    ctx.config.ensure_directories()

@cli.group()
def docs():
    """Documentation related commands."""
    pass

@docs.command()
@click.option('--repo', '-r', help='Git repository URL')
@click.option('--scan', '-s', help='Selective scan selector (e.g., path:src/module)')
@click.option('--force', '-f', is_flag=True, help='Force analysis regardless of git status')
@pass_fluen_context
def generate(ctx: FluenContext, repo: Optional[str], scan: Optional[str], force: bool):
    """Generate documentation for the codebase."""
    try:
        # Initialize scan options
        if scan:
            try:
                ctx.scan_options = ScanOptions(scan, force=force)
            except ValueError as e:
                ctx.console.print(f"❌ Invalid scan selector: {e}")
                raise click.Abort()
        
        # Initialize orchestrator
        orchestrator = Orchestrator(ctx.config)
        
        # Run documentation generation
        async def run_generation():
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                console=ctx.console
            ) as progress:
                # Add initial task
                #task = progress.add_task("Initializing...", total=100)
                
                try:
                    success = await orchestrator.generate_documentation(
                        repo_url=repo,
                        scan_options=ctx.scan_options
                    )
                    if success:
                        #progress.update(task, completed=100, description="Documentation generated successfully!")
                        ctx.console.print("\n✨ Documentation generation complete!")
                        ctx.console.print(f"📚 Manifest output directory: {ctx.config.output_dir}")
                    else:
                        #progress.update(task, description="Documentation manifest generation failed!")
                        ctx.console.print("\n❌ Documentation manifest generation failed!")
                except Exception as e:
                    #progress.update(task, description=f"Error: {str(e)}")
                    ctx.console.print(f"\n❌ Error during documentation manifest generation: {str(e)}")
                    raise click.Abort()

        # Run the async generation process
        asyncio.run(run_generation())

    except Exception as e:
        ctx.console.print(f"❌ Error: {str(e)}")
        raise click.Abort()

@docs.command()
@click.option('--type', '-t', type=click.Choice(['html', 'md']), 
              help='Export format type')
@click.option('--output', '-o', type=click.Path(path_type=Path),
              help='Custom output directory')
@pass_fluen_context
def export(ctx: FluenContext, type: Optional[str], output: Optional[Path]):
    """Export documentation to specified format."""
    from .generator.doc_generator import DocumentationGenerator
    from .generator.templates.template_manager import TemplateManager
    from .generator.manifest import ManifestGenerator

    try:
        # Determine export type
        export_type = type or ctx.config.default_export_type
        
        # Determine output directory
        output_dir = output or ctx.config.output_dir
        manifest_path = ctx.config.output_dir / "manifest.json"

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=ctx.console
        ) as progress:
            task = progress.add_task(f"Exporting documentation to {export_type}...", total=100)

            try:
                # Check if manifest exists
                if not manifest_path.exists():
                    ctx.console.print("❌ Manifest file not found. Please run 'fluen docs generate' first.")
                    raise click.Abort()

                # Load manifest
                progress.update(task, completed=20, description="Loading manifest...")
                manifest_generator = ManifestGenerator(Path.cwd(), output_dir)
                manifest = manifest_generator.load_existing_manifest()

                if not manifest:
                    ctx.console.print("❌ Failed to load manifest.")
                    raise click.Abort()

                # Initialize template manager
                progress.update(task, completed=40, description="Initializing templates...")
                template_manager = TemplateManager()

                # Initialize documentation generator
                progress.update(task, completed=60, description="Generating documentation...")
                doc_generator = DocumentationGenerator(
                    manifest=manifest,
                    output_dir=output_dir,
                    template_manager=template_manager,
                    manifest_generator=manifest_generator
                )

                # Run export
                async def run_export():
                    return await doc_generator.generate(export_type)

                success = asyncio.run(run_export())

                if success:
                    progress.update(task, completed=100, description="Export complete!")
                    ctx.console.print("\n✨ Documentation exported successfully!")
                    ctx.console.print(f"📚 Output directory: {output_dir}/{export_type}")
                else:
                    progress.update(task, description="Export failed!")
                    ctx.console.print("\n❌ Documentation export failed!")

            except Exception as e:
                progress.update(task, description=f"Error: {str(e)}")
                ctx.console.print(f"\n❌ Error during export: {str(e)}")
                raise click.Abort()

    except Exception as e:
        ctx.console.print(f"❌ Error: {str(e)}")
        raise click.Abort()

if __name__ == '__main__':
    cli()
