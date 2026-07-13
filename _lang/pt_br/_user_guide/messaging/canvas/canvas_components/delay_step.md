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

Para criar uma postergação, adicione uma etapa ao seu Canvas. Arraste e solte o componente de postergação da barra lateral, ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e escolha **Postergação**.

### Postergações estendidas {#extended-delays}

Você pode estender etapas de postergação por até dois anos (730 dias). Por exemplo, se você está fazendo a integração de novos usuários no seu app, pode adicionar uma postergação estendida de dois meses antes de enviar uma etapa de mensagem para incentivar os usuários que ainda não iniciaram uma sessão.

## Tipos de postergação por tempo {#time-delay-types}

Você pode escolher o tipo de postergação antes da próxima mensagem no seu Canvas. Você pode definir uma postergação para que os usuários esperem por um período determinado, ou postergar os usuários até uma data e hora específicas.

Se houver uma postergação por tempo, é esperado que alguns usuários só avancem para a próxima etapa do Canvas após a postergação. Os usuários que estiverem na postergação não serão adicionados à métrica _Avançaram para a próxima etapa_. Para saber mais, consulte [Análise de dados de postergação](#delay-analytics).

{% tabs %}
{% tab Duração %}

Selecionar **Duração** permite postergar os usuários por um número definido de segundos, minutos, horas, dias ou semanas, em um horário específico. Por exemplo, você pode postergar os usuários por quatro horas ou por um dia.

Observe a diferença entre como "dias" e "dias corridos" são calculados.

- Um "dia" equivale a 24 horas e é calculado a partir do momento em que o usuário entra na etapa de postergação.
- Um "dia corrido" define o tempo de espera até o próximo horário especificado, que pode ser inferior a 24 horas. Você pode optar por postergar no horário da empresa ou no horário local do usuário. Se nenhum horário for especificado, o usuário será postergado até a meia-noite do dia seguinte no horário da empresa.

Você também pode selecionar **Em um horário específico** para definir quando os usuários avançarão no Canvas. Essa opção leva em consideração o horário em que o usuário entrou na etapa de postergação. Se esse horário já tiver passado do horário configurado nas definições, mais horas serão adicionadas à postergação.

Como exemplo, digamos que hoje é 11 de dezembro e nossa etapa de postergação está configurada com **Duração** de uma semana às 8h UTC. Se um usuário entrar na etapa de postergação em 4 de dezembro, ele será liberado da etapa de postergação para continuar sua jornada hoje, caso tenha entrado originalmente na etapa de postergação antes das 8h UTC. Se ele tiver entrado na etapa de postergação após esse horário, o usuário será postergado até o dia seguinte (a próxima ocorrência desse horário).

{% endtab %}
{% tab Data do calendário %}

Selecionar **Data do calendário** permite manter os usuários na etapa até uma data e hora específicas.

### Considerações {#considerations}

#### Usuários não receberão etapas ou mensagens com datas passadas {#users-wont-receive-past-dated-steps-or-messages}

Se a data e hora selecionadas já tiverem passado quando os usuários chegarem à etapa de postergação, eles sairão do Canvas. Pode haver até 31 dias entre o início do Canvas e as datas escolhidas para etapas de "esperar até um dia exato".

{% alert important %}
Se você está participando do [acesso antecipado ao Canvas Context]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context), pode definir postergações de até 2 anos.
{% endalert %}

Por exemplo, os usuários não receberão etapas ou mensagens nestes cenários:

- Uma mensagem está programada para ser enviada em 3 de maio às 21h, mas a etapa de postergação expira em 3 de maio às 9h.
- Uma etapa do Canvas posterga até um horário específico no fuso horário local do usuário, mas os usuários não têm um fuso horário definido no perfil de usuário. A postergação então usa como padrão o fuso horário da empresa para esses usuários, que já passou do horário especificado.

#### Usuários sairão se uma etapa de postergação subsequente estiver dentro do período de uma etapa de postergação anterior {#users-will-exit-if-a-subsequent-delay-step-is-within-a-prior-delay-steps-timeline}

