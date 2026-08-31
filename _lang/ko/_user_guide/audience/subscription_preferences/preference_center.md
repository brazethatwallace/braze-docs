---
nav_title: 환경설정 센터
article_title: 환경설정 센터
page_order: 8
layout: dev_guide
guide_top_header: "환경설정 센터"
guide_top_text: "이메일 환경설정 센터를 사용하면 사용자가 앱이나 웹사이트의 브랜드 페이지에서 이메일 Campaign 및 뉴스레터에 대한 알림 환경설정을 관리할 수 있습니다. 다음 문서를 통해 <a href='/docs/api/endpoints/preference_center'>Braze 환경설정 센터 API</a> 또는 드래그 앤 드롭 편집기를 사용하여 구독 그룹, 옵트인 상태, 호스팅 페이지 커스터마이즈를 포함한 환경설정 센터를 생성하고 관리하는 방법을 알아보세요."
description: "이 랜딩 페이지에는 Braze 이메일 환경설정 센터 및 환경설정 센터 API 사용 방법에 대한 문서가 포함되어 있습니다."
channel:
  - email

guide_featured_title: "섹션 문서"
guide_featured_list:
- name: API 이메일 환경설정 센터
  link: /docs/user_guide/audience/subscription_preferences/preference_center/api_preference_center
  image: /assets/img/braze_icons/list.svg
- name: 드래그 앤 드롭 환경설정 센터
  link: /docs/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center
  image: /assets/img/braze_icons/mail-01.svg

---

{% multi_lang_include alerts/tip_alerts.md alert="Landing pages manage subscriptions" %}

## 자주 묻는 질문 {#frequently-asked-questions}

### 이메일 환경설정 센터란 무엇인가요? {#what-is-an-email-preference-center}

이메일 환경설정 센터는 사용자가 이메일 구독 상태를 업데이트하고 메시지 카테고리를 선택할 수 있는 호스팅된 페이지입니다. Braze는 API로 구축하는 환경설정 센터와 드래그 앤 드롭 환경설정 센터를 지원합니다.

### 환경설정 센터 API와 드래그 앤 드롭 편집기 중 어떤 것을 사용해야 하나요? {#should-i-use-the-preference-center-api-or-the-drag-and-drop-editor}

코드를 최소화하면서 빠르게 설정하려면 [드래그 앤 드롭 이메일 환경설정 센터]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center)를 사용하세요. 레이아웃, 호스팅, 커스텀 로직을 완전히 제어해야 하는 경우에는 [API 이메일 환경설정 센터]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/api_preference_center)를 사용하세요.