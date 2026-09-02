{% if include.section == "Integration Tabs" %}

{% tabs local %}
{% tab standard %}
표준 통합은 Shopify 온라인 스토어에 맞춤화되어 있으며, 원활하고 간편한 설정 프로세스를 제공합니다. 이 옵션을 사용하면 Shopify 스토어를 Braze에 빠르게 연결하여 광범위한 기술 전문 지식 없이도 강력한 고객 참여 툴을 활용할 수 있습니다. 이 통합 옵션을 통해 고객 데이터를 동기화하고, 개인화된 메시징을 자동화하며, 포괄적인 Braze 기능을 통해 마케팅 활동을 강화할 수 있습니다.

Shopify 표준 통합을 사용하려면 [Shopify 표준 통합 설정]({{site.baseurl}}/shopify_standard_integration)을 참조하세요.
{% endtab %}

{% tab custom %}
커스텀 통합은 Shopify Hydrogen을 사용하거나 헤드리스 스토어를 지원하는 경우 더 유연하고 구성 가능한 솔루션을 제공합니다. 이 옵션을 사용하면 Braze SDK를 Shopify 환경에 직접 구현하여 더 깊은 통합과 맞춤형 기능을 활성화할 수 있습니다. 고유한 고객 경험을 창출하거나 특정 워크플로를 최적화하려는 경우, 커스텀 통합은 헤드리스 설정에서 Braze의 기능을 최대한 활용하는 데 필요한 도구를 제공합니다.

Shopify 커스텀 통합을 사용하려면 [Shopify 커스텀 통합 설정]({{site.baseurl}}/shopify_custom_integration)을 참조하세요.
{% endtab %}
{% endtabs %}

{% endif %}

{% if include.section == 'Custom external ID historical backfill' %}

커스텀 외부 ID로 통합할 계획인 경우([표준 통합]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration#step-4) 또는 [커스텀 통합]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration#step-6) 모두 해당), 기존의 모든 Shopify 고객 프로필에 커스텀 외부 ID를 Shopify 고객 메타필드로 추가한 후 과거 데이터 백필을 수행해야 합니다.

{% endif %}

{% if include.section == "Liquid promotion codes with Currents" %}

[`message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras)와 [프로모션 코드]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes)를 결합하여 Currents에 프로모션 코드 정보를 전송할 수 있습니다. `capture` 태그를 사용하여 프로모션 코드를 변수에 저장한 후, 해당 변수를 `message_extras`에서 참조하세요:

{% raw %}
```liquid
{% capture code %}
{% promotion('puttshacktest2') %}
{% endcapture %}
Use {{code}} for an exclusive discount!
{% message_extras :key cardscode :value {{code}} %}
```
{% endraw %}

{% endif %}