---
nav_title: Conector HTTP personalizado
article_title: Conector HTTP personalizado
alias: /currents/custom_http_connector/
page_order: 3
page_type: reference
tool: Currents
description: "Este artigo de referência descreve como configurar um conector HTTP personalizado para transmitir dados de eventos do Braze Currents diretamente para o seu próprio endpoint HTTP em tempo real."
---

# Conector HTTP personalizado {#custom-http-connector}

> Saiba como integrar um conector Currents personalizado para receber dados de eventos da Braze em tempo real, possibilitando análises, relatórios e automações mais personalizados.

## Pré-requisitos {#prerequisites}

Para integrar um conector Currents personalizado na Braze, você precisará fornecer uma URL de endpoint e um [token de autenticação opcional](#authentication).

Além disso, se você tiver mais de um grupo de app na Braze, precisará configurar um conector Currents personalizado para cada grupo. No entanto, você pode direcionar todos os grupos de app para o mesmo endpoint, ou para um endpoint com um parâmetro `GET` adicional, como `your_app_group_key="Brand A"`.

## Integração {#integration}

### Etapa 1: Configure seu endpoint {#step-1-set-up-your-endpoint}

Você precisará de uma URL de endpoint para configurar essa integração. Seu endpoint deve ser capaz de receber solicitações HTTP POST e retornar um código de status `2XX` para confirmar o recebimento bem-sucedido dos eventos. Se quiser autenticar as solicitações da Braze, você também precisará de um token bearer.

### Etapa 2: Configure o Braze Currents {#step-2-configure-braze-currents}

Na Braze, navegue até **Integrações de parceiros** > **Exportação de dados**, clique em **Criar nova corrente** e selecione **Exportação de Currents personalizada**.

Dê um nome à sua exportação e um e-mail de contato, depois prossiga para a página **Informações da corrente**. Nessa página, insira a URL do seu endpoint e o token bearer opcional.

Após configurar suas credenciais, marque todos os eventos de engajamento com mensagem, comportamento do cliente e eventos de usuário que deseja exportar, e clique em **Lançar corrente**.

## Eventos do Currents compatíveis {#supported-currents-events}

A Braze oferece suporte à exportação dos seguintes dados para o seu conector HTTP personalizado:

- [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events?tab=custom%20http%20connector)
- [Eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events?tab=custom%20http%20connector)

Para ver a estrutura da carga útil de cada evento, selecione a guia **Custom HTTP Connector** no glossário de eventos.

## Prevenção de perda de dados {#preventing-data-loss}

### Monitoramento de erros {#error-monitoring}

Para evitar perda de dados e interrupção do serviço, é essencial que você monitore seus endpoints o tempo todo e resolva prontamente quaisquer erros ou períodos de inatividade.

Para a maioria dos tipos de erro (como erros de servidor e erros de conexão de rede), a Braze tentará reenviar ativamente as transmissões de eventos. Se o problema persistir por mais de 5 dias, a integração será desativada automaticamente. Novos eventos recebidos serão descartados e perdidos permanentemente.

### Resiliência a mudanças {#change-resilience}

Ocasionalmente, faremos alterações não disruptivas nos esquemas do Braze Currents. Alterações não disruptivas são novas colunas anuláveis ou novos tipos de evento.

Normalmente, avisamos com duas semanas de antecedência sobre essas mudanças, mas às vezes isso não é possível. É essencial que você projete sua integração para lidar com campos ou tipos de evento não reconhecidos, caso contrário, isso provavelmente levará à perda de dados.

{% alert tip %}
Para a lista completa dos esquemas de eventos do Currents, consulte [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) e [Eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/).
{% endalert %}

## Agrupamento em lotes e serialização {#batching-and-serialization}

O formato de dados de destino é JSON sobre HTTPS. Por padrão, os eventos são enviados ao seu endpoint em lotes de até 100 eventos cada.

Os eventos são enviados ao endpoint como um array JSON de todos os eventos no seguinte formato:

```json
{"events": [event1, event2, event3, etc...]}
```

Haverá um objeto JSON de nível superior com a chave `"events"` que mapeia para um array de outros objetos JSON, cada um representando um único evento. Cada evento contém dois subobjetos:

| Nome | Descrição |
|----|-----------|
| `"user"` | Contém propriedades do usuário, como `user_id`, `external_user_id`, `device_id` e `timezone`. |
| `"properties"` | Contém atributos de um evento, como o `app/campaign/canvas/platform` ao qual se aplica. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Se um endpoint downstream receber uma carga útil com zero eventos ou um corpo de solicitação vazio, o resultado deve ser considerado um no-op, ou seja, nenhum efeito downstream deve ocorrer a partir dessa chamada. No entanto, você ainda deve verificar o cabeçalho `Authorization` (como faria em uma chamada de API normal) e retornar uma resposta HTTP apropriada para [credenciais inválidas](#authentication), como `401` ou `403`. Isso permite que a Braze saiba que as credenciais do conector são válidas.

## Autenticação {#authentication}

Tokens de autenticação na sua carga útil são opcionais. Eles podem ser passados por meio de um cabeçalho HTTP `Authorization` usando o esquema de autorização `Bearer`, conforme especificado na [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1). Embora opcional, se um token de autenticação for passado, a Braze sempre o validará primeiro&#8212;mesmo que não haja eventos na carga útil.

De acordo com a RFC 6750, os tokens devem ser valores codificados em Base64 com pelo menos um caractere. Tenha em mente que a RFC 6750 permite que os tokens contenham os seguintes caracteres além dos caracteres Base64 normais: `-`, `.`, `_` e `~`. Você pode escolher se deseja incluir esses caracteres no seu token ou não&#8212;no entanto, ele deve estar no formato Base64.

Além disso, se o cabeçalho `Authorization` estiver presente, ele será construído usando o seguinte formato:

```plaintext
"Authorization: Bearer " + <token>
```

Por exemplo, se o seu token de autenticação for `0p3n5354m3==`, seu cabeçalho `Authorization` deve ser semelhante ao seguinte:

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
No futuro, poderemos usar cabeçalhos `Authorization` para implementar um esquema de autorização personalizado, baseado em pares chave-valor, exclusivo da Braze. Isso seguiria a especificação [RFC 7235](https://tools.ietf.org/html/rfc7235), que é como algumas empresas implementam seus esquemas de autenticação, como a Amazon Web Services (AWS).
{% endalert %}

## Versionamento {#versioning}

Todas as solicitações da nossa integração de conector HTTP serão enviadas com um cabeçalho personalizado que designa a versão da solicitação do Currents sendo feita:

```plaintext
Braze-Currents-Version: 1
```

A versão será sempre `1`, pois não esperamos incrementar esse número com frequência, se é que algum dia.

Assim como nossos [esquemas de armazenamento em data warehouse]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics?redirected=1), cada campo de evento em um evento individual tem garantia de compatibilidade retroativa com versões anteriores da carga útil de eventos, de acordo com a definição de compatibilidade retroativa do [Apache Avro](https://avro.apache.org/):

1. Campos de evento específicos têm garantia de sempre manter o mesmo tipo de dados ao longo do tempo.
2. Quaisquer novos campos adicionados à carga útil ao longo do tempo devem ser considerados opcionais por todas as partes.
3. Campos obrigatórios nunca serão removidos.

## Tratamento de erros e mecanismo de nova tentativa {#error-handling-and-retry-mechanism}

Se ocorrer um erro, a Braze enfileirará e tentará reenviar a solicitação com base no código de retorno HTTP recebido. Se o problema persistir por mais de 5 dias, a integração será desativada automaticamente: novos eventos recebidos serão descartados e perdidos permanentemente, e eventos já enfileirados serão descartados permanentemente após serem retidos por 7 dias. Se os dados ficarem presos por mais de 24 horas, nossos engenheiros de plantão serão alertados automaticamente. Para uma análise completa de como cada código de status é tratado, consulte a tabela abaixo.

Se a sua integração do Currents estiver retornando erros de autenticação, a Braze enviará automaticamente um e-mail de notificação para você.

Qualquer código de erro HTTP não listado abaixo será tratado como um erro HTTP `5XX`.

{% alert warning %}
Se o problema persistir por mais de 5 dias, a integração será desativada. Novos eventos recebidos serão descartados e perdidos permanentemente, e eventos já enfileirados serão descartados permanentemente após serem retidos por 7 dias.
{% endalert %}

Os seguintes códigos de status HTTP serão reconhecidos pelo nosso cliente conector:

<table aria-label="Tratamento de erros e mecanismo de nova tentativa">
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
      <td>Os dados do evento serão reenviados em um padrão de backoff exponencial com jitter. Se o problema persistir por mais de 5 dias, a integração será desativada, e os eventos já enfileirados serão retidos por 7 dias.</td>
    </tr>
    <tr>
      <td><code>400</code></td>
      <td>Erro do lado do cliente</td>
      <td>O conector enviou pelo menos um evento malformado. Os dados do evento serão divididos em lotes de tamanho 1 e reenviados. Quaisquer eventos nesses lotes de tamanho 1 que receberem outra resposta <code>400</code> serão descartados permanentemente.</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>Não autorizado</td>
      <td>O conector foi configurado com credenciais inválidas. Os eventos com falha não serão reenviados. Corrija suas credenciais e reative a integração para retomar. Se o problema persistir por mais de 5 dias, a integração será desativada, e os eventos já enfileirados serão retidos por 7 dias.</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>Proibido</td>
      <td>O conector foi configurado com credenciais inválidas. Os eventos com falha não serão reenviados. Corrija suas credenciais e reative a integração para retomar. Se o problema persistir por mais de 5 dias, a integração será desativada, e os eventos já enfileirados serão retidos por 7 dias.</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>Não encontrado</td>
      <td>O conector foi configurado com uma URL de endpoint incorreta ou credenciais inválidas. Verifique se a URL do seu endpoint está correta e acessível. Corrija sua configuração e reative a integração para retomar. Se o problema persistir por mais de 5 dias, a integração será desativada, e os eventos já enfileirados serão retidos por 7 dias.</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>Carga útil muito grande</td>
      <td>Os dados do evento serão divididos em lotes menores e reenviados.</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>Muitas solicitações</td>
      <td>Indica limitação de taxa. Os dados do evento serão reenviados em um padrão de backoff exponencial com jitter. Se o problema persistir por mais de 5 dias, a integração será desativada, e os eventos já enfileirados serão retidos por 7 dias.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }