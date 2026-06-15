---
nav_title: Linkrunner
article_title: Linkrunner
alias: /partners/linkrunner/
description: "Este artigo de referência descreve a parceria entre a Braze e o Linkrunner, uma plataforma de atribuição e análise de dados para dispositivos móveis que permite importar dados de atribuição para entender melhor suas campanhas de aquisição de usuários."
page_type: partner
search_tag: Partner

---

# Linkrunner

> O [Linkrunner](https://linkrunner.io/) é uma plataforma de atribuição e análise de dados para dispositivos móveis que ajuda você a rastrear e analisar suas campanhas de aquisição de usuários.

_Essa integração é mantida pelo Linkrunner._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e o Linkrunner permite importar dados de atribuição para entender melhor quais campanhas estão impulsionando a aquisição e o engajamento de usuários.

## Pré-requisitos {#prerequisites}

O seguinte é necessário antes de começar:

| Requisito | Descrição |
|---|---|
| Conta no Linkrunner | Uma conta no Linkrunner é necessária para aproveitar essa parceria. |
| App iOS ou Android | Essa integração é compatível com apps iOS e Android. Dependendo da sua plataforma, trechos de código podem ser necessários no seu aplicativo. |
| SDK do Linkrunner | Você deve instalar o [SDK do Linkrunner](https://docs.linkrunner.io/introduction). |
| SDK da Braze | Você deve integrar o [SDK da Braze]({{site.baseurl}}/developer_guide/sdk_integration/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Mapear IDs de usuário {#step-1-map-user-ids}

Se você usa a função `changeUser` do SDK da Braze, passe o mesmo ID de usuário no parâmetro `userData` da função `signup` do SDK do Linkrunner.

Se você não usa `changeUser`, passe o `brazeDeviceId` no parâmetro `userData` da função `signup` do SDK do Linkrunner. Obtenha o `brazeDeviceId` a partir do SDK da Braze.

{% tabs local %}
{% tab Android (Kotlin) %}
```kotlin
val userData = UserDataRequest(
    id = "123", // Your user ID
    // ...other user fields
    brazeDeviceId = "BRAZE_DEVICE_ID", // Braze device ID from the Braze SDK (Required if you are not using the changeUser function)
)

LinkRunner.getInstance().signup(userData = userData)
```
{% endtab %}

{% tab iOS (Swift) %}
```swift
let userData = UserData(
    id: "123", // Your user ID
    // ...other user fields
    brazeDeviceId: "BRAZE_DEVICE_ID" // Braze Device ID from the Braze SDK (Required if you are not using the changeUser function)
)

try await LinkrunnerSDK.shared.signup(userData: userData)
```
{% endtab %}
{% endtabs %}

### Etapa 2: Criar chave de API na Braze {#step-2-create-api-key-in-braze}

No dashboard da Braze, acesse **Configurações** > **Configurações e teste** > **APIs e identificadores** > **Chaves de API**.

1. Selecione **Criar chave de API**.
2. Em **Dados de usuários**, selecione as seguintes permissões:
   - `users.track`
   - `users.export.ids`
3. Salve a chave de API.
4. Copie a chave de API e o endpoint REST.

![Esta imagem mostra a página de chaves de API na Braze, onde você pode criar e gerenciar chaves de API, incluindo a chave de importação de dados e o endpoint REST necessários para a integração com o Linkrunner.]({% image_buster /assets/img/attribution/linkrunner/1.png %})

### Etapa 3: Configurar a Braze no dashboard do Linkrunner {#step-3-configure-braze-in-linkrunners-dashboard}

1. No Linkrunner, acesse **Integrations** no painel à esquerda.
2. Em **Analytics**, selecione **Configure** para a Braze.
3. Insira a chave de API e o endpoint REST que você copiou na Etapa 2.

Para saber mais, consulte a [documentação do Linkrunner](https://docs.linkrunner.io/analytics-integrations/braze).

### Etapa 4: Visualizar dados de atribuição de usuários {#step-4-view-user-attribution-data}

O Linkrunner envia `lr_campaign` e `lr_ad_network` como atributos personalizados. Visualize esses dados na seção **Atributos personalizados** do perfil de usuário no dashboard da Braze.

## Dados de atribuição do Facebook e X (antigo Twitter) {#facebook-and-x-formerly-twitter-attribution-data}

Os dados de atribuição de campanhas do Facebook e X (antigo Twitter) não estão disponíveis por meio de nossos parceiros. Essas fontes de mídia não permitem que seus parceiros compartilhem dados de atribuição com terceiros e, portanto, nossos parceiros não podem enviar esses dados para a Braze.