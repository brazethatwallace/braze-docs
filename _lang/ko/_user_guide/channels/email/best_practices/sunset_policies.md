---
nav_title: 일몰 정책
article_title: 이메일 일몰 정책
page_order: 8
page_type: reference
description: "이 문서에서는 일몰 정책에 관한 모범 사례와 참여하지 않는 사용자에게 메시지 발송을 중단하는 것이 더 나은 상황을 이해하는 방법을 다룹니다."
channel: email

---

# 일몰 정책 {#sunset-policies}

> 최대한 많은 사용자에게 Campaign을 보내고 싶을 수도 있지만, 실제로는 참여하지 않는 사용자에게 메시지를 보내는 것을 중단하는 것이 유리한 경우가 있습니다.

이메일의 경우 발신 IP와 도메인 평판은 참여도, 스팸 신고, 차단 목록 등에 영향을 받습니다. 평판이 지속적으로 낮으면 ISP 및 사서함 필터가 비활성 수신자뿐만 아니라 모든 수신자에 대해 이메일을 스팸 또는 우선순위가 낮은 폴더로 분류할 수 있습니다. 일몰 정책은 참여하지 않는 사용자에 대한 지속적인 발송을 제한하여 평판을 보호하는 데 도움이 됩니다. 정기적인 모니터링과 함께 사용하면 문제를 조기에 발견할 수 있습니다.

## IP 및 도메인 상태 모니터링 {#monitor-ip-and-domain-health}

[전달 가능성 센터]({{site.baseurl}}/user_guide/analytics/dashboards/deliverability_center)를 사용하여 메일박스 공급자가 발송을 어떻게 인식하는지 추적하세요:

- **Google Postmaster Tools**(계정 연결 후): Gmail 관련 가시성을 위한 IP 평판, 도메인 평판, 전달 오류, 인증(SPF, DKIM, DMARC) 및 암호화 측정기준.
- **Microsoft Smart Network Data Services(SNDS)**(IP에 대해 구성된 경우): 필터 결과, 불만 비율, 스팸 트랩 히트를 포함한 Outlook 및 Microsoft 메일박스 IP 상태.

보다 광범위한 발송 위생 관리에 대해서는 [이메일 전달 가능성 개선]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability) 및 [전달 가능성 함정과 스팸 트랩]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps)을 참조하세요.

추가 신호를 위해 Braze 외부에서 [Sender Score](https://www.senderscore.org/) 또는 [Outlook Smart Network Data Services](https://postmaster.live.com/snds/)와 같은 외부 도구를 레버리지할 수도 있습니다.

## 억제 목록 사용 {#use-suppression-lists}

[억제 목록]({{site.baseurl}}/user_guide/audience/suppression_lists)은 Segment 필터로 정의된 사용자 그룹으로, 타겟 Segment에 포함되더라도 기본적으로 Campaign이나 Canvases를 수신하지 않습니다. 비활성 또는 참여하지 않는 수신자에 대해 억제 목록은 워크스페이스 전체에 적용되는 안전장치 역할을 합니다. 사용자가 비활성 기준을 충족하면, 모든 Segment나 Campaign을 일일이 수정하지 않아도 대부분의 메시징 수신이 중단됩니다.

선셋 정책에 맞추려면, 더 이상 지속적인 프로모션 이메일을 받지 않아야 하는 사용자를 포착하는 필터(예: `Last Engaged With Message` 또는 **리타겟팅** 아래의 기타 필터)를 사용하여 억제 목록을 구성하세요. 정책에서 "미참여"로 정의한 것과 동일한 조회 기간 및 채널 선택을 적용합니다. 멤버십은 동적이므로, 사용자는 필터 조건을 충족하면 목록에 추가되고 다시 참여하면 목록에서 제외됩니다.

최종 윈백 메시지나 승인된 트랜잭션 여정 등 특정 발송이 비활성 사용자에게 도달하도록 하려면, 억제 목록에 예외 태그를 설정하여 해당 태그가 지정된 Campaign이나 Canvases가 타겟 오디언스에 포함된 사용자에게 계속 전달되도록 합니다. 억제 목록은 세분화와 함께 작동하며, 세분화를 통해 발송에 포함할 대상을 정의할 수 있습니다. 설정 단계, 권한 및 제한 사항에 대해서는 [억제 목록 설정]({{site.baseurl}}/user_guide/audience/suppression_lists#setup)을 참조하세요.

## 세분화 필터 사용하기 {#use-segmentation-filters}

세분화 필터는 이메일, 푸시, 인앱 알림에 대한 일몰 정책을 쉽게 구현할 수 있도록 하여 메시징이 스팸처럼 보이는 것을 방지하는 데 도움이 됩니다. 일몰 정책을 만들 때 고려해야 할 사항은 다음과 같습니다:

- "참여하지 않는" 사용자의 기준은 무엇인가요?
- 참여는 클릭, 구매, 앱 사용 또는 이러한 행동의 조합으로 정의되나요?
- 메시지 발송을 중단하기까지 참여 공백 기간이 얼마나 되어야 하나요?
- Segments에서 제외하기 전에 사용자에게 특별한 Campaigns를 전달할 예정인가요?
- 일몰 정책이 적용될 메시징 채널은 무엇인가요?

예를 들어, [Apple의 MPP(Mail Privacy Protection)]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/mpp)에 옵트인한 사용자가 있는 경우, 이것이 이메일 Campaigns와 전달 가능성 측정기준에 어떤 영향을 미칠 수 있는지 고려하고 일몰 정책을 가장 잘 구성하는 방법을 결정하세요.

일몰 정책을 Campaigns에 적용하려면, 이메일을 스팸으로 표시했거나 일정 기간 동안 메시지와 상호작용하지 않은 사용자를 자동으로 제외하는 [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)를 만드세요.

이러한 Segments를 설정하려면, 필터 드롭다운의 **리타겟팅** 섹션에 있는 `Has Marked You As Spam` 및 `Last Engaged With Message` 필터를 선택하세요.

`Last Engaged With Message` 필터를 적용할 때, 사용자가 상호작용했거나 상호작용하지 않은 메시징 유형(푸시, 이메일 또는 인앱 알림)과 사용자가 마지막으로 상호작용한 이후 경과한 일수를 지정하세요. Segment를 만든 후, 이 Segment를 원하는 [메시징 채널]({{site.baseurl}}/user_guide/channels)로 타겟팅하세요.

!["Last Engaged with Message" 필터가 선택된 Segment 세부 정보 페이지.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Braze는 스팸으로 표시한 사용자에게 자동으로 이메일 발송을 중단하지만, `Has Marked You As Spam` 필터를 사용하면 이러한 사용자에게 타겟팅된 푸시 메시지와 인앱 알림도 보낼 수 있습니다. 이 필터는 [리타겟팅 Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns)에 유용합니다. 예를 들어, 참여하지 않는 사용자에게 이메일을 열지 않을 때 놓치고 있는 기능과 혜택을 상기시키는 메시지를 보낼 수 있습니다.

일몰 정책은 휴면 사용자를 타겟팅하는 이메일 Campaigns에서 특히 유용할 수 있습니다. 이러한 Campaigns는 일정 기간 동안 앱과 상호작용하지 않은 Segments에 초점을 맞추지만, 참여하지 않는 수신자를 반복적으로 포함하면 이메일 전달 가능성이 위험에 처할 수 있습니다. 일몰 정책을 사용하면 스팸 폴더에 들어가지 않으면서 휴면 사용자를 타겟팅할 수 있습니다.