---
nav_title: Dashboard de benchmarks do setor
article_title: Dashboard de benchmarks do setor
alias: "/industry_benchmarks_dashboard/"
page_order: 3
description: "Este artigo fornece uma visão geral do dashboard de benchmarks do setor."
hidden: true
noidex: true
---

# Dashboard de benchmarks do setor {#industry-benchmarks-dashboard}

> O dashboard **Industry Benchmarks** compara o desempenho de engajamento do seu espaço de trabalho com benchmarks agregados e conscientes de privacidade de empresas do mesmo setor.

Use o dashboard **Industry Benchmarks** para comparar o desempenho de e-mail, push, Content Cards e SMS com empresas do mesmo setor e identificar canais e regiões onde há oportunidades de otimização.

Para visualizar o dashboard **Industry Benchmarks**, acesse **Analytics** > **Dashboard Builder** e selecione **Industry Benchmarks**. Se o dashboard não tiver dados, selecione **Run Dashboard** para gerar os resultados mais recentes. Use os filtros na parte superior do dashboard para refinar os resultados por vertical do setor ou período.

{% alert note %}
O dashboard **Industry Benchmarks** está atualmente em acesso antecipado. Fale com o seu gerente de sucesso do cliente se tiver interesse em participar do acesso antecipado.
{% endalert %}

## Sobre o dashboard {#about-the-dashboard}

O dashboard é organizado em quatro seções de canal: **Email**, **Push Notification**, **Content Card** e **SMS**:

| Seção | Descrição |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cartões de KPI | Mostram a taxa do seu espaço de trabalho para cada métrica principal, junto com o delta em comparação com a taxa do setor. Uma seta verde para cima indica que seu espaço de trabalho está acima da taxa do setor; uma seta vermelha para baixo indica que está abaixo. |
| Gráfico de tendência mensal | Plota a taxa do seu espaço de trabalho em relação à taxa do setor ao longo do tempo, para que você possa identificar sazonalidade e tendências de longo prazo. |
| Detalhamento regional | Detalha a taxa do seu espaço de trabalho em relação à taxa do setor por região, para que você possa identificar onde o desempenho regional diverge do setor. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Seção" }

Em todos os gráficos, a série de cor mais clara representa o benchmark do setor e a série mais escura (prefixada com **Workspace**) representa o seu próprio desempenho.

## Métricas disponíveis {#available-metrics}

Cada métrica baseada em canal está disponível em dois tipos:

| Tipo de métrica | Descrição | Exemplo |
|----------|---------------------------------------|------------------------------------------------------|
| _Total_ | Conta todos os eventos de engajamento. | Se um usuário clica três vezes, isso é contado como três cliques. |
| _Distinct_ | Conta usuários únicos. | Se um usuário clica três vezes, isso é contado como um clique. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipo de métrica" }

As métricas são agrupadas pelas seguintes combinações de setor, região, subsetor e data:

- Setor + Data
- Setor + Região + Data
- Setor + Subsetor + Região + Data

Selecione uma guia para visualizar as métricas de cada canal.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

{% tabs %}
{% tab E-mail %}

<table aria-label="Métricas de e-mail"><thead><tr><th>Métrica</th><th>Descrição</th><th>Fórmula</th></tr></thead><tbody>
<tr><td class="no-split"><i>Unique Open Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Essa taxa exclui aberturas por máquina.</td><td class="no-split"><i>Unique Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Unique Click Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Unique Click to Open Rate</i></td><td class="no-split">A porcentagem de usuários que clicaram em um e-mail após abri-lo.</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Opens</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Métricas de e-mail" }

![Métricas de benchmarks do setor para e-mail exibidas em gráficos de linha e gráficos de barras.]({% image_buster /assets/img/dashboards/email_industry.png %})

{% endtab %}
{% tab Push %}

As métricas de push estão disponíveis para iOS, Android, web e para todas as plataformas combinadas.

<table aria-label="Métricas de push"><thead><tr><th>Métrica</th><th>Descrição</th><th>Fórmula</th></tr></thead><tbody>
<tr><td class="no-split"><i>Direct Open Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td><td class="no-split"><i>Direct Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Influenced Open Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}</td><td class="no-split"><i>Influenced Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Total Open Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td><td class="no-split">(<i>Direct Opens</i> + <i>Influenced Opens</i>) / <i>Unique Sends</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Métricas de push" }

![Métricas de benchmarks do setor para push exibidas em gráficos de linha e gráficos de barras.]({% image_buster /assets/img/dashboards/push_industry.png %})

{% endtab %}
{% tab SMS %}

<table aria-label="Métricas de SMS"><thead><tr><th>Métrica</th><th>Descrição</th><th>Fórmula</th></tr></thead><tbody>
<tr><td class="no-split"><i>Delivery Rate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td><td class="no-split"><i>Deliveries</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Short Link Click Rate</i></td><td class="no-split">A porcentagem de usuários que clicaram em um link curto após receber um SMS.</td><td class="no-split"><i>Short Link Clicks</i> / <i>Unique Sends</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Métricas de SMS" }

![Métricas de benchmarks do setor para SMS exibidas em gráficos de linha e gráficos de barras.]({% image_buster /assets/img/dashboards/sms_industry.png %})

{% endtab %}
{% tab Content Cards %}

<table aria-label="Métricas de Content Cards"><thead><tr><th>Métrica</th><th>Descrição</th><th>Fórmula</th></tr></thead><tbody>
<tr><td class="no-split"><i>Click Rate</i></td><td class="no-split">A porcentagem de usuários que receberam um Content Card e clicaram em um link.</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Impressions</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Métricas de Content Cards" }

![Métricas de benchmarks do setor para Content Cards exibidas em gráficos de linha e gráficos de barras.]({% image_buster /assets/img/dashboards/content_card_industry.png %})

{% endtab %}
{% endtabs %}

## Metodologia {#methodology}

Os benchmarks da Braze são calculados usando um processo de três etapas projetado para produzir números estáveis e representativos.

### Etapa 1: Amostragem dinâmica {#step-1-dynamic-sampling}

Em vez de analisar todos os pontos de dados, a Braze seleciona uma amostra representativa. O método de amostragem faz uma sobre-amostragem de grupos menores de usuários para garantir representação adequada e ajusta pelo tamanho da empresa, de modo que um pequeno número de empresas muito grandes não distorça os resultados de um setor inteiro.

### Etapa 2: Remoção de outliers {#step-2-outlier-removal}

A Braze identifica e remove outliers estatísticos. Isso reduz significativamente a volatilidade nos dados com impacto mínimo nas taxas médias de desempenho, o que significa que anomalias são removidas sem alterar as tendências subjacentes.

### Etapa 3: Ponderação pós-estratificação {#step-3-post-stratification-weighting}

A amostra é ponderada para refletir a população do mundo real. Os pesos são aplicados a subgrupos para corrigir quaisquer desequilíbrios remanescentes da amostragem, resultando em benchmarks finais que são representativos e imparciais.

## Governança de dados {#data-governance}

- **Ciclo de atualização:** Os dados são atualizados mensalmente no dia 5 de cada mês e estão atualizados até o último mês concluído.
- **Privacidade:** Todos os benchmarks são agregados e desidentificados para proteger as informações dos usuários.