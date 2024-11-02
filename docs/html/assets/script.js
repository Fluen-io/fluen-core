// Search functionality
class DocumentationSearch {
    constructor() {
        this.searchIndex = null;
        this.searchInput = document.querySelector('.search-input');
        this.searchResults = document.querySelector('.search-results');
        this.currentResults = [];
        
        this.initializeSearch();
    }

    async initializeSearch() {
        // Load search index
        try {
            const response = await fetch('../search-index.json');
            this.searchIndex = await response.json();
            this.setupEventListeners();
        } catch (error) {
            console.error('Failed to load search index:', error);
        }
    }

    setupEventListeners() {
        this.searchInput?.addEventListener('input', () => this.handleSearch());
        this.searchInput?.addEventListener('focus', () => {
            document.body.classList.add('search-active');
        });
        
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.search-container')) {
                document.body.classList.remove('search-active');
            }
        });
    }

    handleSearch() {
        const query = this.searchInput.value.toLowerCase();
        if (!query) {
            this.clearResults();
            return;
        }

        const results = this.performSearch(query);
        this.displayResults(results);
    }

    performSearch(query) {
        if (!this.searchIndex) return [];

        return Object.entries(this.searchIndex)
            .flatMap(([file, data]) => {
                const matches = [];
                
                // Search in file path
                if (file.toLowerCase().includes(query)) {
                    matches.push({
                        type: 'file',
                        file,
                        name: file,
                        excerpt: data.purpose
                    });
                }
                
                // Search in elements
                data.elements?.forEach(element => {
                    if (element.name.toLowerCase().includes(query) ||
                        element.purpose.toLowerCase().includes(query)) {
                        matches.push({
                            type: 'element',
                            file,
                            name: element.name,
                            excerpt: element.purpose
                        });
                    }
                });
                
                return matches;
            })
            .slice(0, 10); // Limit results
    }

    displayResults(results) {
        this.currentResults = results;
        
        const html = results.map((result, index) => `
            <div class="search-result-item" data-index="${index}">
                <div class="result-title">
                    <strong>${result.name}</strong>
                    <span class="result-type">${result.type}</span>
                </div>
                <div class="result-excerpt">${result.excerpt}</div>
                <div class="result-file">${result.file}</div>
            </div>
        `).join('');
        
        this.searchResults.innerHTML = html;
        
        // Add click handlers
        this.searchResults.querySelectorAll('.search-result-item').forEach(item => {
            item.addEventListener('click', () => this.handleResultClick(item));
        });
    }

    handleResultClick(item) {
        const result = this.currentResults[item.dataset.index];
        let url;
        
        if (result.type === 'file') {
            url = `reference/${result.file.replace('/', '_')}.html`;
        } else {
            url = `reference/${result.file.replace('/', '_')}.html#${result.name}`;
        }
        
        window.location.href = url;
    }

    clearResults() {
        this.currentResults = [];
        this.searchResults.innerHTML = '';
        document.body.classList.remove('search-active');
    }
}

// Highlight active navigation item
function highlightCurrentPage() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.sidebar a');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
}

// Initialize components
document.addEventListener('DOMContentLoaded', () => {
    new DocumentationSearch();
    highlightCurrentPage();
});

// Handle mobile navigation
const mobileMenuButton = document.querySelector('.mobile-menu-button');
const sidebar = document.querySelector('.sidebar');

mobileMenuButton?.addEventListener('click', () => {
    sidebar.classList.toggle('active');
});