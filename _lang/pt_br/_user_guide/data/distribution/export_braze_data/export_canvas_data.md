---
nav_title: Exportar dados do Canvas
article_title: Exportar dados do Canvas
page_order: 3
page_type: reference
description: "Este artigo de referência aborda como exportar a análise de dados do Canvas."
tool:
  - Canvas
  - Reports

---

# Exportar dados do Canvas {#export-canvas-data}

> Os dados de usuários podem ser exportados para um arquivo CSV. Esta página aborda como exportar dados de todo o Canvas ou de um componente específico do Canvas.

## Exportação de dados para um Canvas {#exporting-data-for-a-canvas}

Para exportar dados para um Canvas, faça o seguinte:

1. Acesse **Envio de mensagens** > **Canvas** e selecione seu Canvas.
2. Selecione o menu suspenso **Dados de usuários** na seção **Informações do Canvas**.
3. Selecione uma das seguintes opções de exportação:
  - **Exportar dados de usuários em CSV** ou
  - **Exportar endereço de e-mail em CSV**.

Também é possível exportar os dados de usuários de todos os participantes de um Canvas como um arquivo CSV.

## Exportar usuários que entraram ou reentraram em um Canvas {#export-users-who-entered-or-re-entered-a-canvas}

Quando a [reelegibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) está ativada, os usuários podem entrar no mesmo Canvas mais de uma vez. A opção **Exportar dados de usuários em CSV** na página de informações do Canvas exporta os usuários que entraram no Canvas, mas não inclui quantas vezes cada usuário entrou nem o registro de data e hora de cada entrada.

Para analisar quando os usuários entraram ou reentraram em um Canvas, use uma das seguintes opções:

- **Entrada mais recente por usuário:** Exporte um segmento com o campo [`canvases_received`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) usando o endpoint [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment). Para cada Canvas, a exportação inclui os registros de data e hora `last_entered` e `last_exited` para aquele usuário. O campo `canvases_received` contém dados dos últimos 90 dias.
- **Todas as entradas, incluindo reentradas:** Use os [eventos de entrada no Canvas]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-entry-events) no Braze Currents ou no Snowflake Data Sharing. Cada evento `users.canvas.Entry` representa uma entrada no Canvas e inclui um registro de data e hora `time`. Conte os eventos por usuário para determinar quantas vezes ele entrou.
- **Criar uma lista de usuários no dashboard:** Crie um segmento com o filtro **Entered Canvas Variation** e exporte o segmento para CSV. Consulte [Solução de problemas do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#user-didnt-enter-the-canvas).

{% alert note %}
Se você não tem o Currents integrado e precisa de todos os registros de data e hora de entradas históricas, entre em contato com seu gerente de sucesso do cliente da Braze.
{% endalert %}

Para uma etapa específica do Canvas no fluxo de trabalho original, use **Exportar dados de usuários em CSV** na página de informações da etapa.

## Exportação de dados para um componente (somente no fluxo de trabalho original) {#exporting-data-for-a-component-original-workflow-only}

Os resultados do Canvas podem ser exportados individualmente por componente para o fluxo de trabalho original do Canvas. Para fazer isso, selecione o componente específico e, em seguida, selecione o menu suspenso **Dados de usuários** na página **Informações da etapa do Canvas**.

![Menu suspenso de dados de usuários na página Informações do Canvas.]({% image_buster /assets/img/canvas_csv_export.png %})

{% alert tip %}
Para obter ajuda com exportações CSV e API, visite nosso artigo sobre [solução de problemas de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}