---
nav_title: FAQ
article_title: Audience Sync FAQ
alias: /partners/audience_sync_faq/
description: "이 문서에서는 Audience Sync에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
page_order: 80
tool:
  - Canvas

---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 문서에서는 Audience Sync에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## Audience Sync 파트너 대시보드에 오디언스가 채워지는 데 얼마나 걸리나요? {#how-long-does-it-take-for-my-audiences-to-populate-in-my-audience-sync-partner-dashboard}

오디언스가 채워지는 데 걸리는 시간은 특정 파트너에 따라 다릅니다. 모든 네트워크는 Braze의 요청을 처리하고 사용자를 매칭하려고 시도합니다. 이 과정은 일반적으로 6~48시간이 소요될 수 있습니다.

각 Audience Sync 파트너의 설명서에 있는 문제 해결 섹션에서 구체적인 시간 범위를 확인할 수 있습니다.

## Audience Sync에서 어떤 유형의 퍼스트파티 데이터를 사용할 수 있나요? {#what-type-of-first-party-data-can-i-use-in-my-audience-sync}

각 파트너에 사용되는 특정 필드는 파트너의 요구 사항에 따라 다를 수 있습니다.

예를 들어, Facebook에 Audience Sync를 구성할 때 이메일, 전화번호, 이름, 성 등 다양한 퍼스트파티 필드를 사용할 수 있지만, Snapchat에서는 이메일, 전화번호 또는 모바일 광고주 ID 중 하나만 선택할 수 있습니다.

동기화할 수 있는 사용자 필드는 Braze 표준 속성 및 모바일 광고 ID와 연관된다는 점에 유의해야 합니다. SDK 또는 API를 통해 이 데이터를 적절하게 전달해야 합니다.

## 각 Audience Sync 파트너에게 데이터를 전송하기 위해 처리될 때 어떤 일이 발생하나요? {#what-happens-when-my-data-is-being-processed-to-send-to-each-audience-sync-partner}

Audience Sync 대상으로 전송하도록 선택한 데이터는 정규화됩니다. 각 파트너는 API 요구 사항에 따라 데이터 정규화에 대한 서로 다른 사양을 가질 수 있으므로, 자세한 내용은 각 파트너별 엔드포인트를 검토하세요.

또한 Braze는 Audience Sync 파트너와 사용자를 동기화하기 전에 모든 데이터를 해시 처리하여 모든 PII가 SHA256으로 해시되도록 합니다.

## 일부 파트너에서는 한 단계에서 여러 식별자를 선택할 수 있는데, 다른 파트너에서는 하나의 식별자만 선택할 수 있는 이유는 무엇인가요? {#why-can-i-select-multiple-identifiers-in-one-step-for-some-partners-but-can-only-select-one-identifier-for-others}

이는 파트너 통합 방법에 의해 결정되며 Braze가 제어하지 않습니다. 일부 파트너(예: Meta)는 여러 식별자를 동기화할 수 있도록 허용하고, 다른 파트너(예: Google)는 특정 시점에 사용자당 하나의 식별자만 동기화할 수 있도록 허용합니다.

## 통합을 다시 연결하려면 어떻게 해야 하나요? {#how-do-i-reconnect-my-integration}

통합을 연결한 이전 사용자가 더 이상 비즈니스에 소속되어 있지 않은 경우, **Change Account**를 선택하여 새 사용자로 통합을 업데이트해야 합니다. 그런 다음 **Confirm**을 선택하고 새 사용자로 연결합니다. 이전 사용자에서 새 사용자로 전환하는 동안 동기화가 진행되면 활성 Canvases가 중단될 수 있으므로, Canvas에 사용자가 스케줄된 진입 전과 같이 활성 동기화가 진행되지 않는 시점에 사용자를 변경하는 것을 권장합니다.

다시 연결하는 사용자는 모든 오디언스에 대한 읽기 및 쓰기 권한을 모두 가지고 있어야 사용자가 파트너에게 성공적으로 동기화될 수 있습니다. 통합을 다시 연결하는 사용자가 동일한 광고 계정 및 오디언스에 접근할 수 있는지 확인하세요. 기존 캔버스 단계를 편집할 필요는 없습니다.

## Audience Sync를 생성하고 관리할 때 발생할 수 있는 일반적인 오류는 무엇인가요? {#what-are-common-errors-that-can-occur-when-creating-and-managing-my-audience-syncs}

| 오류 | 원인 | 해결 방법 |
| --- | --- | --- |
| 유효하지 않은 토큰 | 특정 광고 네트워크에 로그인하기 위한 비밀번호를 변경했거나 자격 증명이 만료된 경우 발생할 수 있습니다. | 해당 파트너 페이지로 이동하여 계정을 연결 해제한 후 다시 연결하세요. |
| 오디언스 크기가 너무 작음 | 오디언스에서 사용자를 제거하는 Audience Sync 단계를 생성한 경우 발생할 수 있습니다. 오디언스 크기가 0에 가까워지면 네트워크에서 오디언스 크기가 너무 작아 서비스할 수 없다고 표시할 수 있습니다. | 오디언스 크기를 완전히 소진하지 않는 방식으로 정기적으로 사용자를 추가하고 제거하는 Audience Sync 전략을 고려하고 있는지 확인하세요. |
| 오디언스가 존재하지 않음 | Audience Sync 단계가 존재하지 않는 오디언스를 사용합니다. 오디언스에 접근하는 데 필요한 권한이 없는 경우에도 트리거될 수 있습니다. | Audience Sync 구성에 활성 오디언스를 추가하거나 새 오디언스를 생성하세요. |
| 광고 계정 접근 시도 | 광고 계정, 선택한 오디언스 또는 둘 다에 대한 권한이 없는 경우 이 오류가 발생합니다. | 광고 계정 관리자와 협력하여 적절한 접근 권한을 확보하세요. |
| 유효하지 않은 설정 | 광고 계정, 오디언스 또는 매칭할 사용자 필드를 포함하여 Canvas에서 특정 Audience Sync 대상을 구성하지 않은 경우 발생할 수 있습니다. | 시작하기 전에 각 파트너의 구성을 완료하세요. |
| 서비스 약관 | Facebook과 같은 일부 Audience Sync 대상의 경우, Audience Sync 기능을 사용하려면 광고 네트워크에서 특정 서비스 약관에 동의해야 합니다. 적절한 약관에 동의하지 않은 경우 이 오류가 트리거됩니다. | 각 파트너의 필수 약관에 동의했는지 확인하세요. Facebook의 경우 구체적으로 [Facebook 문제 해결]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#troubleshooting)을 검토하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Audience Sync를 생성하고 관리할 때 발생할 수 있는 일반적인 오류는 무엇인가요?" }