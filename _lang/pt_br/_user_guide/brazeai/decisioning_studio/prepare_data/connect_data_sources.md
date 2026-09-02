---
nav_title: Conectar seus dados
article_title: Conectar seus dados
page_order: 6
description: "Saiba como conectar fontes de dados de cliente ao BrazeAI Decisioning Studio para tomada de decisões por IA personalizada."
---

# Conectar seus dados {#connect-your-data}

> Os agentes do BrazeAI Decisioning Studio™ precisam compreender totalmente o contexto do cliente para tomar decisões eficazes. Este artigo explica como conectar fontes de dados de cliente ao Decisioning Studio.

{% alert tip %}
Sua equipe de AI Decisioning Services dará suporte na configuração das conexões de dados para desempenho ideal.
{% endalert %}

## Padrões de integração compatíveis {#supported-integration-patterns}

O Decisioning Studio oferece suporte a vários padrões de integração para conectar dados de clientes:

| Padrão de integração | Ideal para | Complexidade de configuração |
|---------------------|----------|------------------|
| **Braze Data Platform** | Clientes que já usam a Braze | Baixa |
| **Braze Cloud Data Ingestion (CDI)** | Conexão com data warehouses externos | Média |
| **Armazenamento em nuvem (Google Cloud Storage, AWS, Azure)** | Exportações diretas de dados de outras plataformas | Média |
| **Integrações CEP** | Extensões de dados SFMC e Klaviyo | Média |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Padrões de integração compatíveis" }

## Tipos de dados de clientes {#customer-data-types}

Os seguintes ativos de dados de clientes ajudam os agentes a personalizar de forma mais eficaz:

| Tipo de dado | Descrição | Exemplos |
|-----------|-------------|----------|
| **Perfil de usuário** | Atributos estáticos e de mudança lenta | Anos como cliente, localização geográfica, canal de aquisição, nível de satisfação, estimativa de valor do tempo de vida |
| **Comportamento do cliente** | Padrões de atividade e engajamento | Logins na conta, tipo de dispositivo, interações com atendimento ao cliente, uso do produto |
| **Histórico de transações** | Dados de compras e conversões | Produtos comprados, valores de transação, métodos de pagamento, canais de compra |
| **Engajamento de marketing** | Respostas a comunicações | Aberturas/cliques de e-mail, engajamento por SMS, atividade na web e em dispositivos móveis, respostas a pesquisas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipos de dados de clientes" }

{% alert tip %}
Quanto mais informações os agentes tiverem sobre seus clientes, melhor será o desempenho deles. Considere incluir dados sobre quaisquer insights que sejam particularmente importantes para o seu negócio (por exemplo, você quer ver como a IA trata seus clientes de fidelidade de forma diferente? Certifique-se de que o status de fidelidade esteja nos dados de clientes).
{% endalert %}

## Conectar dados por plataforma {#connect-data-by-platform}

{% tabs %}
{% tab Braze %}

### Enviar dados de clientes pela Braze {#send-customer-data-through-braze}

O BrazeAI Decisioning Studio pode usar todos os dados que você já está enviando para a Braze Data Platform.

Para dados de clientes que não estão no perfil de usuário ou em atributos personalizados, há duas formas de trazê-los com a [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion):

- Ingerir na Braze Data Platform. Sincronize dados do data warehouse com perfis de usuário, atributos personalizados ou eventos da Braze. Escolha essa opção quando você também quiser que os dados estejam disponíveis na Braze para segmentação e envio de mensagens. Compatível com Snowflake, Redshift, BigQuery, Databricks, Microsoft Fabric, AWS S3 e Google Cloud Storage.
- Enviar diretamente para o Decisioning Studio (Acesso Antecipado). Sincronize dados do data warehouse diretamente com o Decisioning Studio, sem adicioná-los ao perfil de usuário ou aos atributos personalizados da Braze. Escolha essa opção para dados que você quer que o Decisioning Studio use, mas que não são necessários em outras áreas da Braze. Essa opção está em acesso antecipado. Consulte [Cloud Data Ingestion: sincronizar dados do Decisioning Studio]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/decisioning_studio) para configurá-la.

Quando estiver satisfeito com os dados que está enviando para a Braze Data Platform, entre em contato com sua equipe de AI Decisioning Services para discutir quais campos do perfil de usuário ou atributos personalizados devem ser usados para o AI Decisioning.

