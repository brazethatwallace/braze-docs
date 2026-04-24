---
nav_title: Pré-visualizar jornadas do usuário
article_title: Pré-visualizar jornadas do usuário
page_order: 0.3
alias: /preview_user_paths/
description: "Esta página explica como pré-visualizar jornadas do usuário no Canvas."
Tool:
  - Canvas
---

# Pré-visualizar jornadas do usuário no Canvas

> Experimente a jornada do Canvas que você criou para seus usuários. Isso inclui pré-visualizar o tempo e as mensagens que seus usuários recebem. Essas execuções de teste funcionam como garantia de qualidade de que suas mensagens são enviadas ao público certo, tudo antes de enviar seu Canvas.

## Criando uma execução de teste

Siga estas etapas para pré-visualizar a jornada do usuário:

1. Acesse o criador de Canvas. Salve todas as alterações não salvas e resolva quaisquer erros.
2. Selecione **Test Canvas** no rodapé.
3. Selecione um usuário teste.
4. (Opcional) Selecione um destinatário para o teste.
5. Selecione **Run Test**.

Você pode executar uma pré-visualização mesmo sem permissão para editar um Canvas, mas essa pré-visualização será executada com alterações não salvas, se houver alguma.

### Etapas compatíveis

As seguintes etapas são compatíveis:
- Mensagem
- Jornadas do público
- Divisão de decisão
- Postergação
- Jornada de ação
- Jornadas do experimento
- Atualização de usuário (apenas no editor de interface, ou seja, etapas que usam o editor JSON são ignoradas)

Se o teste se sobrepuser a um tipo de etapa que não está listado acima, a etapa não compatível será ignorada e o usuário teste continuará para a próxima etapa compatível.

### Detalhes da etapa do Canvas

Para ver mais detalhes sobre os critérios de entrada, selecione **See more**. Etapas com segmentação mostram os critérios atendidos ou não atendidos. As mensagens também mostram isso para validações de entrega e elegibilidade de canal. As etapas de mensagem mostram quais canais foram enviados e quais não foram.

### Liquid

A Braze processa a lógica Liquid durante uma execução de teste, mesmo que você não esteja enviando uma mensagem de teste real. Isso significa que a [lógica de cancelamento de mensagem]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/#abort-messages) e outras lógicas Liquid são refletidas e podem impactar a jornada do usuário no Canvas.

Se a sua pré-visualização enviar a última etapa da jornada do usuário em vez de cancelar, a pré-visualização pode estar usando o horário atual como o horário testado para a avaliação Liquid, e não o horário real em que o usuário estaria na etapa com base no horário de entrada no Canvas.

## Pré-visualizações de tempo

Para Canvas agendados, o usuário teste entra no próximo horário de entrada agendado. Para Canvas baseados em ação com datas de início, o usuário teste entra na data e horário de início.

Embora os horários de início padrão ainda se apliquem, o horário de entrada é configurável em todas as instâncias, o que significa que você pode simular uma data no passado ou no futuro. No entanto, não é possível testar antes da data de início ou após a data de término do Canvas.

As etapas de mensagem e postergação mostram o horário em que um usuário avançaria ou receberia a mensagem sem precisar reconfigurar as postergações. Observe que, embora as etapas indiquem se o Intelligent Timing é usado, essa pré-visualização da jornada do usuário não calcula uma estimativa para um usuário teste.

Para Canvas com um gatilho de ação como "mudança no valor de atributo personalizado", a Braze tenta simular a mudança definindo temporariamente o atributo do usuário no gatilho como vazio **apenas para a execução de teste do Canvas** (isso não afeta o perfil do usuário). Isso serve para testar se o atributo muda em relação ao seu valor atual.

## Quando os usuários entram e saem

Os usuários teste entram na pré-visualização mesmo que não sejam elegíveis na vida real. Se não forem elegíveis, você pode ver por que não atenderam aos critérios. Quando um usuário teste entra na pré-visualização, assumimos que ele atendeu aos critérios do público-alvo e realizou os critérios de gatilho de ação. Por exemplo, para um Canvas que usa eventos personalizados nos critérios de entrada, assume-se que o usuário teste realizou o evento personalizado conforme esperado nos critérios de entrada. No entanto, se o mesmo evento personalizado for usado em outro lugar no Canvas (como nos critérios de saída), considere como isso pode impactar a jornada do usuário.

Eventos, gatilhos de API, atributos personalizados e propriedades de entrada do Canvas que são assumidos para permitir que um usuário teste entre no Canvas não são atualizados no perfil real do usuário e não persistem além da execução de teste. Por exemplo, durante o teste, quando um atributo personalizado é usado como gatilho do Canvas, os critérios de gatilho são aplicados à pré-visualização do usuário **como se** ele tivesse disparado a mudança do atributo personalizado.

### Consideração

Se você testar uma jornada de ação com ações que correspondem a critérios de saída (incluindo propriedades de evento), os critérios de saída serão acionados e a execução de teste será encerrada. Se você testar uma etapa de mensagem que corresponde a critérios de saída, os critérios de saída serão acionados e a execução de teste será encerrada.

