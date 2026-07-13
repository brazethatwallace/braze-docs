---
nav_title: Contentsquare
article_title: Contentsquare
description: "이 참조 문서에서는 Braze와 Contentsquare 간의 파트너십에 대해 설명합니다. Contentsquare는 고객의 디지털 경험을 기반으로 메시지를 타겟팅하여 캠페인의 관련성과 전환율을 개선할 수 있는 디지털 경험 분석 플랫폼입니다."
alias: /partners/contentsquare/
page_type: partner
search_tag: Partner

---

# Contentsquare

> [Contentsquare](https://contentsquare.com/)는 고객 경험에 대한 전례 없는 이해를 가능하게 하는 디지털 경험 분석 플랫폼입니다.

_이 통합은 Contentsquare에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Contentsquare 통합을 사용하면 Live Signals(사기, 불만 신호 등)를 Braze에서 커스텀 이벤트로 전송할 수 있습니다. Contentsquare 경험 인사이트를 활용하여 고객의 디지털 경험과 행동 패턴을 기반으로 메시지를 타겟팅함으로써 캠페인의 관련성과 전환율을 개선하세요.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Contentsquare 계정 | 이 파트너십을 활용하려면 Contentsquare 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. Braze 대시보드에서 새 키를 생성하려면 **설정** > **API 키**로 이동하세요. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({% image_buster /assets/img/contentsquare_custom_events.png %}). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 사용 사례 {#use-cases}

Braze와 Contentsquare의 일반적인 사용 사례는 다음과 같습니다:
- Braze 내에서 고객 경험 데이터를 표면화하여 고객 의도에 기반한 초개인화 메시지를 전달합니다.
- 고객의 디지털 행동, 망설임, 불만 및 의도를 기반으로 리타겟합니다.
- Contentsquare 내에서 부정적인 경험을 식별하고 타겟팅된 메시지와 리텐션 오퍼로 고객을 회복합니다.
- 적절한 시간과 장소에서 더 관련성 있고 공감적인 메시지를 전송하여 이탈 위험이 있는 고객을 회복합니다.

## 통합 {#integration}

Contentsquare를 Braze에 통합하려면 Contentsquare 통합 카탈로그에서 "Live Signals" 통합 설치를 요청해야 합니다:

1. Contentsquare에서 **Settings** 메뉴의 **Console**을 클릭합니다. 현재 작업 중인 프로젝트로 리디렉션됩니다.
2. **Projects** 페이지에서 **Integrations** 탭으로 이동하여 **+ Add integration** 버튼을 클릭합니다.
3. 통합 카탈로그에서 **Live Signals** 통합을 찾아 **Add**를 클릭합니다. 그러면 Contentsquare 팀에서 연락하여 Braze에 실시간 신호를 전송하기 위한 코드 스니펫을 구성할 것입니다.
4. Contentsquare가 통합을 처리합니다. 통합이 완료되면 표시 텍스트가 업데이트됩니다.

자세한 내용은 [Contentsquare 통합 요청](https://uxanalyser.zendesk.com/hc/en-gb/articles/4405613239186)을 참조하세요.

## 이 통합 사용하기 {#using-this-integration}

통합이 완료되면 Contentsquare 커스텀 이벤트를 Campaigns 및 Canvases에서 사용할 수 있습니다. Braze로 전송되는 이벤트는 **데이터 설정** > **커스텀 이벤트**에서 확인할 수 있습니다.

![Braze 커스텀 이벤트 탭의 Contentsquare 실시간 신호 데이터]({% image_buster /assets/img/contentsquare_custom_events.png %})