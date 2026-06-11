---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "이 참조 문서에서는 Braze와 Inkit 간의 파트너십에 대해 설명합니다. 이 파트너십을 통해 다이렉트 메일 캠페인을 자동화하여 시간과 노력을 절약하고, 오프라인 고객을 온라인으로 다시 유도할 수 있습니다."
page_type: partner
search_tag: Partner

---

# Inkit

> [Inkit](https://www.inkit.com)과 Braze는 조직이 디지털 방식과 다이렉트 메일을 통해 문서를 안전하게 생성하고 배포할 수 있도록 지원합니다.

_이 통합은 Inkit에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Inkit 통합을 사용하면 문서를 생성하고 Braze 웹훅을 통해 Braze 사용자에게 직접 발송할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| Inkit 계정 | 이 파트너십을 이용하려면 [Inkit 계정](https://www.inkit.com/)이 필요합니다. |
| Inkit API 키<br><br>`<INKIT_API_TOKEN>` | 이 키는 [Inkit 대시보드](https://app.inkit.io/#/account/integrations)의 **Development** 탭에서 확인할 수 있으며, Braze와 Inkit 계정을 연결하는 데 사용됩니다. |
| Inkit 템플릿 ID<br><br>`<INKIT_TEMPLATE_ID>` | 템플릿을 생성한 후 **Templates** 탭에서 템플릿 ID를 복사하여 Braze의 템플릿에서 사용할 수 있습니다.<br><br>예를 들어, Inkit 환경에서 `invoice_template`이라는 템플릿을 생성하면 템플릿 ID가 `tmpl_3bDScFl9cwr3OAVR1RSdEC`와 같이 부여됩니다.
| HTTP 헤더 | HTTP 헤더는 Braze에서 Inkit으로 보내는 API 요청의 일부입니다. 여기에 Inkit API 키를 포함하여 Inkit API 호출을 인증하고 승인합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

### 1단계: Inkit 템플릿 생성 {#step-1-create-an-inkit-template}

Inkit 플랫폼에서 Braze Campaign에 사용할 템플릿을 HTML, Word, PowerPoint, Excel 또는 PDF로 생성합니다. 자세한 내용은 [Inkit 설명서](https://docs.inkit.com/docs/create-a-template)를 참조하세요.

### 2단계: Braze 웹훅 템플릿 생성 {#step-2-create-your-braze-webhook-template}

향후 Campaigns 또는 Canvases에서 사용할 Inkit 웹훅 템플릿을 생성하려면 Braze 플랫폼에서 **콘텐츠** > **웹훅**으로 이동합니다. 그런 다음 **웹훅 템플릿 생성**을 선택합니다.

일회성 Inkit 웹훅 Campaign을 생성하거나 기존 템플릿을 사용하려면 새 Campaign을 생성할 때 Braze에서 **웹훅**을 선택합니다.

![템플릿 및 미디어 섹션의 웹훅 템플릿 탭에서 미리 디자인된 웹훅 템플릿을 선택할 수 있습니다.]({% image_buster /assets/img/inkit-webhook-template.png %})

Inkit 웹훅 템플릿을 선택하면 다음과 같이 표시됩니다:
- **웹훅 URL**: 비어 있음
- **요청 본문**: 원시 텍스트

웹훅 URL 필드에 Inkit 웹훅 URL을 [생성하고](https://docs.inkit.com/docs/set-up-a-webhook-to-an-event) 입력합니다.

![Braze 웹훅 빌더 작성 탭에 표시된 요청 본문 코드와 웹훅 URL.]({% image_buster /assets/img/inkit-integration.png %})

#### 요청 헤더 및 메서드 {#request-headers-and-method}

Inkit은 인증을 위해 base 64로 인코딩된 Inkit API 키를 포함하는 `HTTP Header`가 필요합니다. 다음 항목은 이미 키-값 페어로 템플릿에 포함되어 있지만, **설정** 탭에서 `<INKIT_API_TOKEN>`을 실제 Inkit API 키로 교체해야 합니다.

{% raw %}
- **HTTP 메서드**: POST
- **요청 헤더**:
  - **Authorization**: Basic `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Content-Type**: application/json
{% endraw %}

#### 요청 본문 {#request-body}

Liquid가 다음 필수 및 선택 사항 필드와 연결된 올바른 커스텀 속성과 일치하는지 확인합니다. 모든 요청에 커스텀 데이터 필드를 추가할 수도 있습니다.

```json
{% raw %}{
  "api_token": "<INKIT_API_TOKEN>",
  "template_id": "<INKIT_TEMPLATE_ID>",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "company": "{{custom_attribute.${company_name}}}",
  "phone" : "{{${phone_number}}}",
  "address_line_1": "{{custom_attribute.${address}}}",
  "address_line_2": "{{custom_attribute.${address2}}}",
  "address_city": "{{${city}}}",
  "address_state": "{{custom_attribute.${state}}}",
  "address_zip": "{{custom_attribute.${zip}}}",
  "address_country": "{{${country}}}",
  "source" : "Braze"
}{% endraw %}
```

### 3단계: 요청 미리보기 {#step-3-preview-your-request}

원시 텍스트가 적용 가능한 Braze 태그인 경우 자동으로 강조 표시됩니다. 이 웹훅을 전송하려면 `street`, `unit`, `state`, `zip`을 [커스텀 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes)으로 설정해야 합니다.

**미리보기** 패널에서 요청을 미리 보거나 **테스트** 탭으로 이동하여 랜덤 사용자, 기존 사용자를 선택하거나 직접 커스터마이즈하여 웹훅을 테스트할 수 있습니다.

{% alert important %}
페이지를 떠나기 전에 템플릿을 저장하는 것을 잊지 마세요! <br>업데이트된 웹훅 템플릿은 새 [웹훅 Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)을 생성할 때 **저장된 웹훅 템플릿** 목록에서 찾을 수 있습니다.
{% endalert %}