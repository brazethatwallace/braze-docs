---
nav_title: Salesforce Sales Cloud
article_title: Gerencie leads com o Salesforce Sales Cloud
page_order: 3
page_type: reference
description: "Saiba como usar os webhooks da Braze para criar e atualizar leads no Salesforce Sales Cloud por meio do endpoint Salesforce sobjects/Lead."
---

# Gerencie leads com o Salesforce Sales Cloud {#manage-leads-with-salesforce-sales-cloud}

> A [Salesforce](https://www.salesforce.com/) é uma das principais plataformas de gestão de relacionamento com o cliente (CRM) baseadas em nuvem do mundo, projetada para ajudar as empresas a gerenciar todo o processo de vendas, incluindo geração de leads, rastreamento de oportunidades e gerenciamento de contas.<br><br>Esta página demonstra como usar os webhooks da Braze para criar e atualizar leads no Salesforce Sales Cloud por meio de uma integração enviada pela comunidade.

{% alert important %}
Essa é uma integração enviada pela comunidade e não é diretamente suportada pela Braze. Somente os modelos oficiais de webhook fornecidos pela Braze são compatíveis com a Braze.
{% endalert %}

## Como funciona {#how-it-works}

A integração entre a Braze e o Salesforce Sales Cloud usa webhooks da Braze para criar e atualizar leads no Salesforce Sales Cloud por meio do endpoint [sobjects/Lead](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.html) da Salesforce.

Atualmente, a Braze oferece duas integrações com o Salesforce Sales Cloud para os seguintes casos de uso:
1. [Criação de um lead no Salesforce Sales Cloud](#creating-lead)
2. [Atualização de um lead no Salesforce Sales Cloud](#updating-lead)

{% alert note %}
Essa integração serve exclusivamente para atualizar o Salesforce a partir da Braze como parte de seus esforços de aquisição e nutrição de leads. Para sincronizar dados do Salesforce de volta para a Braze, confira o [modelo de dados B2B]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models) ou entre em contato com um de nossos [parceiros de tecnologia]({{site.baseurl}}/partners/home).
{% endalert %}

## Pré-requisitos {#prerequisites}

Antes de prosseguir com essa integração, o Suporte da Salesforce precisa conceder a você a capacidade de criar apps conectados. Você pode solicitar isso enviando uma [solicitação de suporte da Salesforce](https://help.salesforce.com/s/articleView?id=005167035&type=1).

Depois que o Suporte da Salesforce conceder a você a capacidade de criar um app conectado no Salesforce Sales Cloud, siga as etapas da documentação da Salesforce: [Configure a Connected App for the OAuth 2.0 Client Credentials Flow](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5).

Ao definir as configurações de OAuth necessárias para o app conectado, mantenha todas as configurações de OAuth com seus valores e seleções padrão, exceto as seguintes:
1. Selecione **Enable for device flow**. Você pode deixar o **Callback URL** em branco, pois o padrão será um espaço reservado.
2. Para os **OAuth Scopes** selecionados, adicione **Manage user data via APIs (api)**.
3. Selecione **Enable Client Credentials Flow**.

## Criação de um lead no Salesforce Sales Cloud {#creating-lead}

Como sua plataforma de engajamento com clientes, a Braze pode gerar novos leads com base nos fluxos de usuários, como o preenchimento de um formulário em uma landing page. Quando isso acontece, você pode usar um webhook da Braze para o Salesforce Sales Cloud para criar um lead correspondente no Salesforce.

### Etapa 1: Colete seu `client_id` e `client_secret` {#step-1-collect-your-client_id-and-client_secret}

1. No Salesforce, acesse **Platform Tools** > **Apps** > **App Manager**.
2. Encontre seu Braze App recém-criado e selecione **View**.
3. Em **Consumer Key and Secret**, selecione **Manage Consumer Details**.
4. Na página resultante, anote sua **Consumer Key** e **Consumer Secret**. A **Consumer Key** é seu `client_id`, e o **Consumer Secret** é seu `client_secret`.

### Etapa 2: Configure seu modelo de webhook {#step-2-set-up-your-webhook-template}

Use modelos para reutilizar rapidamente este webhook na plataforma Braze.

1. Na Braze, acesse **Modelos**, selecione **Modelos de webhook** e, em seguida, selecione **+ Criar modelo de webhook**.
2. Forneça um nome para o modelo, como "Salesforce Sales Cloud > Criar lead".
3. Na guia **Redigir**, insira os seguintes detalhes:

#### Redigir webhook {#compose-webhook}

| Campo | Informações |
| --- | --- |
| URL do webhook | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/`{% endraw %} |
| Método HTTP | `POST` |
| Corpo da solicitação | Pares de chave-valor JSON |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Redigir webhook" }

#### Valores-chave da propriedade do corpo {#body-property-key-values}

Selecione **+ Add New Body Property** para cada um dos pares de chave/valor que você deseja mapear da Braze para o Salesforce. Você pode mapear qualquer campo que desejar, portanto, a tabela a seguir é apenas um exemplo.

| Chave | Valor |
| --- | --- |
| firstName | {% raw %}`{{${first_name}}}`{% endraw %} |
| lastName | {% raw %}`{{${last_name}}}`{% endraw %} |
| email | {% raw %}`{{${email_address}}}`{% endraw %} |
| company | {% raw %}`{{custom_attribute.${company}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Valores-chave da propriedade do corpo" }

#### Cabeçalhos da solicitação {#request-headers}

Selecione **+ Add New Header** para cada um dos seguintes cabeçalhos de solicitação.

| Chave | Valor |
| --- | --- |
| Authorization | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cabeçalhos da solicitação" }

{: start="4" }
4. Selecione **Salvar modelo**.

![Um modelo de webhook preenchido para criar um lead.]({% image_buster /assets/img/b2b/create_lead_webhook.png %}){: style="max-width:70%;"}

## Atualização de um lead no Salesforce Sales Cloud {#updating-lead}

Para configurar um webhook da Braze para o Salesforce Sales Cloud que atualiza leads no Salesforce, você precisa de um identificador comum entre o Salesforce Sales Cloud e a Braze. O exemplo na seção a seguir usa o `lead_id` do Salesforce como o `external_id` da Braze, mas você também pode fazer isso usando um `user_alias`. Para mais detalhes, consulte [Dados B2B]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models).

Este exemplo demonstra especificamente como atualizar o estágio de um lead para "MQL" (Marketing Qualified Lead) depois que ele ultrapassa um determinado limite de pontuação. Essa é uma parte essencial do nosso caso de uso de [fluxo de trabalho de pontuação de leads B2B]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring).

### Etapa 1: Colete seu `client_id` e `client_secret`

1. No Salesforce, acesse **Platform Tools** > **Apps** > **App Manager**.
2. Encontre seu Braze App recém-criado e selecione **View**.
3. Em **Consumer Key and Secret**, selecione **Manage Consumer Details**.
4. Na página resultante, anote sua **Consumer Key** e **Consumer Secret**.
    - A **Consumer Key** é seu `client_id`, e o **Consumer Secret** é seu `client_secret`.

### Etapa 2: Configure seu modelo de webhook

1. Na Braze, acesse **Modelos**, selecione **Modelos de webhook** e, em seguida, selecione **+ Criar modelo de webhook**.
2. Forneça um nome para o modelo, como "Salesforce Sales Cloud > Atualizar lead para MQL".
3. Na guia **Redigir**, insira os seguintes detalhes:

#### Redigir webhook

| Campo | Informações |
| --- | --- |
| URL do webhook | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} |
| Método HTTP | `PATCH` |
| Corpo da solicitação | Pares de chave-valor JSON |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Redigir webhook" }

#### Valores-chave da propriedade do corpo

Selecione **+ Add New Body Property** para o seguinte par de chave/valor. Note que `Lead_Stage__c` é um nome de exemplo. O campo personalizado que você usa para rastrear MQLs no Salesforce pode ter um nome diferente, portanto, certifique-se de que eles correspondam.

| Chave | Valor |
| --- | --- |
| `Lead_Stage__c` | `MQL` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Valores-chave da propriedade do corpo" }

#### Cabeçalhos da solicitação

Selecione **+ Add New Header** para cada um dos seguintes cabeçalhos de solicitação.

| Chave | Valor |
| --- | --- |
| Authorization | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cabeçalhos da solicitação" }

{: start="4"}
4. Selecione **Salvar modelo**.

![Um modelo de webhook preenchido para atualizar um lead.]({% image_buster /assets/img/b2b/update_lead_webhook.png %}){: style="max-width:70%;"}

## Uso desses webhooks em um fluxo de trabalho operacional {#using-these-webhooks-in-an-operational-workflow}

Você pode adicionar rapidamente seus modelos aos seus fluxos de trabalho operacionais na Braze, como:

1. Parte de uma [campanha de novo lead](#new-lead) que cria um lead no Salesforce
2. Parte de um [Canvas de pontuação de leads](#lead-scoring) que atualiza os usuários que ultrapassaram seu limite de MQL para "MQL" e que atualiza o Salesforce Sales Cloud com as mesmas informações

### Campanha de novo lead {#new-lead}

Para criar um lead no Salesforce quando um usuário fornece seu endereço de e-mail, você pode criar uma campanha que use o modelo de webhook "Atualizar lead" e dispare quando um usuário adicionar seu endereço de e-mail (por exemplo, preencher um formulário da web).

![Etapa 2 da criação de uma campanha baseada em ação com a ação-gatilho "Adicionar um endereço de e-mail".]({% image_buster /assets/img/b2b/salesforce_create_campaign.png %}){: style="max-width:70%;"}

### Canvas de pontuação de leads para ultrapassar o limite de Marketing Qualified Lead (MQL) {#lead-scoring}

Esse webhook é abordado no caso de uso de [pontuação de leads]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring#lead-handoff), mas você também pode verificar MQLs e atualizar diretamente o Salesforce dentro do Canvas de pontuação de leads (em vez de criar uma campanha de webhook separada):

Adicione uma etapa subsequente à sua atualização de usuário para verificar se um usuário ultrapassou o limite de MQL definido. Se tiver ultrapassado, atualize o status do usuário para "MQL" e, em seguida, atualize o Salesforce com o mesmo status "MQL" usando esse modelo de webhook. O Salesforce cuida do resto, encaminhando esse lead para as equipes de vendas apropriadas usando suas regras de roteamento de leads definidas.

#### Adição da etapa do Canvas para verificar os usuários que ultrapassaram o limite de MQL {#adding-canvas-step-to-check-for-users-who-passed-the-mql-threshold}

1. Adicione uma etapa de **jornada do público** com dois grupos: "MQL Threshold" e "Restante do público".
2. No grupo "MQL Threshold", procure todos os usuários que atualmente não tenham um status de "MQL" (por exemplo, `lead_stage` é igual a "Lead"), mas que tenham uma pontuação de lead acima do limite definido (por exemplo, `lead_score` maior que 50). Em caso afirmativo, eles avançam para a próxima etapa; em caso negativo, saem.

![O grupo de jornada do público "MQL Threshold" com filtros para `lead_stage` igual a "Lead" e `lead_score` maior que "50".]({% image_buster /assets/img/b2b/salesforce_check_mql.png %}){: style="max-width:70%;"}

{: start="3" }
3. Adicione uma etapa de **Atualização de usuário** que atualize o valor do atributo `lead_stage` do usuário para "MQL".

![A etapa de Atualização de usuário "Update to MQL" que atualiza o atributo `lead_stage` para ter o valor "MQL".]({% image_buster /assets/img/b2b/salesforce_update_mql.png %}){: style="max-width:70%;"}

{: start="4" }
4. Adicione uma etapa de webhook que atualize o Salesforce com o novo estágio de MQL.

![A etapa do webhook "Update Salesforce" com os detalhes preenchidos.]({% image_buster /assets/img/b2b/salesforce_webhook.png %}){: style="max-width:70%;"}

Agora seu Canvas Flow atualizará os usuários que ultrapassaram seu limite de MQL!

![Uma etapa de atualização de usuário do Canvas que verifica se um usuário ultrapassa o limite de MQL e, se ultrapassar, atualiza o Salesforce.]({% image_buster /assets/img/b2b/salesforce_canvas.png %}){: style="max-width:50%;"}

## Solução de problemas {#troubleshooting}

Esses fluxos de trabalho têm capacidade limitada de depuração no Salesforce, portanto, recomendamos consultar o [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log#message-activity-log) da Braze para descobrir por que um webhook falhou e se ocorreu algum erro.

Por exemplo, um erro causado por uma URL inválida usada para recuperação de token OAuth seria exibido como `https://[insert_instance_name].my.salesforce.com/services/oauth2/token is not a valid URL`.

![Um corpo de resposta de erro informando que a URL não é válida.]({% image_buster /assets/img/b2b/error_message_invalid_url.png %})