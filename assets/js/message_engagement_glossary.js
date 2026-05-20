/* globals $, jQuery */
/* Message Engagement Events glossary: filter, search, lazy tab loading.
 * Loaded only on pages using the message_engagement_events_glossary layout.
 * Data is read from <script type="application/json"> blocks rendered by the layout.
 */
(function ($) {
  'use strict';

  /*  helpers  */

  function readJson(id) {
    try {
      var el = document.getElementById(id);
      return el && el.textContent ? JSON.parse(el.textContent) : null;
    } catch (e) {
      return null;
    }
  }

  function glossaryFormatCount(template, count, total) {
    if (!template) return '';
    return String(template)
      .replace(/__COUNT__/g, String(count))
      .replace(/__TOTAL__/g, String(total));
  }

  function getUrlParameter(name) {
    name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
    var regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
    var results = regex.exec(location.search);
    return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
  }

  function parseTagsQueryParam() {
    var raw = getUrlParameter('tags');
    if (!raw) return [];
    return raw.toLowerCase().split(',').map(function (t) { return t.trim(); }).filter(Boolean);
  }

  function matchterms(searchterm, items) {
    var needle = Array.isArray(searchterm) ? searchterm : [searchterm];
    var haystack = Array.isArray(items) ? items : [items];
    return needle.some(function (n) {
      return haystack.some(function (h) {
        return h.trim().toLowerCase().indexOf(n.trim().toLowerCase()) > -1;
      });
    });
  }

  function matchAnyTag(required, items) {
    if (!required.length) return true;
    var lower = items.map(function (i) { return i.trim().toLowerCase(); });
    return required.some(function (r) { return lower.indexOf(r.trim().toLowerCase()) > -1; });
  }

  /*  fragment cache & loader  */

  var fragmentCache = {};

  function loadCurrentsLazyTab($pane) {
    var fragmentUrl = $pane.attr('data-currents-fragment');
    var loaded = $pane.attr('data-currents-loaded');
    if (!fragmentUrl || loaded === 'true' || loaded === 'loading') return;

    if (fragmentCache[fragmentUrl]) {
      $pane.html(fragmentCache[fragmentUrl]);
      $pane.attr('data-currents-loaded', 'true');
      return;
    }

    $pane.attr('data-currents-loaded', 'loading');
    $.get(fragmentUrl).done(function (html) {
      fragmentCache[fragmentUrl] = html;
      $pane.html(html);
      $pane.attr('data-currents-loaded', 'true');
    }).fail(function () {
      $pane.html('<p>' + (currentsEventsI18n.loadError || 'Unable to load this schema. Refresh the page and try again.') + '</p>');
      $pane.attr('data-currents-loaded', 'true');
    });
  }

  /*  overview visibility  */

  function updateOverviewVisibility() {
    var hasSearch = !!($('#api_search').val() || '').length;
    var hasFilters = document.querySelectorAll('.api_filter_div input[type="checkbox"]:checked').length > 0;
    var active = hasSearch || hasFilters;
    $('#glossary-preamble')
      .toggleClass('glossary-preamble--hidden', active)
      .attr('aria-hidden', active ? 'true' : null);
  }

  /*  search / filter  */

  var noResultsTimer = null;
  var countTimer = null;
  var innerTimer = null;
  var searchDebounceTimer = null;
  var lastAnnouncedCount = -1;
  var altChar = false;
  var currentsEventsI18n = { noResults: '', showing: '', loading: 'Loading schema\u2026', loadError: 'Unable to load this schema. Refresh the page and try again.' };

  function search_apis() {
    updateOverviewVisibility();

    var resultsMsg = $('#results_msg');
    var resultsCount = $('#results_count');
    var resultsCountLive = $('#results_count_live');
    var resultsMsgLive = $('#results_msg_live');

    clearTimeout(noResultsTimer);
    clearTimeout(countTimer);
    clearTimeout(innerTimer);
    resultsCount.hide();
    resultsMsg.hide();

    // Fix #4: use direct children only to exclude the #api_list container itself
    var api_div = $('#api_list > .api_div');
    var total_cnt = api_div.length;
    var search_str = ($('#api_search').val() || '').toLowerCase();
    var selected_vals = [];
    document.querySelectorAll('.api_filter_div input[type="checkbox"]:checked').forEach(function (cb) {
      selected_vals.push(cb.value);
    });

    var showall = !selected_vals.length && !search_str;

    var result_cnt = 0;
    api_div.each(function () {
      var curdiv = $(this);
      if (showall) { curdiv.show(); return; }

      var tagsLower = (curdiv.find('.api_tags').first().attr('data-tags-lower') || '');
      var apitags = tagsLower ? tagsLower.split(',') : [];
      var filtered = false;

      if (selected_vals.length && apitags.indexOf('all') === -1 && !matchAnyTag(selected_vals, apitags)) {
        filtered = true;
      }
      if (!filtered && search_str) {
        // Search the build-time keyword index (event name + tags + description +
        // schema field names), which avoids touching lazy-loaded tab pane content.
        var keywords = (curdiv.attr('data-search-keywords') || '').toLowerCase();
        if (keywords.indexOf(search_str) < 0) filtered = true;
      }

      if (filtered) { curdiv.hide(); } else { curdiv.show(); result_cnt++; }
    });

    if (showall) {
      resultsMsg.text('');
      resultsCountLive.text('');
      resultsMsgLive.text('');
      lastAnnouncedCount = -1;
      return;
    }

    if (!result_cnt) {
      resultsMsg.show().text(currentsEventsI18n.noResults || '');
      noResultsTimer = setTimeout(function () {
        resultsCountLive.text('');
        resultsMsgLive.text('');
        innerTimer = setTimeout(function () {
          resultsMsgLive.text(currentsEventsI18n.noResults || '');
        }, 150);
      }, 900);
    } else {
      var message = glossaryFormatCount(currentsEventsI18n.showing, result_cnt, total_cnt);
      resultsCount.show().text(message);
      resultsMsgLive.text('');
      countTimer = setTimeout(function () {
        var liveMessage = glossaryFormatCount(currentsEventsI18n.showing, result_cnt, total_cnt);
        if (result_cnt === lastAnnouncedCount) {
          altChar = !altChar;
          if (altChar) liveMessage += '\xa0';
        }
        lastAnnouncedCount = result_cnt;
        resultsCountLive.text('');
        innerTimer = setTimeout(function () { resultsCountLive.text(liveMessage); }, 150);
      }, 900);
    }
  }

  /*  filter toggle (show all / show fewer)  */

  function updateFilterToggleButton() {
    var $btn = $('#glossary-filter-toggle');
    var expanded = $btn.attr('aria-expanded') === 'true';
    $btn.find('.show-more-text').attr('aria-hidden', expanded ? 'true' : 'false');
    $btn.find('.show-less-text').attr('aria-hidden', expanded ? 'false' : 'true');
  }

  function initFilterToggle() {
    var $btn = $('#glossary-filter-toggle');
    updateFilterToggleButton();
    $btn.on('click', function () {
      var expanded = $btn.attr('aria-expanded') === 'true';
      $btn.attr('aria-expanded', String(!expanded));
      updateFilterToggleButton();
      $('.filter-overflow').toggleClass('filter-overflow--hidden', expanded);
    });
  }

  /*  initialise  */

  $(document).ready(function () {
    currentsEventsI18n = readJson('glossary-currents-events-i18n-json') || currentsEventsI18n;

    // Wire checkboxes (rendered by Liquid in the sidebar)
    var query_str = parseTagsQueryParam();
    $('.api_filter_div input[type="checkbox"]').each(function () {
      var $cb = $(this);
      $cb.on('change', search_apis);
      if (matchterms($cb.val(), query_str)) $cb.prop('checked', true);
    });

    initFilterToggle();
    updateOverviewVisibility();

    if (query_str.length > 0) search_apis();

    // Fix #2: debounce text input to avoid layout thrash on every keystroke
    $('#api_search').on('input', function () {
      clearTimeout(searchDebounceTimer);
      searchDebounceTimer = setTimeout(search_apis, 150);
    });

    /* lazy tab loading */
    $('#api-main').on('click', '.tab_toggle', function () {
      var tabTarget = $(this).attr('data-tab-target');
      var tabSlug   = $(this).attr('data-tab');
      if (!tabTarget || !tabSlug) return;
      setTimeout(function () {
        var $pane = $('#' + tabTarget + ' .ab-tab-pane.' + tabSlug + '_tab[data-currents-lazy]');
        loadCurrentsLazyTab($pane);
      }, 0);
    });

    // Load the initially-active tab pane(s) immediately
    setTimeout(function () {
      $('#api_list .ab-tab-pane[data-currents-lazy].active').each(function () {
        loadCurrentsLazyTab($(this));
      });
    }, 0);

    /* scroll to hash */
    var location_hash = (location.hash || '').replace('%20', '-').replace('+', '-').replace(/[^a-zA-Z0-9_-]+/g, '');
    if (location_hash && $(location_hash).length && $(location_hash).offset()) {
      $('html, body').animate({ scrollTop: $(location_hash).offset().top });
    }
  });

}(jQuery));
