---
nav_title: Criar um modelo de mensagem no app
article_title: Criar um modelo de mensagem no app
page_order: 0
description: "Este artigo de referência aborda como criar, salvar e gerenciar modelos de mensagens no app na seção Conteúdo do dashboard da Braze, incluindo perfis de cores e modelos CSS para o editor tradicional."
tool:
  - Templates
channel:
  - in-app messages
search_rank: 1
---

# Criar um modelo de mensagem no app {#create-an-in-app-message-template}

> Use **Content** > **In-App Message** para criar uma biblioteca reutilizável de layouts de mensagens no app e no navegador. Você pode salvar designs do editor de arrastar e soltar ou criar ativos de **Color Profile** e **CSS Template** para o [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

## Etapa 1: Abrir modelos de mensagens no app {#step-1-open-in-app-message-templates}

No dashboard da Braze, acesse **Content** > **In-App Message**.

## Etapa 2: Escolher como criar um modelo {#step-2-choose-how-to-create-a-template}

A forma de adicionar um modelo depende do seu objetivo:

| Objetivo | O que fazer |
|------|------------|
| Salvar um layout de arrastar e soltar para reutilização | No [criador de mensagens no app de arrastar e soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop), selecione **Save as template** depois de sair do editor (primeiro você precisa lançar a Campaign OU salvá-la como rascunho). O modelo aparecerá em **Templates** > **In-App Message Templates** para sua próxima mensagem. |
| Criar um perfil de cores ou modelo CSS (editor tradicional) | Na página **In-App Message Templates**, selecione **+ Create** e escolha **Color Profile** ou **CSS Template**. Para mais informações, consulte [Perfis de cores e modelos CSS](#reusable-color-profiles). |
| Personalizar um modelo da Braze | [Crie uma mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) no editor de arrastar e soltar, escolha um modelo da Braze, faça suas personalizações e selecione **Save as template**. Para descrições de cada modelo da Braze, consulte [Modelos de mensagens no app]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Escolher como criar um modelo" }

{% alert note %}
Perfis de cores e modelos CSS se aplicam ao editor tradicional. Se você usa o editor de arrastar e soltar, utilize as [Configurações de estilo]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings) para estilização no nível da mensagem.
{% endalert %}

## Etapa 3: Gerenciar seus modelos {#step-3-manage-your-templates}

Em **Content** > **In-App Message**, filtre, pesquise ou abra um modelo para editar. Você pode [duplicar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#duplicate-templates) e [arquivar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#archive-templates) modelos como outros tipos de modelo. Para uma visão geral dos fluxos de trabalho de modelos e mídia, consulte [Modelos]({{site.baseurl}}/user_guide/messaging/templates).

Para acessar modelos de mensagens no app, você precisa de [permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para visualizar ou editar modelos de mensagens no app.

### Criar perfis de cores e modelos CSS {#reusable-color-profiles}

{% alert note %}
As opções a seguir se aplicam ao [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional). Se você está usando o editor de arrastar e soltar, utilize as [Configurações de estilo]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings).
{% endalert %}

Você pode editar modelos existentes ou selecionar **+ Create** e escolher **Color Profile** ou **CSS Template** para criar novos modelos para suas mensagens no app.

#### Perfil de cores {#color-profile}

Você pode personalizar o esquema de cores do seu modelo de mensagem inserindo um código de cor HEX ou selecionando a caixa colorida e escolhendo uma cor com o seletor de cores. Se quiser que esse perfil seja aplicado por padrão ao criar novas mensagens no app no editor tradicional, selecione **Use as default profile**.

Selecione **Save Color Profile** quando terminar.

![O editor de modelo de perfil de cores de mensagens no app.]({% image_buster /assets/img/drag_and_drop/templates/color_profile_template.png %})

#### Modelo CSS {#in-app-message-templates}

Você pode personalizar um modelo CSS completo para sua [mensagem no app modal web](#web-modal-css).

Nomeie e adicione tags ao seu modelo CSS e escolha se ele será seu modelo padrão. Você pode escrever seu próprio CSS no espaço fornecido. Esse espaço já vem pré-preenchido com o CSS mostrado na pré-visualização da sua mensagem, e você pode ajustá-lo conforme suas necessidades.

```css
.ab-message-header, .ab-message-text {
  color: #333333;
  text-align: center;
}

.ab-message-header {
  font-size: 20px;
  font-weight: bold;
}

.ab-message-text {
  font-size: 14px;
  font-weight: normal;
}

.ab-close-button svg {
  fill: #9b9b9b;
}

.ab-message-button {
  border: 1px solid #1b78cf;
  font-size: 14px;
  font-weight: bold;
}
.ab-message-button:first-of-type {
  background-color: white;
  color: #1b78cf;
}
.ab-message-button:last-of-type, .ab-message-button:first-of-type:last-of-type {
  background-color: #1b78cf;
  color: white;
}

.ab-background {
  background-color: white;
}

.ab-icon {
  background-color: #0073d5;
  color: white;
}

.ab-page-blocker {
  background-color: rgba(51, 51, 51, .75);
}
```

Você pode editar tudo, desde a cor de fundo até o tamanho e peso da fonte, e muito mais.

#### Modal com CSS (somente web) {#web-modal-css}

Se você optar por usar uma mensagem Modal Web somente para web com CSS, poderá aplicar seu próprio modelo ou escrever seu próprio CSS no espaço fornecido. Esse espaço já vem pré-preenchido com o CSS mostrado na pré-visualização da sua mensagem, mas você pode ajustá-lo conforme suas necessidades.

Se quiser aplicar seu próprio modelo, selecione **Apply Template** e escolha na galeria de modelos de mensagens no app. Se você não tiver nenhuma opção, pode adicionar um [modelo CSS](#in-app-message-templates) usando o construtor de modelos CSS em **Templates** > **In-App Message Templates**.