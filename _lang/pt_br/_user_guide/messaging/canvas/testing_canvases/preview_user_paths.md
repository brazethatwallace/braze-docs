---
nav_title: Prévia das jornadas do usuário
article_title: Prévia das jornadas do usuário
page_order: 0.3
alias: /preview_user_paths/
description: "Esta página aborda como é possível fazer a prévia das jornadas do usuário no Canvas."
tool:
  - Canvas
---

# Prévia das jornadas do usuário no Canvas {#preview-user-paths-in-canvas}

> Experimente a jornada do Canvas que você criou para seus usuários. Isso inclui visualizar o tempo e as mensagens que seus usuários recebem. Essas execuções de teste funcionam como garantia de qualidade de que suas mensagens são enviadas para o público certo, tudo isso antes de enviar seu Canvas.

## Criando uma execução de teste {#creating-a-test-run}

Siga estas etapas para visualizar a jornada do usuário:

1. Acesse o criador de Canvas. Salve quaisquer alterações não salvas e resolva os erros.
2. Selecione **Test Canvas** no rodapé.
3. Selecione um usuário teste.
4. (Opcional) Selecione um destinatário para o teste.
5. Selecione **Run Test**.

Você pode executar uma prévia mesmo sem ter permissão para editar um Canvas, mas essa prévia será executada com alterações não salvas, caso existam.

### Etapas compatíveis {#supported-steps}

As seguintes etapas são compatíveis:
- Mensagem
- Jornada do público
- Divisão de decisão
- Postergação
- Jornada de ação
- Jornada experimental
- Agente
- Atualização de usuário (somente no editor de interface, ou seja, etapas que usam o editor JSON são ignoradas)

Se o teste se sobrepõe a um tipo de etapa que não está listado nesta seção, a etapa não compatível é ignorada e o usuário teste continua para a próxima etapa compatível.

### Etapas de agente {#agent-steps}

Quando uma execução de teste atinge uma [etapa de agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step), a Braze pausa e pergunta **Deseja executar o agente "{agentName}"?** Escolha como continuar:

- **Yes:** Opcionalmente, adicione contexto no campo de texto (além do perfil do usuário teste e qualquer contexto do Canvas já presente na jornada) e selecione **Simulate response** para invocar o agente. Você pode inserir valores de exemplo em linguagem natural — por exemplo, descrevendo o conteúdo do carrinho ou o texto de uma mensagem recebida — para simular o contexto de tempo de execução que o agente receberia em produção.
- **No:** A Braze não invoca o agente. A etapa usa a **saída de fallback** configurada do agente, na seção **Output** do [Agent Console]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values).

Quando você seleciona **Yes** e **Simulate response**, o agente é executado para o usuário da prévia, armazena sua saída na variável de saída da etapa de agente e o teste continua pela jornada. Invocações de **Simulate response** contam para o limite diário de invocações do agente e aparecem em **Agent Console** > **Logs**.

Para testar uma etapa de agente isoladamente (sem executar todo o caminho do Canvas), use a prévia dentro da etapa no criador de Canvas. Para detalhes de configuração, consulte [Testar o agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#step-5-test-the-agent) em etapa de agente.

Se a sua etapa de agente depende de dados de uma [etapa de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) anterior, execute **Test Canvas** para que as variáveis de contexto sejam preenchidas ao longo do caminho. Grupos de teste não avaliam etapas de contexto nem variáveis de contexto para destinatários de teste.

### Detalhes da etapa do Canvas {#canvas-step-details}

Para visualizar mais detalhes sobre os critérios de entrada, selecione **See more**. Etapas com segmentação mostram os critérios atendidos ou não atendidos. As mensagens também mostram isso para validações de entrega e elegibilidade de canal. Etapas de mensagem mostram quais canais foram enviados e quais não foram.

### Liquid

A Braze processa a lógica Liquid durante uma execução de teste, mesmo que você não esteja enviando uma mensagem de teste real. Isso significa que a [lógica de interrupção de mensagem]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) e outras lógicas Liquid são refletidas e podem impactar a jornada do usuário no Canvas.

