---
nav_title: 알 수 없는 전화번호 처리
article_title: 알 수 없는 전화번호 처리
page_order: 3
description: "이 참조 문서에서는 Braze가 신규 사용자의 알 수 없는 전화번호를 처리하는 방법을 설명합니다."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS

---

# 알 수 없는 전화번호 처리 - 신규 사용자 {#handle-unknown-phone-numbers-new-users}

> Braze에서 SMS, MMS, RCS를 설정하고 운영하다 보면 알 수 없는 사용자로부터 메시지를 수신할 수 있습니다. 다음 단계에서는 식별되지 않은 사용자와 번호가 어떻게 처리되는지 설명합니다.

## 알 수 없는 번호에 대한 옵트인/옵트아웃 및 커스텀 키워드 워크플로 {#opt-inout-and-custom-keyword-workflow-for-unknown-numbers}

Braze는 알 수 없는 번호를 다음 세 가지 방법 중 하나로 자동 처리합니다.

1. 옵트인 키워드가 문자로 전송된 경우:
  * Braze가 익명 프로필을 생성합니다
  * 시스템이 전화번호 속성을 설정합니다
  * Braze가 수신한 옵트인 키워드에 따라 해당 구독 그룹에 사용자를 가입시킵니다.<br><br>
2. 옵트아웃 키워드가 문자로 전송된 경우:
  * Braze가 익명 프로필을 생성합니다
  * 시스템이 전화번호 속성을 설정합니다
  * Braze가 수신한 옵트아웃 키워드에 따라 해당 구독 그룹에서 사용자를 탈퇴시킵니다.<br><br>
3. 기타 커스텀 키워드가 문자로 전송된 경우:
  * Braze가 해당 문자 메시지를 무시하고 아무 작업도 수행하지 않습니다.