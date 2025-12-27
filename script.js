let currentLang = 'en';

function openTab(tabName) {
    // Hide all tab contents
    const contents = document.getElementsByClassName('tab-content');
    for (let i = 0; i < contents.length; i++) {
        contents[i].classList.remove('active');
    }

    // Remove active class from all buttons
    const buttons = document.getElementsByClassName('tab-btn');
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove('active');
    }

    // Show the specific tab and set button as active
    document.getElementById(tabName).classList.add('active');

    // Find the button that called this function (rough approximation if not passed directly)
    // Actually simpler: iterate buttons and if inner text matches or onclick matches... 
    // Easier way: passing 'event' is cleaner, but let's just query selector for simplicity based on text content or index logic if needed.
    // However, the onclick in HTML doesn't pass 'this'. 
    // Let's rely on simple DOM traversal or just selecting by matching text/attribute.
    // Alternative: Add ID to buttons? No, let's just loop and check onclick attribute roughly or use event delegation.
    // Correction: Let's just fix the HTML to pass 'event' or use querySelector for buttons. 
    // To keep html simple, I will iterate buttons and check if their onclick contains the tabName.
    for (let i = 0; i < buttons.length; i++) {
        if (buttons[i].getAttribute('onclick').includes(`'${tabName}'`)) {
            buttons[i].classList.add('active');
        }
    }
}

function toggleLanguage() {
    currentLang = currentLang === 'en' ? 'th' : 'en';

    // Update Switcher Button Text
    const langLabel = document.getElementById('curr-lang');
    langLabel.textContent = currentLang.toUpperCase();

    // Update all distinct text elements
    const elements = document.querySelectorAll('.lang-text');
    elements.forEach(el => {
        const text = el.getAttribute(`data-${currentLang}`);
        if (text) {
            // Check if it has HTML content (like <br>)
            if (text.includes('<') && text.includes('>')) {
                el.innerHTML = text;
            } else {
                el.textContent = text;
            }
        }
    });

    // Save preference (Optional)
    localStorage.setItem('preferred-lang', currentLang);
}

// Load saved language on startup
document.addEventListener('DOMContentLoaded', () => {
    const savedLang = localStorage.getItem('preferred-lang');
    if (savedLang && savedLang !== currentLang) {
        toggleLanguage(); // Will switch to saved lang
    }
});
