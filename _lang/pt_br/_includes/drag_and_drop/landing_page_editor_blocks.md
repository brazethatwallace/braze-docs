## Blocos do editor de landing pages {#landing-page-editor-blocks}

Os blocos do editor para landing pages estão na seção **Build** do **editor de arrastar e soltar**, em **Rows** e categorias de blocos. Arraste um bloco para a coluna de uma linha; ele se ajusta automaticamente à largura da coluna. Selecione um bloco para editar suas configurações no painel de propriedades do lado direito.

Para saber mais sobre como criar e publicar landing pages, consulte [Criar landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).

### Título e parágrafo {#title-and-paragraph}

Adiciona texto de cabeçalho ou corpo. Útil para estruturar seções e melhorar a legibilidade.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Botão {#button}

Adiciona um elemento clicável para ações como abrir um link ou enviar um formulário.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportamento ao clicar {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

{% alert important %}
Se você configurar um botão com **Submit form when button is clicked** e abrir uma URL da web em uma nova guia, o Safari do iOS poderá bloquear a navegação. Abra a URL pós-envio na mesma guia ao enviar formulários. Para saber mais, consulte [Criar landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).
{% endalert %}

### Botão de opção {#radio-button}

Adiciona uma lista de opções da qual os usuários podem selecionar uma. Use o painel de propriedades para configurar as opções disponíveis e o atributo personalizado que recebe o valor selecionado. O perfil de usuário registra o valor selecionado como um [atributo personalizado de string]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) quando o formulário é enviado. Atributos personalizados com outros tipos de dados não são salvos no perfil de usuário.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Imagem {#image}

Exibe uma imagem a partir de um upload ou URL externa.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### Comportamento ao clicar

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link

Adiciona um hiperlink que os usuários podem selecionar para acessar uma URL. Pode ficar dentro de um texto ou isolado.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportamento ao clicar

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espaçador {#spacer}

Adiciona espaçamento vertical entre elementos.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Código personalizado {#custom-code}

Insere HTML, CSS ou JavaScript personalizados para customização avançada, como o [Google Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages#adding-google-tag-manager-to-a-landing-page).

| Propriedade | Descrição |
| --- | --- |
| Código personalizado | Permite adicionar, editar ou excluir HTML, CSS e JavaScript. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Código personalizado" }

<!-- Countdown timer is not yet released. Uncomment when available.
### Countdown timer

Displays a countdown to a date and time you set. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze customer success manager.

After you add a **Countdown timer** block, use the properties panel to set the target date and time, labels, and styling.
-->

### Captura de e-mail {#email-capture}

Adiciona um campo de formulário para endereços de e-mail. Ao enviar, o endereço é salvo no perfil da Braze do usuário.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Captura de telefone {#phone-capture}

Adiciona um campo de formulário para números de telefone. Ao enviar, inscreve o usuário no grupo de inscrições de [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) ou [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups) selecionado.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Campo de entrada {#input-field}

Adiciona um campo de formulário para atributos padrão (por exemplo, nome ou sobrenome) ou uma string de atributo personalizado.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Menu suspenso {#dropdown}

Uma lista predefinida de itens; os usuários escolhem um. Você pode mapear valores para strings de atributos personalizados.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Caixa de seleção {#checkbox}

Quando marcada, define o [atributo personalizado booleano]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) do bloco como `true`; quando desmarcada, como `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Grupo de caixas de seleção {#checkbox-group}

Os usuários escolhem múltiplas opções; os valores definem ou são adicionados a um [atributo personalizado de array]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) definido.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Texto longo {#long-text}

Campo de texto com múltiplas linhas para fluxos no estilo de pesquisa. Se você não vir esse bloco, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) ou com o seu gerente de sucesso do cliente. Esse bloco não está disponível para landing pages padrão.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze customer success manager.
-->

## Informações importantes {#things-to-know}

- **Vídeo:** O criador padrão não inclui um bloco de vídeo dedicado. Use **Código personalizado** para incorporar um player, se necessário. Para saber mais, consulte [Landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages).