const mobileBtn = document.getElementById('menu-btn')
    nav = document.querySelector('nav')
    exitBtn = document.getElementById('exit-btn');

mobileBtn.addEventListener('click', () => {
    nav.classList.add('nav-mobile');
});

exitBtn.addEventListener('click', () => {
    nav.classList.remove('nav-mobile');
});