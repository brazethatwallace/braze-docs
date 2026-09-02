---
nav_title: "Configuração"
article_title: Configuração do LINE
description: "Este artigo aborda como configurar o canal LINE na Braze, incluindo pré-requisitos e próximas etapas sugeridas."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# Configuração do LINE {#line-setup}

> Este artigo aborda como configurar o canal LINE na Braze, incluindo como configurar usuários, reconciliar IDs de usuários e criar usuários teste do LINE na Braze.

## Pré-requisitos {#prerequisites}

Você precisará do seguinte para integrar o LINE com a Braze:

- [Conta empresarial do LINE](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- Status de conta premium ou verificada (necessário para sincronizar seguidores existentes)
   - Consulte as [diretrizes de conta do LINE](https://terms2.line.me/official_account_guideline_oth)
- [Conta de desenvolvedor do LINE](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [Canal de API de envio de mensagens do LINE](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

O envio de mensagens do LINE pela Braze consome os créditos de mensagem ou de ação da sua conta.

{% alert note %}
**Configurar `native_line_id`**: Você pode configurar `native_line_id` enviando atualizações de usuário para a Braze (por exemplo, com o endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), [importação por CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) ou [Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)). Se o SDK do seu app não tem um campo dedicado para `native_line_id`, envie-o em atualizações de usuário no lado do servidor usando um desses métodos.
{% endalert %}

## Tipos de contas LINE {#types-of-line-accounts}

| Tipo de conta | Descrição |
| --- | --- |
| Conta não verificada | Uma conta não avaliada que pode ser obtida por qualquer pessoa (física ou jurídica). Essa conta é representada por um selo cinza e não aparecerá nos resultados de busca dentro do app LINE. |
| Conta verificada | Uma conta que passou pela análise do LINE Yahoo. Essa conta é representada por um selo azul e aparecerá nos resultados de busca dentro do app LINE.<br><br>Essa conta está disponível apenas para contas baseadas no Japão, Taiwan, Tailândia e Indonésia. |
| Conta premium | Uma conta que passou pela análise do LINE Yahoo. Essa conta é representada por um selo verde e aparecerá nos resultados de busca dentro do app LINE. Esse tipo de conta é concedido automaticamente durante a análise, a critério do LINE. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de contas LINE" }

### Tipo de conta necessário {#required-account-type}

Para sincronizar seguidores na Braze, sua conta LINE precisa ser verificada ou premium. Quando você cria uma conta, o status padrão será não verificada. Você precisará solicitar a verificação da conta.

### Como solicitar uma conta LINE verificada {#applying-for-a-verified-line-account}

{% alert important %}
Contas verificadas estão disponíveis apenas para contas baseadas no Japão, Taiwan, Tailândia e Indonésia.
{% endalert %}

1. Na página **Official Account** do LINE, selecione **Settings**.
2. Em **Information Disclosure Verification Status**, selecione **Request Account Verification**.
3. Insira as informações necessárias.
4. Aguarde uma notificação com os resultados da análise.

## Integrando o LINE {#integrating-line}

Para configurar atualizações consistentes de usuários, importar os LINE IDs de usuários existentes e sincronizá-los com os estados de inscrição do LINE:

1. [Importar ou atualizar usuários LINE existentes conhecidos](#step-1-import-or-update-existing-line-users)
2. [Integrar o canal LINE](#step-2-integrate-line-channel)
3. [Reconciliar IDs de usuários](#step-3-reconcile-user-ids)
4. [Alterar os métodos de atualização de usuários](#step-4-change-your-user-update-methods)
5. [(Opcional) Mesclar perfis de usuários](#step-5-merge-profiles-optional)

{% alert note %}
Você só pode ter uma conta LINE em um único espaço de trabalho. Se você tiver várias contas LINE, recomendamos usar cada uma em um espaço de trabalho diferente.
{% endalert %}

## Etapa 1: Importar ou atualizar usuários LINE existentes {#step-1-import-or-update-existing-line-users}

Esta etapa é necessária se você tiver um usuário LINE existente e identificado, já que a Braze posteriormente obterá automaticamente o estado de inscrição dele e atualizará o perfil de usuário correto. Se você não conciliou previamente os usuários com o LINE ID deles, pule esta etapa.

Você pode importar ou atualizar usuários usando qualquer um dos métodos compatíveis com a Braze, incluindo o endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), [importação por CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) ou [Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Independentemente do método utilizado, atualize o `native_line_id` para fornecer o LINE ID do usuário. Para saber mais sobre o `native_line_id`, consulte [Configuração do usuário](#user-setup).

{% alert note %}
Não especifique o estado do grupo de inscrições — ele será ignorado. O LINE é a fonte oficial do status de inscrição do usuário, que é sincronizado com a Braze por meio da ferramenta de sincronização de inscrições ou atualizações de eventos.
{% endalert %}

## Etapa 2: Integrar o canal LINE {#step-2-integrate-line-channel}

Após a conclusão do processo de integração, a Braze automaticamente importa os seguidores do LINE desse canal para a Braze. Para quaisquer IDs do LINE que já estejam associados a um perfil de usuário da Braze, cada perfil é atualizado com o status "subscribed", e quaisquer IDs do LINE restantes geram usuários anônimos. Além disso, novos seguidores do seu canal LINE terão perfis de usuário não identificados criados quando seguirem o canal.

### Etapa 2.1: Editar configurações de webhook {#step-21-edit-webhook-settings}

1. No LINE, acesse a guia **Messaging API** e edite suas **Webhook settings**:
   - Defina a **Webhook URL** como `https://anna.braze.com/line/events`.
      - A Braze alterará automaticamente isso para uma URL diferente durante a integração, com base no cluster do seu dashboard.
   - Ative **Use webhook** e **Webhook redelivery**. <br><br> ![Página de configurações de webhook para verificar ou editar a URL do webhook, com opções para ativar ou desativar "Use webhook", "Webhook redelivery" e "Error statistics aggregation".]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. Anote as seguintes informações na guia **Providers**:

| Tipo de informação | Localização |
| --- | --- |
| Provider ID | Selecione seu provedor e acesse ***Settings** > **Basic information** |
| Channel ID | Selecione seu provedor e acesse **Channels** > seu canal > **Basic settings** |
| Channel secret | Selecione seu provedor e acesse **Channels** > seu canal > **Basic settings**. |
| Channel access token | Selecione seu provedor e acesse **Channels** > seu canal > **Messaging API**. Se não houver um channel access token, selecione **Issue**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2.1: Editar configurações de webhook" }

{% alert note %}
Você pode atualizar ou rotacionar o channel secret e o channel access token de um canal LINE já integrado acessando **Integrações com Parceiros** > **Parceiros de Tecnologia** > **LINE** e selecionando sua integração.
{% endalert %}

{: start="3"}
3. Acesse sua página **Settings** > **Response settings** e faça o seguinte:
   - Desative **Greeting message**. Isso pode ser feito na Braze disparando com base no follow.
   - Desative **Auto-response messages**. Todas as mensagens disparadas devem ser feitas pela Braze. Isso não impedirá que você envie diretamente pelo console do LINE.
   - Ative **Webhooks**.

![Página de configurações de resposta com opções para definir como sua conta lidará com chats.]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### Etapa 2.2: Gerar grupos de inscrições LINE na Braze {#step-22-generate-line-subscription-groups-in-braze}

A Braze cria um [grupo de inscrições]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#line-subscription-groups) para cada canal LINE que você integrar. Para saber como os grupos de inscrições LINE funcionam, consulte [Grupos de inscrições LINE]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups).

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

1. Acesse a página de parceiros de tecnologia da Braze para LINE e insira as informações que você anotou da guia **Providers** do LINE:
   - Provider ID
   - Channel ID
   - Channel secret
   - Channel access token

Se você quiser adicionar lista de permissões de IP na sua conta LINE, adicione todos os endereços IP listados para seu cluster em [Lista de permissões de IP]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting) à sua lista de permissões.

{% alert important %}
Durante a integração, certifique-se de verificar se o channel secret está correto. Se estiver incorreto, pode haver inconsistências no status de inscrição.
{% endalert %}

![Página de integração de mensagens LINE com seção de integração LINE.]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2. Após a conexão, a Braze gerará automaticamente um grupo de inscrições da Braze para cada integração LINE adicionada com sucesso ao seu espaço de trabalho. <br><br> Quaisquer alterações na sua lista de seguidores (como novos seguidores ou pessoas que deixaram de seguir) serão automaticamente enviadas para a Braze.

![Seção de grupos de inscrições LINE exibindo um grupo de inscrições para o canal "LINE".]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## Etapa 3: Reconciliar IDs de usuário {#step-3-reconcile-user-ids}

Combine os IDs do LINE dos seus usuários com os perfis de usuário existentes na Braze seguindo as etapas em [Reconciliação de IDs de usuário](#user-id-reconciliation).

## Etapa 4: Altere seus métodos de atualização de usuários {#step-4-change-your-user-update-methods}

Supondo que você já tenha um método para fornecer atualizações de usuários à Braze, será necessário atualizá-lo para incluir o novo campo `native_line_id`, de modo que as atualizações de usuários subsequentes enviadas à Braze incluam esse campo.

Perfis de usuário não identificados com um `native_line_id` podem existir na Braze, criados como parte do processo de sincronização do status de inscrição ou quando um novo seguidor começou a seguir seu canal.

Quando um usuário do LINE é identificado no seu aplicativo por meio da [reconciliação de usuários](#user-id-reconciliation) ou outros meios, você pode direcionar um perfil de usuário potencialmente não identificado na Braze usando o endpoint [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify). Todo perfil de usuário não identificado com um `native_line_id` também possui um alias de usuário `line_id` que pode ser usado para direcionar o perfil de usuário a ser identificado.

Aqui está um exemplo de carga útil para `/users/identify` que direciona um perfil de usuário não identificado pelo alias de usuário `line_id`:

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

Se não existir um perfil de usuário para o `external_id` fornecido, ele será adicionado ao perfil de usuário não identificado, tornando-o identificado. Se um perfil de usuário já existir para o `external_id`, todos os atributos que são exclusivos do perfil de usuário não identificado serão copiados para o perfil de usuário conhecido, incluindo `native_line_id` e o status de inscrição do usuário.

Você pode atualizar usuários do LINE que são conhecidos no seu aplicativo por meio do endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), passando seus identificadores externos e `native_line_id`. Se um perfil de usuário não identificado já existir para um usuário e o mesmo `native_line_id` for adicionado a um perfil de usuário diferente por meio de `/users/track`, ele herdará todos os estados de inscrição do perfil de usuário não identificado. No entanto, perfis de usuário duplicados existirão com o mesmo `native_line_id`. Quaisquer atualizações de inscrição subsequentes provenientes de atualizações de eventos atualizarão todos os perfis de acordo.

{% alert note %}
Os estados de inscrição do LINE são rastreados por `native_line_id`, não por `external_id`. Por exemplo, se o perfil de usuário do Usuário B for criado com o mesmo `native_line_id` do Usuário A, mas não com o mesmo `external_id`, o Usuário B herda o status de inscrição do LINE do Usuário A.
{% endalert %}

Aqui está um exemplo de carga útil para `/users/track` que atualiza um perfil de usuário pelo ID externo do usuário para adicionar um `native_line_id`:

{% raw %}
```json
{
   "attributes": [
       {
           "external_id": "known_external_id_from_your_application",
           "native_line_id": "U89f4a626548ccd48482f529a482f138b",
           "other": "attribute"
       }
   ]
}
```
{% endraw %}

## Etapa 5: Mesclar perfis (opcional) {#step-5-merge-profiles-optional}

Conforme descrito anteriormente nesta seção, existe a possibilidade de vários perfis de usuário com o mesmo `native_line_id`. Se seus métodos de atualização criarem perfis de usuário duplicados, você pode mesclar perfis de usuário não identificados com perfis de usuário identificados usando o endpoint `/user/merge`.

Aqui está um exemplo de carga útil para `/users/merge` que direciona um perfil de usuário não identificado pelo alias de usuário `line_id`:

{% raw %}
```json
{
 "merge_updates": [
   {
     "identifier_to_merge": {
       "user_alias": {
         "alias_name": "U89f4a626548ccd48482f529a482f138b",
         "alias_label": "line_id"
       }
     },
     "identifier_to_keep": {
       "external_id": "known_external_id_from_your_application"
     }
   }
 ]
}
```
{% endraw %}

{% alert tip %}
Para saber mais sobre o gerenciamento de usuários duplicados na Braze, consulte [Usuários duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).
{% endalert %}

## Configuração do usuário {#user-setup}

O LINE é a fonte de verdade para os estados de inscrição dos usuários. Mesmo que você tenha o ID do LINE de um usuário (`native_line_id`), se esse usuário não tiver seguido o canal do LINE de onde você está enviando, o LINE não entregará mensagens a ele.

Para ajudar a gerenciar isso, a Braze oferece ferramentas e lógica que dão suporte a uma base de usuários bem integrada, incluindo sincronização de inscrições e atualizações de eventos para quando os usuários seguem e deixam de seguir no LINE.

### Sincronização de inscrições e lógica de eventos {#subscription-syncing-and-event-logic}

Para saber como a ferramenta de sincronização de inscrições e as atualizações de eventos de seguir e deixar de seguir mantêm o status de inscrição do LINE alinhado com a Braze, consulte [Status de inscrição]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#line).

## Reintegrar um canal do LINE em outro espaço de trabalho {#re-integrate-a-line-channel-in-another-workspace}

Para usar um canal do LINE em um espaço de trabalho diferente da Braze:

1. No espaço de trabalho original, arquive o grupo de inscrições desse canal.
2. No espaço de trabalho de destino, integre o canal usando a [Etapa 2: Integrar o canal do LINE](#step-2-integrate-line-channel).

Confirme que você tem a permissão [Gerenciar grupos de inscrições]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) em ambos os espaços de trabalho. Sem permissões em ambos os espaços de trabalho, a integração falhará com um erro indicando que o canal já está conectado.

Para saber como o arquivamento afeta os grupos de inscrições, consulte [Grupos de inscrições do LINE]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups#archive-behavior).

## Casos de uso {#use-cases}

Estes são casos de uso de como os usuários podem ser atualizados após você seguir as etapas de configuração.

### O perfil de usuário existente da Braze já segue o canal LINE {#existing-braze-user-profile-already-follows-line-channel}

1. O perfil de usuário da Braze é atualizado com um atributo `native_line_id`. Seu status de inscrição padrão é `unsubscribed`.
2. A ferramenta de sincronização de inscrições é executada, identifica que o usuário está seguindo o canal LINE e então atualiza o perfil de usuário com o status de inscrição `subscribed`.
3. Se ocorrer qualquer alteração no status de inscrição (como o usuário bloquear, remover dos amigos ou voltar a seguir o canal), a Braze recebe a atualização do LINE e atualiza o perfil de usuário com o `native_line_id` correspondente.

### O perfil de usuário existente bloqueou, removeu dos amigos ou deixou de seguir o canal LINE {#existing-user-profile-has-blocked-unfriended-or-unfollowed-line-channel}

1. O perfil de usuário da Braze é atualizado com um atributo `native_line_id`. Seu status de inscrição padrão é `unsubscribed`.
2. A ferramenta de sincronização de inscrições não identifica que o usuário está seguindo o canal LINE, e o status de inscrição do usuário permanece como `unsubscribed`.
3. Se o usuário seguir o canal posteriormente, a Braze recebe a atualização do LINE e atualiza o perfil de usuário com o status de inscrição `subscribed`.

### A criação do perfil de usuário ocorre após seguir o LINE {#user-profile-creation-occurs-after-line-follow}

1. O canal recebe um novo seguidor no LINE.
2. A Braze cria um perfil de usuário anônimo com o atributo `native_line_id` definido como o ID LINE do seguidor e um alias de usuário `line_id` definido como o ID LINE do seguidor. O perfil tem um status de inscrição `subscribed`.
3. O usuário é identificado como possuidor do ID LINE por meio da [reconciliação de usuários](#user-id-reconciliation).
  - O perfil de usuário anônimo pode ser identificado usando o endpoint [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify). Atualizações subsequentes (por meio do endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), [importação de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) ou [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)) nesse perfil de usuário podem direcionar o usuário pelo `external_id` conhecido.

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

  - Um novo perfil de usuário pode ser criado (por meio do endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), [importação de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) ou [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)) definindo o `native_line_id`. Esse novo perfil herdará o estado do status de inscrição do perfil de usuário anônimo existente. Isso resultará em múltiplos perfis compartilhando o mesmo `native_line_id`. Eles podem ser mesclados a qualquer momento usando o endpoint `/users/merge` no processo descrito na [Etapa 5](#step-5-merge-profiles-optional).

### A criação do perfil de usuário ocorre antes de seguir o LINE {#user-profile-creation-occurs-before-line-follow}

1. Você adquire um novo usuário e envia as informações para a Braze. Um novo perfil de usuário é criado (perfil 1).
2. O usuário segue sua conta LINE.
3. A Braze recebe um evento de seguir e cria um perfil de usuário anônimo (perfil 2).
4. O usuário é identificado como possuidor do ID LINE por meio da [reconciliação de usuários](#user-id-reconciliation).
5. Você atualiza o perfil 1 para definir o atributo `native_line_id`. Esse perfil herda o estado do status de inscrição do perfil 2.
  - Agora existem dois perfis de usuário com o mesmo `native_line_id`. Eles podem ser mesclados a qualquer momento usando o endpoint `/users/merge` no processo descrito na [Etapa 5](#step-5-merge-profiles-optional).

## Reconciliação de ID de usuário {#user-id-reconciliation}

Os IDs do LINE são recebidos automaticamente pela Braze quando um usuário segue seu canal ou quando você usa o fluxo único de "sincronização de seguidores". Os IDs do LINE também são específicos do canal que os usuários seguem, por isso é improvável que os usuários consigam fornecer seus IDs do LINE.

Existem duas formas de combinar um ID do LINE com um perfil de usuário existente na Braze:

- [Login do LINE](#line-login)
- [Vinculação de conta de usuário](#user-account-linking)

### Login do LINE {#line-login}

Este método utiliza logins de redes sociais para a reconciliação. Quando um usuário faz login no seu app, ele tem a opção de usar o [Login do LINE](https://developers.line.biz/en/docs/line-login/overview/) para criar uma conta de usuário ou fazer login.

{% alert note %}
Para obter o ID correto do LINE para cada usuário, configure o Login do LINE no mesmo provedor da sua conta oficial ou canal do LINE integrado à Braze.
{% endalert %}

1. Acesse o console de desenvolvedores do LINE e [solicite permissão para obter os endereços de e-mail dos usuários](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission) que fazem login no seu app pelo Login do LINE.

2. Siga as etapas apropriadas fornecidas pelo LINE para implementar o Login do LINE:<br><br>
  - [Instruções para apps web](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [Instruções para apps nativos](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>Certifique-se de incluir `email` na [configuração de escopo](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes) para solicitações de verificação.

{: start="3"}
3. Use a [chamada de verificação do token de ID](https://developers.line.biz/en/reference/line-login/#verify-id-token) para obter o e-mail do usuário.

4. Salve o ID do LINE do usuário (`native_line_id`) no perfil do usuário com um e-mail correspondente no seu banco de dados, ou crie um novo perfil de usuário com o e-mail e o ID do LINE do usuário.

5. Envie as informações novas ou atualizadas do usuário para a Braze usando o [endpoint `/user/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), [importação de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) ou [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

#### Fluxos de trabalho {#workflows}

##### Seguidor existente usa o Login do LINE {#existing-follower-uses-line-login}

**Cenário:** Um usuário anônimo foi criado durante a sincronização inicial de inscritos ou após a integração por meio de um evento de "seguir".

1. O usuário faz login no seu app usando o Login do LINE.
2. O LINE fornece o e-mail do usuário.
3. Você envia para a Braze o usuário atualizado (o perfil de usuário existente com aquele e-mail para adicionar o ID do LINE) ou atualiza o usuário anônimo com o e-mail.

##### Novo seguidor usa o Login do LINE {#new-follower-uses-line-login}

**Cenário:** Não existe nenhum perfil de usuário na Braze com o ID do LINE do usuário.

1. O usuário faz login no seu app usando o Login do LINE.
2. O LINE fornece o e-mail do usuário.
3. Você pode:
  - Atualizar um perfil de usuário existente com aquele e-mail para incluir também o ID do LINE do usuário.
  - Criar um novo perfil de usuário com o e-mail e o ID do LINE.
4. Quando o usuário segue sua conta oficial do LINE, a Braze recebe um evento de seguir e atualiza o status de inscrição do usuário para `subscribed`.

### Vinculação de conta de usuário {#user-account-linking}

Este método permite que os usuários vinculem sua conta do LINE à conta de usuário do seu app. Você pode então usar Liquid na Braze, como {% raw %}`{{line_id}}`{% endraw %}, para criar uma URL personalizada para o usuário que passa o ID do LINE do usuário de volta para seu website ou app, onde pode ser associado a um usuário conhecido.

1. Crie um Canvas baseado em ação que se baseia em uma mudança de estado de inscrição e é disparado quando um usuário se inscreve no seu canal do LINE.<br>![Canvas que é disparado quando um usuário se inscreve no canal do LINE.]({% image_buster /assets/img/line/account_link_1.png %})
2. Crie uma mensagem incentivando os usuários a fazerem login no seu website ou app, passando o ID do LINE do usuário como parâmetro de consulta (via Liquid), como:

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3. Crie uma mensagem de acompanhamento que entrega o código do cupom.
4. (Opcional) Crie uma Campaign ou Canvas baseado em ação que é disparado quando o usuário do LINE é identificado para enviar ao usuário o código do cupom. <br>![Campaign baseada em ação que é disparada quando o usuário do LINE é identificado.]({% image_buster /assets/img/line/account_link_2.png %})

#### Como funciona {#how-it-works}

Depois que o usuário faz login, uma alteração é feita no seu website ou app para que o ID do usuário seja enviado de volta para a Braze e associado ao ID do LINE que foi passado como parte da URL, com um código de exemplo como:

```javascript
const currentUrl = new URL(window.location.href)
const queryParams = new URLSearchParams(currentUrl.search);
const lineUserId = queryParams.get("line_user_id")

if (user && isLoggedIn && lineUserId) {
  post(
   "https://rest.iad-03.braze.com	/users/identify",
   {
     "aliases_to_identify": [
       {
   "external_id": user.getUserId(),
   "user_alias": {
     "alias_name": lineUserId,
     "alias_label": "line_id"
   }
 }
      ]
    }
  )
  braze.logCustomEvent("identified_line_user_for_promotion");
}
```

#### Fluxos de trabalho

##### Usuário existente segue seu canal do LINE {#existing-user-follows-your-line-channel}

**Cenário:** Um usuário existente na Braze segue seu canal no LINE.

1. O LINE envia à Braze um evento de seguir.
2. A Braze cria um perfil de usuário anônimo com o ID do LINE, o alias de usuário `line_id` e o status do grupo de inscrições do LINE como `subscribed`.
3. O usuário recebe uma mensagem do LINE com um link para seu website e app e faz login. O perfil de usuário agora é conhecido.
4. O perfil de usuário anônimo que foi criado é identificado e é mesclado por meio do [endpoint /users/identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) no perfil de usuário conhecido. O perfil de usuário conhecido agora contém o ID do LINE e tem um status de inscrição `subscribed`.
5. (Opcional) O usuário recebe uma mensagem do LINE com o código do cupom e a Braze registra o envio no perfil de usuário da Braze.

## Criando usuários de teste LINE na Braze {#creating-line-test-users-in-braze}

Você pode testar seu canal LINE antes de configurar a [reconciliação de usuários](#user-id-reconciliation) criando um Canvas ou Campaign do tipo "Quem sou eu".

1. Configure um Canvas que retorne o ID de usuário Braze de um usuário com base em uma palavra-gatilho específica. <br><br>Exemplo de gatilho <br><br>![Gatilho para enviar a Campaign a usuários que enviaram uma mensagem LINE de entrada para um grupo de inscrições específico.]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>Exemplo de mensagem<br><br>![Mensagem LINE exibindo o ID de usuário Braze.]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. Na Braze, você pode usar o ID Braze para buscar usuários específicos e modificá-los conforme necessário.

{% alert important %}
Verifique se o Canvas não tem controle global ou grupos de controle que impeçam os envios.
{% endalert %}