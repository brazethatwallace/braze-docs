---
nav_title: "Configuração do RCS"
article_title: "Configuração do RCS"
page_order: 1
alias: /rcs_setup/
description: "Este artigo de referência aborda os requisitos necessários para colocar o RCS em funcionamento."
page_type: reference
channel:
  - RCS
---

# Configurar o RCS {#set-up-rcs}

> Este artigo aborda os requisitos necessários para colocar seu canal RCS em funcionamento.

Configurar o RCS é tão simples quanto configurar o SMS. Continue lendo para saber como você pode começar a enviar mensagens ricas e interativas.

## Etapa 1: Atender aos critérios de elegibilidade {#step-1-meet-the-eligibility-criteria}

Para ser elegível para enviar RCS com a Braze, sua empresa deve atender a três critérios iniciais:

1. Seu contrato atual com a Braze deve incluir créditos de mensagem ou de ação.
2. Você deve enviar suas mensagens RCS para um dos seguintes países suportados pela Braze:
- Estados Unidos
- Reino Unido
- Alemanha
- México
- Suécia
- Espanha
- Singapura
- Brasil
- França
- Itália
- Colômbia
3. Você deve adquirir SKU(s) de RCS em seu contrato.

## Etapa 2: Registrar um remetente verificado por RCS {#step-2-register-an-rcs-verified-sender}

Antes de enviar mensagens RCS, você precisa registrar um remetente verificado por RCS. Essa é a representação da sua marca que os usuários veem em seus dispositivos móveis, incluindo o nome da marca, o logotipo, um selo de verificação e uma tagline opcional. O remetente verificado por RCS reforça a confiança do cliente e confirma que suas mensagens vêm de uma fonte autenticada.

![Um exemplo de remetente verificado por RCS em uma mensagem RCS chamada "Cat Failz Cafe".]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

Depois que você adicionar o(s) SKU(s) de RCS ao seu formulário de pedido, a Braze é notificada e entra em contato com as informações de registro do remetente RCS. O formato dessas informações depende dos países para os quais você deseja enviar mensagens RCS.

Quando você enviar os formulários preenchidos para a Braze, a Braze conclui o processo de registro em seu nome.

### Etapa 2.1: Configurar fallbacks de SMS para grupos de inscrições RCS {#step-21-set-up-sms-fallbacks-for-rcs-subscription-groups}

Como a cobertura atual das operadoras varia por país, e o suporte de hardware e software dos usuários varia individualmente, o fallback de SMS é um componente essencial para ter um programa de RCS bem-sucedido hoje. Recomendamos configurar o fallback de SMS. Se uma operadora não suportar RCS ou o dispositivo de um usuário não conseguir receber mensagens RCS, o fallback de SMS envia sua mensagem de qualquer forma, para que você nunca perca um momento importante com seus usuários.

Recomendamos fortemente que você revise sua experiência atual de aceitação de SMS, grupos de inscrições e segmentação de público antes de implantar sua primeira Campaign de RCS. Se necessário, seu gerente de sucesso do cliente está sempre disponível para fornecer orientação e ajudar você a navegar pelo processo de configuração.

#### Como o fallback de SMS funciona com eventos e segmentação {#how-sms-fallback-works-with-events-and-segmentation}

{% tabs %}
{% tab Comportamento de eventos %}

Quando você usa o fallback de SMS com RCS, o comportamento do evento depende de a mensagem ser enviada com sucesso por RCS ou cair para o fallback de SMS:

- **Se o envio de RCS for bem-sucedido:** Você recebe um evento de envio de RCS e um evento de entrega de RCS.
- **Se o envio de RCS cair para o fallback de SMS:** Você recebe um evento de envio de RCS, um evento de rejeição de RCS e um evento de entrega de SMS. O evento de entrega de SMS tem `IS_SMS_FALLBACK=TRUE`.

{% endtab %}
{% tab Comportamento de segmentação %}

Para SMS e RCS, os [filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) de mensagens recebidas (como [Recebeu mensagem de Campaign]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-campaign) e [Recebeu mensagem de etapa do Canvas]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-canvas-step)) avaliam quando uma mensagem é enviada, não quando ela chega ao dispositivo do usuário. Com o fallback de SMS ativado, os usuários ainda podem corresponder a esses filtros se uma mensagem RCS for rejeitada e cair para o fallback de SMS, ou se o SMS de fallback não for entregue ao dispositivo do usuário.

{% endtab %}
{% endtabs %}

### Prazo para aprovação da operadora {#timeline-for-carrier-approval}

O prazo para aprovação da operadora varia por país e também pode variar dentro de um mesmo país. Tenha em mente que o mercado de RCS ainda está em fase inicial, então os processos das operadoras e agregadores estão evoluindo rapidamente. Nos Estados Unidos, a Braze estima que o tempo de resposta para aprovação de um remetente verificado por RCS pela operadora geralmente fica na faixa de 4 a 6 semanas, com um remetente de teste normalmente aprovado em uma semana.

Quando seu remetente verificado por RCS for aprovado, nossa equipe de operações atualiza seus grupos de inscrições conforme necessário para confirmar que eles incluem o remetente RCS.

## Etapa 3: Configurar grupos de inscrições {#step-3-set-up-subscription-groups}

Dependendo da sua integração, a Braze pode adicionar remetentes verificados de RCS aos seus grupos de inscrições de SMS existentes ou configurar novos. Para instruções detalhadas de configuração, consulte [Grupos de inscrições de SMS e RCS]({{site.baseurl}}/sms_rcs_subscription_groups).

## Migrando tráfego de SMS para RCS {#migrating-sms-traffic-to-rcs}

Se você tem grupos de inscrições separados para SMS e RCS, pode migrar usuários de SMS para RCS usando um Canvas de uma única etapa. Para instruções passo a passo, consulte [Migrar tráfego de SMS para RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#migrate-sms-traffic-to-rcs).