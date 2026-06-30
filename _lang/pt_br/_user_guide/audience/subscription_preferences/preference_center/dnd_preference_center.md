---
nav_title: Central de Preferências de e-mail com arrastar e soltar
article_title: Central de Preferências de e-mail com arrastar e soltar
alias: "/dnd_preference_center/"
description: "Esta página de referência aborda como criar uma Central de Preferências de e-mail com o editor de arrastar e soltar."
page_order: 2
---

# Criar uma Central de Preferências de e-mail com arrastar e soltar {#create-an-email-preference-center-with-drag-and-drop}

> Usando o editor de arrastar e soltar, você pode criar e personalizar uma Central de Preferências para ajudar a gerenciar quais usuários recebem determinados tipos de comunicação. Você pode ter até 100 Centrais de Preferências por espaço de trabalho.

Você pode gerenciar as Centrais de Preferências de arrastar e soltar existentes em **Público** > **Central de Preferências de e-mail**:

- Para alterar o nome ou o conteúdo de uma Central de Preferências, abra-a no dashboard.
- As Centrais de Preferências de arrastar e soltar não podem ser excluídas pelo dashboard. Para remover uma, primeiro remova a Liquid tag dela de quaisquer Campaigns de e-mail ou etapas do Canvas e, em seguida, entre em contato com o [suporte da Braze]({{site.baseurl}}/support_contact).
- Se uma Central de Preferências removida foi usada em mensagens enviadas anteriormente, ela deixará de funcionar nesses e-mails entregues.
{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Etapa 1: Criar uma Central de Preferências de e-mail {#step-1-create-an-email-preference-center}

Crie uma Central de Preferências navegando até **Público** > **Central de Preferências de e-mail**.

Aqui, uma lista de Centrais de Preferências personalizadas será exibida. Selecione **Criar nova** para criar uma nova Central de Preferências ou selecione o nome de uma existente para fazer alterações.


## Etapa 2: Nomear a Central de Preferências de e-mail {#step-2-name-the-email-preference-center}

Os nomes das Centrais de Preferências só podem conter caracteres alfanuméricos, hifens ou underscores. O nome que você fornecer determinará a sintaxe da Liquid tag gerada.

Essa Liquid tag pode ser incluída em qualquer Campaign de e-mail de saída ou etapa do Canvas e direcionará os usuários para a Central de Preferências.


## Etapa 3: Adicionar grupos de inscrições à Central de Preferências {#step-3-add-subscription-groups-to-the-preference-center}

Selecione **Abrir editor** para começar a projetar sua Central de Preferências no editor de arrastar e soltar.

### Definir os grupos de inscrições disponíveis {#define-available-subscription-groups}

Para determinar quais grupos de inscrições devem ser exibidos na Central de Preferências, selecione o botão **+ Add subscription groups** para abrir um modal onde os grupos de inscrições desejados podem ser selecionados. Após selecionar, clique no botão **Add Subscription Groups** para adicioná-los à Central de Preferências.

Você pode configurar ainda mais os grupos de inscrições selecionados clicando no bloco inteligente e ajustando as propriedades do bloco.
- Ajustar a ordem dos grupos de inscrições
- Adicionar ou remover grupos de inscrições adicionais
- Incluir descrições
- Adicionar ou remover uma caixa de seleção **Subscribe to all**, que inscreverá o usuário em todos os grupos de inscrições exibidos neste bloco
- Adicionar ou remover uma caixa de seleção **Unsubscribe from all**, que cancelará a inscrição do usuário de todos os grupos de inscrições exibidos neste bloco


O botão **Unsubscribe from all** na parte inferior do modelo não pode ser removido e fará o [cancelamento global da inscrição]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) do usuário, impedindo-o de receber qualquer mensagem de e-mail.

## Etapa 4: Personalizar a Central de Preferências usando o editor de arrastar e soltar {#step-4-customize-the-preference-center-using-the-drag-and-drop-editor}

### Definir estilos comuns {#set-common-styles}

Você pode definir determinados estilos para serem aplicados em todos os blocos relevantes da sua Central de Preferências na guia **Common Styles**. Os estilos definidos nesta seção são usados em toda a sua mensagem, exceto onde você os substituir para um bloco específico. Para uma experiência de design mais fácil, recomendamos configurar os estilos no nível da página antes de personalizar os estilos no nível do bloco.

![Um exemplo de configurações de estilos comuns para texto, botões e links.]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
Para retornar aos estilos comuns, selecione o botão "X" nas propriedades individuais do bloco. Em seguida, selecione o contêiner da mensagem, o botão "X" da mensagem ou o plano de fundo do editor.
{% endalert %}

## Componentes da Central de Preferências de arrastar e soltar {#drag-and-drop-preference-center-components}

O editor de arrastar e soltar usa dois componentes principais para tornar a composição da Central de Preferências rápida e fácil: linhas e blocos. Todos os blocos devem ser colocados em uma linha.

{% tabs %}
{% tab Linhas %}

Linhas são unidades estruturais que definem a composição horizontal de uma seção da mensagem usando células.

![Opção para selecionar o tipo de linha na sua mensagem.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

Quando uma linha é selecionada, você pode adicionar ou remover o número de colunas necessárias na seção de personalização de colunas para colocar diferentes elementos de conteúdo lado a lado. Você também pode deslizar para ajustar o tamanho das colunas existentes.

![Opções para personalizar as propriedades da coluna, incluindo cor de fundo, estilo da borda, raio da borda e preenchimento.]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

Como prática recomendada, formate as propriedades de linha e coluna antes de formatar quaisquer blocos dentro das linhas. Você pode ajustar o espaçamento e o alinhamento em muitos lugares, então começar pela base torna mais fácil editar conforme avança.

{% endtab %}
{% tab Blocos %}

Blocos representam diferentes tipos de conteúdo que você pode usar na sua mensagem. Arraste um para dentro de um segmento de linha existente, que se ajustará automaticamente à largura da célula.

![Opção para selecionar blocos, incluindo título, parágrafo, botão, imagem e espaçador.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

Cada bloco tem suas próprias configurações, como controle granular de preenchimento. O painel do lado direito alterna automaticamente para um painel de estilo do elemento de conteúdo selecionado. Para saber mais, consulte [Blocos do editor (Central de Preferências)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=preference%20center).

Se você estiver usando o bloco de código personalizado na sua Central de Preferências, os iframes podem não ser gerados no código personalizado quando entregues aos seus usuários.

{% endtab %}
{% endtabs %}

## Etapa 5: Personalizar sua página de confirmação {#step-5-customize-your-confirmation-page}

Não se esqueça de personalizar a página de confirmação! Você pode editar essa página selecionando **Página de confirmação** na parte superior da janela do editor de arrastar e soltar. Essa página será exibida aos usuários após atualizarem suas preferências usando a Central de Preferências. Os mesmos recursos de estilo acima também se aplicam a essa página.

![Um exemplo de página de confirmação para comunicar que as preferências do usuário foram atualizadas.]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## Etapa 6: Pré-visualizar e lançar sua Central de Preferências {#step-6-preview-and-launch-your-preference-center}

Você pode pré-visualizar sua Central de Preferências selecionando a guia **Pré-visualização** dentro do editor. No entanto, a funcionalidade de teste está desativada. Após editar sua Central de Preferências, você pode fechar o editor selecionando o botão **Done**.

Você verá uma pré-visualização tanto da Central de Preferências quanto da página de confirmação. Selecione **Salvar como rascunho** para retornar a essa Central de Preferências mais tarde, ou, se estiver satisfeito, selecione **Launch Preference Center**.

Ao lançar a Central de Preferências, você será solicitado a confirmar o nome, pois ele não pode ser editado após o lançamento. Depois de confirmar o nome, a Central de Preferências será lançada e estará pronta para uso.

## Usando a Central de Preferências {#using-the-preference-center}

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Para inserir um link para a Central de Preferências nos seus e-mails, copie a Liquid tag da Central de Preferências desejada selecionando o ícone **Copiar Liquid**.

![A opção Copiar Liquid na linha de uma Central de Preferências.]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

Adicione a Liquid tag no local desejado do seu e-mail, de forma semelhante a como as [URLs de cancelamento de inscrição]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer#adding-a-custom-unsubscribe-link) são inseridas.

## Tratamento de erros {#handling-errors}

Se ocorrer um erro quando um usuário selecionar **Save** em uma Central de Preferências, a seguinte mensagem de erro padrão será exibida, que não pode ser personalizada ou estilizada no editor. No entanto, a localização das mensagens de erro ainda é suportada nessas páginas.

![Um erro informando "Houve um problema ao salvar suas preferências. Por favor, tente novamente."]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}