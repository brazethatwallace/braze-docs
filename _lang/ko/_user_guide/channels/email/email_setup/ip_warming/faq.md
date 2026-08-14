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

다음과 같은 경우에 자동 IP 워밍을 사용하세요:

- 새 IP 주소를 처음으로 워밍할 때
- 새 하위 도메인으로 새 비즈니스 유닛 또는 브랜드를 워밍할 때
- 전달 가능성을 개선하기 위해 기존 IP를 재워밍할 때
- 특정 메일박스 제공업체에 대한 전달 가능성을 개선하기 위해 재워밍할 때

설정 단계 및 사전 요구 사항은 [자동 IP 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming)을 참조하세요.

## 시작 날짜는 얼마나 미리 설정해야 하나요? {#how-far-in-advance-must-the-start-date-be}

시작 날짜는 워크스페이스 시간대(또는 워크스페이스에 재정의가 없는 경우 회사 시간대) 기준으로 내일 이후여야 합니다.

Braze는 해당 시간대의 자정에 당일 및 다음 날(발송 0~1일 전)에 대한 Campaign을 생성합니다. 플랜을 시작하면 예정된 Campaign도 즉시 생성됩니다.

## 몇 개의 템플릿이 필요한가요? {#how-many-templates-are-required}

Braze는 계획된 발송량과 선택한 Segment의 이메일 발송 가능한 사용자 수(전체 Segment 크기가 아님)를 기반으로 최소값을 계산합니다. 시스템이 전달 가능성 문제 발생 시 중단 없이 조정할 수 있도록 최소값보다 더 많은 템플릿을 제공하세요. 자세한 내용은 [3단계: 발송할 메시지 선택]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send)을 참조하세요.

## 여러 워밍 시도에 동일한 Segment를 사용할 수 있나요? {#can-i-use-the-same-segment-for-multiple-warmup-attempts}

단일 활성 플랜 내에서 Braze는 동일한 템플릿에 대해 이전 IP 워밍 발송을 이미 수신한 사용자를 자동으로 제외합니다. 플랜을 중지하고 동일한 Segment를 재사용하는 새 플랜을 시작하는 경우, 이전 플랜의 Campaign을 수신한 사용자를 제외하는 필터를 추가하세요.

## 스케줄 중간에 IP 워밍을 시작할 수 있나요? {#can-i-start-ip-warming-mid-schedule}

자동 IP 워밍은 항상 램프 시작부터 스케줄을 구성합니다. 중간 스케줄 시작을 근사하려면 **현재 일일 발송량**을 현재 발송량에 맞게 0보다 크게 설정하세요. 현재 발송량이 0보다 크면 Braze는 1일차에 IP 수 스케일링을 적용하지 않습니다.

## 발송에 어떤 시간대가 사용되나요? {#what-time-zone-is-used-for-sending}

워크스페이스 시간대가 설정된 경우 해당 시간대를 사용하고, 그렇지 않으면 회사 시간대를 사용합니다. Campaign은 각 사용자의 현지 시간대로 생성되지 않습니다. 현지 시간으로 발송하려면 플랜에서 생성된 Campaign을 수동으로 업데이트하세요.

## 동시에 몇 개의 IP 워밍 플랜을 실행할 수 있나요? {#how-many-ip-warming-plans-can-run-at-the-same-time}

워크스페이스가 여러 플랜을 지원하는 경우 둘 이상의 플랜을 동시에 실행할 수 있습니다. 자세한 내용은 [다중 IP 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#multiple-ip-warming)을 참조하세요.

## 여러 IP가 있는 IP 풀에서 발송량은 어떻게 스케일링되나요? {#how-does-volume-scale-for-ip-pools-with-multiple-ips}

**현재 일일 발송량**이 0인 경우, 1일차는 IP당 50건 또는 총 500건 중 더 낮은 값으로 시작합니다. 이후 발송량은 발송일마다 약 1.75배씩 증가하며, 램프 가드레일의 적용을 받습니다. 예를 들어, IP 10개인 경우: 500 → 875 → 1,532 → 2,681.

0보다 큰 커스텀 현재 발송량을 설정하면 1일차에 IP 수 스케일링이 적용되지 않습니다. 다중 IP 플랜에 대한 자세한 내용은 [하나의 풀에서 여러 IP 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#warm-multiple-ips-in-one-pool)을 참조하세요.

## 자동 IP 워밍은 Campaign별 사용량 제한을 지원하나요? {#does-automated-ip-warming-support-rate-limiting-per-campaign}

아니요. 각 Campaign은 Campaign별 사용량 제한 없이 설정된 시간에 발송됩니다.

## Braze는 IP 워밍 중 언제 발송량을 유지하나요? {#when-does-braze-hold-volume-during-ip-warming}

Braze는 12~20시간 전에 발송된 Campaign의 전달 가능성을 평가합니다. 전달률, 열람률, 반송률 또는 스팸 신고율이 [활성 IP 워밍 중]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#during-active-ip-warming)의 벤치마크를 초과하면, Braze는 다음 발송일에 발송량을 증가시키지 않고 유지합니다.

## 발송량이 유지되면 어떻게 되나요? {#what-happens-when-volume-is-held}

발송량 유지는 해당 임계값이 초과될 때 Braze가 적용하는 자동 조정입니다. 다음 예정된 발송은 증가하지 않고 동일한 발송량을 유지합니다. Braze는 향후 스케줄 항목을 재계획하고, 플랜에서 기존의 향후 Campaign을 아카이브하며, 업데이트된 스케줄에 대한 새 Campaign을 즉시 생성합니다. 플랜이 목표 발송량에 도달하는 데 더 오래 걸릴 수 있습니다.

## Campaign 수정 사항이 IP 워밍 트래커에 표시되지 않는 이유는 무엇인가요? {#why-dont-campaign-edits-appear-on-the-ip-warming-tracker}

자동 IP 워밍으로 생성된 Campaign에 대한 변경 사항(스케줄, Segment 또는 발송량 등)은 IP 워밍 트래커에 다시 동기화되지 않습니다. 관련 설정 참고 사항은 [3단계: 발송할 메시지 선택]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send)을 참조하세요.

## IP 워밍 플랜을 중지할 수 있나요? {#can-i-stop-an-ip-warming-plan}

네. 중지하면 플랜이 영구적으로 종료됩니다. Braze는 연결된 Campaign을 비활성화하고 향후 Campaign을 생성하지 않습니다. 중지된 플랜은 재개할 수 없으며, 계속하려면 새 플랜을 생성해야 합니다. 중지 후 이어서 진행하는 단계는 [IP 워밍 플랜 중지]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#stop-an-ip-warmup-plan)를 참조하세요.

## IP 워밍 플랜은 언제 완료로 표시되나요? {#when-is-an-ip-warming-plan-marked-as-complete}

플랜은 마지막 예정된 발송일이 끝난 후, 유효 시간대(워크스페이스 또는 회사)의 자정에 완료로 표시됩니다. 예를 들어, 마지막 Campaign이 오후 8시에 발송되면 4시간 후 자정에 플랜이 완료로 표시됩니다.

## 어떤 데이터를 다운로드할 수 있나요? {#what-data-can-i-download}

CSV 내보내기에는 일별 측정기준이 포함된 Campaign별 행이 포함됩니다: *발송*, *전달*, *반송*, *스팸 신고*, *총 열람*, *고유 열람*, *클릭*, *탈퇴*. 트래커 테이블은 같은 날의 여러 Campaign을 일별 보기로 집계합니다. 자세한 내용은 [IP 워밍 완료 시]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#when-an-ip-warming-completes)를 참조하세요.