---
nav_title: Relatórios
article_title: Relatórios de mensagens no app
page_order: 21
description: "Este artigo de referência aborda os relatórios e a análise de dados de mensagens no app, incluindo detalhes da campanha, desempenho da mensagem e desempenho histórico."
channel:
  - in-app messages
tool:
  - Reports

---

# Relatórios de mensagens no app {#iam-reporting}

> Este artigo de referência aborda os relatórios e a análise de dados de mensagens no app, incluindo detalhes da campanha, desempenho da mensagem e desempenho histórico.

{% multi_lang_include analytics/campaign_analytics.md channel="in-app message" %}

## Métricas de mensagens no app {#in-app-message-metrics}

Aqui estão as principais métricas de mensagens no app que você pode ver na sua análise de dados. Para definições de todas as métricas usadas na Braze, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

{% alert note %}
Para mensagens no app, esta página define impressões únicas usando um limite de dia do calendário no fuso horário do seu espaço de trabalho.
{% endalert %}

| Termo | Definição |
| --- | --- |
| Impressões únicas | O número total de pessoas que realmente visualizaram a mensagem no app. Se um usuário receber a mensagem mais de uma vez no mesmo dia do calendário no fuso horário do seu espaço de trabalho, apenas uma impressão única é contabilizada naquele dia. <br><br> **Se a reelegibilidade estiver ativada:** As impressões únicas podem ser incrementadas novamente em um novo dia do calendário no fuso horário do seu espaço de trabalho, caso o usuário realize a ação-gatilho novamente. Para mensagens no app, *Impressões únicas* é igual a *Destinatários únicos*, pois ambos são incrementados em um novo dia do calendário. |
| Total de impressões | O número de vezes que a mensagem no app é visualizada. Uma impressão é registrada quando a mensagem se torna visível na tela. Se um usuário visualizar a mensagem duas vezes, ele é contabilizado duas vezes. <br><br> **Se houver múltiplos dispositivos e a reelegibilidade estiver desativada:** O usuário vê a mensagem no app apenas uma vez. Mesmo que o usuário use múltiplos dispositivos, ele a vê apenas no primeiro dispositivo direcionado. Isso pressupõe que o perfil tenha dispositivos consolidados e que o usuário tenha um único ID de usuário conectado em todos os dispositivos. <br><br> **Se a reelegibilidade estiver ativada:** Uma impressão é registrada toda vez que o usuário vê a mensagem no app. <br><br> **Nota:** *Total de impressões* contabiliza cada visualização. *Destinatários únicos* é uma métrica separada rastreada usando um limite de dia do calendário no fuso horário do seu espaço de trabalho. |
| Conversões | O rastreamento de conversão começa depois que um usuário registra uma impressão de uma mensagem no app. Uma conversão é contabilizada se o usuário recebeu e visualizou a Campaign de mensagem no app e, em seguida, realiza o evento de conversão específico dentro da janela de conversão definida, independentemente de ter clicado na mensagem ou não. <br><br> As conversões são atribuídas à mensagem recebida mais recentemente. Se a reelegibilidade estiver ativada, a conversão é atribuída à última mensagem no app recebida, desde que ocorra dentro da janela de conversão definida. No entanto, se a mensagem no app já tiver uma conversão atribuída, uma nova conversão não pode ser registrada para aquela mensagem específica. Isso garante que cada entrega de mensagem no app esteja associada a apenas uma conversão. |
| Total de conversões | Quando um usuário visualiza uma Campaign de mensagem no app apenas uma vez, apenas uma conversão é contabilizada, mesmo que ele realize o evento de conversão várias vezes depois. No entanto, se a reelegibilidade estiver ativada e o usuário vir a Campaign de mensagem no app várias vezes, o *Total de conversões* pode aumentar uma vez para cada vez que o usuário registrar uma impressão para uma nova instância da Campaign de mensagem no app. <br><br> Por exemplo, se um usuário disparar uma mensagem no app duas vezes e converter após cada impressão (resultando em duas conversões), o *Total de conversões* aumenta em dois. No entanto, se houve apenas uma impressão seguida de dois eventos de conversão, apenas uma conversão é registrada e o *Total de conversões* aumenta em um. |
| Taxa de conversão | A métrica de impressões únicas diárias totais (*Impressões únicas*) é usada para calcular a taxa de conversão. <br><br> Taxa de conversão = (Conversões primárias) / (Impressões únicas) <br><br> Para mensagens no app, *Impressões únicas* pode ser contabilizada apenas uma vez por dia do calendário no fuso horário do seu espaço de trabalho. O número de vezes que um usuário realiza uma ação desejada (uma "conversão") pode aumentar dentro desse mesmo dia do calendário. Portanto, se um usuário completar uma conversão várias vezes em um dia, a *Taxa de conversão* pode aumentar proporcionalmente, mas as *Impressões únicas* são contabilizadas apenas uma vez para aquele dia do calendário. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas de mensagens no app" }

