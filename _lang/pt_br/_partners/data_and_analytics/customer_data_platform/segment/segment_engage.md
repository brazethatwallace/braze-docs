---
nav_title: Segment Engage
article_title: Segment Engage
page_order: 3
alias: /partners/segment_personas/
alias: /partners/segment_engage/
alias: /partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/

description: "Este artigo de referência descreve a parceria entre a Braze e a Segment, uma plataforma de dados do cliente que coleta e encaminha informações entre fontes na sua stack de marketing."
page_type: partner
search_tag: Partner

---

# Segment Engage

> A [Segment](https://segment.com) é uma plataforma de dados do cliente que ajuda você a coletar, limpar e ativar os dados dos seus clientes. Este artigo de referência fornece uma visão geral da conexão entre [Braze e Segment Engage](https://segment.com/docs/destinations/braze/#Engage), além de descrever os requisitos e processos para a implementação e o uso adequados.

A integração entre Braze e Segment permite que você use o [Engage](https://segment.com/docs/engage/), o construtor de público integrado da Segment, para criar segmentos de usuários com base nos dados que você já coletou de diversas fontes. Esses públicos serão então sincronizados com a Braze como uma coorte, ou indicados no perfil do usuário por meio de [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) ou [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events) que podem ser usados para criar segmentos na Braze para uso em redirecionamento de Campaign e Canvas.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Segment | É necessário ter uma [conta da Segment](https://app.segment.com/login) para aproveitar essa parceria. |
| Destino na nuvem da Braze | Você já deve ter [configurado a Braze como um destino]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) na sua integração com a Segment.<br><br>Isso inclui fornecer o data center correto da Braze e a chave da REST API nas suas [configurações de conexão]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment#connection-settings). |
| Chave de importação de dados da Braze | Para sincronizar os públicos do Engage com a Braze como coortes, você deve gerar uma chave de importação de dados.<br><br>A importação de coorte está em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente da Braze para obter acesso a esse recurso. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração de destino de coortes {#cohorts-destination-integration}

### Etapa 1: crie um público no Engage {#step-1-create-an-engage-audience}
1. Na Segment, navegue até a guia **Audiences** no Engage e clique em **New**.
2. Crie seu público. Um raio no canto superior da página indicará se o público é atualizado em tempo real.
3. Em seguida, selecione Braze como seu destino.
4. Visualize seu público clicando em **Review & Create**. Por padrão, a Segment consulta todos os dados históricos para definir o valor atual do traço computado e do público. Para omitir esses dados, desmarque **Historical Backfill**.

### Etapa 2: capture sua chave de importação de dados da coorte {#step-2-capture-your-cohort-data-import-key}

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Segment**.

Aqui você encontrará seu endpoint REST e poderá gerar sua chave de importação de dados da Braze. Depois que a chave for gerada, você pode criar uma nova ou invalidar uma existente.

### Etapa 3: conecte o destino de coortes da Braze {#step-3-connect-the-braze-cohorts-destination}
Siga [as instruções da Segment](https://segment.com/docs/connections/destinations/catalog/actions-braze-cohorts/#getting-started) sobre como configurar o destino de coortes para sincronizar seus públicos do Engage como coortes na Braze.

### Etapa 4: crie um segmento na Braze a partir do público do Engage {#step-4-create-a-braze-segment-from-the-engage-audience}
Na Braze, navegue até **Segments**, crie um novo segmento e selecione **Segment Cohorts** como seu filtro. Aqui você pode escolher qual coorte da Segment deseja incluir. Depois que o segmento de coorte da Segment for criado, você pode selecioná-lo como um filtro de público ao criar uma Campaign ou Canvas.

![Criador de segmentos da Braze usando o filtro Segment Cohorts.]({% image_buster /assets/img/segment/segment3.png %})

## Integração no modo nuvem {#cloud-mode-integration}

### Etapa 1: crie um traço computado ou público na Segment {#step-1-create-a-segment-computed-trait-or-audience}

1. Na Segment, navegue até a guia **Computed Traits** ou **Audiences** em **Engage** e clique em **New**.
2. Crie seu traço computado ou público. Um raio no canto superior da página indicará se a computação é atualizada em tempo real.
3. Em seguida, selecione **Braze** como seu destino.
4. Visualize seu público clicando em **Review & Create**. Por padrão, a Segment consulta todos os dados históricos para definir o valor atual do traço computado e do público. Para omitir esses dados, desmarque **Historical Backfill**.
5. Nas configurações do traço computado ou público, ajuste as configurações de conexão com base em como você gostaria que seus dados fossem enviados para a Braze.

#### Traços computados e públicos {#computed-traits-and-audiences}

[Traços computados](https://segment.com/docs/engage/audiences/computed-traits/) e [públicos](https://segment.com/docs/Engage/audiences/) podem ser enviados para a Braze como atributos personalizados ou eventos personalizados.
- Traços e públicos enviados usando a chamada `identify` aparecerão na Braze como atributos personalizados.
- Traços e públicos enviados usando a chamada `track` aparecerão na Braze como eventos personalizados.

Você pode escolher qual método usar (ou optar por usar ambos) ao conectar o traço computado ao destino Braze.

{% tabs %}
{% tab Identify %}

Você pode enviar traços computados e públicos para a Braze como chamadas `identify` para criar atributos personalizados na Braze.

Por exemplo, se você tiver um traço computado do Engage para "Last Product Viewed Item", você encontrará `last_product_viewed_item` no perfil do usuário na Braze em **Custom Attributes**. Se fosse um público do Engage, você encontraria seu público listado em **Custom Attributes** definido como `true`.

| Traço computado | Públicos |
| -------------- | --------- |
| ![A seção de atributo personalizado dentro de um perfil de usuário lista "last_product_viewed_item" como "Sweater".]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![A seção de atributo personalizado dentro de um perfil de usuário lista "dormant_shopper" como "true".]({% image_buster /assets/img/segment/dormant-identify-braze.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Traços computados e públicos" }

{% endtab %}
{% tab Track %}

Você pode enviar traços computados e públicos para a Braze como chamadas `track` para criar eventos personalizados na Braze.

Continuando o exemplo anterior, se um usuário tiver um traço computado para "Last Product Viewed Item", ele aparecerá nos perfis dos usuários na Braze como `Trait Computed` com a contagem correspondente e o carimbo de data/hora mais recente em **Custom Events**. Se fosse um público do Engage, você encontraria seu público, contagem e o carimbo de data/hora mais recente listados em **Custom Attributes** definidos como `true`.

| Traço computado | Públicos |
| -------------- | --------- |
| ![A seção de evento personalizado dentro de um perfil de usuário lista "Trait Computed" "1" vez, sendo a última vez "há 20 horas".]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![A seção de atributo personalizado dentro de um perfil de usuário lista "Audience Entered" "1" vez, sendo a última vez "9 de março às 1:45 am".]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Traços computados e públicos" }

{% endtab %}
{% endtabs %}

### Etapa 2: segmentar usuários na Braze {#step-2-segment-users-in-braze}

Na Braze, para criar um segmento desses usuários, navegue até **Segments** em **Engagement**, crie um novo segmento e dê um nome a ele. Em seguida, com base na chamada que você usou:
- **Identify**: Selecione **custom attribute** como o filtro e localize seu atributo personalizado. Em seguida, use a opção "matches regex" (traço) ou a opção "equals" (público) e insira a variável apropriada.
- **Track**: Selecione **custom event** como o filtro e localize seu evento personalizado. Em seguida, use a opção "more than", "less than" ou "exactly" e insira o valor desejado. Isso dependerá de como você deseja definir seu segmento.

Depois de salvo, você pode referenciar esse segmento durante a criação de Canvas ou Campaign na etapa de direcionamento de usuários.

## Tempo de sincronização {#sync-time}

Embora a configuração padrão para a conexão da Braze com o Segment Engage seja `Realtime`, existem alguns filtros que impedirão a persona de sincronizar em tempo real, incluindo alguns filtros baseados em tempo que restringem o tamanho do seu público no momento do envio da mensagem.

## Teste com o debugger da Segment {#segment-debugger-testing}

O dashboard da Segment oferece um recurso "Debugger" que permite aos clientes testar se os dados de uma "Source" estão sendo transferidos para um "Destination" conforme esperado.

Esse recurso se conecta ao [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) da Braze, o que significa que só pode ser usado para usuários identificados (usuários que já possuem um ID de usuário no perfil de usuário da Braze).

Isso não funcionará para uma integração Braze lado a lado. Nenhum dado do servidor será transmitido se você não tiver inserido as informações corretas da REST API da Braze.