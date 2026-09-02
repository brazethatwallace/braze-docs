# Feature Flags

> As Feature Flags permitem ativar ou desativar remotamente a funcionalidade para uma seleção específica ou aleatória de usuários. É importante ressaltar que elas permitem ativar e desativar um recurso em produção sem implementação adicional de código ou atualizações na loja de aplicativos. Isso permite que você lance novos recursos com segurança e confiança.

{% alert tip %}
Quando estiver pronto para criar suas próprias Feature Flags, consulte [Criar Feature Flags]({{site.baseurl}}/developer_guide/feature_flags/create).
{% endalert %}

## Pré-requisitos {#prerequisites}

Estas são as versões mínimas do SDK or kit de desenvolvimento de software necessárias para começar a usar Feature Flags:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## Casos de uso {#use-cases}

### Lançamentos graduais {#gradual-rollouts}

Use Feature Flags para ativar gradualmente recursos para uma amostra da população. Por exemplo, você pode fazer um lançamento suave de um novo recurso primeiro para seus usuários VIP. Essa estratégia ajuda a mitigar riscos associados ao envio de novos recursos para todos de uma vez e a detectar bugs mais cedo.

![Imagem animada do controle deslizante de tráfego de lançamento indo de 0% a 100%.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %})

Por exemplo, digamos que decidimos adicionar um novo link de "Suporte por Chat ao Vivo" ao nosso app para um atendimento ao cliente mais rápido. Poderíamos lançar esse recurso para todos os clientes de uma vez. No entanto, um lançamento amplo traz riscos, como:

* Nossa equipe de suporte ainda está em treinamento, e os clientes podem abrir tickets de suporte após o lançamento. Isso não nos dá margem caso a equipe de suporte precise de mais tempo.
* Não temos certeza do volume real de novos casos de suporte que receberemos, então talvez não tenhamos a equipe dimensionada adequadamente.
* Se nossa equipe de suporte ficar sobrecarregada, não temos uma estratégia para desativar rapidamente esse recurso.
* Podem surgir bugs no widget de chat, e não queremos que os clientes tenham uma experiência negativa.

Com as Feature Flags da Braze, podemos fazer um lançamento gradual do recurso e mitigar todos esses riscos:

* Vamos ativar o recurso "Suporte por Chat ao Vivo" quando a equipe de suporte disser que está pronta.
* Vamos ativar esse novo recurso apenas para 10% dos usuários para verificar se temos a equipe dimensionada adequadamente.
* Se houver algum bug, podemos desativar rapidamente o recurso em vez de correr para lançar uma nova versão.

Para fazer o lançamento gradual desse recurso, podemos [criar uma Feature Flag]({{site.baseurl}}/developer_guide/feature_flags/create) chamada "Live Chat Widget."

![Detalhes da Feature Flag para um exemplo chamado Live Chat Widget. O ID é enable_live_chat. A descrição dessa Feature Flag indica que o widget de chat ao vivo será exibido na página de suporte.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %})

No código do nosso app, vamos exibir o botão **Start Live Chat** apenas quando a Feature Flag da Braze estiver ativada:

{% tabs %}
{% tab JavaScript %}

```javascript
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// Get the initial value from the Braze SDK
const featureFlag = braze.getFeatureFlag("enable_live_chat");
const [liveChatEnabled, setLiveChatEnabled] = useState(featureFlag.enabled);

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(() => {
    const newValue = braze.getFeatureFlag("enable_live_chat").enabled;
    setLiveChatEnabled(newValue);
});

// Only show the Live Chat if the Braze SDK determines it is enabled
return (<>
  Need help? <button>Email Our Team</button>
  {liveChatEnabled && <button>Start Live Chat</button>}
</>)
```

{% endtab %}
{% tab Java %}

