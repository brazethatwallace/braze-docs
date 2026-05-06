---
nav_title: Conector de Currents personalizado
alias: /currents_connector/
hidden: true
---

# Conector de Currents personalizado {#custom-currents-connector}

> Aprenda a integrar um conector de Currents personalizado para obter dados de eventos da Braze em tempo real, possibilitando análise de dados, relatórios e automação mais personalizados.

## Pré-requisitos {#prerequisites}

Para integrar um conector de Currents personalizado na Braze, você precisará fornecer uma URL de endpoint e um [token de autenticação opcional](#authentication).

Além disso, se você tiver mais de um grupo de app na Braze, precisará configurar um conector de Currents personalizado para cada grupo. No entanto, você pode apontar todos os grupos de app para o mesmo endpoint, ou para um endpoint com um parâmetro `GET` adicional, como `your_app_group_key="Brand A"`.

## Prevenindo perda de dados {#preventing-data-loss}

### Monitoramento de erros {#error-monitoring}

Para evitar perda de dados e interrupção do serviço, é essencial que você monitore seus endpoints o tempo todo e busque resolver erros graves ou inatividade dentro de 24 horas.

Para a maioria dos tipos de erro (como erros de servidor, erros de conexão de rede, etc.), a Braze continuará a enfileirar e tentar retransmitir eventos por até 24 horas. Após esse período, eventos não transmitidos serão descartados. Conectores com taxas de erro ou tempo de atividade consistentemente ruins serão automaticamente suspensos.

### Resiliência a mudanças {#change-resilience}

Ocasionalmente, faremos alterações não disruptivas nos esquemas do Braze Currents. Alterações não disruptivas são novas colunas ou tipos de eventos que podem ser nulos.

Normalmente, damos um aviso de duas semanas para essas mudanças, mas às vezes isso não é possível. É essencial que você projete sua integração para lidar com campos ou tipos de eventos não reconhecidos, caso contrário, isso provavelmente levará à perda de dados.

{% alert tip %}
Para a lista completa de esquemas de eventos do Currents, consulte [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).
{% endalert %}

## Agrupamento e serialização {#batching-and-serialization}

O formato de dados alvo é JSON sobre HTTPS. Por padrão, os eventos são agrupados em lotes de 100 com base no seguinte:

- **Número de eventos enfileirados**: Por exemplo, se o tamanho do lote estiver configurado para 200 eventos e houver 200 eventos na fila.
- **Duração de um evento:** Normalmente, os eventos não são enfileirados se um evento durar mais de 15 minutos. Cada tipo de evento tem uma fila separada, portanto a latência pode variar entre os tipos de eventos.

Os eventos são então enviados para o endpoint como um array JSON de todos os eventos no seguinte formato:

```json
{"events": [event1, event2, event3, etc...]}
```

Haverá um objeto JSON de nível superior com a chave `"events"` que mapeia para um array de outros objetos JSON, cada um representando um único evento.

## Exemplos de carga útil {#payload-examples}

Os exemplos a seguir mostram cargas úteis para eventos individuais, o que significa que as cargas úteis pertenceriam a um array maior de objetos JSON, onde cada objeto JSON representa um único evento no lote.

Além disso, sua estrutura varia ligeiramente da estrutura plana encontrada em [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/). Em particular, eles contêm dois sub-objetos:

| Nome | Descrição |
|----|-----------|
| `"user"` | Contém propriedades do usuário, como `user_id`, `external_user_id`, `device_id` e `timezone`. |
| `"properties"` | Contém atributos de um evento, como o `app/campaign/canvas/platform` ao qual se aplica. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Se um endpoint downstream receber uma carga útil com zero eventos ou um corpo de solicitação vazio, o resultado deve ser considerado um no-op, ou seja, nenhum efeito downstream deve ocorrer a partir dessa chamada. No entanto, você ainda deve verificar o cabeçalho `Authorization` (como faria em uma chamada de API normal) e dar uma resposta HTTP apropriada para [credenciais inválidas](#authentication), como `401` ou `403`. Isso permite que a Braze saiba que as credenciais do conector são válidas.

### Eventos associados a Campaigns {#campaign-associated-events}

Aqui estão alguns exemplos de cargas úteis de eventos para vários eventos, como apareceriam se estivessem associados a uma Campaign:

#### Clique em mensagem no app {#in-app-message-click}

```json
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "platform": "android",
     "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

#### Envio de notificação por push {#push-notification-send}

```json
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

#### Abertura de e-mail {#email-open}

```json
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

#### Entrega de SMS {#sms-delivery}

```json
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Eventos associados a Canvas {#canvas-associated-events}

Aqui estão alguns exemplos de cargas úteis de eventos para vários eventos, como apareceriam se estivessem associados a um Canvas:

#### Clique em mensagem no app {#in-app-message-click}

```json
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "platform": "android",
    "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

#### Envio de notificação por push {#push-notification-send}

```json
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

#### Abertura de e-mail {#email-open}

```json
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

#### Entrega de SMS {#sms-delivery}

```json
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Outros eventos {#other-events}

Aqui estão alguns exemplos de cargas úteis de eventos para vários outros eventos que não estão associados a Campaigns nem a Canvas:

#### Evento personalizado {#custom-event}

```json
// Custom Event: users.behaviors.CustomEvent
{
  "event_type": "users.behaviors.CustomEvent",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "name": "custom event name",
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "custom_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

#### Evento de compra {#purchase-event}

```json
// Purchase Event: users.behaviors.Purchase
{
  "event_type": "users.behaviors.Purchase",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id"
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "product_id": "1234",
    "price": 12.34,
    "currency": "AED,
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "purchase_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

#### Início de sessão {#session-start}

```json
// Session Start: users.behaviors.app.SessionStart
{
  "event_type": "users.behaviors.app.SessionStart",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "session_id": "b1234567-89ab-cdef-0123-456789abcdef"
  }
}
```

## Autenticação {#authentication}

Tokens de autenticação na sua carga útil são opcionais. Eles podem ser passados por meio de um cabeçalho HTTP `Authorization` usando o esquema de autorização `Bearer`, conforme especificado na [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1). Embora opcionais, se um token de autenticação for passado, a Braze sempre o validará primeiro&#8212;mesmo que não haja eventos na carga útil.

De acordo com a RFC 6750, os tokens devem ser valores codificados em Base64 com pelo menos um caractere. Tenha em mente que a RFC 6750 permite que os tokens contenham os seguintes caracteres além dos caracteres normais do Base64: `-`, `.`, `_` e `~`. Você pode escolher se deseja incluir esses caracteres no seu token ou não&#8212;no entanto, ele deve estar no formato Base64.

Além disso, se o cabeçalho `Authorization` estiver presente, ele será construído usando o seguinte formato:

```plaintext
"Authorization: Bearer " + <token>
```

Por exemplo, se seu token de autenticação for `0p3n5354m3==`, seu cabeçalho `Authorization` deve ser semelhante ao seguinte:

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
No futuro, podemos usar cabeçalhos `Authorization` para implementar um esquema de autorização personalizado, de chave-valor, exclusivo da Braze. Isso seguirá a especificação [RFC 7235](https://tools.ietf.org/html/rfc7235), que é como algumas empresas implementam seus esquemas de autenticação, como a Amazon Web Services (AWS).
{% endalert %}

## Versionamento {#versioning}

Todas as solicitações da nossa integração de conector HTTP serão enviadas com um cabeçalho personalizado designando a versão da solicitação Currents que está sendo feita:

```plaintext
Braze-Currents-Version: 1
```

A versão será sempre `1`, já que não esperamos incrementar esse número com muita frequência, se é que algum dia.

Assim como nossos [esquemas de armazenamento de data warehouse]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics?redirected=1), cada campo de evento em um evento individual tem garantia de retrocompatibilidade com versões anteriores de carga útil de eventos, de acordo com a definição de retrocompatibilidade do [Apache Avro](https://avro.apache.org/):

1. Campos de eventos específicos têm garantia de sempre manter o mesmo tipo de dado ao longo do tempo.
2. Qualquer novo campo adicionado à carga útil ao longo do tempo deve ser considerado opcional por todas as partes.
3. Campos obrigatórios nunca serão removidos.

## Mecanismo de tratamento de erros e novas tentativas {#error-handling-and-retry-mechanism}

Se ocorrer um erro, a Braze irá enfileirar e tentar novamente a solicitação com base no código de retorno HTTP recebido. Ela continuará tentando por pelo menos dois dias, desde que os dados estejam armazenados em buffer no sistema. Se os dados ficarem parados por mais de 24 horas, nossos engenheiros de plantão serão alertados automaticamente. Neste momento, nossa estratégia de backoff é tentar novamente periodicamente.

Se sua integração Currents começar a retornar erros `4XX`, a Braze enviará automaticamente um e-mail de notificação e estenderá automaticamente o período de retenção para um mínimo de sete dias.

Qualquer código de erro HTTP não listado abaixo será tratado como um erro HTTP `5XX`.

{% alert warning %}
Se o mecanismo de novas tentativas da Braze falhar em entregar um evento por mais de 24 horas, ocorrerá perda de dados.
{% endalert %}

Os seguintes códigos de status HTTP serão reconhecidos pelo nosso cliente conector:

<table>
  <thead>
    <tr>
      <th>Código de status</th>
      <th>Resposta</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2XX</code></td>
      <td>Deu certo</td>
      <td>Os dados do evento não serão reenviados.</td>
    </tr>
    <tr>
      <td><code>5XX</code></td>
      <td>Erro do lado do servidor</td>
      <td>Os dados do evento serão reenviados em um padrão de backoff exponencial com jitter. Se os dados não forem enviados com sucesso dentro de 24 horas, eles serão descartados.</td>
    </tr>
    <tr>
      <td><code>400</code></td>
      <td>Erro do lado do cliente</td>
      <td>O conector enviou pelo menos um evento malformado. Os dados do evento serão divididos em lotes de tamanho 1 e reenviados. Quaisquer eventos nesses lotes de tamanho 1 que receberem outra resposta <code>400</code> serão descartados permanentemente. Você deve relatar ocorrências repetidas.</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>Não autorizado</td>
      <td>O conector foi configurado com credenciais inválidas. Os dados do evento serão reenviados após um atraso de 2 a 5 minutos. Se não resolvido dentro de 48 horas, os dados do evento serão descartados.</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>Proibido</td>
      <td>O conector foi configurado com credenciais inválidas. Os dados do evento serão reenviados após um atraso de 2 a 5 minutos. Se não resolvido dentro de 48 horas, os dados do evento serão descartados.</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>Não encontrado</td>
      <td>O conector foi configurado com credenciais inválidas. Os dados do evento serão reenviados após um atraso de 2 a 5 minutos. Se não resolvido dentro de 48 horas, os dados do evento serão descartados.</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>Carga útil muito grande</td>
      <td>Os dados do evento serão divididos em lotes menores e reenviados.</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>Muitas solicitações</td>
      <td>Indica limite de taxa. Os dados do evento serão reenviados em um padrão de backoff exponencial com jitter. Se não forem enviados com sucesso dentro de 24 horas, serão descartados.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }