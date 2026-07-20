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

이메일의 경우 발신 IP에는 참여도, 스팸 신고, 차단 목록 등을 고려한 평판 점수가 있습니다. [Sender Score](https://www.senderscore.org/)나 [Outlook의 Smart Network Data Service](https://postmaster.live.com/snds/) 같은 도구를 사용하여 평판 점수를 모니터링할 수 있습니다. 평판 점수가 지속적으로 낮으면 ISP 및 사서함 필터가 참여 중인 수신자를 포함하여 모든 수신자에 대해 자동으로 이메일을 스팸 또는 우선순위가 낮은 폴더로 분류할 수 있습니다. 일몰 정책을 만들면 활성 수신자에게만 이메일을 전송하는 데 도움이 됩니다.

세분화 필터를 사용하면 이메일, 푸시 및 인앱 알림에 대한 일몰 정책을 쉽게 구현하여 메시지가 스팸으로 표시되는 것을 방지할 수 있습니다. 다음은 일몰 정책을 만들 때 고려해야 할 몇 가지 사항입니다:

- 무엇이 "참여하지 않는" 사용자로 간주되나요?
- 참여는 클릭, 구매, 앱 사용 또는 이러한 동작의 조합으로 정의되나요?
- 메시지 전송을 중단하려면 얼마나 오래 참여하지 않아야 하나요?
- Segment에서 제외하기 전에 사용자에게 특별한 Campaign을 제공하나요?
- 어떤 메시징 채널에 일몰 정책이 적용되나요?

예를 들어, [Apple의 MPP]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/mpp)에 옵트인한 사용자가 있는 경우, 이것이 이메일 Campaign과 전달 가능성 측정기준에 어떤 영향을 미칠 수 있는지 고려하고 일몰 정책을 가장 잘 구성하는 방법을 결정하세요.

Campaign에 일몰 정책을 적용하려면, 이메일을 스팸으로 표시했거나 일정 기간 동안 메시지와 상호작용하지 않은 사용자를 자동으로 제외하는 [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)를 만드세요.

이러한 Segment를 설정하려면, 필터 드롭다운의 **리타겟팅** 섹션에 있는 `Has Marked You As Spam` 및 `Last Engaged With Message` 필터를 선택하세요.

`Last Engaged With Message` 필터를 적용할 때, 사용자가 상호작용했거나 상호작용하지 않은 메시징 유형(푸시, 이메일 또는 인앱 알림)과 사용자가 마지막으로 상호작용한 이후 경과한 일수를 지정하세요. Segment를 만든 후, 이 Segment를 원하는 [메시징 채널]({{site.baseurl}}/user_guide/channels)로 타겟팅하세요.

!["Last Engaged with Message" 필터가 선택된 Segment 세부 정보 페이지.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Braze는 스팸으로 표시한 사용자에게 자동으로 이메일 발송을 중단하지만, `Has Marked You As Spam` 필터를 사용하면 이러한 사용자에게 타겟팅된 푸시 메시지와 인앱 알림을 보낼 수도 있습니다. 이 필터는 [리타겟팅 Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns)에 유용합니다. 예를 들어, 참여하지 않는 사용자에게 이메일을 열지 않을 때 놓치고 있는 기능과 혜택을 상기시키는 메시지를 보낼 수 있습니다.

일몰 정책은 휴면 사용자를 타겟팅하는 이메일 Campaign에서 특히 유용할 수 있습니다. 이러한 Campaign은 일정 기간 동안 앱과 상호작용하지 않은 Segment에 초점을 맞추지만, 참여하지 않는 수신자를 반복적으로 포함하면 이메일 전달 가능성이 위험에 처할 수 있습니다. 일몰 정책을 사용하면 스팸 폴더에 들어가지 않으면서 휴면 사용자를 타겟팅할 수 있습니다.