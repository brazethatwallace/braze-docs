---
nav_title: Modelos de webhook
article_title: Modelos de webhook
page_order: 5
tool:
  - Templates
channel:
  - webhooks
description: "Saiba como criar e personalizar modelos de webhook para uso posterior na plataforma Braze."

---

# Criar um modelo de webhook {#create-a-webhook-template}

> À medida que você cria e personaliza seus webhooks, pode criar e aproveitar modelos de webhook para uso posterior na plataforma Braze. Dessa forma, você pode criar de maneira consistente uma variedade de webhooks em suas diferentes Campaigns.

## Etapa 1: Acessar o editor de modelos de webhook {#step-1-go-to-the-webhook-template-editor}

No dashboard da Braze, acesse **Conteúdo** > **Webhook**.

![A página "Modelos de webhook" com modelos de webhook pré-projetados e salvos.]({% image_buster /assets/img_archive/webhook_template_campaign.png %})

## Etapa 2: Escolher seu modelo {#step-2-choose-your-template}

A partir daqui, você pode optar por criar um novo modelo, usar um dos modelos de webhook pré-projetados ou editar um modelo existente.

Por exemplo, se você estiver usando o [LINE]({{site.baseurl}}/user_guide/channels/line) como canal de envio de mensagens, pode configurar vários webhooks usando os modelos pré-projetados para **LINE Carousel** ou **LINE Image**.

## Etapa 3: Preencher os detalhes do modelo {#step-3-fill-out-template-details}

1. Dê ao seu modelo de webhook um nome exclusivo.
2. (Opcional) Adicione uma descrição do modelo para explicar como ele deve ser usado.
3. Adicione [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) conforme necessário para ajudar a encontrar e filtrar seu modelo.

## Etapa 4: Criar seu modelo {#step-4-build-your-template}

1. Insira a URL do webhook.
2. Selecione o método HTTP.
3. Adicione um corpo de solicitação. Pode ser **JSON Key/Value Pairs** ou **Raw Text**.
4. (Opcional) Adicione um cabeçalho de solicitação. Isso pode ser exigido pelo destino do seu webhook.

![A guia "Redigir" ao criar um modelo de webhook. Os campos disponíveis são URL do webhook, método HTTP, corpo da solicitação e cabeçalhos da solicitação. Você também pode adicionar idiomas.]({% image_buster /assets/img_archive/Webhook_template_test.png %}){: style="max-width:90%"}

## Etapa 5: Testar seu modelo {#step-5-test-your-template}

Para ver como seu webhook ficará antes de enviá-lo aos seus usuários, você pode enviar um webhook de teste usando a guia **Test**. Aqui, você pode selecionar a pré-visualização da mensagem como um usuário aleatório, usuário existente ou usuário personalizado.

## Etapa 6: Salvar seu modelo {#step-6-save-your-template}

Certifique-se de salvar seu modelo selecionando **Save Template**. Agora você está pronto para usar esse modelo em qualquer Campaign que escolher.

{% alert note %}
As edições feitas em um modelo existente não são refletidas em Campaigns que foram criadas usando versões anteriores desse modelo.
{% endalert %}

## Gerenciando seus modelos {#managing-your-templates}

Você pode [duplicar e arquivar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates) modelos de webhook para ajudar a organizar e gerenciar melhor sua lista de modelos.