---
nav_title: Meta Business Agent
article_title: Meta Business Agent와 Braze WhatsApp
page_order: 8
description: "이 가이드에서는 Meta Business Agent가 Braze에 연결된 WhatsApp Business 전화번호와 어떻게 상호작용하는지, 그리고 이를 활성화할 경우 예상되는 사항에 대해 설명합니다."
page_type: reference
channel:
  - WhatsApp
alias: /meta_business_agent/
hidden: true
noindex: true
---

# Meta Business Agent와 Braze WhatsApp {#meta-business-agent-and-braze-whatsapp}

> Meta Business Agent는 Braze에도 연결된 번호로 수신되는 WhatsApp 인바운드 메시지에 응답할 수 있습니다. 이 문서에서는 두 시스템이 메시지 가시성을 어떻게 공유하는지, Meta 도구에서 에이전트를 활성화하는 방법, 그리고 과금이 어떻게 분리되는지를 다룹니다. 이 내용은 2026년 8월 기준 Meta의 Business Agent 제품 기능 및 설명서를 반영합니다.

Meta는 Meta Business Agent를 지속적으로 개발하고 있으므로 일부 세부 사항이 변경될 수 있습니다. 최신 정보는 [Meta의 Business Agent 설명서](https://developers.facebook.com/documentation/meta-business-agent/overview)를 참조하세요.

## Meta Business Agent란? {#what-is-meta-business-agent}

Meta Business Agent는 Meta가 WhatsApp Business 전화번호에서 직접 운영하는 AI 기반 응답 시스템입니다. 적격한 번호에 대해 활성화하면, Meta 도구에서 구성한 지식(비즈니스 정보, FAQ, 파일, 웹사이트 콘텐츠)과 커넥터를 사용하여 비즈니스를 대신해 사용자의 인바운드 메시지에 응답할 수 있습니다.

Meta Business Agent 활성화는 전적으로 WhatsApp Manager와 Meta Business Suite에서 설정하며, Braze 워크스페이스와는 별개입니다. 설정에 Braze가 필요하지 않으며, 현재 이를 위한 Braze 대시보드 컨트롤은 없습니다.

## Braze에 연결된 번호와의 상호작용 방식 {#how-it-interacts-with-your-braze-connected-number}

Meta Business Agent와 Braze는 동일한 WhatsApp Business 전화번호에서 공존할 수 있지만, 현재 모든 메시지에 대한 가시성을 공유하지는 않습니다.

- **Braze에서 시작한 아웃바운드 메시지는 영향을 받지 않습니다.** Meta Business Agent 활성화 여부와 관계없이, Braze는 Campaigns 및 Canvases를 통해 기존과 동일하게 WhatsApp 템플릿 메시지와 응답 메시지를 계속 전송합니다.
- **인바운드 메시지는 Meta Business Agent가 라우팅합니다.** 사용자로부터 수신되는 각 인바운드 메시지에 대해, Meta Business Agent가 Braze로 전달할지 또는 자체적으로 처리할지를 결정합니다.
  - **Meta가 메시지를 Braze로 라우팅하는 경우:** 현재 인바운드 WhatsApp 메시지가 처리되는 방식과 동일하게 처리됩니다. 기존에 구축한 로직에 따라 Campaign 및 Canvas 액션 기반 트리거와 작업 경로가 작동합니다.
  - **Meta Business Agent가 메시지를 자체 처리하는 경우:** Braze는 현재 해당 활동을 전달하는 별도 채널(대기 메시지 및 메시지 에코)을 처리하지 않습니다. 에이전트가 처리하기로 결정한 인바운드 메시지와 해당 메시지에 대한 에이전트의 응답은 현재 Braze 화면에서 확인할 수 없습니다.

| 메시지 흐름 | 현재 동작 |
| --- | --- |
| Campaigns 또는 캔버스 단계를 통해 전송되는 WhatsApp 템플릿 메시지 및 응답 메시지 | 영향 없음; Braze가 구성된 대로 계속 전송 |
| Meta가 Braze로 라우팅하는 인바운드 메시지 | 정상적으로 처리됨; 기존 트리거 및 작업 경로 적용 |
| Meta Business Agent가 자체 처리하는 인바운드 메시지 | 현재 Braze에서 확인 불가; 인바운드에 대한 기존 트리거 및 작업 경로가 작동하지 않음 |
| Meta Business Agent가 전송하는 아웃바운드 메시지 | 현재 Braze에서 확인 불가 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="메시지 흐름" }

## Meta Business Agent 활성화 {#enable-meta-business-agent}

Meta Business Agent는 Braze가 아닌 Meta 도구에서 전화번호별로 활성화합니다.

1. [WhatsApp Manager](https://business.facebook.com/wa/manage/home/)에서 적격 여부를 확인하고 전화번호에 대해 활성화하며, Meta Business Agent 서비스 약관에 동의합니다.
2. Meta의 [에이전트 구성 API](https://developers.facebook.com/documentation/meta-business-agent/reference/configure/agent-skills)를 통해 에이전트의 지식과 스킬(비즈니스 정보, FAQ, 파일, 커넥터)을 구성합니다.
3. [Agent Settings](https://developers.facebook.com/documentation/meta-business-agent/reference/onboard/agent-settings)를 사용하여 에이전트를 켭니다.

## 활성화 전 고려 사항 {#things-to-weigh-before-enabling-it}

- **Braze 측 토글 없음:** Meta Business Agent의 활성화, 구성, 비활성화는 모두 Meta 도구에서 이루어지며, Braze에서 켜거나 끌 수 있는 항목은 없습니다.
- **과금:** Meta Business Agent 도입에 따라, 비템플릿 메시지는 이제 서비스(기존 카테고리) 또는 Meta Business Agent(신규 카테고리)의 두 가지 카테고리 중 하나로 분류됩니다.
  - Braze가 처리하는 비템플릿 응답은 2026년 10월 1일부터 서비스 메시지로 과금됩니다.
    - 인바운드에 마케팅, 유틸리티 또는 인증 템플릿으로 응답하는 경우, 해당 유형으로 과금됩니다.
  - Meta Business Agent 메시지는 2026년 8월 1일부터 Meta에서 직접 과금됩니다. 자세한 내용은 Meta의 가격 정책을 참조하세요.
  - 메시지는 하나의 카테고리로만 분류되므로, 동일한 메시지에 대해 이중으로 과금되는 일은 없습니다.