```java
// Get the initial value from the Braze SDK
FeatureFlag featureFlag = braze.getFeatureFlag("enable_live_chat");
Boolean liveChatEnabled = featureFlag != null && featureFlag.getEnabled();

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(event -> {
  FeatureFlag newFeatureFlag = braze.getFeatureFlag("enable_live_chat");
  Boolean newValue = newFeatureFlag != null && newFeatureFlag.getEnabled();
  liveChatEnabled = newValue;
});

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Get the initial value from the Braze SDK
val featureFlag = braze.getFeatureFlag("enable_live_chat")
var liveChatEnabled = featureFlag?.enabled

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates() { event ->
  val newValue = braze.getFeatureFlag("enable_live_chat")?.enabled
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}

```

{% endtab %}
{% tab Swift %}

{% alert note %}
Acessar `braze.featureFlags.featureFlags` ou `braze.featureFlags.featureFlag(id:)` bloqueia a thread que faz a chamada até que o SDK or kit de desenvolvimento de software conclua suas operações pós-inicialização. Para contextos na thread principal ou sensíveis à latência, use [`getAllFeatureFlags(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/getallfeatureflags(_:)).

```swift
// Non-blocking — completion handler always delivers on the main thread.
braze.featureFlags.getAllFeatureFlags { flags in
  let liveChatEnabled = flags.first(where: { $0.id == "enable_live_chat" })?.enabled ?? false
  liveChatView.isHidden = !liveChatEnabled
}
```

Em Objective-C:

```objc
[braze.featureFlags getAllFeatureFlagsWithCompletion:^(NSArray<BRZFeatureFlag *> *flags) {
  // Use `flags` here.
}];
```
{% endalert %}

```swift
// Get the initial value from the Braze SDK
let featureFlag = braze.featureFlags.featureFlag(id: "enable_live_chat")
var liveChatEnabled = featureFlag?.enabled ?? false

// Listen for updates from the Braze SDK
braze.featureFlags.subscribeToUpdates() { _ in
  let newValue = braze.featureFlags.featureFlag(id: "enable_live_chat")?.enabled ?? false
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
liveChatView.isHidden = !liveChatEnabled
```

{% endtab %}
{% endtabs %}

### Controlar variáveis do app remotamente {#remotely-control-app-variables}

Use Feature Flags para modificar a funcionalidade do seu app em produção. Isso pode ser especialmente importante para apps mobile, onde as aprovações das lojas de aplicativos impedem a implementação rápida de mudanças para todos os usuários.

Por exemplo, digamos que nossa equipe de marketing quer listar nossas vendas e promoções atuais na navegação do nosso app. Normalmente, nossos engenheiros precisam de uma semana de antecedência para qualquer mudança e três dias para a revisão da loja de aplicativos. Mas com o Dia de Ação de Graças, Black Friday, Cyber Monday, Hanukkah, Natal e Ano Novo, tudo dentro de dois meses, não conseguiremos cumprir esses prazos apertados.

Com as Feature Flags, podemos deixar a Braze controlar o conteúdo do link de navegação do nosso app, permitindo que nosso gerente de marketing faça alterações em minutos, em vez de dias.

Para configurar remotamente esse recurso, vamos criar uma nova Feature Flag chamada `navigation_promo_link` e definir as seguintes propriedades iniciais:

![Feature Flag com propriedades de link e texto direcionando para uma página genérica de vendas.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %})

No nosso app, usaremos métodos getter da Braze para recuperar as propriedades dessa Feature Flag e construir os links de navegação com base nesses valores:

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation_promo_link");
// Check if the feature flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// Read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// Read the "text" property
const [promoText, setPromoText] = useState(featureFlag.getStringProperty("text"));

return (<>
  <div>
    <a href="/">Home</a>
    { promoEnabled && <a href={promoLink}>{promoText}</a> }
    <a href="/products">Products</a>
    <a href="/categories">Categories
  </div>
</>)
```

{% endtab %}
{% tab Java %}

```java
// liveChatView is the View container for the Live Chat UI
FeatureFlag featureFlag = braze.getFeatureFlag("navigation_promo_link");
if (featureFlag != null && featureFlag.getEnabled()) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
liveChatView.setPromoLink(featureFlag.getStringProperty("link"));
liveChatView.setPromoText(featureFlag.getStringProperty("text"));

```

{% endtab %}
{% tab Kotlin %}

```kotlin
// liveChatView is the View container for the Live Chat UI
val featureFlag = braze.getFeatureFlag("navigation_promo_link")
if (featureFlag?.enabled == true) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}
liveChatView.promoLink = featureFlag?.getStringProperty("link")
liveChatView.promoText = featureFlag?.getStringProperty("text")
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "navigation_promo_link")
if let featureFlag {
  liveChatView.isHidden = !featureFlag.enabled
} else {
  liveChatView.isHidden = true
}
liveChatView.promoLink = featureFlag?.stringProperty("link")
liveChatView.promoText = featureFlag?.stringProperty("text")
```

{% endtab %}
{% endtabs %}

Agora, na véspera do Dia de Ação de Graças, precisamos apenas alterar os valores dessas propriedades no dashboard da Braze.

![Feature Flag com propriedades de link e texto direcionando para uma página de vendas de Dia de Ação de Graças.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %})

Como resultado, na próxima vez que alguém abrir o app, verá as novas ofertas de Dia de Ação de Graças.

### Coordenação de mensagens {#message-coordination}

Use Feature Flags para sincronizar o lançamento de um recurso e o envio de mensagens, fortalecendo a colaboração entre as equipes de produto e marketing. Ao coordenar lançamentos de recursos e mensagens por meio de Feature Flags, ambas as equipes podem alinhar suas estratégias e criar experiências de usuário consistentes.

Por exemplo, digamos que estamos lançando um novo programa de recompensas de fidelidade para nossos usuários. Pode ser difícil para as equipes de marketing e produto coordenar perfeitamente o timing das mensagens promocionais com o lançamento de um recurso. No entanto, com as Feature Flags no Canvas, nossa equipe de produto pode aplicar uma lógica sofisticada para ativar um recurso para um público específico, enquanto nossa equipe de marketing controla as mensagens relacionadas para esses mesmos usuários.

Para coordenar efetivamente o lançamento do recurso e as mensagens, vamos criar uma nova Feature Flag chamada `show_loyalty_program`. Para nosso lançamento em fases inicial, vamos deixar o Canvas controlar quando e para quem a Feature Flag será ativada. Por enquanto, vamos manter a porcentagem de lançamento em 0% e não selecionar nenhum Segment or segmento de destino.

![Uma Feature Flag com o nome Loyalty Rewards Program. O ID é show_loyalty_program, e a descrição indica que este recurso mostra o novo programa de recompensas de fidelidade na tela inicial e na página de perfil.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %})

