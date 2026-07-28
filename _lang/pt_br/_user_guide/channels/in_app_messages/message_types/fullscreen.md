---
nav_title: "Tela inteira"
article_title: Mensagens no app em tela inteira
description: "Este artigo de referência aborda os requisitos de mensagem e design das mensagens no app em tela inteira."
page_type: reference
page_order: 1
channel:
  - in-app messages
tool:
  - Media

---

# Mensagens no app em tela inteira {#fullscreen-in-app-messages}

> As mensagens em tela inteira ocupam toda a tela do dispositivo! Esse tipo de mensagem é ideal quando você realmente precisa da atenção do usuário, como para atualizações obrigatórias do app.

Esse tipo de mensagem está disponível tanto no [editor de arrastar e soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) quanto no [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

{% tabs %}
{% tab Retrato %}

![Duas mensagens no app em tela inteira lado a lado na orientação retrato, detalhando as recomendações de imagem e texto. Consulte as seções a seguir para mais informações.]({% image_buster /assets/img/full-screen-spec.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Paisagem %}

![Duas mensagens no app em tela inteira lado a lado na orientação paisagem, detalhando as recomendações de imagem e texto. Consulte as seções a seguir para mais informações.]({% image_buster /assets/img/full-screen-spec-landscape.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

## Imagens {#images}

As mensagens no app em tela inteira preenchem toda a altura do dispositivo e cortam horizontalmente (lados esquerdo e direito) conforme necessário. Mensagens em tela inteira com imagem e texto preenchem 50% da altura do dispositivo. Todas as mensagens no app em tela inteira preenchem a barra de status em dispositivos com "notch".

{% multi_lang_include in-app_messages/image_requirements.md %}

{% alert tip %} Crie ativos com confiança! Nossos modelos de imagem para mensagens no app e sobreposições de zona segura foram projetados para funcionar bem em dispositivos de todos os tamanhos. [Baixar ZIP de modelos de design]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

### Retrato {#portrait}

| Disposição | Tamanho do ativo | Notas |
|--- | --- | --- |
| Imagem e texto | Proporção 6:5<br> Alta resolução 1200 x 1000&nbsp;px<br> Mínimo 600 x 500&nbsp;px | O corte pode ocorrer em todos os lados, mas a imagem sempre preencherá os 50% superiores da viewport |
| Somente imagem | Proporção 3:5<br> Alta resolução 1200 x 2000&nbsp;px<br> Mínimo 600 x 1000&nbsp;px | O corte pode ocorrer nas bordas principal e direita em dispositivos mais altos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Retrato" }

### Paisagem {#landscape}

| Disposição | Tamanho do ativo | Notas |
|--- | --- | --- |
| Imagem e texto | Proporção 10:3<br> Alta resolução 2000 x 600px<br> Mínimo 1000 x 300&nbsp;px | O corte pode ocorrer em todos os lados, mas a imagem sempre preencherá os 50% superiores da viewport |
| Somente imagem | Proporção 5:3<br> Alta resolução 2000 x 1200px<br> Mínimo 1000 x 600&nbsp;px | O corte pode ocorrer nas bordas principal e direita em dispositivos mais altos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paisagem" }

### Zona segura da imagem {#image-safe-zone}

Ao pré-visualizar uma mensagem no app em tela inteira na plataforma da Braze, você pode ativar a zona segura da imagem para a área da mensagem que está protegida contra cortes quando exibida em diferentes dispositivos. Além de testar a zona segura da imagem no painel de pré-visualização, recomendamos que você sempre [teste sua mensagem]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message).

![Prévia de uma mensagem no app na Braze com "Mostrar zona segura da imagem" ativado. A zona segura da imagem é uma sobreposição sobre a imagem que mostra quais partes da imagem estarão protegidas contra cortes.]({% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %})

## Telas maiores {#larger-screens}

Em um tablet ou navegador de desktop, uma mensagem no app em tela inteira ficará centralizada na tela do app, conforme mostrado na captura de tela a seguir.

{% tabs %}
{% tab Retrato %}

![Mensagem no app em tela inteira como apareceria em uma tela grande na orientação retrato. A mensagem aparece como um modal grande centralizado na tela.]({% image_buster /assets/img/full-screen-large-viewport.png %}){: style="border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Paisagem %}

![Mensagem no app em tela inteira como apareceria em uma tela grande na orientação paisagem. A mensagem aparece como um modal grande centralizado na tela.]({% image_buster /assets/img/full-screen-large-viewport-landscape.png %}){: style="max-width:80%;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}