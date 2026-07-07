---
nav_title: Mensagens no app
article_title: Mensagens no app no Canvas
alias: "/canvas_in-app_messages/"
page_order: 2
page_type: reference
description: "Este artigo de referência descreve recursos e nuances específicos das mensagens no app que você pode adicionar ao seu Canvas para exibir mensagens ricas."
tool: Canvas
channel: in-app messages

---

# Mensagens no app no Canvas {#in-app-messages-in-canvas}

> Você pode adicionar mensagens no app como parte da jornada do seu Canvas para exibir mensagens ricas quando o cliente interage com o seu app.

## Como funciona {#how-it-works}

Antes de usar mensagens no app no seu Canvas, certifique-se de ter um [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) configurado com opções de postergação e público.

No construtor do Canvas, adicione uma etapa de [Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) e selecione **In-App Message** como seu **Messaging Channel**. Você pode personalizar [quando sua mensagem vai expirar](#in-app-message-expiration) e qual [comportamento de avanço](#advancement-behavior) ela terá.

Se o seu espaço de trabalho tiver múltiplos apps, direcione o app correto usando **plataformas de entrega**, {% raw %}`{{targeted_device.${platform}}}`{% endraw %} ou {% raw %}`{{app.${api_id}}}`{% endraw %} Liquid tags — não validações de entrega. As mensagens no app são exibidas apenas quando o usuário abre o app direcionado e atende aos critérios de gatilho da etapa. Para saber mais, consulte [Validações de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).

## Adicionando uma mensagem no app à jornada do usuário {#adding-an-in-app-message-to-your-user-journey}

Para adicionar uma mensagem no app ao seu Canvas, faça o seguinte:

1. Adicione uma etapa de [Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) à jornada do usuário.
2. Selecione **In-App Message** como seu **Messaging Channel**.
3. Determine [quando sua mensagem vai expirar](#in-app-message-expiration) e qual [comportamento de avanço](#advancement-behavior-options) ela terá.

## Mensagens no app disparadas {#triggered-in-app-messages}

Você pode selecionar um gatilho para que suas mensagens no app sejam disparadas no início da sessão, ou por eventos personalizados e compras.

Após quaisquer postergações e verificações de opções de público, as mensagens no app ficam ativas quando o usuário alcança a etapa de Mensagem. Se o usuário iniciar uma sessão e realizar o evento de gatilho da mensagem no app, ele verá a mensagem no app.

Para etapas do Canvas com entrada disparada por ação, os usuários podem entrar no Canvas no meio de uma sessão. As mensagens no app não ficam ativas até que uma sessão seja iniciada. Portanto, se o usuário estiver no meio de uma sessão quando alcançar a etapa de Mensagem, ele não receberá a mensagem no app até iniciar outra sessão e realizar o gatilho relevante.

## Expiração da mensagem no app {#in-app-message-expiration}

Você pode escolher quando a mensagem no app vai expirar. Durante esse período, a mensagem no app ficará aguardando para ser visualizada até atingir a data de vencimento. Após o envio da mensagem no app, ela pode ser visualizada uma única vez.

![A seção Controles de mensagem de uma etapa de Mensagem para uma mensagem no app. A mensagem no app expirará três dias após a etapa ficar disponível.]({% image_buster /assets/img_archive/canvas_expiration2.png %}){: style="max-width:90%"}

| Opção | Descrição | Exemplo |
|---|---|---|
| **Uma duração após a etapa ficar disponível** | Define a expiração da mensagem no app em relação a quando a etapa fica disponível para o usuário. | Uma mensagem no app com expiração de dois dias ficaria disponível quando o usuário entrasse na etapa de Mensagem e as opções de público fossem verificadas. Quaisquer postergações antes de alcançar essa etapa viriam de etapas de Postergação anteriores no seu Canvas. A mensagem no app ficaria então disponível por 2 dias (48 horas) a partir do momento em que o usuário entra na etapa, e durante esses dois dias, os usuários poderiam ver a mensagem no app ao abrir o app. |
| **Em uma data e hora específicas** | Selecione uma data e hora específicas em que a mensagem no app não estará mais disponível. | Se você tiver uma promoção que termina em 30 de novembro de 2024, selecione esta opção para que os usuários não vejam mais a mensagem no app associada quando a promoção terminar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Expiração da mensagem no app" }

Quando um usuário inicia uma sessão, a Braze verifica se a elegibilidade ou a expiração das mensagens no app mudou e envia informações de expiração atualizadas para o dispositivo.

Se uma mensagem no app estiver configurada para expirar em uma data e hora específicas que já passaram quando o usuário alcança a etapa de Mensagem, esse usuário não receberá a mensagem no app. Ele continuará pelo Canvas de acordo com o [comportamento de avanço](#advancement-behavior) daquela etapa.

Isso geralmente acontece quando uma etapa anterior, como uma etapa de [Postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), mantém os usuários em um caminho mais longo. Por exemplo, se você lançar um Canvas em 22 de maio com uma postergação de 72 horas seguida de uma mensagem no app que expira em 23 de maio à meia-noite, os usuários alcançarão a etapa de Mensagem após o horário de expiração e não verão a mensagem no app.

## Casos de uso {#use-cases}

A Braze recomenda que você considere usar esse recurso nos seus Canvas promocionais e de integração.

{% tabs %}
  {% tab Promocional %}

Promoções, cupons e liquidações geralmente têm datas de expiração fixas. O Canvas a seguir deve alertar seus usuários nos momentos mais oportunos sobre uma promoção que eles podem usar, e possivelmente influenciar uma compra. Esta promoção expira em 28 de fevereiro de 2019, às 11h15 no fuso horário da sua empresa.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table aria-label="Casos de uso" class="tg">
  <caption>Casos de uso</caption>
<thead>
  <tr>
    <th>Etapa do Canvas</th>
    <th>Postergação</th>
    <th>Público</th>
    <th>Canal</th>
    <th>Expiração</th>
    <th>Avanço</th>
    <th>Informações</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Dia 1: 50% de desconto</td>
    <td>Nenhuma</td>
    <td>Todos da entrada</td>
    <td>Push</td>
    <td>N/A</td>
    <td>Avançar público após postergação</td>
    <td>Push inicial que alerta seus usuários sobre a promoção. O objetivo é direcionar os usuários ao seu app para aproveitar a promoção.</td>
  </tr>
  <tr>
    <td>No app: 50% de desconto</td>
    <td>Nenhuma</td>
    <td>Todos da entrada</td>
    <td>Mensagem no app</td>
    <td><b>Expira em:</b> 28/02/2019 11:15 Horário da empresa</td>
    <td>Mensagem no app visualizada</td>
    <td>O usuário abriu o app e receberá esta mensagem, independentemente de ter sido por causa do push anterior ou não.</td>
  </tr>
  <tr>
    <td>Lembrete de 50% de desconto</td>
    <td>1 dia após o usuário receber a etapa anterior</td>
    <td>Todos da entrada <br><br><b>Filtro:</b> Última compra realizada há mais de uma semana</td>
    <td>Mensagem no app</td>
    <td><b>Expira em:</b> 28/02/2019 11:15 Horário da empresa</td>
    <td>Nenhum (última mensagem no Canvas)</td>
    <td>O usuário recebeu a mensagem no app na etapa anterior, mas não realizou uma compra apesar de estar no app. <br><br>Esta mensagem tem o objetivo de incentivar ainda mais o usuário a fazer uma compra usando a promoção.</td>
  </tr>
</tbody>
</table>

As mensagens no app expiram quando a promoção expira para evitar discrepâncias entre o envio de mensagens e a experiência do cliente.

  {% endtab %}
  {% tab Integração do usuário %}

Sua primeira impressão com um usuário é, talvez, a mais importante. Ela pode determinar o sucesso ou fracasso de futuras visitas ao seu app. Suas comunicações iniciais com o usuário devem ser programadas de forma inteligente e incentivar visitas frequentes ao app para promover o uso.

<table aria-label="Casos de uso" class="tg">
  <caption>Casos de uso</caption>
<thead>
  <tr>
    <th>Etapa do Canvas</th>
    <th>Postergação</th>
    <th>Público</th>
    <th>Canal</th>
    <th>Expiração</th>
    <th>Avanço</th>
    <th>Informações</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>E-mail de boas-vindas</td>
    <td>Nenhuma</td>
    <td>Todos da entrada</td>
    <td>E-mail</td>
    <td>N/A</td>
    <td>Avançar público após postergação</td>
    <td>E-mail inicial que dá as boas-vindas aos seus usuários em um projeto, assinatura ou outro programa de integração. <br><br>O objetivo é direcionar os usuários ao seu app para iniciar a integração.</td>
  </tr>
  <tr>
    <td>Mensagem no app do dia 3-6</td>
    <td>3 dias após o usuário receber a etapa anterior</td>
    <td>Todos da entrada</td>
    <td>Mensagem no app</td>
    <td><b>Expira:</b> 3 dias após a etapa ficar disponível</td>
    <td>Mensagem no app ativa</td>
    <td>Se o usuário agiu com base no e-mail e foi direcionado ao app, ele receberá a mensagem no app desejada para continuar ou lembrá-lo da integração e de quaisquer requisitos associados.</td>
  </tr>
  <tr>
    <td>Push do dia 5</td>
    <td>2 dias após o usuário receber a etapa anterior</td>
    <td>Todos da entrada</td>
    <td>Push</td>
    <td>N/A</td>
    <td>Mensagem enviada</td>
    <td>Após os usuários receberem a mensagem no app, eles receberão um push de acompanhamento para continuar a integração.</td>
  </tr>
</tbody>
</table>

Essas notificações por push são espaçadas em torno de uma mensagem no app para garantir que o usuário visitou o app e iniciou a integração. Isso ajuda a evitar spam ou mensagens fora de ordem que poderiam desestimular os usuários a visitar o app, criando em vez disso uma sequência fluida e lógica para suas experiências iniciais com o app.

  {% endtab %}
{% endtabs %}


## Priorizando mensagens no app {#prioritizing-in-app-messages}

Um usuário pode disparar duas mensagens no app dentro do seu Canvas ao mesmo tempo. Quando isso acontece, a Braze seguirá a seguinte ordem de prioridade para determinar qual mensagem no app será exibida.

Selecione **Definir prioridade exata** e arraste as diferentes etapas do Canvas para reordenar a prioridade. Por padrão, etapas anteriores em uma variante do Canvas serão exibidas antes das etapas posteriores. Após organizar as etapas na ordem de priorização desejada, selecione **Aplicar ordenação**.

![O organizador de prioridade com duas etapas "Welcome IAM" e "Followup IAM".]({% image_buster /assets/img_archive/canvas_priority2.png %}){: style="max-width:85%"}

### Fazendo alterações em rascunhos de Canvas ativos {#making-changes-to-drafts-of-active-canvases}

Se você fizer alterações na prioridade da mensagem no app em **Configurações de envio** de um rascunho de um Canvas ativo, essas alterações serão aplicadas diretamente ao Canvas ativo quando o organizador de prioridade for fechado. No entanto, em uma etapa de Mensagem, o organizador de prioridade será atualizado quando o rascunho for lançado, já que as configurações da etapa do Canvas se aplicam no nível da etapa.

## Comportamento de avanço {#advancement-behavior}

As etapas de Mensagem avançam automaticamente todos os usuários que entram na etapa. Observe que ela não espera a mensagem no app ser disparada ou exibida. Não é necessário especificar o comportamento de avanço da mensagem, o que torna a configuração geral da etapa mais simples.

Quando um usuário entra em uma etapa de mensagem no app, ele avança imediatamente em vez de ser retido durante o período de expiração. Nesse caso, ter uma etapa de Postergação na jornada do usuário pode ser útil.

Para usar a opção **Avançar quando a mensagem for enviada**, adicione uma [jornada do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) separada para filtrar os usuários que não receberam a etapa anterior.

{% details Editor original do Canvas %}

Não é mais possível criar ou duplicar Canvas usando o editor original. Esta seção está disponível como referência para entender como o comportamento de avanço funciona para etapas com mensagens no app.

Canvas criados no editor original precisam especificar um comportamento de avanço — os critérios para avançar pelo componente do Canvas. [Etapas com apenas mensagens no app](#steps-iam-only) têm opções de avanço diferentes das [etapas com múltiplos tipos de mensagem](#steps-multiple-channels) (como push ou e-mail). Para mensagens no app no fluxo de trabalho atual do Canvas, essa opção é configurada para sempre avançar o público imediatamente.

A entrega baseada em ação não está disponível para etapas do Canvas com mensagens no app. Etapas do Canvas com mensagens no app devem ser agendadas. Em vez disso, as mensagens no app do Canvas aparecerão na primeira vez que o usuário abrir o app (disparadas pelo início da sessão) após a mensagem agendada no componente do Canvas ter sido enviada.

Se você tiver múltiplas mensagens no app dentro de um Canvas, o usuário precisará iniciar múltiplas sessões para receber cada uma dessas mensagens individuais.

{% alert important %}
Quando **Advance When In-App Message Live** estiver selecionado, a mensagem no app ficará disponível até expirar, mesmo que o usuário tenha avançado para etapas subsequentes. Se você não quiser que a mensagem no app esteja ativa quando as próximas etapas do Canvas forem entregues, certifique-se de que a expiração seja menor que a postergação nas etapas subsequentes.
{% endalert %}

### Etapas com múltiplos canais {#steps-multiple-channels}

Etapas com uma mensagem no app e outro canal têm as seguintes opções de avanço:

| Opção | Descrição |
|---|---|
| Advance When Message Sent | Os usuários devem receber um e-mail, webhook ou notificação por push, ou visualizar a mensagem no app para avançar para as etapas subsequentes no Canvas.  <br> <br>  Se a mensagem no app expirar e o usuário não tiver recebido o e-mail, webhook ou push, ou não tiver visualizado a mensagem no app, ele sairá do Canvas e não avançará para as etapas subsequentes. |
| Immediately Advance Audience | Todos no público da etapa avançam para as próximas etapas após a postergação, independentemente de terem visto a mensagem indicada ou não. <br> <br> Os usuários devem atender aos critérios de segmento e filtro da etapa para avançar para as próximas etapas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapas com múltiplos canais" }

{% alert important %}
Quando **Entire Audience** estiver selecionado, a mensagem no app ficará disponível até expirar, mesmo que o usuário tenha avançado para etapas subsequentes. Se você não quiser que a mensagem no app esteja ativa quando as próximas etapas do Canvas forem entregues, verifique se a expiração é menor que a postergação nas etapas subsequentes.
{% endalert %}

{% enddetails %}

## Ações-gatilho {#trigger-actions}

Você pode escolher entre as seguintes ações-gatilho para segmentar seus usuários:

- **Realizar compra:** Segmente usuários que realizam qualquer compra ou uma compra específica
- **Iniciar sessão:** Segmente usuários que iniciam uma sessão em qualquer app ou em um app específico
- **Realizar evento personalizado:** Segmente usuários que realizam o evento personalizado selecionado (o evento personalizado deve ser enviado usando o SDK).

O usuário precisa entrar na etapa do Canvas, iniciar uma sessão e então realizar o gatilho para receber uma mensagem no app. Isso significa que atualizações no meio da sessão não são suportadas. Por exemplo, se o gatilho for iniciar uma sessão, o usuário só precisa entrar na etapa do Canvas e iniciar uma sessão para receber a mensagem no app. Se o gatilho não for iniciar uma sessão, o usuário precisa entrar na etapa do Canvas, iniciar uma sessão e então realizar o gatilho para receber a mensagem no app.

!["Realizar uma compra específica" selecionado como ação-gatilho.]({% image_buster /assets/img_archive/canvas_trigger_actions.png %}){: style="max-width:90%"}

Os seguintes recursos do Canvas não estão disponíveis com mensagens no app, portanto não serão aplicados às suas mensagens no app mesmo que estejam ativados.

- Intelligent Timing
- Limite de taxa
- Limite de frequência
- Critérios de saída
- Horário de silêncio

## Propriedades de eventos personalizados em um Canvas {#custom-event-properties-in-a-canvas}

Propriedades de eventos personalizados em mensagens no app para Canvas são suportadas. No entanto, essas propriedades vêm do evento personalizado ou compra que dispara a mensagem no app, localizada na etapa de Mensagem, e não da jornada de ação anterior.

## Considerações {#considerations}

Aqui estão algumas considerações ao enviar mensagens no app em um Canvas.

- Se o usuário nunca reiniciar o app ou nunca iniciar uma sessão, o app não conseguirá verificar se o usuário é elegível para a mensagem no app, o que significa que a mensagem no app não será enviada.
- Quando o primeiro clique ocorre e há uma variável de contexto do Canvas (propriedades de entrada do Canvas), e o usuário reentra no Canvas cinco vezes, a Braze usará a quinta entrada e essa variável de contexto na mensagem no app.
- Um usuário pode ser elegível para até 10 mensagens no app dentro da mesma etapa do Canvas. Por exemplo, se um Canvas permite reentrada e o usuário entra no Canvas 11 vezes, ele receberá apenas 10 mensagens no app se nenhuma tiver expirado.