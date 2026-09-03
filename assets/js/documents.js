var page_language = site_language;

function generateUUID() { // Public Domain/MIT
    var d = new Date().getTime();//Timestamp
    var d2 = (performance && performance.now && (performance.now()*1000)) || 0;//Time in microseconds since page-load or 0 if unsupported
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random() * 16;//random number between 0 and 16
        if(d > 0){//Use timestamp until depleted
            r = (d + r)%16 | 0;
            d = Math.floor(d/16);
        } else {//Use microseconds since page-load if supported
            r = (d2 + r)%16 | 0;
            d2 = Math.floor(d2/16);
        }
        return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
}

function unEncodeURIComponent(str) {
  let decodedStr = decodeURIComponent(str);
  decodedStr = decodedStr.replace(/%21|%27|%28|%29|%2A/g, function(match) {
    switch (match) {
      case '%21':
        return '!';
      case '%27':
        return "'";
      case '%28':
        return '(';
      case '%29':
        return ')';
      case '%2A':
        return '*';
      default:
        return match;
    }
  });

  return decodedStr;
}

function setAdaTableRole(role='presentation') {
  $('table').each(function(){
    var $table = $(this);

    // Tables with an accessible name are data tables.
    // Ensure they always use native table semantics by clearing any presentation role.
    var hasAccessibleName = !!$table.attr('aria-label') ||
                            !!$table.attr('aria-labelledby') ||
                            $table.children('caption').length > 0;
    if (hasAccessibleName) {
      $table.removeAttr('role');
      return;
    }

    // For tables without an accessible name, apply the original heuristic:
    // mark as presentation, then remove that role if the table has header cells
    // (a signal that it is a data table, not a layout table).
    if (!$table.attr('role')) {
      $table.attr('role', role);
    }
    if ($table.attr('role') === role &&
        ($table.find('th').length > 0 || $table.find('thead').length > 0)) {
      $table.removeAttr('role');
    }
  });
}

function string_to_slug(str) {
  if (str) {
    str = str.toLowerCase().replace(/\s/g, '-').replace(/[^\w-]/g, '');
  }
  return str;
}
// TODO: The __algolia_user cookie and algolia_user variable below are remnants of Algolia
// Insights tracking. The Algolia frontend has been removed; confirm with the team that this
// cookie is no longer needed and remove in a follow-up PR.
let algolia_user = Cookies.get('__algolia_user');
if (!algolia_user){
  algolia_user = generateUUID();
}

var search_color_mapping = {
  'endpoint': '#33C699',
  'channel': '#FF9349',
  'partner': '#3ACCDD',
  'tool': '#F7918E',
  'platform': '#27368F',
  'search_tag': '#0759AA',
};

var custom_word_mapping = {
  'REST': 'REST',
  'API': 'API',
  'APIs': 'APIs',
  'iOS': 'iOS',
  'ID': 'ID',
  'IDs': 'IDs',
  'FAQ': 'FAQ',
  'FAQS': 'FAQs',
  'In-App': 'In-App',
  'GPDR': 'GPDR',
  'mParticle': 'mParticle',
  'SDK': 'SDK',
  'SDKs': 'SDKs',
  'IP': 'IP',
  'IPs': 'IPs',
  'SSL': 'SSL',
  'SAML': 'SAML',
  'SSO': 'SSO',
  'TTL': 'TTL',
  'A/B': 'A/B',
  'HTML': 'HTML',
  'GIF': 'GIF',
  'GIFs': 'GIFs',
  'OTT': 'OTT',
  'TV': 'TV',
  'KPIs': 'KPIs',
  'S3': 'S3',
  'FireOS': 'FireOS',
  'tvOS': 'tvOS',
  'macOS': 'macOS',
  'CocoaPods': 'CocoaPods',
  'AndroidX': 'AndroidX',
  'JavaScript': 'JavaScript',
  'a': 'a',
  'the': 'the',
  'by': 'by',
  'with': 'with',
  'to': 'to',
  'from': 'from',
  'an': 'an',
  'SMS': 'SMS',
  'MMS': 'MMS',
  'Platform Wide': 'Platform Wide Features & Behaviors',
  'lab': 'LAB',
};
// Track Specific tabs to remember on reload
var tab_track = {
  'android': 'tb_android',
  'swift': 'tb_ios',
  'objective-c': 'tb_ios',
  'java': 'tb_android',
  'kotlin': 'tb_android',
  'snowflake': 'tb_data',
  'redshift': 'tb_data',
  'bigquery': 'tb_data',
  'databricks': 'tb_data',
}
// TODO: Remove this cookie set along with the algolia_user variable above in a follow-up PR.
Cookies.set('__algolia_user', algolia_user, { expires: 30 });

String.prototype.upCaseWord = function() {
  return this.toString().replace(/\b\w/g, function(l){ return l.toUpperCase() });
};
String.prototype.replaceUnder = function() {
  return this.toString().replace(/\%20/g, ' ').replace(/\_/g, ' ');
};
Array.prototype.upCaseWord = function() {
  return this.map(function(itm){ return itm.toString().replace(/\b\w/g, function(l){ return l.toUpperCase() }) });
};
Array.prototype.replaceUnder = function() {
  return this.map(function(itm){ return itm.toString().replace(/\%20/g, ' ').replace(/\_/g, ' ')});
};
String.prototype.mapReplace = function(word_map) {
  var mstr = this;
  for (var wd in word_map) {
    if (word_map.hasOwnProperty(wd)) {
        var rep = new RegExp('\\b' + wd + '\\b','gi');
        mstr = mstr.replace(rep,word_map[wd]);
    }
  }
  return mstr;
};

String.prototype.sanitize = function() {
  return this.replace(/\+/g, ' ').replace(/\%20/g, ' ').replace(/\_/g, ' ').replace(/</g,'').replace(/>/g,'').replace(/&lt;/g,'').replace(/&gt;/g,'').replace(/\'/g,'').replace(/\"/g,'');
};

function replaceParams(qs = '', pr = {}, replace_blank = false) {
	var queryString = qs.replace(/^\?/,'').split('&');
	var params = {};
  if (replace_blank){
    params = pr;
  }
	queryString.forEach((e) => {
		let param = e.split('=');
		if (param.length >1){
      // Ignore the parameter if it's blank
      if (pr[param[0]] !== '') {
        params[param[0]] = (pr[param[0]] || param[1]);
      }
		}
	});


  var queryStringParam = [];
  for (const k in params) {
    if (params.hasOwnProperty(k)) {
      queryStringParam.push(`${k}=${params[k]}`);
    }
  }
	return `?${queryStringParam.join('&')}`;
};

$(document).ready(function() {
  $("#braze_header").click((e) => {
    setTimeout(function() {
      let hide_backdrop = false;
      $("#braze_header .nav-link.dropdown-toggle").each((eb, ea) => {
        let itm = $(ea);
        if(itm.attr('aria-expanded') == 'true') {
          hide_backdrop = true;
        }
      });
      if (!hide_backdrop) {
        $("#backdrop").removeClass("backdrop-show");
      }
    }, 100);
  });
  $("#braze_header .nav-link.dropdown-toggle").click((e) => {
    $("#braze_header .nav-link.dropdown-toggle").each((e, ea) => {
      ea.children[0].classList.remove("border-focus-show");
    });
    const isOpen = e.currentTarget.ariaExpanded !== "true";
    const borderDiv = e.currentTarget.children[0];
    borderDiv.classList.toggle("border-focus-show", isOpen);
    $("#backdrop").toggleClass("backdrop-show", isOpen);
  });
  $("#backdrop").click((e) => {
    $("#braze_header .nav-link.dropdown-toggle").each((e, ea) => {
      ea.children[0].classList.remove("border-focus-show");
    });
    e.currentTarget.classList.remove("backdrop-show");
  });

  // Default tab panes must be visible before the first TOC build: toc.js skips
  // headers that are not :visible, and _tabs.scss hides .sdk-ab-tab-pane until .active.
  $('.ab-tab-content .ab-tab-pane:first-child, .sdk-tab-content .sdk-ab-tab-pane:first-child').addClass('active');
  $('.ab-sub_tab-content .ab-sub_tab-pane:first-child, .sdk-ab-sub_tab-content .sdk-ab-sub_tab-pane:first-child').addClass('sub_active');

  $('#toc').toc({
    headers:  ((typeof toc_headers != 'undefined') ? toc_headers : "h2,h3"),
    minimumHeaders: ((typeof toc_minheaders != 'undefined') ? toc_minheaders : 2),
  });
  // Use Bootstrap's "Scrollspy" plugin to dynamically expand/collapse ToC
  if ($('#toc nav').length) {
    $('#toc_col').removeClass('notoc');
    //$('#toc_toggle').removeClass('notoc');

    $('body').scrollspy('refresh');
    $(window).on('activate.bs.scrollspy', function() {
      var active_toc = $('#toc').find("a.nav-link.active").last().attr("href");
      var hash = active_toc;
      if (!hash){
        hash = window.location.pathname || '.';
        active_toc = '.';
      }
      else {
        hash = window.location.pathname + hash;
      }

      window.history.replaceState(null, null, hash);
      var tcol = $('#toc_col'); //.scrollTop('#toc_' + hash, 200);
      // scroll left nav also
      tcol.scrollTop($('#toc_' + active_toc.substring(1)).offset().top - $('#toc').offset().top - 10);
    });

    // Add smooth scrolling on all links inside the navbar
    $("#toc a").on('click', function(event) {

      // Make sure this.hash has a value before overriding default behavior
      if (this.hash !== "") {
        // Prevent default anchor click behavior
        event.preventDefault();
        // Store hash
        var hash = unEncodeURIComponent(this.hash);
        // Using jQuery's animate() method to add smooth page scroll
        // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
        $('html, body').animate({
          scrollTop: $(hash).offset().top
        }, 800, function() {
          // Add hash (#) to URL when done scrolling (default click behavior)
          window.location.hash = hash;
        });

      } // End if

    });

  }
  else {
    //$('#toc_col').addClass('notoc');

  }
  //var nav_bottom_height = $('#nav_bottom').height();
  var backToTopThreshold = 300;
  var $backToTopBtn = $('.back-to-top-btn');
  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function setBackToTopVisible(isVisible) {
    if (!$backToTopBtn.length) {
      return;
    }
    $backToTopBtn.toggleClass('is-visible', isVisible);
    $backToTopBtn.attr('tabindex', isVisible ? '0' : '-1');
    $('body').toggleClass('btt-visible', isVisible);
  }

  var scrollHandler = function() {
    var y_cord = $(this).scrollTop();
    setBackToTopVisible(y_cord > backToTopThreshold);
  };
  scrollHandler();
  $(window).scroll(scrollHandler);

  $backToTopBtn.on('click', function() {
    var contentStart = document.getElementById('content_start');
    if (!contentStart) {
      return;
    }
    contentStart.scrollIntoView({
      behavior: prefersReducedMotion ? 'auto' : 'smooth',
      block: 'start'
    });
    contentStart.focus({ preventScroll: true });
  });

  // See if sdk tabs should be changed based on url hash
  let location_hash = window.location.hash.slice(1).replace(/[^a-zA-Z0-9_-]+/g, '');
  if (location_hash) {
    const sdk_hash = $('#' + decodeURIComponent(location_hash));
    if (sdk_hash.is(':header')) {
      const sdk_el = sdk_hash.closest("[data-sdk-tab]");
      let sdk_tab = sdk_el.attr('data-sdk-tab');
      // add sdk tab to query header
      if (sdk_tab) {
        sdk_tab = sdk_tab.replace('sdk-','');
        let tab_replace = {
          'sdktab': sdk_tab
        };
        let query_str = replaceParams(window.location.search, tab_replace, true) + '#' + sdk_hash.attr('id');
        window.history.replaceState(null, null, window.location.pathname + query_str);
      }
    }
  }


  function setTabState(curtab, query_name = 'tab'){
    let tab_norm = curtab.toLowerCase();
    let tab_replace = {};
    tab_replace[query_name] = encodeURIComponent(tab_norm);
    let query_str = replaceParams(window.location.search, tab_replace, true);
    window.history.replaceState(null, null, window.location.pathname + query_str);
    switch(query_name) {
      case 'sdktab': {
        Cookies.set('sdktab',tab_norm, { expires: 365 });
      }
      case 'sdksubtab': {
        Cookies.set('sdksubtab',tab_norm, { expires: 365 });
      }
      default: {
        if (tab_track[tab_norm]){
          Cookies.set(tab_track[tab_norm],tab_norm, { expires: 365 });
        }
      }
    }
    if (typeof mermaid !== 'undefined') {
      runMermaidCharts();
    }
  }

  // see if a details tag should be auto-opened
  var details_list = $('details');
  var url_hash = window.location.hash.replace('#','')
  details_list.each(function(k,v) {
    var $this = $(this);
    if (url_hash == string_to_slug($this.find('summary')[0].innerText)) {
      $this.attr('open',true);
    }
  });

  // set tab list attribute for screenreader
  var list_tabs = $('ul.ab-nav')
  list_tabs.each(function(i){
    var $this = $(this);
    if (!$this.attr('role')) {
      $this.attr('role','tablist');
    }
  });
  var list_tab = list_tabs.children('li')
  list_tab.each(function(i){
    var $this = $(this);
    if (!$this.attr('role')) {
      $this.attr('role','tab');
    }
  });
  // Safari/WebKit drops list semantics when list-style is removed. Prose lists keep
  // native markers in CSS; role=list reinforces the group. Do not set role=listitem
  // on native <li> - it interferes with bullet and position announcements.
  $('#article-main ul').not('.ab-nav').add('#article-main ol').each(function() {
    if (!$(this).attr('role')) {
      $(this).attr('role', 'list');
    }
  });


  // Footer navigation
  var parent_top = 'nav_top';

  var nav_active = $('#' + parent_top + ' div.nav-item.active');
  var nav_bottom = $('#bottom_page_nav');

  var pg_prev_div = $("#page_prev");
  var pg_next_div = $("#page_next");
  var pg_prev_link = $("#page_prev_link");
  var pg_next_link = $("#page_next_link");

  var data_parent = nav_active.parent();
  var cnt = 0;
  var max_parent = 99;
  while ((data_parent.parent().attr('id') != parent_top) && (data_parent.attr('id') != parent_top) && (cnt < max_parent)){
      data_parent = data_parent.parent();
      cnt++;
  }
  var nav_links = data_parent.find('div.nav-item.active, .nav_link');
  var nav_index = nav_links.index(nav_active) ;
  if (nav_index > 0) {
    var pg_prev = nav_links.eq(nav_index - 1);//nav_active.prevAll('[data-parent="' + data_parent + '"]').first();
    nav_bottom.addClass('flex');
    pg_prev_link.attr('href',pg_prev.attr('href') );
    pg_prev_div.html(`<span class="nav_indicator"><i class="fas fa-long-arrow-alt-left"></i> ${site_i18n['previous'] || 'PREVIOUS'}</span> ${pg_prev.html()}`);
    pg_prev_div.css('display', 'inline-block');
    if (nav_index < (nav_links.length -1)) {
      pg_prev_div.css('border-right', '0px');
    }
  }
  else {
    pg_prev_div.hide();
  }

  if (nav_index < (nav_links.length -1)) {
    var pg_next = nav_links.eq(nav_index + 1);//nav_active.nextAll('[data-parent="' + data_parent + '"]').first();
    nav_bottom.addClass('flex');
    pg_next_link.attr('href',pg_next.attr('href') );
    pg_next_div.html(`<span class="nav_indicator">${site_i18n['next'] || 'NEXT'} <i class="fas fa-long-arrow-alt-right"></i></span> ${pg_next.html()}`);
    pg_next_div.css('display', 'inline-block');
  }
  else {
    pg_next_div.hide();
  }
  // link image fix for underline
  $('#article-main a:has(> img)').css('display','inline-block');

  // Scroll the active nav item into view on page load. Active sections are
  // pre-expanded server-side (no collapse animation), so no delay is needed.
  // Uses scrollTop directly on #left_navmenu rather than scrollIntoView() to
  // avoid scrollIntoView walking up to the main viewport and fighting URL fragments.
  var $nav = $('#left_navmenu');
  var $navActive = $nav.find('.nav-item.active').last();
  if ($navActive.length) {
    $nav.scrollTop(
      $nav.scrollTop() + $navActive.offset().top - $nav.offset().top - ($nav.height() / 2) + ($navActive.outerHeight() / 2)
    );
  }

  function logDocNavRailCustomEvent(eventName, extraProps) {
    if (!window.braze || typeof window.braze.logCustomEvent !== 'function') {
      return;
    }
    var payload = {
      page_url: window.location.pathname,
      page_title: document.title
    };
    if (extraProps) {
      for (var key in extraProps) {
        if (Object.prototype.hasOwnProperty.call(extraProps, key)) {
          payload[key] = extraProps[key];
        }
      }
    }
    braze.logCustomEvent(eventName, payload);
    braze.requestImmediateDataFlush();
  }

  function setSidebarToggleIcon(isCollapsed) {
    var btn = $('#sidebar_toggle');
    var img = $('#sidebar_toggle_icon');
    if (!btn.length || !img.length) { return; }
    var narrowSrc = btn.attr('data-rail-src-narrow');
    var widenSrc = btn.attr('data-rail-src-widen');
    if (!narrowSrc || !widenSrc) { return; }
    img.attr('src', isCollapsed ? widenSrc : narrowSrc);
  }

  var docNavFlyoutHoverLeaveTimer = null;

  // Keep in sync with `$window-medium-px` / Bootstrap `md` (see assets/css/main.scss).
  function isDocNavRailLayout() {
    return window.matchMedia('(min-width: 768px)').matches;
  }

  function syncDocNavDisclosureState() {
    var nav_bar = $('#nav_bar');
    var btn = $('#sidebar_toggle');
    if (!btn.length) { return; }
    var isCollapsed = nav_bar.hasClass('hide_sidebar');
    var flyoutOpen = nav_bar.hasClass('doc-nav-flyout-open');
    var collapseLabel = (typeof site_i18n !== 'undefined' && site_i18n['collapse_navigation']) ? site_i18n['collapse_navigation'] : 'Collapse navigation';
    var expandLabel = (typeof site_i18n !== 'undefined' && site_i18n['expand_navigation']) ? site_i18n['expand_navigation'] : 'Expand navigation';
    btn.attr('aria-label', isCollapsed ? expandLabel : collapseLabel);
    btn.attr('title', isCollapsed ? expandLabel : collapseLabel);
    var expanded = !isCollapsed || (isCollapsed && flyoutOpen);
    btn.attr('aria-expanded', expanded ? 'true' : 'false');
    var hint = $('#sidebar_toggle_flyout_hint');
    if (hint.length) {
      hint.prop('hidden', !isCollapsed);
      if (isCollapsed) {
        btn.attr('aria-describedby', 'sidebar_toggle_flyout_hint');
      } else {
        btn.removeAttr('aria-describedby');
      }
    }
  }

  function closeDocNavFlyout(closeMethod) {
    var nav_bar = $('#nav_bar');
    if (!nav_bar.hasClass('doc-nav-flyout-open')) { return; }
    logDocNavRailCustomEvent('doc_nav_flyout_closed', { close_method: closeMethod });
    nav_bar.removeClass('doc-nav-flyout-open');
    if (docNavFlyoutHoverLeaveTimer) {
      clearTimeout(docNavFlyoutHoverLeaveTimer);
      docNavFlyoutHoverLeaveTimer = null;
    }
    syncDocNavDisclosureState();
    requestAnimationFrame(function() { syncSidebarToggleDock(); });
  }

  function openDocNavFlyoutFromKeyboard() {
    if (!isDocNavRailLayout()) { return; }
    var nav_bar = $('#nav_bar');
    if (!nav_bar.hasClass('hide_sidebar') || nav_bar.hasClass('doc-nav-flyout-open')) { return; }
    nav_bar.addClass('doc-nav-flyout-open');
    logDocNavRailCustomEvent('doc_nav_flyout_opened', { open_method: 'keyboard' });
    syncDocNavDisclosureState();
    requestAnimationFrame(function() {
      syncSidebarToggleDock();
      var firstFocusable = $('#left_navmenu').find('a, button').filter(':visible').first();
      if (firstFocusable.length) {
        firstFocusable[0].focus();
      } else {
        var tgl = document.getElementById('sidebar_toggle');
        if (tgl) { tgl.focus(); }
      }
    });
  }

  // Move rail toggle between the collapsed rail slot and the expanded-nav position.
  // During flyout peek (hide_sidebar + doc-nav-flyout-open), the button stays in the
  // rail slot so it doesn't jump when the flyout opens.
  function syncSidebarToggleDock() {
    var nav_bar = $('#nav_bar');
    var host = $('#sidebar_toggle_host');
    var slot = $('.left-nav-collapsed-slot');
    var btn = $('#sidebar_toggle');
    if (!btn.length) { return; }
    if (nav_bar.hasClass('hide_sidebar')) {
      // Collapsed (with or without flyout peek): button stays in the rail slot.
      if (slot.length && !$.contains(slot[0], btn[0])) { btn.appendTo(slot); }
    } else {
      // Fully expanded: move button to the designated host or below the flyout panel.
      if (host.length) {
        btn.appendTo(host);
      } else {
        var primary = $('.left-nav-primary');
        var flyout = $('#doc_nav_flyout');
        if (primary.length && flyout.length) {
          btn.insertAfter(flyout);
        } else if (slot.length) {
          btn.appendTo(slot);
        }
      }
    }
  }

  $('#sidebar_toggle').on('keydown', function(e) {
    if (e.key !== 'ArrowDown') { return; }
    if (!isDocNavRailLayout()) { return; }
    var nav_bar = $('#nav_bar');
    if (!nav_bar.hasClass('hide_sidebar') || nav_bar.hasClass('doc-nav-flyout-open')) { return; }
    e.preventDefault();
    openDocNavFlyoutFromKeyboard();
  });

  document.addEventListener('keydown', function docNavFlyoutOnEscape(e) {
    if (e.key !== 'Escape') { return; }
    if (!isDocNavRailLayout()) { return; }
    var nav_bar = $('#nav_bar');
    if (!nav_bar.length || !nav_bar.hasClass('hide_sidebar') || !nav_bar.hasClass('doc-nav-flyout-open')) { return; }
    e.preventDefault();
    closeDocNavFlyout('escape');
    var t = document.getElementById('sidebar_toggle');
    if (t) { t.focus(); }
  }, true);

  $('#nav_bar').on('mouseenter.docNavFlyout', function() {
    if (!isDocNavRailLayout()) { return; }
    var nav_bar = $('#nav_bar');
    if (!nav_bar.hasClass('hide_sidebar')) { return; }
    var wasFlyoutOpen = nav_bar.hasClass('doc-nav-flyout-open');
    if (docNavFlyoutHoverLeaveTimer) {
      clearTimeout(docNavFlyoutHoverLeaveTimer);
      docNavFlyoutHoverLeaveTimer = null;
    }
    nav_bar.addClass('doc-nav-flyout-open');
    if (!wasFlyoutOpen) {
      logDocNavRailCustomEvent('doc_nav_flyout_opened', { open_method: 'hover' });
    }
    syncDocNavDisclosureState();
    syncSidebarToggleDock();
  });

  $('#nav_bar').on('mouseleave.docNavFlyout', function(e) {
    if (!isDocNavRailLayout()) { return; }
    var nav_bar = $('#nav_bar');
    if (!nav_bar.hasClass('doc-nav-flyout-open')) { return; }
    var to = e.relatedTarget;
    if (to && nav_bar[0].contains(to)) { return; }
    if (docNavFlyoutHoverLeaveTimer) { clearTimeout(docNavFlyoutHoverLeaveTimer); }
    docNavFlyoutHoverLeaveTimer = setTimeout(function() {
      docNavFlyoutHoverLeaveTimer = null;
      var nb = $('#nav_bar');
      if (!nb.hasClass('doc-nav-flyout-open')) { return; }
      var ae = document.activeElement;
      if (ae && nb[0].contains(ae)) { return; }
      closeDocNavFlyout('mouse_leave');
    }, 200);
  });

  $('#sidebar_toggle').click(function(e){
    e.preventDefault();
    e.stopPropagation();
    if (!isDocNavRailLayout()) { return; }
    var nav_bar = $('#nav_bar');
    var curstate = nav_bar.hasClass('hide_sidebar');
    if (curstate) {
      if (nav_bar.hasClass('doc-nav-flyout-open')) {
        logDocNavRailCustomEvent('doc_nav_flyout_closed', { close_method: 'sidebar_expanded' });
      }
      logDocNavRailCustomEvent('expand_nav_clicked');
      nav_bar.removeClass('doc-nav-flyout-open');
      nav_bar.removeClass('hide_sidebar');
      Cookies.set('ln', '', { expires: 365 });
    } else {
      if (nav_bar.hasClass('doc-nav-flyout-open')) {
        logDocNavRailCustomEvent('doc_nav_flyout_closed', { close_method: 'sidebar_collapsed' });
      }
      logDocNavRailCustomEvent('collapse_nav_clicked');
      nav_bar.removeClass('doc-nav-flyout-open');
      nav_bar.addClass('hide_sidebar');
      Cookies.set('ln','1',  { expires: 365 });
    }
    setSidebarToggleIcon(nav_bar.hasClass('hide_sidebar'));
    syncDocNavDisclosureState();
    syncSidebarToggleDock();
  });
  // Pinned collapsed state uses cookie `ln` only (no URL param). Synthetic click avoided so layout/ARIA stay in sync on first paint.
  if (Cookies.get('ln')) {
    var nav_barInit = $('#nav_bar');
    nav_barInit.addClass('hide_sidebar');
    setSidebarToggleIcon(true);
  }
  syncSidebarToggleDock();
  syncDocNavDisclosureState();

  $(window).on('resize.docNavRail', function() {
    if (!isDocNavRailLayout()) {
      closeDocNavFlyout('viewport_resize');
    }
    syncSidebarToggleDock();
  });

  // Keep collapse containers out of tab order; section caret buttons stay focusable (GitLab-style)
  function setNavCollapseTabindex() {
    $('#left_navmenu .collapse').attr('tabindex', '-1');
  }
  setNavCollapseTabindex();
  $(document).on('shown.bs.collapse', '#left_navmenu .collapse', setNavCollapseTabindex);

  // Update nav section caret icon and aria-label when expand/collapse (GitLab-style)
  $(document).on('shown.bs.collapse', '#left_navmenu .collapse', function() {
    var id = $(this).attr('id');
    var $btn = $('#left_navmenu button[data-target="#' + $.escapeSelector(id) + '"]');
    if (!$btn.length) { return; }
    $btn.attr('aria-expanded', 'true');
    $btn.each(function() {
      var collapseLabel = $(this).attr('data-collapse-label');
      if (collapseLabel) { $(this).attr('aria-label', collapseLabel); }
    });
    $btn.filter('.nav_toggle').find('i.fas').removeClass('fa-chevron-right').addClass('fa-chevron-down');
  });
  $(document).on('hidden.bs.collapse', '#left_navmenu .collapse', function() {
    var id = $(this).attr('id');
    var $btn = $('#left_navmenu button[data-target="#' + $.escapeSelector(id) + '"]');
    if (!$btn.length) { return; }
    $btn.attr('aria-expanded', 'false');
    $btn.each(function() {
      var expandLabel = $(this).attr('data-expand-label');
      if (expandLabel) { $(this).attr('aria-label', expandLabel); }
    });
    $btn.filter('.nav_toggle').find('i.fas').removeClass('fa-chevron-down').addClass('fa-chevron-right');
  });

  function runMermaidCharts() {
    if (typeof mermaid === 'undefined') {
      return;
    }

    var mermaid_charts = $('.language-mermaid').not('[data-processed="true"]').filter(':visible');
    if (!mermaid_charts.length) {
      return;
    }

    mermaid.run({ nodes: mermaid_charts });
    setPanZoom(mermaid_charts);
  }

  function setPanZoom(mermaid_charts){
    setTimeout(function() {
      mermaid_charts.each(function() {
        var container = this;
        var svg_element = $(container).find('svg').first();
        if (svg_element && svg_element.length) {
          const height = svg_element.outerHeight();
          const width = svg_element.outerWidth();
          // Attach the fullscreen button BEFORE svg-pan-zoom initializes — it strips
          // the SVG's viewBox attribute, which we need to clone for the modal.
          attachFullscreenButton(container, svg_element[0]);
          window[svg_element.attr('id')] = svgPanZoom(`#${svg_element.attr('id')}`, {
            zoomEnabled: true,
            controlIconsEnabled: true,
            fit: false,
            contain: true,
            center: true,
            minZoom: 0.1,
            viewportSelector: `#${svg_element.attr('id')}`
          });
          svg_element.height(height)
          svg_element.attr('dim_ratio', height/width);
          window[svg_element.attr('id')].resize();
        }
      });
    }, 500);
  }

  // ---- Mermaid fullscreen modal ---------------------------------------------
  // Adds a "Fullscreen" button to each rendered mermaid chart. Clicking opens
  // the SVG in a viewport-sized modal with its own svg-pan-zoom instance
  // (operates on a clone, so the inline +/- control is unaffected).
  var FS_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8V3h5M21 8V3h-5M3 16v5h5M21 16v5h-5"/></svg>';
  var fsModal, fsModalStage, fsModalTitle, fsActiveZoom, fsLastTrigger;

  function deriveDiagramTitle(container) {
    if (container.dataset && container.dataset.diagramTitle) {
      return container.dataset.diagramTitle;
    }
    var node = container.previousElementSibling;
    while (node) {
      if (/^H[1-6]$/.test(node.tagName)) return (node.textContent || '').trim();
      node = node.previousElementSibling;
    }
    return 'Diagram';
  }

  function attachFullscreenButton(container, svg) {
    if (!container || !svg) return;
    if (container.dataset.mermaidFsEnhanced === '1') return;
    // svg-pan-zoom in the modal needs a viewBox to render correctly. Stash it
    // on the container before the inline svg-pan-zoom strips it from the SVG.
    var viewBox = svg.getAttribute('viewBox');
    if (!viewBox) return;
    container.dataset.mermaidFsEnhanced = '1';
    container.dataset.mermaidViewbox = viewBox;
    container.classList.add('mermaid-figure');

    var title = deriveDiagramTitle(container);
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'mermaid-figure__fullscreen-btn';
    btn.innerHTML = FS_ICON + '<span>Fullscreen</span>';
    btn.setAttribute('aria-label', 'View diagram "' + title + '" fullscreen');
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      openFullscreenModal(svg, title, btn, container.dataset.mermaidViewbox);
    });
    container.appendChild(btn);
  }

  function buildFullscreenModal() {
    fsModal = document.createElement('div');
    fsModal.className = 'mermaid-modal';
    fsModal.setAttribute('role', 'dialog');
    fsModal.setAttribute('aria-modal', 'true');
    fsModal.setAttribute('aria-label', 'Fullscreen diagram viewer');
    fsModal.innerHTML =
      '<div class="mermaid-modal__header">' +
        '<div>' +
          '<span class="mermaid-modal__title"></span>' +
          '<span class="mermaid-modal__hint">Scroll to zoom &middot; drag to pan &middot; +/&minus; keys &middot; 0 to reset &middot; Esc to close</span>' +
        '</div>' +
        '<button type="button" class="mermaid-modal__close" aria-label="Close fullscreen view">Close</button>' +
      '</div>' +
      '<div class="mermaid-modal__stage"></div>';
    document.body.appendChild(fsModal);
    fsModalStage = fsModal.querySelector('.mermaid-modal__stage');
    fsModalTitle = fsModal.querySelector('.mermaid-modal__title');

    fsModal.querySelector('.mermaid-modal__close').addEventListener('click', closeFullscreenModal);
    fsModal.addEventListener('click', function(e) {
      if (e.target === fsModal || e.target === fsModalStage) closeFullscreenModal();
    });
    document.addEventListener('keydown', onFullscreenKeydown);
  }

  function onFullscreenKeydown(e) {
    if (!fsModal || !fsModal.classList.contains('is-open')) return;
    if (e.key === 'Escape') { closeFullscreenModal(); return; }
    if (e.key === 'Tab') {
      // Trap focus within the modal.
      var focusables = fsModal.querySelectorAll('button');
      if (!focusables.length) return;
      var first = focusables[0];
      var last = focusables[focusables.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        last.focus(); e.preventDefault();
      } else if (!e.shiftKey && document.activeElement === last) {
        first.focus(); e.preventDefault();
      }
      return;
    }
    if (!fsActiveZoom) return;
    if (e.key === '+' || e.key === '=') { fsActiveZoom.zoomIn(); e.preventDefault(); }
    else if (e.key === '-' || e.key === '_') { fsActiveZoom.zoomOut(); e.preventDefault(); }
    else if (e.key === '0') { fsActiveZoom.resetZoom(); fsActiveZoom.center(); e.preventDefault(); }
  }

  function openFullscreenModal(svg, title, trigger, viewBox) {
    if (!fsModal) buildFullscreenModal();
    fsLastTrigger = trigger;
    fsModalTitle.textContent = title || 'Diagram';

    var clone = svg.cloneNode(true);
    // Strip inline sizing so the modal can size the SVG to its stage.
    clone.removeAttribute('style');
    clone.removeAttribute('height');
    clone.removeAttribute('width');
    // Restore the viewBox the inline svg-pan-zoom stripped from the source SVG.
    if (viewBox && !clone.getAttribute('viewBox')) {
      clone.setAttribute('viewBox', viewBox);
    }
    // Strip pan-zoom's transform from the cloned viewport group, otherwise
    // the modal opens with the source diagram's current zoom/pan baked in.
    var clonedViewport = clone.querySelector('.svg-pan-zoom_viewport');
    if (clonedViewport) {
      clonedViewport.removeAttribute('transform');
      clonedViewport.removeAttribute('style');
    }
    // Remove any control-icon overlay the inline pan-zoom injected.
    var controlIcons = clone.querySelector('#svg-pan-zoom-controls');
    if (controlIcons && controlIcons.parentNode) {
      controlIcons.parentNode.removeChild(controlIcons);
    }
    // Keep the original SVG id on the clone — Mermaid scopes its injected
    // <style> block by id (e.g. `#mermaid-123 .label { fill: ... }`), so
    // renaming would strip all the diagram's text/edge colors. svg-pan-zoom
    // accepts an element reference directly, so a duplicate id is harmless.
    fsModalStage.innerHTML = '';
    fsModalStage.appendChild(clone);

    fsModal.classList.add('is-open');
    document.body.classList.add('mermaid-modal-open');

    requestAnimationFrame(function() {
      try {
        fsActiveZoom = svgPanZoom(clone, {
          zoomEnabled: true,
          controlIconsEnabled: false,
          fit: true,
          center: true,
          minZoom: 0.2,
          maxZoom: 20,
          zoomScaleSensitivity: 0.35
        });
      } catch (err) {
        if (window.console) console.warn('mermaid fullscreen: svg-pan-zoom init failed', err);
      }
      var closeBtn = fsModal.querySelector('.mermaid-modal__close');
      if (closeBtn) closeBtn.focus();
    });
  }

  function closeFullscreenModal() {
    if (!fsModal) return;
    if (fsActiveZoom) {
      try { fsActiveZoom.destroy(); } catch (_) {}
      fsActiveZoom = null;
    }
    fsModal.classList.remove('is-open');
    document.body.classList.remove('mermaid-modal-open');
    if (fsModalStage) fsModalStage.innerHTML = '';
    if (fsLastTrigger && typeof fsLastTrigger.focus === 'function') {
      fsLastTrigger.focus();
    }
  }
  // ---- end mermaid fullscreen modal -----------------------------------------
  // Resize svg with dim_ration on window resize
  $(window).on('resize', function() {
    $('.language-mermaid').filter('[data-processed="true"]').each(function() {
      const svg_element = $(this).find('svg').first();
      const dimRatio = parseFloat(svg_element.attr('dim_ratio'));
      if (!isNaN(dimRatio)) {
        const newWidth = svg_element.outerWidth();
        const newHeight = newWidth * dimRatio;
        if (newHeight > 0) {
          svg_element.height(newHeight);
          window[svg_element.attr('id')].resize();
        }
      }
    });
  });


  function setTabClass(tabtype, prefix, postfix, curtab){
    var tab_selecter = '.' + tabtype + prefix +'tab_toggle_ul.' + tabtype + 'ab-' + prefix +'nav-' + prefix +'tabs';
    var content_selecter ='div.' + tabtype + prefix +'tab_toggle_div';

    var last_active_tab = {};
    var last_active_content = {};
    $(tab_selecter).each(function (k,v) {
      var el = $(v);
      var li = el.children('li')
      var last_active = li.filter('.' + prefix + 'active');
      if (last_active.length) {
        last_active_tab[el.attr('id')] = last_active.first().attr('id');
      }
      else {
        last_active_tab[el.attr('id')] = li.first().attr('id');
      }
    });

    $(content_selecter).each(function (k,v) {
      var el = $(v);
      var div = el.children('div')
      var last_active = div.filter('.' + tabtype + 'ab-' + prefix + 'tab-pane ' +  prefix + 'active');
      if (last_active.length) {
        last_active_content[el.attr('id')] = last_active.first().attr('id');
      }
      else {
        last_active_content[el.attr('id')] = div.first().attr('id');
      }
    });

    $(tab_selecter + ' li').removeClass(prefix + 'active');
    $(tab_selecter + ' li.' + curtab).addClass(prefix + 'active');
    $(content_selecter + ' div.' + tabtype + 'ab-' + prefix + 'tab-pane').removeClass(prefix + 'active');
    $('div.' + tabtype + prefix +'tab_toggle_div div.' + curtab + postfix).addClass(prefix + 'active');

    $(tab_selecter).each(function (k,v) {
      var el = $(v);
      var li = el.children('li')
      var last_active = li.filter('.' + prefix + 'active');
      if (!last_active.length) {
        $('#' + last_active_tab[el.attr('id')]).addClass(prefix + 'active');
      }
    });
    $(content_selecter).each(function (k,v) {
      var el = $(v);
      var div = el.children('div')
      var last_active = div.filter('.' + tabtype + 'ab-' + prefix + 'tab-pane.' +  prefix + 'active');
      if (!last_active.length) {
        $('#' + last_active_content[el.attr('id')]).addClass(prefix + 'active');
      }
    });
    // Refresh Toc
    $('#toc').toc({
      headers:  ((typeof toc_headers != 'undefined') ? toc_headers : "h2,h3"),
      minimumHeaders: ((typeof toc_minheaders != 'undefined') ? toc_minheaders : 2),
    });
  }

  function setTabOnlyClass(tabtype, prefix, postfix, partab, curtab){
    $('#' + partab + '_nav li').removeClass(prefix + 'active');
    $('#' + partab + '_nav li.' + curtab).addClass(prefix + 'active');
    $('#' + partab + ' div.' + tabtype + 'ab-' + prefix + 'tab-pane').removeClass(prefix + 'active');
    $('#' + partab + ' div.' + curtab + postfix).addClass(prefix + 'active');
  }

  // Sync aria-selected and roving tabindex on all [role="tablist"] from active <li> state.
  // Called after every tab-switch (click handler or initialization).
  function syncTabAriaFromActiveClass() {
    $('ul[role="tablist"]').each(function() {
      $(this).find('li').each(function() {
        var isActive = $(this).hasClass('active') || $(this).hasClass('sub_active');
        $(this).find('[role="tab"]').each(function() {
          $(this).attr('aria-selected', isActive ? 'true' : 'false');
          $(this).attr('tabindex', isActive ? '0' : '-1');
        });
      });
    });
  }

  // Arrow-key navigation between tabs within a tablist (WAI-ARIA tabs pattern).
  $(document).on('keydown', 'ul[role="tablist"] [role="tab"]', function(e) {
    var $tabs = $(this).closest('ul[role="tablist"]').find('[role="tab"]');
    var currentIndex = $tabs.index(this);
    var nextIndex;

    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
      e.preventDefault();
      nextIndex = (currentIndex + 1) % $tabs.length;
    } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
      e.preventDefault();
      nextIndex = (currentIndex - 1 + $tabs.length) % $tabs.length;
    } else if (e.key === 'Home') {
      e.preventDefault();
      nextIndex = 0;
    } else if (e.key === 'End') {
      e.preventDefault();
      nextIndex = $tabs.length - 1;
    } else {
      return;
    }

    $tabs.eq(nextIndex).focus().trigger('click');
  });

  // Updated Tab switcher
  $('.tab_toggle, .sdk-tab_toggle').click(function(e){
    e.preventDefault();
    var $this = $(this);
    var tabtype = $this.attr("class").includes('sdk-') ? 'sdk-' : '';
    var curtab = $this.attr('data-' + tabtype  + 'tab');
    var tabstate = $this.attr("class").includes('sdk-') ? 'sdktab' : 'tab';
    setTabClass(tabtype,'', '_tab', curtab);
    setTabState($this.text(), tabstate);
    syncTabAriaFromActiveClass();
  });

  $('.tab_toggle_only, .sdk-tab_toggle_only').click(function(e){
    e.preventDefault();

    var $this = $(this);
    var tabtype = $this.attr("class").includes('sdk-') ? 'sdk-' : '';
    var curtab = $this.attr('data-' + tabtype + 'tab');
    var partab = $this.attr('data-' + tabtype + 'tab-target');
    var tabstate = $this.attr("class").includes('sdk-') ? 'sdktab' : 'tab';
    setTabOnlyClass(tabtype,'','_tab', partab, curtab);
    setTabState($this.text(), tabstate);
    syncTabAriaFromActiveClass();
  });

  $('.sub_tab_toggle, .sub_sdk-tab_toggle').click(function(e){
    e.preventDefault();
    var $this = $(this);
    var tabtype = $this.attr("class").includes('sdk-') ? 'sdk-' : '';
    var curtab = $this.attr('data-' + tabtype + 'sub_tab');
    var tabstate = $this.attr("class").includes('sdk-') ? 'sdksubtab' : 'subtab';

    setTabClass('','sub_', '', curtab);
    setTabState($this.text(), tabstate);
    syncTabAriaFromActiveClass();
  });

  $('.sub_tab_toggle_only, .sub_sdk-tab_toggle_only').click(function(e){
    e.preventDefault();

    var $this = $(this);
    var tabtype = $this.attr("class").includes('sdk-') ? 'sdk-' : '';
    var curtab = $this.attr('data-' + tabtype + 'sub_tab');
    var partab = $this.attr('data-' + tabtype + 'sub_tab-target');
    var tabstate = $this.attr("class").includes('sdk-') ? 'sdksubtab' : 'subtab';

    setTabOnlyClass(tabtype,'sub_','', partab, curtab);
    setTabState($this.text(), tabstate);
    syncTabAriaFromActiveClass();
  });

  let tab_query = (new URLSearchParams(window.location.search).get('tab') || '').replace('_sub_tab','');
  let sub_tab_query = (new URLSearchParams(window.location.search).get('subtab') || '').replace('_sub_tab','');
  let sdk_tab_query = (new URLSearchParams(window.location.search).get('sdktab') || '').replace('_sub_tab','');
  let sdk_sub_tab_query = (new URLSearchParams(window.location.search).get('sdksubtab') || '').replace('_sub_tab','');

  // if tab is set via param or cookied, activate tab
  $('.tab_toggle, .sdk-tab_toggle').each(function(e,v){
    var $this = $(v);
    var tabtype = $this.attr("class").includes('sdk-') ? 'sdk-' : '';
    var curtab = $this.attr('data-' + tabtype + 'tab');
    var curtab_name = $this.text().toLowerCase();

    if ((tab_query && (tab_query == curtab_name)) || (sdk_tab_query && (sdk_tab_query == curtab_name))){
      setTabClass(tabtype,'', '_tab', curtab)
    }
    else if (tab_track[curtab_name]){
      if (tabtype == 'sdk-') {
        let tab_cookie = Cookies.get('sdktab') || '';
        if (tab_cookie && (curtab_name == tab_cookie)) {
          setTabClass(tabtype,'', '_tab', curtab)
        }
      }
      else {
        let tab_cookie = Cookies.get(tab_track[curtab_name]) || '';
        if (tab_cookie && (curtab_name == tab_cookie)) {
          setTabClass(tabtype,'', '_tab', curtab)
        }
        else {
          $('#toc').toc({
            headers:  ((typeof toc_headers != 'undefined') ? toc_headers : "h2,h3"),
            minimumHeaders: ((typeof toc_minheaders != 'undefined') ? toc_minheaders : 2),
          });
        }
      }
    }

  });

  $('.tab_toggle_only, .sdk-tab_toggle_only').each(function(e,v){
    var $this = $(v);
    var tabtype = $this.attr("class").includes('sdk-') ? 'sdk-' : '';
    var curtab = $this.attr('data-' + tabtype + 'tab');
    var partab = $this.attr('data-' + tabtype + 'tab-target');
    var curtab_name = $this.text().toLowerCase();
    if ((tab_query && (tab_query == curtab_name)) || (sdk_tab_query && (sdk_tab_query == curtab_name))){
      setTabOnlyClass(tabtype,'', '_tab', partab, curtab)
    }
    if (tab_track[curtab_name]){
      if (tabtype == 'sdk-') {
        let tab_cookie = Cookies.get('sdktab') || '';
        if (tab_cookie && (curtab_name == tab_cookie)) {
          setTabClass(tabtype,'', '_tab', partab, curtab)
        }
      }
      else {
        let tab_cookie = Cookies.get(tab_track[curtab_name]) || '';
        if (tab_cookie && (curtab_name == tab_cookie)) {
          setTabClass(tabtype,'', '_tab', partab,  curtab)
        }
        else {
          $('#toc').toc({
            headers:  ((typeof toc_headers != 'undefined') ? toc_headers : "h2,h3"),
            minimumHeaders: ((typeof toc_minheaders != 'undefined') ? toc_minheaders : 2),
          });
        }
      }
    }
  });

  $('.sub_tab_toggle, .sub_sdk-tab_toggle').each(function(e,v){
    var $this = $(v);
    var tabtype = $this.attr("class").includes('sdk-') ? 'sdk' : '';
    var curtab = $this.attr('data-' + tabtype + 'sub_tab');
    var curtab_name = $this.text().toLowerCase();
    if ((tab_query && (tab_query == curtab_name)) ||
      (sub_tab_query && (sub_tab_query == curtab_name))
      ){
      setTabClass(tabtype,'sub_','', curtab)
    }
    else if (tab_track[curtab_name]){
      if (tabtype == 'sdk-') {
        let tab_cookie = Cookies.get('sdksubtab') || '';
        if (tab_cookie && (curtab_name == tab_cookie)) {
          setTabClass(tabtype,'sub_','', curtab)
        }
      }
      else {
        let tab_cookie = Cookies.get(tab_track[curtab_name]) || '';
        if (tab_cookie && (curtab_name == tab_cookie)) {
          setTabClass(tabtype,'sub_','', curtab)
        }
      }
    }
  });

  $('.sub_tab_toggle_only, .sub_sdk-tab_toggle_only').each(function(e,v){
    var $this = $(v);
    var curtab_name = $this.text().toLowerCase();
    var tabtype = $this.attr("class").includes('sdk-') ? 'sdk' : '';

    var curtab = $this.attr('data-' + tabtype + 'sub_tab');
    var partab = $this.attr('data-' + tabtype + 'sub_tab-target');

    if ((tab_query && (tab_query == curtab_name)) ||
      (sub_tab_query && (sub_tab_query == curtab_name))
      ){
      setTabOnlyClass(tabtype,'sub_','', partab, curtab)
    }
    else if (tab_track[curtab_name]){
      if (tabtype == 'sdk-') {
        let tab_cookie = Cookies.get('sdksubtab') || '';
        if (tab_cookie && (curtab_name == tab_cookie)) {
          setTabClass(tabtype,'sub_','',partab, curtab)
        }
      }
      else {
        let tab_cookie = Cookies.get(tab_track[curtab_name]) || '';
        if (tab_cookie && (curtab_name == tab_cookie)) {
          setTabClass(tabtype,'sub_','',partab, curtab)
        }
      }
    }
  });


  // Ensure aria-selected and tabindex reflect whichever tabs were activated by URL params or cookies.
  syncTabAriaFromActiveClass();

  String.prototype.upCaseWord = function() {
    return this.toString().replace(/\b\w/g, function(l){ return l.toUpperCase() });
  };
  String.prototype.replaceUnder = function() {
    return this.toString().replace(/\%20/g, ' ').replace(/\_/g, ' ');
  };
  Array.prototype.replaceUnder = function() {
    return this.map(function(itm){ return itm.toString().replace(/\%20/g, ' ').replace(/\_/g, ' ')});
  };
  Array.prototype.upCaseWord = function() {
    return this.map(function(itm){ return itm.toString().replace(/\b\w/g, function(l){ return l.toUpperCase() }) });
  };

  var external_ignore = ['braze.statuspage.io','www.braze.com']
  $('#main_content a').filter(function() {
    var is_external = this.hostname && this.hostname !== location.hostname && this.text && external_ignore.indexOf(this.hostname) < 0 ;
    if ($(this).hasClass('extignore')) {
      is_external = false;
    }
    else if ($(this).has('img').length > 0) {
      if ($(this).has('img')[0].childNodes.length > 0) {
       is_external = false;
      }
    }
    else if ($(this).has('div').length >0 ) {
      is_external = false;
    }

    var punctuations = ['.','!','?'];
    var has_punchtuation = false;
    var punctuation = null;
    if ($(this)[0]) {
      if ($(this)[0].nextSibling){
        punctuation = ($(this)[0].nextSibling.nodeValue || '').substr(0,1);
        if (punctuations.includes(punctuation)) {
          $(this)[0].nextSibling.nodeValue = ($(this)[0].nextSibling.nodeValue || '').substring(1);
          has_punchtuation = true;
        }
      }
    }

    if (is_external || has_punchtuation){
      $(this).wrap('<span class="inline-link">');
    }

    if (has_punchtuation){
      $(this).after(punctuation);
    }
    if (is_external){
      $(this).after(' <i class="fas fa-external-link-alt"></i>');
      $(this).attr('target', '_blank');
      $(this).attr('rel', function(_, rel) {
        var tokens = (rel || '').split(/\s+/).filter(Boolean);
        if (tokens.indexOf('noopener') < 0) { tokens.push('noopener'); }
        if (tokens.indexOf('noreferrer') < 0) { tokens.push('noreferrer'); }
        return tokens.join(' ');
      });
    }
  });
  // T7: add rel and sr-only warning to all target="_blank" links (static + dynamic).
  // Uses native DOM (not jQuery) so it works on both regular DOM and Shadow DOM roots.
  function patchNewWindowLinks(root) {
    var links = root.querySelectorAll ? Array.prototype.slice.call(root.querySelectorAll('a[target="_blank"]')) : [];
    if (root.nodeName === 'A' && root.getAttribute && root.getAttribute('target') === '_blank') {
      links.push(root);
    }
    links.forEach(function(a) {
      var tokens = (a.getAttribute('rel') || '').split(/\s+/).filter(Boolean);
      if (tokens.indexOf('noopener') < 0) { tokens.push('noopener'); }
      if (tokens.indexOf('noreferrer') < 0) { tokens.push('noreferrer'); }
      a.setAttribute('rel', tokens.join(' '));
      var ariaLabel = a.getAttribute('aria-label');
      if (ariaLabel) {
        // aria-label overrides all text content in the accessible name computation,
        // so the sr-only span inside the link will be ignored. Append the warning
        // directly to aria-label instead.
        if (ariaLabel.indexOf('(opens in new tab)') < 0) {
          a.setAttribute('aria-label', ariaLabel.trim() + ' (opens in new tab)');
        }
      } else if (!a.querySelector('.sr-only')) {
        var span = document.createElement('span');
        span.className = 'sr-only';
        span.textContent = ' (opens in new tab)';
        a.appendChild(span);
      }
    });
  }

  // SearchUnify's full-page search widget (<su-app>) uses Shadow DOM, so we must
  // also observe its shadow root to patch links injected there.
  function watchShadowRoot(el) {
    if (el.shadowRoot) {
      t7Observer.observe(el.shadowRoot, { childList: true, subtree: true });
      patchNewWindowLinks(el.shadowRoot);
    } else {
      var attempts = 0;
      var poll = setInterval(function() {
        if (el.shadowRoot || ++attempts > 50) {
          clearInterval(poll);
          if (el.shadowRoot) {
            t7Observer.observe(el.shadowRoot, { childList: true, subtree: true });
            patchNewWindowLinks(el.shadowRoot);
          }
        }
      }, 100);
    }
  }

  patchNewWindowLinks(document.body);
  var t7Observer = new MutationObserver(function(mutations) {
    for (var i = 0; i < mutations.length; i++) {
      var added = mutations[i].addedNodes;
      for (var j = 0; j < added.length; j++) {
        var node = added[j];
        if (node.nodeType !== 1) { continue; }
        patchNewWindowLinks(node);
        if (node.nodeName === 'SU-APP') { watchShadowRoot(node); }
        var suApps = node.querySelectorAll ? node.querySelectorAll('su-app') : [];
        for (var k = 0; k < suApps.length; k++) { watchShadowRoot(suApps[k]); }
      }
    }
  });
  t7Observer.observe(document.body, { childList: true, subtree: true });
  // Handle su-app already present at load time (e.g. on the /search/ page)
  var suAppEl = document.querySelector('su-app');
  if (suAppEl) { watchShadowRoot(suAppEl); }
  $('.highlight .highlight .rouge-code pre').each(function(k) {
    $this = $(this);
    if ($this.html().length > 120) {
      $this.css('min-height','36px');
    }
    var lines = $this.text().split("\n");
    if (lines.length <= 2) {
      $this.addClass('prewrap');
    }
  });

  $('.lang-select').on('change', function(e){
    let lang = this.value;
    let path = window.location.pathname;
    let query_str = window.location.search;
    let path_lang = (path.split('/') || [])[2];
    let lang_re = new RegExp(`\/docs\/?`);
    // if url has a 2 char language identifier, replace the identifier
    if (path_lang == page_language){
      lang_re = new RegExp(`\/docs\/${page_language}\/?`);
    }
    window.location.href = path.replace(lang_re,`\/docs\/${lang}\/`);
  });

  $('.lang-select').each(function(ind) {
    $(this).val(page_language).prop('selected', true);
  });

  $('[role="tablist"]').each(function(){
    if (!$(this).attr('tabindex')) {
      $(this).attr('tabindex', 0)
    }
  });
  setAdaTableRole();

  // intialized mermaid
  if (typeof mermaid !== 'undefined') {
    mermaid.initialize({
      startOnLoad: false,
      theme: "default",
    });
    runMermaidCharts();
  }


});
