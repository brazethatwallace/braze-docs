---
title: "Movable Ink"
article_title: Movable Ink
alias: "/partners/movable_ink/"
description: "이 참조 문서에서는 디지털 마케터에게 고객을 움직이는 매력적이고 독특한 시각적 경험을 만들 수 있는 방법을 제공하는 클라우드 기반 소프트웨어 플랫폼인 Movable Ink와 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Movable Ink

> [Movable Ink](https://www.movableink.com/)는 디지털 마케터에게 고객을 움직이는 매력적이고 독특한 시각적 경험을 만들 수 있는 방법을 제공하는 클라우드 기반 소프트웨어 플랫폼입니다. Movable Ink 플랫폼은 Campaign에 쉽게 삽입할 수 있는 유용한 커스터마이징 옵션을 제공합니다.

_이 통합은 Movable Ink에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Movable Ink의 Intelligent Creative 기능(투표, 카운트다운 타이머, 스크래치 오프 등)을 활용하여 크리에이티브 역량을 확장하세요. Movable Ink와 Braze 통합은 동적 데이터 중심 메시지에 대한 보다 균형 잡힌 접근 방식을 지원하여 사용자에게 중요한 사항에 대한 실시간 요소를 제공합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Movable Ink 계정 | 이 파트너십을 활용하려면 Movable Ink 계정이 필요합니다. |
| 데이터 소스 | Movable Ink에 데이터 소스를 연결해야 합니다. CSV, 웹사이트 가져오기 또는 API를 통해 연결할 수 있습니다. Braze와 Movable Ink 간에 통합 식별자(예: `external_id`)를 사용하여 데이터를 전달해야 합니다.
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 사용 사례 {#use-cases}

- 개인화된 월간 또는 연말 요약.
- 마지막으로 알려진 행동을 기반으로 이메일, 푸시 또는 리치 알림의 이미지를 동적으로 개인화합니다.<br>
	예시:
	- 리치 푸시 메시지를 사용하여 API에서 데이터를 가져와 이벤트 일정을 동적으로 생성합니다.
	- 카운트다운 타이머를 사용하여 대규모 세일이 다가올 때 사용자에게 알립니다(예: 블랙 프라이데이, 밸런타인데이 또는 연말 할인).
	- 스크래치 오프 기능을 사용하여 프로모션 코드를 재미있고 인터랙티브한 방식으로 배포합니다.

## 지원되는 Movable Ink 기능 {#supported-movable-ink-capabilities}

Intelligent Creative는 회사 사용자가 활용할 수 있는 다양한 오퍼링을 제공합니다. 다음 목록은 지원되는 기능을 보여줍니다.

| Movable Ink 기능 | 기능 | 리치 푸시 알림 | 인앱 메시징 / Content Cards / 이메일 | 세부 정보 |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| Creative Optimizer | A/B 콘텐츠 표시 | ✗ | ✔ | |
| 최적화 | ✗ | ✔* | * Branch의 딥링킹 솔루션을 사용해야 합니다 |
| 타겟팅 규칙 | 날짜 | ✔* | ✔ | * 지원되지만 푸시 알림은 수신 시 캐시되어 새로고침되지 않으므로 권장하지 않습니다 |
| 요일 | ✔* | ✔ | * 지원되지만 푸시 알림은 수신 시 캐시되어 새로고침되지 않으므로 권장하지 않습니다 |
| 시간대 | ✔* | ✔ | * 지원되지만 푸시 알림은 수신 시 캐시되어 새로고침되지 않으므로 권장하지 않습니다 |
| Stories/행동 활동 | | ✔* | ✔* | * Braze에 사용되는 고유 사용자 식별자가 ESP의 식별자에 연결되어야 합니다 |
| 앱 내 딥링킹 | | ✔* | ✔* | * 고객에게 원활한 경험을 제공하려면 Branch를 통한 기존 딥링킹 솔루션 또는 Movable Ink의 Client Experience 팀과 검증된 솔루션을 사용하세요. |
| 앱 | 카운트다운 타이머 | ✔* | ✔ | * 지원되지만 푸시 알림은 수신 시 캐시되어 새로고침되지 않으므로 권장하지 않습니다 |
| 투표 | ✗ | ✔* | * 투표 후 앱을 떠나 모바일 랜딩 페이지로 이동합니다 |
| 스크래치 오프 | ✔* | ✔* | * 클릭 시 앱을 떠나 스크래치 오프 경험으로 이동합니다 |
| 비디오 | ✔* | ✔* | * 애니메이션 GIF만 지원, <br>Android의 경우 Braze 구현에 [GIF 지원]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android)이 필요합니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Supported Movable Ink capabilities" }

## 통합 {#integration}

### 1단계: Movable Ink용 데이터 소스 생성 {#step-1-create-a-data-source-for-movable-ink}

고객은 CSV, 웹사이트 가져오기 또는 API 통합이 될 수 있는 데이터 소스를 생성해야 합니다.

![표시되는 다양한 데이터 소스 옵션: CSV 업로드, 웹사이트 또는 API 통합.]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs local %}
{% tab CSV 데이터 소스 %}
- **CSV 데이터 소스**: 각 행에는 최소 하나의 세그먼트 열과 하나의 콘텐츠 열이 있어야 합니다. CSV를 업로드한 후 콘텐츠를 타겟팅하는 데 사용할 열을 선택합니다. [CSV 파일 예시]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![데이터 소스로 'CSV'를 선택하면 표시되는 필드.]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab 웹사이트 데이터 소스 %}
- **웹사이트 데이터 소스**: 각 행에는 최소 하나의 세그먼트 열과 하나의 콘텐츠 열이 있어야 합니다. CSV를 업로드한 후 콘텐츠를 타겟팅하는 데 사용할 열을 선택합니다.
  - 이 과정에서 다음을 매핑해야 합니다:
    - Segment로 사용할 필드
    - 크리에이티브에서 동적으로 개인화할 수 있는 데이터 필드로 사용할 필드(예: 이름, 성, 구/군/시 등의 사용자 속성 또는 커스텀 속성)

