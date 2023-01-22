// бургер меню
const iconMenu = document.querySelector('.menu__burger');
const menuBody = document.querySelector('.header__body');
const menuItem = document.querySelectorAll('.header__link');

if(iconMenu){
    iconMenu.addEventListener("click", function(e){
        document.body.classList.toggle('lock');
        iconMenu.classList.toggle('active');
        menuBody.classList.toggle('active');
    });
    menuItem.forEach(item => {
        item.addEventListener("click", event => {
            document.body.classList.remove('lock');
            iconMenu.classList.remove('active');
            menuBody.classList.remove('active');
        })
    })
}


// карусель

var swiper = new Swiper(".swiper", {
    loop: true,
    slidesPerView: 1,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
        renderBullet: function () {
            return `<span class="swiper-pagination-bullet"></span>`;
        },
    },
    autoplay: {
        delay: 5000,
    },
    speed: 600,
});

