## Blocos do editor de mensagens no app {#in-app-message-editor-blocks}

Os blocos do editor ficam na seção **Build** para mensagens no app. Arraste um bloco para dentro de uma coluna; ele se ajusta automaticamente à largura da coluna. Selecione um bloco para editar suas configurações no painel do lado direito.

Para saber mais sobre como criar mensagens no app no **editor de arrastar e soltar**, consulte [Criar uma mensagem no app com arrastar e soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop).

### Título e parágrafo {#title-and-paragraph}

Adiciona texto de título ou parágrafo à mensagem.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Botão {#button}

Adiciona um botão padrão com estilo, links e análise de dados configuráveis.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportamento ao clicar {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

### Botão de opção {#radio-button}

Adiciona uma lista de opções das quais os usuários podem selecionar uma. Quando enviado, o perfil de usuário registra o [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) associado, que deve ser uma string para ser salvo. Atributos personalizados com outros tipos de dados não são salvos no perfil de usuário.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Imagem {#image}

Insere uma imagem da [biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

Para especificações de imagem, consulte nossas [especificações de imagem de mensagem no app]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications#in-app-messages).

#### Comportamento ao clicar

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link

Insere um hyperlink que os usuários podem clicar para navegar até uma URL especificada. Pode ser incorporado dentro do texto ou de forma independente.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportamento ao clicar

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espaçador {#spacer}

Adiciona espaço ou preenchimento entre outros blocos.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Código personalizado {#custom-code}

Insere HTML, CSS ou JavaScript personalizados para personalização avançada.

| Propriedade | Descrição |
| --- | --- |
| Código personalizado | Permite adicionar, editar ou excluir HTML, CSS e JavaScript de uma mensagem no app. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Código personalizado" }

### Captura de telefone {#phone-capture}

Insere um campo de formulário para números de telefone. Quando enviado, o usuário é inscrito no grupo de inscrições de [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) ou [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups).

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Captura de e-mail {#email-capture}

Insere um campo de formulário para endereços de e-mail. Quando enviado, o endereço de e-mail é adicionado ao perfil desse usuário na Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Texto curto {#short-text}

Insere um campo de formulário que aceita atributos padrão (como nome e sobrenome) ou uma string de atributo personalizado de sua escolha.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Menu suspenso {#dropdown}

Insere um menu suspenso com uma lista predefinida de itens dos quais os usuários podem selecionar um. Você pode adicionar quaisquer strings de atributos personalizados à lista.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Caixa de seleção {#checkbox}

Insere uma caixa de seleção. Se o usuário marcar a caixa, o [atributo personalizado booleano]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) do bloco é definido como `true`. Se deixado desmarcado, seu atributo é definido como `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Grupo de caixas de seleção {#checkbox-group}

Os usuários podem selecionar entre várias opções. Os valores são definidos ou adicionados a um [atributo personalizado de array]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) definido.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Texto longo {#long-text}

Campo de texto multilinha para fluxos no estilo de pesquisa. Se você não encontrar esse bloco, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) ou com seu gerente de sucesso do cliente da Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze customer success manager.
-->

## Informações importantes {#things-to-know}

- **Vídeo:** O criador padrão não inclui um bloco de vídeo dedicado. Use **Código personalizado** para incorporar um player, se necessário. Para saber mais, consulte [Mensagens no app: perguntas frequentes]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).