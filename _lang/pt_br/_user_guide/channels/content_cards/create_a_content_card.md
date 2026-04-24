---
nav_title: Criar um cartão de conteúdo
article_title: Criar um cartão de conteúdo
page_order: 1
description: "Este artigo de referência aborda como criar, redigir, configurar e enviar Cartões de conteúdo usando campanhas e Canvas da Braze."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Criar um cartão de conteúdo

> Este artigo aborda como criar um cartão de conteúdo na Braze ao construir campanhas e Canvas. Aqui, vamos orientar você na escolha de um tipo de mensagem, na composição do seu cartão e na programação da entrega da mensagem.

## Etapa 1: Escolha onde criar sua mensagem

Use campanhas para envios de mensagens simples e únicos (como informar os usuários sobre um produto com uma única mensagem). Use Canvas para jornadas de usuário com várias etapas (como enviar sugestões de produtos personalizadas com base no comportamento do usuário ao longo do tempo).

{% tabs %}
{% tab Campaign %}

1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.
2. Selecione **Cartões de conteúdo** ou, para campanhas direcionadas a vários canais, selecione **Multicanal**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) e [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) conforme necessário.
   * As tags facilitam a localização das suas campanhas e a criação de relatórios. Por exemplo, ao usar o [Criador de relatórios]({{site.baseurl}}/user_guide/analytics/reports/report_builder/), você pode filtrar pelas tags relevantes.
5. Adicione e nomeie quantas variantes quiser para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagem e disposições para cada variante adicionada. Para saber mais sobre variantes, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% alert tip %}
Se todas as mensagens da sua campanha forem semelhantes ou tiverem o mesmo conteúdo, redija sua mensagem antes de adicionar variantes extras. Em seguida, selecione **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) usando o criador de Canvas.
2. Após configurar seu Canvas, adicione uma etapa de Mensagem no construtor de Canvas. Dê à sua etapa um nome claro e significativo.
3. Selecione **Cartões de conteúdo** como seu canal de envio de mensagens.
4. Escolha quando a Braze calcula a elegibilidade do público e a personalização para o cartão de conteúdo. Isso pode ser na entrada da etapa ou na primeira impressão (recomendado). Etapas que contêm Cartões de conteúdo podem ser agendadas ou baseadas em ação.
5. Escolha se deseja remover os Cartões de conteúdo quando os usuários concluírem uma compra ou realizarem um evento personalizado.
6. Defina uma expiração para o cartão de conteúdo (tempo no feed). Isso pode ser após um período de tempo ou em um momento específico.
7. Filtre seu público, ou os destinatários, para esta etapa conforme necessário em **Configurações de entrega**. Você pode refinar ainda mais seu público especificando segmentos e adicionando filtros adicionais. As opções de público são verificadas após a postergação, no momento em que as mensagens são enviadas.
8. Escolha quaisquer outros canais de envio de mensagens que você queira combinar com sua mensagem.

{% endtab %}
{% endtabs %}

## Etapa 2: Especifique seus tipos de mensagem

Selecione um dos três tipos essenciais de cartão de conteúdo: **Clássico**, **Imagem com legenda** e **Somente imagem**. 

Para saber mais sobre o comportamento esperado e a aparência de cada tipo, consulte [Detalhes criativos]({{site.baseurl}}/user_guide/channels/content_cards/creative_details/) ou confira os links na tabela a seguir. Esses tipos de cartão de conteúdo são aceitos tanto por apps móveis quanto por aplicações web.