Se a sua prévia envia a última etapa da jornada do usuário em vez de interromper, a prévia pode estar usando o horário atual como o horário testado para a avaliação Liquid, e não o horário real em que o usuário estaria na etapa com base no horário de entrada no Canvas.

## Prévias para temporização {#previews-for-timing}

Para Canvas agendados, o usuário teste entra no próximo horário de entrada agendado. Para Canvas baseados em ação com datas de início, o usuário teste entra na data e horário de início.

Embora os horários de início padrão ainda se apliquem, o horário de entrada é configurável em todas as instâncias, o que significa que você pode simular uma data no passado ou no futuro. No entanto, não é possível testar antes da data de início ou após a data de término do Canvas.

As etapas de mensagem e postergação mostram o horário em que um usuário avançaria ou receberia a mensagem sem a necessidade de reconfigurar as postergações. Observe que, embora as etapas indiquem se o Intelligent Timing é utilizado, essa prévia da jornada do usuário não calcula uma estimativa para um usuário teste.

Para Canvas com um disparador de ação como "mudança no valor de atributo personalizado", a Braze tenta simular a mudança definindo temporariamente o atributo do usuário no disparador como vazio **apenas para a execução de teste do Canvas** (isso não afeta o perfil de usuário). O objetivo é testar se o atributo muda em relação ao seu valor atual.

## Quando os usuários entram e saem {#when-users-enter-and-exit}

Os usuários teste entram na prévia mesmo que não sejam elegíveis na vida real. Se não forem elegíveis, você pode ver por que não atenderam aos critérios. Quando um usuário teste entra na prévia, assumimos que ele atendeu aos critérios do público-alvo e realizou a ação dos critérios de disparo. Por exemplo, para um Canvas que usa eventos personalizados nos critérios de entrada, assume-se que o usuário teste realizou o evento personalizado conforme esperado nos critérios de entrada. No entanto, se o mesmo evento personalizado for usado em outro lugar no Canvas (como nos critérios de saída), considere como isso pode impactar a jornada do usuário.

Eventos, disparos de API, atributos personalizados e propriedades de entrada do Canvas que são assumidos como critérios para permitir que um usuário teste entre no Canvas não são atualizados no perfil de usuário real e não persistem além da execução do teste. Por exemplo, durante o teste, quando um atributo personalizado é usado como disparador do Canvas, os critérios de disparo são aplicados à prévia do usuário **como se** ele tivesse disparado a alteração do atributo personalizado.

### Consideração {#consideration}

Se você testar uma jornada de ação com ações que correspondam a critérios de saída (incluindo propriedades de evento), os critérios de saída serão disparados e a execução do teste será encerrada. Se você testar uma etapa de mensagem que corresponda a critérios de saída, os critérios de saída serão disparados e a execução do teste será encerrada.

Neste momento, não é possível selecionar um evento ou propriedade específica dentro de uma jornada de ação para disparar critérios de saída (apenas a jornada como um todo). Se um usuário puder potencialmente atender a múltiplos critérios de saída, o primeiro que for processado e que ele atender será exibido como resultado.

## Jornadas experimentais e variantes do Canvas {#experiment-paths-and-canvas-variants}

- Para Canvas com variantes de nível superior, selecione uma variante no início do teste.
- Para jornadas experimentais, selecione a variante pela qual o usuário progride quando o usuário teste encontra a etapa.
- Para jornadas experimentais que usam Winning Path, a prévia não inclui o período de postergação quando um usuário teste aguarda em uma etapa de mensagem. A Braze assume que o usuário progrediu pela jornada selecionada imediatamente.

## Envios de teste {#test-sends}

Você pode optar por enviar mensagens de teste para um grupo de teste interno ou para um usuário individual à medida que a execução de teste é preenchida. Isso significa que apenas as mensagens que o usuário encontra ao longo da jornada de teste são enviadas. Os destinatários recebem mensagens com seus atributos por padrão, mas você pode substituí-los pelos atributos do usuário teste.

Para enviar todas as mensagens de teste em um Canvas de uma vez, independentemente da jornada, e sem visualizar a jornada, você pode selecionar **Send All Test Messages** na guia **Test Sends**.

