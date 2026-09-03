---
nav_title: 고유 할인 코드
article_title: 고유 할인 코드 보내기
alias: /shopify_discount_codes/
page_order: 7
description: "이 참조 문서에서는 Braze 프로모션 코드와 Shopify Bulk Discount Code Bot을 사용하여 Campaigns 및 Canvases를 통해 고유 할인 코드를 보내는 커뮤니티 제출 사용 사례를 다룹니다."
---

# Shopify를 통해 고유 할인 코드 보내기 {#send-unique-discount-codes-through-shopify}

> 이 커뮤니티 제출 사용 사례에서는 Braze [프로모션 코드]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes)와 Shopify Bulk Discount Code Bot을 사용하여 Campaigns 및 Canvases에 사용할 고유 할인 코드를 생성하는 방법을 보여줍니다. 고유 할인 코드는 일반 프로모션 코드의 악용을 방지하는 데 도움이 됩니다.

{% alert important %}
이것은 커뮤니티에서 제출한 통합이며 Braze에서 직접 지원하지 않습니다. Bulk Discount Code Bot은 Shopify에서 직접 지원합니다. Braze 프로모션 코드만 Braze에서 지원됩니다.
{% endalert %}

## 요구 사항 {#requirements}

| 요구 사항 | 설명 |
| --- | --- |
| Shopify 스토어 설정 | [Braze와 Shopify 스토어를 설정]({{site.baseurl}}/shopify_overview)했는지 확인하세요. |
| Bulk Discount Code Bot 앱 설치 | Shopify 앱 스토어에서 [Bulk Discount Code Bot](https://apps.shopify.com/bulk-discount-generator) 앱을 다운로드하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="요구 사항" }

## 고유 할인 코드 생성하기 {#generating-unique-discount-codes}

### 1단계: 할인 코드 설정하기 {#step-1-configure-your-discount-codes}

Bulk Discount Code Bot를 사용하여 생성할 코드 수, 코드 길이, 할인 값 등을 기반으로 할인 코드를 설정합니다.

![할인 세트의 설정 옵션.][1]{: width="1203" height="677" style="max-width:100%;"}

### 2단계: 코드 내보내기 {#step-2-export-your-codes}

Bulk Discount Code Bot의 검색창에서 할인 세트를 찾은 다음, **Export Codes** > **Download Codes**를 선택하여 다운로드 폴더에 CSV 파일을 다운로드합니다.

![할인 세트를 표시하는 드롭다운이 있는 검색창과 선택 가능한 버튼 행.][2]{: width="1163" height="858" style="max-width:70%;"}

CSV 파일에서 열 헤더 "Promo"를 제거하기 위해 행 1을 삭제합니다. 이렇게 하면 "Promo"가 Braze에서 할인 코드로 등록되는 것을 방지할 수 있습니다.

![CSV 파일에서 행 헤더 "Promo"를 제거하는 과정을 보여주는 순서도.][3]{: width="448" height="222" style="max-width:60%;"}

### 3단계: Braze에 할인 코드 추가하기 {#step-3-add-your-discount-codes-to-braze}

Braze에서 **데이터 설정** > **프로모션 코드** > **프로모션 코드 목록 만들기**로 이동하여 [할인 코드 목록을 설정]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#create)합니다. Bulk Discounts Code Bot에서 설정한 만료 날짜와 일치하는지 확인합니다.

그런 다음, CSV 파일을 업로드하고 **Save List**를 선택합니다.

### 4단계: Braze Campaign 또는 캔버스 단계에 할인 코드 추가하기 {#step-4-add-your-discount-codes-to-a-braze-campaign-or-canvas-step}

고유 할인 코드를 단일 발송 Campaign에 사용하거나, 사용자가 서로 다른 Campaigns 또는 캔버스 단계에서 여러 고유 코드를 받아도 상관없는 경우, 저장한 프로모션 코드 목록에서 코드의 Liquid 스니펫을 복사합니다.

![복사 버튼이 있는 Liquid 코드 스니펫.][4]{: width="958" height="295" style="max-width:60%;"}

Liquid 스니펫을 Campaign 또는 캔버스 단계에 붙여넣습니다.

<video autoplay muted loop playsinline loading="lazy" width="800" height="540" style="max-width:100%;height:auto;aspect-ratio:800/540;" aria-label="캔버스 단계에 Liquid 스니펫을 추가하는 과정을 보여주는 비디오.">
  <source src="{% image_buster /assets/img/shopify/liquid_promo_code.mp4 %}" type="video/mp4">
</video>

할인 코드가 Campaigns 또는 Canvases에서 몇 번 참조되더라도 사용자가 하나의 고유 할인 코드만 받도록 하려면, 할인 코드를 할당하는 첫 번째 메시지 단계 바로 앞에 [사용자 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) 단계를 만들어 "Promo Code"와 같은 커스텀 속성에 할인 코드를 할당합니다.

{% alert tip %}
**데이터 설정** > **커스텀 속성**으로 이동하여 [커스텀 속성을 생성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)할 수도 있습니다.
{% endalert %}

사용자 업데이트 단계에서 각 필드에 대해 다음을 수행합니다.
- **Attribute Name:** **Promo Code**를 선택합니다.
- **Action:** **Update**를 선택합니다.
- **Key Value:** Liquid 코드 스니펫을 붙여넣습니다.

![Liquid 스니펫으로 "Promo Code" 속성을 업데이트하는 사용자 업데이트 단계.][6]{: width="2464" height="1322" style="max-width:100%;"}

이제 모든 메시지에 커스텀 속성 {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %}를 추가할 수 있으며, 할인 코드가 자동으로 템플릿에 적용됩니다.

## 할인 코드 동작 {#discount-code-behavior}

{% details 멀티채널 Campaign 또는 캔버스 단계 %}

멀티채널 Campaign 또는 캔버스 단계에서 할인 코드 스니펫을 사용하면, 사용자는 항상 고유한 코드를 받습니다. 사용자가 두 개 이상의 채널을 통해 코드를 받을 자격이 있는 경우, 각 채널을 통해 동일한 코드를 받게 됩니다. 즉, 자격이 있는 사용자는 해당 Campaign 또는 캔버스 단계에서 보낸 모든 메시지에 걸쳐 하나의 코드만 받습니다.

{% enddetails %}

{% details 서로 다른 캔버스 단계 또는 별도의 Campaigns %}

하나의 Canvas 내 여러 단계 또는 별도의 Campaigns에서 할인 코드를 참조하는 경우, 자격이 있는 사용자는 각 캔버스 단계 또는 Campaign마다 하나씩 여러 개의 고유한 프로모션 코드를 받게 됩니다.

{% enddetails %}

[1]: {% image_buster /assets/img/shopify/configure_discount_codes.png %}
[2]: {% image_buster /assets/img/shopify/export_discount_codes.png %}
[3]: {% image_buster /assets/img/shopify/edited_codes_csv.png %}
[4]: {% image_buster /assets/img/shopify/liquid_code_snippet.png %}
[6]: {% image_buster /assets/img/shopify/user_update_step.png %}