![데이터 소스로 '웹사이트'를 선택하면 표시되는 필드.]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab API 통합 %}
- **API 통합**: 회사의 API를 사용하여 API 응답에서 직접 콘텐츠를 제공합니다.

![데이터 소스로 'API 통합'을 선택할 때 표시되는 필드]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### 2단계: Movable Ink 플랫폼에서 캠페인 생성 {#step-2-create-a-campaign-on-the-movable-ink-platform}

Movable Ink 홈 화면에서 캠페인을 생성합니다. HTML 이메일, 이미지 이메일 또는 푸시, 인앱 메시지, Content Cards(권장)를 포함한 모든 채널에서 사용할 수 있는 블록 중에서 선택할 수 있습니다.

블록을 통해 사용할 수 있는 다양한 콘텐츠 옵션도 살펴보시기 바랍니다.

![새 Movable Ink 캠페인을 만들 때 Movable Ink 플랫폼이 어떻게 보이는지 보여주는 이미지.]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="max-width:70%"}

Movable Ink에는 텍스트나 이미지와 같은 요소를 드래그 앤 드롭할 수 있는 간편한 편집기가 있습니다. 데이터 소스를 채운 경우 데이터 속성을 사용하여 이미지를 동적으로 생성할 수 있습니다. 또한 Campaign이 전송되었지만 사용자가 개인화 기준에 맞지 않는 경우를 위해 이 플로우 내에서 대체 콘텐츠를 생성할 수도 있습니다.

![다양한 커스터마이징 가능한 요소를 보여주는 Movable Ink 블록 편집기.]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

캠페인을 완료하기 전에 동적 이미지를 미리보기하고 쿼리 파라미터를 테스트하여 이미지가 조회 시 어떻게 보이는지 확인하세요. 완료되면 Braze에 삽입할 수 있는 동적 URL이 생성됩니다!

