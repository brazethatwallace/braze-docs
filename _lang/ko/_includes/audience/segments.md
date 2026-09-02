{% if include.section == "Differing audience size" %}

Campaign이나 Canvas에 표시되는 대상 집단 규모는 추가 필터 없이 해당 Segment를 Campaign이나 Canvas에 직접 추가하는 경우에도 해당 [Segment의 도달 가능한 오디언스 규모]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size#segment-membership-calculation)와 다를 수 있습니다.
이는 여러 가지 이유로 발생할 수 있습니다:

- 글로벌 컨트롤 그룹이 Campaign 또는 Canvas에 적용되면 해당 글로벌 컨트롤 그룹에 속한 사용자는 도달 가능 사용자 수에서 제외됩니다.
- Campaign 또는 Canvas의 대상 집단 규모는 다양한 메시지 채널을 통해 연락할 수 없는 사용자를 제외하며, 동작은 채널마다 다릅니다. 예를 들어, Campaign 또는 Canvas의 도달 가능한 오디언스에는 탈퇴했거나 스팸으로 표시된 사용자(이메일의 경우) 또는 하드바운스된 사용자(이메일의 경우)가 제외됩니다. 그러나 Segment 자체는 예상 이메일 도달 가능 사용자 수를 표시할 때만 옵트아웃을 제외합니다.
- Braze는 선택한 구독 그룹에 속한 사용자에게만 SMS 메시지를 보내므로 Campaign 또는 Canvas의 SMS 대상 집단에서도 선택한 구독 그룹에 속하지 않은 사용자는 제외됩니다.

{% endif %}

{% if include.section == "Refresh settings" %}

정기적으로 확장을 새로고침할 필요가 없는 경우 새로고침 설정을 사용하지 않고 저장할 수 있으며, Braze는 해당 시점의 사용자 멤버십을 기반으로 세그먼트 확장을 생성하는 기본값을 적용합니다. 오디언스를 한 번만 생성한 다음 일회성 Campaign으로 타겟팅하려는 경우 기본 동작을 사용하세요.

세그먼트는 항상 최초 저장 후 처리가 시작됩니다. 세그먼트가 새로고침될 때마다 Braze는 세그먼트를 다시 실행하고 새로고침 시점의 사용자를 반영하도록 세그먼트 멤버십을 업데이트합니다. 이를 통해 반복 Campaign이 가장 관련성 높은 사용자에게 도달하는 데 도움이 됩니다.

#### 반복 새로고침 설정하기 {#setting-up-a-recurring-refresh}

새로고침 설정을 지정하여 반복 스케줄을 설정하려면 **새로고침 활성화**를 선택합니다. 새로고침 설정을 지정하는 옵션은 SQL 세그먼트, CDI 세그먼트 확장 및 간단한 양식 기반 세그먼트 확장을 포함한 모든 유형의 세그먼트 확장에 사용할 수 있습니다.

{% alert important %}
데이터 관리를 최적화하기 위해 사용되지 않는 세그먼트 확장에 대해서는 새로고침 설정이 자동으로 해제됩니다. 세그먼트 확장은 다음과 같은 경우 사용되지 않는 것으로 간주됩니다:

- 활성 또는 비활성(초안, 중지됨, 아카이브됨) Campaigns, Canvases 또는 Segments에서 사용되지 않는 경우
- 7일 이상 수정되지 않은 경우

이 설정이 해제되면 Braze는 회사 연락처 및 확장 생성자에게 알림을 보냅니다. 매일 확장을 재생성하는 옵션은 언제든지 다시 활성화할 수 있습니다.
{% endalert %}

#### 새로고침 설정 선택하기 {#selecting-your-refresh-settings}

![새로고침 주기를 주 단위로, 시작 시간을 오전 10시로, 요일을 월요일로 선택한 새로고침 간격 설정.]({% image_buster /assets/img/segment/segment_interval_settings.png %}){: style="max-width:50%;"}

**새로고침 간격 설정** 패널에서 이 세그먼트 확장을 새로고침할 주기를 시간별, 일별, 주별 또는 월별 중에서 선택할 수 있습니다. 또한 새로고침이 수행될 특정 시간(회사 시간대 기준)을 선택해야 합니다. 예를 들면 다음과 같습니다:

- 매주 월요일 오전 11시(회사 시간 기준)에 발송되는 이메일 Campaign이 있고, 발송 직전에 세그먼트를 새로고침하려면 매주 월요일 오전 10시로 새로고침 스케줄을 선택해야 합니다.
- 세그먼트를 매일 새로고침하려면 일별 새로고침 주기를 선택한 다음 새로고침할 시간을 선택하세요.

