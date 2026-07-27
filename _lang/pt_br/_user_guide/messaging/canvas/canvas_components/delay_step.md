---
nav_title: Postergação
article_title: Postergação
alias: "/delay_step/"
page_order: 8
page_type: reference
description: "Este artigo de referência explica como adicionar uma postergação ao seu Canvas sem precisar incluir uma mensagem associada."
tool: Canvas

---

# Postergação {#delay}

> Os componentes de postergação permitem adicionar uma postergação independente a um Canvas. Você pode adicionar uma postergação ao seu Canvas sem precisar incluir uma mensagem associada.

As postergações podem deixar seu Canvas mais organizado. Você também pode usar esse componente para postergar uma etapa diferente até uma data exata, um dia específico ou um dia da semana específico. Um componente de postergação pode se conectar a, no máximo, uma etapa subsequente. <br> ![Uma etapa de postergação com 1 dia de espera como primeira etapa de um Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Criar uma postergação {#create-a-delay}

Para criar uma postergação, adicione uma etapa ao seu Canvas. Arraste e solte o componente de Postergação da barra lateral, ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e escolha **Delay**.

### Postergações estendidas {#extended-delays}

Você pode estender etapas de Postergação em até dois anos (730 dias). Por exemplo, se você está fazendo a integração de novos usuários do seu app, pode adicionar uma postergação estendida de dois meses antes de enviar uma etapa de Mensagem para incentivar os usuários que ainda não iniciaram uma sessão.

## Tipos de postergação de tempo {#time-delay-types}

Você pode escolher o tipo de postergação antes da próxima mensagem no seu Canvas. É possível definir uma postergação para que os usuários aguardem um período de tempo determinado ou postergar os usuários até uma data e hora específicas.

Se houver uma postergação de tempo, é esperado que alguns usuários avancem para a próxima etapa do Canvas somente após a postergação. Os usuários que estiverem na postergação não serão adicionados à métrica _Proceeded to Next Step_. Para saber mais, consulte [Análise de dados de postergação](#delay-analytics).

{% tabs %}
{% tab Duration %}

Selecionar **Duration** permite postergar os usuários por um número definido de segundos, minutos, horas, dias ou semanas, e em um horário específico. Por exemplo, você pode postergar os usuários por quatro horas ou por um dia.

Observe a diferença entre como "dias" e "dias corridos" são calculados.

- Um "dia" equivale a 24 horas e é calculado a partir do momento em que o usuário entra na etapa de postergação.
- Um "dia corrido" define o tempo de espera até o próximo horário especificado, que pode ser inferior a 24 horas. Você pode optar por postergar no horário da empresa ou no fuso local do usuário. Se nenhum horário for especificado, o usuário será postergado até a meia-noite do dia seguinte no horário da empresa.

### Comportamento da postergação: "dias corridos" em um horário específico versus "dias" {#delay-behavior-calendar-days-at-a-specific-time-versus-days}

Quando você seleciona **calendar days** como unidade e ativa **At a specific time** (por exemplo, **1 calendar day at 9 AM**), o Canvas calcula primeiro a data corrida alvo e depois aplica o horário agendado. Por exemplo, se uma etapa do Canvas envia às 21h de segunda-feira e a etapa de postergação está definida como **1 calendar day at 9 AM**, a próxima etapa envia às 9h de terça-feira. O Canvas calcula segunda-feira + 1 dia corrido = terça-feira e depois aplica o horário das 9h.

Por outro lado, quando você seleciona **days** como unidade sem **At a specific time** (por exemplo, **After 1 day**), o Canvas aguarda um período completo de 24 horas a partir do momento em que o usuário entra na etapa de postergação. Por exemplo, se uma etapa envia às 9h35 de 13 de outubro e a etapa de postergação é **After 1 day**, a próxima etapa envia às 9h35 de 14 de outubro.

Você também pode selecionar **At a specific time** para especificar quando os usuários avançam no Canvas. Essa opção leva em consideração o horário em que o usuário entrou na etapa de postergação. Se esse horário for posterior ao horário configurado nas configurações, a Braze adiciona mais horas à postergação.

Como exemplo, digamos que hoje é 11 de dezembro e nossa etapa de postergação está definida como **Duration** de uma semana às 8h UTC. Se um usuário entrar na etapa de postergação em 4 de dezembro, ele será liberado da etapa de postergação para continuar sua jornada hoje, caso tenha entrado originalmente na etapa de postergação antes das 8h UTC. Se ele entrou na etapa de postergação após esse horário, o usuário será postergado até o dia seguinte (a próxima ocorrência desse horário).

{% endtab %}
{% tab Calendar date %}

Selecionar **Calendar date** permite manter os usuários na etapa até uma data e hora específicas.

### Considerações {#considerations}

#### Os usuários não receberão etapas ou mensagens com datas passadas {#users-wont-receive-past-dated-steps-or-messages}

Se a data e hora selecionadas já tiverem passado quando os usuários chegarem à etapa de postergação, eles sairão do Canvas. Pode haver até 31 dias entre o início do Canvas e as datas escolhidas para etapas de "aguardar até um dia exato".

{% alert important %}
Se você está participando do [acesso antecipado ao Canvas Context]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context), é possível definir postergações de até 2 anos.
{% endalert %}

Por exemplo, os usuários não receberão etapas ou mensagens nestes cenários:

- Uma mensagem está agendada para ser enviada em 3 de maio às 21h, mas a etapa de postergação expira em 3 de maio às 9h.
- Uma etapa do Canvas posterga até um horário específico no fuso local do usuário, mas os usuários não têm um fuso horário definido no perfil de usuário. A postergação então usa como padrão o fuso horário da empresa para esses usuários, que já passou do horário especificado.

#### Os usuários saem se uma etapa de postergação subsequente estiver dentro do período de uma etapa de postergação anterior {#users-exit-if-a-subsequent-delay-step-is-within-a-prior-delay-steps-timeline}

Se o Canvas tiver duas etapas de postergação, mas a primeira etapa de postergação for mais longa que a segunda, os usuários também sairão do Canvas.

Por exemplo, digamos que um Canvas tenha estas etapas:
- Etapa 1: etapa de mensagem
- Etapa 2: etapa de postergação até 13 de dezembro às 22h
- Etapa 3: etapa de mensagem
- Etapa 4: etapa de postergação até 13 de dezembro às 19h
- Etapa 5: etapa de mensagem

Os usuários que entrarem na Etapa 4 sairão do Canvas antes de receber a Etapa 5, porque a postergação da Etapa 4 faz parte do período da Etapa 2.

{% endtab %}
{% tab Day of the week %}

Selecionar **Day of the week** permite manter os usuários na etapa até um dia da semana específico, em um horário específico. Por exemplo, você pode postergar os usuários até a próxima quinta-feira às 16h no fuso horário da empresa.

Para configurar isso corretamente, você também deve selecionar o que acontece se o usuário entrar no Canvas no dia da semana selecionado (por exemplo, quinta-feira), mas após o horário especificado. Você pode optar por avançar o usuário no mesmo dia ou mantê-lo até a semana seguinte.
{% endtab %}
{% endtabs %}

## Usando etapas de Postergação {#using-delay-steps}

Digamos que estamos em 10 de junho. No dia 11 de junho, você gostaria que os usuários entrassem no Canvas e recebessem uma mensagem sobre uma promoção futura. Depois, você quer manter os usuários no Canvas até 17 de junho às 15h no fuso local. Às 15h no fuso local do dia 17 de junho, você quer enviar aos usuários uma mensagem de lembrete sobre a promoção.

A sequência de etapas do Canvas poderia ser assim:

1. Comece adicionando uma etapa de Mensagem que envia imediatamente após os usuários entrarem no Canvas em 11 de junho.
2. Crie uma etapa de Postergação que mantém os usuários até as 13h no fuso local do dia 17 de junho.
3. Vincule a etapa de Postergação a outra etapa de Mensagem que envia sua mensagem imediatamente.

### Componentes de postergação no final de um Canvas {#delay-as-last-step}

Se você adicionar um componente de Postergação ao seu Canvas e não houver etapas subsequentes, qualquer usuário que alcançar a última etapa será automaticamente avançado para fora do Canvas. Isso é verdade mesmo que o tempo da etapa de Postergação ainda não tenha sido atingido. Isso significa que os usuários que já alcançaram a etapa de Postergação não receberão nenhuma mensagem que você adicionar após essa etapa. No entanto, se um usuário ainda não tiver alcançado a etapa de Postergação e uma mensagem for adicionada, ele receberá essa mensagem.

### Postergações personalizadas {#personalized-delays}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The personalized delays and extended delays feature' %}

Selecione o botão **Personalizar postergação** para configurar uma postergação personalizada para seus usuários. Você pode usar isso com uma [etapa de Contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) para selecionar a variável de contexto pela qual postergar. Isso substitui o horário do dia definido no atributo ou propriedade selecionada. Isso é útil ao aplicar um deslocamento em dias ou semanas, e você quer que os usuários avancem em um horário específico. O fuso horário vem do atributo ou propriedade, ou usa o fallback se nenhum estiver disponível.

#### Comportamento de fuso horário para "em horário específico" {#time-zone-behavior-for-at-specific-time}

Ao configurar postergações personalizadas com a opção **em horário específico**, o comportamento do fuso horário depende do tipo de dados do seu atributo ou variável de contexto:

- **Tipo de dados string com fuso horário:** Se o atributo ou variável de contexto for um tipo de dados string que inclui informações de fuso horário, ele segue o fuso horário especificado na string. Por exemplo, `2025-06-10T10:00:00-08:00` usa UTC-8.
- **Tipo de dados string sem fuso horário:** Se o atributo ou variável de contexto for um tipo de dados string sem informações de fuso horário, ele segue o fuso horário de fallback. Por exemplo, `2025-06-10` usa o fuso horário de fallback.
- **Tipo de dados time:** Se o atributo ou variável de contexto for um tipo de dados time, ele segue UTC. Isso ocorre porque o tipo de dados time é sempre convertido para UTC quando salvo no banco de dados, então "em horário específico" sempre referencia UTC quando a variável está definida como tipo de dados time. Por exemplo, `2025-06-10T10:00:00-08:00` usa UTC+0.

{% alert note %}
É possível que um atributo personalizado ou variável de contexto não tenha nem um horário específico nem um fuso horário se for um tipo de dados string. Se for um tipo de dados time, você precisará especificar o horário e o fuso horário. No entanto, se o atributo personalizado ou variável de contexto for uma string "irrelevante" (como "product_name"), o usuário sai do Canvas.
{% endalert %}

#### Caso de uso {#use-case}

Digamos que você quer lembrar seus clientes de comprar pasta de dente daqui a 30 dias. Usando uma combinação de uma etapa de Contexto e uma etapa de Postergação, você pode selecionar essa variável de contexto pela qual postergar. Nesse caso, sua etapa de Contexto teria os seguintes campos:

- **Nome da variável de contexto:** product_reminder_interval
- **Tipo de dados:** Time
- **Valor:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![A variável "product_reminder_interval" e seu valor.]({% image_buster /assets/img/context_step1.png %})

Em seguida, como você quer lembrar seus clientes daqui a 30 dias, selecione **Até um dia específico** como a opção de postergação e selecione **Personalizar postergação** para usar as informações da sua etapa de Contexto. Isso significa que seus usuários serão postergados até a variável de Contexto selecionada.

## Análise de dados da postergação {#delay-analytics}

Os componentes de postergação têm as seguintes métricas disponíveis na visualização de análise de dados de um Canvas ativo ou anteriormente ativo.

| Métrica | Descrição |
|---|---|
| _Entrou_ | Reflete o número de vezes que a etapa foi acessada. Se o seu Canvas tiver reelegibilidade e um usuário entrar em uma etapa de postergação duas vezes, duas entradas serão registradas. |
| _Prosseguiu para a próxima etapa_ | Reflete o número de entradas que prosseguiram para a próxima etapa no Canvas. |
| _Saiu do Canvas_ | Reflete o número de entradas que saíram do Canvas e não prosseguiram para a próxima etapa. |
| _Falha na personalização_ | Reflete o número de vezes que uma mensagem personalizada ou conteúdo destinado a um usuário não pôde ser entregue devido ao seguinte:<br> {::nomarkdown}<ul><li>O valor da postergação está no passado</li><li>O valor da postergação está mais de 2 anos no futuro</li><li>O valor <b>Após uma duração</b> não é um número</li><li>O valor <b>Até um dia específico</b> não é uma data ou string formatada como data</li></ul>{:/} <br>Consulte [Erros de falha na personalização](#personaliztion-failed-errors) para mais detalhes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Análise de dados da postergação" }

As séries temporais dessas análises estão disponíveis na visualização expandida do componente.

## Solução de problemas {#troubleshooting}

### Erros de falha na personalização {#personalization-failed-errors}

Se os usuários não estão disparando uma postergação personalizada, pode ser porque a etapa de Contexto que você configurou para qualificá-los para a etapa de Postergação não está funcionando como esperado. Quando uma [variável de contexto é inválida]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#troubleshooting), o usuário continua pelo seu Canvas sem ter o contexto definido pela etapa de Contexto. Isso pode fazer com que ele não se qualifique para etapas posteriores no seu Canvas, como postergações personalizadas.

## Solução de problemas

### Usuários em uma etapa de postergação quando um Canvas é interrompido {#users-in-a-delay-step-when-a-canvas-is-stopped}

Quando você [interrompe um Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#stopping-canvases), os usuários que já estão aguardando em uma etapa de postergação não são removidos imediatamente. A Braze ainda agenda a conclusão da postergação, mas **nenhuma mensagem adicional é enviada** enquanto o Canvas estiver interrompido.

Se você reativar o Canvas antes que a postergação de um usuário termine, ele poderá avançar para a próxima etapa conforme agendado. Se o período de postergação já tiver passado enquanto o Canvas estava interrompido, esses usuários saem do Canvas em vez de receber a próxima etapa. Para ver exemplos, consulte [O que acontece quando você interrompe um Canvas?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas) e [Interrompendo Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#stopping-canvases).