Movable Ink 플랫폼 사용 방법에 대한 자세한 내용은 [Movable Ink 지원 센터](https://support.movableink.com/)를 방문하세요.

### 3단계: Movable Ink 콘텐츠 URL 가져오기 {#step-3-obtain-movable-ink-content-url}

Braze 메시지에 Movable Ink 콘텐츠를 포함하려면 Movable Ink에서 제공한 소스 URL을 찾아야 합니다.

소스 URL을 가져오려면 Movable Ink 대시보드에서 콘텐츠를 설정한 다음 콘텐츠를 완료하고 내보내야 합니다. **Finish** 페이지에서 크리에이티브 태그의 소스 URL(`img src`)을 복사합니다.

![Movable Ink 캠페인을 완료한 후 표시되는 페이지에서 콘텐츠 URL을 찾을 수 있습니다.]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="max-width:80%;"}

다음으로 Braze 플랫폼에서 적절한 필드에 URL을 붙여넣습니다. 메시징 채널에 적합한 필드는 4단계에서 확인할 수 있습니다. 마지막으로 병합 태그(예: {% raw %}`&mi_u=%%email%%`{% endraw %})를 해당 Liquid 변수(예: {% raw %}`&mi_u={{${email_address}}}`{% endraw %})로 교체합니다.

### 4단계: Braze 경험 {#step-4-braze-experience}

{% tabs local %}
{% tab 이메일 %}
Braze 플랫폼에서 크리에이티브 태그를 이메일 본문에 붙여넣습니다.![Movable Ink 크리에이티브 태그가 메시지 본문에 삽입된 Braze 이메일 작성기.]({% image_buster /assets/img/movable_ink/web2.png %}){: style="max-width:90%"}<br><br>

{% endtab %}
{% tab 푸시 알림 %}

1. Braze 플랫폼에서:
	- Android 푸시: **Push Icon Image** 및 **Expanded Notification Image** 필드에 URL을 붙여넣습니다.<br>![Movable Ink 콘텐츠용 이미지 URL 필드가 표시된 Braze Android 푸시 설정.]({% image_buster /assets/img/movable_ink/android.png %}){: style="max-width:60%"}<br><br>
	- iOS 푸시: **Media** 링크 필드에 URL을 붙여넣고 사용 중인 파일 형식을 지정합니다.<br>![Movable Ink URL이 입력된 Braze iOS 푸시 작성기 미디어 필드.]({% image_buster /assets/img/movable_ink/ios.png %}){: style="max-width:60%"}<br><br>
	- 웹 푸시: **Push Icon Image** 및 **Large Notification Image** 필드에 URL을 붙여넣습니다.<br>![푸시 아이콘 및 대형 이미지 URL 필드가 있는 Braze 웹 푸시 편집기.]({% image_buster /assets/img/movable_ink/web.png %}){: style="max-width:60%"}<br><br>
2. 이미지가 캐시되지 않도록 하려면 메시지의 URL 앞에 빈 Liquid 태그를 추가합니다: <br>{% raw %}`{% if true %}{% endif %}https://movable-ink-image-url-goes-here`{% endraw %}

{% endtab %}
{% tab 인앱 메시지 %}

1. Braze 플랫폼에서 **Rich Notification Media** 필드에 URL을 붙여넣습니다.![Movable Ink 이미지 URL이 입력된 Braze 리치 알림 미디어 필드.]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. 캐싱을 방지하기 위해 고유한 URL을 제공합니다. Movable Ink의 실시간 이미지가 작동하고 캐싱의 영향을 받지 않도록 하려면 Liquid를 사용하여 Movable Ink 이미지 URL 끝에 타임스탬프를 추가합니다.

이렇게 하려면 다음 구문을 사용하고 필요에 따라 이미지 URL을 교체합니다:
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
이 템플릿은 현재 시간(초 단위)을 가져와 Movable Ink 이미지 탭 끝에 쿼리 파라미터로 추가한 다음 최종 결과를 출력합니다. **Test** 탭에서 미리보기할 수 있으며&#8212;이 탭에서 코드를 평가하고 미리보기를 표시합니다.

