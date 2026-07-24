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

  global.SuSearchA11y = {
    searchI18n,
    applySearchInputLabel,
    applyDefaultSearchInputLabel,
    syncClearButtonTabindex,
    configureSearchSubmitButton,
  };
})(typeof window !== "undefined" ? window : this);
