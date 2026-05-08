---
nav_title: Biblioteca de mídia
article_title: Biblioteca de mídia
page_order: 2
page_type: reference
description: "Este artigo de referência aborda a Biblioteca de mídia. Aqui, você pode aprender a gerenciar seus ativos em um único local centralizado, gerar imagens usando IA e acessar mídias no criador de mensagens."
tool: Media

---

# Biblioteca de mídia

> A Biblioteca de mídia permite que você gerencie seus ativos em um único local centralizado.

## Biblioteca de mídia versus CDN

Usar a Biblioteca de mídia em vez de uma Content Delivery Network (CDN) oferece melhor cache e desempenho para mensagens no app. Todos os ativos da Biblioteca de mídia encontrados em uma mensagem no app serão pré-armazenados em cache para exibição mais rápida e estarão disponíveis para exibição offline. Além disso, a Biblioteca de mídia é integrada aos criadores da Braze, permitindo que profissionais de marketing selecionem ou adicionem tags às imagens em vez de copiar e colar URLs de imagens.

## Acessando a Biblioteca de mídia

Na Biblioteca de mídia, você pode ver o tipo de ativo, tamanho, dimensões, URL, a data em que foi adicionado à biblioteca e outras informações. Para acessar a Biblioteca de mídia da Braze, acesse **Modelos** > **Biblioteca de mídia**. Aqui, você pode:

* Fazer upload de várias imagens de uma vez
* Fazer upload de arquivos de contato virtual (.vcf)
* Fazer upload de arquivos de vídeo para uso em mensagens do WhatsApp
* Fazer upload de uma pasta com suas imagens (até 50 imagens)
* [Gerar uma imagem usando IA](#generate-ai) e armazená-la na Biblioteca de mídia
* Recortar uma imagem existente para criar a proporção certa para suas mensagens
* Adicionar tags ou equipes para ajudar a organizar melhor suas imagens
* Pesquisar por tags ou equipes na grade da Biblioteca de mídia
* Arrastar e soltar imagens ou pastas para fazer upload
* Excluir imagens

![Página da Biblioteca de mídia que inclui uma seção "Fazer upload para a biblioteca" para arrastar e soltar ou fazer upload de arquivos. Também há uma lista de conteúdo já enviado na Biblioteca de mídia.]({% image_buster /assets/img_archive/media_library_main.png %})

Depois, ao redigir uma mensagem na Braze, você pode importar suas imagens da Biblioteca de mídia.

![Duas formas comuns de acessar a Biblioteca de mídia dependendo do criador de mensagens. Uma mostra o editor de arrastar e soltar de e-mail com o título "Imagens e GIFs" e um botão "Adicionar da Biblioteca de mídia". A outra mostra os editores padrão, como push e mensagens no app, com o título "Mídia" e um botão "Adicionar imagem".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Para mais ajuda com a Biblioteca de mídia, confira nossas [Perguntas frequentes sobre a Biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/faq/). {% endalert %}

## Especificações de imagem

Todas as imagens enviadas para a Biblioteca de mídia devem ter menos de 5&nbsp;MB. Os tipos de arquivo compatíveis são PNG, JPEG, GIF, SVG e WebP. Para tamanhos e especificações de imagem recomendados por canal de envio de mensagens, consulte [Especificações de imagem]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications/).

{% alert important %}
GIFs com formatos muito alongados (por exemplo, 3000 x 2 pixels) ou com 300 ou mais quadros podem falhar no upload, mesmo que o tamanho total do arquivo seja pequeno.
{% endalert %}

## Gerando imagens com BrazeAI<sup>TM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Antes de usar esse recurso, revise [como seus dados são usados e enviados para a OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}