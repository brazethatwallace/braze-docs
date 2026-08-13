# Perguntas frequentes {#frequently-asked-questions}

> Estas são respostas para perguntas frequentes sobre Banners na Braze. Para informações mais gerais, consulte [Sobre Banners]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}).

## Quando as atualizações de Banners aparecem para os usuários? {#when-do-banner-updates-appear-for-users}

Os Banners são atualizados com os dados mais recentes sempre que você chama o método de atualização&#8212;não é necessário reenviar ou atualizar sua Campaign de Banner.

## Quantos posicionamentos posso solicitar em uma sessão? {#how-many-placements-can-i-request-in-a-session}

Em uma única solicitação de atualização, você pode solicitar no máximo 10 posicionamentos. Para cada um solicitado, a Braze retorna o Banner de maior prioridade para o qual o usuário é elegível. Solicitações adicionais retornam um erro.

Para saber mais, consulte [Solicitações de posicionamento]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## Quantas campanhas de Banner podem estar ativas simultaneamente? {#how-many-banner-campaigns-can-be-active-simultaneously}

Cada espaço de trabalho pode suportar até 200 campanhas de Banner ativas. Se esse limite for atingido, você precisará [arquivar ou desativar]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses#changing-the-status) uma campanha existente antes de criar uma nova.

## Para campanhas que compartilham um posicionamento, qual Banner é exibido primeiro? {#for-campaigns-sharing-a-placement-which-banner-is-displayed-first}

Se um usuário se qualificar para várias campanhas de Banner que compartilham o mesmo posicionamento, o Banner com a maior prioridade será exibido. Para saber mais, consulte [Prioridade de Banner]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## Posso usar Banners no meu feed existente de Content Cards? {#can-i-use-banners-in-my-existing-content-card-feed}

Banners são diferentes de Content Cards, o que significa que você não pode usar Banners e Content Cards no mesmo feed. Para substituir feeds existentes de Content Cards por Banners, você precisará [criar posicionamentos no seu app ou website]({{site.baseurl}}/developer_guide/banners/placements).

## Como os Banners são diferentes das mensagens no app? {#how-are-banners-different-from-in-app-messages}

Banners e [mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages) alcançam os usuários dentro do seu app ou website, mas usam modelos de entrega diferentes. Se você está comparando Banners a uma configuração existente de mensagem no app, espere diferenças em disparadores, tempo de atualização e testes — não uma substituição direta.

| Tópico | Banners | Mensagens no app |
| --- | --- | --- |
| Onde as mensagens aparecem | Inline nos [posicionamentos]({{site.baseurl}}/developer_guide/banners/placements) que você define no seu app ou site | Sobreposições em tela inteira, modal ou slide-up gerenciadas pelo SDK |
| Quando o conteúdo é atualizado | Quando seu app ou site solicita uma atualização de Banner (por exemplo, no início da sessão ou durante a sessão) | Mensagens com modelo avaliam o Liquid quando a mensagem no app é disparada (por exemplo, em um evento personalizado ou início de sessão), após a carga útil ser armazenada em cache no dispositivo |
| Disparadores baseados em ação | Sem [entrega baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery); use Segments, prioridade e tempo de atualização em vez disso | Suporta entrega baseada em ação e disparada por API |
| Testes | Visualize um usuário e confirme se a atualização do posicionamento no seu app ou site exibe o Banner esperado | Use **Test Send** ou fluxos de prévia no app para exibição baseada em disparadores |
| Relatórios | Visualizações e cliques de Banner seguem a análise de dados de Banner | Impressões e cliques no app seguem a análise de dados de mensagens no app |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Como os Banners são diferentes das mensagens no app?" }

## Os Banners podem incluir vídeo? {#can-banners-include-video}

O construtor padrão de Banners suporta imagens, texto e botões. Para incluir um vídeo em um Banner, você pode usar um bloco de **Custom Code** no construtor, ou criar o Banner inteiro com o editor de HTML e incorporar um player de vídeo diretamente no seu HTML.

## Posso disparar um banner com base nas ações do usuário? {#can-i-trigger-a-banner-based-on-user-actions}

Embora os Banners não suportem [entrega baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery), você pode direcionar usuários com base em suas ações anteriores usando segmentação e prioridade.

Por exemplo, para exibir um Banner especial apenas para usuários que concluíram um evento `purchase`:
1. **Direcionamento:** Na sua Campaign, direcione um Segment de usuários que realizaram o evento personalizado `purchase` pelo menos uma vez.
2. **Prioridade:** Se você tiver um Banner geral para todos os usuários e esse Banner específico para compradores direcionado ao mesmo posicionamento, defina a prioridade do Banner específico como **High** e a do Banner geral como **Medium** ou **Low**.

