---
nav_title: Exportar dados da campanha
article_title: Exportar dados da campanha
page_order: 2
page_type: reference
description: "Este artigo de referência aborda como exportar dados de resultados de campanhas únicas, multicanais ou multivariantes. O artigo também lista como exportar dados de usuários dos destinatários."
tool:
  - Campaigns
  - Reports

---

# Exportar dados da campanha {#export-campaign-data}

> Na página **Campaigns** do dashboard, selecione a campanha que deseja visualizar e role para baixo até os gráficos de desempenho histórico, que podem ser exportados.<br><br>Esta página aborda como exportar dados de resultados de campanhas únicas, multicanais e multivariantes, e como exportar dados de usuários dos destinatários.

## Campanhas multicanais {#multichannel-campaigns}

Para campanhas multicanais, os dados que podem ser exportados dependem dos canais de envio de mensagens que você usou. Aqui está uma lista de todos os dados que podem ser exportados de uma campanha que usou push para iOS, push para Android, e-mail e mensagens no app:

- Mensagens enviadas por data
    - Total de mensagens enviadas
    - Mensagens enviadas nos canais da campanha (pode incluir push, e-mail e mensagem no app)
- Engajamento com mensagens de e-mail por data
    - Número de e-mails entregues
    - Número de e-mails enviados
    - Número de e-mails abertos
    - Número de cliques em e-mails
    - Número de bounces de e-mail
    - Número de e-mails relatados como spam
- Engajamento com mensagens no app por data
    - Número de mensagens no app enviadas
    - Impressões de mensagem no app
    - Número de cliques em mensagens no app
- Engajamento de push do iOS por data
    - Número de notificações por push do iOS enviadas
    - Total de aberturas
    - Aberturas diretas
    - Bounces
- Engajamento de push do Android por data
    - Número de notificações por push do Android enviadas
    - Total de aberturas
    - Aberturas diretas
    - Bounces

## Campanhas multivariantes {#multivariate-campaigns}

Para campanhas multivariantes, que usam apenas um canal de envio de mensagens, é possível exportar dados que mostrem o desempenho de cada variante na análise de dados do canal de envio de mensagens específico ao longo do tempo. Você pode visualizar esses dados agrupados por estatística ou por variante de mensagem.

Os resultados da campanha de push contêm gráficos para as seguintes análises de dados:

- Mensagens enviadas por data para cada variante
- Conversões por data para cada variante
- Destinatários únicos por data para cada variante
- Aberturas por data para cada variante
- Aberturas diretas por data para cada variante
- Bounces por data para cada variante

Os resultados da campanha de e-mail contêm gráficos para as seguintes análises de dados:

- Número entregue por data para cada variante
- Número enviado por data para cada variante
- Aberturas por data para cada variante
- Cliques por data para cada variante
- Bounces por data para cada variante
- Relatórios de spam por data para cada variante

Os resultados da campanha de mensagens no app contêm gráficos para as seguintes análises de dados:

- Enviado por data para cada variante
- Impressões por data para cada variante
- Cliques por data para cada variante

## Destinatários da campanha {#campaign-recipients}

É possível exportar dados de usuários para todos os destinatários de uma campanha como um arquivo CSV. Para fazer isso, selecione o botão **User Data** na seção **Campaign Details**.

{% alert note %}
Não consegue ver o botão **User Data**? Para exportar dados de usuários, é necessário ter as [permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#limited-and-team-role-permissions) **Export User Data** para esse espaço de trabalho.
{% endalert %}

![Menu suspenso de dados de usuários na página Campaign Details]({% image_buster /assets/img/campaign_export_example.png %})

A saída CSV contém dados de perfil de usuário para cada destinatário da campanha. A Braze gerará o relatório em segundo plano e o enviará por e-mail para o usuário que estiver conectado no momento.

Se você tiver vinculado suas [credenciais do Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) à Braze, o CSV também será enviado para o seu bucket S3. Caso contrário, o link enviado por e-mail expirará em algumas horas.

O arquivo exportado inclui os mesmos campos de dados de usuários que são incluídos quando você [exporta dados de usuários para um segmento]({{site.baseurl}}/user_guide/analytics/dashboards/home#exporting-app-usage-data). Além desses campos de dados, se você escolher "Exportar todos os dados do destinatário", o arquivo exportado também conterá os seguintes dados de cada usuário:

- Nome da variação da campanha recebida
- ID da API da variação da campanha recebida
- Se o usuário está no grupo de controle

{% alert tip %}
Para obter ajuda com exportações CSV e API, consulte [Solução de problemas de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}