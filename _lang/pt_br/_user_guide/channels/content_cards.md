---
nav_title: Content Cards
article_title: Content Cards
page_order: 2
page_type: landing
description: "Envie um fluxo dinâmico de conteúdo rico para seus usuários com os Content Cards, incorporados diretamente no seu app ou site."
channel:
  - content cards
search_rank: 5
---

# Content Cards {#content-cards}

> Com os Content Cards, você pode enviar um fluxo altamente direcionado e dinâmico de conteúdo rico para seus clientes dentro dos apps que eles adoram, sem interromper a experiência. Os Content Cards são incorporados diretamente no seu app ou site, permitindo criar caixas de entrada de mensagens e interfaces personalizadas que ampliam o alcance de outros canais, como e-mail ou notificações por push.

## Pré-requisitos {#prerequisites}

A disponibilidade dos Content Cards depende do seu pacote da Braze. Entre em contato com seu gerente de conta ou CSM para começar.

Antes de usar os Content Cards, você precisa integrar o [SDK da Braze]({{site.baseurl}}/developer_guide/content_cards) ao seu app ou site. Nenhuma configuração adicional é necessária. Para criar sua própria interface, consulte o [guia de personalização de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards).

## Benefícios de usar Content Cards {#benefits-of-using-content-cards}

Veja alguns benefícios de usar Content Cards em vez de pedir para seus desenvolvedores criarem conteúdo diretamente no app:

- **Segmentação e personalização mais fáceis:** Seus dados de usuários ficam na Braze, facilitando a definição do público e a personalização das mensagens com Content Cards.
- **Relatórios centralizados:** A análise de dados dos Content Cards é rastreada na Braze, então você tem insight de todas as suas Campaigns em um único local.
- **Jornadas do cliente coesas:** Você pode combinar Content Cards com outros canais na Braze para criar experiências consistentes para o cliente. Um caso de uso popular é enviar uma notificação por push e depois salvar essa notificação como um Content Card no seu app para quem não interagiu com o push. Se o conteúdo for criado diretamente no app pelos seus desenvolvedores, ele fica isolado do restante do seu envio de mensagens.
- **Sem necessidade de opt-in:** Assim como as mensagens no app, os Content Cards não exigem opt-in ou permissões dos seus usuários. Porém, enquanto as mensagens no app não precisam de permissão e são temporárias, os Content Cards não precisam de permissão e são permanentes. Isso significa que estratégias de envio de mensagens que combinam mensagens no app e Content Cards alcançam um ótimo equilíbrio.
- **Mais controle sobre a experiência de mensagens:** Embora você ainda precise dos seus desenvolvedores para a configuração inicial dos Content Cards, depois disso, você pode controlar a mensagem, os destinatários, o timing e muito mais diretamente pelo dashboard da Braze.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## Content Cards em números {#content-cards-by-the-numbers}

Quando você cria Content Cards na Braze, pode atualizar mensagens e medir o impacto sem reformular seu app ou site. Destaques das pesquisas da Braze incluem:

- Content Cards são **38X** mais eficazes que o e-mail para impulsionar vendas em um período de 72 horas.[^1]
- Usar Content Cards em Campaigns de inscrição em programas de fidelidade aumenta as conversões em **5X**.[^1]
- O alcance por meio de notificações por push, mensagens no app e Content Cards gera **6,9X** mais sessões do que o push sozinho.[^2]
- O alcance por meio de e-mail, mensagens no app e Content Cards gera **3,6X** mais tempo de vida médio do usuário do que o e-mail sozinho.[^2]

[^1]: [8 dicas para aproveitar ao máximo suas campanhas de retenção de clientes](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Relatório: A diferença do marketing multicanal](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)

## Casos de uso {#use-cases}

Consulte esta seção para conhecer alguns casos de uso comuns dos Content Cards.

{% alert tip %}
Para mais inspiração, consulte o [Guia de Inspiração para Content Cards](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), que inclui mais de 20 campanhas personalizáveis, incluindo programas de indicação, lançamentos de novos produtos e renovações de inscrição.
{% endalert %}

{% tabs %}
{% tab Integração e próximos passos %}

Conforme novos usuários exploram seu app e site, guie-os pelos valores e benefícios do que você oferece com Content Cards estrategicamente posicionados. Incentive os usuários a fazer opt-in em outros canais de comunicação com um Content Card na sua página inicial e salve tarefas de integração pendentes em uma guia dedicada de integração alimentada por Content Cards. Não se esqueça de remover um cartão depois que o usuário concluir a tarefa desejada!

![Exemplo de caso de uso de integração com Content Card.]({% image_buster /assets/img_archive/cc_usecase_onboarding.png %})

{% endtab %}
{% tab Participação em eventos %}

Exiba Content Cards no topo da página inicial do usuário para incentivar a participação em eventos, usando direcionamento por local para alcançar usuários potenciais onde eles estão. Convidar usuários para eventos presenciais relevantes faz com que se sintam especiais, especialmente com mensagens personalizadas que aproveitam a atividade anterior deles com sua marca.

![Exemplo de caso de uso de participação em eventos com Content Card.]({% image_buster /assets/img_archive/cc_usecase_event.png %})

{% endtab %}
{% tab Recomendações %}

Use os dados que você tem sobre comportamentos e preferências dos usuários para exibir conteúdo relevante em tempo real a partir de Content Cards na página inicial ou na caixa de entrada, atraindo-os de volta para o seu produto.

![Exemplo de caso de uso de recomendações com Content Card.]({% image_buster /assets/img_archive/cc_usecase_recommendation.png %})

{% endtab %}
{% tab Vendas e promoções %}

Aproveite os Content Cards para destacar mensagens promocionais e ofertas não resgatadas diretamente na sua página inicial ou em uma caixa de entrada promocional dedicada. Exiba conteúdo relevante com base nas compras anteriores de cada cliente para entregar promoções personalizadas que chamam a atenção.

![Exemplo de caso de uso de vendas e promoções com Content Card.]({% image_buster /assets/img_archive/cc_usecase_promo.png %})

{% endtab %}
{% endtabs %}

### Outros casos de uso {#other-use-cases}

Além desses casos de uso principais, os clientes usam Content Cards de muitas formas diferentes. O poder dos Content Cards está na sua flexibilidade. Se o caso de uso que você deseja não está listado aqui, você pode configurar [pares chave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) e enviar as cargas úteis para seu app ou site.

Para uma visão geral de como implementar posicionamentos de Content Cards no seu app ou site, consulte [Criando Content Cards personalizados]({{site.baseurl}}/developer_guide/content_cards/creating_cards).

## Próximos passos {#next-steps}

- [Criar um cartão de conteúdo]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card)
- [Detalhes criativos]({{site.baseurl}}/user_guide/channels/content_cards/creative_details)