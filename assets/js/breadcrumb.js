$(document).ready(function() {

  var breadcrumb = $('#breadcrumb');
  if (breadcrumb.length) {
    var curpage = $('#left_navmenu .nav-item.active');
    var currentPageText = curpage.text().trim();
    var bc_items = [];
    var bc_link = '';
    var curtext = '';
    var dataparent = curpage.attr('data-parent');

    while (dataparent) {
      curpage = $('#' + dataparent);
      curtext = curpage.text().trim();
      if (curtext) {
        bc_link = curpage.find('.nav_link');
        if (bc_link.length && bc_link[0].href) {
          bc_items.unshift('<li><a href="' + bc_link[0].href + '">' + curtext + '</a><span aria-hidden="true"> &gt; </span></li>');
        } else {
          bc_items.unshift('<li>' + curtext + '<span aria-hidden="true"> &gt; </span></li>');
        }
      }
      dataparent = curpage.attr('data-parent');
    }

    if (currentPageText.length || bc_items.length) {
      if (page_collection_title) {
        bc_items.unshift('<li><a href="' + base_url + '/' + page_collection + '/' + page_collection_default_path + '">' + page_collection_title + '</a><span aria-hidden="true"> &gt; </span></li>');
      }
      bc_items.push('<li aria-current="page">' + currentPageText + '</li>');

      breadcrumb.html('<nav aria-label="Breadcrumb"><ol>' + bc_items.join('') + '</ol></nav>');
      breadcrumb.parent().addClass('has_breadcrumb');
    } else {
      breadcrumb.hide();
    }
  }
});
