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

## Sobre limite de taxa {#about-rate-limiting}

A Braze permite que você controle a pressão de marketing limitando a taxa das suas campanhas, regulando a quantidade de tráfego de saída da sua plataforma. Você pode implementar dois tipos diferentes de limite de taxa para suas campanhas:

1. [Limite de taxa centrado no usuário:](#user-centric-rate-limiting) Foca em proporcionar a melhor experiência para o usuário.
2. [Limite de taxa de velocidade de entrega:](#delivery-speed-rate-limiting) Leva em consideração a largura de banda dos seus servidores.

A Braze não oferece suporte a limite de taxa por segundo. A Braze tenta distribuir os envios de mensagens uniformemente ao longo do minuto, mas não pode garantir isso. Por exemplo, se você tem uma campanha com um limite de taxa de 5.000 mensagens por minuto, tentamos distribuir as 5.000 solicitações uniformemente ao longo do minuto (cerca de 84 mensagens por segundo), mas pode haver alguma variação na taxa por segundo.

### Limite de taxa centrado no usuário {#user-centric-rate-limiting}

À medida que você cria mais segmentos, haverá casos em que a composição desses segmentos se sobrepõe. Se você está enviando campanhas para esses segmentos, é importante garantir que não está enviando mensagens aos seus usuários com muita frequência. Se um usuário recebe muitas mensagens em um curto período, ele se sentirá sobrecarregado e poderá desativar as notificações por push ou desinstalar seu app.

#### Filtros de segmento relevantes {#relevant-segment-filters}

A Braze fornece os seguintes filtros para ajudar você a limitar a taxa com que seus usuários recebem mensagens:

- Last Engaged With Message
- Last Received Any Message
- Last Received Push
- Last Received Email
- Last Received SMS

#### Implementando filtros {#implementing-filters}

Digamos que criamos um segmento chamado "Retargeting Filter Showcase" com o filtro "Last used app more than 7 days ago" para direcionar usuários. Esse seria um segmento padrão de reengajamento.

Se você tem outros segmentos mais direcionados recebendo notificações recentemente, talvez não queira que seus usuários sejam direcionados por campanhas mais genéricas voltadas a esse segmento. Ao adicionar o filtro "Last Received Push" a esse segmento, o usuário garante que, se recebeu outra notificação nas últimas 24 horas, sairá desse segmento pelas próximas 24 horas. Se ele ainda atender aos outros critérios do segmento 24 horas depois e não tiver recebido mais notificações, voltará ao segmento.

![Um segmento chamado "Retargeting Filter Showcase" com o grupo de filtros "Last used app more than 7 days ago".]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"}

Adicionar esse filtro a todos os segmentos direcionados por campanhas faria com que seus usuários recebessem no máximo um push a cada 24 horas. Você poderia então priorizar suas mensagens garantindo que as mais importantes sejam entregues antes das menos importantes.

#### Definindo um limite máximo de usuários {#setting-a-maximum-user-cap}

Na etapa **Públicos-alvo** do criador de campanhas, você também pode limitar o número total de usuários que receberão sua mensagem. Isso funciona como uma verificação independente dos filtros da sua campanha.

![Resumo do público com uma caixa de seleção marcada para limitar o número de pessoas que recebem a campanha.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"}

Ao selecionar o limite máximo de usuários, você pode limitar o volume de mensagens enviadas por canal ou globalmente em todos os tipos de mensagem. A Braze não despacha mensagens para usuários atribuídos a grupos de controle, então eles não contam para o limite.

{% alert note %}
O limite máximo de usuários limita o número de usuários despachados, não o número de mensagens enviadas com sucesso. Como mensagens interrompidas contam para esse limite, o número real de mensagens enviadas pode ser menor que o limite configurado. Por exemplo, se você definir um limite de 10.000 e 2.000 mensagens forem interrompidas devido à lógica Liquid ou outras condições, apenas 8.000 mensagens serão enviadas.
{% endalert %}

##### Limite máximo de usuários para campanhas multicanal {#maximum-user-cap-for-multichannel-campaigns}

Para campanhas multicanal, a Braze primeiro seleciona um público até o limite máximo de usuários configurado. Em seguida, a Braze avalia cada usuário desse público limitado para cada canal da campanha.

Como resultado, o tamanho do público limitado permanece o mesmo, mas os envios por canal podem variar com base na elegibilidade do canal. Por exemplo, se você definir um limite máximo de 500.000 usuários e um usuário for elegível apenas para push e Content Cards, esse usuário receberá esses canais, mas não e-mail.

Se você dividir esses canais em campanhas separadas, cada uma direcionada ao mesmo segmento e com seu próprio limite máximo de usuários, cada campanha avalia e limita os usuários de forma independente. A Braze não garante que cada campanha selecione exatamente o mesmo subconjunto de usuários.

Se você precisa que campanhas de acompanhamento direcionem usuários que receberam uma campanha anterior, crie um segmento usando o filtro **Received Campaign** e use esse segmento para as campanhas de acompanhamento.

##### Limite máximo de usuários com otimizações {#maximum-user-cap-with-optimizations}

Se você está usando uma otimização como variante vencedora ou variante personalizada, a campanha consistirá em dois envios: o experimento inicial e o envio final.

Para configurar um limite máximo de usuários nesse cenário, selecione **Limitar o número de pessoas que receberão esta campanha**, depois selecione **No total, esta campanha deve** e insira um limite de público. Seu limite de público será dividido pelas porcentagens mostradas no painel **Testes A/B**.

Se você selecionar **Toda vez que a campanha for agendada**, essas duas fases serão limitadas separadamente ao número definido. Isso normalmente não é desejável.

#### Definindo um limite máximo de impressões em campanhas {#setting-a-maximum-impression-cap-on-campaigns}

Para mensagens no app, você pode controlar a pressão de marketing definindo um número máximo de impressões que serão exibidas à sua base de usuários, após o qual a Braze não enviará mais mensagens aos seus usuários. No entanto, é importante observar que esse limite não é exato.

As regras de mensagens no app são enviadas ao app no início da sessão, o que significa que a Braze pode enviar uma mensagem ao usuário antes que o limite seja atingido, mas quando o usuário dispara a mensagem, o limite já foi atingido. Nessa situação, o dispositivo ainda exibirá a mensagem.

Por exemplo, digamos que você tem um jogo com uma mensagem no app que é disparada quando um usuário passa de fase, e você limita a 100 impressões. Até agora, houve 99 impressões. Alice e Bob abrem o jogo, e a Braze informa aos dispositivos deles que são elegíveis para receber a mensagem quando passarem de fase. Alice passa de fase primeiro e recebe a mensagem. Bob passa de fase em seguida, mas como seu dispositivo não se comunicou com os servidores da Braze desde o início da sessão, seu dispositivo não sabe que a mensagem atingiu o limite, e ele também recebe a mensagem. No entanto, quando o limite de impressões é atingido, na próxima vez que qualquer dispositivo solicitar a lista de mensagens no app elegíveis, o sistema não enviará essa mensagem e a removerá daquele dispositivo.

### Limite de taxa e testes A/B {#rate-limiting-and-ab-testing}

Ao usar limite de taxa com um teste A/B, o limite de taxa não é aplicado ao grupo de controle da mesma forma que ao grupo de teste, o que é uma fonte potencial de viés temporal. Para evitar esse viés, use janelas de conversão apropriadas.

### Limite de taxa de velocidade de entrega {#delivery-speed-rate-limiting}

Se você prevê que grandes campanhas causarão um pico na atividade dos usuários e sobrecarregarão seus servidores, você pode especificar um limite de taxa por minuto para o envio de mensagens, o que significa que a Braze não envia mais do que a configuração de limite de taxa dentro de um minuto.

Ao direcionar usuários durante a criação da campanha, você pode navegar até **Públicos-alvo** (para campanhas) ou **Configurações de envio** (para Canvas) para selecionar um limite de taxa (em vários incrementos, de 10 até 500.000 mensagens por minuto).

Observe que campanhas sem limite de taxa podem exceder esses limites de entrega. No entanto, esteja ciente de que as mensagens serão interrompidas se forem atrasadas em 72 horas ou mais devido a um limite de taxa baixo. Se o limite de taxa for muito baixo, o criador da campanha receberá alertas no dashboard e por e-mail.

{% alert tip %}
Defina um [limite de taxa de envio de mensagens do espaço de trabalho]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) para aplicar um limite de taxa em todo o espaço de trabalho.
{% endalert %}

#### Exemplo {#example}

Se você está tentando enviar 75.000 mensagens com um limite de taxa de 10.000 por minuto, a entrega será distribuída ao longo de oito minutos. Sua campanha entregará no máximo 10.000 mensagens em cada um dos primeiros sete minutos e 5.000 no último minuto.

#### Número de envios {#number-of-sends}

Observe que mensagens com limite de taxa podem não ser enviadas uniformemente ao longo de cada minuto. Usando o exemplo de um limite de taxa de 10.000 por minuto, isso significa que a Braze garante que não mais de 10.000 mensagens sejam enviadas por minuto. Isso pode significar que uma porcentagem maior das 10.000 mensagens é enviada na primeira metade do minuto em comparação com a segunda metade.

O limite de taxa é aplicado no início da tentativa de envio da mensagem. Quando há flutuações no tempo necessário para concluir o envio, o número de envios concluídos pode exceder ligeiramente o limite de taxa por alguns minutos. Com o tempo, o número de envios por minuto se estabilizará em não mais do que o limite de taxa.

{% alert important %}
Tenha cuidado ao atrasar mensagens urgentes com essa forma de limite de taxa em relação ao número total de usuários em um segmento. Por exemplo, se o segmento contém 30 milhões de usuários, mas definimos o limite de taxa para 10.000 por minuto, uma grande parte da sua base de usuários não receberá a mensagem até o dia seguinte.
{% endalert %}

#### Campanhas multicanal e Canvas {#multichannel-campaigns-and-canvases}

Ao definir um limite de taxa de velocidade de entrega para uma campanha multicanal ou Canvas, você pode optar por definir um limite de taxa compartilhado ou um limite baseado em canal.

Quando uma campanha multicanal ou Canvas usa um limite de taxa compartilhado, isso significa que o número total de mensagens enviadas por minuto pela campanha ou Canvas não excede o limite de taxa. Por exemplo, se seu Canvas tem um limite de taxa de 500.000 por minuto e contém etapas de mensagem de e-mail e SMS, a Braze envia um total de 500.000 mensagens por minuto entre e-mail e SMS.

![A opção de limitar a taxa de envio da campanha, selecionada com 500.000 mensagens por minuto.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"}

Quando uma campanha multicanal ou Canvas usa limite de taxa baseado em canal, o limite de taxa será aplicado a cada um dos canais selecionados. Por exemplo, você pode configurar sua campanha ou Canvas para enviar no máximo 5.000 webhooks e 2.500 mensagens SMS por minuto em toda a campanha ou Canvas.

![Limites de taxa separados para dois canais, webhook e SMS/MMS/RCS, com 5.000 e 2.500 mensagens por minuto respectivamente.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Notificações por push {#push-notifications}

Para campanhas ou Canvas com plataformas de push (como Android, iOS, Web Push ou Kindle), você pode selecionar **Notificações por push** para aplicar um limite de taxa compartilhado entre todas as plataformas de push na sua campanha ou Canvas.

![O menu suspenso de canal com opções para plataformas de push e notificações por push.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"}

Se você selecionar um limite para notificações por push, não poderá definir limites de taxa individuais por canal de push. Da mesma forma, se você selecionar limites para canais de push individuais, não poderá definir limites compartilhados de notificações por push.

{% alert important %}
**Atualizações na interface de limite de taxa**<br>
A Braze atualizou a interface de limite de taxa para fornecer mais transparência e controle sobre como os limites de taxa se aplicam a campanhas multicanal e Canvas.<br><br>

- **Campanhas e Canvas existentes:** Todas as campanhas e Canvas existentes foram migrados para esta interface. O comportamento de entrega permanece o mesmo. O dashboard exibe se a campanha usa lógica compartilhada ou por canal.<br>
- **Novas campanhas e Canvas:** Para todas as novas campanhas e Canvas, há um botão de alternância manual para escolher a lógica de limite de taxa preferida. Certifique-se de selecionar o comportamento de limite de taxa que se alinha com o comportamento pretendido ao definir ou atualizar um limite de taxa de campanha ou Canvas.
{% endalert %}

##### Considerações sobre limite de taxa {#rate-limiting-considerations}

Algumas observações a ter em mente ao configurar limites de taxa e o comportamento esperado:

- Envios de SMS estão sujeitos a um limite de taxa de 50.000 por grupo de inscrições. Alguns provedores de SMS podem aplicar outros limites.
- As seguintes mensagens não serão limitadas ou contabilizadas no limite de taxa:
    - Envios de teste
    - Grupos de teste
    - Content Cards configurados para criar "na primeira impressão" (Isso será controlado pela taxa de impressões do app. Consulte [Criação de cartão]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences) para mais informações sobre as diferenças entre as opções de criação de cartão.)
- Limites de velocidade de entrega não são suportados para os seguintes itens:
    - Respostas automáticas de SMS
    - Mensagens com SLA garantido (como [E-mail de transação]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email))
    - Mensagens no app
    - Feature Flags
    - Banners

#### Limite de taxa e novas tentativas de Connected Content {#rate-limiting-and-connected-content-retries}

Quando a [nova tentativa de Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries) está ativada, a Braze tentará novamente as chamadas com falha respeitando o limite de taxa que você definiu para cada reenvio. Vamos considerar o cenário de envio de 75.000 mensagens com um limite de taxa de 10.000 por minuto. Imagine que no primeiro minuto, a chamada falha ou é lenta e envia apenas 4.000 mensagens.

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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Limite de taxa e novas tentativas de Connected Content" }

As solicitações de Connected Content não são limitadas de forma independente e seguirão o limite de taxa do webhook. Isso significa que, se houver uma chamada de Connected Content para um endpoint único por webhook, você esperaria 5.000 webhooks e também 5.000 chamadas de Connected Content por minuto. Observe que o cache pode afetar isso e reduzir o número de chamadas de Connected Content. Além disso, as novas tentativas podem aumentar as chamadas de Connected Content, então recomendamos verificar se o endpoint de Connected Content pode lidar com alguma flutuação.

{% alert note %}
**Limites de taxa são limites de velocidade e não definem uma velocidade exata de envio.** Geralmente, as mensagens são distribuídas uniformemente dentro de qualquer minuto, e na grande maioria dos casos, são enviadas no limite configurado ou muito próximo dele. Nem sempre é assim — por exemplo, quando as mensagens são muito grandes (como e-mails com muitos Content Blocks, tags de Connected Content ou tags de itens de catálogo), ou quando há muitas interrupções Liquid (mensagens interrompidas ainda consomem um slot e podem reduzir as taxas efetivas de envio).<br><br>
Na prática, a taxa de envio sustentada (mensagens concluídas por minuto) pode ser menor que o limite de taxa configurado devido a novas tentativas, variabilidade de rede, latência do endpoint de destino e suavização por minuto. Se você observar consistentemente uma taxa de transferência significativamente menor do que o esperado, verifique os tempos de resposta do Connected Content, taxas de erro (como `429`) e comportamento de novas tentativas.
{% endalert %}

## Sobre o limite de frequência {#about-frequency-capping}

À medida que sua base de usuários continua a crescer e seu envio de mensagens se expande para incluir campanhas de ciclo de vida, disparadas, transacionais e de conversão, é importante evitar que suas notificações pareçam "spam" ou sejam disruptivas. Ao fornecer maior controle sobre a experiência dos seus usuários, o limite de frequência permite que você crie as campanhas que deseja sem sobrecarregar seu público.

### Use o limite de taxa e o limite de frequência juntos {#use-rate-limiting-and-frequency-capping-together}

Quando você ativa tanto o limite de taxa quanto o limite de frequência em uma campanha, a Braze os aplica na seguinte ordem:

1. **O limite de taxa** é aplicado primeiro para selecionar o grupo inicial de usuários que podem receber mensagens.
2. **O limite de frequência** é aplicado em seguida para filtrar usuários desse grupo.
3. **As mensagens são enviadas** para os usuários restantes.

{% alert important %}
Se muitos usuários no seu grupo com limite de taxa estiverem com limite de frequência, você pode enviar menos mensagens do que o valor do seu limite de taxa. A Braze não preenche usuários adicionais do limite de taxa depois que o limite de frequência remove usuários do grupo de envio.
{% endalert %}

#### Exemplo

Com um limite de taxa de 500 usuários e o limite de frequência ativado, se 200 desses 500 usuários com limite de taxa estiverem com limite de frequência, apenas 300 mensagens serão enviadas — não 500.

#### Recomendações {#recommendations}

Se você precisa alcançar um número específico de usuários ao usar ambos os recursos juntos, considere as seguintes abordagens:

- **Aumente seu limite de taxa:** para compensar os usuários que estão com limite de frequência. Por exemplo, se você deseja alcançar 500 usuários, mas espera que alguns estejam com limite de frequência, defina seu limite de taxa mais alto (como 1.000 usuários).
- **Use apenas o limite de taxa:** se seu objetivo é controlar o volume de mensagens enviadas por campanha.
- **Fale com seu gerente de sucesso do cliente:** para obter ajuda no design de uma estratégia de envio de mensagens robusta que equilibre necessidades de negócio e considerações técnicas.

### Visão geral do recurso {#freq-cap-feat-over}

O limite de frequência é aplicado no nível de envio da campanha ou do componente do Canvas e pode ser configurado para cada espaço de trabalho em **Configurações** > **Regras de limite de frequência**.

Por padrão, o limite de frequência é ativado quando novas campanhas são criadas. A partir daí, você pode escolher o seguinte:

- O canal de envio de mensagens que você deseja limitar: push, e-mail, SMS, webhook, WhatsApp, LINE ou qualquer um desses canais.
- Quantas vezes cada usuário deve receber uma campanha ou componente do Canvas enviado por um canal dentro de um determinado período.
- Quantas vezes cada usuário deve receber uma campanha ou componente do Canvas enviado por [tag](#frequency-capping-by-tag) dentro de um determinado período.

Esse período pode ser medido em minutos, dias ou semanas (sete dias), com duração máxima de 30 dias.

Cada linha de limites de frequência é conectada usando o operador `AND`, e você pode adicionar até 10 regras por espaço de trabalho. Você pode incluir vários limites para os mesmos tipos de mensagem. Por exemplo, você pode limitar os usuários a no máximo um push por dia e no máximo três pushes por semana. Mensagens com interrupção não contam para o limite de frequência.

![Seção de limite de frequência com listas de campanhas e Canvas aos quais as regras serão e não serão aplicadas.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"}

#### Comportamento quando os usuários estão com limite de frequência ou uma mensagem é interrompida em uma etapa do Canvas {#behavior-when-users-are-frequency-capped-or-a-message-is-aborted-on-a-canvas-step}

O limite de frequência global sozinho não faz os usuários saírem de um Canvas. Nas [etapas de Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step), os usuários ainda avançam quando uma mensagem não é enviada por causa do limite de frequência global, de acordo com [como os usuários avançam]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance) pela etapa. O mesmo se aplica quando uma mensagem é interrompida (por exemplo, por uma condição de interrupção Liquid): o usuário continua pelo Canvas como se a mensagem tivesse sido enviada.

Isso é separado das **Validações de entrega** em uma etapa de Mensagem. Se um usuário não atender aos critérios de validação de entrega no momento do envio, ele pode sair do Canvas nessa etapa.

### Regras de entrega {#delivery-rules}

Pode haver algumas campanhas, como mensagens transacionais, que você deseja que sempre cheguem ao usuário, mesmo que ele já tenha atingido seu limite de frequência. Por exemplo, um app de entregas pode querer enviar um e-mail ou push quando um item é entregue, independentemente de quantas campanhas o usuário já recebeu.

Se você deseja que uma campanha específica ignore as regras de limite de frequência, pode configurar isso no dashboard da Braze ao agendar a entrega dessa campanha, alternando **Limite de frequência** para **DESATIVADO**.

Depois disso, será perguntado se você ainda deseja que essa campanha conte para o seu limite de frequência. Mensagens que contam para o limite de frequência são incluídas nos cálculos do filtro de canal inteligente.

Ao enviar [campanhas via API]({{site.baseurl}}/developer_guide/rest_api/messaging#messaging), que geralmente são transacionais, você terá a possibilidade de especificar que uma campanha deve ignorar as regras de limite de frequência definindo `override_frequency_capping` como `true` na requisição da API.

Por padrão, novas campanhas e Canvas que não obedecem aos limites de frequência também não contam para eles. Isso é configurável para cada campanha e Canvas.

{% alert note %}
Esse comportamento altera o comportamento padrão quando você desativa o limite de frequência para uma campanha ou Canvas. As alterações são retrocompatíveis e não afetam mensagens que estão ativas no momento.
{% endalert %}

![Seção de controles de entrega com o limite de frequência ativado.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"}

#### Como os envios contam para os limites {#how-sends-count-toward-caps}

O limite de frequência é aplicado por despacho: cada vez que a Braze envia uma campanha ou componente do Canvas para um usuário conta para seus limites — não cada variante de mensagem ou plataforma dentro desse envio. Por exemplo, se os usuários estão limitados a cinco campanhas de push por semana, eles não recebem nenhuma campanha de push após o quinto despacho até que o limite seja redefinido.

##### Envios multicanal {#multichannel-sends}

Quando um único despacho usa vários canais, esse despacho conta no máximo uma vez por regra de limite de frequência aplicável. Por exemplo, se você criar uma campanha multicanal que envia e-mail, push para iOS e push para Android em uma única entrega e seu espaço de trabalho tiver regras para push e e-mail, além de uma regra que se aplica a todos os canais, essa entrega conta uma vez para a regra de push, uma vez para a regra de e-mail e uma vez para a regra de todos os canais — ela não conta uma vez por plataforma de push ou por mensagem dentro do envio. Se os usuários estão limitados a uma campanha de push e uma de e-mail por dia e recebem essa campanha multicanal, eles não são elegíveis para campanhas adicionais de push ou e-mail pelo resto do dia, a menos que uma campanha ignore as regras de limite de frequência.

In-App Messages e Content Cards não são contados como ou para limites em campanhas ou componentes do Canvas de qualquer tipo.

##### Notificações por push com vários dispositivos {#push-notifications-with-multiple-devices}

Para campanhas de push, o limite de frequência conta no nível da campanha ou do componente do Canvas, não por dispositivo individual. Se um perfil de usuário tem vários dispositivos registrados para push (por exemplo, um iPhone e um iPad), um limite de frequência no nível da campanha conta isso como um envio, independentemente de quantos dispositivos recebem a notificação. Isso é semelhante a como uma campanha recorrente com cadência diária conta como um envio por dia, mesmo que ela se repita várias vezes ao longo da semana.

{% alert important %}
O limite de frequência global é agendado com base no fuso horário do usuário e é calculado por dias corridos, não por períodos de 24 horas. Por exemplo, se você configurar uma regra de limite de frequência para enviar no máximo uma campanha por dia, um usuário pode receber uma mensagem às 23h no seu fuso local e seria elegível para receber outra mensagem uma hora depois.
{% endalert %}

#### Casos de uso {#use-cases}

{% tabs %}
{% tab Caso de uso 1 %}

Digamos que você defina uma regra de limite de frequência para que seus usuários recebam no máximo três campanhas de notificação por push ou etapas do Canvas por semana de todas as campanhas ou etapas do Canvas.

Se seu usuário está programado para receber três notificações por push, duas mensagens no app e um cartão de conteúdo nesta semana, ele receberá todas essas mensagens.

{% endtab %}
{% tab Caso de uso 2 %}

Este cenário usa uma regra de limite de frequência para que os usuários recebam no máximo duas campanhas de notificação por push ou etapas do Canvas por semana de todas as campanhas ou etapas do Canvas.

**Quando o seguinte cenário ocorre:**

- Um usuário dispara a mesma campanha `Campaign ABC` três vezes ao longo de uma semana.
- Esse usuário dispara `Campaign ABC` uma vez na segunda-feira, uma vez na quarta-feira e uma vez na quinta-feira.

![Seção de limite de frequência com a regra de enviar no máximo 2 campanhas de notificação por push/etapas do Canvas de todas as campanhas/etapas do Canvas para um usuário a cada 1 semana.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Então, o comportamento esperado é que:**

- Esse usuário receberá os envios da campanha disparados na segunda-feira e na quarta-feira.
- Esse usuário não receberá o terceiro envio da campanha na quinta-feira porque já recebeu dois envios de campanha de push naquela semana.

{% endtab %}
{% endtabs %}

### Limite de frequência por tag {#frequency-capping-by-tag}

As [regras de limite de frequência](#delivery-rules) podem ser aplicadas a espaços de trabalho usando tags específicas que você aplicou às suas campanhas e Canvas, permitindo que você essencialmente baseie seu limite de frequência em grupos com nomes personalizados.

Com o limite de frequência por tag, as regras podem ser definidas nas tags principais e aninhadas, então a Braze levará em conta todas as tags. Por exemplo, se você selecionou usar a tag principal A como limite de frequência, também incluiremos informações de todas as tags aninhadas (por exemplo, tags B e C) ao determinar o limite.

Você também pode combinar o limite de frequência regular com o limite de frequência por tags. Considere as seguintes regras:

1. No máximo três campanhas de notificação por push ou componentes do Canvas por semana de todas as campanhas e etapas do Canvas. <br>**E**
2. No máximo duas campanhas de notificação por push ou componentes do Canvas por semana com a tag `promotional`.

![Seção de limite de frequência com duas regras limitando quantas campanhas de notificação por push/Canvas podem ser enviadas a um usuário a cada 1 semana.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Como resultado, seus usuários receberão no máximo três envios de campanha por semana de todas as campanhas e etapas do Canvas e no máximo duas campanhas de notificação por push ou componentes do Canvas com a tag `promotional`.

{% alert important %}
Os Canvas são marcados com tags no nível do Canvas, e não por componente. Portanto, cada componente do Canvas herdará todas as tags do nível do Canvas.
{% endalert %}

#### Regras conflitantes {#conflicting-rules}

Quando as regras entram em conflito, a regra de limite de frequência mais restritiva e aplicável é aplicada aos seus usuários. Por exemplo, digamos que você tenha as seguintes regras:

1. No máximo uma campanha de notificação por push ou componente do Canvas por semana de todas as campanhas e componentes do Canvas. <br>**E**
2. No máximo três campanhas de notificação por push ou componentes do Canvas por semana com a tag `promotional`.

![Seção de limite de frequência com regras conflitantes para limitar quantas campanhas de notificação por push/etapas do Canvas são enviadas a um usuário a cada 1 semana.]({% image_buster /assets/img/global_rules.png %} "global rules")

Neste exemplo, seu usuário não receberá mais de uma campanha de notificação por push ou componente do Canvas com a tag "promotional" em uma determinada semana, porque você especificou que os usuários não devem receber mais de uma campanha de notificação por push ou componente do Canvas de todas as campanhas e componentes do Canvas. Em outras palavras, a regra de frequência mais restritiva aplicável é a regra que será aplicada a um determinado usuário.

#### Contagem de tags {#tag-count}

As regras de limite de frequência por tag são calculadas no momento em que uma mensagem é enviada. Isso significa que o limite de frequência por tag conta apenas as tags que estão atualmente nas campanhas ou Canvas que um usuário recebeu no passado. Ele não conta as tags que estavam nas campanhas ou Canvas no momento em que foram enviados, mas que foram removidas desde então. Ele conta se uma tag é adicionada posteriormente a uma mensagem que um usuário recebeu no passado, mas antes que a mensagem mais recente com tag seja enviada.

##### Caso de uso {#use-case}

Considere as seguintes campanhas e regra de limite de frequência por tag:

**Campanhas**:

- **Campaign A** é uma campanha de push com a tag `promotional`. Ela está programada para ser enviada às 9h da segunda-feira.
- **Campaign B** é uma campanha de push com a tag `promotional`. Ela está programada para ser enviada às 9h da quarta-feira.

**Regra de limite de frequência por tag:**

- Seu usuário deve receber no máximo uma campanha de notificação por push por semana com a tag `promotional`.<br><br>

| Ação | Resultado |
|---|---|
| A tag `promotional` é removida da **Campaign A** depois que seu usuário recebeu a mensagem, mas antes que a **Campaign B tenha sido enviada.** | Seu usuário recebe a **Campaign B**.|
| A tag `promotional` é removida por engano da **Campaign A** depois que seu usuário recebeu a mensagem. <br> A tag é adicionada de volta à **Campaign A** na terça-feira, antes que a **Campaign B** seja enviada. | Seu usuário não recebe a **Campaign B**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Caso de uso" }

#### Envio em grande escala {#sending-at-large-scales}

As regras de limite de frequência por tag podem não ser aplicadas corretamente em grande escala, como 100 mensagens por canal de campanhas ou componentes do Canvas.

Por exemplo, se sua regra de limite de frequência por tag é:

> No máximo duas campanhas de e-mail ou componentes do Canvas com a tag `Promotional` para um usuário a cada semana.

E você envia ao usuário mais de 100 e-mails de campanhas e etapas do Canvas com limite de frequência ativado ao longo de uma semana, mais de dois e-mails podem ser enviados ao usuário.

Como 100 mensagens por canal são mais mensagens do que a maioria das marcas envia aos seus usuários, é improvável que você seja impactado por essa limitação. Para evitar essa limitação, você pode definir um limite para o número máximo de e-mails que deseja que seus usuários recebam ao longo de uma semana.

Por exemplo, você pode configurar a seguinte regra:

> No máximo três campanhas de e-mail ou componentes do Canvas por semana de todas as campanhas e etapas do Canvas.

Essa regra garante que nenhum usuário receba mais de 100 e-mails por semana porque, no máximo, os usuários recebem três e-mails por semana de campanhas ou componentes do Canvas com limite de frequência ativado.

## Perguntas frequentes {#frequently-asked-questions}

### Se eu alterar a limitação de envio em um Canvas ativo, isso afeta os usuários que já estão no Canvas? {#if-i-change-a-send-throttle-on-an-active-canvas-does-it-affect-users-already-in-the-canvas}

Sim. Quando você aumenta ou diminui o limite de taxa de um Canvas, o limite atualizado entra em vigor para novas mensagens em aproximadamente 30 segundos após a alteração, devido ao cache.

### O limite de frequência faz com que os usuários saiam de um Canvas? {#does-frequency-capping-cause-users-to-exit-a-canvas}

Não. Se um usuário do Canvas for limitado por frequência devido às configurações globais de limite de frequência, ele avança imediatamente para a próxima etapa do Canvas. O usuário **não** sai do Canvas por causa do limite de frequência.

### Como posso identificar usuários que foram limitados por frequência em um Canvas? {#how-can-i-identify-users-who-were-frequency-capped-in-a-canvas}

Usuários limitados por frequência não geram um evento de envio para aquela etapa. Para identificar esses usuários, você pode usar o [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para rastrear eventos de mensagens limitadas por frequência. Como alternativa, você pode criar uma [extensão de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension) para analisar os usuários que entraram no Canvas, mas não receberam a mensagem esperada.

### Por que o dashboard mostra um erro de limite de taxa para minha campanha? {#why-does-the-dashboard-show-a-rate-limit-error-for-my-campaign}

Isso geralmente significa que o [limite de taxa de velocidade de entrega](#delivery-speed-rate-limiting) da campanha está definido muito baixo para o tamanho do público, de modo que concluir o envio levaria mais tempo do que a janela permitida, e a Braze exibe um alerta. Aumente o limite de taxa de velocidade de entrega, reduza o público ou use **Limit send volume** para que cada ocorrência agendada termine dentro da janela de envio permitida. Você também pode definir um [limite de taxa de envio de mensagens do espaço de trabalho]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) para aplicar um limite entre campanhas.

**Limit send volume** controla quantos usuários são elegíveis para um envio, não quantas mensagens a Braze envia por minuto. Somente um limite de taxa de velocidade de entrega define a taxa de envio por minuto.

### O que significa "Enviado" para o limite de frequência? {#what-does-sent-mean-for-frequency-capping}

Em análise de dados e limite de frequência, _Enviado_ refere-se ao momento em que a Braze despacha a mensagem (o envio é registrado), e não à entrega final garantida ao dispositivo ou à caixa de entrada. O limite de frequência e as contagens de envio usam esses eventos de envio registrados, que podem diferir das métricas de "entregue" posteriores.

### Por que estou vendo bounces ou adiamentos de e-mail? {#why-am-i-seeing-email-bounces-or-deferrals}

Mensagens de bounce e adiamento de e-mail usam muitos códigos diferentes e textos específicos de cada provedor. Não trate um código específico como sinal de um problema de limite de taxa, pois a causa depende do seu contexto de envio e do feedback do provedor de caixa de entrada.

Se as mensagens estiverem sendo temporariamente adiadas, enviar menos pode ajudar no curto prazo. Use um [limite de taxa de velocidade de entrega](#delivery-speed-rate-limiting), **Limit send volume**, ou ambos.

Para uma solução de longo prazo, trabalhe com um especialista em entregabilidade para revisar seus dados de bounce e adiamento.