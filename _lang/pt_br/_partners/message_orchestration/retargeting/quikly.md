---
nav_title: Quikly
article_title: Quikly
description: "Este artigo de referência descreve a parceria entre a Braze e a Quikly, uma plataforma de marketing de urgência, que permite acelerar as conversões em eventos dentro de uma jornada do cliente da Braze."
alias: /partners/quikly/
page_type: partner
search_tag: Partner

---

# Quikly

> [A Quikly](https://www.quikly.com), uma plataforma de marketing de urgência, usa a psicologia para motivar os consumidores, para que as marcas possam aumentar imediatamente a resposta em torno de suas principais iniciativas de marketing.

_Essa integração é mantida pela Quikly._

## Sobre a integração {#about-the-integration}

A parceria Braze e Quikly permite que você acelere as conversões em eventos dentro de uma jornada do cliente da Braze. A Quikly faz isso usando a psicologia da urgência para motivar os consumidores de forma divertida e instantânea. Por exemplo, as marcas podem usar a Quikly para adquirir imediatamente novos assinantes de e-mail e SMS diretamente na Braze ou para motivar outros objetivos importantes de marketing, como baixar seu app para celular.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Quikly | É necessário ter uma conta de parceiro da marca [Quikly](https://www.quikly.com) para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com as permissões `users.track`, `subscription.status.set`, `users.export.ids` e `subscription.status.get`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | [Sua URL de endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
| Chave de API da Quikly (opcional) | Uma chave de API da Quikly fornecida por seu gerente de sucesso do cliente (somente webhook). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso {#use-cases}

A Quikly permite que as marcas acelerem a aquisição por e-mail ou SMS e motiva os assinantes a fornecer dados primários diretamente na Braze. Você também pode usar a Braze para direcionar os clientes perdidos com uma ativação da Quikly que reativará e reterá esse público. Além disso, os profissionais de marketing podem usar essa integração para incentivar eventos específicos da jornada do cliente com estruturas de recompensas exclusivas.

Por exemplo:
 - Crie antecipação e engajamento ao longo dos dias à medida que os consumidores aceitam a chance de ganhar recompensas incríveis com o [Quikly Hype](https://www.quikly.com/urgency-marketing/platform/product-overview/hype). Os dados primários são automaticamente enviados para a Braze.
 - Acelere a aquisição de novos assinantes de e-mail e SMS usando ofertas exclusivas e em tempo real com base na velocidade de resposta do consumidor, na classificação em relação a outros, aleatoriamente ou antes que o tempo ou as quantidades se esgotem com o [Quikly Swap](https://www.quikly.com/urgency-marketing/platform/product-overview/swap).
 - Motive etapas específicas da jornada do cliente com estruturas de recompensas exclusivas usando webhooks.
 - Aplique atributos ou eventos personalizados ao perfil do usuário ao participar de uma ativação da Quikly.

## Integração {#integration}

Abaixo estão descritas quatro integrações diferentes: aquisição de e-mail, aquisição de SMS, atributos personalizados e webhooks. A integração escolhida dependerá da sua ativação da Quikly e do caso de uso.

{% tabs %}
{% tab Email Acquisition %}

### Aquisição de e-mail {#email-acquisition}

Se suas ativações da Quikly coletarem endereços de e-mail de clientes ou dados de perfil, a única etapa necessária é fornecer à Quikly sua chave da API REST e o endpoint. A Quikly configurará sua conta de marca para passar esses dados para a Braze. Se houver atributos de usuário adicionais que você gostaria de incluir, mencione isso ao fornecer as credenciais da API à Quikly.

Aqui está um esboço de como a Quikly executa esse fluxo de trabalho.
1. Ao participar de uma ativação da Quikly, a Quikly agenda uma pesquisa de usuário usando a [API de exportação]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para ver se existe um usuário com um determinado `email_address`.
2. Registre ou atualize o usuário.
  - Se o usuário existir:
    - Não crie um novo perfil.
    - Se desejar, a Quikly pode registrar um atributo personalizado no perfil do usuário para indicar que o usuário participou da ativação.
  - Se o usuário não existir:
    - A Quikly cria um perfil somente de alias por meio do [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) da Braze, definindo o e-mail do usuário como o alias do usuário para fazer referência a esse usuário no futuro (já que o usuário não terá um ID externo).
    - Se desejar, a Quikly pode registrar eventos personalizados para indicar que esse perfil participou da ativação da Quikly.

{% details /users/track request %}

#### Cabeçalhos da solicitação {#request-headers}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Corpo da solicitação {#request-body}
```
{
  "attributes": [{
    "_update_existing_only": false,
    "user_alias:": {
      "alias_name": "email@example.com",
      "alias_label: "email"
    },
    "email": "email@example.com"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab SMS Acquisition %}

### Inscrições para SMS {#sms-subscriptions}

As ativações da Quikly podem coletar números de telefones celulares diretamente dos clientes e iniciar uma nova inscrição por SMS. Para ativar essa integração, forneça ao gerente de sucesso do cliente da Quikly o `subscription_group_id`. É possível acessar o `subscription_group_id` de um grupo de inscrições navegando até a página **Grupo de inscrições**.

A Quikly realizará uma pesquisa de inscrição usando o número de telefone do cliente e o creditará automaticamente na ativação se já existir uma inscrição por SMS. Caso contrário, uma nova inscrição será iniciada e, depois que o status da inscrição for verificado, o cliente receberá o crédito.

Aqui está o fluxo de trabalho completo quando um cliente fornece seu número de celular e consentimento por meio da Quikly:
1. A Quikly realiza uma pesquisa de inscrição usando o [status do grupo de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) para ver se um determinado `phone` está inscrito em um `subscription_group_id`. Se houver uma inscrição, credite o usuário na ativação da Quikly. Nenhuma ação adicional é necessária.
2. A Quikly realiza uma pesquisa de usuário usando o [endpoint Exportar perfil de usuário por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para ver se existe um perfil de usuário com um determinado `email_address`. Se não houver nenhum usuário, crie um perfil somente de alias por meio do [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) da Braze, definindo o e-mail do usuário como o alias do usuário para fazer referência a esse usuário no futuro (já que o usuário não terá um ID externo).
3. Atualize o status da inscrição usando o [endpoint Atualizar status do grupo de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).

Para dar suporte aos fluxos de trabalho de inscrição por SMS de aceitação dupla existentes, a Quikly pode enviar um evento personalizado para a Braze em vez do fluxo de trabalho acima. Nesse caso, em vez de atualizar o status da inscrição diretamente, o [evento personalizado dispara o processo de dupla aceitação]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in/), e o status da inscrição é monitorado periodicamente para verificar se o usuário fez a aceitação total antes de creditá-lo na ativação da Quikly.

{% alert important %}
A Braze aconselha que, ao criar novos usuários por meio do endpoint `/users/track`, deve haver uma postergação de cerca de 2 minutos antes de adicionar usuários ao grupo de inscrições relevante para dar tempo à Braze de criar completamente o perfil do usuário.
{% endalert %}

{% details Detailed /subscription/status/set request %}
#### Cabeçalhos da solicitação
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Corpo da solicitação
```
{
  "subscription_group_id": "the-id-of-the-subscription-group",
    "subscription_status": "subscribed",
    "phone": "+13135551212"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab Custom Attributes %}
### Atributos personalizados {#custom-attributes}

Dependendo da sua implementação da Braze, você pode querer que os eventos dentro da ativação da Quikly passem em cascata pela Braze para processamento adicional. Por exemplo, você pode querer aplicar um atributo personalizado de usuário com base no nível ou incentivo alcançado na ativação da Quikly, permitindo que você exiba o cartão de conteúdo relevante quando eles abrirem o app ou acessarem seu site. A Quikly trabalhará diretamente com você para implementar essas integrações.

{% endtab %}
{% tab Webhooks %}
### Webhooks
Use webhooks para disparar incentivos para eventos específicos na jornada do cliente. Por exemplo, se você tiver um evento Braze para quando um usuário faz login no seu app, ativa notificações por push ou usa o localizador de lojas, você pode usar um webhook para disparar uma oferta personalizada para esse usuário com base na configuração de uma ativação específica da Quikly. Exemplos de táticas incluem recompensar os primeiros X usuários que realizarem uma ação (como fazer login no seu app) com uma oferta personalizada ou fornecer uma oferta que diminui de valor à medida que o tempo passa para motivar uma resposta imediata.

### Criar um webhook da Quikly na Braze {#create-a-quikly-webhook-in-braze}

Para criar um modelo de webhook da Quikly para futuras Campaigns ou Canvas, navegue até **Conteúdo** > **Webhook** na plataforma Braze. Em seguida, selecione **Criar modelo de webhook**.

Se quiser criar uma Campaign única de webhook da Quikly ou usar um modelo existente, selecione **Webhook** na Braze ao criar uma nova Campaign.

Selecione **Blank Template** e insira o seguinte para a URL do webhook e o corpo da solicitação:
- **Webhook URL**: https://api.quikly.com/webhook/braze
- **Request Body**: pares de chave/valor JSON

#### Cabeçalhos de solicitação e método {#request-headers-and-method}

A Quikly exige um `HTTP Header` para autorização.

- **HTTP Method**: POST
- **Request Header**:
  - **Authorization**: Bearer [PARTNER_AUTHORIZATION_HEADER]
  - **Content-Type**: application/json

#### Corpo da solicitação

Selecione ***JSON key/value pairs*** e adicione os seguintes pares:
{% raw %}
```
"q_scope": "your-activations-scope-id"
"event": "your-event-identifier"
"email": {{${email_address}}
```
{% endraw %}

### Pré-visualize sua solicitação {#preview-your-request}

Pré-visualize a solicitação no painel **Preview** ou navegue até a guia `Test`, onde é possível selecionar um usuário aleatório, um usuário existente ou personalizar o seu próprio para testar o webhook.

{% alert important %}
Lembre-se de salvar seu modelo antes de sair da página! <br>Os modelos de webhook atualizados podem ser encontrados na lista **Modelos de webhooks salvos** ao criar uma nova [Campaign de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}

{% endtab %}
{% endtabs %}

## Suporte {#support}
Entre em contato com o gerente de sucesso do cliente da Quikly em caso de dúvidas.