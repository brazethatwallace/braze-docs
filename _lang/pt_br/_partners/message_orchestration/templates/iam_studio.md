---
nav_title: IAM Studio
article_title: IAM Studio
description: "Este artigo de referência descreve a parceria entre a Braze e o IAM Studio, uma plataforma de personalização de mensagens que permite criar experiências ricas e personalizadas no app e entregá-las por meio da Braze."
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# IAM Studio

> O [IAM Studio](https://www.inappmessage.com) é uma plataforma de personalização de mensagens sem código que permite criar experiências no app ricas e personalizadas e entregá-las por meio da Braze.

_Esta integração é mantida pelo IAM Studio._

## Sobre a integração {#about-the-integration}

Com a integração da Braze e do IAM Studio, você pode inserir facilmente modelos de mensagens no app personalizáveis nas suas mensagens no app da Braze, oferecendo substituição de imagem, modificação de texto, configurações de deep link, atributos personalizados e configurações de eventos. Usando o IAM Studio, é possível reduzir o tempo de produção de mensagens e dedicar mais tempo ao planejamento de conteúdo.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do IAM Studio | É necessário ter uma [conta do IAM Studio](https://www.inappmessage.com/register) para aproveitar essa parceria. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

- Incentivar a compra de produtos
- Coleta de informações do usuário
- Aumentar o cadastro de membros
- Informações sobre emissão de cupons

## Integração {#integration}

### Etapa 1: Escolha um modelo {#step-1-choose-a-template}

Escolha um modelo de mensagem no app que você deseja usar na galeria de modelos de mensagens no app.

![A galeria de modelos do IAM Studio mostra diferentes modelos, como "carousel slide modal", "simple icon modal", "modal full image" e muito mais.]({% image_buster /assets/img/iam_studio/iam_template_gallery.png %})

### Etapa 2: Personalize o modelo {#step-2-customize-the-template}

Primeiro, personalize a imagem, o texto e o botão para o seu conteúdo. Certifique-se de conectar o **Deeplink** para a imagem e o botão.

{% tabs local %}
{% tab Image %}
![A interface do IAM Studio mostrando as opções para personalizar a imagem. Essas opções incluem a imagem, o raio da imagem e a imagem esmaecida.]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab Text %}
![A interface do IAM Studio mostrando as opções para personalizar o título e o subtítulo da mensagem. Essas opções incluem texto, formatação e fonte.]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab Button %}
![A interface do IAM Studio mostrando as opções para personalizar os botões principal, esquerdo e direito. Essas opções incluem cor, deep link, texto e formatação.]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

Em seguida, crie sua mensagem personalizada no app adicionando fontes personalizadas e usando Liquid tags. Para ativar o registro e o rastreamento, selecione **Log data and track user behavior**.

{% tabs local %}
{% tab Fonts %}
![A interface do IAM Studio mostrando as opções para adicionar Liquid. Essas opções incluem a criação de frases personalizadas.]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab Liquid %}
![A interface do IAM Studio mostrando as opções para personalizar o registro de eventos/atributos. Essas opções incluem o registro de comportamento do usuário.]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab Logging and Tracking %}
![A interface do IAM Studio mostrando as opções para personalizar a fonte. Essas opções incluem a possibilidade de o usuário personalizar o estilo da fonte.]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png  %})
{% endtab %}
{% endtabs %}

### Etapa 3: Exporte o modelo {#step-3-export-the-template}

Quando toda a edição estiver concluída, exporte o modelo clicando em **Export**. Após a exportação, o código HTML da mensagem no app será gerado. Copie esse código clicando no botão **Copy code**.

![Diálogo de exportação do IAM Studio com o HTML da mensagem no app gerado e a ação de copiar código.]({% image_buster /assets/img/iam_studio/export_iam_code.png %}){: style="max-width:45%;"}

### Etapa 4: Use o código na Braze {#step-4-use-code-in-braze}

Navegue até a Braze e, na sua mensagem no app, cole o código personalizado na caixa **HTML Input**. Certifique-se de testar sua mensagem para verificar se ela está sendo exibida corretamente.

![Editor de Campaign de mensagem no app da Braze com o HTML do IAM Studio colado na caixa HTML Input.]({% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}){: style="max-width:85%;"}