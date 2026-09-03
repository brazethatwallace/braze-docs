---
nav_title: Kickbox
article_title: Kickbox
alias: /partners/kickbox/
description: "이 참고 문서에서는 이메일 목록을 검증하거나 애플리케이션에 인증을 통합하는 데 사용되는 이메일 인증 플랫폼인 Braze와 Kickbox 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner
---

# Kickbox

> [Kickbox](https://kickbox.com/)는 이메일 데이터를 깨끗하고 전달 가능하게 유지하는 데 필요한 기능, 통합, 보안을 갖춘 올인원 이메일 인증 플랫폼입니다. Kickbox 통합은 전송 전에 Kickbox 이메일 인증을 사용하여 전달 불가능하거나 품질이 낮은 이메일 주소를 식별함으로써 Braze Campaigns의 전달 가능성을 향상시킵니다.

Kickbox를 사용하면 Braze에서 고객 프로필이 업데이트되는 순간 사용자 이메일 주소의 품질을 검증할 수 있습니다. 이는 프로필의 `email` 필드가 채워질 때 트리거되는 전용 Canvas 또는 Campaign 워크플로를 통해 이루어집니다.

Canvas 또는 Campaign은 사용자의 이메일 주소를 공유하는 웹훅을 Kickbox에 전송합니다. Kickbox는 이메일 주소의 유효성을 검사하고 Braze REST API 엔드포인트를 사용하여 품질을 상세히 설명하는 커스텀 속성으로 고객 프로필을 업데이트합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --------------------------------------|-------------------------------------------------------------------------------|
| Kickbox 계정 | 이 통합을 사용하려면 활성 Kickbox 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br>Braze 대시보드에서 **설정** > **API 및 식별자** > **API 키**로 이동하여 생성할 수 있습니다. |
| 통합에 대한 액세스 권한 요청 | Kickbox 고객지원팀에 문의하여 Braze 통합에 대한 액세스 권한을 부여받으세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

Kickbox와 통합하려면 [Braze와 통합하기](https://docs.kickbox.com/docs/integrating-with-braze#/)의 단계를 따르세요.

## 활용 사례 {#use-cases}

### 대량 인증 {#bulk-verification}

몇 달 또는 분기별로 전체 목록을 인증하여 고객이탈되는 이메일이나 시간이 지남에 따라 품질이 저하되어 전달 가능성이 서서히 떨어지는 목록으로부터 보호할 수도 있습니다.

이렇게 하려면 Kickbox에 설명된 대로 워크플로의 **진입 설정** 설정을 변경해야 합니다. **실행 기반 전달**을 선택하는 대신 **스케줄**을 선택합니다. 그런 다음 목록을 한 번에 인증할 스케줄 시간을 선택합니다.

### 인증된 세그먼트 생성 {#create-verified-segments}

Kickbox의 커스텀 속성은 다음 예시와 같이 일관된 스키마를 가지고 있습니다.

{% raw %}
```json
   {
  "attributes": [
    {
      "email": "example1@example.com",
      "_update_existing_only": true,
      "success": true,
      "code": null,
      "message": null,
      "result": "deliverable",
      "reason": "accepted_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": null,
      "sendex": 1,
      "user": "example1",
      "domain": "example.com"
    },
    {
      "email": "example2@exampl.com",
      "_update_existing_only": true,
      "success": true,
      "code": "44312",
      "message": "SMTP verification",
      "result": "undeliverable",
      "reason": "rejected_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": "example2@example.com",
      "sendex": 0.23,
      "user": "example2",
      "domain": "exampl.com"
    }
  ]
}
```
{% endraw %}

즉, 이메일 주소가 인증된 사용자로 오디언스 세그먼트를 생성하여 Campaigns와 Canvases의 전달 성공률을 높이고 이메일 서비스 공급자와의 평판을 보호할 수 있습니다.

이를 위해 다음 단계를 따르세요.

1. Braze에서 **오디언스** > **Segments** > **세그먼트 생성**으로 이동합니다.
2. **필터 그룹** 섹션에서 **커스텀 속성** 필터를 추가하고 드롭다운에서 "result"를 선택합니다.

사용 사례에 따라 고객 프로필에 Kickbox 커스텀 속성 "result"가 존재하는 세그먼트를 생성하거나 해당 값이 "deliverable"인 세그먼트를 생성하는 것이 적절할 수 있습니다. 이 필터를 단독으로 사용하여 세그먼트를 만들거나 향후 모든 세그먼트의 일부로 만들어 그 안에 있는 모든 사용자를 검증할 수 있습니다.