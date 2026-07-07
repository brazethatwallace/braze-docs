---
nav_title: Roku SDK
article_title: Guia do repositório do Roku SDK
page_order: 8
description: "Referência do README do Braze Roku SDK espelhada do GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guia do repositório do Roku SDK {#roku-sdk-repository-guide}

## Sobre o Braze Roku SDK {#about-the-braze-roku-sdk}

O Braze Roku SDK ajuda você a integrar recursos de envio de mensagens, análise de dados e engajamento de usuários da Braze ao seu aplicativo.

Para começar, consulte os seguintes recursos:

- [Guia do Usuário da Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guia do Desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=roku)

## Integração inicial do SDK {#initial-sdk-integration}

O Braze Roku SDK fornecerá uma API para reportar informações a serem usadas em análise de dados, segmentação e engajamento.

## Etapa 1: Adicionar arquivos {#step-1-add-files}

1. Adicione `BrazeSDK.brs` ao seu app no diretório `source`.
2. Adicione `BrazeTask.brs` e `BrazeTask.xml` ao seu app no diretório `components`.

## Etapa 2: Adicionar referências {#step-2-add-references}

Adicione uma referência a `BrazeSDK.brs` na sua cena principal usando o seguinte elemento `script`:

``` text
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

## Etapa 3: Configurar {#step-3-configure}

Dentro de `main.brs`, defina a configuração da Braze no nó global:

``` text
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = "YOUR_API_KEY_HERE"
config[config_fields.ENDPOINT] = "YOUR_ENDPOINT_HERE (e.g. https://sdk.iad-01.braze.com/)"
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

## Etapa 4: Inicializar Braze {#step-4-initialize-braze}

Inicialize a instância Braze:

``` text
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Configuração de mensagens no app {#in-app-message-setup}

Para processar mensagens no app, você pode adicionar um observador em `BrazeTask.BrazeInAppMessage`:

``` text
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

Dentro do seu manipulador, você tem acesso à mensagem no app de maior prioridade que suas campanhas dispararam:

``` text
in_app_message = m.BrazeTask.BrazeInAppMessage
```

Você pode então decidir o que fazer com a mensagem no app. Alguns dos campos disponíveis:

- `in_app_message.message` - O texto do corpo da mensagem no app
- `in_app_message.buttons` - Lista de botões (pode ser uma lista vazia).
- `in_app_message.id` - ID a ser usado ao registrar impressões ou cliques
- `in_app_message.extras` - Pares de chave/valor
- `in_app_message.image_url` - URL da imagem
- `in_app_message.click_action` - Quando não há botões, esta é a ação que deve ocorrer quando o usuário clica em "OK" quando a mensagem no app é exibida. Pode ser "URI" ou "NONE".
- `in_app_message.dismiss_type` - Pode ser "AUTO_DISMISS" ou "SWIPE"
- `in_app_message.display_delay` - Quanto tempo (em segundos) esperar até exibir a mensagem no app
- `in_app_message.duration` - Por quanto tempo (em milissegundos) a mensagem deve ser exibida quando `dismiss_type` é "AUTO_DISMISS"
- `in_app_message.header` - O texto do cabeçalho da mensagem no app
- `in_app_message.uri` - Quando `click_action` é "URI", este valor deve ser exibido

Também existem vários campos de estilização que você pode optar por usar a partir do dashboard. Alternativamente, você pode implementar a mensagem no app e estilizá-la dentro do seu aplicativo Roku usando uma paleta padrão.
- `in_app_message.bg_color` - Cor de fundo
- `in_app_message.close_button_color` - Cor do botão de fechar
- `in_app_message.frame_color` - A cor da sobreposição da tela de fundo
- `in_app_message.header_text_color` - Cor do texto do cabeçalho
- `in_app_message.message_text_color` - Cor do texto da mensagem
- `in_app_message.text_align` - Pode ser "START", "CENTER" ou "END"

Os campos de botão incluem:
- `buttons[0].click_action` - Pode ser "URI" para indicar a abertura do campo `uri`. Pode ser "NONE" para indicar que este botão deve fechar a mensagem no app.
- `buttons[0].id` - O valor de ID do próprio botão
- `buttons[0].text` - O texto a ser exibido no botão
- `buttons[0].uri` - Quando `click_action` é "URI", este valor deve ser exibido
- `buttons[0].bg_color` - Cor de fundo do botão
- `buttons[0].border_color` - Cor da borda do botão
- `buttons[0].text_color` - Cor do texto do botão

Quando uma mensagem é exibida ou vista, registre uma impressão:

``` text
LogInAppMessageImpression(in_app_message.id, brazetask)
```

Depois que um usuário clica na mensagem, registre um clique:
``` text
LogInAppMessageClick(in_app_message.id, brazetask)
```
e então processe `in_app_message.click_action`

Se o usuário clicar em um botão, registre o clique do botão:

``` text
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```
e então processe `inappmessage.buttons[selected].click_action`

Depois de processar a mensagem no app, você deve limpar o campo:

``` text
m.BrazeTask.BrazeInAppMessage = invalid
```

## Integração básica do SDK concluída {#basic-sdk-integration-complete}

A Braze agora deve estar coletando dados do seu aplicativo. Consulte nossa documentação pública sobre como registrar atributos, eventos e compras no nosso SDK. A cena `MainScene.brs` do nosso app de exemplo também contém exemplos de uso da API.

`BrazeInAppMessage.brs` e `CustomSideBySideInAppMessage.brs` mostram exemplos de tratamento de In-App Messages. `onInAppMessageTriggered()` em `MainScene.brs` mostra como oferecer suporte a múltiplos layouts.

## Referência adicional {#additional-reference}

O diretório `torchietv` contém um app de exemplo com o SDK da Braze integrado.
<!-- END GENERATED README CONTENT -->

Para detalhes do repositório e projetos de exemplo, consulte [https://github.com/braze-inc/braze-roku-sdk](https://github.com/braze-inc/braze-roku-sdk).