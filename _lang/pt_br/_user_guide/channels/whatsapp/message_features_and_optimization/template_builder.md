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

Acesse **Conteúdo** > **WhatsApp** e selecione **Criar novo modelo**.

![Página de modelos de WhatsApp com botão para criar um novo modelo.]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

### Etapa 2: Configurar as definições do modelo {#step-2-configure-template-settings}

Preencha os seguintes campos:

| Campo | Descrição |
| ----- | ----- |
| **Conta** | A conta do WhatsApp Business (WABA) para a qual você deseja enviar o modelo. Todos os grupos de inscrições e números de telefone dentro de uma WABA compartilham o acesso ao modelo. |
| **Idioma** | O idioma deste modelo. O WhatsApp exige um modelo separado para cada idioma. |
| **Nome do modelo** | Um nome exclusivo para o seu modelo. Os nomes de modelo só podem conter letras minúsculas, números e underscores. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Configure template settings" }

### Etapa 3: Escolher uma disposição {#step-3-choose-a-layout}

Em **Disposição**, selecione o tipo de modelo:

- **Padrão:** Uma mensagem padrão do WhatsApp. Esta é a disposição abordada neste artigo.
- **Carrossel:** Uma mensagem com cartões roláveis horizontalmente. Para saber mais, consulte [Modelos de carrossel]({{site.baseurl}}/whatsapp_carousel_templates/).

### Etapa 4: Criar seu modelo {#step-4-build-your-template}

#### Cabeçalho (opcional) {#header-optional}

Adicione um cabeçalho para aparecer acima do corpo da mensagem. Você pode escolher:

- **Texto:** Um cabeçalho de texto curto.
- **Mídia:** Uma imagem, vídeo ou documento (somente URL). A Braze armazena a referência de mídia e envia uma amostra para a Meta para aprovação.
- **Nenhum:** Sem cabeçalho

#### Corpo {#body}

Insira o conteúdo principal da sua mensagem e personalize o corpo conforme necessário usando Liquid ou variáveis genéricas:

{% raw %}
- Use Liquid tags (por exemplo, `{{${first_name}}}`). A Braze salva seu Liquid e o exibe quando você usa o modelo em uma Campaign ou no criador de Canvas.
- Use variáveis genéricas, como placeholders numerados (por exemplo, `{{1}}`), se preferir adicionar personalização depois, ao criar sua mensagem.
{% endraw %}

Você pode adicionar personalização onde o botão **+** (mais) aparecer. Nem todos os campos suportam personalização.

#### Rodapé (opcional) {#footer-optional}

Adicione um rodapé curto para aparecer abaixo do corpo da mensagem.

#### Botões (opcional) {#buttons-optional}

Adicione até 10 botões ao seu modelo. Os tipos de botão têm categorias e especificações diferentes.

| Tipo de botão | Categoria | Especificações |
| --- | --- | --- |
| Resposta rápida | Botões de resposta rápida |{::nomarkdown}<ul><li><b>Quantidade máxima:</b> 10</li><li><b>Texto do botão:</b> Até 25 caracteres</li></ul> {:/}|
| Número de telefone | Botões de chamada para ação | {::nomarkdown}<ul><li><b>Quantidade máxima:</b> 1</li><li><b>Texto do botão:</b> Até 25 caracteres</li><li><b>Número de telefone:</b> Número de telefone válido com código do país, sem + (como "14155552671")</li></ul> {:/}|
| Visitar site | Botões de chamada para ação | {::nomarkdown}<ul><li><b>Quantidade máxima:</b> 2</li><li><b>Texto do botão:</b> Até 25 caracteres</li><li><b>URL do site:</b> Até 2.000 caracteres</li></ul> {:/}|
| Copiar código de oferta | Botões de chamada para ação | {::nomarkdown}<ul><li><b>Quantidade máxima:</b> 1</li><li><b>Texto do botão:</b> "Copy offer code" (não pode ser editado)</li><li><b>Código de oferta:</b> Até 15 caracteres</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Buttons (optional)" }

![Criador de modelos de WhatsApp com botões de resposta rápida e chamada para ação.]({% image_buster /assets/img/whatsapp/templates/buttons.png %})

### Etapa 5: Pré-visualizar seu modelo {#step-5-preview-your-template}

Antes de enviar, pré-visualize como sua mensagem aparecerá para os destinatários:

- **Pré-visualizar como um usuário:** Veja uma pré-visualização genérica da mensagem.
- **Pré-visualizar como um usuário específico:** Selecione um perfil de usuário para pré-visualizar como o modelo será renderizado com os dados desse usuário.

### Etapa 6: Enviar para revisão {#step-6-submit-for-review}

Selecione **Submit** para enviar seu modelo à Meta para revisão, o que normalmente leva alguns minutos, mas pode levar até 24 horas. O modelo aparece na sua página de **Modelos de WhatsApp** quando é enviado, e o status é atualizado quando você atualiza a página de **Modelos de WhatsApp**.

## Categorias de modelo suportadas {#supported-template-categories}

Atualmente, apenas modelos de marketing são suportados no Criador de modelos de WhatsApp.

## Usar um modelo aprovado em uma campanha {#use-an-approved-template-in-a-campaign}

Depois que a Meta aprovar seu modelo, você pode usá-lo em uma Campaign ou Canvas de WhatsApp.

1. Acesse **Campaigns** e selecione **Create Campaign** > **WhatsApp**.
2. No criador de mensagens, selecione seu modelo aprovado.
3. A Braze preenche automaticamente o conteúdo do modelo, incluindo qualquer mídia e Liquid que você inseriu durante a criação do modelo, para que você não precise inseri-los novamente.
4. Atualize qualquer conteúdo variável ou personalização conforme necessário. Os campos bloqueados pela Meta (exibidos em cinza) não podem ser editados. Para alterar conteúdo bloqueado, você deve editar e reenviar o modelo para aprovação.
5. Use a guia **Test** para pré-visualizar a mensagem, atualizar as variáveis do corpo e confirmar que a mensagem está como esperado antes do lançamento.

Para saber mais sobre como criar campanhas de WhatsApp, consulte [Criar uma mensagem de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/).

## Perguntas frequentes {#frequently-asked-questions}

### Quanto tempo leva a revisão de modelo pela Meta? {#how-long-does-meta-template-review-take}

As revisões normalmente são concluídas em cinco minutos, mas podem levar até 24 horas.

### Posso editar um modelo depois que ele foi aprovado? {#can-i-edit-a-template-after-its-been-approved}

Qualquer alteração em conteúdo bloqueado (texto do corpo ou outros campos controlados pela Meta) exige o reenvio do modelo para aprovação, o que deve ser feito pelo WhatsApp Business Manager. Você pode atualizar conteúdo e personalização ao criar sua Campaign ou Canvas.

### O que acontece com os modelos que enviei antes de o Criador de modelos estar disponível? {#what-happens-to-templates-i-submitted-before-the-template-builder-was-available}

Os modelos criados no Meta Business Manager ainda estão disponíveis para uso na Braze. O Criador de modelos é uma forma adicional de criar e gerenciar modelos sem sair do dashboard da Braze.

### Por que não consigo adicionar personalização a todos os campos? {#why-cant-i-add-personalization-to-every-field}

A Meta restringe quais partes de um modelo podem ser personalizadas. O botão **+** (mais) aparece apenas nos campos que suportam conteúdo variável.