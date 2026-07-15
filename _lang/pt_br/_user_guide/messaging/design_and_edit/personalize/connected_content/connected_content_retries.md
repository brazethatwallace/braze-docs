---
nav_title: Novas tentativas de Conteúdo conectado
article_title: Novas tentativas de Conteúdo conectado
page_order: 5
description: "Este artigo de referência aborda como lidar com novas tentativas de Conteúdo conectado."

---

# Usar lógica de nova tentativa para Conteúdo conectado {#use-retry-logic-for-connected-content}

> Esta página explica como adicionar novas tentativas às suas chamadas de Conteúdo conectado.

## Como as novas tentativas funcionam {#how-retries-work}

Como o Conteúdo conectado depende do recebimento de dados de APIs, uma API pode ficar temporariamente indisponível enquanto a Braze faz a chamada. Nesse caso, a Braze oferece suporte à lógica de nova tentativa para refazer a solicitação usando backoff exponencial.

{% alert note %}
O `:retry` do Conteúdo conectado não está disponível para mensagens no app.
{% endalert %}

## Usando a lógica de nova tentativa {#using-retry-logic}

Para usar a lógica de nova tentativa, adicione a tag `:retry` à chamada de Conteúdo conectado, conforme mostrado no trecho de código a seguir:

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Quando uma tag `:retry` é incluída na chamada de Conteúdo conectado, a Braze tentará refazer a chamada até cinco vezes.

### Resultados das novas tentativas {#retry-outcomes}

#### Quando uma nova tentativa é bem-sucedida {#when-a-retry-succeeds}

Se uma nova tentativa for bem-sucedida, a mensagem será enviada e nenhuma nova tentativa adicional será feita para essa mensagem.

#### Quando a chamada de API falha e as novas tentativas estão ativadas {#when-the-api-call-fails-and-retries-are-enabled}

Se a chamada de API falhar e essa opção estiver ativada, a Braze tentará novamente a chamada respeitando o [limite de taxa]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) que você definiu para cada reenvio. A Braze moverá as mensagens com falha para o final da fila e adicionará minutos extras, se necessário, ao tempo total necessário para enviar sua mensagem.

Se a chamada de Conteúdo conectado falhar mais de cinco vezes, a mensagem será cancelada, de forma semelhante a como uma [tag de cancelamento de mensagem]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content) é acionada.

{% multi_lang_include connected_content/abort_and_retry_logic.md %}