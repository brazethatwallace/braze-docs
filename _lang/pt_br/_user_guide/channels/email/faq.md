---
nav_title: FAQ
article_title: FAQ sobre e-mail
page_order: 30
description: "Esta página fornece respostas para perguntas frequentes sobre envio de mensagens por e-mail."
channel: email

---

# Perguntas frequentes {#frequently-asked-questions}

> Este artigo fornece respostas para algumas perguntas frequentes sobre e-mails.

## O que acontece quando um e-mail é enviado e vários perfis têm o mesmo endereço de e-mail? {#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address}

Se vários usuários com endereços de e-mail correspondentes estiverem em um Segment or segmento para receber uma Campaign, um único perfil de usuário com esse endereço de e-mail é selecionado no momento do envio. Dessa forma, o e-mail é enviado apenas uma vez e deduplicado, garantindo que não chegue ao mesmo endereço de e-mail várias vezes.

**Endereços de e-mail exclusivos:** A Braze não exige endereços de e-mail exclusivos entre perfis. Se você depende de uma relação um-para-um entre um endereço de e-mail e um perfil, monitore duplicatas internamente ao criar usuários.

**Deduplicação antes do Liquid:** Para envios em que a Braze deduplica por endereço de e-mail dentro de um único despacho (por exemplo, Campaigns agendadas em que vários membros de Segments com o mesmo endereço são processados juntos), essa deduplicação acontece antes de o Liquid ser executado para o perfil escolhido para representar aquele endereço. Se o Liquid for interrompido para esse perfil (por exemplo, com [`abort_message()`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)), esse endereço não recebe a mensagem naquele despacho — incluindo perfis já ignorados pela deduplicação. Envios disparados não aplicam essa mesma deduplicação de endereço dentro do despacho; vários perfis que compartilham um endereço podem permanecer elegíveis em um lote, então esse comportamento de interrupção não se aplica da mesma forma (veja o próximo parágrafo).

Se vários perfis compartilham um endereço de e-mail e um perfil cancela a inscrição, a Braze atualiza outros perfis (até 100) com esse endereço para o mesmo estado de inscrição. Isso se aplica a cancelamentos de inscrição e outras alterações, como estado de inscrição global e status individuais de grupos de inscrições.

**Grupos de teste:** Para Campaigns com [grupos de teste]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups), a Braze seleciona um perfil para entrega principal quando vários perfis compartilham um endereço. Esse destinatário principal pode não estar no seu grupo de teste, mesmo quando outro perfil com o mesmo endereço está.

Os seguintes cenários podem fazer parecer que um usuário recebeu um e-mail duas vezes:

- **Listas de teste ou destinatários de teste:** Endereços de teste e destinatários internos de teste podem receber um envio além do seu público principal, o que pode parecer uma duplicata quando uma caixa de entrada corresponde tanto a um perfil quanto a uma entrada de teste.
- **Ocorreu um erro durante a criação da Campaign ou do Canvas:** O usuário pode não receber o mesmo envio duas vezes, mas pode receber dois e-mails separados com a mesma linha de assunto. Quando uma Campaign ou Canvas é duplicada, verifique os detalhes de configuração do e-mail, como imagens ou linhas de assunto. Você também pode consultar os changelogs para ver se a Campaign ou o Canvas foi modificado após o lançamento — uma duplicata pode compartilhar a mesma linha de assunto que a original quando o usuário a recebeu.
- **Vários perfis de usuário têm encaminhamento de e-mail:** Se um usuário tem várias contas em um determinado app, mas uma conta encaminha e-mails, o usuário recebe a Campaign uma vez por caixa de entrada; o e-mail pode aparecer duas vezes na caixa de entrada para onde as mensagens são encaminhadas. Apenas alguns provedores indicam quando um e-mail foi encaminhado de outra conta.
- **Configuração de e-mail no destinatário:** Alguns clientes de e-mail mesclam caixas de entrada ("caixa de entrada universal"). Se a mesma Campaign direciona várias contas que compartilham uma caixa de entrada, pode parecer que uma pessoa recebeu a Campaign duas vezes quando dois perfis distintos foram realmente notificados. O destinatário pode confirmar se várias contas estão combinadas em uma única caixa de entrada.

Essa deduplicação se aplica quando os usuários direcionados estão no mesmo despacho. A reelegibilidade é avaliada por perfil, não por endereço de e-mail.

A reelegibilidade de Campaigns de e-mail e etapas do Canvas usa o perfil de cada usuário — não a caixa de entrada — então vários perfis podem se qualificar para envios separados enquanto essa lógica é satisfeita. Combinado com disparadores, isso pode entregar mais de uma mensagem para a mesma caixa de entrada, mesmo quando você está tentando respeitar um único período de inelegibilidade no nível do endereço. Campaigns disparadas (excluindo Campaigns disparadas por API or interface de programação do aplicativo (API)) e Canvas também podem enviar duas vezes para um endereço quando perfis diferentes com endereços de e-mail correspondentes atendem ao disparador em momentos diferentes — por exemplo, se o usuário A e o usuário B compartilham `johndoe@example.com`, mas estão em fusos horários diferentes enquanto a entrega usa fusos horários locais.

Os usuários não são deduplicados por e-mail na entrada do Canvas, então podem não ser deduplicados além da primeira etapa de um Canvas se progredirem em momentos ligeiramente diferentes devido à entrada com limite de frequência. Quando um usuário associado a um determinado endereço de e-mail abre ou clica em um e-mail, todos os perfis de usuário que compartilham esse endereço de e-mail são marcados como tendo aberto ou clicado na Campaign.

### Exceção: Campaigns disparadas por API or interface de programação do aplicativo (API) {#exception-api-triggered-campaigns}

Campaigns disparadas por API or interface de programação do aplicativo (API) deduplicarão ou enviarão duplicatas dependendo de onde o público é definido. E-mails duplicados devem ser direcionados separadamente na chamada de API or interface de programação do aplicativo (API) usando `user_ids` distintos para receber várias entregas. Aqui estão três cenários possíveis para Campaigns disparadas por API or interface de programação do aplicativo (API):

