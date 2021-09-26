const backToTop = document.getElementById('backtotop');

function checkScroll() {

}

function moveBackToTop() {
    let pageYOffset = window.pageYOffset;
    
    if (pageYOffset !== 0) {
        backToTop.classList.add('show')
    } else {
        backToTop.classList.remove('show')
    }
}

window.addEventListener('scroll', checkScroll);
backToTop.addEventListener('click', moveBackToTop);
