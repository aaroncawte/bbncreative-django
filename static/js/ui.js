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
    $('.window-first').css("min-height", stringifyPixel(firstWindowHeight));

    let heroWindowHeight = Math.max(windowHeight - offset, absoluteMinimum);
    $('.window-hero').css("min-height", stringifyPixel(heroWindowHeight));

});