- **Cenário 1: E-mails duplicados no Segment or segmento de destino:** Se o mesmo e-mail aparece em vários perfis de usuário que estão agrupados nos filtros de público do dashboard para uma Campaign disparada por API or interface de programação do aplicativo (API), apenas um dos perfis recebe o e-mail.
- **Cenário 2: E-mails duplicados em `user_ids` diferentes dentro do objeto de destinatários:** Se o mesmo e-mail aparece em vários valores `external_user_id` referenciados pelo objeto `recipients`, o e-mail é enviado duas vezes.
- **Cenário 3: E-mails duplicados devido a `user_ids` duplicados dentro do objeto de destinatários:** Se você tenta adicionar o mesmo perfil de usuário duas vezes, apenas um dos perfis recebe o e-mail.

{% alert important %}
Se você enviar uma Campaign de API or interface de programação do aplicativo (API) por meio de uma chamada de API or interface de programação do aplicativo (API) (excluindo Campaigns disparadas por API or interface de programação do aplicativo (API)), e vários usuários forem especificados no público do Segment or segmento com o mesmo endereço de e-mail, o envio será feito para esse endereço tantas vezes quanto listado na chamada. Isso ocorre porque as chamadas de API or interface de programação do aplicativo (API) são consideradas construídas intencionalmente.
{% endalert %}

#### Testes A/B com endereços de e-mail duplicados {#ab-testing-with-duplicate-email-addresses}

Evite [testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) em e-mail quando vários perfis podem compartilhar o mesmo endereço de e-mail. As variantes são atribuídas por perfil, o que pode produzir mais de uma mensagem para a mesma caixa de entrada. Se você precisar testar nessa situação, não combine uma etapa de **variante vencedora** com [entrega por fuso local]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) de uma forma que atrase a seleção do vencedor — essas opções juntas podem aumentar a chance de envios duplicados.

#### Canvas e endereços de e-mail duplicados {#canvas-and-duplicate-email-addresses}

Para jornadas do Canvas, se endereços de e-mail duplicados recebem um envio ou mais de um pode depender do lote de entrada, do tempo das etapas e de outros fatores. Trate o comportamento como indefinido até validá-lo para a sua jornada. Sempre que possível, mescle ou consolide perfis duplicados. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="deterministic deduplication for duplicate email addresses in Canvas" %}

### O que acontece com o estado de inscrição quando o endereço de e-mail de um usuário muda para um compartilhado por outro usuário? {#what-happens-to-the-subscription-state-when-a-users-email-address-changes-to-one-shared-by-another-user}

Se você definir ou atualizar o endereço de e-mail do usuário A para outro endereço de e-mail que é compartilhado por um usuário B existente, o usuário A herda o estado de inscrição que já existe do usuário B, a menos que a configuração **Reinscrever usuários quando atualizarem seu e-mail** esteja ativada.

### As atualizações nas minhas configurações de e-mail de saída serão aplicadas retroativamente? {#will-updates-to-my-outbound-email-settings-apply-retroactively}

Não. As atualizações feitas nas configurações de e-mail de saída não afetam retroativamente os envios existentes. Por exemplo, alterar o nome de exibição padrão nas configurações de e-mail não substituirá automaticamente o nome de exibição padrão existente nas suas Campaigns ou Canvas ativos.

### O que é uma "boa" taxa de entrega de e-mail? {#what-is-a-good-email-delivery-rate}

Normalmente, o "número mágico" é cerca de 98% das mensagens entregues, com uma taxa de bounce não superior a 3%. Se menos de 98% das mensagens forem entregues, geralmente há motivo para preocupação.

No entanto, uma taxa de entrega de 98% ou superior ainda pode apresentar problemas de entregabilidade. Por exemplo, se todos os seus bounces vêm de um único domínio, isso é um sinal claro de um problema de reputação com esse provedor.

Além disso, as mensagens podem estar sendo entregues e indo para a pasta de SPAM, indicando problemas de reputação potencialmente sérios. É importante monitorar não apenas o número de mensagens sendo entregues, mas também as taxas de abertura e cliques para determinar se os usuários estão realmente vendo as mensagens em suas caixas de entrada. Como os provedores geralmente não relatam cada instância de SPAM, uma taxa de SPAM de apenas 1% pode ser motivo de preocupação e análise adicional.

Por fim, o seu negócio e os tipos de e-mails que você envia também podem afetar a entrega. Por exemplo, alguém que envia principalmente [e-mails de transação]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email) deve esperar uma taxa melhor do que alguém que envia muitas mensagens de marketing.

### Por que as minhas métricas de entrega de e-mail não somam 100%? {#why-are-my-email-delivery-metrics-not-adding-up-to-100}

As métricas de entrega de e-mail (entregas, bounces e taxa de SPAM) podem não somar 100% por causa de e-mails que sofrem soft bounce e não são entregues após o período de nova tentativa de até 72 horas.

Soft bounces são e-mails que sofrem bounce devido a um problema temporário ou transitório, como "caixa de entrada cheia", "servidor temporariamente indisponível" e outros. Se um e-mail com soft bounce ainda não for entregue após 72 horas, esse e-mail não será contabilizado nas métricas de entrega da Campaign.

### O que é um loop de feedback de e-mail? {#what-is-an-email-feedback-loop}

Um loop de feedback de e-mail (FBL) permite que os remetentes monitorem sua reputação identificando Campaigns que recebem um alto volume de reclamações. Para saber as etapas para implementar um loop de feedback do Gmail, consulte o artigo [Loop de feedback do Google](https://support.google.com/a/answer/6254652).

### O que são pixels de rastreamento de abertura? {#what-are-open-tracking-pixels}

[Pixels de rastreamento de abertura]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement) utilizam o domínio de rastreamento de cliques de e-mail do remetente para rastrear eventos de abertura de e-mail. O pixel é uma tag de imagem adicionada ao HTML do e-mail. Geralmente, é o último elemento HTML dentro da tag body. Quando um usuário carrega seu e-mail, uma requisição é feita para preencher a imagem a partir do domínio de rastreamento de marca, que registra um evento de abertura.

### Posso rastrear aberturas de e-mails renderizados em texto simples? {#can-i-track-opens-for-emails-rendered-in-plain-text}

Não. A Braze rastreia aberturas de e-mail usando um [pixel de rastreamento de abertura]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#open-tracking-pixel) incorporado no HTML do e-mail. Quando o cliente de e-mail do destinatário carrega o e-mail, ele solicita essa imagem, e a Braze registra um evento de abertura.

Como e-mails em texto simples não podem conter imagens, o pixel de rastreamento de abertura não é incluído, então as aberturas não podem ser rastreadas para e-mails renderizados em texto simples. Os cliques ainda podem ser rastreados, pois os hyperlinks permanecem funcionais em texto simples.

