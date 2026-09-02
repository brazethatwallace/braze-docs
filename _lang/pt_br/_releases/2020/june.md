---
nav_title: Junho
page_order: 7
noindex: true
page_type: update
description: "Este artigo contém notas de versão para junho de 2020."
---
# Junho de 2020 {#june-2020}

## Relatórios de retenção {#retention-reports}

Os relatórios de retenção agora oferecem retenção por intervalo para [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/test_campaigns/retention_reports/) e [Canvas]({{site.baseurl}}/user_guide/analytics/reports/retention_reports/). A retenção por intervalo mede quantos usuários retornam e realizam um evento de retenção selecionado durante intervalos de tempo específicos.

## Atualizações da API de rastreamento do usuário {#user-track-api-updates}

O [endpoint `users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) agora tem uma taxa padrão de 50.000 solicitações de API por minuto para empresas do dashboard criadas após 2 de junho de 2020. As empresas existentes criadas antes dessa data e seus espaços de trabalho ainda poderão fazer solicitações ilimitadas de API para o endpoint `users/track`.

 A Braze está impondo esse padrão em nosso endpoint voltado para o cliente mais utilizado como uma etapa em direção às nossas metas de estabilidade e confiabilidade para nossa API e infraestrutura. O limite imposto é muito liberal e afetará muito poucas empresas do dashboard e suas operações regulares. Caso precise aumentar esse limite, entre em contato com seu CSM ou com nossa equipe de suporte para solicitar um aumento.