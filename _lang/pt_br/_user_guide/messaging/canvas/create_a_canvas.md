---
nav_title: Criar um Canvas
article_title: Criar um Canvas
page_order: 1
description: "Saiba como criar e lançar um Canvas: configure os dados básicos, cronograma de entrada, público-alvo, configurações de envio, monte sua jornada e muito mais."
tool: Canvas
search_rank: 1
---

# Criar um Canvas {#create-a-canvas}

> Este artigo de referência aborda as etapas necessárias para criar, manter e testar um Canvas. Siga este guia ou confira nosso [curso do Braze Learning sobre Canvas](https://learning.braze.com/quick-overview-canvas-setup). Você também pode começar a partir de um [modelo de Canvas da Braze]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates/) para agilizar sua configuração. Para saber mais, consulte [Modelos de Canvas]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/).

{% details Expandir para ver detalhes do editor original do Canvas %}
Não é mais possível criar ou duplicar Canvas usando a experiência original do Canvas. A Braze recomenda [clonar seus Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/) para o editor mais recente.
{% enddetails %}

## Etapa 1: Configurar um novo Canvas {#step-1-set-up-a-new-canvas}

Primeiro, acesse **Messaging** > **Canvas** e selecione **Create Canvas**.

O criador de Canvas vai guiar você passo a passo pela configuração do seu Canvas — desde dar um nome até definir eventos de conversão e trazer os usuários certos para sua jornada. Selecione cada uma das abas a seguir para ver quais configurações você pode ajustar em cada etapa do criador.

{% tabs local %}
  {% tab Basics %}
    Aqui, você vai configurar os dados básicos do seu Canvas:
    - Dê um nome ao seu Canvas
    - Adicione equipes
    - Adicione tags
    - Atribua eventos de conversão e escolha seus tipos de evento e prazos

    Saiba mais sobre a [etapa Dados básicos](#step-11-start-with-your-canvas-basics).
  {% endtab %}
  {% tab Entry Schedule %}
    Aqui, você vai decidir como e quando seus usuários entrarão no Canvas:
    - Agendado: Esta é uma entrada no Canvas baseada em tempo
    - Baseada em ação: Seu usuário entrará no Canvas após realizar uma ação definida
    - Disparada por API: Use uma solicitação de API para inserir usuários no seu Canvas

    Saiba mais sobre a [etapa Cronograma de entrada](#step-12-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Target Audience %}
    Aqui, você vai selecionar seu público-alvo:
    - Crie seu público adicionando segmentos e filtros
    - Ajuste a reentrada e os limites de entrada do Canvas
    - Veja um resumo do seu público-alvo

    Saiba mais sobre a [etapa Público-alvo](#step-13-set-your-target-entry-audience).
  {% endtab %}
  {% tab Send Settings %}
    Aqui, você vai selecionar as configurações de envio do Canvas:
    - Selecione suas configurações de inscrição
    - Defina um limite de taxa de envio para as mensagens do Canvas
    - Ative e configure o horário de silêncio

    Saiba mais sobre a [etapa Configurações de envio](#step-14-select-your-send-settings).
  {% endtab %}
  {% tab Build Canvas %}
    Aqui, você vai montar seu Canvas.

    Saiba como [montar seu Canvas](#step-2-build-your-canvas) usando o criador de Canvas.
  {% endtab %}
  {% tab Summary %}
    Aqui, você encontrará o resumo dos detalhes do seu Canvas. Se o [fluxo de aprovação do Canvas]({{site.baseurl}}/user_guide/messaging/governance/approvals/) estiver ativado, você poderá aprovar os detalhes listados do Canvas antes do lançamento.

  {% endtab %}
{% endtabs %}

### Etapa 1.1: Comece com os dados básicos do Canvas {#step-11-start-with-your-canvas-basics}

Aqui, você vai dar um nome ao Canvas, atribuir [Equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams/#teams) e criar ou adicionar [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/#tags). Você também pode atribuir eventos de conversão para o Canvas.

{% alert tip %}
Adicione tags aos seus Canvas para facilitar a busca e a criação de relatórios. Por exemplo, ao usar o [Criador de relatórios]({{site.baseurl}}/user_guide/analytics/reports/report_builder/), você pode filtrar por tags específicas.
{% endalert %}

![A página de detalhes do Canvas, com campos para nome, descrição, local e tags do Canvas.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

#### Escolha os eventos de conversão {#choose-conversion-events}

Escolha o tipo de evento de conversão e selecione as conversões a serem registradas. Esses [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) medirão a eficiência do seu Canvas.

![Evento de conversão primária A com o tipo de evento de conversão Realiza compra para registrar conversões de usuários que fazem qualquer compra dentro de um prazo de conversão de três dias.]({% image_buster /assets/img/add_canvas_conversions.png %})

Se o seu Canvas tiver múltiplas variantes ou um grupo de controle, a Braze usará esse evento de conversão para determinar a melhor variação para atingir essa meta de conversão. Usando a mesma lógica, você pode criar múltiplos eventos de conversão.

### Etapa 1.2: Determine o cronograma de entrada do Canvas {#step-12-determine-your-canvas-entry-schedule}

Você pode escolher uma das três formas pelas quais os usuários podem entrar no Canvas.

#### Tipos de cronograma de entrada {#entry-schedule-types}

{% tabs local %}
{% tab Scheduled Delivery %}
Com a entrega agendada, os usuários entrarão em um cronograma de tempo, de forma semelhante a como você agendaria uma Campaign. Você pode inscrever usuários em um Canvas assim que ele for lançado, inseri-los na jornada em algum momento no futuro ou de forma recorrente (diária, semanal ou mensal).

Se você selecionar um cronograma recorrente mensal, observe que alguns meses podem não ter o dia selecionado. Por exemplo, digamos que você configure um Canvas para enviar mensalmente no dia 31. Nesse cenário, a Braze envia no último dia daquele mês, como 30 de abril, porque 31 de abril não existe.

Neste exemplo, com base nas opções de tempo, os usuários entram neste Canvas toda terça-feira às 12h no fuso horário local, toda semana, começando em 14 de novembro de 2025 até 31 de dezembro de 2025.

![A página "Cronograma de entrada" com o tipo definido como "Agendado". Devido à seleção, são exibidas opções baseadas em tempo, incluindo frequência, horário de início, recorrência, dias e mais.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})

Ao usar a entrega no fuso horário local, a Braze avalia a elegibilidade de entrada duas vezes: primeiro no horário de Samoa (UTC+13) no dia agendado, e novamente no fuso horário local do usuário. O usuário precisa ser elegível em ambas as verificações para entrar no Canvas. Se seus filtros de entrada usam janelas de tempo relativas (por exemplo, "mais de 2 dias atrás"), o período de 24 horas pode não ter se passado no momento da primeira verificação, fazendo com que os usuários entrem um dia atrasados. Para evitar isso, use uma janela de tempo mais ampla, como pelo menos dois dias. Para mais detalhes, consulte [Quando a Braze avalia os usuários para entrega no fuso horário local?]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#when-does-braze-evaluate-users-for-local-time-zone-delivery)
{% endtab %}
{% tab Action-Based Delivery %}
Com a entrega baseada em ação, os usuários entrarão no Canvas e começarão a receber mensagens quando realizarem ações específicas, como abrir o app, fazer uma compra ou disparar um evento personalizado.

Você pode controlar outros aspectos do comportamento do Canvas na janela **Público de entrada**, incluindo regras de reelegibilidade e configurações de limite de frequência. Observe que a entrega baseada em ação não está disponível para componentes do Canvas com mensagens no app.

![Um exemplo de entrega baseada em ação. Os usuários entrarão no Canvas se fizerem uma compra, com uma janela de entrada começando às 13h30 em 10 de junho de 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

{% alert important %}
Se o seu Canvas baseado em ação enviar mensagens antes do esperado, verifique se o timestamp do evento personalizado está sendo enviado com o horário atual em vez de um horário retroativo. Por exemplo, se um Canvas baseado em ação tem uma postergação de três horas após o usuário realizar um evento personalizado, a Braze usa o timestamp enviado com o evento personalizado para avaliar essa postergação. Se o timestamp estiver retroativo em mais de três horas, a Braze tratará a postergação como já decorrida e enviará a mensagem imediatamente.
{% endalert %}
{% endtab %}
{% tab API-Triggered Delivery %}
Com a entrega disparada por API, os usuários entrarão no Canvas e começarão a receber mensagens após serem adicionados usando o [endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) via API. No dashboard, você pode encontrar um exemplo de solicitação cURL que faz isso, além de atribuir [`context`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) opcional usando o [objeto de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/).

![Um exemplo de entrega disparada por API com um ID do Canvas e um exemplo de solicitação cURL.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

Você pode usar os seguintes endpoints para entrega disparada por API:
- [POST: Enviar mensagens do Canvas via entrega disparada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
- [POST: Agendar Canvas disparados por API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
- [POST: Atualizar Canvas agendados disparados por API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)
{% endtab %}
{% endtabs %}

Após selecionar seu método de entrega, ajuste as configurações de acordo com seu caso de uso e continue para definir seu público-alvo.

{% details Comportamento de deduplicação para Canvas usando o editor original %}
Se a janela de reelegibilidade for menor que a duração máxima do Canvas, um usuário poderá reentrar e receber mensagens de mais de um componente. No caso extremo em que a reentrada de um usuário alcança o mesmo componente da entrada anterior, a Braze deduplicará as mensagens desse componente.

Se um usuário reentrar no Canvas, alcançar o mesmo componente da entrada anterior e for elegível para uma mensagem no app em cada entrada, o usuário receberá a mensagem duas vezes (dependendo da prioridade da mensagem no app), desde que reabra uma sessão duas vezes.
{% enddetails %}

### Etapa 1.3: Defina seu público-alvo de entrada {#step-13-set-your-target-entry-audience}

Somente os usuários que correspondem aos critérios definidos podem entrar na jornada na etapa **Público-alvo**. Isso significa que a Braze avalia a elegibilidade do público-alvo primeiro, **antes** de os usuários entrarem na jornada do Canvas. Por exemplo, se você quiser direcionar novos usuários, pode selecionar um segmento de usuários que usaram seu app pela primeira vez há menos de uma semana.

Em **Controles de entrada**, você pode limitar o número de usuários toda vez que o Canvas for agendado para execução. Para Canvas baseados em disparo por API e baseados em ação, esse limite ocorre a cada hora UTC.

{% multi_lang_include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

#### Testando seu público {#testing-your-audience}

Após adicionar segmentos e filtros ao seu público-alvo, você pode testar se o público está configurado conforme esperado [buscando um usuário]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/) para confirmar se ele corresponde aos critérios do público.

![O campo "Busca de usuário", que permite pesquisar por ID de usuário externo ou ID da Braze.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Selecionando controles de entrada {#selecting-entry-controls}

Os controles de entrada determinam se os usuários podem reentrar em um Canvas. Você também pode limitar o número de pessoas que potencialmente entrariam neste Canvas por uma cadência selecionada, dependendo do tipo de cronograma de entrada:

- **Agendado:** Tempo de vida do Canvas ou toda vez que o Canvas for agendado
- **Baseado em ação:** Por hora, diariamente ou tempo de vida do Canvas
- **Disparado por API:** Por hora, diariamente ou tempo de vida do Canvas

Por exemplo, se você tem um Canvas baseado em ação e seleciona **Limitar volume de entrada** e define o campo **Máximo de entradas** como 5.000 usuários com **Diariamente** como cadência limite, então o Canvas envia para apenas 5.000 usuários por dia.

![A página "Controles de entrada" exibindo caixas de seleção para "Permitir que usuários reentrem no Canvas" e "Limitar volume de entrada". A última permite definir o máximo de entradas e escolher uma cadência que depende do tipo de cronograma de entrada (por exemplo, tempo de vida do Canvas ou toda vez que o Canvas for agendado para entrada agendada, e por hora, diariamente ou tempo de vida do Canvas para entrada baseada em ação e disparada por API).]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
A Braze não recomenda selecionar **Toda vez que o Canvas for agendado** para aquecimento de IP, pois isso pode levar a volumes de envio aumentados.
{% endalert %}

#### Definindo critérios de saída {#setting-exit-criteria}

Definir os [critérios de saída]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria/) determina quais usuários você deseja que saiam de um Canvas. Se um usuário realizar o evento de exceção ou corresponder aos segmentos e filtros, ele não receberá mais mensagens.

#### Calculando o público-alvo {#calculating-target-population}

Na seção **Público-alvo**, você pode ver um resumo do seu público, como os segmentos selecionados e filtros adicionais, além de um detalhamento de quantos usuários são contatáveis por canal de envio de mensagens. Para calcular o número exato de usuários contatáveis no seu público-alvo em vez da estimativa padrão, selecione [Calcular estatísticas exatas]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#calculating-exact-statistics).

Observe que:

- Calcular estatísticas exatas pode levar alguns minutos para ser executado. Essa função calcula apenas as estatísticas exatas no nível do segmento, não no nível do filtro ou grupo de filtros.
- Enquanto as estatísticas exatas estão sendo carregadas, uma estimativa arredondada pode aparecer. O número exato aparece na seção **Usuários contatáveis** quando carregado. Você pode selecionar **Mostrar estatísticas adicionais** para um detalhamento completo.
- Para segmentos grandes, é normal ver pequenas variações mesmo ao calcular estatísticas exatas. A precisão dessa funcionalidade é esperada em 99,999% ou mais.

Para ver estatísticas adicionais, como a receita média de tempo de vida dos usuários direcionados, selecione **Mostrar estatísticas adicionais**.

![Detalhamento do público-alvo com opção de calcular estatísticas exatas.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

#### Por que a contagem do público-alvo pode diferir da contagem de usuários contatáveis {#why-the-target-audience-count-could-differ-from-the-reachable-users-count}

{% multi_lang_include segments.md section='Differing audience size' %}

### Etapa 1.4: Selecione suas configurações de envio {#step-14-select-your-send-settings}

Selecione **Configurações de envio** para editar suas configurações de inscrição, ativar o limite de taxa e ativar o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/). Ao ativar o [limite de taxa]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#rate-limiting-and-canvas-components) ou o [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping), você pode aliviar a pressão de marketing sobre seus usuários e garantir que não está enviando mensagens em excesso.

Para Canvas direcionados a canais de e-mail e push, você pode querer limitar seu Canvas para que apenas os usuários que fizeram opt-in explicitamente recebam a mensagem (excluindo usuários inscritos ou que cancelaram a inscrição). Por exemplo, digamos que você tenha três usuários com diferentes status de opt-in:

- **Usuário A** está inscrito em e-mail e tem push ativado. Este usuário não recebe o e-mail, mas receberá o push.
- **Usuário B** fez opt-in em e-mail, mas não tem push ativado. Este usuário receberá o e-mail, mas não receberá o push.
- **Usuário C** fez opt-in em e-mail e tem push ativado. Este usuário receberá tanto o e-mail quanto o push.

Para fazer isso, defina as **Configurações de inscrição** para enviar este Canvas para "apenas usuários com opt-in". Essa opção garantirá que apenas usuários com opt-in receberão seu e-mail, e a Braze enviará push apenas para usuários que têm push ativado por padrão.

Essas configurações de inscrição são aplicadas por etapa, ou seja, não há efeito no público de entrada. Portanto, essa configuração é usada para avaliar a elegibilidade de um usuário para receber cada etapa do Canvas.

{% alert important %}
Com essa configuração, não inclua nenhum filtro na etapa **Público-alvo** que limite o público a um único canal (por exemplo, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

Se desejar, especifique o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/) (o período durante o qual suas mensagens não serão enviadas) para o Canvas. Marque **Ativar horário de silêncio** nas **Configurações de envio**. Em seguida, selecione o horário de silêncio no fuso horário local do usuário e qual ação será tomada se a mensagem for disparada durante esse período.

![A página "Horário de silêncio" exibindo uma caixa de seleção para ativar o horário de silêncio. Se ativado, o horário de início, horário de término e comportamento de fallback podem ser definidos.]({% image_buster /assets/img/quiet_hours.png %})

## Etapa 2: Monte seu Canvas {#step-2-build-your-canvas}

{% alert tip %}
Economize tempo e agilize a criação do seu Canvas usando os [modelos de Canvas da Braze]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates/)! Navegue pela nossa biblioteca de modelos pré-construídos para encontrar um que se encaixe no seu caso de uso e personalize-o para atender às suas necessidades específicas. Para saber mais, consulte [Modelos de Canvas]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/).
{% endalert %}

### Etapa 2.1: Adicione uma variante {#step-21-add-a-variant}

![O botão "Adicionar variante" selecionado para mostrar um menu de contexto com a opção "Adicionar variante".]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Selecione **Adicionar variante** e adicione uma nova variante ao seu Canvas. As variantes representam uma jornada que seus usuários percorrerão e podem conter múltiplas etapas e ramificações.

Você pode adicionar variantes adicionais selecionando o botão de mais <i class="fas fa-plus-circle"></i>. Ao adicionar novas variantes, você poderá ajustar como seus usuários serão distribuídos entre elas para comparar e analisar a eficácia de diferentes estratégias de engajamento.

![Dois exemplos de variantes em um Canvas da Braze.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
Por padrão, a atribuição de variante do Canvas é determinada por uma função do ID do usuário e do ID do Canvas, o que significa que um determinado usuário é atribuído de forma consistente à mesma variante ao reentrar, desde que as porcentagens de distribuição de variantes permaneçam inalteradas. Se você ajustar a distribuição de variantes após o lançamento, os usuários podem ser atribuídos a variantes diferentes quando reentrarem no Canvas. <br><br>Se você precisar de controle total sobre a atribuição de variantes que persista mesmo quando a distribuição mudar, pode criar um gerador de números aleatórios usando Liquid, executá-lo no início de cada entrada do usuário no Canvas, armazenar o valor como um atributo personalizado e usar esse atributo para dividir os usuários em ramificações.

{% details Expandir para ver as etapas %}

1. Crie um atributo personalizado para armazenar seu número aleatório. Dê um nome fácil de localizar, como "lottery_number" ou "random_assignment". Você pode criar o atributo [no dashboard]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/) ou por meio de chamadas de API para o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).<br><br>
2. Crie uma Campaign de webhook no início do seu Canvas. Essa Campaign será o meio pelo qual você criará seu número aleatório e o armazenará como um atributo personalizado. Consulte [Criar um webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/#step-1-set-up-a-webhook) para mais informações. Defina a URL para o endpoint `/users/track`.<br><br>
3. Crie o gerador de números aleatórios. Você pode fazer isso com o código [descrito aqui](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486), que aproveita o horário único de entrada de cada usuário para criar um número aleatório. Defina o número resultante como uma variável Liquid dentro da sua Campaign de webhook.<br><br>
4. Formate a chamada `/users/track` na sua Campaign de webhook para que ela defina o atributo personalizado criado na etapa 1 com o número aleatório gerado no perfil do usuário atual. Quando essa etapa for executada, você terá criado com sucesso um número aleatório que muda a cada vez que um usuário entra na sua Campaign.<br><br>
5. Ajuste as ramificações do seu Canvas para que, em vez de serem divididas por variantes escolhidas aleatoriamente, sejam divididas com base em regras de público. Nas regras de público de cada ramificação, defina o filtro de público de acordo com seu atributo personalizado. <br><br>Por exemplo, uma ramificação pode ter "lottery_number é menor que 3" como filtro de público, enquanto outra ramificação pode ter "lottery_number é maior que 3 e menor que 6" como filtro de público.

{% enddetails %}
{% endalert %}

### Etapa 2.2: Adicione etapas ao Canvas {#step-22-add-canvas-steps}

Você pode adicionar mais etapas ao fluxo de trabalho do Canvas arrastando e soltando componentes da barra lateral **Componentes**. Ou selecione o botão de mais <i class="fas fa-plus-circle"></i> para adicionar um componente com o menu pop-up.

{% alert tip %}
Conforme você adiciona mais etapas, pode alterar o nível de zoom para focar nos detalhes ou visualizar toda a jornada do usuário. Aumente o zoom com <kbd>Shift</kbd> + <kbd>+</kbd> ou diminua com <kbd>Shift</kbd> + <kbd>-</kbd>.
{% endalert %}

![A janela de busca de componentes adicionando uma etapa de postergação ao Canvas da Braze.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
Você pode adicionar até 200 etapas em um Canvas. Se o Canvas exceder 200 etapas, podem ocorrer problemas de carregamento.
{% endalert %}

#### Duração máxima {#maximum-duration}

Conforme a jornada do Canvas aumenta em etapas, a duração máxima é o maior tempo possível que um usuário pode levar para concluir este Canvas. Ela é calculada somando as postergações e janelas de disparo de cada etapa para cada variante na jornada mais longa. Por exemplo, se o Canvas tem uma etapa de postergação com uma postergação de 3 dias e uma etapa de mensagem, a duração máxima do Canvas será de 3 dias.

#### Editando uma etapa {#editing-a-step}

Quer editar uma etapa na jornada do usuário? Veja como fazer isso dependendo do fluxo de trabalho do Canvas!

Você pode editar qualquer etapa no fluxo de trabalho do Canvas selecionando qualquer um dos componentes. Por exemplo, digamos que você queira editar sua primeira etapa, um componente de [Postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/), no seu fluxo de trabalho para um dia específico. Selecione a etapa para ver suas configurações e ajuste a postergação para 1º de março. Isso significa que em 1º de março, seus usuários avançarão para a próxima etapa do Canvas.

![Um exemplo de etapa "Postergação" com a postergação definida como "Até um dia específico."]({% image_buster /assets/img_archive/edit_delay_flow.png %})

Ou você pode editar e ajustar rapidamente as **Configurações de ação** da etapa [Jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/) para manter os usuários por um período de tempo. Isso prioriza a próxima jornada deles com base nas ações durante esse período de avaliação.

![A segunda etapa no Canvas, "Configurações de ação", com uma janela de avaliação definida como 1 dia.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Os componentes leves do Canvas permitem uma experiência de edição simples, facilitando o ajuste dos detalhes mais finos do seu Canvas.

#### Mensagens no Canvas {#messages-in-canvas}

Edite as mensagens em um componente do Canvas para controlar as mensagens que uma etapa específica enviará. O Canvas pode enviar mensagens de e-mail, push para celular e web, e webhooks para integração com outros sistemas. De forma semelhante às Campaigns, você pode usar certos modelos [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/) para personalizar suas mensagens.

{% alert tip %}
Você sabia que pode incluir nomes de componentes do Canvas nas suas mensagens e modelos de link?<br>
Use a Liquid tag `campaign.${name}` no Canvas para exibir o nome do componente atual do Canvas.
{% endalert %}

O componente de mensagem gerencia as mensagens enviadas aos usuários. Você pode selecionar seus **Canais de envio de mensagens** e ajustar as **Configurações de entrega** para otimizar o envio de mensagens do Canvas. Para mais detalhes sobre este componente, confira [Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/).

![A etapa "Configurar mensagens", com "Canais de envio de mensagens" selecionado, exibindo a lista de canais de envio de mensagens disponíveis, como push para Android, Content Cards, e-mail e mais.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Selecione **Done** após terminar de configurar o componente do Canvas.

{% tabs local %}
{% tab Canvas Entry Properties %}

O [objeto `context`]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) é configurado na etapa **Cronograma de entrada** da criação de um Canvas e indica o gatilho que insere um usuário em um Canvas. Essas propriedades também podem acessar as propriedades das cargas úteis de entrada em Canvas disparados por API. Observe que o objeto `context` pode ter até 50 KB.

Use o seguinte Liquid ao referenciar essas propriedades criadas ao entrar no Canvas: {% raw %} ``context.${property_name}`` {% endraw %}. Observe que os eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma.

{% raw %}
Por exemplo, considere a seguinte solicitação: `"context" : {"product_name" : "shoes", "product_price" : 79.99}`. Você poderia adicionar a palavra "shoes" a uma mensagem com este Liquid ``{{context.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Event Properties %}
Propriedades de evento são as propriedades definidas por você em eventos personalizados e compras. Essas `event_properties` podem ser usadas em Campaigns com entrega baseada em ação, bem como em Canvas.

No Canvas, propriedades de eventos personalizados e de compra podem ser usadas em Liquid em qualquer etapa de mensagem que siga uma etapa de Jornadas de ação. Use este Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} ao referenciar essas `event_properties`. Esses eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma no componente de mensagem.

Na primeira etapa de mensagem após uma Jornada de ação, você pode usar `event_properties` relacionadas ao evento referenciado nessa Jornada de ação. Você pode ter outras etapas (que não sejam outra Jornada de ação ou etapa de mensagem) entre essa etapa de Jornadas de ação e a etapa de mensagem. Observe que você só terá acesso a `event_properties` se sua etapa de mensagem puder ser rastreada de volta a uma jornada que não seja Restante do público em uma etapa de Jornadas de ação.

{% endtab %}
{% endtabs %}

### Etapa 2.3: Edite as conexões {#step-23-edit-connections}

Para mover uma conexão entre etapas, selecione a seta que conecta os dois componentes e selecione um componente diferente. Para remover a conexão, selecione a seta seguida de **Cancelar conexão** no rodapé do criador de Canvas.

Se uma única variante tiver múltiplas ramificações com o mesmo público e horário de envio, a Braze não garante uma divisão uniforme entre essas ramificações. A distribuição pode favorecer a ramificação que foi criada primeiro. Para uma divisão uniforme, use filtros de [números de bucket aleatórios]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/) em cada ramificação. Para saber mais, consulte [O que acontece se o público e o horário de envio forem idênticos para um Canvas que tem uma variante, mas múltiplas ramificações?]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches).

## Etapa 3: Adicione um grupo de controle {#step-3-add-a-control-group}

Você pode adicionar um grupo de controle ao Canvas selecionando o botão de mais <i class="fas fa-plus-circle"></i> para adicionar uma nova variante.

A Braze rastreará as conversões dos usuários que forem colocados no grupo de controle, embora eles não recebam nenhuma mensagem. Para preservar um teste preciso, rastrearemos o número de conversões das suas variantes e do grupo de controle pelo mesmo período de tempo, conforme mostrado na tela de seleção de eventos de conversão.

Você pode ajustar a distribuição entre suas mensagens clicando duas vezes nos cabeçalhos de **Nome da variante**.

Neste exemplo, temos nosso Canvas dividido em duas variantes. A Variante 1 tem 70% dos usuários. A segunda variante é um grupo de controle com os 30% restantes dos usuários.

![Um exemplo de variante em um Canvas da Braze, onde 70% vão para a "Variante 1", que posterga por 1 dia na primeira etapa e depois envia uma mensagem na segunda etapa. Os outros 30% vão para um "Controle" que não tem etapas subsequentes.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

### Seleção inteligente para Canvas {#intelligent-selection-for-canvas}

Os recursos de Seleção inteligente agora estão disponíveis em Canvas multivariantes. De forma semelhante ao recurso de [Seleção inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/) para Campaigns multivariantes, a Seleção inteligente para Canvas analisa o desempenho de cada variante do Canvas e ajusta a porcentagem de usuários direcionados para cada variante. Essa distribuição é baseada nas métricas de desempenho de cada variante para maximizar o número total esperado de conversões.

Lembre-se de que Canvas multivariantes permitem testar não apenas o texto, mas também o timing e os canais. Por meio da Seleção inteligente, você pode testar Canvas de forma mais eficiente e ter confiança de que seus usuários serão enviados na melhor jornada possível do Canvas.

![A opção "Seleção inteligente" está ativada na página "Editar distribuição de variantes". Conforme analisa e otimiza o Canvas, exibe uma barra horizontal na página dividida em várias seções, cada uma variando em cor e tamanho. Esta é apenas uma representação visual e não corresponde a nenhuma análise de dados específica.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

A Seleção inteligente para Canvas otimiza os resultados do Canvas fazendo ajustes graduais em tempo real na distribuição de usuários direcionados para cada variante. Quando o algoritmo estatístico determina um vencedor decisivo entre suas variantes, ele descartará as variantes com desempenho inferior e direcionará todos os futuros destinatários elegíveis do Canvas para as variantes vencedoras.

Por esse motivo, a Seleção inteligente funciona melhor em Canvas que têm novos usuários entrando com frequência.

## Etapa 4: Salve e lance {#step-4-save-and-launch}

Após terminar de criar seu Canvas, selecione **Launch Canvas** para salvar e lançar seu Canvas. Depois de lançar o Canvas, você poderá ver a análise de dados da sua jornada conforme eles chegam na página **Canvas Details**.

Você também pode salvar seu Canvas como rascunho se precisar voltar a ele depois.

![Um exemplo de Canvas na Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
Precisa fazer edições no Canvas após o lançamento? Você pode! Confira [Editando Canvas após o lançamento]({{site.baseurl}}/post-launch_edits/) para saber mais.
{% endalert %}