Esse é o comportamento esperado. Para precisão na taxa de abertura, crie e-mails em HTML e esteja ciente de que as aberturas não serão contabilizadas quando os destinatários visualizarem a versão em texto simples.

### Como funciona o rastreamento de e-mail quando os destinatários encaminham e-mails? {#how-does-email-tracking-work-when-recipients-forward-emails}

Quando um destinatário encaminha um e-mail, o e-mail encaminhado inclui o mesmo pixel de rastreamento de abertura e os mesmos links de rastreamento de cliques do original. Isso significa:

- Se alguém que não estava no público original da sua Campaign receber um e-mail encaminhado e abri-lo, a Braze registra um evento de abertura.
- Se essa pessoa clicar em um link no e-mail encaminhado, a Braze registra um evento de clique.
- Esses eventos são atribuídos ao perfil do destinatário original, não à pessoa que recebeu o e-mail encaminhado, porque o pixel de rastreamento e os links estão vinculados ao destinatário original.

A Braze não consegue distinguir entre aberturas e cliques do destinatário original e aqueles de pessoas que receberam uma cópia encaminhada. Esse é o comportamento padrão para pixels de rastreamento de e-mail e afeta todos os provedores de serviços de e-mail.

Ao analisar as métricas de e-mail, esteja ciente de que a atividade de encaminhamento pode contribuir para as contagens de aberturas e cliques. Se você notar taxas de engajamento incomumente altas ou atividade repetida do mesmo perfil ao longo do tempo, o encaminhamento pode ser um fator.

### Uma Campaign de e-mail ou Canvas enviado pode ser cancelado? {#can-a-sent-email-campaign-or-canvas-be-recalled}

Não. Depois que a Braze entrega uma solicitação de envio ao seu provedor de serviços de e-mail (ESP), esse envio não pode ser cancelado. Depois que a mensagem está na caixa de entrada do destinatário, ela também não pode ser removida.

Para interromper envios futuros, selecione **Parar Campaign** ou **Parar Canvas**. Mensagens já entregues ao ESP ainda podem ser enviadas. Para saber mais, consulte [O que acontece quando uma Campaign de e-mail ou Canvas é parado?](#what-happens-when-an-email-campaign-or-canvas-is-stopped)

### O que acontece quando uma Campaign de e-mail ou Canvas é parado? {#what-happens-when-an-email-campaign-or-canvas-is-stopped}

Os usuários são impedidos de entrar no Canvas e nenhuma mensagem adicional é enviada.

Para Campaigns de e-mail e Canvas, o botão de parar não interrompe o envio imediatamente. Quando as solicitações de envio são enviadas, elas não podem ser impedidas de serem entregues ao usuário, o que pode acontecer após algum atraso.

Embora a Braze não envie mais solicitações depois que a Campaign ou o Canvas é parado, as análises ainda podem aumentar enquanto o ESP finaliza o processamento das solicitações que já estavam em andamento.

### Por que estou vendo mais _Total de cliques_ do que _Total de aberturas_ nas minhas análises de e-mail? {#why-am-i-seeing-more-_total-clicks_-than-_total-opens_-in-my-email-analytics}

_Total de aberturas_ é a contagem de quantas vezes o e-mail foi aberto pelos usuários, enquanto _Total de cliques_ é a contagem de quantas vezes os usuários clicaram dentro do e-mail entregue, incluindo qualquer tipo de clique, como cliques em links. Você pode estar vendo mais cliques do que aberturas por qualquer um dos seguintes motivos:

- Os usuários estão realizando vários cliques no corpo do e-mail dentro de uma única abertura.
- Os usuários clicam em alguns links de e-mail dentro do painel de visualização dos seus celulares. Nesse caso, a Braze registra esse e-mail como clicado, mas não como aberto.
- Os usuários reabrem um e-mail que visualizaram anteriormente.

### Por que minhas contagens de cliques são maiores do que meu Segment or segmento de usuários que clicaram? {#why-are-my-click-counts-higher-than-my-segment-of-users-who-clicked}

As análises da Campaign mostram o número total de eventos de clique, enquanto os Segments retornam o número de usuários únicos que realizaram esses cliques. Como cada usuário pode clicar várias vezes, o total de cliques nas análises é geralmente maior do que a contagem de usuários que clicaram quando você cria um Segment or segmento.

Por exemplo, se 100 usuários clicam em um link 3 vezes cada, as análises da Campaign mostram 300 cliques totais, mas um Segment or segmento filtrado por "Clicou no e-mail" para essa Campaign retorna 100 usuários.

### Por que estou vendo zero aberturas e cliques de e-mail? {#why-am-i-seeing-zero-email-opens-and-clicks}

Você pode ver nenhuma abertura ou clique de e-mail se houver uma configuração incorreta no seu domínio de rastreamento. Isso pode ser devido a qualquer um dos seguintes motivos:
- Há um problema de SSL em que as URLs de rastreamento são `http` em vez de `https`.
- Há um problema com sua CDN em que a string de user agent nos eventos de abertura, eventos de clique ou ambos não está sendo preenchida.

### Por que estou vendo comportamento incomum de abertura ou clique de e-mail? {#why-am-i-seeing-unusual-email-open-or-click-behavior}

Se você notar padrões inesperados nas suas métricas de abertura ou clique de e-mail — como um único usuário parecendo clicar em todos os links imediatamente, ou aberturas não sendo registradas como esperado — revise as seguintes causas comuns:

#### O recorte de e-mail remove o pixel de rastreamento {#email-clipping-removes-the-tracking-pixel}

Quando um e-mail é recortado pelo provedor de e-mail do destinatário (como o Gmail recortando mensagens com mais de aproximadamente 102 KB), o conteúdo na parte inferior do e-mail pode ser truncado. Como o pixel de rastreamento de abertura é normalmente inserido na parte inferior do e-mail, o recorte pode impedir que o rastreamento de abertura funcione.

**Como identificar:** Verifique se o e-mail exibe um link "Ver mensagem completa" ou similar na parte inferior. Você pode usar o [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) para visualizar o e-mail completo com rolagem e verificar se a mensagem está sendo recortada.

**Como resolver:** Você pode configurar a Braze para posicionar o pixel de rastreamento no topo do e-mail em vez da parte inferior. Mover o pixel de rastreamento pode afetar como alguns clientes de e-mail renderizam seu HTML, então teste seus e-mails no Inbox Vision após fazer essa alteração. Observe que, se o destinatário tiver imagens desativadas, as aberturas não podem ser rastreadas independentemente do posicionamento do pixel.

#### O pixel de rastreamento causa espaço branco no topo do e-mail {#tracking-pixel-causes-white-gap-at-top-of-email}

Quando o pixel de rastreamento de abertura é posicionado no topo de um e-mail, uma linha ou lacuna branca visível pode aparecer no topo do corpo do e-mail, particularmente em dispositivos móveis.

**Como identificar:** Na Braze, acesse **Configurações** > **Preferências de E-mail** e selecione a seção **Pixel de rastreamento de abertura**. Se **Mover para SendGrid**, **Mover para SparkPost** ou **Mover para Amazon SES** estiver ativado para o seu provedor de envio, o pixel está posicionado no topo do HTML do seu e-mail. Se você notar uma lacuna ou linha branca no topo do seu e-mail renderizado, essa configuração pode ser a causa.

**Como resolver:** Desative a opção relevante **Mover para SendGrid**, **Mover para SparkPost** ou **Mover para Amazon SES** na seção **Pixel de rastreamento de abertura** para o seu provedor de envio. O pixel de rastreamento geralmente é menos visível na parte inferior de um e-mail. Teste seus e-mails no [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) após alterar o posicionamento. Para saber mais, consulte [Atualizar o posicionamento]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement).