Se o Canvas tiver duas etapas de postergação, mas a primeira for mais longa que a segunda, os usuários também sairão do Canvas.

Por exemplo, digamos que um Canvas tenha estas etapas:
- Etapa 1: Etapa de mensagem
- Etapa 2: Etapa de postergação até 13 de dezembro às 22h
- Etapa 3: Etapa de mensagem
- Etapa 4: Etapa de postergação até 13 de dezembro às 19h
- Etapa 5: Etapa de mensagem

Os usuários que entrarem na Etapa 4 sairão do Canvas antes de receber a Etapa 5, porque a postergação da Etapa 4 está dentro do período da Etapa 2.

{% endtab %}
{% tab Dia da semana %}

Selecionar **Dia da semana** permite manter os usuários na etapa até um dia da semana específico, em um horário específico. Por exemplo, você pode postergar os usuários até a próxima quinta-feira às 16h no fuso horário da empresa.

Para configurar isso corretamente, você também precisará selecionar o que acontece se o usuário entrar no Canvas no dia da semana selecionado (por exemplo, quinta-feira), mas após o horário especificado. Você pode optar por avançar o usuário no mesmo dia ou mantê-lo até a semana seguinte.
{% endtab %}
{% endtabs %}

## Usando etapas de postergação {#using-delay-steps}

Digamos que hoje é 10 de junho. Em 11 de junho, você gostaria que os usuários entrassem no Canvas e recebessem uma mensagem sobre uma promoção futura. Depois, você quer manter os usuários no Canvas até 17 de junho às 15h no horário local. Às 15h no horário local de 17 de junho, você quer enviar aos usuários uma mensagem de lembrete sobre a promoção.

A sequência de etapas do Canvas poderia ser assim:

1. Comece adicionando uma etapa de mensagem que é enviada imediatamente após os usuários entrarem no Canvas em 11 de junho.
2. Crie uma etapa de postergação que mantém os usuários até as 13h no horário local de 17 de junho.
3. Conecte a etapa de postergação a outra etapa de mensagem que envia sua mensagem imediatamente.

### Componentes de postergação no final de um Canvas {#delay-as-last-step}

Se você adicionar um componente de postergação ao seu Canvas e não houver etapas subsequentes, qualquer usuário que chegar à última etapa será automaticamente avançado para fora do Canvas. Isso acontece mesmo que o tempo da etapa de postergação ainda não tenha sido atingido. Isso significa que os usuários que já chegaram à etapa de postergação não receberão nenhuma mensagem que você adicionar após essa etapa. No entanto, se um usuário ainda não tiver chegado à etapa de postergação e uma mensagem for adicionada, ele receberá essa mensagem.

### Postergações personalizadas {#personalized-delays}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The personalized delays and extended delays feature' %}

Selecione o botão **Personalizar postergação** para configurar uma postergação personalizada para seus usuários. Você pode usar isso com uma [etapa de Context]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) para selecionar a variável de contexto pela qual postergar. Isso substituirá o horário do dia definido no atributo ou propriedade selecionada. Isso é útil ao aplicar um deslocamento em dias ou semanas quando você quer que os usuários avancem em um horário específico. O fuso horário vem do atributo ou propriedade, ou usa o fallback se nenhum estiver disponível.

#### Comportamento do fuso horário para "em um horário específico" {#time-zone-behavior-for-at-specific-time}

Ao configurar postergações personalizadas com a opção **em um horário específico**, o comportamento do fuso horário depende do tipo de dados do seu atributo ou variável de contexto:

- **Tipo de dados string com fuso horário:** Se o atributo ou variável de contexto for do tipo string e incluir informações de fuso horário, ele seguirá o fuso horário especificado na string. Por exemplo, `2025-06-10T10:00:00-08:00` usa UTC-8.
- **Tipo de dados string sem fuso horário:** Se o atributo ou variável de contexto for do tipo string sem informações de fuso horário, ele seguirá o fuso horário de fallback. Por exemplo, `2025-06-10` usa o fuso horário de fallback.
- **Tipo de dados time:** Se o atributo ou variável de contexto for do tipo time, ele seguirá UTC. Isso acontece porque o tipo de dados time é sempre convertido para UTC quando salvo no banco de dados. Portanto, "em um horário específico" sempre referenciará UTC quando a variável estiver definida como tipo de dados time. Por exemplo, `2025-06-10T10:00:00-08:00` usa UTC+0.

