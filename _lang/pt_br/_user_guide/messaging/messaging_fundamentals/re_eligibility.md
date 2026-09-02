---
nav_title: Reelegibilidade
article_title: Reelegibilidade
page_order: 10
page_type: reference
description: "Este artigo de referência define a reelegibilidade para Campaigns e Canvas."
tool:
    - Campaigns
    - Canvas
toc_headers: h2
---

# Reelegibilidade para Campaigns e Canvas {#re-eligibility-for-campaigns-and-canvas}

> Ao programar uma Campaign ou Canvas recorrente ou disparada, você tem a opção de permitir que os usuários se tornem reelegíveis. Reelegibilidade significa que os usuários podem entrar na Campaign ou no Canvas várias vezes com base no gatilho.

## Como funciona {#how-it-works}

Por padrão, a Braze envia uma mensagem a um usuário apenas uma vez, mesmo que ele se requalifique várias vezes, pois a reelegibilidade precisa ser ativada separadamente. Depois de ativada, os membros qualificados poderão receber mensagens novamente após terem recebido a primeira instância da Campaign ou do Canvas. Você pode definir o período após o qual os usuários se tornarão reelegíveis.

## Ativando a reelegibilidade {#turning-on-re-eligibility}

{% tabs local %}
{% tab campaign %}
Para ativar a reelegibilidade de uma Campaign, marque a caixa de seleção **Allow users to become re-eligible to receive campaign** na seção **Delivery Controls**. O tempo máximo de reelegibilidade para uma Campaign é de 720 dias.

