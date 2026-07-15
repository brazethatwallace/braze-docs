---
nav_title: 크리에이티브 세부 정보
article_title: Content Cards 크리에이티브 세부 정보
page_order: 2
description: "이 문서에서는 세 가지 표준 Content Cards 유형에 대한 이미지 크기 권장 사항 및 해제 동작과 같은 크리에이티브 세부 정보를 다룹니다."
channel:
  - content cards
tool: Media

---

# Content Cards 크리에이티브 세부 정보 {#creative-details-for-content-cards}

> Content Cards와 카드가 위치한 피드의 커스터마이징은 Campaign 생성 과정에서 수행할 수 없습니다. 엔지니어 및 개발자와 협력하여 카드를 구축하고 커스터마이징해야 합니다. 기술적인 세부 정보는 [개발자 설명서]({{site.baseurl}}/developer_guide/getting_started/customization_overview)를 참조하세요.

## Content Cards 유형 {#content-card-types}

{% tabs %}
{% tab 클래식 %}

클래식 카드는 표준 메시징 및 알림, 또는 아이콘을 사용하여 메시지를 시각적으로 분류하는 데 적합합니다. 이미지는 선택 사항이지만, 1:1 비율이어야 합니다.

![권장 세부 정보가 포함된 클래식 카드 이미지와 클래식 카드 예시]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}

| 카드 기능 | 세부 정보 |
| --- | ---|
| 헤더 텍스트 | 18px; 볼드 <br> 한 줄의 텍스트가 이상적입니다. <br> Liquid을 사용하여 메시지를 개인화할 수 있습니다. |
| 메시지 텍스트 | 13px; 일반 굵기 <br> 2~4줄의 텍스트가 이상적입니다. <br> Liquid을 사용하여 메시지를 개인화할 수 있습니다. |
| 링크 텍스트 | 선택 사항. <br> 13&nbsp;px <br> 웹 페이지 링크 또는 앱 내 딥링크. |
| 이미지 | 선택 사항. <br> 1:1 비율이어야 합니다. <br> 60 x 60&nbsp;px 이미지 품질을 권장합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Cards 유형" }

{% endtab %}
{% tab 캡션 이미지 %}

캡션 이미지 카드는 대규모 세일이나 새로운 앱 기능과 같은 중요한 콘텐츠를 보여주고 관심을 끌기에 좋은 방법입니다.

![권장 세부 정보가 포함된 캡션 이미지 카드 이미지와 캡션 이미지 카드 예시]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}

| 카드 기능 | 세부 정보 |
| --- | ---|
| 헤더 텍스트 | 18px; 볼드 <br> 한 줄의 텍스트가 이상적입니다. <br> Liquid을 사용하여 메시지를 개인화할 수 있습니다. |
| 메시지 텍스트 | 13px; 일반 굵기 <br> 2~4줄의 텍스트가 이상적입니다. <br> Liquid을 사용하여 메시지를 개인화할 수 있습니다. |
| 링크 텍스트 | 선택 사항. <br> 13&nbsp;px <br> 웹 페이지 링크 또는 앱 내 딥링크. |
| 이미지 | 4:3 비율을 권장합니다. <br> 최소 너비 600&nbsp;px. <br> 고해상도 PNG, JPEG, GIF를 지원합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Cards 유형" }

{% endtab %}
{% tab 이미지 전용 %}

더 많은 크리에이티브 제어를 원한다면 이미지 전용 카드가 적합합니다. 원하는 도구를 사용하여 이미지를 만들고 이 카드 유형에 이미지를 업로드하세요.

![권장 세부 정보가 포함된 이미지 전용 Content Cards 이미지와 이미지 전용 예시]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}

| 카드 기능 | 세부 정보 |
| --- | ---|
| 링크 카드 | 선택 사항. <br> 13&nbsp;px <br> 클릭 시 웹 페이지 또는 앱 내 딥링크로 연결됩니다. |
| 이미지 | 모든 종횡비를 지원합니다. <br> 최소 너비 600&nbsp;px. <br> 고해상도 PNG, JPEG, GIF를 지원합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Cards 유형" }

{% endtab %}
{% endtabs %}

## 글로벌 크리에이티브 세부 정보 {#general}

Content Cards는 기본적으로 텍스트와 이미지(GIF 포함)를 지원합니다. 현재 다른 글꼴 색상이나 여러 이미지와 같은 카드의 커스텀 스타일은 대시보드에서 설정할 수 없습니다. 통합 과정에서 Content Cards와 피드에 커스텀 스타일을 적용할 수 있습니다. 자세한 내용은 Braze SDK의 [카드 커스터마이징]({{site.baseurl}}/developer_guide/content_cards/customizing_cards)을 참조하세요.

### 해제 동작 {#dismissal-behavior}

사용자가 카드를 해제하려면 모바일에서 스와이프하거나 다음 스크린샷에 표시된 것처럼 `close X` 기능을 사용할 수 있습니다. `x`는 Web SDK에서만 마우스를 올렸을 때 나타납니다.

![카드의 스와이프 또는 닫기 해제 동작을 보여주는 이미지]({% image_buster /assets/img/dismissal-cc.png %})

사용자가 모든 카드를 해제했거나 새로운 업데이트를 푸시하지 않은 경우, 사용자의 피드는 일반적으로 다음과 같이 표시됩니다:

![빈 Content Cards 피드 이미지]({% image_buster /assets/img/empty-cc.png %}){: style="max-width:45%"}

{% alert tip %}
사용자가 관련 동작을 취할 때 해제되도록 설정하여 Content Cards의 관련성을 유지하세요. 예를 들어, 프로모션 Content Cards를 사용자가 구매하는 즉시 해제되도록 설정하면 이미 구매한 항목에 대한 제안을 계속 보지 않게 됩니다.
{% endalert %}

### Content Cards에서 GIF 사용 {#using-gifs-in-content-cards}

| Android용 Content Cards | iOS용 Content Cards | 웹용 Content Cards |
| --- | --- |---|
| Android SDK는 기본적으로 애니메이션 GIF 지원을 제공하지 않습니다. GIF 지원 활성화에 대한 자세한 내용은 [GIF]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs?sdktab=android)를 참조하세요. | Swift SDK는 기본적으로 애니메이션 GIF 지원을 제공하지 않습니다. GIF 지원 활성화에 대한 자세한 내용은 [GIF 지원 튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support)을 참조하세요. | GIF 지원은 Web SDK 통합에 기본적으로 포함되어 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Content Cards에서 GIF 사용" }