function stringifyPixel(val) {
    return val.toString() + "px";
}

$(function () {

    /* Automatic first/hero window height
   ======================================================================== */
    const absoluteMinimum = 400;
    const offset = 100 + 80;
    let windowHeight = window.innerHeight;

    let firstWindowHeight = absoluteMinimum;
    $(".window-first").css("min-height", stringifyPixel(firstWindowHeight));

    let heroWindowHeight = Math.max(windowHeight - offset, absoluteMinimum);
    $(".window-hero").css("min-height", stringifyPixel(heroWindowHeight));

    /* Automatic first/hero window colour box dimensions
   ======================================================================== */
    const $heroImage = $(".first-hero-image");

    let windowWidth = window.innerWidth;
    let limit = 1280;
    let wrapper = 1200;
    let logoSpace = 240;

    if (windowWidth > limit) {
        let boxWidth = (windowWidth - wrapper) / 2 + (wrapper - logoSpace);
        $heroImage.css("width", stringifyPixel(boxWidth));
    } else {
        $heroImage.css("width", "100%");
    }

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
    });
});