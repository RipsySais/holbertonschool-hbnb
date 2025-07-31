// Modern HBNB Scripts 2025

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize all components
    initAnimations();
    initSearchForm();
    initNavbarEffects();
    initDestinationCards();
    initScrollEffects();
    initFormValidation();
    
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Initialize animations
function initAnimations() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    document.querySelectorAll('.card, .destination-card, .feature-icon').forEach(el => {
        observer.observe(el);
    });
    
    // Hero section animations
    const heroContent = document.querySelector('.hero-content');
    const kitchenPreview = document.querySelector('.kitchen-preview');
    
    if (heroContent) {
        setTimeout(() => {
            heroContent.classList.add('animate-slide-in-left');
        }, 300);
    }
    
    if (kitchenPreview) {
        setTimeout(() => {
            kitchenPreview.classList.add('animate-slide-in-right');
        }, 600);
    }
}

// Initialize search form functionality
function initSearchForm() {
    const searchForm = document.querySelector('.search-form');
    const searchButton = document.querySelector('.search-form .btn-primary');
    
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Show loading state
            if (searchButton) {
                const originalText = searchButton.innerHTML;
                searchButton.innerHTML = '<span class="loading"></span> Recherche...';
                searchButton.disabled = true;
                
                // Simulate search
                setTimeout(() => {
                    searchButton.innerHTML = originalText;
                    searchButton.disabled = false;
                    
                    // Show success message
                    showNotification('Recherche effectuée avec succès !', 'success');
                }, 2000);
            }
        });
        
        // Form field animations
        const formFields = searchForm.querySelectorAll('.form-control, .form-select');
        formFields.forEach(field => {
            field.addEventListener('focus', function() {
                this.parentElement.classList.add('focused');
            });
            
            field.addEventListener('blur', function() {
                if (!this.value) {
                    this.parentElement.classList.remove('focused');
                }
            });
        });
    }
}

// Initialize navbar effects
function initNavbarEffects() {
    const navbar = document.querySelector('.navbar');
    
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
        
        // Mobile menu toggle animation
        const navbarToggler = document.querySelector('.navbar-toggler');
        const navbarCollapse = document.querySelector('.navbar-collapse');
        
        if (navbarToggler && navbarCollapse) {
            navbarToggler.addEventListener('click', function() {
                navbarCollapse.classList.toggle('show');
            });
        }
    }
}

// Initialize destination cards
function initDestinationCards() {
    const destinationCards = document.querySelectorAll('.destination-card');
    
    destinationCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
        
        card.addEventListener('click', function() {
            const destination = this.querySelector('h6').textContent;
            showNotification(`Exploration de ${destination} en cours...`, 'info');
        });
    });
}

// Initialize scroll effects
function initScrollEffects() {
    let ticking = false;
    
    function updateScrollEffects() {
        const scrolled = window.pageYOffset;
        const parallaxElements = document.querySelectorAll('.kitchen-island, .stool, .appliance');
        
        parallaxElements.forEach((element, index) => {
            const speed = 0.5 + (index * 0.1);
            const yPos = -(scrolled * speed);
            element.style.transform = `translateY(${yPos}px)`;
        });
        
        ticking = false;
    }
    
    function requestTick() {
        if (!ticking) {
            requestAnimationFrame(updateScrollEffects);
            ticking = true;
        }
    }
    
    window.addEventListener('scroll', requestTick);
}

// Initialize form validation
function initFormValidation() {
    const form = document.querySelector('.search-form');
    
    if (form) {
        const inputs = form.querySelectorAll('input, select');
        
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                validateField(this);
            });
            
            input.addEventListener('input', function() {
                if (this.classList.contains('is-invalid')) {
                    validateField(this);
                }
            });
        });
    }
}

// Validate individual form field
function validateField(field) {
    const value = field.value.trim();
    const fieldName = field.getAttribute('id');
    
    // Remove existing validation classes
    field.classList.remove('is-valid', 'is-invalid');
    
    // Validation rules
    let isValid = true;
    let errorMessage = '';
    
    switch (fieldName) {
        case 'address':
            if (value.length < 3) {
                isValid = false;
                errorMessage = 'Veuillez entrer une destination valide';
            }
            break;
            
        case 'arrival':
        case 'departure':
            if (value) {
                const date = new Date(value);
                const today = new Date();
                if (date < today) {
                    isValid = false;
                    errorMessage = 'La date ne peut pas être dans le passé';
                }
            }
            break;
            
        case 'adults':
        case 'children':
            if (value < 0) {
                isValid = false;
                errorMessage = 'Le nombre doit être positif';
            }
            break;
    }
    
    // Apply validation result
    if (isValid && value) {
        field.classList.add('is-valid');
    } else if (!isValid) {
        field.classList.add('is-invalid');
        showFieldError(field, errorMessage);
    }
}

// Show field error message
function showFieldError(field, message) {
    // Remove existing error message
    const existingError = field.parentElement.querySelector('.invalid-feedback');
    if (existingError) {
        existingError.remove();
    }
    
    // Create new error message
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.textContent = message;
    field.parentElement.appendChild(errorDiv);
}

// Show notification
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = `
        top: 20px;
        right: 20px;
        z-index: 9999;
        min-width: 300px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    `;
    
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Add to page
    document.body.appendChild(notification);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentElement) {
            notification.remove();
        }
    }, 5000);
}

// Kitchen animation effects
function initKitchenAnimations() {
    const kitchenElements = document.querySelectorAll('.kitchen-island, .stool, .appliance');
    
    kitchenElements.forEach((element, index) => {
        element.style.animationDelay = `${index * 0.2}s`;
        element.classList.add('floating');
    });
}

// Initialize kitchen animations after page load
setTimeout(initKitchenAnimations, 1000);

// Parallax effect for hero section
function initParallaxEffect() {
    const heroSection = document.querySelector('.hero-section');
    const heroBackground = document.querySelector('.hero-background');
    
    if (heroSection && heroBackground) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            heroBackground.style.transform = `translateY(${rate}px)`;
        });
    }
}

// Initialize parallax
initParallaxEffect();

// Add CSS for additional effects
const additionalStyles = `
    .navbar.scrolled {
        background: rgba(255, 255, 255, 0.98) !important;
        box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
    }
    
    .form-floating.focused label {
        color: var(--primary-color);
        transform: scale(0.85) translateY(-1rem) translateX(0.15rem);
    }
    
    .form-control.is-valid {
        border-color: #198754;
        box-shadow: 0 0 0 0.2rem rgba(25, 135, 84, 0.25);
    }
    
    .form-control.is-invalid {
        border-color: #dc3545;
        box-shadow: 0 0 0 0.2rem rgba(220, 53, 69, 0.25);
    }
    
    .invalid-feedback {
        display: block;
        color: #dc3545;
        font-size: 0.875rem;
        margin-top: 0.25rem;
    }
    
    .floating {
        animation: floating 3s ease-in-out infinite;
    }
    
    @keyframes floating {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
`;

// Inject additional styles
const styleSheet = document.createElement('style');
styleSheet.textContent = additionalStyles;
document.head.appendChild(styleSheet);

// Performance optimization
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Optimize scroll events
const optimizedScrollHandler = debounce(function() {
    // Scroll-based animations and effects
}, 16);

window.addEventListener('scroll', optimizedScrollHandler); 