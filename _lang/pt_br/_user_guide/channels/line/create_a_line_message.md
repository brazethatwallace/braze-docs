---
nav_title: Criar uma mensagem LINE
article_title: Criar uma mensagem LINE
page_order: 1
description: "Crie uma mensagem LINE e configure tipos de mensagem, campos, rastreamento de cliques, configurações de entrega e comportamento específicos do canal."
page_type: reference
tool:
  - Campaigns
  - Canvas
channel:
  - LINE
alias: /line/create/
---

# Criar uma mensagem LINE {#create-a-line-message}

> Crie mensagens LINE personalizadas em Campaigns ou Canvas. Escolha entre mensagens de texto, imagem, rica e baseada em cartão, e combine até cinco mensagens em um único envio.

## Pré-requisitos {#prerequisites}

Antes de começar, confirme que você tem o seguinte:

| Requisito | Descrição |
| --- | --- |
| Conexão LINE | Conclua a [configuração do LINE]({{site.baseurl}}/user_guide/channels/line/line_setup) e revise as políticas, limites e regras de conteúdo do canal. |
| Campaign ou Canvas | Use uma Campaign para uma única mensagem direcionada ou Canvas para uma jornada de usuário com várias etapas. |
| Plano de mensagem | Prepare seu conteúdo, imagens, links e grupo de inscrições. |
| Créditos de mensagem ou ação | Confirme que sua conta tem créditos disponíveis. O envio de mensagens LINE a partir da Braze utiliza esses créditos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos de mensagem LINE" }

## Criar uma mensagem {#create-a-message}

### Etapa 1: Escolha onde criar sua mensagem {#step-1-choose-where-to-build-your-message}

{% tabs %}
{% tab Campaign %}

1. Acesse **Envio de mensagens** > **Campaigns** e selecione **Criar Campaign**.
2. Selecione **LINE** ou, para campanhas direcionadas a vários canais, selecione **Campanha multicanal**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [Equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) conforme necessário.
   * Tags facilitam a busca e o uso das suas campanhas em relatórios.
5. Adicione e nomeie as variantes da sua campanha. Cada variante pode usar tipos de mensagem e layouts diferentes. Para saber mais, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Se as variantes da sua campanha tiverem conteúdo semelhante, redija a primeira mensagem antes de adicionar mais variantes. Depois, selecione **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

### Etapa 2: Selecione um grupo de inscrições {#step-2-select-a-subscription-group}

Selecione o **Grupo de inscrições** associado ao canal LINE que envia a mensagem. É necessário informar um grupo de inscrições antes de iniciar o editor.

Todas as variantes em uma campanha LINE devem usar o mesmo grupo de inscrições. Para saber mais sobre os estados de inscrição do LINE, consulte [Grupos de inscrições do LINE]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups).

### Etapa 3: Redija sua mensagem LINE {#step-3-compose-your-line-message}

Selecione **Iniciar editor** e arraste tipos de mensagem para o editor. Combine até cinco mensagens em um único envio e organize-as na ordem em que os usuários as receberão.

![Criador do LINE com uma mensagem exibida na prévia.]({% image_buster /assets/img/line/line_composer.png %})

#### Tipos de mensagem {#message-types}

| Tipo de mensagem | Campos e configurações | Limites e comportamento |
| --- | --- | --- |
| **Texto** | Corpo da mensagem com emojis, Liquid e URLs | Até 5.000 caracteres. |
| **Imagem** | Imagem da biblioteca de mídia ou de uma URL, incluindo URL dinâmica | URLs de imagem podem conter até 2.000 caracteres. Mensagens de imagem independentes não suportam ações ao clicar. |
| **Mensagem rica** | Imagem, texto alternativo, modelo e áreas clicáveis com ações de URI | O texto alternativo pode conter até 400 caracteres. Adicione entre uma e 50 áreas clicáveis. Os rótulos de ação podem conter até 100 caracteres, e cada URI pode conter até 1.000 caracteres. |
| **Mensagem baseada em cartão** | Até 10 cartões com imagem e cabeçalho opcionais, corpo obrigatório e ações de URI | O texto alternativo pode conter até 400 caracteres. Um cabeçalho pode conter até 40 caracteres. Um corpo pode conter até 60 caracteres com imagem ou cabeçalho, ou 120 caracteres sem nenhum dos dois. Cada cartão requer entre uma e três ações com rótulos de até 20 caracteres. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipos de mensagem LINE, campos e limites" }

Os limites de caracteres excluem a sintaxe Liquid.

