## Blocos do editor de Banner {#banner-editor-blocks}

No criador de Banner, arraste linhas e blocos da seção **Build** para o canvas para organizar o layout da sua mensagem. Selecione **Styles** para ajustar o estilo no nível da página, ou selecione um bloco ou linha para editar suas propriedades no painel lateral.

Para o fluxo completo de criação de Banner, consulte [Criar um Banner]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#compose-a-banner).

O criador de Banner oferece os mesmos tipos de blocos de layout que outras superfícies de arrastar e soltar, mas não o conjunto completo de blocos de formulário (por exemplo, não há blocos de botão de opção, texto curto, menu suspenso ou caixa de seleção). Você pode adicionar blocos de **Phone capture** e **Email capture**; apenas **um** bloco de captura de telefone e **um** bloco de captura de e-mail são permitidos por mensagem.

### Título e parágrafo {#title-and-paragraph}

Adiciona texto de título ou corpo com opções de formatação de texto.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Botão {#button}

Adiciona um botão clicável. Você pode definir links e opções de análise de dados no painel de propriedades.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportamento ao clicar {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

Para saber mais, consulte [Definir comportamento ao clicar]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#step-32-define-on-click-behavior-optional) no artigo de Banner.

### Imagem {#image}

Exibe uma imagem a partir de uma URL hospedada. Configure as opções de exibição no painel de propriedades.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### Comportamento ao clicar

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link

Insere um hiperlink que os usuários podem selecionar.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportamento ao clicar

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espaçador {#spacer}

Adiciona espaçamento vertical entre blocos.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Código personalizado {#custom-code}

Insere HTML personalizado para layouts avançados ou conteúdo incorporado (por exemplo, vídeo). Cliques dentro de HTML personalizado não são rastreados, a menos que você chame `brazeBridge.logClick()` — consulte [Código personalizado e ponte JavaScript para Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code/).

| Propriedade | Descrição |
| --- | --- |
| Código personalizado | Adicione ou edite HTML (e ativos relacionados) para o Banner. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Código personalizado" }

### Captura de telefone {#phone-capture}

Coleta um número de telefone. Ao enviar, inscreve o usuário no grupo de inscrições de [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) ou [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/) selecionado. Apenas um por Banner.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Captura de e-mail {#email-capture}

Coleta um endereço de e-mail e o adiciona ao perfil da Braze do usuário ao enviar. Apenas um por Banner.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Texto longo {#long-text}

Campo de texto multilinha para fluxos no estilo de pesquisa. Se você não vir esse bloco, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support/) ou seu gerente de sucesso do cliente.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.
-->

## Informações importantes {#things-to-know}

- **Vídeo:** O criador padrão não inclui um bloco de vídeo dedicado. Use **Custom code** para incorporar um player, se necessário. Para saber mais, consulte [Banners: perguntas frequentes]({{site.baseurl}}/user_guide/channels/banners/faq/).
- **Liquid:** A maioria do Liquid é compatível; existem exceções, como tags de re-renderização de catálogo. Para saber mais, consulte [Banners: perguntas frequentes]({{site.baseurl}}/user_guide/channels/banners/faq/).