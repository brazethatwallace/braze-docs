---
nav_title: FAQ
article_title: FAQ do editor de arrastar e soltar
alias: "/dnd/faq/"
channel: email
page_order: 5
description: "Este artigo aborda diversas perguntas frequentes relacionadas ao editor de arrastar e soltar."
tool:
  - Campaigns
  - Canvas

---

# Perguntas frequentes {#frequently-asked-questions}

> Esta página fornece respostas para algumas perguntas frequentes relacionadas ao editor de arrastar e soltar para e-mail.

### Posso pré-visualizar como meu e-mail aparece no modo escuro? {#can-i-preview-how-my-email-appears-in-dark-mode}

Sim. Acesse a seção **Preview and Test** do editor de arrastar e soltar e ative o **Dark mode**. Recomendamos também pré-visualizar e testar seus e-mails em diferentes plataformas de usuários e usar imagens transparentes para imagens de fundo de linha sempre que possível.

### Como devo projetar e-mails para modo escuro e modo claro? {#how-should-i-design-emails-for-dark-mode-and-light-mode}

Os e-mails não precisam ser enviados em layouts separados para claro e escuro, pois os clientes de e-mail e dispositivos podem aplicar seu próprio tema escuro. No entanto, isso pode inverter cores ou ocultar fundos se cores explícitas não forem definidas no contêiner externo e nas seções principais. Para evitar isso, recomendamos definir cores de fundo sólidas para que sua mensagem seja lida claramente tanto no modo escuro quanto no modo claro.

### Como posso alterar o padding do e-mail no celular sem atualizar o padding na visualização web? {#how-can-i-change-the-email-padding-on-mobile-without-updating-the-padding-in-the-web-view}

Não é possível editar o padding para visualizações de celular e web de forma independente, então qualquer edição é refletida em ambas as visualizações. No entanto, você pode adicionar lógica CSS no editor de HTML que define o padding com base em diferentes tamanhos de tela. Isso não é compatível com o editor de arrastar e soltar, então você pode exportar o arquivo HTML e usar o editor de HTML.

### Como posso otimizar uma linha de botões para permanecer horizontal no desktop e no celular? {#how-can-i-optimize-a-row-of-buttons-to-remain-horizontal-on-desktop-and-mobile}

Ao criar um e-mail usando o editor de arrastar e soltar, se você criar uma linha horizontal de botões de chamada para ação, pode perceber que os botões são alterados para uma orientação vertical no celular.

Para manter o mesmo formato em diferentes tamanhos de dispositivo, recomendamos criar uma linha separada com botões de CTA que tenham padding otimizado para celular e estejam configurados para ocultar a linha em um dispositivo desktop. Ter duas linhas separadas significa que você pode definir o padding desejado para a melhor renderização de texto em dispositivos desktop e celular.

### Posso ajustar a altura da linha no editor de arrastar e soltar? {#can-i-adjust-the-row-height-in-the-drag-and-drop-editor}

A altura da linha se ajusta automaticamente ao conteúdo. Como alternativa, recomendamos que você:
1. Adicione um bloco divisor.
2. Clique no botão para ativar sua transparência.
3. Ajuste a altura.

### É possível criar camadas no editor? Posso adicionar uma imagem de fundo, sobrepor uma imagem e adicionar uma camada de texto sobre isso? {#is-it-possible-to-build-layers-in-the-editor-can-i-add-a-background-image-layer-on-an-image-and-add-a-text-layer-over-that}

O editor de arrastar e soltar atualmente suporta duas camadas. Você pode definir uma imagem de fundo de linha e personalizar cores de fundo.

### Posso salvar meu e-mail de arrastar e soltar como modelo depois de criá-lo na minha Campaign ou Canvas? {#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

Não, você deve recriar o e-mail em **Modelos de e-mail** para salvá-lo.

### Posso adicionar anexos de e-mail ao editor de arrastar e soltar? {#can-i-add-email-attachments-to-the-drag-and-drop-editor}

Sim. Você pode adicionar anexos à sua mensagem de e-mail acessando **Sending Settings** > **Advanced**.