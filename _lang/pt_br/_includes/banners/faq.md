# Perguntas frequentes {#frequently-asked-questions}

> Estas são respostas para perguntas frequentes sobre Banners na Braze. Para informações mais gerais, consulte [Sobre Banners]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}/).

## Quando as atualizações de Banner aparecem para os usuários? {#when-do-banner-updates-appear-for-users}

Os Banners são atualizados com os dados mais recentes sempre que você chama o método de atualização&#8212;não é necessário reenviar ou atualizar sua campanha de Banner.

## Quantos posicionamentos posso solicitar em uma sessão? {#how-many-placements-can-i-request-in-a-session}

Em uma única solicitação de atualização, você pode solicitar no máximo 10 posicionamentos. Para cada um solicitado, a Braze retornará o Banner de maior prioridade para o qual o usuário é elegível. Solicitações adicionais retornarão um erro.

Para saber mais, consulte [Solicitações de posicionamento]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## Quantas campanhas de Banner podem estar ativas simultaneamente? {#how-many-banner-campaigns-can-be-active-simultaneously}

Cada espaço de trabalho pode suportar até 200 campanhas de Banner ativas. Se esse limite for atingido, você precisará [arquivar ou desativar]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) uma campanha existente antes de criar uma nova.

## Para campanhas que compartilham um posicionamento, qual Banner é exibido primeiro? {#for-campaigns-sharing-a-placement-which-banner-is-displayed-first}

Se um usuário se qualificar para várias campanhas de Banner que compartilham o mesmo posicionamento, o Banner com a maior prioridade será exibido. Para saber mais, consulte [Prioridade do Banner]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## Posso usar Banners no meu feed de Content Cards existente? {#can-i-use-banners-in-my-existing-content-card-feed}

Os Banners são diferentes dos Content Cards, o que significa que você não pode usar Banners e Content Cards no mesmo feed. Para substituir feeds de Content Cards existentes por Banners, você precisará [criar posicionamentos no seu app ou site]({{site.baseurl}}/developer_guide/banners/placements/).

## Os Banners podem incluir vídeo? {#can-banners-include-video}

O criador padrão de Banners suporta imagens, texto e botões. Para incluir um vídeo em um Banner, você pode usar um bloco de **Custom Code** e renderizar um vídeo ou player incorporado no seu app ou site.

## Posso disparar um banner com base nas ações do usuário? {#can-i-trigger-a-banner-based-on-user-actions}

Embora os Banners não suportem [entrega baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/), você pode direcionar usuários com base em suas ações passadas usando segmentação e prioridade.

Por exemplo, para mostrar um Banner especial apenas para usuários que completaram um evento `purchase`:
1. **Direcionamento:** Na sua campanha, direcione um segmento de usuários que realizaram o evento personalizado `purchase` pelo menos uma vez.
2. **Prioridade:** Se você tiver um Banner geral para todos os usuários e este Banner específico para compradores direcionando o mesmo posicionamento, defina a prioridade do Banner específico como **Alta** e a do Banner geral como **Média** ou **Baixa**.

Quando o usuário inicia uma nova sessão ou atualiza os Banners após realizar a ação, a Braze avalia sua elegibilidade. Se ele corresponder ao segmento "Compra", o Banner de alta prioridade será exibido.


## Os usuários podem dispensar um Banner? {#can-users-dismiss-a-banner}

Sim. Você pode permitir que os usuários dispensem manualmente um Banner ativando o comportamento de dispensa no criador de Banners. Consulte [Configurar comportamento de dispensa]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#dismiss-behavior) para detalhes sobre como ativar a dispensa e personalizar o botão de dispensar.

Os usuários podem dispensar manualmente os Banners apenas se o comportamento de dispensa estiver ativado. Se a dispensa não estiver ativada, você pode controlar a visibilidade do Banner gerenciando a elegibilidade do segmento de usuários. Quando um usuário não atende mais aos critérios de direcionamento de uma campanha de Banner, ele não verá o Banner novamente na próxima sessão.

Quando um usuário dispensa um Banner, ele se torna inelegível para essa campanha por padrão. Para permitir que usuários que dispensaram vejam o Banner novamente, [configure a reelegibilidade]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#re-eligibility) na etapa de **Controles de entrega** da campanha. As etapas de Banner em Canvas usam as configurações de reentrada do Canvas para controlar a reelegibilidade.

Por exemplo, se você exibir um Banner promocional até que um usuário faça uma compra, registrar um evento como `purchase_completed` pode remover esse usuário do segmento direcionado, ocultando efetivamente o Banner nas sessões seguintes.

## Posso exportar a análise de dados de campanhas de Banners usando a API da Braze? {#can-i-export-banners-campaign-analytics-using-the-braze-api}

Sim. Você pode usar o [endpoint `/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) para obter dados sobre quantas campanhas de Banners foram visualizadas, clicadas ou convertidas.

## Quando os usuários são segmentados? {#when-are-users-segmented}

Os usuários são segmentados no início da sessão. Se os segmentos direcionados de uma campanha dependem de atributos personalizados, eventos personalizados ou outros atributos de direcionamento, eles devem estar presentes no usuário no início da sessão.

## Como posso criar Banners para garantir a menor latência? {#how-can-i-compose-banners-to-ensure-the-lowest-latency}

Quanto mais simples for o conteúdo do seu Banner, mais rápido ele será renderizado. O ideal é testar sua campanha de Banner considerando a latência esperada para o seu caso de uso. Por exemplo, certifique-se de testar atributos Liquid como `catalog_items`.

## Todas as Liquid tags são suportadas? {#are-all-liquid-tags-supported}

Não. No entanto, a maioria das Liquid tags é suportada para mensagens de Banner, exceto `catalog_items` que são re-renderizados usando a [tag `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid).

## Posso capturar eventos de clique? {#can-i-capture-click-events}

Sim. A forma como os eventos de clique são capturados depende de como seu Banner é renderizado:

- **Componentes do editor padrão:** Se seu Banner usar componentes do editor padrão (imagens, botões, texto), os cliques são rastreados automaticamente ao usar os métodos de inserção do SDK.
- **Blocos de Custom Code:** Se você quiser rastrear cliques em elementos dentro de um bloco do editor de Custom Code, deve chamar `brazeBridge.logClick()` de dentro do seu HTML personalizado para rastrear cliques. Isso se aplica mesmo ao usar os métodos do SDK para inserir e renderizar o Banner. Para a referência completa, consulte [Código personalizado e ponte JavaScript para Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/custom_code/#javascript-bridge).
- **UI personalizada (headless):** Se você estiver construindo uma UI totalmente personalizada usando as propriedades personalizadas do Banner em vez de renderizar o HTML do Banner, chame `logClick()` no objeto Banner a partir do código da sua aplicação.

Para saber mais, consulte [Registro de cliques]({{site.baseurl}}/developer_guide/banners/placements/#logging-clicks).