Em seguida, no Canvas, vamos criar uma [etapa Feature Flag]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags) que ativa a Feature Flag `show_loyalty_program` para nosso Segment or segmento "Clientes de alto valor":

![Um exemplo de Canvas com uma etapa de divisão de público em que o Segment de clientes de alto valor ativa a Feature Flag show_loyalty_program.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %})

Agora, os usuários nesse Segment or segmento começam a ver o novo programa de fidelidade e, após a ativação, um e-mail e uma pesquisa são enviados automaticamente para ajudar nossas equipes a coletar feedback.

### Experimentação de recursos {#feature-experimentation}

Use Feature Flags para experimentar e confirmar suas hipóteses sobre seu novo recurso. Ao dividir o tráfego em dois ou mais grupos, você pode comparar o impacto de uma Feature Flag entre os grupos e determinar o melhor curso de ação com base nos resultados.

Para experimentos com Feature Flags, você pode ter até nove grupos no total: um grupo de controle mais até oito variantes.

Um [teste A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) é uma ferramenta poderosa que compara as respostas dos usuários a múltiplas versões de uma variável.

Neste exemplo, nossa equipe criou um novo fluxo de checkout para nosso app de eCommerce. Embora estejamos confiantes de que está melhorando a experiência do usuário, queremos executar um teste A/B para medir seu impacto na receita do nosso app.

Para começar, vamos criar uma nova Feature Flag chamada `enable_checkout_v2`. Não vamos adicionar um público ou porcentagem de lançamento. Em vez disso, vamos usar um experimento de Feature Flag para dividir o tráfego, ativar o recurso e medir o resultado.

