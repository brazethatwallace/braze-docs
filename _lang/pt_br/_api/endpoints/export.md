---
nav_title: Exportar
article_title: Endpoints de exportação
search_tag: Endpoint
page_order: 2
description: "Este artigo de referência explica os endpoints de exportação da Braze, incluindo pré-requisitos, o que você pode exportar, como os dados são entregues e uma lista completa."
page_type: reference
---

# Endpoints de exportação {#export-endpoints}

Com esta coleção de endpoints, você pode acessar e exportar vários níveis de detalhes sobre seus KPIs, sessões de app, usuários, Segments, Campaigns e Canvas. Certifique-se de conhecer sua [instância da Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints), [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics) e [identificador de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/identifier_types) ao criar seus parâmetros e corpos de solicitação.

## Pré-requisitos {#prerequisites}

Antes de começar, verifique se você tem o seguinte:

| Requisito | Descrição |
| --- | --- |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional com as permissões de exportação apropriadas para os endpoints que você pretende chamar. As chaves de API or interface de programação do aplicativo (API) são vinculadas a endpoints específicos, e as permissões não podem ser alteradas após a criação. Para mais detalhes, consulte [Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional]({{site.baseurl}}/api/basics#about-rest-api-keys). |
| Identificadores relevantes | Os identificadores dos dados que você deseja exportar, como um ID de Campaign, ID de Segment or segmento ou ID de Canvas. Você pode encontrá-los no dashboard da Braze. Para uma lista completa, consulte [Tipos de identificadores de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/identifier_types). |
| Credenciais de armazenamento em nuvem (opcional) | Se você estiver exportando grandes conjuntos de dados, conecte um bucket do [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3), [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents) ou [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents) para que os arquivos de exportação sejam gravados diretamente no seu armazenamento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{% alert note %}
Se você é um profissional de marketing ou membro da equipe sem acesso à API or interface de programação do aplicativo (API), coordene com um desenvolvedor ou administrador da sua organização para configurar chaves de API or interface de programação do aplicativo (API) e integrações.
{% endalert %}

## O que você pode exportar {#what-you-can-export}

A tabela a seguir resume as categorias de dados disponíveis por meio das APIs de exportação.

| Categoria | O que inclui | Referência da API or interface de programação do aplicativo (API) |
| --- | --- | --- |
| Campaigns | Análise de desempenho, detalhes de Campaign, listas de Campaigns e análise de envios | [Endpoints de Campaign]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) |
| Canvas | Análise de séries de dados, resumos de análise, detalhes de Canvas e listas de Canvas | [Endpoints de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) |
| Segments | Listas de Segments, análise de Segments e detalhes de Segments | [Endpoints de Segment or segmento]({{site.baseurl}}/api/endpoints/export/segments/get_segment) |
| Dados de usuários | Perfis completos de usuários por identificador ou por Segment or segmento or segmento, e usuários por grupo de controle global | [Endpoints de dados de usuários]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) |
| KPIs | Usuários ativos diários, usuários ativos mensais, novos usuários diários e desinstalações por data | [Endpoints de KPI]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) |
| Sessões | Dados de séries temporais de sessões do app | [Endpoint de sessões]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) |
| Eventos personalizados | Nomes de eventos, listas de eventos e análise de eventos ao longo do tempo | [Endpoints de eventos personalizados]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) |
| Atributos personalizados | Nomes de atributos | [Endpoint de atributos personalizados]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) |
| Compras | Dados de receita por período, listas de IDs de produtos e contagens de compras | [Endpoints de compras]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="O que você pode exportar" }

## Como os dados de exportação são entregues {#how-export-data-is-delivered}

As exportações de API or interface de programação do aplicativo (API) retornam dados em formato JSON, diferentemente dos arquivos CSV que você baixa do dashboard. O método de entrega depende de você ter ou não armazenamento em nuvem conectado:

- **Sem armazenamento em nuvem:** a Braze grava os arquivos de exportação em seu próprio bucket S3 e inclui uma URL de download temporária na resposta da API or interface de programação do aplicativo (API). Essa URL expira após quatro horas, e a exportação é empacotada como um arquivo compactado (ZIP ou GZIP, dependendo do parâmetro `output_format`) contendo arquivos JSON. Cada linha nos arquivos JSON representa um objeto de dados.
- **Com armazenamento em nuvem conectado:** a Braze grava os arquivos de exportação diretamente no seu bucket configurado. A resposta da API or interface de programação do aplicativo (API) não inclui uma URL de download. Os arquivos seguem suas próprias políticas de retenção e costumam ser mais confiáveis para exportações grandes.

{% alert tip %}
"Armazenamento em nuvem" significa seu próprio bucket de armazenamento (por exemplo, Amazon S3, Microsoft Azure Blob Storage ou Google Cloud Storage). Você pode conectar seu bucket em **Partner Integrations** > **Technology Partners** para que a Braze possa gravar arquivos de exportação diretamente nele.
{% endalert %}

Para mais detalhes sobre entrega de exportação e solução de problemas, consulte [Solução de problemas de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).

## Endpoints de exportação

A tabela a seguir lista todas as APIs de exportação disponíveis.

| Categoria | Método | Endpoint |
| --- | --- | --- |
| Campaigns | GET | [Análise de dados de Campaign]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) |
| Campaigns | GET | [Detalhes de Campaign]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) |
| Campaigns | GET | [Lista de Campaigns]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) |
| Campaigns | GET | [Análise de dados de envio]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) |
| Canvas | GET | [Análise de dados de séries de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) |
| Canvas | GET | [Resumo de análise de dados de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) |
| Canvas | GET | [Detalhes de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) |
| Canvas | GET | [Lista de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) |
| Eventos personalizados | GET | [Eventos personalizados]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) |
| Eventos personalizados | GET | [Lista de eventos personalizados]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) |
| Eventos personalizados | GET | [Análise de dados de eventos personalizados]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) |
| Atributos personalizados | GET | [Atributos personalizados]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) |
| KPIs | GET | [KPIs de novos usuários diários por data]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) |
| KPIs | GET | [KPIs de usuários ativos diários por data]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) |
| KPIs | GET | [KPIs de MAU nos últimos 30 dias]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) |
| KPIs | GET | [KPIs de desinstalações por data]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) |
| Compras | GET | [Lista de IDs de produtos]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) |
| Compras | GET | [Número de compras]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) |
| Compras | GET | [Dados de receita por período]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) |
| Segments | GET | [Lista de Segments]({{site.baseurl}}/api/endpoints/export/segments/get_segment) |
| Segments | GET | [Análise de dados de Segment or segmento]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) |
| Segments | GET | [Detalhes de Segment or segmento]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) |
| Sessões | GET | [Dados de séries temporais de sessões do app]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) |
| Dados de usuários | POST | [Dados de usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) |
| Dados de usuários | POST | [Dados de usuários por Segment or segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) |
| Dados de usuários | POST | [Dados de usuários por grupo de controle global]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Endpoints de exportação" }

## Artigos relacionados {#related-articles}

Para exportações pontuais a partir do dashboard, consulte estes artigos:

- [Exportar dados de Campaign]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_campaign_results_data)
- [Exportar dados de Canvas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data)
- [Exportar dados de Segment or segmento para CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv)