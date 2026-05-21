---
nav_title: Eventos
article_title: Eventos
page_order: 0
hidden: true
page_type: reference
description: "Este artigo descreve os diferentes eventos na Braze — eventos padrão, eventos de compra e eventos personalizados — e suas finalidades."
---

# Eventos {#events}

> Esta página aborda os diferentes eventos na Braze e suas finalidades.

A Braze utiliza alguns tipos diferentes de eventos para fornecer uma compreensão abrangente do comportamento do usuário e do engajamento com a sua marca. Cada tipo de evento tem uma finalidade única:

- [Eventos padrão](#standard-events): Fornecem uma compreensão básica do engajamento do usuário com seu app ou site.
- [Eventos de compra](#purchase-events): Essenciais para entender o comportamento de compra dos usuários e para rastrear a receita.
- [Eventos personalizados](#custom-events): Fornecem insights mais profundos sobre comportamentos dos usuários que são exclusivos do seu app ou negócio.

Ao rastrear esses diferentes tipos de eventos, você pode obter uma compreensão mais profunda dos seus usuários, o que pode orientar suas estratégias de marketing, ajudar a otimizar seu app e permitir que você ofereça uma experiência de usuário mais personalizada. Vamos lá!

## Eventos padrão {#standard-events}

Na Braze, eventos padrão são ações predefinidas que a Braze reconhece em toda a sua plataforma. Diferentemente dos [eventos personalizados](#custom-events), você não precisa criar ou nomear eventos padrão — eles já vêm integrados. No entanto, nem todos os eventos padrão são rastreados da mesma forma.

Os seguintes eventos são rastreados automaticamente após a integração de SDK:

- Início de sessão
- Fim de sessão

Os seguintes eventos são rastreados após configuração adicional:

- [Eventos de compra](#purchase-events): Sua equipe de desenvolvimento registra esses eventos usando os métodos de compra do SDK. Para saber mais, consulte a seção Eventos de compra.
- Eventos de engajamento de e-mail (como aberturas de e-mail e cliques em links): Rastreados pela Braze quando você configura o e-mail da Braze e ativa o rastreamento de e-mail.
- Eventos de engajamento de push (como aberturas e cliques em notificações por push): Rastreados após você configurar o push na Braze e integrar o tratamento de push com o SDK da Braze no seu app.

Como profissional de marketing, você pode usar eventos padrão para entender o comportamento e o engajamento dos usuários. Por exemplo, os dados de sessão mostram com que frequência os usuários abrem seu app ou site, enquanto os eventos de compra ajudam a rastrear a receita ao longo do tempo.

## Eventos de compra {#purchase-events}

Eventos de compra registram e rastreiam as compras feitas pelos seus usuários. Após integrar o SDK da Braze, sua equipe de desenvolvimento pode registrar compras usando os métodos de compra do SDK. Quando você usa eventos de compra para rastrear compras, é possível monitorar sua receita ao longo do tempo e em diferentes fontes de receita diretamente na Braze.

Os eventos de compra registram as seguintes informações principais sobre uma compra:

- ID do produto (geralmente o nome ou a categoria do produto)
- Moeda
- Preço
- Quantidade

Você pode então usar esses dados para segmentar seus usuários com base no lifetime value, frequência de compra, compras específicas e muito mais.

A Braze também oferece suporte a compras em múltiplas moedas. Se uma compra for registrada em uma moeda diferente de USD, ela será exibida no dashboard da Braze em USD, com base na taxa de câmbio da data em que a compra foi registrada.

Para saber mais, visite nosso artigo dedicado sobre [eventos de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/).

{% details Exemplo de implementação %}

Observe que a implementação real de eventos de compra exigirá algum conhecimento técnico, pois envolve a integração do SDK da Braze com o seu app. Seu gerente de sucesso do cliente orientará sua equipe nesse processo como parte da sua integração, mas as etapas gerais são as seguintes:

1. **Integrar o SDK da Braze:** Antes de registrar qualquer evento, você precisa integrar o SDK da Braze no seu app.
2. **Registrar o evento de compra:** Após a integração do SDK, você pode registrar um evento de compra sempre que um usuário fizer uma compra no seu app. Isso geralmente é feito na função ou método chamado quando uma compra é concluída.

Aqui está um exemplo de como registrar um evento de compra em um app iOS usando Swift:

```swift
Appboy.sharedInstance()?.logPurchase("product_name", inCurrency: "USD", atPrice: NSDecimalNumber(string: "1.99"), withQuantity: 1)
```

Neste exemplo, "product_name" é o nome do produto que foi comprado, "USD" é a moeda da compra, "1.99" é o preço do produto e "1" é a quantidade comprada.

{:start="3"}
3. **Visualizar o evento de compra no dashboard da Braze:** Após o evento de compra ser registrado, você pode visualizá-lo no dashboard da Braze. Você pode usar esses dados para analisar sua receita, segmentar seus usuários e muito mais.

Lembre-se de que a implementação exata pode variar dependendo da plataforma (iOS, Android, Web) e dos requisitos específicos do seu app.

{% enddetails %}

## Eventos personalizados {#custom-events}

Eventos personalizados são eventos que você define com base nas ações específicas que deseja rastrear dentro do seu app ou site. A Braze não os rastreia automaticamente — você deve configurar esses eventos manualmente na implementação do SDK da Braze. Eventos personalizados podem ser qualquer coisa, desde um usuário completando uma fase em um jogo até um usuário atualizando suas informações de perfil.

Aqui está um exemplo de como registrar um evento personalizado em um app iOS usando Swift:

```swift
Appboy.sharedInstance()?.logCustomEvent("completed_level")
```

Neste exemplo, "completed_level" é o nome do evento personalizado que é registrado quando um usuário completa uma fase em um jogo. Esse evento personalizado é então registrado no perfil de usuário na Braze, e você pode usá-lo para disparar campaigns e personalizar o envio de mensagens.

Para saber mais, visite nosso artigo dedicado sobre [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/).

{% details Exemplo de implementação %}

Assim como os eventos de compra, os eventos personalizados exigem configuração adicional. Aqui está um processo geral para implementar eventos personalizados na Braze:

1. **Integrar o SDK da Braze:** Antes de registrar qualquer evento, você precisa integrar o SDK da Braze no seu app.
2. **Definir seu evento personalizado:** Decida qual ação no seu app você deseja rastrear como um evento personalizado. Pode ser qualquer coisa significativa para o seu app, como um usuário completando uma fase em um jogo, um usuário atualizando seu perfil ou um usuário fazendo um tipo específico de compra.
3. **Registrar o evento personalizado:** Após definir seu evento personalizado, você pode registrá-lo no código do seu app. Isso geralmente é feito na função ou método que é chamado quando a ação ocorre.

Aqui está um exemplo de como registrar um evento personalizado em um app iOS usando Swift:

```swift
Appboy.sharedInstance()?.logCustomEvent("updated_profile")
```

Neste exemplo, "updated_profile" é o nome do evento personalizado que é registrado quando um usuário atualiza seu perfil.

{:start="4"}
4. **Adicionar propriedades ao seu evento personalizado (opcional):** Se você quiser capturar detalhes adicionais sobre o evento personalizado, pode adicionar propriedades a ele. Isso é feito passando um dicionário de propriedades ao registrar o evento.

Aqui está um exemplo de como registrar um evento personalizado com propriedades em um app iOS usando Swift:

```swift
let properties: [AnyHashable: Any] = ["Property Name": "Property Value"]
Appboy.sharedInstance()?.logCustomEvent("updated_profile", withProperties: properties)
```

Neste exemplo, o evento personalizado tem uma propriedade chamada "Property Name" com o valor "Property Value".

{:start="5"}
5. **Visualizar o evento personalizado no dashboard da Braze:** Após o evento personalizado ser registrado, você pode visualizá-lo no dashboard da Braze. Você pode usar esses dados para analisar o comportamento dos usuários, segmentar seus usuários e muito mais.

{% enddetails %}

<!--

### Using custom events instead of purchase events to track purchases

You might prefer to use custom events to track purchases if you need to capture more specific or additional information about the purchase that the standard purchase event doesn't cover. Here's what you can do with custom events that you can't accomplish with purchase events:

- **Custom definitions:** Custom events can be defined based on any significant action within your app. This level of customization is not available with standard purchase events, which are predefined and specifically designed to track purchases.
- **Additional properties:** You can log additional properties to custom events that provide more context about the event. For example, you could log a custom event when a user makes a purchase and include properties such as the product category or the payment method. This is not possible with standard purchase events, which have a fixed schema that only tracks the product name, currency, price, and quantity.
- **Event frequency:** Custom events allow you to track the frequency of specific actions. With purchase events, you can only track the occurrence of purchases, not other types of actions.

#### Use case 1

Let's say you have an eCommerce app, and you want to track the purchase itself and the product category. The standard purchase event in Braze does not capture this level of detail, so you could use a custom event instead.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Product Category": "Electronics"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the product category is "Electronics". Now you can segment your users based on the product categories they purchase from.

#### Use case 2

Consider a fitness app where users can purchase personal training sessions or premium workout plans. In this case, you might want to track these purchases as custom events to capture additional details about the purchase.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Workout Plan": "10 Sessions Personal Training"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the workout plan is "10 Sessions Personal Training". Now you can segment your users based on the types of workout plans they purchase.

-->