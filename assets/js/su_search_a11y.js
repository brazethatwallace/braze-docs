/**
 * Shared SearchUnify input label helpers for header and main search.
 */
(function (global) {
  function searchI18n(key, fallback) {
    return typeof site_i18n !== "undefined" && site_i18n[key]
      ? site_i18n[key]
      : fallback;
  }

  /**
   * @param {HTMLInputElement} input
   * @param {string} labelText
   * @param {string} placeholderHint
   */
  function applySearchInputLabel(input, labelText, placeholderHint) {
    const inputId = input.id || "search-box-autocomplete";
    const scope = input.closest("#auto, #su_main_search");
    const labelId = `${scope?.id || "search"}-search-label`;
    let label = document.getElementById(labelId);
    if (!label) {
      label = document.createElement("label");
      label.id = labelId;
      label.className = "sr-only";
      label.setAttribute("for", inputId);
      input.parentNode?.insertBefore(label, input);
    }
    label.textContent = labelText;
    input.setAttribute("aria-labelledby", labelId);
    input.removeAttribute("aria-label");
    input.setAttribute("placeholder", placeholderHint);
    const inputType = (input.getAttribute("type") || "text").toLowerCase();
    if (inputType === "text" || inputType === "input") {
      input.setAttribute("type", "search");
    }
  }

  /**
   * @param {HTMLInputElement} input
   */
  function applyDefaultSearchInputLabel(input) {
    applySearchInputLabel(
      input,
      searchI18n("site_search_input_aria", "Search everything"),
      searchI18n("site_search_input_placeholder_hint", "Search…")
    );
  }

  /**
   * Keep decorative clear controls out of the tab order until they are visible.
   * @param {HTMLElement | null} clearButton
   * @param {HTMLInputElement | null} input
   */
  function syncClearButtonTabindex(clearButton, input) {
    if (!clearButton || !input) return;

    const isVisible =
      clearButton.offsetParent !== null &&
      getComputedStyle(clearButton).visibility !== "hidden" &&
      getComputedStyle(clearButton).display !== "none" &&
      input.value.trim() !== "";

    clearButton.setAttribute("tabindex", isVisible ? "0" : "-1");
  }

  /**
   * Icon submit buttons duplicate the text field in the tab order; Enter already submits.
   * @param {HTMLButtonElement | null} searchButton
   */
  function configureSearchSubmitButton(searchButton) {
    if (!searchButton) return;
    searchButton.setAttribute("tabindex", "-1");
  }

  /**
   * @param {HTMLInputElement | null} input
   * @returns {HTMLElement | null}
   */
  function getSuggestionPanel(input) {
    const sibling = input?.nextElementSibling;
    if (sibling?.classList.contains("su__autocomplete-suggestion")) {
      return sibling;
    }

    return (
      input?.closest("#auto, #su_main_search, form")?.querySelector(
        ".su__autocomplete-suggestion"
      ) || null
    );
  }

  /**
   * @param {HTMLElement} panel
   * @returns {boolean}
   */
  function panelHasSuggestionContent(panel) {
    return (
      panel.querySelector(
        ".su__suggestions-list > *, .su__suggestion-title, .su__recentSearch_result, .su__suggestion-desc"
      ) !== null
    );
  }

  /**
   * @param {HTMLInputElement | null} input
   * @returns {boolean}
   */
  function isSuggestionPanelOpen(input) {
    const panel = getSuggestionPanel(input);
    if (!panel) return false;

    const style = getComputedStyle(panel);
    if (
      style.display === "none" ||
      style.visibility === "hidden" ||
      panel.offsetHeight === 0
    ) {
      return false;
    }

    // SearchUnify can reveal the panel shell (or a loader) before results render.
    return panelHasSuggestionContent(panel);
  }

  /**
   * @param {HTMLElement | null} container
   * @param {HTMLInputElement | null} input
   */
  function syncSuggestionsOpenState(container, input) {
    if (!container || !input) return;

    container.classList.toggle(
      "su-search-suggestions-open",
      isSuggestionPanelOpen(input)
    );
  }

  /**
   * Reveal the widget after SearchUnify injects markup and clear init-time focus.
   * @param {HTMLElement | null} container
   * @param {HTMLInputElement | null} input
   */
  function markSearchReady(container, input) {
    if (!container || container.dataset.searchReady) return;

    container.dataset.searchReady = "true";
    container.classList.add("su-search-ready");
    syncSuggestionsOpenState(container, input);

    if (input && document.activeElement === input && !input.dataset.userFocused) {
      input.blur();
    }
  }

  /**
   * Keep panel-connect styles in sync with the visible autocomplete dropdown.
   * @param {HTMLElement | null} container
   * @param {HTMLInputElement | null} input
   */
  function watchSuggestionsOpenState(container, input) {
    if (!container || !input || input.dataset.suggestionsWatcherApplied) return;

    input.dataset.suggestionsWatcherApplied = "true";

    const scheduleSync = () =>
      requestAnimationFrame(() => {
        syncSuggestionsOpenState(container, input);
        attachPanelObserver(input, scheduleSync);
      });

    input.addEventListener("focus", scheduleSync);
    input.addEventListener("blur", () => setTimeout(scheduleSync, 200));
    input.addEventListener("input", scheduleSync);
    input.addEventListener("pointerdown", () => {
      input.dataset.userFocused = "true";
    });
    input.addEventListener("keydown", (event) => {
      if (event.key === "Tab") {
        input.dataset.userFocused = "true";
      }
    });

    attachPanelObserver(input, scheduleSync);

    const containerObserver = new MutationObserver(scheduleSync);
    containerObserver.observe(container, {
      childList: true,
      subtree: true,
    });

    scheduleSync();
  }

  const panelObservers = new WeakMap();

  /**
   * @param {HTMLInputElement} input
   * @param {() => void} scheduleSync
   * @returns {boolean}
   */
  function attachPanelObserver(input, scheduleSync) {
    const panel = getSuggestionPanel(input);
    const existing = panelObservers.get(input);

    if (existing?.panel === panel && panel?.isConnected) {
      return true;
    }

    if (existing) {
      existing.observer.disconnect();
      panelObservers.delete(input);
    }

    if (!panel) return false;

    const panelObserver = new MutationObserver(scheduleSync);
    panelObserver.observe(panel, {
      attributes: true,
      attributeFilter: ["style", "class"],
      childList: true,
      subtree: true,
    });
    panelObservers.set(input, { panel, observer: panelObserver });
    return true;
  }

  global.SuSearchA11y = {
    searchI18n,
    applySearchInputLabel,
    applyDefaultSearchInputLabel,
    syncClearButtonTabindex,
    configureSearchSubmitButton,
    syncSuggestionsOpenState,
    markSearchReady,
    watchSuggestionsOpenState,
  };
})(typeof window !== "undefined" ? window : this);
