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

- Se você está criando uma Campaign, quantas variantes dessa mensagem gostaria de exibir? Para ideias de testes de variantes, confira [Dicas para diferentes canais]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#tips-different-channels).
- Se você está criando um Canvas, essa mensagem será combinada com outros canais de envio de mensagens nessa etapa?
- Quando você gostaria que [sua mensagem expirasse]({{site.baseurl}}/canvas_in-app_messages)?

## Considerações de direcionamento {#targeting-considerations}

- Mensagens no app são ideais para usuários que visitam seu app regularmente. Você está incluindo esse público?
- Onde você quer que seus usuários vejam sua mensagem? No seu app web? No seu app mobile?
- Qual evento deve disparar essa mensagem?
- Algum dos seus usuários está usando versões mais antigas do seu app? Se sim, eles podem não conseguir ver alguns elementos da sua mensagem.
- Para qual tipo de dispositivo ou dispositivos você está criando essa mensagem? Lembre-se de que você pode visualizar sua mensagem usando a caixa de **Prévia** ou a guia **Teste**. Consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) para saber mais.

## Agendamento, postergações e início de sessões {#scheduling-delays-and-session-starts}

Quando uma Campaign de mensagem no app tem **Schedule Delay** com um disparo no início de sessão, um usuário que inicia uma sessão e depois fecha o app antes que a mensagem no app seja exibida ainda pode receber essa mensagem no próximo início de sessão, após a postergação expirar.

Esse comportamento pode produzir exibições inesperadas, especialmente se a opção **Re-evaluate campaign eligibility before displaying** não estiver selecionada na Campaign.

Por exemplo, um usuário pode receber uma mensagem no app com uma postergação de oito segundos um mês após o lançamento da Campaign. Isso pode acontecer se ele iniciou uma sessão, encerrou a sessão imediatamente, iniciou uma nova sessão um mês depois e, oito segundos mais tarde, recebeu a mensagem no app. Se ele sair do app sem fechá-lo, a mensagem no app será exibida quando ele retornar ao app.

## Considerações sobre o conteúdo {#content-considerations}

- Quais idiomas você usará nesta mensagem?
- Qual é o texto do cabeçalho e do corpo? Eles são atraentes e relevantes para o seu usuário?
- As mensagens no app aparecem apenas por um período definido. Seu texto é conciso e memorável?
- Você usará [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) para adicionar textos personalizados?
- Os usuários precisam copiar o texto da mensagem (como um código de desconto ou voucher)? No iOS e no Android, os usuários podem pressionar e segurar o texto ou campos de entrada de texto para copiar o conteúdo. Pressionar e segurar não funciona em imagens, então use texto ou campos de entrada de texto em vez de imagens que contenham códigos ou outros textos que os usuários possam precisar copiar.
- Para mensagens no app em tela cheia, sua imagem ou outra mídia está dentro da [zona segura]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen#image-safe-zone)?
- Para mensagens no app de pesquisa, você deseja registrar atributos ou envios? Você configurou sua página de confirmação?
- Para mensagens no app em HTML personalizado, seu HTML inclui codificação UTF-8 para exibir corretamente caracteres especiais? Consulte [Mensagens no app em HTML personalizado]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#character-encoding) para mais detalhes.
- Se você está incluindo vídeo na sua mensagem no app: embora a Braze não imponha um limite técnico para o tamanho do arquivo de vídeo na reprodução local no dispositivo, lembre-se de que os usuários podem ter conexões lentas, planos de dados caros ou armazenamento limitado. Otimize os arquivos de vídeo para equilibrar qualidade e tamanho do arquivo.

## Considerações sobre conversão {#conversion-considerations}

- Qual é o seu objetivo com essa mensagem? Como você pode representar isso na sua mensagem?
- Os seus botões oferecem opções que fazem sentido para o usuário? Qual é a sua [chamada para ação principal]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#buttons)?
- Você está usando [deep linking para outro conteúdo no app]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content)? Você está usando essa mensagem no app para enviar e aceitar uma [solicitação de permissão ou push priming]({{site.baseurl}}/user_guide/channels/push/best_practices)?
- Você tem uma opção de saída da mensagem? Se não, você pode copiar e colar este snippet para criar um botão rápido:
    ```html
    <a href="appboy://close">X</a>
    ```

## Considerações sobre o editor de arrastar e soltar {#drag-and-drop-editor-considerations}

### Adição de deep links para diferentes dispositivos {#adding-deep-links-for-different-devices}

O editor de arrastar e soltar não oferece suporte à adição de deep links diferentes para dispositivos diferentes (ao contrário do editor tradicional).

### Ajuste da opacidade da imagem de fundo {#adjusting-background-image-opacity}

A configuração de opacidade não permite transparência total das imagens de fundo (ao contrário do editor tradicional de mensagem no app). Você pode usar as configurações de opacidade para tornar a cor de fundo da mensagem completamente transparente.

### Definição da largura máxima {#setting-the-maximum-width}

A largura máxima no editor de arrastar e soltar é limitada a 325px; isso é pensado principalmente para acomodar a prévia do dashboard. As mensagens podem ser exibidas corretamente em dispositivos com telas menores.

### Seleção de fundos diferentes para plataformas diferentes {#selecting-different-backgrounds-for-different-platforms}

Não é possível exibir dois fundos diferentes para a mesma mensagem em plataformas diferentes (como web e mobile).

### Aplicação de estilos de mensagem {#applying-message-styles}

As imagens de fundo se aplicam à mensagem inteira e não podem ser personalizadas por página. Os estilos de mensagem se aplicam à mensagem inteira, não a páginas individuais.

### Medição da altura dos blocos de espaçamento {#measuring-spacer-blocks-height}

A unidade de medida dos blocos de espaçamento é pixels (px) e não pode ser alterada.

### Formatos compatíveis {#supported-formats}

Atualmente, apenas mensagens no app do tipo modal e tela cheia são compatíveis com o editor de arrastar e soltar.

### Ajuste de tamanho e proporção {#adjusting-to-size-and-aspect-ratio}

A imagem de fundo vai esticar a mensagem no app, pois o modal se ajusta ao tamanho e à proporção da imagem de fundo. Você pode ajustar a proporção conforme necessário.

### Imagens de fundo e comportamento ao clicar {#background-images-and-on-click-behavior}

Esses elementos persistem entre as páginas. Para mensagens no app com várias páginas e imagens diferentes em cada página, adicione um botão para permitir que os usuários cliquem para ir à próxima página.