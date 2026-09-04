---
nav_title: ドキュメントのフィードバック
permalink: /feedback/
hide_toc: true
---

<fieldset style="margin-top: 60px;">
<legend style="font-size: 2.5rem;color: #212123;font-weight:bold;">ドキュメントのフィードバック</legend>
<div id="フィードバック">
    <div id="feedback_section">
    ドキュメントを改善するアイデアや、お気づきの問題はありますか？ぜひお聞かせください。すべてのフィードバックをチームで確認し、改善に役立てています。<br /><br />

    <b>Brazeのドキュメントは平均してどの程度役に立っていますか？</b><br />

    <div id="feedback_answer_star">
      <div class="rating-list">
        <div class="フィードバック-star">
          <input type="radio" id="rating_1" name="feedback_rating" value="Very Unhelpful" tabindex="-1">
          <label for="rating_1" class="star-label" tabindex="0" aria-label="Very Unhelpful">
            <i class="fas fa-star" data-value="Very Unhelpful" title="Very Unhelpful"></i><br />1<br />役に立たない</label>
        </div>
        <div class="フィードバック-star">
          <input type="radio" id="rating_2" name="feedback_rating" value="Unhelpful" tabindex="-1">
          <label for="rating_2" class="star-label" tabindex="0" aria-label="Unhelpful">
            <i class="fas fa-star" data-value="Unhelpful" title="Unhelpful"></i><br />2<br />
          </label>
        </div>
        <div class="フィードバック-star">
          <input type="radio" id="rating_3" name="feedback_rating" value="Somewhat Helpful" tabindex="-1">
          <label for="rating_3" class="star-label" tabindex="0" aria-label="Somewhat helpful">
            <i class="fas fa-star" data-value="Somewhat Helpful" title="Somewhat Helpful"></i><br />3<br />やや役に立つ</label>
        </div>

        <div class="フィードバック-star">
          <input type="radio" id="rating_4" name="feedback_rating" value="Helpful" tabindex="-1">
          <label for="rating_4" class="star-label" tabindex="0" aria-label="Helpful">
            <i class="fas fa-star" data-value="Helpful" title="Helpful"></i><br />4<br />
          </label>
        </div>

        <div class="フィードバック-star">
          <input type="radio" id="rating_5" name="feedback_rating" value="Very Helpful" tabindex="-1">
          <label for="rating_5" class="star-label" tabindex="0" aria-label="Very Helpful">
            <i class="fas fa-star" data-value="Very Helpful" title="Very Helpful"></i><br />5<br />とても役に立つ
          </label>
        </div>

      </div>
    </div>
    <div style="margin-top: 15px;">
      <b>フィードバックをお寄せください</b> <br />
      <textarea id="feedback_comment" placeholder="&quot;このエラーメッセージに関する情報が見つかりませんでした&quot;"></textarea><br />
        ご質問がありますか？サポートチームまでお問い合わせください。
    </div>
    <button type="submit" name="submit_feedback" value="Submit フィードバック" class="btn btn-black" id="feedback_submit" role="button" style="margin-top:15px;"> フィードバックを送信 </button>
  </div>
  <div id="feedback_msg">
  </div>

</div>
</fieldset>

<style type="text/css">
#フィードバック {
  font-size: 16px;
}
#feedback_answer_star {
  display: inline-block;
}
#feedback_answer_star .rating-list {
  display: flex;
  list-style: none !important;
  margin: 0 !important;
  line-height: 1;
  flex-direction: row;
}
#feedback_answer_star .フィードバック-star {
  position: relative;
  padding: 10px 5px;
  width: 65px;
}
#feedback_answer_star .フィードバック-star input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 100%;
  height: 100%;
  margin: 0;
  cursor: pointer;
}
#feedback_answer_star .フィードバック-star .star-label {
  display: block;
  color: #999999 !important;
  font-size: 14px;
  text-align: center;
  padding-top: 5px;
  line-height: 1.5em;
  cursor: pointer;
  margin: 0;
}
#feedback_answer_star .フィードバック-star.hover-active .star-label {
  color: #000000 !important;
}
#feedback_answer_star .フィードバック-star input[type="radio"]:checked ~ .star-label,
#feedback_answer_star .フィードバック-star.active .star-label {
  color: #000000 !important;
}
#feedback_answer_star .フィードバック-star .star-label > i {
  font-size: 35px;
  margin-bottom: 15px;
}

#feedback_comment {
  margin-top: 15px;
  width: 100%;
  max-width: 680px;
  height: 140px !important;
  border: 2px solid grey !important;
  border-radius: 3px;
}
#feedback_msg {
  margin-top: 10px;
}

