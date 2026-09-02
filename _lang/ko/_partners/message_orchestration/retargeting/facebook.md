---
nav_title: Facebook
article_title: Facebook 오디언스 내보내기
alias: /partners/facebook/
description: "이 참조 문서에서는 브랜드가 고객에게 도달하고 참여를 유도할 수 있는 대표적인 소셜 플랫폼인 Facebook과 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner
---

# Facebook 오디언스 내보내기 {#facebook-audience-export}

> Braze와 Facebook 통합을 사용하면 Braze Segments를 Facebook으로 수동 내보내기하여 Facebook 커스텀 오디언스를 생성할 수 있습니다. 이 기능은 일회성 정적 오디언스 내보내기이며, 새로운 Facebook 커스텀 오디언스만 생성합니다.

Facebook 커스텀 오디언스 내보내기의 일반적인 사용 사례는 다음과 같습니다:
- 라이프사이클의 특정 시점에서 사용자 리타겟팅
- 제외 타겟팅 목록 생성
- 신규 사용자를 보다 효율적으로 확보하기 위한 [유사 오디언스](https://www.facebook.com/business/help/164749007013531?id=401668390442328) 생성
<br><br>

{% alert note %}
Facebook 오디언스 내보내기는 **사용자 액세스 토큰**을 사용하여 요청을 인증합니다.<br><br>
이 기능을 [Facebook 오디언스 동기화]({{site.baseurl}}/audience_sync_facebook) 기능과 함께 사용하는 경우, Braze는 기본적으로 이미 생성한 보다 안정적인 **시스템 사용자 토큰**을 사용하여 요청을 인증합니다.
{% endalert %}

{% alert note %}
Meta 워크 계정 베타 테스트에 참여 중인 경우, [Facebook 파트너 페이지]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync#step-1-connect-to-facebook)에서 계정을 연결 해제한 후 다시 연결하세요.
{% endalert %}

## 전제 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| [Facebook Business 매니저](https://www.facebook.com/business/help/113163272211510?id=180505742745347) | 브랜드의 Facebook 자산(예: 광고 계정, 페이지, 앱)을 관리하는 중앙 집중식 도구입니다. |
| [Facebook 광고 계정](https://www.facebook.com/business/help/910137316041095?id=420299598837059) | Braze 커스텀 오디언스에 사용하려는 브랜드의 비즈니스 매니저에 연결된 활성 Facebook 광고 계정입니다.<br><br>Facebook 비즈니스 매니저 관리자가 Braze에서 사용할 Facebook 광고 계정에 대한 관리자 권한을 부여했는지, 그리고 광고 계정 이용약관에 동의했는지 확인하세요. 그렇지 않으면 Braze 내에서 Facebook 광고 계정에 접근할 수 없습니다. |
| [Facebook 커스텀 오디언스 약관](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Braze에서 사용할 Facebook 광고 계정에 대해 Facebook의 커스텀 오디언스 약관에 동의해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 통합 {#integration}

### 1단계: Facebook에 연결하기 {#step-1-connect-to-facebook}

1. Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동하여 **Facebook**을 선택합니다.

{: start="2"}
2. Facebook 오디언스 내보내기 모듈에서 **Connect Facebook**을 선택합니다. <br><br>![Braze 플랫폼의 Facebook 기술 파트너 페이지.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:70%;"}

{: start="3"}
3. Facebook oAuth 대화 상자 창에서 Braze가 Facebook 광고 계정에 커스텀 오디언스를 생성할 수 있도록 승인합니다. <br><br>![Facebook 사용자 이름으로 연결하라는 첫 번째 Facebook 대화 상자.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![광고 계정의 광고 관리 권한을 요청하는 두 번째 Facebook 대화 상자.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

{: start="4"}
4. Braze가 Facebook 계정에 연결되면, Braze 워크스페이스 내에서 동기화할 광고 계정을 선택합니다. <br><br>![Facebook에 연결할 수 있는 사용 가능한 광고 계정 목록.]({% image_buster /assets/img/fb/afb_4.png %}){: style="max-width:70%;"}<br><br> 연결이 완료되면 파트너 페이지로 돌아가며, 여기에서 연결된 계정을 확인하고 기존 계정의 연결을 해제할 수 있습니다. <br><br> ![연결된 광고 계정이 표시된 업데이트된 Facebook 기술 파트너 페이지.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:70%;"}<br>
<br> Facebook 연결은 Braze 워크스페이스 수준에서 적용됩니다. Facebook 관리자가 Facebook Business 매니저에서 사용자를 제거하거나 연결된 Facebook 계정에 대한 액세스를 취소하면, Braze가 유효하지 않은 토큰을 감지합니다. 그 결과 Facebook 오디언스 단계를 사용하는 활성 Canvases에 오류가 표시되며, Braze가 사용자를 동기화할 수 없게 됩니다.

{% alert important %}
이전에 [광고 관리](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) 및 [광고 관리 표준 액세스](https://developers.facebook.com/docs/marketing-api/access#standard)에 대한 Facebook 앱 검토 프로세스를 완료한 고객의 경우, 시스템 사용자 토큰은 Facebook 오디언스 단계에 여전히 유효합니다. Facebook 파트너 페이지를 통해 Facebook 시스템 사용자 토큰을 편집하거나 취소할 수 없습니다. 대신, Facebook 계정을 연결하여 Braze 워크스페이스 내에서 Facebook 시스템 사용자 토큰을 대체할 수 있습니다.

<br><br>새로운 Facebook oAuth 구성은 [Segments를 통한 Facebook 내보내기]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook#prerequisites)에도 적용됩니다.
{% endalert %}

### 2단계: Facebook으로 사용자 내보내기 {#step-2-export-your-users-into-facebook}

Braze에서 Facebook 오디언스 내보내기는 **Segments** 페이지를 통해 이용할 수 있습니다.

1. **Segments** 페이지에서 내보내려는 Segment를 선택합니다.
2. **사용자 데이터**를 선택한 다음 **Export as Facebook Audience**를 선택합니다. <br><br>![드롭다운 옵션에 "Export as Facebook Audience"가 포함된 "사용자 데이터"가 선택된 Segment의 "Segment 세부 정보" 섹션.]({% image_buster /assets/img/fb/afb_6.png %})

{: start="3"}
3. Braze에서 Facebook을 아직 활성화하지 않은 경우, 대시보드의 Facebook 기술 파트너 페이지로 이동하라는 안내가 표시됩니다. **기술 파트너** > **Facebook**을 통해 이미 Facebook을 활성화한 경우, Facebook 광고 계정과 내보낼 사용자 필드를 선택할 수 있습니다. <br><br> 다음 필드를 내보낼 수 있습니다:
- 기기 IDFA
- 전화번호
- 이메일

{% alert note %}
단일 내보내기에서는 하나의 사용자 필드만 선택할 수 있습니다. 두 개 이상의 데이터 유형을 선택하면, Braze가 각각에 대해 별도의 커스텀 오디언스를 생성합니다.
{% endalert %}

{: start="4"}
4. 사용자 필드를 선택한 후 **Export Segment**를 선택합니다. CSV 내보내기와 마찬가지로, Segment가 Facebook으로 내보내기를 완료하면 이메일을 받게 됩니다.
5. [Facebook 광고 관리자](https://www.facebook.com/ads/manager/audiences/manage/)에서 커스텀 오디언스를 확인합니다.

{% alert important %}
사용자 개인정보 보호 이유로 인해 Facebook에서는 다음을 확인할 수 없습니다:

- 커스텀 오디언스에 성공적으로 추가된 정확한 사용자. [개별 오디언스 구성원이 숨겨지는 이유에 대한 Facebook의 자세한 내용을 참조하세요](https://www.facebook.com/business/help/112061095610075).
- 커스텀 오디언스의 크기. [Facebook의 오디언스 크기 추정 변경 사항에 대한 자세한 내용을 참조하세요](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923).
{% endalert %}

#### 오디언스 내보내기 구성하기 {#configuring-your-audience-export}

Facebook 오디언스를 구성할 때, 사용자의 환경 설정에 따라 특정 사용자를 포함하거나 제외할 수 있으며, [CCPA](https://oag.ca.gov/privacy/ccpa)에 따른 "판매 또는 공유 금지" 권리와 같은 개인정보 보호법을 준수하기 위해 이를 구현할 수 있습니다. 마케터는 Canvas 진입 기준 내에서 사용자 적격성에 대한 관련 필터를 구현해야 합니다. 다음 옵션이 도움이 될 수 있습니다.

- [Braze SDK를 통해 iOS IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection)를 수집한 경우, **Ads Tracking Enabled** 필터를 사용할 수 있습니다. 값을 `true`로 선택하면 옵트인한 사용자만 오디언스 동기화 대상으로 전송합니다.

![Ads Tracking Enabled가 true로 설정된 Canvas 진입 필터.]({% image_buster /assets/img/tiktok/tiktok16.png %}){: style="max-width:75%;"}

- 옵트인, 옵트아웃, `Do Not Sell Or Share` 또는 기타 관련 커스텀 속성을 수집하는 경우, Canvas 진입 기준에 필터로 포함해야 합니다:

![진입 오디언스가 "opted_in_marketing"이 "true"인 Canvas.]({% image_buster /assets/img/tiktok/tiktok13.png %}){: style="max-width:75%;"}


#### 유사 오디언스 {#lookalike-audiences}

Segment를 Facebook 오디언스로 성공적으로 내보낸 후, Facebook [유사 오디언스](https://www.facebook.com/business/help/164749007013531?id=401668390442328)를 사용하여 추가 그룹을 생성할 수 있습니다. 이 기능은 선택한 오디언스의 인구 통계, 관심사 및 기타 속성을 분석하여 유사한 속성을 가진 새로운 오디언스를 생성합니다.

## 문제 해결 {#troubleshooting}

### 액세스 토큰 유효성 검사 오류 {#error-validating-access-token}

Facebook 내보내기를 사용할 때 `Error Validating Access Token` 오류는 다음과 같은 경우에 나타납니다:
- 비밀번호를 변경하여 현재 세션이 무효화된 경우
- Facebook에서 보안 조치로 로그아웃된 경우

이 오류를 해결하려면 다음 단계를 따르세요:
1. Facebook에서 로그아웃한 다음 다시 로그인합니다.
2. Braze에서 Facebook 자격 증명을 제거하고 저장합니다. Segment 내보내기를 시도하여 자격 증명이 제거되었는지 확인합니다(내보내기 아이콘이 비활성화되어야 합니다).
3. Facebook 자격 증명을 다시 추가하고 저장합니다.
4. 다시 내보내기를 시도합니다.

내보내기가 작동하지 않는 경우 다음을 수행하세요:
1. 자격 증명을 다시 제거하고 저장합니다.
2. 자격 증명을 다시 추가하고 저장합니다.
3. **기술 파트너** 페이지에서 Facebook 통합을 연결 해제한 다음 다시 연결합니다.

### Facebook 오디언스 내보내기 시 오류 {#error-when-exporting-a-facebook-audience}

Segment를 Facebook 오디언스로 내보낼 때 오류가 발생하면, Facebook 개발자 설명서에서 다음과 같은 일반적인 원인을 안내하고 있습니다:

1. **액세스 토큰이 앱 및 광고 계정의 관리자가 아닌 사용자의 것입니다:** Braze에 연결된 Facebook 사용자의 자격 증명에 적절한 권한이 있어야 합니다.
2. **내보내기 대상 광고 계정이 앱과 연결되어 있지 않습니다:** Facebook 광고 계정이 Facebook 설정에서 앱에 연결되어 있어야 합니다.

다음 점검 사항을 통해 설정을 확인하세요:

- **앱의 관리자인지 확인합니다:** [developers.facebook.com](https://developers.facebook.com/)으로 이동하여 **My Apps**를 열고 회사의 앱을 선택합니다. 앱이 보이지 않으면 개발팀에서 추가해야 할 수 있습니다. 앱 대시보드에서 **Roles**로 이동하여 본인의 역할(Admin, Developer, Tester 또는 Analytics User)을 확인합니다.
- **광고 계정이 앱과 연결되어 있는지 확인합니다:** Facebook 앱 대시보드에서 **Settings** > **Advanced**로 이동하고 **Advertising Accounts**까지 스크롤한 다음, Braze 오디언스 내보내기에 사용할 Facebook 광고 계정 ID가 목록에 없으면 추가합니다.
- **광고 계정의 관리자인지 확인합니다:** [business.facebook.com](https://business.facebook.com/)으로 이동하여 메인 메뉴에서 **Business Settings**를 열고 **Accounts** > **Ad accounts**로 이동하여 광고 계정을 선택합니다. 본인의 접근 권한과 커스텀 오디언스를 생성하는 데 필요한 권한이 있는지 확인합니다.

자세한 내용은 [Facebook 커스텀 오디언스 API 설명서](https://developers.facebook.com/docs/) 및 [Facebook 비즈니스 고객센터의 커스텀 오디언스 가이드](https://www.facebook.com/business/help)를 참조하세요.