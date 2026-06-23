---
nav_title: Condições de corrida
article_title: Condições de corrida
alias: /race_conditions/
page_order: 9
page_type: reference
description: "Este artigo aborda as práticas recomendadas para evitar que as condições de corrida afetem suas campanhas de mensagens."
toc_headers: h2
---

# Condições de corrida {#race-conditions}

> Uma condição de corrida ocorre quando um resultado depende da sequência ou do tempo de vários eventos. Por exemplo, se a sequência desejada de eventos for "Evento A" e depois "Evento B", mas às vezes o "Evento A" vem primeiro e outras vezes o "Evento B" vem primeiro, isso é conhecido como condição de corrida. Isso pode levar a resultados inesperados ou erros porque esses eventos competem para acessar recursos ou dados compartilhados.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

Na Braze, as condições de corrida podem ocorrer quando várias ações são disparadas ao mesmo tempo com base em dados de usuários ou eventos. Por exemplo, se um usuário disparar várias campanhas (como inscrever-se em um boletim informativo ou fazer uma compra), ele poderá não receber as mensagens na ordem correta.

## Tipos de condições de corrida {#types-of-race-conditions}

Os tipos mais comuns de condições de corrida podem ocorrer quando você estiver fazendo o seguinte:

- Direcionamento a novos usuários
- Uso de vários endpoints de API
- Correspondência entre filtros de público e disparadores baseados em ação
- Uso do gatilho "Interagir com etapa"

Considere os seguintes cenários e implemente as práticas recomendadas para evitar essas condições de corrida.

## Cenário 1: Direcionamento a novos usuários {#scenario-1-targeting-new-users}

Na Braze, uma das condições de corrida mais comuns ocorre com mensagens direcionadas a usuários recém-criados. A ordem esperada dos eventos é:

1. Um usuário é criado;
2. O mesmo usuário é imediatamente direcionado para uma mensagem, realiza um evento personalizado ou registra um atributo personalizado.

No entanto, em alguns casos, o segundo evento é disparado primeiro. Isso significa que uma mensagem tenta ser enviada a um usuário que ainda não existe. Como resultado, o usuário nunca a recebe. Isso também se aplica a eventos ou atributos, em que o evento ou atributo tenta ser registrado em um perfil de usuário que ainda não foi criado.

No caso de mensagens no app, a mensagem no app precisa ser carregada no dispositivo do usuário antes de ser disparada. Se o evento de gatilho faz parte do processo de integração, ou se o usuário sai do segmento para o evento personalizado como parte de sua primeira sessão, é provável que o usuário não veja a mensagem no app.

### Mensagens no app {#in-app-messages}

Com mensagens no app, a situação pode ser mais complexa. Uma mensagem no app precisa ser entregue e armazenada em cache no SDK — normalmente no início de uma sessão — antes de poder ser disparada. Se o evento de gatilho faz parte do processo de criação do usuário, ou se a Campaign de mensagem no app é entregue antes de o usuário atender (ou depois de não mais atender) aos critérios de público durante sua primeira sessão, ele pode não ver a mensagem no app.

### Práticas recomendadas {#best-practices}

#### Introduza postergações {#introduce-delays}

Depois que um novo usuário é criado, você pode adicionar uma postergação antes de enviar qualquer Campaign ou Canvas direcionado. Essa postergação permite que o perfil do usuário seja criado e que quaisquer atributos relevantes sejam atualizados, o que pode determinar sua elegibilidade para receber a mensagem.

Por exemplo, depois que um usuário se registra no seu app, você pode enviar uma oferta promocional após 24 horas. Ou, se você está criando um usuário ou registrando um atributo personalizado, pode adicionar uma postergação de um minuto antes de prosseguir no seu processo para evitar essa condição de corrida.

Você também pode adicionar essa postergação no [SDK da Braze]({{site.baseurl}}/developer_guide/sdk_integration/) para o evento personalizado específico que faz um novo usuário entrar em um Canvas.

## Cenário 2: Usando múltiplos endpoints de API {#scenario-2-using-multiple-api-endpoints}

{% alert important %}
Usamos processamento assíncrono para maximizar a velocidade e a flexibilidade. Isso significa que, quando chamadas de API são enviadas separadamente, não podemos garantir que elas sejam processadas na ordem em que foram enviadas.
{% endalert %}

Existem alguns cenários em que múltiplos endpoints de API também podem resultar nessa condição de corrida, como quando:

- Endpoints de API separados são usados para criar usuários e disparar Canvas ou Campaigns
- Múltiplas chamadas separadas são feitas ao endpoint `/users/track` para atualizar atributos personalizados, eventos ou compras

