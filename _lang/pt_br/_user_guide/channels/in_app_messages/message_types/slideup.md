---
nav_title: Slideup
article_title: Mensagens no app slideup
page_order: 3
channel:
  - in-app messages
tool:
  - Media
description: "Este artigo de referência aborda os requisitos de mensagem e design das mensagens no app do tipo slideup."

---

# Mensagens no app slideup {#slideup-in-app-messages}

> Nossos slideups geralmente aparecem na parte superior ou inferior da tela do app (você pode definir isso ao criar sua mensagem). Eles são ótimos para alertar seus usuários sobre novos termos de serviço, cookies e outros trechos de informação. São discretos e permitem que seus usuários continuem interagindo com o app enquanto a mensagem é exibida.

Esse tipo de mensagem está disponível no [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/).

![Duas mensagens no app do tipo slideup, uma aparecendo na parte superior da tela e outra na parte inferior, detalhando as recomendações de imagem e texto. Consulte as seções a seguir para mais informações.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width: 40%; border: none;"}

## Comportamento de imagem e texto {#image-and-copy-behavior}

As mensagens slideup podem conter até três linhas de texto antes de serem truncadas com reticências. As imagens nos slideups nunca serão cortadas ou recortadas — elas sempre serão redimensionadas para caber no contêiner de imagem de 50 x 50 pixels.

- Todas as imagens devem ter menos de 5&nbsp;MB.
- Aceitamos apenas os formatos PNG, JPEG e GIF.
- Recomendamos que suas imagens tenham 500&nbsp;KB.

{% alert tip %} Crie ativos com confiança! Nossos modelos de imagem para mensagens no app e sobreposições de zona segura foram projetados para funcionar bem em dispositivos de todos os tamanhos. [Baixar ZIP de modelos de design]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Disposição | Tamanho do ativo | Notas |
|--- | --- | --- |
| Imagem + Texto | Proporção 1:1<br>Alta resolução 150 x 150&nbsp;px<br> Mínimo 50 x 50&nbsp;px | Imagens de diversas proporções se ajustarão a um contêiner de imagem quadrado, sem cortes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comportamento de imagem e texto" }

Você deve sempre [pré-visualizar e testar suas mensagens]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=in-app%20message) em diversos dispositivos para garantir que as áreas mais importantes da sua imagem e mensagem apareçam conforme esperado. Observe que, ao pré-visualizar sua mensagem no criador, a renderização real nos dispositivos pode ser diferente.

## Hiperlinks e texto âncora {#hyperlinks-and-anchor-text}

Para adicionar um link em um slideup, insira o texto da mensagem no campo **Corpo** e defina o destino em **Comportamento ao clicar** (por exemplo, **Redirecionar para URL**). Quando o **Comportamento ao clicar** está configurado, toques em qualquer lugar da mensagem, exceto no controle de fechar, acionam essa ação.

Para mensagens no app em HTML personalizado, você pode usar links HTML diretamente. Consulte [Mensagens no app em HTML personalizado]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/).

## Dispositivos móveis {#mobile-devices}

Em dispositivos móveis, os slideups aparecem na parte superior ou inferior da tela do app. Você pode especificar isso ao criar sua mensagem. Os usuários podem deslizar para dispensar o slideup ou tocar para abri-lo se uma ação de clique estiver incluída. Se uma ação de clique for adicionada ao slideup, um ícone de seta ">" será exibido.

## Telas maiores {#larger-screens}

{% tabs %}
{% tab Desktop %}

Em um navegador desktop, uma mensagem no app do tipo slideup aparecerá no canto da tela, conforme mostrado na captura de tela a seguir (a menos que seja configurado de outra forma ao criar a mensagem no app). Os usuários podem clicar no botão de fechar "X" para dispensar o slideup.

![Mensagem no app do tipo slideup como aparece em um navegador desktop. A mensagem aparece no canto inferior direito da tela e não ocupa toda a largura da tela.]({% image_buster /assets/img/slideup-large-viewport.png %}){: style="border: none;"}

{% endtab %}
{% tab Tablet %}

Em um tablet, uma mensagem no app do tipo slideup aparece na parte inferior da tela. Assim como em dispositivos móveis, os usuários podem deslizar para dispensar o slideup ou tocar para abri-lo se uma ação de clique estiver incluída. Se uma ação de clique for adicionada ao slideup, um ícone de seta ">" será exibido. O botão de fechar "X" não é exibido por padrão.

![Mensagem no app do tipo slideup como aparece em uma tela de tablet. A mensagem aparece na parte inferior central da tela e não ocupa toda a largura da tela.]({% image_buster /assets/img/slideup-tablet.png %}){: style="border: none;"}

{% endtab %}
{% endtabs %}