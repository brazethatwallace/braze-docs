---
title: "Movable Ink Da Vinci"
article_title: Movable Ink Da Vinci
alias: "/partners/movable_ink_da_vinci/"
description: "Braze와 Movable Ink Da Vinci 통합을 통해 브랜드는 Da Vinci의 AI 기반 콘텐츠 의사결정 엔진을 활용하여 고도로 개인화된 메시징을 제공할 수 있습니다. Da Vinci는 각 사용자에게 가장 관련성 높은 콘텐츠를 큐레이션하고 Braze를 통해 메시지를 원활하게 배포합니다."
page_type: partner
search_tag: Partner

---

# Movable Ink Da Vinci

> Braze와 Movable Ink [Da Vinci](https://movableink.com/da-vinci) 통합을 통해 브랜드는 Da Vinci의 AI 기반 콘텐츠 의사결정 엔진을 활용하여 고도로 개인화된 메시징을 제공할 수 있습니다. Da Vinci는 각 사용자에게 가장 관련성 높은 콘텐츠를 큐레이션하고 Braze를 통해 메시지를 원활하게 배포합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|------------|-------------|
| Movable Ink Da Vinci | 이 파트너십을 활용하려면 Movable Ink Da Vinci 계정이 필요합니다. |
| Braze 커런츠 - 메시지 참여 이벤트 | 메시지 참여 이벤트 데이터를 Movable Ink로 전송하려면 Braze 커스텀 Currents 내보내기가 필요합니다. |
| Braze REST API 키 | `messages.send`, `sends.id.create`, `campaigns.details` 권한이 있는 Braze REST API 키가 필요합니다. 이 키는 Braze 대시보드에서 **Settings** > **API Keys**로 이동하여 생성할 수 있습니다. <br><br>Movable Ink 계정 팀에서 자세한 설정 안내를 직접 제공합니다. [통합](#integration) 섹션을 참조하세요. |
| Braze 내 Da Vinci 앱 인스턴스 | Braze에서 전용 Da Vinci 앱 인스턴스를 생성합니다. Braze 대시보드에서 **Settings** > **App Settings** > **+ Add App**으로 이동하여 새 앱을 생성할 수 있습니다. 앱 이름을 "**Movable Ink - Da Vinci**"로 지정하고 아무 플랫폼이나 선택합니다(플랫폼 선택은 필수이지만 유형은 기능에 영향을 미치지 않습니다). [새 앱을 추가하는 방법]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/#step-3-add-your-app-instances)에서 자세히 알아보세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

통합을 시작하려면 Movable Ink 계정 팀에 문의하여 지원을 받으세요. Movable Ink에서 액세스 권한과 설정 안내를 제공합니다. Da Vinci가 Braze의 메시징 API를 통해 이메일 배포를 전송할 수 있도록 Movable Ink에 Braze API 자격 증명 세트를 제공해야 합니다.

연결이 완료되면 Movable Ink에서 다음을 수행합니다:

- 클라이언트 및 Braze와 협력하여 브랜드의 Da Vinci 계정이 Braze를 통해 성공적으로 배포할 수 있도록 설정합니다.
- 브랜드별 구성을 캡처하여 메시징 사용 사례에 맞게 조정합니다.
- 이메일이 의도한 대로 전달되고 모든 성능 및 운영 표준을 충족하는지 검증하기 위해 종합적인 테스트 및 품질 보증을 수행합니다.