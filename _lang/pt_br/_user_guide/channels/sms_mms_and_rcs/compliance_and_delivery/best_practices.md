---
nav_title: "Melhores práticas"
article_title: Melhores práticas para SMS, MMS e RCS
page_order: 2
description: "Este artigo de referência aborda as melhores práticas para SMS/MMS."
alias: /sms_mms_rcs_best_practices/
page_type: reference
channel:
  - SMS
  - MMS
  - RCS

---

# Melhores práticas para SMS, MMS e RCS {#best-practices-for-sms-mms-and-rcs}

> Saiba mais sobre as melhores práticas para SMS, MMS e RCS com a Braze, incluindo nossas recomendações para monitoramento de descadastramento e bombeamento de tráfego.

## Recomendações de monitoramento de descadastramento {#opt-out-monitoring-recommendations}

Cumprir as solicitações dos destinatários para descadastramento de comunicações é exigido por lei. O não cumprimento das solicitações de descadastramento de destinatários de SMS pode acarretar penalidades, incluindo multas, e pode levar a processos judiciais. A Braze possui recursos para possibilitar um gerenciamento robusto de opt-in e descadastramento de SMS e MMS, além de mecanismos para ajudar a garantir que as solicitações sejam processadas corretamente.

De acordo com os contratos de assinatura firmados conosco, nossos clientes são os únicos responsáveis pelo cumprimento da legislação aplicável no uso de nossos serviços. Sendo assim, recomendamos fortemente que os clientes prestem muita atenção à configuração correta do SMS e que testem essas configurações minuciosamente, tomem medidas para monitorar a conformidade com o descadastramento e ajam prontamente caso identifiquem casos de não conformidade com solicitações de descadastramento.

Ao configurar SMS e MMS na Braze para gerenciar opt-ins e descadastramentos, consulte a seguinte lista de recursos:
* [Grupos de inscrições de SMS]({{site.baseurl}}/sms_rcs_subscription_groups): Grupos de inscrições e métodos e status de opt-in/descadastramento.
* [REST APIs de grupos de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups): Como processar opt-ins e descadastramentos recebidos de uma fonte diferente de uma resposta direta a uma mensagem.
* [Processamento de palavras-chave]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing): Explicações sobre como a Braze aborda o processamento e gerenciamento de palavras-chave.
* [Duplo opt-in de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in): Exige que os usuários confirmem explicitamente sua intenção de opt-in antes de receberem mensagens SMS. O duplo opt-in de SMS é um requisito em alguns países, por isso a Braze recomenda configurá-lo.
* [Envio de mensagens SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending): Fundamentos do envio de SMS na Braze, incluindo a importância dos grupos de inscrições, requisitos para segmentos de SMS e corpos de mensagem, e mais.

### Considerações {#considerations}

Quando SMS e MMS foram configurados em várias instâncias e, devido a uma configuração incorreta, os descadastramentos de uma Campaign ou Canvas são enviados para o espaço de trabalho errado.

* A Braze possui monitoramento para identificar essas situações. Se esse comportamento for detectado, a Braze redirecionará os descadastramentos para a instância correta e fará o preenchimento retroativo de quaisquer descadastramentos que ocorreram durante o período.
* Recomendamos fortemente que os clientes testem os descadastramentos para cada grupo de inscrições que possuem na Braze. Identificar esse problema antes de lançar uma mensagem é melhor do que mitigar após a identificação de um problema.

A Braze gerencia as inscrições de SMS/MMS tanto no nível do perfil de usuário (`user_id`) quanto no nível do número de telefone (`channel_id`). Quando um número de telefone é inscrito ou descadastrado, a atualização se aplica a todos os perfis que compartilham esse número. No caso em que um usuário final fez opt-in com um determinado número de telefone, mas depois muda de número, o novo número herdará o status do grupo de inscrições do usuário. Dessa forma, se um usuário final fez descadastramento, mas depois retorna ao app ou site com um novo número de telefone, ele não receberá mensagens indesejadas.

## Recomendações de higiene da lista de números de telefone {#phone-number-list-hygiene-recommendations}

