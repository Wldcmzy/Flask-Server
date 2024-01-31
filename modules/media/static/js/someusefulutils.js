function scrollPage(factor) {
    // Scroll the page by a certain percentage of the total page height
    var totalHeight = Math.max(
        document.body.scrollHeight,
        document.documentElement.scrollHeight,
        document.body.offsetHeight,
        document.documentElement.offsetHeight,
        document.body.clientHeight,
        document.documentElement.clientHeight
    );

    window.scrollTo({
        top: window.scrollY + totalHeight * factor,
        behavior: 'smooth'
    });
}