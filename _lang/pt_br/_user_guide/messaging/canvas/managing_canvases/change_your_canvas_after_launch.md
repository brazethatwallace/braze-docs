---
nav_title: Editar Canvas após o lançamento
article_title: Editar Canvas após o lançamento
page_order: 0
description: "Este artigo de referência aborda os diferentes aspectos de um Canvas que podem ser alterados após o lançamento inicial."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Editar Canvas após o lançamento {#edit-canvases-after-launch}

> Este artigo de referência aborda o que pode ser alterado em um Canvas após o lançamento inicial.

Você pode editar seus Canvas após o lançamento das seguintes formas:

* Inserindo novas etapas do Canvas na jornada do usuário
* Adicionando novas variantes e conexões
* Ajustando a distribuição de variantes
* Parando ou retomando todas as etapas do Canvas

{% alert note %}
A distribuição da variante de controle só pode ser diminuída após o lançamento.
{% endalert %}

Você pode excluir qualquer um dos seguintes itens na jornada do usuário:

- [Etapas do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about)
- Variantes do Canvas
- Conexões entre etapas do Canvas

Se você quiser editar ou adicionar mais etapas à jornada do usuário no Canvas, os seguintes detalhes se aplicam:

- Usuários que ainda não entraram no Canvas são elegíveis para quaisquer etapas recém-criadas.
- Se as configurações de entrada do Canvas permitem que os usuários reentrem nas etapas, os usuários que já passaram pelas etapas recém-criadas são elegíveis para reentrar.
- Usuários que estão atualmente em um Canvas lançado, mas ainda não alcançaram os pontos da jornada do usuário onde novas etapas foram adicionadas, são elegíveis para receber essas etapas recém-adicionadas.

Se você excluir uma etapa de [Postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) ou [jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), você pode opcionalmente redirecionar os usuários que estão aguardando na etapa para outra etapa do Canvas. Para postergações, os usuários permanecem na etapa até o final do período de postergação. Para jornadas de ação, os usuários permanecem na etapa até o final do período de avaliação.

Observe que, quando você lança um Canvas inicialmente, a Braze enfileira os usuários para a etapa de mensagem em que eles estão, e não todas as mensagens subsequentes no Canvas. Se você fizer uma edição no Canvas após o lançamento, alguns usuários podem já estar enfileirados e podem não receber as alterações. Se você parar o Canvas, duplicá-lo, alterá-lo e lançar essa nova versão, o Canvas reavalia todos os usuários novamente, não apenas os que ainda não foram enfileirados.

Consulte a seção [Práticas recomendadas](#best-practices) para casos de uso específicos de edição. Em geral, a prática recomendada é evitar editar Canvas ativos, pois pode haver comportamentos inesperados.

{% details Expandir para detalhes do editor original do Canvas %}

Tenha em mente as seguintes edições permitidas após o lançamento do Canvas, dependendo do fluxo de trabalho com o qual seu Canvas foi criado. Se o seu Canvas usa o fluxo de trabalho original do Canvas, você precisará cloná-lo para o Canvas Flow primeiro para realizar edições pós-lançamento.

Você não pode editar ou excluir conexões existentes, e não pode inserir uma etapa entre etapas já conectadas. Se você quiser editar ou adicionar mais etapas à jornada do usuário no Canvas, os seguintes detalhes se aplicam:

- Usuários que ainda não entraram no Canvas são elegíveis para quaisquer etapas recém-criadas.
- Se as configurações de entrada do Canvas permitem que os usuários reentrem nas etapas, os usuários que já passaram pelas etapas recém-criadas são elegíveis para reentrar.
- Usuários que estão atualmente em um Canvas lançado, mas ainda não alcançaram as etapas recém-adicionadas na jornada do usuário, são elegíveis para receber essas etapas recém-adicionadas.
- Se uma etapa de postergação é a última etapa do Canvas, os usuários que alcançam essa etapa são automaticamente avançados para fora do Canvas e não receberão nenhuma etapa recém-criada.

{% alert important %}
Se você atualizar as configurações de **Postergação** ou **Período** de uma etapa do Canvas, os usuários que estão atualmente nessa etapa no momento da atualização seguem o tempo de postergação que foi atribuído quando entraram originalmente. Apenas novos usuários que entram no Canvas e aqueles que ainda não foram enfileirados para essa etapa recebem a mensagem no horário atualizado.
{% endalert %}

Parar um Canvas não faz com que os usuários que estão aguardando para receber uma mensagem saiam. Se você reativar o Canvas e os usuários ainda estiverem aguardando a mensagem, eles a receberão (a menos que o horário em que a mensagem deveria ter sido enviada já tenha passado — nesse caso, eles não a receberão).

{% enddetails %}

## Detalhes do Canvas {#canvas-details}

Você pode editar as seguintes configurações e detalhes após lançar um Canvas:

* Nome e descrição do Canvas
* Equipes e tags
* Tipo de entrada, cronograma e controles
* Status de inscrição
* Limite de frequência
* Limite de frequência
* Horário de silêncio
* Público-alvo

Após o lançamento de um Canvas:

- Os eventos de conversão não podem ser editados.
- As seguintes etapas não podem ser adicionadas ou removidas, e não podem ser reordenadas para ajustar a classificação: [Jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), [jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) e [jornadas experimentais]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step).
  - **Alternativa 1:** Crie uma nova jornada do público, jornada de ação ou jornada experimental e reconfigure as jornadas para essa nova etapa.
  - **Alternativa 2:** Duplique o Canvas para fazer suas edições.

### Etapas individuais {#individual-steps}

Para etapas individuais do Canvas, você pode editar os seguintes detalhes após o lançamento:

* Nome
* Conteúdo da mensagem
* Gatilhos
* Público
* Eventos de exceção
* Postergações (apenas para etapas de postergação)

No entanto, o tipo de cronograma da etapa e as porcentagens de controle não são editáveis após o lançamento. Para etapas de jornadas de ação e jornadas do público, as classificações e os períodos de avaliação não são editáveis após o lançamento.

#### Etapa Enviar para destino {#send-to-destination-step}

Ao editar a etapa [Enviar para destino]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) em um Canvas ativo, os seguintes comportamentos se aplicam:

- **Alterar o Canvas de destino:** Editar a etapa Enviar para destino para apontar para um Canvas de destino diferente segue as mesmas regras gerais de edição pós-lançamento. As alterações afetam apenas os usuários que ainda não alcançaram a etapa Enviar para destino.
  - Usuários que já passaram pela etapa permanecem no Canvas de destino original — eles não são redirecionados.
  - Usuários atualmente enfileirados em etapas anteriores (por exemplo, aguardando em uma etapa de postergação antes da etapa Enviar para destino) são avaliados em relação aos critérios de entrada e público do novo Canvas de destino quando alcançam a etapa. Usuários elegíveis são enviados para o novo Canvas de destino.
- **Canvas de destino parado:** Se o Canvas de destino for parado enquanto o Canvas de origem ainda estiver ativo, os usuários que alcançarem a etapa Enviar para destino não serão enviados para o Canvas de destino. Isso causa perda de usuários na transferência, não uma pausa enquanto o destino está parado.
  - Usuários que não conseguem entrar no Canvas de destino parado continuam no Canvas de origem se houver mais etapas após a etapa Enviar para destino. Para mais informações sobre o comportamento de avanço, consulte [Enviar para destino]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination#how-does-advancement-behavior-work-for-send-to-destination-steps).
  - Você não pode lançar um Canvas de origem com uma etapa Enviar para destino que aponta para um destino parado. Esse comportamento se aplica quando um Canvas de destino é parado após o Canvas de origem já estar ativo.

### Porcentagens de variantes do Canvas {#canvas-variant-percentages}

Após lançar um Canvas, você só pode diminuir as porcentagens da variante de controle. Se uma porcentagem de variante for modificada no Canvas, os usuários podem ser redistribuídos para outras variantes.

Inicialmente, esses usuários são atribuídos aleatoriamente a uma variante específica antes de receber uma campanha pela primeira vez. A partir daí, cada vez que a campanha é recebida (ou o usuário reentra em uma variante do Canvas), eles recebem a mesma variante, a menos que as porcentagens de variante sejam modificadas.

