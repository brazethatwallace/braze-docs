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

A parte superior da página **Detalhes do Canvas** contém as estatísticas principais do Canvas. Elas incluem o número de mensagens enviadas dentro do Canvas, o número total de vezes que os clientes entraram no Canvas, quantos converteram e sua taxa total, a receita gerada pelo Canvas e o público total estimado.

Esse é um ótimo lugar para ter uma visão geral de alto nível e verificar o desempenho do seu Canvas em relação ao seu objetivo. Para receber notificações proativas caso o desempenho de um Canvas caia fora do intervalo esperado, consulte [Alertas de limite do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/canvas_threshold_alerts).

### Usuários contatáveis e estatísticas exatas {#reachable-users-and-exact-statistics}

Quando a opção **[Calcular estatísticas exatas]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#single-user-segments)** está em execução para os públicos vinculados ao seu Canvas, a Braze pode exibir brevemente uma estimativa arredondada na área de **Usuários contatáveis**. O total exato substitui a estimativa quando o cálculo é concluído. Selecione **Mostrar estatísticas adicionais** para ver um detalhamento completo por canal. O construtor de Canvas documenta o mesmo fluxo em **Público-alvo**; consulte [Calculando o público-alvo]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#calculating-target-population).

![A página Detalhes do Canvas mostrando estatísticas principais, incluindo mensagens enviadas, taxa de conversão, total de entradas, receita total, total de saídas e público estimado, com filtros de canal e estatísticas.]({% image_buster /assets/img_archive/Journey_5.png %})

{% alert tip %}
Se um Segment or segmento criado a partir da atividade do Canvas mostrar menos usuários contatáveis do que o esperado com base na análise de dados do Canvas, existem dois motivos comuns:

- **Amostragem de estimativa:** As estatísticas do Segment or segmento podem exibir uma estimativa baseada em uma amostra aleatória com um intervalo de confiança de 95% de ±1%, em vez de uma contagem exata.
- **Usuários que não atendem mais aos critérios:** Alguns usuários contabilizados na análise de dados do Canvas podem não se qualificar mais para o Segment or segmento — por exemplo, porque cancelaram a inscrição ou seus dados de perfil mudaram desde que o Canvas foi executado. Verifique o **Desempenho histórico** do Canvas para um alto volume de cancelamentos de inscrição.
{% endalert %}

### Alterações desde a última visualização {#changes-since-last-viewed}

O número de atualizações no Canvas feitas por outros membros da sua equipe é rastreado pela métrica *Alterações desde a última visualização* na página de visão geral do Canvas. Selecione **Alterações desde a última visualização** para ver um changelog de atualizações no nome, cronograma, tags, mensagem, público, status de aprovação ou configuração de acesso da equipe do Canvas. Para cada atualização, você pode ver quem realizou a atualização e quando. Você pode usar esse changelog para auditar alterações nos seus Canvas.

## Visualização de performance {#performance-visualization}

Conforme você desce pela página **Detalhes do Canvas**, é possível ver a performance de cada componente — como quantos usuários entraram, seguiram para a próxima etapa ou saíram do Canvas. Selecione uma etapa ou componente específico do Canvas para focar o painel nessa parte da jornada e revisar suas métricas com mais detalhes.

{% alert note %}
No Canvas Flow, um usuário sairá do Canvas após entrar e receber a carga útil da mensagem na última etapa da jornada do usuário.
{% endalert %}

As métricas também incluem impressões, destinatários únicos, contagem de conversões e receita gerada. Você pode clicar em um componente para detalhar ainda mais seus dados e ver a performance específica por canal.

![Dois exemplos de detalhes de performance para componentes do Canvas. À esquerda, são exibidos os detalhes de performance de uma jornada de usuário com um componente do Canvas. À direita, são exibidos os detalhes de performance de um componente do Canvas expandido e uma etapa aninhada que mostra a contagem de impressões de mensagens no app.]({% image_buster /assets/img_archive/Journey_6.png %})

## Detalhamento de performance por variante {#performance-breakdown-by-variant}

Na parte inferior da página **Detalhes do Canvas**, clique em **Analisar variantes** para abrir o modal **Analisar Canvas**. Esse modal contém três guias:

- Analisar variantes
- Relatório de funil do Canvas
- Relatório de retenção do Canvas

### Analisar variantes {#analyze-variants}

Na guia **Analisar variantes**, você pode ver um detalhamento de performance por variante e grupo de controle, caso tenha mais de um. Também é possível copiar o identificador de API or interface de programação do aplicativo (API) do Canvas, baixar um arquivo CSV das métricas e copiar as células. A guia **Analisar variantes** contém uma tabela que mostra o detalhamento de cada variante em vários níveis.

