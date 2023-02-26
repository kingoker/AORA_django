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


// Плавная прокрутка якорных ссылок
// выбираем все якорные ссылки на странице
const anchors = document.querySelectorAll('a[href*="#"]');

// добавляем обработчик событий на каждую якорную ссылку
for (let anchor of anchors) {
  anchor.addEventListener('click', function (e) {
    e.preventDefault(); // отменяем стандартное поведение браузера при клике на ссылку
    const blockID = anchor.getAttribute('href').substr(1); // получаем id элемента, на который ссылается якорная ссылка
    const block = document.getElementById(blockID); // получаем целевой элемент
    const offset = 95; // задаем отступ для остановки прокрутки
    const top = block.getBoundingClientRect().top + window.pageYOffset - offset; // вычисляем позицию целевого элемента с учетом отступа
    window.scrollTo({
      top: top,
      behavior: 'smooth'
    }); // прокручиваем страницу к целевому элементу с учетом отступа
  });
}


