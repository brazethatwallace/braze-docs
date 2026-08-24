---
nav_title: RudderStack
article_title: RudderStack
description: "Este artigo descreve a parceria entre a Braze e o RudderStack, uma infraestrutura de dados de clientes de código aberto que oferece integração perfeita da Braze para seus aplicativos Android, iOS e web. Com o RudderStack, você pode enviar seus dados de eventos de clientes no app diretamente para a Braze para análise contextual."
page_type: partner
search_tag: Partner

---

# RudderStack

> O [RudderStack](https://rudderstack.com/) é uma infraestrutura de dados de clientes de código aberto para coletar e rotear dados de eventos de clientes para seu data warehouse preferido e dezenas de outros provedores de análise de dados, como a Braze. Ele está pronto para empresas e oferece uma estrutura de transformação robusta para processar seus dados de eventos em tempo real.

A integração entre a Braze e o RudderStack oferece uma integração de SDK nativo para seus aplicativos Android, iOS e web e uma integração de servidor para servidor de seus serviços de back-end.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta do RudderStack | É necessário ter uma [conta RudderStack](https://app.rudderstack.com/) para usar essa parceria. |
| Fonte configurada | Uma [fonte](https://www.rudderstack.com/docs/dashboard-guides/sources/) é essencialmente a origem de qualquer dado enviado ao RudderStack, como websites, apps móveis ou servidores de backend. É necessário configurar a fonte antes de definir a Braze como destino no RudderStack. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com as permissões `users.track`, `users.identify`, `users.delete` e `users.alias.new`.<br><br>Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Chave do app da Braze | Para obter a chave do seu app no dashboard da Braze, acesse **Configurações** > **Configurações do app** > **Identificação** e encontre o nome do seu app. Salve a string do identificador associado.
| Data center | Seu data center está alinhado com a [instância]({{site.baseurl}}/api/basics#endpoints) do seu dashboard da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Adicionar uma fonte {#step-1-add-a-source}

Para começar a enviar dados para a Braze, primeiro você precisa garantir que uma fonte esteja configurada no seu app RudderStack. Acesse o [RudderStack](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started) para saber como configurar sua fonte de dados.

### Etapa 2: Configurar o destino {#step-2-configure-destination}

Agora que sua fonte de dados está configurada, no dashboard do RudderStack, selecione **ADD DESTINATION** em **Destinations**. Na lista de destinos disponíveis, selecione **Braze** e clique em **Next**.

No destino da Braze, forneça a chave do app, a chave da API REST da Braze, o cluster de dados e a opção de SDK nativo (somente modo de dispositivo). A opção de SDK nativo usará o SDK nativo da Braze para enviar eventos se estiver ativada.

### Etapa 3: Escolher o tipo de integração {#step-3-choose-the-type-of-integration}

Você pode escolher integrar as bibliotecas web e nativas do lado do cliente do RudderStack com a Braze usando uma das seguintes abordagens:

- [Integração lado a lado / modo de dispositivo](#device-mode)**:** O RudderStack enviará os dados do evento para a Braze diretamente do seu cliente (navegador ou aplicativo móvel).
- [Servidor para servidor / modo de nuvem](#cloud-mode)**:** O SDK da Braze envia os dados do evento diretamente para o RudderStack, que então os transforma e encaminha para a Braze.
- [Modo híbrido](#hybrid-mode)**:** Use o modo híbrido para enviar eventos gerados automaticamente e gerados pelo usuário no iOS e Android para a Braze usando uma única conexão.

{% alert note %}
Para saber mais sobre os [modos de conexão](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/) do RudderStack e os benefícios de cada um.
{% endalert %}

#### Integração lado a lado (modo de dispositivo) {#device-mode}

Com esse modo, você pode enviar seus eventos para a Braze usando o SDK da Braze configurado no seu website ou app móvel.

Configure os mapeamentos para o SDK do RudderStack na sua plataforma no repositório GitHub da Braze, conforme descrito em [métodos compatíveis](#supported-methods):

- [Android](https://github.com/rudderlabs/rudder-integration-braze-android)
- [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master)
- [Swift](https://github.com/rudderlabs/rudder-integration-braze-swift)
- [Web](https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Braze)
- [React Native](https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native)
- [Flutter](https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter)

Para concluir a integração no modo de dispositivo, consulte as instruções detalhadas do RudderStack para [adicionar a Braze ao seu projeto](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration).

#### Integração servidor para servidor (modo de nuvem) {#cloud-mode}

Nesse modo, o SDK envia os dados do evento diretamente para o servidor do RudderStack. O RudderStack então transforma esses dados e os encaminha para o destino desejado. Essa transformação é feita no backend do RudderStack usando o módulo transformer do RudderStack.

Para ativar a integração, você precisará mapear os métodos do RudderStack para a Braze, conforme descrito em [métodos compatíveis](#supported-methods).

{% alert note %}
Os SDKs do lado do servidor do RudderStack (Java, Python, Node.js, Go, Ruby) suportam apenas o modo de nuvem. Isso porque seus SDKs do lado do servidor operam no backend do RudderStack e não conseguem carregar nenhum SDK específico da Braze.
{% endalert %}

{% alert important %}
A integração servidor para servidor não suporta recursos de interface da Braze, como notificações por push ou envio de mensagens no app. Esses recursos são, no entanto, suportados pela integração no modo de dispositivo.
{% endalert %}

#### Modo híbrido {#hybrid-mode}

Use o modo híbrido para enviar todos os eventos para a Braze a partir das suas fontes iOS e Android.

Quando você escolhe o modo híbrido para enviar eventos para a Braze, o RudderStack:
1. Inicializa o SDK da Braze.
2. Envia todos os eventos gerados pelo usuário (identify, track, page, screen e group) para a Braze somente pelo modo de nuvem e impede que sejam enviados pelo modo de dispositivo.
3. Envia os eventos gerados automaticamente (mensagens no app, notificações por push que requerem o SDK da Braze) pelo modo de dispositivo.

Para [enviar eventos pelo modo híbrido](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode), use a opção de modo híbrido ao conectar sua fonte ao destino da Braze. Em seguida, adicione a integração da Braze ao seu projeto.

## Etapa 4: Definir configurações adicionais {#step-4-configure-additional-settings}

Após concluir a configuração inicial, defina as seguintes configurações para receber seus dados corretamente na Braze:

- **Enable subscription groups in group call**: Ative essa configuração para enviar o status do grupo de inscrições nos seus eventos de grupo. Para saber mais, consulte [Group](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group).
- **Use Custom Attributes Operation**: Ative essa configuração se quiser usar a funcionalidade de [atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) na Braze para criar Segments e personalizar suas mensagens usando um objeto de atributo personalizado. Para saber mais, consulte [Send user traits as nested custom attributes](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes).
- **Track events for anonymous users**: Ative essa configuração para rastrear a atividade de usuários anônimos e enviar essas informações para a Braze.

### Configurações do modo de dispositivo {#device-mode-settings}

As configurações a seguir são aplicáveis somente se você estiver enviando eventos para a Braze pelo [modo de dispositivo](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode):

- **Client-side Events Filtering**: Essa configuração permite especificar quais eventos devem ser bloqueados ou autorizados a fluir para a Braze. Para saber mais sobre essa configuração, consulte [Client-side Events Filtering](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/).
- **Deduplicate Traits**: Ative essa configuração para deduplicar os traços do usuário na chamada [`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify).
- **Show Braze logs**: Essa configuração é aplicável somente ao usar o [SDK JavaScript](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/) como fonte. Ative-a para exibir os logs da Braze para seus usuários.
- **OneTrust Cookie Categories**: Essa configuração permite associar os grupos de consentimento de cookies do [OneTrust](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/) à Braze.

## Métodos compatíveis {#supported-methods}

A Braze é compatível com os métodos RudderStack identify, track, screen, page, group e alias.

{% tabs %}
{% tab Identify %}

O [método `identify`](https://rudderstack.com/docs/destinations/marketing/braze/#identify) do RudderStack associa os usuários às suas ações. O RudderStack captura um ID de usuário exclusivo e traços opcionais associados a esse usuário, como nome, e-mail, endereço IP etc.

**Gerenciamento de delta para chamadas identify**<br>
Se você envia eventos para a Braze por meio do modo de dispositivo, é possível economizar custos deduplicando suas chamadas `identify`. Para isso, ative a configuração Deduplicate Traits no dashboard. O RudderStack então envia apenas os atributos (traços) alterados ou modificados para a Braze.

**Exclusão de um usuário**<br>
Você pode excluir um usuário na Braze usando a regulação [Suppression with Delete](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation) da [API de Regulação de Dados](https://www.rudderstack.com/docs/api/data-regulation-api/) do RudderStack.

{% endtab %}
{% tab Track %}

O [método `track`](https://rudderstack.com/docs/destinations/marketing/braze/#track) do RudderStack captura todas as atividades dos usuários e as propriedades associadas a essas atividades.

**Pedido concluído**<br>
Ao usar a [API de eCommerce do RudderStack](https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/) para chamar o método track para um evento com o nome `Order Completed`, o RudderStack envia os produtos listados nesse evento para a Braze como [`purchases`]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data).

{% endtab %}
{% tab Screen %}

O [método `screen`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen) do RudderStack permite registrar as visualizações de tela móvel dos seus usuários com qualquer informação adicional sobre a tela visualizada.

{% endtab %}
{% tab Page %}

O [método `page`](https://rudderstack.com/docs/destinations/marketing/braze/#page) do RudderStack permite registrar as visualizações de páginas do seu website. Ele também captura qualquer outra informação relevante sobre essa página.

{% endtab %}
{% tab Group %}

O [método `group`](https://rudderstack.com/docs/destinations/marketing/braze/#group) do RudderStack permite associar um usuário a um grupo.

**Status do grupo de inscrições**<br>
Para atualizar o status do grupo de inscrições, ative a configuração "Enable subscription groups in group call" no dashboard do RudderStack e envie o status do grupo de inscrições na chamada group.

{% endtab %}
{% tab Alias %}

O [método `alias`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias) do RudderStack permite mesclar diferentes identidades de um usuário conhecido. Note que o RudderStack é compatível com a chamada alias para a Braze apenas no modo cloud.

{% endtab %}
{% endtabs %}

## Enviar traits de usuário como atributos personalizados aninhados {#send-user-traits-as-nested-custom-attributes}

Você pode enviar os traits de usuário para a Braze como atributos personalizados aninhados e realizar operações de adição, atualização e remoção neles. Para isso, ative a configuração "Use Custom Attributes Operation dashboard" no RudderStack ao configurar o destino da Braze. Esse recurso está disponível apenas no modo cloud.

Você pode enviar os traits de usuário como atributos personalizados aninhados nos seus eventos `identify` no seguinte formato:
```javascript
rudderanalytics.identify("1hKOmRA4GRlm", {
  "cars": {
    "add": [{
      "age": 27,
      "id": 1,
      "name": "Alex Keener"
    }],
    "update": [{
        "age": 30,
        "id": 2,
        "identifier": "id",
        "name": "Rowan"
      },
      {
        "age": 27,
        "id": 1,
        "identifier": "id",
        "name": "Alex"
      }
    ]
  },
  "country": "USA",
  "email": "alex@example.com",
  "firstName": "Alex",
  "gender": "M",
  "pets": [{
      "breed": "beagle",
      "id": 1,
      "name": "Scooby",
      "type": "dog"
    },
    {
      "breed": "calico",
      "id": 2,
      "name": "Garfield",
      "type": "cat"
    }
  ]
})
```

Para enviar os traits de usuário como atributos personalizados de usuário por meio das chamadas `track`, `page` ou `screen`, passe `traits` como um campo contextual no evento:
```javascript
rudderanalytics.track("Product Viewed", {
    revenue: 8.99,
    currency: "USD",
 },{
  "traits": {
    "cars": {
      "add": [{
        "age": 27,
        "id": 1,
        "name": "Alex Keener"
      }],
      "update": [{
          "age": 30,
          "id": 2,
          "identifier": "id",
          "name": "Alex"
        },
        {
          "age": 27,
          "id": 1,
          "identifier": "id",
          "name": "Rowan"
        }
      ]
    },
    "city": "Disney",
    "country": "USA",
    "email": "alexa@example.com",
    "firstName": "Alexa",
    "gender": "woman",
    "pets": [{
        "breed": "beagle",
        "id": 1,
        "name": "Scooby",
        "type": "dog"
      },
      {
        "breed": "calico",
        "id": 2,
        "name": "Garfield",
        "type": "cat"
      }
    ]
  }
});
```

{% alert note %}
Para as operações de atualização e remoção, `identifier` é uma chave obrigatória. Se as operações de adição, atualização ou remoção não estiverem presentes no array aninhado, o RudderStack usará a operação de criação para criar as propriedades por padrão. Consulte [Array de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) para saber mais sobre o envio de atributos personalizados aninhados.
{% endalert %}

## Solução de problemas {#troubleshooting}

### Vejo "[Braze Deduplication]: Duplicate user detected, the user is dropped" nos logs do RudderStack {#i-see-braze-deduplication-duplicate-user-detected-the-user-is-dropped-in-rudderstack-logs}

Essa mensagem é do RudderStack quando a opção **Deduplicate Traits** está ativada e o RudderStack descarta traits de usuário inalterados antes de encaminhá-los para a Braze. Não se trata de um erro da Braze.

O RudderStack compara os traits recebidos de `identify` e `track` com o perfil de usuário e ignora atributos sem alteração para reduzir o uso de pontos de dados da Braze. Para saber mais, consulte o guia [User Trait Deduplication in Braze](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/trait-deduplication/) do RudderStack.

Se você precisar que todos os traits sejam enviados em cada chamada, desative a opção **Deduplicate Traits** nas configurações de destino da Braze no RudderStack. Esteja ciente de que isso pode aumentar o consumo de pontos de dados da Braze.