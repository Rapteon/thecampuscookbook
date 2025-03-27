$(document).ready(() => {
  const menuToggle = document.getElementById("menu-toggle");
  const mobileMenu = document.getElementById("mobile-menu");

  $('#menu-toggle').click(() => {
    mobileMenu.classList.toggle("active");
  }
  );

  $('.mobile-nav-item').each((index, item) => {
    $(item).click(function() {
      $(mobileMenu).removeClass("active");
    });
  });

  $(document).click((event) => {
    if (!mobileMenu.contains(event.target) && !menuToggle.contains(event.target)) {
      mobileMenu.classList.remove("active");
    }
  });
})