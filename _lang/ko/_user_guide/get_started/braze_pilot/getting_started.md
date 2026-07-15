---
nav_title: 시작하기
article_title: Braze Pilot 시작하기
page_order: 2
page_type: reference
description: "이 참조 문서에서는 엔지니어 또는 개발자에게 필요한 통합 단계에 대해 간략하게 설명합니다."
---

# Braze Pilot 시작하기 {#get-started-with-braze-pilot}

> 이 문서에서는 Braze Pilot 사용을 시작하는 방법을 다룹니다. 앱 다운로드, Braze 대시보드와의 연결 초기화, 설정 완료까지의 과정을 단계별로 안내해 드리겠습니다.

## 1단계: Braze Pilot 다운로드 {#step-1-download-braze-pilot}

Braze Pilot을 사용하려면 먼저 Apple 앱 스토어 또는 Google Play Store에서 앱을 다운로드해야 합니다. 앱 스토어에서 앱을 검색하거나 아래 섹션의 QR 코드를 스캔하여 기기에 맞는 앱 페이지로 이동할 수 있습니다.

## 2단계: 이용 약관 동의 {#step-2-accept-the-terms-and-conditions}

다음으로 이용 약관에 동의한 후, 양식에 업무용 이메일을 입력하세요. 이메일은 앱 사용 분석 목적으로만 사용되며, 마케팅 목적으로는 사용되지 않습니다.

![Braze Pilot 환영 페이지.]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"} ![업무용 이메일 주소를 입력하는 옵션.]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## 3단계: Braze SDK와의 연결 초기화 {#step-3-initialize-the-connection-with-the-braze-sdk}

Braze Pilot을 사용하면 모든 Braze 대시보드에 대해 Braze SDK를 초기화할 수 있습니다. SDK가 초기화되면 Pilot은 인게이지먼트 데이터를 Braze로 전송하기 시작하며, 해당 Braze 대시보드에서 실행된 모든 메시징을 트리거할 수 있습니다.

Pilot에서 SDK 연결을 구성하는 방법은 두 가지입니다: 데모 QR 코드와 설정 마법사입니다.

{% tabs local %}
{% tab 데모 QR 코드 %}

### 방법 1: 데모 QR 코드 {#method-1-demo-qr-codes}

SDK 초기화에 필요한 모든 세부 정보가 포함된 QR 코드를 스캔하면 고객 프로필이 생성되고, Braze Pilot 내 특정 앱 시뮬레이션으로 딥링크됩니다. 데모 QR 코드는 무료 평가판의 특정 데모 Campaign에 대한 컴패니언 드로어에 표시됩니다.

| Android용 Pilot | iOS용 Pilot |
| --- | --- |
| ![Android용 QR 코드.]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | ![iOS용 QR 코드.]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="방법 1: 데모 QR 코드" }

{% endtab %}
{% tab 설정 마법사 %}

### 방법 2: 설정 마법사 {#method-2-setup-wizard}

Braze 대시보드의 **앱 설정** 페이지에서 대시보드 워크스페이스와의 연결을 초기화하는 단계별 가이드를 따르세요.

![Braze Pilot 설정 마법사의 1단계.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

이 연결은 워크스페이스별로 적용됩니다. 즉, 데모 워크스페이스에서 연결을 초기화한 후 무료 평가판 대시보드의 라이브 워크스페이스로 전환하면, 해당 워크스페이스에서 실행된 Campaign을 수신하려면 SDK를 다시 초기화해야 합니다.

![Braze 대시보드의 워크스페이스 드롭다운에서 "Demo - Braze"가 활성 워크스페이스로 선택된 모습.]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## 4단계: 푸시 권한 허용 {#step-4-allow-push-permissions}

마지막으로, 앱을 통해 푸시 기능을 테스트하려면 앱이 푸시 알림을 보낼 수 있도록 허용하는 것이 좋습니다. 다음과 같은 방법으로 앱에 권한을 부여할 수 있습니다: 기기 설정에서 앱 설정을 업데이트하거나, Braze에서 앱으로 푸시 프라이머 메시지를 실행하는 방법입니다.

{% tabs local %}
{% tab 앱 설정 업데이트 %}

기기 설정을 열고 Braze Pilot을 찾으세요. 그런 다음, 잠금 화면에 알림이 표시되도록 설정을 업데이트하세요.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/device_settings.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab 푸시 프라이머 메시지 실행 %}

일반 소비자에게 하는 것처럼 Braze 인앱 메시지를 사용하여 앱에 대한 푸시 권한을 요청할 수 있습니다. Braze에서 이러한 유형의 메시지를 구축하는 방법은 [푸시 프라이머 인앱 메시지]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages#push-primer-in-app-messages)를 참조하세요.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## 5단계: Pilot에서 Braze 메시징 체험하기 {#step-5-experience-braze-messaging-in-pilot}

이제 Braze Pilot 사용자로서 Braze 대시보드에서 Campaigns와 Canvases를 수신할 준비가 되었습니다! 데모 워크스페이스에서 실행된 Campaign을 방문하여 Braze 사용 사례에 대한 간단한 데모를 확인한 후, 라이브 워크스페이스로 이동하여 직접 메시지를 보내기 시작하세요.

Braze에서 캠페인 설정과 Canvases 구성 방법에 대한 자세한 내용은 [시작하기: Campaigns와 Canvases]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases)를 참조하세요.