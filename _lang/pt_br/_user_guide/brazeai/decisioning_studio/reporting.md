---
nav_title: Relatórios e insights
article_title: Relatórios e insights
description: "Saiba como visualizar os relatórios do BrazeAI Decisioning Studio™ na Braze, para que você possa entender como as decisões baseadas em IA afetam suas campanhas."
page_order: 6
---

# Relatórios e insights {#reports-and-insights}

> Saiba como visualizar os relatórios do BrazeAI Decisioning Studio™ na Braze, para que você possa entender como as decisões baseadas em IA afetam suas campanhas. Desde as métricas de desempenho até a integridade dos dados e as alterações no sistema, esses relatórios ajudam você a entender os resultados, solucionar problemas e tomar decisões informadas com confiança.

## Pré-requisitos {#prerequisites}

Antes de visualizar os relatórios do Decisioning Studio na Braze, você precisará:

- Ter um contrato ativo para a Braze e o BrazeAI Decisioning Studio™.
- Fale com seu CSM para ativar o BrazeAI Decisioning Studio™ para você.
- Ter um agente do BrazeAI Decisioning Studio™ ativo.

## Visualizar relatórios {#view}

Para visualizar métricas de um agente do Decisioning Studio na Braze, acesse **AI Decisioning** > **BrazeAI Decisioning Studio™** e selecione um agente.

Aqui, você pode visualizar relatórios como desempenho, insights, diagnósticos e linhas do tempo. Para saber mais, consulte [Relatórios disponíveis](#available-reports).

## Alterar datas do relatório {#change-report-dates}

Após [abrir um relatório](#view), você pode alterar o intervalo de datas selecionando uma nova data inicial e final no menu suspenso do calendário.

![Seletor de intervalo de datas do BrazeAI Decisioning Studio™ aberto com um menu suspenso de calendário. O calendário exibe datas de início e término selecionáveis para personalizar a exibição do relatório.]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

Você também pode definir uma data de início padrão ou escolher datas a serem sempre excluídas. As datas excluídas serão filtradas de todos os relatórios desse agente.

Para definir ou excluir datas, selecione <i class="fa-solid fa-gear" aria-label="Configurações"></i> **Configurações** e, em seguida, altere a data padrão ou exclua as datas conforme necessário.

![Painel de configurações aberto no BrazeAI Decisioning Studio™ mostrando opções para definir uma data de início padrão e excluir datas específicas dos relatórios. O painel exibe duas seções denominadas Data de início padrão e Excluir datas. Em Excluir datas, várias datas são listadas com caixas de seleção ao lado de cada uma.]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## Relatórios disponíveis {#available-reports}

- [Desempenho]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/performance/): Métricas de alto nível do agente que comparam grupos de tratamento a grupos de controle, com as visualizações **Trending** e **Driver Tree**.
- [Insights]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/insights/): Como as opções de recomendação no seu banco de ações são geradas, incluindo preferências do agente e relatórios SHAPs.
- [Diagnóstico]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/diagnostics/): Integridade dos dados de saída e entrada, incluindo volume de recomendações e monitoramento de feeds de dados.
- [Linha do tempo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/timeline/): Um registro visual dos principais eventos (execuções de agentes, alterações de configuração, atualizações de guardrails) juntamente com métricas de desempenho.