Quando informações de usuários são enviadas à Braze usando o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), pode levar alguns segundos para o processamento. Isso significa que, quando solicitações são feitas simultaneamente aos endpoints `/users/track` e de envio de mensagens como `/campaign/trigger/send`, não há garantia de que as informações do usuário sejam atualizadas antes de uma mensagem ser enviada.

{% alert note %}
Se atributos e eventos de usuários são enviados na mesma solicitação (seja pelo `/users/track` ou pelo SDK), a Braze processa os atributos antes dos eventos ou de tentar enviar qualquer mensagem.
{% endalert %}

### Práticas recomendadas

#### Ao usar múltiplos endpoints, envie suas solicitações uma de cada vez {#when-using-multiple-endpoints-send-your-requests-one-at-a-time}

Se você está usando múltiplos endpoints, pode tentar escalonar suas solicitações para que cada uma seja concluída antes de a próxima começar. Isso pode reduzir a chance de uma condição de corrida. Por exemplo, se você precisa atualizar atributos de usuário e enviar uma mensagem, primeiro aguarde a atualização completa do perfil do usuário antes de enviar uma mensagem usando um endpoint.

Se você está enviando uma solicitação de API de mensagem agendada, essas solicitações devem ser separadas, e o usuário deve ser criado antes de enviar a solicitação de API agendada.

#### Inclua dados essenciais junto com o gatilho {#include-key-data-with-the-trigger}

