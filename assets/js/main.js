document.addEventListener("DOMContentLoaded", function () {
  var header = document.querySelector(".site-header");
  var navToggle = document.querySelector(".nav-toggle");

  if (header) {
    var headerTop = header.getBoundingClientRect().top + window.scrollY;
    var updateStickyHeader = function () {
      header.classList.toggle("is-scrolled", window.scrollY > headerTop);
    };
    window.addEventListener("scroll", updateStickyHeader, { passive: true });
    updateStickyHeader();
  }

  if (navToggle && header) {
    navToggle.addEventListener("click", function () {
      header.classList.toggle("open");
    });
  }

  // On mobile, tapping a dropdown parent link opens the submenu instead of navigating
  document.querySelectorAll(".has-dropdown > a").forEach(function (link) {
    link.addEventListener("click", function (e) {
      if (window.innerWidth <= 720) {
        var parent = link.parentElement;
        var alreadyOpen = parent.classList.contains("dd-open");
        if (!alreadyOpen) {
          e.preventDefault();
          document.querySelectorAll(".has-dropdown").forEach(function (li) { li.classList.remove("dd-open"); });
          parent.classList.add("dd-open");
        }
      }
    });
  });

  // Highlight the current page in the nav
  var here = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a, .dropdown a").forEach(function (a) {
    var href = a.getAttribute("href");
    if (href === here) a.classList.add("active");
  });

  // FAQ accordion
  document.querySelectorAll(".faq-q").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var item = btn.closest(".faq-item");
      var isOpen = item.classList.contains("open");
      item.parentElement.querySelectorAll(".faq-item").forEach(function (i) { i.classList.remove("open"); });
      if (!isOpen) item.classList.add("open");
    });
  });

  // Back to top button
  var backToTop = document.querySelector(".back-to-top");
  if (backToTop) {
    window.addEventListener("scroll", function () {
      if (window.scrollY > 500) backToTop.classList.add("show");
      else backToTop.classList.remove("show");
    });
    backToTop.addEventListener("click", function () {
      window.scrollTo(0, 0);
    });
  }

  // Footer year
  document.querySelectorAll(".js-year").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // Basic contact form handling (no backend — opens a pre-filled mail client)
  var form = document.querySelector("#contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var name = form.querySelector("#name").value.trim();
      var email = form.querySelector("#email").value.trim();
      var phone = form.querySelector("#phone").value.trim();
      var topic = form.querySelector("#topic").value;
      var message = form.querySelector("#message").value.trim();

      var subject = encodeURIComponent("Website enquiry: " + (topic || "General"));
      var body = encodeURIComponent(
        "Name: " + name + "\nEmail: " + email + "\nPhone: " + phone + "\nTopic: " + topic + "\n\n" + message
      );
      window.location.href = "mailto:Info@constructionhelps.com?subject=" + subject + "&body=" + body;
    });
  }
});
