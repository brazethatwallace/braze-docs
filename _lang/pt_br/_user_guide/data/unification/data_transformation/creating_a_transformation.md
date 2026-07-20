---
nav_title: Criar uma transformação
article_title: Criar uma transformação
page_order: 1
page_type: reference
description: "Este artigo de referência fornece etapas para criar uma transformação usando a Transformação de Dados da Braze."
---

# Criar uma transformação {#create-a-transformation}

> A Transformação de Dados da Braze permite que você crie e gerencie integrações de webhook para automatizar o fluxo de dados de plataformas externas para a Braze. Essas integrações de webhook podem então alimentar casos de uso de marketing ainda mais sofisticados. Você pode construir sua Transformação de Dados a partir do código padrão ou usando nossa biblioteca de modelos dedicada para ajudar você a começar com certas plataformas externas.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Autenticação de dois fatores ou SSO | Você deve ter a [autenticação de dois fatores]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#two-factor-authentication-2fa) (2FA) ou o [login único]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#single-sign-on-sso-authentication) (SSO) ativado para sua conta. |
| Permissões corretas | Você deve ser um administrador de conta ou um administrador de espaço de trabalho, ou ter permissões de usuário para "Gerenciar Transformações". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Etapa 1: Identificar uma plataforma de origem {#step-1-identify-a-source-platform}

Identifique uma plataforma externa que você deseja conectar à Braze e verifique se a plataforma aceita webhooks. Essas configurações às vezes são chamadas de "notificações de API" ou "solicitações de serviço da web".

O seguinte é um exemplo de [webhook do Typeform](https://www.typeform.com/help/a/webhooks-360029573471/), que é configurável ao fazer login na plataforma deles:

![Um exemplo de carga útil de webhook do Typeform nas configurações da plataforma Typeform.]({% image_buster /assets/img/data_transformation/data_transformation8.png %})

## Etapa 2: Criar uma transformação {#step-2-create-a-transformation}

{% multi_lang_include data_activation/create_transformation.md location="default" %}

## Etapa 3: Enviar um webhook de teste (recomendado) {#step-3-send-a-test-webhook-recommended}

Esta etapa é opcional, mas recomendamos enviar um webhook de teste da sua plataforma de origem para sua transformação recém-criada.

1. Copie a URL da sua transformação.
2. Na sua plataforma de origem, encontre a funcionalidade de "Enviar Teste" para que ela gere um webhook de amostra para enviar para essa URL.
- Se a sua plataforma de origem solicitar um tipo de solicitação, selecione **POST**.
- Se a sua plataforma de origem fornecer opções de autenticação, selecione **No authentication**.
- Se a sua plataforma de origem pedir segredos, selecione **No secrets**.
3. Atualize sua página no dashboard da Braze para ver se o webhook foi recebido. Se tiver sido recebido, você deverá ver uma carga útil de webhook em **Most recent webhook**.

Aqui está como fica para o Typeform:

![Exemplo de código de Transformação de Dados que mapeia o webhook para perfis de usuários da Braze.]({% image_buster /assets/img/data_transformation/data_transformation11.png %})

{% alert note %}
A Transformação de Dados da Braze pode ainda não oferecer suporte a plataformas externas que exigem verificação ou autenticação especial para webhooks. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="webhook authentication for external platforms" %}
{% endalert %}

## Etapa 4: Escrever o código de transformação {#step-4-write-transformation-code}

Se você tem pouca ou nenhuma experiência com código JavaScript ou prefere instruções mais detalhadas, siga a guia **Iniciante - POST: Rastrear usuários** ou **Iniciante - PUT: Atualizar vários itens do catálogo** para escrever seu código de transformação.

Se você é um desenvolvedor ou tem experiência significativa com código JavaScript, siga a guia **Avançado - POST: Rastrear usuários** para instruções de alto nível sobre como escrever seu código de transformação.

{% alert tip %}
Para gerar código de transformação com IA, escolha **Code with Operator** no editor de código de transformação. Para usar isso, um webhook deve ser enviado para sua transformação. Para começar a partir de um modelo pré-construído, escolha **Insert Template**. Para exemplos de prompts, consulte [Gerar código de transformação de dados]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-data-transformation-code).

