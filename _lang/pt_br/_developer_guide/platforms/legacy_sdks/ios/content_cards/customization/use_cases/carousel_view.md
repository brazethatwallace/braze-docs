---
nav_title: Visualização do carrossel
article_title: Visualização de carrossel de Content Card para iOS
platform: iOS
page_order: 5
description: "Este artigo aborda como implementar um caso de uso de visualização de carrossel de Content Card para aplicativos iOS."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Caso de uso: visualização do carrossel {#use-case-carousel-view}

![App de notícias de exemplo mostrando carrossel de Content Cards em um artigo.]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Esta seção aborda como implementar um feed de carrossel com vários cartões, em que o usuário pode deslizar horizontalmente para ver cartões adicionais em destaque. Para integrar uma visualização de carrossel, você precisará usar uma implementação de Content Card totalmente personalizada — a fase de "execução" da [abordagem crawl, walk, run]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize#customization-approaches).

Com essa abordagem, você não usará as visualizações da Braze e a lógica padrão, mas exibirá os Content Cards de maneira totalmente personalizada, usando suas próprias visualizações preenchidas com dados dos modelos da Braze.

Em termos de nível de esforço de desenvolvimento, as principais diferenças entre a implementação básica e a implementação do carrossel incluem:

- Criar suas próprias visualizações
- Registrar a análise de dados dos Content Cards
- Introduzir lógica adicional no lado do cliente para determinar quantos e quais cartões serão exibidos no carrossel

## Implementação {#implementation}

### Etapa 1: Criar um controlador de visualização personalizado {#step-1-create-a-custom-view-controller}

Para criar o carrossel de Content Cards, crie seu próprio controlador de visualização personalizado (como `UICollectionViewController`) e [assine as atualizações de dados]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration#getting-the-data). Note que você não poderá estender ou criar uma subclasse do nosso `ABKContentCardTableViewController` padrão, pois ele só é capaz de lidar com nossos tipos padrão de Content Card.

### Etapa 2: Implementar análise de dados {#step-2-implement-analytics}

Ao criar um controlador de visualização totalmente personalizado, as impressões, os cliques e os descartes de Content Card não são registrados automaticamente. É necessário implementar os respectivos métodos de análise de dados para garantir que as impressões, os eventos de descarte e os cliques sejam registrados corretamente na análise de dados do dashboard da Braze.

Para obter informações sobre os métodos de análise de dados, consulte [Métodos de cartão]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration#card-methods).

{% alert note %}
A mesma página também detalha as diferentes propriedades herdadas da nossa classe genérica de modelo de Content Card, que podem ser úteis durante a implementação da visualização.
{% endalert %}

### Etapa 3: Criar um observador de Content Card {#step-3-create-a-content-card-observer}

Crie um [observador de Content Card]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds#step-2-set-up-a-content-card-listener) que seja responsável por lidar com a chegada de Content Cards e implemente a lógica condicional para exibir um número específico de cartões no carrossel a qualquer momento. Por padrão, os Content Cards são classificados por data de criação (o mais recente primeiro), e o usuário vê todos os cartões para os quais é elegível.

Dito isso, você pode ordenar e aplicar lógica de exibição adicional de várias maneiras. Por exemplo, você pode selecionar os cinco primeiros objetos de Content Card do array ou introduzir pares de chave-valor (a propriedade `extras` no modelo de dados) para criar uma lógica condicional.

Se estiver implementando um carrossel como um feed secundário de Content Cards, consulte [Uso de vários feeds de Content Card]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds) para garantir que você classifique os cartões no feed correto com base em pares de chave-valor.

{% alert important %}
É importante garantir que as equipes de marketing e de desenvolvimento coordenem os pares de chave-valor que serão usados (por exemplo, `feed_type = brand_homepage`), pois todos os pares de chave-valor que os profissionais de marketing inserirem no dashboard da Braze devem corresponder exatamente aos pares de chave-valor que os desenvolvedores criam na lógica do app.
{% endalert %}

Para obter a documentação do desenvolvedor específica do iOS sobre a classe, os métodos e os atributos dos Content Cards, consulte a referência de classe do iOS [`ABKContentCard`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html).

## Considerações {#considerations}

- Ao usar visualizações totalmente personalizadas, você não poderá estender ou criar subclasses dos métodos usados em `ABKContentCardsController`. Em vez disso, você mesmo precisará integrar os métodos e as propriedades do modelo de dados.
- A lógica e a implementação da visualização de carrossel não são um tipo padrão de Content Card na Braze e, portanto, a lógica para alcançar o caso de uso deve ser fornecida e mantida pela sua equipe de desenvolvimento.
- Você precisará implementar a lógica do lado do cliente para exibir um número específico de cartões no carrossel a qualquer momento.