**3.** 마지막으로 세그먼트 멤버십을 재평가합니다. 이렇게 하려면 Campaign의 **Target Audiences** 단계에 있는 `Re-evaluate audience membership and liquid at send-time` 옵션을 활성화합니다. 이 옵션을 사용할 수 없는 경우 고객 성공 매니저 또는 Braze 고객지원팀에 문의하세요. 이 옵션은 Braze SDK에 Campaign을 다시 요청하도록 지시하여 인앱 메시지가 트리거될 때마다 고유한 URL을 제공합니다.

{% endtab %}
{% tab Content Card %}

1. Braze 플랫폼에서 **Rich Notification Media** 필드에 URL을 붙여넣습니다.![Movable Ink 이미지 URL이 입력된 Braze Content Cards 미디어 필드.]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. 모바일의 경우: iOS 및 Android의 Content Cards 이미지는 수신 시 캐시되며 새로고침되지 않습니다.
  - 해결 방법으로, Content Card가 다시 템플릿화되도록 해당 만료 기간과 함께 일별, 주별 또는 월별 반복 메시지로 Campaign을 예약합니다. 예를 들어, 하루에 한 번 새로고침해야 하는 Content Card는 1일 만료 기간의 일별 예약 발송으로 설정해야 합니다.
3. Movable Ink의 실시간 이미지가 작동하고 Content Card가 다시 템플릿화될 때 캐싱의 영향을 받지 않도록 하려면 Liquid를 사용하여 Movable Ink 이미지 URL 끝에 타임스탬프를 추가합니다.

이렇게 하려면 다음 구문을 사용하고 필요에 따라 이미지 URL을 교체합니다:
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
이 템플릿은 현재 시간(초 단위)을 가져와 Movable Ink 이미지 탭 끝에 쿼리 파라미터로 추가한 다음 최종 결과를 출력합니다. **Test** 탭에서 미리보기할 수 있으며, 이 탭에서 코드를 평가하고 미리보기를 표시합니다.

{% endtab %}
{% endtabs %}

## 문제 해결 {#troubleshooting}

### 동적 이미지가 올바르게 표시되지 않나요? 어떤 채널에서 문제가 발생하고 있나요? {#dynamic-images-not-showing-correctly-what-channel-are-you-experiencing-difficulties-with}
- **푸시**: Movable Ink 이미지 URL 앞에 빈 로직이 있는지 확인하세요: <br>{% raw %}`{% if true %}{% endif %}https://movable-ink-image-url-goes-here`{% endraw %}
- **인앱 메시지 및 Content Cards**: 이미지 URL이 각 노출마다 고유한지 확인하세요. 적절한 Liquid를 추가하여 각 URL이 다르도록 할 수 있습니다. [인앱 및 Content Cards 메시지 안내]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink#step-4-braze-experience)를 참조하세요.
- **이미지가 로드되지 않음**: Braze 대시보드에서 모든 "병합 태그"를 해당 Liquid 필드로 교체했는지 확인하세요. 예: {% raw %}`https://mi-msg.com/p/rp/image.png?mi_u=%%email%%`{% endraw %}를 {% raw %}`https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}`{% endraw %}로 교체합니다.

### Android에서 GIF 표시에 문제가 있나요? {#having-trouble-showing-gifs-on-android}
- Android는 구현에서 GIF 지원이 필요합니다. 이 설정이 되어 있지 않은 경우 Android [인앱 메시지 커스터마이징]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android) 문서를 참조하세요.


[1]: https://www.movableink.com/
[datasource]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
[1]: ({% image_buster /assets/img/movable_ink/android.png %})
[2]: ({% image_buster /assets/img/movable_ink/ios.png %})
[3]: ({% image_buster /assets/img/movable_ink/web.png %})