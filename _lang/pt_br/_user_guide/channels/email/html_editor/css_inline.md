---
nav_title: CSS inlining
article_title: CSS inlining
page_order: 5.1
description: "Este artigo de referência aborda como ativar o CSS inlining e algumas práticas recomendadas."
channel:
  - email

---

# CSS inlining {#css-inlining}

> O CSS inlining é uma forma de pré-processamento de e-mail que move estilos de uma folha de estilo CSS para o corpo de um e-mail HTML. O termo "inlining" refere-se ao fato de que os estilos são aplicados "inline" a elementos HTML individuais.

Para alguns clientes de e-mail, o CSS inlining pode melhorar a forma como os e-mails são renderizados e ajudar a confirmar que seus e-mails têm a aparência esperada. Se você já tiver a maior parte do CSS incorporado ou tiver certeza de que seu HTML e CSS são compatíveis com os requisitos da maioria dos clientes de e-mail, talvez não seja necessário ativar esse recurso. Isso pode fazer com que os estilos incorporados dinamicamente entrem em conflito com os estilos inline existentes e pode alterar a pré-visualização esperada e a renderização do e-mail.

## Uso de CSS inlining {#using-css-inlining}

É possível controlar se o CSS inlining está ativado ou desativado em qualquer mensagem de e-mail usando a opção **Ativar CSS inline** na guia **Informações de envio** do editor de HTML.

![Caixa de seleção para gerenciar o CSS inlining no criador de HTML.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### Estado padrão de inlining {#default-inlining-state}

Você pode definir um estado padrão ligado ou desligado globalmente em **Configurações** > **Preferências de e-mail**. Localize a configuração para **CSS Inlining**. Essa configuração determina o valor padrão desejado com o qual todas as novas mensagens de e-mail começam. Observe que alterar essa configuração não afetará nenhuma das suas mensagens de e-mail existentes. Você também pode substituir esse padrão a qualquer momento ao redigir mensagens de e-mail.

![Opção de aplicar CSS inline em novos e-mails por padrão, localizada nas configurações de e-mail.]({% image_buster /assets/img_archive/css-inline1.png %})

## Conteúdo conectado e CSS inlining {#connected-content-and-css-inlining}

O CSS inlining é executado **antes** de o [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) ser avaliado. O HTML retornado pelo Conteúdo conectado **não** passa pela mesma etapa de inlining. Coloque os estilos necessários do Conteúdo conectado diretamente na resposta (atributos `style` inline ou regras incorporadas), ou desative o inlining para a mensagem se isso for mais adequado ao seu modelo.

## Content Blocks em modelos HTML personalizados {#content-blocks-in-custom-html-templates}

Quando você insere um [bloco de conteúdo]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) com Liquid dentro de um modelo de e-mail ou Campaign em **HTML personalizado**, as regras CSS do modelo pai podem sobrescrever os estilos definidos dentro do bloco de conteúdo. Verifique se há seletores conflitantes ou regras globais no wrapper do modelo.