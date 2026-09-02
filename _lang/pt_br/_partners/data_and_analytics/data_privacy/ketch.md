---
title: Ketch
nav_title: Ketch
description: "Este artigo de referência aborda a integração entre a Braze e a Ketch. A Ketch fornece operações de privacidade simplificadas e controle de dados completo, dinâmico e inteligente."
alias: /partners/ketch
page_type: partner
search_tag: Ketch
---

# Ketch

> [Ketch](https://www.ketch.com) permite que as empresas sejam administradoras responsáveis por seus dados. A Ketch fornece operações de privacidade simplificadas e controle de dados completo, dinâmico e inteligente.

_Esta integração é mantida pela Ketch._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Ketch permite que você controle as preferências de comunicação do cliente na Central de Preferências da Ketch e propague automaticamente essas alterações para a Braze.

{% alert note %}
Procurando orientação sobre como criar grupos de inscrições? Confira nossos artigos para <a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/'>grupos de inscrições por SMS</a> e <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/'>grupos de inscrições por e-mail</a>.
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisitos | Descrição |
|---|---|
| Conta Ketch | Uma conta [Ketch](https://www.ketch.com) com privilégios de administrador é necessária para ativar esta integração. |
| Chave de API or interface de programação do aplicativo (API) da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com as permissões `users.track`, `subscription.status.get`, `subscription.status.set`, `users.delete`, `users.alias.new`, `users.export.ids`, `email.unsubscribe` e `email.blacklist`. <br><br> Ela pode ser criada no dashboard da Braze (**Console de desenvolvedor** > **Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional** > **Criar nova chave de API or interface de programação do aplicativo (API)**). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

### Etapa 1: Configure a conexão com a Braze {#step-1-set-up-the-braze-connection}

1. Na sua [instância do Ketch](https://app.ketch.com), navegue até **Data Systems** e selecione **Braze**. Em seguida, clique em **New Connection**.
2. Dê à sua conexão com a Braze um nome identificável, que será usado para se referir a essa conexão em processos baseados em API or interface de programação do aplicativo (API). Um código também será criado para essa conexão. Esse código deve ser único em todas as conexões.
3. Confirme o mapeamento de identidade dos seus usuários. Por padrão, a Ketch mapeará as identidades dos usuários pelo endereço de e-mail ou pelo `external_id` na Braze.
4. Adicione a chave de API or interface de programação do aplicativo (API) da Braze e forneça o endpoint da API or interface de programação do aplicativo (API). Esse [endpoint da API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics/#endpoints) é baseado na instância da Braze que sua organização utiliza.

### Etapa 2: Configure as preferências de inscrição {#step-2-configure-subscription-preferences}

1. Acesse **Policy Center** > **Subscriptions**. Se você não vir a guia de inscrições em **Policy Center**, certifique-se de que você tem acesso à Central de Preferências de marketing e verifique se possui as permissões de conta corretas para acessar essa parte do produto.
2. Clique em **Create New Subscription** para criar um novo tópico. Cada inscrição terá um nome e um código.
3. Adicione os canais para enviar seus tópicos de inscrição. Cada canal será exibido na Central de Preferências de marketing para seus usuários. Você também pode adicionar os detalhes de como deseja que a Central de Preferências da Ketch orquestre um sinal específico de opt-in ou descadastramento.
4. Selecione a conexão com a Braze que você gostaria de usar para orquestrar os sinais de opt-in e descadastramento.
5. Insira o `subscription_group_id` da Braze para o grupo de inscrições ao qual você deseja enviar as preferências do usuário da Ketch.

![ID do grupo de inscrições da Braze.]({% image_buster /assets/img/ketch/ketch1.png %})

{% alert note %}
Para coletar e orquestrar sinais de opt-in e descadastramento dos usuários, as identidades devem ser configuradas corretamente. A Ketch recomenda configurar o e-mail como o identificador para orquestrar os sinais de preferência do usuário nesta integração.
{% endalert %}


### Etapa 3: Configure as identidades {#step-3-configure-identities}

Um usuário só pode ver a Central de Preferências de marketing quando a Ketch consegue confirmar a identidade de preferência de marketing desse usuário. Se a Ketch não conseguir capturar a identidade do usuário corretamente, a página de preferências de marketing não aparecerá para esse usuário, pois a Ketch não consegue gerenciar suas preferências.

1. Para configurar a identidade de preferência de marketing, acesse a página **Settings** na Ketch e clique em **Identity space**. Você precisará criar um novo espaço de identidade ou editar um existente para atribuí-lo como a identidade de preferência de marketing. Verifique se a tag da Ketch implantada na propriedade captura corretamente esse espaço de identidade.
2. Acesse **Experience Server** > **Properties** e edite a propriedade desejada. Na camada de dados dessa propriedade, ative o espaço de identidade personalizado. Em seguida, configure como a identidade de preferência de marketing é capturada neste site.
3. Depois de configurar o espaço de identidade, teste para ver se a Central de Preferências aparece abrindo-a no site onde a tag da Ketch foi implantada.