---
nav_title: Medir o tamanho do segmento
article_title: Medir o tamanho do Segment
page_order: 5
page_type: reference
tool:
- Segments
description: "Esta página aborda como você pode monitorar a associação e o tamanho do seu Segment."
---

# Medir o tamanho do Segment {#measure-segment-size}

> Esta página aborda como você pode monitorar a associação e o tamanho do seu Segment.

## Cálculo de pertencimento a Segments {#segment-membership-calculation}

A Braze atualiza o pertencimento do usuário a Segments conforme os dados são enviados de volta aos nossos servidores e processados, normalmente de forma instantânea. O pertencimento de um usuário a um Segment não será alterado até que a sessão tenha sido processada. Por exemplo, um usuário que se enquadra em um Segment de usuários inativos quando a sessão começa será imediatamente removido desse Segment de usuários inativos quando a sessão for processada.

### Cálculo do total de usuários contatáveis {#total-reachable-users-calculation}

Cada Segment exibe o número total de usuários que são membros daquele Segment. Ao filtrar por **Usuários de todos os apps**, também são exibidos alguns dos canais de envio de mensagens mais utilizados (como web push ou e-mail) e o número de usuários contatáveis para esses canais específicos.

É possível que o número total de usuários seja diferente do número de usuários contatáveis por cada canal. Além disso, nem todos os canais são listados na tabela de usuários contatáveis. Por exemplo, Content Cards, webhooks e WhatsApp não são exibidos no detalhamento. Isso significa que a contagem total de usuários contatáveis pode ser maior do que a soma dos usuários de cada canal exibido.

