// Landing Page JavaScript for Group 9 Freelance Platform

document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS (Animate On Scroll)
    AOS.init({
        duration: 800,
        easing: 'ease',
        once: true,
        offset: 100
    });
    
    // Navbar scroll effect
    const header = document.querySelector('header');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
    
    // Mobile menu toggle
    const navbarToggle = document.querySelector('.navbar-toggle');
    const navbarNav = document.querySelector('.navbar-nav');
    
    if (navbarToggle && navbarNav) {
        navbarToggle.addEventListener('click', function() {
            navbarNav.classList.toggle('show');
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const headerHeight = document.querySelector('header').offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                
                // Close mobile menu if open
                if (navbarNav.classList.contains('show')) {
                    navbarNav.classList.remove('show');
                }
            }
        });
    });
    
    // Testimonial slider (simple version)
    const testimonialList = document.querySelector('.testimonial-list');
    if (testimonialList && testimonialList.children.length > 0) {
        let currentIndex = 0;
        const testimonials = testimonialList.children;
        const totalTestimonials = testimonials.length;
        
        // Auto-scroll testimonials
        setInterval(() => {
            currentIndex = (currentIndex + 1) % totalTestimonials;
            testimonialList.scrollTo({
                left: testimonials[currentIndex].offsetLeft,
                behavior: 'smooth'
            });
        }, 5000);
    }
    
    // Counter animation for statistics
    const counters = document.querySelectorAll('.counter');
    if (counters.length > 0) {
        const counterObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counter = entry.target;
                    const target = parseInt(counter.getAttribute('data-target'));
                    const duration = 2000; // 2 seconds
                    const step = Math.ceil(target / (duration / 16)); // 60fps
                    
                    let current = 0;
                    const updateCounter = () => {
                        current += step;
                        if (current < target) {
                            counter.textContent = current;
                            requestAnimationFrame(updateCounter);
                        } else {
                            counter.textContent = target;
                        }
                    };
                    
                    updateCounter();
                    observer.unobserve(counter);
                }
            });
        }, { threshold: 0.5 });
        
        counters.forEach(counter => {
            counterObserver.observe(counter);
        });
    }
    
    // Typed.js for hero section (if available)
    const typedElement = document.querySelector('.typed-text');
    if (typedElement && typeof Typed !== 'undefined') {
        new Typed(typedElement, {
            strings: [
                'Freelancers',
                'Web Developers',
                'Designers',
                'Writers',
                'Marketers'
            ],
            typeSpeed: 80,
            backSpeed: 40,
            backDelay: 1500,
            loop: true
        });
    }
    
    console.log('Group 9 Freelance Platform landing page initialized Muhahaahah');
});
