---
nav_title: Guia de preparação
article_title: Guia de preparação para mensagens no app
page_order: 0.5

page_type: reference
description: "Este artigo aborda perguntas e práticas recomendadas a serem consideradas antes de criar mensagens no app, incluindo direcionamento, agendamento, conteúdo, desempenho e conversões."
channel: in-app messages
toc_headers: h2
---

# Guia de preparação para mensagens no app {#in-app-message-prep-guide}

> Antes de criar suas mensagens no app, considere os tópicos a seguir para tornar o processo mais eficiente.

## Considerações gerais {#general-considerations}

- Se você está criando uma Campaign, quantas variantes dessa mensagem gostaria de exibir? Para ideias de testes de variantes, confira [Dicas para diferentes canais]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#tips-different-channels).
- Se você está criando um Canvas, essa mensagem será combinada com outros canais de envio de mensagens nessa etapa?
- Quando você gostaria que [sua mensagem expirasse]({{site.baseurl}}/canvas_in-app_messages)?

## Considerações de direcionamento {#targeting-considerations}

- Mensagens no app são ideais para usuários que visitam seu app regularmente. Você está incluindo esse público?
- Onde você quer que seus usuários vejam sua mensagem? No seu app web? No seu app móvel?
- Qual evento deve disparar essa mensagem?
- Algum dos seus usuários está usando versões mais antigas do seu app? Se sim, eles podem não conseguir ver alguns elementos da sua mensagem.
- Para qual tipo de dispositivo ou dispositivos você está criando essa mensagem? Lembre-se de que você pode visualizar sua mensagem usando a caixa de **Prévia** ou a guia **Teste**. Consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) para saber mais.

## Agendamento, postergações e início de sessão {#scheduling-delays-and-session-starts}

Quando uma campanha de mensagem no app tem **Postergação de Cronograma** com um disparo no início de sessão, um usuário que inicia uma sessão e fecha o app antes que a mensagem no app seja exibida ainda pode receber essa mensagem no próximo início de sessão, após a postergação expirar.

Campanhas de mensagem no app podem postergar a entrega após o disparo por até duas horas. Para uma espera mais longa, adicione uma etapa de [Postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) antes de uma etapa de mensagem no app em um Canvas. Para configuração de postergação, consulte [Entrega baseada em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-2-select-delay-length).

Esse comportamento de temporização pode produzir uma exibição inesperada, especialmente se a opção **Reavaliar a elegibilidade da campanha antes de exibir** não estiver selecionada na campanha.

Por exemplo, um usuário pode receber uma mensagem no app com uma postergação de oito segundos um mês após o lançamento da campanha. Isso pode acontecer se ele iniciou uma sessão, encerrou a sessão imediatamente, iniciou uma sessão um mês depois e, oito segundos mais tarde, recebeu a mensagem no app. Se ele navegar para fora do app sem fechá-lo, a mensagem no app será exibida quando ele retornar ao app.

## Considerações sobre o conteúdo {#content-considerations}

- Quais idiomas você usará nesta mensagem?
- Qual é o texto do cabeçalho e do corpo? Eles são atraentes e relevantes para o seu usuário?
- As mensagens no app aparecem apenas por um período determinado. Seu texto é conciso e memorável?
- Você usará [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) para adicionar textos personalizados?
- Os usuários precisam copiar o texto da mensagem (como um código de desconto ou voucher)? No iOS e Android, os usuários podem manter o texto ou campos de entrada de texto pressionados para copiar o conteúdo. Manter pressionado não funciona em imagens, então use texto ou campos de entrada de texto em vez de imagens que contenham códigos ou outros conteúdos que os usuários possam precisar copiar.
- Para mensagens no app em tela cheia, sua imagem ou outra mídia está dentro da [zona segura]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen#image-safe-zone)?
- Para mensagens no app de pesquisa, você deseja registrar atributos ou envios? Você configurou sua página de confirmação?
- Para mensagens no app com HTML personalizado, seu HTML inclui codificação UTF-8 para exibir corretamente caracteres especiais? Consulte [Mensagens no app com HTML personalizado]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#character-encoding) para mais detalhes.
- Se você está incluindo vídeo na sua mensagem no app: embora a Braze não imponha um limite técnico para o tamanho do arquivo de vídeo para reprodução local no dispositivo, lembre-se de que os usuários podem ter conexões lentas, planos de dados caros ou armazenamento limitado. Otimize os arquivos de vídeo para equilibrar qualidade e tamanho do arquivo.