#feedback_msg.error {
  color: red;
  font-weight: bold;
}
#フィードバック button[type=submit] {
  font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  text-transform: capitalize;
  border-radius: 3px;
  padding: 1rem 2rem;
  border: 1px solid black !important;
}
#フィードバック button.btn-white {
  font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  text-transform: capitalize;
  border-radius: 3px;
  padding: 1rem 2rem;
  border: 1px solid black !important;
  background-color: #ffffff;
  color: #202024;
}
#フィードバック button.btn-white:hover {
  background-color: #202024 !important;
  color: #ffffff !important;
}
#フィードバック button[type=submit]:focus, #フィードバック button[type=submit]:hover {
  color: #000000;
  background-color: #FFFFFF;
}
#main_content h3 {
  margin-top: 48px;
}
</style>
<script type="text/javascript">
  var feedback_site = '{{site.baseurl}}{{page.url}}';
  var feedback_article_title = '{{page.article_title}}';
  var feedback_nav_title = '{{page.nav_title}}';
  var feedback_helpful = '';

  $('input[name="feedback_rating"]').on('change', function(e){
      feedback_helpful = $(this).val();

      // Update visual state for all stars
      $('.フィードバック-star').removeClass('active');
      var selectedStar = $(this).closest('.フィードバック-star');
      var selectedValue = $(this).val();

      // Mark selected star and all previous stars as active
      $('.フィードバック-star').each(function() {
        var starValue = $(this).find('input').val();
        if (starValue === selectedValue || shouldHighlightStar(starValue, selectedValue)) {
          $(this).addClass('active');
        }
      });
  });

  // Handle hover effect from left to right
  $('.フィードバック-star').on('mouseenter', function() {
    var hoveredIndex = $(this).index();
    $('.フィードバック-star').removeClass('hover-active');
    $('.フィードバック-star').each(function(index) {
      if (index <= hoveredIndex) {
        $(this).addClass('hover-active');
      }
    });
  });

  $('.rating-list').on('mouseleave', function() {
    $('.フィードバック-star').removeClass('hover-active');
  });

  // Handle keyboard interaction for accessibility
  $('.star-label').on('keydown', function(e) {
    if (e.key === ' ' || e.key === 'Enter') {
      e.preventDefault();
      $(this).prev('input[type="radio"]').prop('checked', true).trigger('change');
    }
  });

  function shouldHighlightStar(starValue, selectedValue) {
    var ratings = ['Very Unhelpful', 'Unhelpful', 'Somewhat Helpful', 'Helpful', 'Very Helpful' ];
    var starIndex = ratings.indexOf(starValue);
    var selectedIndex = ratings.indexOf(selectedValue);
    return starIndex <= selectedIndex;
  }


  $('#feedback_submit').on('click',function(e){
    var external_id = window.braze ? window.braze.getUser().getUserId() : '';
    var title = 'Documentations フィードバック';
    var comment = $('#feedback_comment').val().trim();
    var feedback_div = $('#feedback_msg');
    var submit_data = {
      'Helpful': feedback_helpful,
      'URL': feedback_site,
      'Article Title': title,
      'Nav Title': title,
      'Params': window.location.search,
      "Language": page_language,
      'フィードバック': comment,
      'ExternalId': external_id,
    };
    if (!feedback_helpful || !comment){
      feedback_div.fadeIn();
      feedback_div.addClass('error');
      feedback_div.html('Please provide a rating and フィードバック');
      feedback_div.fadeOut(2000).removeClass('error');
      return;
    }
    $('#feedback_submit').hide();

    if (window.braze) {
      window.braze.logCustomEvent(
        "Documentations フィードバック Comment", {
          "フィードバック": feedback_helpful,
          "Article Title": title,
          "Nav Title": title,
          "URL": feedback_site,
          "Language": page_language,
          "Comment": comment
        }
      );
    }

    var jqxhr = $.ajax({
        url: 'https://c9616da7-4322-4bed-9b51-917c1874fb31.trayapp.io/feedback',
        method: "GET",
        dataType: "json",
        data: submit_data
      }).done(function(dt) {
        feedback_div.html('');
        if (dt['result'] == 'success'){
          $('#feedback_section').hide();
          feedback_div.html('We truly value every piece of フィードバック. Thank you for your response.');
          feedback_div.fadeIn("slow");
        }
        else {
          feedback_div.html('Error. Please try again at a later time.');
          $('#feedback_submit').show();
        }
        feedback_div.fadeIn("slow");
      });
  });
</script>