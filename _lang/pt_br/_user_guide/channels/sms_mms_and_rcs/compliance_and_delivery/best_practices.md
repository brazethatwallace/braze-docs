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

Cumprir as solicitações de descadastramento de comunicações dos destinatários é exigido por lei. O não cumprimento das solicitações de descadastramento do canal por parte dos destinatários de SMS pode gerar penalidades, incluindo multas, e pode resultar em processos judiciais. A Braze possui recursos implementados para possibilitar uma gestão robusta de aceitação e descadastramento de SMS e MMS, além de mecanismos para ajudar a garantir que as solicitações sejam processadas corretamente.

De acordo com os contratos de assinatura firmados conosco, nossos clientes são os únicos responsáveis pelo cumprimento da legislação aplicável no uso dos nossos serviços. Dessa forma, recomendamos fortemente que os clientes prestem muita atenção à configuração correta do SMS e que testem essas configurações minuciosamente, adotem medidas para monitorar a conformidade com os descadastramentos e ajam prontamente caso identifiquem situações de não conformidade com solicitações de descadastramento.

Ao configurar SMS e MMS na Braze para gerenciar aceitações e descadastramentos, consulte a seguinte lista de recursos:
* [Grupos de inscrições de SMS]({{site.baseurl}}/sms_rcs_subscription_groups): Grupos de inscrições e métodos e status de aceitação/descadastramento.
* [REST APIs de grupos de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups): Como processar aceitações e descadastramentos recebidos de uma fonte diferente de uma resposta direta a uma mensagem.
* [Processamento de palavras-chave]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing): Explicações sobre como a Braze trata o processamento e o gerenciamento de palavras-chave.
* [Dupla aceitação de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in): Exige que os usuários confirmem explicitamente sua intenção de aceitação antes de receberem mensagens SMS. A dupla aceitação de SMS é um requisito em alguns países, por isso a Braze recomenda configurar esse recurso.
* [Envio de mensagens SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending): Fundamentos do envio de SMS na Braze, incluindo a importância dos grupos de inscrições, requisitos para segmentos de SMS e corpos de mensagem, entre outros.

### Considerações {#considerations}

Quando SMS e MMS são configurados em várias instâncias, uma configuração incorreta pode fazer com que descadastramentos de Campaign ou Canvas sejam enviados para o espaço de trabalho errado.

* A Braze possui monitoramento para identificar essas situações. Se esse comportamento for detectado, a Braze aplica os descadastramentos à instância correta e preenche retroativamente aqueles que ocorreram durante o período.
* Recomendamos fortemente que os clientes testem os descadastramentos para cada grupo de inscrições que possuem na Braze. Identificar esse problema antes de lançar uma mensagem é melhor do que mitigar após a identificação de um problema.

A Braze gerencia as inscrições de SMS/MMS tanto no nível do perfil de usuário (`user_id`) quanto no nível do número de telefone (`channel_id`). Quando um número de telefone é aceito ou descadastrado, a atualização se aplica a todos os perfis que compartilham esse número. No caso em que um usuário fez a aceitação com um determinado número de telefone, mas depois altera o número, o novo número herda o status do grupo de inscrições do usuário. Dessa forma, se um usuário se descadastrou e depois retorna ao app ou website com um novo número de telefone, ele não recebe mensagens indesejadas.

## Recomendações de higiene da lista de números de telefone {#phone-number-list-hygiene-recommendations}

Manter a higiene da lista de números de telefone ajuda você a preservar dados válidos de consentimento e acessibilidade ao longo do tempo. A Braze marca alguns números de telefone como inválidos para ajudar a reduzir riscos de conformidade, apoiar práticas de envio de mensagens baseadas em consentimento e evitar o envio para números que podem não pertencer mais ao usuário original.

Para saber os motivos pelos quais os números de telefone geralmente são marcados como inválidos, consulte [Tratamento de números de telefone inválidos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers).

Recomendamos o seguinte fluxo de trabalho para remover números de telefone inválidos:

1. Identifique os números de telefone impactados por meio do [endpoint `/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers).
2. Diferencie entre números de telefone desativados e números de telefone que receberam erros do provedor.
3. Para números de telefone desativados, verifique novamente o número com o usuário. Depois que o usuário confirmar seu número de telefone, remova o número da lista de inválidos por meio do [endpoint `/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers).

## Recomendações sobre traffic pumping {#traffic-pumping-recommendations}

### O que é traffic pumping? {#what-is-traffic-pumping}

Traffic pumping é uma forma de fraude que ocorre quando um agente mal-intencionado usa um formulário online para disparar o envio de mensagens SMS em alto volume (por exemplo, mensagens de aceitação ou senhas de uso único). O agente mal-intencionado configura um número de telefone de tarifa premium para receber essas mensagens e reivindica uma parcela da receita da operadora móvel com a qual o número de tarifa premium foi configurado, gerando assim receita ilícita.

### Como identificar traffic pumping {#how-to-spot-traffic-pumping}

* Os números de tarifa premium que sustentam esse tipo de golpe são frequentemente, mas nem sempre, configurados em países fora das suas geografias de envio habituais.
* Picos incomuns no envio de mensagens a partir de formulários online podem indicar traffic pumping.
    * Recomendamos configurar [alertas de campanha]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/campaign_alerts) para limitar e notificar caso um número implausivelmente alto de mensagens seja enviado.
* Formulários online incompletos podem indicar preenchimento programático de formulários.
* Ao criar formulários online, recomendamos definir regras para garantir que os formulários estejam totalmente preenchidos e usar ferramentas como CAPTCHA para minimizar o risco.

### Impacto do traffic pumping {#impact-of-traffic-pumping}

