---
nav_title: "알 수 없는 전화번호 처리"
article_title: "알 수 없는 전화번호 처리"
description: "이 참조 문서에서는 Braze가 WhatsApp 사용자의 알 수 없는 전화번호를 처리하는 방법을 다룹니다."
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# 알 수 없는 전화번호 처리 {#handle-unknown-phone-numbers}

> WhatsApp을 Braze와 연동하여 운영하기 시작한 후 알 수 없는 사용자로부터 메시지를 받을 수 있습니다. 다음 단계에서는 미확인 사용자와 번호가 어떻게 처리되는지 설명합니다.

## 알 수 없는 번호에 대한 옵트인/옵트아웃 및 커스텀 키워드 워크플로 {#opt-inout-and-custom-keyword-workflow-for-unknown-numbers}

Braze는 먼저 일치하는 번호를 가진 사용자를 찾으려고 시도합니다. 일치하는 사용자가 없으면 Braze는 다음 두 가지 방법 중 하나로 알 수 없는 번호를 자동으로 처리합니다.

1. **트리거 단어가 포함된 [옵트인 Canvas]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs)가 설정된 경우:**
- Braze가 익명 프로필을 생성합니다
- 다음 세부 정보로 프로필에 사용자 별칭을 할당합니다:
  - 사용자가 제공한 전화번호를 값으로 하는 `alias_name`
  - `phone`을 값으로 하는 `alias_label`
- 시스템이 전화번호 속성을 설정합니다
- Canvas 내에 설정된 로직에 따라 사용자가 해당 구독 그룹에 가입됩니다<br><br>
2. **옵트인 Canvas가 설정되지 않은 경우:**
- Braze가 익명 프로필을 생성합니다
- 다음 세부 정보로 프로필에 사용자 별칭을 할당합니다:
  - 사용자가 제공한 전화번호를 값으로 하는 `alias_name`
  - `phone`을 값으로 하는 `alias_label`
- 시스템이 전화번호 속성을 설정합니다
- 모든 WhatsApp 구독 그룹에 대해 사용자의 구독 상태가 기본값으로 `unsubscribed`로 설정됩니다<br><br>