Para agilizar esse processo, crie uma lista de atributos do perfil de usuário da Braze que você acredita representar melhor os comportamentos dos seus clientes e que devem ser usados no Decisioning Studio (consulte a [lista de campos disponíveis]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#fields-to-export)). Sua equipe de serviços também pode ajudar você a conduzir sessões de descoberta para decidir quais campos são mais apropriados para o AI Decisioning.

Outras opções para enviar dados incluem:

- Enviar eventos personalizados da Braze via SDK
- Enviar eventos usando o endpoint REST ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

Esses padrões exigem mais esforço de engenharia, mas às vezes são preferíveis dependendo da sua configuração atual da Braze. Entre em contato com a equipe de AI Decisioning Services para saber mais.

{% endtab %}
{% tab SFMC %}

### Enviar dados de clientes pelo SFMC {#send-customer-data-through-sfmc}

Para integrações com o Salesforce Marketing Cloud:

1. Configure as Data Extension(s) do SFMC para seus dados de clientes
2. Configure o SFMC Installed Package para integração via API com as permissões apropriadas exigidas pelo Decisioning Studio
3. Certifique-se de que as data extensions sejam atualizadas diariamente, pois o Decisioning Studio extrairá os dados incrementais mais recentes disponíveis

Forneça o ID da extensão e a chave de API para sua equipe de AI Decisioning Services. Eles ajudarão com as próximas etapas na ingestão de dados de clientes.

{% endtab %}
{% tab Klaviyo %}

### Enviar dados de clientes pelo Klaviyo {#send-customer-data-through-klaviyo}

Para integrações com o Klaviyo:

1. Confirme que os dados do perfil de cliente estão disponíveis nos perfis do Klaviyo
2. Gere uma chave de API privada com acesso completo a perfis
3. Forneça a chave de API para sua equipe de AI Decisioning Services

Consulte a [documentação do Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) para saber mais sobre a configuração de chaves de API.

{% endtab %}
{% tab Cloud Storage %}

### Outras soluções em nuvem (Google Cloud Storage, Azure, AWS) {#other-cloud-solutions-google-cloud-storage-azure-aws}

Se os dados de clientes não estão armazenados atualmente na Braze, no SFMC ou no Klaviyo, a melhor próxima etapa é configurar uma exportação automatizada diretamente para um bucket do Google Cloud Storage controlado pela Braze. Também oferecemos suporte para exportação para AWS ou Azure (embora o GCS seja preferível). Para essas plataformas, exporte para o armazenamento em nuvem interno dessas plataformas e a Braze poderá então extrair esses dados.

Para determinar se isso é viável, consulte a documentação da sua plataforma de MarTech. Por exemplo:

- O mParticle oferece uma [integração nativa com o Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/)
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

Se isso for viável, podemos fornecer um bucket do GCS para exportar dados de clientes, isolado para o Decisioning Studio.

{% endtab %}
{% endtabs %}

## Práticas recomendadas {#best-practices}

- **Nomes de colunas descritivos:** Os dados de clientes devem ter nomes de colunas claros e descritivos. O ideal é que um dicionário de dados seja fornecido.
- **Atualizações incrementais:** Arquivos incrementais são preferíveis em vez de snapshots de todo o histórico do cliente todos os dias.
- **Identificadores consistentes:** Cada registro deve conter um identificador único de cliente que seja consistente em todos os ativos de dados.
- **Incluir timestamps:** Os registros devem ter timestamps associados para atribuição precisa e treinamento do agente.

## Integrações personalizadas {#custom-integrations}

Outras opções ou pipelines de dados completamente personalizados são possíveis. Eles podem exigir trabalho adicional de serviços ou de engenharia da sua equipe. Para determinar o que é viável e ideal, trabalhe com sua equipe de AI Decisioning Services.

{% alert important %}
Este guia explica os padrões de integração mais comuns. A equipe de Segurança da Informação ainda precisará avaliar todos os pontos de conexão, e os consultores de soluções estarão disponíveis para orientar sobre a implementação.
{% endalert %}

## Próximas etapas {#next-steps}

Após conectar suas fontes de dados, prossiga para configurar a orquestração:

- [Configurar a orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/orchestration_setup)