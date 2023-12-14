document.addEventListener("DOMContentLoaded", function () {
  // var swiper1 = new Swiper(".mySwiper", {
  //   pagination: {
  //     el: ".swiper-pagination",
  //     dynamicBullets: true,
  //   },
  // });

  var swiper = new Swiper(".mySwiper", {
    spaceBetween: 10,
    slidesPerView: 0,
    freeMode: true,
    watchSlidesProgress: true,
  });
  var swiper2 = new Swiper(".mySwiper2", {
    spaceBetween: 10,
    slidesPerView: 1,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    thumbs: {
      swiper: swiper,
    },
  });
});
