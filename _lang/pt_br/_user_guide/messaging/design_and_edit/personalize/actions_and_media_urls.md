---
nav_title: URLs de ação e mídia
article_title: Personalize URLs de ação e mídia com Liquid
page_order: 2
description: "Este artigo de referência descreve como personalizar URLs de ação e mídia usando Liquid."
---

# Personalize URLs de ação e mídia com Liquid {#personalize-action-and-media-urls-with-liquid}

> Personalize os destinos de links e o conteúdo para cada usuário que recebe sua mensagem adicionando variáveis Liquid às URLs de botões, links, imagens e vídeos.

## Deep link para conteúdo no app {#deep-link-to-in-app-content}

{% alert tip %}
**Para desenvolvedores:** Para um guia sobre como escolher entre esquemas personalizados, links universais e outras opções — incluindo quando você precisa de um arquivo AASA, quais métodos de app delegate implementar e como depurar problemas — consulte o [Guia de deep linking para iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide) e [Solução de problemas de deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).
{% endalert %}

### O que é deep linking? {#what-is-deep-linking}

Deep linking é uma forma de abrir um app nativo e fornecer informações adicionais que instruem o app a executar uma ação específica ou exibir um conteúdo específico.

Existem três partes nesse processo:

1. Identificar qual app abrir.
2. Instruir o app sobre qual ação executar.
3. Fornecer à ação quaisquer dados adicionais necessários.

Deep links são URIs personalizados que direcionam para uma parte específica do app e contêm todas essas três partes. O ponto-chave é definir um esquema personalizado. `http:` é o esquema com o qual quase todos estão familiarizados, mas os esquemas podem começar com qualquer palavra. Um esquema deve começar com uma letra, mas pode conter letras, números, sinais de mais, sinais de menos ou pontos. Na prática, não existe um registro central para evitar conflitos, então é uma boa prática incluir o nome do seu domínio no esquema. Por exemplo, `twitter://` é o URI do iOS para abrir o app móvel do X, antigo Twitter.

Tudo após os dois pontos em um deep link é texto livre. Cabe a você definir sua estrutura e interpretação. No entanto, uma convenção comum é modelá-lo com base em URLs `http:`, incluindo `//` no início e parâmetros de consulta (por exemplo, `?foo=1&bar=2`). No exemplo anterior, `twitter://user?screen_name=[id]` seria usado para abrir um perfil específico no app.

{% alert important %}
Para apps criados com frameworks wrapper (por exemplo, Flutter ou Cordova), a Braze não oferece suporte a deep linking específico para wrappers. Você deve configurar deep links nas camadas nativas do iOS e Android. Para Cordova, consulte [Deep linking em notificações por push]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=cordova).
{% endalert %}

### Tags UTM e atribuição de campanha {#utm-tags-and-campaign-attribution}

#### O que é uma tag UTM? {#what-is-a-utm-tag}

[Tags UTM (Urchin Traffic Manager)](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article) permitem incluir detalhes de atribuição de campanha diretamente nos links. As tags UTM são usadas pelo Google Analytics para coletar dados de atribuição de campanha e podem ser usadas para rastrear as seguintes propriedades:

- `utm_source`: O identificador da origem do tráfego (por exemplo, `my_app`)
- `utm_medium`: O meio da campanha (por exemplo, `newsfeed`)
- `utm_campaign`: O identificador da campanha (por exemplo, `spring_2016_campaign`)
- `utm_term`: Identificador de um termo de pesquisa paga que trouxe o usuário ao seu app ou website (por exemplo, `pizza`)
- `utm_content`: Um identificador para o link ou conteúdo específico em que o usuário clicou (por exemplo, `toplink` ou `android_iam_button2`)

As tags UTM podem ser incorporadas tanto em links HTTP regulares (web) quanto em deep links e rastreadas usando o Google Analytics.

##### Cálculos de tags UTM {#utm-tag-calculations}

A Braze reporta o _Total de Cliques_ para todos os links em uma Campaign ou etapa do Canvas, o que pode incluir links que não possuem tags UTM. Isso significa que você pode ver um resultado diferente (geralmente menor) nos links de rastreamento de campanha do Google Analytics em comparação com o _Total de Cliques_ exibido no desempenho da sua campanha ou no Criador de relatórios.