## Otimizar o desempenho de mensagens no app {#optimize-in-app-message-performance}

A Braze entrega os disparos de mensagens no app elegíveis ao usuário no início da sessão. Preparar muitas mensagens com Liquid pode atrasar o início da sessão e afetar o desempenho do app.

Se esse trabalho levar mais do que alguns segundos, a Braze pode adiar a renderização Liquid restante. Cada mensagem é então renderizada quando disparada e buscada sob demanda. Essa [entrega com modelo]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages) protege seus usuários de um desempenho ruim do app causado pelo aumento da latência de resposta.

Use estas práticas recomendadas para acelerar a entrega das suas mensagens:

- Direcione apenas usuários que podem executar o disparo da Campaign. Um direcionamento muito amplo pode fazer com que usuários recebam um disparo de mensagem no app que nunca conseguirão ativar. Por exemplo, uma mensagem no app disparada por uma Campaign de push específica pode ter seu escopo reduzido para usar o mesmo público-alvo. Isso pode ser aplicado de forma similar a outros tipos de Campaign, Canvas, eventos personalizados que só podem ser disparados por determinados usuários, e mais.
- Defina uma data de término para Campaigns com prazo definido. Interrompa Campaigns quando você não espera mais que elas recebam impressões.
- Evite inserir folhas de estilo estáticas grandes, scripts ou ativos de mídia codificados em base64 diretamente na mensagem ou por meio de um bloco de conteúdo. Use a [biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) para ajudar a reduzir o tempo gasto na renderização da sua mensagem.
- Reduza lógicas Liquid complexas com ramificações ou loops.
- Ative a reelegibilidade apenas quando os usuários devem receber uma mensagem várias vezes. Se a reelegibilidade estiver desativada, a Braze para de entregar o disparo de mensagem no app após o usuário visualizá-la. Para saber mais, consulte [Reelegibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).
- Dê uma prioridade mais alta a Campaigns importantes. A Braze renderiza primeiro as mensagens elegíveis de maior prioridade, tornando a entrega com modelo menos provável quando um usuário se qualifica para muitas Campaigns. Para saber mais, consulte [Escolher uma prioridade]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority).

### Separar código estático e ativos {#separate-static-code-and-assets}

Mantenha valores personalizados e regras condicionais na mensagem. Hospede CSS, JavaScript e ativos de mídia reutilizáveis na [biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) e então crie links para eles.

Isso não precisa ser feito para todos os scripts e estilos. É útil principalmente para reduzir o excesso de ativos grandes, como estilos de marca compartilhados e scripts complexos, como widgets interativos.

Folhas de estilo e scripts da biblioteca de mídia não avaliam Liquid, permitindo que o dispositivo do usuário os armazene em cache. O exemplo a seguir mantém valores dinâmicos inline e carrega código reutilizável de arquivos estáticos:

{% raw %}

```liquid
<head>
  <style>
    /* Select a hero image URL based on the user's subscription tier. */
    {% capture hero_image_url %}
      {% if custom_attribute.${subscription_tier} == 'premium' %}
        https://braze-images.com/path/to/premium/hero.jpg
      {% else %}
        https://braze-images.com/path/to/standard/hero.jpg
      {% endif %}
    {% endcapture %}
    /* Assigning to a CSS variable so it can be used inside our stylesheet. */
    :root {
      --hero-image: url("{{ hero_image_url | url_escape }}");
    }
  </style>
  <script>
    // Assigning to the global window object so the value can be referenced in our script.
    window.brandConfig = {
      subscriptionTier: "{{custom_attribute.${subscription_tier} | json_escape }}"
    };
  </script>
  <!-- Linking to a stylesheet from the Braze media library. -->
  <link rel="stylesheet" href="https://braze-images.com/path/to/media/library/asset.css">
  <!-- Linking to a script from the Braze media library. -->
  <script src="https://braze-images.com/path/to/other/media/library/asset.js" defer></script>
</head>

<body>
  <div class="hero"></div>
  <div class="user-styles" data-subscription-tier="{{custom_attribute.${subscription_tier} | escape}}">
    ...
  </div>
</body>
```

