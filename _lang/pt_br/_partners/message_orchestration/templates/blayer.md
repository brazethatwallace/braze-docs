---
nav_title: B.Layer
article_title: B.Layer
description: "Este artigo de referência descreve a parceria entre a Braze e o B.Layer, um construtor de mensagens no app, que você pode usar para criar mensagens no app com design personalizado de forma simples, rápida e sem codificação."
alias: /partners/blayer-inapps/
page_type: partner
search_tag: Partner

---

# B.Layer

> O [B.Layer](https://blayer.phiture.com) é o criador de mensagens no app da Phiture que ajuda as equipes de CRM dos aplicativos móveis a criar mensagens no app personalizadas de forma simples, rápida e sem escrever código.

_Essa integração é mantida pelo B.Layer._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e o B.Layer permite que você use o construtor de mensagens no app B.Layer para ajudá-lo a criar mensagens no app com a sua marca, que podem ser exportadas como um arquivo zip ou HTML em linha para a Braze. Essa integração não exige recursos adicionais de desenvolvimento, o que economiza tempo e orçamento.

![Interface do construtor B.Layer com prévia de uma mensagem no app com marca.]({% image_buster /assets/img/blayer/blayer2.png %})

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta B.Layer | É necessário ter uma conta do [B.Layer](https://blayer.phiture.com) para aproveitar essa parceria. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

Com o B.Layer, há inúmeras oportunidades para criar e experimentar, incluindo controles deslizantes de recomendação do produto, integração ou pesquisas em várias telas, NPS, captura de e-mail, ofertas especiais e muito mais.

Eles estão trabalhando com marcas como Lifesum, Blinkist, OnX Hunt e muitas outras para ajudar a melhorar a experiência do usuário sem recursos adicionais. Também estamos entre os finalistas do APS Awards 2022 na categoria de inovação de app.

## Integração {#integration}

### Etapa 1: Crie sua mensagem no app {#step-1-create-your-in-app-message}

#### Definir cores e fontes da marca {#set-brand-colors-and-fonts}

No B.Layer, no menu de hambúrguer na parte superior da página, clique em **Brand assets > add your brand assets**. Aqui, você pode atribuir a cor e as fontes da sua marca.
Está tudo pronto. Agora você pode começar a criar sua mensagem no app.

![Tela de ativos de marca do B.Layer para configurar cores e fontes.]({% image_buster /assets/img/blayer/blayer4.png %})

#### Crie sua mensagem no app {#design-your-in-app-message}

Para criar sua mensagem no app, selecione uma única mensagem no app. Em seguida, estilize sua mensagem e adicione os componentes necessários. Cada componente pode ser ajustado.

![Editor de mensagens do B.Layer com componentes e controles de estilo.]({% image_buster /assets/img/blayer/blayer5.png %})

### Baixe sua mensagem no app {#download-your-in-app-message}

Quando terminar, baixe sua mensagem. Sua mensagem pode ser baixada como ZIP ou HTML em linha.

### Etapa 2: Adicionar o código personalizado B.Layer {#step-2-add-blayer-custom-code}

Na Braze, crie uma mensagem no app com código personalizado. Se você tiver um arquivo ZIP, arraste-o e solte-o na caixa de upload nesta seção. Se tiver um arquivo HTML em linha, cole o conteúdo na seção de HTML.

![Editor de mensagem no app com código personalizado da Braze com conteúdo exportado do B.Layer.]({% image_buster /assets/img/blayer/blayer6.png %})

## Rastreamento de botões {#button-tracking}

Com o B.Layer, é possível registrar interações de botões ou entrada de texto como um atributo da Braze. Isso pode ser feito no editor. Um exemplo popular é uma pesquisa NPS.

O B.Layer usa o rastreamento de botões da Braze adicionado aos links que você insere (por exemplo, `?button=0`). Dessa forma, você pode ver os cliques no botão na parte de análise de dados da sua Campaign.