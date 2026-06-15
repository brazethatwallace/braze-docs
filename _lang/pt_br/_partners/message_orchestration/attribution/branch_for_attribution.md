---
nav_title: Branch para atribuição
article_title: Branch para atribuição
alias: /partners/branch_for_attribution/
description: "Este artigo de referência descreve a parceria entre a Braze e a Branch, uma plataforma de links móveis que ajuda você a adquirir, engajar e medir em todos os dispositivos, canais e plataformas."
page_type: partner
search_tag: Partner
---

# Branch para atribuição {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> A [Branch](https://docs.branch.io/pages/integrations/braze/) é uma plataforma de links móveis que ajuda a adquirir, engajar e medir em todos os dispositivos, canais e plataformas por meio de uma visão holística de todos os pontos de contato dos usuários.

_Essa integração é mantida pela Branch._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Branch ajuda a entender exatamente quando e onde aconteceu a aquisição de um usuário e a personalizar a jornada de cada um por meio de atribuição robusta e [deep linking]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/).

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta da Branch | É necessário ter uma conta Branch para usar essa parceria. |
| App iOS ou Android | Essa integração é compatível com apps para iOS e Android. Dependendo da sua plataforma, trechos de código podem ser necessários no seu aplicativo. Consulte os detalhes sobre esses requisitos na etapa 1 do processo de integração. |
| SDK da Branch | Além do SDK da Braze obrigatório, você deve instalar o [SDK da Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

### Etapa 1: Mapear IDs de dispositivos {#step-1-map-device-ids}

#### Android

Se você tiver um app para Android, precisará passar um ID de dispositivo exclusivo da Braze para a Branch. Esse ID pode ser definido no método `setRequestMetadataKey()` do SDK da Branch. O trecho de código a seguir deve ser incluído antes de chamar `initSession`. Você também deve inicializar o SDK da Braze antes de definir os metadados da solicitação no SDK da Branch.

{% tabs local %}
{% tab Java %}
```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId);
```
{% endtab %}
{% tab Kotlin %}
```kotlin
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId)
```
{% endtab %}
{% endtabs %}

#### iOS

{% alert important %}
Antes de fevereiro de 2023, nossa integração de atribuição da Branch usava o Identifier for Vendor (IDFV) como identificador principal para corresponder aos dados de atribuição do iOS. Não é necessário que os clientes da Braze que usam Objective-C busquem o `device_id` da Braze e o enviem para a Branch durante a instalação, pois não há interrupção do serviço.
{% endalert%}

Para quem usa o Swift SDK v5.7.0+, se você deseja continuar usando o IDFV como identificador mútuo, confirme se o campo `useUUIDAsDeviceId` está definido como `false` para que não haja interrupção da integração.

Se estiver definido como `true`, implemente o mapeamento de ID do dispositivo iOS para Swift a fim de passar o `device_id` da Braze para a Branch na instalação do app para que a Braze possa corresponder adequadamente as atribuições do iOS.

{% tabs local %}
{% tab Objective-C %}
```objc
[braze deviceIdOnQueue:dispatch_get_main_queue() completion:^(NSString * _Nonnull deviceId) {
  [[Branch getInstance] setRequestMetadataKey:@"$braze_install_id" value:deviceId];
  // Branch init
}];
```
{% endtab %}
{% tab Swift %}

```swift
braze.deviceId { deviceId in
  Branch.getInstance.setRequestMetadata("$braze_install_id", deviceId)
  // Branch init
}
```

{% endtab %}
{% endtabs %}

### Etapa 2: Obtenha a chave de importação de dados da Braze {#step-2-get-the-braze-data-import-key}

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Branch**.

Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. Depois que a chave é gerada, você pode criar outra ou invalidar uma existente. A chave de importação de dados e o endpoint REST são usados na próxima etapa ao configurar um postback no dashboard da Branch.<br><br>![Esta imagem mostra a caixa "Importação de dados para atribuição de instalação" encontrada na página de tecnologia da Branch. Essa caixa contém a chave de importação de dados e o endpoint REST.]({% image_buster /assets/img/attribution/branch.png %}){: style="max-width:90%;"}

### Etapa 3: Configurar Data Feeds {#step-3-set-up-data-feeds}

1. Na Branch, na seção **Exports**, selecione **Data Feeds**.
2. Na página **Data Feeds Manager**, selecione a guia **Data Integrations** na parte superior da página.
3. Selecione Braze na lista de parceiros de dados disponíveis.
4. Na página de exportação da Braze, forneça a chave de importação de dados e o endpoint REST que você encontrou no dashboard da Braze e selecione **Enable**.

### Etapa 4: Confirmar a integração {#step-4-confirm-the-integration}

Depois que a Braze receber dados de atribuição da Branch, o indicador de status da conexão na página de parceiros de tecnologia da Branch na Braze mudará de "Not Connected" para "Connected" e incluirá um registro de data e hora da última solicitação bem-sucedida.

Esse status é alterado somente depois que a Braze recebe dados sobre uma atribuição de instalação. A Braze ignora as instalações orgânicas (as exclui do postback da Branch) e não as conta ao determinar se a conexão foi bem-sucedida.

## Dados de atribuição do Facebook e do X (antigo Twitter) {#facebook-and-x-formerly-twitter-attribution-data}

Os dados de atribuição para campanhas do Facebook e do X (antigo Twitter) não estão disponíveis por meio de nossos parceiros. Essas fontes de mídia não permitem que seus parceiros compartilhem dados de atribuição com terceiros e, portanto, nossos parceiros não podem enviar esses dados para a Braze.

## URLs de rastreamento de cliques da Branch na Braze (opcional) {#branch-click-tracking-urls-in-braze-optional}

Usar links de rastreamento de cliques nas suas campanhas da Braze permitirá que você veja facilmente quais campanhas estão gerando instalações de apps e reengajamento. Como resultado, você poderá medir seus esforços de marketing de forma mais eficaz e tomar decisões baseadas em dados sobre onde investir mais recursos para obter o máximo ROI.

Para começar a usar os links de rastreamento de cliques da Branch, consulte a [documentação](https://help.branch.io/using-branch/docs/ad-links) da Branch. Você pode inserir os links de rastreamento de cliques da Branch diretamente nas suas campanhas da Braze. A Branch usará então suas [metodologias de atribuição probabilística](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings) para atribuir o usuário que clicou no link. Recomendamos anexar seus links de rastreamento da Branch com um identificador de dispositivo para melhorar a precisão das atribuições das suas campanhas da Braze. Isso atribuirá de forma determinística o usuário que clicou no link.

{% tabs local %}
{% tab Android %}
Para Android, a Braze permite que os clientes façam a aceitação da [coleta do Google Advertising ID (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). O GAID também é coletado nativamente pela integração do SDK da Branch. Você pode incluir o GAID nos seus links de rastreamento de cliques da Branch utilizando a seguinte lógica Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
user_data_aaid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto a Braze quanto a Branch coletam automaticamente o IDFV de forma nativa por meio das nossas integrações de SDK. Isso pode ser usado como o identificador do dispositivo. Você pode incluir o IDFV nos seus links de rastreamento de cliques da Branch utilizando a seguinte lógica Liquid:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
user_data_idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Esta recomendação é puramente opcional**<br>
Se você não usa identificadores de dispositivo, como o IDFV ou GAID, nos seus links de rastreamento de cliques nem planeja adotá-los, a Branch ainda será capaz de atribuir esses cliques por meio de modelagem probabilística.
{% endalert %}