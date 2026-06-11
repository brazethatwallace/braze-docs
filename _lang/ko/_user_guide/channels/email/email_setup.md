---
nav_title: "설정"
article_title: 이메일 설정
layout: dev_guide
page_order: 0
guide_top_header: "이메일 설정"
guide_top_text: "Braze는 이메일 캠페인 발송을 시작하는 데 도움을 줄 수 있습니다. 가이드를 따르거나 <a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>이메일 온보딩</a> Braze 학습 과정을 확인하세요."
page_type: landing
description: "이 랜딩 페이지에는 IP 및 도메인 설정, IP 워밍, 이메일 유효성 검사 등 이메일 캠페인 시작에 필요한 리소스가 포함되어 있습니다."
channel: email

guide_featured_title: "섹션 문서"
guide_featured_list:
- name: "IP 및 도메인 설정"
  link: /docs/user_guide/channels/email/email_setup/setting_up_ips_and_domains
  image: /assets/img/braze_icons/target-05.svg
- name: "IP 워밍"
  link: /docs/user_guide/channels/email/email_setup/ip_warming
  image: /assets/img/braze_icons/annotation-alert.svg
- name: "이메일 유효성 검사"
  link: /docs/user_guide/channels/email/email_setup/email_validation
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "이메일 인증"
  link: /docs/user_guide/channels/email/email_setup/authentication
  image: /assets/img/braze_icons/user-square.svg
- name: "이메일 목록 가져오기"
  link: /docs/user_guide/channels/email/email_setup/import_your_email_list
  image: /assets/img/braze_icons/list.svg
- name: "SSL 개요"
  link: /docs/user_guide/channels/email/email_setup/ssl
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: "동의 및 주소 수집"
  link: /docs/user_guide/channels/email/email_setup/consent_and_address_collection
  image: /assets/img/braze_icons/book-closed.svg
- name: "전달 가능성의 함정 및 스팸 트랩"
  link: /docs/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps
  image: /assets/img/braze_icons/alert-triangle.svg
- name: "오픈 픽셀 및 클릭 추적"
  link: /docs/user_guide/channels/email/email_setup/open_pixel_and_click_tracking
  image: /assets/img/braze_icons/cursor-click-02.svg
---

## 요구 사항 {#requirements}

이메일 발송을 시작하기 전에 준비해야 할 사항이 있습니다. 다음 표를 참고하여 이러한 요구 사항에 대해 자세히 알아보세요.

| 요구 사항 | 설명 | 소스 |
|---|---|---|
| 전용 IP(인터넷 프로토콜) | 전용 IP는 단일 호스팅 계정에만 제공되는 고유한 인터넷 주소입니다. | Braze는 이메일 발신자 평판을 제어할 수 있도록 전용 IP를 제공합니다. Braze 온보딩에서 이를 설정해 드립니다.|
| 화이트라벨 도메인 | 도메인과 하위 도메인으로 구성됩니다. 화이트라벨링을 사용하면 DKIM 및 SPF에 대한 이메일 인증 검사를 통과할 수 있습니다. | Braze 온보딩 팀에서 이러한 도메인을 생성해 드리지만, 도메인의 이름은 직접 선택해야 합니다. |
| 하위 도메인 | 이메일 주소 내 도메인의 하위 구분(예: "@news.company.com")입니다. 하위 도메인이 있으면 회사의 공식 이메일 평판을 손상시킬 수 있는 오류를 방지할 수 있습니다. | 온보딩 팀에서 생성해 드리지만 하위 도메인의 이름은 직접 정해야 합니다. 현재 Braze 외부에서 사용 중인 하위 도메인은 사용할 수 없습니다. |
| IP 풀 | 서로 다른 유형의 이메일(예: "프로모션"과 "트랜잭션")의 평판을 분리하여 한쪽의 평판이 다른 쪽에 영향을 미치지 않도록 하고 더 높은 전달 가능성을 지원하는 데 사용되는 선택적 구성입니다. | 온보딩 팀에서 풀을 설정해 드립니다. 그런 다음 이메일을 작성할 때 **타겟 오디언스** 단계에서 이메일의 IP 풀을 확인할 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requirements" }

## IP 워밍 {#ip-warming}

{% alert important %}
IP 워밍은 이메일 설정 과정에서 **가장 중요한 단계**입니다. 첫 번째 단계는 아니지만(실제로는 마지막 단계입니다), 여기서 미리 안내드리는 이유는 IP 주소를 반드시 워밍해야 하기 때문입니다. 그렇지 않으면 발송하는 이메일이 스팸으로 분류되거나 기타 발송 장벽에 부딪힐 수 있습니다.
{% endalert %}

[IP 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/)은 첫 번째 배치에서 비교적 적은 수의 이메일을 발송한 후, 시간이 지남에 따라 이후 배치에서 발송량을 점진적으로 늘려 일반적인 일일 발송량에 도달하는 과정입니다. 이 작업은 이메일 설정 과정의 맨 마지막에 수행됩니다.

적은 양의 이메일부터 시작하면 이메일 제공업체와의 신뢰 수준을 구축하여 관련성 있는 사용자에게만 이메일을 보내고 있음을 보여줄 수 있습니다. 첫 번째 배치를 가장 참여도가 높은 사용자에게 발송하면 제공업체와의 신뢰를 더 빠르게 확보하는 데 도움이 됩니다.

IP 워밍이 완료되면 [이메일 작성 및 발송을 시작]({{site.baseurl}}/user_guide/channels/email/html_editor/)할 수 있습니다!

## 법적으로 필수인 트랜잭션 이메일 {#legally-required-transactional-emails}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

<br><br>