#### Estatísticas atrasadas ou cliques sem aberturas {#delayed-stats-or-clicks-without-opens}

O rastreamento de abertura depende do destinatário carregar o e-mail com imagens ativadas. Em alguns casos, as estatísticas podem parecer atrasadas ou cliques podem ser registrados sem aberturas correspondentes devido a:

- O destinatário visualizar o e-mail em um painel de visualização sem abri-lo completamente, e então clicar em links diretamente da visualização.
- O cliente de e-mail não carregar imagens (e, portanto, o pixel de rastreamento) até depois que o destinatário interagiu com os links.

#### Software de segurança simula cliques em links {#security-software-simulates-link-clicks}

Algumas ferramentas de segurança de e-mail corporativo (como Barracuda, Proofpoint e serviços similares) verificam e-mails recebidos clicando automaticamente em todos os links na mensagem para verificar se são seguros. Isso pode resultar em eventos de clique aparecendo em segundos após o envio, frequentemente com todos os links do e-mail clicados em rápida sucessão.

Esse comportamento é mais comum com domínios de e-mail institucionais (como escolas, universidades e ambientes corporativos) e é mais provável quando o seu domínio de envio difere significativamente do seu domínio de rastreamento. Configurar um [domínio de rastreamento personalizado de marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) pode reduzir a frequência desses cliques automatizados.

**Como identificar:** Pesquise o endereço IP do evento de clique (disponível nos dados do Currents) em um mecanismo de busca. Se o IP estiver associado a um provedor de segurança conhecido (como Barracuda Networks), os cliques provavelmente são automatizados. Você também pode ver um cabeçalho User-Agent consistente em vários cliques automatizados.

Para contexto adicional sobre como a verificação de segurança afeta as métricas de e-mail, consulte [Lidando com aumentos nas taxas de cliques]({{site.baseurl}}/user_guide/channels/email/reporting).

### Quais são os riscos potenciais de disparar cliques de servidor? {#what-are-the-potential-risks-of-triggering-server-clicks}

Certos elementos de uma mensagem de e-mail, como mensagens excessivamente longas ou muitos pontos de exclamação, podem disparar respostas de segurança de e-mail. Essas respostas podem afetar os relatórios e a reputação do IP e levar os usuários a cancelar a inscrição.

Para saber as melhores práticas sobre como lidar com essas respostas, consulte [Lidando com aumentos nas taxas de cliques]({{site.baseurl}}/user_guide/channels/email/reporting).

### A Braze pode rastrear links de cancelamento de inscrição contabilizados na métrica "Cancelamentos de inscrição"? {#can-braze-track-unsubscribe-links-counted-toward-the-unsubscribe-metric}

A Braze rastreia links de cancelamento de inscrição se o seguinte Liquid for usado nos e-mails: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Por que estou vendo um número diferente de cancelamentos de inscrição do que cliques no meu link de cancelamento de inscrição? {#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link}

Se houver mais _Cancelamentos de inscrição_ do que usuários que clicaram no link de cancelamento de inscrição no corpo do e-mail, o [**List-unsubscribe**]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) geralmente explica a diferença. O List-unsubscribe é um caminho adicional de cancelamento de inscrição no cabeçalho do e-mail (não o link no corpo da sua mensagem). Quando um usuário cancela a inscrição dessa forma, isso conta como _Cancelamentos de inscrição_, mas não conta como um clique na URL de cancelamento de inscrição rastreada no corpo.

Se o número total de cliques no link de cancelamento de inscrição no corpo for maior que o número de _Cancelamentos de inscrição_, os usuários podem ter clicado no link mais de uma vez — por exemplo, se cancelaram a inscrição, se reinscreveram e cancelaram novamente, as análises de e-mail podem registrar vários cliques no detalhamento de cliques.

Se um usuário clicar no link de cancelamento de inscrição duas vezes (por exemplo, se cancelou a inscrição, se inscreveu novamente e então cancelou novamente), isso conta duas vezes nas análises de e-mail.

### Posso adicionar um link "ver este e-mail no navegador" aos meus e-mails? {#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails}

Não. A Braze não oferece essa funcionalidade. Isso ocorre porque a grande maioria dos e-mails é aberta em dispositivos móveis e em clientes de e-mail modernos, que renderizam imagens e conteúdo sem problemas.

**Alternativa:** Para alcançar esse mesmo resultado, você pode hospedar o conteúdo do seu e-mail em uma landing page externa (como o seu website), que pode então ser vinculada a partir da Campaign de e-mail que você está criando, usando a ferramenta **Link** ao editar o corpo do e-mail.

### A Braze converte automaticamente URLs em texto simples ou texto "www." em links? {#does-braze-automatically-turn-plain-text-urls-or-www-text-into-links}

Não. A Braze não verifica sua mensagem e converte texto simples, como texto que começa com `www.` ou parece uma URL, em hyperlinks. Apenas links que você define com tags de âncora HTML (`<a href="...">`) são processados por meio da renderização normal e dos recursos de link na Braze.

Se um destinatário vê texto simples exibido como um link clicável, esse comportamento geralmente vem do cliente de e-mail dele (por exemplo, Gmail, Outlook ou Apple Mail). Muitos clientes detectam strings parecidas com URLs após a entrega da mensagem e as transformam em links no dispositivo do destinatário. A Braze não controla esse comportamento e não pode desativá-lo para o destinatário.

Para aparência, rastreamento e estilização previsíveis dos links, use tags `<a href>` explícitas em vez de URLs em texto simples.

### Posso controlar o atributo `target` nos links de e-mail? {#can-i-control-the-target-attribute-on-email-links}

Embora você possa definir o atributo `target` (como `target="_blank"` ou `target="_top"`) nos links do HTML do seu e-mail, a maioria dos clientes de e-mail ignora ou substitui esse atributo. Por exemplo, o Gmail efetivamente força um comportamento semelhante a `_blank` independentemente do que você especificar.

Como o comportamento do cliente de e-mail varia, o atributo `target` não deve ser usado como método confiável para controlar como os links abrem. Para saber quais clientes de e-mail suportam o atributo `target`, consulte [caniemail.com](https://www.caniemail.com/features/html-target/).

### Por que um sinal de mais `+` no meu link de e-mail se transforma em um espaço? {#why-does-a-plus-sign-in-my-email-link-turn-into-a-space}

Alguns analisadores de consulta tratam um sinal de mais `+` não codificado como um espaço. Se a URL de destino precisa de um sinal de mais em um parâmetro de consulta, codifique-o em porcentagem como `%2B` antes de adicionar o link ao seu e-mail.

### Por que meus usuários estão sendo cancelados automaticamente por software de segurança de e-mail? {#why-are-my-users-being-auto-unsubscribed-by-email-security-software}

Algumas ferramentas de segurança de e-mail corporativo (como Barracuda, Proofpoint e serviços similares) pré-buscam ou verificam todas as URLs em e-mails recebidos, incluindo links de cancelamento de inscrição. Isso pode causar cancelamentos de inscrição não intencionais quando a ferramenta de segurança segue o link de cancelamento de inscrição com um clique.

Para mitigar isso:

- **Recomende que os destinatários adicionem seu domínio de envio à lista de permissões:** Trabalhe com as equipes de TI dos destinatários afetados para adicionar seu domínio de envio e os domínios de rastreamento da Braze à lista de permissões de segurança de e-mail.
- **Use uma Central de Preferências:** Em vez de um link direto de cancelamento de inscrição, use uma [Central de Preferências]({{site.baseurl}}/user_guide/channels/email/subscriptions) que exija interação do usuário para confirmar a ação de cancelamento de inscrição. Verificadores de segurança normalmente não completam formulários de várias etapas.
- **Revise os logs de cancelamento de inscrição:** Verifique o cabeçalho `User-Agent` e o endereço IP nos dados de eventos de cancelamento de inscrição do Currents para identificar padrões consistentes com verificação automatizada (como cabeçalhos `User-Agent` consistentes em vários cancelamentos de inscrição).

Para saber mais sobre como a verificação do lado do servidor pode afetar as métricas de e-mail, consulte [Lidando com aumentos nas taxas de cliques]({{site.baseurl}}/user_guide/channels/email/reporting).

### Por que minha taxa de abertura por máquina mudou inesperadamente? {#why-has-my-machine-open-rate-changed-unexpectedly}

[Aberturas por máquina]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) são disparadas por recursos de segurança de e-mail, como a Proteção de Privacidade do Apple Mail (MPP or proteção de privacidade de e-mail), que pré-carrega o conteúdo do e-mail (incluindo o pixel de rastreamento) sem que o usuário abra fisicamente o e-mail. As taxas de abertura por máquina podem flutuar com base em:

- Mudanças na proporção do seu público usando Apple Mail ou outros clientes de e-mail com privacidade ativada.
- Atualizações nos recursos de privacidade dos provedores de e-mail ou comportamentos de detecção de bots.
- Mudanças na sua segmentação ou direcionamento de público.

As porcentagens de abertura por máquina não são uma medida confiável do engajamento real. Para uma visão mais precisa do desempenho do e-mail, concentre-se em *Outras aberturas* (aberturas não por máquina) e *Cliques únicos*. Você também pode comparar essas métricas ao longo do tempo usando o [Dashboard de desempenho de e-mail]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance).

### Por que meus deep links não estão funcionando no Gmail? {#why-are-my-deep-links-not-working-in-gmail}

O Gmail remove todos os links não-HTTP/HTTPS de mensagens de e-mail. Se o seu deep link usa um esquema personalizado (como `myapp://path/to/content`), o Gmail o removerá, e o link não funcionará para os destinatários que leem o e-mail no Gmail. Essa é uma limitação do Gmail, não da Braze.

Para contornar isso:

- **Use Universal Links (iOS) ou App Links (Android).** Eles usam URLs `https://` padrão que abrem seu app quando instalado e redirecionam para uma página web caso contrário. Consulte [Universal Links e App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links) para instruções de configuração.
- **Use um provedor de deep linking.** Serviços como [Branch or ramificação](https://www.branch.io/) geram deep links no formato HTTP compatíveis com clientes de e-mail, incluindo o Gmail.
- **Configure um endpoint de redirecionamento.** Hospede um endpoint `https://` no seu servidor que redirecione para a URL de esquema personalizado do seu app. Os clientes de e-mail preservarão o link `https://`, e o redirecionamento cuidará de abrir o app.

### A métrica *Aberturas únicas* inclui *Aberturas por máquina*? {#does-the-unique-opens-metric-include-machine-opens}

Sim. *Aberturas únicas* incluem *Aberturas por máquina*. Você pode visualizar ambas as métricas na visualização de **Análise da Campaign** e no **Report Builder**.

Para saber como isso afeta a atribuição do **Dashboard de conversões**, consulte [Por que os totais de abertura de e-mail não correspondem às análises da Campaign?]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#why-dont-email-open-totals-match-campaign-analytics) em [Solução de problemas]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#troubleshooting) na página do Dashboard de conversões.

### Por que o volume de entrega de e-mail não corresponde ao volume de envio? {#why-does-my-email-delivery-volume-not-match-my-send-volume}

Depois que um e-mail é enviado, a caixa de entrada do destinatário decide quando ele é entregue. As mensagens podem ser adiadas por horas ou dias por causa de uma caixa de entrada cheia, limitação do ESP de um determinado IP e razões semelhantes.

Quando mensagens adiadas são entregues em um dia diferente do dia de envio, as _Entregas_ podem exceder os _Envios_ para o mesmo intervalo de datas. Quando muitos adiamentos são entregues em um dia, os _Envios_ podem exceder as _Entregas_ para esse intervalo.

### Por que estou vendo um aviso para incluir um link de cancelamento de inscrição quando meu e-mail já tem um? {#why-am-i-seeing-a-warning-to-include-an-unsubscribe-link-when-my-email-already-has-one}

Esse aviso pode persistir para Campaigns duplicadas de uma Campaign que não tinha um link de cancelamento de inscrição. Para resolvê-lo:

- Para e-mails HTML, acesse a guia **Texto simples** e selecione **Regenerar a partir do HTML**.
- Após duplicar, duplique a variante e remova a variante original. **Não** selecione a variante original, pois o aviso pode permanecer.

### Por que um usuário recebeu um e-mail que não deveria ter recebido? {#why-did-a-user-receive-an-email-they-shouldnt-have}

A entrega pode parecer incorreta mesmo quando a Braze se comportou conforme configurado. Verifique o seguinte:

- **Perfis duplicados** que compartilham uma caixa de entrada (consulte [O que acontece quando um e-mail é enviado e vários perfis têm o mesmo endereço de e-mail?](#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address)).
- **Listas de teste, destinatários de teste ou endereços internos** incluídos no público ou em um envio como CC/BCC.
- **Momento do Segment or segmento ou Canvas:** o usuário correspondia ao público ou à etapa do Canvas quando a Braze avaliou a elegibilidade, mas os atributos ou estado de inscrição mudaram antes de ele ler a mensagem.
- **Grupos de inscrições:** o usuário permaneceu inscrito em um grupo que sua mensagem direcionou, mesmo que seu estado de inscrição global sugeria o contrário.
- **Importações de API or interface de programação do aplicativo (API) ou arquivos** que atualizaram o usuário após a segmentação, mas antes de você esperar que a alteração fosse aplicada.

Revise o [Log de atividades de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), changelogs da Campaign ou Canvas e definição do Segment or segmento. Se você ainda não conseguir reconciliar o envio, entre em contato com o suporte da Braze com identificadores do usuário, `dispatch_id` (se disponível) e timestamps.

### Por que um usuário não recebeu minha mensagem de e-mail? {#why-hasnt-a-user-received-my-email-message}

Existem vários motivos pelos quais um usuário não recebe um e-mail que você esperava que ele recebesse, incluindo:

- Ele não era elegível para receber o e-mail.
- O endereço de e-mail dele é inválido ou não existe.
- Ele pode ter perdido ou excluído a mensagem.
- A mensagem pode estar na pasta de SPAM dele.

{% alert tip %}
Um evento de entrega na Braze significa que o e-mail foi aceito pelo servidor do provedor de caixa de entrada. No entanto, isso não garante que a mensagem apareça na caixa de entrada do usuário. O provedor de caixa de entrada pode direcionar a mensagem para SPAM ou, em casos raros, impedir silenciosamente a exibição da mensagem.
{% endalert %}

Use as tabelas a seguir para identificar a causa.

#### O e-mail não foi enviado {#the-email-wasnt-sent}

| Causa possível | O que verificar |
|---|---|
| O usuário não era elegível para a Campaign ou Canvas | Verifique as configurações de **Públicos-alvo** (para Campaigns) ou **Público-alvo** (para Canvas) nas [configurações]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) para confirmar que o usuário atendeu a todos os filtros de público, critérios de Segment or segmento e regras de entrega no momento do envio. |
| A mensagem foi interrompida | Verifique o [Log de atividades de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) para motivos de interrupção, como erros de Liquid ou campos obrigatórios ausentes. |
| O endereço de e-mail do usuário era inválido ou estava ausente | Na **Pesquisa de usuário**, verifique o perfil do usuário para confirmar que um endereço de e-mail válido estava registrado no momento do envio. |
| O endereço de e-mail do usuário sofreu hard bounce anteriormente | Um hard bounce marca o endereço de e-mail como inválido e impede envios futuros para esse endereço. Da mesma forma, se um destinatário marcar seu e-mail como SPAM, a Braze envia apenas e-mails de transação para esse usuário, não Campaigns padrão. Verifique a guia **Engajamento** do perfil do usuário. Para saber mais, consulte [Endereços de e-mail cancelados]({{site.baseurl}}/user_guide/channels/email/subscriptions#unsubscribed-email-addresses) e [Bounces e e-mails inválidos]({{site.baseurl}}/user_guide/channels/email/subscriptions#bounces-and-invalid-emails). |
| O usuário cancelou a inscrição de e-mail | Verifique o status de inscrição do usuário em **Configurações de contato** na guia **Engajamento**. A Braze não envia e-mails para usuários que cancelaram a inscrição. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Causa de e-mail não enviado" }

#### O e-mail foi enviado, mas não chegou na caixa de entrada {#the-email-was-sent-but-didnt-arrive-in-their-inbox}

| Causa possível | O que verificar |
|---|---|
| O provedor de caixa de entrada (MBP) estava inacessível | Um problema temporário impediu que o e-mail chegasse ao MBP do destinatário. Isso normalmente se resolve com novas tentativas. Os provedores de serviços de e-mail tentam novamente soft bounces por até 72 horas. |
| O MBP rejeitou o e-mail | O servidor de e-mail do destinatário rejeitou o e-mail. Revise o [Log de atividades de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) para detalhes do bounce. |
| O MBP descartou silenciosamente o e-mail | O MBP aceitou o e-mail, mas não o exibiu para o usuário e não retornou um bounce. Isso está fora do controle da Braze e não pode ser detectado nos logs da Braze. |
| O e-mail foi para a pasta de SPAM | O MBP identificou a mensagem como SPAM e a direcionou para a pasta de SPAM ou lixo eletrônico do usuário. Peça ao usuário para verificar a pasta de SPAM. |
| O destinatário tem filtragem de e-mail personalizada | O usuário ou o administrador de TI pode ter configurado regras de caixa de entrada que filtram, redirecionam ou excluem mensagens recebidas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Causa de e-mail não na caixa de entrada" }

### Como posso remover um endereço de e-mail da lista de bounces? {#how-can-i-remove-an-email-address-from-the-bounce-list}

Se um endereço de e-mail válido aparece como inválido na Braze (normalmente após um hard bounce do seu provedor de serviços de e-mail), use o endpoint [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces). Isso remove o endereço da sua lista de bounces da Braze e da lista de bounces mantida pelo seu provedor de e-mail. A Braze então retoma os envios para esse endereço.

Se o endereço foi marcado como SPAM em vez de hard bounce, use o endpoint [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam).

Para saber mais, consulte [Bounces e e-mails inválidos]({{site.baseurl}}/user_guide/channels/email/subscriptions#bounces-and-invalid-emails) e [Remover um endereço de e-mail da sua lista de bounces ou SPAM]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps#remove-an-email-address-from-your-bounce-or-spam-list).

### Como solucionar problemas de entregabilidade de e-mail? {#how-do-i-troubleshoot-email-deliverability-issues}

Se seus e-mails estão atrasados, adiados ou sofrendo bounce, revise o [Log de atividades de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) para detalhes de bounces e adiamentos, e então identifique onde o problema ocorre na cadeia de entrega. Problemas comuns de entregabilidade se dividem em quatro categorias:

#### Lendo respostas de limite de frequência do ESP {#reading-esp-rate-limit-responses}

Seu provedor de serviços de e-mail (ESP), como Amazon SES, SparkPost ou SendGrid, retorna códigos de resposta SMTP ao aceitar ou adiar mensagens. Respostas de limite de frequência normalmente usam códigos 4xx, que indicam falhas temporárias:

- **421:** Serviço temporariamente indisponível, frequentemente devido a alto volume, limites de conexão ou restrições de recursos do servidor. A mensagem permanece na fila e seu ESP tenta a entrega novamente automaticamente.
- **429:** Limite de frequência de API or interface de programação do aplicativo (API) excedido. Você enviou muitas solicitações dentro da janela de tempo permitida.
- **450 / 451:** Adiamento temporário devido a volume ou conexões. O servidor do destinatário está pedindo para você reduzir a velocidade.

Quando você vê esses códigos no [Log de atividades de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) ou no dashboard do seu ESP, reduza o volume de envio para o domínio afetado e use intervalos de tentativa progressivamente mais longos. Continuar com volume total enquanto está com limite de frequência pode escalar adiamentos temporários para rejeições permanentes.

#### Limites de frequência do provedor de caixa de entrada {#mailbox-provider-rate-limits}

Os provedores de caixa de entrada aplicam seus próprios limites de frequência no e-mail recebido, separados dos controles de envio da Braze. Esses limites podem ser rigorosos e estão fora do seu controle direto:

- Virgin Media / NTL (UK): Usa limite de frequência por hora que dispara erros `421 4.1.1 MXIN503 Hourly ratelimit for your IP exceeded`. Esses limites podem afetar até remetentes de baixo volume. Eles são aplicados no nível do IP em todos os remetentes que compartilham esse IP.
- Gmail, Yahoo, iCloud, Microsoft: Cada provedor tem limites proprietários baseados na sua reputação como remetente, volume e padrões de engajamento.

Se você encontrar limites de frequência específicos de um provedor, considere distribuir seus envios em um período mais longo ou segmentar por provedor de caixa de entrada para distribuir o volume mais gradualmente. Verifique sua lista de destinatários para concentração em um provedor — se a maioria dos destinatários usa um domínio, escalone a entrega.

#### Atrasos de e-mail corporativo por verificação de antivírus {#corporate-email-delays-from-antivirus-scanning}

Endereços de e-mail empresariais frequentemente passam por gateways de segurança corporativa que verificam as mensagens antes da entrega. Isso pode atrasar e-mails em 15 a 20 minutos ou mais, especialmente para mensagens com:

- Anexos grandes
- Links para domínios desconhecidos
- Conteúdo que se assemelha a padrões de phishing

Esses atrasos ocorrem porque os sistemas de segurança colocam as mensagens em fila para análise comportamental em ambientes sandbox isolados. Se um grande volume de e-mails chega simultaneamente, as mensagens são enfileiradas para análise e o atraso se estende. Esse é o comportamento normal para segurança de e-mail corporativo e não é algo que você possa contornar. Ao enviar mensagens urgentes para destinatários corporativos, considere essa janela de processamento no seu cronograma de comunicação.

#### Solução de problemas para erros de limite de frequência 421 4.7.28 do Google {#troubleshooting-google-421-4728-rate-limit-errors}

O Gmail retorna um erro `421-4.7.28` quando detecta uma taxa incomum de e-mails não solicitados do seu endereço IP, faixa de IP de envio, domínio SPF, domínio DKIM ou domínio de URL. Essa é uma restrição temporária, não um bloqueio permanente, mas sinaliza que seu volume de envio, velocidade ou reputação não atendem às expectativas atuais do Gmail.

Se você receber esse erro:

1. Pause envios não essenciais imediatamente por 24 a 48 horas. Continuar enviando enquanto está restrito escala o problema e pode levar a rejeições permanentes 550.
2. Confirme que SPF, DKIM e DMARC estão configurados corretamente e que seu cabeçalho From: está alinhado com sua autenticação.
3. Verifique o [Google Postmaster Tools](https://postmaster.google.com/) e o [Centro de entregabilidade]({{site.baseurl}}/user_guide/analytics/dashboards/deliverability_center) da Braze (após conectar o Google Postmaster) para o status de conformidade do seu domínio e taxas de reclamação de SPAM. Sua taxa de SPAM reportada por usuários deve ficar abaixo de 0,1% (o teto máximo é 0,3%).
4. Após a pausa, retome o envio com 10 a 20% do volume anterior apenas para seus destinatários mais engajados. Aumente o volume lentamente ao longo de várias semanas somente se nenhum erro 4xx adicional ocorrer.

Para orientações adicionais, consulte as [Diretrizes do Google para remetentes em massa](https://support.google.com/mail/answer/81126).

### Como posso otimizar imagens no Outlook? {#how-can-i-optimize-images-in-outlook}

O Outlook frequentemente usa renderização do Microsoft Word em vez da renderização padrão do navegador, o que pode fazer com que imagens sejam renderizadas incorretamente ou adicionar bordas ao redor das imagens. Essa mesma renderização específica do cliente também afeta [como o texto alternativo é exibido]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text) em diferentes clientes de e-mail.

Se as imagens forem exibidas maiores do que a largura esperada no Outlook, adicione o seguinte CSS à imagem:

```css
max-width: 100%;
```

Por exemplo:

```html
<img src="your-image.png" style="max-width: 100%;" alt="Description">
```

Você também pode encapsular conteúdo para que ele fique oculto no Outlook desktop usando comentários condicionais:

```html
<!--[if !mso]><!-- -->
<span>Content hidden in Outlook desktop</span>
<!--<![endif]-->
```

### Posso usar imagens SVG ou WebP nas minhas mensagens de e-mail? {#can-i-use-svg-or-webp-images-in-my-email-messages}

Imagens SVG não são recomendadas para e-mail devido ao suporte limitado entre clientes de e-mail. O Gmail e vários outros provedores de e-mail importantes não renderizam imagens SVG, o que pode resultar em imagens quebradas ou ausentes para os destinatários. WebP não é suportado de forma consistente entre os clientes.

Em vez disso, use formatos amplamente suportados como PNG ou JPEG para que as imagens sejam renderizadas de forma confiável.

### Posso incorporar vídeos em e-mails? {#can-i-embed-videos-in-emails}

Vídeos incorporados não são nativamente suportados por muitos clientes de e-mail populares como Gmail, Outlook e Yahoo. Como resultado, elementos de vídeo incorporados podem não ser exibidos conforme o esperado ou podem não aparecer. Além disso, incorporar vídeo diretamente em um e-mail pode aumentar significativamente o tamanho do e-mail, o que aumenta a chance de a mensagem ser marcada como SPAM.

Em vez disso, você pode criar um GIF ou imagem estática que se assemelhe a um vídeo em um player de vídeo e vincular essa imagem ao seu vídeo. Quando os usuários clicam na imagem, eles são direcionados ao vídeo hospedado no seu website ou em uma plataforma de vídeo. A Braze também suporta integração com [Playable]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/playable), que fornece conteúdo de vídeo otimizado que reproduz automaticamente em clientes de e-mail suportados.

### Variáveis Liquid atribuídas em uma parte do criador de mensagem podem ser usadas em outra? {#can-liquid-variables-assigned-in-one-part-of-the-message-composer-be-used-in-another}

Não. Cada parte do e-mail (assunto, corpo, cabeçalhos, botões e assim por diante) é gerada separadamente, então o Liquid atribuído em um campo não está disponível em outro. Atribua variáveis em cada campo que precisar delas.

### Meu modelo de e-mail está faltando. Onde está? {#my-email-template-is-missing-where-is-it}

Primeiro, confirme que você tem as [permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para visualizar modelos. Para visualizar modelos de e-mail salvos, acesse **Conteúdo** > **E-mail**. Você pode filtrar modelos por status e tipo (HTML ou arrastar e soltar).

### Preciso registrar domínios para e-mails de relay ou mascarados? {#do-i-need-to-register-domains-for-relay-or-masked-emails}

O [Private Email Relay da Apple]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/email_private_relay_apple_SSO) exige que você registre seus domínios de envio no Apple Developer Portal para evitar bounces. O Google Shielded Email não exige um processo manual de registro ou adição à lista de permissões de domínio.

### Posso adicionar hyperlinks nas linhas de assunto ou pré-cabeçalhos de e-mail? {#can-i-add-hyperlinks-in-email-subject-lines-or-preheaders}

Não. Adicionar hyperlinks nas linhas de assunto de e-mail não é suportado pelos provedores de caixa de entrada. Embora alguns provedores de caixa de entrada verifiquem automaticamente as linhas de assunto e convertam endereços físicos, datas ou horários em links clicáveis, isso acontece automaticamente no dispositivo do destinatário e está fora do controle da Braze (ou de qualquer ESP).

Da mesma forma, adicionar hyperlinks dentro do pré-cabeçalho não é suportado em toda a indústria de e-mail.

Se você precisa de funcionalidade semelhante a conteúdo clicável na linha de assunto ou na área do pré-cabeçalho, considere usar [Promoções do Gmail]({{site.baseurl}}/user_guide/channels/email/html_editor/gmail_promotions_tab) para adicionar anotações interativas aos seus e-mails para usuários do Gmail.

### O que significa o motivo de bounce `unable to get mx info` ou `failed to get IPs from PTR record`? {#what-does-the-bounce-reason-unable-to-get-mx-info-or-failed-to-get-ips-from-ptr-record-mean}

No [Log de atividades de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), um motivo de bounce semelhante ao seguinte indica um problema ao resolver a configuração de e-mail do domínio de recebimento (o domínio após o `@` no endereço), não à composição da mensagem da Braze:

As causas típicas incluem:

- Registros **MX** ausentes, incorretos ou inacessíveis para aquele domínio
- Hostnames de e-mail de entrada que não resolvem ou que falham nas verificações de **PTR (DNS reverso)** esperadas pela infraestrutura de recebimento
- Domínios inválidos ou digitados incorretamente no endereço de e-mail

**Próximas etapas:**

- Confirme a ortografia do endereço e do domínio.
- Se o endereço estiver correto, entre em contato com o proprietário da caixa de entrada ou a equipe de TI daquele domínio.
- Peça para auditarem os registros MX e DNS relacionados, incluindo registros PTR para seus servidores de e-mail, junto ao provedor DNS.

Outros destinatários geralmente não são afetados. Para saber como soft bounces aparecem nos relatórios, consulte [Soft Bounce]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce).

### Por que recebo um alerta de SPAM ao enviar um e-mail da Braze para mim mesmo? {#why-do-i-get-a-spam-alert-when-sending-an-email-from-braze-to-myself}

Se você enviar um e-mail de teste da Braze para o seu próprio endereço de e-mail e vir um aviso de SPAM ou alerta de phishing — como "o domínio de envio é semelhante ao domínio da sua empresa, mas não o reconhecemos" — esse é um recurso comum de segurança anti-phishing, não um erro na configuração da Braze.

Esse alerta normalmente aparece quando o domínio de envio do e-mail corresponde ao domínio do destinatário (por exemplo, ambos são `@suaempresa.com`). Os sistemas de segurança de e-mail sinalizam isso porque golpistas frequentemente falsificam domínios que parecem semelhantes ao domínio da empresa do destinatário.

Para verificar se seu e-mail está configurado corretamente:

1. Visualize a mensagem original (cabeçalhos brutos do e-mail) no seu cliente de e-mail.
2. Verifique se a autenticação SPF, DKIM e DMARC está aprovada.
3. Se todas as três passarem, o envio de e-mail da Braze está configurado corretamente.

Para evitar que esse alerta apareça:

Peça à sua equipe de TI para adicionar seu domínio de envio da Braze e os endereços IP à lista de permissões nos serviços de segurança de e-mail ou gateway de e-mail da sua empresa. Isso informa ao seu sistema de segurança para confiar nos e-mails da sua infraestrutura de envio da Braze.