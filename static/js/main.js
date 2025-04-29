// Main JavaScript file for Group 9 Freelance Platform

document.addEventListener('DOMContentLoaded', function() {

    console.log('Group 9 Freelance Platform initialized');
});


function handleFormSubmit(event) {
    event.preventDefault();

}


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