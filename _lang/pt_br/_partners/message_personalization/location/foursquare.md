---
nav_title: Foursquare
article_title: Foursquare
alias: /partners/foursquare/
description: "Este artigo de referência descreve a parceria entre a Braze e o Foursquare, uma plataforma de dados de localização que fornece disparo de eventos em tempo real com base no local."
page_type: partner
search_tag: Partner
---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="right" %}

> O [Foursquare](https://foursquare.com/) é uma plataforma de dados de localização que fornece direcionamento de dados de localização em suas campanhas na Braze. Use o Pilgrim SDK or kit de desenvolvimento de software do Foursquare nos apps iOS e Android para fornecer disparos de eventos em tempo real com base no local, permitindo que você aproveite os poderosos recursos de direcionamento geográfico do Foursquare para enviar mensagens relevantes e personalizadas com a Braze.

_Esta integração é mantida pelo Foursquare._

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Foursquare | Uma conta Foursquare é necessária para aproveitar essa parceria. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões de `users.track`. <br><br> Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Espaço de trabalho e IDs de app da Braze | O espaço de trabalho e os IDs de app da Braze podem ser encontrados no [console de desenvolvedor]({{site.baseurl}}/api/basics). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Para integrar as duas plataformas, você deve integrar os dois SDKs e mapear os campos de usuário correspondentes. Após integrar o Pilgrim SDK or kit de desenvolvimento de software, você receberá eventos de local no dispositivo ou por meio de um webhook.

### Etapa 1: Mapear campos de ID de usuário {#step-1-map-user-id-fields}

Para mapear corretamente os campos entre os dois SDKs, defina o mesmo ID de usuário em ambos os sistemas usando o [método `changeUser`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#setting-user-ids) no SDK or kit de desenvolvimento de software da Braze e o método `setUserId` do [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data) no Pilgrim SDK or kit de desenvolvimento de software.

### Etapa 2: Configurar o console do Pilgrim {#step-2-configure-pilgrim-console}
![Uma imagem do console do Pilgrim solicitando Group ID, Android App ID e iOS App ID.]({% image_buster /assets/img_archive/pilgrim-dev-console.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Encontre o espaço de trabalho e os App IDs no console de desenvolvedor da Braze. Em seguida, insira sua chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze e os App IDs no Foursquare Pilgrim Console.

Depois de configurar o Pilgrim Console, o Pilgrim SDK or kit de desenvolvimento de software registrará eventos de local e os encaminhará para a Braze, permitindo que você redirecione e segmente clientes qualificados. Consulte o [site para desenvolvedores do Foursquare](https://developer.foursquare.com/) para mais detalhes.

{% alert important %}
O Pilgrim SDK or kit de desenvolvimento de software requer que você ative os serviços de localização.
{% endalert %}

## Disparo de mensagens {#triggering-messages}

Depois que a integração estiver configurada, você pode criar uma Campaign ou Canvas que responda aos eventos de localização gerados pelo SDK or kit de desenvolvimento de software do Pilgrim. Essa rota de integração é ideal para envio de mensagens em tempo real logo após os usuários entrarem em um local de interesse, ou para comunicações de acompanhamento com postergação após a saída, como uma nota de agradecimento ou lembrete.

Para enviar uma Campaign que enviará mensagens com base em um local definido:
- Crie uma Campaign ou Canvas da Braze que envie com **entrega baseada em ação**
- Para o seu disparador, use um evento personalizado de `arrival` com um filtro de propriedade de evento para `locationType`, conforme mostrado na captura de tela a seguir.

![Uma Campaign baseada em ação na etapa de entrega mostrando "arrival" selecionado como opção de "perform custom event", onde "locationType" é igual a "home".]({% image_buster /assets/img_archive/action-based-campaign.png %})

## Redirecionamento {#retargeting}

Para redirecionar seus usuários, use o SDK or kit de desenvolvimento de software Pilgrim para definir um atributo personalizado `last_location` nos perfis de usuário dos seus usuários da Braze. Você pode então usar a comparação `matches regex` para redirecionar usuários que foram a um local específico no mundo real — por exemplo, segmentando todos os usuários que estiveram recentemente em uma pizzaria.

![Uma Campaign baseada em ação na etapa de direcionamento de usuários mostrando "last_location" igual a "Pizza Place".]({% image_buster /assets/img_archive/last-location-segment.png %})

Você também pode segmentar usuários na Braze que visitaram um tipo específico de estabelecimento com base no `primaryCategoryId` do Foursquare em um período de tempo específico. Para aproveitar esse ponto de dados nos seus casos de uso de redirecionamento, registre o `primaryCategoryId` como uma propriedade de evento durante o processo de segmentação de público. Para identificar os usuários e propriedades usados pela API or interface de programação do aplicativo (API) do Foursquare e pelo SDK or kit de desenvolvimento de software Pilgrim, consulte o [site de desenvolvedores do Foursquare](https://developer.foursquare.com/).