$(document).ready(function() {

  var breadcrumb = $('#breadcrumb');
  if (breadcrumb.length) {
    var curpage = $('#left_navmenu .nav-item.active');
    var current_page_text = curpage.text().trim();
    var bc_items = [];
    var bc_link = '';
    var curtext = '';
    var dataparent = curpage.attr('data-parent');

    while (dataparent) {
      curpage = $('#' + dataparent);
      curtext = curpage.text().trim();
      if (curtext) {
        bc_link = curpage.find('.nav_link');
        var li = $('<li>');
        if (bc_link.length && bc_link[0].href) {
          $('<a>').attr('href', bc_link[0].href).text(curtext).appendTo(li);
        } else {
          li.append(document.createTextNode(curtext));
        }
        $('<span>').attr('aria-hidden', 'true').html('&nbsp; &gt; &nbsp;').appendTo(li);
        bc_items.unshift(li);
      }
      dataparent = curpage.attr('data-parent');
    }

    if (current_page_text.length || bc_items.length) {
      if (page_collection_title) {
        var collection_li = $('<li>');
        $('<a>').attr('href', base_url + '/' + page_collection + '/' + page_collection_default_path).text(page_collection_title).appendTo(collection_li);
        $('<span>').attr('aria-hidden', 'true').html('&nbsp; &gt; &nbsp;').appendTo(collection_li);
        bc_items.unshift(collection_li);
      }
      bc_items.push($('<li>').attr('aria-current', 'page').text(current_page_text));

      var ol = $('<ol>');
      $.each(bc_items, function(i, item) { ol.append(item); });
      breadcrumb.empty().append($('<nav>').attr('aria-label', 'Breadcrumb').append(ol));
      breadcrumb.parent().addClass('has_breadcrumb');
    } else {
      breadcrumb.hide();
    }
  }
});
