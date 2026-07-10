## Blocos do editor da Central de Preferências {#preference-center-editor-blocks}

Arraste blocos da seção **Build** para uma linha no editor de arrastar e soltar da Central de Preferências. Cada bloco tem suas próprias configurações; o painel do lado direito alterna entre propriedades ou estilo do elemento selecionado.

Antes de editar os blocos, adicione grupos de inscrições e configure o **smart block** de inscrição (veja a seção a seguir). Para o fluxo completo de configuração, consulte [Criar uma Central de Preferências de e-mail com arrastar e soltar]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center).

### Título e parágrafo {#title-and-paragraph}

Adiciona um cabeçalho ou corpo de texto com opções de rich text.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Botão {#button}

Adiciona um botão clicável (por exemplo, **Salvar** ou navegação).

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

### Imagem {#image}

Exibe uma imagem da [biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) ou de uma URL.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

### Espaçador {#spacer}

Adiciona espaçamento vertical entre blocos.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Grupos de inscrições (smart block) {#subscription-groups-smart-block}

Adiciona um bloco de modelo que lista grupos de inscrições, controles opcionais de **Subscribe to all** / **Unsubscribe from all** e descrições. Configure-o depois de adicionar grupos no fluxo de trabalho da Central de Preferências.

Depois de [adicionar grupos de inscrições]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#step-3-add-subscription-groups-to-the-preference-center), selecione o smart block no canvas para:

- Reordenar grupos de inscrições
- Adicionar ou remover grupos
- Adicionar ou remover descrições
- Alternar **Subscribe to all** e **Unsubscribe from all** para os grupos nesse bloco

O controle **Unsubscribe from all** na parte inferior do modelo padrão é obrigatório e realiza um [cancelamento de inscrição global]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) de e-mail.

## Informações importantes {#things-to-know}

- **Estilos comuns:** você pode definir padrões para toda a página em **Common Styles** antes de ajustar blocos individuais. Para saber mais, consulte [Personalizar a Central de Preferências usando o editor de arrastar e soltar]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#step-4-customize-the-preference-center-using-the-drag-and-drop-editor).
- **Página de confirmação:** alterne para **Confirmation Page** no topo do editor para estilizar a experiência pós-salvamento usando os mesmos tipos de bloco.