{% alert tip %}
O *Total de impressões* pode exceder as *Impressões únicas* quando um usuário visualiza a mensagem mais de uma vez no mesmo dia do calendário (consulte as definições de métricas na tabela anterior). Para investigar usuários com contagens de impressões infladas, crie um Segment or segmento com o filtro **Device Count** definido como **more than** `1` e o filtro **Received Message from Campaign** para a Campaign específica.
{% endalert %}

### Rastreamento de cliques {#click-tracking}

A Braze registra uma impressão quando uma mensagem no app se torna visível na tela. Para mensagens no app criadas com o [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional), a tabela a seguir descreve o que conta como um clique.

| Ação do usuário | Clique registrado |
|-------------|--------------|
| O usuário clica no corpo da mensagem quando a mensagem não tem botões | Sim (clique no corpo) |
| O usuário clica em um botão | Sim (clique no botão) |
| O usuário clica no botão de fechar (X) | Não |
| O usuário toca ou clica fora da mensagem para dispensá-la (quando ativado) | Não |
| O usuário fecha o app enquanto a mensagem está sendo exibida | Não |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rastreamento de cliques" }

#### Métricas de mensagens em tela cheia por ação do usuário {#fullscreen-metrics-by-user-action}

Para mensagens no app em [tela cheia]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen) criadas com o editor tradicional, a tabela a seguir mostra o que a Braze registra para ações comuns do usuário. Uma impressão é registrada quando a mensagem se torna visível na tela.

| Ação do usuário | Tela cheia com botões | Tela cheia sem botões |
| --- | --- | --- |
| O usuário vê uma mensagem no app, não clica em nada e fecha o app | 1 impressão | 1 impressão |
| O usuário vê uma mensagem no app e clica no botão de fechar | 1 impressão | 1 impressão |
| O usuário vê uma mensagem no app e clica em um botão de CTA | 1 clique no botão e 1 impressão | N/A |
| O usuário vê uma mensagem no app e toca na tela, mas não em um botão | 1 impressão<br><br>Tocar na mensagem no app não fecha a mensagem | 1 clique no corpo e 1 impressão<br><br>Tocar na mensagem no app fecha a mensagem ou dispara o comportamento ao clicar |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Métricas de mensagens no app em tela cheia por comportamento do usuário" }

{% alert note %}
Cliques no corpo não são coletados automaticamente para mensagens no app criadas com o [editor de arrastar e soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop). Para registrar cliques no corpo, adicione um bloco de **Custom code** e chame `brazeBridge.logClick()`. Para mais detalhes, consulte [Rastreamento de botões]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#button-tracking-improvements) e [Ponte JavaScript]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge).
{% endalert %}

Para definições de cliques no corpo e cliques em botões, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

Para desequilíbrios de impressões entre grupo de controle e variante em testes A/B, consulte [Discrepâncias entre o grupo de controle e a variante]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#discrepancies-between-the-control-group-and-variant).

## Como as conversões são incrementadas com a reelegibilidade? {#how-do-conversions-increment-with-re-eligibility}

A Braze atribui apenas uma conversão a cada entrega de mensagem no app e a associa à mensagem recebida mais recentemente.

Com a reelegibilidade ativada, cada nova entrega pode gerar sua própria conversão. Por exemplo, se um usuário vê a mesma mensagem no app cinco vezes e converte após cada impressão, cinco conversões são contabilizadas. Se um usuário vê a mensagem apenas uma vez, mas converte várias vezes depois, apenas uma conversão é contabilizada.

