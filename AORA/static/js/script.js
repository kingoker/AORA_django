// Свайпер на главной странице
if (document.querySelector('.swiper')){
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
}


// бургер меню
var iconMenu = document.querySelector('.menu__burger');
var menuBody = document.querySelector('.header__body');
var menuItem = document.querySelectorAll('.header__link');

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


// Прогресс бар на странице Инновации
if (document.getElementsByClassName("innovation__block_line")){
    var pogress = document.getElementsByClassName("innovation__block_line");
    let scrollHeight = document.body.scrollHeight;
    let innerHeight = window.innerHeight;
    var totalHeight = scrollHeight-innerHeight;
    window.onscroll = function(){
        var progressHeight = window.pageYOffset / totalHeight) * 100;
        pogress[0].style.height = progressHeight + "%";
    }
}

