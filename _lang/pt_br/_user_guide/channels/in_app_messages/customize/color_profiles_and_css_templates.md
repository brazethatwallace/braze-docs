---
nav_title: Perfis de cores e modelos CSS
article_title: Perfis de cores e modelos CSS
page_order: 3
page_type: reference
description: "Este artigo fornece uma visão geral dos perfis de cores e modelos CSS para mensagens no app."
channel:
  - in-app messages
---

# Perfis de cores e modelos CSS {#reusable-color-profiles}

> Você pode salvar modelos de mensagens no app e mensagens no navegador no dashboard para criar rapidamente novas campanhas e mensagens usando seu estilo. Este artigo se aplica ao [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/). Se você estiver usando o editor de arrastar e soltar, consulte [Configurações de estilo]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/).

Acesse **Modelos** > **Modelos de mensagens no app**.

Nesta página, você pode editar modelos existentes ou clicar em **+ Criar** e escolher **Perfil de cores** ou **Modelo CSS** para criar novos modelos para usar nas suas mensagens no app.

## Perfil de cores {#color-profile}

Você pode personalizar o esquema de cores do seu modelo de mensagem inserindo um código de cor HEX ou clicando na caixa colorida e selecionando uma cor com o seletor de cores.

Clique em **Salvar perfil de cores** quando terminar.

### Gerenciando perfis de cores {#managing-color-profiles}

Você também pode [duplicar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) e [arquivar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) modelos! Saiba mais sobre como criar e gerenciar modelos e conteúdo criativo em [Modelos e mídia]({{site.baseurl}}/user_guide/messaging/templates/).

## Modelo CSS {#in-app-message-templates}

Você pode personalizar um modelo CSS completo para sua [mensagem no app do tipo modal web](#web-modal-css).

Nomeie e adicione tags ao seu modelo CSS, depois escolha se ele será ou não o seu modelo padrão. Você pode escrever seu próprio CSS no espaço fornecido. Esse espaço já vem pré-preenchido com o CSS mostrado na pré-visualização da sua mensagem, e você pode ajustá-lo livremente para atender às suas necessidades.

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

Como você pode ver, é possível editar tudo, desde a cor de fundo até o tamanho e peso da fonte, e muito mais.

### Gerenciando modelos CSS {#managing-css-templates}

Você também pode [duplicar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) e [arquivar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) modelos! Saiba mais sobre como criar e gerenciar modelos e conteúdo criativo em [Modelos e mídia]({{site.baseurl}}/user_guide/messaging/templates/).

## Modal com CSS (somente web) {#web-modal-css}

Se você optar por usar uma mensagem do tipo modal web com CSS (somente web), poderá aplicar seu próprio modelo ou escrever seu próprio CSS no espaço fornecido. Esse espaço já vem pré-preenchido com o CSS mostrado na pré-visualização da sua mensagem, mas fique à vontade para ajustá-lo conforme suas necessidades.

Se quiser aplicar seu próprio modelo, clique em **Aplicar modelo** e escolha na galeria de modelos de mensagens no app. Se você não tiver nenhuma opção, pode fazer upload de um [modelo CSS]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/color_profiles_and_css_templates/#in-app-message-templates) usando o construtor de modelos CSS.