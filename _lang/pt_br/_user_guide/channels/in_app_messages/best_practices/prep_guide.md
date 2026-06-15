---
nav_title: Guia de preparação
article_title: Guia de preparação para mensagens no app
page_order: 0.5

page_type: reference
description: "Este artigo aborda perguntas e práticas recomendadas a serem consideradas antes de criar mensagens no app, incluindo direcionamento, agendamento, conteúdo e conversões."
channel: in-app messages
toc_headers: h2
---

# Guia de preparação para mensagens no app {#in-app-message-prep-guide}

> Antes de criar suas mensagens no app, considere alguns dos tópicos a seguir para que a criação da sua mensagem seja rápida e fácil.

## Considerações gerais {#general-considerations}

- Se você está criando uma Campaign, quantas variantes dessa mensagem gostaria de exibir? Para ideias de testes de variantes, confira [Dicas para diferentes canais]({{site.baseurl}}/user_guide/messaging/ab_testing/#tips-different-channels).
- Se você está criando um Canvas, essa mensagem será combinada com outros canais de envio de mensagens nessa etapa?
- Quando você gostaria que [sua mensagem expirasse]({{site.baseurl}}/canvas_in-app_messages/)?

## Considerações de direcionamento {#targeting-considerations}

- Mensagens no app são ideais para usuários que visitam seu app regularmente. Você está incluindo esse público?
- Onde você quer que seus usuários vejam sua mensagem? No seu app web? No seu app mobile?
- Qual evento deve acionar essa mensagem?
- Algum dos seus usuários está usando versões mais antigas do seu app? Se sim, eles podem não conseguir ver alguns elementos da sua mensagem.
- Para qual tipo de dispositivo ou dispositivos você está criando essa mensagem? Lembre-se de que você pode pré-visualizar sua mensagem usando a caixa **Preview** ou a guia **Test**. Consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=in-app%20message) para mais informações.

## Agendamento, postergações e início de sessão {#scheduling-delays-and-session-starts}

Quando uma Campaign de mensagem no app tem **Agendar postergação** com um gatilho no início de sessão, um usuário que inicia uma sessão e depois fecha o app antes que a mensagem no app seja exibida ainda pode receber essa mensagem no próximo início de sessão, após a postergação expirar.

Esse comportamento de tempo pode produzir exibições inesperadas, especialmente se **Reavaliar a elegibilidade da campanha antes de exibir** não estiver selecionado na Campaign.

Por exemplo, um usuário pode receber uma mensagem no app com uma postergação de oito segundos um mês após o lançamento da Campaign. Isso pode acontecer se ele iniciou uma sessão, encerrou a sessão imediatamente, iniciou uma sessão um mês depois e, oito segundos depois, recebeu a mensagem no app. Se ele navegar para fora do app sem fechá-lo, a mensagem no app será exibida quando ele retornar ao app.

## Considerações de conteúdo {#content-considerations}

- Quais idiomas você usará nessa mensagem?
- Qual é o texto do cabeçalho e do corpo? Eles são chamativos e relevantes para o seu usuário?
- Mensagens no app aparecem apenas por um período definido. Seu texto é conciso e memorável?
- Você usará [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/) para adicionar texto personalizado?
- Para mensagens no app em tela cheia, sua imagem ou outra mídia está dentro da [zona segura]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen/#image-safe-zone)?
- Para mensagens no app de pesquisa, você deseja registrar atributos ou envios? Você configurou sua página de confirmação?

## Considerações de conversão {#conversion-considerations}

- Qual é o seu objetivo com essa mensagem? Como você pode representar isso na sua mensagem?
- Seus botões oferecem opções que fazem sentido para o seu usuário? Qual é a sua [chamada para ação principal]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/#buttons)?
- Você está usando [deep linking para outro conteúdo no app]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/#deep-link-to-in-app-content)? Você está usando essa mensagem no app para enviar e aceitar uma [solicitação de permissão ou push priming]({{site.baseurl}}/user_guide/channels/push/best_practices/)?
- Você tem uma opção de saída da mensagem? Se não, você sempre pode copiar e colar este trecho para criar um botão rápido:
    ```html
    <a href="appboy://close">X</a>
    ```

## Considerações do editor de arrastar e soltar {#drag-and-drop-editor-considerations}

### Adicionar deep links para diferentes dispositivos {#adding-deep-links-for-different-devices}

O editor de arrastar e soltar não suporta a adição de deep links diferentes para dispositivos diferentes (diferentemente do editor tradicional).

### Ajustar a opacidade da imagem de fundo {#adjusting-background-image-opacity}

A configuração de opacidade não permite transparência completa das imagens de fundo (diferentemente do editor tradicional de mensagens no app). Você pode usar as configurações de opacidade para tornar a cor de fundo da mensagem completamente transparente.

### Definir a largura máxima {#setting-the-maximum-width}

A largura máxima no editor de arrastar e soltar é limitada a 325px; isso é destinado principalmente para acomodar a pré-visualização do dashboard. As mensagens podem ser exibidas corretamente em dispositivos com telas menores.

### Selecionar fundos diferentes para plataformas diferentes {#selecting-different-backgrounds-for-different-platforms}

Não é possível exibir dois fundos diferentes para a mesma mensagem em plataformas diferentes (como web e mobile).

### Aplicar estilos de mensagem {#applying-message-styles}

As imagens de fundo se aplicam à mensagem inteira e não podem ser personalizadas por página. Os estilos de mensagem se aplicam à mensagem inteira, não a páginas individuais.

### Medir a altura dos blocos de espaçamento {#measuring-spacer-blocks-height}

A unidade de medida para blocos de espaçamento é pixels (px) e não pode ser alterada.

### Formatos suportados {#supported-formats}

Atualmente, apenas mensagens no app modais e em tela cheia são suportadas no editor de arrastar e soltar.

### Ajustar ao tamanho e proporção {#adjusting-to-size-and-aspect-ratio}

A imagem de fundo vai esticar a mensagem no app, pois o modal se ajusta ao tamanho e à proporção da imagem de fundo; você pode ajustar a proporção conforme necessário.

### Imagens de fundo e comportamento ao clicar {#background-images-and-on-click-behavior}

Esses persistem entre as páginas. Para mensagens no app de várias páginas com imagens completas diferentes em cada página, adicione um botão para permitir que os usuários cliquem para ir à próxima página.