{% comment %}
  Shared webhook billing note for Message Credits / Action Credits pages.
  Optional parameter:
  - credit_name: Product name shown in the sentence (default: "Message Credits")
{% endcomment %}
{% assign credit_name = include.credit_name | default: "Message Credits" %}
2026년 8월 19일부터 실패한 웹훅 요청은 사용량 청구에서 제외되며, 성공한 요청만 {{ credit_name }}을 사용합니다. 이 변경 사항은 시행일 이후에 적용되며, 시행일 이전에 청구된 사용량에는 영향을 미치지 않습니다.