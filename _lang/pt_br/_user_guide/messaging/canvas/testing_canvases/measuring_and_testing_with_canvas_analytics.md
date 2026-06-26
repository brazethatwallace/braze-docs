---
nav_title: Análise de dados do Canvas
article_title: Análise de dados do Canvas
page_order: 2
page_type: reference
description: "Este artigo de referência descreve as diversas análises de dados e relatórios que você pode usar para entender o desempenho do seu Canvas."
tool:
  - Canvas
  - Reports

---

# Análise de dados do Canvas {#canvas-analytics}

> Você precisa saber se o que está construindo está gerando resultados. Com a análise de dados do Canvas, você pode ter uma visão completa de como as experiências que está criando estão impactando seus objetivos.

Depois de criar seu Canvas e ativá-lo, acesse a página **Canvas** e selecione seu Canvas para abrir a página de detalhes. Lá, você pode medir e testar o desempenho do seu Canvas.

## Visão geral do Canvas {#canvas-overview}

A parte superior da página **Canvas Details** contém as estatísticas gerais do Canvas. Isso inclui o número de mensagens enviadas dentro do Canvas, o número total de vezes que os clientes entraram no Canvas, quantos converteram e sua taxa total, a receita gerada pelo Canvas e o público total estimado.

Este é um ótimo lugar para ter uma visão geral e verificar como seu Canvas está performando em relação ao seu objetivo.

### Usuários contatáveis e estatísticas exatas {#reachable-users-and-exact-statistics}

Quando a opção **[Calcular estatísticas exatas]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#single-user-segments)** está em execução para públicos vinculados ao seu Canvas, a Braze pode exibir brevemente uma estimativa arredondada na área **Usuários contatáveis**. O total exato substitui a estimativa quando o cálculo é concluído. Selecione **Show Additional Stats** para ver um detalhamento completo por canal. O construtor de Canvas documenta o mesmo fluxo em **Público-alvo**; consulte [Calculando o público-alvo]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#calculating-target-population).

![A página Canvas Details mostrando estatísticas gerais, incluindo mensagens enviadas, taxa de conversão, total de entradas, receita total, total de saídas e público estimado, com filtros de canal e estatísticas.]({% image_buster /assets/img_archive/Journey_5.png %})

{% alert tip %}
Se um segmento que você criou a partir da atividade do Canvas mostrar menos usuários contatáveis do que o esperado com base na análise de dados do Canvas, existem dois motivos comuns:

- **Amostragem de estimativa:** As estatísticas do segmento podem exibir uma estimativa baseada em uma amostra aleatória com um intervalo de confiança de 95% de ±1%, em vez de uma contagem exata.
- **Usuários que não atendem mais aos critérios:** Alguns usuários contabilizados na análise de dados do Canvas podem não se qualificar mais para o segmento — por exemplo, porque cancelaram a inscrição ou seus dados de perfil mudaram desde que o Canvas foi executado. Verifique o **Desempenho histórico** do Canvas para um alto volume de cancelamentos de inscrição.
{% endalert %}

### Alterações desde a última visualização {#changes-since-last-viewed}

O número de atualizações no Canvas feitas por outros membros da sua equipe é rastreado pela métrica *Changes Since Last Viewed* na página de visão geral do Canvas. Selecione **Changes Since Last Viewed** para ver um changelog de atualizações no nome, programação, tags, mensagem, público, status de aprovação ou configuração de acesso da equipe do Canvas. Para cada atualização, você pode ver quem realizou a alteração e quando. Você pode usar esse changelog para auditar alterações nos seus Canvas.

## Visualização de desempenho {#performance-visualization}

Conforme você desce na página **Canvas Details**, pode ver o desempenho de cada componente — como quantos usuários entraram, prosseguiram para a próxima etapa ou saíram do Canvas. Selecione uma etapa ou componente específico do Canvas para focar o painel naquela parte da jornada e revisar suas métricas com mais detalhes.

{% alert note %}
No Canvas Flow, um usuário sairá do Canvas após entrar e receber a carga útil da mensagem na última etapa da jornada do usuário.
{% endalert %}

As métricas também incluem impressões, destinatários únicos, contagem de conversões e receita gerada. Você pode clicar em um componente para detalhar ainda mais seus dados e ver o desempenho específico por canal.

![Dois exemplos de detalhes de desempenho para componentes do Canvas. À esquerda, são mostrados os detalhes de desempenho de uma jornada de usuário com um componente do Canvas. À direita, são mostrados os detalhes de desempenho de um componente expandido do Canvas e uma etapa aninhada que exibe a contagem de impressões de mensagens no app.]({% image_buster /assets/img_archive/Journey_6.png %})

## Detalhamento de desempenho por variante {#performance-breakdown-by-variant}

Na parte inferior da página **Canvas Details**, clique em **Analyze Variants** para abrir o modal **Analyze Canvas**. Esse modal contém três guias:

- Analyze Variants
- Canvas Funnel Report
- Canvas Retention Report

### Analyze Variants {#analyze-variants}

Na guia **Analyze Variants**, você pode ver um detalhamento de desempenho por variante e grupo de controle, caso tenha mais de um. Você também pode copiar o identificador de API do Canvas, baixar um arquivo CSV das métricas e copiar as células. A guia **Analyze Variants** contém uma tabela que mostra um detalhamento de cada variante em vários níveis.

Você pode identificar rapidamente variantes eficazes e encontrar as cadências, conteúdos, gatilhos, horários e outros elementos mais adequados.

![O modal Analyze Canvas com a guia Analyze Variants selecionada, mostrando uma tabela comparativa para Path 1 e Path 2 com entradas, envios, receita, taxas de conversão, variação percentual e métricas de intervalo de confiança.]({% image_buster /assets/img_archive/analyze_variants.png %})

As métricas básicas incluem:

- **Variant API Identifier:** O identificador de API da sua variante, que pode ser usado nas suas chamadas de API.
- **Total Entries:** O número total de usuários que entraram na variante do Canvas.
- **Total Sends:** O número total de mensagens enviadas na variante do Canvas.
- **Total Steps:** O número total de etapas na variante do Canvas.
- **Total Revenue:** A receita total em dólares dos destinatários do Canvas dentro da janela de conversão primária definida. A *Total Revenue* é a soma das compras atribuídas aos usuários que receberam aquela variante durante aquele período. As compras ainda contam para a *Total Revenue* mesmo quando o usuário não realiza o evento de conversão primária configurado, desde que a compra esteja dentro das regras de atribuição do período.

{% alert note %}
Assim como as conversões, a receita é tecnicamente rastreada no nível do Canvas, mas é atribuída ao componente mais recente e à variante mais recente da qual o usuário recebeu uma mensagem (ou na qual entrou, caso ainda não tenha recebido uma mensagem).<br><br>
Por exemplo, se um usuário concluir duas etapas e depois fizer uma compra, essa receita é atribuída ao segundo componente e à variante na qual ele entrou. Se ele entrar no Canvas, mas fizer uma compra antes de receber o primeiro componente do Canvas, essa receita é atribuída à variante na qual ele entrou, mas não a nenhum componente.
{% endalert %}

Além disso, você pode ver um detalhamento mais explícito dos [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), incluindo:

- Totais de conversão e taxas de conversão para cada evento de conversão
- Uplift em relação à variante de controle
- Intervalo de confiança estatístico para cada evento de conversão

### Como as conversões são rastreadas {#how-conversions-are-tracked}

Um usuário só pode converter uma vez por evento de conversão por entrada no Canvas. As conversões são atribuídas à mensagem mais recente recebida pelo usuário naquela entrada. O resumo do Canvas reflete todas as conversões realizadas pelos usuários naquela jornada, independentemente de terem recebido uma mensagem ou não. Cada etapa subsequente mostrará apenas as conversões que ocorreram enquanto aquela era a etapa mais recente que o usuário recebeu.

Considere o seguinte exemplo: um Canvas tem 10 notificações por push e o evento de conversão é "Abre o app" (ou "Início de sessão").
- O Usuário A abre o app após entrar, mas antes de receber a primeira mensagem.
- O Usuário B abre o app após cada notificação por push.

O resumo do Canvas mostrará duas conversões, enquanto as etapas individuais mostrarão uma conversão na primeira etapa e nenhuma nas etapas subsequentes. Se o horário de silêncio estiver ativo quando o evento de conversão acontecer, as mesmas regras se aplicam.

Agora, vamos supor que temos um Canvas com horário de silêncio e os seguintes eventos ocorrem:

1. O Usuário A entra em um Canvas.
2. A primeira etapa é uma etapa de postergação dentro do horário de silêncio definido, então a mensagem é suprimida.
3. O Usuário A realiza o evento de conversão.

O Usuário A será contado como convertido na variante geral do Canvas, mas não na etapa, já que não recebeu a etapa.

Para nosso último exemplo, vamos supor que temos um Canvas com reelegibilidade ativada. Se um usuário reelegível realizar o evento de conversão na primeira entrada e na segunda entrada, duas conversões serão contabilizadas.

### Relatório de funil {#funnel-report}

O relatório de funil oferece um relatório visual que permite analisar as jornadas que seus clientes percorrem após receberem um Canvas. Se o seu Canvas usa um grupo de controle ou múltiplas variantes, você poderá entender como as diferentes variantes impactaram o funil de conversão em um nível mais granular e otimizar com base nesses dados. Para saber mais sobre relatórios de funil, consulte [Relatórios de funil]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/).

### Relatório de retenção {#retention-report}

A retenção de usuários é uma das métricas mais importantes para qualquer profissional de marketing. Manter usuários engajados voltando para mais indica que o negócio está saudável. A Braze agora permite que você meça a retenção de usuários diretamente na página **Analytics** do Canvas. Para saber mais sobre como ler e interpretar seu relatório de retenção, confira [Relatórios de retenção]({{site.baseurl}}/user_guide/analytics/reports/retention_reports/).