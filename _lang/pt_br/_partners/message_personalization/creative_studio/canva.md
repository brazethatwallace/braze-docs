---
nav_title: Canva
article_title: Canva
description: "Este artigo de referência descreve a parceria entre a Braze e o Canva para enviar ativos de mídia para a biblioteca de mídia da Braze e publicar designs de e-mail do Canva como modelos de e-mail da Braze."
alias: /partners/canva/
page_type: partner
search_tag: Partner

---

# Canva

> O [Canva](https://www.canva.com/) é uma plataforma e ferramenta de design gráfico que permite criar conteúdo visual para publicações em redes sociais, apresentações, vídeos e muito mais. O app da Braze no Canva também permite exportar designs de **e-mail** como modelos de e-mail da Braze, além de enviar designs estáticos para a sua biblioteca de mídia.

## Sobre a integração {#about-the-integration}

A integração entre a Braze e o Canva oferece dois caminhos de exportação:

| Tipo de exportação | O que faz |
| --- | --- |
| **Imagem ou design para a biblioteca de mídia** | Envia seu design como um ativo para a biblioteca de mídia da Braze. |
| **Design de e-mail para a Braze** | Publica um documento de **e-mail** do Canva como um modelo de e-mail da Braze, incluindo metadados de linha de assunto. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sobre a integração" }

## Integrar a Braze com o Canva {#integrate-braze-with-canva}

### Etapa 1: Instalar o app da Braze no Canva {#step-1-install-the-braze-app-in-canva}

Você pode encontrar o app da Braze no [Canva Apps Marketplace](https://www.canva.com/your-apps/AAG1cO7kIyc).

Após instalar o app, ele fica disponível dentro de um design, no menu **Apps**.

![App da Braze no menu Apps do Canva.]({% image_buster /assets/img/canva_integration/braze-canva-app.png %}){: style="max-width:50%;"}

### Etapa 2: Autorizar sua conta da Braze {#step-2-authorize-your-braze-account}

Na primeira vez que você usar o app da Braze — seja abrindo pelo menu **Apps** (exportação para a biblioteca de mídia) ou pelo menu **Share** (exportação de e-mail) — selecione **Connect** para iniciar a autorização. Isso permite que o Canva liste os espaços de trabalho da Braze aos quais você tem acesso e crie ativos na biblioteca de mídia em seu nome.

Para exportações de **e-mail**, o Canva pode solicitar que você faça login novamente e aprove acessos adicionais, incluindo permissão para **criar modelos de e-mail**. Aceite essas permissões para concluir a publicação de designs de e-mail na Braze.

![Botão Connect e fluxo de autorização para vincular o Canva à Braze.]({% image_buster /assets/img/canva_integration/canva-connect-panel.jpg %})

## Exportar imagens para a biblioteca de mídia {#export-images-to-the-media-library}

Use este fluxo para designs padrão do Canva quando você quiser um arquivo na biblioteca de mídia da Braze.

Os vídeos a seguir mostram como enviar designs do Canva para a sua biblioteca de mídia da Braze.

Vídeo: Abra o app da Braze no Canva e inicie uma exportação para a biblioteca de mídia.

{% multi_lang_include video.html id="uf5krks2cx" source="wistia" %}

Vídeo: Escolha um espaço de trabalho da Braze e conclua a exportação para a biblioteca de mídia.
{% multi_lang_include video.html id="3d09tafx7c" source="wistia" %}

1. No menu **Apps** do seu design, abra o app da Braze. Se você ainda não estiver conectado, selecione **Connect** e conclua as etapas em [Autorizar sua conta da Braze](#step-2-authorize-your-braze-account).
2. Escolha o espaço de trabalho de destino, opcionalmente insira um nome de arquivo e selecione **Start Export**.

![Tela de exportação do Canva com espaço de trabalho de destino e botão Start Export.]({% image_buster /assets/img/canva_integration/canva-upload-screen.jpg %})

{: start="3"}
3. Quando a exportação for concluída, seu novo ativo estará disponível na **biblioteca de mídia**, com a origem "Canva".

![Ativo exportado do Canva na biblioteca de mídia da Braze.]({% image_buster /assets/img/canva_integration/media-library-source.jpg %})

## Exportar designs de e-mail como modelos da Braze {#export-email-designs-as-braze-templates}

Use este fluxo quando seu arquivo do Canva for um design do tipo **e-mail**. Ele publica o HTML na Braze como um modelo (metadados semelhantes ao fluxo de imagem, mas você começa pelo **Share** em vez de **Apps**).

1. No Canva, crie ou abra um design de **e-mail**. Construa sua mensagem do zero ou use um modelo de e-mail do Canva.
2. Clique em **Share** na barra de ações do editor e selecione **Braze**. Se a Braze não estiver listada, abra **See more** e role até **More options** para encontrar a Braze.

![Mais formas de publicar no Canva com a Braze em More options.]({% image_buster /assets/img/canva_integration/canva-share-more-options-braze.png %})

{: start="3"}
3. Se for solicitado que você conecte ou faça login novamente, selecione **Connect** no painel da Braze (ou conclua o fluxo de login no navegador) para que o Canva possa criar modelos no seu espaço de trabalho.

![Barra lateral da Braze no Canva solicitando Connect para exportação de e-mail.]({% image_buster /assets/img/canva_integration/canva-email-connect-sidebar.png %})

{: start="4"}
4. No painel da Braze, selecione qual página de **e-mail** publicar (se o design tiver várias páginas), escolha seu **espaço de trabalho da Braze**, insira um **Template name** e uma **Subject line** e selecione **Publish now**. O Canva mostra o progresso enquanto seu design é publicado.

![Painel da Braze no Canva com espaço de trabalho, nome do modelo, linha de assunto e Publish now.]({% image_buster /assets/img/canva_integration/canva-email-publish-fields.png %})

{: start="5"}
5. Quando a publicação for concluída, uma mensagem de sucesso aparece. Selecione **Check it out** para abrir o modelo de e-mail na Braze.

![Mensagem de sucesso após publicar um design de e-mail do Canva na Braze, com Check it out.]({% image_buster /assets/img/canva_integration/canva-email-publish-success.png %})

{: start="6"}
6. Na Braze, finalize as configurações de e-mail necessárias — como endereço de **remetente**, pré-cabeçalho e um link de cancelamento de inscrição — antes de usar o modelo em uma Campaign ou Canvas.

![Modelo de e-mail na Braze aberto a partir do Canva, com informações de envio e prévia.]({% image_buster /assets/img/canva_integration/braze-email-template-from-canva.png %})