(function () {
  function enableFolderTitleToggle() {
    document.querySelectorAll(".md-nav__item--nested").forEach(function (item) {
      var toggle = item.querySelector(":scope > .md-nav__toggle");
      var link = item.querySelector(":scope > .md-nav__link");

      if (!toggle || !link || link.dataset.folderToggleReady === "true") {
        return;
      }

      link.dataset.folderToggleReady = "true";
      link.style.cursor = "pointer";

      link.addEventListener("click", function (event) {
        event.preventDefault();
        toggle.checked = !toggle.checked;
        toggle.dispatchEvent(new Event("change", { bubbles: true }));
      });
    });
  }

  document.addEventListener("DOMContentLoaded", enableFolderTitleToggle);

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(enableFolderTitleToggle);
  }
})();