Neste momento, não é possível selecionar um evento ou propriedade específica dentro de uma jornada de ação para acionar critérios de saída (apenas a jornada como um todo). Se um usuário puder potencialmente atender a múltiplos critérios de saída, o primeiro que for processado e que ele atender será mostrado como resultado.

## Jornadas do experimento e variantes do Canvas

- Para Canvas com variantes de nível superior, selecione uma variante no início do teste.
- Para Jornadas do experimento, selecione a variante pela qual o usuário avança quando o usuário teste encontra a etapa.
- Para Jornadas do experimento usando Jornada personalizada ou Variante vencedora, embora haja um período de espera durante o qual o usuário teste aguarda em uma etapa de mensagem, essa espera não é levada em conta, pois a Braze assume que o usuário avançou pela variante selecionada imediatamente.

## Envios de teste

Você pode optar por enviar mensagens de teste para um grupo de teste interno ou para um usuário individual conforme a execução de teste é preenchida. Isso significa que apenas as mensagens que o usuário encontra ao longo da jornada de teste são enviadas. Os destinatários recebem mensagens com seus próprios atributos por padrão, mas você pode substituí-los pelos atributos do usuário teste.

Para enviar todas as mensagens de teste em um Canvas de uma vez, independentemente da jornada, e sem pré-visualizar a jornada, você pode selecionar **Send All Test Messages** na guia **Test Sends**.

## Responsividade

As etapas do Canvas respondem ao tempo ao pré-visualizar jornadas do usuário. Atualizações feitas pela etapa de Atualização de usuário são refletidas nas etapas subsequentes do fluxo, mas não são aplicadas ao perfil real do usuário. Os efeitos de um usuário entrar em uma variante são refletidos nas etapas futuras da pré-visualização.

Da mesma forma, os filtros reconhecem ações que ocorreram como resultado da interação do usuário teste com outras etapas no Canvas. Por exemplo, esse modo de pré-visualização reconhece que um usuário encontrou uma etapa de mensagem que foi "enviada" anteriormente no Canvas e reconhece que o usuário teste "realizou uma ação" para avançar por uma jornada de ação.

Consulte [Critérios de saída]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria/) para mais detalhes sobre o comportamento responsivo.

## Conteúdo conectado

O Conteúdo conectado é executado se estiver incluído no Canvas. Isso significa que, se você testar um Canvas que tem chamadas de Conteúdo conectado ou Blocos de conteúdo que contêm Conteúdo conectado, o Canvas pode enviar as chamadas de Conteúdo conectado, o que modificaria os dados referenciados em outras campanhas ou Canvas.

Ao pré-visualizar jornadas do usuário, considere remover o Conteúdo conectado que altera perfis de usuário ou dados referenciados em outros Canvas ou campanhas.

## Webhooks

Os webhooks são executados quando mensagens de teste são enviadas, mas não durante a execução de teste. Assim como o Conteúdo conectado, considere remover webhooks que alteram perfis de usuário ou dados referenciados em outros Canvas ou campanhas.

## Variáveis de contexto e Grupos de teste

Para uma etapa de mensagem com e-mail como canal de envio de mensagens, os Grupos de teste enviam cópias seed dos e-mails quando um usuário alcança essa etapa no Canvas. Essas cópias seed não são enviadas como parte das jornadas do Canvas dos próprios destinatários do Grupo de teste, então a Braze não executa [etapas de Contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) nem avalia variáveis de contexto para esses destinatários. Se o conteúdo do seu e-mail referencia variáveis de contexto, os destinatários do Grupo de teste recebem uma cópia seed sem esses dados preenchidos. Para testar mensagens que dependem de dados de variáveis de contexto, use a pré-visualização **Test Canvas** com envios de teste em vez de Grupos de teste.

## Caso de uso

Neste cenário, o Canvas é configurado para direcionar usuários que não tiveram uma sessão em um app. Essa jornada inclui uma etapa de mensagem com um e-mail de boas-vindas, uma etapa de postergação definida para um dia e uma etapa de Jornadas do público que se divide em duas jornadas: usuários com pelo menos uma sessão e todos os demais. Dependendo de qual jornada do público o usuário se enquadra, a etapa de mensagem subsequente é enviada.

![Um exemplo de Canvas com uma etapa de mensagem, etapa de postergação, etapa de Jornadas do público e duas etapas de mensagem.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

Como nosso usuário teste atende aos critérios de entrada do Canvas, ele pode entrar no Canvas e percorrer a jornada do usuário. No entanto, como nosso usuário teste não abriu o app no último dia corrido, ele continua pela jornada "Restante do público" e recebe uma notificação por push que diz: "Última chance! Conclua sua primeira tarefa para ganhar um bônus exclusivo."

![A seção "Test Results" mostra que o usuário teste atendeu aos critérios de entrada e fornece um resumo da jornada, incluindo quais etapas foram enviadas.]({% image_buster /assets/img/preview_user_path_results_example.png %})