Manter a higiene da lista de números de telefone ajuda a preservar dados válidos de consentimento e alcançabilidade ao longo do tempo. A Braze marca alguns números de telefone como inválidos para ajudar a reduzir riscos de conformidade, apoiar práticas de envio de mensagens baseadas em consentimento e evitar o envio para números que podem não pertencer mais ao usuário original.

Para saber por que números de telefone são normalmente marcados como inválidos, consulte [Tratamento de números de telefone inválidos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers).

Recomendamos o seguinte fluxo de trabalho para remover números de telefone inválidos:

1. Identifique os números de telefone afetados por meio do [endpoint `/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers).
2. Diferencie entre números de telefone desativados e números de telefone que receberam erros de provedor.
3. Para números de telefone desativados, verifique novamente o número com o usuário. Após o usuário confirmar seu número de telefone, remova o número da lista de inválidos por meio do [endpoint `/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers).

## Recomendações sobre bombeamento de tráfego {#traffic-pumping-recommendations}

### O que é bombeamento de tráfego? {#what-is-traffic-pumping}

O bombeamento de tráfego é uma forma de fraude que ocorre quando um agente mal-intencionado usa um formulário online para disparar o envio de mensagens SMS em alto volume (por exemplo, mensagens de opt-in ou senhas de uso único). O agente mal-intencionado configura um número de tarifa premium para o qual essas mensagens são enviadas e reivindica uma participação na receita da operadora móvel com a qual o número de tarifa premium foi configurado, gerando assim receita ilícita.

### Como identificar bombeamento de tráfego {#how-to-spot-traffic-pumping}

* Números de tarifa premium que suportam esse tipo de golpe são frequentemente, mas nem sempre, configurados em países fora das suas geografias normais de envio.
* Picos incomuns no envio de mensagens a partir de formulários online podem indicar bombeamento de tráfego.
    * Recomendamos configurar [alertas de Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/campaign_alerts) para limitar e notificar caso um número implausível de mensagens seja enviado.
* Formulários online incompletos podem indicar preenchimento programático de formulários.
* Ao criar formulários online, recomendamos definir regras para garantir que os formulários sejam totalmente preenchidos e usar ferramentas como CAPTCHA para minimizar o risco.

### Impacto do bombeamento de tráfego {#impact-of-traffic-pumping}

Os clientes são responsáveis por monitorar o tráfego que estão enviando e serão faturados por todos os SMS enviados por meio de sua conta. Entre a Braze e o cliente, o cliente é a parte em melhor posição para detectar e prevenir o bombeamento de tráfego.

## Envio de SMS para múltiplos países {#multi-country-sms-sending}

Algumas marcas podem desejar enviar mensagens para um grupo de usuários que possuem números de telefone de diferentes países. Para enviar uma mensagem SMS para um número de telefone em um determinado país, a melhor prática é usar um código longo ou código curto do mesmo país. Na verdade, códigos curtos só podem enviar SMS para números de telefone do mesmo país em que o código curto foi criado.

Para superar essa limitação, durante o [processo de configuração]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) dos grupos de inscrições, os grupos podem ser configurados para conter códigos longos e curtos de vários países diferentes. Quando concluído, os números de envio com o mesmo código de país do número de telefone do usuário-alvo serão usados automaticamente ao lançar uma Campaign. Você não precisará criar Campaigns separadas para usuários com números de telefone de diferentes códigos de país, permitindo que você lance uma Campaign ou use um componente do Canvas para direcionar os usuários relevantes.

![As cargas úteis de SMS são enviadas usando o mesmo código de país do número de telefone do usuário-alvo.]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

### Melhores práticas gerais de envio {#general-sending-best-practices}

