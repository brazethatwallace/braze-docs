---
nav_title: FAQ
article_title: 자동 IP 워밍 FAQ
channel: email
page_order: 3
description: "Braze의 자동 IP 워밍에 대해 자주 묻는 질문에 대한 답변입니다."
---

# 자동 IP 워밍 FAQ {#automated-ip-warming-faq}

> [자동 IP 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming)에 대한 일반적인 질문에 대한 답변입니다. IP 워밍 개념 및 수동 스케줄에 대해서는 [IP 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)을 참조하세요.

## 자동 IP 워밍은 언제 사용해야 하나요? {#when-should-i-use-automated-ip-warming}

다음과 같은 경우에 자동 IP 워밍을 사용합니다:

- 새로운 IP 주소를 처음으로 워밍할 때
- 새로운 하위 도메인을 사용하는 새 비즈니스 단위 또는 브랜드를 워밍할 때
- 전달 가능성을 개선하기 위해 기존 IP를 재워밍할 때
- 특정 메일박스 제공업체에 대한 전달 가능성을 개선하기 위해 재워밍할 때

설정 단계 및 전제 조건은 [자동 IP 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming)을 참조하세요.

## 시작 날짜는 얼마나 앞서 설정해야 하나요? {#how-far-in-advance-must-the-start-date-be}

시작 날짜는 워크스페이스 시간대(또는 워크스페이스에 별도 설정이 없는 경우 회사 시간대)를 기준으로 내일 이후여야 합니다.

Braze는 해당 시간대의 자정에 당일과 다음 날(발송 0~1일 전)에 해당하는 Campaigns를 생성합니다. 플랜을 시작하면 예정된 Campaigns도 즉시 생성됩니다.

## 몇 개의 템플릿이 필요한가요? {#how-many-templates-are-required}

Braze는 계획된 발송량과 선택한 Segments에서 이메일 수신 가능한 사용자(전체 Segment 크기가 아님)를 기반으로 최소 필요 수를 계산합니다. 전달 가능성 문제가 발생해도 시스템이 중단 없이 조정할 수 있도록 최소 필요 수보다 더 많은 템플릿을 제공하세요. 자세한 내용은 [3단계: 발송할 메시지 선택]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send)을 참조하세요.

## 동일한 Segment를 여러 워밍업 시도에 사용할 수 있나요? {#can-i-use-the-same-segment-for-multiple-warmup-attempts}

하나의 활성 플랜 내에서 Braze는 동일한 템플릿에 대해 이전 IP 워밍 발송을 이미 수신한 사용자를 자동으로 제외합니다. 플랜을 중지하고 동일한 Segments를 재사용하는 새 플랜을 시작하는 경우, 이전 플랜의 Campaigns에서 메시지를 수신한 사용자를 제외하는 필터를 추가하세요.

## 같은 날 한 사용자가 두 개 이상의 이메일 템플릿을 받을 수 있나요? {#can-a-user-receive-more-than-one-email-template-on-the-same-day}

네, 가능합니다. Braze는 플랜 내에서 이미 특정 템플릿을 수신한 사용자를 제외하지만, 다른 템플릿을 수신한 사용자는 여전히 수신 대상으로 유지됩니다. 하루 스케줄에 사용할 수 있는 오디언스가 소진되면, 플랜이 템플릿을 다시 순환하며 일부 사용자가 해당 날에 두 번째 템플릿을 수신하게 됩니다.

이는 선택한 Segments 전체에서 이메일 수신 가능한 사용자의 총 수가 **목표 발송량**보다 작을 때 발생하며, 플랜의 마지막 날 또는 며칠 동안 가장 자주 나타납니다. 예를 들어, 이메일 수신 가능한 사용자가 400,000명이고 목표 발송량이 600,000인 경우, 마지막 날에 약 200,000명의 사용자가 두 개의 템플릿을 수신하게 됩니다. 이를 방지하려면 이메일 수신 가능한 사용자의 총 수를 목표 발송량 이상으로 유지하세요. 자세한 내용은 [오디언스 크기 및 사용자당 다중 발송]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#audience-size-and-multiple-sends-per-user)을 참조하세요.

## 스케줄 중간에 IP 워밍을 시작할 수 있나요? {#can-i-start-ip-warming-mid-schedule}

자동화된 IP 워밍은 항상 램프 시작부터 스케줄을 구성합니다. 스케줄 중간 시작을 근사하게 구현하려면, **현재 일일 발송량**을 현재 발송량에 맞게 0보다 큰 값으로 설정하세요. 현재 발송량이 0보다 크면, Braze는 1일차에 IP 수 스케일링을 적용하지 않습니다.

## 발송에는 어떤 시간대가 사용되나요? {#what-time-zone-is-used-for-sending}

