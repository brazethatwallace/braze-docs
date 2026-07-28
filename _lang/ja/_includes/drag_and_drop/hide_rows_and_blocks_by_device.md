{% comment %}
  Shared drag-and-drop editor guidance for hiding rows and blocks by device.
  Parameters:
  - channel (required): "banner", "in_app_message", or "landing_page"
{% endcomment %}

{% if include.channel == 'banner' %}
{% assign heading_level = '#####' %}
{% assign preview_subject = 'Banner' %}
{% assign live_phrase = 'ライブBannerでは' %}
{% elsif include.channel == 'in_app_message' %}
{% assign heading_level = '###' %}
{% assign preview_subject = 'メッセージ' %}
{% assign live_phrase = 'ライブアプリ内メッセージでは' %}
{% elsif include.channel == 'landing_page' %}
{% assign heading_level = '####' %}
{% assign preview_subject = 'ページ' %}
{% assign live_phrase = 'ライブランディングページでは' %}
{% endif %}

{{ heading_level }} デバイス別に行やブロックを非表示にする

デスクトップとタブレット・モバイルでレイアウトを調整するには、キャンバス上の行またはブロックを選択し、プロパティパネルの **Hide on** トグルを使用して、**Desktop** または **Tablet and smaller devices** で非表示にします。非表示にした行やブロックは、ドラッグ＆ドロップエディターで{{ preview_subject }}をプレビューする場合でも、{{ live_phrase }}でも、そのデバイスタイプには表示されません。