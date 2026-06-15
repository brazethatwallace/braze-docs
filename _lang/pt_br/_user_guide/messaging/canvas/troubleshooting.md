---
nav_title: Solução de problemas
article_title: Solução de problemas do Canvas
page_order: 7
page_type: reference
description: "Esta página fornece etapas de solução de problemas para o Canvas."
tool: Canvas
---

# Solução de problemas do Canvas {#troubleshoot-canvases}

> Esta página ajuda você a solucionar problemas com seus Canvas.

## Erro "Too many Canvas branches" {#too-many-canvas-branches-error}

Se você vir o erro "Too many Canvas branches" ao lançar um Canvas agendado, a combinação de ramificações de etapas e o tamanho do público de entrada pode criar problemas de desempenho no cluster da Braze que impedem o envio de mensagens.

A Braze exibe essa mensagem quando você lança um Canvas com entrada agendada — não quando salva um rascunho. Para resolver, tente o seguinte:

- Reduza as ramificações de etapas no Canvas.
- Reduza o tamanho do público de entrada.
- Use [Jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) para consolidar ramificações em vez de muitas jornadas paralelas.
- Se o seu Canvas usa o editor original, [clone-o para o Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/) e reconstrua com componentes do Canvas.

Se você ainda precisar lançar o Canvas sem alterações e não puder migrar para o Canvas Flow, entre em contato com o [Suporte]({{site.baseurl}}/support_contact/).

## Por que um usuário não recebeu uma etapa disparada do Canvas? {#why-did-a-user-not-receive-a-triggered-canvas-step}

Primeiro, confirme que o evento personalizado está sendo enviado para a Braze. Acesse **Analytics** > **Relatório de eventos personalizados** e selecione o evento personalizado e o intervalo de datas correspondentes. Se o evento não aparecer, confirme que ele está configurado corretamente e que o usuário realizou a ação correta.

Se o evento personalizado aparecer, investigue mais fazendo o seguinte:

- Verifique o download do perfil do usuário para confirmar que ele disparou o evento e quando isso aconteceu. Se o evento foi disparado, compare o timestamp de quando o evento foi disparado com o horário em que o Canvas entrou no ar. O evento pode ter sido disparado antes do Canvas entrar no ar.
- Revise os changelogs do Canvas e de quaisquer Segments usados no direcionamento para determinar se o usuário estava no Segment quando o evento personalizado foi disparado. Se ele não estava no Segment, não teria recebido a etapa do Canvas.
- Verifique se o usuário foi atribuído ao grupo de controle do Canvas na entrada e, consequentemente, impedido de receber a etapa do Canvas.
- Se houver uma postergação agendada, verifique se o evento personalizado do usuário foi disparado antes da postergação. Se o evento foi disparado antes da postergação, ele não teria recebido a etapa do Canvas.

{% alert note %}
As mensagens no app só podem ser disparadas por eventos enviados pelo SDK, não pela REST API.
{% endalert %}

## Por que meu Canvas não está enviando como esperado? {#why-isnt-my-canvas-sending-as-expected}

Os Canvas são robustos e complexos, e sabemos que você dedica tempo e cuidado ao criá-los. Então, se você perceber que seu Canvas não está enviando da forma desejada, recomendamos verificar a programação do Canvas, o público de entrada e as configurações de entrada, além de revisar as etapas para [criar um Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/).

### Programação {#schedule}

- O Canvas está [programado corretamente]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#entry-schedule-types)?
- Você selecionou a data e o horário corretos?
- Para a [entrega baseada em ação]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=action-based%20delivery#entry-schedule-types), os usuários realizaram as ações especificadas desde que você lançou o Canvas?

### Configurações de entrada {#entry-settings}

As [configurações de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=basics#selecting-entry-controls) são importantes para entender como seus Canvas estão enviando. Verifique se você limitou o número de pessoas que potencialmente entrarão no Canvas.

Os usuários também podem sair de um Canvas se não forem mais elegíveis para receber mensagens. Por exemplo, se o Canvas contém apenas notificações por push e um usuário cancela a inscrição de push após receber a primeira etapa, esse usuário sairia do Canvas. Considere usar [diferentes etapas do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/) para adicionar jornadas alternativas para os usuários.

### Segmentando seu público {#segmenting-your-audience}

Considere as seguintes perguntas sobre seu público-alvo:

- Você selecionou o Segment correto?
- Como o Segment está configurado?
- Você confirmou que o Segment contém algum usuário?
- Você adicionou filtros adicionais que limitariam o número de usuários entrando no Canvas?
- Os usuários se qualificam para receber a primeira etapa das suas variantes? Por exemplo, se a primeira etapa do seu Canvas é uma notificação por push, mas o público de entrada é composto inteiramente por usuários com push desativado, nenhum usuário receberá mensagens.

## Por que os envios ou entregas são menores que o tamanho do meu público-alvo? {#why-are-sends-or-deliveries-lower-than-my-target-audience-size}

O número de mensagens enviadas ou entregues frequentemente difere do público estimado ou da contagem de destinatários. Os motivos mais comuns incluem:

- **Reavaliação do público:** os usuários podem sair do Segment entre o momento em que entram em uma etapa e o momento em que a mensagem é enviada.
- **Elegibilidade do canal:** os usuários podem não ter endereços de e-mail, tokens por push ou o status de inscrição necessário para aquele canal naquela etapa.
- **Grupos de controle:** um grupo de controle global ou do Canvas pode impedir que usuários recebam mensagens.
- **Horário de silêncio, Intelligent Timing e limites de taxa:** essas configurações podem adiar ou suprimir envios.
- **Etapas de mensagens no app:** as mensagens no app podem mostrar zero *Envios* enquanto existem impressões. Isso é esperado porque a entrega de mensagens no app funciona de forma diferente das notificações por push ou e-mail. Consulte [Por que um Canvas pode mostrar zero Envios mesmo que impressões estejam sendo registradas?]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged) nas perguntas frequentes do Canvas.

