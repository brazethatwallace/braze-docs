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

## Geral {#general}

### Existem limites de armazenamento para imagens na biblioteca de mídia? {#are-there-storage-limits-for-images-within-the-media-library}

Não, não existem limites de armazenamento para ativos na biblioteca de mídia. No entanto, existem limites de tamanho para ativos (máximo de 5 MB).

### Existem datas de expiração para ativos enviados? {#are-there-expiration-dates-for-uploaded-assets}

Não, os ativos enviados para a biblioteca de mídia serão mantidos durante toda a duração do seu contrato com a Braze.

### Posso enviar ativos de vídeo? {#can-i-upload-video-assets}

Não, a biblioteca de mídia não suporta arquivos de vídeo. Recomendamos que você hospede esses arquivos externamente ou em uma plataforma como o YouTube.

### Posso cortar todos os tipos de imagem? {#can-i-crop-all-image-types}

Não, a biblioteca de mídia não suporta o corte de imagens GIF.

### Como copio a URL de uma imagem enviada para a biblioteca de mídia? {#how-do-i-copy-the-url-of-an-image-uploaded-to-the-media-library}

Para copiar a URL de uma imagem enviada para a biblioteca de mídia, navegue até **Conteúdo** > **Biblioteca de mídia**. Passe o cursor sobre a imagem que deseja referenciar e selecione o ícone **Copiar URL da imagem** para copiar a URL da imagem para a área de transferência.

### Posso usar imagens SVG em e-mail? {#can-i-use-svg-images-in-email}

Imagens SVG não são recomendadas para e-mail devido ao suporte limitado entre os clientes de e-mail. O Gmail e vários outros provedores de e-mail importantes não renderizam imagens SVG, o que pode resultar em imagens quebradas ou ausentes para os destinatários. Para uma renderização confiável de e-mail, use os formatos PNG, JPEG ou GIF.

### Como corto uma imagem existente? {#how-do-i-crop-an-existing-image}

Você pode cortar uma imagem existente selecionando a imagem na biblioteca de mídia e clicando em **Cortar e salvar nova imagem**.

![Prévia da imagem na biblioteca de mídia.]({% image_buster /assets/img_archive/media_library_crop1.png %}){: height="75%" width="75%"}

Você será redirecionado para um criador de corte onde poderá selecionar o tipo de proporção e editar o nome da nova imagem. Ao selecionar **Salvar**, sua nova imagem estará pronta para uso.

![Janela para cortar e salvar imagem da biblioteca de mídia.]({% image_buster /assets/img_archive/media_library_crop2.png %}){: height="75%" width="75%"}

### Minha imagem fica expirando quando tento enviá-la. O que posso fazer? {#my-image-keeps-timing-out-when-i-try-to-upload-it-what-can-i-do-about-this}

Isso pode acontecer por vários motivos, mas uma solução comum é garantir que sua imagem esteja otimizada antes de tentar enviá-la. Isso significa passar sua imagem por um otimizador de imagens como o [ImageOptim](https://imageoptim.com/mac).

Além disso, se sua imagem foi criada no Photoshop (ou software similar) e possui muitas camadas, mesclar e reduzir o número de camadas também pode ajudar.

### Vejo um "Erro inesperado" ao enviar uma imagem, mesmo ela tendo menos de 5 MB e estando em um formato suportado. Qual é o problema? {#i-see-an-unexpected-error-when-uploading-an-image-even-though-its-under-5-mb-and-in-a-supported-format-whats-wrong}

Isso pode acontecer por dois motivos principais:

1. **Metadados inválidos no arquivo:** O software que a Braze usa para processar imagens pode rejeitar arquivos com metadados inválidos ou incompatíveis. Em alguns casos, o arquivo também pode ser processado de uma forma que ultrapasse o limite de 5 MB. Tente usar uma imagem diferente (por exemplo, reexporte ou salve novamente a imagem no seu editor de imagens) ou uma imagem de outra fonte.
2. **Caracteres especiais no nome do arquivo:** Nomes de arquivo que contêm caracteres especiais (como `&` ou `%`) podem causar falha no envio. Renomeie o arquivo para usar apenas letras, números, hifens ou underscores e tente enviar novamente.

### Por que não consigo enviar qualquer imagem nos criadores de push? {#why-cant-i-upload-any-image-i-want-into-the-push-composers}

Isso acontece porque a maioria dos criadores possui restrições na proporção de tamanho de imagem permitida.

### Gerar uma imagem usando IA {#generate-an-image-using-ai}

Você pode gerar imagens em **Conteúdo** > **Biblioteca de mídia** selecionando **Gerador de imagens com IA**. Você precisa da permissão **Editar ativos da biblioteca de mídia**. Se não vir a opção, entre em contato com a equipe de clientes da Braze. Para etapas e detalhes de política, consulte [Gerar imagens com BrazeAI]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-images) e [Gerando imagens com BrazeAI]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#generate-ai).

### O que acontece quando excluo uma imagem da biblioteca de mídia? {#what-happens-when-i-delete-an-image-from-the-media-library}

Excluir um ativo o remove da interface da biblioteca de mídia, mas a Braze mantém o arquivo hospedado na URL existente, de modo que Campaigns e Canvas ativos que referenciam essa URL continuam carregando a imagem. Para remover permanentemente um ativo da hospedagem da Braze, entre em contato com o suporte da Braze. Para atualizar o que os destinatários veem sem alterar URLs em cada mensagem, use [Substituir um arquivo]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file).

### Posso alterar ativos de imagem em e-mails que já foram enviados? {#can-i-change-image-assets-in-emails-that-have-already-been-sent}

Você pode atualizar a imagem em um e-mail já enviado [substituindo o arquivo]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file) na URL existente. A URL e o ID do ativo permanecem os mesmos, então qualquer mensagem que o referencia, incluindo e-mails já enviados, reflete o novo arquivo. Alguns destinatários ainda podem ver a imagem anterior se ela já estava em cache no dispositivo antes da alteração, então isso não garante que todos os destinatários vejam a atualização imediatamente.

### Posso criar URLs personalizadas para ativos de imagem da biblioteca de mídia? {#can-i-create-vanity-urls-for-media-library-image-assets}

URLs personalizadas para ativos da biblioteca de mídia não são suportadas porque URLs customizadas quebrariam a entrega via rede de distribuição de conteúdo (CDN). Você pode substituir uma imagem na URL existente quando Campaigns já referenciam essa URL. Para saber mais, consulte [Substituir um arquivo]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file).

### Por que o Chrome salva imagens JPEG ou PNG como arquivos WebP? {#why-does-chrome-save-jpeg-or-png-images-as-webp-files}

Ao usar o Chrome para salvar imagens da biblioteca de mídia, o navegador pode converter automaticamente arquivos JPEG ou PNG para o formato WebP. Esse é o comportamento padrão do Chrome para downloads de imagens e não é específico da Braze. Se você precisa salvar imagens no formato original, tente usar um navegador diferente, como Safari ou Firefox.