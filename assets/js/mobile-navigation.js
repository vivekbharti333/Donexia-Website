document.addEventListener("DOMContentLoaded", () => {
  const mobileBreakpoint = window.matchMedia("(max-width: 991.98px)");

  document.querySelectorAll(".navbar").forEach((navbar) => {
    const menu = navbar.querySelector(".navbar-collapse");
    if (!menu) return;

    const closeMenu = () => {
      if (!mobileBreakpoint.matches || !menu.classList.contains("show")) return;

      bootstrap.Collapse.getOrCreateInstance(menu, { toggle: false }).hide();
    };

    document.addEventListener("pointerdown", (event) => {
      if (!navbar.contains(event.target)) closeMenu();
    });

    menu.addEventListener("click", (event) => {
      const link = event.target.closest("a");
      if (!link || link.classList.contains("dropdown-toggle")) return;
      closeMenu();
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") closeMenu();
    });
  });
});

// Sticky header shadow: add .is-stuck once the page is scrolled
document.addEventListener("DOMContentLoaded", () => {
  const header = document.querySelector(".site-header");
  if (!header) return;

  const updateHeaderState = () => {
    header.classList.toggle("is-stuck", window.scrollY > 8);
  };

  updateHeaderState();
  window.addEventListener("scroll", updateHeaderState, { passive: true });
});

// Announcement bar: remember dismissal across pages
document.addEventListener("DOMContentLoaded", () => {
  const bar = document.querySelector(".announcement-bar");
  if (!bar) return;

  try {
    if (localStorage.getItem("donexia_announcement_closed") === "1") {
      bar.classList.add("is-hidden");
      return;
    }
  } catch (e) { /* private mode etc. */ }

  const closeBtn = bar.querySelector(".announcement-close");
  if (!closeBtn) return;

  closeBtn.addEventListener("click", () => {
    bar.classList.add("is-hidden");
    try {
      localStorage.setItem("donexia_announcement_closed", "1");
    } catch (e) { /* ignore */ }
  });
});

// Announcement bar: page-specific messages that reinforce the feature each page sells
document.addEventListener("DOMContentLoaded", () => {
  const bar = document.querySelector(".announcement-bar");
  if (!bar) return;

  const prefix = location.pathname.indexOf("/guides/") !== -1 ? "../" : "";
  const page = location.pathname.split("/").pop() || "index.html";

  const messages = {
    "index.html": {
      text: "New: Free plan — start with no credit card.",
      link: "See what's included",
      href: prefix + "pricing.html#free-plan"
    },
    "80g-donation-receipt-software.html": {
      text: "Send 80G receipts automatically on WhatsApp, SMS & email.",
      link: "Start free",
      href: prefix + "signup.html"
    },
    "form-10bd-software.html": {
      text: "Keep Form 10BD records organized all year — not rebuilt in May.",
      link: "Start free",
      href: prefix + "signup.html"
    },
    "ngo-donor-management-software.html": {
      text: "Every donor, every gift, one searchable register.",
      link: "Start free",
      href: prefix + "signup.html"
    },
    "whatsapp-donation-receipts.html": {
      text: "WhatsApp donation receipts the moment money arrives.",
      link: "Start free",
      href: prefix + "signup.html"
    },
    "campaign.html": {
      text: "Track campaign goals, donations and receipts in real time.",
      link: "Start free",
      href: prefix + "signup.html"
    },
    "pricing.html": {
      text: "Start free — upgrade only when your NGO outgrows it.",
      link: "See the Free plan",
      href: "pricing.html#free-plan"
    },
    "contact.html": {
      text: "Book a free demo — our team replies within one working day.",
      link: "Book now",
      href: "contact.html#contact-form"
    },
    "signup.html": null
  };

  let msg = messages[page];
  if (page === "index.html" && location.pathname.indexOf("/guides/") !== -1) {
    msg = {
      text: "Put these guides to work — start free, no credit card.",
      link: "Start free",
      href: "../signup.html"
    };
  } else if (location.pathname.indexOf("/guides/") !== -1) {
    msg = {
      text: "Put these guides to work — start free, no credit card.",
      link: "Start free",
      href: "../signup.html"
    };
  }

  // Signup page: the hero already makes the offer — hide the bar there
  if (msg === null) {
    bar.classList.add("is-hidden");
    return;
  }

  // Unknown pages keep the static default message baked into the HTML
  if (!msg) return;

  const span = bar.querySelector("span");
  if (!span) return;

  const anchor = document.createElement("a");
  anchor.href = msg.href;
  anchor.textContent = msg.link;

  span.textContent = msg.text + " ";
  span.appendChild(anchor);
});

// ============================================================
// Pricing page — selectable plan cards (radio behaviour)
// ============================================================
(function () {
  var cards = document.querySelectorAll(".plans-container .plan-card");
  if (!cards.length) return;

  function select(card) {
    cards.forEach(function (c) {
      c.classList.remove("is-selected");
      c.setAttribute("aria-pressed", "false");
    });
    card.classList.add("is-selected");
    card.setAttribute("aria-pressed", "true");
  }

  cards.forEach(function (card) {
    card.setAttribute("tabindex", "0");
    card.setAttribute("role", "button");
    card.setAttribute("aria-pressed", card.classList.contains("is-selected") ? "true" : "false");

    card.addEventListener("click", function (e) {
      if (e.target.closest("a")) return;
      select(card);
    });

    card.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        select(card);
      }
    });
  });
})();

// ============================================================
// Pricing page — Monthly / Yearly billing toggle
// ============================================================
(function () {
  var toggle = document.querySelector(".billing-toggle");
  if (!toggle) return;

  var options = toggle.querySelectorAll(".billing-option");
  var note = document.getElementById("billing-note");

  var notes = {
    monthly: "Billed monthly. Free and Enterprise plans stay the same.",
    yearly: "Billed annually — 2 months free. Free and Enterprise plans stay the same."
  };

  function setBilling(mode) {
    options.forEach(function (opt) {
      var active = opt.getAttribute("data-billing") === mode;
      opt.classList.toggle("is-active", active);
      opt.setAttribute("aria-pressed", active ? "true" : "false");
    });

    document.querySelectorAll(".price-amount").forEach(function (el) {
      var value = el.getAttribute("data-" + mode);
      if (value) el.textContent = value;
    });

    document.querySelectorAll(".price-period").forEach(function (el) {
      var value = el.getAttribute("data-" + mode);
      if (value) el.textContent = value;
    });

    if (note && notes[mode]) note.textContent = notes[mode];
  }

  options.forEach(function (opt) {
    opt.addEventListener("click", function () {
      setBilling(opt.getAttribute("data-billing"));
    });
  });
})();
