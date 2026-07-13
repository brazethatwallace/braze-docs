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
| Conta do RudderStack | É necessário ter uma [conta RudderStack](https://app.rudderstack.com/) para usar a parceria. |
| Fonte configurada | Uma [fonte](https://www.rudderstack.com/docs/dashboard-guides/sources/) é essencialmente a origem de qualquer dado enviado ao RudderStack, como sites, apps móveis ou servidores back-end. É necessário configurar a fonte antes de configurar a Braze como um destino no RudderStack. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com as permissões `users.track`, `users.identify`, `users.delete` e `users.alias.new`.<br><br>Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Chave do app da Braze | Para obter sua chave do app no dashboard da Braze, acesse **Configurações** > **Configurações do app** > **Identificação** e encontre o nome do seu app. Salve a string de identificador associada.
| Data center | Seu data center se alinha com sua [instância]({{site.baseurl}}/api/basics#endpoints) do dashboard da Braze.  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Adicionar uma fonte {#step-1-add-a-source}

Para começar a enviar dados para a Braze, primeiro você precisa confirmar se há uma fonte configurada no seu app do RudderStack. Visite o [RudderStack](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started) para saber como configurar sua fonte de dados.

### Etapa 2: Configurar o destino {#step-2-configure-destination}

Agora que sua fonte de dados está configurada, no dashboard do RudderStack, selecione **ADD DESTINATION** em **Destinations**. Na lista de destinos disponíveis, selecione **Braze** e clique em **Next**.

No destino da Braze, forneça a chave do app, a chave da API REST da Braze, o cluster de dados e a opção de SDK nativo (somente no modo dispositivo). Se ativada, a opção de SDK nativo usará o SDK nativo da Braze para enviar eventos.

### Etapa 3: Escolher o tipo de integração {#step-3-choose-the-type-of-integration}

Você pode optar por integrar as bibliotecas web e nativas do lado do cliente do RudderStack com a Braze usando uma das seguintes abordagens:

- [Integração lado a lado / modo dispositivo](#device-mode)**:** O RudderStack enviará os dados do evento para a Braze diretamente do seu cliente (navegador ou aplicativo móvel).
- [Servidor para servidor / modo nuvem](#cloud-mode)**:** O SDK da Braze envia os dados do evento diretamente para o RudderStack, onde são transformados e reencaminhados para a Braze.
- [Modo híbrido](#hybrid-mode)**:** Use o modo híbrido para enviar eventos gerados automaticamente e pelo usuário no iOS e Android para a Braze usando uma única conexão.

{% alert note %}
Saiba mais sobre os [modos de conexão](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/) do RudderStack e os benefícios de cada um.
{% endalert %}

#### Integração lado a lado (modo dispositivo) {#device-mode}

Com esse modo, você pode enviar seus eventos para a Braze usando o SDK da Braze configurado em seu site ou app móvel.

Configure os mapeamentos para o SDK do RudderStack para sua plataforma no repositório do Braze no GitHub, conforme descrito em [métodos suportados](#supported-methods):

- [Android](https://github.com/rudderlabs/rudder-integration-braze-android)
- [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master)
- [Swift](https://github.com/rudderlabs/rudder-integration-braze-swift)
- [Web](https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Braze)
- [React Native](https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native)
- [Flutter](https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter)

Para concluir a integração do modo dispositivo, consulte as instruções detalhadas do RudderStack para [adicionar a Braze ao seu projeto](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration).

#### Integração de servidor para servidor (modo nuvem) {#cloud-mode}

Nesse modo, o SDK envia os dados de evento diretamente para o servidor do RudderStack. Em seguida, o RudderStack transforma esses dados e os encaminha para o destino desejado. Essa transformação é feita no back-end do RudderStack usando o módulo de transformação do RudderStack.

Para ativar a integração, você precisará mapear os métodos do RudderStack para a Braze, conforme descrito em [métodos suportados](#supported-methods).

{% alert note %}
Os SDKs do lado do servidor do RudderStack (Java, Python, Node.js, Go, Ruby) suportam apenas o modo nuvem. Isso ocorre porque seus SDKs do lado do servidor operam no back-end do RudderStack e não podem carregar nenhum SDK específico da Braze.
{% endalert %}

{% alert important %}
A integração de servidor para servidor não oferece suporte aos recursos da interface da Braze, como notificações por push ou envio de mensagens no app. Esses recursos são, no entanto, suportados pela integração do modo dispositivo.
{% endalert %}

#### Modo híbrido {#hybrid-mode}

Use o modo híbrido para enviar todos os eventos para a Braze a partir de suas fontes iOS e Android.

Quando você escolhe o modo híbrido para enviar eventos para a Braze, o RudderStack:
1. Inicializa o SDK da Braze.
2. Envia todos os eventos gerados pelo usuário (identify, track, page, screen e group) para a Braze somente pelo modo nuvem e impede que sejam enviados pelo modo dispositivo.
3. Envia os eventos gerados automaticamente (mensagens no app, notificações por push que requerem o SDK da Braze) por meio do modo dispositivo.

Para [enviar eventos por meio do modo híbrido](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode), use a opção de modo híbrido ao conectar sua origem ao destino da Braze. Em seguida, adicione a integração da Braze ao seu projeto.

## Etapa 4: Configurar definições adicionais {#step-4-configure-additional-settings}

Após concluir a configuração inicial, defina as seguintes configurações para receber corretamente seus dados na Braze:

- **Ativar grupos de inscrições em chamadas de grupo**: Ative essa configuração para enviar o status do grupo de inscrições em seus eventos de grupo. Para saber mais, consulte [Group](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group).
- **Usar operação de atributos personalizados**: Ative essa configuração se quiser usar a funcionalidade de [atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) na Braze para criar segmentos e personalizar suas mensagens usando um objeto de atributo personalizado. Para saber mais, consulte [Enviar características de usuário como atributos personalizados aninhados](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes).
- **Rastrear eventos para usuários anônimos**: Ative essa configuração para rastrear a atividade de usuários anônimos e enviar essas informações para a Braze.

### Configurações do modo dispositivo {#device-mode-settings}

As configurações a seguir são aplicáveis somente se você estiver enviando eventos para a Braze por meio do [modo dispositivo](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode):

- **Filtragem de eventos no lado do cliente**: Essa configuração permite que você especifique quais eventos devem ser bloqueados ou autorizados a fluir para a Braze. Para saber mais sobre essa configuração, consulte [Filtragem de eventos no lado do cliente](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/).
- **Desduplicar características**: Ative essa configuração para desduplicar as características do usuário na chamada [`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify).
- **Mostrar registros da Braze**: Essa configuração é aplicável somente ao usar o [SDK para JavaScript](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/) como fonte. Ative-a para mostrar os registros da Braze aos seus usuários.
- **Categorias de cookies da OneTrust**: Essa configuração permite que você associe os grupos de consentimento de cookies da [OneTrust](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/) à Braze.

## Métodos suportados {#supported-methods}

A Braze oferece suporte aos métodos identify, track, screen, page, group e alias do RudderStack.

{% tabs %}
{% tab Identify %}

O [método `identify`](https://rudderstack.com/docs/destinations/marketing/braze/#identify) do RudderStack associa os usuários às suas ações. O RudderStack captura um ID de usuário exclusivo e características opcionais associadas a esse usuário, como nome, e-mail, endereço IP etc.

**Gerenciamento de delta para chamadas identify**<br>
Se você enviar eventos para a Braze usando o modo dispositivo, poderá economizar custos ao desduplicar suas chamadas `identify`. Para fazer isso, ative a configuração de desduplicação de características no dashboard. O RudderStack envia apenas os atributos alterados ou modificados (traits) para a Braze.

**Exclusão de um usuário**<br>
É possível excluir um usuário na Braze usando a [regulamentação Suppression with Delete](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation) da [API de regulamentação de dados](https://www.rudderstack.com/docs/api/data-regulation-api/) do RudderStack.

{% endtab %}
{% tab Track %}

O [método `track`](https://rudderstack.com/docs/destinations/marketing/braze/#track) do RudderStack captura todas as atividades do usuário e as propriedades associadas a essas atividades.

**Pedido concluído**<br>
Ao usar a [API de eCommerce do RudderStack](https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/) para chamar o método track de um evento com o nome `Order Completed`, o RudderStack envia os produtos listados nesse evento para a Braze como [`purchases`]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data).

{% endtab %}
{% tab Screen %}

O [método `screen`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen) do RudderStack permite gravar as visualizações de tela móvel dos usuários com qualquer informação adicional sobre a tela visualizada.

{% endtab %}
{% tab Page %}

O [método `page`](https://rudderstack.com/docs/destinations/marketing/braze/#page) do RudderStack permite que você registre as visualizações de página do seu site. Ele também captura qualquer outra informação relevante sobre essa página.

{% endtab %}
{% tab Group %}

O [método `group`](https://rudderstack.com/docs/destinations/marketing/braze/#group) do RudderStack permite que você associe um usuário a um grupo.

**Status do grupo de inscrições**<br>
Para atualizar o status do grupo de inscrições, ative a configuração "Ativar grupos de inscrições na chamada de grupo" no dashboard do RudderStack e envie o status do grupo de inscrições na chamada de grupo.

{% endtab %}
{% tab Alias %}

O [método `alias`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias) do RudderStack permite mesclar diferentes identidades de um usuário conhecido. Observe que o RudderStack oferece suporte à chamada de alias para a Braze somente no modo nuvem.

{% endtab %}
{% endtabs %}

## Enviar características do usuário como atributos personalizados aninhados {#send-user-traits-as-nested-custom-attributes}

É possível enviar as características do usuário para a Braze como atributos personalizados aninhados e realizar operações de adição, atualização e remoção sobre eles. Para fazer isso, ative a configuração "Use Custom Attributes Operation dashboard" no RudderStack ao configurar o destino da Braze. Esse recurso só está disponível no modo nuvem.

É possível enviar as características do usuário como atributos personalizados aninhados em seus eventos `identify` no seguinte formato:
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

Para enviar as características do usuário como atributos personalizados por meio das chamadas `track`, `page` ou `screen`, passe `traits` como um campo contextual no evento:
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
Para as operações de atualização e remoção, `identifier` é uma chave obrigatória. Se as operações de adição, atualização ou remoção não estiverem presentes no vetor aninhado, o RudderStack usará a operação de criação para criar as propriedades por padrão. Consulte [Vetor de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) para saber mais sobre o envio de atributos personalizados aninhados.
{% endalert %}