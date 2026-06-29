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
3. Você deve adquirir um ou mais SKUs de RCS no seu contrato.

## Etapa 2: Registrar um remetente verificado de RCS {#step-2-register-an-rcs-verified-sender}

Antes de enviar mensagens RCS, você deve registrar um remetente verificado de RCS. Essa é a representação da sua marca que os usuários verão em seus dispositivos móveis, incluindo o nome da marca, logotipo, um selo de verificação e uma tagline opcional. O remetente verificado de RCS reforça a confiança do cliente e confirma que suas mensagens vêm de uma fonte autenticada.

![Um exemplo de remetente verificado de RCS em uma mensagem RCS chamado "Cat Failz Cafe".]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

Depois de adicionar o(s) SKU(s) de RCS ao seu formulário de pedido, a Braze será notificada e entrará em contato com você com as informações de registro do remetente RCS. O formato dessas informações dependerá dos países para os quais você deseja enviar mensagens RCS.

Quando você enviar seus formulários preenchidos para a Braze, nós concluiremos o processo de registro em seu nome.

### Etapa 2.1: Configurar fallbacks de SMS para grupos de inscrições de RCS {#step-21-set-up-sms-fallbacks-for-rcs-subscription-groups}

Como a cobertura atual das operadoras varia por país, e o suporte de hardware e software dos usuários varia individualmente, o fallback de SMS é um componente essencial para ter um programa de RCS bem-sucedido hoje. Recomendamos configurar o fallback de SMS. Se uma operadora não suportar RCS ou o dispositivo de um usuário não conseguir receber mensagens RCS, o fallback de SMS enviará sua mensagem de qualquer forma, para que você nunca perca um momento importante com seus usuários.

Recomendamos fortemente que você revise sua experiência atual de opt-in de SMS, grupos de inscrições e segmentação de público antes de implantar sua primeira Campaign de RCS. Se necessário, seu gerente de sucesso do cliente está sempre disponível para fornecer orientação e ajudá-lo a navegar pelo processo de configuração.

#### Como o fallback de SMS funciona com eventos e segmentação {#how-sms-fallback-works-with-events-and-segmentation}

{% tabs %}
{% tab Comportamento de eventos %}

Quando você usa o fallback de SMS com RCS, o comportamento dos eventos depende de a mensagem ter sido enviada com sucesso via RCS ou ter recorrido ao fallback de SMS:

- **Se o envio de RCS for bem-sucedido:** Você recebe um evento de envio de RCS e um evento de entrega de RCS.
- **Se o envio de RCS recorrer ao fallback de SMS:** Você recebe um evento de envio de RCS, um evento de rejeição de RCS e um evento de entrega de SMS. O evento de entrega de SMS tem `IS_SMS_FALLBACK=TRUE`.

{% endtab %}
{% tab Comportamento de segmentação %}

