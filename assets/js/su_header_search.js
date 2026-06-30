// search-form-handler.js

document.addEventListener("DOMContentLoaded", function () {
  const { applyDefaultSearchInputLabel } = window.SuSearchA11y;

  const buttonLabels = {
    en:     { form: "Site search", search: "Search", clear: "Clear search" },
    "pt-br":{ form: "Pesquisa do site", search: "Pesquisar", clear: "Limpar pesquisa" },
    ko:     { form: "사이트 검색", search: "검색", clear: "검색 지우기" },
    fr:     { form: "Recherche sur le site", search: "Rechercher", clear: "Effacer la recherche" },
    es:     { form: "Búsqueda en el sitio", search: "Buscar", clear: "Borrar búsqueda" },
    de:     { form: "Sitesuche", search: "Suchen", clear: "Suche löschen" },
    ja:     { form: "サイト検索", search: "検索", clear: "検索をクリア" },
  };

  /**
   * Bind submit + click listeners to search form and apply ARIA labels.
   * @param {HTMLFormElement} form
   */
  function bindSearchForm(form) {
    if (form && !form.dataset.listenerAdded) {
      const originalAction = form.getAttribute("action") || "";
      const lang = document.documentElement.lang;
      const labels = buttonLabels[lang] || buttonLabels.en;

      form.setAttribute("aria-label", labels.form);

      // Handle form submit
      form.addEventListener(
        "submit",
        function (e) {
          e.preventDefault();
          e.stopImmediatePropagation();
          handleSearch();
          return false;
        },
        true
      );

      // Handle search button click
      const searchButton = form.querySelector(".su__search_btn");
      if (searchButton) {
        searchButton.setAttribute("type", "submit");
        searchButton.setAttribute("aria-label", labels.search);
        searchButton.addEventListener(
          "click",
          function (e) {
            e.preventDefault();
            e.stopImmediatePropagation();
            handleSearch();
            return false;
          },
          true
        );
      }

      // Handle clear (×) button
      const clearButton = form.querySelector(".su__input-close");
      if (clearButton) {
        clearButton.setAttribute("aria-label", labels.clear);
        clearButton.setAttribute("role", "button");
        clearButton.setAttribute("tabindex", "0");
        clearButton.addEventListener("keydown", function (e) {
          if (e.key === "Enter" || e.key === " ") {
            e.preventDefault();
            clearButton.click();
          }
        });
        clearButton.addEventListener("click", function (e) {
          e.preventDefault();
          e.stopImmediatePropagation();
          const input = form.querySelector("#search-box-autocomplete");
          if (input) {
            input.value = "";
            input.classList.remove("has-text");
            input.focus();
          }
        });
      }

      form.dataset.listenerAdded = "true";
      form.setAttribute("data-original-action", originalAction);
    }
  }

  /**
   * Handle search action
   */
  function handleSearch() {
    const queryInput = document.getElementById("search-box-autocomplete");
    const langSelect = document.getElementById("lang_select");
    const lang = langSelect ? langSelect.value : "en";

    if (queryInput && queryInput.value.trim() !== "") {
      const query = queryInput.value.trim();
      const targetUrl = `/docs/${lang}/search?searchString=${encodeURIComponent(
        query
      )}`;
      window.location.href = targetUrl;
    } else {
      console.warn("Search input not found or empty.");
      if (queryInput) queryInput.focus();
    }
  }

  /**
   * Set up placeholder, ARIA combobox attributes, key events & has-text logic.
   */
  function setupInputWatcher() {
    const input = document.getElementById("search-box-autocomplete");
    if (!input || input.dataset.a11yLabelApplied) return;

    applyDefaultSearchInputLabel(input);
    input.dataset.a11yLabelApplied = "true";

    // Combobox ARIA — tells assistive technology this input controls a listbox
    input.setAttribute("role", "combobox");
    input.setAttribute("aria-haspopup", "listbox");
    input.setAttribute("aria-expanded", "false");
    input.setAttribute("autocomplete", "off");

    input.addEventListener("focus", () =>
      input.setAttribute("aria-expanded", "true")
    );
    input.addEventListener("blur", () => {
      // Delay so a click on a suggestion isn't cut off before it fires
      setTimeout(() => input.setAttribute("aria-expanded", "false"), 200);
    });
    input.addEventListener("input", () => {
      input.setAttribute(
        "aria-expanded",
        input.value.trim() !== "" ? "true" : "false"
      );
    });

    // --- Function to toggle has-text class ---
    function toggleHasTextClass() {
      if (input.value && input.value.trim() !== "") {
        input.classList.add("has-text");
      } else {
        input.classList.remove("has-text");
      }
    }

    // --- Watch for typing or pasting ---
    input.addEventListener("input", toggleHasTextClass);
    input.addEventListener("blur", toggleHasTextClass);
    input.addEventListener("focus", toggleHasTextClass);

    // --- Handle Enter key manually ---
    input.addEventListener(
      "keypress",
      function (e) {
        if (e.key === "Enter") {
          e.preventDefault();
          e.stopImmediatePropagation();
          handleSearch();
          return false;
        }
      },
      true
    );

    // --- Run check immediately and periodically for autofill/preload ---
    const checkDelays = [0, 100, 300, 1000, 2000];
    checkDelays.forEach((delay) => setTimeout(toggleHasTextClass, delay));
  }

  /**
   * Remove source/type label badges from the tab order — they are metadata
   * inside result rows, not independent interactive controls.
   * @param {Element} [root] — scope the search; defaults to document
   */
  function patchSourceLabels(root) {
    (root || document)
      .querySelectorAll(".su__source-label, .su__ribbon-title")
      .forEach((el) => {
        if (el.getAttribute("tabindex") !== "-1") {
          el.setAttribute("tabindex", "-1");
        }
      });
  }

  /**
   * MutationObserver → waits for dynamic injection of searchForm, input,
   * or suggestion results.
   */
  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      if (mutation.addedNodes.length) {
        const form = document.getElementById("searchForm");
        if (form) bindSearchForm(form);

        const input = document.getElementById("search-box-autocomplete");
        if (input) setupInputWatcher();

        patchSourceLabels();
      }
    });
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true,
  });

  // Initial setup if already present
  const initialForm = document.getElementById("searchForm");
  if (initialForm) {
    setTimeout(() => bindSearchForm(initialForm), 100);
  }

  setupInputWatcher();
  patchSourceLabels();

  // Override AngularJS form handling (if present)
  setTimeout(() => {
    const form = document.getElementById("searchForm");
    if (form) {
      form.removeAttribute("ng-submit");
      form.removeAttribute("data-ng-submit");
      bindSearchForm(form);
    }
  }, 500);
});
