---
nav_title: Criar uma mensagem LINE
article_title: Criar uma mensagem LINE
page_order: 1
description: "Este artigo aborda como criar uma Campaign ou Canvas de mensagem LINE."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/
---

# Criar uma mensagem LINE {#create-a-line-message}

> As Campaigns LINE podem alcançar diretamente e conversar de forma programática com seus clientes. Você pode usar Liquid e outros conteúdos dinâmicos para criar uma experiência pessoal com seus usuários e criar um ambiente que promova e aprimore uma experiência de usuário discreta com sua marca.

## Pré-requisitos {#prerequisites}

Antes de criar uma mensagem LINE, faça o seguinte:

1. Leia a visão geral do LINE.
2. Reconheça as políticas, limites e regras de conteúdo.
3. [Configure sua conexão LINE]({{site.baseurl}}/user_guide/channels/line/line_setup).

O envio de mensagens LINE pela Braze consumirá os Créditos de Mensagem ou de Ação da sua conta.

## Etapa 1: Escolha onde criar sua mensagem {#step-1-choose-where-to-build-your-message}

Não tem certeza se sua mensagem deve ser enviada usando uma Campaign ou um Canvas? Campaigns são melhores para campanhas de mensagens únicas e direcionadas, enquanto Canvas é melhor para jornadas de usuário com várias etapas.

{% tabs %}
{% tab Campaign %}

**Etapas:**

1. Acesse **Messaging** > **Campaigns** e selecione **Create Campaign**.
2. Selecione **LINE** ou, para campanhas direcionadas a vários canais, selecione **Multichannel Campaign**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) conforme necessário.
   * Tags facilitam a busca e a criação de relatórios das suas campanhas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagem e layouts para cada uma das variantes adicionadas. Para saber mais sobre esse tópico, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Se todas as mensagens da sua campanha forem semelhantes ou tiverem o mesmo conteúdo, redija sua mensagem antes de adicionar variantes adicionais. Em seguida, você pode escolher **Copy from Variant** no menu suspenso **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Etapas:**

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

## Etapa 2: Componha sua mensagem LINE {#step-2-compose-your-line-message}

Escreva sua mensagem usando personalização (como Liquid ou Connected Content) conforme necessário. O LINE permite até cinco balões de mensagem em cada mensagem, que podem ser qualquer um dos layouts de mensagem disponíveis: texto, imagem, rica ou baseada em cartão.

![Criador do LINE com uma mensagem exibida na prévia.]({% image_buster /assets/img/line/line_composer.png %})

### Dicas {#tips}

#### Usando Liquid {#using-liquid}

Se você planeja usar Liquid, inclua um valor padrão para sua personalização. Isso evitará que destinatários com perfis de usuário incompletos recebam um espaço reservado em branco. Por exemplo, em vez de um usuário receber a mensagem "Oi, !", ele pode receber a mensagem "Oi, novo inscrito!".

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Criando mensagens da direita para a esquerda {#creating-right-to-left-messages}

A aparência final das mensagens da direita para a esquerda depende em grande parte de como os prestadores de serviço as renderizam. Para práticas recomendadas sobre como criar mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

## Etapa 3: Prévia e teste da sua mensagem {#step-3-preview-and-test-your-message}

Alterne para a guia **Teste** para enviar uma mensagem LINE de teste para grupos de teste de conteúdo ou usuários individuais, ou visualize a prévia da mensagem como um usuário diretamente na Braze.

![A guia "Testes" exibindo uma prévia de uma mensagem de teste.]({% image_buster /assets/img/line/test_preview.png %})

Para saber mais, consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=line).

## Etapa 4: Construa o restante da sua campanha ou Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Construa o restante da sua campanha. Consulte as seções a seguir para mais detalhes sobre como usar nossas ferramentas da melhor forma para criar mensagens LINE.

### Escolha o cronograma de entrega ou o disparo {#choose-delivery-schedule-or-trigger}

As mensagens LINE podem ser entregues com base em um horário agendado, uma ação ou um disparo de API. Para saber mais sobre opções de agendamento e disparo, consulte [Agendando sua campanha]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Você pode especificar controles de entrega, como permitir que os usuários se tornem [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) para receber a campanha, ou ativar regras de [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping). Para entrega baseada em ação, você também pode definir a duração da campanha e o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

### Escolha os usuários a serem direcionados {#choose-users-to-target}

[Direcione usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) escolhendo segmentos ou filtros para refinar seu público. Você já deve ter escolhido o grupo de inscrições, que filtra os usuários pelo nível ou categoria de comunicação que desejam ter com você.

Selecione o público mais amplo dos seus segmentos e, opcionalmente, refine ainda mais esse segmento com nossos [filtros]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters). Você recebe automaticamente um resumo de como é a população aproximada desse segmento. Lembre-se de que a composição exata do segmento é sempre calculada antes do envio da mensagem.

### Escolha os eventos de conversão {#choose-conversion-events}

A Braze permite que você rastreie com que frequência os usuários realizam ações específicas, chamadas [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), após receberem uma campanha. Você tem a opção de permitir uma janela de até 30 dias durante a qual uma conversão será contabilizada se o usuário realizar a ação especificada.

Os eventos de conversão ajudam a medir o sucesso da sua campanha. Por exemplo:

- Se você está usando geolocalização para disparar uma mensagem LINE com o objetivo final de o usuário realizar uma compra, defina o evento de conversão como `Purchase`.
- Se você está tentando levar o usuário ao seu app, defina o evento de conversão como `Starts Session`.

Você também pode definir eventos de conversão personalizados com base no seu caso de uso específico. Seja criativo e pense em como deseja medir o sucesso desta campanha.

{% endtab %}
{% tab Canvas %}

Se ainda não o fez, conclua as seções restantes do seu Canvas. Para saber mais sobre como construir o restante do seu Canvas, usar testes multivariantes e seleção inteligente, e muito mais, consulte [Criar um Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).

{% endtab %}
{% endtabs %}

## Etapa 5: Revisar e implantar {#step-5-review-and-deploy}

Depois de terminar de criar sua Campaign ou Canvas, revise os detalhes, teste e envie!

Em seguida, confira [Relatórios do LINE]({{site.baseurl}}/line/reporting) para saber como acessar os resultados das suas Campaigns do LINE.