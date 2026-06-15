---
nav_title: LiftIgniter
article_title: LiftIgniter
alias: /partners/liftigniter/
description: "이 참조 문서에서는 기업이 고객 경험을 혁신할 수 있도록 지원하는 선도적인 개인화 플랫폼인 LiftIgniter와 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Liftigniter

> [LiftIgniter](https://www.liftigniter.com/)는 기업이 모든 터치포인트에서 실시간 개인화를 통해 고객 경험을 혁신할 수 있도록 지원하는 선도적인 개인화 플랫폼입니다.

_이 통합은 Liftigniter에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

LiftIgniter와 Braze의 통합은 연결된 콘텐츠를 사용하여 뉴스 기사, 의류, 기타 리테일 아이템 및 동영상과 같은 흥미로운 주제를 추천할 수 있도록 합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| LiftIgniter 계정 | 이 파트너십을 활용하려면 [LiftIgniter 계정](https://console.liftigniter.com/login)이 필요합니다. |
| LiftIgniter API 통합 | 추천을 가져오려면 LiftIgniter를 사이트 또는 앱에 [통합](https://support.liftigniter.com/support/solutions/articles/30000024667-api-integration-overview)해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

[LiftIgniter의 REST API](https://documenter.getpostman.com/view/2166502/liftigniter/7TFGvSV#9bdf75da-edd6-45ec-9c28-a0edefad1389)를 사용하여 개인화된 콘텐츠를 메시지에 삽입하세요. LiftIgniter 계정이 있고 LiftIgniter가 앱에 통합된 후, 다음 템플릿을 메시지 작성기에 추가하여 메시지에 콘텐츠를 호출하고 필요에 따라 정보를 교체하세요(`x-api-key`, `theapikey` 등).

{% raw %}
```
{% connected_content https://query.petametrics.com/v3/lkdk9usg5av95fvs/userId/model :method post :headers {"x-api-key": "theapikey"} :body "UseActivity"=false :content_type application/json :save json %}
```

다음으로, JSON으로 호출할 콘텐츠를 정의하여 메시지를 작성합니다. 예를 들어, `{{json.items[0].title}}`과 같이 작성합니다.

{% endraw %}

![LiftIgniter 전용 연결된 콘텐츠 호출이 포함된 푸시 캠페인을 보여주는 이미지. 이미지 필드에 연결된 콘텐츠 로직도 추가되어 있습니다.]({% image_buster /assets/img/liftigniter.png %})

이 메시지를 작성기 본문에 입력하면 메시지를 미리 볼 수 있습니다. 다음 예시와 같이 이미지를 가져올 수도 있습니다:

![메시지가 전송된 후 어떤 모습일지 보여주는 미리보기 이미지입니다.]({% image_buster /assets/img/liftigniter2.png %})