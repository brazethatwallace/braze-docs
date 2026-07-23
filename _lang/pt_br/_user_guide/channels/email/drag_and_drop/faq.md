---
nav_title: FAQ
article_title: FAQ do editor de arrastar e soltar
alias: "/dnd/faq/"
channel: email
page_order: 5
description: "Perguntas frequentes sobre o editor de arrastar e soltar para e-mail."
tool:
  - Campaigns
  - Canvas


---

# Perguntas frequentes {#frequently-asked-questions}

> Esta página fornece respostas para algumas perguntas frequentes relacionadas ao editor de arrastar e soltar para e-mail.

## Posso visualizar como meu e-mail aparece no modo escuro? {#can-i-preview-how-my-email-appears-in-dark-mode}

Sim. Acesse a seção **Prévia e Teste** do editor de arrastar e soltar e ative o **Modo escuro**. Recomendamos também visualizar e testar seus e-mails em diferentes plataformas de usuários e usar imagens transparentes para imagens de fundo de linha sempre que possível.

## Como devo projetar e-mails para modo escuro e modo claro? {#how-should-i-design-emails-for-dark-mode-and-light-mode}

Os e-mails não precisam ser enviados em layouts separados para modo claro e modo escuro, pois os clientes de e-mail e dispositivos podem aplicar seu próprio tema escuro. No entanto, isso pode inverter cores ou ocultar fundos se cores explícitas não forem definidas no contêiner externo e nas seções principais. Para evitar isso, recomendamos definir cores de fundo sólidas para que sua mensagem seja lida com clareza tanto no modo escuro quanto no modo claro.

Alguns clientes de e-mail substituem imagens de fundo ou invertem texto de baixo contraste no modo escuro, fazendo com que o corpo do texto pareça ausente ou seja renderizado de forma diferente entre clientes (por exemplo, Gmail no iOS versus Android). Defina `background-color` no contêiner externo e nas seções principais em vez de depender apenas de imagens de fundo para fundos claros.

## Por que minha fonte personalizada não aparece na prévia do e-mail de arrastar e soltar? {#why-doesnt-my-custom-font-appear-in-drag-and-drop-email-preview}

As fontes personalizadas são carregadas na prévia do editor quando um bloco **Text** na mensagem faz referência à fonte. Se a prévia ainda mostrar uma fonte de fallback após você configurar uma fonte personalizada nas configurações do **Drag-and-Drop Email Editor**, adicione um bloco **Text** que use essa fonte para que o editor a carregue na prévia. Confirme que o compartilhamento de recursos entre origens (CORS) está ativado no arquivo da sua fonte. Verifique novamente em **Preview and Test** e nos clientes de e-mail de destino antes de enviar. Para as etapas de configuração, consulte [Fonte personalizada]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings#custom-font).

## Como posso manter a formatação de texto ao copiar e colar de outro aplicativo? {#how-can-i-carry-over-text-formatting-when-i-copy-and-paste-from-another-application}

Diferentes editores de texto e aplicativos têm suas próprias formas de lidar com a formatação de texto, que podem não ser universalmente reconhecidas. Quando você copia e cola texto formatado de fora da Braze no editor de arrastar e soltar, a formatação rica pode não ser mantida.

Para colar texto sem formatação rica, use um destes métodos:
- No Mac: Pressione <kbd>cmd</kbd>+<kbd>shift</kbd>+<kbd>V</kbd> em vez de <kbd>cmd</kbd>+<kbd>V</kbd>
- No Windows: Pressione <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>V</kbd> em vez de <kbd>ctrl</kbd>+<kbd>V</kbd>
- Clique com o botão direito dentro do editor e selecione **Colar e Corresponder Estilo**

## Como posso alterar o padding do e-mail no celular sem atualizar o padding na visualização web? {#how-can-i-change-the-email-padding-on-mobile-without-updating-the-padding-in-the-web-view}

Não é possível editar o padding exclusivamente para as visualizações de celular e web, então qualquer edição é refletida em ambas as visualizações. No entanto, você pode adicionar lógica CSS no editor de HTML que define o padding com base em diferentes tamanhos de tela. Isso não é compatível com o editor de arrastar e soltar, então você pode exportar o arquivo HTML e usar o editor de HTML.

## Como posso otimizar uma linha de botões para que permaneça horizontal no desktop e no celular? {#how-can-i-optimize-a-row-of-buttons-to-remain-horizontal-on-desktop-and-mobile}

Ao criar um e-mail usando o editor de arrastar e soltar, se você criar uma linha horizontal de botões de chamada para ação, pode perceber que os botões são alterados para uma orientação vertical no celular.

Para manter o mesmo formato em diferentes tamanhos de dispositivo, recomendamos criar uma linha separada com botões de CTA que tenham o preenchimento otimizado para celular e estejam configurados para ocultar a linha em um dispositivo desktop. Ter duas linhas separadas significa que você pode definir o preenchimento desejado para a melhor renderização de texto em dispositivos desktop e celulares.

## Posso ajustar a altura da linha no editor de arrastar e soltar? {#can-i-adjust-the-row-height-in-the-drag-and-drop-editor}

A altura da linha se ajusta automaticamente ao conteúdo. Como alternativa, recomendamos que você:
1. Adicione um bloco divisor.
2. Clique no botão de alternância para ativar a transparência.
3. Ajuste a altura.

## É possível criar camadas no editor? Posso adicionar uma imagem de fundo, sobrepor uma imagem e adicionar uma camada de texto por cima? {#is-it-possible-to-build-layers-in-the-editor-can-i-add-a-background-image-layer-on-an-image-and-add-a-text-layer-over-that}

