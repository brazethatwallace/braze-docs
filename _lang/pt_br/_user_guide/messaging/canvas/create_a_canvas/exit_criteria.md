---
nav_title: Critérios de saída
article_title: Critérios de saída
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "Este artigo de referência aborda os critérios de saída e como os usuários podem sair do seu Canvas com base nos critérios selecionados."
tool: Canvas
---

# Critérios de saída {#exit-criteria}

> Ao adicionar eventos de exceção diretamente às regras de entrada do seu Canvas, você pode remover usuários da jornada quando eles realizam uma ação específica.
> A Braze registra a saída assim que o evento acontece.
> A velocidade com que um usuário sai completamente do Canvas depende da etapa em que ele está, especialmente em etapas de postergação.
> Para saber mais, consulte [Como os usuários saem](#how-users-exit).

## Como os usuários saem {#how-users-exit}

Quando um usuário realiza o evento de saída, a Braze imediatamente o marca para sair do Canvas. Depois disso, ele não avança para nenhuma etapa posterior.

Se o usuário estiver em uma etapa de postergação, ele permanece nessa etapa até que o período de postergação termine. Ele não prossegue para nenhuma etapa seguinte quando a postergação termina — em vez disso, ele sai completamente do Canvas. Dependendo de onde você analisa os dados do Canvas, é possível ver atividade relacionada à saída no momento em que o evento de saída ocorre e novamente quando a etapa de postergação é concluída e o usuário sai completamente do Canvas.

Por exemplo, se um usuário está em uma etapa de postergação de 30 dias e realiza o evento de saída no primeiro dia dessa etapa, ele é marcado para sair imediatamente, mas não sai completamente do Canvas até que a etapa de postergação termine (29 dias depois).

Vamos considerar outro exemplo usando critérios de saída baseados em tempo. Um usuário entra em uma etapa de postergação configurada para 24 horas em 1º de julho às 00h. Durante esse período de postergação, ele realiza o evento de saída "Fez um pedido pela última vez há menos de 1 hora" às 3h. Esse usuário será avaliado nos critérios de saída em 2 de julho às 00h, que é o momento de conclusão da duração da etapa de postergação. Como já se passaram 21 horas desde o pedido feito em 1º de julho às 3h, ele não sairá do Canvas porque não fez um pedido dentro de uma hora antes do término da etapa de postergação em 2 de julho. Isso impacta o "Total Exits by Exit Criteria" na análise de dados do Canvas, que só é atualizado depois que o usuário tiver saído completamente do Canvas.

## Configurando critérios de saída {#setting-up-exit-criteria}

Na etapa **Público-alvo** do criador de Canvas, você pode configurar critérios de saída para identificar quais usuários devem sair do seu Canvas.

Os critérios de saída incluem um evento de exceção, que é a ação específica que pode fazer com que os usuários saiam do Canvas.

![Os critérios de saída configurados para reengajar usuários que navegaram por produtos, mas ainda não os adicionaram ao carrinho nem fizeram um pedido.]({% image_buster /assets/img/exit_criteria.png %}){: style="max-width:90%;"}

### Selecionando eventos de exceção {#exception-events}

Quando um usuário realiza o evento de exceção, a Braze o marca para sair de acordo com [Como os usuários saem](#how-users-exit). Eventos de exceção se aplicam enquanto o usuário está no Canvas, incluindo quando está aguardando em uma etapa, como uma etapa de postergação.

Digamos que você tenha um Canvas configurado para promover um novo produto. Nesse caso, o pedido do produto seria o evento de exceção. Dessa forma, depois que o usuário fizer o pedido, ele não receberá mais mensagens sobre um produto que já comprou. Os eventos de exceção mantêm suas mensagens relevantes e personalizadas.

Eventos de exceção adicionais incluem:

- Fazer um pedido
- Iniciar uma sessão
- Realizar um evento personalizado
- Realizar um evento de conversão
- Adicionar um endereço de e-mail
- Alterar o valor de um atributo personalizado
- Atualizar um status de inscrição
- Atualizar um status de grupo de inscrições
- Interagir com uma Campaign
- Entrar em um local
- Disparar uma geofence
- Enviar uma mensagem SMS de entrada
- Enviar uma mensagem WhatsApp de entrada
- Enviar uma mensagem LINE de entrada
- Realizar um evento de carrinho atualizado

#### Etapas agendadas {#scheduled-steps}

Para etapas do Canvas que não mantêm o usuário em uma etapa de postergação até um horário futuro, o usuário normalmente sai do Canvas assim que a etapa atual é concluída. Essa conclusão geralmente ocorre imediatamente após o evento de exceção, porque não há temporizador de postergação restante naquela etapa. Isso difere de uma etapa de postergação, em que o usuário permanece até que a postergação termine, mesmo depois de ter sido marcado para sair (consulte [Como os usuários saem](#how-users-exit)).

#### Etapas disparadas {#triggered-steps}

Se uma etapa do Canvas é disparada por um evento, o último envio agendado enfileirado a partir desse disparo será cancelado, mas o usuário permanecerá dentro do Canvas durante a janela. Isso significa que o usuário ainda poderá receber a etapa se realizar o evento-gatilho novamente dentro da janela. Após a janela expirar, o usuário sairá do Canvas.

### Usando Segments e filtros {#using-segments-and-filters}

Você também pode adicionar Segments e filtros nos critérios de saída. Isso significa que os usuários que corresponderem ao Segment or segmento e ao filtro sairão do Canvas e não receberão mais mensagens.

Por exemplo, se a primeira etapa de um Canvas é uma etapa de postergação com cinco dias de espera, os critérios de saída são avaliados quando essa etapa é concluída. Se um usuário atender aos critérios de saída enquanto estiver na etapa de postergação, ele será marcado para sair imediatamente, mas deixará o Canvas completamente ao final dos cinco dias (e não avançará para nenhuma etapa após a postergação).

{% alert note %}
Atributos de array não são compatíveis atualmente como critérios de saída em eventos de exceção.
{% endalert %}

### Mesmo evento de saída e evento de conversão {#having-the-same-exit-event-and-conversion-event}

Quando o evento de saída e o evento de conversão são iguais, tanto a conversão quanto o evento de saída serão contabilizados. Por exemplo, se um Canvas tem uma etapa de postergação e um usuário atende aos critérios de saída enquanto está nessa etapa, o evento de saída será incrementado assim que o usuário sair da etapa de postergação. A conversão também será incrementada assim que o evento for registrado no perfil de usuário.

As conversões são rastreadas mesmo após o término do Canvas, mas as saídas não são rastreadas depois que o usuário sai do Canvas. A janela de conversão se estende até três dias além da duração máxima do Canvas. Isso significa que as conversões continuarão sendo rastreadas após as saídas deixarem de ser rastreadas.

O tempo mínimo para uma janela de conversão é de cinco minutos. Defina as janelas de conversão para cinco minutos nos seus eventos de conversão para se aproximar o máximo possível da paridade com os eventos de saída. Também recomendamos definir a janela de conversão para, pelo menos, corresponder à jornada mais longa do Canvas.

Considere o exemplo a seguir sobre como a análise de dados é calculada:

1. Dez usuários passam pelo Canvas.
2. Três usuários realizam o evento de conversão em cinco minutos (o número de eventos de saída é três, e o número de eventos de conversão é três).
3. Outros cinco usuários saem do Canvas após cinco minutos, mas realizam o evento de conversão após dois dias (o número de eventos de saída permanece o mesmo, mas o evento de conversão aumenta para oito).
4. Os dois últimos usuários saem do Canvas após cinco minutos, mas não realizam o evento de conversão, ou o realizam após três dias e cinco minutos (eles não são contabilizados nas métricas de eventos de saída nem de eventos de conversão).

## Exemplo {#example}

Digamos que queremos direcionar usuários que ainda não fizeram um pedido na nossa empresa de mochilas. Para configurar os critérios de saída, faríamos o seguinte:

1. Selecione **Place an Order** como o evento de exceção.
2. Selecione **Add Trigger**.
3. Em **Segments**, selecione **Used in last day** para que, quando o Canvas for lançado, o público exclua usuários que tenham feito qualquer compra.
4. Em **Filters**, selecione **Purchase behavior** > **Number of purchases** > **Purchased product**.
5. Defina o grupo de filtros como `backpack-example exactly 1`. Isso significa que os usuários que compraram nosso produto de mochila sairiam do Canvas.

![Configurações de critérios de saída com "Makes Any Purchase" como evento de exceção. Se um usuário fizer qualquer compra, ele sairá deste Canvas.]({% image_buster /assets/img_archive/exit_criteria_example.png %}){: style="max-width:80%;"}

{% alert tip %}
Para configurar critérios de saída que comparem propriedades de eventos com propriedades de entrada do Canvas (por exemplo, sair apenas quando um usuário comprar o item específico que abandonou), consulte [Correspondência entre critérios de saída e eventos de entrada]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria).
{% endalert %}