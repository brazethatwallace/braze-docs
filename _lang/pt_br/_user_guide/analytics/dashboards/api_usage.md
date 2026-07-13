---
nav_title: Uso da API
article_title: Dashboard de uso da API
alias: "/api_usage/"
page_order: 5
description: "Este artigo fornece uma visão geral do dashboard de uso da API."
---

# Dashboard de uso da API {#api-usage-dashboard}

> O dashboard de uso da API permite monitorar o tráfego de entrada da REST API na Braze para entender as tendências de uso das nossas REST APIs e solucionar possíveis problemas.

## Sobre o dashboard de uso da API {#about-the-api-usage-dashboard}

Para visualizar o dashboard de uso da API, acesse **Configurações** > **APIs e identificadores** e selecione **Dashboard**.

O dashboard padrão exibe todas as solicitações de entrada da REST API para o seu espaço de trabalho nas últimas 24 horas. Dependendo do seu caso de uso, você pode ajustar os controles do dashboard para filtrar ou agrupar o tráfego e também configurar o intervalo de tempo do dashboard.

![Dashboard de uso da API com 130 solicitações totais, com uma taxa de sucesso de 70% e uma taxa de falha de 30%.]({% image_buster /assets/img/api_usage_dashboard/api_usage_dashboard.png %})

## Métricas disponíveis {#available-metrics}

O dashboard de uso da API inclui as seguintes estatísticas:

| Métrica | Descrição |
|----------------|-------------|
| Total de solicitações | O número total de solicitações enviadas à Braze para o seu espaço de trabalho atual, considerando os filtros e controles aplicados ao dashboard. |
| Taxa de sucesso | A porcentagem do total de solicitações em que a Braze retornou uma resposta de sucesso `2XX`. |
| Taxa de erro | A porcentagem do total de solicitações em que a Braze retornou uma resposta de erro `4XX` ou `5XX`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas disponíveis" }

## Usando o dashboard {#using-the-dashboard}

![Filtros para aplicar ao dashboard, incluindo: chave de API, endpoint, códigos de resposta, agrupar dados e data.]({% image_buster /assets/img/api_usage_dashboard/filters.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

### Filtros {#filters}

Selecione **Filtros** para aplicar filtros e restringir a visualização do tráfego da REST API para o seu espaço de trabalho, incluindo:

- Chave de API
- Endpoint
- Código de resposta

### Agrupar dados {#group-data}

Você pode agrupar dados em diferentes séries para explorar padrões variados no seu uso, incluindo:

- Códigos de resposta (padrão)
- Endpoint da API
- Chave de API
- Apenas sucesso e falha

### Data {#date}

Ajuste o filtro de data para exibir um intervalo de tempo menor ou maior conforme necessário. As opções incluem:

- Hoje (padrão)
- Personalizado
- Últimas 3 horas
- Últimas 6 horas
- Últimas 12 horas
- Últimas 24 horas
- Ontem
- Últimos 7 dias
- Últimos 14 dias
- Últimos 30 dias
- Mês atual até agora

{% alert note %}
As opções **Últimas 3 horas** e **Últimas 6 horas** exibirão o tráfego por minuto. Períodos maiores exibirão o tráfego a cada cinco minutos, hora ou dia.
{% endalert %}

## Considerações {#considerations}

O dashboard de uso da API inclui todas as solicitações da REST API que a Braze recebeu e para as quais retornou uma resposta `2XX`, `4XX` ou `5XX`. Isso inclui saídas de Transformação de dados e sincronizações de Ingestão de dados na nuvem. O tráfego do SDK e as etapas de Atualização de usuário não estão incluídos neste dashboard.

Os dados exibidos no dashboard podem ter um pequeno atraso para mostrar o tráfego recente. Durante períodos de alto uso, você pode atualizar o dashboard até 4 vezes por minuto. Pode ser necessário aguardar alguns minutos antes de atualizar o dashboard novamente.

### Chaves de API no corpo da solicitação {#api-keys-in-request-body}

Quando as chaves de API são enviadas no corpo da solicitação em vez do cabeçalho, algumas solicitações podem não aparecer no dashboard de uso da API. Isso pode levar a dados incompletos no dashboard e dificultar o monitoramento preciso do uso da API.

Para obter relatórios mais precisos no dashboard de uso da API, [inclua as chaves de API no cabeçalho da solicitação]({{site.baseurl}}/api/basics#bearer-token-authentication) em vez de no corpo da solicitação.

## Artigos relacionados {#related-articles}

- [Alertas de uso da API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts)
- [Limites de taxa]({{site.baseurl}}/api/api_limits)
- [Autenticação por token Bearer]({{site.baseurl}}/api/basics#bearer-token-authentication)