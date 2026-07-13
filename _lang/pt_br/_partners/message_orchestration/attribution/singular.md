---
nav_title: Singular
article_title: Singular
alias: /partners/singular/
description: "Esse artigo de referência descreve a parceria entre a Braze e a Singular, uma plataforma unificada de análise de dados de marketing que permite que você importe dados de atribuição de instalação paga."
page_type: partner
search_tag: Partner

---

# Singular

> [A Singular](https://www.singular.net/) é uma plataforma unificada de análise de dados de marketing que oferece atribuição, agregação de custos, análise de marketing, relatórios criativos e automação de fluxo de trabalho.

_Essa integração é mantida pela Singular._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Singular permite importar dados de atribuição de instalação paga para segmentar de forma inteligente suas campanhas de ciclo de vida.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta da Singular | É necessário ter uma conta na Singular para aproveitar essa parceria. |
| App iOS ou Android | Essa integração é compatível com apps para iOS e Android. Dependendo da sua plataforma, trechos de código podem ser necessários no seu aplicativo. Consulte os detalhes sobre esses requisitos na etapa 1 do processo de integração. |
| SDK da Singular | Além do SDK da Braze obrigatório, você deve instalar o [SDK da Singular](https://support.singular.net/hc/en-us/articles/360037640172-Getting-Started-with-the-Singular-SDK-S2S). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

### Etapa 1: Mapear IDs de usuários {#step-1-map-user-ids}

#### Android

Se você tiver um app para Android, precisará incluir o seguinte trecho de código, que passa um ID de usuário Braze exclusivo para a Singular.

```java
String appboyDeviceId = Braze.getInstance(context).getDeviceId();
SingularConfig config = new SingularConfig("SDK KEY", "SDK SECRET")
  .withGlobalProperty(“brazeDeviceID”, appboyDeviceId, true);
```
#### iOS

{% alert important %}
Antes de fevereiro de 2023, nossa integração de atribuição da Singular usava o Identificador de Fornecedor (IDFV) como o identificador principal para corresponder aos dados de atribuição do iOS. Não é necessário que os clientes da Braze que usam Objective-C obtenham o `device_id` da Braze e o enviem para a Singular após a instalação, pois não há interrupção do serviço.
{% endalert%}

Para quem usa o SWIFT SDK v5.7.0+, se você deseja continuar usando o IDFV como o identificador mútuo, confirme se o campo `useUUIDAsDeviceId` está definido como `false` para que não haja interrupção da integração.

Se estiver definido como `true`, implemente o mapeamento de ID do dispositivo iOS para Swift a fim de passar o `device_id` da Braze para a Singular na instalação do app para que a Braze possa corresponder adequadamente as atribuições do iOS.

{% tabs local %}
{% tab Objective-C %}

```objc
SingularConfig* config = [[SingularConfig
  alloc] initWithApiKey:SDKKEY andSecret:SDKSECRET];

  [config setGlobalProperty:@"brazeDeviceId" withValue:brazeDeviceId
  overrideExisting:YES];
  [Singular start:config];
```

{% endtab %}
{% tab Swift%}

```swift
config.setGlobalProperty("brazeDeviceId", withValue: brazeDeviceId, overrideExisting: true)
```

{% endtab %}
{% endtabs %}

### Etapa 2: Obtenha a chave de importação de dados da Braze {#step-2-get-the-braze-data-import-key}

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Singular**.

Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. Depois que a chave é gerada, você pode criar outra ou invalidar uma existente.

Você precisará fornecer a chave de importação de dados e o endpoint REST ao gerente da sua conta Singular para concluir a integração.<br><br>![Esta imagem mostra a caixa "Importação de dados para atribuição de instalação" encontrada na página da tecnologia Singular. Essa caixa contém a chave de importação de dados e o endpoint REST.]({% image_buster /assets/img/attribution/singular.png %}){: style="max-width:90%;"}

### Etapa 3: Confirmar a integração {#step-3-confirm-the-integration}

Depois que a Braze receber dados de atribuição da Singular, o indicador de status da conexão na página de parceiros de tecnologia da Singular na Braze mudará de "Not Connected" para "Connected" e incluirá um registro de data e hora da última solicitação bem-sucedida.

Esse status é alterado somente depois que a Braze recebe dados sobre uma atribuição de instalação. A Braze ignora as instalações orgânicas (as exclui do postback da Singular) e não as conta ao determinar se a conexão foi bem-sucedida.

## Dados de atribuição do Facebook e do X (antigo Twitter) {#facebook-and-x-formerly-twitter-attribution-data}

Os dados de atribuição para campanhas do Facebook e do X (antigo Twitter) não estão disponíveis por meio de nossos parceiros. Essas fontes de mídia não permitem que seus parceiros compartilhem dados de atribuição com terceiros e, portanto, nossos parceiros não podem enviar esses dados para a Braze.

## URLs de rastreamento de cliques da Singular na Braze (opcional) {#singular-click-tracking-urls-in-braze-optional}

Usar links de rastreamento de cliques nas suas campanhas da Braze permitirá que você veja facilmente quais campanhas estão gerando instalações de apps e reengajamento. Como resultado, você será capaz de medir seus esforços de marketing de forma mais eficaz e tomar decisões baseadas em dados sobre onde investir mais recursos para obter o máximo ROI.

Para começar a usar os links de rastreamento de cliques da Singular, visite a [documentação](https://support.singular.net/hc/en-us/articles/360030934212-Singular-Links-FAQ?navigation_side_bar=true). Você pode inserir os links de rastreamento de cliques da Singular diretamente nas suas campanhas da Braze. A Singular usará então suas [metodologias de atribuição probabilística](https://support.singular.net/hc/en-us/articles/115000526963-Understanding-Singular-Mobile-App-Attribution?navigation_side_bar=true) para atribuir o usuário que clicou no link. Recomendamos anexar seus links de rastreamento da Singular com um identificador de dispositivo para melhorar a precisão das atribuições das suas campanhas da Braze. Isso atribuirá de forma determinística o usuário que clicou no link.

{% tabs local %}
{% tab Android %}
Para Android, a Braze permite que os clientes façam a aceitação da [coleta do ID de publicidade do Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). O GAID também é coletado nativamente pela integração do SDK da Singular. É possível incluir o GAID nos seus links de rastreamento de cliques da Singular utilizando a seguinte lógica Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto a Braze quanto a Singular coletam automaticamente o IDFV de forma nativa por meio das nossas integrações de SDK. Isso pode ser usado como o identificador do dispositivo. É possível incluir o IDFV nos seus links de rastreamento de cliques da Singular utilizando a seguinte lógica Liquid:

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
Se você não usa atualmente nenhum identificador de dispositivo — como o IDFV ou GAID — nos seus links de rastreamento de cliques, ou não planeja fazê-lo no futuro, a Singular ainda poderá atribuir esses cliques por meio da sua modelagem probabilística.
{% endalert %}