{% alert note %}
RCS 메시지의 경우, 링크 단축 및 URL 수준 클릭 추적은 메시지 본문의 URL에 대해 지원되지만, 추천 작업의 URL에는 지원되지 않습니다. 추천 작업 URL의 클릭은 RCS 클릭 이벤트로 기록되지만, `URL` 및 `SHORT_URL` 필드는 Currents 및 Snowflake에서 null이 됩니다.
{% endalert %}