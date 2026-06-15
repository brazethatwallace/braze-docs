# Banners

> Com Banners, você pode criar mensagens personalizadas para seus usuários, enquanto amplia o alcance de seus outros canais, como e-mail ou notificações por push. Você pode incorporar Banners diretamente no seu app ou site, o que permite interagir com os usuários por meio de uma experiência que parece natural.

## Pré-requisitos {#prerequisites}

A disponibilidade de Banners depende do seu pacote da Braze. Entre em contato com seu gerente de conta ou gerente de sucesso do cliente para começar.

Antes de começar, certifique-se de ter [posicionamentos de Banner]({{site.baseurl}}/developer_guide/banners/placements/) criados no seu app ou site.

![Um exemplo de Banner exibido em um dispositivo.]({% image_buster /assets/img/banners/sample_banner.png %})

## Por que usar Banners? {#why-use-banners}

Os Banners permitem que as equipes de marketing e produto personalizem o conteúdo do app ou site dinamicamente, refletindo a elegibilidade e o comportamento do usuário em tempo real. Eles exibem mensagens de forma persistente e inline, proporcionando experiências contextualmente relevantes e não intrusivas que podem ser atualizadas no início de uma sessão ou durante a sessão, quando seu app ou site solicita explicitamente.

Depois que os Banners são integrados a um app ou site, os profissionais de marketing podem projetar e lançar Banners usando um simples editor de arrastar e soltar, eliminando a necessidade de assistência contínua de desenvolvedores, reduzindo a complexidade e melhorando a eficiência.

| Caso de uso | Explicação |
| --- | --- |
| Anúncios | Mantenha anúncios como eventos futuros ou mudanças de políticas em destaque na experiência do seu app. |
| Personalização de ofertas | Mostre promoções e incentivos personalizados com base no histórico de navegação, conteúdo do carrinho, nível de inscrição e status de fidelidade de cada usuário. |
| Engajamento de novos usuários | Guie novos usuários através de fluxos de integração e configuração de conta. |
| Vendas e promoções | Destaque conteúdo em destaque, produtos em tendência e campanhas de marca em andamento de forma persistente e direta na sua página inicial, sem interromper a experiência do usuário. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Por que usar Banners?" }

## Recursos {#features}

Os recursos dos Banners incluem:

- **Construção de conteúdo fácil:** Crie e visualize seu Banner usando um editor visual de arrastar e soltar com suporte para imagens, texto, botões, formulários de captura de e-mail, código personalizado e muito mais.
- **Posicionamentos flexíveis:** Defina múltiplos locais dentro do seu aplicativo ou site onde os Banners podem aparecer, permitindo direcionamento preciso a contextos ou experiências de usuário específicas.
- **Personalização dinâmica:** Os Banners só podem ser atualizados no início de uma nova sessão ou durante a sessão se você solicitar explicitamente a atualização. Os Banners não são atualizados automaticamente em uma nova sessão. Se você não solicitar a atualização, o Banner não será atualizado.
- **Priorização nativa:** Defina a prioridade de exibição para quando vários Banners visam o mesmo posicionamento, garantindo que a mensagem certa chegue aos usuários no momento certo.
- **Bloco de editor de código personalizado:** Use o bloco de editor de código personalizado para adicionar HTML personalizado para personalização avançada ou integração perfeita com seus estilos web existentes.

## Sobre os Banners {#about-banners}

### IDs de posicionamento {#placement-id}

Os posicionamentos de Banner são locais específicos no seu app ou site [que você cria com o SDK da Braze]({{site.baseurl}}/developer_guide/banners/placements/) que designam onde os Banners podem aparecer.

Locais comuns incluem o topo da sua página inicial, páginas de detalhes de produtos e fluxos de checkout. Depois que os posicionamentos são criados, os Banners podem ser [atribuídos na sua campanha de Banner]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/).

Não há um limite fixo para o número de posicionamentos que você pode criar por espaço de trabalho, e você pode criar quantos IDs de posicionamento sua experiência exigir. Cada posicionamento deve ser único dentro de um espaço de trabalho. Um único ID de posicionamento pode ser referenciado por até 25 mensagens ativas ao mesmo tempo.

{% alert important %}
Evite modificar IDs de posicionamento após lançar uma campanha de Banner.
{% endalert %}

### Prioridade do Banner {#priority}

Quando várias mensagens de Banner referenciam o mesmo ID de posicionamento, os Banners são exibidos em ordem de prioridade: alta, média ou baixa. Por padrão, os Banners são definidos como média, mas você pode [definir manualmente a prioridade]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#set-banner-priority-optional) ao criar ou editar sua campanha de Banner.

Se vários Banners estiverem definidos com a mesma prioridade, o Banner mais recente para o qual o usuário é elegível será exibido primeiro.

### Solicitações de posicionamento {#requests}

{% multi_lang_include banners/placement_requests.md %}

### Entrega de mensagens {#message-delivery}

As mensagens de Banner são entregues ao seu app ou site como conteúdo HTML, tipicamente renderizado dentro de um iframe. Isso garante que seus Banners sejam renderizados de forma consistente em diferentes dispositivos e ajuda a manter seus estilos e scripts separados do restante do seu código.

Os iframes permitem atualizações de conteúdo dinâmico e personalizado que não requerem alterações na sua base de código. Cada iframe recupera e exibe o HTML para cada sessão de usuário usando direcionamento de Campaign e lógica de personalização.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

### Dimensões e tamanhos {#dimensions-and-sizing}

Aqui está o que você precisa saber sobre dimensões e tamanhos de Banners:

- Embora o criador permita que você visualize Banners em diferentes dimensões, essa informação não é salva ou enviada para o SDK.
- O HTML ocupa toda a largura do contêiner em que é renderizado.
- Recomendamos criar um elemento de dimensão fixa e testar essas dimensões no criador.

## Limitações {#limitations}

Cada espaço de trabalho pode suportar até 200 campanhas de Banner ativas. Se esse limite for atingido, você precisará [arquivar ou desativar]({{site.baseurl}}/user_guide/messaging/governance/statuses/#changing-the-status) uma campanha existente antes de criar uma nova.

Além disso, as mensagens de Banner não suportam os seguintes recursos:

- Campaigns disparadas por API e baseadas em ações
- Conteúdo conectado
- Códigos promocionais
- `catalog_items` usando a [tag `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid)
- Dispensas controladas pelo usuário (somente acesso antecipado)

{% alert important %}
Permitir que os usuários dispensem manualmente um Banner está em acesso antecipado. Consulte [Configurar comportamento de dispensa]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#dismiss-behavior) para mais detalhes. Se você tem interesse em participar do acesso antecipado, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

## Próximos passos {#next-steps}

- [Criar posicionamentos de Banner no seu app ou site]({{site.baseurl}}/developer_guide/banners/placements/)
- [Criar uma campanha de Banner na Braze]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/)
- [Tutorial: Exibindo um Banner pelo ID de posicionamento]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners/)

{% alert tip %}
Quer ajudar a priorizar o que vem a seguir? Entre em contato com [banners-feedback@braze.com](mailto:banners-feedback@braze.com).
{% endalert %}