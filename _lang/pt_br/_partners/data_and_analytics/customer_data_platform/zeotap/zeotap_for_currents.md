---
nav_title: Zeotap para Currents
article_title: Zeotap para Currents
description: "Este artigo de referência descreve a parceria entre Braze Currents e Zeotap, uma CDP de próxima geração que ajuda você a descobrir e entender seu público móvel, fornecendo resolução de identidade, insights e enriquecimento de dados."
page_type: partner
tool: Currents
search_tag: Partner
---

# Zeotap para Currents {#zeotap-for-currents}

> A [Zeotap](https://zeotap.com/) é uma CDP de próxima geração que ajuda você a descobrir e entender seu público móvel, fornecendo resolução de identidade, insights e enriquecimento de dados.

A integração da Braze com a Zeotap permite que você amplie a escala e o alcance das suas campanhas sincronizando os segmentos de clientes da Zeotap com os perfis de usuários da Braze. Com o [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), você também pode conectar dados à Zeotap para torná-los acionáveis em toda a growth stack.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta Zeotap | É necessário ter uma [conta da Zeotap](https://zeotap.com/) para aproveitar essa parceria. |
| Currents | Para exportar dados de volta para a Zeotap, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) configurado na sua conta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Implementação {#implementation}

### Etapa 1: Crie uma fonte no Currents {#step-1-create-a-currents-source}

1. Na Zeotap, acesse **Sources** em **Integrate**.
2. Selecione **Create Source**.
3. Selecione **Customer Engagement Channels** como a categoria.<br><br>![Uma janela "Create Source" listando diferentes categorias, incluindo "Customer Engagement Channels".]({% image_buster /assets/img/zeotap/cec.png %}){: style="max-width:70%;"}<br><br>
4. Selecione **Braze** como a fonte de dados.
5. Insira um nome para a fonte.
6. Selecione sua região.<br><br>![Janela com opções para selecionar sua região e entidade de dados.]({% image_buster /assets/img/zeotap/select_region.png %}){: style="max-width:70%;"}<br><br>
7. Selecione **Create Source**.
8. Acesse a guia **Implementation Details** e anote a **API URL** e a **Write Key**.<br><br>![Detalhes de implementação do Braze Currents contendo a API URL e a Write Key.]({% image_buster /assets/img/zeotap/implementation_details.png %})

### Etapa 2: Configure o fluxo de dados no Currents {#step-2-configure-data-streaming-in-currents}

1. Na Braze, acesse **Integrações de parceiros** > **Exportação de dados**.
2. Selecione **Create New Current** e depois **Custom Currents Export**.<br><br>![O botão "Create New Current" com um menu suspenso contendo "Custom Currents Export".]({% image_buster /assets/img/zeotap/custom_currents_export.png %}){: style="max-width:60%;"}<br><br>
3. Insira um nome de integração e um e-mail para contato caso ocorram erros com a integração.
4. Em **Credentials**, insira as informações que você anotou na [Etapa 1](#step-1-create-a-currents-source):
- A API URL como o **Endpoint**
- A Write Key como o **Bearer Token**<br><br>![Seções para inserir detalhes de integração e credenciais.]({% image_buster /assets/img/zeotap/credentials.png %})<br><br>
5. Selecione os eventos de engajamento com mensagem que você deseja enviar para a Zeotap.<br><br>![A guia "General Settings" com uma seção para selecionar eventos de engajamento com mensagem.]({% image_buster /assets/img/zeotap/message_engagement_events.png %})
6. Selecione **Launch Current** para salvar as alterações e começar a enviar eventos para a Zeotap.

{% alert important %}
O conector do Currents não oferece suporte a usuários anônimos (usuários sem um `external_id`).
{% endalert %}