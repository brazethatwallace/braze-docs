---
nav_title: FAQ
article_title: FAQ da Biblioteca de mídia
page_order: 2
page_type: FAQ
tool: Media
description: "Este artigo fornece respostas para perguntas frequentes sobre a Biblioteca de mídia na Braze."

---

# Perguntas frequentes {#frequently-asked-questions}

> Esta página fornece respostas para perguntas frequentes sobre a Biblioteca de mídia na Braze.

### Existem limites de armazenamento para imagens na Biblioteca de mídia? {#are-there-storage-limits-for-images-within-the-media-library}

Não, não existem limites de armazenamento para ativos na Biblioteca de mídia. No entanto, existem limites de tamanho para ativos (máximo de 5 MB).

### Existem datas de expiração para ativos enviados? {#are-there-expiration-dates-for-uploaded-assets}

Não, os ativos enviados para a Biblioteca de mídia serão mantidos durante toda a duração do seu contrato com a Braze.

### Posso fazer upload de ativos de vídeo? {#can-i-upload-video-assets}

Não, a Biblioteca de mídia não oferece suporte a arquivos de vídeo. Recomendamos que você hospede esses arquivos externamente ou em uma plataforma como o YouTube.

### Posso recortar todos os tipos de imagem? {#can-i-crop-all-image-types}

Não, a Biblioteca de mídia não oferece suporte ao recorte de imagens GIF.

### Como faço para recortar uma imagem existente? {#how-do-i-crop-an-existing-image}

Você pode recortar uma imagem existente selecionando a imagem na Biblioteca de mídia e clicando em **Crop & Save New Image**.

![Pré-visualização de imagem da Biblioteca de mídia.]({% image_buster /assets/img_archive/media_library_crop1.png %}){: height="75%" width="75%"}

Você será redirecionado para um criador de recorte onde poderá selecionar o tipo de proporção e editar o nome da nova imagem. Ao selecionar **Save**, sua nova imagem estará pronta para uso.

![Janela para recortar e salvar imagem da Biblioteca de mídia.]({% image_buster /assets/img_archive/media_library_crop2.png %}){: height="75%" width="75%"}

### Minha imagem fica expirando quando tento fazer upload. O que posso fazer? {#my-image-keeps-timing-out-when-i-try-to-upload-it-what-can-i-do-about-this}

Isso pode acontecer por vários motivos, mas uma solução comum é garantir que sua imagem esteja otimizada antes de tentar fazer upload. Isso significa passar sua imagem por um otimizador de imagens como o [ImageOptim](https://imageoptim.com/mac).

Além disso, se sua imagem foi criada no Photoshop (ou software similar) e possui muitas camadas, mesclar e reduzir o número de camadas também pode ajudar.

### Vejo um "Erro inesperado" ao fazer upload de uma imagem, mesmo ela tendo menos de 5 MB e estando em um formato compatível. Qual é o problema? {#i-see-an-unexpected-error-when-uploading-an-image-even-though-its-under-5-mb-and-in-a-supported-format-whats-wrong}

Isso pode acontecer por dois motivos principais:

1. **Metadados inválidos no arquivo:** O software que a Braze usa para processar imagens pode rejeitar arquivos com metadados inválidos ou incompatíveis. Em alguns casos, o arquivo também pode ser processado de uma forma que ultrapasse o limite de 5 MB. Tente usar uma imagem diferente (por exemplo, reexporte ou salve novamente a imagem no seu editor de imagens) ou uma imagem de outra origem.
2. **Caracteres especiais no nome do arquivo:** Nomes de arquivo que contêm caracteres especiais (como `&` ou `%`) podem causar falha no upload. Renomeie o arquivo para usar apenas letras, números, hifens ou underscores e tente fazer upload novamente.

### Por que não consigo fazer upload de qualquer imagem nos criadores de push? {#why-cant-i-upload-any-image-i-want-into-the-push-composers}

Isso acontece porque a maioria dos criadores possui restrições quanto à proporção de tamanho de imagem permitida.

### Gerar uma imagem usando IA {#generate-an-image-using-ai}

Você pode gerar imagens em **Conteúdo** > **Biblioteca de mídia** selecionando **Gerador de imagens com IA**. Você precisa da permissão **Editar ativos da Biblioteca de mídia**. Se você não vir essa opção, entre em contato com a equipe da Braze. Para etapas e detalhes de política, consulte [Gerar imagens com BrazeAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/) e [Gerando imagens com BrazeAI]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/#generate-ai).

### Posso criar URLs personalizadas para ativos de imagem da Biblioteca de mídia? {#can-i-create-vanity-urls-for-media-library-image-assets}

URLs personalizadas para ativos da Biblioteca de mídia não são suportadas porque URLs customizadas quebrariam a entrega via CDN. Você pode substituir uma imagem na URL existente quando Campaigns já fazem referência a essa URL. Para saber mais, consulte [Substituir um arquivo]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/#replace-a-file).