Em vez de usar múltiplos endpoints, você pode incluir os [atributos de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object/#object-body) e as [propriedades de gatilho]({{site.baseurl}}/api/objects_filters/trigger_properties_object/) em uma única chamada de API usando o [endpoint `campaign/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).

Quando esses objetos são incluídos com o gatilho, os atributos são processados primeiro, antes de a mensagem ser disparada, eliminando possíveis condições de corrida. As propriedades de gatilho não atualizam o perfil do usuário, mas são usadas apenas no contexto da mensagem.

#### Use o endpoint POST: Rastrear usuários (síncrono) {#use-the-post-track-users-sync-endpoint}

Use o [endpoint `/users/track/sync/`]({{site.baseurl}}/api/endpoints/user_data/post_user_track_synchronous/) para registrar eventos personalizados e compras e atualizar atributos do perfil de usuário de forma síncrona. Usar esse endpoint para atualizar perfis de usuários ao mesmo tempo e em uma única chamada pode ajudar a evitar possíveis condições de corrida.

{% multi_lang_include early_access_beta_alert.md feature='This endpoint' type='beta' %}

## Cenário 3: Correspondência entre gatilhos baseados em ação e filtros de público {#scenario-3-matching-action-based-triggers-and-audience-filters}

Outra condição de corrida comum pode ocorrer se você configurar uma Campaign ou Canvas baseado em ação com o mesmo gatilho do filtro de público (como um atributo alterado ou um evento personalizado realizado). O usuário pode não estar no público no momento em que realiza o evento de gatilho, o que significa que ele não receberá a Campaign nem entrará no Canvas.

### Práticas recomendadas

#### Verifique seu público após uma postergação {#check-your-audience-after-a-delay}

Para evitar o uso de filtros de público que contenham os critérios de gatilho, recomendamos verificar seu público antes da entrega. Por exemplo, você pode [usar validações de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#edit-delivery-settings) nas etapas de Mensagem do Canvas como uma verificação adicional para confirmar que seu público atende aos critérios de entrega no momento do envio da mensagem. Você também pode aproveitar os critérios de saída do Canvas para remover qualquer usuário em qualquer ponto da jornada se ele atender aos seus critérios.

Para Campaigns, você pode usar eventos de saída para permitir que Campaigns com um evento de gatilho cancelem mensagens para usuários que realizem o evento de saída enquanto estiverem na postergação.

#### Use filtros exclusivos com o evento de gatilho {#use-unique-filters-with-the-trigger-event}

Ao configurar seus filtros, você pode querer adicionar um filtro redundante "por precaução". No entanto, essa redundância pode causar mais problemas. Em vez disso, evite usar qualquer filtro que contenha o gatilho quando possível. Essa é a rota mais segura para evitar uma condição de corrida.

Por exemplo, se o gatilho da sua Campaign é "Fez uma compra" e seu filtro de público é "Fez qualquer compra", essa redundância pode causar uma condição de corrida.

#### Evite filtros de público que assumam que o evento de gatilho foi atualizado {#avoid-audience-filters-that-assume-the-trigger-event-has-been-updated}

Essa prática recomendada é semelhante a evitar filtros redundantes com o evento de gatilho. Normalmente, um filtro que assume que o evento de gatilho foi atualizado no perfil do usuário falha.

#### Use aborts de Liquid (somente atributos) {#use-liquid-aborts-attributes-only}

Em Campaigns e etapas do Canvas, use aborts de Liquid para evitar o uso de filtros de público que contenham os atributos de gatilho no cronograma de entrada. Por exemplo, digamos que você tenha um atributo de array "cores favoritas" e queira direcionar qualquer usuário que atualize o array de atributos com qualquer valor e que também tenha a cor "azul" no array após a conclusão da atualização. Se você usar os filtros de público neste exemplo, encontrará uma condição de corrida e perderá usuários que estão adicionando "azul" no array pela primeira vez.

Nesse caso, você pode implementar uma postergação de gatilho em uma Campaign ou usar uma etapa de postergação no Canvas para permitir que o perfil do usuário seja atualizado por um período de tempo, e então usar a seguinte lógica de abort de Liquid:

{% raw %}
```liquid
{%assign colors={{custom_attribute.$(Favorite Color)|split:”,”}}%}
{%unless colors contains ‘Blue’%}
{%abort_message(Blue not present)%}
{%endunless%}
```
{% endraw %}

#### Confirme como os dados de usuários estão sendo gerenciados {#confirm-how-user-data-is-being-managed}

Se houver uma condição de corrida durante a avaliação de entrada do Canvas, os usuários podem entrar em um Canvas no qual não deveriam entrar. Por exemplo, o perfil do usuário pode estar configurado para ser incluído no público e, em seguida, ser atualizado após o Canvas ter enfileirado os usuários para não serem mais elegíveis no público.

Se um usuário dispara o evento de entrada do Canvas várias vezes dentro do mesmo segundo, a Braze permite apenas uma entrada para aquele segundo (mesmo que a reentrada esteja ativada). Isso evita entradas duplicadas, então o número total de entradas no Canvas pode ser menor do que o total de eventos de gatilho.

Recomendamos confirmar como os dados de usuários são gerenciados e atualizados, especificamente quando e como atributos específicos são atualizados, como por SDK, API, API em lote e outros métodos. Isso pode ajudar a identificar e esclarecer por que um usuário entrou em uma Campaign ou Canvas em comparação com quando o perfil do usuário foi atualizado.

## Cenário 4: Usando o gatilho "Interagir com etapa" {#scenario-4-using-the-interact-with-step-trigger}

Em um Canvas, quando uma etapa de Mensagem é imediatamente seguida por uma etapa de Jornadas de ação que usa o gatilho "Interagir com etapa", uma condição de corrida pode ocorrer. Como os usuários podem interagir com uma mensagem assim que ela é entregue, é possível que um usuário conclua a ação rastreada antes de entrar oficialmente na etapa de Jornadas de ação.

Nesse caso, a etapa de Jornadas de ação não registra a interação, pois ela avalia apenas eventos que ocorrem após a entrada na etapa, o que significa que o usuário pode ser direcionado por uma jornada não intencional.

Um Canvas envia uma notificação por push em uma etapa de Mensagem, seguida por uma etapa de Jornadas de ação que verifica se o usuário abriu essa notificação por push. Se um usuário abrir a notificação por push imediatamente ao recebê-la (antes de entrar na etapa de Jornadas de ação), o evento de abertura pode não ser capturado. O usuário poderia então ser incorretamente direcionado pela jornada "não abriu", mesmo tendo interagido com a mensagem.

### Práticas recomendadas

#### Rastreie o engajamento usando um evento personalizado {#track-engagement-using-a-custom-event}

Evite depender de "Interagir com etapa" imediatamente após uma etapa de Mensagem quando se espera que as interações dos usuários ocorram rapidamente. Em vez disso, rastreie o engajamento usando um evento personalizado (por exemplo, disparado a partir do app ou site após a interação) e avalie esse evento em uma etapa posterior. Isso garante que o evento seja registrado após o usuário ter entrado na etapa.

#### Evite ramificações que dependam da interação {#avoid-branches-that-are-dependent-on-interaction}

Projete seu Canvas de modo que a perda de uma interação imediata não prejudique a experiência do usuário. Por exemplo, evite decisões críticas de ramificação que dependam exclusivamente de a interação ser capturada na próxima etapa, ou adicione lógica de acompanhamento que possa corrigir as rotas dos usuários.