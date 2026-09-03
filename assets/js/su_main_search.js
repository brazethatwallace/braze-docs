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

  function showSearchContainer(container) {
    if (!container || container.dataset.searchReady) return;

    container.dataset.searchReady = "true";
    container.classList.add("su-search-ready");
  }

  function revealSearchContainer(container, input) {
    if (!container || container.dataset.searchReady) return;

    showSearchContainer(container);

    if (input && document.activeElement === input && !input.dataset.userFocused) {
      input.blur();
    }
  }

  function trackUserFocus(input) {
    if (!input || input.dataset.userFocusTrackingApplied) return;

    input.dataset.userFocusTrackingApplied = "true";
    input.addEventListener("pointerdown", () => {
      input.dataset.userFocused = "true";
    });
    input.addEventListener("keydown", (event) => {
      if (event.key === "Tab") {
        input.dataset.userFocused = "true";
      }
    });
  }

  const buttonLabels = {
    en:     { form: "Site search", search: "Search", clear: "Clear search" },
    "pt-br":{ form: "Pesquisa do site", search: "Pesquisar", clear: "Limpar pesquisa" },
    ko:     { form: "사이트 검색", search: "검색", clear: "검색 지우기" },
    fr:     { form: "Recherche sur le site", search: "Rechercher", clear: "Effacer la recherche" },
    es:     { form: "Búsqueda en el sitio", search: "Buscar", clear: "Borrar búsqueda" },
    de:     { form: "Sitesuche", search: "Suchen", clear: "Suche löschen" },
    ja:     { form: "サイト検索", search: "検索", clear: "検索をクリア" },
  };

  function bindSearchForm(container) {
    const form = container.querySelector("form");
    const queryInput = container.querySelector("#search-box-autocomplete");
    const searchButton = container.querySelector(".su__search_btn");
    const clearButton = container.querySelector(".su__input-close");
    const langSelect = document.querySelector("#lang_select");

    if (!form || form.dataset.listenerAdded) return;

    const lang = document.documentElement.lang;
    const labels = buttonLabels[lang] || buttonLabels.en;

    form.setAttribute("aria-label", labels.form);

    // Prevent form submit
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      e.stopImmediatePropagation();
      handleSearch(queryInput, langSelect);
    });

    // Search button click
    if (searchButton) {
      searchButton.setAttribute("type", "submit");
      searchButton.setAttribute("aria-label", labels.search);
      if (configureSearchSubmitButton) {
        configureSearchSubmitButton(searchButton);
      }
      searchButton.addEventListener("click", function (e) {
        e.preventDefault();
        e.stopImmediatePropagation();
        handleSearch(queryInput, langSelect);
      });
    }

    // Clear button
    if (clearButton) {
      clearButton.setAttribute("aria-label", labels.clear);
      clearButton.setAttribute("role", "button");
      if (syncClearButtonTabindex) {
        syncClearButtonTabindex(clearButton, queryInput);
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
        if (queryInput) {
          queryInput.value = "";
          queryInput.focus();
          if (syncClearButtonTabindex) {
            syncClearButtonTabindex(clearButton, queryInput);
          }
        }
      });
    }

    // Enter key
    if (queryInput) {
      /*
      queryInput.addEventListener("keypress", function (e) {
        if (e.key === "Enter") {
          e.preventDefault();
          e.stopImmediatePropagation();
          handleSearch(queryInput, langSelect);
        }
      });
      */

      if (applyDefaultSearchInputLabel) {
        applyDefaultSearchInputLabel(queryInput);
      }

      // Combobox ARIA — tells assistive technology this input controls a listbox
      queryInput.setAttribute("role", "combobox");
      queryInput.setAttribute("aria-haspopup", "listbox");
      queryInput.setAttribute("aria-expanded", "false");
      queryInput.setAttribute("autocomplete", "off");

      queryInput.addEventListener("focus", () => {
        queryInput.setAttribute("aria-expanded", "true");
        if (syncClearButtonTabindex) {
          syncClearButtonTabindex(clearButton, queryInput);
        }
      });
      queryInput.addEventListener("blur", () => {
        // Delay so a click on a suggestion isn't cut off before it fires
        setTimeout(() => queryInput.setAttribute("aria-expanded", "false"), 200);
      });
      queryInput.addEventListener("input", () => {
        queryInput.setAttribute(
          "aria-expanded",
          queryInput.value.trim() !== "" ? "true" : "false"
        );
        if (syncClearButtonTabindex) {
          syncClearButtonTabindex(clearButton, queryInput);
        }
      });
    }

    if (queryInput) {
      if (watchSuggestionsOpenState) {
        watchSuggestionsOpenState(container, queryInput);
      } else {
        trackUserFocus(queryInput);
      }
      if (markSearchReady) {
        markSearchReady(container, queryInput);
      } else {
        revealSearchContainer(container, queryInput);
      }
    }

    form.dataset.listenerAdded = "true";
  }

  function handleSearch(queryInput, langSelect) {
    const query = queryInput ? queryInput.value.trim() : "";
    const lang = langSelect ? langSelect.value : "en";

    if (query) {
      const targetUrl = `/docs/${lang}/search?searchString=${encodeURIComponent(query)}`;
      window.location.href = targetUrl;
    } else {
      if (queryInput) queryInput.focus();
    }
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

  // Watch for dynamic content
  const targetNode = document.querySelector("#su_main_search");
  if (targetNode) {
    setTimeout(() => {
      showSearchContainer(targetNode);
    }, 5000);

    const observer = new MutationObserver(() => {
      const form = targetNode.querySelector("form");
      const input = targetNode.querySelector("#search-box-autocomplete");
      if (form && input) {
        bindSearchForm(targetNode);
      }
      patchSourceLabels(targetNode);
    });

    observer.observe(targetNode, { childList: true, subtree: true });

    bindSearchForm(targetNode);
  }

  patchSourceLabels();
});