## Responsividade {#responsiveness}

As etapas do Canvas são responsivas ao tempo ao visualizar jornadas de usuários. As atualizações feitas pela etapa de Atualização de Usuário são refletidas nas etapas subsequentes do fluxo, mas não são aplicadas ao perfil de usuário real. Os efeitos de um usuário entrar em uma variante são refletidos nas etapas futuras em uma prévia.

Da mesma forma, os filtros reconhecem ações que ocorreram como resultado da interação do usuário teste com outras etapas do Canvas. Por exemplo, esse modo de prévia reconhece que um usuário encontrou uma etapa de Mensagem que foi "enviada" anteriormente no Canvas e reconhece que o usuário teste "realizou uma ação" para avançar por uma jornada de ação.

Consulte [Critérios de saída]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) para mais detalhes sobre o comportamento responsivo.

## Connected Content {#connected-content}

O Connected Content é executado se estiver incluído no Canvas. Isso significa que, se você testar um Canvas que tenha chamadas de Connected Content ou Content Blocks que contenham Connected Content, o Canvas poderá enviar as chamadas de Connected Content, o que modificaria os dados referenciados em outras Campaigns ou Canvas.

Ao visualizar as jornadas dos usuários, considere remover o Connected Content que altera perfis de usuário ou dados referenciados em outros Canvas ou Campaigns.

## Webhooks {#webhooks}

Os webhooks são executados quando mensagens de teste são enviadas, mas não durante a execução do teste. Assim como o Connected Content, considere remover webhooks que alterem perfis de usuário ou dados referenciados em outros Canvas ou Campaigns.

## Variáveis de contexto e grupos de teste {#context-variables-and-seed-groups}

Para uma etapa de Mensagem com e-mail como canal de envio de mensagens, os grupos de teste enviam cópias de teste dos e-mails quando um usuário atinge essa etapa no Canvas. Essas cópias de teste não são enviadas como parte das jornadas do Canvas dos próprios destinatários do grupo de teste, então a Braze não executa [etapas de Contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) nem avalia variáveis de contexto para esses destinatários. Se o conteúdo do seu e-mail faz referência a variáveis de contexto, os destinatários do grupo de teste recebem uma cópia de teste sem esses dados preenchidos. Para testar mensagens que dependem de dados de variáveis de contexto, use a prévia **Test Canvas** com envios de teste em vez de grupos de teste.

## Visualizar mensagens enviadas aos usuários {#view-messages-sent-to-users}

A prévia de jornadas do usuário simula uma jornada; ela não substitui a verificação dos envios reais no perfil de um usuário. Para revisar as mensagens que a Braze enviou a um usuário específico, abra o perfil dele em **Público** > **Pesquisar usuários** e use as guias **Histórico de mensagens** e **Engajamento**.

Para campos de pesquisa, detalhes das guias e a janela de 30 dias do histórico de mensagens, consulte [Perfis de usuário]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles).

## Caso de uso {#use-case}

Neste cenário, o Canvas é configurado para direcionar usuários que não tiveram uma sessão em um app. Essa jornada inclui uma etapa de Mensagem com um e-mail de boas-vindas, uma etapa de Postergação definida para um dia e uma etapa de Jornadas do Público que se divide em dois caminhos: usuários com pelo menos uma sessão e todos os demais. Dependendo de qual jornada do público o usuário se encaixa, a etapa de Mensagem subsequente é enviada.

![Um exemplo de Canvas com uma etapa de Mensagem, etapa de Postergação, etapa de Jornadas do Público e duas etapas de Mensagem.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

Como nosso usuário teste atende aos critérios de entrada do Canvas, ele pode entrar no Canvas e percorrer a jornada do usuário. No entanto, como nosso usuário teste não abriu o app no último dia, ele continua pelo caminho "Todos os demais" e recebe uma notificação por push que diz: "Última chance! Conclua sua primeira tarefa para um bônus exclusivo."

![A seção "Resultados do teste" mostra que o usuário teste atendeu aos critérios de entrada e fornece um resumo da jornada, incluindo quais etapas foram enviadas.]({% image_buster /assets/img/preview_user_path_results_example.png %})