Para Campaigns disparadas com reelegibilidade ativada, os usuários que [não receberam de fato a mensagem da Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#why-did-a-user-not-receive-my-triggered-campaign) (apesar de terem concluído o evento-gatilho) se qualificarão automaticamente para a mensagem na próxima vez que concluírem o evento-gatilho. Isso ocorre porque a reelegibilidade é baseada no recebimento da mensagem, e não na entrada na Campaign. Ao tornar os usuários reelegíveis para uma Campaign disparada, você permite que eles realmente recebam (e não apenas disparem) a mensagem mais de uma vez.

{% alert note %}
"Recebimento" inclui atribuição por meio de identificadores de canal compartilhados: quando uma mensagem é entregue, aberta ou clicada, a Braze atualiza os dados de todos os perfis que compartilham o mesmo e-mail ou número de telefone. Portanto, um usuário que nunca recebeu a mensagem diretamente pode ser marcado como tendo recebido e pode não se tornar reelegível.
{% endalert %}

Além disso, se você estiver tentando enviar uma mensagem imediatamente com uma reelegibilidade de zero minutos, sempre tentaremos programá-la imediatamente, independentemente de como o usuário recebeu versões anteriores da Campaign ou do Canvas.

### Reelegibilidade com Campaigns disparadas por API or interface de programação do aplicativo (API) {#re-eligibility-with-api-triggered-campaigns}

O número de vezes que um usuário recebe uma Campaign disparada por API or interface de programação do aplicativo (API) pode ser limitado usando as configurações de reelegibilidade. Isso significa que o usuário receberá a Campaign apenas uma vez ou uma vez em um determinado período, independentemente de quantas vezes o gatilho da API or interface de programação do aplicativo (API) for acionado.

Por exemplo, digamos que você esteja usando uma Campaign disparada por API or interface de programação do aplicativo (API) para enviar ao usuário uma Campaign sobre um item que ele visualizou recentemente. Nesse caso, você pode limitar a Campaign para enviar no máximo uma mensagem por dia, independentemente de quantos itens ele visualizou, enquanto aciona o gatilho da API or interface de programação do aplicativo (API) para cada item. Por outro lado, se sua Campaign disparada por API or interface de programação do aplicativo (API) for transacional, você vai querer garantir que o usuário receba a Campaign toda vez que realizar a transação, definindo a postergação como zero minutos.
{% endtab %}

{% tab canvas %}

Para ativar a reelegibilidade de um Canvas, selecione **Allow users to re-enter this Canvas** na seção **Entry Controls**. Você pode escolher entre permitir que os usuários reentrem após a duração máxima do Canvas ou após um período especificado.

A reelegibilidade para variantes do Canvas está vinculada à entrada no Canvas, e não ao recebimento da mensagem. Os usuários que entram em um Canvas e não recebem nenhuma mensagem não poderão reentrar no Canvas, a menos que a reelegibilidade esteja ativada.

Observe que um usuário não precisa sair de um Canvas antes de reentrar se a reelegibilidade estiver definida como zero segundos, o que significa que um usuário pode entrar no mesmo Canvas novamente. Como outro exemplo, se a duração do Canvas estiver definida como 7 dias e o período de reelegibilidade estiver definido como 3 dias, um usuário pode reentrar no Canvas antes de concluir sua primeira jornada nele.

Você pode adicionar filtros adicionais para evitar que os usuários recebam a mesma etapa ou mensagem várias vezes. No entanto, quando um usuário reentra em um Canvas pela segunda vez, as etapas recebidas anteriormente durante a primeira vez no Canvas não ficam visíveis para o usuário. Isso significa que o usuário ainda pode receber a mesma mensagem novamente. Para evitar isso, você pode configurar o Canvas para impedir a reentrada ou definir a reelegibilidade para a duração máxima do Canvas.

Você também pode usar uma [etapa de Atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) para que o usuário que recebe a etapa registre isso como um atributo personalizado, que pode ser usado para filtrar os usuários que já receberam a etapa durante sua jornada no Canvas.

### Exemplo {#example}

Por exemplo, suponha que um usuário sem endereço de e-mail entre em um Canvas recorrente diário que contém uma etapa na jornada do usuário. Essa etapa contém apenas uma mensagem de e-mail, então o usuário não recebe o engajamento. Esse usuário não poderá entrar no Canvas novamente, a menos que o Canvas tenha a reelegibilidade ativada.

Se você tiver um Canvas recorrente ou disparado ativo sem reelegibilidade e quiser que os usuários reentrem no Canvas até receberem uma mensagem dele, considere permitir que os usuários sejam reelegíveis para entrada adicionando um filtro aos critérios de entrada que exclua os clientes que já receberam uma mensagem do Canvas.

Se a reelegibilidade de um Canvas estiver definida como menor que a duração do Canvas, é possível que os usuários entrem no Canvas mais de uma vez, o que pode levar a comportamentos enganosos para Canvas que usam mensagens no app com postergações particularmente longas. Como várias mensagens no app do Canvas podem ser disparadas pelo mesmo início de sessão, o usuário pode ter a experiência de receber a mesma mensagem repetidamente se um componente específico renderizar mais rápido que outros.
{% endtab %}
{% endtabs %}

## Cálculos de postergação de reelegibilidade {#re-eligibility-delay-calculations}

A reelegibilidade para Campaigns e Canvas é calculada em segundos, não em dias corridos. Isso significa que um dia conta como 24 horas (ou 86.400 segundos) a partir do momento em que o usuário recebe a mensagem, não no próximo dia corrido à meia-noite. Da mesma forma, um mês conta como exatamente 2.592.000 segundos, equivalente a aproximadamente 30 dias.

### Exemplo

Considere o seguinte cenário:

* Uma Campaign está configurada para enviar mensalmente no dia 15, com reelegibilidade definida como 30 dias.
* Há menos de 30 dias entre 15 de fevereiro e 15 de março.

Isso significa que os usuários que receberam a Campaign em 15 de fevereiro não são elegíveis para a Campaign enviada em 15 de março. (Um usuário pode ser marcado como tendo "recebido" a Campaign devido a identificadores de canal compartilhados — por exemplo, se ele compartilha um e-mail ou número de telefone com alguém que recebeu, abriu ou clicou na mensagem.) Se a Campaign estiver configurada para enviar diariamente às 8h com reelegibilidade de 1 dia, e houver uma latência no envio da mensagem, os usuários que receberam a Campaign às 8h30 ainda não são reelegíveis no dia seguinte às 8h.

## Reelegibilidade para Content Cards {#re-eligibility-for-content-cards}

Quando a reelegibilidade está ativada para Campaigns ou etapas do Canvas de Content Cards, um usuário pode receber outro cartão enquanto um cartão anterior da mesma Campaign ainda está no feed, o que pode parecer cartões duplicados. Para reduzir duplicatas, desative a reelegibilidade ou aumente o período de reelegibilidade para que o primeiro cartão [expire do feed]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#the-30-day-expiration-and-re-eligibility) antes que o usuário se qualifique para outro envio.

Diferentemente de outros canais (como push e e-mail), em que a reelegibilidade é calculada a partir do timestamp de entrega da mensagem, a reelegibilidade de Content Cards é calculada com base no timestamp de impressão, que é quando o usuário realmente visualiza o cartão. Isso significa que, se houver um intervalo entre o momento em que o cartão é entregue e o momento em que o usuário abre a sessão para visualizá-lo, ele pode não se tornar reelegível conforme esperado.

Por exemplo, se uma Campaign diária de Content Cards tiver um período de reelegibilidade de 24 horas e o usuário visualizar o cartão várias horas após a entrega, ele pode não receber o cartão do dia seguinte porque 24 horas não se passaram desde a impressão. Para lidar com isso, considere reduzir ligeiramente o período de reelegibilidade para Campaigns recorrentes de Content Cards.

## Reelegibilidade para Banners {#re-eligibility-for-banners}

Quando a reelegibilidade está ativada para Campaigns de Banner, os usuários que dispensam um Banner podem se tornar elegíveis novamente após um período de espera configurável que começa na dispensa. Se a reelegibilidade não estiver ativada, os usuários que dispensaram permanecem inelegíveis. Para configurar a reelegibilidade, consulte [Configurar reelegibilidade]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility). Observe que as etapas de Banner do Canvas usam as configurações de reentrada do Canvas.

## Testes multivariantes {#multivariate-testing}

Para testes multivariantes, a Braze determina a reelegibilidade de variante para todas as Campaigns, mensagens no app disparadas e Canvas usando as seguintes regras:

- Quando os percentuais de variante não são alterados, cada usuário sempre entrará na mesma variante de uma Campaign, mensagem no app disparada ou entrada no Canvas toda vez que for reelegível.
- Se os percentuais de variante mudarem, os usuários podem ser redistribuídos para outras variantes.
- Os grupos de controle permanecerão consistentes se o percentual de variante não for alterado, e nenhum usuário que tenha recebido mensagens anteriormente entrará no grupo de controle em um envio posterior, nem qualquer usuário no grupo de controle receberá uma mensagem.