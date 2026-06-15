---
nav_title: WSC Sports
article_title: WSC Sports
description: "이 참조 문서에서는 Braze와 WSC Sports 간의 파트너십에 대해 설명합니다. WSC Sports는 Braze 푸시 알림에 풍부하고 강력한 스포츠 미디어를 포함할 수 있게 해주는 스포츠 비디오 플랫폼입니다."
alias: /partners/wsc_sports/
page_type: partner
search_tag: Partner

---

# WSC Sports

> [WSC Sports](https://wsc-sports.com/) 플랫폼은 모든 디지털 플랫폼과 모든 스포츠 팬을 위해 개인화된 스포츠 비디오를 자동으로 실시간 생성합니다.

_이 통합은 WSC Sports에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 WSC Sports 통합을 통해 Braze 푸시 알림에 풍부하고 강력한 스포츠 미디어를 포함할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| WSC 계정 | 이 파트너십을 활용하려면 WSC 계정이 필요합니다. |
| Braze REST API 키 | **Messages**, **Segments**, **Campaigns** 및 **Canvas** 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **Settings** > **API Keys**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

WSC Sports 애플리케이션은 비디오 선택부터 최종 사용자의 기기에 푸시 알림이 도착하기까지의 전체 프로세스를 처리합니다.

### 1단계: 발송 설정 선택 {#step-1-select-send-settings}

![]({% image_buster /assets/img/wsc_sports/braze_integration.jpg %} "braze_integration.jpg"){: style="float:right;max-width:25%;margin-bottom:15px;"}

통합을 시작하기 전에 Braze에서 원하는 Campaign과 사용자 Segments가 구축되어 있는지 확인하세요. 완료되면 WSC Sports 플랫폼에서 원하는 비디오를 선택하고, 발송 설정에서 사용할 Braze 사용자 Segment 및 Campaign ID를 선택합니다. 마지막으로 푸시 메시지를 발송할 시간을 선택합니다.

#### API 호출 {#api-call}

발송되면 WSC Sports는 선택한 옵션에 따라 다음 Braze 엔드포인트를 사용하여 선택한 사용자 Segments에 푸시 알림을 전달합니다:
- [/messages/schedule/create]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/#create-scheduled-messages)
- [/messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#sending-messages-immediately-via-api-only)

결과 메시지 본문은 다음과 같습니다:
```
{
  "apple_push": {
    "alert": {
      "body": "Push Message Title"
    },
    "asset_url": "internalURI.mp4",
    "asset_file_type": "mp4"
  }
}
```

### 2단계: 테스트 발송 {#step-2-test-send}

이 시점에서 Campaign을 테스트하고 발송할 준비가 되어 있어야 합니다. 오류가 발생하면 Braze 오류 메시지 로그를 확인하세요.