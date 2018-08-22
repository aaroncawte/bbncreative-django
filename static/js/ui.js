/* bbncreative UI Variables
   ======================================================================== */
const wideBreakpoint = 1280;
const mobileBreakpoint = 690;


/* Operational Functions
   ======================================================================== */
function stringifyPixel(val) {
    return val.toString() + "px";
}


/* Automatic first/hero window height
   ======================================================================== */
const firstWindowHeight = 400;
const heroPeekOffset = 100 + 80;

function heroWindowHeight() {
    let windowHeight = window.innerHeight;
    return Math.max(windowHeight - heroPeekOffset, firstWindowHeight);
}

function sizeFirstWindows() {
    $(".window-hero").css("min-height", stringifyPixel(heroWindowHeight()));
}


/* Automatic first/hero window colour box dimensions
   ======================================================================== */
function sizeHeroImage() {
    const $heroImage = $(".first-hero-image");

    let windowWidth = document.body.clientWidth; // Excluding scroll bar
    let logoSpace = 240;
    let wrapper = windowWidth;

    if (windowWidth >= wideBreakpoint)
        wrapper = 1240;

    if (windowWidth >= mobileBreakpoint) {
        let boxWidth = (windowWidth - wrapper) / 2 + (wrapper - logoSpace);
        $heroImage.css("width", stringifyPixel(boxWidth));
    } else {
        $heroImage.css("width", "100%");
    }
}

/* UI Functions for window resize
   ======================================================================== */
$(window).on('resize', function () {
    sizeFirstWindows();
    sizeHeroImage();

});

$(function () {

    const $windowHero = $(".window-hero");
    const $backToButton = $("#backTo");
    const $heroScrollTrigger = $("#heroScrollTrigger");

    /* UI Functions on page load
   ======================================================================== */
    sizeFirstWindows();
    sizeHeroImage();


    /* Menu Display Mechanics
   ======================================================================== */
    const $menuGlobal = $("#menuGlobal");
    const $menuProjects = $("#menuProjects");
    const $menuFeeds = $("#menuFeeds");
    const $allMenus = $("#menuGlobal, #menuProjects, #menuFeeds");

    const $closeMenuButton = $('.menu-close');

    const $mbGlobal = $("#menuGlobalButton");
    const $mbProjects = $("#menuProjectsButton");
    const $mbFeeds = $("#menuFeedsButton");
    const $allButtons = $("#menuGlobalButton, #menuProjectsButton, #menuFeedsButton");

    const $mbProjectsGroup = $("#menuProjectsButton, #inMenuProjectsButton");
    const $mbFeedsGroup = $("#menuFeedsButton, #inMenuFeedsButton");

    function showOrHide(menu, menuButton) {
        if (menu.hasClass("menu-hidden")) {
            $allMenus.addClass("menu-hidden");
            $allButtons.removeClass("active-button");
            menu.removeClass("menu-hidden");
            menuButton.addClass("active-button");
        } else {
            menu.addClass("menu-hidden");
            menuButton.removeClass("active-button");
        }
    }

    $mbGlobal.on("click", function () {
        showOrHide($menuGlobal, $mbGlobal);
    });
    $mbProjectsGroup.on("click", function () {
        showOrHide($menuProjects, $mbProjects);
    });
    $mbFeedsGroup.on("click", function () {
        showOrHide($menuFeeds, $mbFeeds);
    });

    $closeMenuButton.on('click', function () {
        $allMenus.addClass("menu-hidden");
        $allButtons.removeClass("active-button");
    });

    $('.window').on('click', function () {
        $allMenus.addClass("menu-hidden");
        $allButtons.removeClass("active-button");
    });

    /* Scroll Down Button
   ======================================================================== */
    $heroScrollTrigger.on('click', function () {
        $("html, body").animate({
            scrollTop: stringifyPixel(heroWindowHeight())
        }, 200);
    });

    /* Auto-hide elements on scroll
    ======================================================================= */
    function scrollMultiplier(hideValue) {
        let scroll = $(window).scrollTop();
        return Math.max(0, (hideValue - scroll) / hideValue);
    }

    $(window).scroll(function () {

        // Scroll down hint
        if ($windowHero.length) {
            let heroHeight = $windowHero.height();
            let multiplier = scrollMultiplier(heroHeight);
            $heroScrollTrigger.css({'opacity': multiplier});
        }

        // Back-to buttons
        if ($backToButton.length) {
            const hideValue = 60;
            let multiplier = scrollMultiplier(hideValue);
            $backToButton.css({'opacity': multiplier});
        }
    });

    /* Even/Odd Assets
   ======================================================================== */
    $('.window[data-side-panel]').filter(":odd").children(".wrapper-1200").children(".panel-right").addClass("panel-left").removeClass("panel-right");
});