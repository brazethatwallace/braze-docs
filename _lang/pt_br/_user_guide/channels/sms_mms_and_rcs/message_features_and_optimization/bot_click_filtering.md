---
nav_title: "Filtragem de cliques de bots"
article_title: "Filtragem de cliques de bots em SMS e RCS"
description: "Este artigo de referência aborda a filtragem de cliques de bots em SMS e RCS."
alias: /sms_rcs_bot_click_filtering/
page_type: reference
page_order: 5
channel:
  - SMS
  - RCS
---

# Filtragem de cliques de bots em SMS e RCS {#sms-and-rcs-bot-click-filtering}

> A filtragem de cliques de bots em SMS e RCS aprimora a análise de dados e os fluxos de trabalho de Campaigns ao excluir cliques suspeitos de bots. Um "clique de bot" refere-se a cliques automatizados em links encurtados em mensagens SMS e RCS, como aqueles de rastreadores web, pré-visualizações de links do Android e iOS ou softwares de segurança CPaaS. Esse recurso facilita relatórios precisos, segmentação e orquestração para engajar usuários reais. <br><br> Para filtragem de cliques de bots em Campaigns de e-mail, consulte [Filtragem de bots para e-mails]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/bot_filtering).

## Como funciona {#how-it-works}

A Braze possui um sistema proprietário de detecção que usa múltiplas entradas para identificar cliques suspeitos de bots, também conhecidos como interações não humanas (NHI). Cliques de bots podem inflar as taxas de cliques, distorcendo as métricas de engajamento. Ao filtrar esses cliques, a Braze facilita a captura de dados confiáveis para a tomada de decisões.

Nosso sistema analisa user agents associados a rastreadores web, prévias de links no Android e iOS ou softwares de segurança CPaaS. Alguns exemplos de user agents filtrados incluem `GoogleBot`, `GoogleMessages/20`, `python-requests/2.32.3` e `Barracuda Sentinel (EE)`.

## Métricas e fluxos de trabalho afetados {#affected-metrics-and-workflows}

As seguintes métricas e fluxos de trabalho da Braze são impactados por cliques de bots:

- **_Total de cliques_:** As análises de dados de Campaigns e Canvas excluem cliques de bots, refletindo apenas interações humanas.
- **Filtros de segmentação:** Os filtros de Segment que fazem referência a interações de links de SMS excluem cliques de bots para um redirecionamento mais preciso em Campaigns e Canvas.
- **Orquestração:** Os cliques de bots são filtrados de disparos baseados em ação e jornadas de ação do Canvas que fazem referência a interações de links de SMS, permitindo que os disparos reflitam o comportamento humano.
- **Braze Intelligence:**
    - **Otimizar com BrazeAI<sup>TM</sup>:** Exclui cliques de bots ao otimizar a seleção de variantes.
    - **Canal inteligente:** Exclui cliques de bots quando SMS ou RCS é selecionado para uma seleção de canal precisa.
    - **Etapas de experimento:** Exclui cliques de bots para resultados de experimentos confiáveis.
    - **Exportações de dados do Currents:** Inclui os campos `is_suspected_bot_click` e `suspected_bot_click_reason` para ajudar a analisar cliques humanos versus cliques de bots. Esses campos estão disponíveis no [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), no [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) e no [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder).

Os cancelamentos de inscrição provenientes de cliques suspeitos de bots não são afetados. A Braze processa todas as solicitações de cancelamento de inscrição normalmente. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="blocking unsubscribes from suspected bot clicks" %}

## Campos do Currents em eventos de clique de SMS {#currents-fields-in-sms-click-events}

A Braze inclui os seguintes campos do Currents para eventos de clique de SMS:

| Campo | Tipo de dados | Descrição |
| --- | --- | --- |
| `is_suspected_bot_click` | Boolean | Indica se o clique é um clique suspeito de bot. Para cliques em links curtos de SMS e RCS, a Braze avalia a detecção de bots em cada clique e preenche este campo com `true` ou `false`. |
| `suspected_bot_click_reason` | String, Array | Indica o motivo de um clique suspeito de bot (como `user_agent`). É preenchido quando a detecção de bots é executada para cliques em links curtos de SMS e RCS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos do Currents em eventos de clique de SMS" }

## Modelo do Query Builder {#query-builder-template}

Para ajudar a analisar seus dados, você pode usar o modelo pré-criado para dispositivos móveis **SMS click events by bots** no [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates).

## Perguntas frequentes {#frequently-asked-questions}

### Como a filtragem de cliques de bot afeta o desempenho da campanha? {#how-does-bot-click-filtering-impact-campaign-performance}

A filtragem de cliques de bot é executada automaticamente para cliques em links encurtados de SMS e RCS. As taxas de cliques no dashboard excluem cliques suspeitos de bot, de modo que as taxas reportadas refletem interações humanas em vez de prévias automáticas de links ou tráfego de rastreadores.

### A filtragem de cliques de bot impede que bots cliquem em links de cancelamento de inscrição? {#does-bot-click-filtering-prevent-bots-from-clicking-unsubscribe-links}

Não. Todas as solicitações de cancelamento de inscrição são processadas normalmente.

### As prévias de links são incluídas na filtragem de cliques de bot? {#are-link-previews-included-in-bot-click-filtering}

Sim. As prévias de links (como prévias de links do Android e iOS) são sinalizadas como cliques de bot e filtradas.