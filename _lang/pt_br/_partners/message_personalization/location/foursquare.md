---
nav_title: Foursquare
article_title: Foursquare
alias: /partners/foursquare/
description: "Este artigo de referência descreve a parceria entre a Braze e o Foursquare, uma plataforma de dados de localização, fornecendo disparo de eventos em tempo real com base no local."
page_type: partner
search_tag: Partner

---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="right" %}

> [O Foursquare](https://foursquare.com/) é uma plataforma de dados de localização que fornece direcionamento de dados de localização em suas campanhas na Braze. Use o Pilgrim SDK do Foursquare nos apps iOS e Android para fornecer disparos de eventos em tempo real com base no local, permitindo que você aproveite os poderosos recursos de direcionamento geográfico do Foursquare para enviar mensagens relevantes e personalizadas com a Braze.

_Esta integração é mantida pelo Foursquare._

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta do Foursquare | É necessário ter uma conta no Foursquare para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Espaço de trabalho e IDs de app da Braze | O espaço de trabalho e os IDs de app da Braze podem ser encontrados no [console de desenvolvedor]({{site.baseurl}}/api/api_key/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Para integrar as duas plataformas, é necessário integrar os dois SDKs e mapear os campos de usuário correspondentes. Após a integração do Pilgrim SDK, você receberá eventos de localização no dispositivo ou em um webhook.

### Etapa 1: Mapear campos de ID de usuário {#step-1-map-user-id-fields}

Para mapear corretamente os campos entre os dois SDKs, defina o mesmo ID de usuário em ambos os sistemas usando o [método `changeUser`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#setting-user-ids) no SDK da Braze e o método `setUserId` de [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data) no Pilgrim SDK.

### Etapa 2: Configurar o console do Pilgrim {#step-2-configure-pilgrim-console}
![Uma imagem do console do Pilgrim solicitando o ID do grupo, o ID do app Android e o ID do app iOS.]({% image_buster /assets/img_archive/pilgrim-dev-console.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Encontre os IDs do espaço de trabalho e do app no console de desenvolvedor da Braze. Em seguida, insira sua chave da API REST da Braze e os IDs do app no Foursquare Pilgrim Console.

Depois de configurar o Pilgrim Console, o Pilgrim SDK registrará os eventos de localização e os encaminhará para a Braze, permitindo que você redirecione e segmente clientes qualificados. Consulte o [site do desenvolvedor do Foursquare](https://developer.foursquare.com/) para obter mais detalhes.

{% alert important %}
O Pilgrim SDK requer que você ative os serviços de localização.
{% endalert %}

## Disparo de mensagens {#triggering-messages}

Depois que a integração estiver configurada, você poderá configurar uma campanha ou um Canvas que atuará a partir de eventos de localização gerados pelo Pilgrim SDK. Essa rota de integração é ideal para envio de mensagens em tempo real logo após os usuários entrarem em um local de interesse ou para comunicação de acompanhamento com postergação após a saída, como uma nota de agradecimento ou um lembrete.

Para enviar uma campanha de mensagens com base em um local definido:
- Crie uma campanha ou um Canvas na Braze que envie com **Entrega baseada em ação**
- Para seu gatilho, use um evento personalizado de `arrival` com um filtro de propriedade de evento para `locationType`, conforme mostrado na captura de tela a seguir.

![Uma campanha baseada em ação na etapa de entrega mostrando "arrival" selecionado como a opção "realizar evento personalizado", onde "locationType" é igual a "home".]({% image_buster /assets/img_archive/action-based-campaign.png %})

## Redirecionamento {#retargeting}

Para redirecionar seus usuários, use o Pilgrim SDK para definir um atributo personalizado `last_location` nos perfis de usuário da Braze. Em seguida, é possível usar a comparação `matches regex` para redirecionar os usuários que foram a um determinado local no mundo real, por exemplo, segmentando todos os usuários que estiveram recentemente em uma pizzaria.

![Uma campanha baseada em ação na etapa de usuários-alvo mostrando "last_location" igual a "Pizza Place".]({% image_buster /assets/img_archive/last-location-segment.png %})

Também é possível segmentar os usuários na Braze que visitaram um determinado tipo de local com base no `primaryCategoryId` do Foursquare em um determinado período de tempo. Para aproveitar esse ponto de dados para seus casos de uso de redirecionamento, registre `primaryCategoryId` como uma propriedade de evento durante o processo de segmentação do público. Para identificar os usuários e as propriedades usadas pela API do Foursquare e pelo Pilgrim SDK, consulte o [site do desenvolvedor do Foursquare](https://developer.foursquare.com/).