No nosso app, vamos verificar se a Feature Flag está ativada ou não e trocar o fluxo de checkout com base na resposta:

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag?.enabled) {
  return <NewCheckoutFlow />
} else {
  return <OldCheckoutFlow />
}
```

{% endtab %}
{% tab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewCheckoutFlow();
} else {
  return new OldCheckoutFlow();
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("enable_checkout_v2")
braze.logFeatureFlagImpression("enable_checkout_v2")
if (featureFlag?.enabled == true) {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "enable_checkout_v2")
braze.featureFlags.logFeatureFlagImpression(id: "enable_checkout_v2")
if let featureFlag, featureFlag.enabled {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% endtabs %}

Vamos configurar nosso teste A/B em um [Experimento de Feature Flag]({{site.baseurl}}/developer_guide/feature_flags/experiments).

Agora, 50% dos usuários verão a experiência antiga, enquanto os outros 50% verão a nova experiência. Podemos então analisar as duas variantes para determinar qual fluxo de checkout resultou em uma taxa de conversão mais alta. {% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

![Um experimento de Feature Flag dividindo o tráfego em dois grupos de 50 por cento.]({% image_buster /assets/img/feature_flags/feature-flag-use-case-campaign-experiment.png %})

Depois de determinarmos o vencedor, podemos encerrar essa Campaign e aumentar a porcentagem de lançamento na Feature Flag para 100% para todos os usuários enquanto nossa equipe de engenharia incorpora isso diretamente na próxima versão do app.

### Segmentação {#segmentation}

Use o filtro **Feature Flag** para criar um Segment or segmento ou direcionar mensagens para usuários com base em se eles têm uma Feature Flag ativada. Por exemplo, digamos que você tem uma Feature Flag que controla conteúdo premium no seu app. Você poderia criar um Segment or segmento que filtra os usuários que não têm a Feature Flag ativada e, em seguida, enviar a esse Segment or segmento uma mensagem incentivando-os a fazer upgrade de suas contas para visualizar o conteúdo premium.

1. Abra seu Segment or segmento ou público da mensagem.
2. Adicione o filtro **Feature Flag**.
3. Selecione a Feature Flag.
4. Defina o comparador como **is** para incluir usuários que têm a Feature Flag ativada, ou **is not** para incluir usuários que não têm.
![Criador de Segments da Braze usando um filtro de valor ativado de Feature Flag.]({% image_buster /assets/img/feature_flags/feature_flag_segmentation_filter.png %})

Para saber mais sobre filtragem em Segments, consulte [Criando um Segment or segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

{% alert note %}
Para evitar Segments recursivos, não é possível criar um Segment or segmento que faça referência a outras Feature Flags.
{% endalert %}

## Limitações do plano {#plan-limitations}

Estas são as limitações de Feature Flags para planos gratuitos e pagos.

| Recurso                                                                                                   | Versão gratuita     | Versão paga      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [Feature Flags ativas](#active-feature-flags)                                                                     | 10 por espaço de trabalho | 110 por espaço de trabalho |
| [Experimentos de Campaign ativos]({{site.baseurl}}/developer_guide/feature_flags/experiments)          | 1 por espaço de trabalho  | 100 por espaço de trabalho |
| [Etapas de Feature Flag no Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags) | Ilimitado        | Ilimitado         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limitações do plano" }

Uma Feature Flag é considerada ativa e contará para o seu limite se qualquer uma das seguintes condições se aplicar:

- O rollout é maior que 0%
- Usada em um Canvas ativo
- Usada em um experimento ativo

Mesmo que a mesma Feature Flag atenda a múltiplos critérios, como ser usada em um Canvas e ter o rollout em 50%, ela contará apenas como 1 Feature Flag ativa para o seu limite.

{% alert note %}
Para adquirir a versão paga das Feature Flags, entre em contato com o gerente da sua conta na Braze ou solicite um upgrade no dashboard da Braze.
{% endalert %}