1. **Obtenha permissão.** Uma das regras mais importantes para usar SMS como empresa é que você deve primeiro obter permissão dos clientes para contatá-los. Não fazer isso pode prejudicar sua marca e resultar em altas taxas legais.
2. **Escolha o número certo para o seu caso de uso.** Três tipos principais de números de telefone podem enviar e receber mensagens SMS: códigos longos, códigos curtos e IDs de remetente alfanuméricos, e suas capacidades e disponibilidade em diferentes regiões variam. Pense com antecedência se o seu negócio é melhor atendido com um código personalizado.
3. **Preste atenção ao timing.** Tenha em mente que os clientes são mais receptivos a materiais que são direcionados diretamente a eles. Um pouco de personalização faz muita diferença, como usar o nome do destinatário ou adicionar um toque conversacional que reflita os interesses dos seus clientes.
4. **Participe de conversas bidirecionais.** O SMS é um canal tão eficaz para engajar clientes que é importante antecipar e lidar efetivamente com as respostas às suas mensagens. 85% dos consumidores não apenas querem receber informações, mas também responder às empresas ou participar de uma conversa.
5. **Meça o que funciona.** Você está alcançando os clientes no momento certo, com a melhor frequência e usando as chamadas para ação mais eficazes? Usar as ferramentas de rastreamento certas pode oferecer métricas diretas e mensuráveis que comprovam o ROI.

## Envio em alto volume {#high-volume-sending}

Planeja fazer envios em alto volume? Temos algumas melhores práticas para garantir que tudo funcione sem problemas.

- Ajuste o limite de frequência de velocidade de entrega da sua Campaign ou Canvas conforme necessário, com base no tamanho do público-alvo. Isso garante que você alcance o volume de envio necessário e que a Braze envie as mensagens na taxa que a Twilio espera e pode processar.
- Certifique-se de respeitar o limite de 160 caracteres e esteja ciente de que caracteres especiais contam em dobro (por exemplo, barras invertidas `\`, acentos circunflexos `^` e tis `~`).

## Recomendações de horário de silêncio {#quiet-hours-recommendations}

{% alert warning %}
**O horário de silêncio nativo da Braze não garante horários de entrega no nível do dispositivo.** Quando uma mensagem é enviada, ela é repassada a uma operadora. Depois que a operadora aceita a mensagem, a Braze não tem mais controle sobre o momento exato em que ela é entregue ao dispositivo do usuário.<br><br> Por exemplo, se uma mensagem é repassada a uma operadora às 20h59, ela pode chegar ao dispositivo somente às 21h02. Para reduzir esse risco, recomendamos usar o método de horário de silêncio baseado em Liquid a seguir. Isso suprime a mensagem no nível do motor da Braze antes do repasse.
{% endalert %}

### Horário de silêncio nativo da Braze {#braze-native-quiet-hours}

Recomendamos fortemente ativar o [horário de silêncio]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#quiet-hours) em todas as Campaigns e Canvas de SMS para ajudar a cumprir regulamentações regionais e melhores práticas.

### Proteção adicional por meio de Content Blocks {#additional-safeguard-through-content-blocks}

Você pode adicionar uma verificação baseada em Liquid dentro de um Content Block. Isso oferece uma proteção confiável e escalável que funciona em conjunto com as configurações nativas.

#### Configuração {#setup}

Inclua o trecho a seguir no topo do corpo da sua mensagem SMS. Este exemplo cancela o envio se ele estiver fora de uma janela das 9h às 21h no [fuso horário local]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer) do usuário.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour >= 21 or hour < 9 %}
  {% abort_message("Outside allowed time window") %}
{% endif %}
```
{% endraw %}

#### Considerações

- {% raw %}`time_zone: ${time_zone}`{% endraw %} permite que a janela seja avaliada com base no horário local de cada usuário, e não em um horário global fixo, conforme explicado no [FAQ de Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer).
- Mensagens suprimidas por {% raw %}`abort_message()`{% endraw %} não são reagendadas para o dia seguinte; elas são canceladas.
- {% raw %} Por padrão, mensagens canceladas não são visíveis nos relatórios padrão de Campaign. No entanto, quando o Liquid cancela um envio com `{% abort_message %}`, a Braze registra isso no registro de atividades de mensagem como um erro de mensagem (por padrão, exibe `{% abort_message %}` chamado). Se você passar uma string, esse motivo é o que aparece no registro, como `{% abort_message('language was nil') %}`{% endraw %}. Para ter visibilidade dessas supressões no dashboard, entre em contato com seu gerente de sucesso do cliente para obter acesso ao [Dashboard de diagnóstico de envio de mensagens]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard).