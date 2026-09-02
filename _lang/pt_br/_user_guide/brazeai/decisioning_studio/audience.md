---
nav_title: Defina seu público
article_title: Defina seu público
page_order: 3
page_type: reference
description: "Saiba como definir e configurar o público do seu agente do BrazeAI Decisioning Studio, incluindo grupos de tratamento e etapas de configuração específicas por plataforma."
---

# Defina seu público {#define-your-audience}

> Os públicos de casos de uso são normalmente definidos em uma plataforma de engajamento com clientes (como a Braze ou o Salesforce Marketing Cloud) e, em seguida, enviados ao agente do Decisioning Studio. O agente então divide os clientes em grupos de tratamento para conduzir testes controlados randomizados.

## Grupos de tratamento {#treatment-groups}

| Grupo | Descrição |
|-------|-----------|
| **Decisioning Studio** | Clientes que recebem recomendações otimizadas por IA |
| **Controle aleatório** | Clientes que recebem opções selecionadas aleatoriamente (comparação de referência) |
| **Business-as-Usual (opcional)** | Clientes que recebem a jornada de marketing atual (para comparação com o desempenho existente) |
| **Holdout (opcional)** | Clientes que não recebem comunicações (para medir o impacto geral da campanha) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Grupos de tratamento" }

## Configure seu público {#configure-your-audience}

{% tabs %}
{% tab Braze %}

1. Crie um Segment or segmento or segmento para o público que você deseja direcionar.
2. Forneça o ID do Segment or segmento or segmento à sua equipe de AI Decisioning Services.

{% alert note %}
Na Braze, é possível ingerir múltiplos segmentos e combiná-los para criar o público. O Decisioning Studio pode ingerir um Segment or segmento or segmento para uma Campaign de comparação Business-as-Usual. Todos esses padrões são aceitáveis.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

1. Configure uma Data Extension do SFMC para o seu público e forneça o ID da data extension.
2. Configure um SFMC Installed Package para integração via API or interface de programação do aplicativo (API) com as permissões apropriadas exigidas pelo Decisioning Studio.
3. Confirme que essa data extension é atualizada diariamente, pois o Decisioning Studio extrai os dados incrementais mais recentes disponíveis.

Forneça o ID da extensão e a chave de API or interface de programação do aplicativo (API) à nossa equipe de AI Decisioning Services, que auxiliará nas próximas etapas de ingestão de dados de cliente.

{% endtab %}
{% tab Outras plataformas %}

### Google Cloud Storage

Se o público não está armazenado atualmente na Braze ou no Salesforce Marketing Cloud, a melhor alternativa é configurar uma exportação automatizada diretamente para um bucket do Google Cloud Storage (GCS) controlado pela Braze.

Para determinar se isso é viável, consulte a documentação da sua plataforma. Por exemplo, o mParticle oferece uma [integração nativa com o Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/). Se esse for o caso, podemos fornecer um bucket do GCS para exportar os dados do público.

### Recursos adicionais {#additional-resources}

- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## Próximas etapas {#next-steps}

Após definir seu público, prossiga para configurar a orquestração:

- [Configurar a orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/orchestration_setup)