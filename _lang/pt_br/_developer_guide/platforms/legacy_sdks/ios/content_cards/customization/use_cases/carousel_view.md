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

Esta seção aborda como implementar um feed de carrossel com vários cartões, em que o usuário pode deslizar horizontalmente para ver cartões adicionais em destaque. Para integrar uma visualização de carrossel, você precisará usar uma implementação de Content Card totalmente personalizada — a fase de "execução" da [abordagem crawl, walk, run]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

Com essa abordagem, você não usará as visualizações da Braze e a lógica padrão, mas exibirá os Content Cards de maneira totalmente personalizada, usando suas próprias visualizações preenchidas com dados dos modelos da Braze.

Em termos de nível de esforço de desenvolvimento, as principais diferenças entre a implementação básica e a implementação do carrossel incluem:

- Criar suas próprias visualizações
- Registrar a análise de dados dos Content Cards
- Introduzir lógica adicional no lado do cliente para determinar quantos e quais cartões serão exibidos no carrossel

## Implementação {#implementation}

### Etapa 1: Criar um view controller personalizado {#step-1-create-a-custom-view-controller}

Para criar o carrossel de Content Cards, crie seu próprio view controller personalizado (como `UICollectionViewController`) e [inscreva-se para atualizações de dados]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration#getting-the-data). Note que não será possível estender ou criar uma subclasse do nosso `ABKContentCardTableViewController` padrão, pois ele só é capaz de lidar com nossos tipos padrão de Content Cards.

### Etapa 2: Implementar análise de dados {#step-2-implement-analytics}

Ao criar um view controller totalmente personalizado, impressões, cliques e dispensas de Content Cards não são registrados automaticamente. Você deve implementar os respectivos métodos de análise de dados para garantir que impressões, eventos de dispensa e cliques sejam devidamente registrados nas análises do dashboard da Braze.

Para informações sobre os métodos de análise de dados, consulte [Métodos de cartão]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration#card-methods).

{% alert note %}
A mesma página também detalha as diferentes propriedades herdadas da nossa classe de modelo genérico de Content Cards, que podem ser úteis durante a implementação da sua view.
{% endalert %}

### Etapa 3: Criar um observador de Content Cards {#step-3-create-a-content-card-observer}

Crie um [observador de Content Cards]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds#step-2-set-up-a-content-card-listener) responsável por lidar com a chegada de Content Cards e implemente lógica condicional para exibir um número específico de cartões no carrossel a qualquer momento. Por padrão, os Content Cards são classificados pela data de criação (mais recentes primeiro), e o usuário vê todos os cartões para os quais é elegível.

Dito isso, você pode ordenar e aplicar lógica de exibição adicional de diversas maneiras. Por exemplo, você pode selecionar os cinco primeiros objetos de Content Cards do array ou usar pares chave-valor (a propriedade `extras` no modelo de dados) para construir lógica condicional.

Se estiver implementando um carrossel como um feed secundário de Content Cards, consulte [Usando múltiplos feeds de Content Cards]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds) para garantir que os cartões sejam classificados no feed correto com base em pares chave-valor.

{% alert important %}
É importante garantir que suas equipes de marketing e de desenvolvedores coordenem quais pares chave-valor serão usados (por exemplo, `feed_type = brand_homepage`), pois quaisquer pares chave-valor que os profissionais de marketing inserirem no dashboard da Braze devem corresponder exatamente aos pares chave-valor que os desenvolvedores implementarem na lógica do app.
{% endalert %}

Para a documentação de desenvolvedor específica para iOS sobre a classe, os métodos e os atributos de Content Cards, consulte a [referência da classe `ABKContentCard` para iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html).

## Considerações {#considerations}

- Ao usar visualizações totalmente personalizadas, você não poderá estender ou criar subclasses dos métodos usados em `ABKContentCardsController`. Em vez disso, será necessário integrar os métodos e propriedades do modelo de dados por conta própria.
- A lógica e a implementação da visualização de carrossel não é um tipo padrão de Content Cards na Braze, e portanto a lógica para alcançar o caso de uso deve ser fornecida e mantida pela sua equipe de desenvolvimento.
- Será necessário implementar lógica no lado do cliente para exibir um número específico de cartões no carrossel a qualquer momento.