{% alert note %}
양식 기반 세그먼트 확장에서는 시간별 새로고침 스케줄을 설정하는 기능을 사용할 수 없습니다(일별, 주별 또는 월별 스케줄은 설정할 수 있습니다).
{% endalert %}

#### 크레딧 소비 및 추가 비용 {#credit-consumption-and-additional-costs}

새로고침은 세그먼트의 쿼리를 다시 실행하기 때문에 SQL 세그먼트의 각 새로고침은 SQL 세그먼트 크레딧을 소비하고, CDI 세그먼트 확장의 각 새로고침은 서드파티 데이터 웨어하우스 내에서 비용을 발생시킵니다.

{% alert note %}
데이터 처리 시간으로 인해 세그먼트를 새로고침하는 데 최대 60분이 소요될 수 있습니다. 현재 새로고침 중인 세그먼트는 세그먼트 확장 목록에서 "처리 중" 상태로 표시됩니다. 이에 따른 몇 가지 참고 사항이 있습니다:

- 특정 시간 전에 세그먼트 처리를 완료하려면 새로고침 시간을 60분 더 일찍 선택하세요.
- 특정 세그먼트 확장에 대해 한 번에 하나의 새로고침만 수행할 수 있습니다. 기존 새로고침이 이미 처리를 시작한 상태에서 새 새로고침이 시작되는 충돌이 발생하면 Braze는 새 새로고침 요청을 취소하고 진행 중인 처리를 계속합니다.
{% endalert %}

#### 오래된 확장을 자동으로 비활성화하는 기준 {#criteria-to-automatically-disable-stale-extensions}

세그먼트 확장이 오래되면 스케줄된 새로고침이 자동으로 비활성화됩니다. 세그먼트 확장은 다음 기준을 충족하는 경우 오래된 것으로 간주됩니다:

- 활성 Campaigns이나 Canvases에서 사용되지 않음
- 활성 Campaign 또는 Canvas에 있는 Segment에서 사용되지 않음
- [분석 추적]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)이 켜져 있는 Segment에서 사용되지 않음
- 7일 이상 수정되지 않음
- 7일 이상 Campaign이나 Canvas(초안 포함) 또는 Segment에 추가되지 않음

세그먼트 확장에 대해 스케줄된 새로고침이 비활성화되면 해당 확장에 이를 알리는 알림이 표시됩니다.

!["이 확장은 활성 Campaigns, Canvases 또는 Segments에서 사용되지 않기 때문에 스케줄된 새로고침이 해제되었습니다. 세그먼트 확장은 2025년 2월 23일 오전 12:00에 비활성화되었습니다."라는 알림.]({% image_buster /assets/img/segment/segment_extension_disabled.png %})

오래된 세그먼트 확장을 사용할 준비가 되면 새로고침 설정을 검토하고 사용 사례에 맞는 새로고침 스케줄을 선택한 다음 수정 사항을 저장하세요.

{% endif %}

{% if include.section == "same channel identifier" %}

메시지가 수신, 열람 또는 클릭되면 Braze는 해당 상호작용을 기록한 프로필과 동일한 채널 식별자를 공유하는 모든 프로필의 데이터를 업데이트합니다(예: 이메일의 경우 동일한 이메일 주소, SMS 또는 WhatsApp의 경우 동일한 전화번호). 메시지를 수신, 열람 또는 클릭한 사용자와 식별자를 공유하는 사용자는 원래 Campaign에 포함되지 않았거나 메시지를 직접 받지 않았더라도 이 필터에 매칭될 수 있습니다.

{% endif %}

{% if include.section == "Canvas variant archived segment" %}

### 아카이브된 Segment로 인해 캔버스 배리언트를 삭제할 수 없는 경우 {#cant-delete-a-canvas-variant-because-of-an-archived-segment}

Braze가 Segment 필터가 해당 배리언트를 여전히 참조하고 있어 캔버스 배리언트 삭제를 차단하는 경우, 해당 참조를 사용하는 Segment(아카이브된 Segment 포함)를 열고 필터에서 해당 배리언트를 제거하세요. Segment를 저장한 다음 Canvas로 돌아가 배리언트 삭제를 다시 시도하세요.

Canvas를 참조하는 Segment를 찾으려면 Canvas를 열고 오디언스 필터를 검토하거나, 각 Segment의 [메시징 사용 현황]({{site.baseurl}}/user_guide/audience/segments/managing_segments#messaging-use) 섹션에서 연결된 Canvases를 확인하세요.

{% endif %}