---
nav_title: "Push Stories"
article_title: "Push Stories"
page_order: 2
page_type: reference
description: "이 참조 문서에서는 Push Stories가 무엇인지, 어떻게 만드는지, 그리고 자주 묻는 질문에 대해 다룹니다."
channel:
  - push

---

# Push Stories {#push-stories}

> Push Stories는 Instagram과 Facebook에서 대중화된 사진 캐러셀 기능을 활용하여 마케터가 푸시 내에서 풍부하고 일관된 스토리를 전달하는 캐러셀 페이지를 만들 수 있게 해줍니다. 이 페이지는 이미지, 클릭 동작, 제목, 설명으로 구성됩니다. 사용자는 이 페이지를 스와이프하며 여러분이 전달하는 스토리를 볼 수 있습니다.

| Android 예시 (확장됨) | iOS 예시 (확장됨) |
| :-----: | :----------: |
| ![Push Stories Android 미리보기.]({% image_buster /assets/img_archive/pushstories_android_preview.png %}) | ![Push Stories iOS 미리보기]({% image_buster /assets/img_archive/pushstories_ios_preview.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push Stories" }

{% alert note %}
iOS SDK 버전 3.13.0 이상에서는 SDK가 이미지를 다운로드하는 방식이 변경되어 첫 번째 이미지의 썸네일이 푸시의 축소된 보기에 표시되지 않습니다. 메시지 문구에서 사용자가 이미지를 보려면 푸시를 확장하도록 안내해야 합니다.
{% endalert %}

## 필수 조건 {#prerequisites}

Push Stories를 수신하려면 다음 SDK 버전이 필요합니다:

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## Push Stories 사용 방법 {#how-to-use-push-stories}

![Push Stories 작성기 드롭다운]({% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Push Stories를 사용하려면 다음을 수행합니다:

1. [푸시 Campaign]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/)을 생성합니다.
2. **알림 유형**에서 **Push Stories**를 선택합니다.
3. **iOS** 또는 **Android**를 선택합니다. 푸시 메시지에서 두 가지를 모두 선택하면 Push Story를 만드는 옵션이 나타나지 않습니다.

### Push Story 작성기 {#push-story-composer}

페이지를 만들려면 다음 단계를 수행합니다:

1. 메인 작성기에서 **새 페이지 추가**를 선택합니다.
2. 각 페이지에 이미지를 삽입하고 해당 이미지의 클릭 동작을 설정합니다.
3. 원하는 경우 각 페이지에 **제목**과 **설명**을 추가합니다. 한 페이지에 제목과 설명을 사용하면 모든 페이지에 삽입해야 합니다.

미리보기가 반영되며 인터랙티브합니다.

![Push Stories 작성기]({% image_buster /assets/img_archive/pushstories_composer.png %}){: style="max-width:60%"}

{% alert important %}
[연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/#about-connected-content)로 이미지를 가져오는 경우 이미지 URL이 `https://`로 시작하는지 확인합니다. `http://`를 사용하면 앱이 충돌합니다.
{% endalert %}

### 이미지 및 텍스트 사양 {#image-and-text-specifications}

다음 이미지 및 텍스트 사양은 Push Stories의 사진 캐러셀 부분에 적용됩니다. 사용자가 Push Story를 활성화하기 위해 상호작용하는 기본 푸시에 대한 정보는 [푸시 메시지 및 이미지 형식]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/)을 참조하세요.

{% tabs %}
{% tab 이미지 %}

- **이미지 비율:** 2:1 (필수)
- **권장 이미지 크기:** 500 KB
- **최대 이미지 크기:** 5 MB
- **파일 유형:** PNG, JPEG

{% endtab %}
{% tab 텍스트 %}

- **제목:** 30자 (권장)
- **설명:** 30자 (권장)

{% alert note %}
기기마다 글자 수에 약간의 차이가 있을 수 있지만, Push Stories의 제목과 설명은 각각 한 줄로 제한됩니다. 나머지 메시지는 잘립니다. 항상 실제 기기에서 메시지를 테스트하세요.
{% endalert %}

{% endtab %}
{% endtabs %}

### Push Story 세분화 {#push-story-segmentation}

Campaign 또는 Canvas를 생성할 때 Push Story 페이지를 클릭했는지 여부에 따라 타겟팅할 사용자를 필터링할 수 있습니다. 그런 다음 사용자를 타겟팅하는 데 사용할 Campaign과 페이지를 선택합니다.

### Push Stories 분석 {#push-stories-analytics}

분석은 현재 푸시 알림의 분석 섹션과 매우 유사합니다. Push Stories 분석에서는 **직접 열람 수** 측정기준을 열어 페이지별 클릭 수를 확인할 수 있습니다.

![샘플 분석과 직접 열람 수 측정기준의 확장된 세부 정보가 포함된 iOS 푸시 성능 테이블.]({% image_buster /assets/img_archive/pushstories_analytics.png %})

## 문제 해결 {#troubleshooting}

### iOS

#### Push Story를 자신에게 보냈지만 알림을 받지 못했습니다 {#i-sent-myself-a-push-story-but-didnt-receive-the-notification}

Apple은 다양한 요인에 따라 특정 유형의 알림이 기기로 전송되지 않도록 하는 특정 규칙을 적용하고 있습니다. 여기에는 고객의 데이터 요금제, 알림 크기, 고객의 저장 용량 평가가 포함됩니다. 그 결과 때때로 고객에게 알림이 전송되지 않을 수 있습니다.

이는 Apple이 부과하는 제한 사항이며 Push Story를 설계할 때 고려해야 합니다.

#### Push Story를 자신에게 보냈지만 축소된 보기가 표시되었습니다 {#i-sent-myself-a-push-story-but-saw-the-condensed-view-instead}

데이터 연결 끊김 등으로 인해 모든 페이지가 로드되지 않는 특정 상황에서는 Push Story가 축소된 알림만 표시합니다.

### Android

#### 이미지를 클릭한 후 Push Story가 닫히지 않습니다 {#push-story-doesnt-dismiss-after-clicking-the-image}

기본적으로 Android에서는 사용자가 이미지를 클릭한 후 Push Stories가 닫히지 않습니다. 알림을 닫으려면 [`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721)을 호출하세요.