Você pode identificar rapidamente as variantes mais eficazes e descobrir as cadências, conteúdos, disparadores, horários ideais e muito mais.

![O modal Analisar Canvas com a guia Analisar variantes selecionada, mostrando uma tabela comparativa para a Jornada 1 e a Jornada 2 com entradas, envios, receita, taxas de conversão, variação percentual e métricas de confiança.]({% image_buster /assets/img_archive/analyze_variants.png %})

As métricas básicas incluem:

- **Identificador de API or interface de programação do aplicativo (API) da variante:** O identificador de API or interface de programação do aplicativo (API) da sua variante, que pode ser usado em suas chamadas de API or interface de programação do aplicativo (API).
- **Total de entradas:** O número total de usuários que entraram na variante do Canvas.
- **Total de envios:** O número total de mensagens enviadas na variante do Canvas.
- **Total de etapas:** O número total de etapas na variante do Canvas.
- **Receita total:** A receita total em dólares dos destinatários do Canvas dentro da janela de conversão primária definida. A *Receita total* é a soma das compras atribuídas aos usuários que receberam aquela variante durante essa janela. As compras ainda contam para a *Receita total* mesmo quando o usuário não realiza o evento de conversão primária configurado, desde que a compra esteja dentro das regras de atribuição da janela.

{% alert note %}
Assim como as conversões, a receita é tecnicamente rastreada no nível do Canvas, mas é atribuída ao componente mais recente e à variante mais recente da qual o usuário recebeu uma mensagem (ou na qual entrou, caso ainda não tenha recebido uma mensagem).<br><br>
Por exemplo, se um usuário conclui duas etapas e depois faz uma compra, essa receita é atribuída ao segundo componente e à variante na qual ele entrou. Se ele entra no Canvas, mas faz uma compra antes de receber o primeiro componente do Canvas, essa receita é atribuída à variante na qual ele entrou, mas não a nenhum componente.
{% endalert %}

Além disso, você pode ver um detalhamento mais explícito dos [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), incluindo:

- Totais de conversão e taxas de conversão para cada evento de conversão
- Aumento em relação à variante de controle
- Confiança estatística para cada evento de conversão

### Como as conversões são rastreadas {#how-conversions-are-tracked}

Um usuário só pode converter uma vez por evento de conversão por entrada no Canvas. As conversões são atribuídas à mensagem mais recente recebida pelo usuário naquela entrada. O resumo do Canvas reflete todas as conversões realizadas pelos usuários naquela jornada, independentemente de terem recebido uma mensagem ou não. Cada etapa subsequente mostrará apenas as conversões que ocorreram enquanto aquela era a etapa mais recente recebida pelo usuário.

Considere o seguinte exemplo: um Canvas tem 10 notificações por push e o evento de conversão é "Abre o app" (ou "Início de sessão").
- O Usuário A abre o app após entrar, mas antes de receber a primeira mensagem.
- O Usuário B abre o app após cada notificação por push.

O resumo do Canvas mostrará duas conversões, enquanto as etapas individuais mostrarão uma conversão na primeira etapa e nenhuma nas etapas subsequentes. Se o horário de silêncio estiver ativo quando o evento de conversão ocorrer, as mesmas regras se aplicam.

Agora, vamos supor que temos um Canvas com horário de silêncio e os seguintes eventos ocorrem:

1. O Usuário A entra em um Canvas.
2. A primeira etapa é uma etapa de postergação dentro do horário de silêncio definido, então a mensagem é suprimida.
3. O Usuário A realiza o evento de conversão.

O Usuário A será contado como convertido na variante geral do Canvas, mas não na etapa, já que não recebeu a etapa.

Para nosso último exemplo, vamos supor que temos um Canvas com reelegibilidade ativada. Se um usuário reelegível realizar o evento de conversão na primeira entrada e na segunda entrada, duas conversões serão contabilizadas.

### Relatório de funil {#funnel-report}

O relatório de funil oferece um relatório visual que permite analisar as jornadas que seus clientes percorrem após receberem um Canvas. Se o seu Canvas usa um grupo de controle ou múltiplas variantes, você poderá entender como as diferentes variantes impactaram o funil de conversão em um nível mais granular e otimizar com base nesses dados. Para saber mais sobre relatórios de funil, consulte [Relatórios de funil]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports).

### Relatório de retenção {#retention-report}

A retenção de usuários é uma das métricas mais importantes para qualquer profissional de marketing. Manter os usuários engajados voltando para mais indica que o negócio está saudável. A Braze agora permite que você meça a retenção de usuários diretamente na página **Canvas Analytics**. Para saber mais sobre como ler e interpretar seu relatório de retenção, confira [Relatórios de retenção]({{site.baseurl}}/user_guide/analytics/reports/retention_reports).