**Code with Operator** só está disponível se o Operator estiver ativado para sua conta. Se você não vir essa opção, entre em contato com seu gerente de conta.
{% endalert %}

{% tabs %}
{% tab Iniciante - Rastrear usuários %}

Aqui, escreva o código de transformação para definir como mapear vários valores do webhook para os perfis de usuário da Braze.

1. As novas transformações têm esse modelo padrão na seção **Transformation Code**:

```java
// Here, we will define a variable, "brazecall", to build up a `/users/track` request
// Everything from the incoming webhook is accessible via the special variable "payload"
// So you can template in desired values in your `/users/track` request with dot notation, such as payload.x.y.z

let brazecall = {
  "attributes": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "attribute_1": payload.attribute_1
    }
  ],
  "events": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "name": payload.event_1,
      "time": new Date(),
      "properties": {
        "property_1": payload.event_1.property_1
      }
    }
  ],
  "purchases": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "product_id": payload.product_id,
      "currency": payload.currency,
      "price": payload.price,
      "quantity": payload.quantity,
      "time": payload.timestamp,
      "properties": {
        "property_1": payload.purchase_1.property_1
      }
    }
  ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2. Para incluir atributos personalizados, eventos personalizados e compras em suas chamadas de transformação, pule para a etapa 3. Caso contrário, exclua as seções que você não precisa.<br><br>
3. Cada atributo, evento e objeto de compra requer um identificador de usuário, seja um `external_id`, `user_alias`, `braze_id`, `email` ou `phone`. Encontre o identificador do usuário na carga útil do webhook recebido e modele esse valor no seu código de transformação por meio de uma linha de carga útil. Use a notação de ponto para acessar as propriedades do objeto de carga útil. <br><br>
4. Encontre os valores do webhook que você gostaria de representar como atributos, eventos ou compras, e modele esses valores em seu código de transformação por meio de uma linha de carga útil. Use a notação de ponto para acessar as propriedades do objeto de carga útil.<br><br>
5. Para cada atributo, evento e objeto de compra, examine o valor `_update_existing_only`. Defina como `false` se você quiser que a transformação crie um novo usuário que pode não existir. Deixe como `true` para atualizar apenas perfis existentes.<br><br>
6. Clique em **Validate** para retornar uma prévia da saída do seu código e verificar se é uma solicitação `/users/track` aceitável.<br><br>
7. Ative sua transformação. Para obter ajuda adicional com seu código antes de ativá-lo, entre em contato com seu gerente de conta da Braze.<br><br>
7. Faça com que sua plataforma de origem comece a enviar webhooks. Seu código de transformação será executado para cada webhook recebido, e os perfis dos usuários começarão a ser atualizados.

Sua integração de webhook está completa!

{% endtab %}
{% tab Iniciante - Atualizar itens do catálogo %}

Aqui, você pode escrever código de transformação para definir como deseja mapear vários valores de webhook para atualizações de itens do catálogo da Braze.

1. Novas transformações incluirão este modelo padrão na seção **Transformation Code**:

```java
// This is a default template that you can use as a starting point
// Feel free to delete this entirely to start from scratch, or to edit specific components

// First, this code defines a variable, "brazecall", to build a PUT /catalogs/{catalog_name}/items request
// Everything from the incoming webhook is accessible via the special variable "payload"
// As such, you can template in desired values in your request with JS dot notation, such as payload.x.y.z

let brazecall = {
  // For Braze Data Transformation to update Catalog items, the special variable "catalog_name" is required
  // This variable is used to specify the catalog name which would otherwise go in the request URL
  "catalog_name": "catalog_name",

  // After defining "catalog name", construct the Update Multiple Catalog Items request as usual below
  // Documentation for the destination endpoint: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/
  "items": [
    {
      "id": payload.item_id_1,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_2,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_3,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    }
  ]
};