![Uma tabela exibindo o total de usuários contatáveis, detalhado por usuários contatáveis por e-mail, push iOS, push Android, web push e push Kindle.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

Para que um usuário seja listado como contatável por um determinado canal, ele deve ter ambos:
* Um endereço de e-mail válido ou token por push associado ao seu perfil, e
* Ter feito opt-in ou estar inscrito no seu app.

Um único usuário pode pertencer a diferentes grupos de usuários contatáveis. Por exemplo, um usuário pode ter tanto um endereço de e-mail válido quanto um token por push Android válido e ter feito opt-in para ambos, mas não ter nenhum token por push iOS associado. A diferença entre o total de usuários contatáveis e a soma dos diferentes canais representa o número de usuários que se qualificaram para o Segment, mas não são contatáveis por esses canais de comunicação.

{% alert note %}
O **total de usuários contatáveis** inclui todos que correspondem aos filtros do seu Segment, mesmo que não estejam mais inscritos em um canal. As linhas de canal, como **iOS**, contam os usuários que são contatáveis apenas naquele canal de acordo com as regras em [Usuários contatáveis por canal](#reachable-users-by-channel). Para alinhar os totais do Segment com os usuários inscritos, adicione filtros como **Push ativado para iOS** é verdadeiro (ou o equivalente para o seu canal).
{% endalert %}

## Estatísticas para tamanho do segmento {#statistics-for-segment-size}

As estatísticas estimadas são aproximadas por meio da amostragem de apenas uma parte do seu segmento, então você deve esperar que os tamanhos estimados sejam maiores ou menores do que o valor real, com espaços de trabalho maiores apresentando margens de erro potencialmente maiores. Para obter uma contagem precisa de usuários no seu segmento, selecione **Calcular estatísticas exatas**. A associação exata ao segmento sempre será calculada antes que um segmento seja afetado por uma mensagem enviada em uma Campaign ou Canvas.

A Braze fornece as seguintes estatísticas sobre o tamanho do segmento.

### Estatísticas de filtro {#filter-statistics}

Para cada grupo de filtros, você pode visualizar os usuários contatáveis estimados. Selecione **Expandir estatísticas extras do funil** para ver um detalhamento por canal.

![Um grupo de filtros com um filtro para usuários que tiveram exatamente uma contagem de sessão.]({% image_buster /assets/img_archive/segment_filter_stats.png %})

## Estimativa de usuários contatáveis {#reachable-users-estimate}

Você pode visualizar a estimativa de usuários contatáveis de um Segment inteiro, incluindo contagens estimadas de usuários para cada canal, no painel lateral **Usuários contatáveis**. Essa estimativa mostra um intervalo aproximado para o tamanho do seu Segment e uma estimativa de qual porcentagem da sua base de usuários total se enquadra nesse Segment. As estatísticas estimadas ficam em cache por 15 minutos, a menos que você faça edições no seu Segment. Nesse caso, as estatísticas estimadas serão atualizadas automaticamente. Você também pode visualizar uma contagem exata de usuários contatáveis (tanto para o Segment geral quanto por canal) selecionando **Calcular estatísticas exatas**.

{% alert note %}
Espaços de trabalho com mais de 50.000 usuários mostram **Usuários estimados**; espaços de trabalho menores mostram **Usuários exatos**.
{% endalert %}

![O painel "Usuários contatáveis" indicando que há entre 2,3M e 2,4M de usuários estimados.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### Considerações sobre contagens estimadas {#considerations-for-estimate-counts}

A Braze mede o número de usuários estimados consultando um subconjunto dos seus usuários e, em seguida, extrapola esses resultados para todo o seu público. Como o subconjunto de usuários que a Braze consulta pode variar a cada cálculo dessa estimativa, a estimativa também pode mudar em casos em que a composição do seu público tecnicamente deveria ter permanecido a mesma. Por exemplo, se você reordenar seus filtros ou verificar o mesmo Segment em um horário diferente, é possível que a contagem estimada mude (mesmo que **Calcular estatísticas exatas** revelasse os mesmos resultados se o seu Segment não tivesse mudado).

Se você tem uma grande população de usuários no seu espaço de trabalho, pode haver mais variação entre as contagens estimadas e as contagens de cálculo exato, especialmente em casos em que o seu Segment representa uma porcentagem muito pequena da população total do espaço de trabalho. Isso acontece porque a Braze mede a estimativa consultando um subconjunto dos seus usuários e extrapolando os resultados para toda a sua base de usuários. Para bases de usuários maiores, diferenças maiores entre contagens estimadas e exatas são esperadas.

Segments muito pequenos terão um intervalo estimado que inclui 0, o que significa que a porcentagem do total de usuários pode ser arredondada para 0. Nesses casos, **Calcular estatísticas exatas** ajudará você a ver uma contagem precisa do tamanho do seu Segment, que pode não ser realmente 0.

![O painel lateral "Usuários contatáveis" mostrando uma contagem exata de usuários de "31".]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### Usuários contatáveis por canal {#reachable-users-by-channel}

Para visualizar o número de usuários contatáveis para cada canal de envio de mensagens, selecione **Mostrar detalhamento** no painel **Usuários contatáveis**. Isso exibe alguns dos canais de envio de mensagens mais utilizados (como web push ou e-mail) e o número de usuários contatáveis para esses canais específicos.

A métrica _Total_ representa usuários únicos. Por exemplo, se um usuário tem tanto push Android quanto push iOS, ele será contado em ambas as linhas, mas contará como apenas 1 usuário na linha _Total_.

No entanto, é possível que o número total de usuários seja diferente da soma dos usuários contatáveis por cada canal, já que um único usuário pode pertencer a diferentes grupos de usuários contatáveis. Por exemplo, um usuário pode ter tanto um endereço de e-mail válido quanto um token por push Android válido e estar inscrito em ambos, mas não ter nenhum token por push iOS associado.

Tenha em mente que nem todos os canais estão listados na tabela **Usuários contatáveis** (como Content Cards, webhooks e WhatsApp). Por exemplo, se você tem usuários contatáveis apenas pelo WhatsApp, eles serão refletidos no _Total_, mas não em nenhuma das linhas específicas de canal. Isso significa que a contagem total de usuários contatáveis pode ser diferente da soma dos usuários de cada canal exibido.

Em casos em que o _Total_ é maior que a soma dos canais, a diferença representa o número de usuários que se qualificaram para o Segment, mas não são contatáveis por esses canais de comunicação.

Para que um usuário seja listado como contatável por um determinado canal, ele deve ter:
- Um endereço de e-mail válido ou token por push associado ao seu perfil, e
- Optado por receber ou inscrito no seu app.

#### Filtros aplicados para usuários contatáveis por canal específico {#applied-filters-for-channel-specific-reachable-users}

Os seguintes filtros são aplicados para cada canal ao determinar os usuários contatáveis.

| Canal | Filtro |
| --- | --- |
| E-mail | **Email Available** é verdadeiro. |
| Push | **Foreground Push Enabled** é verdadeiro. |
| SMS | **Subscription Group** é qualquer grupo de inscrições de SMS. **Invalid Phone Number** é falso. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Filtros aplicados para usuários contatáveis por canal específico" }

## Calculando estatísticas exatas {#calculating-exact-statistics}

Para visualizar uma contagem precisa do número de usuários no seu Segment, selecione **Calcular estatísticas exatas** no painel **Usuários contatáveis**.

Para atualizar as estatísticas de um cálculo que você já executou anteriormente, selecione **Atualizar estatísticas exatas**. A data em que esse cálculo foi executado pela última vez será atualizada automaticamente.

Observe que a precisão de um cálculo é de apenas 99,999% ou mais. Portanto, para Segments grandes, você pode notar pequenas variações&#8212;mesmo ao calcular estatísticas exatas&#8212;o que é um comportamento normal. Além disso, os resultados de estatísticas exatas ficam em cache por 24 horas, a menos que você faça edições no seu Segment. Nesse caso, você pode recalcular as estatísticas exatas.

{% alert note %}
Segments divididos igualmente por [números de bucket aleatórios]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) não terão o mesmo tamanho. Por exemplo, se você criar um Segment com o filtro **Random Bucket # menor que 5000** e outro Segment com o filtro **Random Bucket # pelo menos 5000**, é possível e esperado que os tamanhos dos Segments variem em até alguns pontos percentuais. Isso ocorre por situações como usuários inativos sendo excluídos e usuários sendo incontatáveis.
{% endalert %}

![Captura de tela do painel de usuários contatáveis mostrando estatísticas exatas e um menu de detalhamento expandido.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

As estatísticas no nível de cada filtro sempre serão estimadas, mesmo que você calcule estatísticas exatas. **Calcular estatísticas exatas** calcula apenas as estatísticas exatas no nível do Segment, não no nível do filtro ou do grupo de filtros. Esse cálculo pode levar alguns minutos para ser executado. Espaços de trabalho maiores, em particular, podem exigir períodos mais longos para concluir os cálculos. Você pode acompanhar o progresso na barra de progresso do painel **Usuários contatáveis**. Quando se espera que um cálculo leve mais de cinco minutos, a Braze enviará os resultados por e-mail.

A Braze prioriza um cálculo por vez por espaço de trabalho, então executar vários cálculos ao mesmo tempo causará atrasos. Você pode selecionar **Visualizar fila de cálculos** para ver quais Segments estão à frente do seu, o progresso deles, quem os iniciou e ter uma ideia de quando seu cálculo poderá ser priorizado.

![Uma fila de cálculos com um cálculo.]({% image_buster /assets/img_archive/calculation_queue.png %})

Você pode cancelar um cálculo de estatísticas exatas selecionando **Cancelar**. Isso pode ser útil quando há vários cálculos na fila e você deseja priorizar outro cálculo primeiro.

## Visualizando o tamanho histórico de membros do Segment {#viewing-historical-segment-membership-size}

Para todos os Segments, você pode visualizar um gráfico histórico de membros que mostra a estimativa de membros do Segment para cada dia. Esse gráfico mostra como o tamanho do seu Segment mudou ao longo do tempo. Use o menu suspenso para filtrar os membros do Segment por intervalo de datas.

![Use o menu suspenso de membros históricos para filtrar os membros do Segment por intervalo de datas.]({% image_buster /assets/img_archive/historical_membership2.png %})

Como o objetivo desse gráfico é dar uma noção das tendências gerais de membros do Segment, a contagem diária é uma estimativa, semelhante a como o tamanho do Segment é uma estimativa antes de você selecionar **Calculate Exact Statistics**. E como esse gráfico mostra estimativas, é possível que o tamanho do seu Segment apareça como "0" nesse gráfico, mesmo que o tamanho real (que pode ser determinado após selecionar **Calculate Exact Stats**) não seja "0". É especialmente provável que o gráfico mostre uma estimativa de "0" se o seu Segment for muito pequeno em relação ao tamanho da população do seu espaço de trabalho.

Por exemplo, digamos que seu espaço de trabalho contém 100 milhões de usuários e seu Segment tem cerca de 700 usuários. É possível que, em alguns dias, nenhum usuário esteja no Segment e nenhum usuário caia na faixa de bucket aleatório usada para a estimativa histórica de membros, resultando em uma contagem de membros de 0 para aquele dia.

A Braze estima a contagem de membros do Segment consultando um subconjunto dos seus usuários e, em seguida, extrapolando esses resultados para todo o seu público. Isso significa que os resultados do gráfico fornecem apenas uma estimativa de quantos membros o Segment pode ter naquele dia, e é esperado que também haja flutuações diárias, pois uma amostra diferente de usuários pode ser consultada para essa estimativa a cada dia.

{% alert note %}
Todas as estimativas podem ser maiores ou menores do que o valor exibido em aproximadamente 1% do tamanho total da população do seu espaço de trabalho. Espaços de trabalho maiores com mais usuários têm maior probabilidade de apresentar estimativas que podem diferir dos cálculos exatos por um valor numérico mais alto, mesmo que a diferença ainda seja de 1% da população de usuários do espaço de trabalho. Isso significa que diferenças maiores entre estimativas e contagens exatas em espaços de trabalho grandes são esperadas.
{% endalert %}

### Razões para mudanças significativas {#reasons-for-significant-changes}

A contagem de membros pode mudar significativamente por diversas razões, como as listadas nesta tabela.

| Razão | Exemplo |
| --- | --- |
| Comportamento normal do usuário | Usuários se inscrevem após uma Campaign particularmente bem-sucedida. |
| Usuários são importados por CSV | Um arquivo CSV de usuários foi importado, aumentando significativamente os membros do Segment. |
| Critérios de público do Segment são modificados | As regras de público de um Segment existente (como filtros) foram alteradas, causando mudanças significativas nos membros do Segment. |
| Usuários são excluídos | Um número significativo de usuários foi excluído. |
| Uma integração com parceiros sincronizou com a Braze | Um terceiro enviou dados para a Braze que influenciaram significativamente os membros do Segment. |
| Usuários inativos são arquivados | Um número significativo de perfis inativos foi arquivado. Por exemplo, um grande número de usuários importados por CSV nunca registra atividade e é arquivado ao mesmo tempo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Razões para mudanças significativas" }