{% endraw %}

A folha de estilo da biblioteca de mídia pode referenciar as variáveis CSS e definir outros estilos reutilizáveis:

```css
.hero {
  background-image: var(--hero-image);
}

.user-styles {
  /* styles for all users */
}

.user-styles[data-subscription-tier="premium"] {
  /* premium subscription tier user styles, color scheme, etc */
}

.user-styles[data-subscription-tier="standard"] {
  /* standard subscription tier user styles, color scheme, etc */
}
```

O script da biblioteca de mídia pode usar as variáveis JavaScript inline para adicionar comportamentos reutilizáveis:

```javascript
const config = window.brandConfig || {};

if (config.subscriptionTier === "standard") {
  // add some sort of logic to show a "subscribe to premium" button
} else if (config.subscriptionTier === "premium") {
  // thank the user for being a premium user
}
```

## Considerações sobre conversão {#conversion-considerations}

- Qual é o seu objetivo com esta mensagem? Como você pode representar isso na sua mensagem?
- Seus botões oferecem opções que fazem sentido para o usuário? Qual é a sua [chamada para ação principal]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#buttons)?
- Você está usando [deep linking para conteúdo no app]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content)? Você está usando essa mensagem no app para enviar e aceitar uma [solicitação de permissão ou push priming]({{site.baseurl}}/user_guide/channels/push/best_practices)?
- Você tem uma opção de saída da mensagem? Se não, você sempre pode copiar e colar este snippet para criar um botão rápido:
  ```html
  <a href="appboy://close">X</a>
  ```

## Considerações sobre o editor de arrastar e soltar {#drag-and-drop-editor-considerations}

### Adição de deep links para diferentes dispositivos {#adding-deep-links-for-different-devices}

O editor de arrastar e soltar não oferece suporte à adição de deep links diferentes para dispositivos diferentes (ao contrário do editor tradicional).

### Ajuste da opacidade da imagem de fundo {#adjusting-background-image-opacity}

A configuração de opacidade não permite transparência total das imagens de fundo (ao contrário do editor tradicional de mensagens no app). Você pode usar as configurações de opacidade para tornar a cor de fundo da mensagem completamente transparente.

### Definição da largura máxima {#setting-the-maximum-width}

A largura máxima no editor de arrastar e soltar é limitada a 325px; isso serve principalmente para acomodar a prévia do dashboard. As mensagens podem ser exibidas corretamente em dispositivos com telas menores.

### Seleção de fundos diferentes para plataformas diferentes {#selecting-different-backgrounds-for-different-platforms}

Não é possível exibir dois fundos diferentes para a mesma mensagem em plataformas diferentes (como web e dispositivos móveis).

### Aplicação de estilos de mensagem {#applying-message-styles}

As imagens de fundo são aplicadas à mensagem inteira e não podem ser personalizadas por página. Os estilos de mensagem são aplicados à mensagem inteira, não a páginas individuais.

### Medição da altura dos blocos de espaçamento {#measuring-spacer-blocks-height}

A unidade de medida dos blocos de espaçamento é pixels (px) e não pode ser alterada.

### Formatos compatíveis {#supported-formats}

Atualmente, apenas mensagens no app em formato modal e tela cheia são compatíveis com o editor de arrastar e soltar.

### Ajuste de tamanho e proporção {#adjusting-to-size-and-aspect-ratio}

A imagem de fundo vai esticar a mensagem no app, pois o modal se ajusta ao tamanho e à proporção da imagem de fundo; você pode ajustar a proporção conforme necessário.

### Imagens de fundo e comportamento ao clicar {#background-images-and-on-click-behavior}

Esses elementos persistem entre as páginas. Para mensagens no app com várias páginas e imagens inteiras diferentes em cada página, adicione um botão para permitir que os usuários cliquem para ir à próxima página.