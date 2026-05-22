---
nav_title: Adjust
article_title: Adjust
alias: /partners/adjust/
description: "Esse artigo de referência descreve a parceria entre a Braze e a Adjust, uma empresa de análise e atribuição móvel que permite importar dados de atribuição de instalação não orgânica para segmentar de forma mais inteligente suas campanhas de ciclo de vida."
page_type: partner
search_tag: Partner

---

# Adjust

> [A Adjust](https://www.adjust.com/) é uma empresa de atribuição e análise de dados móveis que combina a atribuição de fontes de publicidade com análises avançadas para obter um quadro abrangente de business intelligence.

_Essa integração é mantida pela Adjust._

## Sobre a integração {#about-the-integration}

A integração da Braze e da Adjust permite importar dados de atribuição de instalação não orgânica para segmentar de forma mais inteligente suas campanhas de ciclo de vida.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Adjust | É necessário ter uma conta Adjust para aproveitar essa parceria. |
| App para iOS ou Android | Essa integração é compatível com apps para iOS e Android. Dependendo da sua plataforma, trechos de código podem ser necessários no seu aplicativo. Consulte os detalhes sobre esses requisitos na etapa 1 do processo de integração. |
| SDK da Adjust | Além do SDK da Braze obrigatório, você deve instalar o [SDK da Adjust](https://dev.adjust.com/en/sdk). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Mapear IDs de dispositivos {#step-1-map-device-ids}

#### Android

Se você tiver um app Android, deve passar um ID de dispositivo Braze único para a Adjust. Esse ID pode ser definido no método `addGlobalPartnerParameter()` do SDK da Adjust. O snippet de código a seguir deve ser incluído antes da inicialização do SDK em `Adjust.initSdk.`

```
Adjust.addGlobalPartnerParameter("braze_device_id", Braze.getInstance(getApplicationContext()).getDeviceId()););
```

#### iOS

<!--
{% alert important %}
Prior to February 2023, our Adjust attribution integration used the Identifier for Vendor (IDFV) as the primary identifier to match iOS attribution data. Braze customers don't need to use Objective-C to fetch the Braze `device_id` and send it to Adjust upon installation because there is no service disruption.
{% endalert%}

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration.

If set to `true`, you must implement the iOS device ID mapping for Swift to pass the Braze `device_id` to Adjust upon app installation in order for Braze to match iOS attributions appropriately.
--->

{% tabs local %}
{% tab Objective-C %}

Se você tiver um app para iOS, seu IDFV será coletado pela Adjust e enviado à Braze. Esse ID será então mapeado para um ID de dispositivo exclusivo na Braze.

A Braze ainda armazenará os valores de IDFA dos usuários que fizeram opt-in se você estiver coletando o IDFA com a Braze, conforme descrito em nosso [Guia de atualização do iOS]({{site.baseurl}}/developer_guide/platforms/swift/ios_18/). Caso contrário, o IDFV será usado como um identificador de fallback para mapear os usuários.

{% endtab %}
{% tab Swift %}

Se você tiver um app para iOS, poderá aceitar a coleta de IDFV definindo o campo `useUUIDAsDeviceId` como `false`. Se não for definido, a atribuição do iOS provavelmente não será mapeada com precisão da Adjust para a Braze. Para saber mais, consulte [Coleta de IDFV]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift).

{% endtab %}
{% endtabs %}

{% alert note %}
Se estiver planejando enviar eventos pós-instalação da Adjust para a Braze, será necessário: <br><br>1) Anexar `external_id` como um parâmetro de sessão e evento no SDK da Adjust. Para o encaminhamento de eventos de receita, você também precisará configurar `product_id` como um parâmetro para eventos. Visite a [documentação da Adjust](https://github.com/adjust/sdks) para saber mais sobre a definição de parâmetros de parceiros para encaminhamento de eventos.<br><br>2) Gerar uma nova chave de API para inserir na Adjust. Isso pode ser feito selecionando o botão **Generate API Key** encontrado na página de parceiro da Adjust no dashboard da Braze.
{% endalert %}

### Etapa 2: Obter a chave de importação de dados da Braze {#step-2-get-the-braze-data-import-key}

Na Braze, navegue até **Integrações** > **Parceiros de tecnologia** e selecione **Adjust**.

Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. Depois que a chave é gerada, você pode criar outra ou invalidar uma existente. A chave de importação de dados e o endpoint REST são usados na próxima etapa ao configurar um postback no dashboard da Adjust.<br><br>![Esta imagem mostra a caixa "Importação de dados para atribuição de instalação" encontrada na página de tecnologia da Adjust. Essa caixa contém a chave de importação de dados e o endpoint REST.]({% image_buster /assets/img/attribution/adjust.png %}){: style="max-width:90%;"}

### Etapa 3: Configurar a Braze na Adjust {#step-3-configure-braze-in-adjust}

1. No dashboard da Adjust, navegue até **App Settings** e depois até **Partner Setup** e, em seguida, **Add Partners**.
2. Selecione **Braze (formerly Appboy)** e forneça a chave de importação de dados e o endpoint REST da Braze.
3. Clique em **Save & Close**.

### Etapa 4: Confirmar a integração {#step-4-confirm-the-integration}

Depois que a Braze receber dados de atribuição da Adjust, o indicador de status da conexão na página de parceiros de tecnologia da Adjust na Braze mudará de "Not Connected" para "Connected" e incluirá um registro de data e hora da última solicitação bem-sucedida.

Esse status é alterado somente depois que a Braze recebe dados sobre uma atribuição de instalação. A Braze ignora as instalações orgânicas (as exclui do postback da Adjust) e não as conta ao determinar se a conexão foi bem-sucedida.

## Campos de dados disponíveis {#available-data-fields}

Supondo que você configure sua integração conforme sugerido, a Braze mapeará os dados da Adjust para os filtros de segmento, conforme descrito na tabela a seguir.

| Campo de dados da Adjust | Filtro de segmento da Braze |
| --- | --- |
| `{network_name}` | Attributed Source |
| `{campaign_name}` | Attributed Campaign |
| `{adgroup_name}` | Attributed Adgroup |
| `{creative_name}` | Attributed Ad |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos de dados disponíveis" }

## Dados de atribuição do Facebook e do X (antigo Twitter) {#facebook-and-x-formerly-twitter-attribution-data}

Os dados de atribuição para campanhas do Facebook e do X (antigo Twitter) não estão disponíveis por meio de nossos parceiros. Essas fontes de mídia não permitem que seus parceiros compartilhem dados de atribuição com terceiros e, portanto, nossos parceiros não podem enviar esses dados para a Braze.

## URLs de rastreamento de cliques da Adjust na Braze (opcional) {#adjust-click-tracking-urls-in-braze-optional}

O uso de links de rastreamento de cliques em suas campanhas da Braze permitirá que você veja facilmente quais campanhas estão gerando instalações de apps e reengajamento. Como resultado, você poderá medir seus esforços de marketing de forma mais eficaz e tomar decisões baseadas em dados sobre onde investir mais recursos para obter o máximo de ROI.

Para começar a usar os links de rastreamento de cliques da Adjust, visite a [documentação](https://help.adjust.com/tracking/attribution/tracker-urls). Você pode inserir os links de rastreamento de cliques da Adjust diretamente em suas campanhas da Braze. A Adjust usará então suas [metodologias de atribuição probabilística](https://www.adjust.com/blog/attribution-compatible-with-ios14/) para atribuir o usuário que clicou no link. Recomendamos anexar seus links de rastreamento da Adjust com um identificador de dispositivo para melhorar a precisão das atribuições de suas campanhas na Braze. Isso atribuirá de forma determinística o usuário que clicou no link.

{% tabs local %}
{% tab Android %}
Para Android, a Braze permite que os clientes façam opt-in da [coleta do ID de publicidade do Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration/#google-advertising-id). O GAID também é coletado nativamente pela integração do SDK da Adjust. Você pode incluir o GAID nos seus links de rastreamento de cliques da Adjust utilizando a seguinte lógica Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto a Braze quanto a Adjust coletam automaticamente o IDFV de forma nativa por meio de nossas integrações de SDK. Isso pode ser usado como identificador do dispositivo. É possível incluir o IDFV em seus links de rastreamento de cliques da Adjust utilizando a seguinte lógica Liquid:

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
Se você atualmente não usa nenhum identificador de dispositivo — como o IDFV ou GAID — em seus links de rastreamento de cliques, ou não planeja usar no futuro, a Adjust ainda será capaz de atribuir esses cliques por meio de sua modelagem probabilística.
{% endalert %}