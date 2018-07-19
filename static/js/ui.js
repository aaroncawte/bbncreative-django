function stringifyPixel(val) {
    return val.toString() + "px";
}

$(function () {

    /* Automatic first/hero window height
   ======================================================================== */
    const absoluteMinimum = 250;
    const offset = 100 + 80;
    let windowHeight = window.innerHeight;

    let firstWindowHeight = absoluteMinimum;
    $(".window-first").css("min-height", stringifyPixel(firstWindowHeight));

    let heroWindowHeight = Math.max(windowHeight - offset, absoluteMinimum);
    $(".window-hero").css("min-height", stringifyPixel(heroWindowHeight));

    /* Menu Display Mechanics
   ======================================================================== */
    const $menuGlobal = $("#menuGlobal");
    const $menuProjects = $("#menuProjects");
    const $menuFeeds = $("#menuFeeds");
    const $allMenus = $("#menuGlobal, #menuProjects, #menuFeeds");

    const $closeMenuButton = $('.menu-close');

    const $mbGlobal = $("#menuGlobalButton");
    const $mbProjects = $("#menuProjectsButton, #inMenuProjectsButton");
    const $mbFeeds = $("#menuFeedsButton, #inMenuFeedsButton");

    function showOrHide(menu) {
        if (menu.hasClass("menu-hidden")) {
            $allMenus.addClass("menu-hidden");
            menu.removeClass("menu-hidden");
        } else {
            menu.addClass("menu-hidden");
        }
    }

    $mbGlobal.on("click", function () {
        showOrHide($menuGlobal);
    });
    $mbProjects.on("click", function () {
        showOrHide($menuProjects);
    });
    $mbFeeds.on("click", function () {
        showOrHide($menuFeeds);
    });

    $closeMenuButton.on('click', function () {
        $allMenus.addClass("menu-hidden");
    });

    $('.window').on('click', function () {
        $allMenus.addClass("menu-hidden");
    });
});