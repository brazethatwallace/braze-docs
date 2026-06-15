---
nav_title: 전달 가능성의 함정 및 스팸 트랩
article_title: 전달 가능성의 함정 및 스팸 트랩
page_order: 7
page_type: reference
description: "이 참조 문서에서는 잠재적인 이메일 전달 가능성 함정, 스팸 트랩 및 이를 방지하는 방법에 대해 설명합니다."
channel: email

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"}전달 가능성의 함정 및 스팸 트랩 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomemail-onboarding-for-pro-and-enterprise-achieving-high-deliverability-stylefloatrightwidth120pxborder0-classnoimgborderdeliverability-pitfalls-and-spam-traps}

> 이 문서에서는 일반적인 이메일 전달 가능성 함정, 스팸 트랩 및 이를 방지하는 방법에 대해 설명합니다.

이메일 전달 가능성은 다음과 같은 스팸 트랩에 의해 영향을 받을 수 있습니다:

| 트랩 유형 | 설명 |
|---|---|
| 프리스타인 트랩 | 한 번도 사용된 적 없는 이메일 주소 및 도메인. |
| 재활용 트랩 | 원래는 실제 사용자였지만 현재는 휴면 상태인 이메일 주소. |
| 오타 트랩 | 일반적인 오타가 포함된 이메일 주소. |
| 스팸 신고 | 고객이 귀하의 이메일을 스팸으로 표시한 경우. |
| 높은 반송률 | 수신자의 주소가 유효하지 않아 이메일이 지속적으로 전달되지 않는 경우. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 스팸 트랩을 피하는 방법 {#how-to-avoid-spam-traps}

확인된 옵트인 프로세스를 설정하면 이러한 트랩을 피할 수 있습니다. 초기 옵트인 이메일을 보내고 고객에게 메시지 수신 여부를 확인하도록 요청하면, 수신자가 메시지를 받고 싶어하는지 그리고 실제 유효한 주소로 발송하고 있는지 확인할 수 있습니다. 스팸 트랩을 피하는 추가 방법은 다음과 같습니다:

1. 이중 옵트인 이메일을 보냅니다. 이 이메일은 사용자가 링크를 클릭하여 구독 선택을 확인해야 하는 이메일입니다.
2. 모범 사례로 [일몰 정책]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/)을 시행하세요.
3. **이메일 목록을 절대 구매하지 마세요.**

{% alert tip %}
Braze 고객 성공 및 전달 가능성 팀은 전 세계에서 전달 가능성을 극대화하기 위한 모범 사례를 따르고 있는지 확인할 수 있도록 도와드립니다.
{% endalert %}

## 반송 또는 스팸 목록에서 이메일 주소 제거하기 {#remove-an-email-address-from-your-bounce-or-spam-list}

다음 엔드포인트를 사용하여 반송된 이메일과 Braze 스팸 목록의 이메일을 제거할 수 있습니다:
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/)

## 이메일 전달 가능성 개선 {#improve-email-deliverability}

이메일 전달 가능성을 개선하기 위한 모범 사례는 [이메일 전달 가능성 개선]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability/)을 참조하세요.