---
nav_title: Friendbuy
article_title: Friendbuy
description: "Friendbuy와 Braze를 통합하는 방법을 알아보세요."
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# Friendbuy

> [Friendbuy](https://www.friendbuy.com/)와 Braze의 통합을 사용하여 이메일 및 단문 메시지 서비스 기능을 확장하는 동시에 추천 및 로열티 프로그램 커뮤니케이션을 손쉽게 자동화할 수 있습니다. Braze는 Friendbuy를 통해 수집된 모든 옵트인 전화번호에 대해 고객 프로필을 생성합니다.

_이 통합은 Friendbuy에서 유지 관리합니다._

## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다:

| 요구 사항 | 설명 |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Friendbuy 계정 | 이 파트너십을 활용하려면 [Friendbuy 계정](https://retailer.friendbuy.io/)이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)은 Braze 인스턴스의 URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Friendbuy 통합하기 {#integrating-friendbuy}

[Friendbuy](https://retailer.friendbuy.io/)에서 **Developer Center** > **Integrations**로 이동한 다음, Braze 통합 카드에서 **Add integration**을 선택합니다.

![Friendbuy의 Braze 통합 카드.]({% image_buster /assets/img/friendbuy/choosing_braze.png %}){: style="max-width:75%;"}

양식에 REST 엔드포인트와 API 키를 입력한 다음, **Install Integration**을 선택합니다.

![Friendbuy 통합 양식.]({% image_buster /assets/img/friendbuy/install_form.png %}){: style="max-width:55%;"}

[Friendbuy 계정](https://retailer.friendbuy.io/)으로 돌아가서 페이지를 새로고침합니다. 통합이 성공적으로 완료되면 다음과 유사한 메시지가 표시됩니다:

![통합 설치 완료]({% image_buster /assets/img/friendbuy/install_success.png %}){: style="max-width:55%;"}

### 커스텀 속성 {#custom-attributes}

| 커스텀 속성 이름 | 정의 | 데이터 유형 |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Friendbuy Referral Status** | 추천인은 *Advocate*로, 피추천인은 *Referred Friend*로 분류됩니다. | 문자열 |
| **Friendbuy Customer Name** | 고객이 추천 위젯을 통해 정보를 제출할 때 입력한 이름입니다. | 문자열 |
| **Friendbuy Referral Link** | Advocate를 위해 생성된 개인 추천 링크(PURL)입니다. 예: https://fbuy.io/EzcW | 문자열 |
| **Friendbuy Date of Last Share** | Advocate가 공유 채널을 통해 Friend에게 마지막으로 공유한 날짜와 시간입니다. Advocate가 아직 공유하지 않은 경우 이 등록정보는 표시되지 않습니다. | 시간 |
| **Friendbuy Campaign ID** | Advocate를 위해 생성된 개인 추천 링크와 연결된 Campaign ID입니다. | 문자열 |
| **Friendbuy Campaign Name** | Advocate를 위해 생성된 개인 추천 링크와 연결된 Campaign 이름입니다. | 문자열 |
| **Friendbuy Coupon Code** | 고객에게 배포된 가장 최근의 추천 쿠폰 코드입니다. 참고: 하나의 코드만 표시됩니다. | 문자열 |
| **Friendbuy Coupon Value** | 고객에게 배포된 가장 최근 쿠폰 코드의 통화 가치입니다. | 숫자 |
| **Friendbuy Coupon Status** | 고객에게 배포된 가장 최근 쿠폰 코드의 상태입니다. 참고: 상태는 'distributed' 또는 'redeemed'입니다. | 문자열 |
| **Friendbuy Coupon Currency** | 고객에게 배포된 가장 최근 쿠폰 코드와 연결된 통화 코드(USD, CAD 등) 또는 퍼센트(%)입니다. | 문자열 |
| **Friendbuy Coupon Campaign ID** | 고객을 위해 생성된 쿠폰 코드와 연결된 Campaign ID입니다. | 문자열 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="커스텀 속성" }

## 기본 동작 {#default-behavior}

고객 데이터를 Braze로 전송하기 전에, 고객은 추천 위젯에서 다음 체크박스 중 하나 이상을 선택하여 옵트인해야 합니다:

![추천 위젯]({% image_buster /assets/img/friendbuy/referral_widget.png %})

{% alert note %}
Friendbuy는 국제 표준(E.164)을 사용하여 실제 전화번호를 확인합니다. `555-555-5555`와 같은 유효하지 않은 번호는 Braze로 전송되지 않습니다.
{% endalert %}

### 체크박스 동작 {#checkbox-behavior}

| 선택된 체크박스 | 동작 |
|-------------------|-----------------------------------------------------------------|
| 이메일만 | 고객의 이메일 주소만 Braze로 전송됩니다. |
| 전화번호만 | 고객의 전화번호만 Braze로 전송됩니다. |
| 둘 다 선택하지 않음 | 고객 데이터가 Braze로 전송되지 않습니다. |
| 둘 다 선택 | 고객의 이메일 주소와 전화번호가 Braze로 전송됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Checkbox behavior" }