---
nav_title: Zeotap
description: "Este artigo de referência descreve a parceria entre a Braze e a Zeotap, uma CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente de última geração que fornece resolução de identidade, insights e enriquecimento."
page_type: partner
search_tag: Partner
page_order: 1
---

# Zeotap

> A [Zeotap](https://zeotap.com/) é uma CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente de última geração que ajuda você a descobrir e entender seu público móvel, fornecendo resolução de identidade, insights e enriquecimento de dados.

Com a integração da Zeotap e da Braze, você pode ampliar a escala e o alcance das suas campanhas sincronizando os segmentos de clientes da Zeotap para mapear os dados de usuários para as contas de usuários da Braze. Em seguida, é possível agir com base nesses dados, oferecendo experiências personalizadas e direcionadas aos seus usuários.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta Zeotap | É necessário ter uma [conta da Zeotap](https://zeotap.com/) para aproveitar essa parceria. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Endpoint REST da Braze | A URL do seu endpoint REST. Seu endpoint dependerá da [URL da Braze para sua instância]({% image_buster /assets/img/zeotap/zeotap1.png %}). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Criar um destino Zeotap {#step-1-create-a-zeotap-destination}

1. Na plataforma Zeotap Unity, navegue até o aplicativo **DESTINATIONS**.
2. Em **All Channels**, selecione **Braze**.
3. No prompt exibido, dê um nome ao seu destino e forneça o nome do cliente e a chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze associados à sua conta da Braze.
4. Por fim, selecione sua instância de endpoint REST da Braze no menu suspenso e salve o destino. <br><br>![Configuração do destino Zeotap para Braze com menu suspenso de instância de endpoint.]({% image_buster /assets/img/zeotap/zeotap1.png %})

### Etapa 2: Crie e vincule um Segment or segmento or segmento Zeotap ao seu destino {#step-2-create-and-link-a-zeotap-segment-to-your-destination}

1. Na plataforma Zeotap Unity, navegue até o aplicativo **CONNECT**.
2. Crie um Segment or segmento or segmento e selecione o destino Braze criado na etapa 1.
3. Selecione um identificador de saída compatível: MAIDs, endereço de e-mail com hash SHA256 ou qualquer identificador de cliente 1P reconhecido pela Braze (se quiser usar um identificador personalizado para sua conta da Braze, entre em contato com a Zeotap para que ele possa ser ativado para sua conta). Somente um identificador de saída pode ser usado para a integração com a Braze. Esses identificadores devem ser os mesmos que o ID externo definido ao coletar dados do Braze SDK or kit de desenvolvimento de software.
4. Salve o Segment or segmento or segmento.

![Configuração de segmento Zeotap CONNECT vinculado ao destino Braze.]({% image_buster /assets/img/zeotap/zeotap2.png %})

{% alert note %}
Os identificadores que aparecem estão disponíveis no Segment or segmento or segmento e são compatíveis com a Braze.
{% endalert %}

### Etapa 3: Criar um Segment or segmento na Braze {#step-3-create-braze-segment}

Após a criação, o envio e o processamento bem-sucedidos de um Segment or segmento or segmento na Zeotap, os usuários da Zeotap aparecerão no dashboard da Braze. Você pode procurar usuários por ID de usuário no dashboard da Braze.

![Um perfil de usuário da Braze mostrando os segmentos de um a quatro listados como "true" em "Custom attributes".]({% image_buster /assets/img/zeotap/zeotap4.png %})

Se um usuário fizer parte do Segment or segmento or segmento Zeotap, o nome do Segment or segmento or segmento aparecerá como um atributo personalizado em seu perfil de usuário com o valor booleano `true`. Anote o nome do atributo personalizado, pois você precisará dele ao criar um Segment or segmento or segmento na Braze.

Em seguida, você deve criar e definir esse Segment or segmento or segmento na Braze:
1. No dashboard da Braze, selecione **Segments** e depois **Create Segment**.
2. Em seguida, dê um nome ao seu Segment or segmento or segmento e selecione o Segment or segmento or segmento de atributo personalizado criado na Zeotap.
3. Salve suas alterações.

![No criador de segmentos da Braze, você pode encontrar os segmentos importados definidos como atributos personalizados.]({% image_buster /assets/img/zeotap/zeotap3.png %})

Agora é possível adicionar esse Segment or segmento or segmento recém-criado a futuras Campaigns e Canvas da Braze para direcionar esses usuários finais.