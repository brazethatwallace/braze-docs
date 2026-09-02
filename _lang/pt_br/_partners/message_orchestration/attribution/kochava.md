---
nav_title: Kochava
article_title: Kochava
alias: /partners/kochava/
description: "Este artigo de referência descreve a parceria entre a Braze e a Kochava, uma plataforma de atribuição móvel que oferece insights de atribuição e análise de dados para ajudá-lo a aproveitar seus dados para crescer."
page_type: partner
search_tag: Partner

---

# Kochava

> [A Kochava](https://www.kochava.com/) oferece atribuição e análises de dados móveis para ajudá-lo a aproveitar seus dados para crescer. Com a Kochava Audience Platform, é possível planejar, direcionar, ativar, medir e otimizar suas campanhas de apps.

_Essa integração é mantida pela Kochava._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Kochava ajuda a proporcionar uma compreensão mais holística de suas campanhas, enviando dados de atribuição para a Braze para entender melhor quais campanhas estão gerando instalações, atividades no aplicativo e muito mais.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Kochava | É necessário ter uma conta Kochava para aproveitar essa parceria. |
| App para iOS ou Android | Essa integração é compatível com apps para iOS e Android. Dependendo da sua plataforma, trechos de código podem ser necessários no seu aplicativo. Consulte os detalhes sobre esses requisitos na etapa 1 do processo de integração. |
| Kochava SDK or kit de desenvolvimento de software | Além do SDK or kit de desenvolvimento de software da Braze obrigatório, você deve instalar o [SDK or kit de desenvolvimento de software da Kochava](https://support.kochava.com/sdk-integration/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

### Etapa 1: Mapear IDs de usuários {#step-1-map-user-ids}

#### Android

O SDK or kit de desenvolvimento de software [do Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) gera um GUID (Globally Unique Identifier) como o Braze ID no início da sessão. Esse identificador deve ser passado para o método `IdentityLink` da Kochava para que a Braze possa reconciliar os dados de volta ao perfil de usuário correto. Recupere o Braze ID com o seguinte método:

```java
Apppboy.getInstance(context).getDeviceId();
```

#### iOS

{% alert important %}
Antes de fevereiro de 2023, nossa integração de atribuição da Kochava usava o Identificador de Fornecedor (IDFV) como o identificador principal para corresponder aos dados de atribuição do iOS. Não é necessário que os clientes da Braze que usam Objective-C busquem o `device_id` da Braze e o enviem para a Kochava durante a instalação, pois não há interrupção do serviço.
{% endalert%}

Para quem usa o Swift SDK or kit de desenvolvimento de software v5.7.0+, se você deseja continuar usando o IDFV como o identificador mútuo, confirme se o campo `useUUIDAsDeviceId` está definido como `false` para que não haja interrupção da integração. Se estiver definido como `true`, implemente o mapeamento de ID do dispositivo iOS para Swift a fim de passar o `device_id` da Braze para a Kochava na instalação do app para que a Braze possa corresponder adequadamente as atribuições do iOS.

A Braze tem duas APIs que produzirão o mesmo valor, uma com um manipulador de conclusão e outra usando o novo suporte de concorrência do Swift. Note que você precisará modificar os seguintes trechos de código para que fiquem em conformidade com as instruções do [SDK or kit de desenvolvimento de software para iOS](https://support.kochava.com/sdk-integration/ios-sdk-integration/) da Kochava. Para obter ajuda adicional, entre em contato com o suporte da Kochava.

##### Manipulador de conclusão {#completion-handler}
```
AppDelegate.braze?.deviceId(completion: { deviceId in
  // Use `deviceId`
})
```
##### Concorrência Swift {#swift-concurrency}
```
let deviceId = await AppDelegate.braze?.deviceId()
```

### Etapa 2: Obter a chave de importação de dados da Braze {#step-2-get-the-braze-data-import-key}

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Kochava**.

Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. Depois que a chave é gerada, você pode criar outra ou invalidar uma existente. A chave de importação de dados e o endpoint REST são usados na próxima etapa ao configurar um postback no dashboard da Kochava.<br><br>![Esta imagem mostra a caixa "Importação de dados para atribuição de instalação" encontrada na página de tecnologia da Kochava. Essa caixa contém a chave de importação de dados e o endpoint REST.]({% image_buster /assets/img/attribution/kochava.png %}){: style="max-width:90%;"}

### Etapa 3: Configure um postback da Kochava {#step-3-set-up-a-postback-from-kochava}

[Adicione um postback](https://support.kochava.com/campaign-management/create-a-kochava-certified-postback) no seu dashboard da Kochava. Você será solicitado a fornecer a chave de importação de dados e o endpoint REST or transferir estado representacional que encontrou no dashboard da Braze.

### Etapa 4: Confirmar a integração {#step-4-confirm-the-integration}

Depois que a Braze receber dados de atribuição da Kochava, o indicador de status da conexão na página de parceiros de tecnologia da Kochava na Braze mudará de "Not Connected" para "Connected" e incluirá um registro de data e hora da última solicitação bem-sucedida.

Esse status é alterado somente depois que a Braze recebe dados sobre uma atribuição de instalação. A Braze ignora as instalações orgânicas (exclui-as do postback da Kochava) e não as conta ao determinar se a conexão foi bem-sucedida.

## Dados de atribuição do Facebook e do X (antigo Twitter) {#facebook-and-x-formerly-twitter-attribution-data}

Os dados de atribuição para campanhas do Facebook e do X (antigo Twitter) não estão disponíveis por meio de nossos parceiros. Essas fontes de mídia não permitem que seus parceiros compartilhem dados de atribuição com terceiros e, portanto, nossos parceiros não podem enviar esses dados para a Braze.

## URLs de rastreamento de cliques da Kochava na Braze (opcional) {#kochava-click-tracking-urls-in-braze-optional}

O uso de links de rastreamento de cliques nas suas campanhas da Braze permitirá que você veja facilmente quais campanhas estão gerando instalações de apps e reengajamento. Como resultado, você poderá medir seus esforços de marketing de forma mais eficaz e tomar decisões baseadas em dados sobre onde investir mais recursos para obter o máximo de ROI or retorno sobre o investimento (ROI).

Para começar a usar os links de rastreamento de cliques da Kochava, visite a [documentação](https://support.kochava.com/reference-information/attribution-overview/) deles. Você pode inserir os links de rastreamento de cliques da Kochava diretamente nas suas campanhas da Braze. A Kochava usará então suas [metodologias de atribuição probabilística](https://www.kochava.com/getting-prepared-for-ios-14/) para atribuir o usuário que clicou no link. Recomendamos anexar seus links de rastreamento da Kochava com um identificador de dispositivo para melhorar a precisão das atribuições das suas campanhas da Braze. Isso atribuirá de forma determinística o usuário que clicou no link.

{% tabs local %}
{% tab Android %}
Para Android, a Braze permite que os clientes façam a aceitação da [coleta do ID de publicidade do Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). O GAID também é coletado nativamente por meio da integração do SDK or kit de desenvolvimento de software da Kochava. É possível incluir o GAID nos seus links de rastreamento de cliques da Kochava utilizando a seguinte lógica Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto a Braze quanto a Kochava coletam automaticamente o IDFV nativamente por meio das nossas integrações de SDK or kit de desenvolvimento de software. Isso pode ser usado como identificador do dispositivo. É possível incluir o IDFV nos seus links de rastreamento de cliques da Kochava utilizando a seguinte lógica Liquid:

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
**Essa recomendação é puramente opcional**<br>
Se você não usa atualmente nenhum identificador de dispositivo — como o IDFV ou GAID — nos seus links de rastreamento de cliques, ou não planeja fazê-lo no futuro, a Kochava ainda poderá atribuir esses cliques por meio de sua modelagem probabilística.
{% endalert %}