Para SMS e RCS, os [filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/) de mensagens recebidas (como [Recebeu mensagem de Campaign]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#received-message-from-campaign) e [Recebeu mensagem de etapa do Canvas]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#received-message-from-canvas-step)) são avaliados quando uma mensagem é enviada, não quando ela chega ao dispositivo do usuário. Com o fallback de SMS ativado, os usuários ainda podem corresponder a esses filtros se uma mensagem RCS for rejeitada e recorrer ao fallback de SMS, ou se o SMS de fallback não for entregue ao dispositivo do usuário.

{% endtab %}
{% endtabs %}

### Prazo para aprovação da operadora {#timeline-for-carrier-approval}

O prazo para aprovação da operadora varia por país e também pode variar dentro de um mesmo país. Tenha em mente que o mercado de RCS ainda está em seus estágios iniciais, então os processos das operadoras e agregadores estão evoluindo rapidamente. Nos Estados Unidos, a Braze estima que o tempo de resposta para aprovação de um remetente verificado de RCS pela operadora normalmente fica na faixa de 4 a 6 semanas, com um remetente de teste geralmente aprovado em uma semana.

Quando seu remetente verificado de RCS for aprovado, nossa equipe de operações atualizará seus grupos de inscrições conforme necessário para confirmar que eles incluem o remetente RCS.

## Etapa 3: Configurar grupos de inscrições {#step-3-set-up-subscription-groups}

Dependendo da sua integração, a Braze pode adicionar remetentes verificados de RCS aos seus grupos de inscrições de SMS existentes ou configurar novos. Para instruções detalhadas de configuração, consulte [Grupos de inscrições de SMS e RCS]({{site.baseurl}}/sms_rcs_subscription_groups/).

## Migrar tráfego de SMS para RCS {#migrating-sms-traffic-to-rcs}

Se você tem grupos de inscrições de SMS e RCS separados, pode migrar usuários de SMS para RCS usando um Canvas de uma única etapa.

A Braze recomenda que você teste o envio de RCS para volumes menores de usuários inicialmente e migre mais usuários para o grupo de inscrições de RCS ao longo do tempo. Por exemplo, se você tem 1.000.000 de usuários inscritos em um grupo de inscrições de SMS, isso poderia significar primeiro migrar todos os usuários para o novo grupo de inscrições e depois segmentar um público menor de 50.000 a 100.000 (5-10%) para testar as mensagens RCS.

### Etapa 1: Criar um Canvas e preencher o cronograma de entrada {#step-1-create-a-canvas-and-fill-out-the-entry-schedule}

Crie um Canvas e dê a ele um nome facilmente identificável (como "Transferência de usuários do grupo de inscrições SMS-RCS"). Em seguida, programe o Canvas no momento mais conveniente para você.

### Etapa 2: Definir seu público {#step-2-define-your-audience}

Defina seu público usando um dos métodos a seguir. Em seguida, vá para a etapa **Configurações de envio** e selecione **Usuários inscritos ou com opt-in**.

| Método | Descrição |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Criar um segmento** | Crie um segmento que inclua todos os usuários em um grupo de inscrições ou um subconjunto usando filtros de segmentação (como 5-10% aleatórios). Os segmentos são atualizados antes de cada envio para refletir sua base de usuários atual. |
| **Aplicar filtros de Campaign ou Canvas** | Refine o público na etapa **Público-alvo** da sua Campaign ou Canvas. Ajuste as opções de direcionamento sem sair da página para maior flexibilidade. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Definir seu público" }

### Etapa 3: Configurar uma etapa de Atualização de Usuário {#step-3-configure-a-user-update-step}

Adicione uma etapa de Atualização de Usuário ao seu Canvas. Na etapa, abra o **Editor JSON avançado** e insira o seguinte (para o campo de identificador único do usuário, recomendamos usar o campo `braze_id`):

{% raw %}
```json
{
  "attributes": [
    {
      "braze_id": "{{${braze_id}}}",
      "subscription_groups": [
        {
          "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}
```
{% endraw %}

![Objeto de Atualização de Usuário que contém o código JSON mencionado anteriormente.]({% image_buster /assets/img/sms/user_update_object.png %})

### Etapa 4: Testar o Canvas {#step-4-test-the-canvas}

Recomendamos fortemente [testar seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases/) para confirmar que ele funciona conforme esperado antes de enviá-lo para seu público mais amplo.

### Etapa 5: Lançar seu Canvas {#step-5-launch-your-canvas}

Depois de testar seu Canvas com sucesso, vá em frente e lance-o para seu subconjunto de usuários!

Para confirmar que seus usuários foram migrados com sucesso, recomendamos verificar alguns perfis de usuários individuais que foram atualizados. Na guia **Engajamento**, procure por **Configurações de contato** e role para visualizar os grupos de inscrições nos quais o usuário está inscrito. O toggle do grupo de inscrições de RCS agora deve estar ativado.