document.addEventListener("DOMContentLoaded", function () {
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
      clearButton.setAttribute("tabindex", "0");
      clearButton.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          clearButton.click();
        }
      });
    }

    // Enter key
    if (queryInput) {
      queryInput.addEventListener("keypress", function (e) {
        if (e.key === "Enter") {
          e.preventDefault();
          e.stopImmediatePropagation();
          handleSearch(queryInput, langSelect);
        }
      });

      const translations = {
        en: "Search everything",
        "pt-br": "Buscar tudo",
        ko: "전체 검색",
        fr: "Rechercher tout",
        es: "Buscar todo",
        de: "Alles durchsuchen",
        ja: "すべて検索"
      };

      const placeholderText = translations[lang] || translations.en;
      queryInput.setAttribute("placeholder", `${placeholderText}...`);
      queryInput.setAttribute("aria-label", placeholderText);
    }

    // Clear icon click
    if (queryInput) {
      container.addEventListener("click", function (e) {
        if (e.target.closest(".su__input-close")) {
          queryInput.value = "";
          queryInput.focus();
        }
      });
    }

    form.dataset.listenerAdded = "true";
  }

  function handleSearch(queryInput, langSelect) {
    const query = queryInput ? queryInput.value.trim() : "";
    const lang = langSelect ? langSelect.value : "en";

    const targetUrl = `/docs/${lang}/search?searchString=${encodeURIComponent(query)}`;
    window.location.href = targetUrl;
  }

  // Watch for dynamic content
  const targetNode = document.querySelector("#su_main_search");
  if (targetNode) {
    const observer = new MutationObserver(() => {
      const form = targetNode.querySelector("form");
      const input = targetNode.querySelector("#search-box-autocomplete");
      if (form && input) {
        bindSearchForm(targetNode);
      }
    });

    observer.observe(targetNode, { childList: true, subtree: true });
  }
});