{% alert note %}
É possível que um atributo personalizado ou variável de contexto não tenha nem um horário específico nem um fuso horário se for do tipo string. Se for do tipo time, você precisará especificar o horário e o fuso horário. No entanto, se o atributo personalizado ou variável de contexto for uma string "irrelevante" (como "product_name"), o usuário sairá do Canvas.
{% endalert %}

#### Caso de uso {#use-case}

Digamos que você quer lembrar seus clientes de comprar pasta de dente daqui a 30 dias. Usando uma combinação de uma etapa de Context e uma etapa de postergação, você pode selecionar essa variável de contexto para postergar. Nesse caso, sua etapa de Context teria os seguintes campos:

- **Nome da variável de contexto:** product_reminder_interval
- **Tipo de dados:** Time
- **Valor:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![O "product_reminder_interval" e seu valor.]({% image_buster /assets/img/context_step1.png %})

Em seguida, como você quer lembrar seus clientes daqui a 30 dias, selecione **Até um dia específico** como opção de postergação e selecione **Personalizar postergação** para usar as informações da sua etapa de Context. Isso significa que seus usuários serão postergados até a variável de contexto selecionada.

## Análise de dados de postergação {#delay-analytics}

Os componentes de postergação têm as seguintes métricas disponíveis na visualização de análise de dados de um Canvas ativo ou anteriormente ativo.

| Métrica | Descrição |
|---|---|
| _Entradas_ | Reflete o número de vezes que a etapa foi acessada. Se o seu Canvas tiver reelegibilidade e um usuário entrar em uma etapa de postergação duas vezes, duas entradas serão registradas. |
| _Avançaram para a próxima etapa_ | Reflete o número de entradas que avançaram para a próxima etapa no Canvas. |
| _Saíram do Canvas_ | Reflete o número de entradas que saíram do Canvas e não avançaram para a próxima etapa. |
| _Falha na personalização_ | Reflete o número de vezes que uma mensagem ou conteúdo personalizado destinado a um usuário não pôde ser entregue devido ao seguinte:<br> {::nomarkdown}<ul><li>O valor da postergação está no passado</li><li>O valor da postergação está mais de 2 anos no futuro</li><li>O valor de <b>Após uma duração</b> não é um número</li><li>O valor de <b>Até um dia específico</b> não é uma data ou string formatada como data</li></ul>{:/} <br>Consulte [Erros de falha na personalização](#personaliztion-failed-errors) para mais informações. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Análise de dados de postergação" }

As séries temporais dessas análises estão disponíveis na visualização expandida do componente.

## Solução de problemas {#troubleshooting}

### Erros de falha na personalização {#personaliztion-failed-errors}

Se os usuários não estiverem acionando uma postergação personalizada, pode ser porque a etapa de Context que você configurou para qualificá-los para a etapa de postergação não está funcionando como esperado. Quando uma [variável de contexto é inválida]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#troubleshooting), o usuário continuará pelo Canvas sem ter seu contexto definido pela etapa de Context. Isso pode fazer com que eles não se qualifiquem para etapas posteriores no Canvas, como postergações personalizadas.

### Usuários em uma etapa de postergação quando um Canvas é interrompido

Quando você [interrompe um Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#stopping-canvases), os usuários que já estão aguardando em uma etapa de postergação não são removidos imediatamente. A Braze ainda agenda a conclusão da postergação, mas **nenhuma mensagem adicional é enviada** enquanto o Canvas estiver interrompido.

Se você reativar o Canvas antes que a postergação de um usuário termine, ele poderá avançar para a próxima etapa conforme programado. Se o período de postergação já tiver passado enquanto o Canvas estava interrompido, esses usuários sairão do Canvas em vez de receber a próxima etapa. Para ver exemplos, consulte [O que acontece quando você interrompe um Canvas?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas) e [Interrompendo Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#stopping-canvases).