---
nav_title: Braze Go
permalink: "/braze_go/"
hidden: true
noindex: true
hide_toc: true
---

# Braze Go

> Braze Go는 Braze 고객 인게이지먼트 플랫폼에 대한 간소화된 액세스를 제공하여 마케팅 팀이 어디서든 시작하고 어디로든 나아갈 수 있도록 지원합니다. 간편함과 효율성을 위해 설계된 Braze Go는 일부 신흥 시장에 맞춤화되어 있습니다.

{% alert important %}
Braze Go는 모든 시장에서 이용할 수 있는 것은 아닙니다. Braze Go에 대해 더 알고 싶으시면 계정 매니저에게 문의하세요.
{% endalert %}

Braze Go는 Braze와 동일한 모든 기능을 제공하며, 다음 기능에 대해 집중적인 변경 사항이 적용됩니다:

- 최대 30개의 활성 Campaign을 보유할 수 있습니다.
- 최대 20개의 활성 Canvas를 보유할 수 있습니다.
- 총 REST API 기본 사용량 제한은 워크스페이스당 시간당 50,000건입니다.
    - Braze Go 이외의 사용에 대해서는 [REST API 제한]({{site.baseurl}}/api/api_limits#rate-limits-by-request-type)에서 자세히 알아보세요.
- Campaign 및 Canvas 상호작용 데이터 보존 기간은 2개월이며 복원이 불가합니다.
    - Braze Go 이외의 사용에 대해서는 [메시징 상호작용 데이터 가용성]({{site.baseurl}}/messaging_interaction_data)에서 자세히 알아보세요.

{% alert note %}
Campaign 및 Canvas의 상호작용 데이터는 Snowflake 데이터와 다르며 어떠한 영향도 미치지 않습니다.
{% endalert %}

- Braze 간 웹훅은 지원되지 않습니다.
- 태그와 관련된 필터는 지원되지 않으며, 구체적으로 다음 필터가 해당됩니다:
    - 태그가 있는 Campaign 또는 Canvas를 클릭했거나 열람함
    - 태그가 있는 Campaign 또는 Canvas에서 마지막으로 메시지를 수신함
    - 태그가 있는 Campaign 또는 Canvas를 수신함
- Braze는 또한 고객 프로필 이벤트 및 구매 데이터에 대해 데이터 보존 정책을 시행할 수 있으며, 1년 이내에 다시 수행되지 않은 1년 이상 된 이벤트, 구매 또는 둘 다를 제거합니다. 그러나 이 데이터는 SQL 세그먼트 확장에서 2년간 계속 사용할 수 있습니다.

이 문서에 설명된 기능이 업데이트되면 이 문서에 반영되며 [릴리스 노트]({{site.baseurl}}/help/release_notes#most-recent-braze-release-notes)에 기록됩니다.