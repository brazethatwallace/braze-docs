---
nav_title: Início
article_title: Dashboard Início (anteriormente Visão geral)
page_order: 1
page_type: reference
description: "Este artigo de referência descreve o dashboard Início e fornece definições para as estatísticas disponíveis nesta página."
tool:
  - Reports

---

# Dashboard Início {#home-dashboard}

> A página **Início** no dashboard fornece métricas essenciais para você acompanhar e entender o desempenho do seu app ou site, além de oferecer uma visão geral de alto nível da sua base de usuários.

A página **Início** tem duas seções principais:
- [Continue de onde parou](#pick-up-where-you-left-off)
- [Visão geral de desempenho](#performance-overview)

![Dashboard Início na Braze.]({% image_buster /assets/img_archive/home_dashboard.png %})

## Continue de onde parou {#pick-up-where-you-left-off}

Você pode continuar de onde parou no dashboard da Braze com acesso direto aos arquivos que editou ou criou recentemente. Esta seção aparece no topo da página **Início** do dashboard da Braze.

Você pode revisitar Campaigns, Canvas e Segments editados ou criados recentemente. Cada cartão é acompanhado de tags que indicam o tipo de conteúdo (Campaign, Canvas, Segment) e o status (ativo, rascunho, arquivado, parado).

{% alert note %}
A seção **Continue de onde parou** aparece depois que você edita ou cria uma Campaign, Canvas ou Segment.
{% endalert %}

![Um rascunho de Canvas, um Segment ativo e um rascunho de Campaign na seção "Continue de onde parou".]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

## Visão geral de desempenho {#performance-overview}

Por padrão, a seção **Visão geral de desempenho** mostra os dados dos últimos 30 dias para todos os apps e sites. Suas métricas são calculadas com base no intervalo de datas selecionado.

![Campos de intervalo de datas e app no dashboard Início.]({% image_buster /assets/img_archive/home_dashboard_select_date.png %}){: style="max-width:60%;"}

Os percentuais são calculados com base no intervalo de datas atual em comparação com o intervalo anterior, com exceção dos *Usuários ativos mensais* (MAU), que usam o último dia do período anterior em vez de um intervalo.

Por exemplo, se você definir o intervalo de datas como **Últimos 7 dias** e seus *Usuários ativos diários* mostrarem um aumento percentual de 1,8%, isso significa que você teve 1,8% mais usuários ativos diários nesta semana em comparação com a semana passada.

![Um bloco de métrica da visão geral de desempenho mostrando o valor da métrica e a variação percentual.]({% image_buster /assets/img_archive/home_dashboard_metric_tile.png %}){: style="max-width:60%;"}

### Mostrar detalhamento {#show-breakdown}

Selecione **Show Breakdown** para cada linha das estatísticas da visão geral de desempenho para visualizar o valor de cada estatística por dia no intervalo de datas especificado.

![Expandir detalhamento das estatísticas do dashboard Início.]({% image_buster /assets/img_archive/home_dashboard_breakdown.png %})

### Desempenho ao longo do tempo {#performance-over-time}

O gráfico **Performance Over Time** mostra o valor de cada estatística no intervalo de datas especificado para os apps selecionados.

![O gráfico Desempenho ao longo do tempo mostrando estatísticas de novos usuários ao longo de 30 dias.]({% image_buster /assets/img/dashboards/performance_over_time.png %})

Você pode visualizar estatísticas para:
- Banners
- Content Cards
- Usuários ativos diários
  - (Opcional) Detalhamento por Segment
- E-mail
- Mensagens no app
- Fórmulas de KPI
  - Selecione **Manage KPI Formulas** para criar uma fórmula ou editar uma fórmula existente.
- LINE
- Usuários ativos mensais (MAU)
- Novos usuários
- Push
  - (Opcional) Detalhamento por Segment
- Sessões
  - (Opcional) Detalhamento por Segment ou versão do app
- Sessões por hora
- Sessões por MAU
- SMS
- Stickiness
- Desinstalações
  - (Opcional) Detalhamento por Segment
- Usuários
- Webhooks
- WhatsApp

## Estatísticas disponíveis {#available-statistics}

A seguir estão as definições das estatísticas disponíveis, como são calculadas e por que são importantes para você.

### Usuários {#users}

*Usuários* é o número total de usuários criados nesse espaço de trabalho. Isso inclui todos os usuários que usaram seu app ou site em qualquer momento, além daqueles que podem não estar associados a um app ou site específico. Esse número é o percentual de quantos dos seus usuários totais são representados como *Usuários ativos mensais* (MAU), o que é útil para avaliar a retenção de usuários ao longo de um período prolongado.

Uma proporção baixa de MAU em relação ao total de usuários pode indicar que você precisa diversificar seus canais de envio de mensagens ou aumentar seus esforços para alcançar usuários inativos. Consulte nossa dica rápida sobre [captura de usuários inativos]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/capturing_lapsing_users/#capture-lapsing-users) para mais informações. De modo geral, a proporção de MAU em relação ao total de usuários tende a diminuir ao longo do tempo devido ao churn, mas as ferramentas da Braze podem ajudar a minimizar esse efeito mantendo os usuários engajados por mais tempo.

### Sessões totais {#lifetime-sessions}

*Sessões totais* é a contagem total de sessões que a Braze registrou desde a integração. Uma sessão é cada vez que um usuário usa o app ou visita seu site. Para uma definição mais precisa de como as sessões são definidas por plataforma, consulte os artigos de rastreamento de sessões para desenvolvedores correspondentes:
[iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [Android e FireOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android) ou [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web).

### Usuários ativos mensais {#monthly-active-users}

*Usuários ativos mensais* (MAU) é o número de usuários que registraram uma sessão no seu app ou site nos últimos 30 dias. O MAU é calculado todas as noites com uma janela móvel de 30 dias. O MAU oferece uma boa compreensão da integridade de um app ou site ao longo de um período prolongado, pois suaviza as inconsistências entre dias com intensidades de uso variáveis.

O percentual ao lado da contagem de MAU mostra a variação do MAU neste período em comparação com o período anterior.

$$\text{Variação no MAU} = \frac{\text{MAU do último dia do intervalo} - \text{MAU do dia anterior à data de início}}{\text{MAU do dia anterior à data de início}}$$

#### Regras de cálculo do MAU {#mau-calculation-rules}

Os cálculos de MAU seguem regras específicas para garantir uma cobrança precisa e consistente:

- **Momento do cálculo**: Calculado uma vez por dia às 12:05 UTC como um snapshot de 30 dias; as contagens nunca mudam retroativamente.
- **Perfis anônimos**: Contam **apenas** quando pelo menos uma sessão é registrada.
- **Perfis identificados**: Contam apenas quando `date_of_last_session` está dentro da janela móvel de 30 dias.
- **Perfis órfãos**: Duplicatas mescladas em outro usuário **não** são contadas.
- **Uploads por CSV e importações via REST API**: Usuários enviados por CSV ou pela REST API contam para o MAU quando você fornece `date_of_last_session` dentro da janela móvel de 30 dias, ou quando eles registram uma sessão posteriormente. Fornecer apenas `date_of_first_session` não afeta o MAU.
- **Exclusões via API**: Excluir um usuário via API não atualiza o MAU imediatamente; a contagem se corrige automaticamente no próximo ciclo mensal.

{% alert note %}
Usuários anônimos também contam para o seu MAU. Em dispositivos móveis, os usuários anônimos dependem do dispositivo. Para usuários web, os usuários anônimos dependem do cache do navegador.

As contagens de MAU na Braze podem diferir de ferramentas como a Amplitude quando cada produto usa uma definição diferente de usuário ativo. Compare a configuração na Amplitude (e suas regras de MAU da Braze acima) antes de investigar uma discrepância como um problema no pipeline de dados.
{% endalert %}

#### Exemplo de cálculo do MAU {#mau-calculation-example}

O exemplo a seguir demonstra como os cálculos de MAU funcionam com diferentes ações de usuários:

| Etapa | Ação | Variação imediata no MAU | Total resultante |
|-------|------|--------------------------|------------------|
| 1 | Criar **Usuário anônimo 1** e registrar uma sessão | +1 | 1 |
| 2 | Identificar **Usuário anônimo 1** (perfil convertido para identificado) | 0 | 1 |
| 3 | Criar **Usuário anônimo 2** e registrar uma sessão | +1 | 2 |
| 4 | Identificar **Usuário anônimo 2** como a **mesma pessoa** que o Usuário 1 (Usuário 2 se torna órfão) | –1 | 1 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Exemplo de cálculo do MAU" }

Os snapshots de MAU são calculados uma vez por dia e nunca mudam retroativamente. Neste exemplo, a contagem de MAU do dia após a etapa 3 permanece permanentemente em 2, mesmo que o Usuário 2 se torne órfão posteriormente. No entanto, a contagem de MAU dos dias seguintes reflete apenas o usuário não órfão. Dentro de qualquer janela de 30 dias, esse fluxo consome 1 MAU, já que apenas um usuário distinto e não órfão permanece.

### Usuários ativos diários {#daily-active-users}

*Usuários ativos diários* (DAU) exibe o número de usuários únicos que registram pelo menos uma sessão no seu app ou site em um determinado dia. O DAU pode ser uma estatística útil para examinar a variabilidade diária do uso do seu app ou site e ajustar suas campanhas de mensagens para serem o mais eficazes possível. Por exemplo, o uso do seu app pode ter um pico considerável nos fins de semana — isso indicaria que você poderia alcançar mais usuários com mensagens no app nesses dias, em vez de dias úteis.

### Novos usuários {#new-users}

*Novos usuários* informa quantos usuários que nunca haviam registrado uma sessão começaram a usar seu app ou site. Esse número é o total de novos usuários no período selecionado. Essa estatística pode ser muito valiosa para acompanhar a eficácia dos seus esforços de publicidade.

{% alert note %}
Quando você integra a Braze pela primeira vez, todos os usuários aparecerão como novos, pois a Braze nunca registrou uma sessão para eles antes.

Diferentemente do MAU, a contagem de *Novos usuários* pode diminuir retroativamente quando a Braze mescla um perfil anônimo em um perfil identificado e torna o perfil anônimo órfão. A Braze remove o perfil órfão dos totais de uso do app, o que pode reduzir a contagem de *Novos usuários* para datas que você já visualizou. Para saber mais sobre o comportamento de vinculação de perfis, consulte [Ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/).
{% endalert %}

{% alert important %}
Usuários associados a mais de um app são contados separadamente para cada app. Isso significa que um único usuário pode contribuir para a contagem de *Novos usuários* várias vezes se iniciar sessões em diferentes apps no seu espaço de trabalho.
{% endalert %}

### Stickiness {#stickiness}

O valor de *Stickiness* é a proporção entre o DAU e o MAU de um determinado período. Essencialmente, o stickiness mede o percentual do seu MAU que retorna diariamente.

Por exemplo, se o intervalo de datas for definido como 30 dias, uma proporção de 50% indica que, em média, um usuário ativo está usando o app ou site por 15 dos 30 dias, ou que cerca de metade dos seus usuários ativos retorna diariamente. O stickiness é uma métrica importante para o sucesso, pois a maioria dos usuários não para de usar um app porque o odeia ativamente, mas sim porque ele não se tornou parte da sua rotina diária. Portanto, você pode usar o stickiness como um indicador de quão bem você está engajando seus usuários.

O percentual ao lado da proporção de stickiness mostra a variação do stickiness neste período em comparação com o período anterior.

$$\text{Variação no stickiness} = \frac{\text{Stickiness do último período} - \text{Stickiness deste período}}{\text{Stickiness deste período}}$$

Os intervalos de tempo para "último período" e "este período" são determinados pelo intervalo de datas que você selecionar.

{% alert important %}
O valor de MAU é calculado todas as noites e não será atualizado até o dia seguinte.
{% endalert %}

### Sessões diárias {#daily-sessions}

*Sessões diárias* é o número de sessões registradas em um determinado dia. Comparar esse valor com a contagem de DAU pode informar quantas vezes seus usuários abrem o app ou visitam seu site nos dias em que registram pelo menos uma sessão.

{% alert note %}
A contagem de *Sessões diárias* para uma determinada data pode mudar quando você visualiza o dashboard Início em dias diferentes. Se um usuário iniciar uma sessão enquanto estiver offline, a sessão pode não chegar à Braze até que ele abra o app novamente. Quando essa sessão é enviada, a Braze a atribui à data em que a sessão começou, o que pode aumentar a contagem daquela data retroativamente.
{% endalert %}

### Sessões diárias por MAU {#daily-sessions-per-mau}

*Sessões diárias por MAU* é a proporção de *Sessões diárias* em relação ao MAU em um determinado dia. Essa estatística informa quantas sessões por dia você pode esperar que sejam registradas por MAU. Quando agregado e calculada a média, isso pode dar uma ideia da frequência relativa com que seus usuários usam seu app ou site. Ou seja, se suas *Sessões diárias por MAU* fossem em média 0,5, você poderia esperar que cada MAU registrasse uma sessão aproximadamente a cada 2 dias.