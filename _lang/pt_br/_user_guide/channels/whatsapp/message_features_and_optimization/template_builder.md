---
nav_title: Criador de modelos de WhatsApp
article_title: Criador de modelos de WhatsApp
description: "Saiba como criar, configurar e enviar modelos de mensagens do WhatsApp diretamente na Braze usando o Criador de modelos de WhatsApp."
alias: /whatsapp_template_builder/
page_type: reference
channel:
  - WhatsApp
---

# Criador de modelos de WhatsApp {#whatsapp-template-builder}

> O Criador de modelos de WhatsApp permite criar e enviar modelos de mensagens do WhatsApp diretamente na Braze, sem precisar alternar entre a Braze e o Meta Business Manager. Depois que a Meta aprovar seu modelo, use-o em quantas campanhas e Canvas quiser.

## Pré-requisitos {#prerequisites}

{% multi_lang_include whatsapp/template_prerequisites.md %}

## Criar um modelo {#create-a-template}

### Etapa 1: Acessar os modelos de WhatsApp {#step-1-go-to-whatsapp-templates}

Acesse **Conteúdo** > **Modelos** > **WhatsApp** e selecione **Criar novo modelo**.

![Página de modelos de WhatsApp com botão para criar um novo modelo.]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

Você também pode criar um modelo enquanto compõe uma campanha ou Canvas de WhatsApp. Para saber mais, consulte [Criar um modelo a partir de uma campanha ou Canvas](#create-a-template-from-a-campaign-or-canvas).

### Etapa 2: Escolher uma categoria e um tipo {#step-2-choose-a-category-and-type}

Selecione uma categoria de modelo e um tipo de modelo e, quando estiver pronto, selecione **Continuar para o modelo**.

{% alert note %}
A Meta revisa os modelos com base nas [diretrizes de categoria](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization) e no conteúdo.
{% endalert %}

#### Marketing {#marketing}

Os modelos de marketing são para mensagens promocionais e de engajamento (por exemplo, mensagens de boas-vindas, promoções, ofertas, cupons, newsletters e anúncios).

| Tipo | Descrição |
| --- | --- |
| **Personalizado** | Uma mensagem padrão de WhatsApp que você cria do zero. Este é o layout abordado em [Criar seu modelo](#step-4-build-your-template). |
| **Carrossel** | Uma mensagem com cartões roláveis horizontalmente. Para saber mais, consulte [Modelos de carrossel]({{site.baseurl}}/whatsapp_carousel_templates). |
| **Oferta por tempo limitado** | Uma oferta promocional com prazo definido. Para saber mais, consulte [Modelos de oferta por tempo limitado]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats#limited-time-offer-templates). |
| **Flow** | Um modelo que abre um WhatsApp Flow (por exemplo, pesquisas ou agendamentos). Crie e gerencie o Flow no WhatsApp Manager da Meta e selecione-o ao criar o modelo. Para saber mais, consulte [WhatsApp Flows]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de modelo de marketing" }

#### Utilidade {#utility}

Os modelos de utilidade são para mensagens não promocionais (por exemplo, confirmações de pedido, atualizações de conta, recibos, lembretes de agendamento e cobrança). A Meta reclassifica conteúdo promocional como marketing.

| Tipo | Descrição |
| --- | --- |
| **Personalizado** | Uma mensagem de utilidade padrão que você cria do zero. Siga as mesmas etapas de composição em [Criar seu modelo](#step-4-build-your-template). |
| **Flow** | Um modelo de Flow de utilidade (por exemplo, lembretes, feedback ou gerenciamento de pedidos). Crie e gerencie o Flow no WhatsApp Manager da Meta e selecione-o ao criar o modelo. Para saber mais, consulte [WhatsApp Flows]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de modelo de utilidade" }

{% alert note %}
Os layouts de carrossel e oferta por tempo limitado estão disponíveis apenas para modelos de marketing.
{% endalert %}

### Etapa 3: Definir configurações do modelo {#step-3-configure-template-settings}

Preencha os seguintes campos:

| Campo | Descrição |
| ----- | ----- |
| **Conta** | A conta do WhatsApp Business (WABA) para a qual você deseja enviar o modelo. Todos os grupos de inscrições e números de telefone dentro de uma WABA compartilham o acesso ao modelo. |
| **Idioma** | O idioma deste modelo. O WhatsApp exige um modelo separado para cada idioma. |
| **Nome do modelo** | Um nome exclusivo para o seu modelo. Os nomes de modelo podem conter apenas letras minúsculas, números e underscores. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Definir configurações do modelo" }

### Etapa 4: Criar seu modelo {#step-4-build-your-template}

#### Cabeçalho (opcional) {#header-optional}

Adicione um cabeçalho para aparecer antes do corpo da mensagem. Você pode escolher:

- **Texto:** Um cabeçalho de texto curto.
- **Mídia:** Uma imagem, vídeo ou documento (somente URL). A Braze armazena a referência de mídia e envia uma amostra para a Meta para aprovação.
- **Nenhum:** Sem cabeçalho

#### Corpo {#body}

Insira o conteúdo principal da sua mensagem e personalize o corpo conforme necessário usando Liquid ou variáveis genéricas:

{% raw %}
- Use Liquid tags (por exemplo, `{{${first_name}}}`). A Braze salva seu Liquid e o exibe quando você usa o modelo em um criador de Campaign ou Canvas.
- Use variáveis genéricas, como placeholders numerados (por exemplo, `{{1}}`), se você preferir adicionar personalização depois ao criar sua mensagem.
{% endraw %}

Você pode adicionar personalização em qualquer lugar onde o botão **+** apareça. Nem todos os campos oferecem suporte a personalização.

#### Limites de caracteres do Liquid {#liquid-character-limits}

A Meta impõe limites de caracteres na estrutura do modelo que você envia para aprovação (por exemplo, 1.024 caracteres para o corpo e 60 caracteres para um cabeçalho de texto). No construtor de modelos, esses limites se aplicam ao modelo enviado para a Meta, não à mensagem final renderizada no momento do envio.

- **Variáveis {% raw %}`{{ }}`{% endraw %}:** A Braze converte variáveis Liquid em placeholders numerados ({% raw %}`{{1}}`, `{{2}}`{% endraw %}) antes de verificar o comprimento. Uma expressão longa como {% raw %}`{{${first_name}}}`{% endraw %} conta como um placeholder curto, não como a sintaxe Liquid completa.
- **Tags {% raw %}`{% %}`{% endraw %}:** As tags de lógica Liquid contam como texto literal em seu comprimento total e aparecem como cópia não editável em mensagens de modelo.

Para personalização complexa, use uma [etapa de Contexto]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) para computar valores e, em seguida, referencie variáveis mais curtas no modelo. Para restrições de Message Extras e lógica condicional, consulte [Liquid no construtor de modelos de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder/template_builder_liquid).

#### Rodapé (opcional) {#footer-optional}

Adicione um rodapé curto para aparecer após o corpo da mensagem.

#### Botões (opcional) {#buttons-optional}

Adicione até 10 botões ao seu modelo. Os tipos de botão possuem diferentes categorias e especificações, e são agrupados por categoria após o corpo da mensagem. Por padrão, os botões de resposta rápida aparecem primeiro. Para alterar a ordem em que aparecem — como mover botões de resposta rápida para depois dos botões de call-to-action — selecione **Trocar ordem dos grupos**.

| Tipo de botão | Categoria | Especificações |
| --- | --- | --- |
| Resposta rápida | Botões de resposta rápida |{::nomarkdown}<ul><li><b>Contagem máxima:</b> 10</li><li><b>Texto do botão:</b> Até 25 caracteres</li></ul> {:/}|
| Número de telefone | Botões de call-to-action | {::nomarkdown}<ul><li><b>Contagem máxima:</b> 1</li><li><b>Texto do botão:</b> Até 25 caracteres</li><li><b>Número de telefone:</b> Número de telefone válido com código do país, sem + (por exemplo, "14155552671")</li></ul> {:/}|
| Visitar website | Botões de call-to-action | {::nomarkdown}<ul><li><b>Contagem máxima:</b> 2</li><li><b>Texto do botão:</b> Até 25 caracteres</li><li><b>URL do website:</b> Até 2.000 caracteres</li></ul> {:/}|
| Copiar código da oferta | Botões de call-to-action | {::nomarkdown}<ul><li><b>Contagem máxima:</b> 1</li><li><b>Texto do botão:</b> "Copy offer code" (não pode ser editado)</li><li><b>Código da oferta:</b> Até 15 caracteres</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Botões (opcional)" }

Para modelos de Flow, configure o botão de Flow e selecione um Flow existente da Meta em vez de adicionar botões padrão de call-to-action.

### Etapa 5: Visualizar seu modelo {#step-5-preview-your-template}

Antes de enviar, visualize como sua mensagem aparece para os destinatários:

- **Visualizar como um usuário:** Veja uma prévia genérica da mensagem.
- **Visualizar como um usuário específico:** Selecione um perfil de usuário para visualizar como o modelo é renderizado com os dados desse usuário.

### Etapa 6: Enviar para revisão {#step-6-submit-for-review}

Selecione **Enviar** para enviar seu modelo à Meta para revisão, o que normalmente leva alguns minutos, mas pode levar até 24 horas. O modelo aparece na sua página de **modelos de WhatsApp** quando é enviado, e o status é atualizado quando você atualiza a página de **modelos de WhatsApp**.

## Criar um modelo a partir de uma Campaign ou Canvas {#create-a-template-from-a-campaign-or-canvas}

Você pode criar e enviar um modelo de WhatsApp sem sair de uma Campaign ou de uma etapa de mensagem do Canvas.

1. Em uma [Campaign]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message) de WhatsApp ou em uma etapa de mensagem do Canvas, selecione o tipo de mensagem **WhatsApp Template Message**.
2. Selecione **Create new template**.
3. Escolha uma categoria e um tipo e, em seguida, crie e envie o modelo da mesma forma que faria na página de modelos do WhatsApp.
4. Após o envio, a Braze vincula o modelo pendente à mensagem. Continue personalizando enquanto o modelo estiver pendente e, depois que a Meta aprová-lo, faça o envio.

Selecione **Choose template from library** para sair do construtor e escolher um modelo existente.

{% alert note %}
Quando você cria um modelo a partir de uma Campaign ou Canvas, a Braze pode salvar seu trabalho como rascunho para que ele seja mantido caso você saia da etapa de mensagem.
{% endalert %}

## Usar um modelo aprovado em uma campanha {#use-an-approved-template-in-a-campaign}

Depois que a Meta aprovar seu modelo, você pode usá-lo em uma Campaign de WhatsApp ou em um Canvas.

1. Acesse **Campaigns** e selecione **Create Campaign** > **WhatsApp**.
2. No criador de mensagem, selecione seu modelo aprovado.
3. A Braze preenche automaticamente o conteúdo do modelo — incluindo qualquer mídia e Liquid que você inseriu durante a criação do modelo — para que você não precise digitá-lo novamente.
4. Atualize qualquer conteúdo de variável ou personalização conforme necessário. Campos bloqueados pela Meta (exibidos em cinza) não podem ser editados. Para alterar conteúdo bloqueado, você deve editar e reenviar o modelo para aprovação.
5. Use a guia **Test** para visualizar a mensagem, atualizar as variáveis do corpo e confirmar que a mensagem está conforme o esperado antes do envio.

Para saber mais sobre como criar Campaigns de WhatsApp, consulte [Criar uma mensagem de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message).

## Perguntas frequentes {#frequently-asked-questions}

### Quanto tempo leva a revisão de modelo pela Meta? {#how-long-does-meta-template-review-take}

As revisões geralmente são concluídas em cinco minutos, mas podem levar até 24 horas.

### Posso editar um modelo depois de aprovado? {#can-i-edit-a-template-after-its-been-approved}

Você pode atualizar o conteúdo de variáveis e a personalização ao criar uma Campaign ou Canvas. Alterações em conteúdo bloqueado (corpo do texto, layout de botões ou outros campos controlados pela Meta) exigem a criação de um novo modelo no construtor de modelos ou a edição do modelo no WhatsApp Manager da Meta, aguardando uma nova aprovação. Se você usar o [rastreamento de cliques]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/click_tracking), consulte esse artigo antes de editar modelos criados pela Braze no WhatsApp Manager da Meta.

### O que acontece com os modelos que enviei antes do construtor de modelos estar disponível? {#what-happens-to-templates-i-submitted-before-the-template-builder-was-available}

Os modelos criados no Meta Business Manager ainda estão disponíveis para uso na Braze. O construtor de modelos é uma forma adicional de criar e gerenciar modelos sem sair do dashboard da Braze.

### Por que não consigo adicionar personalização em todos os campos? {#why-cant-i-add-personalization-to-every-field}

A Meta restringe quais partes de um modelo podem ser personalizadas. O botão **+** (mais) aparece apenas nos campos que suportam conteúdo de variáveis.