document.addEventListener("DOMContentLoaded", () => {


    // --- INDEPENDENT THEME PRELOADER LOGIC ---
    const preloader = document.getElementById('theme-preloader');
    
    // --- PURE CSS TIMELINE TRIGGER ---
    const playHomeChoreography = () => {
        const homeSection = document.getElementById('home-section');
        if (!homeSection) return;
        
        // Single 1000ms trigger. CSS animation-delay handles the rest flawlessly.
        setTimeout(() => {
            homeSection.classList.add('hero-scene-active');
        }, 1000);
    };
    
    const dismissPreloader = () => {
        if (!preloader) return;
        
        // Resource Management: Pause the video
        const themeVideo = document.getElementById('theme-preloader-video');
        if (themeVideo) themeVideo.pause();

        // 1. Fade out the overlay
        preloader.classList.add('preloader-hidden');
        
        // 2. Fade in the main site content & restore scrolling
        document.body.classList.remove('hide-content', 'no-scroll');
        document.body.classList.add('site-fade-in');
        
        // 3. Register the session
        sessionStorage.setItem('starkPreloaderPlayed', 'true');
        
        // 4. Safely destroy the overlay DOM node after CSS transition finishes
        setTimeout(() => {
            preloader.remove();
        }, 800);

        // 5. Trigger the Home Section cinematic timeline
        playHomeChoreography();
    };

    // --- INITIALIZATION ---
    if (sessionStorage.getItem('starkPreloaderPlayed') === 'true') {
        // [RETURNING USER] - INSTANT BYPASS
        if (preloader) preloader.remove();
        document.body.classList.remove('hide-content', 'no-scroll');
        document.body.classList.add('site-fade-in');
        
        // Trigger timeline instantly for returning users
        playHomeChoreography();
    } else {
        // [NEW USER] - PLAY SEQUENCE
        // Immediately lock the body to hide main content and prevent scrolling
        document.body.classList.add('hide-content', 'no-scroll');
        
        const preloaderVideo = document.getElementById('theme-preloader-video');
        let fallbackTimeout;

        // The Escape Instruction (User overrides timeline)
        const handleBypass = (e) => {
            if (e.key === 'Enter' || e.key === 'Escape') {
                if (fallbackTimeout) clearTimeout(fallbackTimeout);
                if (preloaderVideo) {
                    preloaderVideo.removeEventListener('ended', dismissPreloader);
                    preloaderVideo.removeEventListener('error', dismissPreloader);
                }
                document.removeEventListener('keydown', handleBypass);
                dismissPreloader();
            }
        };

        document.addEventListener('keydown', handleBypass);

        if (preloaderVideo) {
            // Wait for the video to organically finish
            preloaderVideo.addEventListener('ended', () => {
                if (fallbackTimeout) clearTimeout(fallbackTimeout);
                document.removeEventListener('keydown', handleBypass);
                dismissPreloader();
            });

            // Dismiss immediately if video fails to play/load
            preloaderVideo.addEventListener('error', () => {
                if (fallbackTimeout) clearTimeout(fallbackTimeout);
                document.removeEventListener('keydown', handleBypass);
                dismissPreloader();
            });

            // Fallback: If the video fails to load/play, dismiss after 3 seconds anyway
            fallbackTimeout = setTimeout(() => {
                if (preloaderVideo) {
                    preloaderVideo.removeEventListener('ended', dismissPreloader);
                    preloaderVideo.removeEventListener('error', dismissPreloader);
                }
                document.removeEventListener('keydown', handleBypass);
                dismissPreloader();
            }, 3000);
        } else {
            // Ultimate fallback if the video element is missing
            fallbackTimeout = setTimeout(dismissPreloader, 1000);
        }
    }

    /**
     * AUTO-SPAN INJECTOR FOR TEXT REVEAL & ACCESSIBILITY
     * Splits inner text into wrapped characters for CSS staggered animations 
     * while preserving clean a11y output for screen readers.
     */
    const revealTextElement = document.getElementById('reveal-text');
    if (revealTextElement) {
        const textContent = revealTextElement.innerText.trim();

        // A11y Constraint: Ensure screen readers read the full sentence normally
        revealTextElement.setAttribute('aria-label', textContent);
        revealTextElement.innerHTML = ''; // Clear original text

        // Split specifically by character for the smooth left-to-right waterfall
        const characters = textContent.split('');

        let charIndex = 1;
        characters.forEach((char) => {
            if (char === ' ') {
                // Keep spaces as distinct nodes to allow the flex wrapper to wrap distinct words
                // Using non-breaking space \u00A0 so flexbox doesn't collapse it
                revealTextElement.appendChild(document.createTextNode('\u00A0'));
            } else {
                const span = document.createElement('span');
                span.innerText = char;
                // A11y Constraint: Hide individual characters from screen readers 
                span.setAttribute('aria-hidden', 'true');
                span.style.setProperty('--i', charIndex); // CSS var for staggered delay

                charIndex++;
                revealTextElement.appendChild(span);
            }
        });
    }

    /**
     * ==========================================
     *  ENVIRONMENT-AGNOSTIC ACTIVE ROUTING
     * ==========================================
     */
    const identifyActiveRoute = () => {
        const currentUrl = window.location.href;
        const navLinks = document.querySelectorAll('.nav-links a');
        let matched = false;

        navLinks.forEach(link => {
            // Extract the target hash from the href (e.g., "#about")
            const hrefAttr = link.getAttribute('href');
            const targetHash = hrefAttr.substring(hrefAttr.indexOf('#'));
            
            // The .includes() Shield: Mathematically verify if the URL contains the target hash
            // (Only apply if targetHash is an actual section link, not the top logo jump)
            if (targetHash && targetHash !== '#top' && currentUrl.includes(targetHash)) {
                link.classList.add('active-link');
                matched = true;
            } else {
                link.classList.remove('active-link');
            }
        });

        // Ultimate Fallback: If URL has no specific hash, 
        // mark the 'YASHWANT' logo (or just remove all active states from standard links)
        const homeLogo = document.getElementById('nav-logo-ys');
        if (!matched && (currentUrl.endsWith('/') || currentUrl.endsWith('index.html') || currentUrl.includes('#top'))) {
            if (homeLogo) {
                // We keep the logo clean, so we just ensure no other link is active.
                // You could add an active class to the logo here if desired.
            }
        }
    };

    // Run on load
    identifyActiveRoute();
    
    // Run exactly when the hash changes in the URL
    window.addEventListener('hashchange', identifyActiveRoute);

    /**
     * ==========================================
     *  HUD MOBILE NAVIGATION TOGGLE
     * ==========================================
     */
    const mobileMenuBtn = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', () => {
            const isExpanded = mobileMenuBtn.getAttribute('aria-expanded') === 'true';
            
            // Toggle Accessibility Attribute
            mobileMenuBtn.setAttribute('aria-expanded', !isExpanded);
            
            // Toggle CSS Class for the sliding panel transition
            navLinks.classList.toggle('nav-open');
        });

        // Close the menu automatically if a navigation link is clicked
        const links = navLinks.querySelectorAll('a');
        links.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenuBtn.setAttribute('aria-expanded', 'false');
                navLinks.classList.remove('nav-open');
            });
        });
    }


    /**
     * ==========================================
     *  GLOBAL FOOTER AUTOMATION
     * ==========================================
     */

    // 1. Dynamic Copyright Year
    // Avoids hardcoding the year so it updates automatically
    const yearElement = document.getElementById('current-year');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }

    // 2. Smooth "Back to Top" Scroll (Global Button)
    // Uses native window.scrollTo for optimized rendering
    const backToTopBtn = document.getElementById('back-to-top');
    if (backToTopBtn) {
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // 3. Navigation Logo "Back to Top" functionality & Focus Reset
    const navLogo = document.getElementById('nav-logo-ys');
    if (navLogo) {
        navLogo.addEventListener('click', (e) => {
            // Prevent immediate instant jump to top anchor
            e.preventDefault();

            // Smoothly scroll to the top
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });

            // Focus Reset (Crucial a11y)
            // Reset keyboard focus to the very top container of the webpage
            const topAnchor = document.getElementById('top');
            if (topAnchor) {
                topAnchor.focus();
            }
        });
    }

});
