---
nav_title: Catálogos
article_title: Catálogos
page_order: 3
layout: dev_guide

guide_top_header: "Catálogos"
guide_top_text: "Os catálogos acessam dados de arquivos CSV importados e endpoints de API para enriquecer suas mensagens, de forma semelhante a como você acessaria atributos personalizados ou propriedades de eventos personalizados por meio do Liquid."

description: "Esta landing page contém catálogos. Use catálogos e conjuntos filtrados para aproveitar dados de não usuários em suas campanhas da Braze para enviar mensagens personalizadas."

guide_featured_title: "Artigos da seção"
guide_featured_list:
- name: Criar um catálogo
  link: /docs/user_guide/data/activation/catalogs/create
  image: /assets/img/braze_icons/users-01.svg
- name: Usando catálogos
  link: /docs/user_guide/data/activation/catalogs/use
  image: /assets/img/braze_icons/users-01.svg
- name: Notificações de reposição de estoque
  link: /docs/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Notificações de queda de preço
  link: /docs/price_drop_notifications
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Seleções
  link: /docs/user_guide/data/activation/catalogs/selections
  image: /assets/img/braze_icons/list.svg

guide_menu_title: "Outros artigos"
guide_menu_list:
- name: Endpoints da API de catálogos
  link: /docs/api/endpoints/catalogs
  image: /assets/img/braze_icons/server-01.svg
- name: Blocos de produtos de arrastar e soltar
  link: /docs/dnd_product_blocks
  image: /assets/img/braze_icons/columns-01.svg
---
<br><br>

## Casos de uso de catálogos {#catalog-use-cases}

Você pode importar qualquer tipo de dados para um catálogo. Normalmente, os dados são metadados sobre ofertas, como produtos, descontos, promoções, eventos e similares. Veja os casos de uso a seguir para alguns exemplos de como usar esses dados para direcionar os usuários com envio de mensagens altamente relevantes.

### Varejo e e-commerce {#retail-and-ecommerce}

- **Promoções sazonais:** importe coleções de produtos sazonais e personalize mensagens para refletir as tendências atuais.
- **Mensagens localizadas:** importe os endereços, horários e serviços dos seus locais físicos e personalize as notificações com base na localização dos usuários.
- **Notificações de reposição de estoque:** importe informações de produtos que incluam a quantidade em estoque e use as [notificações de reposição de estoque]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) e eventos personalizados da Braze para disparar uma Campaign ou um Canvas que envie aos usuários uma notificação de que um produto voltou ao estoque.
- **Notificações de queda de preço:** importe informações de produtos que incluam os preços e use as [notificações de queda de preço]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications) e eventos personalizados da Braze para disparar um Canvas que envie aos usuários uma notificação de que o preço de um produto caiu.

### Entretenimento {#entertainment}

- **Planos de inscrição:** importe planos de inscrição e promova complementos para seus usuários com base nos padrões de uso e nos tipos de conteúdo que eles mais consomem.
- **Próximos eventos:** importe listas de eventos futuros com seus locais e faixas etárias do público e envie notificações personalizadas para usuários que estejam na região e na faixa etária alvo.
- **Preferências de mídia:** importe informações sobre filmes e séries e recomende conteúdo aos seus usuários com base nos títulos favoritos e nos gêneros mais assistidos.

### Viagens e hospitalidade {#travel-and-hospitality}

- **Destinos:** importe destinos de viagem com suas atrações, restaurantes e atividades mais populares e personalize as recomendações para seus usuários com base em viagens anteriores.
- **Acomodações:** importe propriedades de hotéis com suas comodidades, tipos de quartos e preços e envie promoções para seus usuários com base nas preferências selecionadas.
- **Meios de transporte:** importe ofertas e promoções para meios de transporte (como voos, trens, aluguel de carros e outros) e envie-as aos seus usuários com base no histórico de pesquisa recente.
- **Preferências de refeições:** importe informações sobre ofertas de refeições e use [seleções]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) para enviar mensagens personalizadas aos usuários que têm preferências específicas de refeições com base na categoria de alimentos visualizada mais recentemente.

## Como os catálogos e o Liquid funcionam juntos {#how-catalogs-and-liquid-work-together}

Os catálogos são um recurso de armazenamento de dados. Eles contêm grandes conjuntos de dados que podem ser referenciados nas suas mensagens para personalização. Para referenciar os dados, você usará o [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) como linguagem de template. Em outras palavras, os catálogos são o armazenamento onde os dados ficam guardados, e o Liquid é a linguagem que extrai os dados relevantes desse armazenamento.

Para exemplos de como usar o Liquid para extrair informações do catálogo, consulte os casos de uso adicionais em [Criar um catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create#use-cases).

## Limitações de armazenamento de dados {#data-storage-limitations}

O armazenamento de dados para catálogos é limitado com base no tamanho dos itens do catálogo, que pode ser diferente do tamanho dos arquivos CSV enviados por upload.

Para a versão gratuita dos catálogos, a quantidade de armazenamento permitida é de até 500&nbsp;MB. Você pode ter itens ilimitados, desde que o espaço de armazenamento não exceda 500&nbsp;MB.

Para o Catalogs Pro, as opções de tamanho de armazenamento são: 5&nbsp;GB, 10&nbsp;GB, 15&nbsp;GB ou 50&nbsp;GB. Note que o armazenamento da versão gratuita (500&nbsp;MB) está incluído em cada um desses planos.

Se você precisar fazer upgrade do armazenamento do seu catálogo, entre em contato com o gerente de conta da Braze. Para detalhes do plano e notas sobre direitos, consulte [Armazenamento de catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers).