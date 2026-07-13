// https://github.com/ghiculescu/jekyll-table-of-contents
// Modified to generate nav tags for bootstrap 4.1 scrollspy
(function($){
  $.fn.toc = function(options) {
    var defaults = {
      noBackToTopLinks: true,
      minimumHeaders: 3,
      headers: 'h1, h2, h3, h4, h5, h6',
      listType: 'ul', // nested sub-lists only; outer wrapper is a single <nav>
      listPrefix: 'toc_',
      showEffect: 'fadeIn', // values: [show|slideDown|fadeIn|none]
      showSpeed: 'fast', // set to 0 to deactivate effect
      toc_header: `${ site_i18n['page_nav_title'] || "On this page"}...`,
      toc_header_class: 'toc_header',
      toc_container_class: 'toc_container',
      toc_item_class: 'nav_item',
      toc_link_class: 'nav-link',
      bootstrapStyling: ' class="nav"' // appended to each nested list element
    },
    settings = $.extend(defaults, options);

    var headers = $(settings.headers).filter(function() {
      // get all headers with an ID
      var previousSiblingName = $(this).prev().attr( "name" );
      if (!this.id && previousSiblingName) {
        this.id = $(this).attr( "id", previousSiblingName.replace(/\./g, "-") );
      }
      if ($(this).html().length == 0 || !$(this).is(":visible")) {
        return false;
      }
      return this.id;
    }), output = $(this);
    if (!headers.length || headers.length < settings.minimumHeaders || !output.length) {
      return;
    }

    if (0 === settings.showSpeed) {
      settings.showEffect = 'none';
    }

    var render = {
      show: function() { output.hide().html(html).show(settings.showSpeed); },
      slideDown: function() { output.hide().html(html).slideDown(settings.showSpeed); },
      fadeIn: function() { output.hide().html(html).fadeIn(settings.showSpeed); },
      none: function() { output.html(html); }
    };

    var get_level = function(ele) {
      var lvl = 1
      if (ele.nodeName.substring(0,1) == 'H')  {
        lvl = parseInt(ele.nodeName.replace("H", ""), 10);
      }
      return lvl;
    }
    var highest_level = headers.map(function(_, ele) { return get_level(ele); }).get().sort()[0];
    var return_to_top = '<i class="icon-arrow-up back-to-top"> </i>';

    var tocRootLevel = highest_level;
    var level = get_level(headers[0]),
      this_level,
      openUlDepth = 0,
      openLiCount = 0,
      pendingLinkLi = false,
      tocTitle = settings.toc_header.replace(/\.\.\.$/, ''),
      html = "<nav class='nav' aria-labelledby='toc-heading'>" +
        "<h2 id='toc-heading' class='" + settings.toc_header_class + "'>" + tocTitle + "</h2>" +
        "<div class='" + settings.toc_container_class + "'>";

    function linkHtml(header) {
      return "<a class='" + settings.toc_link_class + "' href='#" + header.id + "' id='" + settings.listPrefix + header.id + "'>" + header.innerHTML + "</a>";
    }

    function closeLi() {
      if (openLiCount > 0) {
        html += "</li>";
        openLiCount--;
        pendingLinkLi = false;
      }
    }

    function openUl() {
      html += "<" + settings.listType + settings.bootstrapStyling + ">";
      openUlDepth++;
    }

    function closeUl() {
      html += "</" + settings.listType + ">";
      openUlDepth--;
    }

    function ulDepthForLevel(headingLevel) {
      return Math.max(0, headingLevel - tocRootLevel);
    }

    function closeToUlDepth(targetDepth) {
      while (openUlDepth > targetDepth) {
        closeLi();
        closeUl();
      }
    }

    function openToUlDepth(targetDepth) {
      while (openUlDepth < targetDepth) {
        if (openUlDepth === 0) {
          openUl();
        } else if (pendingLinkLi) {
          // Nest the next sub-list inside the open item (e.g. H3 -> H4).
          openUl();
          pendingLinkLi = false;
        } else {
          // Skipped heading levels need a structural <li> wrapper per depth.
          html += "<li>";
          openLiCount++;
          openUl();
        }
      }
    }

    function renderEntry(header) {
      if (get_level(header) <= tocRootLevel) {
        // Top-level entries stay in div wrappers to preserve scrollspy highlight behavior.
        html += "<div>" + linkHtml(header) + "</div> ";
        pendingLinkLi = false;
        return;
      }
      html += "<li>" + linkHtml(header);
      openLiCount++;
      pendingLinkLi = true;
    }

    headers.on('click', function() {
      if (!settings.noBackToTopLinks) {
        window.location.hash = this.id;
      }
    })
    .addClass('clickable-header')
    .each(function(_, header) {
      this_level = get_level(header);
      if (!settings.noBackToTopLinks && this_level === highest_level) {
        $(header).addClass('top-level-header').after(return_to_top);
      }
      // Top-level items use div wrappers; nested sub-lists use valid ul > li > ul nesting.
      var targetUlDepth = ulDepthForLevel(this_level);
      if (this_level < level) {
        closeToUlDepth(targetUlDepth);
        if (this_level > tocRootLevel) {
          closeLi();
        }
      } else if (this_level === level) {
        closeToUlDepth(targetUlDepth);
        if (this_level > tocRootLevel) {
          closeLi();
        }
      } else {
        openToUlDepth(targetUlDepth);
      }
      // First nested entry when headers[0] is below tocRootLevel (e.g. H3 before H2).
      if (this_level > tocRootLevel && openUlDepth < targetUlDepth) {
        openToUlDepth(targetUlDepth);
      }
      renderEntry(header);
      level = this_level; // update for the next one
    });
    closeToUlDepth(0);
    html += "</div></nav>";
    if (!settings.noBackToTopLinks) {
      $(document).on('click', '.back-to-top', function() {
        $(window).scrollTop(0);
        window.location.hash = '';
      });
    }

    render[settings.showEffect]();
  };
})(jQuery);
