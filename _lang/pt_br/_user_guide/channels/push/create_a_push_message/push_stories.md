---
nav_title: "Push Stories"
article_title: "Push Stories"
page_order: 2
page_type: reference
description: "Este artigo de referência aborda o que são Push Stories, como criar uma, além de algumas perguntas frequentes."
channel:
  - Push
---

# Push Stories {#push-stories}

> Push Stories utilizam a funcionalidade de carrossel de fotos popularizada pelo Instagram e Facebook, permitindo que profissionais de marketing criem um carrossel de páginas dentro de uma notificação por push que conta uma história rica e coesa. Essas páginas consistem em uma imagem, ação de clique, título e descrição. Seus usuários podem deslizar por essas páginas e visualizar a história — contada por você.

| Exemplo Android (expandido) | Exemplo iOS (expandido) |
| :-----: | :----------: |
| ![Pré-visualização de Push Stories no Android.]({% image_buster /assets/img_archive/pushstories_android_preview.png %}) | ![Pré-visualização de Push Stories no iOS]({% image_buster /assets/img_archive/pushstories_ios_preview.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push Stories" }

{% alert note %}
Nas versões 3.13.0+ do SDK para iOS, devido a uma mudança na forma como o SDK baixa imagens, uma miniatura da primeira imagem não será exibida na visualização condensada do push. Certifique-se de que o texto da sua mensagem incentive os usuários a expandir o push para ver as imagens.
{% endalert %}

## Pré-requisitos {#prerequisites}

As seguintes versões do SDK são necessárias para receber Push Stories:

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## Como usar Push Stories {#how-to-use-push-stories}

![Menu suspenso do criador de Push Stories]({% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Para usar Push Stories, faça o seguinte:

1. Crie uma [Campaign de push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/).
2. Em **Notification Type**, selecione **Push Stories**.
3. Selecione **iOS** ou **Android**. Observe que, se você selecionar ambos para uma mensagem push, a opção de criar uma Push Story não aparecerá.

### Criador de Push Story {#push-story-composer}

Para criar uma página, siga as etapas a seguir:

1. Selecione **Add new page** no criador principal.
2. Insira uma imagem para cada página, junto com o comportamento de clique para essa imagem.
3. Se desejar, adicione um **Title** e uma **Description** para cada página. Se você usar um título e uma descrição para uma página, eles devem ser inseridos para todas as páginas.

As pré-visualizações serão refletidas e são interativas.

![Criador de Push Stories]({% image_buster /assets/img_archive/pushstories_composer.png %}){: style="max-width:60%"}

{% alert important %}
Se você estiver carregando imagens com [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/#about-connected-content), certifique-se de que a URL da sua imagem comece com `https://`. Usar `http://` causará uma falha no seu app.
{% endalert %}

### Especificações de imagem e texto {#image-and-text-specifications}

As seguintes especificações de imagem e texto se aplicam à parte do carrossel de fotos das Push Stories. Para informações sobre o push básico com o qual os usuários interagem para ativar a Push Story, consulte [Formatos de mensagem e imagem de push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/).

{% tabs %}
{% tab Imagens %}

- **Proporção da imagem:** 2:1 (obrigatória)
- **Tamanho de imagem recomendado:** 500 KB
- **Tamanho máximo da imagem:** 5 MB
- **Tipos de arquivo:** PNG, JPEG

{% endtab %}
{% tab Texto %}

- **Título:** 30 caracteres (recomendado)
- **Descrição:** 30 caracteres (recomendado)

{% alert note %}
Embora possa haver alguma variação no comprimento dos caracteres de dispositivo para dispositivo, o título e a descrição das Push Stories são limitados a uma linha cada. O restante da sua mensagem será truncado. Sempre teste sua mensagem em um dispositivo real.
{% endalert %}

{% endtab %}
{% endtabs %}

### Segmentação de Push Story {#push-story-segmentation}

Ao criar uma Campaign ou Canvas, você pode filtrar quais usuários deseja segmentar com base em se eles clicaram em uma página de Push Story. Em seguida, selecione a Campaign e a página que deseja usar para segmentar seus usuários.

### Análise de dados de Push Stories {#push-stories-analytics}

A análise de dados será muito semelhante à seção de análise de dados atual para notificações por push. Para a análise de dados de Push Stories, você pode abrir a métrica **Aberturas diretas** para visualizar os cliques por página.

![Tabela de desempenho de push no iOS com dados de análise de exemplo e detalhes expandidos para a métrica de aberturas diretas.]({% image_buster /assets/img_archive/pushstories_analytics.png %})

## Solução de problemas {#troubleshooting}

### iOS

#### Enviei uma Push Story para mim, mas não recebi a notificação {#i-sent-myself-a-push-story-but-didnt-receive-the-notification}

A Apple possui regras específicas que impedem o envio de certos tipos de notificações para um dispositivo com base em diversos fatores. Isso inclui a avaliação do plano de dados do cliente, o tamanho da notificação e a capacidade de armazenamento do cliente. Como resultado, às vezes nenhuma notificação será enviada aos seus clientes.

Essas são limitações impostas pela Apple que devem ser consideradas ao projetar sua Push Story.

#### Enviei uma Push Story para mim, mas vi a visualização condensada {#i-sent-myself-a-push-story-but-saw-the-condensed-view-instead}

Em certas situações em que todas as páginas não são carregadas, por exemplo, devido a uma perda de conexão de dados, a Push Story exibirá apenas a notificação condensada.

### Android

#### A Push Story não é dispensada após clicar na imagem {#push-story-doesnt-dismiss-after-clicking-the-image}

Por padrão, as Push Stories não são dispensadas no Android após o usuário clicar na imagem. Se você deseja dispensar a notificação, chame [`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721).