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
| 스팸 신고 | 소비자가 이메일을 스팸으로 표시한 경우. |
| 높은 반송률 | 수신자의 주소가 유효하지 않아 이메일이 지속적으로 전달되지 않는 경우. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전달 가능성의 함정 및 스팸 트랩" }

## 스팸 트랩을 피하는 방법 {#how-to-avoid-spam-traps}

이러한 트랩은 확인된 옵트인 프로세스를 설정하면 피할 수 있습니다. 초기 옵트인 이메일을 보내고 가입자에게 메시지 수신을 원하는지 확인하도록 요청하면, 수신자가 실제로 여러분의 메시지를 원하고 있으며 실제 유효한 주소로 발송하고 있음을 보장할 수 있습니다. 스팸 트랩을 피하는 추가적인 방법은 다음과 같습니다:

1. 이중 옵트인 이메일을 보내세요. 이는 사용자가 링크를 클릭하여 가입 선택을 확인하도록 요구하는 이메일입니다.
2. 모범 사례로서 [일몰 정책]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies)을 구현하세요.
3. **절대로 이메일 목록을 구매하지 마세요.**

{% alert tip %}
Braze 고객 성공 및 전달 가능성 팀이 전 세계적으로 전달 가능성을 극대화하기 위한 모범 사례를 따르고 있는지 확인하는 데 도움을 드릴 수 있습니다.
{% endalert %}

## Microsoft 무료 이메일 도메인 차단을 해결하는 방법 {#how-to-resolve-a-free-email-domain-block-for-microsoft}

Microsoft는 무료 이메일 도메인(Hotmail, Live, MSN, Outlook)으로의 전달에 문제가 있는 발송자의 차단을 해제하는 경우가 드뭅니다. 대신, 해당 도메인으로의 발송량을 적극적으로 줄이고 최근에 참여한 연락처에만 발송하세요. 참여도가 높은 핵심 수신자 그룹을 식별할 수 없는 경우, 해당 도메인으로의 발송을 완전히 중단하세요.

무료 이메일 도메인 차단 메시지의 예시는 다음과 같습니다:

`550 5.7.1 Unfortunately, messages from [xx.xx.xx.xx] weren't sent. Please contact your Internet service provider since part of their network is on our block list (S3150). You can also refer your provider to: http://mail.live.com/mail/troubleshooting.aspx#errors.`

[IP 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)과 유사하게 발송량을 천천히 늘리면서 측정기준을 면밀히 모니터링할 수 있습니다. 전달 가능성 문제에는 대개 식별하고 해결해야 할 근본 원인이 있습니다. 일반적으로 이는 적절한 권한 부족, 지속적인 이메일 목록 관리 부족, 또는 이 두 가지 요인의 조합입니다.

## 반송 또는 스팸 목록에서 이메일 주소 제거하기 {#remove-an-email-address-from-your-bounce-or-spam-list}

다음 엔드포인트를 사용하여 반송된 이메일과 Braze 스팸 목록에 있는 이메일을 제거할 수 있습니다:

- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)

## 이메일 전달 가능성 개선 {#improve-email-deliverability}

자세한 내용은 [이메일 전달 가능성 개선]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability)을 참조하세요.

## BIMI

BIMI(메시지 식별을 위한 브랜드 표시기)에 대해서는 [이메일 인증]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication)을 참조하세요.