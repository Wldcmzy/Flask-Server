
function search() {
    var searchTerm = document.getElementById('search-input').value.toLowerCase();
    var boxes = document.querySelectorAll('.box');

    boxes.forEach(function(box) {
        var boxText = box.querySelector('p').innerText.toLowerCase();
        if (boxText.includes(searchTerm)) {
            box.style.display = 'flex';
        } else {
            box.style.display = 'none';
        }
    });
}

function scrollPage(percentage) {
    var currentScrollPosition = window.scrollY || document.documentElement.scrollTop;
    var windowHeight = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
    var totalHeight = document.body.scrollHeight - windowHeight;
    var targetScrollPosition = currentScrollPosition + percentage * totalHeight;
    window.scrollTo({
        top: targetScrollPosition,
        behavior: 'smooth'
    });
}
