---
nav_title: Rastreamento de cliques
article_title: Rastreamento de cliques
page_order: 2
description: "Este artigo de referência aborda como ativar o rastreamento de cliques nas suas mensagens do WhatsApp, testar links encurtados, usar seu domínio personalizado em links rastreados e muito mais."
page_type: reference
alias: "/whatsapp_click_tracking/"
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Rastreamento de cliques {#click-tracking}

> Esta página aborda como ativar o rastreamento de cliques nas suas mensagens do WhatsApp, testar links encurtados, usar seu domínio personalizado em links rastreados e muito mais.

O rastreamento de cliques permite medir quando alguém toca em um link na sua mensagem do WhatsApp, oferecendo uma visão clara de qual conteúdo está gerando engajamento. A Braze encurta seus URLs, adiciona rastreamento nos bastidores e registra eventos de clique conforme eles acontecem.

Você pode ativar o rastreamento de cliques tanto em mensagens de resposta quanto em mensagens de modelo. Ele funciona com links em botões e no corpo do texto, e oferece suporte a URLs personalizados e domínios personalizados. Depois de ativado, você verá os dados de cliques nos seus relatórios de desempenho do WhatsApp e poderá segmentar usuários com base em quem clicou em quê.

{% alert note %}
O rastreamento de cliques não funciona com deep links. Você pode encurtar links universais de provedores como Branch ou Appsflyer, mas a Braze não consegue solucionar problemas que possam surgir ao fazer isso (como quebrar a atribuição ou causar um redirecionamento).
{% endalert %}

## Como funciona {#how-it-works}

### Mensagens de resposta {#response-messages}

Para configurar o rastreamento de cliques para mensagens de resposta:
1. Crie uma mensagem de resposta que inclua um botão de chamada para ação (CTA) com um URL de site.
2. Ative o rastreamento de cliques clicando no botão designado na interface.

O link será encurtado para o domínio da Braze, ou para o domínio personalizado especificado para o grupo de inscrições, e personalizado para o usuário.

Quaisquer URLs estáticos que comecem com `http://` ou `https://` serão encurtados. URLs encurtados que contenham personalização com Liquid (como direcionamento de rastreamento no nível do usuário) serão válidos por dois meses.

![Criador de mensagens do WhatsApp com corpo de conteúdo e um botão.]({% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %})

### Mensagens de modelo {#template-messages}

Recomendamos ativar o rastreamento de cliques para mensagens de modelo por meio do **WhatsApp Template Builder** na Braze. Esse método de ativação lida automaticamente com os requisitos de formatação de URL, então você não precisa configurar nada manualmente no WhatsApp Business Manager.

Se você estiver criando modelos diretamente no WhatsApp Business Manager, consulte [Configurar o rastreamento de cliques a partir do WhatsApp Business Manager](#configuring-click-tracking-from-whatsapp-business-manager).

#### Usar o Template Builder {#use-the-template-builder}

Ao criar um modelo no Template Builder, o rastreamento de cliques é configurado na guia **Settings**.

##### Etapa 1: Ativar o rastreamento de cliques {#step-1-enable-click-tracking}

No Template Builder, acesse a guia **Settings**. Em **Link options**, marque a caixa de seleção **Click tracking**. Quando ativado, todos os links no seu modelo (tanto no corpo da mensagem quanto nos botões CTA de site) são encurtados e rastreados.

![Guia Settings no Template Builder mostrando a seção Link options com a caixa de seleção Click tracking ativada e um menu suspenso de domínio personalizado.]({% image_buster /assets/img/whatsapp/click_tracking/template_builder_settings.png %})

##### Etapa 2: Selecionar um domínio personalizado (opcional) {#step-2-select-a-custom-domain-optional}

Em **Custom domain**, selecione o domínio que você deseja usar para links encurtados. O menu suspenso mostra todos os domínios de rastreamento personalizados configurados para o seu espaço de trabalho. Se você não selecionar um, a Braze usará o domínio padrão `brz.ai`.

Para adicionar ou alterar domínios, selecione **Subscription Group Management**.

{% alert important %}
Depois que um modelo é enviado à Meta para aprovação, o domínio de rastreamento não pode ser alterado. Confirme que você selecionou o domínio correto antes de enviar.
{% endalert %}

##### Etapa 3: Adicionar seus URLs de destino {#step-3-add-your-destination-urls}

Volte para a guia **Compose** e adicione o conteúdo da sua mensagem.

- **Para botões CTA de site:** Insira o URL de destino no campo **Click tracking URL**. A Braze armazena seu URL de destino e formata automaticamente o URL do site do botão com o domínio de rastreamento e um espaço reservado de variável {% raw %}(por exemplo, `https://brz.ai/{{1}}`){% endraw %}. Esse espaço reservado é o que é enviado à Meta. No momento do envio, a Braze gera o URL rastreado completo para cada usuário e preenche a variável.
- **Para links no corpo do texto:** Insira os URLs diretamente no corpo.

Você pode pré-visualizar o formato do URL rastreado para cada botão diretamente no campo **Website URL** (por exemplo, `https://brz.ai/XXXXXXXX`).

![Seção de botões de chamada para ação mostrando um botão Visit website com o Website URL pré-preenchido no formato rastreado e um campo Click tracking URL para o destino.]({% image_buster /assets/img/whatsapp/click_tracking/template_builder_compose.png %}){: style="max-width:70%;"}

##### Atualizar URLs de destino após o envio {#update-destination-urls-after-submission}

Depois que um modelo é enviado à Meta, o domínio de rastreamento fica bloqueado, mas o URL de destino permanece editável a qualquer momento. Para atualizar para onde um link aponta, edite o campo **Click tracking URL** desse botão. O formato do URL rastreado permanece o mesmo; a Braze redireciona os usuários para o novo destino no momento do envio.

#### Configurar o rastreamento de cliques a partir do WhatsApp Business Manager {#configure-click-tracking-from-whatsapp-business-manager}

Se você estiver criando modelos no WhatsApp Business Manager em vez do Template Builder, siga estas etapas para que o rastreamento de cliques funcione corretamente quando o modelo for usado na Braze.

##### Etapa 1: Criar um modelo compatível com rastreamento de cliques no WhatsApp Business Manager {#step-1-build-a-click-tracking-supported-template-in-whatsapp-business-manager}

1. No seu WhatsApp Business Manager, crie um URL base que seja seu domínio personalizado ou `brz.ai`.
2. Certifique-se de que os links incluídos no modelo sejam compatíveis com o rastreamento de cliques.
3. Não altere as variáveis do modelo depois que ele for configurado como uma Campaign na Braze; alterações posteriores não podem ser incorporadas.
4. Para links de botão CTA, selecione **Dynamic** e forneça o URL base (`brz.ai` ou seu domínio personalizado).

![Seção para criar uma chamada para ação.]({% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %}){: style="max-width:70%;"}

{: start="5"}
5. Para links no corpo do texto, ao escrever o modelo no seu WhatsApp Business Manager, remova quaisquer espaços inseridos nos links contidos no corpo que você deseja rastrear.

![Caixa de texto para inserir o corpo do conteúdo da chamada para ação.]({% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %}){: style="max-width:70%;"}

##### Etapa 2: Concluir seu modelo na Braze {#step-2-complete-your-template-in-braze}

Ao redigir, a Braze detecta automaticamente quais modelos possuem domínios de URL compatíveis, tanto no corpo do texto quanto para botões CTA. O status é exibido na parte inferior do modelo.

![Seção Link Status mostrando um status ativo para rastreamento de cliques.]({% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}){: style="max-width:70%;"}

- **Links compatíveis:** Links enviados com o URL base correspondente terão o rastreamento de cliques ativado.
- **Links parcialmente compatíveis:** Se alguns links em um modelo forem enviados como URLs completos, o rastreamento de cliques **não** será aplicado a esses links.
- **Links não compatíveis:** Links sem um URL base aprovado **não** terão capacidade de rastreamento de cliques.

O URL de destino precisa ser fornecido para qualquer link com um URL base que corresponda a `brz.ai` ou ao seu domínio personalizado.

![Seção Buttons com campos para nome do botão, URL do site e URL de rastreamento de cliques.]({% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}){: style="max-width:70%;"}

{% alert important %}
**Envio de mensagens de modelo via API**: O rastreamento de cliques do WhatsApp (usando `brz.ai` ou um domínio de rastreamento personalizado e o campo **Click tracking URL** no criador de mensagens) não é compatível ao enviar mensagens de modelo do WhatsApp pelo [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages).

Se você enviar uma mensagem de modelo pela API, poderá preencher variáveis de URL do CTA (usando `button_variables`), mas a Braze não gera um URL de rastreamento de cliques ou link de redirecionamento no fluxo de solicitação da API. Para usar o rastreamento de cliques, envie o modelo pelo dashboard da Braze ou por meio de um gatilho de Campaign da Braze.
{% endalert %}

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

## Personalização com Liquid em URLs {#liquid-personalization-in-urls}

Você pode construir seu URL dinamicamente diretamente no criador da Braze, permitindo adicionar parâmetros UTM dinâmicos aos seus URLs ou enviar links exclusivos aos usuários (como direcionar usuários ao carrinho abandonado ou a um produto específico que voltou ao estoque).
Os URLs podem ser gerados dinamicamente por meio do uso de quaisquer tags de personalização com Liquid compatíveis.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Também oferecemos suporte ao encurtamento de variáveis Liquid definidas de forma personalizada, como nestes exemplos:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Encurtar URLs renderizados por variáveis Liquid {#shorten-urls-rendered-by-liquid-variables}

A Braze encurta URLs renderizados por Liquid, incluindo aqueles incluídos em propriedades de gatilho de API. Por exemplo, se {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representar um URL válido, encurtaremos e rastrearemos esse URL antes de enviar a mensagem do WhatsApp.

## Testes {#testing}

Antes de lançar sua Campaign ou Canvas, a prática recomendada é pré-visualizar e testar sua mensagem primeiro. Para isso, acesse a guia **Test** para pré-visualizar e enviar um WhatsApp para grupos de teste de conteúdo ou para um usuário individual.

Esta prévia será atualizada com a personalização relevante e o URL encurtado.

{% alert important %}
Se um rascunho for criado dentro de um Canvas ativo, um URL encurtado não será gerado. O URL encurtado real é gerado quando o rascunho do Canvas é ativado.
{% endalert %}

## Relatórios {#reporting}

Quando o rastreamento de cliques está ativado ou é usado com modelos compatíveis, a tabela de desempenho do WhatsApp inclui a coluna **Total Clicks** que mostra uma contagem de eventos de clique por variante e uma taxa de cliques associada. Para mais detalhes sobre métricas do WhatsApp, consulte [Desempenho de mensagens do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/reporting).

![Etapa do Canvas de mensagem do WhatsApp.]({% image_buster /assets/img/whatsapp/click_tracking/canvas_step.png %}){: style="max-width:30%;"}

Os dados de cliques serão reportados automaticamente no dashboard de análise de dados.

![Tabela de desempenho de mensagens do WhatsApp.]({% image_buster /assets/img/whatsapp/click_tracking/message_performance.png %})

## Redirecionamento de usuários {#retargeting-users}

Você pode usar o filtro `Clicked/Opened Step` e a interação `clicked tracked WhatsApp link` para segmentar usuários com base nas interações deles com os links.

![Grupo de filtros com um filtro para "clicked tracked WhatsApp link".]({% image_buster /assets/img/whatsapp/click_tracking/filter_group.png %})

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Eu sei quais usuários individuais estão clicando em um URL? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Sim. Quando o rastreamento de cliques está ativado (ou habilitado com base na configuração do modelo), você pode redirecionar usuários que clicaram em URLs aproveitando os filtros de redirecionamento do WhatsApp ou os eventos de clique do WhatsApp (`users.messages.whatsapp.Click`) enviados pelo Currents.

### As prévias no dispositivo WhatsApp contam como cliques? {#do-previews-on-the-whatsapp-device-count-as-clicks}

Não, elas não contribuem para a taxa de cliques das mensagens do WhatsApp.