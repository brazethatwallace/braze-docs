---
nav_title: Biblioteca de mídia
article_title: Biblioteca de mídia
page_order: 2
page_type: reference
description: "Este artigo de referência aborda a Biblioteca de mídia. Aqui, você pode aprender a gerenciar seus ativos em um único local centralizado, gerar imagens usando IA e acessar mídias no criador de mensagens."
tool: Media

---

# Biblioteca de mídia {#media-library}

> A Biblioteca de mídia permite que você gerencie seus ativos em um único local centralizado.

## Pré-requisitos {#prerequisites}

| Requisitos | Descrição |
|---|---|
| Permissão "View Media Library Assets" | Visualizar ativos da biblioteca de mídia |
| Permissão "Edit Media Library Assets" | Criar e atualizar ativos da biblioteca de mídia |
| Permissão "Delete Media Library Assets" | Remover ativos da biblioteca de mídia da interface. Os ativos excluídos continuam hospedados pela Braze para evitar a quebra de mensagens que os referenciam. Para excluir permanentemente um ativo, entre em contato com o suporte da Braze. |
| Permissão "Replace Media Library Assets" | Substituir o arquivo de um ativo existente na biblioteca de mídia, mantendo sua URL e ID do ativo estáveis |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permissões da biblioteca de mídia" }