Se as porcentagens de variante mudarem, os usuários podem ser redistribuídos para outras variantes. Os usuários permanecem nessas variantes até que as porcentagens sejam modificadas novamente. Observe que, para Canvas que usam ramificação com filtros `NOT` com números de bucket aleatórios, os usuários podem não receber a mesma ramificação a cada vez em sua jornada quando reentram no Canvas.

#### Grupos de controle {#control-groups}

Os grupos de controle permanecem consistentes se a porcentagem da variante não for alterada. Se a porcentagem de um grupo de controle for diminuída ou aumentada, os usuários que receberam mensagens anteriormente não poderão entrar no grupo de controle em um envio posterior, e nenhum usuário no grupo de controle receberá uma mensagem.

### Horário de envio local {#local-send-time}

Canvas programados para lançar em um horário de envio local podem ser editados até 24 horas antes do horário de envio programado. Esse período é chamado de "zona segura".

{% alert tip %}
Se você pretende fazer edições maiores que levem à criação de uma cópia totalmente nova do Canvas, lembre-se de excluir os usuários que receberam o primeiro Canvas e reajustar os horários de programação do Canvas para permitir o envio por fuso horário.
{% endalert %}

Quando um cronograma de entrada é configurado para inserir usuários imediatamente após o lançamento, o Canvas é lançado no horário mais próximo em incrementos de 5 minutos. Por exemplo, se você atualizar um Canvas para inserir usuários imediatamente às 8h31 PST, o horário de lançamento será definido como 8h30 PST no fuso horário da empresa.

### Excluindo variantes {#deleting-variants}

Quando variantes são excluídas de um Canvas, o seguinte ocorre:

- As etapas dentro da variante (incluindo aquelas compartilhadas por outras variantes) são excluídas.
- A análise de dados da etapa e a análise de dados de nível superior do Canvas, como _Total de entradas_, _Total de saídas_ e _Taxa de conversão_, são excluídas.
- Os usuários em variantes excluídas saem das etapas, e quaisquer mensagens seguintes não são enviadas.

### Propriedades de entrada do Canvas {#canvas-entry-properties}

As propriedades de entrada do Canvas não são aplicadas como template nas etapas quando enviadas. Isso significa que, quando as propriedades de entrada do Canvas são editadas após o lançamento, essas alterações se aplicam apenas a novos usuários que entram no Canvas. Se o seu Canvas permite que os usuários reentrem, quaisquer usuários que reentrarem serão determinados pelas propriedades de entrada atualizadas do Canvas.

## Práticas recomendadas {#best-practices}

Confira estas práticas recomendadas a ter em mente ao editar ou adicionar ao seu Canvas após o lançamento.

{% alert important %}
Em geral, evite fazer alterações enquanto o Canvas está ativo e enfileirando usuários.
{% endalert %}

### Etapas desconectadas {#disconnected-steps}

Você pode lançar seu Canvas com etapas desconectadas e também salvar esses Canvas após o lançamento. Antes de desconectar uma etapa do seu fluxo de trabalho, recomendamos verificar a visualização de análise de dados das etapas para usuários pendentes.

Digamos que um usuário está em uma etapa desconectada do fluxo de trabalho do seu Canvas. Esse usuário avança para a etapa subsequente, se houver uma. As configurações da etapa determinam como o usuário deve avançar.

Ao criar ou editar etapas desconectadas, você pode fazer alterações nessas etapas independentes sem precisar conectá-las diretamente ao restante do seu Canvas. Isso ajuda a testar suas etapas antes de lançar o Canvas novamente.

### Etapa da jornada experimental {#experiment-path-step}

Se o seu Canvas tem um experimento de jornada vencedora ou jornada personalizada ativo ou em andamento e você atualiza o Canvas ativo (independentemente de atualizar a etapa da jornada experimental em si), o experimento em andamento é encerrado, e a etapa de jornadas experimentais não determina uma jornada vencedora ou jornadas personalizadas. Para reiniciar o experimento, você pode desconectar a jornada experimental existente e lançar uma nova, ou duplicar o Canvas e lançar um novo Canvas. Caso contrário, os usuários seguem pela jornada experimental como se nenhum método de otimização tivesse sido selecionado.

