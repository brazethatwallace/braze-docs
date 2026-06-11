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

## Padrões de integração suportados {#supported-integration-patterns}

O Decisioning Studio suporta múltiplos padrões de integração para conectar dados de cliente:

| Padrão de integração | Ideal para | Complexidade de configuração |
|---------------------|----------|------------------|
| **Braze Data Platform** | Clientes que já utilizam a Braze | Baixa |
| **Ingestão de dados na nuvem (CDI) da Braze** | Conectar data warehouses externos | Média |
| **Armazenamento em nuvem (GCS, AWS, Azure)** | Exportações diretas de dados de outras plataformas | Média |
| **Integrações com CEP** | Extensões de dados do SFMC e Klaviyo | Média |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Supported integration patterns" }

## Tipos de dados de cliente {#customer-data-types}

Os seguintes ativos de dados de cliente ajudam os agentes a personalizar de forma mais eficaz:

| Tipo de dado | Descrição | Exemplos |
|-----------|-------------|----------|
| **Perfil do cliente** | Atributos estáticos e de mudança lenta | Tempo como cliente, localização geográfica, canal de aquisição, nível de satisfação, estimativa de lifetime value |
| **Comportamento do cliente** | Padrões de atividade e engajamento | Logins na conta, tipo de dispositivo, interações com atendimento ao cliente, uso do produto |
| **Histórico de transações** | Dados de compra e conversão | Produtos comprados, valores de transação, métodos de pagamento, canais de compra |
| **Engajamento de marketing** | Respostas a comunicações | Aberturas/cliques de e-mail, engajamento por SMS, atividade web e mobile, respostas a pesquisas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Customer data types" }

{% alert tip %}
Quanto mais informações os agentes tiverem sobre seus clientes, melhor será o desempenho deles. Considere incluir dados sobre quaisquer insights que sejam particularmente importantes para o seu negócio (por exemplo, você quer ver como a IA trata seus clientes de fidelidade de forma diferente? Certifique-se de que o status de fidelidade esteja nos dados de cliente).
{% endalert %}

## Conectar dados por plataforma {#connect-data-by-platform}

{% tabs %}
{% tab Braze %}

### Enviar dados de cliente pela Braze {#send-customer-data-through-braze}

O BrazeAI Decisioning Studio pode utilizar todos os dados que você já está enviando para a Braze Data Platform.

Se houver dados de cliente que você deseja usar no Decisioning Studio e que não estão armazenados atualmente no perfil de usuário ou em atributos personalizados, a abordagem recomendada é usar a [Ingestão de dados na nuvem da Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) para ingerir dados de outras fontes.

A CDI suporta integrações diretas com:

- Snowflake
- Redshift
- BigQuery
- Databricks
- Microsoft Fabric
- AWS S3

Para a lista completa de fontes suportadas, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/).

Quando estiver satisfeito com os dados que está enviando para a Braze Data Platform, entre em contato com sua equipe de AI Decisioning Services para discutir quais campos do perfil de usuário ou atributos personalizados devem ser usados para a tomada de decisões por IA.

Para agilizar esse processo, crie uma lista de atributos do perfil de usuário da Braze que você acredita que melhor representam os comportamentos dos seus clientes e que devem ser usados no Decisioning Studio (consulte a [lista de campos disponíveis]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#fields-to-export)). Sua equipe de serviços também pode ajudar a conduzir sessões de descoberta para decidir quais campos são mais apropriados para a tomada de decisões por IA.

Outras opções para enviar dados incluem:

- Enviar eventos personalizados da Braze via SDK
- Enviar eventos usando o endpoint REST ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/))

Esses padrões exigem mais esforço de engenharia, mas às vezes são preferíveis dependendo da sua configuração atual da Braze. Entre em contato com a equipe de AI Decisioning Services para saber mais.

{% endtab %}
{% tab SFMC %}

### Enviar dados de cliente pelo SFMC {#send-customer-data-through-sfmc}

Para integrações com o Salesforce Marketing Cloud:

1. Configure as extensões de dados (Data Extensions) do SFMC para seus dados de cliente
2. Configure o pacote instalado (Installed Package) do SFMC para integração via API com as permissões apropriadas exigidas pelo Decisioning Studio
3. Certifique-se de que as extensões de dados sejam atualizadas diariamente, pois o Decisioning Studio extrairá os dados incrementais mais recentes disponíveis

Forneça o ID da extensão e a chave de API para sua equipe de AI Decisioning Services. Eles auxiliarão nas próximas etapas de ingestão dos dados de cliente.

{% endtab %}
{% tab Klaviyo %}

### Enviar dados de cliente pelo Klaviyo {#send-customer-data-through-klaviyo}

Para integrações com o Klaviyo:

1. Confirme que os dados do perfil do cliente estão disponíveis nos perfis do Klaviyo
2. Gere uma chave de API privada com acesso completo a perfis
3. Forneça a chave de API para sua equipe de AI Decisioning Services

Consulte a [documentação do Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) para mais informações sobre a configuração de chaves de API.

{% endtab %}
{% tab Cloud Storage %}

### Outras soluções em nuvem (Google Cloud Storage, Azure, AWS) {#other-cloud-solutions-google-cloud-storage-azure-aws}

Se os dados de cliente não estão armazenados atualmente na Braze, no SFMC ou no Klaviyo, a melhor alternativa é configurar uma exportação automatizada diretamente para um bucket do Google Cloud Storage controlado pela Braze. Também oferecemos suporte para exportação para AWS ou Azure (embora o GCS seja preferível). Para essas plataformas, exporte para o armazenamento em nuvem interno dessas plataformas e a Braze poderá então extrair esses dados.

Para determinar se isso é viável, consulte a documentação da sua plataforma MarTech. Por exemplo:

- O mParticle oferece uma [integração nativa com o Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/)
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

Se isso for viável, podemos fornecer um bucket GCS para exportar dados de cliente, isolado para o Decisioning Studio.

{% endtab %}
{% endtabs %}

## Práticas recomendadas {#best-practices}

- **Nomes de colunas descritivos:** Os dados de cliente devem ter nomes de colunas claros e descritivos. Idealmente, um dicionário de dados deve ser fornecido.
- **Atualizações incrementais:** Arquivos incrementais são preferíveis em vez de snapshots de todo o histórico do cliente todos os dias
- **Identificadores consistentes:** Cada registro deve conter um identificador único de cliente que seja consistente em todos os ativos de dados
- **Inclua timestamps:** Os registros devem ter timestamps associados para atribuição precisa e treinamento do agente

## Integrações personalizadas {#custom-integrations}

Outras opções ou pipelines de dados completamente personalizados são possíveis. Eles podem exigir trabalho adicional de serviços ou esforço de engenharia da sua equipe. Para determinar o que é viável e ideal, trabalhe com sua equipe de AI Decisioning Services.

{% alert important %}
Este guia explica os padrões de integração mais comuns. A equipe de Segurança da Informação ainda precisará avaliar todos os pontos de conexão, e os consultores de soluções estarão disponíveis para orientar na implementação.
{% endalert %}

## Próximas etapas {#next-steps}

Após conectar suas fontes de dados, prossiga para configurar a orquestração:

- [Configurar a orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/orchestration_setup/)