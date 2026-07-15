---
nav_title: Glossário de métricas
article_title: Glossário de métricas
layout: report_metrics
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Este glossário define os termos que você encontrará nos seus relatórios na sua conta da Braze."
tool: Reports
---

<style>
  .calculation-line {
    color: #5B6B75;
    font-size: 14px;
  }
</style>

{% api %}

## AMP Clicks {#amp-clicks}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

## AMP Opens {#amp-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

## Público {#audience}

{% apitags %}
All
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Cálculo: (Número de destinatários na variante) / (Destinatários únicos)</span>

{% endapi %}

{% api %}

## Bounces {#bounces}

{% apitags %}
Email, Web Push, iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} Isso pode ocorrer porque não há um token por push válido, o usuário cancelou a inscrição após o lançamento da campanha, ou o endereço de e-mail é impreciso ou foi desativado.

| Canal | Informações adicionais |
|-------|-----------------------|
| E-mail | Um bounce de e-mail para clientes que usam SendGrid consiste em hard bounces, spam (`spam_report_drops`) e e-mails enviados para endereços inválidos (`invalid_emails`).<br><br>Para e-mail, *Bounce %* ou *Taxa de bounce* é a porcentagem de mensagens que não foram enviadas com sucesso ou designadas como "devolvidas" ou "não recebidas" dos serviços de envio usados, ou não recebidas pelos usuários com e-mail válido pretendidos. |
| Push | Esses usuários foram automaticamente cancelados de todas as futuras notificações por push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bounces" }

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Bounces</i>: Contagem</li>
        <li><i>Bounce %</i> ou <i>Taxa de bounce %</i>: (Bounces) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Body Click {#body-click}

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Click' %}

<span class="calculation-line">Cálculo: (Body Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

## Body Clicks {#body-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}

<span class="calculation-line">Cálculo: (Body Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

## Button 1 Clicks {#button-1-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} O relatório de _Button 1 Clicks_ só funciona quando você especifica o **Identifier for Reporting** como "0" na mensagem no app.

<span class="calculation-line">Cálculo: (Button 1 Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

## Button 2 Clicks {#button-2-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} O relatório de _Button 2 Clicks_ só funciona quando você especifica o **Identifier for Reporting** como "1" na mensagem no app.

<span class="calculation-line">Cálculo: (Button 2 Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

## Campaign analytics {#campaign-analytics}

{% apitags %}
Feature Flags
{% endapitags %}

O desempenho da mensagem em vários canais. As métricas exibidas dependem do canal de envio de mensagens selecionado e se o [experimento de Feature Flag]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments#campaign-analytics) é um teste multivariante.

{% endapi %}

{% api %}

## Choices Submitted {#choices-submitted}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

## Click-to-Open Rate {#click-to-open-rate}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Cálculo: (Unique Clicks) / (Unique Opens) (para e-mail)</span>

{% endapi %}

{% api %}

## RCS Confirmed Deliveries ou SMS Confirmed Deliveries {#rcs-confirmed-deliveries-or-sms-confirmed-deliveries}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} Como cliente da Braze, as entregas são cobradas da sua cota de SMS.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Confirmed Deliveries</i>: Contagem</li>
        <li><i>Confirmed Delivery Rate</i>: (Confirmed Deliveries) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Confiança {#confidence}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

## Botão da página de confirmação {#confirmation-page-button}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

## Dispensas da página de confirmação {#confirmation-page-dismissals}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

## Conversões (B, C, D) {#conversions-b-c-d}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} Esse evento definido é determinado por você ao criar a campanha.

| Canal | Informações adicionais |
|-------|-----------------------|
| E-mail, push, webhooks | As conversões são rastreadas após o envio inicial. |
| Content Cards | As conversões são contadas quando o usuário visualiza um Content Card pela primeira vez. |
| Mensagens no app | Uma conversão é contada se o usuário recebeu e visualizou a campanha de mensagem no app e, em seguida, realizou o evento de conversão específico dentro da janela de conversão definida, independentemente de ter clicado na mensagem ou não.<br><br>As conversões são atribuídas à mensagem recebida mais recentemente. Se a reelegibilidade estiver ativada, a conversão será atribuída à mensagem no app mais recente recebida, desde que ocorra dentro da janela de conversão definida. No entanto, se a mensagem no app já tiver uma conversão atribuída, a nova conversão não poderá ser registrada para essa mensagem específica. Isso significa que cada entrega de mensagem no app está associada a apenas uma conversão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conversions (B, C, D)" }

{% endapi %}

{% api %}

## Total Conversions {#total-conversions}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

Quando um usuário visualiza uma campanha de mensagem no app apenas uma vez, apenas uma conversão é contada, mesmo que ele realize o evento de conversão várias vezes depois. No entanto, se a reelegibilidade estiver ativada e o usuário visualizar a campanha de mensagem no app várias vezes, o *Total Conversions* pode aumentar uma vez para cada vez que o usuário registrar uma impressão para uma nova instância da campanha de mensagem no app.

Por exemplo, se um usuário acionar uma mensagem no app duas vezes e converter após cada impressão de mensagem no app (resultando em duas conversões), o *Total Conversions* aumentará em dois. No entanto, se houver apenas uma impressão de mensagem no app seguida de dois eventos de conversão, apenas uma conversão será registrada, e o *Total Conversions* aumentará em um.

{% endapi %}

{% api %}

## Close Message {#close-message}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Close Message' %}

{% endapi %}

{% api %}

## Taxa de conversão {#conversion-rate}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

| Canal | Informações adicionais |
|-------|-----------------------|
| Mensagens no app | A métrica de <i>Unique Impressions</i> diárias totais é usada para calcular a <i>Conversion Rate</i> para mensagens no app.<br><br><i>Unique Impressions</i> para mensagens no app só podem ser contadas uma vez por dia do calendário no fuso horário do seu espaço de trabalho. O número de vezes que um usuário conclui uma ação desejada (uma "conversão") pode aumentar dentro desse mesmo dia do calendário. Embora as conversões possam acontecer mais de uma vez por dia, as <i>Unique Impressions</i> não podem. Portanto, se um usuário concluir uma conversão várias vezes em um dia, a <i>Conversion Rate</i> pode aumentar proporcionalmente, mas as <i>Unique Impressions</i> são contadas apenas uma vez para aquele dia do calendário. Para mais detalhes, consulte <a href="/docs/user_guide/channels/in_app_messages/reporting">Relatórios de mensagens no app</a>. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conversion Rate" }

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>In-App Messages</b>: (Primary Conversions) / (Unique Impressions)</li>
        <li><b>Outros canais</b>: (Primary Conversions) / (Unique Recipients)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Janela de conversão {#conversion-window}

{% apitags %}
All
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

## Entregas {#deliveries}

{% apitags %}
Email, Web Push, iOS Push, Android Push, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %}

| Canal | Informações adicionais |
|-------|-----------------------|
| E-mail | Refere-se ao número total de mensagens (envios) enviadas com sucesso e recebidas por destinatários com e-mail válido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Deliveries" }

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Deliveries</i>: Contagem</li>
        <li><i>Deliveries %</i>: (Sends - Bounces) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## RCS Delivery Failures ou SMS Delivery Failures {#rcs-delivery-failures-or-sms-delivery-failures}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}

Entre em contato com o <a href="/docs/braze_support">suporte da Braze</a> para obter ajuda na compreensão dos motivos das falhas de entrega.

<span class="calculation-line">Cálculo: (Sends) - (Sends to Carrier)</span>

{% endapi %}

{% api %}

## Delivery Failures {#delivery-failures}

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

Entre em contato com o <a href="/docs/braze_support">suporte da Braze</a> para obter ajuda na compreensão dos motivos das falhas de entrega.

<span class="calculation-line">Cálculo: (Sends) - (Sends to Carrier)</span>

{% endapi %}

{% api %}

## Taxa de falha na entrega {#failed-delivery-rate}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

Entre em contato com o <a href="/docs/braze_support">suporte da Braze</a> para obter ajuda na compreensão dos motivos das falhas de entrega.

<span class="calculation-line">Cálculo: (Delivery Failures) / (Sends)</span>

{% endapi %}

{% api %}

## Aberturas Diretas {#direct-opens}

{% apitags %}
iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}

<span class="calculation-line">Cálculo: (Direct Opens) / (Deliveries)</span>

{% endapi %}

{% api %}

## Emailable {#emailable}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

## Erros {#errors}

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Errors' %} Os erros são incluídos na contagem de <i>Sends</i>, mas não são incluídos na contagem de <i>Unique Recipients</i>.

{% endapi %}

{% api %}

## Estimated Real Opens {#estimated-real-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

## Falhas {#failures}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failures' %} As falhas são incluídas na contagem de <i>Sends</i>, mas não na contagem de <i>Deliveries</i>.</td>

<span class="calculation-line">Cálculo (<i>Failure Rate</i>): (Failures) / (Sends)</span>

{% endapi %}

{% api %}

## Desempenho do experimento de Feature Flag {#feature-flag-experiment-performance}

{% apitags %}
Feature Flags
{% endapitags %}

Métricas de desempenho para a mensagem em um experimento de Feature Flag. As métricas específicas exibidas variam dependendo do canal de envio de mensagens e se o experimento foi ou não um teste multivariante.

{% endapi %}

{% api %}

## Hard Bounce {#hard-bounce}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}

Quando isso ocorre, a Braze marca o endereço de e-mail como inválido, mas não atualiza o [status de inscrição]({{site.baseurl}}/user_guide/channels/email/subscriptions) do usuário. Se um e-mail receber um hard bounce, a Braze interrompe quaisquer solicitações futuras para esse endereço de e-mail.

{% endapi %}

{% api %}

## Help {#help}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} A resposta de um usuário é medida sempre que ele envia uma mensagem de entrada dentro de quatro horas após receber sua mensagem.

{% endapi %}

{% api %}

## Aberturas por Influência {#influenced-opens}

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">Cálculo: (Influenced Opens) / (Deliveries)</span>

{% endapi %}

{% api %}

## Lifetime Revenue {#lifetime-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

## Lifetime Value Per User {#lifetime-value-per-user}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

## Receita média diária {#average-daily-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

## Compras diárias {#daily-purchases}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

## Receita diária por usuário {#daily-revenue-per-user}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

## Machine Opens {#machine-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Essa métrica é rastreada a partir de 11 de novembro de 2021 para SendGrid e 2 de dezembro de 2021 para SparkPost. Para Amazon SES, a análise de dados aparecerá como _Opens_. No entanto, a filtragem de bots para cliques será suportada.

{% endapi %}

{% api %}

## Opens {#opens}

{% apitags %}
Web Push, iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

## Descadastramento {#opt-out}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} A resposta de um usuário é medida sempre que ele envia uma mensagem de entrada dentro de quatro horas após receber sua mensagem.

{% endapi %}

{% api %}

## Other Opens {#other-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Observe que um usuário também pode abrir um e-mail (de modo que a abertura conta para Other Opens) antes que uma contagem de Machine Opens seja registrada. Se um usuário abrir um e-mail uma vez (ou mais) após um evento de Machine Opens de uma caixa de entrada que não seja Apple Mail, a quantidade de vezes que o usuário abre o e-mail é calculada para Other Opens e apenas uma vez para Unique Opens.

{% endapi %}

{% api %}

## Tentativa pendente {#pending-retry}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

## Primary Conversions (A) ou Primary Conversion Event {#primary-conversions-a-or-primary-conversion-event}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}

| Canal | Informações adicionais |
|-------|-----------------------|
| E-mail, push, webhooks | Após o envio inicial. |
| Content Cards, mensagens no app | Quando o usuário visualiza o Content Card ou a mensagem pela primeira vez. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Primary Conversions (A) or Primary Conversion Event" }

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Primary Conversions (A) ou Primary Conversion Event</i>: Contagem</li>
        <li><i>Primary Conversions (A) %</i> ou <i>Primary Conversion Event Rate</i>: (Primary Conversions) / (Unique Recipients)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Reads {#reads}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Reads' %}

{% endapi %}

{% api %}

## Read Rate {#read-rate}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Read Rate' %}

<span class="calculation-line">Cálculo: (Reads com confirmação de leitura) / (Sends)</span>

{% endapi %}

{% api %}

## Recebidas {#received}

{% apitags %}
Email, Content Cards, In-App Message, Web Push, iOS Push, Android Push, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %}

| Canal | Informações adicionais |
|-------|-------|
| Content Cards | Recebido quando os usuários visualizam o cartão no app. |
| Push | Recebido quando as mensagens são enviadas do servidor da Braze para o provedor de push. |
| E-mail | Recebido quando as mensagens são enviadas do servidor da Braze para o provedor de serviço de e-mail. |
| SMS/MMS | "Entregue" após o provedor de SMS receber a confirmação da operadora upstream e do dispositivo de destino. |
| Mensagem no app | Recebido no momento da exibição com base na ação-gatilho definida. |
| WhatsApp | Recebido no momento da exibição com base na ação-gatilho definida. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Received" }

{% endapi %}

{% api %}

## RCS Rejections ou SMS Rejections {#rcs-rejections-or-sms-rejections}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Rejections' %} Como cliente da Braze, as rejeições são cobradas da sua cota de SMS.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Rejections</i>: Contagem</li>
        <li><i>Rejection Rate</i>: (Rejections) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Receita {#revenue}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

## Sent {#sent}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sent' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

## Sends {#sends}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} Essa métrica é fornecida pela Braze. Observe que, ao lançar uma campanha agendada, essa métrica incluirá todas as mensagens enviadas, independentemente de já terem sido enviadas ou não devido ao limite de frequência.

{% alert tip %}
Para Content Cards, essa métrica é calculada de forma diferente dependendo do que você selecionou para [Criação de cartão]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation):

- **No lançamento ou entrada na etapa:** O número de cartões criados e disponíveis para serem vistos. Isso não conta se os usuários visualizaram o cartão.
- **Na primeira impressão:** O número de cartões exibidos aos usuários.
{% endalert %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

## Messages Sent {#messages-sent}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Essa métrica é fornecida pela Braze. Observe que, ao lançar uma campanha agendada, essa métrica incluirá todas as mensagens enviadas, independentemente de já terem sido enviadas ou não devido ao limite de frequência.

{% alert tip %}
Para Content Cards, essa métrica é calculada de forma diferente dependendo do que você selecionou para [Criação de cartão]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation):

- **No lançamento ou entrada na etapa:** O número de cartões criados e disponíveis para serem vistos. Isso não conta se os usuários visualizaram o cartão.
- **Na primeira impressão:** O número de cartões exibidos aos usuários.
{% endalert %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

## Sends to Carrier {#sends-to-carrier}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Sends to Carrier</i>: Contagem</li>
        <li><i>Sends to Carrier Rate</i>: (Sends to Carrier) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Soft Bounce {#soft-bounce}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Se um e-mail receber um soft bounce, geralmente tentaremos novamente dentro de 72 horas, mas o número de tentativas varia de destinatário para destinatário.

Observe que _Soft Bounces_ diferem de _Deferrals_. Se nenhum e-mail for entregue com sucesso durante esse período de nova tentativa, a Braze envia um evento de soft bounce por tentativa de envio de campanha. Antes de 25 de fevereiro de 2025, essas novas tentativas eram contadas como múltiplos soft bounces para um envio de campanha.

Embora os soft bounces não sejam rastreados na análise de dados da sua campanha, você pode monitorar os soft bounces no [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log). Você também pode excluir esses usuários do seu envio ou verificar a quantidade de soft bounces dos últimos 30 dias com o [filtro de segmento Soft Bounced]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced). No Registro de atividades de envio de mensagem, você também pode ver o motivo dos soft bounces e entender possíveis discrepâncias entre os "envios" e as "entregas" das suas campanhas de e-mail.

{% endapi %}

{% api %}

## Spam {#spam}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
As reclamações de spam são tratadas diretamente pelos provedores de serviço de e-mail e depois retransmitidas para a Braze por meio de um loop de feedback. A maioria dos loops de feedback relata apenas uma parte das reclamações reais, então a métrica _Spam_ frequentemente representa uma fração do total real. Apenas os provedores de serviço de e-mail podem ver o volume real de reclamações de spam, o que significa que _Spam_ deve ser visto como uma métrica indicativa, não exaustiva.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Spam</i>: Contagem</li>
        <li><i>Spam %</i> ou <i>Spam Rate %</i>: (Marked as Spam) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Survey Page Dismissals {#survey-page-dismissals}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

## Survey Submissions {#survey-submissions}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

## Total Clicks {#total-clicks}

{% apitags %}
Email, Content Cards, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}

| Canal | Informações adicionais |
|-------|-------|
| LINE | Rastreado após um limite mínimo de 20 mensagens por dia ser atingido. E-mails AMP incluem cliques registrados nas versões HTML e texto simples. Esse número pode ser inflado artificialmente por ferramentas anti-spam. |
| Banners | O número total (e porcentagem) de usuários que clicaram na mensagem entregue, independentemente de o mesmo usuário clicar várias vezes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Total Clicks" }

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>E-mail:</b> (Total Clicks) / (Deliveries)</li>
        <li><b>Content Cards:</b> (Total Clicks) / (Total Impressions)</li>
        <li><b>SMS:</b> (Click Opens) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Total Dismissals {#total-dismissals}

{% apitags %}
Content Cards, Banners
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} Para Content Cards, se um usuário receber dois cartões diferentes da mesma campanha e dispensar ambos, essa contagem aumentará em dois. A reelegibilidade permite incrementar o _Total Dismissals_ uma vez a cada vez que um usuário recebe um cartão; cada cartão é uma mensagem diferente. Para Banners, isso conta cada dispensa quando o comportamento de dispensa está ativado.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Total Dismissals:</i> Contagem</li>
        <li><i>Total Dismissal Rate:</i> Total Dismissals / Total Impressions</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Total Impressions {#total-impressions}

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Esse número é a soma dos eventos de impressão que a Braze recebe dos SDKs.

| Canal | Informações adicionais |
|-------|-----------------------|
| Content Cards | A contagem total de impressões registradas para um determinado Content Card. Isso pode ser incrementado várias vezes para o mesmo usuário. |
| Mensagens no app | Se houver vários dispositivos e a reelegibilidade estiver desativada, o usuário deverá ver a mensagem no app apenas uma vez. Mesmo que o usuário use vários dispositivos, ele a verá apenas no primeiro dispositivo direcionado. Isso pressupõe que o perfil tenha dispositivos consolidados e que o usuário tenha um ID de usuário com o qual está conectado em todos os dispositivos. Se a reelegibilidade estiver ativada, uma impressão é registrada para cada vez que o usuário vê a mensagem no app. Para mais detalhes, consulte <a href="/docs/user_guide/channels/in_app_messages/reporting">Relatórios de mensagens no app</a>. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Total Impressions" }

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

## Total Opens {#total-opens}

{% apitags %}
Email, iOS Push, Android Push, Web Push, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

| Canal | Informações adicionais |
|-------|-----------------------|
| LINE | Rastreado após um limite mínimo de 20 mensagens por dia ser atingido. |
| E-mails AMP | O total de aberturas para as versões HTML e texto simples. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Total Opens" }

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>Email <i>Total Opens</i>:</b> Contagem</li>
        <li><b>Email <i>Total Open Rate</i>:</b> (Opens) / (Deliveries)</li>
        <li><b>Web push <i>Total Opens</i>:</b> Contagem de <i>Direct Opens</i></li>
        <li><b>Web push <i>Total Open Rate</i>:</b> (Total Opens) / (Deliveries)</li>
        <li><b>iOS, Android e Kindle push <i>Total Opens</i>:</b> (Direct Opens) + (Influenced Opens)</li>
        <li><b>iOS, Android e Kindle push <i>Total Open Rate</i>:</b> (Total Opens) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Total Revenue {#total-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} Essa métrica está disponível apenas nos relatórios de comparação de Campaigns por meio do <a href='/docs/user_guide/analytics/reports/report_builder'>Criador de relatórios</a>.

{% endapi %}

{% api %}

## Unique Clicks {#unique-clicks}

{% apitags %}
Email, Content Cards, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

Isso inclui cliques nos links de cancelamento de inscrição fornecidos pela Braze.

| Canal | Informações adicionais |
|-------|-----------------------|
| E-mail | Rastreado ao longo de um período de sete dias. |
| LINE | Rastreado após um limite mínimo de 20 mensagens por dia ser atingido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Unique Clicks" }

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Unique Clicks</i>: Contagem</li>
        <li><b>Content Cards</b> <i>Unique Clicks %</i> ou <i>Unique Clicks Rate</i>: (Unique Clicks) / (Unique Impressions)</li>
        <li><b>Email</b> <i>Unique Clicks %</i> ou <i>Unique Clicks Rate</i>: (Unique Clicks) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Unique Dismissals {#unique-dismissals}

{% apitags %}
Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">Cálculo: (Unique Dismissals) / (Unique Impressions)</span>

{% endapi %}

{% api %}

## Unique Daily Impressions {#unique-daily-impressions}

{% apitags %}
Content Cards, Banners
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Daily Impressions' %}

Esse número é recebido da Braze e é baseado no `user_id`. As impressões diárias únicas são contadas no nível da campanha ou etapa do Canvas.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

## Unique Impressions {#unique-impressions}

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}

| Canal | Informações adicionais |
|-------|-----------------------|
| Mensagens no app | As impressões únicas podem ser incrementadas novamente em um novo dia do calendário no fuso horário do seu espaço de trabalho se a reelegibilidade estiver ativada e o usuário realizar a ação-gatilho. Se a reelegibilidade estiver ativada, <i>Unique Impressions</i> = <i>Unique Recipients</i>. Para mais detalhes, consulte <a href="/docs/user_guide/channels/in_app_messages/reporting">Relatórios de mensagens no app</a>. |
| Content Cards | A contagem não deve ser incrementada na segunda vez que um usuário visualiza um cartão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Unique Impressions" }

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

## Unique Opens {#unique-opens}

{% apitags %}
Email, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Ao avaliar um período de tempo específico, <i>Unique Opens</i> pode parecer maior do que <i>Sends</i> para o mesmo período. Isso pode ocorrer porque os usuários ainda podem registrar eventos de abertura para mensagens que foram enviadas fora desse período de tempo. Para a duração total da campanha, <i>Unique Opens</i> é sempre menor do que o total de <i>Sends</i>.

| Canal | Informações adicionais |
|-------|-----------------------|
| E-mail | Rastreado ao longo de um período de 7 dias. |
| LINE | Rastreado após um limite mínimo de 20 mensagens por dia ser atingido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Unique Opens" }

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Unique Opens</i>: Contagem</li>
        <li><i>Unique Opens %</i> ou <i>Unique Open Rate</i>: (Unique Opens) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Unique Recipients {#unique-recipients}

{% apitags %}
Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}

Como um visualizador pode ser um destinatário único a cada dia, você deve esperar que esse número seja maior do que <i>Unique Impressions</i>. Esse número é recebido da Braze e é baseado no `user_id`. Os destinatários únicos são contados no nível da campanha ou etapa do Canvas, não no nível do <a href='{{ site.homeurl }}{{ site.baseurl }}/api/identifier_types/#send-identifier'>identificador de envio</a>.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

## Unsubscribers ou Unsub {#unsubscribers-or-unsub}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Unsubscribers</i> ou <i>Unsub</i>: Contagem</li>
        <li><i>Unsubscribers %</i> ou <i>Unsub Rate</i>: (Unsubscribes) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Unsubscribes {#unsubscribes}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribes' %}

<span class="calculation-line">Cálculo: (Unsubscribes) / (Deliveries)</span>

{% endapi %}

{% api %}

## Variante {#variation}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}