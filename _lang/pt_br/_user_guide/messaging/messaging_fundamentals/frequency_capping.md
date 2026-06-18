---
nav_title: Limite de taxa e limite de frequência
article_title: Limite de taxa e limite de frequência
page_order: 6
tool: Campaigns
page_type: reference
description: "Este artigo de referência discute o conceito de limite de taxa e limite de frequência em Campaigns, e como você pode gerenciar a pressão de marketing para melhorar a experiência do usuário."

---

# Limite de taxa e limite de frequência {#rate-limiting-and-frequency-capping}

> O limite de taxa e o limite de frequência podem ser usados juntos para garantir que seus usuários recebam as mensagens de que precisam.

## Sobre o limite de taxa {#about-rate-limiting}

A Braze permite que você controle a pressão de marketing limitando a taxa das suas Campaigns, regulando a quantidade de tráfego de saída da sua plataforma. Você pode implementar dois tipos diferentes de limite de taxa para suas Campaigns:

1. [Limite de taxa centrado no usuário:](#user-centric-rate-limiting) Foca em proporcionar a melhor experiência para o usuário.
2. [Limite de taxa de velocidade de entrega:](#delivery-speed-rate-limiting) Leva em consideração a largura de banda dos seus servidores.

A Braze não suporta um limite de taxa por segundo. A Braze tenta distribuir uniformemente os envios de mensagens ao longo do minuto, mas não pode garantir isso. Por exemplo, se você tem uma Campaign com um limite de taxa de 5.000 mensagens por minuto, tentamos distribuir as 5.000 solicitações uniformemente ao longo do minuto (cerca de 84 mensagens por segundo), mas pode haver alguma variação na taxa por segundo.

### Limite de taxa centrado no usuário {#user-centric-rate-limiting}

À medida que você cria mais segmentos, haverá casos em que a composição desses segmentos se sobrepõe. Se você está enviando Campaigns para esses segmentos, é importante garantir que não está enviando mensagens para seus usuários com muita frequência. Se um usuário receber muitas mensagens em um curto período de tempo, ele se sentirá sobrecarregado e poderá desativar as notificações por push ou desinstalar seu app.

#### Filtros de segmento relevantes {#relevant-segment-filters}

A Braze fornece os seguintes filtros para ajudar você a limitar a taxa com que seus usuários recebem mensagens:

- Última interação com mensagem
- Última mensagem recebida
- Último push recebido
- Último e-mail recebido
- Último SMS recebido

#### Implementando filtros {#implementing-filters}

Digamos que criamos um segmento chamado "Vitrine de filtro de redirecionamento" com o filtro "Último uso do app há mais de 7 dias" para direcionar usuários. Esse seria um segmento padrão de reengajamento.

Se você tem outros segmentos mais direcionados que receberam notificações recentemente, talvez não queira que seus usuários sejam direcionados por Campaigns mais genéricas voltadas para esse segmento. Ao adicionar o filtro "Último push recebido" a esse segmento, o usuário garante que, se recebeu outra notificação nas últimas 24 horas, sairá desse segmento pelas próximas 24 horas. Se ainda atender aos outros critérios do segmento 24 horas depois e não tiver recebido mais notificações, voltará a fazer parte do segmento.

![Um segmento chamado "Vitrine de filtro de redirecionamento" com o grupo de filtros "Último uso do app há mais de 7 dias".]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"}

Adicionar esse filtro a todos os segmentos direcionados por Campaigns faria com que seus usuários recebessem no máximo um push a cada 24 horas. Você poderia então priorizar suas mensagens garantindo que as mais importantes sejam entregues antes das menos importantes.

#### Definindo um limite máximo de usuários {#setting-a-maximum-user-cap}

Na etapa **Públicos-alvo** do criador da sua Campaign, você também pode limitar o número total de usuários que receberão sua mensagem. Isso serve como uma verificação independente dos filtros da sua Campaign.

![Resumo do público com uma caixa de seleção marcada para limitar o número de pessoas que recebem a Campaign.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"}

Ao selecionar o limite máximo de usuários, você pode limitar o volume de mensagens enviadas por canal ou globalmente em todos os tipos de mensagem. A Braze não despacha mensagens para usuários atribuídos a grupos de controle, então eles não contam para o limite.

{% alert note %}
O limite máximo de usuários limita o número de usuários despachados, não o número de mensagens enviadas com sucesso. Como mensagens abortadas contam para esse limite, o número real de mensagens enviadas pode ser menor que o limite configurado. Por exemplo, se você definir um limite de 10.000 e 2.000 mensagens forem abortadas devido à lógica Liquid ou outras condições, apenas 8.000 mensagens serão enviadas.
{% endalert %}

##### Limite máximo de usuários com otimizações {#maximum-user-cap-with-optimizations}

Se você está usando uma otimização como Variante Vencedora ou Variante Personalizada, a Campaign consistirá em dois envios: o experimento inicial e o envio final.

Para configurar um limite máximo de usuários nesse cenário, selecione **Limitar o número de pessoas que receberão esta Campaign**, depois selecione **No total, esta Campaign deve** e insira um limite de público. Seu limite de público será dividido pelas porcentagens mostradas no painel de **Testes A/B**.

Se você selecionar **Toda vez que a Campaign for agendada**, essas duas fases serão limitadas separadamente ao número definido. Isso normalmente não é desejável.

#### Definindo um limite máximo de impressões em Campaigns {#setting-a-maximum-impression-cap-on-campaigns}

Para mensagens no app, você pode controlar a pressão de marketing definindo um número máximo de impressões que serão exibidas para sua base de usuários, após o qual a Braze não enviará mais mensagens para seus usuários. No entanto, é importante observar que esse limite não é exato.

As regras de mensagens no app são enviadas para o app no início da sessão, o que significa que a Braze pode enviar uma mensagem ao usuário antes que o limite seja atingido, mas quando o usuário aciona a mensagem, o limite já foi atingido. Nessa situação, o dispositivo ainda exibirá a mensagem.

Por exemplo, digamos que você tem um jogo com uma mensagem no app que é acionada quando um usuário passa de fase, e você limita a 100 impressões. Até agora, houve 99 impressões. Alice e Bob abrem o jogo, e a Braze informa aos dispositivos deles que são elegíveis para receber a mensagem quando passarem de fase. Alice passa de fase primeiro e recebe a mensagem. Bob passa de fase em seguida, mas como seu dispositivo não se comunicou com os servidores da Braze desde o início da sessão, seu dispositivo não sabe que a mensagem atingiu o limite, e ele também recebe a mensagem. No entanto, quando o limite de impressões é atingido, na próxima vez que qualquer dispositivo solicitar a lista de mensagens no app elegíveis, o sistema não enviará essa mensagem e a removerá daquele dispositivo.

### Limite de taxa e testes A/B {#rate-limiting-and-ab-testing}

Ao usar o limite de taxa com um teste A/B, o limite de taxa não é aplicado ao grupo de controle da mesma forma que ao grupo de teste, o que é uma fonte potencial de viés temporal. Para evitar esse viés, use janelas de conversão apropriadas.

### Limite de taxa de velocidade de entrega {#delivery-speed-rate-limiting}

Se você prevê que grandes Campaigns causarão um pico na atividade dos usuários e sobrecarregarão seus servidores, você pode especificar um limite de taxa por minuto para o envio de mensagens, o que significa que a Braze não envia mais do que o limite definido dentro de um minuto.

Ao direcionar usuários durante a criação da Campaign, você pode navegar até **Públicos-alvo** (para Campaigns) ou **Configurações de envio** (para Canvas) para selecionar um limite de taxa (em vários incrementos, de 10 até 500.000 mensagens por minuto).

Observe que Campaigns sem limite de taxa podem exceder esses limites de entrega. No entanto, esteja ciente de que as mensagens serão abortadas se forem atrasadas 72 horas ou mais devido a um limite de taxa baixo. Se o limite de taxa for muito baixo, o criador da Campaign receberá alertas no dashboard e por e-mail.

{% alert tip %}
Defina um [limite de taxa de envio de mensagens do espaço de trabalho]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits/) para aplicar um limite de taxa em todo o espaço de trabalho.
{% endalert %}

#### Exemplo {#example}

Se você está tentando enviar 75.000 mensagens com um limite de taxa de 10.000 por minuto, a entrega será distribuída ao longo de oito minutos. Sua Campaign entregará no máximo 10.000 mensagens em cada um dos primeiros sete minutos e 5.000 no último minuto.

#### Número de envios {#number-of-sends}

Observe que mensagens com limite de taxa podem não ser enviadas uniformemente ao longo de cada minuto. Usando o exemplo de um limite de taxa de 10.000 por minuto, isso significa que a Braze garante que não mais de 10.000 mensagens sejam enviadas por minuto. Isso pode significar que uma porcentagem maior das 10.000 mensagens é enviada na primeira metade do minuto em comparação com a segunda metade.

O limite de taxa é aplicado no início da tentativa de envio da mensagem. Quando há flutuações no tempo necessário para concluir o envio, o número de envios concluídos pode exceder ligeiramente o limite de taxa por alguns minutos. Com o tempo, o número de envios por minuto se estabilizará em não mais do que o limite de taxa.

{% alert important %}
Tenha cuidado ao atrasar mensagens urgentes com essa forma de limite de taxa em relação ao número total de usuários em um segmento. Por exemplo, se o segmento contém 30 milhões de usuários, mas definimos o limite de taxa para 10.000 por minuto, uma grande parte da sua base de usuários não receberá a mensagem até o dia seguinte.
{% endalert %}

#### Campaigns multicanais e Canvas {#multichannel-campaigns-and-canvases}

Ao definir um limite de taxa de velocidade de entrega para uma Campaign multicanal ou Canvas, você pode optar por definir um limite de taxa compartilhado ou um limite baseado em canal.

Quando uma Campaign multicanal ou Canvas usa um limite de taxa compartilhado, isso significa que o número total de mensagens enviadas por minuto pela Campaign ou Canvas não excede o limite de taxa. Por exemplo, se seu Canvas tem um limite de taxa de 500.000 por minuto e contém etapas de mensagem de e-mail e SMS, a Braze envia um total de 500.000 mensagens por minuto entre e-mail e SMS.

![A opção de limitar a taxa de envio da Campaign, selecionada com 500.000 mensagens por minuto.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"}

Quando uma Campaign multicanal ou Canvas usa limite de taxa baseado em canal, o limite de taxa será aplicado a cada um dos canais selecionados. Por exemplo, você pode configurar sua Campaign ou Canvas para enviar no máximo 5.000 webhooks e 2.500 mensagens SMS por minuto em toda a Campaign ou Canvas.

![Limites de taxa separados para dois canais, webhook e SMS/MMS/RCS, com 5.000 e 2.500 mensagens por minuto, respectivamente.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Notificações por push {#push-notifications}

Para Campaigns ou Canvas com plataformas de push (como Android, iOS, push para a web ou Kindle), você pode selecionar **Notificações por push** para aplicar um limite de taxa compartilhado entre todas as plataformas de push na sua Campaign ou Canvas.

![O menu suspenso de canal com opções para plataformas de push e notificações por push.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"}

Se você selecionar um limite para notificações por push, não poderá definir limites de taxa individuais por canal de push. Da mesma forma, se selecionar limites para canais de push individuais, não poderá definir limites compartilhados de notificações por push.

{% alert important %}
**Atualizações na interface de limite de taxa**<br>
A Braze atualizou a interface de limite de taxa para fornecer mais transparência e controle sobre como os limites de taxa se aplicam a Campaigns multicanais e Canvas.<br><br>

- **Campaigns e Canvas existentes:** Todas as Campaigns e Canvas existentes foram migrados para esta interface. O comportamento de entrega permanece o mesmo. O dashboard exibe se a Campaign usa lógica compartilhada ou por canal.<br>
- **Novas Campaigns e Canvas:** Para todas as novas Campaigns e Canvas, há um botão manual para escolher a lógica de limite de taxa preferida. Certifique-se de selecionar o comportamento de limite de taxa que se alinha com o comportamento pretendido ao definir ou atualizar um limite de taxa de Campaign ou Canvas.
{% endalert %}

##### Considerações sobre limite de taxa {#rate-limiting-considerations}

Algumas observações a ter em mente ao configurar limites de taxa e o comportamento esperado:

- Envios de SMS estão sujeitos a um limite de taxa de 50.000 por grupo de inscrições. Alguns provedores de SMS podem impor outros limites.
- As seguintes mensagens não serão limitadas ou contabilizadas no limite de taxa:
    - Envios de teste
    - Grupos de teste
    - Content Cards configurados para criar "na primeira impressão" (Isso será controlado pela taxa de impressões do app. Consulte [Criação de cartão]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation/#differences) para mais informações sobre as diferenças entre as opções de criação de cartão.)
- Limites de velocidade de entrega não são suportados para o seguinte:
    - Respostas automáticas de SMS
    - Mensagens com SLA garantido (como [E-mail de transação]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email/))
    - Mensagens no app
    - Feature Flags
    - Banners

#### Limite de taxa e novas tentativas de Conteúdo conectado {#rate-limiting-and-connected-content-retries}

Quando a [nova tentativa de Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries/) está ativada, a Braze tentará novamente as chamadas com falha respeitando o limite de taxa definido para cada reenvio. Vamos considerar o cenário de envio de 75.000 mensagens com um limite de taxa de 10.000 por minuto. Imagine que no primeiro minuto, a chamada falha ou é lenta e envia apenas 4.000 mensagens.

Em vez de tentar compensar o atraso e enviar as 6.000 mensagens restantes no segundo minuto ou adicioná-las às 10.000 já programadas para envio, a Braze moverá essas 6.000 mensagens para o "final da fila" e adicionará um minuto, se necessário, ao total de minutos necessários para enviar sua mensagem.

| Minuto | Sem falha | 6.000 falhas no minuto 1 |
|--------|-----------|--------------------------|
| 1      | 10.000    | 4.000                    |
| 2      | 10.000    | 10.000                   |
| 3      | 10.000    | 10.000                   |
| 4      | 10.000    | 10.000                   |
| 5      | 10.000    | 10.000                   |
| 6      | 10.000    | 10.000                   |
| 7      | 10.000    | 10.000                   |
| 8      | 5.000     | 10.000                   |
| 9      | 0         | 6.000                    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Limite de taxa e novas tentativas de Conteúdo conectado" }

As solicitações de Conteúdo conectado não são limitadas independentemente e seguirão o limite de taxa de webhook. Isso significa que, se houver uma chamada de Conteúdo conectado para um endpoint único por webhook, você esperaria 5.000 webhooks e também 5.000 chamadas de Conteúdo conectado por minuto. Observe que o cache pode afetar isso e reduzir o número de chamadas de Conteúdo conectado. Além disso, as novas tentativas podem aumentar as chamadas de Conteúdo conectado, então recomendamos verificar se o endpoint de Conteúdo conectado pode lidar com alguma flutuação aqui.

{% alert note %}
**Limites de taxa são limites de velocidade e não definem uma velocidade exata de envio.** Geralmente, as mensagens são distribuídas uniformemente dentro de qualquer minuto dado, e na grande maioria dos casos, são enviadas no limite configurado ou muito próximo dele. Nem sempre é o caso — por exemplo, quando as mensagens são muito grandes (como e-mails com muitos Content Blocks, tags de Conteúdo conectado ou tags de itens de Catálogo), ou quando há muitos abortos Liquid (mensagens abortadas ainda consomem um slot e podem reduzir as taxas efetivas de envio).<br><br>
Na prática, a taxa de envio sustentada (mensagens concluídas por minuto) pode ser menor que o limite de taxa configurado devido a novas tentativas, variabilidade de rede, latência do endpoint de destino e suavização por minuto. Se você consistentemente observar um desempenho significativamente menor do que o esperado, verifique os tempos de resposta do Conteúdo conectado, taxas de erro (como `429`) e comportamento de novas tentativas.
{% endalert %}

## Sobre o limite de frequência {#about-frequency-capping}

À medida que sua base de usuários continua a crescer e seu envio de mensagens se expande para incluir Campaigns de ciclo de vida, acionadas, transacionais e de conversão, é importante evitar que suas notificações pareçam "spam" ou disruptivas. Ao fornecer maior controle sobre a experiência dos seus usuários, o limite de frequência permite que você crie as Campaigns que deseja sem sobrecarregar seu público.

### Visão geral do recurso {#freq-cap-feat-over}

O limite de frequência é aplicado no nível de envio da Campaign ou componente do Canvas e pode ser configurado para cada espaço de trabalho em **Configurações** > **Regras do limite de frequência**.

Por padrão, o limite de frequência é ativado quando novas Campaigns são criadas. A partir daqui, você pode escolher o seguinte:

- O canal de envio de mensagens que você deseja limitar: push, e-mail, SMS, webhook, WhatsApp, LINE ou qualquer um desses canais.
- Quantas vezes cada usuário deve receber uma Campaign ou componente do Canvas enviado por um canal dentro de um determinado período de tempo.
- Quantas vezes cada usuário deve receber uma Campaign ou componente do Canvas enviado por [tag](#frequency-capping-by-tag) dentro de um determinado período de tempo.

Esse período de tempo pode ser medido em minutos, dias ou semanas (sete dias), com duração máxima de 30 dias.

Cada linha de limites de frequência é conectada usando o operador `AND`, e você pode adicionar até 10 regras por espaço de trabalho. Você pode incluir múltiplos limites para os mesmos tipos de mensagem. Por exemplo, você pode limitar os usuários a não mais de um push por dia e não mais de três pushes por semana. Observe que mensagens abortadas não contam para o limite de frequência.

![Seção de limite de frequência com listas de Campaigns e Canvas aos quais as regras serão e não serão aplicadas.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"}

#### Comportamento quando os usuários atingem o limite de frequência em uma etapa do Canvas {#behavior-when-users-are-frequency-capped-on-a-canvas-step}

O limite de frequência global sozinho não faz com que os usuários saiam de um Canvas. Em [etapas de Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/), os usuários ainda avançam quando uma mensagem não é enviada por causa do limite de frequência global, de acordo com [como os usuários avançam]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#how-users-advance) pela etapa.

Isso é separado das **Validações de entrega** em uma etapa de Mensagem. Se um usuário não atender aos critérios de validação de entrega no momento do envio, ele pode sair do Canvas naquela etapa.

### Regras de entrega {#delivery-rules}

Pode haver algumas Campaigns, como mensagens transacionais, que você deseja que sempre cheguem ao usuário, mesmo que ele já tenha atingido o limite de frequência. Por exemplo, um app de entregas pode querer enviar um e-mail ou push quando um item é entregue, independentemente de quantas Campaigns o usuário já recebeu.

Se você deseja que uma Campaign específica ignore as regras de limite de frequência, pode configurar isso no dashboard da Braze ao agendar a entrega dessa Campaign, alternando **Limite de frequência** para **DESLIGADO**.

Depois disso, será perguntado se você ainda deseja que essa Campaign conte para o seu limite de frequência. Mensagens que contam para o limite de frequência são incluídas nos cálculos do filtro de Canal Inteligente.

Ao enviar [Campaigns da API]({{site.baseurl}}/developer_guide/rest_api/messaging/#messaging), que geralmente são transacionais, você terá a capacidade de especificar que uma Campaign deve ignorar as regras de limite de frequência definindo `override_frequency_capping` como `true` na solicitação da API.

Por padrão, novas Campaigns e Canvas que não obedecem aos limites de frequência também não contarão para eles. Isso é configurável para cada Campaign e Canvas.

{% alert note %}
Esse comportamento altera o comportamento padrão quando você desativa o limite de frequência para uma Campaign ou Canvas. As alterações são retrocompatíveis e não afetam mensagens que estão atualmente ativas.
{% endalert %}

![Seção de controles de entrega com o limite de frequência ativado.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"}

#### Como os envios contam para os limites {#how-sends-count-toward-caps}

O limite de frequência é aplicado por despacho: cada vez que a Braze envia uma Campaign ou componente do Canvas para um usuário conta para os seus limites — não cada variante de mensagem ou plataforma dentro daquele envio. Por exemplo, se os usuários estão limitados a cinco Campaigns de push por semana, eles não recebem nenhuma Campaign de push após o quinto despacho até que o limite seja redefinido.

##### Envios multicanais {#multichannel-sends}

Quando um único despacho usa múltiplos canais, esse despacho conta no máximo uma vez por regra de limite de frequência aplicável. Por exemplo, se você criar uma Campaign multicanal que envia e-mail, push para iOS e push para Android em uma única entrega e seu espaço de trabalho tiver regras para push e e-mail, além de uma regra que se aplica a todos os canais, essa entrega conta uma vez para a regra de push, uma vez para a regra de e-mail e uma vez para a regra de todos os canais — não conta uma vez por plataforma de push ou por mensagem dentro do envio. Se os usuários estão limitados a uma Campaign de push e uma de e-mail por dia e recebem essa Campaign multicanal, eles não são elegíveis para Campaigns adicionais de push ou e-mail pelo resto do dia, a menos que uma Campaign ignore as regras de limite de frequência.

Mensagens no app e Content Cards não são contabilizados como ou para limites em Campaigns ou componentes do Canvas de qualquer tipo.

{% alert important %}
O limite de frequência global é agendado com base no fuso horário do usuário e é calculado por dias corridos, não por períodos de 24 horas. Por exemplo, se você configurar uma regra de limite de frequência para enviar no máximo uma Campaign por dia, um usuário pode receber uma mensagem às 23h no seu fuso horário local e seria elegível para receber outra mensagem uma hora depois.
{% endalert %}

#### Casos de uso {#use-cases}

{% tabs %}
{% tab Caso de uso 1 %}

Digamos que você defina uma regra de limite de frequência para que seus usuários recebam no máximo três Campaigns ou etapas do Canvas de notificação por push por semana de todas as Campaigns ou etapas do Canvas.

Se seu usuário está programado para receber três notificações por push, duas mensagens no app e um cartão de conteúdo nesta semana, ele receberá todas essas mensagens.

{% endtab %}
{% tab Caso de uso 2 %}

Este cenário usa uma regra de limite de frequência para que os usuários recebam no máximo duas Campaigns ou etapas do Canvas de notificação por push por semana de todas as Campaigns ou etapas do Canvas.

**Quando o seguinte cenário ocorre:**

- Um usuário aciona a mesma Campaign `Campaign ABC` três vezes ao longo de uma semana.
- Esse usuário aciona a `Campaign ABC` uma vez na segunda-feira, uma vez na quarta-feira e uma vez na quinta-feira.

![Seção de limite de frequência com a regra de enviar no máximo 2 Campaigns/etapas do Canvas de notificação por push de todas as Campaigns/etapas do Canvas para um usuário a cada 1 semana.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Então, o comportamento esperado é que:**

- Esse usuário receberá os envios da Campaign acionados na segunda-feira e na quarta-feira.
- Esse usuário não receberá o terceiro envio da Campaign na quinta-feira porque já recebeu dois envios de Campaign de push naquela semana.

{% endtab %}
{% endtabs %}

### Limite de frequência por tag {#frequency-capping-by-tag}

As [regras de limite de frequência](#delivery-rules) podem ser aplicadas a espaços de trabalho usando tags específicas que você aplicou às suas Campaigns e Canvas, permitindo que você essencialmente baseie seu limite de frequência em grupos com nomes personalizados.

Com o limite de frequência por tag, as regras podem ser definidas nas tags principais e aninhadas, então a Braze levará em conta todas as tags. Por exemplo, se você selecionou usar a tag principal A como limite de frequência, também incluiremos informações de todas as tags aninhadas (por exemplo, tags B e C) ao determinar o limite.

Você também pode combinar o limite de frequência regular com o limite de frequência por tags. Considere as seguintes regras:

1. No máximo três Campaigns ou componentes do Canvas de notificação por push por semana de todas as Campaigns e etapas do Canvas. <br>**E**
2. No máximo duas Campaigns ou componentes do Canvas de notificação por push por semana com a tag `promotional`.

![Seção de limite de frequência com duas regras limitando quantas Campaigns/Canvas de notificação por push podem ser enviadas a um usuário a cada 1 semana.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Como resultado, seus usuários receberão no máximo três envios de Campaign por semana em todas as Campaigns e etapas do Canvas e no máximo duas Campaigns ou componentes do Canvas de notificação por push com a tag `promotional`.

{% alert important %}
Os Canvas são marcados com tags no nível do Canvas, ao contrário da marcação por componente. Portanto, cada componente do Canvas herdará todas as tags do nível do Canvas.
{% endalert %}

#### Regras conflitantes {#conflicting-rules}

Quando as regras entram em conflito, a regra de limite de frequência mais restritiva e aplicável é aplicada aos seus usuários. Por exemplo, digamos que você tenha as seguintes regras:

1. No máximo uma Campaign ou componente do Canvas de notificação por push por semana de todas as Campaigns e componentes do Canvas. <br>**E**
2. No máximo três Campaigns ou componentes do Canvas de notificação por push por semana com a tag `promotional`.

![Seção de limite de frequência com regras conflitantes para limitar quantas Campaigns/etapas do Canvas de notificação por push são enviadas a um usuário a cada 1 semana.]({% image_buster /assets/img/global_rules.png %} "global rules")

Neste exemplo, seu usuário não receberá mais de uma Campaign ou componente do Canvas de notificação por push com a tag "promotional" em uma determinada semana, porque você especificou que os usuários não devem receber mais de uma Campaign ou componente do Canvas de notificação por push de todas as Campaigns e componentes do Canvas. Em outras palavras, a regra de frequência mais restritiva aplicável é a regra que será aplicada a um determinado usuário.

#### Contagem de tags {#tag-count}

As regras de limite de frequência por tag são calculadas no momento em que a mensagem é enviada. Isso significa que o limite de frequência por tag conta apenas as tags que estão atualmente nas Campaigns ou Canvas que um usuário recebeu no passado. Não conta as tags que estavam nas Campaigns ou Canvas no momento em que foram enviados, mas que foram removidas desde então. Conta se uma tag é adicionada posteriormente a uma mensagem que um usuário recebeu no passado, mas antes que a mensagem mais recente com tag seja enviada.

##### Caso de uso {#use-case}

Considere as seguintes Campaigns e regra de limite de frequência por tag:

**Campaigns**:

- **Campaign A** é uma Campaign de push marcada como `promotional`. Está programada para ser enviada às 9h de segunda-feira.
- **Campaign B** é uma Campaign de push marcada como `promotional`. Está programada para ser enviada às 9h de quarta-feira.

**Regra de limite de frequência por tag:**

- Seu usuário deve receber no máximo uma Campaign de notificação por push por semana com a tag `promotional`.<br><br>

| Ação | Resultado |
|---|---|
| A tag `promotional` é removida da **Campaign A** depois que seu usuário recebeu a mensagem, mas antes da **Campaign B ser enviada.** | Seu usuário recebe a **Campaign B**. |
| A tag `promotional` é removida por engano da **Campaign A** depois que seu usuário recebeu a mensagem. <br> A tag é adicionada de volta à **Campaign A** na terça-feira, antes da **Campaign B** ser enviada. | Seu usuário não recebe a **Campaign B**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Caso de uso" }

#### Envio em grande escala {#sending-at-large-scales}

As regras de limite de frequência por tag podem não ser aplicadas corretamente em grande escala, como 100 mensagens por canal de Campaigns ou componentes do Canvas.

Por exemplo, se sua regra de limite de frequência por tag é:

> No máximo duas Campaigns ou componentes do Canvas de e-mail com a tag `Promotional` para um usuário a cada semana.

E você envia ao usuário mais de 100 e-mails de Campaigns e etapas do Canvas com limite de frequência ativado ao longo de uma semana, mais de dois e-mails podem ser enviados ao usuário.

Como 100 mensagens por canal são mais mensagens do que a maioria das marcas envia para seus usuários, é improvável que você seja impactado por essa limitação. Para evitar essa limitação, você pode definir um limite para o número máximo de e-mails que deseja que seus usuários recebam ao longo de uma semana.

Por exemplo, você pode configurar a seguinte regra:

> No máximo três Campaigns ou componentes do Canvas de e-mail por semana de todas as Campaigns e etapas do Canvas.

Essa regra determina que nenhum usuário receba mais de 100 e-mails por semana porque, no máximo, os usuários recebem três e-mails por semana de Campaigns ou componentes do Canvas com limite de frequência ativado.

## Perguntas frequentes {#frequently-asked-questions}

### Se eu alterar a limitação de envio em um Canvas ativo, isso afeta os usuários que já estão no Canvas? {#if-i-change-a-send-throttle-on-an-active-canvas-does-it-affect-users-already-in-the-canvas}

Sim. Quando você aumenta ou diminui o limite de taxa de um Canvas, o limite atualizado entra em vigor para novas mensagens em aproximadamente 30 segundos após a alteração, devido ao cache.

### O limite de frequência faz com que os usuários saiam de um Canvas? {#does-frequency-capping-cause-users-to-exit-a-canvas}

Não. Se um usuário do Canvas é limitado por frequência devido às configurações de limite de frequência global, o usuário avança imediatamente para a próxima etapa do Canvas. O usuário **não** sai do Canvas por causa do limite de frequência.

### Como posso identificar usuários que foram limitados por frequência em um Canvas? {#how-can-i-identify-users-who-were-frequency-capped-in-a-canvas}

Usuários que são limitados por frequência não geram um evento de envio para aquela etapa. Para identificar esses usuários, você pode usar o [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) para rastrear eventos de mensagens limitadas por frequência. Como alternativa, você pode criar uma [extensão de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) para analisar usuários que entraram no Canvas, mas não receberam a mensagem esperada.

### Por que o dashboard mostra um erro de limite de taxa para minha Campaign? {#why-does-the-dashboard-show-a-rate-limit-error-for-my-campaign}

Isso geralmente significa que o [limite de taxa de velocidade de entrega](#delivery-speed-rate-limiting) da Campaign está definido muito baixo para o tamanho do público, então concluir o envio levaria mais tempo do que a janela permitida e a Braze exibe um aviso. Aumente o limite de taxa de velocidade de entrega, reduza o público ou use **Limitar o número de pessoas que receberão esta Campaign** para que cada ocorrência agendada termine dentro da janela de envio permitida. Você também pode definir um [limite de taxa de envio de mensagens do espaço de trabalho]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits/) para aplicar um limite em todas as Campaigns.

**Limitar o número de pessoas que receberão esta Campaign** controla quantos usuários são elegíveis para um envio, não quantas mensagens a Braze envia por minuto. Apenas um limite de taxa de velocidade de entrega define o desempenho por minuto.

### O que significa "Enviado" para o limite de frequência? {#what-does-sent-mean-for-frequency-capping}

Em análise de dados e limite de frequência, _Enviado_ refere-se ao momento em que a Braze despacha a mensagem (o envio é registrado), não à entrega final garantida ao dispositivo ou caixa de entrada. O limite de frequência e as contagens de envio usam esses eventos de envio registrados, que podem diferir das métricas de "entregue" downstream.

### Por que estou vendo bounces ou adiamentos de e-mail? {#why-am-i-seeing-email-bounces-or-deferrals}

Mensagens de bounce e adiamento de e-mail usam muitos códigos diferentes e textos específicos de provedores. Não trate um código específico como sinal de um problema de limite de taxa, pois a causa depende do seu contexto de envio e do feedback do provedor de caixa de entrada.

Se as mensagens estão sendo temporariamente adiadas, enviar menos pode ajudar a curto prazo. Use um [limite de taxa de velocidade de entrega](#delivery-speed-rate-limiting), **Limitar o número de pessoas que receberão esta Campaign**, ou ambos.

Para uma solução de longo prazo, trabalhe com um especialista em entregabilidade para revisar seus dados de bounce e adiamento.