{% tabs %}
{% tab Abandoned browse %}

### 유기한 탐색 {#abandoned-browse}

제품을 탐색했지만 장바구니에 추가하거나 주문하지 않은 사용자의 참여를 유도하려면 **유기한 탐색** 템플릿을 사용하세요.

![확장된 "진입 규칙"이 포함된 적용된 "유기한 탐색" Canvas 템플릿.]({% image_buster /assets/img_archive/abandoned_browse.png %})

#### 설정 {#setup}

Canvas 페이지에서 **Use a Canvas Template** > **Braze templates**를 선택한 다음 **유기한 탐색** 템플릿을 적용합니다.

##### 기본 설정 {#default-settings}

Canvas에는 다음 설정이 미리 구성되어 있습니다:
- 기본 사항
    - Canvas 이름: **Abandoned browse**
    - 전환 이벤트: `ecommerce.order placed`
        - 전환 마감일: 3일
- 진입 스케줄
    - 사용자가 `ecommerce.product_viewed` 이벤트를 수행할 때 액션 기반
    - 시작 시간은 Canvas 템플릿을 생성하는 시점입니다<br><br>![Canvas의 "액션 기반 옵션".]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br>
- 타겟 오디언스
    - 진입 오디언스
        - 이메일이 **비어 있지 않음**
        - 비즈니스 요구 사항에 맞게 진입 오디언스 기준을 수정할 수도 있습니다
    - 진입 제어
        - Canvas의 전체 기간이 완료된 후 사용자가 이 Canvas에 다시 진입할 수 있습니다
    - 종료 기준
        - `ecommerce.cart_updated`, `ecommerce.checkout_started` 또는 `ecommerce.order_placed` 수행<br><br>![Canvas의 진입 제어 및 종료 기준.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br>
- 발송 설정
    - 가입했거나 옵트인한 사용자
- 지연 단계
    - 1시간 지연
- 메시지 단계
    - 이메일 템플릿과 HTML 블록을 Liquid 템플릿 예시와 함께 검토하여 미리 작성된 템플릿의 메시지에 제품을 추가하세요. 자체 이메일 템플릿을 사용하는 경우 다음 섹션에서 설명하는 것처럼 [Liquid 변수](#message-personalization)를 참조할 수도 있습니다.

#### 이메일용 유기한 탐색 제품 개인화 {#abandoned-browse-product-personalization-for-emails}

다음은 유기한 탐색 이메일에 HTML 제품 블록을 추가하는 방법의 예시입니다.

{% raw %}
```java
<table aria-label="Abandoned browse product personalization for emails" style="width:100%">
  <tr>
    <th><img src="{{context.${image_url}}}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{context.${product_name}}}</li>
        <li>Price: ${{context.${price}}}</li>
      </ul>
    </th>
  </tr>
</table>
```
{% endraw %}

##### 제품 URL {#product-url}

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}

{% endtab %}
{% tab Abandoned cart %}

### 유기한 장바구니 {#abandoned-cart}

**유기한 장바구니** 템플릿을 사용하여 장바구니에 제품을 추가했지만 결제나 주문을 계속하지 않은 고객의 잠재적인 매출 손실에 대응하세요.

![확장된 "진입 규칙"이 포함된 적용된 "유기한 장바구니" Canvas 템플릿.]({% image_buster /assets/img_archive/abandoned_cart.png %})

#### 설정

Canvas 페이지에서 **Use a Canvas Template** > **Braze templates**를 선택한 다음 **유기한 장바구니** 템플릿을 적용합니다.

##### 기본 설정

Canvas에는 다음 설정이 미리 구성되어 있습니다:
- 기본 사항
    - Canvas 이름: **Abandoned cart**
    - 전환 이벤트: `ecommerce.order_placed`
        - 전환 마감일: 3일
- 진입 스케줄
    - 사용자가 **Perform Cart Updated Event**(드롭다운에 위치)를 트리거할 때 액션 기반 트리거
    - 시작 시간은 Canvas 템플릿을 생성하는 시점입니다<br><br>![Canvas의 "액션 기반 옵션".]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br>
- 타겟 오디언스
    - 진입 오디언스
        - 이 앱을 **0회 이상** 사용한 적이 있음
        - 이메일이 **비어 있지 않음**
    - 진입 제어
        - 사용자가 즉시 Canvas 진입 자격을 다시 얻음
    - 종료 기준
        - `ecommerce.cart_updated`, `ecommerce.checkout_started` 또는 `ecommerce.order_placed` 수행<br><br>![Canvas의 진입 제어 및 종료 기준.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br>
- 발송 설정
    - 가입했거나 옵트인한 사용자
- 지연 단계
     - 4시간 지연
- 메시지 단계
    - 이메일 템플릿과 HTML 블록을 Liquid 템플릿 예시와 함께 검토하여 미리 작성된 템플릿의 메시지에 제품을 추가하세요. 자체 이메일 템플릿을 사용하는 경우 다음 섹션에서 설명하는 것처럼 [Liquid 변수](#message-personalization)를 참조할 수도 있습니다.

#### 유기한 장바구니 재진입 로직 작동 방식 {#how-abandoned-cart-re-entry-logic-works}

사용자가 결제 프로세스를 시작하면 장바구니가 `checkout_started`로 표시됩니다. 그 시점 이후로 동일한 장바구니 ID를 사용하는 추가 장바구니 업데이트는 사용자가 유기한 장바구니 사용자 여정에 재진입할 자격을 부여하지 않습니다.

1. 사용자가 장바구니에 항목을 추가하면 Canvas에 진입합니다.
2. 항목을 추가하거나 업데이트할 때마다 Canvas에 재진입합니다—이를 통해 장바구니 데이터와 메시징이 최신 상태로 유지됩니다.
3. 사용자가 결제 프로세스를 시작하면 장바구니에 `checkout_started` 태그가 붙고 Canvas를 종료합니다.
4. 동일한 장바구니 ID를 사용하는 이후 장바구니 업데이트는 재진입을 트리거하지 않습니다. 이 장바구니가 이미 결제 단계로 이동했기 때문입니다.

사용자가 결제 사용자 여정으로 이동하면 대신 [유기한 결제 Canvas](#abandoned-checkout)의 타겟이 됩니다. 이 Canvas는 구매 여정에서 더 진행된 사용자를 위해 설계되었습니다.

#### 이메일용 유기한 장바구니 제품 개인화 {#abandoned-cart-checkout}

유기한 장바구니 사용자 여정에는 제품 개인화를 위한 특별한 `shopping_cart` Liquid 태그가 필요합니다.

다음은 `shopping_cart` Liquid 태그가 포함된 HTML 블록을 추가하여 이메일에 제품을 추가하는 방법의 예시입니다.

{% raw %}
```java
<table aria-label="Abandoned cart product personalization for emails #abandoned-cart-checkout" style="width:100%">
  {% shopping_cart {{context.${cart_id}}} %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

{% alert note %}
Shopify를 사용하는 경우 카탈로그 이름을 추가하여 배리언트 이미지 URL을 가져오세요.
{% endalert %}

##### HTML 장바구니 URL {#html-cart-url}

사용자를 장바구니로 다시 유도하려면 메타데이터 오브젝트 아래에 중첩된 이벤트 속성정보를 추가할 수 있습니다. 예를 들어:

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Shopify를 사용하는 경우 이 Liquid 템플릿을 사용하여 장바구니 URL을 생성하세요:

{% raw %}
```liquid
{{context.${source}}}/checkouts/cn/{{context.${cart_id}}}
```
{% endraw %}

{% endtab %}
{% tab Abandoned checkout %}

### 유기한 결제 {#abandoned-checkout}

**유기한 결제** 템플릿을 사용하여 결제 프로세스를 시작했지만 주문하기 전에 이탈한 고객을 타겟팅하세요.

![확장된 "진입 규칙"이 포함된 적용된 "유기한 결제" Canvas 템플릿.]({% image_buster /assets/img_archive/abandoned_checkout.png %})

#### 설정

Canvas 페이지에서 **Use a Canvas Template** > **Braze templates**를 선택한 다음 **유기한 결제** 템플릿을 적용합니다.

##### 기본 설정

Canvas에는 다음 설정이 미리 구성되어 있습니다:

- 기본 사항
    - Canvas 이름: **Abandoned checkout**
    - 전환 이벤트: `ecommerce.order_placed`
        - 전환 마감일: 3일
- 진입 스케줄
    - 사용자가 `ecommerce.checkout_started` 이벤트를 수행할 때 액션 기반 트리거
    - 시작 시간은 Canvas 템플릿을 생성하는 시점입니다<br><br>![Canvas의 "액션 기반 옵션".]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- 타겟 오디언스
    - 진입 오디언스
        - 이 앱을 **0회 이상** 사용한 적이 있음
        - 이메일이 **비어 있지 않음**
    - 진입 제어
        - 사용자가 즉시 Canvas 진입 자격을 다시 얻음
        - 종료 기준
            - `ecommerce.order_placed` 이벤트 수행<br><br>![Canvas의 진입 제어 및 종료 기준.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- 발송 설정
    - 가입했거나 옵트인한 사용자
- 지연 단계
    - 4시간 지연
- 메시지 단계
    - 이메일 템플릿과 HTML 블록을 Liquid 템플릿 예시와 함께 검토하여 미리 작성된 템플릿의 메시지에 제품을 추가하세요. 자체 이메일 템플릿을 사용하는 경우 다음 섹션에서 설명하는 것처럼 [Liquid 변수](#message-personalization)를 참조할 수도 있습니다.

#### 이메일용 유기한 결제 개인화 {#abandoned-checkout-personalization-for-emails}

유기한 결제 사용자 여정에는 제품 개인화를 위한 특별한 `shopping_cart` Liquid 태그가 필요합니다.

다음은 `shopping_cart` Liquid 태그가 포함된 HTML 블록을 추가하여 이메일에 제품을 추가하는 방법의 예시입니다.

{% raw %}
```java
<table aria-label="Abandoned checkout personalization for emails" style="width:100%">
  {% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
    {% endfor %}
</table>
```
{% endraw %}

##### `abort_if_not_abandoned` {#abort-if-not-abandoned}

`abort_if_not_abandoned` 파라미터는 유기한 결제 사용 사례에 특화되어 있으며, `ecommerce.checkout_started` 이벤트와 함께 `shopping_cart` Liquid 태그에서만 사용됩니다.

| 값 | 동작 |
| ----- | -------- |
| `true` (기본값) | 장바구니가 유기되지 않은 경우, 즉 사용자가 이후 주문을 완료한 경우 메시지가 중단됩니다. |
| `false` | 장바구니가 유기 상태가 아니더라도 메시지가 발송되어, 현재 결제 상태와 관계없이 이메일에 장바구니 세부 정보를 포함할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="abortifnotabandoned #abort-if-not-abandoned" }

발송 시점에 장바구니가 여전히 유기 상태인지 여부와 관계없이 결제 리마인더를 보내려면 `abort_if_not_abandoned`를 `false`로 설정하세요. 파라미터를 생략하거나 `true`로 설정하면 Braze는 이미 구매를 완료한 사용자에 대해 메시지를 중단합니다.

##### 결제 URL {#checkout-url}

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

{% endtab %}
{% tab Order confirmation and feedback survey %}

### 주문 확인 및 피드백 설문조사 {#order-confirmation-and-feedback-survey}

**주문 확인 및 피드백 설문조사** 템플릿을 사용하여 성공적인 주문을 확인하고 고객 만족을 향상시키세요.

![확장된 "진입 규칙"이 포함된 적용된 "주문 확인" Canvas 템플릿.]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

#### 설정

Canvas 페이지에서 **Use a Canvas Template** > **Braze templates**를 선택한 다음 **주문 확인 및 피드백 설문조사** 템플릿을 적용합니다.

##### 기본 설정

Canvas에는 다음 설정이 미리 구성되어 있습니다:

- 기본 사항
    - Canvas 이름: **Order confirmation with feedback survey**
    - 전환 이벤트: `ecommerce.session_start`
        - 전환 마감일: 10일
- 진입 스케줄
    - 사용자가 `ecommerce.cart_updated` 이벤트를 수행할 때 액션 기반 트리거
    - 시작 시간은 Canvas 템플릿을 생성하는 시점입니다<br><br>![Canvas의 "액션 기반 옵션".]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- 타겟 오디언스
    - 진입 오디언스
        - 이 앱을 **0회 이상** 사용한 적이 있음
        - 이메일이 **비어 있지 않음**
    - 진입 제어
        - 사용자가 즉시 Canvas 진입 자격을 다시 얻음
    - 종료 기준
        - 해당 없음<br><br>![Canvas의 추가 필터 및 진입 제어.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- 발송 설정
    - 가입했거나 옵트인한 사용자
- 메시지 단계
    - 이메일 템플릿과 HTML 블록을 Liquid 템플릿 예시와 함께 검토하여 미리 작성된 템플릿의 메시지에 제품을 추가하세요. 자체 이메일 템플릿을 사용하는 경우 다음 섹션에서 설명하는 것처럼 [Liquid 변수](#message-personalization)를 참조할 수도 있습니다.

#### 이메일용 주문 확인 개인화 {#order-confirmation-personalization-for-emails}

다음은 주문이 접수된 후 주문 확인에 HTML 제품 블록을 추가하는 방법의 예시입니다.

{% raw %}
```json
<table aria-label="Order confirmation personalization for emails" style="width:100%">
  {% for item in {{context.${products}}} %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200" /></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{item.product_name}}</li>
        <li>Price: {{item.price}}</li>
        <li>Quantity: {{item.quantity}}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

##### 주문 상태 URL {#order-status-url}

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

{% endtab %}
{% endtabs %}