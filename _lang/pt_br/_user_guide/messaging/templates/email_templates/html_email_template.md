---
nav_title: Fazer upload de um modelo de e-mail HTML
article_title: Fazer upload de um modelo de e-mail HTML
page_order: 2
description: "Este artigo de referência aborda como criar, gerenciar e solucionar problemas de um modelo de e-mail HTML usando o dashboard da Braze."
tool:
  - Templates
channel:
  - email

---

# Fazer upload de um modelo de e-mail HTML {#upload-an-html-email-template}

> O dashboard da Braze permite que você faça upload dos seus próprios modelos de e-mail HTML e os salve para uso posterior em Campaigns. Você também pode [criar um modelo de e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template) usando nosso editor.

## Requisitos {#upload-requirements}

Primeiro, você precisará criar seu modelo de e-mail HTML. Ele deve ser um arquivo ZIP contendo o seguinte:

* Um único arquivo HTML — o corpo do seu e-mail
* Uma pasta de imagens referenciadas no arquivo HTML
* Menos de 50 arquivos de imagem
* Tamanho inferior a 5&nbsp;MB

## Fazendo upload do seu modelo {#uploading-your-template}

### Etapa 1: Acesse o editor de modelos de e-mail {#step-1-go-to-the-email-template-editor}

Acesse **Content** > **Email**. Selecione **Create email template**.

### Etapa 2: Adicione os detalhes do modelo {#step-2-add-template-details}

Forneça um nome para o modelo. Opcionalmente, adicione uma descrição, equipes e tags.

### Etapa 3: Faça upload do seu modelo {#step-3-upload-your-template}

Na seção **Template content**, selecione **Upload file** abaixo do bloco **HTML code editor**. Selecione seu modelo no computador. Consulte a seção [Requisitos](#upload-requirements) para garantir que seu modelo atenda aos requisitos de upload.

### Etapa 4: Finalize e salve seu modelo {#step-4-finish-and-save-your-template}

Não se esqueça de salvar seu modelo selecionando **Save template**. Agora você está pronto para usar esse modelo em qualquer Campaign ou Canvas que desejar.

{% alert note %}
Se você fizer edições em um modelo existente, essas alterações não serão refletidas em Campaigns que foram criadas usando versões anteriores desse modelo.
{% endalert %}

## Usando seus modelos em Campaigns da API {#api_for_upload_email_templates}

Para usar seu e-mail em uma Campaign da API, você precisa do `email_template_id`, que pode ser encontrado na parte inferior de qualquer modelo de e-mail criado na Braze.

![Seção do identificador de API de um modelo de e-mail HTML.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## Gerenciando modelos de e-mail {#managing-email-templates}

Você pode [duplicar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates) e [arquivar]({{site.baseurl}}/user_guide/messaging/templates/managing_templates) modelos de e-mail! Saiba mais sobre como criar e gerenciar modelos e conteúdo criativo em [Modelos]({{site.baseurl}}/user_guide/messaging/templates).

## Solução de problemas {#troubleshooting}

Existem várias mensagens de erro de e-mail que você pode receber ao fazer upload de um arquivo de modelo HTML. Se você receber um erro, consulte a tabela a seguir para problemas comuns e suas correções recomendadas:

| Erro | Correção |
|------|---|
|`.zip over 5&nbsp;MB`| Reduza o tamanho do arquivo e tente fazer upload novamente.|
|`.zip corrupt`| Inspecione seu arquivo e tente fazer upload novamente. |
|`Missing HTML`| Adicione o arquivo HTML ao seu arquivo ZIP e tente fazer upload novamente.|
|`Multiple HTML`| Remova um dos arquivos HTML e tente fazer upload novamente.|
|`Images over 5&nbsp;MB`| Reduza o número de imagens e tente fazer upload novamente. |
|`Extra Images`| Pode haver imagens adicionais no seu arquivo que não são referenciadas no arquivo HTML. Isso não causa um erro de falha, mas as imagens extras são descartadas. Se essas imagens deveriam ser referenciadas no arquivo HTML, verifique o conteúdo, corrija quaisquer erros e tente fazer upload novamente.|
|`Missing Images`| Se houver imagens referenciadas no seu arquivo HTML, mas essas imagens não estiverem incluídas na pasta de imagens do arquivo ZIP, você receberá um erro de arquivo. Inspecione seu arquivo e corrija quaisquer erros (como erros de digitação), ou adicione as imagens ausentes ao seu arquivo ZIP e tente fazer upload novamente.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas" }

Observe que, ao baixar os arquivos de Campaigns HTML, etapas do Canvas com mensagens de e-mail ou modelos em uma máquina Windows, o caractere `|` (pipe) não é suportado, então pode ser necessário usar um aplicativo diferente para extrair o conteúdo do download do arquivo ZIP.

## Perguntas frequentes {#frequently-asked-questions}

Para respostas a perguntas frequentes sobre modelos de e-mail, confira nossa página de [perguntas frequentes sobre modelos de e-mail e links]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq).