// Configuration de base
const API_BASE_URL = 'http://localhost:5001/api/v1';
let currentUser = null;

/* ==================== */
/*  FONCTIONS UTILITAIRES */
/* ==================== */

function getCookie(name) {
    const cookies = document.cookie.split('; ');
    const cookie = cookies.find(c => c.startsWith(`${name}=`));
    return cookie ? cookie.split('=')[1] : null;
}

function setCookie(name, value, days = 1) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const secureFlag = window.location.protocol === 'https:' ? '; Secure' : '';
    document.cookie = `${name}=${value}; expires=${date.toUTCString()}; path=/; SameSite=Lax${secureFlag}`;
}

function deleteCookie(name) {
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
}

function showError(message, duration = 5000) {
    const errorElement = document.createElement('div');
    errorElement.className = 'error-message';
    errorElement.textContent = message;

    const dismissButton = document.createElement('button');
    dismissButton.textContent = 'Dissiper';
    dismissButton.onclick = () => errorElement.remove(); // Ajoute une fonctionnalité de dissipation
    errorElement.appendChild(dismissButton);

    document.body.prepend(errorElement);
    
    // Si aucun bouton n'est cliqué, retirer automatiquement après la durée
    setTimeout(() => errorElement.remove(), duration);
}


/* ==================== */
/*  GESTION AUTHENTIFICATION */
/* ==================== */

async function checkAuth() {
    const token = getCookie('auth_token');
    if (!token) return false;

    try {
        const response = await fetch(`${API_BASE_URL}/users/me`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        
        if (response.ok) {
            currentUser = await response.json();
            return true;
        }
    } catch (error) {
        console.error('Auth check failed:', error);
    }
    
    return false;
}

async function login(email, password) {
    const loginForm = document.getElementById('login-form');
    const submitBtn = loginForm?.querySelector('button[type="submit"]');
    
    try {
        submitBtn?.setAttribute('disabled', 'true');
        
        const response = await fetch(`${API_BASE_URL}/auth/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.message || 'Login failed');
        }

        const data = await response.json();
        setCookie('auth_token', data.token);
        currentUser = data.user;
        
        window.location.href = 'index.html';
        return data.user;
    } catch (error) {
        console.error('Login error:', error);
        showError(error.message);
        throw error;
    } finally {
        submitBtn?.removeAttribute('disabled');
    }
}

function logout() {
    deleteCookie('auth_token');
    currentUser = null;
    window.location.href = 'login.html';
}

function updateAuthUI(isAuthenticated) {
    document.querySelectorAll('.login-button').forEach(el => {
        el.style.display = isAuthenticated ? 'none' : 'block';
    });
    document.querySelectorAll('.logout-button').forEach(el => {
        el.style.display = isAuthenticated ? 'block' : 'none';
    });
    document.querySelectorAll('.auth-only').forEach(el => {
        el.style.display = isAuthenticated ? 'block' : 'none';
    });
}

/* ==================== */
/*  GESTION DES DONNÉES */
/* ==================== */

async function fetchData(endpoint, options = {}) {
    try {
        const token = getCookie('auth_token');
        const headers = {
            'Content-Type': 'application/json',
            ...(token && { 'Authorization': `Bearer ${token}` }),
            ...options.headers
        };

        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            ...options,
            headers
        });

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.message || `Request failed with status ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error(`Fetch error for ${endpoint}:`, error);
        throw error;
    }
}

// Fonctions spécifiques
async function fetchPlaces(filters = {}) {
    const query = new URLSearchParams(filters).toString();
    return fetchData(`/places?${query}`);
}

async function fetchPlaceDetails(placeId) {
    return fetchData(`/places/${placeId}`);
}

async function fetchReviews(placeId) {
    return fetchData(`/places/${placeId}/reviews`);
}

async function submitReview(placeId, rating, text) {
    return fetchData(`/places/${placeId}/reviews`, {
        method: 'POST',
        body: JSON.stringify({ rating, text })
    });
}

/* ==================== */
/*  RENDU DES PAGES */
/* ==================== */

function renderPlaces(places) {
    const container = document.getElementById('places-list');
    if (!container) return;

    container.innerHTML = places.map(place => `
        <article class="place-card">
            <div class="price_by_night">$${place.price_by_night}</div>
            <h2>${place.name}</h2>
            <div class="information">
                <div class="max_guest">
                    <img src="images/icon_group.png" alt="Guests" loading="lazy">
                    ${place.max_guest} Guest${place.max_guest !== 1 ? 's' : ''}
                </div>
                <div class="number_rooms">
                    <img src="images/icon_bed.png" alt="Bedrooms" loading="lazy">
                    ${place.number_rooms} Bedroom${place.number_rooms !== 1 ? 's' : ''}
                </div>
                <div class="number_bathrooms">
                    <img src="images/icon_bath.png" alt="Bathrooms" loading="lazy">
                    ${place.number_bathrooms} Bathroom${place.number_bathrooms !== 1 ? 's' : ''}
                </div>
            </div>
            <div class="description">${place.description}</div>
            <button class="details-button" data-id="${place.id}">View Details</button>
        </article>
    `).join('');

    // Gestion des clics sur les boutons de détails
    container.querySelectorAll('.details-button').forEach(btn => {
        btn.addEventListener('click', () => {
            window.location.href = `place.html?id=${btn.dataset.id}`;
        });
    });
}

function renderPlaceDetails(place) {
    const setTextContent = (id, text) => {
        const el = document.getElementById(id);
        if (el) el.textContent = text;
    };

    setTextContent('place-name', place.name);
    setTextContent('place-price', `$${place.price_by_night}`);
    setTextContent('place-description', place.description);
    setTextContent('place-owner', place.user?.name || 'Unknown');
    setTextContent('place-guests', `${place.max_guest} Guest${place.max_guest !== 1 ? 's' : ''}`);
    setTextContent('place-rooms', `${place.number_rooms} Bedroom${place.number_rooms !== 1 ? 's' : ''}`);
    setTextContent('place-bathrooms', `${place.number_bathrooms} Bathroom${place.number_bathrooms !== 1 ? 's' : ''}`);

    // Gestion des images
    const mainImage = document.getElementById('place-image');
    if (mainImage && place.images?.length > 0) {
        mainImage.src = place.images[0];
        mainImage.alt = place.name;
    }

    const thumbnailsContainer = document.querySelector('.thumbnail-container');
    if (thumbnailsContainer && place.images?.length > 1) {
        thumbnailsContainer.innerHTML = place.images.slice(1).map((image, index) => `
            <img src="${image}" alt="${place.name} - Image ${index + 2}" loading="lazy">
        `).join('');
    }

    // Commodités
    const amenitiesList = document.getElementById('amenities-list');
    if (amenitiesList) {
        amenitiesList.innerHTML = place.amenities?.map(amenity => `
            <li>${amenity.name}</li>
        `).join('') || '';
    }
}

function renderReviews(reviews) {
    const reviewsList = document.getElementById('reviews-list');
    if (!reviewsList) return;

    const reviewsCount = document.getElementById('reviews-count');
    if (reviewsCount) reviewsCount.textContent = `(${reviews.length})`;

    reviewsList.innerHTML = reviews.length === 0 ? 
        '<p>No reviews yet. Be the first to review!</p>' :
        reviews.map(review => `
            <div class="review-card">
                <h3 class="review-user">${review.user?.name || 'Anonymous'}</h3>
                <p class="review-date">${new Date(review.created_at).toLocaleDateString()}</p>
                <p class="review-rating">
                    <span class="stars">${'★'.repeat(review.rating)}${'☆'.repeat(5 - review.rating)}</span>
                    <span class="rating-text">${review.rating}/5</span>
                </p>
                <p class="review-text">${review.text}</p>
            </div>
        `).join('');
}

/* ==================== */
/*  INITIALISATION PAGES */
/* ==================== */

async function initPlacesPage() {
    try {
        const places = await fetchPlaces();
        renderPlaces(places);
        
        const searchBtn = document.getElementById('search-btn');
        if (searchBtn) {
            searchBtn.addEventListener('click', async () => {
                try {
                    const filters = {
                        min_price: document.getElementById('min-price')?.value,
                        max_price: document.getElementById('max-price')?.value,
                        amenities: Array.from(
                            document.querySelectorAll('input[name="amenity"]:checked')
                        ).map(cb => cb.value)
                    };
                    
                    const filteredPlaces = await fetchPlaces(filters);
                    renderPlaces(filteredPlaces);
                } catch (error) {
                    showError('Failed to filter places');
                }
            });
        }
    } catch (error) {
        showError('Failed to load places');
    }
}

async function initPlaceDetailsPage() {
    const urlParams = new URLSearchParams(window.location.search);
    const placeId = urlParams.get('id');
    
    if (!placeId) {
        window.location.href = 'index.html';
        return;
    }

    try {
        const [place, reviews] = await Promise.all([
            fetchPlaceDetails(placeId),
            fetchReviews(placeId)
        ]);
        
        renderPlaceDetails(place);
        renderReviews(reviews);
        
        const reviewForm = document.getElementById('review-form');
        if (reviewForm) {
            reviewForm.addEventListener('submit', async (e) => {
                e.preventDefault();
                
                try {
                    await submitReview(
                        placeId,
                        e.target['review-rating'].value,
                        e.target['review-text'].value
                    );
                    window.location.reload();
                } catch (error) {
                    showError('Failed to submit review');
                }
            });
        }
    } catch (error) {
        showError('Failed to load place details');
    }
}

async function initAddReviewPage() {
    const isAuthenticated = await checkAuth();
    if (!isAuthenticated) {
        window.location.href = 'login.html';
        return;
    }

    const urlParams = new URLSearchParams(window.location.search);
    const placeId = urlParams.get('place_id');
    
    if (!placeId) {
        window.location.href = 'index.html';
        return;
    }

    try {
        const place = await fetchPlaceDetails(placeId);
        document.getElementById('place-name').textContent = place.name;
        document.getElementById('place-id').value = placeId;
        
        const reviewForm = document.getElementById('review-form');
        if (reviewForm) {
            reviewForm.addEventListener('submit', async (e) => {
                e.preventDefault();
                
                try {
                    await submitReview(
                        placeId,
                        e.target.rating.value,
                        e.target.review.value
                    );
                    window.location.href = `place.html?id=${placeId}`;
                } catch (error) {
                    showError('Failed to submit review');
                }
            });
        }
    } catch (error) {
        showError('Failed to load place details');
    }
}

function initLoginPage() {
    const loginForm = document.getElementById('login-form');
    if (!loginForm) return;

    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        await login(e.target.email.value, e.target.password.value);
    });

    document.getElementById('logout-btn')?.addEventListener('click', (e) => {
        e.preventDefault();
        logout();
    });
}

/* ==================== */
/*  INITIALISATION APP */
/* ==================== */

document.addEventListener('DOMContentLoaded', async () => {
    // Gestion du logout
    document.addEventListener('click', (e) => {
        if (e.target.classList.contains('logout-button')) {
            e.preventDefault();
            logout();
        }
    });

    // Vérification auth et mise à jour UI
    const isAuthenticated = await checkAuth();
    updateAuthUI(isAuthenticated);

    // Protection des pages privées
    const protectedPages = ['add_review.html'];
    const currentPage = window.location.pathname.split('/').pop();
    
    if (protectedPages.includes(currentPage)) {
        const isAuthenticated = await checkAuth();
        if (!isAuthenticated) {
            window.location.href = 'login.html';
            return;
        }
    }

    // Routeur simple
    switch (currentPage) {
        case 'index.html':
            await initPlacesPage();
            break;
        case 'place.html':
            await initPlaceDetailsPage();
            break;
        case 'add_review.html':
            await initAddReviewPage();
            break;
        case 'login.html':
            initLoginPage();
            break;
    }
});