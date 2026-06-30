---
nav_title: 캠페인 데이터
article_title: 캠페인 데이터 내보내기
page_order: 2
page_type: reference
description: "이 참조 문서에서는 단일, 다중 채널 또는 다변량 Campaign에서 Campaign 결과 데이터를 내보내는 방법에 대해 설명합니다. 이 문서에는 수신자로부터 사용자 데이터를 내보내는 방법도 나와 있습니다."
tool:
  - Campaigns
  - Reports

---

# 캠페인 데이터 내보내기 {#export-campaign-data}

> 대시보드의 **Campaigns** 페이지에서 보려는 Campaign을 선택하고 아래로 스크롤하여 내보낼 수 있는 과거 성과 그래프까지 이동합니다.<br><br>이 페이지에서는 단일, 다중 채널 및 다변량 Campaign에서 Campaign 결과 데이터를 내보내는 방법과 수신자의 사용자 데이터를 내보내는 방법에 대해 설명합니다.

## 멀티채널 Campaign {#multichannel-campaigns}

멀티채널 Campaign의 경우 내보낼 수 있는 데이터는 사용한 메시징 채널에 따라 달라집니다. 다음은 iOS 푸시, Android 푸시, 이메일 및 인앱 메시지를 사용한 Campaign에서 내보낼 수 있는 모든 데이터의 목록입니다.

- 날짜별 전송 메시지
    - 총 전송 메시지 수
    - Campaign 채널별 전송 메시지(푸시, 이메일, 인앱 메시지 포함 가능)
- 날짜별 이메일 메시지 참여
    - 전달된 이메일 수
    - 전송된 이메일 수
    - 열람된 이메일 수
    - 이메일 클릭 수
    - 이메일 반송 수
    - 스팸으로 신고된 이메일 수
- 날짜별 인앱 메시지 참여
    - 전송된 인앱 메시지 수
    - 인앱 메시지 노출 횟수
    - 인앱 메시지 클릭 수
- 날짜별 iOS 푸시 참여
    - iOS 푸시 알림 전송 수
    - 총 열람 수
    - 직접 열람 수
    - 반송 수
- 날짜별 Android 푸시 참여
    - Android 푸시 알림 전송 수
    - 총 열람 수
    - 직접 열람 수
    - 반송 수

## 다변량 Campaign {#multivariate-campaigns}

하나의 메시징 채널만 사용하는 다변량 Campaign의 경우, 시간 경과에 따른 특정 메시징 채널의 분석에서 각 배리언트가 어떤 성과를 보였는지 나타내는 데이터를 내보낼 수 있습니다. 이 데이터를 통계별로 그룹화하거나 메시지 배리언트별로 그룹화하여 볼 수 있습니다.

푸시 Campaign 결과에는 다음 분석에 대한 그래프가 포함됩니다.

- 각 배리언트의 날짜별 전송 메시지
- 각 배리언트의 날짜별 전환
- 각 배리언트의 날짜별 고유 수신자
- 각 배리언트의 날짜별 열람
- 각 배리언트의 날짜별 직접 열람
- 각 배리언트의 날짜별 반송

이메일 Campaign 결과에는 다음 분석에 대한 그래프가 포함됩니다.

- 각 배리언트의 날짜별 전달 수
- 각 배리언트의 날짜별 전송 수
- 각 배리언트의 날짜별 열람
- 각 배리언트의 날짜별 클릭 수
- 각 배리언트의 날짜별 반송
- 각 배리언트의 날짜별 스팸 신고

인앱 메시지 Campaign 결과에는 다음 분석에 대한 그래프가 포함됩니다.

- 각 배리언트의 날짜별 전송
- 각 배리언트의 날짜별 노출 횟수
- 각 배리언트의 날짜별 클릭 수

## Campaign 수신자 {#campaign-recipients}

Campaign의 모든 수신자에 대한 사용자 데이터를 CSV 파일로 내보낼 수 있습니다. 이렇게 하려면 **Campaign Details** 섹션에서 **User Data** 버튼을 선택합니다.

{% alert note %}
**User Data** 버튼이 보이지 않나요? 사용자 데이터를 내보내려면 해당 워크스페이스에 대한 **Export User Data** [권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#limited-and-team-role-permissions)이 필요합니다.
{% endalert %}

![Campaign Details 페이지의 User Data 드롭다운]({% image_buster /assets/img/campaign_export_example.png %})

CSV 출력에는 Campaign의 모든 수신자에 대한 고객 프로필 데이터가 포함됩니다. Braze는 백그라운드에서 보고서를 생성하여 현재 로그인한 사용자에게 이메일로 전송합니다.

[Amazon S3 인증정보]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)를 Braze에 연결한 경우 CSV가 S3 버킷에도 업로드됩니다. 그렇지 않으면 이메일로 전송된 링크가 몇 시간 후에 만료됩니다.

내보낸 파일에는 [Segment의 사용자 데이터를 내보낼 때]({{site.baseurl}}/user_guide/analytics/dashboards/home#exporting-app-usage-data) 포함되는 것과 동일한 사용자 데이터 필드가 포함됩니다. 이러한 데이터 필드 외에도 "모든 수신자 데이터 내보내기"를 선택하면 내보낸 파일에 각 사용자에 대한 다음 데이터도 포함됩니다.

- 수신된 Campaign 배리언트 이름
- 수신된 Campaign 배리언트의 API ID
- 사용자가 대조군에 속해 있는지 여부

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)을 참조하세요.
{% endalert %}