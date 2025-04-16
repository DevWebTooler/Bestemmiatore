document.addEventListener('DOMContentLoaded', () => {
    const generateButton = document.getElementById('generate-button');
    const resultContainer = document.getElementById('result-container');
    const resultText = document.getElementById('result-text');
    const copyButton = document.getElementById('copy-button');
    const shareButton = document.getElementById('share-button');
    const shareMenu = document.getElementById('share-menu');
    const notification = document.getElementById('notification');
    const generationCounter = document.getElementById('generation-counter');
    const themeToggle = document.getElementById('theme-toggle');
    let generations = 0;

    // Theme Management
    const getTheme = () => localStorage.getItem('theme') || 'light';
    const setTheme = (theme) => {
        localStorage.setItem('theme', theme);
        document.documentElement.setAttribute('data-theme', theme);
        document.querySelectorAll('.theme-toggle').forEach(toggle => {
            toggle.innerHTML = theme === 'dark' ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
        });
    };

    // Initialize theme from localStorage
    const savedTheme = getTheme();
    setTheme(savedTheme);
    
    // Theme toggle listener
    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const newTheme = getTheme() === 'dark' ? 'light' : 'dark';
            setTheme(newTheme);
        });
    }

    generateButton.addEventListener('click', async () => {
        try {
            const response = await fetch('/generate');
            const data = await response.json();
            
            // Update counter
            generations++;
            generationCounter.textContent = `Generazioni: ${generations}`;
            
            // Show result with animation
            resultText.textContent = data.result;
            resultContainer.classList.remove('hidden');
            resultContainer.classList.add('slide-in');
            
            // Remove animation class after animation completes
            setTimeout(() => {
                resultContainer.classList.remove('slide-in');
            }, 300);
        } catch (error) {
            console.error('Errore:', error);
            resultText.textContent = 'Si è verificato un errore durante la generazione.';
        }
    });

    // Copy to clipboard functionality
    copyButton.addEventListener('click', async () => {
        try {
            await navigator.clipboard.writeText(resultText.textContent);
            showNotification('Copiato negli appunti!');
        } catch (err) {
            console.error('Errore durante la copia:', err);
            showNotification('Errore durante la copia', 'error');
        }
    });

    // Share functionality
    shareButton.addEventListener('click', () => {
        shareMenu.classList.toggle('show');
    });

    // Close share menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!shareButton.contains(e.target) && !shareMenu.contains(e.target)) {
            shareMenu.classList.remove('show');
        }
    });

    // Handle share buttons
    document.querySelectorAll('.share-button').forEach(button => {
        button.addEventListener('click', () => {
            const platform = button.dataset.platform;
            const text = encodeURIComponent(resultText.textContent);
            let url;

            switch (platform) {
                case 'whatsapp':
                    url = `https://wa.me/?text=${text}`;
                    break;
                case 'telegram':
                    url = `https://t.me/share/url?url=&text=${text}`;
                    break;
                case 'twitter':
                    url = `https://twitter.com/intent/tweet?text=${text}`;
                    break;
            }

            if (url) {
                window.open(url, '_blank');
            }
            shareMenu.classList.remove('show');
        });
    });

    // Handle feedback buttons
    document.querySelectorAll('.feedback-button').forEach(button => {
        button.addEventListener('click', () => {
            const wasActive = button.classList.contains('active');
            
            // Remove active class from all feedback buttons
            document.querySelectorAll('.feedback-button').forEach(btn => 
                btn.classList.remove('active')
            );
            
            if (!wasActive) {
                button.classList.add('active');
                const isLike = button.classList.contains('like');
                showNotification(`Grazie per il ${isLike ? 'like' : 'feedback'}!`);
            }
        });
    });

    // Notification helper
    function showNotification(message, type = 'success') {
        notification.textContent = message;
        notification.className = `notification ${type}`;
        notification.classList.remove('hidden');
        notification.classList.add('show');
        
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => {
                notification.classList.add('hidden');
            }, 300);
        }, 2000);
    }
});