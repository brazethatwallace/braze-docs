### 이 사기를 방지하기 위해 회사에서 즉시 취해야 할 기본 조치는 무엇인가요? {#what-immediate-foundational-steps-should-my-company-take-to-prevent-this-fraud}

회사가 고객 참여 플랫폼 내에서 취할 수 있는 가장 중요한 조치는 지리적 제한을 사용하여 공격 표면을 최소화하는 것입니다.

#### Braze 지리적 권한 허용 목록 활용 {#utilize-the-braze-geographic-permissions-allowlist}

실제 타겟 고객이 거주하는 지역을 사전에 점검하고, 해당 국가에만 메시징을 명시적으로 허용하는 허용 목록을 구성해야 합니다. 설정 단계는 [지리적 권한]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions/)을 참조하세요.

##### 고위험 대상 차단 {#block-high-risk-destinations}

북미 또는 서유럽에서만 비즈니스를 운영하는 경우, 다른 지역의 고비용 국제 국가에 대한 경로를 열어둘 이유가 없습니다. 일반적으로, 적극적으로 마케팅하거나 운영하지 않는 국가는 사전에 비활성화하여 불필요한 노출을 제거하세요.

{% if include.detail %}
**사기 위험이 높은** 것으로 표시된 국가에 대한 경로 개방 요청은 신중하게 검토하세요.

##### 다층 방어 {#layered-defense}

지리적 제한은 중요한 첫 번째 단계이지만, 보다 광범위한 심층 방어 전략의 한 계층에 불과합니다. 단일 제어만으로는 충분하지 않으며, 여러 조치를 결합하면 악용이 훨씬 더 복잡해지고 대규모로 실행하기 어려워집니다. 지리적 허용 목록 외에도 주요 제어에는 다음과 같은 보호 조치가 포함됩니다.

- 데이터 무결성을 보장하기 위한 클라이언트 측 및 서버 측 유효성 검사
- 자동화된 제출을 늦추기 위한 취약한 엔드포인트에 대한 합리적인 사용량 제한
- 요청이 합법적인 양식에서 발생하는지 확인하기 위한 CSRF 토큰
- 대량의 사기성 항목을 방지하기 위한 CAPTCHA

{% alert note %}
이러한 제안을 특정 인프라에 맞게 조정하려면 내부 보안 팀과 협력하는 것을 권장합니다.
{% endalert %}
{% endif %}