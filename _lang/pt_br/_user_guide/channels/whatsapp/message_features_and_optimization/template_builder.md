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

### Etapa 2: Configurar as definições do modelo {#step-2-configure-template-settings}

Preencha os seguintes campos:

| Campo | Descrição |
| ----- | ----- |
| **Conta** | A conta do WhatsApp Business (WABA) para a qual você deseja enviar o modelo. Todos os grupos de inscrições e números de telefone dentro de uma WABA compartilham o acesso ao modelo. |
| **Idioma** | O idioma deste modelo. O WhatsApp exige um modelo separado para cada idioma. |
| **Nome do modelo** | Um nome exclusivo para o seu modelo. Os nomes de modelo podem conter apenas letras minúsculas, números e underscores. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Configurar as definições do modelo" }

### Etapa 3: Escolher um layout {#step-3-choose-a-layout}

Em **Layout**, selecione o tipo de modelo:

- **Padrão:** Uma mensagem padrão do WhatsApp. Este é o layout abordado neste artigo.
- **Carrossel:** Uma mensagem com cartões roláveis horizontalmente. Para saber mais, consulte [Modelos de carrossel]({{site.baseurl}}/whatsapp_carousel_templates).

### Etapa 4: Construir seu modelo {#step-4-build-your-template}

#### Cabeçalho (opcional) {#header-optional}

Adicione um cabeçalho para aparecer antes do corpo da mensagem. Você pode escolher:

- **Texto:** Um cabeçalho de texto curto.
- **Mídia:** Uma imagem, vídeo ou documento (somente URL). A Braze armazena a referência de mídia e envia uma amostra para a Meta para aprovação.
- **Nenhum:** Sem cabeçalho

#### Corpo {#body}

Insira o conteúdo principal da sua mensagem e personalize o corpo conforme necessário usando Liquid ou variáveis genéricas:

{% raw %}
- Use Liquid tags (por exemplo, `{{${first_name}}}`). A Braze salva seu Liquid e o disponibiliza quando você usa o modelo em uma Campaign ou no criador de Canvas.
- Use variáveis genéricas, como placeholders numerados (por exemplo, `{{1}}`), se preferir adicionar personalização depois ao construir sua mensagem.
{% endraw %}

Você pode adicionar personalização onde o botão **+** (mais) aparecer. Nem todos os campos suportam personalização.

#### Limites de caracteres do Liquid {#liquid-character-limits}

A Meta impõe limites de caracteres na estrutura do modelo que você envia para aprovação (por exemplo, 1.024 caracteres para o corpo e 60 caracteres para um cabeçalho de texto). No construtor de modelos, esses limites se aplicam ao modelo enviado para a Meta, não à mensagem final renderizada no momento do envio.

- **Variáveis {% raw %}`{{ }}`{% endraw %}:** A Braze converte variáveis Liquid em placeholders numerados ({% raw %}`{{1}}`, `{{2}}`{% endraw %}) antes de verificar o comprimento. Uma expressão longa como {% raw %}`{{${first_name}}}`{% endraw %} conta como um placeholder curto, não como a sintaxe Liquid completa.
- **Tags {% raw %}`{% %}`{% endraw %}:** As Liquid logic tags contam como texto literal em seu comprimento total e aparecem como texto não editável em mensagens de modelo.

Para personalização complexa, use uma [etapa de Contexto]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) para calcular valores e, em seguida, referencie variáveis mais curtas no modelo. Para restrições de Message Extras e lógica condicional, consulte [Liquid no construtor de modelos de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder/template_builder_liquid).

#### Rodapé (opcional) {#footer-optional}

Adicione um rodapé curto para aparecer após o corpo da mensagem.

#### Botões (opcional) {#buttons-optional}

Adicione até 10 botões ao seu modelo. Os tipos de botão têm categorias e especificações diferentes.

