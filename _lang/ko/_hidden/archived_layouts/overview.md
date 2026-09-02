---
nav_title: 개요
page_order: 0
noindex: true
---

# 레이아웃 예시: 개요

> 개요 레이아웃은 사용자가 버튼을 클릭하여 페이지의 특정 부분 또는 완전히 다른 페이지로 이동할 수 있도록 페이지 상단에 특정 탐색 옵션을 만드는 데 유용합니다.

SELECTOR 레이아웃의 대표적인 예로는 [SDK 체인지로그]({{site.baseurl}}/developer_guide/changelogs) 페이지 또는 [인앱 메시지 크리에이티브 세부 정보 페이지]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types)가 있습니다.

## 필수 구성 요소

1. YAML 열기 및 닫기 표기. 즉, 콘텐츠 앞에 ---, 뒤에 ---를 사용합니다.
2. 특정 매개변수 콘텐츠 주위에 따옴표 사용. (헤더 매개변수, 텍스트 매개변수, 하이픈 또는 기타 특수 문자가 포함된 콘텐츠.)
3. 용어집 태그 표기 (필터 태그에 해당)

## 필수 매개변수

| 매개변수 | 콘텐츠 유형 | 세부 사항 |
|---|---|---|
| `page_order` | 숫자 | 섹션 내에서 페이지 순서를 지정합니다. 이 순서는 왼쪽 내비게이션에 반영됩니다. |
| `nav-title` | 영숫자 | 왼쪽 내비게이션에 표시될 제목입니다. |
| `layout` | 영숫자 - 공백 없음 | 설명서의 [레이아웃 섹션](https://github.com/Appboy/braze-docs/tree/develop/_layouts)에서 레이아웃을 선택합니다. |
| `guide_top_header` | 영숫자 | 페이지 제목을 지정합니다. |
| `guide_top_text` | 영숫자 | 페이지를 설명하며, 버튼과 제목 바로 위에 표시됩니다. 콘텐츠 주위에 따옴표가 필요합니다. |
| `guide_featured_title` | 영숫자 | 카드 제목을 지정합니다. 버튼 바로 위에 표시됩니다. |
| `guide_featured_list` | 추가 YAML, 영숫자 | 아래의 [가이드 목록 형식](#guide-listing-format)을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="필수 매개변수" }

### 가이드 목록 형식 {#guide-listing-format}

| 매개변수 | 콘텐츠 유형 | 세부 사항 |
|---|---|---|
| `name` | 영숫자 | 박스 이름을 지정합니다. |
| `link` | URL 또는 경로 | 박스가 연결될 위치의 링크입니다. 전체 URL 또는 (내부 링크인 경우) `/docs...`를 포함해야 합니다. |
| `image` | 경로 | 이미지 위치에 대한 링크입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="가이드 목록 형식" }

형식 예시:

```yaml
- name: Modal
  link: /docs/user_guide/channels/in_app_messages/message_types/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
```

```yaml
---
nav_title: 크리에이티브 세부 사항
page_order: 4
layout: featured
guide_top_header: "크리에이티브 세부 사항"
guide_top_text: "인앱 메시지로 창의력을 발휘해 보세요! 하지만 먼저 몇 가지 가이드라인을 알아두어야 합니다! 규칙을 깨려면 먼저 그 규칙을 알아야 하니까요! 아래에서 개별 메시지 유형의 크리에이티브 사양 또는 전체 크리에이티브 세부 사항을 확인하세요."

guide_featured_title: "메시지 유형별 크리에이티브 사양"
guide_featured_list:
- name: Modal
  link: /docs/user_guide/channels/in_app_messages/message_types/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: 슬라이드업
  link: /docs/user_guide/channels/in_app_messages/message_types/#slideup
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: 전체화면
  link: /docs/user_guide/channels/in_app_messages/message_types/#full-screen
  image: /assets/img/braze_icons/expand-05.svg
---

# 크리에이티브 세부 사항 {#general}

Braze 인앱 메시지에는 전체 크리에이티브 사양과 개별 크리에이티브 사양이 모두 있습니다. 더 커스텀 가능한 인앱 메시지 유형에 대한 자세한 내용은 [커스텀]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/) 페이지를 참조하세요.

{% alert important %}
  이 세부 사항은 최신 인앱 메시지 세대(3세대)에만 적용됩니다. 최신 세대의 인앱 메시지를 사용하지 않는 경우 [이전 인앱 메시지 세대]({{ site.baseurl }}/help/best_practices/in-app_messages/previous_in-app_message_generations/) 설명서를 확인하세요.
{% endalert %}