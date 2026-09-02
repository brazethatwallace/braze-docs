---
nav_title: Worthy
article_title: Worthy
description: "Este artigo de referência descreve a parceria entre a Braze e a Worthy, uma plataforma de personalização de mensagens que permite criar experiências ricas e personalizadas no app e entregá-las por meio da Braze."
alias: /partners/worthy/
page_type: partner
search_tag: Partner

---

# Worthy

> A integração entre a [Worthy](https://worthy.ai/) e a Braze permite que você crie experiências ricas e personalizadas no app usando o editor de arrastar e soltar da Worthy e as entregue por meio da Braze. Além disso, a Worthy faz automaticamente o seguinte:

_Essa integração é mantida pela Worthy._

## Sobre a integração {#about-the-integration}

- Criar um servidor de Conteúdo conectado e uma API or interface de programação do aplicativo (API) segura para seu envio de mensagens.
- Construir suas mensagens no app com análise de dados e rastreamento de cliques que aparecerão diretamente na Braze.
- Exportar automaticamente o HTML por meio do editor de arrastar e soltar da Worthy para usar em Campaigns de mensagens no app com **Custom Code** na Braze, com as conexões de API or interface de programação do aplicativo (API) necessárias e o conteúdo dinâmico que você configurar.

## Casos de uso {#use-cases}

- Experiências de boas-vindas personalizadas com base nas seleções de integração do usuário
- Experiências no app para eventos e promoções especiais
- Coleta de feedback e classificações dos clientes com base no comportamento do app
- Testar rapidamente possíveis ideias de produtos de app
- Avisos ricos, notícias e atualizações da comunidade

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta da [Worthy](https://worthy.ai/) | É necessário ter uma conta Worthy para aproveitar essa parceria. |
| SDK or kit de desenvolvimento de software da Braze | Você precisará configurar o SDK or kit de desenvolvimento de software da Braze no seu aplicativo móvel para enviar mensagens avançadas no app. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Crie mensagens personalizadas na Worthy {#step-1-create-personalized-messaging-in-worthy}

Navegue até seu app no dashboard da Worthy, selecione o **Message Creator** e crie uma mensagem personalizada que deseja usar para engajar seus usuários.

### Etapa 2: Crie uma Campaign na Braze {#step-2-create-a-braze-campaign}

Crie uma [Campaign de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/) na Braze e defina o **Message Type** como **Custom Code**.

### Etapa 3: Copie sua mensagem personalizada na Braze {#step-3-copy-your-personalized-message-into-braze}

No criador de mensagens da Worthy, clique em **Export** e selecione **Braze** para exportar sua mensagem personalizada para uso em Campaigns da Braze. Copie o conteúdo exportado para a caixa de texto HTML em **HTML + Asset Zip** no editor de Campaigns da Braze.

É isso aí! Você pode testar imediatamente sua mensagem personalizada usando a guia **Test** no editor de Campaigns da Braze.