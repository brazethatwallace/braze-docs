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
    if (input.getAttribute("type") === "input") {
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

  global.SuSearchA11y = {
    searchI18n,
    applySearchInputLabel,
    applyDefaultSearchInputLabel,
  };
})(typeof window !== "undefined" ? window : this);