Os clientes são responsáveis por monitorar o tráfego que estão enviando e são faturados por todos os SMS enviados por meio de sua conta. Entre a Braze e o Cliente, o Cliente é a parte em melhor posição para detectar e prevenir traffic pumping.

## Envio de SMS para múltiplos países {#multi-country-sms-sending}

Algumas marcas podem desejar enviar mensagens para um grupo de usuários que possuem números de telefone de diferentes países. Para enviar uma mensagem SMS para um número de telefone em um determinado país, a melhor prática é usar um código longo ou código curto do mesmo país. Na verdade, códigos curtos só podem enviar SMS para números de telefone do mesmo país em que o código curto foi criado.

Para superar essa limitação, durante o [processo de configuração]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) dos grupos de inscrições, os grupos podem ser configurados para incluir códigos longos e curtos de múltiplos países diferentes. Após a configuração, os números de envio com o mesmo código de país do número de telefone do usuário-alvo serão usados automaticamente ao lançar uma Campaign. Você não precisará criar Campaigns separadas para usuários com números de telefone com códigos de país diferentes, o que permite lançar uma Campaign ou usar um componente de Canvas para alcançar os usuários relevantes.

![As cargas úteis de SMS são enviadas usando o mesmo código de país do número de telefone do usuário-alvo.]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

### Melhores práticas gerais de envio {#general-sending-best-practices}

1. **Obtenha permissão.** Uma das regras mais importantes para usar SMS como empresa é que você deve primeiro obter a permissão dos clientes para contatá-los. Não fazer isso pode prejudicar sua marca e resultar em multas legais pesadas.
2. **Escolha o número certo para seu caso de uso.** Três tipos principais de números de telefone podem enviar e receber mensagens SMS: códigos longos, códigos curtos e IDs de remetente alfanuméricos, e suas capacidades e disponibilidade em diferentes regiões variam. Pense antecipadamente se sua empresa seria melhor atendida com um código personalizado.
3. **Preste atenção ao timing.** Lembre-se de que os clientes são mais receptivos a materiais direcionados diretamente a eles. Um pouco de personalização faz muita diferença, como usar o nome do destinatário ou adicionar um toque conversacional que reflita os interesses dos seus clientes.
4. **Participe de conversas bidirecionais.** O SMS é um canal tão eficaz para engajar clientes que é importante antecipar e lidar de forma eficiente com as respostas às suas mensagens. 85% dos consumidores não apenas querem receber informações, mas também responder às empresas ou participar de uma conversa.
5. **Meça o que funciona.** Você está alcançando os clientes no momento certo, com a melhor frequência e usando as chamadas para ação mais eficazes? Usar as ferramentas de rastreamento certas pode oferecer métricas diretas e mensuráveis que comprovam seu ROI.

## Envio em grande volume {#high-volume-sending}

Planejando enviar mensagens em grande volume? Temos algumas melhores práticas para garantir que tudo funcione sem problemas.

- Ajuste o limite de frequência da velocidade de entrega da sua Campaign ou Canvas conforme necessário, com base no tamanho do público-alvo. Isso garante que você atinja o volume de envio necessário e que a Braze envie as mensagens na taxa que a Twilio espera e consegue processar.
- Respeite o limite de 160 caracteres e fique atento aos caracteres especiais que contam em dobro (por exemplo, barras invertidas `\`, acentos circunflexos `^` e tis `~`).

## Recomendações de horário de silêncio {#quiet-hours-recommendations}

{% alert warning %}
**O horário de silêncio nativo da Braze não garante horários de entrega no nível do dispositivo.** Quando uma mensagem é enviada, ela é entregue a uma operadora. Após a operadora aceitar a mensagem, a Braze não tem mais controle sobre o momento exato em que ela é entregue ao dispositivo do usuário.<br><br> Por exemplo, se uma mensagem é entregue a uma operadora às 20h59, ela pode não chegar ao dispositivo até as 21h02. Para reduzir riscos, recomendamos usar o método de horário de silêncio baseado em Liquid a seguir. Isso suprime a mensagem no nível do motor da Braze antes do envio à operadora.
{% endalert %}

### Horário de silêncio nativo da Braze {#braze-native-quiet-hours}

Recomendamos fortemente ativar o [horário de silêncio]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#quiet-hours) em todas as Campaigns e Canvas de SMS para ajudar a atender às regulamentações regionais e melhores práticas.

### Proteção adicional por meio de Content Blocks {#additional-safeguard-through-content-blocks}

Você pode adicionar uma verificação baseada em Liquid dentro de um Content Block. Isso oferece uma proteção confiável e escalável que funciona junto com as configurações nativas.

#### Configuração {#setup}

Inclua o snippet a seguir no topo do corpo da sua mensagem SMS. Este exemplo interrompe o envio se ele estiver fora de uma janela de 9h às 21h no [fuso local]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer) do usuário.

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

- {% raw %}`time_zone: ${time_zone}`{% endraw %} permite que a janela seja avaliada de acordo com o fuso local de cada usuário, e não em um horário global fixo, conforme explicado nas [Perguntas frequentes sobre Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer).
- Mensagens suprimidas por {% raw %}`abort_message()`{% endraw %} não são reagendadas para o dia seguinte; elas são canceladas.
- {% raw %} Por padrão, mensagens interrompidas não ficam visíveis nos relatórios padrão de Campaigns. No entanto, quando o Liquid interrompe um envio com `{% abort_message %}`, a Braze registra isso no Registro de Atividade de Mensagens como um erro de mensagem (por padrão, aparece `{% abort_message %}` chamado). Se você passar uma string, esse motivo é o que aparece no registro, como `{% abort_message('language was nil') %}`{% endraw %}. Para ter visibilidade dessas supressões no dashboard, entre em contato com seu gerente de sucesso do cliente para obter acesso ao [Dashboard de Diagnóstico de Mensagens]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard).