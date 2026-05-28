---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "이 참조 문서에서는 고객 생애주기 전반에 걸쳐 개인화를 제공하는 실시간 옴니채널 개인화 솔루션인 Braze와 Certona의 파트너십에 대해 설명합니다. Certona를 Braze 연결된 콘텐츠 파트너와 함께 사용하여 멀티채널 Campaigns에 콘텐츠 추천을 쉽게 삽입할 수 있습니다."
page_type: partner
search_tag: Partner

---

# Certona

> [Certona](https://www.certona.com/)의 플랫폼은 고객 생애주기 전반에 걸쳐 개인화를 촉진합니다. 고도로 개인화된 이메일 Campaigns부터 머신 러닝 기반 제품 추천까지, Certona는 개인화의 힘을 최대한 활용할 수 있도록 보장합니다.

_이 통합은 Certona에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze와 Certona의 통합은 연결된 콘텐츠를 통해 Braze Campaigns 및 Canvases에서 Certona의 머신 러닝 제품 추천을 사용합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| [Certona 계정](https://manage.certona.com/) | 이 파트너십을 활용하려면 Certona 계정이 필요합니다. |
| [Certona REST API 엔드포인트](https://manage.certona.com/) | 이 엔드포인트는 Braze Campaign 메시지에서 직접 사용되어 사용자 ID를 기반으로 추천 콘텐츠를 가져옵니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합 {#integration}

Certona의 REST API를 사용하여 메시지에 개인화된 콘텐츠를 삽입합니다. 이를 위해 다음 연결된 콘텐츠 템플릿을 Certona REST API 엔드포인트와 함께 Braze 메시지 작성기에 추가하면 됩니다.

{% raw %}
```liquid
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}
```

다음으로, 관련 텍스트나 이미지 등 호출하려는 콘텐츠를 정의합니다. 예를 들어, `{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}`과 같이 작성합니다.

{% endraw %}

![메시지 본문에 Certona 관련 연결된 콘텐츠가 포함된 푸시 Campaign 이미지입니다.]({% image_buster /assets/img/certona.png %})

이 메시지를 작성기 본문에 입력한 후에는 연결된 콘텐츠 호출을 미리 보고 올바른 정보가 표시되는지 확인합니다.

![사용자가 메시지를 보내기 전에 철저히 테스트하도록 권장하는 "테스트" 탭을 보여주는 이미지입니다.]({% image_buster /assets/img/certona2.png %})