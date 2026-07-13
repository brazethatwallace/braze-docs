{%- assign portal_url = site.baseurl | append: '/user_guide/administer/personal/product_portal' -%}
{%- assign feature_label = include.feature | default: 'this capability' -%}
{%- assign pain_point_channel = include.channel | default: '' | downcase -%}
{%- if include.context == 'gap' -%}
{{ feature_label }}에 관심이 있으시면 [제품 피드백]({{ portal_url }})을 제출해 주세요.
{%- elsif include.context == 'new_feature' -%}
{%- assign feature_label = include.feature | default: 'This capability' -%}
{{ feature_label }}이(가) 정식 출시되었습니다. [제품 피드백]({{ portal_url }})을 통해 팀에서 어떻게 활용하고 계신지 공유해 주세요.
{%- elsif include.context == 'pain_point' -%}
{%- if pain_point_channel == 'feature' -%}
{{ feature_label }}을(를) 원하시나요? [제품 피드백]({{ portal_url }})을 남겨 보세요.
{%- elsif pain_point_channel == 'ux' -%}
{{ feature_label }}에 대한 피드백이 있으시면 글로벌 헤더의 **지원** 메뉴를 열고 **피드백 공유**를 선택하여 의견을 보내 주세요.
{%- else -%}
<!-- product_feedback_cta fallback: missing or invalid pain_point channel; expected feature or ux -->
{{ feature_label }}을(를) 원하시나요? [제품 피드백]({{ portal_url }})을 남겨 보세요.
{%- endif -%}
{%- endif -%}