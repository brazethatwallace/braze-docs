---
nav_title: 전달 가능성 함정 및 스팸 트랩
article_title: 전달 가능성 함정 및 스팸 트랩
page_order: 7
page_type: reference
description: "이 참조 문서에서는 잠재적인 이메일 전달 가능성 함정, 스팸 트랩 및 이를 방지하는 방법을 다룹니다."
channel: email

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"}전달 가능성 함정 및 스팸 트랩

이메일 전달 가능성은 다음과 같은 스팸 트랩의 영향을 받을 수 있습니다:

| 트랩 유형 | 설명 |
|---|---|
| 프리스틴 트랩 | 한 번도 사용된 적이 없는 이메일 주소 및 도메인입니다. |
| 재활용 트랩 | 원래 실제 사용자였지만 현재는 비활성 상태인 이메일 주소입니다. |
| 오타 트랩 | 일반적인 오타가 포함된 이메일 주소입니다. |
| 스팸 신고 | 고객이 이메일을 스팸으로 표시한 경우입니다. |
| 높은 반송률 | 수신자의 주소가 유효하지 않아 이메일이 지속적으로 전달되지 않는 경우입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 스팸 트랩을 방지하는 방법

확인된 옵트인 프로세스를 설정하면 이러한 트랩을 방지할 수 있습니다. 초기 옵트인 이메일을 보내고 고객에게 메시지 수신을 원하는지 확인하도록 요청하면, 수신자가 여러분의 메시지를 원하고 있으며 실제 유효한 주소로 발송하고 있음을 보장할 수 있습니다. 스팸 트랩을 방지하는 추가 방법은 다음과 같습니다:

1. 이중 옵트인 이메일을 보내세요. 이는 사용자가 링크를 클릭하여 구독 선택을 확인하도록 요구하는 이메일입니다.
2. 모범 사례로 [일몰 정책]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/)을 구현하세요.
3. **절대 이메일 목록을 구매하지 마세요.**

{% alert tip %}
Braze 고객 성공 및 전달 가능성 팀이 전 세계적으로 전달 가능성을 극대화하기 위한 모범 사례를 따르도록 도와드릴 수 있습니다.
{% endalert %}

## 반송 또는 스팸 목록에서 이메일 주소 제거

다음 엔드포인트를 사용하여 반송된 이메일과 Braze 스팸 목록에 있는 이메일을 제거할 수 있습니다:
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)

## 이메일 전달 가능성 개선

이메일 전달 가능성을 개선하기 위한 모범 사례는 [이메일 전달 가능성 개선]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability/)을 참조하세요.