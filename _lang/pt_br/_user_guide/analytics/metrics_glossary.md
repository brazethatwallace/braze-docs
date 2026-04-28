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
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Cliques AMP {#amp-clicks}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

### Aberturas AMP {#amp-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

### Público {#audience}

{% apitags %}
All
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Cálculo: (Número de destinatários na variante) / (Destinatários únicos)</span>

{% endapi %}

{% api %}

### Bounces

{% apitags %}
Email, Web Push, iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} Isso pode ocorrer porque não há um token por push válido, o usuário cancelou a inscrição após o lançamento da campanha, ou o endereço de e-mail é impreciso ou foi desativado.

| Canal | Informações adicionais |
|-------|-----------------------|
| E-mail | Um bounce de e-mail para clientes que usam SendGrid consiste em hard bounces, spam (`spam_report_drops`) e e-mails enviados para endereços inválidos (`invalid_emails`).<br><br>Para e-mail, *Bounce %* ou *Taxa de bounce* é a porcentagem de mensagens que não foram enviadas com sucesso ou designadas como "devolvidas" ou "não recebidas" dos serviços de envio usados, ou não recebidas pelos usuários com e-mail válido pretendidos. |
| Push | Esses usuários foram automaticamente cancelados de todas as futuras notificações por push. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Bounces</i>: Contagem</li>
        <li><i>Bounce %</i> ou <i>Taxa de bounce %</i>: (Bounces) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Clique no corpo {#body-click}

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Click' %}

<span class="calculation-line">Cálculo: (Cliques no corpo) / (Impressões)</span>

{% endapi %}

{% api %}

### Cliques no corpo {#body-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}

<span class="calculation-line">Cálculo: (Cliques no corpo) / (Impressões)</span>

{% endapi %}

{% api %}

### Cliques no botão 1 {#button-1-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} O relatório de _Cliques no botão 1_ só funciona quando você especifica o **Identifier for Reporting** como "0" na mensagem no app.

<span class="calculation-line">Cálculo: (Cliques no botão 1) / (Impressões)</span>

{% endapi %}

{% api %}

### Cliques no botão 2 {#button-2-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} O relatório de _Cliques no botão 2_ só funciona quando você especifica o **Identifier for Reporting** como "1" na mensagem no app.

<span class="calculation-line">Cálculo: (Cliques no botão 2) / (Impressões)</span>

{% endapi %}

{% api %}

### Análise de dados de Campaign {#campaign-analytics}

{% apitags %}
Feature Flags
{% endapitags %}

O desempenho da mensagem em vários canais. As métricas exibidas dependem do canal de envio de mensagens selecionado e se o [experimento de Feature Flag]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/#campaign-analytics) é um teste multivariante.

{% endapi %}

{% api %}

### Opções enviadas {#choices-submitted}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

### Taxa de clique por abertura {#click-to-open-rate}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Cálculo: (Cliques únicos) / (Aberturas únicas) (para e-mail)</span>

{% endapi %}

{% api %}

### Entregas confirmadas de RCS ou entregas confirmadas de SMS {#rcs-confirmed-deliveries-or-sms-confirmed-deliveries}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} Como cliente da Braze, as entregas são cobradas da sua cota de SMS.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Entregas confirmadas</i>: Contagem</li>
        <li><i>Taxa de entrega confirmada</i>: (Entregas confirmadas) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Intervalo de confiança {#confidence}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Botão da página de confirmação {#confirmation-page-button}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

### Dispensas da página de confirmação {#confirmation-page-dismissals}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

### Conversões (B, C, D) {#conversions-b-c-d}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} Esse evento definido é determinado por você ao criar a campanha.

| Canal | Informações adicionais |
|-------|-----------------------|
| E-mail, push, webhooks | As conversões são rastreadas após o envio inicial. |
| Content Cards | As conversões são contadas quando o usuário visualiza um Content Card pela primeira vez. |
| Mensagens no app | Uma conversão é contada se o usuário recebeu e visualizou a campanha de mensagem no app e, em seguida, realizou o evento de conversão específico dentro da janela de conversão definida, independentemente de ter clicado na mensagem ou não.<br><br>As conversões são atribuídas à mensagem recebida mais recentemente. Se a reelegibilidade estiver ativada, a conversão será atribuída à mensagem no app mais recente recebida, desde que ocorra dentro da janela de conversão definida. No entanto, se a mensagem no app já tiver uma conversão atribuída, a nova conversão não poderá ser registrada para essa mensagem específica. Isso significa que cada entrega de mensagem no app está associada a apenas uma conversão. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### Total de conversões {#total-conversions}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

Quando um usuário visualiza uma campanha de mensagem no app apenas uma vez, apenas uma conversão é contada, mesmo que ele realize o evento de conversão várias vezes depois. No entanto, se a reelegibilidade estiver ativada e o usuário visualizar a campanha de mensagem no app várias vezes, o *Total de conversões* pode aumentar uma vez para cada vez que o usuário registrar uma impressão para uma nova instância da campanha de mensagem no app.

Por exemplo, se um usuário acionar uma mensagem no app duas vezes e converter após cada impressão de mensagem no app (resultando em duas conversões), o *Total de conversões* aumentará em dois. No entanto, se houver apenas uma impressão de mensagem no app seguida de dois eventos de conversão, apenas uma conversão será registrada, e o *Total de conversões* aumentará em um.

{% endapi %}

{% api %}

### Fechar mensagem {#close-message}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Close Message' %}

{% endapi %}

{% api %}

### Taxa de conversão {#conversion-rate}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

| Canal | Informações adicionais |
|-------|-----------------------|
| Mensagens no app | A métrica de <i>Impressões únicas</i> diárias totais é usada para calcular a <i>Taxa de conversão</i> para mensagens no app.<br><br><i>Impressões únicas</i> para mensagens no app só podem ser contadas uma vez por dia do calendário no fuso horário do seu espaço de trabalho. O número de vezes que um usuário conclui uma ação desejada (uma "conversão") pode aumentar dentro desse mesmo dia do calendário. Embora as conversões possam acontecer mais de uma vez por dia, as <i>Impressões únicas</i> não podem. Portanto, se um usuário concluir uma conversão várias vezes em um dia, a <i>Taxa de conversão</i> pode aumentar proporcionalmente, mas as <i>Impressões únicas</i> são contadas apenas uma vez para aquele dia do calendário. Para mais detalhes, consulte <a href="/docs/user_guide/channels/in_app_messages/reporting/">Relatórios de mensagens no app</a>. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>Mensagens no app</b>: (Conversões primárias) / (Impressões únicas)</li>
        <li><b>Outros canais</b>: (Conversões primárias) / (Destinatários únicos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Janela de conversão {#conversion-window}

{% apitags %}
All
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

### Entregas {#deliveries}

{% apitags %}
Email, Web Push, iOS Push, Android Push, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %}

| Canal | Informações adicionais |
|-------|-----------------------|
| E-mail | Refere-se ao número total de mensagens (envios) enviadas com sucesso e recebidas por destinatários com e-mail válido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Entregas</i>: Contagem</li>
        <li><i>Entregas %</i>: (Envios - Bounces) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Falhas de entrega de RCS ou falhas de entrega de SMS {#rcs-delivery-failures-or-sms-delivery-failures}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}

Entre em contato com o <a href="/docs/braze_support/">suporte da Braze</a> para obter ajuda na compreensão dos motivos das falhas de entrega.

<span class="calculation-line">Cálculo: (Envios) - (Envios para operadora)</span>

{% endapi %}

{% api %}

### Falhas de entrega {#delivery-failures}

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

Entre em contato com o <a href="/docs/braze_support/">suporte da Braze</a> para obter ajuda na compreensão dos motivos das falhas de entrega.

<span class="calculation-line">Cálculo: (Envios) - (Envios para operadora)</span>

{% endapi %}

{% api %}

### Taxa de falha de entrega {#failed-delivery-rate}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

Entre em contato com o <a href="/docs/braze_support/">suporte da Braze</a> para obter ajuda na compreensão dos motivos das falhas de entrega.

<span class="calculation-line">Cálculo: (Falhas de entrega) / (Envios)</span>

{% endapi %}

{% api %}

### Aberturas diretas {#direct-opens}

{% apitags %}
iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}

<span class="calculation-line">Cálculo: (Aberturas diretas) / (Entregas)</span>

{% endapi %}

{% api %}

### Com e-mail válido {#emailable}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Erros {#errors}

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Errors' %} Os erros são incluídos na contagem de <i>Envios</i>, mas não são incluídos na contagem de <i>Destinatários únicos</i>.

{% endapi %}

{% api %}

### Aberturas reais estimadas {#estimated-real-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

### Falhas {#failures}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failures' %} As falhas são incluídas na contagem de <i>Envios</i>, mas não na contagem de <i>Entregas</i>.</td>

<span class="calculation-line">Cálculo (<i>Taxa de falha</i>): (Falhas) / (Envios)</span>

{% endapi %}

{% api %}

### Desempenho do experimento de Feature Flag {#feature-flag-experiment-performance}

{% apitags %}
Feature Flags
{% endapitags %}

Métricas de desempenho para a mensagem em um experimento de Feature Flag. As métricas específicas exibidas variam dependendo do canal de envio de mensagens e se o experimento foi ou não um teste multivariante.

{% endapi %}

{% api %}

### Hard bounce

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}

Quando isso ocorre, a Braze marca o endereço de e-mail como inválido, mas não atualiza o [status de inscrição]({{site.baseurl}}/user_guide/channels/email/subscriptions/) do usuário. Se um e-mail receber um hard bounce, a Braze interrompe quaisquer solicitações futuras para esse endereço de e-mail.

{% endapi %}

{% api %}

### Ajuda {#help}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} A resposta de um usuário é medida sempre que ele envia uma mensagem de entrada dentro de quatro horas após receber sua mensagem.

{% endapi %}

{% api %}

### Aberturas por influência {#influenced-opens}

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">Cálculo: (Aberturas por influência) / (Entregas)</span>

{% endapi %}

{% api %}

### Lifetime Revenue

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### Lifetime Value por usuário {#lifetime-value-per-user}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### Receita média diária {#average-daily-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

### Compras diárias {#daily-purchases}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### Receita diária por usuário {#daily-revenue-per-user}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

### Aberturas por máquina {#machine-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Essa métrica é rastreada a partir de 11 de novembro de 2021 para SendGrid e 2 de dezembro de 2021 para SparkPost. Para Amazon SES, a análise de dados aparecerá como _Aberturas_. No entanto, a filtragem de bots para cliques será suportada.

{% endapi %}

{% api %}

### Aberturas {#opens}

{% apitags %}
Web Push, iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### Descadastramento {#opt-out}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} A resposta de um usuário é medida sempre que ele envia uma mensagem de entrada dentro de quatro horas após receber sua mensagem.

{% endapi %}

{% api %}

### Outras aberturas {#other-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Observe que um usuário também pode abrir um e-mail (de modo que a abertura conta para Outras aberturas) antes que uma contagem de Aberturas por máquina seja registrada. Se um usuário abrir um e-mail uma vez (ou mais) após um evento de abertura por máquina de uma caixa de entrada que não seja Apple Mail, a quantidade de vezes que o usuário abre o e-mail é calculada para Outras aberturas e apenas uma vez para Aberturas únicas.

{% endapi %}

{% api %}

### Tentativa pendente {#pending-retry}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

### Conversões primárias (A) ou evento de conversão primária {#primary-conversions-a-or-primary-conversion-event}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}

| Canal | Informações adicionais |
|-------|-----------------------|
| E-mail, push, webhooks | Após o envio inicial. |
| Content Cards, mensagens no app | Quando o usuário visualiza o Content Card ou a mensagem pela primeira vez. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Conversões primárias (A) ou evento de conversão primária</i>: Contagem</li>
        <li><i>Conversões primárias (A) %</i> ou <i>Taxa de evento de conversão primária</i>: (Conversões primárias) / (Destinatários únicos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Leituras {#reads}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Reads' %}

{% endapi %}

{% api %}

### Taxa de leitura {#read-rate}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Read Rate' %}

<span class="calculation-line">Cálculo: (Leituras com confirmação de leitura) / (Envios)</span>

{% endapi %}

{% api %}

### Recebidas {#received}

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
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### Rejeições de RCS ou rejeições de SMS {#rcs-rejections-or-sms-rejections}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Rejections' %} Como cliente da Braze, as rejeições são cobradas da sua cota de SMS.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Rejeições</i>: Contagem</li>
        <li><i>Taxa de rejeição</i>: (Rejeições) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Receita {#revenue}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

### Enviado {#sent}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sent' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Envios {#sends}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} Essa métrica é fornecida pela Braze. Observe que, ao lançar uma campanha agendada, essa métrica incluirá todas as mensagens enviadas, independentemente de já terem sido enviadas ou não devido ao limite de taxa.

{% alert tip %}
Para Content Cards, essa métrica é calculada de forma diferente dependendo do que você selecionou para [Criação de cartão]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation/):

- **No lançamento ou entrada na etapa:** O número de cartões criados e disponíveis para serem vistos. Isso não conta se os usuários visualizaram o cartão.
- **Na primeira impressão:** O número de cartões exibidos aos usuários.
{% endalert %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Mensagens enviadas {#messages-sent}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} Essa métrica é fornecida pela Braze. Observe que, ao lançar uma campanha agendada, essa métrica incluirá todas as mensagens enviadas, independentemente de já terem sido enviadas ou não devido ao limite de taxa.

{% alert tip %}
Para Content Cards, essa métrica é calculada de forma diferente dependendo do que você selecionou para [Criação de cartão]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation/):

- **No lançamento ou entrada na etapa:** O número de cartões criados e disponíveis para serem vistos. Isso não conta se os usuários visualizaram o cartão.
- **Na primeira impressão:** O número de cartões exibidos aos usuários.
{% endalert %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Envios para operadora {#sends-to-carrier}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Envios para operadora</i>: Contagem</li>
        <li><i>Taxa de envios para operadora</i>: (Envios para operadora) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Soft bounce

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Se um e-mail receber um soft bounce, geralmente tentaremos novamente dentro de 72 horas, mas o número de tentativas varia de destinatário para destinatário.

Observe que _Soft bounces_ diferem de _Adiamentos_. Se nenhum e-mail for entregue com sucesso durante esse período de nova tentativa, a Braze envia um evento de soft bounce por tentativa de envio de campanha. Antes de 25 de fevereiro de 2025, essas novas tentativas eram contadas como múltiplos soft bounces para um envio de campanha.

Embora os soft bounces não sejam rastreados na análise de dados da sua campanha, você pode monitorar os soft bounces no [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/). Você também pode excluir esses usuários do seu envio ou verificar a quantidade de soft bounces dos últimos 30 dias com o [filtro de segmento Soft Bounced]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#soft-bounced). No Registro de atividades de envio de mensagem, você também pode ver o motivo dos soft bounces e entender possíveis discrepâncias entre os "envios" e as "entregas" das suas campanhas de e-mail.

{% endapi %}

{% api %}

### Spam

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
        <li><i>Spam %</i> ou <i>Taxa de spam %</i>: (Marcado como spam) / (Envios)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Dispensas da página de pesquisa {#survey-page-dismissals}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

### Envios de pesquisa {#survey-submissions}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

### Total de cliques {#total-clicks}

{% apitags %}
Email, Content Cards, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}

| Canal | Informações adicionais |
|-------|-------|
| LINE | Rastreado após um limite mínimo de 20 mensagens por dia ser atingido. E-mails AMP incluem cliques registrados nas versões HTML e texto simples. Esse número pode ser inflado artificialmente por ferramentas anti-spam. |
| Banners | O número total (e porcentagem) de usuários que clicaram na mensagem entregue, independentemente de o mesmo usuário clicar várias vezes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>E-mail:</b> (Total de cliques) / (Entregas)</li>
        <li><b>Content Cards:</b> (Total de cliques) / (Total de impressões)</li>
        <li><b>SMS:</b> (Aberturas por clique) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total de dispensas {#total-dismissals}

{% apitags %}
Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} Se um usuário receber dois cartões diferentes da mesma campanha e dispensar ambos, essa contagem aumentará em dois. A reelegibilidade permite incrementar o _Total de dispensas_ uma vez a cada vez que um usuário recebe um cartão; cada cartão é uma mensagem diferente.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Total de dispensas:</i> Contagem</li>
        <li><i>Taxa total de dispensas:</i> Total de dispensas / Total de impressões</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total de impressões {#total-impressions}

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Esse número é a soma dos eventos de impressão que a Braze recebe dos SDKs.

| Canal | Informações adicionais |
|-------|-----------------------|
| Content Cards | A contagem total de impressões registradas para um determinado Content Card. Isso pode ser incrementado várias vezes para o mesmo usuário. |
| Mensagens no app | Se houver vários dispositivos e a reelegibilidade estiver desativada, o usuário deverá ver a mensagem no app apenas uma vez. Mesmo que o usuário use vários dispositivos, ele a verá apenas no primeiro dispositivo direcionado. Isso pressupõe que o perfil tenha dispositivos consolidados e que o usuário tenha um ID de usuário com o qual está conectado em todos os dispositivos. Se a reelegibilidade estiver ativada, uma impressão é registrada para cada vez que o usuário vê a mensagem no app. Para mais detalhes, consulte <a href="/docs/user_guide/channels/in_app_messages/reporting/">Relatórios de mensagens no app</a>. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Total de aberturas {#total-opens}

{% apitags %}
Email, iOS Push, Android Push, Web Push, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

| Canal | Informações adicionais |
|-------|-----------------------|
| LINE | Rastreado após um limite mínimo de 20 mensagens por dia ser atingido. |
| E-mails AMP | O total de aberturas para as versões HTML e texto simples. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>E-mail <i>Total de aberturas</i>:</b> Contagem</li>
        <li><b>E-mail <i>Taxa total de aberturas</i>:</b> (Aberturas) / (Entregas)</li>
        <li><b>Push para a web <i>Total de aberturas</i>:</b> Contagem de <i>Aberturas diretas</i></li>
        <li><b>Push para a web <i>Taxa total de aberturas</i>:</b> (Total de aberturas) / (Entregas)</li>
        <li><b>Push para iOS, Android e Kindle <i>Total de aberturas</i>:</b> (Aberturas diretas) + (Aberturas por influência)</li>
        <li><b>Push para iOS, Android e Kindle <i>Taxa total de aberturas</i>:</b> (Total de aberturas) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Receita total {#total-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} Essa métrica está disponível apenas nos relatórios de comparação de Campaigns por meio do <a href='/docs/user_guide/analytics/reports/report_builder'>Criador de relatórios</a>.

{% endapi %}

{% api %}

### Cliques únicos {#unique-clicks}

{% apitags %}
Email, Content Cards, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

Isso inclui cliques nos links de cancelamento de inscrição fornecidos pela Braze.

| Canal | Informações adicionais |
|-------|-----------------------|
| E-mail | Rastreado ao longo de um período de sete dias. |
| LINE | Rastreado após um limite mínimo de 20 mensagens por dia ser atingido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Cliques únicos</i>: Contagem</li>
        <li><b>Content Cards</b> <i>Cliques únicos %</i> ou <i>Taxa de cliques únicos</i>: (Cliques únicos) / (Impressões únicas)</li>
        <li><b>E-mail</b> <i>Cliques únicos %</i> ou <i>Taxa de cliques únicos</i>: (Cliques únicos) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Dispensas únicas {#unique-dismissals}

{% apitags %}
Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">Cálculo: (Dispensas únicas) / (Impressões únicas)</span>

{% endapi %}

{% api %}

### Impressões únicas {#unique-impressions}

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}

| Canal | Informações adicionais |
|-------|-----------------------|
| Mensagens no app | As impressões únicas podem ser incrementadas novamente em um novo dia do calendário no fuso horário do seu espaço de trabalho se a reelegibilidade estiver ativada e o usuário realizar a ação-gatilho. Se a reelegibilidade estiver ativada, <i>Impressões únicas</i> = <i>Destinatários únicos</i>. Para mais detalhes, consulte <a href="/docs/user_guide/channels/in_app_messages/reporting/">Relatórios de mensagens no app</a>. |
| Content Cards | A contagem não deve ser incrementada na segunda vez que um usuário visualiza um cartão. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Aberturas únicas {#unique-opens}

{% apitags %}
Email, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %}

| Canal | Informações adicionais |
|-------|-----------------------|
| E-mail | Rastreado ao longo de um período de 7 dias. |
| LINE | Rastreado após um limite mínimo de 20 mensagens por dia ser atingido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Aberturas únicas</i>: Contagem</li>
        <li><i>Aberturas únicas %</i> ou <i>Taxa de aberturas únicas</i>: (Aberturas únicas) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Destinatários únicos {#unique-recipients}

{% apitags %}
All
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}

Como um visualizador pode ser um destinatário único a cada dia, você deve esperar que esse número seja maior do que <i>Impressões únicas</i>. Para Content Cards, cada Content Card só pode ser recebido uma vez, então visualizar o mesmo Content Card uma segunda vez, independentemente do dia, não incrementará essa contagem.<br><br>Esse número é recebido da Braze e é baseado no `user_id`. Os destinatários únicos são contados no nível da campanha ou etapa do Canvas, não no nível do <a href='https://braze.com/docs/api/identifier_types/#send-identifier'>identificador de envio</a>.

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}

{% api %}

### Cancelamentos de inscrição ou Unsub {#unsubscribers-or-unsub}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Cancelamentos de inscrição</i> ou <i>Unsub</i>: Contagem</li>
        <li><i>Cancelamentos de inscrição %</i> ou <i>Taxa de Unsub</i>: (Cancelamentos de inscrição) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Cancelamentos de inscrição {#unsubscribes}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribes' %}

<span class="calculation-line">Cálculo: (Cancelamentos de inscrição) / (Entregas)</span>

{% endapi %}

{% api %}

### Variação {#variation}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Cálculo: Contagem</span>

{% endapi %}