### Postergações de tempo {#time-delays}

Editar Canvas com postergações de tempo pode ser um pouco complicado, então tenha em mente os seguintes detalhes ao fazer edições nos seus Canvas:

- Se você atualizar a postergação em uma etapa de postergação, apenas novos usuários que entram no Canvas e usuários que ainda não foram enfileirados para essa etapa recebem a mensagem no tempo de postergação atualizado.
- Se você excluir uma etapa com postergação de tempo (como postergação ou jornadas de ação) e decidir redirecionar esses usuários para outra etapa do Canvas, os usuários só serão redirecionados após a postergação de tempo da etapa ter sido concluída. Por exemplo, digamos que você exclua uma etapa de postergação com uma postergação de um dia e redirecione esses usuários para uma etapa de mensagem. Nesse caso, os usuários só serão redirecionados após a postergação de um dia ter sido concluída.
- Se o seu Canvas tem uma ou mais etapas de jornadas experimentais, excluir etapas pode invalidar os resultados dessa etapa.

### Parando Canvas {#stopping-canvases}

Parar um Canvas não faz com que os usuários que estão aguardando em uma etapa saiam. Se você reativar o Canvas e os usuários ainda estiverem aguardando, eles completam a etapa e avançam para a próxima etapa. No entanto, se o horário em que o usuário deveria ter avançado para a próxima etapa já tiver passado, ele sairá do Canvas.

Por exemplo, digamos que você tenha um Canvas criado usando o fluxo de trabalho Canvas Flow programado para lançar às 14h com uma variante com duas etapas: uma etapa de postergação com uma postergação de uma hora que leva a uma etapa de mensagem.

Um usuário entra neste Canvas às 14h01 e entra na etapa de postergação ao mesmo tempo. Isso significa que o usuário está programado para avançar para a próxima etapa da jornada do usuário (a etapa de mensagem) às 15h01. Se você parar o Canvas às 14h30 e reativá-lo às 15h30, o usuário sairá do Canvas, pois já passou das 15h01. No entanto, se você reativar o Canvas às 14h40, o usuário avançará para a etapa de mensagem conforme esperado às 15h01.

## Informações importantes {#things-to-know}

Os seguintes problemas comuns podem ser causados pela edição ou adição de mais componentes a qualquer outro componente em um Canvas após o lançamento.

{% alert important %}
Os seguintes problemas são evitáveis. Se você precisar fazer edições em um Canvas após o lançamento, recomendamos primeiro confirmar que todos os usuários que já entraram no Canvas completaram sua jornada do usuário. Além disso, sugerimos que você não exclua etapas que já foram processadas por pelo menos um usuário.
{% endalert %}

- Dados de relatório ausentes (quando variantes de mensagem são excluídas e readicionadas)
- Usuários não seguem a jornada esperada
- Mensagens são enviadas em horários inesperados
- As edições não sobrescrevem dados do Currents, então você pode notar discrepâncias entre etapas do Canvas (como `canvas_step_ids` que não existem no Canvas devido à exclusão)
- Usuários podem receber a mesma mensagem duas vezes
- Usuários não receberão mensagens devido ao limite de frequência existente
  - Quando você atualiza o limite de frequência em um Canvas ativo, o novo limite de frequência se aplica apenas aos usuários que passam pela etapa de mensagem após a alteração do limite de frequência. Usuários que já estão enfileirados para uma etapa de mensagem mantêm o limite de frequência original que estava em vigor quando foram enfileirados. Para aplicar um novo limite de frequência a todos os usuários, pare o Canvas, duplique-o com o limite de frequência atualizado e lance o novo Canvas. Use um filtro para impedir que usuários que receberam mensagens do Canvas original entrem no duplicado.
- Quando um Canvas é [parado automaticamente]({{site.baseurl}}/user_guide/messaging/governance/statuses#available-statuses), os rascunhos pós-lançamento do Canvas também são excluídos.