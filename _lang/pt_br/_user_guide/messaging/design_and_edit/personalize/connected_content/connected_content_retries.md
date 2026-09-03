---
nav_title: Novas tentativas de Conteúdo conectado
article_title: Novas tentativas de Conteúdo conectado
page_order: 5
description: "Este artigo de referência aborda como lidar com novas tentativas de Conteúdo conectado."

---

# Usar lógica de nova tentativa para Conteúdo conectado {#use-retry-logic-for-connected-content}

> Esta página explica como adicionar novas tentativas às suas chamadas de Conteúdo conectado.

## Como funcionam as novas tentativas {#how-retries-work}

Como o Connected Content depende do recebimento de dados de APIs, uma API pode ficar temporariamente indisponível enquanto a Braze faz a chamada. Nesse caso, a Braze oferece suporte a uma lógica de novas tentativas para reenviar a requisição usando backoff exponencial.

{% alert note %}
O `:retry` do Connected Content não está disponível para mensagens no app.
{% endalert %}

## Usando lógica de nova tentativa {#using-retry-logic}

Para usar a lógica de nova tentativa, adicione a tag `:retry` à chamada de Connected Content, conforme mostrado no trecho de código a seguir:

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Quando uma tag `:retry` é incluída na chamada de Connected Content, a Braze tenta repetir a chamada até cinco vezes.

### Comportamento da prévia {#preview-behavior}

A lógica de nova tentativa se aplica apenas a envios em tempo real (incluindo envios de teste), não a prévias. Se uma chamada de Connected Content com `:retry` falhar durante a prévia, ela poderá exibir a mensagem "This message would not have been shown because retry functionality was triggered" em vez de renderizar o conteúdo. Esse é o comportamento esperado e não indica um problema na Braze.

### Resultados das novas tentativas {#retry-outcomes}

#### Quando uma nova tentativa é bem-sucedida {#when-a-retry-succeeds}

Se uma tentativa repetida for bem-sucedida, a mensagem é enviada e nenhuma nova tentativa adicional é feita para essa mensagem.

#### Quando a chamada de API falha e as novas tentativas estão ativadas {#when-the-api-call-fails-and-retries-are-enabled}

Se a chamada de API falhar e essa funcionalidade estiver ativada, a Braze tentará repetir a chamada respeitando o [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) que você definiu para cada reenvio. A Braze moverá as mensagens com falha para o final da fila e adicionará minutos extras, se necessário, ao tempo total necessário para enviar sua mensagem.

Se a chamada de Connected Content apresentar erro mais de cinco vezes, a mensagem será abortada, de forma semelhante a como uma [tag de interrupção de mensagem]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content) é disparada.

{% multi_lang_include connected_content/abort_and_retry_logic.md %}