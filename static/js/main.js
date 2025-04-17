// Main JavaScript file for Group 8 Freelance Platform

document.addEventListener('DOMContentLoaded', function() {
    // Initialize any necessary functionality
    console.log('Group 8 Freelance Platform initialized');
});

// Utility function to handle form submissions
function handleFormSubmit(event) {
    event.preventDefault();
    // Add form handling logic here
}

// Utility function to show/hide loading spinner
function toggleLoading(show = true) {
    const loader = document.getElementById('loader');
    if (loader) {
        loader.style.display = show ? 'block' : 'none';
    }
}

// Utility function for responsive navigation
function toggleMobileMenu() {
    const nav = document.querySelector('.mobile-nav');
    if (nav) {
        nav.classList.toggle('active');
    }
} 