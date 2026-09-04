---
nav_title: Bloco Gerenciar Inscrições
article_title: Bloco Gerenciar Inscrições
description: "Este artigo aborda como adicionar e configurar o bloco de formulário Gerenciar Inscrições em uma landing page da Braze, para que os consumidores possam aceitar e gerenciar seus grupos de inscrições para e-mail, SMS ou WhatsApp."
page_order: 5
---

# Bloco Gerenciar Inscrições {#manage-subscriptions-block}

> Adicione um bloco **Gerenciar Inscrições** a uma landing page para que os usuários possam visualizar, aceitar e atualizar seus grupos de inscrições para e-mail, SMS ou WhatsApp.

O bloco **Gerenciar Inscrições** suporta dois casos de uso principais:

- **[Gerenciar inscrições existentes](#update-existing-subscriptions):** Compartilhe a [Liquid tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) da landing page em uma mensagem de e-mail, SMS, WhatsApp ou outro canal. Quando um usuário identificado abre a página, o bloco preenche automaticamente a caixa de seleção de cada grupo de inscrições com o estado atual de inscrição dele, para que ele possa revisar e atualizar suas preferências.
- **[Capturar novas aceitações](#capture-new-subscribers):** Adicione o bloco a uma landing page de geração de leads, junto com um bloco **Email Capture** ou **Phone Capture**, para que novos visitantes possam escolher a quais grupos de inscrições desejam se juntar ao enviar o formulário.

{% alert important %}
Cada bloco **Gerenciar Inscrições** é para um único canal: [e-mail]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups), [SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states) ou [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states). Para coletar mais de um canal, adicione um bloco para cada. Para consentimento de RCS, use um bloco [Phone Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisitos | Descrição |
| --- | --- |
| Grupos de inscrições para e-mail, SMS ou WhatsApp | Pelo menos um [grupo de inscrições para e-mail]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups), [grupo de inscrições para SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states) ou [grupo de inscrições para WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states) para o canal que você adicionar ao bloco. Crie grupos de e-mail pelo dashboard ou pelos [endpoints de grupo de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups). Os grupos de SMS são provisionados durante a [configuração de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#enable-subscription-groups). Os grupos de WhatsApp são criados quando você [integra o WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) ao seu espaço de trabalho. |
| Permissões de landing page | As mesmas [permissões]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites) necessárias para criar e editar qualquer landing page. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Etapa 1: Adicionar o bloco Gerenciar inscrições {#step-1-add-the-manage-subscriptions-block}

No editor de landing page de arrastar e soltar, acesse a seção **Build** e selecione **Form Blocks**. Arraste **Manage Subscriptions** para uma linha da sua página; ele se ajusta automaticamente à largura da coluna.

O bloco fica vazio até que você adicione grupos de inscrições a ele. Para exibir grupos de mais de um canal, adicione um bloco **Manage Subscriptions** para cada canal.

## Etapa 2: Selecionar o canal e os grupos de inscrições {#step-2-select-the-channel-and-subscription-groups}

Com o bloco **Manage Subscriptions** selecionado, selecione **+ Add subscription groups** no painel **Block properties** à direita. O modal **Add subscription groups** será aberto.

1. Em **Select channel**, escolha **Email**, **SMS** ou **WhatsApp**. Cada bloco aceita apenas um canal. Se um canal já tiver um bloco **Manage Subscriptions** na página, o cartão desse canal ficará desativado e com o rótulo **Added**.
2. Em **Select subscription groups**, selecione os grupos que deseja incluir. O título da lista corresponde ao canal (**Email subscription groups**, **SMS subscription groups** ou **WhatsApp subscription groups**).
3. Selecione **Add selected**.

Cada grupo de inscrições aparece como sua própria caixa de seleção na landing page.

Se você selecionar **SMS** e seu espaço de trabalho ainda não tiver grupos de inscrições para SMS, o modal exibirá **No SMS subscription groups yet**. Conclua a [configuração do grupo de inscrições para SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states) e depois retorne ao bloco.

Se você selecionar **WhatsApp** e seu espaço de trabalho ainda não tiver grupos de inscrições para WhatsApp, o modal exibirá **No WhatsApp subscription groups yet**. Conclua a [configuração do grupo de inscrições para WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states) e depois retorne ao bloco.

{% alert note %}
O bloco **Manage Subscriptions** lista apenas os grupos que você adicionar explicitamente. Adicionar um grupo de inscrições ao bloco não inscreve automaticamente os visitantes nele — o visitante precisa marcar a caixa de seleção do grupo e enviar o formulário.
{% endalert %}

## Etapa 3: Configurar as definições do bloco {#step-3-configure-the-block-settings}

Use o painel **Propriedades do bloco** para ajustar o comportamento e a aparência do bloco.

### Grupos de inscrições {#subscription-groups}

- **Reordenar grupos:** Arraste um grupo de inscrições pela alça para alterar a ordem em que ele aparece no bloco.
- **Adicionar ou remover grupos:** Selecione **+ Adicionar grupos de inscrições** para incluir mais grupos, ou selecione o ícone de exclusão ao lado de um grupo para removê-lo do bloco.

### Incluir descrições {#include-descriptions}

Ative **Incluir descrições** para exibir o texto de descrição de cada grupo de inscrições junto ao nome, oferecendo mais contexto aos visitantes sobre o que estão aceitando. Grupos de e-mail podem incluir uma descrição em Gerenciamento de inscrições. Grupos de SMS e WhatsApp neste bloco não exibem texto de descrição.

### Caixa de seleção "Inscrever-se em todos" {#subscribe-to-all-checkbox}

Ative a configuração **Caixa de seleção "Inscrever-se em todos"** para adicionar uma caixa de seleção extra ao bloco. Quando um visitante a seleciona, todas as caixas de seleção de grupos de inscrições no bloco são marcadas — útil para uma aceitação rápida de todos os grupos listados.

## Atualizar inscrições existentes {#update-existing-subscriptions}

Para permitir que usuários existentes revisem e atualizem suas inscrições de e-mail, SMS ou WhatsApp, compartilhe a landing page usando sua [Liquid tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) em um e-mail, SMS, WhatsApp, etapa do Canvas ou outra mensagem. Quando um usuário abre a página por meio desse link, a Braze o identifica e preenche automaticamente cada caixa de seleção do grupo de inscrições no bloco **Manage Subscriptions** para corresponder ao estado atual de inscrição — de forma semelhante a uma [Central de Preferências de e-mail]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

O usuário pode marcar ou desmarcar caixas de seleção para atualizar suas inscrições e, em seguida, enviar o formulário para salvar as alterações.

{% alert note %}
O preenchimento automático do estado atual de inscrição do usuário no bloco **Manage Subscriptions** está incluído por padrão e não requer o [nível Landing Pages Pro]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers). Isso é diferente do [preenchimento prévio baseado em Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#pre-fill-form-fields) para outros campos de formulário, que requer o Landing Pages Pro.
{% endalert %}

## Capturar novos inscritos {#capture-new-subscribers}

Para coletar novos inscritos, combine o bloco **Manage Subscriptions** com um campo de captura para o canal desejado:

- **E-mail:** Adicione um bloco [Email Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) para que a página capture o endereço de e-mail do visitante junto com as seleções de grupo de inscrições para e-mail.
- **SMS ou WhatsApp:** Adicione um bloco [Phone Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) para que a página capture o número de telefone do visitante junto com as seleções de grupo de inscrições de SMS ou WhatsApp.

Se o visitante não for identificado (por exemplo, se ele acessar a página sem uma Liquid tag de landing page), as caixas de seleção começam desmarcadas. Quando ele enviar o formulário, será inscrito nos grupos de inscrições que selecionou.

## O que saber {#things-to-know}

- **Um canal por bloco:** Você pode adicionar um bloco **Manage Subscriptions** por canal em uma página (um para e-mail, um para SMS e um para WhatsApp).
- **RCS:** Este bloco não lista grupos de inscrições de RCS. Para coletar consentimento para RCS, use um bloco [Phone Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).
- **Experiência de confirmação:** Landing pages com blocos de formulário, incluindo **Manage Subscriptions**, precisam de uma experiência de confirmação após o envio. [Crie uma página de confirmação]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional) e vincule-a ao seu botão **Submit**.
- **Referência de blocos do editor:** Para uma referência completa de cada bloco de landing page e suas propriedades, consulte [Blocos do editor (landing pages)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).