| Tipo de botão | Categoria | Especificações |
| --- | --- | --- |
| Resposta rápida | Botões de resposta rápida |{::nomarkdown}<ul><li><b>Quantidade máxima:</b> 10</li><li><b>Texto do botão:</b> Até 25 caracteres</li></ul> {:/}|
| Número de telefone | Botões de chamada para ação | {::nomarkdown}<ul><li><b>Quantidade máxima:</b> 1</li><li><b>Texto do botão:</b> Até 25 caracteres</li><li><b>Número de telefone:</b> Número de telefone válido com código do país, sem + (como "14155552671")</li></ul> {:/}|
| Visitar website | Botões de chamada para ação | {::nomarkdown}<ul><li><b>Quantidade máxima:</b> 2</li><li><b>Texto do botão:</b> Até 25 caracteres</li><li><b>URL do website:</b> Até 2.000 caracteres</li></ul> {:/}|
| Copiar código de oferta | Botões de chamada para ação | {::nomarkdown}<ul><li><b>Quantidade máxima:</b> 1</li><li><b>Texto do botão:</b> "Copy offer code" (não pode ser editado)</li><li><b>Código de oferta:</b> Até 15 caracteres</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Botões (opcional)" }

![Criador de modelos de WhatsApp com botões de resposta rápida e chamada para ação.]({% image_buster /assets/img/whatsapp/templates/buttons.png %})

### Etapa 5: Visualizar seu modelo {#step-5-preview-your-template}

Antes de enviar, visualize como sua mensagem aparecerá para os destinatários:

- **Visualizar como um usuário:** Veja uma prévia genérica da mensagem.
- **Visualizar como um usuário específico:** Selecione um perfil de usuário para visualizar como o modelo será renderizado com os dados desse usuário.

### Etapa 6: Enviar para revisão {#step-6-submit-for-review}

Selecione **Enviar** para enviar seu modelo para a Meta para revisão, que normalmente leva alguns minutos, mas pode levar até 24 horas. O modelo aparece na sua página de **modelos de WhatsApp** quando é enviado, e o status é atualizado quando você atualiza a página de **modelos de WhatsApp**.

## Categorias de modelos compatíveis {#supported-template-categories}

Atualmente, apenas modelos de Marketing são compatíveis com o construtor de modelos do WhatsApp.

## Usar um modelo aprovado em uma campaign {#use-an-approved-template-in-a-campaign}

Após a Meta aprovar seu modelo, você pode usá-lo em uma Campaign de WhatsApp ou em um Canvas.

1. Acesse **Campaigns** e selecione **Create Campaign** > **WhatsApp**.
2. No criador de mensagem, selecione seu modelo aprovado.
3. A Braze preenche automaticamente o conteúdo do modelo, incluindo qualquer mídia e Liquid que você inseriu durante a criação do modelo, para que você não precise inseri-los novamente.
4. Atualize qualquer conteúdo de variável ou personalização conforme necessário. Os campos bloqueados pela Meta (exibidos em cinza) não podem ser editados. Para alterar o conteúdo bloqueado, você deve editar e reenviar o modelo para aprovação.
5. Use a guia **Test** para visualizar a mensagem, atualizar as variáveis do corpo e confirmar que a mensagem está como esperado antes do envio.

Para saber mais sobre como criar Campaigns de WhatsApp, consulte [Criar uma mensagem de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message).

## Perguntas frequentes {#frequently-asked-questions}

### Quanto tempo leva a revisão de modelo pela Meta? {#how-long-does-meta-template-review-take}

As revisões geralmente são concluídas em cinco minutos, mas podem levar até 24 horas.

### Posso editar um modelo depois que ele for aprovado? {#can-i-edit-a-template-after-its-been-approved}

Você pode atualizar o conteúdo de variáveis e a personalização ao criar uma Campaign ou Canvas. Alterações em conteúdo bloqueado (texto do corpo, layout de botões ou outros campos controlados pela Meta) exigem a criação de um novo modelo no construtor de modelos ou a edição do modelo no WhatsApp Manager da Meta, seguida de uma nova aprovação pela Meta. Se você usa [rastreamento de cliques]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/click_tracking), consulte esse artigo antes de editar modelos criados pela Braze no WhatsApp Manager da Meta.

### O que acontece com os modelos que enviei antes do construtor de modelos estar disponível? {#what-happens-to-templates-i-submitted-before-the-template-builder-was-available}

Os modelos criados no Meta Business Manager ainda estão disponíveis para uso na Braze. O construtor de modelos é uma forma adicional de criar e gerenciar modelos sem sair do dashboard da Braze.

### Por que não consigo adicionar personalização a todos os campos? {#why-cant-i-add-personalization-to-every-field}

A Meta restringe quais partes de um modelo podem ser personalizadas. O botão de adição **+** aparece apenas nos campos que aceitam conteúdo variável.