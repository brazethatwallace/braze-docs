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

Aqui estão as principais métricas de mensagens no app que você pode ver na sua análise de dados. Para definições de todas as métricas usadas na Braze, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/analytics/metrics_glossary/).

{% alert note %}
Para mensagens no app, esta página define impressões únicas usando um limite de dia corrido no fuso horário do seu espaço de trabalho.
{% endalert %}

| Termo | Definição |
| --- | --- |
| Impressões únicas | O número total de pessoas que realmente visualizaram a mensagem no app. Se um usuário receber a mensagem mais de uma vez no mesmo dia corrido no fuso horário do seu espaço de trabalho, apenas uma impressão única é contabilizada naquele dia. <br><br> **Se a reelegibilidade estiver ativada:** as impressões únicas podem ser incrementadas novamente em um novo dia corrido no fuso horário do seu espaço de trabalho, caso o usuário execute a ação-gatilho novamente. Para mensagens no app, *Impressões únicas* é igual a *Destinatários únicos*, pois ambos são incrementados em um novo dia corrido. |
| Total de impressões | O número de vezes que a mensagem no app é visualizada. Uma impressão é registrada quando a mensagem se torna visível na tela. Se um usuário visualizar a mensagem duas vezes, ele é contado duas vezes. <br><br> **Se houver múltiplos dispositivos e a reelegibilidade estiver desativada:** o usuário vê a mensagem no app apenas uma vez. Mesmo que o usuário use múltiplos dispositivos, ele a vê apenas no primeiro dispositivo direcionado. Isso pressupõe que o perfil tenha dispositivos consolidados e que o usuário tenha um único ID de usuário conectado em todos os dispositivos. <br><br> **Se a reelegibilidade estiver ativada:** uma impressão é registrada toda vez que o usuário vê a mensagem no app. <br><br> **Nota:** *Total de impressões* conta cada visualização. *Destinatários únicos* é uma métrica separada rastreada usando um limite de dia corrido no fuso horário do seu espaço de trabalho. |
| Conversões | O rastreamento de conversão começa depois que um usuário registra uma impressão de uma mensagem no app. Uma conversão é contabilizada se o usuário recebeu e visualizou a campanha de mensagem no app e, em seguida, realiza o evento de conversão específico dentro da janela de conversão definida, independentemente de ter clicado ou não na mensagem. <br><br> As conversões são atribuídas à mensagem recebida mais recentemente. Se a reelegibilidade estiver ativada, a conversão é atribuída à mensagem no app mais recente recebida, desde que ocorra dentro da janela de conversão definida. No entanto, se a mensagem no app já tiver uma conversão atribuída, uma nova conversão não pode ser registrada para essa mensagem específica. Isso garante que cada entrega de mensagem no app esteja associada a apenas uma conversão. |
| Total de conversões | Quando um usuário visualiza uma campanha de mensagem no app apenas uma vez, apenas uma conversão é contabilizada, mesmo que ele realize o evento de conversão várias vezes depois. No entanto, se a reelegibilidade estiver ativada e o usuário vir a campanha de mensagem no app várias vezes, o *Total de conversões* pode aumentar uma vez para cada vez que o usuário registrar uma impressão de uma nova instância da campanha de mensagem no app. <br><br> Por exemplo, se um usuário acionar uma mensagem no app duas vezes e converter após cada impressão (resultando em duas conversões), o *Total de conversões* aumenta em dois. No entanto, se houve apenas uma impressão seguida de dois eventos de conversão, apenas uma conversão é registrada e o *Total de conversões* aumenta em um. |
| Taxa de conversão | A métrica de impressões únicas diárias (*Impressões únicas*) é usada para calcular a taxa de conversão. <br><br> Taxa de conversão = (Conversões primárias) / (Impressões únicas) <br><br> Para mensagens no app, *Impressões únicas* pode ser contabilizada apenas uma vez por dia corrido no fuso horário do seu espaço de trabalho. O número de vezes que um usuário realiza uma ação desejada (uma "conversão") pode aumentar dentro desse mesmo dia corrido. Portanto, se um usuário realizar uma conversão várias vezes em um dia, a *Taxa de conversão* pode aumentar proporcionalmente, mas as *Impressões únicas* são contabilizadas apenas uma vez para aquele dia corrido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas de mensagens no app" }

## Como as conversões são incrementadas com a reelegibilidade? {#how-do-conversions-increment-with-re-eligibility}

A Braze atribui apenas uma conversão a cada entrega de mensagem no app e a associa à mensagem recebida mais recentemente.

Com a reelegibilidade ativada, cada nova entrega pode gerar sua própria conversão. Por exemplo, se um usuário vir a mesma mensagem no app cinco vezes e converter após cada impressão, cinco conversões são contabilizadas. Se um usuário vir a mensagem apenas uma vez, mas converter várias vezes depois, apenas uma conversão é contabilizada.

Se um usuário visualizar uma mensagem no app em dois dias diferentes, mas converter no terceiro dia, a Braze registra a conversão na impressão do segundo dia. Para Canvas, as conversões são rastreadas por entrada no Canvas, não por etapa. Se um usuário converter em várias etapas durante a mesma entrada, isso ainda conta como apenas uma conversão.

{% tabs local %}
{% tab Cenário 1 %}

*Um usuário recebe a mesma mensagem no app cinco vezes em um único dia e converte cinco vezes nesse mesmo dia.*

Sarah recebe uma mensagem no app de um app de compras sobre uma promoção por tempo limitado na sua marca favorita de sapatos. Ela clica na mensagem e compra dois pares de sapatos.

Algumas horas depois, ela recebe a mesma mensagem no app novamente e decide comprar outro par de sapatos. Isso acontece um total de cinco vezes em um único dia, e Sarah acaba fazendo cinco compras separadas, cada vez após clicar na mensagem no app.

**Resultados:** o *Total de conversões* e o *Total de impressões* de Sarah são incrementados em cinco naquele dia. Como as *Impressões únicas* só podem ser incrementadas novamente após o limite de um dia corrido no fuso horário do espaço de trabalho, as *Impressões únicas* permanecem iguais. Isso faz com que a *Taxa de conversão* aumente dentro desse período.

{% alert note %}
Cada impressão e conversão neste cenário é processada como um evento de SDK separado. Se o seu SDK agrupar um evento de impressão e um evento de conversão juntos, a contagem de conversões pode ser diferente.
{% endalert %}

{% endtab %}
{% tab Cenário 2 %}

*Um usuário recebe uma mensagem no app e converte em um único dia.*

Lena recebe uma mensagem no app sobre um novo curso. Ela clica na mensagem e começa o curso. Enquanto está no app, ela também se inscreve em mais quatro cursos. Tudo isso acontece no mesmo dia após receber apenas uma mensagem.

**Resultados:** o *Total de conversões* e o *Total de impressões* de Lena são incrementados em um.

{% endtab %}
{% tab Cenário 3 %}

*Um usuário recebe uma mensagem no app e converte um dia depois.*

Tom é um cliente frequente de um app de eCommerce. Ele recebe uma mensagem no app promovendo um desconto por tempo limitado em um produto pelo qual ele se interessa. Tom clica na mensagem, mas decide não comprar imediatamente. No dia seguinte, Tom lembra do desconto e faz a compra, que é atribuída à mensagem no app que ele recebeu no dia anterior.

**Resultados:** o *Total de conversões* e o *Total de impressões* de Tom são incrementados em um.

{% endtab %}
{% tab Cenário 4 %}

*Um usuário recebe uma mensagem no app e converte duas vezes um dia depois.*

Alex baixou recentemente um app de jogos arcade. Um dia, Alex recebe uma mensagem no app incentivando a completar uma fase em um novo jogo. Alex clica na mensagem, mas se distrai e não completa nenhuma fase. No dia seguinte, Alex completa duas fases no mesmo jogo.

**Resultados:** como completar uma fase é o evento de conversão, Alex converteu duas vezes no segundo dia. No entanto, como recebeu apenas uma mensagem no app, o *Total de conversões* e o *Total de impressões* de Alex são incrementados em um.

{% endtab %}
{% tab Cenário 5 %}

*Um usuário recebe a mesma mensagem no app duas vezes em um único dia e converte duas vezes no dia seguinte.*

John é um profissional ocupado que usa um app de delivery para pedir comida dos seus restaurantes favoritos. No caminho para o trabalho, ele aciona uma geofence e recebe uma mensagem no app promovendo restaurantes próximos. Quando volta para casa mais tarde, ele recebe a mesma mensagem novamente porque a reelegibilidade está ativada. Embora goste das ofertas, ele decide não pedir nada naquele dia.

No dia seguinte, John pede almoço e jantar pelo app, realizando o evento de conversão duas vezes.

**Resultados:** o *Total de conversões* de John é incrementado em um, e o *Total de impressões* é incrementado em dois. Como a reelegibilidade está ativada, a conversão é atribuída à mensagem no app mais recente que John recebeu (a segunda impressão). Uma conversão pode ser registrada apenas uma vez para cada entrega de mensagem no app.

{% endtab %}
{% endtabs %}