---
nav_title: Erros e respostas
article_title: Erros e respostas da API
description: "Este artigo de referência aborda os vários erros e respostas do servidor que podem surgir ao usar a API da Braze e como solucioná-los."
page_type: reference
page_order: 2.3

---
# Erros e respostas da API {#api-errors-and-responses}

> Este artigo de referência aborda os vários erros e respostas do servidor que podem surgir ao usar a API da Braze e como solucioná-los.

## Respostas do servidor {#server-responses}

Se a carga útil do seu POST foi aceita pelos nossos servidores, as mensagens bem-sucedidas recebem a seguinte resposta:

```json
{
  "message" : "success"
}
```

Observe que "success" significa apenas que a carga útil da API RESTful foi corretamente formada e enviada para nossos serviços de notificação por push, e-mail ou outros serviços de envio de mensagens. Isso não significa que as mensagens foram realmente entregues, pois fatores adicionais podem impedir a entrega da mensagem (por exemplo, um dispositivo pode estar offline, o token por push pode ser rejeitado pelos servidores da Apple ou você pode ter fornecido um ID de usuário desconhecido).

### Por que minha solicitação retorna "success" quando nenhuma mensagem foi entregue? {#why-does-my-request-return-success-when-no-message-was-delivered}

Uma resposta `message: success` ou `2XX` significa que a Braze aceitou e enfileirou a solicitação para os endpoints envolvidos — não que cada destinatário recebeu uma mensagem. Para envio de mensagens, a entrega ainda depende da elegibilidade do canal, tokens, erros do provedor e validação de conteúdo. Consulte a tabela de [erros fatais]({{site.baseurl}}/api/errors#fatal-errors) para erros HTTP que bloqueiam envios, e as análises da sua Campaign ou Canvas para métricas de entrega downstream.

Para endpoints como [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify), que não enviam mensagens, uma mensagem de sucesso significa apenas que a Braze recebeu a solicitação para processamento. Se não houver correspondência para o alias após o processamento, a solicitação é interrompida.

Se sua mensagem for bem-sucedida, mas contiver erros não fatais, você receberá a seguinte resposta:

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

No caso de sucesso, quaisquer mensagens que não foram afetadas por um erro no array `errors` ainda serão entregues. Se sua mensagem contiver um erro fatal, você receberá a seguinte resposta:

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## Respostas para IDs de envio rastreados {#responses-for-tracked-send-ids}

A análise de dados está sempre disponível para Campaigns. Além disso, a análise de dados fica disponível para uma instância de envio específica de uma Campaign quando ela é enviada como broadcast. Quando o rastreamento está disponível para uma instância de envio específica de uma Campaign, você recebe a seguinte resposta:

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

O ID de envio fornecido pode ser usado como parâmetro para o endpoint `/send/data_series` para recuperar a análise de dados específica do envio.

## Erros {#errors}

O elemento de código de status da resposta de um servidor é um número de 3 dígitos, em que o primeiro dígito do código define a classe da resposta.

- A **classe 2XX** de código de status (não fatal) indica que **sua solicitação** foi recebida, compreendida e aceita com sucesso.
- A **classe 4XX** de código de status (fatal) indica um **erro do cliente**. Consulte a tabela de erros fatais para uma lista completa de códigos de erro 4XX e suas descrições.
- A **classe 5XX** de código de status (fatal) indica um **erro do servidor**. Existem várias causas possíveis. Por exemplo, o servidor que você está tentando acessar não consegue executar a solicitação, o servidor está em manutenção e, por isso, não consegue executar a solicitação, ou o servidor está enfrentando altos níveis de tráfego. Quando isso acontecer, recomendamos que você tente novamente sua solicitação com backoff exponencial. No caso de um incidente ou interrupção, a Braze não consegue reproduzir nenhuma chamada de REST API que falhou durante a janela do incidente. Você deve tentar novamente todas as chamadas que falharam durante a janela do incidente.
  - Um **erro 502** é uma falha antes de chegar ao servidor de destino.
  - Um **erro 503** significa que a solicitação chegou ao servidor de destino, mas não foi possível completá-la porque não há capacidade suficiente, há um problema de rede ou algo semelhante.
  - Um **erro 504** indica que um servidor não recebeu uma resposta de outro servidor upstream.

### Erros fatais {#fatal-errors}

Os seguintes códigos de status e mensagens de erro associadas são retornados quando sua solicitação encontra um erro fatal.

{% alert warning %}
Todos os códigos de erro a seguir indicam que nenhuma mensagem é enviada.
{% endalert %}

| Código de erro | Descrição |
|---|---|
| `5XX Internal Server Error` | Tente novamente sua solicitação com backoff exponencial.|
| `400 Bad Request` | Sintaxe incorreta. JSON inválido retorna HTTP 400. O campo `error` pode incluir uma mensagem indicando que você deve enviar um `application/json` válido no corpo da solicitação, ou `Error while parsing request body. Please check your syntax.` Consulte [Erro ao analisar o corpo da solicitação](#error-while-parsing-request-body).|
| `400 No Recipients` | Não há IDs externos, IDs de Segment ou tokens por push na solicitação.|
| `400 Invalid Campaign ID` | Nenhuma Campaign de API de envio de mensagens foi encontrada para o ID de Campaign fornecido.|
| `400 Message Variant Unspecified` | Você forneceu um ID de Campaign, mas nenhum ID de variante de mensagem.|
| `400 Invalid Message Variant` | Você forneceu um ID de Campaign válido, mas o ID de variante de mensagem não corresponde a nenhuma das mensagens dessa Campaign.|
| `400 Mismatched Message Type` | Você forneceu uma variante de mensagem com o tipo de mensagem incorreto para pelo menos uma de suas mensagens.|
| `400 Invalid Extra Push Payload` | Você forneceu a chave `extra` para `apple_push` ou `android_push`, mas ela não é um dicionário.|
| `400 Max Input Length Exceeded` | Para `/users/track`, esse erro é causado por exceder o número máximo de objetos permitidos em uma única solicitação. O limite depende do modelo de limite de frequência: para a maioria dos clientes, cada solicitação suporta até 75 objetos no total combinados entre `attributes`, `events` e `purchases`. Para clientes com limites de frequência legados, cada array suporta até 75 objetos independentemente. Para saber mais, consulte [POST: Criar e atualizar usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track).|
| `400 The max number of external_ids and aliases per request was exceeded` | Causado por chamar mais de 50 IDs externos.|
| `400 The max number of ids per request was exceeded` | Causado por chamar mais de 50 IDs externos.|
| `400 No message to send` | Nenhuma carga útil foi especificada para a mensagem.|
| `400 Slideup Message Length Exceeded` | A mensagem slideup contém mais de 140 caracteres.|
| `400 Apple Push Length Exceeded` | A carga útil JSON tem mais de 1.912 bytes.|
| `400 Android Push Length Exceeded` | A carga útil JSON tem mais de 4.000 bytes.|
| `400 Bad Request` | Não é possível analisar o datetime de `send_at`.|
| `400 Bad Request` | Na sua solicitação, `in_local_time` é true, mas `time` já passou no fuso horário da sua empresa.|
| `401 Unauthorized` | Chave de API inválida. Causas comuns incluem:<br><br>- **Cabeçalho Authorization ausente ou malformado.** O valor do cabeçalho deve ser `Bearer` seguido de um espaço e sua chave de API: `Authorization: Bearer YOUR-API-KEY`. Erros comuns incluem omitir `Bearer`, omitir a chave após `Bearer` ou colocar o valor entre aspas.<br>- **Endpoint REST incorreto.** Você está enviando a solicitação para a [instância]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) incorreta. Por exemplo, se sua conta está na nossa instância da UE (`https://dashboard-01.braze.eu`), a solicitação deve ser enviada para `https://rest.fra-01.braze.eu`.<br>- **Permissões insuficientes.** Cada chave de API é vinculada a um espaço de trabalho e a um conjunto de permissões específicos. Verifique as permissões da chave em **Configurações** > **Chaves de API** no dashboard.<br>- **Chave de API incorreta.** As chaves de API são específicas do espaço de trabalho. Uma chave de um espaço de trabalho não pode ser usada para autenticar solicitações de um espaço de trabalho diferente. |
| `403 Forbidden` | O plano de tarifação não oferece suporte, ou a conta está inativada.|
| `403 Access Denied` | A chave da REST API que você está usando não tem permissões suficientes. Causas comuns incluem: {::nomarkdown}<ul><li><strong>A chave de API é anterior ao recurso.</strong> Se a chave de API foi criada antes do lançamento de um recurso (como grupos de inscrições ou catálogos), a chave não herda automaticamente essas permissões. Crie uma nova chave de API com as permissões necessárias em <strong>Configurações</strong> &gt; <strong>Chaves de API</strong>.</li><li><strong>Permissão específica do endpoint ausente.</strong> Cada endpoint de API requer um escopo de permissão específico (por exemplo, <code>users.track</code> ou <code>email.status</code>). Verifique se as permissões da chave correspondem ao endpoint que você está chamando.</li><li><strong>Barra final ou erro de digitação na URL.</strong> Por exemplo, <code>/users/track/</code> (com uma barra final) em vez de <code>/users/track</code> pode gerar erros inesperados.</li></ul>{:/}|
| `404 Not Found` | URL inválida. |
| `415 Unsupported Media Type` | O cabeçalho da solicitação `Content-Type` está ausente ou incorreto. Na página de **Configurações**, adicione `Content-Type` com o valor `application/json`. |
| `429 Rate Limited` | Limite de frequência excedido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Erros fatais" }

### Erro ao analisar o corpo da solicitação {#error-while-parsing-request-body}

A Braze retorna HTTP 400 quando o corpo da solicitação não é um JSON válido. Isso se aplica a endpoints REST que aceitam um corpo JSON, como POST, PUT e PATCH.

O campo `error` inclui uma mensagem indicando que você deve enviar um `application/json` válido no corpo da solicitação. Você também pode ver `Error while parsing request body. Please check your syntax.`

Causas comuns incluem vírgulas extras no final, comentários dentro do JSON, strings com aspas simples, uma chave de abertura `{` extra antes da carga útil ou o envio de uma string concatenada em vez de um objeto codificado em JSON.

Antes de tentar novamente:

1. Valide a carga útil com um linter de JSON.
2. Defina `Content-Type: application/json` e envie JSON codificado em UTF-8.
3. Confirme que seu cliente HTTP codifica o objeto em JSON em vez de concatenar strings brutas.

Para limites de tamanho de carga útil e limites de objetos por solicitação do `/users/track`, consulte [Por que recebo `400 Bad Request` com um erro de sintaxe incorreta ou de análise?]({{site.baseurl}}/api/endpoints/user_data/post_user_track#why-do-i-get-400-bad-request-with-a-bad-syntax-or-parse-error).