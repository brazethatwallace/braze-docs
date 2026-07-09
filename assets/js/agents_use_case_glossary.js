/* globals $, jQuery */
/* Agents use case glossary: filter and search.
 * Loaded only on pages using the agents_use_case_glossary layout.
 */
(function ($) {
  'use strict';

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
        return h.trim().toLowerCase() === n.trim().toLowerCase();
      });
    });
  }

  function matchAnyTag(required, items) {
    if (!required.length) return true;
    var lower = items.map(function (i) { return i.trim().toLowerCase(); });
    return required.some(function (r) { return lower.indexOf(r.trim().toLowerCase()) > -1; });
  }

  function updateOverviewVisibility() {
    var hasSearch = !!($('#api_search').val() || '').length;
    var hasFilters = document.querySelectorAll('.api_filter_div input[type="checkbox"]:checked').length > 0;
    var active = hasSearch || hasFilters;
    $('#glossary-preamble')
      .toggleClass('glossary-preamble--hidden', active)
      .attr('aria-hidden', active ? 'true' : null);
  }

  var noResultsTimer = null;
  var countTimer = null;
  var innerTimer = null;
  var searchDebounceTimer = null;
  var lastAnnouncedCount = -1;
  var altChar = false;
  var agentsUseCasesI18n = { noResults: '', showing: '' };

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

    var api_div = $('#api_list > .api_div');
    var total_cnt = api_div.length;
    var search_str = ($('#api_search').val() || '').toLowerCase();
    var selectedByGroup = {};
    document.querySelectorAll('.api_filter_div input[type="checkbox"]:checked').forEach(function (cb) {
      var group = cb.getAttribute('data-filter-group') || 'default';
      (selectedByGroup[group] = selectedByGroup[group] || []).push(cb.value);
    });
    var groupIds = Object.keys(selectedByGroup);

    var showall = !groupIds.length && !search_str;
    var result_cnt = 0;

    api_div.each(function () {
      var curdiv = $(this);
      if (showall) { curdiv.show(); return; }

      var tagsLower = (curdiv.find('.api_tags').first().attr('data-tags-lower') || '');
      var apitags = tagsLower ? tagsLower.split(',') : [];
      var filtered = groupIds.some(function (g) {
        return !matchAnyTag(selectedByGroup[g], apitags);
      });
      if (!filtered && search_str) {
        var keywords = (curdiv.attr('data-search-keywords') || '').toLowerCase();
        var curcontent = curdiv.text().replace(/(\n|\r\n|\r)\d+/g, '').toLowerCase().replace(/\s\s+/g, ' ');
        if (keywords.indexOf(search_str) < 0 && curcontent.indexOf(search_str) < 0) {
          filtered = true;
        }
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
      resultsMsg.show().html('<p>' + (agentsUseCasesI18n.noResults || '') + '</p>');
      noResultsTimer = setTimeout(function () {
        resultsCountLive.text('');
        resultsMsgLive.text('');
        innerTimer = setTimeout(function () {
          resultsMsgLive.text(agentsUseCasesI18n.noResults || '');
        }, 150);
      }, 900);
    } else {
      var message = glossaryFormatCount(agentsUseCasesI18n.showing, result_cnt, total_cnt);
      resultsCount.show().text(message);
      resultsMsgLive.text('');
      countTimer = setTimeout(function () {
        var liveMessage = glossaryFormatCount(agentsUseCasesI18n.showing, result_cnt, total_cnt);
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

  $(document).ready(function () {
    agentsUseCasesI18n = readJson('glossary-agents-use-cases-i18n-json') || agentsUseCasesI18n;

    var query_str = parseTagsQueryParam();
    $('.api_filter_div input[type="checkbox"]').each(function () {
      var $cb = $(this);
      $cb.on('change', search_apis);
      if (matchterms($cb.val(), query_str)) $cb.prop('checked', true);
    });

    updateOverviewVisibility();
    if (query_str.length > 0) search_apis();

    $('#api_search').on('input', function () {
      clearTimeout(searchDebounceTimer);
      searchDebounceTimer = setTimeout(search_apis, 150);
    });

    var location_hash = (location.hash || '').replace('%20', '-').replace('+', '-').replace(/[^a-zA-Z0-9_-]+/g, '');
    if (location_hash && $(location_hash).length && $(location_hash).offset()) {
      $('html, body').animate({ scrollTop: $(location_hash).offset().top });
    }
  });

}(jQuery));
