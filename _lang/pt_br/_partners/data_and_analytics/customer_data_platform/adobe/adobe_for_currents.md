---
nav_title: Adobe para Currents
article_title: Adobe para Currents
alias: /partners/adobe_for_currents/
description: "Este artigo de referência descreve a parceria entre Braze Currents e Adobe, uma CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente que permite que as marcas conectem e mapeiem seus dados da Adobe (atributos personalizados e Segments) para a Braze em tempo real."
page_type: partner
tool: Currents
search_tag: Partner
---

# Adobe para Currents {#adobe-for-currents}

> A [Adobe](https://www.adobe.com/) é uma CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente que permite que as marcas conectem e mapeiem seus dados da Adobe (atributos personalizados e Segments) para a Braze em tempo real.

A integração da Braze com a Adobe permite que você controle de forma contínua o fluxo de informações entre os dois sistemas. Com o [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), você também pode conectar dados à Adobe para torná-los acionáveis em toda a growth stack.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Currents | Para exportar dados de volta para a Adobe, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado para sua conta. |
| Conta do Adobe Experience Platform | Uma [conta do Adobe Experience Platform](https://experience.adobe.com/#/platform/home) é necessária para aproveitar esta parceria. |
| Permissão para criar um conector | Você precisa de permissões para criar uma conexão de fonte de streaming para usar esta integração. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Crie um esquema XDM na Adobe {#step-1-create-an-xdm-schema-in-adobe}

1. No Adobe Experience Platform, acesse **Schemas** > selecione **Create schema** > selecione **Experience Event** > selecione **Next**.<br><br>![Página de Schemas da Adobe para o esquema chamado "Braze Currents Walk-Through".]({% image_buster /assets/img/adobe/currents_sources.png %})<br><br>
2. Forneça um nome e uma descrição para seu esquema.
3. No painel **Composition**, configure os atributos do seu esquema:
- Em **Field groups**, selecione **Add** e, em seguida, adicione o grupo de campos **Braze Currents User Event**.
- Selecione **Save**.

Para saber mais sobre esquemas, consulte a documentação da Adobe sobre [criação de esquemas](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui).

### Etapa 2: Conecte a Braze à Adobe Experience Platform {#step-2-connect-braze-to-the-adobe-experience-platform}

1. No Adobe Experience Platform, acesse **Sources** > **Catalog** > **Marketing automation**.
2. Selecione **Add data** para Braze Currents.
3. Faça upload do [arquivo de amostra do Braze Currents](https://github.com/Appboy/currents-examples/blob/master/sample-data/Adobe/adobe_examples.json).<br><br>![Página "Add data" da Adobe.]({% image_buster /assets/img/adobe/currents_add_data.png %})<br><br>
4. Após o upload do seu arquivo, forneça os detalhes do seu fluxo de dados, incluindo informações sobre seu conjunto de dados e o esquema ao qual você está mapeando.
    - Se esta é a sua primeira vez conectando uma fonte de Braze Currents, crie um novo conjunto de dados e certifique-se de usar o esquema que você criou na [Etapa 1](#step-1-create-an-xdm-schema-in-adobe).
    - Se esta não é a sua primeira vez, use qualquer conjunto de dados existente que faça referência ao esquema da Braze.
5. Configure o mapeamento para seus dados e resolva os problemas.
    - Altere o mapeamento de `id` de `to _braze.appID` para `_id` no nível raiz do esquema.
    - Certifique-se de que `properties.is_amp` está mapeado para `_braze.messaging.email.isAMP`.
    - Exclua o mapeamento de `time` e `timestamp`, depois selecione o ícone de adicionar > **Add calculated field** e insira **time * 1000**. Selecione **Save**.
    - Selecione **Map target field** ao lado do novo campo de origem e mapeie-o para **timestamp** no nível raiz do esquema. <br><br>![Página "Add data" da Adobe com mapeamentos.]({% image_buster /assets/img/adobe/currents_mapping.png %})<br><br>
6. Selecione **Validate** para confirmar que você resolveu os problemas.

{% alert important %}
Os timestamps da Braze são expressos em segundos. Para refletir com precisão os timestamps na Adobe Experience Platform, seus campos calculados precisam estar em milissegundos. Para converter segundos em milissegundos, use o cálculo **time * 1000**.
{% endalert %}

{: start="7"}
7. Selecione **Next**, revise os detalhes do seu fluxo de dados e, em seguida, selecione **Finish**.<br><br>![Página "Add data" da Adobe sem erros de mapeamento.]({% image_buster /assets/img/adobe/currents_no_errors.png %})

### Etapa 3: Coletar credenciais {#step-3-gather-credentials}

Colete as seguintes credenciais para inserir na Braze, o que permitirá à Braze enviar dados para a Adobe Experience Platform.

| Campo         | Descrição                          |
|---------------|-------------------------------------|
| Client ID     | O ID do cliente associado à sua fonte do Adobe Experience Platform. |
| Client Secret | O segredo do cliente associado à sua fonte do Adobe Experience Platform. |
| Tenant ID     | O ID do tenant associado à sua fonte do Adobe Experience Platform. |
| Sandbox Name  | O sandbox associado à sua fonte do Adobe Experience Platform.   |
| Dataflow ID   | O ID do fluxo de dados associado à sua fonte do Adobe Experience Platform.   |
| Streaming Endpoint  | O endpoint de streaming associado à sua fonte do Adobe Experience Platform. A Braze converte isso automaticamente para o endpoint de streaming em lote. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Coletar credenciais" }

### Etapa 4: Configure o Currents para enviar dados para sua fonte de dados {#step-4-configure-currents-to-stream-data-to-your-data-source}

1. Na Braze, acesse **Integrações de parceiros** > **Exportação de dados** e selecione **Create New Current**.
2. Forneça o seguinte:
    - Um nome para o conector
    - Informações de contato para notificações sobre o conector
    - As credenciais da [Etapa 3](#step-3-gather-credentials)
3. Selecione os eventos que você deseja receber.
4. Opcionalmente, configure quaisquer exclusões ou transformações de campo desejadas.
5. Selecione **Launch Current**.