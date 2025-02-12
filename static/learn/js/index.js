function toggleMenu() {
    const menu = document.getElementById('hamburgerMenu');
    menu.classList.toggle('active');
}

let dropdownTimeout;

const dropdown = document.querySelector('.username-dropdown');
const dropdownMenu = document.querySelector('.username-dropdown-menu');

// Show dropdown when hovering over the username-dropdown
dropdown.addEventListener('mouseenter', () => {
    clearTimeout(dropdownTimeout); // Cancel any hiding timeout
    dropdownMenu.style.display = 'block';
});

// Keep dropdown visible when hovering over the dropdown menu
dropdownMenu.addEventListener('mouseenter', () => {
    clearTimeout(dropdownTimeout); // Cancel any hiding timeout
    dropdownMenu.style.display = 'block';
});

// Hide dropdown when the mouse leaves both the username-dropdown and dropdown menu
dropdown.addEventListener('mouseleave', () => {
    dropdownTimeout = setTimeout(() => {
        dropdownMenu.style.display = 'none';
    }, 200); // Add a slight delay to prevent immediate hiding
});

dropdownMenu.addEventListener('mouseleave', () => {
    dropdownTimeout = setTimeout(() => {
        dropdownMenu.style.display = 'none';
    }, 200); // Add a slight delay to prevent immediate hiding
});