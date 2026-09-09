---
nav_title: Olo
article_title: Olo
description: "Este artigo descreve a parceria entre a Braze e a Olo, uma plataforma SaaS aberta líder para restaurantes que permite hospitalidade em cada ponto de contato."
alias: /partners/olo/
page_type: partner
search_tag: Partner
---

# Olo

> A [Olo](https://www.olo.com/) é uma plataforma SaaS aberta líder para restaurantes que permite hospitalidade em cada ponto de contato.

Ao integrar a Olo e a Braze, você pode:

- Atualizar os perfis de usuário na Braze para mantê-los consistentes com os perfis de usuário da Olo
- Enviar a próxima melhor mensagem pela Braze com base nos eventos da Olo

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Olo | É necessária uma conta Olo com acesso a webhooks para aproveitar essa parceria. Configure as inscrições de webhook por meio da [ferramenta de webhooks de autoatendimento](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) no dashboard da Olo. |
| Braze Data Transformation | Uma [URL de Data Transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation) é necessária para receber dados da Olo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

Um webhook é uma maneira de a Olo enviar informações baseadas em eventos para a Braze sobre os usuários e suas ações, incluindo eventos como Pedido Realizado, Opt-in do Cliente, Pedido Retirado e mais. O webhook da Olo entrega o evento para a Braze geralmente em segundos após a ação ser realizada.

## Aviso legal {#disclaimer}

No Olo, você tem um limite de um webhook por ambiente para cada marca aprovada, todos enviados para a mesma **URL de destino**. Marcas diferentes podem ter URLs diferentes, mas eventos da mesma marca devem compartilhar uma URL. Na Braze, isso significa que você pode criar apenas uma transformação para uso com o Olo.

Para lidar com vários eventos do Olo dentro dessa única transformação, procure o cabeçalho `X-Olo-Event-Type` em cada webhook. Esse cabeçalho permite processar condicionalmente diferentes eventos do Olo.

## Integração {#integration}

### Etapa 1: Configure a Transformação de Dados da Braze para aceitar o evento de teste do Olo {#step-1}

{% multi_lang_include data_activation/create_transformation.md location="default" %}

### Etapa 2: Configure os webhooks do Olo {#step-2-set-up-olo-webhooks}

Use a [ferramenta de webhooks de autoatendimento](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) no dashboard do Olo para configurar webhooks que enviem dados para sua Transformação de Dados.

1. Escolha quais eventos devem ser enviados para a Braze
2. Configure a **URL de destino**. Essa será a URL da Transformação de Dados criada na [etapa 1](#step-1).

{% alert note %}
`OAuth` e o shared secret do header `X-Olo-Signature` não são necessários para a transformação.
{% endalert %}

{:start="3"}
3. Verifique se o webhook está configurado corretamente enviando um [Evento de Teste](https://developer.olo.com/docs/load/webhooks#operation/test) para sua Transformação de Dados. Apenas usuários do dashboard do Olo com a [permissão de Developer Tools](https://olosupport.zendesk.com/hc/en-us/articles/115001427843-Dashboard-Permissions) podem enviar Eventos de Teste.

O Olo exige uma resposta bem-sucedida do webhook de Evento de Teste antes que você consiga concluir o processo de configuração do webhook do Olo.

### Etapa 3: Escreva o código de transformação para aceitar os eventos do Olo escolhidos {#step-3-write-transformation-code-to-accept-your-chosen-olo-events}

Nesta etapa, você transformará a carga útil do webhook que será enviada da plataforma de origem em um valor de retorno de objeto JavaScript.

1. Envie uma solicitação para a URL da sua Transformação de Dados com uma carga útil de evento de exemplo de um evento do Olo que você pretende suportar. Consulte o [formato do corpo da solicitação](#request-body-format) para ajuda na formatação da sua solicitação.
2. Atualize sua Transformação de Dados e verifique se você consegue ver a carga útil do evento de exemplo nos **Detalhes do Webhook**.
3. Atualize o código da sua Transformação de Dados para suportar os eventos do Olo escolhidos.
4. Clique em **Validate** para retornar uma prévia da saída do seu código e verificar se é uma solicitação `/users/track` aceitável.
5. Salve e ative sua Transformação de Dados.

#### Formato do corpo da solicitação {#request-body-format}

Esse valor de retorno deve seguir o formato do corpo da solicitação `/users/track` da Braze:

{% multi_lang_include data_transformation/transformation_code_requirements.md %}

## Exemplos de Data Transformations para webhooks do Olo {#example-data-transformations-for-olo-webhooks}

Esta seção contém modelos de exemplo que podem ser usados como ponto de partida. Fique à vontade para começar do zero ou excluir componentes específicos conforme necessário.

Em cada modelo, o código define uma variável, `brazecall`, para criar uma requisição `/users/track`.

Após a requisição `/users/track` ser atribuída a `brazecall`, você retornará explicitamente `brazecall` para gerar uma saída.

### Transformação de evento único {#single-event-transformation}

Se você deseja suportar apenas um único evento do Olo, não será necessário usar o cabeçalho `X-Olo-Event-Type` para criar condicionalmente a carga útil da requisição `/users/track`. Por exemplo, registrar um evento de compra ou um evento personalizado no perfil de usuário quando um webhook de Order Placed do Olo é enviado para a Braze.

### Registrando cada produto como uma compra {#logging-each-product-as-a-purchase}

```javascript
// iterate through the items included within the order

const purchases = payload.items.map((item) => {
 return {
   external_id: payload.customer.customerId.toString(),
   product_id: item.productId.toString(),
   currency: 'USD',
   price: item.sellingPrice,
   time: new Date().toISOString(),
   quantity: item.quantity,
   properties: {
     customValues: item.customValues
   }
 };
});

// log a purchase per item in the order

let brazecall = {
 "purchases": purchases
};

return brazecall;
```

### Registrando um evento personalizado {#logging-a-custom-event}

```javascript
// log an event “Order Placed” to the profile that includes all items in the order as event properties.

let brazecall = {
"events": [
   {
     "external_id": payload.customer.customerId.toString(),
     "_update_existing_only": false,
     "name": "Order Placed",
     "time": new Date().toISOString(),
     "properties": {
       "Delivery Method": payload.deliveryMethod,
       "Items": payload.items,
       "Total": payload.totals.total,
       "Location": payload.location.name
     }
   }
 ]
};

return brazecall;
```

## Transformação de eventos múltiplos {#multi-event-transformation}

O Olo envia o tipo de evento dentro do cabeçalho `X-Olo-Event-Type` de cada webhook. Para oferecer suporte a vários eventos de webhook do Olo em uma única transformação, use lógica condicional para transformar a carga útil do webhook com base no valor desse tipo de cabeçalho.

No exemplo de transformação a seguir, nosso JavaScript cria uma carga útil específica para os eventos `UserSignedUp` e `OrderPlaced`. Além disso, uma condição `else` trata uma carga útil para quaisquer eventos do Olo enviados à Braze sem o cabeçalho X-Olo-Event-Type de `UserSignedUp` e `OrderPlaced`.

```javascript
// captures the value within the X-Olo-Event-Type header for use in the conditional logic

let event_type = headers["X-Olo-Event-Type"];

// defines a variable 'brazecall' that will hold the request payload for the /users/track request

let brazecall;

// if the X-Olo-Event-Type header is 'UserSignedUp', define a variable for the different subscription statuses that could be included within the Olo event payload

if (event_type == "UserSignedUp") {
	let emailSubscribe;
	let emailSubscriptionGroup;
	let smsSubscriptionGroup;


// determine if the user has opted into marketing emails


	if (payload.allowEmail) {
		emailSubscribe = "opted_in";
		emailSubscriptionGroup = "subscribed";
	} else {
		emailSubscribe = "unsubscribed";
		emailSubscriptionGroup = "unsubscribed";
	}


	// determine if the user has opted into SMS


	if (payload.allowMarketingSms) {
		smsSubscriptionGroup = "subscribed";
	} else {
		smsSubscriptionGroup = "unsubscribed";
	}

	// build the /users/track request and pass in the appropriate subscription statuses


	brazecall = {
		"attributes": [{
			"external_id": payload.id.toString(),
			"_update_existing_only": false,
			"email": payload.emailAddress,
			"first_name": payload.firstName,
			"last_name": payload.lastName,
			"email_subscribe": emailSubscribe,
			"phone": payload.contactNumber,
			"subscription_groups": [{
					"subscription_group_id": "57e5307f-9084-490d-9d6d-8244dc919a48",
					"subscription_state": emailSubscriptionGroup
				},
				{
					"subscription_group_id": "6440ba26-86ea-47db-a935-6647941dc78b",
					"subscription_state": smsSubscriptionGroup
				}
			]
		}]
	}; // if the X-Olo-Event-Type header is 'OrderPlaced', build the /users/track request to log an event to the user profile
} else if (event_type == "OrderPlaced") {
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": false,
			"name": "Order Placed",
			"time": new Date().toISOString(),
			"properties": {
				"Delivery Method": payload.deliveryMethod,
				"Items": payload.items,
				"Total": payload.totals.total,
				"Location": payload.location.name
			}
		}]
	};
} else { // if the X-Olo-Event-Type header is anything else, build the /users/track request to log an event to the user profile
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": true,
			"name": "Another Event",
			"time": new Date().toISOString()
		}]

	};
}

// return `brazecall` to create an output.

return brazecall;
```

### Etapa 4: Publique seu webhook do Olo {#step-4-publish-your-olo-webhook}

Depois de ativar sua Transformação de Dados na Braze, use a [ferramenta de webhooks de autoatendimento](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) no dashboard do Olo para publicar seu webhook. Quando o webhook for publicado, a Transformação de Dados começará a receber mensagens de eventos de webhook do Olo.

## O que saber {#things-to-know}

### Novas tentativas {#retries}

A Olo tentará reenviar chamadas de webhook que resultem em um código de status de resposta HTTP `429 - Too Many Requests` ou na faixa `5xx` (por exemplo, devido a um timeout de gateway ou erro de servidor), até 50 vezes ao longo de um período de 24 horas antes de descartar a solicitação.

### Entrega pelo menos uma vez {#at-least-once-delivery}

Se uma chamada de webhook resultar em um código de status de resposta HTTP `429 - Too Many Requests` ou na faixa `5xx` (por exemplo, devido a um timeout de gateway ou erro de servidor), a Olo tentará reenviar a mensagem até 50 vezes ao longo de um período de 24 horas antes de desistir.

Portanto, os webhooks podem ser recebidos várias vezes por um assinante. Cabe ao assinante ignorar duplicatas verificando o cabeçalho `X-Olo-Message-Id`.