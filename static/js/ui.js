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
function sizeHeroWindow() {
    const firstWindowHeight = 400;
    const offset = 100 + 80;
    let windowHeight = window.innerHeight;

    $(".window-first").css("min-height", stringifyPixel(firstWindowHeight));

    let heroWindowHeight = Math.max(windowHeight - offset, firstWindowHeight);
    $(".window-hero").css("min-height", stringifyPixel(heroWindowHeight));
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
        $heroImage.css("height", "calc(100% - 70px)");
    } else {
        $heroImage.css("width", "100%");
        $heroImage.css("height", "100%");
    }
}

/* UI Functions for window resize
   ======================================================================== */
$(window).on('resize', function () {
    sizeHeroWindow();
    sizeHeroImage();

});

$(function () {

    /* UI Functions on page load
   ======================================================================== */
    sizeHeroWindow();
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
});