발송 시 워크스페이스 시간대가 설정되어 있으면 해당 시간대를 사용하고, 그렇지 않으면 회사 시간대를 사용합니다. Campaigns는 각 사용자의 현지 시간대로 생성되지 않습니다. 현지 시간대로 발송하려면, 플랜에서 생성된 Campaigns를 수동으로 업데이트하세요.

## 동시에 몇 개의 IP 워밍 플랜을 실행할 수 있나요? {#how-many-ip-warming-plans-can-run-at-the-same-time}

두 개 이상의 플랜을 동시에 실행할 수 있습니다. 자세한 내용은 [다중 IP 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#multiple-ip-warming)을 참조하세요.

## 여러 IP가 포함된 IP 풀에서 발송량은 어떻게 확장되나요? {#how-does-volume-scale-for-ip-pools-with-multiple-ips}

**현재 일일 발송량**이 0일 때, 1일차는 IP당 50건 또는 총 500건 중 더 낮은 값에서 시작합니다. 이후 발송량은 발송일마다 약 1.75배씩 증가하며, 램프 가드레일의 적용을 받습니다. 예를 들어, IP가 10개인 경우: 500 → 875 → 1,532 → 2,681.

커스텀 현재 발송량을 0보다 큰 값으로 설정하면, 1일차에 IP 수 기반 스케일링이 적용되지 않습니다. 다중 IP 플랜에 대한 자세한 내용은 [하나의 풀에서 여러 IP 워밍하기]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#warm-multiple-ips-in-one-pool)를 참조하세요.

## 자동 IP 워밍은 Campaign별 사용량 제한을 지원하나요? {#does-automated-ip-warming-support-rate-limiting-per-campaign}

아니요. 각 Campaign은 Campaign별 사용량 제한 없이 설정된 시간에 발송됩니다.

## Braze는 IP 워밍 중 언제 발송량을 유지하나요? {#when-does-braze-hold-volume-during-ip-warming}

Braze는 12~20시간 전에 발송된 Campaigns의 전달 가능성을 평가합니다. 전달, 열람, 반송 또는 스팸 신고 비율이 [활성 IP 워밍 중]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#during-active-ip-warming)의 벤치마크를 초과하면, Braze는 발송량을 늘리는 대신 다음 발송일에 발송량을 유지합니다.

## 볼륨이 보류되면 어떻게 되나요? {#what-happens-when-volume-is-held}

볼륨 보류는 해당 임계값을 초과했을 때 Braze가 자동으로 적용하는 조정입니다. 다음 예약 발송은 볼륨을 늘리지 않고 동일한 볼륨을 유지합니다. Braze는 향후 스케줄 항목을 재계획하고, 플랜에서 기존의 향후 Campaigns를 아카이브한 후, 업데이트된 스케줄에 맞춰 새로운 Campaigns를 즉시 생성합니다. 이로 인해 목표 볼륨에 도달하는 데 더 오래 걸릴 수 있습니다.

## Campaign 편집 사항이 IP 워밍 트래커에 반영되지 않는 이유는 무엇인가요? {#why-dont-campaign-edits-appear-on-the-ip-warming-tracker}

자동 IP 워밍으로 생성된 Campaign에 대한 변경 사항(스케줄, Segment 또는 발송량 등)은 IP 워밍 트래커에 다시 동기화되지 않습니다. 관련 설정 참고 사항은 [3단계: 발송할 메시지 선택]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send)을 참조하세요.

## IP 워밍 플랜을 중단할 수 있나요? {#can-i-stop-an-ip-warming-plan}

네. 중단하면 플랜이 영구적으로 종료됩니다. Braze는 연결된 Campaigns를 비활성화하고 이후 새로운 Campaign을 생성하지 않습니다. 중단된 플랜은 재개할 수 없으므로 계속하려면 새 플랜을 만들어야 합니다. 중단 후 다시 시작하는 단계는 [IP 워밍 플랜 중단]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#stop-an-ip-warmup-plan)을 참조하세요.

## IP 워밍 플랜은 언제 완료로 표시되나요? {#when-is-an-ip-warming-plan-marked-as-complete}

플랜은 마지막 예약된 발송일이 끝난 후, 유효 시간대(워크스페이스 또는 회사)의 자정에 완료로 표시됩니다. 예를 들어, 마지막 Campaign이 오후 8시에 발송되면, 플랜은 4시간 후 자정에 완료로 표시됩니다.

## 어떤 데이터를 다운로드할 수 있나요? {#what-data-can-i-download}

CSV 내보내기에는 Campaign별 행과 일별 측정기준이 포함됩니다: *발송*, *전달*, *반송*, *스팸 신고*, *총 열람*, *고유 열람*, *클릭*, *탈퇴*. 추적 테이블은 같은 날 발송된 여러 Campaign을 일별 뷰로 집계합니다. 자세한 내용은 [IP 워밍이 완료되는 시점]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#when-an-ip-warming-completes)을 참조하세요.