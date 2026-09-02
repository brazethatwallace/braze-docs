---
nav_title: Criar um cartão de conteúdo
article_title: Criar um cartão de conteúdo
page_order: 1
description: "Este artigo de referência aborda como criar, redigir, configurar e enviar Content Cards usando Campaigns e Canvas da Braze."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Criar um cartão de conteúdo {#create-a-content-card}

> Este artigo aborda como criar um cartão de conteúdo na Braze ao construir Campaigns e Canvas. Aqui, vamos orientar você na escolha de um tipo de mensagem, na composição do seu cartão e na programação da entrega da mensagem.

## Etapa 1: Escolha onde criar sua mensagem {#step-1-choose-where-to-build-your-message}

Use Campaigns para envio de mensagens simples e únicas (como informar os usuários sobre um produto com uma única mensagem). Use Canvas para jornadas de usuário com várias etapas (como enviar sugestões de produtos personalizadas com base no comportamento do usuário ao longo do tempo).

{% tabs %}
{% tab Campaign %}

1. Acesse **Envio de mensagens** > **Campaigns** e selecione **Criar Campaign**.
2. Selecione **Content Cards** ou, para Campaigns direcionadas a vários canais, selecione **Multicanal**.
3. Dê à sua Campaign um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) conforme necessário.
   * Tags facilitam a busca e a criação de relatórios das suas Campaigns. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder), você pode filtrar pelas tags relevantes.
5. Adicione e nomeie quantas variantes quiser para a sua Campaign. Você pode escolher diferentes plataformas, tipos de mensagem e layouts para cada variante adicionada. Para saber mais sobre variantes, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Se todas as mensagens da sua Campaign forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes adicionais. Em seguida, selecione **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) usando o criador de Canvas.
2. Após configurar seu Canvas, adicione uma etapa de Mensagem no criador de Canvas. Dê à sua etapa um nome claro e significativo.
3. Selecione **Content Cards** como canal de envio de mensagens.
4. Escolha quando a Braze calcula a elegibilidade do público e a personalização para o Content Card. Isso pode ser na entrada da etapa ou na primeira impressão (recomendado). Etapas contendo Content Cards podem ser agendadas ou baseadas em ação.
5. Escolha se deseja remover Content Cards quando os usuários concluírem uma compra ou realizarem um evento personalizado.
6. Defina uma expiração para o Content Card (tempo no feed). Isso pode ser após um período de tempo ou em um momento específico.
7. Filtre seu público, ou os destinatários, para esta etapa conforme necessário nas **Configurações de entrega**. Você pode refinar ainda mais seu público especificando Segments e adicionando filtros adicionais. As opções de público são verificadas após a postergação, no momento em que as mensagens são enviadas.
8. Escolha quaisquer outros canais de envio de mensagens que você queira combinar com sua mensagem.

{% endtab %}
{% endtabs %}

## Etapa 2: Especifique seus tipos de mensagem {#step-2-specify-your-message-types}

Selecione um dos três tipos essenciais de Content Cards: **Clássico**, **Imagem com legenda** e **Somente imagem**.

Para saber mais sobre o comportamento esperado e a aparência de cada tipo, consulte [Detalhes criativos]({{site.baseurl}}/user_guide/channels/content_cards/creative_details) ou confira os links na tabela a seguir. Esses tipos de Content Cards são aceitos tanto por apps para dispositivos móveis quanto por aplicações web.

