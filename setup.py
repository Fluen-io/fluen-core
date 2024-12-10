from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fluen",
    version="0.1.4",
    packages=find_packages(where="src"),
    package_dir={"": "src"},  # Tell setuptools packages are under src
    python_requires=">=3.8",
    include_package_data=True,
    install_requires=[
        "click>=8.0.0",           # CLI interface
        "gitpython>=3.1.0",       # Git operations
        "pyyaml>=6.0",           # YAML configuration
        "rich>=10.0.0",          # Rich text and progress bars
        "jinja2>=3.0.0",         # Template rendering
        "aiohttp>=3.8.0",        # Async HTTP client
        "openai>=1.0.0",         # OpenAI API
        "mistralai>=0.0.7",      # Mistral AI API
        "markdown>=3.5.0",       # Process markdown in templates
        "bleach>=6.1.0",         # For HTML sanitization
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "mypy>=1.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "fluen=fluen.cli:cli",
        ],
    },
    # Metadata
    author="Abi Chatterjee",
    author_email="abi@fluen.io",
    description="LLM-based AI powered Code Documentation Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="documentation, llm, code-analysis",
    url="https://github.com/Fluen-io/fluen-core",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Documentation",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)