Quando o usuário inicia uma nova sessão ou atualiza os Banners após realizar a ação, a Braze avalia sua elegibilidade. Se ele corresponder ao Segment "Purchase", o Banner de alta prioridade será exibido.

## Os usuários podem dispensar um Banner? {#can-users-dismiss-a-banner}

Sim. Você pode permitir que os usuários dispensem manualmente um Banner. Consulte [Configurar comportamento de dispensa]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#dismiss-behavior) para saber como configurar a dispensa tanto no construtor quanto no editor de HTML.

Os usuários só podem dispensar Banners manualmente se o comportamento de dispensa estiver ativado. Se a dispensa não estiver ativada, você pode controlar a visibilidade do Banner gerenciando a elegibilidade do Segment de usuários. Quando um usuário não atende mais aos critérios de direcionamento de uma Campaign de Banner, ele não o verá novamente na próxima sessão.

Quando um usuário dispensa um Banner, ele fica inelegível para essa Campaign por padrão. Para permitir que usuários que dispensaram vejam o Banner novamente, [configure a reelegibilidade]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility) na etapa **Delivery Controls** da Campaign. As etapas de Banner no Canvas usam as configurações de reentrada do Canvas para controlar a reelegibilidade.

Por exemplo, se você exibe um Banner promocional até que um usuário faça uma compra, registrar um evento como `purchase_completed` pode remover esse usuário do Segment direcionado, ocultando efetivamente o Banner nas sessões seguintes.

## Posso exportar análises de dados de Campaigns de Banners usando a API da Braze? {#can-i-export-banners-campaign-analytics-using-the-braze-api}

Sim. Você pode usar o [endpoint `/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) para obter dados sobre quantas Campaigns de Banners foram visualizadas, clicadas ou convertidas.

## Quando os usuários são segmentados? {#when-are-users-segmented}

Os usuários são segmentados no início da sessão. Se os Segments direcionados de uma Campaign dependem de atributos personalizados, eventos personalizados ou outros atributos de direcionamento, eles devem estar presentes no usuário no início da sessão.

## Como posso compor Banners para garantir a menor latência? {#how-can-i-compose-banners-to-ensure-the-lowest-latency}

Quanto mais simples a mensagem no seu Banner, mais rápido ele é renderizado. O ideal é testar sua Campaign de Banner em relação à latência esperada para o seu caso de uso. Por exemplo, teste atributos Liquid como `catalog_items`.

Se você usar [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) (em acesso antecipado), saiba que cada chamada conta contra um orçamento compartilhado de renderização de aproximadamente dois segundos em todos os posicionamentos em uma única atualização. Se o orçamento for excedido ou uma chamada expirar, o resultado do Connected Content é tratado como nulo, e os Banners não fazem nova tentativa. Para minimizar a latência:

- Mantenha seus endpoints rápidos e [armazene respostas em cache]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) sempre que possível.
- Limite o número de URLs únicos de Connected Content entre posicionamentos que são renderizados juntos.
- Evite encadear chamadas em que uma resposta de Connected Content determina a URL da próxima.
- Use instruções de proteção Liquid ou o [filtro `default`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) para lidar com resultados nulos e evitar Banners em branco.

## Todas as Liquid tags são suportadas? {#are-all-liquid-tags-supported}

Não. No entanto, a maioria das Liquid tags é suportada para mensagens de Banner, exceto `catalog_items` que são re-renderizados usando a [tag `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs#using-liquid).

## Posso capturar eventos de clique? {#can-i-capture-click-events}

Sim. A forma como os eventos de clique são capturados depende de como seu Banner é renderizado:

- **Builder — componentes padrão:** Se o seu Banner usa componentes padrão do editor (imagens, botões, texto), os cliques são rastreados automaticamente ao usar os métodos de inserção do SDK.
- **Builder — blocos de Custom Code:** Se você deseja rastrear cliques em elementos dentro de um bloco do editor de Custom Code, é necessário chamar `brazeBridge.logClick()` de dentro do seu HTML personalizado. Isso se aplica mesmo ao usar os métodos do SDK para inserir e renderizar o Banner.
- **Editor de HTML:** O rastreamento de cliques não é automático. Você deve chamar `brazeBridge.logClick()` para cada elemento clicável que deseja rastrear. Para a referência completa, consulte [Custom code e ponte JavaScript para Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).
- **UI personalizada (headless):** Se você está construindo uma UI totalmente personalizada usando as propriedades personalizadas do Banner em vez de renderizar o HTML do Banner, chame `logClick()` no objeto Banner a partir do código da sua aplicação.

Para saber mais, consulte [Registrando cliques]({{site.baseurl}}/developer_guide/banners/placements#logging-clicks).