| Tipo de mensagem | Exemplo | Descrição |
|---|---|---|
| [Clássico]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![Um cartão de conteúdo clássico com um ícone pequeno e texto incentivando a reservar uma aula de treino.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) | O cartão Clássico tem um layout direto com título em negrito, texto da mensagem e uma imagem opcional que fica no início do título e do texto. É melhor usar uma imagem quadrada ou um ícone com o cartão Clássico. |
| [Imagem com legenda]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![Um cartão de conteúdo com legenda, mostrando a imagem de um halterofilista e texto incentivando a reservar uma aula de treino.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | O cartão Imagem com legenda destaca seu conteúdo com texto e uma imagem chamativa. |
| [Somente imagem]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![Um cartão de conteúdo somente com imagem, contendo apenas texto.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | O cartão Somente imagem chama a atenção com espaço para imagens, GIFs e outros conteúdos criativos sem texto. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 2: Especifique seus tipos de mensagem" }

## Etapa 3: Criar um Content Card {#step-3-compose-a-content-card}

Você pode editar todos os aspectos do conteúdo e do comportamento da sua mensagem na guia **Composição** do editor de mensagens.

![Exemplo de detalhes de Content Card na guia Composição do editor de mensagens.]({% image_buster /assets/img/content_card_compose.png %})

O conteúdo aqui varia com base no **Tipo de cartão** escolhido na etapa anterior, mas pode incluir qualquer uma das seguintes opções:

### Idioma {#language}

Selecione **Adicionar idiomas** para adicionar os idiomas desejados na lista fornecida. Isso insere [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) na sua mensagem. Recomendamos selecionar os idiomas antes de escrever o conteúdo para que você possa preencher o texto no local correto dentro do Liquid. Para consultar a lista completa de idiomas disponíveis, acesse [Idiomas suportados]({{site.baseurl}}/developer_guide/localization?tab=android).

![Uma janela com inglês, espanhol e francês selecionados como idiomas, e título, descrição e texto do link selecionados como campos para internacionalização.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

#### Criar mensagens da direita para a esquerda {#create-right-to-left-messages}

A aparência final das mensagens da direita para a esquerda depende em grande parte de como os provedores de serviço as renderizam. Para conferir as práticas recomendadas sobre como criar mensagens da direita para a esquerda que sejam exibidas com a maior precisão possível, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Título e mensagem {#title-and-message}

Escreva o que quiser. Não há limites, mas quanto mais rápido você conseguir transmitir sua mensagem e fazer o cliente clicar, melhor! Recomendamos títulos e conteúdos de mensagem claros e concisos. Esses campos não são fornecidos para cartões somente de imagem.

#### Imagem {#image}

Para adicionar uma imagem ao seu Content Card, selecione **Adicionar imagem** ou forneça um URL de imagem. Ao selecionar **Adicionar imagem**, a **Biblioteca de mídia** é aberta, onde você pode selecionar uma imagem carregada anteriormente ou adicionar uma nova.

Cada tipo de mensagem e plataforma pode ter suas próprias proporções e requisitos sugeridos. Por isso, verifique quais são antes de encomendar ou criar uma imagem do zero. Os campos de mensagem de Content Card são limitados a 2&nbsp;KB no tamanho total.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Fixar no topo {#pin-to-top}

A Braze exibe um cartão fixado no topo do feed do usuário, e o usuário não pode descartá-lo. Se o feed de um usuário tiver vários cartões fixados, a Braze os ordena cronologicamente. Quando a Braze entrega um Content Card, ele é fixado ou não fixado, e esse status não muda durante toda a vida útil do cartão. Se você alterar a configuração de fixação em uma Campaign, a atualização se aplica apenas aos cartões enviados após a modificação. Ela não altera o status de fixação dos cartões que já estão no feed do usuário.

![Comparação lado a lado da prévia do Content Card na Braze para dispositivos móveis e web com a opção "Fixar este cartão no topo do feed" selecionada.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Comportamento ao clicar {#on-click-behavior}

Quando o cliente clica em um link apresentado no cartão, o link pode levá-lo para uma área mais profunda do app ou para outro site. Se você escolher um comportamento ao clicar para o seu Content Card, lembre-se de atualizar o **Texto do link** de acordo.

As seguintes ações estão disponíveis para links de Content Card:

| Ação | Descrição |
|---|---|
| Redirecionar para URL da web | Abrir uma página web não nativa. |
| [Deep link para o app]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | Deep link para uma tela existente no seu app. |
| Registrar evento personalizado | Escolher um [evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events) para disparar. Pode ser usado para exibir outro Content Card ou disparar envios de mensagens adicionais. |
| Registrar atributo personalizado | Escolher um [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) para definir para o usuário atual. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportamento ao clicar" }

As opções **Registrar evento personalizado** e **Registrar atributo personalizado** exigem a seguinte compatibilidade de versão do SDK:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Etapa 4: Definir configurações adicionais (opcional) {#step-4-configure-additional-settings-optional}

Você pode usar [pares chave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) para criar categorias para seus cartões, criar [vários feeds de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#implementing-multiple-feeds) e personalizar como os cartões são classificados.

Para adicionar pares chave-valor à sua mensagem, acesse a guia **Settings** e selecione **Add New Pair**.

## Etapa 5: Crie o restante da sua campanha ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Crie o restante da sua campanha. Continue nas próximas seções para mais detalhes sobre como usar nossas ferramentas para criar Content Cards.

### Escolha um cronograma de entrega ou disparador {#choose-a-delivery-schedule-or-trigger}

Os Content Cards podem ser entregues com base em um horário agendado, uma ação ou um disparo por API. Para saber mais, consulte [Agendando sua campanha]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Você também pode definir a duração da campanha e o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours), além de determinar a expiração do Content Card. Defina uma data de expiração específica ou o número de dias até o cartão expirar, em até 30 dias. Todas as variantes devem usar a mesma expiração (duração ou horário específico).

A contagem regressiva da expiração começa a partir do horário de envio do cartão:

- **Campanhas agendadas:** A contagem regressiva começa no horário de lançamento agendado.
- **Campanhas baseadas em ação:** A contagem regressiva começa quando o usuário realiza a ação de disparo.

Por exemplo, se um Content Card baseado em ação for enviado hoje às 14h com expiração de 1 dia, ele expira às 14h do dia seguinte.

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

Para entrega baseada em ação, há um pequeno atraso esperado antes que o Content Card apareça. Para detalhes sobre por que isso acontece e como minimizá-lo, consulte [Por que os Content Cards não aparecem imediatamente após um evento-gatilho?]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#why-dont-content-cards-appear-immediately-after-a-trigger-event).

#### Entrega agendada {#scheduled-delivery}

Para campanhas de Content Card com entrega agendada, você pode escolher quando a Braze avalia a elegibilidade do público e a personalização para novas campanhas de Content Card, especificando quando o cartão é criado. Para saber mais, consulte [criação de cartões]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation).

#### Escolha os usuários a direcionar {#choose-users-to-target}

Em seguida, [direcione os usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) escolhendo segmentos ou filtros para refinar seu público. Você recebe automaticamente uma prévia de como é a população aproximada desse segmento. Lembre-se de que a associação exata ao segmento é sempre calculada antes do envio da mensagem.

{% multi_lang_include audience/target_audiences.md %}

#### Escolha os eventos de conversão {#choose-conversion-events}

A Braze permite que você rastreie com que frequência os usuários realizam ações específicas, os [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), após receberem uma campanha. Você tem a opção de permitir uma janela de até 30 dias durante a qual uma conversão é contabilizada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não tiver feito, conclua as seções restantes do componente do Canvas. Para detalhes sobre como criar o restante do Canvas, incluindo testes multivariantes e [Otimizar com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), consulte [Crie seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).

{% endtab %}
{% endtabs %}

## Etapa 6: Revisar e lançar {#step-6-review-and-deploy}

Depois de terminar de criar sua Campaign ou Canvas, revise os detalhes, [teste-a]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) e envie. Para saber mais, consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=content%20card).

{% alert note %}
Embora os Content Cards não exijam notificações por push em produção, os envios de teste exigem que o push esteja ativado nos seus dispositivos de teste, pois o cartão é entregue na carga útil do push. Os Content Cards de teste expiram aproximadamente cinco minutos após o envio.
{% endalert %}

{% alert warning %}
Depois que um Content Card é lançado, ele não pode ser editado. Ele só pode ser impedido de ser enviado a novos usuários e removido dos feeds dos usuários. Consulte [Atualização de cartões enviados]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards) para entender como você pode lidar com esse cenário.
{% endalert %}

Em seguida, confira [Relatórios de Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/reporting) para saber como acessar os resultados das suas Campaigns de Content Cards.

## Informações importantes {#things-to-know}

### Limitações de carga útil e feed {#payload-and-feed-limitations}

Para garantir a performance, os Content Cards têm duas restrições principais: um limite no tamanho da carga útil de cada cartão e um número máximo de cartões que podem aparecer em um feed.

#### Limitações de tamanho para Content Cards {#size-limitations-for-content-cards}

A carga útil total de dados de um único Content Card não pode exceder 2 KB **após** qualquer personalização com Liquid ser renderizada. Isso inclui:

* Título
* Mensagem
* URL da imagem (o comprimento da string da URL em si, não o tamanho do arquivo de imagem)
* Texto do link
* URLs de link para todas as plataformas especificadas (URLs separadas para iOS, Android e web contam para o total)
* Pares chave-valor (tanto os nomes das chaves quanto seus valores)

Usar Liquid para inserir strings longas de texto (como de atributos personalizados) pode fazer com que você exceda o limite.

O criador de Campaigns exibe um aviso se o seu conteúdo estático exceder o limite. Não é feita uma previsão do tamanho para conteúdo dinâmico usando Liquid. Se o tamanho da mensagem exceder 2 KB, ela será interrompida no momento do envio. Você pode ver essas interrupções no registro de atividade de mensagens com o motivo `Content card maximum size exceeded`.

{% alert important %}
Durante envios de teste, Content Cards que excedem 2 KB ainda podem ser entregues e exibidos corretamente.
{% endalert %}

Aqui estão algumas práticas recomendadas para gerenciar o tamanho da carga útil dos Content Cards:

* Use encurtadores de URL para links longos. URLs, especialmente aquelas com parâmetros de rastreamento extensos, podem ter problemas com o limite de tamanho. Usar um serviço de encurtamento de URL pode reduzir drasticamente a contagem de caracteres e liberar espaço na carga útil.
* Trunque conteúdo dinâmico com Liquid. Ao personalizar cartões com texto dinâmico de atributos de usuário ou chamadas de API, o comprimento do conteúdo pode ser imprevisível. Use proativamente filtros Liquid como `truncate` para limitar o comprimento de qualquer texto dinâmico.
* Seja eficiente com URLs multiplataforma. O limite de 2 KB inclui as URLs de todas as plataformas que você define. Usar URLs longas e únicas para cada plataforma pode multiplicar o tamanho da carga útil. Se possível, use um único link que funcione em todas as plataformas, ou use encurtadores de URL conforme necessário.
* Considere Banners para conteúdo mais rico. Para casos de uso que exigem consistentemente grandes quantidades de conteúdo, Content Cards pode não ser o canal adequado. Banners não têm a mesma limitação de carga útil de 2 KB e são mais adequados para incorporar conteúdo mais rico diretamente em uma experiência de app ou website.

#### Número de cartões no feed {#number-of-cards-in-feed}

Cada usuário pode ter até 250 Content Cards não expirados em seu feed a qualquer momento. Quando esse limite é excedido, a Braze para de retornar os cartões mais antigos, mesmo que não tenham sido lidos. Cartões dispensados também contam para esse limite, o que significa que um número alto de cartões dispensados pode reduzir o espaço disponível para os mais antigos.

Para evitar problemas com o limite de cartões, recomendamos as seguintes práticas:

- **Use datas de expiração mais curtas:** para Campaigns sensíveis ao tempo (como uma promoção de fim de semana), defina uma data de expiração específica. Dessa forma, os cartões são removidos automaticamente do feed e não contam mais para o limite depois que não forem mais relevantes.
- **Aproveite a remoção baseada em ação:** configure eventos de remoção para cartões transacionais ou baseados em metas. Por exemplo, um cartão solicitando que um usuário complete seu perfil deve ser removido assim que um evento `profile_completed` for registrado.
- **Audite Campaigns de longa duração:** revise Campaigns recorrentes ou contínuas para garantir que não estejam criando uma experiência ruim para seus usuários, preenchendo o feed com cartões demais ao longo do tempo.

### Entendendo a reelegibilidade para Content Cards {#understanding-re-eligibility-for-content-cards}

A reelegibilidade determina se e quando um usuário pode receber uma mensagem da mesma Campaign mais de uma vez. Para Content Cards, entender como isso funciona é fundamental para gerenciar Campaigns recorrentes e garantir que os usuários não recebam mensagens duplicadas ou desatualizadas.

{% alert tip %}
Quer que seu conteúdo dure mais de 30 dias? Experimente [Banners]({{site.baseurl}}/user_guide/channels/banners).
{% endalert %}

#### Como a reelegibilidade é calculada {#how-re-eligibility-is-calculated}

Se você ativar a reelegibilidade, a contagem regressiva para quando um usuário pode "reentrar" em uma Campaign começa após o envio da mensagem. O momento específico em que essa contagem começa depende das suas configurações de criação de cartão:

- Content Cards que usam [na primeira impressão]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences) utilizam o horário da impressão para calcular a reelegibilidade.
- Content Cards criados no lançamento da Campaign, em Campaigns multicanal ou na entrada da etapa do Canvas usam o horário de envio ou de impressão mais recente, o que for mais tardio.

#### A expiração de 30 dias e a reelegibilidade {#the-30-day-expiration-and-re-eligibility}

Uma fonte comum de confusão é a interação entre a reelegibilidade da Campaign e a expiração automática de 30 dias de todos os Content Cards.

Todos os Content Cards são automaticamente removidos dos sistemas da Braze 30 dias após serem enviados ou removidos. Se você tem uma Campaign recorrente de longa duração com a reelegibilidade **desativada**, um usuário ainda pode receber o mesmo cartão novamente após 30 dias. Quando o cartão original é removido, o sistema não vê mais um registro de que aquele usuário recebeu a Campaign, tornando-o elegível novamente na próxima sessão.

Para que os usuários recebam uma mensagem de uma Campaign específica apenas uma vez, adicione um filtro de público à sua Campaign ou etapa do Canvas para usuários que não receberam uma mensagem desta Campaign. Esse filtro é a forma mais confiável de evitar envios duplicados em Campaigns de longa duração.

### Gerenciando Content Cards ativos {#managing-live-content-cards}

Após serem enviados, os Content Cards ficam esperando em uma "caixa de entrada" prontos para serem entregues ao usuário (semelhante ao que acontece com e-mails). Depois que o conteúdo é carregado no Content Card (no momento da exibição), ele não pode ser alterado durante sua vida útil. Isso se aplica mesmo se você estiver chamando uma API por meio de Connected Content e os dados do endpoint mudarem. Esses dados não são atualizados. Só é possível impedir o envio para novos usuários e remover dos feeds dos usuários. Se você modificar uma Campaign, apenas os cartões enviados após a modificação incluem a atualização.

#### Atualizando cartões já lançados {#updating-launched-cards}

Para alterar um cartão para usuários que já o receberam, você deve usar um dos seguintes métodos:

##### Opção 1: Duplicar a Campaign (recomendado para mudanças imediatas) {#option-1-duplicate-the-campaign-recommended-for-immediate-changes}

{% alert tip %}
Recomendamos esta opção para mensagens em que você está exibindo o conteúdo mais recente no cartão, as mudanças devem ser mostradas imediatamente ou quando a reelegibilidade está desativada.
{% endalert %}

A primeira abordagem é arquivar a Campaign e lançar uma nova Campaign duplicada:

1. Pare a Campaign original e, quando solicitado, selecione `Remove card after the next sync`.
2. Duplique a Campaign, faça suas edições e lance a nova versão.

Ao duplicar a Campaign, você precisa definir o público para a nova versão. Use filtros de segmentação para controlar quem recebe o cartão atualizado:
* Se os usuários nunca devem ser reelegíveis para um Content Card, você pode filtrar por usuários que não receberam a versão anterior do Content Card definindo o filtro `Received Message from Campaign` com a condição `Has Not`.
* Se os usuários que receberam o cartão anterior devem ser reelegíveis em X dias, você pode definir o filtro `Last Received Message from specific campaign` para mais de X dias atrás **OU** `Received Message from Campaign` com a condição `Has Not`.

###### Impacto {#impact}

- **Destinatários existentes:** destinatários novos e existentes veem o cartão atualizado na próxima atualização do feed, se forem elegíveis.
- **Relatórios:** cada versão do cartão possui análises separadas.

Digamos que você configurou uma Campaign para ser disparada no início de uma sessão, com reelegibilidade definida para 30 dias. Um usuário recebeu a Campaign dois dias atrás e você quer alterar o texto. Primeiro, arquive a Campaign e remova os cartões do feed. Segundo, duplique a Campaign e relance com o novo texto. Se o usuário tiver outra sessão, ele recebe o novo cartão imediatamente.

##### Opção 2: Parar e relançar a mesma Campaign {#option-2-stop-and-relaunch-the-same-campaign}

{% alert tip %}
Recomendamos usar esta opção para mensagens exclusivas em uma central de notificações ou caixa de entrada de mensagens (como promoções), quando é importante que as análises sejam unificadas, ou quando a urgência da mensagem não é uma preocupação (ou seja, os destinatários existentes podem esperar a janela de elegibilidade antes de ver os cartões atualizados).
{% endalert %}

Essa abordagem mantém todas as suas análises unificadas em uma única Campaign. Usuários recém-elegíveis recebem o novo cartão, mas isso atrasa a atualização para destinatários existentes até que sejam reelegíveis:

1. Pare sua Campaign e, quando solicitado, selecione **Remove card after the next sync**.
2. Edite sua Campaign conforme necessário.
3. Reinicie sua Campaign.

###### Impacto

* **Destinatários existentes:** usuários que já receberam o cartão não recebem os cartões atualizados até se tornarem reelegíveis. Se a reelegibilidade estiver desativada, eles nunca receberão o novo cartão.
* **Relatórios:** uma Campaign contém todas as análises de relatórios para as versões de cartões lançadas. A Braze não diferencia entre as versões lançadas.

Digamos que você tem uma Campaign disparada no início de uma sessão com reelegibilidade definida para 30 dias. Um usuário recebeu a Campaign dois dias atrás e você quer alterar o texto. Primeiro, pare a Campaign e remova o cartão do feed. Segundo, republique a Campaign com o novo texto. Se o usuário tiver outra sessão, ele receberá o novo cartão em 28 dias.

{% alert note %}
Se você parar uma Campaign, editar as configurações do evento de remoção e reiniciar a Campaign sem remover os cartões do feed, quaisquer cartões existentes nos feeds dos usuários usarão as configurações atualizadas do evento de remoção. Os cartões não mantêm a configuração original do evento de remoção de quando foram enviados pela primeira vez.
{% endalert %}

#### Removendo e expirando cartões {#removing-and-expiring-cards}

##### Remoção manual de cartões {#manual-card-removal}

Você pode remover manualmente cartões dos feeds de todos os usuários a qualquer momento parando a Campaign.

1. Abra a Campaign de Content Card e selecione Stop Campaign.
2. Quando solicitado, selecione **Remove card after the next sync**. O cartão é removido na próxima atualização do feed.

##### Remoção automatizada de cartões {#action-based-card-removal}

Você pode remover automaticamente um cartão quando um usuário realiza uma ação específica, como concluir uma compra ou ativar um recurso.

Na sua Campaign ou etapa do Canvas, especifique um evento de remoção. Quando um usuário realiza esse evento, o cartão é removido do feed dele em uma atualização subsequente após a Braze processar o evento.

{% alert note %}
Essa remoção não é instantânea. Há um atraso no processamento, então pode levar vários minutos e mais de uma atualização do feed para o cartão desaparecer.
{% endalert %}

{% alert tip %}
Você pode especificar vários eventos personalizados e compras que devem remover um cartão do feed de um usuário. Quando qualquer uma dessas ações for realizada pelo usuário, quaisquer cartões existentes enviados pelos cartões da Campaign são removidos. Cartões elegíveis continuam sendo enviados de acordo com o cronograma da mensagem.
{% endalert %}

![Painel de condições de remoção de Content Card com a opção de evento de remoção de Content Card.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### Expiração de cartões {#card-expiration}

Content Cards permanecem disponíveis por até 30 dias a partir do envio; após 30 dias, a Braze os remove dos feeds dos usuários e os elimina dos sistemas da Braze.

#### Fazendo cartões durarem mais de 30 dias {#making-cards-last-longer-than-30-days}

{% alert tip %}
Para casos de uso que exigem que as mensagens persistam por mais tempo do que o limite de 30 dias dos Content Cards, considere usar Banners. Banners são projetados para persistência e não têm uma data de expiração obrigatória, permitindo que permaneçam visíveis pelo tempo que forem necessários.
{% endalert %}

Se você quiser que um cartão pareça estar sempre disponível, pode criar uma Campaign recorrente que efetivamente substitui o cartão a cada 30 dias:

1. Defina a duração do Content Card para 30 dias.
2. Defina a reelegibilidade da Campaign para 30 dias.
3. Configure a Campaign para ser disparada em "Session Start".

### Sincronização e atualização de Content Cards {#content-card-sync-and-refresh}

Os Content Cards são sincronizados em um cronograma e quando seu app atualiza o feed. O comportamento de sincronização difere entre sincronizações completas e parciais, e sua integração de SDK afeta quando os cartões são atualizados no início da sessão. Para detalhes de implementação, consulte [Personalizar o feed de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed) e [Criando Content Cards]({{site.baseurl}}/developer_guide/content_cards/creating_cards).

### Impacto de parar Campaigns de Content Cards {#impact-of-stopping-content-cards-campaigns}

Quando você para uma Campaign e seleciona **Remove card after the next sync**, a Braze remove o cartão dos feeds dos usuários na próxima atualização. As contagens de impressões podem ser menores do que as contagens de envio porque os usuários não podem registrar impressões em cartões que são removidos antes de serem visualizados.

## Solução de problemas {#troubleshooting}

### Por que os Content Cards não aparecem imediatamente após um evento-gatilho? {#why-dont-content-cards-appear-immediately-after-a-trigger-event}

Para Campaigns de entrega baseada em ação (como início de sessão), existe um breve atraso esperado entre o evento-gatilho e a disponibilidade do cartão. Esse atraso ocorre porque:

- O evento-gatilho é enviado aos servidores da Braze
- A Campaign é disparada e a elegibilidade do usuário é registrada
- O cartão de conteúdo é criado no banco de dados para esse usuário
- O SDK sincroniza e busca todos os cartões disponíveis no dispositivo

Se a sincronização do SDK acontecer antes de a elegibilidade do usuário ser registrada, o usuário não recebe o cartão.

Para novos usuários em sua primeira sessão, esse atraso é inevitável. Para usuários existentes que precisam de disponibilidade imediata, considere usar entrega agendada.

Se você precisar minimizar atrasos tanto para novos quanto para usuários existentes, pode criar duas Campaigns:

- **Usuários existentes com contagem de sessões maior que 0:** Use uma Campaign de entrega agendada. Os cartões são pré-criados e ficam disponíveis imediatamente.
- **Novos usuários com contagem de sessões igual a 0:** Use uma Campaign disparada por ação. Os cartões são criados após o primeiro evento-gatilho de sessão.

Essa abordagem garante que usuários existentes vejam os cartões instantaneamente, enquanto ainda alcança novos usuários após um breve atraso em sua primeira sessão. Para estratégias adicionais de melhoria de latência, consulte [Melhorar a baixa latência para Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/best_practices/improving_low_latency_requirements).

### Por que os timestamps de impressão ou descarte ficam fora do cronograma da Campaign? {#why-do-impression-or-dismiss-timestamps-fall-outside-the-campaign-schedule}

Os timestamps de impressão e descarte em análise de dados e Currents refletem quando um usuário visualiza ou descarta um Content Card, não quando a Braze cria ou envia o cartão. Um cartão pode permanecer no feed de um usuário até que os Content Cards sejam atualizados, então os timestamps de impressão e descarte podem ocorrer após a janela de envio da Campaign.

Se os horários ainda parecerem inesperados:

- Confirme se você está visualizando a análise de dados no fuso horário da sua empresa ou no fuso horário do usuário no Currents.
- Verifique se o usuário realmente visualizou ou descartou o cartão após recebê-lo, em vez de comparar apenas com o horário de envio.

Para saber mais sobre métricas de Content Cards, consulte [Relatórios de Content Card]({{site.baseurl}}/user_guide/channels/content_cards/reporting).

### Erro "All expiration values for a campaign must match" {#all-expiration-values-for-a-campaign-must-match-error}

Esse erro aparece quando uma Campaign de Content Card multivariante usa configurações de expiração diferentes entre as variantes. Defina a mesma expiração (duração ou horário específico) em cada variante, ou reduza a Campaign a uma única variante e salve novamente. Para saber como definir a expiração ao criar uma Campaign, consulte [Escolher um cronograma de entrega ou evento-gatilho](#choose-a-delivery-schedule-or-trigger).