Se um usuário visualiza uma mensagem no app em dois dias diferentes, mas converte no terceiro dia, a Braze registra a conversão na impressão do segundo dia. Para Canvas, as conversões são rastreadas por entrada no Canvas, não por etapa. Se um usuário converte em várias etapas durante a mesma entrada, isso ainda conta como apenas uma conversão.

{% tabs local %}
{% tab Cenário 1 %}

*Um usuário recebe a mesma mensagem no app cinco vezes em um único dia e converte cinco vezes nesse mesmo dia.*

Sarah recebe uma mensagem no app de um app de compras sobre uma promoção por tempo limitado da sua marca favorita de sapatos. Ela clica na mensagem e compra dois pares de sapatos.

Algumas horas depois, ela recebe a mesma mensagem no app novamente e decide comprar outro par de sapatos. Isso acontece um total de cinco vezes em um único dia, e Sarah acaba fazendo cinco compras separadas, cada vez após clicar na mensagem no app.

**Resultados:** *Total de conversões* e *Total de impressões* de Sarah são incrementados em cinco naquele dia. Como *Impressões únicas* só pode ser incrementado novamente após a virada do dia no fuso horário do espaço de trabalho, *Impressões únicas* permanece o mesmo. Isso faz com que a *Taxa de conversão* aumente dentro desse período.

{% alert note %}
Cada impressão e conversão neste cenário é processada como um evento de SDK or kit de desenvolvimento de software separado. Se o seu SDK or kit de desenvolvimento de software agrupa um evento de impressão e um evento de conversão juntos, a contagem de conversões pode ser diferente.
{% endalert %}

{% endtab %}
{% tab Cenário 2 %}

*Um usuário recebe uma mensagem no app e converte em um único dia.*

Lena recebe uma mensagem no app sobre um novo curso do Braze Learning. Ela clica na mensagem e começa o curso. Enquanto está no app, ela também se inscreve em mais quatro cursos. Tudo isso acontece no mesmo dia após receber apenas uma mensagem.

**Resultados:** *Total de conversões* e *Total de impressões* de Lena são incrementados em um.

{% endtab %}
{% tab Cenário 3 %}

*Um usuário recebe uma mensagem no app e converte um dia depois.*

Tom é um cliente frequente de um app de eCommerce. Ele recebe uma mensagem no app promovendo um desconto por tempo limitado em um produto pelo qual ele se interessa. Tom clica na mensagem, mas decide não comprar imediatamente. No dia seguinte, Tom se lembra do desconto e faz a compra, que é atribuída à mensagem no app que ele recebeu no dia anterior.

**Resultados:** *Total de conversões* e *Total de impressões* de Tom são incrementados em um.

{% endtab %}
{% tab Cenário 4 %}

*Um usuário recebe uma mensagem no app e converte duas vezes um dia depois.*

Alex baixou recentemente um app de jogos arcade. Um dia, Alex recebe uma mensagem no app incentivando a completar uma fase em um novo jogo. Alex clica na mensagem, mas se distrai e não completa nenhuma fase. No dia seguinte, Alex completa duas fases no mesmo jogo.

**Resultados:** Como completar uma fase é o evento de conversão, Alex converteu duas vezes no segundo dia. No entanto, como recebeu apenas uma mensagem no app, *Total de conversões* e *Total de impressões* de Alex são incrementados em um.

{% endtab %}
{% tab Cenário 5 %}

*Um usuário recebe a mesma mensagem no app duas vezes em um único dia e converte duas vezes no dia seguinte.*

John é um profissional ocupado que usa um app de delivery para pedir comida dos seus restaurantes favoritos. No caminho para o trabalho, ele aciona um geofence e recebe uma mensagem no app promovendo restaurantes próximos. Quando volta para casa mais tarde, ele recebe a mesma mensagem novamente porque a reelegibilidade está ativada. Embora goste das ofertas, ele decide não pedir nada naquele dia.

No dia seguinte, John pede almoço e jantar pelo app, realizando o evento de conversão duas vezes.

**Resultados:** *Total de conversões* de John é incrementado em um, e *Total de impressões* é incrementado em dois. Como a reelegibilidade está ativada, a conversão é atribuída à mensagem no app mais recente que John recebeu (a segunda impressão). Uma conversão só pode ser registrada uma vez para cada entrega de mensagem no app.

{% endtab %}
{% endtabs %}