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

A Braze possui um sistema proprietário de detecção que usa múltiplas entradas para identificar cliques suspeitos de bots, também conhecidos como interações não humanas (NHI). Cliques de bots podem inflar as taxas de cliques, distorcendo as métricas de engajamento. Ao filtrá-los, a Braze facilita a captura de dados confiáveis para a tomada de decisões.

Nosso sistema analisa user agents associados a rastreadores web, pré-visualizações de links do Android e iOS ou softwares de segurança CPaaS. Alguns exemplos de user agents filtrados incluem `GoogleBot`, `GoogleMessages/20`, `python-requests/2.32.3` e `Barracuda Sentinel (EE)`.

## Métricas e fluxos de trabalho afetados {#affected-metrics-and-workflows}

As seguintes métricas e fluxos de trabalho da Braze são impactados por cliques de bots:

- **_Total de cliques_:** A análise de dados de Campaigns e Canvas excluirá cliques de bots, refletindo apenas interações humanas.
- **Filtros de segmentação:** Filtros de Segment que referenciam interações de links SMS excluirão cliques de bots para um redirecionamento mais preciso em Campaigns e Canvas.
- **Orquestração:** Cliques de bots são filtrados de gatilhos baseados em ações e jornadas de ação do Canvas que referenciam interações de links SMS, permitindo que os gatilhos reflitam o comportamento humano.
- **Braze Intelligence:**
    - **Seleção inteligente:** Exclui cliques de bots ao otimizar a seleção de variantes.
    - **Canal inteligente:** Exclui cliques de bots quando SMS ou RCS é selecionado para uma seleção de canal precisa.
    - **Etapas de experimento:** Exclui cliques de bots para resultados de experimentos confiáveis.
    - **Exportações de dados do Currents:** Inclui os campos `is_suspected_bot_click` e `suspected_bot_click_reason` para ajudar a analisar cliques humanos versus cliques de bots. Esses campos estão disponíveis no [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) e [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder).

Cancelamentos de inscrição provenientes de cliques suspeitos de bots não são afetados. A Braze processa todas as solicitações de cancelamento de inscrição normalmente. Para bloquear esses cancelamentos de inscrição, [envie feedback de produto]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Campos do Currents em eventos de clique SMS {#currents-fields-in-sms-click-events}

A Braze inclui os seguintes campos do Currents para eventos de clique SMS:

| Campo | Tipo de dado | Descrição |
| --- | --- | --- |
| `is_suspected_bot_click` | Booleano | Indica se o clique é um clique suspeito de bot. Retorna `null` para todos os usuários até que a filtragem de cliques de bots seja ativada para sua empresa. Quando ativada, será preenchido com `true` ou `false` para todos os novos cliques a partir daquele momento. |
| `suspected_bot_click_reason` | String, Array | Indica o motivo de um clique suspeito de bot (como `user_agent`). É preenchido mesmo se a filtragem estiver desativada, fornecendo insight sobre possível atividade de bots. Este campo está disponível globalmente e é preenchido com um motivo para todos os usuários, mesmo que a filtragem de cliques de bots ainda não esteja ativada. Isso fornece insight sobre possível atividade de bots antes de você ativar a filtragem de cliques de bots. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos do Currents em eventos de clique SMS" }

## Modelo do Criador de consultas {#query-builder-template}

Para ajudar a analisar seus dados, você pode usar o modelo móvel pré-construído **SMS click events by bots** no [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates).

## Perguntas frequentes {#frequently-asked-questions}

### Como a filtragem de cliques de bots impacta o desempenho de Campaigns? {#how-does-bot-click-filtering-impact-campaign-performance}

A filtragem não afeta Campaigns enviadas anteriormente. Quando ativada, ela reduz as taxas de cliques daquele momento em diante ao excluir cliques de bots.

### A filtragem de cliques de bots impede que bots cliquem em links de cancelamento de inscrição? {#does-bot-click-filtering-prevent-bots-from-clicking-unsubscribe-links}

Não. Todas as solicitações de cancelamento de inscrição são processadas normalmente.

### Pré-visualizações de links estão incluídas na filtragem de cliques de bots? {#are-link-previews-included-in-bot-click-filtering}

Sim. Pré-visualizações de links (como pré-visualizações de links do Android e iOS) são sinalizadas como cliques de bots e filtradas.

### Como ativo a filtragem de cliques de bots? {#how-do-i-enable-bot-click-filtering}

Você deve entrar em contato com a equipe de conta da Braze para ativar a filtragem de cliques de bots durante o acesso antecipado. Quando a filtragem de cliques de bots estiver disponível de forma geral, o recurso será ativado por padrão para todos os usuários de SMS e RCS.

Certifique-se também de que você ativou o rastreamento avançado de cliques para [encurtamento de links]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening). Isso permite que você receba a análise de dados de cliques de bots, pois rastreamos esses dados no nível do usuário individual.

{% alert note %}
Para assistência adicional, [entre em contato com o Suporte]({{site.baseurl}}/braze_support).
{% endalert %}