| Tipo de mensagem | Exemplo | Descrição |
|---|---|---|
|[Clássico]({{site.baseurl}}/user_guide/channels/content_cards/creative_details/#classic)| ![Um cartão de conteúdo clássico com um ícone pequeno e texto incentivando a reservar uma aula de treino.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |O cartão clássico tem uma disposição direta com um título em negrito, texto da mensagem e uma imagem opcional posicionada à esquerda do título e do texto. É melhor usar uma imagem quadrada ou ícone com o cartão clássico. |
|[Imagem com legenda]({{site.baseurl}}/user_guide/channels/content_cards/creative_details/#captioned-image)| ![Um cartão de conteúdo com legenda mostrando a imagem de um halterofilista e texto incentivando a reservar uma aula de treino.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | O cartão de imagem com legenda destaca seu conteúdo com texto e uma imagem chamativa. |
|[Somente imagem]({{site.baseurl}}/user_guide/channels/content_cards/creative_details/#banner)| ![Um cartão de conteúdo somente imagem com apenas texto.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | O cartão somente imagem chama a atenção com espaço para imagens, GIFs e outros conteúdos criativos sem texto. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Etapa 3: Redija um cartão de conteúdo

Você pode editar todos os aspectos do conteúdo e do comportamento da sua mensagem na guia **Redigir** do editor de mensagens.

![Exemplo de detalhes de cartão de conteúdo na guia Redigir do editor de mensagens.]({% image_buster /assets/img/content_card_compose.png %})

O conteúdo aqui varia com base no **Tipo de cartão** escolhido na etapa anterior, mas pode incluir qualquer uma das seguintes opções:

#### Idioma

Selecione **Adicionar idiomas** para adicionar os idiomas desejados da lista fornecida. Isso insere [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/#conditional-logic) na sua mensagem. Recomendamos selecionar seus idiomas antes de escrever o conteúdo para que você possa preencher o texto nos locais corretos no Liquid. Para ver a lista completa de idiomas disponíveis, consulte [Idiomas suportados]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

![Uma janela com inglês, espanhol e francês selecionados como idiomas, e título, descrição e texto do link selecionados como campos para internacionalizar.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

##### Criar mensagens da direita para a esquerda

A aparência final das mensagens da direita para a esquerda depende muito de como os prestadores de serviço as renderizam. Para conhecer as práticas recomendadas na criação de mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/).

#### Título e mensagem

Escreva o que quiser. Não há limites, mas quanto mais rápido você conseguir transmitir sua mensagem e fazer o cliente clicar, melhor! Recomendamos títulos e conteúdos de mensagem claros e concisos. Esses campos não estão disponíveis para cartões somente imagem.

#### Imagem

Para adicionar uma imagem ao seu cartão de conteúdo, selecione **Adicionar imagem** ou forneça uma URL de imagem. Ao selecionar **Adicionar imagem**, a **Biblioteca de mídia** é aberta, onde você pode selecionar uma imagem carregada anteriormente ou adicionar uma nova. 

Cada tipo de mensagem e plataforma pode ter suas próprias proporções e requisitos sugeridos, então verifique quais são antes de encomendar ou criar uma imagem do zero. Lembre-se de que os campos de mensagem do cartão de conteúdo são limitados a 2&nbsp;KB no tamanho total.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Fixar no topo

A Braze exibe um cartão fixado no topo do feed do usuário, e o usuário não pode descartá-lo. Se o feed de um usuário tiver vários cartões fixados, a Braze os ordena cronologicamente. Depois de enviar um cartão, não é possível atualizar retroativamente sua opção de fixação. Alterar essa opção após o envio de uma campanha afeta apenas envios futuros.

![Lado a lado da pré-visualização do cartão de conteúdo na Braze para celular e web com a opção "Fixar este cartão no topo do feed" selecionada.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Comportamento ao clicar

Quando o cliente clica em um link apresentado no cartão, o link pode levá-lo para uma área mais profunda do seu app ou para outro site. Se você escolher um comportamento ao clicar para seu cartão de conteúdo, lembre-se de atualizar o **Texto do link** de acordo.

As seguintes ações estão disponíveis para links de cartão de conteúdo:

| Ação | Descrição |
|---|---|
| Redirecionar para URL da web | Abrir uma página web não nativa. |
| [Deep link para o app]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/#deep-link-to-in-app-content) | Deep link para uma tela existente no seu app. |
| Registrar evento personalizado | Escolha um [evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) para disparar. Pode ser usado para exibir outro cartão de conteúdo ou disparar envios de mensagens adicionais. |
| Registrar atributo personalizado | Escolha um [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) para definir para o usuário atual. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

As opções **Registrar evento personalizado** e **Registrar atributo personalizado** exigem a seguinte compatibilidade de versão do SDK:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Etapa 4: Configure definições adicionais (opcional)

Você pode usar [pares chave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/) para criar categorias para seus cartões, criar [múltiplos feeds de Cartões de conteúdo]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) e personalizar como os cartões são ordenados.

Para adicionar pares chave-valor à sua mensagem, acesse a guia **Configurações** e selecione **Adicionar novo par**.

## Etapa 5: Construa o restante da sua campanha ou Canvas

{% tabs %}
{% tab Campaign %}

Construa o restante da sua campanha. Continue nas próximas seções para mais detalhes sobre como usar nossas ferramentas da melhor forma para criar Cartões de conteúdo.

#### Escolha um cronograma de entrega ou gatilho

Os Cartões de conteúdo podem ser entregues com base em um horário agendado, uma ação ou um gatilho de API. Para saber mais, consulte [Agendando sua campanha]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

Você também pode definir a duração da campanha e o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#quiet-hours), além de determinar a expiração do cartão de conteúdo. Defina uma data de expiração específica ou os dias até o cartão expirar, até 30 dias. Todas as variantes têm datas de expiração idênticas.

Se você optar por expirar um cartão após um período definido (por exemplo, após duas semanas), a expiração é calculada a partir do momento do envio do cartão. Para campanhas agendadas, esse é o horário de lançamento programado. Para campanhas baseadas em ação, esse é o momento em que o usuário realiza a ação de gatilho. Por exemplo, se um cartão baseado em ação for enviado às 14h hoje com expiração de 1 dia, ele expira às 14h do dia seguinte.

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

Para entrega baseada em ação, há um pequeno atraso esperado antes que o cartão de conteúdo apareça. Por exemplo, quando uma campanha é disparada no início da sessão, esse evento de gatilho precisa primeiro ser enviado aos servidores da Braze. Em seguida, a elegibilidade do usuário para a campanha é registrada. Quando o SDK sincroniza, o cartão é criado e retornado na mesma resposta de sincronização. Se a sincronização do SDK aconteceu antes da elegibilidade do usuário ser registrada, ele não recebe o cartão. Para usuários de primeira sessão, esse atraso é inevitável. Para usuários existentes que precisam de disponibilidade imediata, considere usar a entrega agendada.

##### Entrega agendada

Para campanhas de cartão de conteúdo com entrega agendada, você pode escolher quando a Braze avalia a elegibilidade do público e a personalização para novas campanhas de cartão de conteúdo, especificando quando o cartão é criado. Para saber mais, consulte [criação de cartão]({{site.baseurl}}/card_creation).

#### Escolha os usuários-alvo

Em seguida, [direcione os usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/) escolhendo segmentos ou filtros para refinar seu público. Você recebe automaticamente uma pré-visualização de como é a população aproximada desse segmento. Lembre-se de que a composição exata do segmento é sempre calculada antes do envio da mensagem.

{% multi_lang_include target_audiences.md %}

#### Escolha eventos de conversão

A Braze permite que você rastreie com que frequência os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão é contabilizada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não o fez, conclua as seções restantes do seu componente de Canvas. Para mais detalhes sobre como construir o restante do seu Canvas, implementar [testes multivariantes]({{site.baseurl}}/user_guide/messaging/ab_testing/) e [Seleção inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/), e mais, consulte a etapa [Construa seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) da nossa documentação de Canvas.

{% endtab %}
{% endtabs %}

## Etapa 6: Revise e implante

Após terminar de construir a última parte da sua campanha ou Canvas, revise os detalhes, [teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/) e envie quando estiver pronto. Para saber mais, consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=content%20card).

{% alert warning %}
Depois que um cartão de conteúdo é lançado, ele não pode ser editado. Ele só pode ser impedido de ser enviado a novos usuários e removido dos feeds dos usuários. Consulte [Atualizando cartões lançados]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/#updating-launched-cards) para entender como lidar com esse cenário.
{% endalert %}

Em seguida, confira [Relatórios de Cartões de conteúdo]({{site.baseurl}}/user_guide/channels/content_cards/reporting/) para saber como acessar os resultados das suas campanhas de cartão de conteúdo.

## Informações importantes

### Limitações de carga útil e feed

Para garantir a performance, os Cartões de conteúdo têm duas restrições principais: um limite no tamanho da carga útil de cada cartão e um número máximo de cartões que podem aparecer em um feed.

#### Limitações de tamanho para Cartões de conteúdo

A carga útil total de dados de um único cartão de conteúdo não pode exceder 2 KB **após** qualquer personalização Liquid ser renderizada. Isso inclui:

* Título
* Mensagem
* URL da imagem (o comprimento da string da URL em si, não o tamanho do arquivo de imagem)
* Texto do link
* URLs de link para todas as plataformas especificadas (URLs separadas para iOS, Android e Web contam para o total)
* Pares chave-valor (tanto os nomes das chaves quanto seus valores)

Usar Liquid para puxar strings longas de texto (como de atributos personalizados) pode fazer com que você exceda o limite. 

O criador de campanha exibe um aviso se o conteúdo estático exceder o limite. (Não é possível prever o tamanho de conteúdo dinâmico usando Liquid.) **Se o tamanho da mensagem exceder 2 KB, ela é abortada no momento do envio.** Você pode ver esses abortos no Registro de atividades de envio de mensagem com o motivo `Content card maximum size exceeded`.

{% alert important %}
Durante envios de teste, Cartões de conteúdo que excedem 2 KB ainda podem ser entregues e exibidos corretamente.
{% endalert %}

Aqui estão algumas práticas recomendadas para gerenciar o tamanho da carga útil do cartão de conteúdo:

* Use encurtadores de URL para links longos. URLs, especialmente aquelas com parâmetros de rastreamento extensos, podem ter problemas com o limite de tamanho. Usar um serviço de encurtamento de URL pode reduzir drasticamente a contagem de caracteres e liberar espaço na carga útil.
* Trunque conteúdo dinâmico com Liquid. Ao personalizar cartões com texto dinâmico de atributos de usuário ou chamadas de API, o comprimento do conteúdo pode ser imprevisível. Use proativamente filtros Liquid como `truncate` para limitar o comprimento de qualquer texto dinâmico.
* Seja eficiente com URLs multiplataforma. O limite de 2 KB inclui as URLs de todas as plataformas que você definir. Usar URLs longas e exclusivas para cada plataforma pode multiplicar o tamanho da carga útil. Se possível, use um único link que funcione em todas as plataformas ou use encurtadores de URL conforme necessário.
* Considere Banners para conteúdo mais rico. Para casos de uso que consistentemente exigem grandes quantidades de conteúdo, os Cartões de conteúdo podem não ser o canal certo. Os Banners não têm a mesma limitação de carga útil de 2 KB e são mais adequados para incorporar conteúdo mais rico diretamente em uma experiência de app ou site.

#### Número de cartões no feed

Cada usuário pode ter até 250 Cartões de conteúdo não expirados em seu feed a qualquer momento. Quando esse limite é excedido, a Braze para de retornar os cartões mais antigos, mesmo que não tenham sido lidos. Cartões descartados também contam para esse limite, o que significa que um grande número de cartões descartados pode reduzir o espaço disponível para os mais antigos.

Para evitar problemas com o limite de cartões, recomendamos as seguintes práticas:

- **Use datas de expiração mais curtas:** Para campanhas sensíveis ao tempo (como uma promoção de fim de semana), defina uma data de expiração específica. Dessa forma, os cartões são automaticamente removidos do feed e não contam para o limite depois que não são mais relevantes.
- **Aproveite a remoção baseada em ação:** Configure eventos de remoção para cartões transacionais ou baseados em metas. Por exemplo, um cartão solicitando que o usuário complete seu perfil deve ser removido assim que um evento `profile_completed` for registrado.
- **Audite campanhas de longa duração:** Revise campanhas recorrentes ou contínuas para garantir que não estejam criando uma experiência ruim para seus usuários ao encher o feed com muitos cartões ao longo do tempo.

### Entendendo a reelegibilidade para Cartões de conteúdo

A reelegibilidade determina se e quando um usuário pode receber uma mensagem da mesma campanha mais de uma vez. Para Cartões de conteúdo, entender como isso funciona é fundamental para gerenciar campanhas recorrentes e garantir que os usuários não recebam mensagens duplicadas ou desatualizadas.

{% alert tip %}
Quer que seu conteúdo dure mais de 30 dias? Experimente os [Banners]({{site.baseurl}}/user_guide/channels/banners).
{% endalert %}

#### Como a reelegibilidade é calculada

Se você ativar a reelegibilidade, a contagem regressiva para quando um usuário pode "reentrar" em uma campanha começa após o envio da mensagem. O momento específico em que essa contagem começa depende das suas configurações de criação de cartão:

* Cartões de conteúdo que usam [na primeira impressão]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) usam o momento da impressão para calcular a reelegibilidade.
* Cartões de conteúdo criados no lançamento da campanha ou na entrada da etapa do Canvas usam o que for mais recente entre o momento do envio e o momento da impressão.

#### A expiração de 30 dias e a reelegibilidade

Uma fonte comum de confusão é a interação entre a reelegibilidade da campanha e a expiração automática de 30 dias de todos os Cartões de conteúdo. 

Todos os Cartões de conteúdo são automaticamente removidos dos sistemas da Braze 30 dias após serem enviados ou removidos. Se você tiver uma campanha recorrente de longa duração com a reelegibilidade **desativada**, um usuário ainda pode receber o mesmo cartão novamente após 30 dias. Quando o cartão original é removido, o sistema não vê mais um registro de que o usuário recebeu a campanha, tornando-o elegível novamente na próxima sessão. 

Para que os usuários recebam uma mensagem de uma campanha específica apenas uma vez, adicione um filtro de público à sua campanha ou etapa do Canvas para usuários que não receberam uma mensagem desta campanha. Esse filtro é a forma mais confiável de evitar envios duplicados em campanhas de longa duração.

### Gerenciando Cartões de conteúdo ativos

Depois que os Cartões de conteúdo são enviados, eles ficam aguardando em uma "caixa de entrada" prontos para serem entregues ao usuário (semelhante ao que acontece com e-mails). Depois que o conteúdo é carregado no cartão de conteúdo (no momento da exibição), ele não pode ser alterado durante sua vida útil. Isso se aplica mesmo se você estiver chamando uma API por meio de Conteúdo conectado e os dados do endpoint mudarem. Esses dados não serão atualizados. O cartão só pode ser impedido de ser enviado a novos usuários e removido dos feeds dos usuários. Se você modificar uma campanha, apenas cartões futuros que forem enviados terão a atualização.

#### Atualizando cartões lançados

Para alterar um cartão para usuários que já o receberam, você deve usar um dos seguintes métodos:

##### Opção 1: Duplicar a campanha (recomendado para alterações imediatas)

{% alert tip %}
Recomendamos esta opção para mensagens em que você está mostrando o conteúdo mais recente no cartão, as alterações devem ser exibidas imediatamente ou quando a reelegibilidade está desativada.
{% endalert %}

A primeira abordagem é arquivar a campanha e lançar uma nova campanha duplicada:

1. Interrompa a campanha original e, quando solicitado, selecione `Remove card after the next sync`.
2. Duplique a campanha, faça suas edições e lance a nova versão.

Ao duplicar a campanha, você precisa definir o público para a nova versão. Use filtros de segmentação para controlar quem recebe o cartão atualizado:
* Se os usuários nunca devem ser reelegíveis para um cartão de conteúdo, você pode filtrar por usuários que não receberam a versão anterior do cartão de conteúdo definindo o filtro `Received Message from Campaign` com a condição `Has Not`.
* Se os usuários que receberam o cartão anterior devem ser reelegíveis em X dias, você pode definir o filtro para `Last Received Message from specific campaign` como mais de X dias atrás **OU** `Received Message from Campaign` com a condição `Has Not`.

###### Impacto

* **Destinatários existentes:** Destinatários novos e existentes veriam o cartão atualizado na próxima atualização do feed, se forem elegíveis.
* **Relatórios:** Cada versão do cartão teria análises de dados separadas.

Digamos que você configurou uma campanha para ser disparada no início da sessão, com reelegibilidade definida para 30 dias. Um usuário recebeu a campanha dois dias atrás e você quer alterar o texto. Primeiro, você arquivaria a campanha e removeria os cartões do feed. Segundo, duplicaria a campanha e relançaria com o novo texto. Se o usuário tiver outra sessão, receberá imediatamente o novo cartão.

##### Opção 2: Interromper e relançar a mesma campanha

{% alert tip %}
Recomendamos usar esta opção para mensagens únicas em uma central de notificações ou caixa de mensagens (como promoções), quando é importante que a análise de dados seja unificada, ou quando a urgência da mensagem não é uma preocupação (ou seja, os destinatários existentes podem esperar pelo período de elegibilidade antes de ver os cartões atualizados).
{% endalert %}

Essa abordagem mantém toda a sua análise de dados unificada em uma única campanha. Usuários recém-elegíveis recebem o novo cartão, mas a atualização é atrasada para os destinatários existentes até que se tornem reelegíveis:

1. Interrompa sua campanha e, quando solicitado, selecione **Remove card after the next sync**.
2. Edite sua campanha conforme necessário.
3. Reinicie sua campanha.

###### Impacto

* **Destinatários existentes:** Usuários que já receberam o cartão não receberiam os cartões atualizados até se tornarem reelegíveis. Se a reelegibilidade estiver desativada, eles nunca receberiam o novo cartão.
* **Relatórios:** Uma campanha contém toda a análise de dados de relatórios para as versões de cartão lançadas. A Braze não diferenciará entre as versões lançadas.

Digamos que você tem uma campanha disparada no início da sessão com reelegibilidade definida para 30 dias. Um usuário recebeu a campanha dois dias atrás e você quer alterar o texto. Primeiro, interrompa a campanha e remova o cartão do feed. Segundo, republique a campanha com o novo texto. Se o usuário tiver outra sessão, receberá o novo cartão em 28 dias.

#### Removendo e expirando cartões

##### Remoção manual de cartões

Você pode remover manualmente cartões dos feeds de todos os usuários a qualquer momento interrompendo a campanha.

1. Abra a campanha de cartão de conteúdo e selecione Interromper campanha.
2. Quando solicitado, selecione **Remove card after the next sync**. O cartão é removido na próxima atualização do feed.

##### Remoção automatizada de cartões {#action-based-card-removal}

Você pode remover automaticamente um cartão quando um usuário realiza uma ação específica, como concluir uma compra ou ativar um recurso.

Na sua campanha ou etapa do Canvas, especifique um evento de remoção. Quando um usuário realiza esse evento, o cartão é removido do feed em uma atualização subsequente após a Braze processar o evento. 

{% alert note %}
Essa remoção não é instantânea. Há um atraso de processamento, então pode levar vários minutos e mais de uma atualização do feed para o cartão desaparecer.
{% endalert %}

{% alert tip %}
Você pode especificar vários eventos personalizados e compras que devem remover um cartão do feed de um usuário. Quando **qualquer** uma dessas ações for realizada pelo usuário, quaisquer cartões existentes enviados pela campanha são removidos. Quaisquer cartões futuros elegíveis continuam a ser enviados de acordo com o cronograma da mensagem.
{% endalert %}

![Painel de condições de remoção de cartão de conteúdo com a opção de evento de remoção de cartão de conteúdo.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### Expiração de cartões

Os Cartões de conteúdo permanecem disponíveis por até 30 dias a partir do envio; após 30 dias, a Braze os remove dos feeds dos usuários e os elimina dos sistemas da Braze.

#### Fazendo cartões durarem mais de 30 dias

{% alert tip %}
Para casos de uso que exigem que as mensagens persistam por mais tempo que o limite de 30 dias dos Cartões de conteúdo, considere usar Banners. Os Banners são projetados para persistência e não têm uma data de expiração obrigatória, permitindo que permaneçam visíveis pelo tempo que for necessário.
{% endalert %}

Se você quiser que um cartão pareça estar sempre disponível, pode criar uma campanha recorrente que efetivamente substitui o cartão a cada 30 dias:

1. Defina a duração do cartão de conteúdo para 30 dias.
2. Defina a reelegibilidade da campanha para 30 dias.
3. Configure a campanha para ser disparada no "Início da sessão".