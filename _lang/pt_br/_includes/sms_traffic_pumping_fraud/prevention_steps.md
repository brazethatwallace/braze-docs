### Quais etapas fundamentais imediatas minha empresa deve tomar para prevenir essa fraude? {#what-immediate-foundational-steps-should-my-company-take-to-prevent-this-fraud}

A etapa mais crítica que sua empresa pode tomar dentro da sua plataforma de engajamento com clientes é minimizar sua superfície de ataque usando limitações geográficas.

#### Utilize a lista de permissões geográficas da Braze {#utilize-the-braze-geographic-permissions-allowlist}

Você deve auditar proativamente as regiões onde seus clientes-alvo reais residem e configurar uma lista de permissões para permitir explicitamente o envio de mensagens apenas para esses países. Para as etapas de configuração, consulte [Permissões geográficas]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions/).

##### Bloqueie destinos de alto risco {#block-high-risk-destinations}

Se você opera apenas na América do Norte ou na Europa Ocidental, não há motivo para deixar as portas abertas para países internacionais de alto custo em outras regiões. Como regra geral, desative proativamente qualquer país onde você não faz marketing ativamente ou não tem operações, para eliminar exposição desnecessária.

{% if include.detail %}
Considere cuidadosamente qualquer solicitação para abrir rotas para países sinalizados como **Alto Risco de Fraude**.

##### Defesa em camadas {#layered-defense}

As restrições geográficas são uma primeira etapa crítica, mas representam apenas uma camada em uma estratégia mais ampla de defesa em profundidade. Nenhum controle isolado é suficiente — combinar múltiplas medidas torna o abuso significativamente mais complexo e difícil de executar em escala. Além da lista de permissões geográficas, os controles principais incluem proteções como:

- Validação no lado do cliente e no lado do servidor para garantir a integridade dos dados
- Limite de taxa sensato em endpoints vulneráveis para desacelerar envios automatizados
- Tokens CSRF para garantir que as solicitações se originem dos seus formulários legítimos
- CAPTCHA para impedir entradas fraudulentas em massa

{% alert note %}
Recomendamos colaborar com sua equipe interna de Segurança para adaptar essas sugestões à sua infraestrutura específica.
{% endalert %}
{% endif %}