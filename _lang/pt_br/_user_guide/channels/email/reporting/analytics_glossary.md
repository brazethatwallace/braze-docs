---
nav_title: Glossário de análise de dados de e-mail
article_title: Glossário de análise de dados de e-mail
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Este glossário inclui os termos que você encontrará na seção de análise de dados da sua campanha de e-mail ou Canvas, após o lançamento. Este glossário não inclui métricas do Currents."
channel:
  - email
---

> Este glossário define as métricas na guia **Analytics** para campanhas de e-mail e Canvas. A Braze não oferece uma página hospedada de "visualizar este e-mail no navegador" — consulte [Posso adicionar um link "visualizar este e-mail no navegador" aos meus e-mails?]({{site.baseurl}}/user_guide/channels/email/faq#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails) para uma alternativa. Para outras soluções de problemas que abrangem múltiplas métricas, consulte [Perguntas frequentes sobre e-mail]({{site.baseurl}}/user_guide/channels/email/faq).

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Variante {#variation}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Envio de e-mail {#emailable}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### % de público {#audience}

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Cálculo: (Número de destinatários na variante) / (Destinatários únicos)</span>

{% endapi %}

{% api %}

### Destinatários únicos {#unique-recipients}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} Esse número é recebido da Braze.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Envios {#sends}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  Essa métrica é fornecida pela Braze.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Mensagens enviadas {#messages-sent}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Essa métrica é fornecida pela Braze.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Entregas {#deliveries}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} Para e-mails, *Entregas* é o número total de mensagens (Envios) enviadas com sucesso e recebidas por destinatários elegíveis para e-mail.

<span class="calculation-line">Cálculo: (Envios) - (Bounces) </span>

{% alert note %}
Para o estado de **recebimento** no nível do usuário e a lógica relacionada (como limite de frequência), a Braze geralmente marca um usuário quando o envio é processado e entregue para despacho — não quando o provedor de serviços de e-mail (ESP) confirma a entrega final na caixa de entrada. Isso evita lacunas de tempo entre a confirmação do ESP e as regras no produto. Pode diferir dos relatórios de entrega do ESP ou de terceiros.
{% endalert %}

{% endapi %}

{% api %}

### % de entregas

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">Cálculo: (Envios - Bounces) / (Envios) </span>

{% endapi %}

{% api %}

### Bounces {#bounces}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %}

Para e-mail, *% de bounce* ou *taxa de bounce* é a porcentagem de mensagens que não foram enviadas com sucesso ou foram designadas como "devolvidas" ou "não recebidas" pelos serviços de envio utilizados, ou que não foram recebidas pelos usuários elegíveis para e-mail.

Um bounce de e-mail para clientes que usam SendGrid consiste em hard bounces, spam (`spam_report_drops`) e e-mails enviados para endereços inválidos (`invalid_emails`).

{% alert note %}
No [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), adiamentos temporários do ESP são frequentemente representados como soft bounces. Ferramentas de entregabilidade (por exemplo, relatórios nativos do SendGrid ou modelos do Looker) podem usar adiamentos para a mesma situação. Adiamentos geralmente são temporários, e o e-mail costuma ser entregue após novas tentativas. Após tentativas prolongadas (até aproximadamente 72 horas para soft bounces na análise de dados de campanhas), uma mensagem pode ser tratada como não entregável, dependendo do seu ESP. Os eventos de e-mail do Currents são somente de adição — um soft bounce registrado não é removido posteriormente se a mensagem for entregue.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Bounces</i>:</b> Contagem</li>
        <li><b><i>% de bounce</i> ou <i>taxa de bounce %</i>:</b> (Bounces) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Hard bounce {#hard-bounce}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}

Quando um e-mail sofre hard bounce ou é marcado como spam, a Braze marca o endereço de e-mail como inválido, mas não atualiza o [status de inscrição]({{site.baseurl}}/user_guide/channels/email/subscriptions) do usuário. A Braze interrompe qualquer envio futuro para esse endereço de e-mail. Para remover um endereço de e-mail da sua lista de hard bounce, use o [endpoint Remover e-mails com hard bounce]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces).

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Soft bounce {#soft-bounce}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Se um e-mail receber um soft bounce, geralmente tentaremos novamente dentro de 72 horas, mas o número de tentativas varia de acordo com o destinatário.

Embora os soft bounces não sejam rastreados na análise de dados da sua campanha, você pode monitorá-los no [Registro de atividades de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) ou excluir esses usuários do seu envio com o [filtro de segmento Soft Bounce]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced). No Registro de atividades de mensagem, você também pode ver o motivo dos soft bounces e entender possíveis discrepâncias entre os "envios" e as "entregas" das suas campanhas de e-mail.

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Spam {#spam}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Spam</i>:</b> Contagem</li>
        <li><b><i>% de spam</i> ou <i>taxa de spam %</i>:</b> (Marcados como spam) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Aberturas únicas {#unique-opens}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Para e-mail, isso é rastreado ao longo de um período de sete dias. Isso significa que um único usuário que abrir o mesmo e-mail novamente após sete dias conta como uma nova abertura única. Como resultado, as contagens de aberturas únicas no dashboard podem ser maiores do que uma simples consulta `DISTINCT user_id` nos dados do Currents. Para corresponder às contagens do dashboard a partir do Currents, filtre por eventos em que `is_unique` é `true`.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Aberturas únicas</i>:</b> Contagem</li>
        <li><b><i>% de aberturas únicas</i> ou <i>taxa de abertura única</i>:</b> (Aberturas únicas) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Cliques únicos {#unique-clicks}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Isso é rastreado ao longo de um período de sete dias para e-mail e medido por <a href='/docs/user_guide/messaging/messaging_fundamentals/dispatch_id'>dispatch_id</a> (uma única tentativa de envio). Isso inclui cliques nos links de cancelamento de inscrição fornecidos pela Braze. URLs de cancelamento de inscrição personalizadas rastreadas também contam para *Cliques únicos* quando um usuário seleciona o link. Após sete dias, outro clique único é contabilizado para o mesmo usuário se ele clicar novamente. As métricas de engajamento de e-mail no dashboard, incluindo _Cliques únicos_, são calculadas na Braze e não são reconciliadas a partir de relatórios agregados do ESP. Para corresponder às contagens do dashboard a partir do Currents, filtre por eventos em que `is_unique` é `true`.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Cliques únicos</i>:</b> Contagem</li>
        <li><b><i>% de cliques únicos</i> ou <i>taxa de cliques</i>:</b> (Cliques únicos) / (Entregas)</li>
    </ul>
</span>
{:/}

#### Links inesperados no mapa de calor de e-mail {#unexpected-links-on-the-email-heatmap}

Quando o [mapa de calor de e-mail]({{site.baseurl}}/user_guide/channels/email/reporting) mostrar links que você não espera, inspecione o HTML da mensagem em busca de [blocos de conteúdo]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/dnd_editor_blocks) ou espaçamentos entre palavras que criam URLs rastreadas. Use a **Tabela de links por total de cliques** na visualização do mapa de calor para identificar URLs que não correspondem ao texto visível.

{% endapi %}

{% api %}

### Total de cliques {#total-clicks}

{% apitags %}
Count, Percentage
{% endapitags %}

<i>Total de cliques</i> é o número total de vezes que os usuários clicaram em links no e-mail entregue, incluindo múltiplos cliques do mesmo usuário. Isso inclui cliques nos links de cancelamento de inscrição da Braze e URLs de cancelamento de inscrição personalizadas rastreadas.

Quando o *Total de cliques* é muito maior do que os *Cliques únicos*, ferramentas de segurança ou provedores de caixa de e-mail estão escaneando links sem que os usuários abram a mensagem. Compare os *Cliques únicos* ao avaliar o engajamento internamente.

{% endapi %}

{% api %}

### Cancelamentos de inscrição {#unsubscribers-or-unsub}

{% apitags %}
Count, Percentage
{% endapitags %}

_Cancelamentos de inscrição_ refletem o link padrão de cancelamento de inscrição da Braze. Páginas de cancelamento de inscrição personalizadas não incrementam essa métrica, a menos que você atualize os usuários usando a API. A **Série temporal do grupo de inscrições** ainda reflete as alterações feitas via API.

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Cancelamentos de inscrição</i>:</b> Contagem</li>
        <li><b><i>% de cancelamentos de inscrição</i> ou <i>taxa de cancelamento de inscrição</i>:</b> (Cancelamentos de inscrição) / (Entregas)</li>
    </ul>
</span>
{:/}

#### Por que *Cancelamentos de inscrição* e cliques no link de cancelamento de inscrição podem ser diferentes {#why-unsubscribes-and-unsubscribe-link-clicks-can-differ}

Na página **Analytics** de uma campanha de e-mail ou Canvas, compare a contagem de *Cancelamentos de inscrição* com os cliques na URL de cancelamento de inscrição da Braze no detalhamento por link ao expandir **Total Clicks** ou **Unique Clicks**. Os dois valores geralmente coincidem, mas podem ser diferentes:

- **Mais *Cancelamentos de inscrição* do que cliques na URL de cancelamento de inscrição no corpo:** O [List-unsubscribe]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) é um caminho adicional de cancelamento de inscrição no cabeçalho do e-mail (não o link no corpo da mensagem). Quando um usuário cancela a inscrição dessa forma, isso conta para *Cancelamentos de inscrição*, mas não conta como um clique na URL de cancelamento de inscrição rastreada no corpo.
- **Mais cliques na URL de cancelamento de inscrição no corpo do que *Cancelamentos de inscrição*:** Um usuário pode clicar nesse link mais de uma vez. Se ele cancelar a inscrição, se inscrever novamente e cancelar a inscrição outra vez, a análise de dados de e-mail pode registrar múltiplos cliques (por exemplo, dois) no detalhamento de cliques.

Para saber mais, consulte [Por que estou vendo um número diferente de cancelamentos de inscrição em relação aos cliques no meu link de cancelamento de inscrição?]({{site.baseurl}}/user_guide/channels/email/faq#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link).

{% endapi %}

{% api %}

### Receita {#revenue}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Conversões primárias (A) ou evento de conversão primária {#primary-conversions-a-or-primary-conversion-event}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} Para e-mail, push e webhooks, começamos a rastrear conversões após o envio inicial.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Conversões primárias (A)</i> ou <i>Evento de conversão primária</i>:</b> Contagem</li>
        <li><b><i>% de conversões primárias (A)</i> ou <i>taxa de evento de conversão primária</i>:</b> (Conversões primárias) / (Destinatários únicos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confiança {#confidence}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Aberturas por máquina {#machine-opens}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Essa métrica é rastreada a partir de 11 de novembro de 2021 para SendGrid e 2 de dezembro de 2021 para SparkPost.

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Outras aberturas {#other-opens}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Observe que um usuário também pode abrir um e-mail (de forma que a abertura conte para <i>Outras aberturas</i>) antes que uma contagem de <i>Aberturas por máquina</i> seja registrada. Se um usuário abrir um e-mail uma vez (ou mais) após um evento de abertura por máquina em uma caixa de entrada que não seja do Apple Mail, a quantidade de vezes que o usuário abre o e-mail é calculada em <i>Outras aberturas</i> e apenas uma vez em <i>Aberturas únicas</i>.

<span class="calculation-line">Cálculo: Contagem </span>

{% endapi %}

{% api %}

### Aberturas reais estimadas {#estimated-real-opens}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} A Braze recalcula essa estimativa à medida que novos dados de abertura e clique chegam. O valor normalmente se estabiliza alguns dias após o envio, mas continua sendo atualizado quando novos eventos qualificados ocorrem.

{% endapi %}

{% api %}

### Taxa de clique por abertura {#click-to-open-rate}

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Cálculo: (Cliques únicos) / (Aberturas únicas) (para e-mail)</span>

#### Pontuações de probabilidade de abertura de mensagem (segmentação) {#message-open-likelihood-scores-segmentation}

O filtro de segmento [`Message Open Likelihood`]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#message-open-likelihood) classifica a probabilidade de um usuário abrir e-mails em uma escala de 0 a 100%. Usuários sem histórico suficiente de envio ou abertura para o canal aparecem em branco. Para e-mail, as aberturas por máquina são excluídas do cálculo, que usa o histórico recente de mensagens nesse canal (consulte [Filtro de probabilidade de abertura de mensagem para canais individuais]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel#individual-channels)).

{% endapi %}

## Solução de problemas e perguntas frequentes sobre relatórios de e-mail {#email-reporting-troubleshooting-and-faqs}

### Links de cancelamento de inscrição e cliques únicos {#unsubscribe-links-and-unique-clicks}

Quando um destinatário clica em um link de cancelamento de inscrição, a Braze contabiliza como um clique porque a ação usa uma URL. Isso se aplica tanto aos links de cancelamento de inscrição fornecidos pela Braze quanto aos links de cancelamento de inscrição personalizados no corpo da sua mensagem. Esses cliques contribuem para *Cliques únicos* e *Total de cliques* junto com outros cliques em links. Para definições de métricas, consulte [Cliques únicos](#unique-clicks) acima e [Por que estou vendo um número diferente de cancelamentos de inscrição em relação aos cliques no meu link de cancelamento de inscrição?]({{site.baseurl}}/user_guide/channels/email/faq#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link).

### Visualizar no navegador {#view-in-browser}

A Braze não inclui um recurso nativo de "Visualizar este e-mail no navegador". Hospede o conteúdo do e-mail em uma landing page externa (como o seu site) e adicione um link a partir da mensagem usando a ferramenta **Link** do editor de e-mail. Para saber mais, consulte [Posso adicionar um link "visualizar este e-mail no navegador" aos meus e-mails?]({{site.baseurl}}/user_guide/channels/email/faq#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails).

### Atualizações na página de cancelamento de inscrição personalizada {#custom-unsubscribe-page-updates}

Alterações na sua [página de cancelamento de inscrição personalizada]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) aparecem em poucos minutos. Envios ativos usam um cache de curta duração da página que é atualizado quando você salva as alterações.

### Bounces por cota excedida e caixa de e-mail cheia {#over-quota-and-full-mailbox-bounces}

Um bounce por cota excedida ou caixa de e-mail cheia significa que a caixa de entrada do destinatário não pode aceitar novos e-mails. Você pode ver esses endereços entre novos cadastros com endereços inválidos ou arriscados, ou entre perfis inativos há muito tempo cujas caixas de entrada ficaram cheias enquanto estavam inativos.

Revise as taxas de bounce por segmento e origem, remova ou desative endereços que sofrem hard bounce repetidamente e use opt-in confirmado ou duplo para novos assinantes. Para práticas de higiene de lista, consulte [Armadilhas de entregabilidade e spam traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps) e [Relatórios de e-mail]({{site.baseurl}}/user_guide/channels/email/reporting#troubleshooting).

### 550 5.7.1 e-mail não solicitado {#550-571-unsolicited-mail}

Uma resposta `550 5.7.1` como "Nosso sistema detectou que esta mensagem provavelmente é e-mail não solicitado" geralmente vem de provedores de caixa de e-mail rigorosos (por exemplo, Gmail) quando os sinais de reputação ou engajamento parecem ruins. Fatores comuns incluem reclamações de spam, baixo engajamento, listas compradas ou alugadas e picos repentinos de volume.

Concentre-se no crescimento de lista baseado em consentimento, desative assinantes inativos e monitore as taxas de reclamação e bounce. Para saber mais, consulte [Armadilhas de entregabilidade e spam traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps).

### Boas taxas de entregabilidade de e-mail {#good-email-deliverability-rates}

**Entrega** é quando o servidor receptor aceita sua mensagem; você pode medi-la com métricas como *Entregas* e taxa de bounce. **Entregabilidade** (posicionamento na caixa de entrada) depende da filtragem do provedor e não é exibida como uma única métrica na Braze.

Como orientação geral, busque uma taxa de entrega próxima de 99% com hard bounces abaixo de aproximadamente 1%, e acompanhe aberturas e cliques para tendências de engajamento. As metas exatas variam por setor e padrão de envio. Para práticas que apoiam a reputação, consulte [Melhorar a entregabilidade de e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability) e [Armadilhas de entregabilidade e spam traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps).

### "Campaign is already in delay window, so not enqueueing another" {#campaign-is-already-in-delay-window-so-not-enqueueing-another}

No registro de atividades de mensagem ou nos logs de diagnóstico de [Campaigns baseadas em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery), esse resultado de processamento significa que a Braze bloqueou um envio duplicado enquanto um gatilho anterior para o mesmo usuário ainda está dentro do período de entrega da Campaign. Um bloqueio de debounce impede múltiplos enfileiramentos para a mesma rajada de gatilhos.

Você pode ver esse resultado mesmo quando a Campaign mostra **Enviar imediatamente** se qualquer uma das seguintes condições se aplicar:

- A Campaign usa um [evento de exceção]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) ou uma postergação no horário de envio que afeta o tempo.
- Os usuários têm um período de [reelegibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility), então não podem receber a mensagem novamente até que esse período passe.
- Outra Campaign ou etapa de mensagem do Canvas com prioridade mais alta consumiu o slot de envio quando os gatilhos se sobrepõem.

Se um usuário deveria ter recebido a mensagem, mas não recebeu, verifique os resultados anteriores para o mesmo gatilho (por exemplo, bounce de e-mail ou canal não ativado). Outra mensagem no mesmo fluxo de trabalho pode ter impedido esse envio.