// After the request body is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2. As transformações para destinos `/catalogs` requerem um `catalog_name` para definir o catálogo específico a ser atualizado. Você pode codificar esse campo diretamente ou modelar o campo com um campo de webhook por meio de uma linha de carga útil. Use a notação de ponto para acessar as propriedades do objeto de carga útil.<br><br>
3. Defina quais itens você gostaria de atualizar no catálogo com os campos `id` na matriz de itens. Você pode codificar esses campos diretamente ou modelar em um campo de webhook por meio de uma linha de carga útil. <br><br> Lembre-se de que `catalog_column` é um valor de espaço reservado. Certifique-se de que os objetos de item contenham apenas campos que existam no catálogo.<br><br>
4. Selecione **Validate** para retornar uma prévia da saída de seu código e verificar se é uma solicitação aceitável para o [endpoint Atualizar vários itens de catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items).<br><br>
5. Ative sua transformação. Para obter ajuda adicional com seu código antes de ativá-lo, entre em contato com seu gerente de conta da Braze.<br><br>
6. Certifique-se de verificar se sua plataforma de origem possui uma configuração para começar a enviar webhooks. Seu código de transformação será executado para cada webhook recebido, e os itens do catálogo começarão a ser atualizados.

Sua integração de webhook está completa!

{% endtab %}
{% tab Avançado - Rastrear usuários %}

Nesta etapa, você transformará a carga útil do webhook da plataforma de origem em um valor de retorno de objeto JavaScript. Esse valor de retorno deve seguir o formato do corpo da solicitação do endpoint `/users/track`:

- O código de transformação é aceito na linguagem de programação JavaScript. Qualquer fluxo de controle JavaScript padrão, como a lógica if/else, é aceito.
- O código de transformação acessa o corpo da solicitação do webhook por meio da variável `payload`. Essa variável é um objeto populado pela análise do corpo da solicitação JSON.
- Qualquer recurso aceito em nosso endpoint `/users/track` é aceito, incluindo:
  - Objetos de atributos de usuário, objetos de eventos e objetos de compra
  - Atributos aninhados e propriedades de evento personalizado aninhadas
  - Atualizações do grupo de inscrições
  - Endereço de e-mail como identificador

Selecione **Validate** para retornar uma prévia da saída do seu código e verificar se é uma solicitação `/users/track` aceitável.

{% alert note %}
Solicitações de rede externa, bibliotecas de terceiros e webhooks não JSON não são suportados atualmente.
{% endalert %}

{% endtab %}
{% endtabs %}

## Etapa 5: Monitore sua transformação {#step-5-monitor-your-transformation}

Depois de ativar sua transformação, consulte a análise de dados na página principal de **Transformations** para obter um resumo do desempenho.

* **Incoming Requests:** Este é o número de webhooks recebidos na URL desta transformação. Se as solicitações recebidas forem 0, sua plataforma de origem não enviou nenhum webhook ou a conexão não pôde ser estabelecida.
* **Deliveries:** Após receber solicitações de entrada, a Transformação de Dados aplica seu código de transformação para enviar ao destino da Braze selecionado.

É uma boa meta ter 100% das solicitações recebidas levando a entregas. O número de entregas nunca excederá o número de solicitações recebidas.

### Solução de problemas {#troubleshooting}

Para monitoramento e solução de problemas mais detalhados, consulte a página **Logs** para obter registros específicos, onde são registradas as últimas 1.000 solicitações de entrada para todas as transformações em seus espaços de trabalho. Você pode selecionar cada registro para visualizar o corpo da solicitação de entrada, a saída da transformação e o corpo da resposta do destino da transformação.

Se não houver entregas, verifique se há erros de sintaxe no código de transformação e confirme se o código está sendo compilado. Em seguida, verifique se a saída é uma solicitação de destino válida.

Entregas menores que o número de solicitações recebidas indicam que pelo menos alguns webhooks foram entregues com êxito. Consulte os registros de transformação para ver exemplos de erros e verifique se a saída da transformação é a esperada. É possível que seu código de transformação não esteja considerando todas as variações de webhooks recebidos.