O editor de arrastar e soltar atualmente suporta duas camadas. Você pode definir uma imagem de fundo para a linha e personalizar as cores de fundo.

## Posso salvar meu e-mail de arrastar e soltar como modelo depois de criá-lo na minha Campaign ou Canvas? {#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

Não. Não é possível salvar um e-mail de arrastar e soltar de uma Campaign ou Canvas como um **modelo de e-mail** de arrastar e soltar em **Modelos** > **Modelos de e-mail**. Recrie o layout em **Modelos** > **Modelos de e-mail** ou comece a partir de um modelo salvo na próxima vez. Para instruções, consulte [Criar um modelo de e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template).

Se você precisar de um modelo HTML reutilizável, selecione **Baixar arquivo** enquanto edita o corpo de arrastar e soltar, abra o HTML do ZIP e cole a marcação em um [modelo de e-mail HTML]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template) usando o editor de código HTML. Verifique novamente o Liquid, os links e os ativos hospedados depois.

Para saber mais sobre onde os modelos ficam, consulte [Modelos e mídia]({{site.baseurl}}/user_guide/messaging/templates).

## Por que não consigo alterar a cor de preenchimento de um botão no editor de arrastar e soltar? {#why-cant-i-change-a-buttons-fill-color-in-the-drag-and-drop-editor}

Os estilos no nível da página podem substituir os estilos no nível da mensagem. Se atualizar o **Preenchimento** em um botão ou bloco não surtir efeito, tente o seguinte:
1. Abra as [configurações globais de estilo de e-mail]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings) e selecione **Redefinir para o padrão** no estilo de página conflitante para que a cor no nível da mensagem possa ser aplicada.
2. Defina a cor novamente no bloco.

## Posso adicionar anexos de e-mail ao editor de arrastar e soltar? {#can-i-add-email-attachments-to-the-drag-and-drop-editor}

Sim. Você pode adicionar anexos à sua mensagem de e-mail acessando **Configurações de envio** > **Avançado**.

## Como faço para baixar o HTML bruto de um e-mail de arrastar e soltar? {#how-do-i-download-the-raw-html-for-a-drag-and-drop-email}

1. Abra sua Campaign ou Canvas e edite a mensagem de e-mail.
2. Selecione **Editar corpo do e-mail** para abrir o editor de arrastar e soltar.
3. Selecione **Baixar arquivo** (na parte inferior do editor). Extraia o arquivo para acessar o HTML gerado.

Você pode colar esse HTML em um [bloco HTML]({{site.baseurl}}/user_guide/channels/email/drag_and_drop#content) ou no editor de HTML quando precisar de edições de baixo nível — por exemplo, para [desativar o rastreamento de cliques em links específicos]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis).

## Por que meu layout de arrastar e soltar está quebrando? {#why-is-my-drag-and-drop-layout-breaking}

Problemas de layout geralmente são causados por **HTML ou CSS personalizado** que entra em conflito com a marcação gerada pelo editor. Tente estas etapas:

1. Remova ou isole blocos de HTML personalizado para verificar se o problema desaparece.
2. Verifique as configurações do **editor de arrastar e soltar de e-mail** para fontes personalizadas que podem não carregar em todos os clientes.
3. Em **Row Properties**, revise o preenchimento e as larguras das colunas.
4. Ao adicionar HTML personalizado, prefira layouts baseados em tabelas, imagens fluidas e larguras totais de tabela que se ajustem à largura do seu e-mail — imagens com pixels fixos ou estruturas que não usam tabelas frequentemente quebram no Outlook e em outros clientes.

## Por que meu Content Block não é renderizado na prévia do e-mail? {#why-doesnt-my-content-block-render-in-email-preview}

Se um Content Block não for renderizado na prévia do e-mail, verifique se há tags de âncora não fechadas. Para URLs de Connected Content, use o filtro `replace` para converter e-comerciais com codificação dupla (`&amp;amp;`) em um e-comercial com codificação simples (`&amp;`). Limite o aninhamento de Content Blocks a dois níveis.

## Por que um Content Block de arrastar e soltar perde a estilização mobile dentro de um bloco de código personalizado? {#why-does-a-drag-and-drop-content-block-lose-mobile-styling-inside-a-custom-code-block}

Quando você insere um **Content Block** de arrastar e soltar dentro de um bloco de **Código personalizado** (HTML), a estilização e o alinhamento específicos para dispositivos móveis do Content Block podem não ser aplicados na mensagem enviada. Quando tanto o Content Block quanto o modelo usam o editor de arrastar e soltar, adicione o Content Block como sua própria linha em vez de aninhá-lo dentro de Código personalizado.

Quando você empilha vários Content Blocks, use uma linha separada para cada bloco em vez de colocar vários blocos em uma única linha.

## Por que o editor de arrastar e soltar está ignorando as configurações de alinhamento? {#why-is-the-drag-and-drop-editor-ignoring-alignment-settings}

Se o editor de arrastar e soltar estiver ignorando as configurações de alinhamento, remova CSS personalizado ou blocos HTML, remova fontes personalizadas, verifique se há conflitos de CSS e evite duplicar blocos de linha. Entre em contato com o suporte da Braze se o problema persistir.

## Por que o código hexadecimal de cor que escolhi não corresponde à fonte no meu e-mail? {#why-does-my-chosen-hex-color-code-not-match-the-font-in-my-email}

Se você estiver usando um Content Block, o bloco pode ter sua própria configuração de cor de fonte. Selecione o bloco de texto dentro do Content Block e limpe qualquer substituição local de **Font color** para que a cor hexadecimal do estilo global ou de parágrafo possa ser aplicada.