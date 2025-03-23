document.addEventListener("DOMContentLoaded", function () {
  const menuToggle = document.getElementById("menu-toggle");
  const mobileMenu = document.getElementById("mobile-menu");

  // Toggle the menu when clicking the menu button
  menuToggle.addEventListener("click", function () {
    mobileMenu.classList.toggle("active");
  });

  // Close menu when clicking a nav link
  document.querySelectorAll(".mobile-nav-item").forEach(link => {
    link.addEventListener("click", function () {
      mobileMenu.classList.remove("active");
    });
  });

  // Close the menu when clicking outside
  document.addEventListener("click", function (event) {
    if (!mobileMenu.contains(event.target) && !menuToggle.contains(event.target)) {
      mobileMenu.classList.remove("active");
    }
  });
});
