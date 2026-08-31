// search-form-handler.js

document.addEventListener("DOMContentLoaded", function () {
  const applyDefaultSearchInputLabel =
    window.SuSearchA11y?.applyDefaultSearchInputLabel;
  const syncClearButtonTabindex =
    window.SuSearchA11y?.syncClearButtonTabindex;
  const configureSearchSubmitButton =
    window.SuSearchA11y?.configureSearchSubmitButton;
  const markSearchReady = window.SuSearchA11y?.markSearchReady;
  const watchSuggestionsOpenState =
    window.SuSearchA11y?.watchSuggestionsOpenState;

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
   * @returns {HTMLFormElement | null}
   */
  function getHeaderSearchForm() {
    return document.querySelector("#auto #searchForm");
  }

  /**
   * Bind submit + click listeners to search form and apply ARIA labels.
   * @param {HTMLFormElement} form
   */
  function bindSearchForm(form) {
    if (!form || !form.closest("#auto") || form.dataset.listenerAdded) return;

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
        handleSearch(form);
        return false;
      },
      true
    );

    // Handle search button click
    const searchButton = form.querySelector(".su__search_btn");
    if (searchButton) {
      searchButton.setAttribute("type", "submit");
      searchButton.setAttribute("aria-label", labels.search);
      if (configureSearchSubmitButton) {
        configureSearchSubmitButton(searchButton);
      }
      searchButton.addEventListener(
        "click",
        function (e) {
          e.preventDefault();
          e.stopImmediatePropagation();
          handleSearch(form);
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
      const input = form.querySelector("#search-box-autocomplete");
      if (syncClearButtonTabindex) {
        syncClearButtonTabindex(clearButton, input);
      }
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
          if (syncClearButtonTabindex) {
            syncClearButtonTabindex(clearButton, input);
          }
        }
      });
    }

    form.dataset.listenerAdded = "true";
    form.setAttribute("data-original-action", originalAction);

    const input = form.querySelector("#search-box-autocomplete");
    const container = form.closest("#auto");
    if (input && container) {
      if (watchSuggestionsOpenState) {
        watchSuggestionsOpenState(container, input);
      }
      if (markSearchReady) {
        markSearchReady(container, input);
      }
    }
  }

  /**
   * Handle search action
   * @param {HTMLFormElement} [form]
   */
  function handleSearch(form) {
    const queryInput =
      form?.querySelector("#search-box-autocomplete") ||
      document.querySelector("#auto #search-box-autocomplete");
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
    const input = document.querySelector("#auto #search-box-autocomplete");
    if (!input || input.dataset.searchWatcherApplied) return;

    if (applyDefaultSearchInputLabel) {
      applyDefaultSearchInputLabel(input);
    }

    // Combobox ARIA — tells assistive technology this input controls a listbox
    input.setAttribute("role", "combobox");
    input.setAttribute("aria-haspopup", "listbox");
    input.setAttribute("aria-expanded", "false");
    input.setAttribute("autocomplete", "off");

    input.addEventListener("input", () => {
      input.setAttribute(
        "aria-expanded",
        input.value.trim() !== "" ? "true" : "false"
      );
      const clearButton = input
        .closest("form")
        ?.querySelector(".su__input-close");
      if (syncClearButtonTabindex) {
        syncClearButtonTabindex(clearButton, input);
      }
    });

    input.addEventListener("blur", () => {
      // Delay so a click on a suggestion isn't cut off before it fires
      setTimeout(() => input.setAttribute("aria-expanded", "false"), 200);
    });
    input.addEventListener("focus", () => {
      input.setAttribute("aria-expanded", "true");
      const clearButton = input
        .closest("form")
        ?.querySelector(".su__input-close");
      if (syncClearButtonTabindex) {
        syncClearButtonTabindex(clearButton, input);
      }
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
    /*
    input.addEventListener(
      "keypress",
      function (e) {
        if (e.key === "Enter") {
          e.preventDefault();
          e.stopImmediatePropagation();
          handleSearch(input.closest("form") || undefined);
          return false;
        }
      },
      true
    );
    */

    // --- Run check immediately and periodically for autofill/preload ---
    const checkDelays = [0, 100, 300, 1000, 2000];
    checkDelays.forEach((delay) => setTimeout(toggleHasTextClass, delay));

    const container = input.closest("#auto");
    if (container && watchSuggestionsOpenState) {
      watchSuggestionsOpenState(container, input);
    }
    if (container && markSearchReady) {
      markSearchReady(container, input);
    }

    input.dataset.searchWatcherApplied = "true";
  }

  const patchSourceLabels =
    window.SuSearchA11y?.patchSourceLabels ||
    function (root) {
      (root || document)
        .querySelectorAll(".su__source-label, .su__ribbon-title")
        .forEach((el) => {
          if (el.getAttribute("tabindex") !== "-1") {
            el.setAttribute("tabindex", "-1");
          }
        });
    };

  /**
   * MutationObserver → waits for dynamic injection of searchForm, input,
   * or suggestion results.
   */
  const headerSearchRoot = document.querySelector("#auto");
  if (headerSearchRoot) {
    const observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        if (mutation.addedNodes.length) {
          const form = getHeaderSearchForm();
          if (form) bindSearchForm(form);

          const input = document.querySelector("#auto #search-box-autocomplete");
          if (input) setupInputWatcher();

          patchSourceLabels(headerSearchRoot);
        }
      });
    });

    observer.observe(headerSearchRoot, {
      childList: true,
      subtree: true,
    });
  }

  // Initial setup if already present
  const initialForm = getHeaderSearchForm();
  if (initialForm) {
    setTimeout(() => bindSearchForm(initialForm), 100);
  }

  setupInputWatcher();
  patchSourceLabels(headerSearchRoot);

  // Override AngularJS form handling (if present)
  setTimeout(() => {
    const form = getHeaderSearchForm();
    if (form) {
      form.removeAttribute("ng-submit");
      form.removeAttribute("data-ng-submit");
      bindSearchForm(form);
    }
  }, 500);
});
