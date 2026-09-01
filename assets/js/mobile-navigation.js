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