Para saber mais, consulte [Permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

## Biblioteca de mídia versus CDN {#media-library-versus-cdn}

Usar a biblioteca de mídia em vez de uma rede de distribuição de conteúdo (CDN) oferece melhor cache e performance para mensagens no app. Todos os ativos da biblioteca de mídia encontrados em uma mensagem no app são pré-armazenados em cache para exibição mais rápida e ficam disponíveis para exibição offline. Além disso, a biblioteca de mídia é integrada aos criadores da Braze, permitindo que você selecione ou adicione tags às imagens em vez de copiar e colar URLs de imagens.

## Acessando a biblioteca de mídia {#accessing-the-media-library}

Na biblioteca de mídia, você pode ver o tipo de ativo, tamanho, dimensões, URL, a data em que foi adicionado à biblioteca e outras informações. Para acessar a biblioteca de mídia da Braze, acesse **Conteúdo** > **Biblioteca de mídia**. Aqui, você pode:

* Fazer upload de várias imagens de uma vez
* Fazer upload de arquivos de contato virtual (.vcf)
* Fazer upload de arquivos de vídeo para uso em mensagens do WhatsApp
* Fazer upload de uma pasta com suas imagens (até 50 imagens)
* [Gerar uma imagem usando IA](#generate-ai) e armazená-la na biblioteca de mídia
* Cortar uma imagem existente para criar a proporção certa para suas mensagens
* Substituir o arquivo de um ativo existente mantendo sua URL estável
* Adicionar tags ou equipes para ajudar a organizar melhor suas imagens
* Pesquisar por tags ou equipes na grade da biblioteca de mídia
* Arrastar e soltar imagens ou pastas para upload
* Excluir imagens

![Página da Biblioteca de mídia que inclui uma seção "Fazer upload para a biblioteca" para arrastar e soltar ou fazer upload de arquivos. Também há uma lista de conteúdo enviado na biblioteca de mídia.]({% image_buster /assets/img_archive/media_library_main.png %})

Depois, ao redigir uma mensagem na Braze, você pode importar suas imagens da biblioteca de mídia.

![Duas formas comuns de acessar a biblioteca de mídia dependendo do criador de mensagem. Uma mostra o editor de arrastar e soltar de e-mail com o título "Imagens e GIFs" e um botão "Adicionar da Biblioteca de mídia". A outra mostra os editores padrão, como push e mensagens no app, com o título "Mídia" e um botão "Adicionar imagem".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Para mais ajuda com a biblioteca de mídia, confira nosso [FAQ da Biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/faq). {% endalert %}

## Uploads de arquivos ZIP {#zip-file-uploads}

Ao fazer upload de um arquivo ZIP para a biblioteca de mídia, todos os arquivos devem estar na raiz da pasta ZIP — não inclua subdiretórios.

Isso se aplica a todos os arquivos no arquivo compactado, incluindo arquivos de fonte (`.ttf`, `.woff`, `.otf`, `.woff2`), HTML, CSS, JavaScript e imagens. Coloque cada arquivo na raiz do ZIP junto com os demais.

Como alternativa, faça upload dos ativos individualmente para a biblioteca de mídia sem compactá-los.

## Substituir um arquivo {#replace-a-file}

Você pode substituir o arquivo de um ativo existente na biblioteca de mídia mantendo a URL e o ID do ativo estáveis. Como a URL não muda, qualquer mensagem ou Campaign que faça referência a esse ativo — incluindo e-mails já enviados — reflete automaticamente o arquivo atualizado. Isso é útil quando você deseja atualizar um ativo compartilhado (como um logotipo) em um único lugar, em vez de atualizar cada Campaign individualmente.

Para substituir um ativo, você precisa ter a permissão "Replace Media Library Assets":

1. Acesse **Conteúdo** > **Biblioteca de mídia**.
2. Selecione o ativo que deseja substituir.
3. No modal, selecione **Replace file**.
4. Faça upload do arquivo de substituição.

![Modal de edição da biblioteca de mídia mostrando os botões Replace file, Crop image e Delete para um ativo.]({% image_buster /assets/img_archive/media_library_replace_file.png %}){: style="max-width:60%;border:none"}

### Requisitos e limitações {#requirements-and-limitations}

- O arquivo de substituição deve ter a mesma extensão de arquivo que o original. Por exemplo, não é possível substituir um ativo `.png` por um arquivo `.jpg`.
- Ativos de vídeo não podem ser substituídos.
- Após a substituição, o arquivo atualizado pode levar algum tempo para ser exibido para todos os consumidores devido ao cache da CDN.

### Canais com cópias de imagem processadas {#channels-with-processed-image-copies}

Alguns canais criam uma cópia otimizada da imagem quando a mensagem é configurada, resultando em uma URL separada. Isso se aplica independentemente de a imagem ter sido adicionada a partir da biblioteca de mídia ou por meio de uma URL externa (por exemplo, de um bucket S3). Substituir o ativo original da biblioteca de mídia não atualiza o que os consumidores veem nas mensagens criadas usando esses canais, incluindo Content Cards, notificações por push e banners.

Mensagens no app tradicionais (modal, slideup e tela cheia) também seguem esse comportamento. No entanto, mensagens no app em HTML e mensagens no app de arrastar e soltar não seguem. Para esses tipos, a Braze não armazena a imagem em cache, então alterar ou remover a URL da imagem original quebra a imagem em campanhas ativas.

Você também pode substituir um ativo programaticamente usando o endpoint [`PUT /media_library/replace_file`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/replace_file).

## Especificações de imagem {#image-specifications}

Todas as imagens enviadas para a biblioteca de mídia devem ter menos de 5&nbsp;MB. Os tipos de arquivo suportados são PNG, JPEG, GIF, SVG e WebP. Para tamanhos e especificações de imagem recomendados por canal de envio de mensagens, consulte [Especificações de imagem]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications).

{% alert important %}
GIFs com formatos muito alongados (por exemplo, 3000 x 2 pixels) ou com 300 ou mais quadros podem falhar no upload, mesmo que o tamanho total do arquivo seja pequeno.
{% endalert %}

## Gerando imagens com BrazeAI<sup>TM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Antes de usar esse recurso, revise [como seus dados são usados e enviados para a OpenAI]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#data-privacy-and-security).
{% endalert %}

Se você não vir **Gerar com Operator** na página da **Biblioteca de mídia**, confirme que você tem a permissão "Edit Media Library Assets". Se a opção ainda não aparecer, entre em contato com a equipe da Braze para confirmar que seu espaço de trabalho tem acesso à geração de imagens com BrazeAI. Se a geração falhar, revise a [política de conteúdo da OpenAI]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#data-privacy-and-security).