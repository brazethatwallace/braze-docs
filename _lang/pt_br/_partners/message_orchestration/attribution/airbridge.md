---
nav_title: Airbridge
article_title: Airbridge
alias: /partners/airbridge/
description: "Este artigo de referência descreve a parceria entre a Braze e a Airbridge, que oferece atribuição baseada em pessoas e medição incremental para medir a verdadeira eficácia do marketing em dispositivos, identidades e plataformas."
page_type: partner
search_tag: Partner

---

# Airbridge

> A [Airbridge](https://www.airbridge.io/) é uma plataforma unificada de medição móvel para descobrir fontes de crescimento por meio de atribuição móvel, medição incremental e modelagem de marketing mix.

_Essa integração é mantida pela Airbridge._

## Sobre a integração {#about-the-integration}

A integração da Braze com a Airbridge permite que você passe todos os dados de atribuição de instalação não orgânica da Airbridge para a Braze para criar campanhas de marketing personalizadas.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Airbridge | Uma conta Airbridge é necessária para aproveitar essa parceria. |
| App para iOS ou Android | Essa integração é compatível com apps para iOS e Android. Dependendo da sua plataforma, trechos de código podem ser necessários na sua aplicação. |
| Airbridge SDK | Além do SDK obrigatório da Braze, você deve instalar o SDK da Airbridge para [Android](https://help.airbridge.io/en/developers/android-sdk) ou [iOS](https://help.airbridge.io/en/developers/ios-sdk). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: mapeie o ID do dispositivo {#step-1-map-device-id}

A integração de servidor para servidor pode ser habilitada incluindo os seguintes trechos de código nos seus apps.

#### Android

Se você tiver um app para Android, precisará passar um ID de dispositivo exclusivo da Braze para a Airbridge.

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
// MainApplciation.java
@Override
public void onCreate() {
    super.onCreate();
    // Initialize Airbridge SDK
    AirbridgeConfig config = new AirbridgeConfig.Builder("APP_NAME", "APP_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build();
    Airbridge.init(this, config);

    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).getDeviceId());
    // Explicitly start tracking
    Airbridge.startTracking();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
// MainApplication.kt
override fun onCreate() {
    super.onCreate()
    // Initialize Airbridge SDK
    val config = AirbridgeConfig.Builder("YOUR_APP_NAME", "YOUR_APP_SDK_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build()
    Airbridge.init(this, config)

    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).deviceId)
    // Explicitly start tracking
    Airbridge.startTracking()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### iOS

Se você tiver um app para iOS, será possível coletar o IDFV definindo o campo useUUIDAsDeviceId como false. Se não for definido, a atribuição do iOS provavelmente não será mapeada com precisão da Airbridge para a Braze. Para saber mais, consulte Coleta de IDFV.

{% tabs %}
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

```swift
// AppDelegate.swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]?
) {
    AirBridge.setAutoStartTrackingEnabled(false)
    AirBridge.getInstance("YOUR_APP_TOKEN", appName:"YOUR_APP_NAME", withLaunchOptions:launchOptions)

    AirBridge.state()?.addUserAlias(withKey:"braze_device_id", value:Appboy.sharedInstance()?.getDeviceId())
    AirBridge.startTracking()
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// AppDelegate.m
-           (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  AirBridge.autoStartTrackingEnabled = NO;
  [AirBridge getInstance:@"YOUR_APP_TOKEN" appName:@"YOUR_APP_NAME" withLaunchOptions:launchOptions];

    [AirBridge.state addUserAliasWithKey:@"braze_device_id" value:Appboy.sharedInstance.getDeviceId];
    [AirBridge startTracking];
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### React Native

{% tabs %}
{% tab TypeScript %}

```typescript
Braze.getInstallTrackingId(function (error, brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
    Airbirdge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Cordova

{% tabs %}
{% tab TypeScript %}

```typescript
AppboyPlugin.getDeviceId(function (brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Flutter

{% tabs %}
{% tab TypeScript %}

```typescript
BrazePlugin.getInstallTrackingId().then((brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Unity

{% tabs %}
{% tab C# %}

```c#
string BrazeID = AppboyBinding.GetInstallTrackingId();
AirbridgeUnity.SetDeviceAlias("braze_device_id", BrazeID);
AirbridgeUnity.StartTracking()
```

{% endtab %}
{% endtabs %}

### Etapa 2: obtenha a chave de importação de dados da Braze {#step-2-get-the-braze-data-import-key}

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Airbridge**.

Aqui você encontrará o endpoint REST e poderá gerar sua chave de importação de dados da Braze. Depois que a chave for gerada, você pode criar outra ou invalidar uma existente. A chave de importação de dados e o endpoint REST são usados na próxima etapa ao configurar um postback no dashboard da Airbridge.

![Página de parceiro Airbridge na Braze mostrando os campos de chave de importação de dados e endpoint REST.]({% image_buster /assets/img/airbridge/airbridge_integration_step_1.png %})

### Etapa 3: configure a Braze no dashboard da Airbridge {#step-3-configure-braze-in-airbridges-dashboard}

1. Na Airbridge, navegue até **Integrations > Third-party Integrations** na barra lateral de navegação e selecione **Braze**.
2. Forneça a chave de importação de dados e o endpoint REST que você encontrou no dashboard da Braze.
3. Selecione o tipo de evento (Install Event ou Install & Deeplink Open Event) e salve.

{% alert note %}
Os dados de atribuição para campanhas que levaram a eventos de abertura de deeplink são atualizados no nível do dispositivo. Por exemplo, se dois usuários usam um único dispositivo e um deles realiza um evento de abertura de deeplink, os dados de atribuição desse evento também são refletidos nos dados do outro usuário.
{% endalert %}

Para obter instruções mais detalhadas, visite [Airbridge](https://help.airbridge.io/en/guides/braze).

### Etapa 4: confirme a integração {#step-4-confirm-the-integration}

Depois que a Braze receber dados de atribuição da Airbridge, o indicador de status da conexão na página de parceiros de tecnologia da Airbridge na Braze mudará de "Not Connected" para "Connected" e incluirá um registro de data e hora da última solicitação bem-sucedida.

Esse status é alterado somente depois que a Braze recebe dados sobre uma instalação atribuída. A Braze ignora as instalações orgânicas (as exclui do postback da Airbridge) e não as conta ao determinar se a conexão foi bem-sucedida.

## Campos de dados disponíveis {#available-data-fields}

A Airbridge pode enviar quatro tipos de dados de atribuição para a Braze, listados na tabela de campos de dados a seguir. Esses dados podem ser visualizados no dashboard da Airbridge e são usados para atribuição de instalação e filtragem de usuários.

Supondo que você configure sua integração conforme sugerido, a Braze mapeará os dados de instalação para filtros de Segment.

| Campo de dados da Airbridge | Filtro de Segment da Braze | Descrição |
| -------------------- | ---------------------| ---- |
| `Channel` | Origem da atribuição da instalação | O canal ao qual as instalações ou aberturas de deeplink são atribuídas |
| `Campaign` | Campaign da atribuição da instalação | A Campaign à qual as instalações ou aberturas de deeplink são atribuídas |
| `Ad Group` | Grupo de anúncios da atribuição da instalação | O grupo de anúncios ao qual as instalações ou aberturas de deeplink são atribuídas |
| `Ad Creative` | Anúncio da atribuição da instalação | O criativo do anúncio ao qual as instalações ou aberturas de deeplink são atribuídas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos de dados disponíveis" }

Sua base de usuários pode ser segmentada por dados de atribuição no dashboard da Braze usando os filtros de atribuição da instalação.

![Filtros de Segment da Braze exibindo os campos de atribuição de instalação da Airbridge disponíveis.]({% image_buster /assets/img/airbridge/airbridge_integration_step_2.png %})

## Dados de atribuição do Meta Business {#meta-business-attribution-data}

Os dados de atribuição para campanhas do Meta Business não estão disponíveis por meio dos nossos parceiros. Essa fonte de mídia não permite que seus parceiros compartilhem dados de atribuição com terceiros e, portanto, nossos parceiros não podem enviar esses dados para a Braze.

## URLs de rastreamento de cliques da Airbridge na Braze (opcional) {#airbridge-click-tracking-urls-in-braze-optional}

O uso de links de rastreamento de cliques nas suas campanhas da Braze mostra quais campanhas geram instalações de apps e reengajamento. Use os resultados para medir o desempenho do marketing e decidir onde investir recursos para obter um ROI mais forte.

Para começar com os links de rastreamento de cliques da Airbridge, visite [Airbridge](https://help.airbridge.io/en/guides/creating-a-new-tracking-link). Depois que a configuração estiver concluída, você pode inserir diretamente os links de rastreamento de cliques da Airbridge nas suas campanhas da Braze. A Airbridge usará então suas [metodologias de atribuição probabilística](https://help.airbridge.io/en/guides/identity-matching) para atribuir o usuário que clicou no link. Recomendamos anexar seus links de rastreamento da Airbridge com um identificador de dispositivo para melhorar a precisão das atribuições das suas campanhas da Braze. Isso atribuirá de forma determinística o usuário que clicou no link.

{% tabs %}
{% tab Android %}
Para Android, a Braze permite que os clientes façam a aceitação da [coleta do ID de publicidade do Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection#optional-google-advertising-id). O GAID também é coletado nativamente pela integração do SDK da Airbridge. Você pode incluir o GAID nos seus links de rastreamento de cliques da Airbridge utilizando a seguinte lógica Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto a Braze quanto a Airbridge coletam automaticamente o IDFV de forma nativa por meio das nossas integrações de SDK. Isso pode ser usado como o identificador do dispositivo. Você pode incluir o IDFV nos seus links de rastreamento de cliques da Airbridge utilizando a seguinte lógica Liquid:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Esta recomendação é puramente opcional**<br>
Se você não usa identificadores de dispositivo, como o IDFV ou GAID, nos seus links de rastreamento de cliques nem planeja adotá-los, a Airbridge ainda será capaz de atribuir esses cliques por meio de modelagem probabilística.
{% endalert %}