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

O envio de mensagens LINE pela Braze consumirá os créditos de mensagem ou de ação da sua conta.

## Etapa 1: Escolha onde criar sua mensagem {#step-1-choose-where-to-build-your-message}

Não tem certeza se sua mensagem deve ser enviada usando uma Campaign ou um Canvas? Campaigns são melhores para campanhas de mensagens únicas e direcionadas, enquanto Canvas é melhor para jornadas de usuário com várias etapas.

{% tabs %}
{% tab Campaign %}

**Etapas:**

1. Acesse **Envio de mensagens** > **Campaigns** e selecione **Criar Campaign**.
2. Selecione **LINE** ou, para Campaigns direcionadas a múltiplos canais, selecione **Multichannel Campaign**.
3. Dê à sua Campaign um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) conforme necessário.
   * Tags facilitam encontrar suas Campaigns e criar relatórios a partir delas.
5. Adicione e nomeie quantas variantes forem necessárias para sua Campaign. Você pode escolher diferentes plataformas, tipos de mensagem e disposições para cada uma das variantes adicionadas. Para saber mais sobre este tópico, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Se todas as mensagens da sua Campaign forem semelhantes ou tiverem o mesmo conteúdo, redija sua mensagem antes de adicionar variantes adicionais. Em seguida, escolha **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Etapas:**

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) usando o criador de Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa no construtor de Canvas. Dê à sua etapa um nome claro e significativo.
3. Escolha um [cronograma de etapa]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) e especifique uma postergação conforme necessário.
4. Filtre seu público para esta etapa conforme necessário. Você pode refinar ainda mais os destinatários desta etapa especificando segmentos e adicionando filtros adicionais. As opções de público serão verificadas após a postergação, no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento de avanço]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases).
6. Escolha quaisquer outros canais de envio de mensagens que você deseja combinar com sua mensagem.

{% endtab %}
{% endtabs %}

## Etapa 2: Redija sua mensagem LINE {#step-2-compose-your-line-message}

Escreva sua mensagem usando personalização (como Liquid ou Conteúdo conectado) conforme necessário. O LINE permite até cinco balões de mensagem em cada mensagem, que podem ser qualquer uma das disposições de mensagem disponíveis: texto, imagem, rich ou baseada em cartão.

![Criador LINE com uma mensagem exibida na prévia.]({% image_buster /assets/img/line/line_composer.png %})

### Dicas {#tips}

#### Usando Liquid {#using-liquid}

Se você planeja usar Liquid, certifique-se de incluir um valor padrão para sua personalização. Isso evitará que destinatários com perfis de usuário incompletos recebam um espaço reservado em branco. Por exemplo, em vez de um usuário receber a mensagem "Oi, !", ele pode receber a mensagem "Oi, novo inscrito!".

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Criando mensagens da direita para a esquerda {#creating-right-to-left-messages}

A aparência final das mensagens da direita para a esquerda depende em grande parte de como os prestadores de serviço as renderizam. Para práticas recomendadas sobre como criar mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

## Etapa 3: Pré-visualize e teste sua mensagem {#step-3-preview-and-test-your-message}

Alterne para a guia **Teste** para enviar uma mensagem LINE de teste para grupos de teste de conteúdo ou usuários individuais, ou pré-visualize a mensagem como um usuário diretamente na Braze.

![A guia "Teste" exibindo uma prévia de uma mensagem de teste.]({% image_buster /assets/img/line/test_preview.png %})

Para saber mais, consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=line).

## Etapa 4: Construa o restante da sua Campaign ou Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Construa o restante da sua Campaign. Consulte as seções a seguir para mais detalhes sobre como usar melhor nossas ferramentas para criar mensagens LINE.

### Escolha o cronograma de entrega ou gatilho {#choose-delivery-schedule-or-trigger}

As mensagens LINE podem ser entregues com base em um horário agendado, uma ação ou um gatilho de API. Para saber mais sobre opções de agendamento e gatilho, consulte [Agendando sua Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Você pode especificar controles de entrega, como permitir que os usuários se tornem [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) para receber a Campaign, ou ativar regras de [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping). Para entrega baseada em ação, você também pode definir a duração da Campaign e o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

### Escolha os usuários a serem direcionados {#choose-users-to-target}

[Direcione usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) escolhendo segmentos ou filtros para restringir seu público. Você já deve ter escolhido o grupo de inscrições, que restringe os usuários pelo nível ou categoria de comunicação que desejam ter com você.

Selecione o público maior dos seus segmentos e, opcionalmente, refine ainda mais esse segmento com nossos [filtros]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters). Você receberá automaticamente um resumo de como é a população aproximada desse segmento. Tenha em mente que a composição exata do segmento é sempre calculada antes do envio da mensagem.

### Escolha eventos de conversão {#choose-conversion-events}

A Braze permite que você acompanhe com que frequência os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), após receberem uma Campaign. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão será contabilizada se o usuário realizar a ação especificada.

Os eventos de conversão ajudam a medir o sucesso da sua Campaign. Por exemplo:

- Se você está usando geotargeting para disparar uma mensagem LINE com o objetivo final de o usuário realizar uma compra, defina o evento de conversão como `Purchase`.
- Se você está tentando direcionar o usuário para o seu app, defina o evento de conversão como `Starts Session`.

Você também pode definir eventos de conversão personalizados com base no seu caso de uso específico. Seja criativo e pense em como você deseja medir o sucesso desta Campaign.

{% endtab %}
{% tab Canvas %}

Se ainda não o fez, conclua as seções restantes do seu Canvas. Para mais detalhes sobre como construir o restante do seu Canvas, usar testes multivariantes e seleção inteligente, e mais, consulte [Criar um Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).

{% endtab %}
{% endtabs %}

## Etapa 5: Revise e implante {#step-5-review-and-deploy}

Depois de terminar de construir a última parte da sua Campaign ou Canvas, revise os detalhes, teste e envie!

Em seguida, confira os [relatórios LINE]({{site.baseurl}}/line/reporting) para saber como acessar os resultados das suas Campaigns LINE.