#### Usando tags UTM com a Braze {#using-utm-tags-with-braze}

Se você deseja usar tags UTM com links HTTP regulares (web) (por exemplo, para fazer atribuição de campanha para suas campanhas de e-mail) e sua organização já usa o Google Analytics, você pode usar o [construtor de URLs do Google](https://ga-dev-tools.google/ga4/campaign-url-builder/) para gerar links UTM. Esses links podem ser facilmente incorporados ao texto da Campaign na Braze, assim como qualquer outro link.

Para usar tags UTM em deep links para o seu app, o app deve ter o [SDK do Google Analytics](https://developers.google.com/analytics/devguides/collection/) relevante integrado e configurado corretamente para lidar com deep links. Consulte seus desenvolvedores se não tiver certeza sobre isso.

Após o SDK do Analytics estar integrado e configurado, as tags UTM podem ser usadas com deep links em Campaigns da Braze. Para configurar tags UTM para sua Campaign, inclua as tags UTM necessárias na URL de destino ou nos deep links. Os exemplos a seguir mostram como usar tags UTM em notificações por push e mensagens no app.

##### Atribuir aberturas de push e cliques em mensagens no app com tags UTM {#attribute-push-opens-and-in-app-message-clicks-with-utm-tags}

{% tabs %}
{% tab Aberturas de push %}

Para incluir tags UTM nos seus deep links para notificações por push, defina o comportamento ao clicar da mensagem push como um deep link e, em seguida, escreva o endereço do deep link e inclua as tags UTM desejadas da seguinte forma:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![Captura de tela relacionada à atribuição de aberturas de push e cliques em mensagens no app com tags UTM.]({% image_buster /assets/img_archive/push_utm_tags.png %})

{% endtab %}
{% tab Cliques em mensagens no app %}

Para incluir tags UTM nos deep links das suas mensagens no app, use o seguinte:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![Captura de tela relacionada à atribuição de aberturas de push e cliques em mensagens no app com tags UTM.]({% image_buster /assets/img_archive/iam_utm_tags.png %})

{% endtab %}
{% endtabs %}

## Use personalização Liquid em URLs {#use-liquid-personalization-in-urls}

Você pode construir dinamicamente sua URL diretamente no criador da Braze, permitindo adicionar parâmetros UTM dinâmicos às suas URLs ou enviar links exclusivos aos usuários (como direcionar usuários ao carrinho abandonado ou a um produto específico que voltou ao estoque).

### Crie uma URL com tags de personalização Liquid compatíveis {#create-a-url-with-supported-liquid-personalization-tags}

URLs podem ser geradas dinamicamente por meio do uso de quaisquer [tags de personalização Liquid compatíveis]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Também oferecemos suporte ao encurtamento de variáveis Liquid personalizadas. Vários exemplos são mostrados na seção a seguir:

### Crie uma URL usando variáveis Liquid {#create-a-url-using-liquid-variables}

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Encurte URLs renderizadas por variáveis Liquid {#shorten-urls-rendered-by-liquid-variables}

**Canais compatíveis:** KakaoTalk, LINE, SMS, RCS, WhatsApp

Encurtamos URLs que são renderizadas por Liquid, incluindo aquelas presentes em propriedades de gatilho de API. Por exemplo, se {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representar uma URL válida, encurtamos e rastreamos essa URL antes de enviar a mensagem.

### Encurte URLs no endpoint `/messages/send` {#shorten-urls-in-messagessend-endpoint}

O encurtamento de links também está ativado para mensagens somente via API por meio do [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages). Para uma lista completa de parâmetros de solicitação, consulte [parâmetros de solicitação]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters).

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `link_shortening_enabled` | Sim | Booleano | Defina `link_shortening_enabled` como `true` para ativar o encurtamento de links. Para usar o rastreamento, um `campaign_id` e um `message_variation_id` devem estar presentes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Encurtar URLs no endpoint /messages/send" }