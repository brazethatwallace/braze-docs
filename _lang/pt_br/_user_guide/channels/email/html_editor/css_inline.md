---
nav_title: CSS inlining
article_title: CSS Inlining
page_order: 5.1
description: "Este artigo de referência aborda como ativar o CSS inlining e algumas práticas recomendadas."
channel:
  - email

---

# CSS inlining

> CSS inlining é uma forma de pré-processamento de e-mail que move os estilos de uma folha de estilos CSS para o corpo de um e-mail HTML. O termo "inlining" se refere ao fato de que os estilos são aplicados "inline" a elementos HTML individuais.

Para alguns clientes de e-mail, o CSS inlining pode melhorar a forma como os e-mails são renderizados e ajudar a garantir que seus e-mails tenham a aparência esperada. Se você já tem a maior parte do CSS inline ou tem certeza de que seu HTML e CSS são compatíveis com os requisitos da maioria dos clientes de e-mail, pode não ser necessário ativar esse recurso. Ele pode fazer com que estilos incorporados dinamicamente entrem em conflito com seus estilos inline existentes e pode alterar a pré-visualização e a renderização esperadas do e-mail.

## Usando CSS inlining

Você pode controlar se o CSS inlining está ativado ou desativado para qualquer mensagem de e-mail usando o botão **Enable inline CSS** na guia **Sending Info** do editor de HTML.

![Caixa de seleção para gerenciar CSS inlining no criador de HTML.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### Estado padrão de inlining

Você pode definir um estado padrão ativado ou desativado globalmente em **Configurações** > **Preferências de e-mail**. Localize a configuração de **CSS Inlining**. Essa configuração determina o valor padrão desejado com o qual todas as novas mensagens de e-mail começam. Observe que alterar essa configuração não afetará nenhuma das suas mensagens de e-mail existentes. Você também pode substituir esse padrão a qualquer momento ao redigir mensagens de e-mail.

![Opção de aplicar CSS inline em novos e-mails por padrão, localizada nas configurações de e-mail.]({% image_buster /assets/img_archive/css-inline1.png %})