Para especificações de imagem, modelos de mensagem rica, configurações de imagem de carrossel e exemplos, consulte [Tipos de mensagem LINE]({{site.baseurl}}/user_guide/channels/line/create_a_line_message/message_types).

{% alert note %}
Mensagens baseadas em cartão aplicam os mesmos campos opcionais e número de ações a todos os cartões. Por exemplo, se um cartão incluir uma imagem e duas ações, todos os cartões devem incluir uma imagem e duas ações.
{% endalert %}

#### Comportamento ao clicar {#on-click-behavior}

Para áreas clicáveis em mensagens ricas e cartões, selecione **URI** para **Comportamento ao clicar** e insira o destino em **Abrir URL**. Escolha se a URL deve abrir dentro do LINE.

#### Personalização {#personalization}

Use [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) ou [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) para personalizar textos, imagens e URLs. Inclua um valor padrão para a personalização com Liquid para que perfis com dados incompletos não recebam conteúdo em branco.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Para idiomas escritos da direita para a esquerda, consulte [Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### Etapa 4: Configure o rastreamento de cliques {#step-4-configure-click-tracking}

Na guia **Configurações**, use **Rastreamento de cliques** para encurtar e rastrear links no momento do envio. O rastreamento de cliques está ativado por padrão para novas mensagens e se aplica a URLs HTTP e HTTPS em mensagens de texto, ricas e baseadas em cartão.

A Braze usa `https://brz.ai` ou o domínio personalizado configurado para o grupo de inscrições. Você pode personalizar URLs rastreadas com Liquid. Para configuração por tipo de mensagem, comportamento de teste, domínios personalizados e redirecionamento, consulte [Rastreamento de cliques do LINE]({{site.baseurl}}/user_guide/channels/line/create_a_line_message/line_click_tracking).

### Etapa 5: Visualize e teste sua mensagem {#step-5-preview-and-test-your-message}

Acesse a guia **Prévia e teste** para visualizar a mensagem como um usuário ou enviar uma mensagem LINE de teste para um grupo de teste de conteúdo ou um usuário individual.

![A guia Prévia e teste exibindo uma prévia de uma mensagem de teste.]({% image_buster /assets/img/line/test_preview.png %})

Para requisitos e etapas de teste, consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=line).

### Etapa 6: Construa o restante da sua campanha ou Canvas {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Escolha um cronograma ou gatilho de entrega {#choose-a-delivery-schedule-or-trigger}

Entregue mensagens LINE em um horário agendado ou em resposta a uma ação ou gatilho de API. Para opções de agendamento e gatilho, consulte [Agendar sua campanha]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Configure controles de entrega como [reelegibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) e [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping). Para entrega baseada em ação, defina a duração da campanha e o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

#### Escolha os usuários para direcionar {#choose-users-to-target}

[Direcione usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) selecionando segmentos e filtros. A Braze calcula a associação exata ao segmento antes de enviar a mensagem.

O LINE controla o status de inscrição de cada usuário. Um usuário deve ter um `native_line_id` e seguir o canal LINE associado ao grupo de inscrições selecionado para receber a mensagem. Para mais detalhes, consulte [Status de inscrição do LINE]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#line).

#### Escolha eventos de conversão {#choose-conversion-events}

Use [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) para medir ações após um usuário receber a campanha. Defina uma janela de conversão de até 30 dias.

{% endtab %}
{% tab Canvas %}

Conclua as seções restantes do seu Canvas. Para cronogramas de entrada, configurações de público e controles de envio, consulte [Criar um Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).

Você pode usar mensagens LINE recebidas para iniciar ou ramificar um Canvas com base em palavras-gatilho. Para requisitos de comportamento e capitalização, consulte [Enviar mensagens para usuários LINE]({{site.baseurl}}/user_guide/channels/line/message_users).

{% endtab %}
{% endtabs %}

### Etapa 7: Revise e publique {#step-7-review-and-deploy}

Depois de terminar de construir sua campanha ou Canvas, revise os detalhes e teste a mensagem antes de enviá-la.

Após o lançamento, use os [relatórios do LINE]({{site.baseurl}}/user_guide/channels/line/reporting) para analisar o desempenho das mensagens.

## Informações importantes {#things-to-know}

- Uma mensagem LINE pode conter entre uma e cinco bolhas de mensagem.
- Um grupo de inscrições é mapeado para um canal LINE, e todas as variantes em uma campanha devem usar o mesmo grupo de inscrições.
- O LINE é a fonte da verdade para o status de inscrição. Usuários que não seguem o canal LINE selecionado não recebem a mensagem.
- O LINE calcula estatísticas de abertura e relacionadas a cliques somente quando mais de 20 usuários realizam o evento em um determinado dia.