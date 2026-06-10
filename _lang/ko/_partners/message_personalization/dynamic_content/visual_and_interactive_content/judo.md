---
nav_title: Judo
article_title: Judo
description: "이 참조 문서에서는 Braze와 Judo의 파트너십에 대해 설명합니다. Judo는 노코드 서버 기반 UI 플랫폼으로, iOS 및 Android 앱에 위치 컨텍스트와 추적 기능을 추가할 수 있습니다."
alias: /partners/judo/
page_type: partner
search_tag: Partner

---

# Judo

> [Judo](https://judo.app)는 퍼블리셔가 앱 업데이트 없이 풍부하고 매력적인 인앱 사용자 경험을 효율적으로 제공할 수 있도록 지원하는 서버 기반 UI 플랫폼입니다.

_이 통합은 Judo에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Judo 통합은 Campaign 및 Canvases에서 맞춤형 경험을 제공합니다. 단순한 템플릿 기반 랜딩 페이지 경험 대신, Braze Campaign에 여러 화면, 모달, 동영상, 커스텀 글꼴, 다크 모드 및 접근성과 같은 지원 설정을 포함하는 콘텐츠를 통합할 수 있으며, 이 모든 것이 코드 없이 구축되고 앱 업데이트 없이 배포됩니다. Braze의 데이터를 사용하여 Judo 경험에서 개인화된 콘텐츠를 지원할 수도 있습니다. 경험에서 발생한 사용자 이벤트와 데이터는 기여도 분석 및 타겟팅을 위해 Braze로 피드백될 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Judo 계정 | 이 파트너십을 활용하려면 [Judo](https://www.judo.app/) 계정이 필요합니다. |
| Judo SDK | Judo SDK를 [iOS](https://github.com/judoapp/judo-ios/) 및/또는 [Android](https://github.com/judoapp/judo-android) 앱에 통합해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 활용 사례 {#use-cases}

**온보딩**: Judo를 사용하는 앱 퍼블리셔는 풍부한 네이티브 온보딩 경험을 구축하고 배포합니다. 이러한 경험은 이제 Braze를 통해 조율되는 개인화된 크로스채널 온보딩 여정의 한 요소가 될 수 있습니다. 앱 업데이트 없이 경험을 개인화하고 빠르게 업데이트하여 다양한 인앱 플로우의 효과를 테스트할 수 있습니다.

**전환**: 앱 퍼블리셔는 Braze의 데이터를 사용하여 Judo의 통합 훅을 활용해 인앱 구매, 유료 구독 또는 상황별 머천다이징을 유도하는 개인화된 풍부한 인앱 경험을 만들 수 있습니다. 이러한 경험에 대한 접근은 Braze에서 생성된 참여 마케팅 Campaign을 통해 트리거될 수 있습니다.

**이벤트 기반 콘텐츠**: 스포츠 및 엔터테인먼트 분야에서 Judo의 주요 용도는 이벤트를 미리보기, 홍보 및 요약하는 풍부한 경험을 구축하는 것입니다. 이 기능은 시즌별 및 뉴스 기반 콘텐츠를 위해 다른 업종에서도 폭넓게 활용됩니다. 이벤트를 적시에 홍보하거나 강조하는 메시징을 풍부한 인앱 경험과 연결하면 퍼블리셔가 상황에 맞는 관련성을 통해 참여를 유도할 수 있습니다.

## 병렬 SDK 통합 {#side-by-side-sdk-integration}

Judo는 모바일 앱에서 Judo와 Braze SDK를 병렬로 통합하는 데 필요한 작업의 일부를 자동화하는 추가 라이브러리를 제공합니다.

### 1단계: Judo-Braze 통합 라이브러리 설치 {#step-1-install-the-judo-braze-integration-library}

앱에 Judo-Braze 통합 라이브러리를 설치하고 설정합니다. 이렇게 하면 이벤트 추적이 자동으로 활성화됩니다.

- [iOS 설치 안내](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Android 설치 안내](https://github.com/judoapp/judo-braze-android/wiki#installation).

### 2단계: 인앱 메시징 구성 {#step-2-configure-in-app-messaging}

이 단계에서는 iOS 및 Android용 커스텀 `ABKInAppMessageControllerDelegate` 및 `IInAppMessageManagerListener` 구현을 생성합니다.

각 통합 라이브러리에 포함된 인앱 메시지 설정 문서를 참조하세요:

- [iOS 인앱 메시징 설정](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Android 인앱 메시징 설정](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## 이 통합 사용하기 {#using-this-integration}

앱 측 통합을 완료한 후, Judo 경험에 대한 테스트 Braze 인앱 메시지 Campaign을 실행하여 예상대로 작동하는지 확인할 수 있습니다.

### 1단계: 사용자 지정 코드 인앱 메시지 Campaign 생성 {#step-1-create-a-custom-code-in-app-message-campaign}

Braze 플랫폼에서 **Custom Code** 메시지 유형으로 Braze 인앱 메시지 Campaign을 생성합니다. 다음으로 커스텀 유형으로 **HTML Upload**를 선택합니다. 메시지 콘텐츠를 기본 인앱 메시징 필드로 채워야 하며, 이 콘텐츠는 사용자에게 표시되지 않습니다.

!["Custom Code" 메시지 유형을 선택할 때 대시보드의 모습을 보여주는 이미지.]({% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %})

다음으로 아래의 최소한의 HTML 스니펫을 사용하여 양식 유효성 검사를 충족합니다:
```
<a href="appboy://close">X</a>
```

Judo에서 이를 다시 작성하고 Judo 경험으로 대체하므로 프로덕션 환경의 기기에는 표시되지 않습니다.

![Campaign의 작성 단계에 추가된 양식 유효성 검사 코드를 보여주는 이미지.]({% image_buster /assets/img/judo/braze-html-boilerplate.png %})

### 2단계: Judo용 키-값 페어 설정 {#step-2-set-a-key-value-pair-for-judo}
![이 이미지에서는 이 통합에 필요한 하나의 키-값 페어를 보여줍니다. "키"는 "judo-experience"이고 "값"은 Judo 링크입니다.]({% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Campaign에서 `judo-experience` 키로 [커스텀 키-값 페어]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/)를 설정합니다. 여기에 표시하려는 Judo 경험의 URL을 입력합니다. Judo-Braze 통합 라이브러리가 핸들러에서 이 키-값 페어를 감지하고 이를 사용하여 표준 Braze 인앱 메시지 UI 대신 Judo 경험을 삽입합니다.
<br><br>
### 3단계: Campaign 완료 {#step-3-finishing-the-campaign}

마지막으로 Campaign을 완료하고, Campaign의 트리거를 설정하고 **전달** 및 **타겟 사용자** 섹션에서 Segments를 통해 사용자를 선택합니다. Braze 인앱 메시지의 다양한 구성요소에 대해서는 인앱 메시지 [문서]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)를 참조하세요.