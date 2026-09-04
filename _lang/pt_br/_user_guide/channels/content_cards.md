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

A disponibilidade dos Content Cards depende do seu pacote da Braze. Entre em contato com seu gerente de conta ou gerente de sucesso do cliente para começar.

Antes de usar os Content Cards, é necessário integrar o [SDK da Braze]({{site.baseurl}}/developer_guide/content_cards) ao seu app ou website. Nenhuma configuração adicional é necessária. Para criar sua própria interface, consulte o [guia de personalização de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards).

## Benefícios de usar Content Cards {#benefits-of-using-content-cards}

Veja alguns benefícios de usar Content Cards em vez de pedir aos seus desenvolvedores que criem conteúdo diretamente no app:

- **Segmentação e personalização mais fáceis:** Os dados dos seus usuários ficam na Braze, o que facilita a definição do seu público e a personalização das suas mensagens com Content Cards.
- **Relatórios centralizados:** As análises de dados de Content Cards são rastreadas na Braze, então você tem insights sobre todas as suas Campaigns em um único lugar.
- **Jornadas do cliente coesas:** Você pode combinar Content Cards com outros canais na Braze para criar experiências consistentes para os clientes. Um caso de uso popular é enviar uma notificação por push e depois salvar essa notificação como um Content Card no seu app para qualquer pessoa que não interagiu com o push. Se o conteúdo é criado diretamente no app pelos seus desenvolvedores, ele fica isolado do restante do seu envio de mensagens.
- **Aceitação não obrigatória:** Semelhante às mensagens no app, Content Cards não exigem aceitação ou permissões dos seus usuários. Porém, enquanto as mensagens no app não precisam de permissão e são temporárias, Content Cards não precisam de permissão e são permanentes. Isso significa que estratégias de envio de mensagens que combinam mensagens no app e Content Cards encontram um ótimo equilíbrio.
- **Mais controle sobre a experiência de mensagens:** Embora você ainda precise dos seus desenvolvedores para ajudar na configuração inicial dos Content Cards, depois disso, você pode controlar a mensagem, os destinatários, o horário e muito mais diretamente pelo dashboard da Braze.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## Content Cards em números {#content-cards-by-the-numbers}

Ao criar Content Cards na Braze, você pode atualizar mensagens e medir o impacto sem precisar reformular seu app ou website. Destaques das pesquisas da Braze incluem:

- Content Cards são **38X** mais eficazes do que e-mail para impulsionar vendas em uma janela de 72 horas.[^1]
- Usar Content Cards em Campaigns de inscrição em programas de fidelidade aumenta as conversões em **5X**.[^1]
- O alcance por meio de notificações por push, In-App Messages e Content Cards gera **6,9X** mais sessões do que push sozinho.[^2]
- O alcance por meio de e-mail, In-App Messages e Content Cards gera **3,6X** mais tempo médio de vida do usuário do que e-mail sozinho.[^2]

## Casos de uso {#use-cases}

Consulte esta seção para conhecer alguns casos de uso comuns para Content Cards.

{% alert tip %}
Para mais inspiração, consulte o [Guia de inspiração de Content Cards](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), que inclui mais de 20 campanhas personalizáveis, incluindo programas de indicação, lançamentos de novos produtos e renovações de inscrição.
{% endalert %}

{% tabs %}
{% tab Integração e próximos passos %}

Conforme novos usuários exploram seu app e website, guie-os pelos valores e benefícios do que você oferece com Content Cards posicionados estrategicamente. Incentive os usuários a aderir a outros canais de comunicação com um cartão de conteúdo na sua página inicial e salve tarefas de integração pendentes em uma guia dedicada de integração alimentada por Content Cards. Não se esqueça de remover um cartão depois que o usuário concluir a tarefa desejada!

![Exemplo de caso de uso de integração com Content Cards.]({% image_buster /assets/img_archive/cc_usecase_onboarding.png %})

{% endtab %}
{% tab Participação em eventos %}

Exiba Content Cards no topo da página inicial do usuário para incentivar a participação em eventos, usando direcionamento por localização para alcançar usuários potenciais onde eles estão. Convidar usuários para eventos presenciais relevantes faz com que eles se sintam especiais, principalmente com mensagens personalizadas que aproveitam sua atividade anterior com sua marca.

![Exemplo de caso de uso de participação em eventos com Content Cards.]({% image_buster /assets/img_archive/cc_usecase_event.png %})

{% endtab %}
{% tab Recomendações %}

Use os dados que você tem sobre comportamentos e preferências dos usuários para exibir conteúdo relevante em tempo real a partir de Content Cards na página inicial ou na caixa de entrada, atraindo-os de volta para o que você oferece.

![Exemplo de caso de uso de recomendações com Content Cards.]({% image_buster /assets/img_archive/cc_usecase_recommendation.png %})

{% endtab %}
{% tab Vendas e promoções %}

Aproveite os Content Cards para destacar mensagens promocionais e ofertas não resgatadas diretamente na sua página inicial ou em uma caixa de entrada promocional dedicada. Inclua conteúdo relevante com base nas compras anteriores de cada cliente para entregar promoções personalizadas que chamem a atenção.

![Exemplo de caso de uso de vendas e promoções com Content Cards.]({% image_buster /assets/img_archive/cc_usecase_promo.png %})

{% endtab %}
{% endtabs %}

### Outros casos de uso {#other-use-cases}

Além desses casos de uso principais, os clientes utilizam Content Cards de muitas formas diferentes. O poder dos Content Cards está na sua flexibilidade. Se o caso de uso que você deseja não está listado aqui, você pode configurar [pares chave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) e enviar as cargas úteis para o seu app ou website.

Para uma visão geral sobre como implementar posicionamentos de Content Cards no seu app ou website, consulte [Criando Content Cards personalizados]({{site.baseurl}}/developer_guide/content_cards/creating_cards).

## Próximos passos {#next-steps}

{% article_tiles %}
- name: Criar um cartão de conteúdo
  link: /docs/user_guide/channels/content_cards/create_a_content_card
- name: Detalhes criativos
  link: /docs/user_guide/channels/content_cards/creative_details
{% endarticle_tiles %}

[^1]: [8 dicas para aproveitar ao máximo suas campanhas de retenção de clientes](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Relatório: A diferença do marketing em diferentes canais](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)