Para e-mail e outros canais, muitos dos mesmos fatores se aplicam como para Campaigns. Para uma lista detalhada, consulte [Por que os envios são menores que o tamanho estimado do público?]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#why-are-sends-lower-than-the-estimated-audience-size).

## Por que nenhum usuário entrou no meu Canvas agendado diariamente no dia do horário de verão? {#why-did-no-users-enter-my-daily-scheduled-canvas-on-daylight-saving-time-day}

Nos dias de transição do horário de verão, os Canvas agendados diariamente podem ser executados até uma hora antes ou depois do normal. Se seus critérios de entrada dependem de atributos personalizados ou eventos com timestamps que estão dentro de uma hora do horário de entrada agendado, os usuários podem não se qualificar no dia do horário de verão porque o atributo ou evento ainda não foi registrado.

Por exemplo, suponha que os usuários normalmente recebem uma atualização de atributo personalizado às 15h no fuso horário do seu Canvas e seu Canvas é executado diariamente às 15h30 nesse mesmo fuso horário. Em um dia de adiantamento do horário de verão, o Canvas pode avaliar os usuários até uma hora antes do normal em relação a essa atualização de atributo — antes que o atributo tenha sido registrado. Se a reelegibilidade estiver desativada, os usuários que entraram em dias anteriores não podem reentrar, resultando em zero entradas naquele dia.

Para evitar isso, garanta que as atualizações de atributos personalizados ou eventos ocorram mais de uma hora antes do horário de entrada agendado do Canvas.

## Por que meu público não se dividiu igualmente entre o grupo de controle e o grupo de variante? {#why-didnt-my-audience-split-evenly-between-the-control-group-and-variant-group}

Ao criar seu Canvas, você pode ter esperado que seu público se dividisse igualmente entre o grupo de controle e o grupo de variante, como no seguinte [caso de uso](#use-case). Vamos discutir por que isso acontece e como corrigir!

A atribuição ao grupo de controle e à variante acontece na entrada do Canvas com base nas porcentagens que você definiu no construtor — não por meio de filtros de Segment. Um usuário entra em um Canvas quando atende a todos os critérios definidos na [Etapa de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule).

Se os usuários entrarem na variante mas não receberem mensagens porque não são elegíveis para um canal, use as [Configurações de envio]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-14-select-your-send-settings) em cada etapa (por exemplo, **Configurações de inscrição** definidas apenas para usuários que optaram por receber) em vez de adicionar filtros de canal ao **Público-alvo**. Para Canvas multicanal, não limite o público de entrada a um único canal (como **Foreground Push Enabled**).

Usuários que não podem receber um canal específico ainda podem entrar em uma variante. Para limitar quem recebe cada tipo de mensagem, use as configurações de envio por etapa em vez de filtros de público de entrada.

### Caso de uso {#use-case}

Vamos imaginar o seguinte cenário:
- Um Canvas tem uma única variante e um grupo de controle.
- A primeira etapa da variante é uma notificação por push.
- 90% dos usuários foram selecionados para entrar na variante e 10% para entrar no grupo de controle.

![Exemplo de Canvas com 90% de variante e 10% de grupo de controle.]({% image_buster /assets/img_archive/trouble15.png %})

Neste cenário, 90% dos usuários que entram no Canvas entrarão na variante.

Analisando os usuários ativos, podemos ver que, embora o Segment contenha 29,8 mil usuários, apenas 64% deles têm push ativado:

![Segment com o filtro "Push Enabled" definido como "true" e estimativa de 29,8 mil usuários.]({% image_buster /assets/img_archive/trouble16.png %})

Isso significa que, embora tenhamos especificado que 90% dos usuários entrariam na variante, nem todos esses usuários são realmente capazes de receber uma notificação por push. Esses usuários que não podem receber uma notificação por push ainda entrarão na variante independentemente.

## Por que o editor do Canvas está travando ou não carregando? {#why-is-the-canvas-editor-freezing-or-not-loading}

Se você está fazendo edições em Canvas grandes ou complexos com muitas ramificações ou variantes, muitas etapas ou fluxos muito amplos, o editor pode não carregar ou travar. Nesse caso, recomendamos o seguinte:

- Limpe o cache e os cookies do navegador e recarregue a página. Se você usa algum bloqueador de anúncios corporativo ou extensões de navegador, isso pode interferir na plataforma da Braze.
- Use os controles de zoom do Canvas para reduzir a visualização para 25% ou 10%. Isso reduz a quantidade de interface que o navegador precisa renderizar de uma vez.
- Tente usar um navegador diferente.