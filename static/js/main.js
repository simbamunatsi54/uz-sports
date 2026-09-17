document.addEventListener("DOMContentLoaded", function () {

    /* =====================================================
       MOBILE SIDEBAR
       ===================================================== */

    const mobileMenu = document.getElementById("mobileMenu");
    const sidebar = document.getElementById("sidebar");

    if (mobileMenu && sidebar) {

        mobileMenu.addEventListener("click", function () {

            sidebar.classList.toggle("open");

        });

    }


    /* =====================================================
       CLOSE MOBILE SIDEBAR WHEN LINK IS CLICKED
       ===================================================== */

    if (sidebar) {

        const sidebarLinks =
            sidebar.querySelectorAll("a");

        sidebarLinks.forEach(function (link) {

            link.addEventListener("click", function () {

                if (window.innerWidth <= 700) {

                    sidebar.classList.remove("open");

                }

            });

        });

    }


    /* =====================================================
       HERO SLIDER
       ===================================================== */

    const heroPanel =
        document.querySelector(".hero-panel");

    const heroDots =
        document.querySelectorAll(".hero-dots span");

    const heroLeft =
        document.querySelector(".hero-arrow-left");

    const heroRight =
        document.querySelector(".hero-arrow-right");


    let currentSlide = 0;


    function updateHeroDots() {

        heroDots.forEach(function (dot, index) {

            dot.classList.toggle(
                "active",
                index === currentSlide
            );

        });

    }


    function nextSlide() {

        if (heroDots.length === 0) {
            return;
        }

        currentSlide++;

        if (currentSlide >= heroDots.length) {
            currentSlide = 0;
        }

        updateHeroDots();

    }


    function previousSlide() {

        if (heroDots.length === 0) {
            return;
        }

        currentSlide--;

        if (currentSlide < 0) {
            currentSlide = heroDots.length - 1;
        }

        updateHeroDots();

    }


    if (heroRight) {

        heroRight.addEventListener(
            "click",
            nextSlide
        );

    }


    if (heroLeft) {

        heroLeft.addEventListener(
            "click",
            previousSlide
        );

    }


    heroDots.forEach(function (dot, index) {

        dot.addEventListener(
            "click",
            function () {

                currentSlide = index;

                updateHeroDots();

            }
        );

    });


    /* =====================================================
       ESCAPE KEY
       ===================================================== */

    document.addEventListener(
        "keydown",
        function (event) {

            if (event.key === "Escape") {

                if (sidebar) {
                    sidebar.classList.remove("open");
                }

            }

        }
    );


    /* =====================================================
       WINDOW RESIZE
       ===================================================== */

    window.addEventListener(
        "resize",
        function () {

            if (
                window.innerWidth > 700 &&
                sidebar
            ) {

                sidebar.classList.remove("open");

            }

        }
    );

});