---
nav_title: Bloco Gerenciar Inscrições
article_title: Bloco Gerenciar Inscrições
description: "Este artigo aborda como adicionar e configurar o bloco de formulário Gerenciar Inscrições em uma landing page da Braze, para que os consumidores possam aceitar e gerenciar seus grupos de inscrições para e-mail."
page_order: 5
---

# Bloco Gerenciar Inscrições {#manage-subscriptions-block}

> Adicione um bloco **Gerenciar Inscrições** a uma landing page para que os usuários possam visualizar, aceitar e atualizar seus grupos de inscrições para e-mail.

O bloco **Gerenciar Inscrições** suporta dois casos de uso principais:

- **[Gerenciar inscrições existentes](#update-existing-subscriptions):** Compartilhe a [Liquid tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) da landing page em um e-mail ou mensagem de outro canal. Quando um usuário identificado abre a página, o bloco preenche automaticamente a caixa de seleção de cada grupo de inscrições com o estado atual de inscrição dele, para que ele possa revisar e atualizar suas preferências.
- **[Capturar novas aceitações](#capture-new-subscribers):** Adicione o bloco a uma landing page de geração de leads, junto com um bloco **Email Capture**, para que novos visitantes possam escolher a quais grupos de inscrições desejam se juntar ao enviar o formulário.

{% alert important %}
O bloco **Gerenciar Inscrições** suporta apenas [grupos de inscrições para e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups). Ele não suporta grupos de inscrições de SMS, RCS ou WhatsApp.
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisitos | Descrição |
| --- | --- |
| Grupos de inscrições para e-mail | Pelo menos um [grupo de inscrições para e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups), [criado pelo dashboard]({{site.baseurl}}/user_guide/channels/email/subscriptions#creating-a-subscription-group) ou pelos [endpoints de grupo de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups). |
| Permissões de landing page | As mesmas [permissões]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites) necessárias para criar e editar qualquer landing page. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Etapa 1: Adicionar o bloco Gerenciar inscrições {#step-1-add-the-manage-subscriptions-block}

No editor de landing page de arrastar e soltar, acesse a seção **Build** e selecione **Form Blocks**. Arraste **Manage Subscriptions** para uma linha da sua página; o bloco se ajusta automaticamente à largura da coluna.

O bloco fica vazio até que você adicione grupos de inscrições a ele.

## Etapa 2: Selecionar os grupos de inscrições {#step-2-select-the-subscription-groups}

Com o bloco **Manage Subscriptions** selecionado, selecione **+ Add subscription groups** no painel **Block properties** à direita. Isso abre uma lista dos [grupos de inscrições para e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups) disponíveis no seu espaço de trabalho.

Marque a caixa de seleção ao lado de cada grupo de inscrições que você deseja incluir e confirme sua seleção para adicioná-los ao bloco. Cada grupo de inscrições aparece como sua própria caixa de seleção na landing page.

{% alert note %}
O bloco **Manage Subscriptions** lista apenas os grupos que você adicionar explicitamente. Adicionar um grupo de inscrições ao bloco não inscreve automaticamente os visitantes nele — o visitante precisa marcar a caixa de seleção do grupo e enviar o formulário.
{% endalert %}

## Etapa 3: Configurar as opções do bloco {#step-3-configure-the-block-settings}

Use o painel **Propriedades do bloco** para ajustar o comportamento e a aparência do bloco.

### Grupos de inscrições {#subscription-groups}

- **Reordenar grupos:** Arraste um grupo de inscrições pela alça para alterar a ordem em que ele aparece no bloco.
- **Adicionar ou remover grupos:** Selecione **+ Adicionar grupos de inscrições** para incluir mais grupos, ou selecione o ícone de exclusão ao lado de um grupo para removê-lo do bloco.

### Incluir descrições {#include-descriptions}

Ative **Incluir descrições** para exibir o texto de descrição de cada grupo de inscrições ao lado do nome, oferecendo mais contexto aos visitantes sobre o que estão aceitando.

### Caixa de seleção "Inscrever-se em todos" {#subscribe-to-all-checkbox}

Ative a configuração **Caixa de seleção "Inscrever-se em todos"** para adicionar uma caixa de seleção extra ao bloco. Quando um visitante a seleciona, todas as caixas de seleção de grupos de inscrições no bloco são marcadas — útil para uma aceitação rápida de todos os grupos listados.

## Atualizar inscrições existentes {#update-existing-subscriptions}

Para permitir que usuários existentes revisem e atualizem suas inscrições de e-mail, compartilhe a landing page usando sua [Liquid tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) em um e-mail, etapa do canva ou outra mensagem. Quando um usuário abre a página por meio desse link, a Braze o identifica e preenche automaticamente cada caixa de seleção de grupo de inscrições no bloco **Manage Subscriptions** para corresponder ao estado atual de inscrição dele, de forma semelhante a uma [Central de Preferências de e-mail]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

O usuário pode marcar ou desmarcar as caixas de seleção para atualizar suas inscrições e, em seguida, enviar o formulário para salvar as alterações.

{% alert note %}
O preenchimento automático do estado atual de inscrição do usuário no bloco **Manage Subscriptions** está incluído por padrão e não requer o [plano Landing Pages Pro]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers). Isso é diferente do [preenchimento automático baseado em Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#pre-fill-form-fields) para outros campos de formulário, que requer o Landing Pages Pro.
{% endalert %}

## Capturar novos inscritos {#capture-new-subscribers}

Para coletar novos inscritos, por exemplo em uma landing page de geração de leads, combine o bloco **Manage Subscriptions** com um [bloco de captura de e-mail]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) para que a página capture o endereço de e-mail do consumidor junto com as seleções de grupo de inscrições.

Se o consumidor não estiver identificado (por exemplo, se ele acessar a página sem uma Liquid tag de landing page), as caixas de seleção começam desmarcadas. Quando ele envia o formulário, é inscrito nos grupos de inscrições que selecionou.

## Informações importantes {#things-to-know}

- **Consentimento para SMS, RCS e WhatsApp:** Para coletar o consentimento para esses canais em uma landing page em vez de e-mail, use um [bloco de captura de telefone]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).
- **Experiência de confirmação:** Landing pages com blocos de formulário, incluindo **Manage Subscriptions**, precisam de uma experiência de confirmação após o envio. [Crie uma página de confirmação]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional) e vincule-a ao seu botão **Submit**.
- **Referência dos blocos do editor:** Para uma referência completa de cada bloco de landing page e suas propriedades, consulte [Blocos do editor (landing pages)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).