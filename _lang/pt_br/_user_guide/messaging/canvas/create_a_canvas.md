---
nav_title: Criar um Canvas
article_title: Criar um Canvas
page_order: 1
description: "Saiba como criar e lançar um Canvas: configure os dados básicos, cronograma de entrada, público-alvo, configurações de envio, monte sua jornada e muito mais."
tool: Canvas
search_rank: 1
---

# Criar um Canvas {#create-a-canvas}

> Este artigo de referência aborda as etapas necessárias para criar, manter e testar um Canvas. Siga este guia ou confira nosso [curso do Braze Learning sobre Canvas](https://learning.braze.com/quick-overview-canvas-setup). Você também pode começar a partir de um [modelo de Canvas da Braze]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) para agilizar sua configuração. Para saber mais, consulte [Modelos de Canvas]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates). Para rascunhar um Canvas a partir de uma descrição em linguagem natural, pergunte ao [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#canvases).

{% details Expandir para ver detalhes do editor original do Canvas %}
Não é mais possível criar ou duplicar Canvas usando a experiência original do Canvas. A Braze recomenda [clonar seus Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases) para o editor mais recente.
{% enddetails %}

## Etapa 1: Configurar um novo Canvas {#step-1-set-up-a-new-canvas}

Primeiro, acesse **Messaging** > **Canvas** e selecione **Create Canvas**.

O criador de Canvas guiará você passo a passo pela configuração do seu Canvas — desde nomeá-lo até definir eventos de conversão e trazer os usuários pretendidos para a jornada do cliente. Selecione cada uma das guias a seguir para ver quais configurações podem ser ajustadas em cada etapa do criador.

{% tabs local %}
  {% tab Básico %}
    Aqui, você configurará o básico do seu Canvas:
    - Nomeie seu Canvas
    - Adicione equipes
    - Adicione tags
    - Atribua eventos de conversão e escolha seus tipos de evento e prazos

    Saiba mais sobre a [etapa Básico](#step-11-start-with-your-canvas-basics).
  {% endtab %}
  {% tab Cronograma de entrada %}
    Aqui, você decidirá como e quando seus usuários entrarão no Canvas:
    - Agendado: Trata-se de uma entrada no Canvas baseada em tempo
    - Baseada em ação: Seu usuário entrará no Canvas após realizar uma ação definida
    - Disparada por API: Use uma requisição de API para inserir usuários no seu Canvas

    Saiba mais sobre a [etapa Cronograma de entrada](#step-12-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Público-alvo %}
    Aqui, você selecionará seu público-alvo:
    - Crie seu público adicionando Segments e filtros
    - Ajuste a reentrada e os limites de entrada no Canvas
    - Veja um resumo do seu público-alvo

    Saiba mais sobre a [etapa Público-alvo](#step-13-set-your-target-entry-audience).
  {% endtab %}
  {% tab Configurações de envio %}
    Aqui, você selecionará as configurações de envio do Canvas:
    - Selecione suas configurações de inscrição
    - Defina um limite de frequência para as mensagens do Canvas
    - Ative e configure o horário de silêncio

    Saiba mais sobre a [etapa Configurações de envio](#step-14-select-your-send-settings).
  {% endtab %}
  {% tab Criar Canvas %}
    Aqui, você criará seu Canvas.

    Saiba como [criar seu Canvas](#step-2-build-your-canvas) usando o criador de Canvas.
  {% endtab %}
  {% tab Resumo %}
    Aqui, você encontrará o resumo dos detalhes do seu Canvas. Se o [fluxo de aprovação do Canvas]({{site.baseurl}}/user_guide/messaging/governance/approvals) estiver ativado, você pode aprovar os detalhes listados do Canvas antes do lançamento.

  {% endtab %}
{% endtabs %}

### Etapa 1.1: Comece com o básico do Canvas {#step-11-start-with-your-canvas-basics}

Aqui, você nomeará seu Canvas, atribuirá [Equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e criará ou adicionará [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags). Você também pode atribuir eventos de conversão para o Canvas.

{% alert tip %}
Marque seus Canvas com tags para que sejam fáceis de encontrar e gerar relatórios. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder), você pode filtrar por tags específicas.
{% endalert %}

![A página de detalhes do Canvas, com campos para nome, descrição, local e tags do Canvas.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

#### Escolher eventos de conversão {#choose-conversion-events}

Escolha o tipo de evento de conversão e selecione as conversões a serem registradas. Esses [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) medirão a eficiência do seu Canvas.

![Evento de conversão primária A com o tipo de evento de conversão Realiza compra para registrar conversões de usuários que realizam qualquer compra dentro de um prazo de conversão de três dias.]({% image_buster /assets/img/add_canvas_conversions.png %})

Se o seu Canvas tiver múltiplas variantes ou um grupo de controle, a Braze usará esse evento de conversão para determinar a melhor variação para atingir essa meta de conversão. Usando a mesma lógica, você pode criar múltiplos eventos de conversão.

### Etapa 1.2: Determine o cronograma de entrada do Canvas {#step-12-determine-your-canvas-entry-schedule}

Você pode escolher uma das três formas pelas quais os usuários podem entrar no seu Canvas.

#### Tipos de cronograma de entrada {#entry-schedule-types}

{% tabs local %}
{% tab Entrega agendada %}
Com a entrega agendada, os usuários entrarão em um cronograma baseado em tempo, de forma semelhante a como você agendaria uma campanha. Você pode inscrever usuários em um Canvas assim que ele for lançado, inseri-los na jornada em algum momento futuro, ou de forma recorrente (diária, semanal ou mensal).

Se você selecionar um cronograma recorrente mensal, observe que alguns meses podem não ter o dia selecionado. Por exemplo, digamos que você configure um Canvas para enviar mensalmente no dia 31. Nesse cenário, a Braze envia no último dia daquele mês, como 30 de abril, já que 31 de abril não existe.

Neste exemplo, com base nas opções baseadas em tempo, os usuários entram neste Canvas toda terça-feira às 12h no fuso local, toda semana, começando em 14 de novembro de 2025 até 31 de dezembro de 2025.

![A página "Cronograma de entrada" com o tipo definido como "Agendado". Devido à seleção, são exibidas opções baseadas em tempo, incluindo frequência, horário de início, recorrência, dias e mais.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})

Ao usar entrega no fuso local, a Braze avalia a elegibilidade de entrada duas vezes: primeiro no horário de Samoa (UTC+13) no dia agendado, e novamente no fuso local do usuário. Um usuário deve ser elegível em ambas as verificações para entrar no Canvas. Se seus filtros de entrada usam intervalos de tempo relativos (por exemplo, "há mais de 2 dias"), o período de 24 horas pode não ter decorrido no momento da primeira verificação, fazendo com que os usuários entrem um dia atrasados. Para evitar isso, use um intervalo de tempo mais amplo, como pelo menos dois dias. Para saber mais, consulte [Quando a Braze avalia os usuários para entrega no fuso local?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery)
{% endtab %}
{% tab Entrega baseada em ação %}
Com a entrega baseada em ação, os usuários entrarão no Canvas e começarão a receber mensagens quando realizarem ações específicas, como abrir o app, fazer uma compra ou disparar um evento personalizado.

Você pode controlar outros aspectos do comportamento do Canvas na janela **Público de entrada**, incluindo regras de reelegibilidade e configurações de limite de frequência. Observe que a entrega baseada em ação não está disponível para componentes do Canvas com mensagens no app.

![Um exemplo de entrega baseada em ação. Os usuários entrarão no Canvas se realizarem uma compra com uma janela de entrada começando às 13h30 em 10 de junho de 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

{% alert note %}
**Interagir com etapa do Canvas** não está disponível como disparador de entrada baseada em ação para Canvas. Só pode ser usado como disparador para Campaigns. Para disparar um Canvas a partir de outro, use o componente de Canvas [Enviar para destino]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination), ou crie um [webhook Braze-para-Braze]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook#trigger-a-second-canvas-from-an-initial-canvas) que chame o endpoint `/canvas/trigger/send`.
{% endalert %}

{% alert important %}
Se o seu Canvas baseado em ação envia mensagens antes do esperado, verifique se o timestamp do evento personalizado está sendo enviado com a hora atual, e não com uma hora retroativa. Por exemplo, se um Canvas baseado em ação tem uma postergação de três horas após o usuário realizar um evento personalizado, a Braze usa o timestamp enviado com o evento personalizado para avaliar essa postergação. Se o timestamp for retroativo em mais de três horas, a Braze trata a postergação como já decorrida e envia a mensagem imediatamente.
{% endalert %}
{% endtab %}
{% tab Entrega disparada por API %}
Com a entrega disparada por API, os usuários entrarão no seu Canvas e começarão a receber mensagens após serem adicionados usando o [endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) via API. No dashboard, você pode encontrar um exemplo de requisição cURL que faz isso, bem como atribuir [`context`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) opcional usando o [objeto de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context).

![Um exemplo de entrega disparada por API com um ID do Canvas e um exemplo de requisição cURL.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

Você pode usar os seguintes endpoints para entrega disparada por API:
- [POST: Enviar mensagens de Canvas via entrega disparada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [POST: Agendar Canvas disparados por API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)
- [POST: Atualizar Canvas agendados disparados por API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases)
{% endtab %}
{% endtabs %}

Após selecionar seu método de entrega, ajuste as configurações para corresponder ao seu caso de uso e prossiga para definir seu público-alvo.

{% details Comportamento de deduplicação para Canvas usando o editor original %}
Se a janela de reelegibilidade for menor que a duração máxima do Canvas, um usuário poderá reentrar e receber as mensagens de mais de um componente. No caso extremo em que a reentrada de um usuário alcance o mesmo componente da entrada anterior, a Braze deduplicará as mensagens desse componente.

Se um usuário reentrar no Canvas, alcançar o mesmo componente da entrada anterior e for elegível para uma mensagem no app em cada entrada, o usuário receberá a mensagem duas vezes (dependendo da prioridade da mensagem no app), desde que ele reabra uma sessão duas vezes.
{% enddetails %}

### Etapa 1.3: Defina seu público de entrada {#step-13-set-your-target-entry-audience}

Somente os usuários que correspondam aos critérios definidos poderão entrar na jornada na etapa **Público-alvo**, ou seja, a Braze avalia a elegibilidade do público-alvo primeiro, **antes** de os usuários entrarem na jornada do Canvas. Por exemplo, se você quiser direcionar novos usuários, pode selecionar um Segment de usuários que usaram seu app pela primeira vez há menos de uma semana.

{% alert important %}
Em espaços de trabalho com múltiplos apps, a elegibilidade do público de entrada do Canvas (incluindo Segments e filtros) é avaliada somente quando os usuários entram no Canvas, não nas etapas de Mensagem individuais. Se seu espaço de trabalho tem múltiplos apps e você precisa garantir que as etapas de mensagem direcionem apenas usuários de um app específico, use uma das seguintes abordagens em cada etapa de Mensagem:
- Ative **Validar público no envio da mensagem** nas [validações de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) da etapa de Mensagem e adicione Segments ou filtros específicos do app.
- Use Liquid para verificar o dispositivo ou app de destino no momento do envio.

Sem essas proteções, usuários que se qualificaram para a jornada em um app podem receber mensagens destinadas a outro app se também usarem outros apps no seu espaço de trabalho.
{% endalert %}

Em **Controles de entrada**, você pode limitar o número de usuários cada vez que o Canvas for agendado para execução. Para Canvas baseados em disparador de API e em ação, esse limite ocorre a cada hora UTC.

{% multi_lang_include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

#### Testando seu público {#testing-your-audience}

Após adicionar Segments e filtros ao seu público-alvo, você pode testar se o público está configurado conforme o esperado [pesquisando um usuário]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) para confirmar se ele corresponde aos critérios do público.

![O campo "Pesquisa de usuário", que permite pesquisar por ID de usuário externo ou ID da Braze.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Selecionando controles de entrada {#selecting-entry-controls}

Os controles de entrada determinam se os usuários podem reentrar em um Canvas. Você também pode limitar o número de pessoas que potencialmente entrariam neste Canvas por uma cadência selecionada, dependendo do tipo de cronograma de entrada:

- **Agendado:** Tempo de vida do Canvas ou a cada vez que o Canvas for agendado
- **Baseado em ação:** Por hora, diário ou tempo de vida do Canvas
- **Disparado por API:** Por hora, diário ou tempo de vida do Canvas

Por exemplo, se você tem um Canvas agendado e seleciona **Limitar volume de entrada** e define o campo **Máximo de entradas** para 500.000 usuários com **A cada vez que o Canvas for agendado** como cadência limite, então o Canvas envia apenas para 500.000 usuários por envio agendado.

![A página "Controles de entrada" exibindo caixas de seleção para "Permitir que usuários reentrem no Canvas" e "Limitar volume de entrada".]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
A Braze não recomenda selecionar **A cada vez que o Canvas for agendado** para aquecimento de IP, pois isso pode levar a volumes de envio aumentados.
{% endalert %}

#### Definindo critérios de saída {#setting-exit-criteria}

Definir os [critérios de saída]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) determina quais usuários você deseja que saiam de um Canvas. Se um usuário realizar o evento de exceção ou corresponder aos Segments e filtros, ele não receberá mais mensagens.

#### Calculando o público-alvo {#calculating-target-population}

Na seção **Público-alvo**, você pode ver um resumo do seu público, como os Segments selecionados e filtros adicionais, e um detalhamento de quantos usuários são contatáveis por canal de envio de mensagens. Para calcular o número exato de usuários contatáveis no seu público-alvo em vez da estimativa padrão, selecione [Calcular estatísticas exatas]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#calculating-exact-statistics).

Observe que:

- Calcular estatísticas exatas pode levar alguns minutos para ser executado. Essa função calcula as estatísticas exatas apenas no nível do Segment, não no nível do filtro ou grupo de filtros.
- Enquanto as estatísticas exatas estão carregando, uma estimativa arredondada pode aparecer. O número exato aparece na seção **Usuários contatáveis** quando carregado. Você pode selecionar **Mostrar estatísticas adicionais** para um detalhamento completo.
- Para Segments grandes, é normal ver pequenas variações mesmo ao calcular estatísticas exatas. A precisão desse recurso é esperada em 99,999% ou mais.

Para ver estatísticas adicionais, como a receita média de tempo de vida dos usuários direcionados, selecione **Mostrar estatísticas adicionais**.

![Detalhamento do público-alvo com opção de calcular estatísticas exatas.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

#### Por que a contagem do público-alvo pode diferir da contagem de usuários contatáveis {#why-the-target-audience-count-could-differ-from-the-reachable-users-count}

{% multi_lang_include audience/segments.md section='Differing audience size' %}

### Etapa 1.4: Selecione suas configurações de envio {#step-14-select-your-send-settings}

Selecione **Configurações de envio** para editar suas configurações de inscrição, ativar o limite de frequência e ativar o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours). Ao ativar o [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting) ou o [limite de frequência de mensagens]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping), você pode aliviar a pressão de marketing sobre seus usuários e garantir que não está enviando mensagens em excesso.

Para Canvas direcionados a canais de e-mail e push, você pode querer limitar seu Canvas para que apenas os usuários que aceitaram explicitamente recebam a mensagem (excluindo usuários inscritos ou cancelados). Por exemplo, digamos que você tem três usuários com diferentes status de aceitação:

{% multi_lang_include messaging/intelligent_channel_user_examples.md %}

Para fazer isso, defina as **Configurações de inscrição** para enviar este Canvas apenas para "usuários que aceitaram". Essa opção garante que apenas os usuários que aceitaram receberão seu e-mail, e a Braze enviará push apenas para usuários que estejam habilitados para push por padrão.

Essas configurações de inscrição são aplicadas por etapa, o que significa que não há efeito no público de entrada. Portanto, essa configuração é usada para avaliar a elegibilidade de um usuário para receber cada etapa do Canvas.

{% alert important %}
Com essa configuração, não inclua nenhum filtro na etapa **Público-alvo** que limite o público a um único canal (por exemplo, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

Você pode optar por especificar o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) (o período durante o qual suas mensagens não são enviadas) para o seu Canvas. Marque **Ativar horário de silêncio** nas **Configurações de envio**. Em seguida, selecione seu horário de silêncio no fuso local do usuário e se a mensagem deve ser interrompida ou enviada no próximo horário disponível.

Quando **Enviar no próximo horário disponível** estiver selecionado, o horário de silêncio suprime a mensagem e a envia no próximo horário disponível fora do período de silêncio. Por exemplo, digamos que o horário de silêncio está configurado para impedir o envio de mensagens entre 11h30 e 14h30 no fuso local do usuário, e um usuário entra em uma etapa de Mensagem às 11h35. Como esse horário está dentro do período de silêncio, a mensagem ainda não é enviada, e o usuário recebe a etapa de Mensagem às 14h30, que é após o horário de silêncio.

![A página "Horário de silêncio" exibindo uma caixa de seleção para ativar o horário de silêncio. Se ativado, o horário de início, horário de término e comportamento de fallback podem ser configurados.]({% image_buster /assets/img/quiet_hours.png %})

## Etapa 2: Crie seu Canvas {#step-2-build-your-canvas}

{% alert tip %}
Economize tempo e simplifique a criação do seu Canvas usando os [modelos de Canvas da Braze]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates)! Navegue pela nossa biblioteca de modelos pré-construídos para encontrar um que se encaixe no seu caso de uso e personalize-o para atender às suas necessidades específicas. Para saber mais, consulte [Modelos de Canvas]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates).
{% endalert %}

### Etapa 2.1: Adicione uma variante {#step-21-add-a-variant}

![O botão "Adicionar variante" selecionado mostrando um menu de contexto com a opção "Adicionar variante".]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Selecione **Adicionar variante** e, em seguida, adicione uma nova variante ao seu Canvas. As variantes representam uma jornada que seus usuários seguirão e podem conter múltiplas etapas e ramificações.

Você pode adicionar variantes adicionais selecionando o botão de mais <i class="fas fa-plus-circle"></i>. Quando você adicionar novas variantes, poderá ajustar como seus usuários serão distribuídos entre elas para que você possa comparar e analisar a eficácia de diferentes estratégias de engajamento.

![Dois exemplos de variantes em um Canvas da Braze.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
Por padrão, a atribuição de variante do Canvas é determinada por um hash determinístico do ID do usuário e do ID do Canvas (não pelo [número de bucket aleatório]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) do usuário), o que significa que um determinado usuário é consistentemente atribuído à mesma variante em reentradas, desde que os percentuais de distribuição de variantes permaneçam inalterados. Se você ajustar a distribuição de variantes após o lançamento, os usuários podem ser atribuídos a variantes diferentes quando reentrarem no Canvas. <br><br>Se você precisa de uma atribuição que permaneça fixa quando os percentuais de distribuição mudam, use uma única variante de Canvas e direcione os usuários com uma etapa de [jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths). No início da jornada, use uma etapa de [Atualização do usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) para armazenar um número aleatório em um atributo personalizado e, em seguida, filtre por esse atributo nas jornadas do público.

{% details Expandir para ver as etapas %}

1. Crie um atributo personalizado do tipo **Number** para armazenar seu número aleatório. Dê um nome fácil de localizar, como `lottery_number` ou `random_assignment`. No seu dashboard, acesse **Data Settings** > **Custom Attributes**.<br><br>
2. Use uma única variante de Canvas (ou adicione a mesma etapa de Atualização do usuário a cada variante). Adicione uma etapa de [Atualização do usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) no início da jornada. Essa etapa gera e armazena o número aleatório antes que os usuários alcancem sua etapa de jornadas do público.<br><br>
3. Na etapa de Atualização do usuário, selecione o [Editor JSON avançado]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor). Use a tag {% raw %}{% random %}{% endraw %} para gerar o número. Para mais detalhes, consulte [Enviar mensagens com um número aleatório]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#send-messages-with-a-random-number). Por exemplo, {% raw %}`{% random 10 %}`{% endraw %} retorna um número inteiro de 0 a 9. Defina o atributo personalizado da etapa 1 usando JSON assim:<br><br>{% raw %}
```json
{% if {{custom_attribute.${lottery_number}}} == blank %}
{% capture lottery_number_str %}{% random 10 %}{% endcapture %}
{
  "attributes": [
    {
      "lottery_number": {{ lottery_number_str | plus: 0 }}
    }
  ]
}
{% endif %}
```
{% endraw %}
<br><br>
O bloco {% raw %}`{% if %}`{% endraw %} define o número apenas quando o atributo está vazio, para que os usuários mantenham a mesma atribuição quando reentrarem no Canvas.<br><br>

{: start="4"}
4. Adicione uma etapa de [jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) após a etapa de Atualização do usuário. Em cada grupo de público, adicione filtros baseados no seu atributo personalizado em vez de usar percentuais de distribuição de variantes.<br><br>Por exemplo, se você usou {% raw %}`{% random 10 %}`{% endraw %}, um grupo pode usar `lottery_number` **é menor que 4**, outro **é maior que 3 e menor que 7**, e um terceiro **é maior que 6 e menor que 10**.

{% enddetails %}
{% endalert %}

### Etapa 2.2: Adicione etapas ao Canvas {#step-22-add-canvas-steps}

Você pode adicionar mais etapas ao fluxo de trabalho do seu Canvas arrastando e soltando componentes da barra lateral **Componentes**. Ou selecione o botão de mais <i class="fas fa-plus-circle"></i> para adicionar um componente com o menu popover.

{% alert tip %}
À medida que você começa a adicionar mais etapas, pode alterar o nível de zoom para focar nos detalhes ou visualizar toda a jornada do usuário. Aumente o zoom com <kbd>Shift</kbd> + <kbd>+</kbd> ou diminua com <kbd>Shift</kbd> + <kbd>-</kbd>.
{% endalert %}

![A janela de busca de componentes adicionando uma etapa de postergação ao Canvas da Braze.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
Você pode adicionar até 200 etapas em um Canvas. Se o seu Canvas exceder 200 etapas, podem ocorrer problemas de carregamento.
{% endalert %}

#### Duração máxima {#maximum-duration}

À medida que a jornada do seu Canvas aumenta em etapas, a duração máxima é o maior tempo possível que um usuário pode levar para concluir este Canvas. Isso é calculado somando as postergações e janelas de disparo de cada etapa para cada variante na jornada mais longa. Por exemplo, se o seu Canvas tem uma etapa de postergação com uma postergação de 3 dias e uma etapa de mensagem, a duração máxima do seu Canvas será de 3 dias.

#### Editando uma etapa {#editing-a-step}

Quer editar uma etapa na jornada do seu usuário? Confira como fazer isso dependendo do fluxo de trabalho do seu Canvas!

Você pode editar qualquer etapa no fluxo de trabalho do seu Canvas selecionando qualquer um dos componentes. Por exemplo, digamos que você queira editar sua primeira etapa, um componente de [postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), no seu fluxo de trabalho para um dia específico. Selecione a etapa para visualizar suas configurações e ajuste sua postergação para 1 de março. Isso significa que, em 1 de março, seus usuários avançarão para a próxima etapa do seu Canvas.

![Um exemplo de etapa de "Postergação" com a postergação definida como "Até um dia específico".]({% image_buster /assets/img_archive/edit_delay_flow.png %})

Ou você pode editar e ajustar rapidamente as **Configurações de ação** da sua etapa de [jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) para manter os usuários por um período de tempo. Isso prioriza a próxima jornada deles com base nas ações durante esse período de avaliação.

![A segunda etapa no Canvas, "Configurações de ação", com uma janela de avaliação definida para 1 dia.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Os componentes leves no Canvas permitem uma experiência de edição simples, tornando mais fácil ajustar os detalhes mais específicos do seu Canvas.

#### Mensagens no Canvas {#messages-in-canvas}

Edite as mensagens em um componente do Canvas para controlar as mensagens que uma etapa específica enviará. O Canvas pode enviar e-mail, push para dispositivos móveis e web, e webhooks para integração com outros sistemas. Assim como nas Campaigns, você pode usar certos modelos de [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) para personalizar suas mensagens.

{% alert tip %}
Você sabia que pode incluir nomes de componentes do Canvas nas suas mensagens e modelos de link?<br>
Use a tag Liquid `campaign.${name}` no Canvas para exibir o nome do componente atual do Canvas.
{% endalert %}

O componente de mensagem gerencia as mensagens enviadas aos usuários. Você pode selecionar seus **Canais de envio de mensagens** e ajustar as **Configurações de entrega** para otimizar o envio de mensagens do seu Canvas. Para mais detalhes sobre este componente, confira [Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

![A etapa "Configurar mensagens", com "Canais de envio de mensagens" selecionado, exibindo a lista de canais de envio de mensagens disponíveis, como push Android, Content Cards, e-mail e mais.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Selecione **Concluído** após terminar de configurar seu componente do Canvas.

{% tabs local %}
{% tab Propriedades de entrada do Canvas %}

O [objeto `context`]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) é configurado na etapa **Cronograma de entrada** da criação de um Canvas e indica o gatilho que insere um usuário em um Canvas. Essas propriedades também podem acessar as propriedades das cargas úteis de entrada em Canvas disparados por API. Observe que o objeto `context` pode ter até 50 KB.

Use o Liquid a seguir ao referenciar essas propriedades criadas ao entrar no Canvas: {% raw %} ``context.${property_name}`` {% endraw %}. Observe que os eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma.

{% raw %}
Por exemplo, considere a seguinte requisição: `"context" : {"product_name" : "shoes", "product_price" : 79.99}`. Você pode adicionar a palavra "shoes" a uma mensagem com este Liquid ``{{context.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Propriedades de evento %}
Propriedades de evento são as propriedades definidas por você em eventos personalizados e compras. Essas `event_properties` podem ser usadas em Campaigns com entrega baseada em ação, assim como em Canvas.

No Canvas, propriedades de eventos personalizados e de compra podem ser usadas em Liquid em qualquer etapa de mensagem que segue uma etapa de jornadas de ação. Use este Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} ao referenciar essas `event_properties`. Esses eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma no componente de mensagem.

Na primeira etapa de mensagem após uma jornada de ação, você pode usar `event_properties` relacionadas ao evento referenciado naquela jornada de ação. Você pode ter outras etapas (que não sejam outra etapa de jornadas de ação ou de mensagem) entre essa etapa de jornadas de ação e a etapa de mensagem. Observe que você só terá acesso a `event_properties` se sua etapa de mensagem puder ser rastreada de volta a uma jornada que não seja "Todos os outros" em uma etapa de jornadas de ação.

{% endtab %}
{% endtabs %}

### Etapa 2.3: Edite as conexões {#step-23-edit-connections}

Para mover uma conexão entre etapas, selecione a seta que conecta os dois componentes e selecione um componente diferente. Para remover a conexão, selecione a seta seguida de **Cancelar conexão** no rodapé do criador do Canvas.

Se uma única variante tiver múltiplas ramificações com o mesmo público e horário de envio, a Braze não garante uma divisão uniforme entre essas ramificações. A distribuição pode favorecer a ramificação que foi criada primeiro. Para uma divisão uniforme, use filtros de [número de bucket aleatório]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) em cada ramificação. Para saber mais, consulte [O que acontece se o público e o horário de envio são idênticos para um Canvas que tem uma variante, mas múltiplas ramificações?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches).

## Etapa 3: Adicionar um grupo de controle {#step-3-add-a-control-group}

Você pode adicionar um grupo de controle ao seu Canvas selecionando o botão de mais <i class="fas fa-plus-circle"></i> para adicionar uma nova variante.

A Braze rastreará as conversões dos usuários que forem colocados no grupo de controle, embora eles não recebam nenhuma mensagem. Para preservar um teste preciso, rastrearemos o número de conversões das suas variantes e do grupo de controle pelo mesmo período de tempo, conforme mostrado na tela de seleção de eventos de conversão.

Você pode ajustar a distribuição entre suas mensagens clicando duas vezes nos cabeçalhos de **Nome da variante**.

Neste exemplo, nosso Canvas está dividido em duas variantes. A Variante 1 tem 70% dos usuários. A segunda variante é um grupo de controle com os 30% restantes dos usuários.

![Um exemplo de variante em um Canvas da Braze, onde 70% vão para a "Variante 1", que posterga por 1 dia na primeira etapa e depois envia uma mensagem na segunda etapa. Os outros 30% vão para um "Controle" que não tem nenhuma etapa subsequente.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

### Otimizar variantes do Canvas com BrazeAI {#optimize-canvas-variants-with-brazeai}

Para um Canvas com múltiplas variantes de nível superior, ative **Otimizar com BrazeAI<sup>TM</sup>** para ajustar automaticamente a porcentagem de usuários que entram em cada variante. O BrazeAI<sup>TM</sup> usa o desempenho das variantes para maximizar o número esperado de conversões.

Adicione pelo menos duas variantes e um evento de conversão. Em seguida, selecione uma porcentagem de variante para abrir **Editar distribuição de variantes** e ative **Otimizar com BrazeAI<sup>TM</sup>**.

Após o prazo inicial de conversão, o BrazeAI<sup>TM</sup> analisa o desempenho a cada 12 horas e direciona mais usuários para a variante que gera mais conversões. Quando a otimização identifica um vencedor decisivo, todos os futuros usuários elegíveis entram nessa variante.

Essa otimização funciona melhor para Canvas que recebem novos usuários com frequência.

## Etapa 4: Salvar e lançar {#step-4-save-and-launch}

Depois de criar seu Canvas, selecione **Launch Canvas** para salvar e lançar. Após o lançamento, você poderá visualizar a análise de dados da sua jornada conforme os dados forem chegando na página **Canvas Details**.

Você também pode salvar seu Canvas como rascunho se precisar voltar a ele depois.

![Um exemplo de Canvas na Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
Precisa fazer edições no seu Canvas após o lançamento? Você pode! Confira [Editando Canvas após o lançamento]({{site.baseurl}}/post-launch_edits) para saber mais.
{% endalert %}