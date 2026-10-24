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

  var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  var wheelTarget = window.scrollY;
  var wheelFrame = null;

  function hasScrollableParent(target, deltaY) {
    var element = target.nodeType === 1 ? target : target.parentElement;

    while (element && element !== document.body) {
      var style = window.getComputedStyle(element);
      var canScrollVertically = /(auto|scroll|overlay)/.test(style.overflowY) &&
        element.scrollHeight > element.clientHeight;

      if (canScrollVertically) {
        var canScrollDown = element.scrollTop + element.clientHeight < element.scrollHeight;
        var canScrollUp = element.scrollTop > 0;
        if ((deltaY > 0 && canScrollDown) || (deltaY < 0 && canScrollUp)) return true;
      }
      element = element.parentElement;
    }
    return false;
  }

  function smoothWheelScroll(event) {
    var target = event.target.nodeType === 1 ? event.target : event.target.parentElement;
    if (reducedMotion.matches || event.ctrlKey || event.deltaY === 0 ||
        (target && target.closest("input, textarea, select, [contenteditable='true']")) ||
        hasScrollableParent(target, event.deltaY)) return;

    var delta = event.deltaY;
    if (event.deltaMode === 1) delta *= 16;
    else if (event.deltaMode === 2) delta *= window.innerHeight;
    delta *= 1.6;

    var doc = document.documentElement;
    var maxScroll = Math.max(doc.scrollHeight, document.body.scrollHeight) - window.innerHeight;
    var currentTarget = wheelFrame === null ? window.scrollY : wheelTarget;
    var nextTarget = Math.max(0, Math.min(maxScroll, currentTarget + delta));
    if (nextTarget === currentTarget) return;

    event.preventDefault();
    wheelTarget = nextTarget;

    if (wheelFrame === null) {
      function animateWheelScroll() {
        var distance = wheelTarget - window.scrollY;
        if (Math.abs(distance) < 1.5) {
          window.scrollTo({ top: wheelTarget, behavior: "instant" });
          wheelFrame = null;
          return;
        }

        window.scrollTo({ top: window.scrollY + distance * 0.45, behavior: "instant" });
        wheelFrame = window.requestAnimationFrame(animateWheelScroll);
      }
      wheelFrame = window.requestAnimationFrame(animateWheelScroll);
    }
  }

  document.addEventListener("wheel", smoothWheelScroll, { passive: false });

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
      var behavior = window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth";
      window.scrollTo({ top: 0, behavior: behavior });
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
