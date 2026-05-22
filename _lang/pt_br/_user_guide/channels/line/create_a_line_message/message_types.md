---
nav_title: Tipos de mensagem
article_title: Tipos de mensagem LINE
page_order: 0
description: "Este artigo aborda os diferentes tipos de mensagens LINE."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/message_types/
---

# Tipos de mensagem LINE {#line-message-types}

> Este artigo aborda os tipos de mensagem LINE que você pode redigir, incluindo aspectos e limitações.

Ao redigir uma mensagem LINE, você pode arrastar e soltar tipos de mensagem no criador e depois personalizá-los.

![Painel de tipos de mensagem com opções para arrastar no editor do criador, incluindo texto, imagem, mensagem rica e mensagem baseada em cartão.]({% image_buster /assets/img/line/line_message_types.png %}){: style="max-width:40%;"}

## Texto {#text}

Uma mensagem de texto LINE pode conter até 5.000 caracteres e incluir emojis e personalização com Liquid.

Casos de uso incluem:
- Anunciar uma promoção por tempo limitado para estoque em liquidação
- Enviar cumprimentos de aniversário personalizados com cartões de promoção exclusivos
- Compartilhar atualizações rápidas sobre eventos futuros

![Uma mensagem de texto lembrando o usuário de não esquecer da festa de Black Friday e do potencial de economizar até 80% antes da meia-noite.]({% image_buster /assets/img/line/line_text_message.png %}){: style="max-width:40%;"}

## Imagem {#image}

Uma mensagem de imagem LINE pode ser adicionada pela [Biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/), por URL ou por Liquid. Essas imagens são independentes e não contêm links clicáveis.

Casos de uso incluem:
- Exibir um destino de férias para inspirar os usuários a pesquisar passagens aéreas
- Destacar promoções de fim de temporada para incentivar os usuários a estocar roupas de inverno do próximo ano com ótimas ofertas
- Iniciar uma contagem regressiva visual para uma liquidação anual em toda a loja

![Uma mensagem de imagem promovendo uma liquidação de torradeiras.]({% image_buster /assets/img/line/line_image_message.png %}){: style="max-width:40%;"}

### Imagem por URL {#url-image}

Use imagens por URL para casos de uso que incorporam:
- Imagens dinâmicas com Liquid, incluindo o Liquid no atributo de origem da imagem. Por exemplo, você pode inserir {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} como a URL da imagem para incluir o nome do usuário na imagem
- [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) puxando imagens diretamente do seu servidor web ou de APIs acessíveis publicamente
- [Catálogos da Braze]({{site.baseurl}}/user_guide/data/activation/catalogs/) acessando imagens de arquivos CSV importados e endpoints de API

| **Especificações** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| Comprimento da URL do arquivo de imagem | 2.000 caracteres no máximo  |
| Formato da imagem          | PNG, JPEG             |
| Tamanho do arquivo     |  10&nbsp;MB no máximo |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URL image" }

## Mensagens ricas (mapa de imagem) {#rich-messages-image-map}

Uma mensagem rica LINE é uma imagem que contém um ou mais links que são abertos ao selecionar áreas específicas na imagem. Selecione um modelo de mensagem rica para escolher como os links são mapeados na imagem.

Casos de uso incluem:
- Exibir uma grade de bolsas recém-chegadas com links para a página de produto de cada bolsa
- Apresentar um menu interativo que inicia um pedido de combo ao selecionar um item
- Dispor múltiplas promoções para os usuários escolherem ao selecionar um quadrado da grade

![Uma mensagem rica de seis quadrados com uma foto de uma grade em preto e branco que os usuários podem tocar para receber uma oferta aleatória.]({% image_buster /assets/img/line/line_rich_message.png %})

### Mapa de imagem {#image-map}

| **Especificações** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| Comprimento da URL do arquivo de imagem | 2.000 caracteres no máximo  |
| Formato da imagem          | PNG (pode ser transparente), JPEG             |
| Proporção          | 1:1 (largura:altura)
| Tamanho do arquivo     |  10&nbsp;MB no máximo |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image map" }

### Link URI {#uri-link}

| **Especificações** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| Contagem de caracteres      | 1.000 no máximo |
| Esquemas              | HTTP, HTTPS, LINE, tel |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URI link" }

### Texto

Uma mensagem rica de texto pode conter até 400 caracteres.

## Baseada em cartão (carrossel) {#card-based-carousel}

Uma mensagem LINE baseada em cartão permite que os usuários rolem por várias mensagens, como um carrossel, e tomem ação nas mensagens mais relevantes para eles ao selecionar um cartão ou os botões de um cartão.

Casos de uso incluem:
- Exibir promoções para itens específicos do menu
- Destacar as jaquetas mais vendidas da temporada
- Apresentar uma amostra de utensílios e gadgets de cozinha incluídos em um kit

![Uma mensagem baseada em cartão com pelo menos dois cartões que promovem sanduíches no editor do criador.]({% image_buster /assets/img/line/line_card_message.png %})

### Mensagem {#message}

| **Especificações** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| Colunas                  | 10 no máximo |
| Proporção             | Retângulo: 1,51:1 <br> Quadrado: 1:1  |
| Título                    | 40 caracteres no máximo
{: .reset-td-br-1 .reset-td-br-2 aria-label="Message" }


### Imagem

| **Especificações** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| URL da imagem                 | 2.000 caracteres no máximo |
| Formato da imagem              | JPEG ou PNG |
| Largura                     | 1.024 pixels  |
| Tamanho do arquivo                 | 1 MB |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image" }


### Texto

| **Especificações** | **Propriedades recomendadas** |
|-------------------------|----------------------------|
| Caracteres              | 120 no máximo (sem imagem ou título) <br> 60 no máximo (mensagem com imagem ou título)  |
| Ações                 | 3 no máximo |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Text" }