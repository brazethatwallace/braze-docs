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
**Para desenvolvedores:** Para instruções de integração, consulte [Deep linking no Android]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=android) ou [Deep linking no Swift]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift). Para ajuda na escolha de um tipo de link no iOS, consulte o [guia de deep linking no iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide). Para diagnosticar problemas, consulte [Solução de problemas de deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).
{% endalert %}

### O que é deep linking? {#what-is-deep-linking}

Deep linking é uma forma de abrir um app nativo e fornecer informações adicionais que orientam o app a executar uma ação específica ou exibir um conteúdo específico.

Existem três partes nesse processo:

1. Identificar qual app abrir.
2. Instruir o app sobre qual ação executar.
3. Fornecer à ação os dados adicionais necessários.

Deep links são URIs personalizados que direcionam para uma parte específica do app e contêm todas essas três partes. O ponto-chave é definir um esquema personalizado. `http:` é o esquema com o qual quase todos estão familiarizados, mas os esquemas podem começar com qualquer palavra. Um esquema deve começar com uma letra, mas pode conter letras, números, sinais de mais, sinais de menos ou pontos. Na prática, não existe um registro central para evitar conflitos, então é uma boa prática incluir o nome do seu domínio no esquema. Por exemplo, `twitter://` é o URI do iOS para abrir o app móvel do X, antigo Twitter.

Tudo após os dois-pontos em um deep link é texto livre. Você define a estrutura e a interpretação. No entanto, uma convenção comum é seguir o modelo de URLs `http:`, incluindo `//` no início e parâmetros de consulta (por exemplo, `?foo=1&bar=2`). No exemplo anterior, `twitter://user?screen_name=[id]` seria usado para abrir um perfil específico no app.

{% alert important %}
Para apps criados com frameworks wrapper (por exemplo, Flutter ou Cordova), a Braze não oferece suporte a deep linking específico para wrappers. Você deve configurar deep links nas camadas nativas do iOS e Android. Para Cordova, consulte [Deep linking em notificações por push]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=cordova).
{% endalert %}

### Esquemas de URI do sistema {#system-uri-schemes}

Esquemas de URI padrão tratados nativamente pelo iOS e Android (como `tel:`, `mailto:` e `sms:`) podem ser inseridos diretamente no campo de URL do deep link sem a necessidade de uma integração personalizada de deep link no seu app.

| Esquema | Exemplo | Ação |
| ------ | ------- | ------ |
| `tel:` | `tel:+18005555555` | Abre o discador do telefone |
| `mailto:` | `mailto:support@example.com` | Abre o compositor de e-mail |
| `sms:` | `sms:+18005555555` | Abre o compositor de SMS |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Esquemas de URI do sistema"}

Esses esquemas funcionam para comportamentos ao clicar em notificações por push e ações de botões de mensagens no app. Nenhuma configuração adicional do SDK or kit de desenvolvimento de software ou alteração no código do app é necessária.

### Deep link para o aplicativo {#deep-link-into-application}

Ao criar notificações por push, mensagens no app, Banners ou Content Cards, selecione **Deeplink into application** para abrir uma tela ou ação específica no seu app. Em alguns criadores, essa opção aparece como **Deep Link Into App**.

Antes de usar essa opção, trabalhe com seus desenvolvedores para definir o formato do URI e configurar o app para abri-lo. Esquemas personalizados, como `myapp://`, abrem o app instalado diretamente. Links universais (iOS) e App Links (Android) usam URLs `https://` que podem abrir o app quando instalado e redirecionar para uma página web quando o app não está instalado.

Para definir esse comportamento ao clicar:

1. No criador da sua Campaign ou Canvas, localize **On-click behavior**:
   - Para notificações por push e Content Cards, acesse a guia **Compose**.
   - Para mensagens no app, acesse a guia **Compose**. No editor de arrastar e soltar, selecione um bloco de botão ou imagem e abra o painel de propriedades.
2. Selecione **Deeplink into application** ou **Deep Link Into App**.
3. Insira o link no campo de URL — por exemplo, `myapp://products/12345` para um esquema personalizado ou `https://example.com/products/12345` para um link universal ou App Link.
4. Envie uma mensagem de teste para um dispositivo físico. Um teste bem-sucedido abre o app e direciona para a tela ou ação pretendida. Para um link universal ou App Link, teste também em um dispositivo sem o app instalado para confirmar o fallback web esperado.

### Tags UTM e atribuição de Campaign {#utm-tags-and-campaign-attribution}

#### O que é uma tag UTM? {#what-is-a-utm-tag}

[Tags UTM (Urchin Traffic Manager)](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article) permitem incluir detalhes de atribuição de Campaign diretamente nos links. As tags UTM são usadas pelo Google Analytics para coletar dados de atribuição de Campaign e podem ser usadas para rastrear as seguintes propriedades:

- `utm_source`: O identificador da origem do tráfego (por exemplo, `my_app`)
- `utm_medium`: O meio da Campaign (por exemplo, `newsfeed`)
- `utm_campaign`: O identificador da Campaign (por exemplo, `spring_2016_campaign`)
- `utm_term`: Identificador de um termo de pesquisa paga que trouxe o usuário ao seu app ou website (por exemplo, `pizza`)
- `utm_content`: Um identificador para o link ou conteúdo específico em que o usuário clicou (por exemplo, `toplink` ou `android_iam_button2`)

As tags UTM podem ser incorporadas tanto em links HTTP (web) regulares quanto em deep links e rastreadas usando o Google Analytics.

##### Cálculos de tags UTM {#utm-tag-calculations}

A Braze reporta _Total de cliques_ para todos os links em uma Campaign ou etapa do Canvas, o que pode incluir links que não possuem tags UTM. Isso significa que você pode ver um resultado diferente (geralmente menor) nos links de rastreamento de Campaign do Google Analytics em comparação com o _Total de cliques_ exibido no desempenho da sua Campaign ou no Report Builder.

#### Usando tags UTM com a Braze {#using-utm-tags-with-braze}

Se você deseja usar tags UTM com links HTTP (web) regulares (por exemplo, para fazer atribuição de Campaign para suas campanhas de e-mail) e sua organização já usa o Google Analytics, você pode usar o [construtor de URLs do Google](https://ga-dev-tools.google/ga4/campaign-url-builder/) para gerar links UTM. Esses links podem ser facilmente incorporados ao conteúdo da Campaign na Braze, assim como qualquer outro link.

Para usar tags UTM em deep links para o seu app, o app deve ter o [SDK or kit de desenvolvimento de software do Google Analytics](https://developers.google.com/analytics/devguides/collection/) relevante integrado e configurado corretamente para lidar com deep links. Consulte seus desenvolvedores se não tiver certeza sobre isso.

Após o SDK or kit de desenvolvimento de software do Analytics estar integrado e configurado, as tags UTM podem ser usadas com deep links em Campaigns da Braze. Para configurar tags UTM para sua Campaign, inclua as tags UTM necessárias na URL de destino ou nos deep links. Os exemplos a seguir mostram como usar tags UTM em notificações por push e mensagens no app.

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

## Usar personalização Liquid em URLs {#use-liquid-personalization-in-urls}

Você pode construir dinamicamente sua URL diretamente no criador da Braze, permitindo adicionar parâmetros UTM dinâmicos às suas URLs ou enviar links exclusivos aos usuários (como direcionar usuários ao carrinho abandonado ou a um produto específico que voltou ao estoque).

### Criar uma URL com tags de personalização Liquid compatíveis {#create-a-url-with-supported-liquid-personalization-tags}

As URLs podem ser geradas dinamicamente por meio do uso de qualquer [tag de personalização Liquid compatível]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Também oferecemos suporte ao encurtamento de variáveis Liquid definidas pelo usuário, como nos exemplos a seguir:

### Criar uma URL usando variáveis Liquid {#create-a-url-using-liquid-variables}

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Encurtar URLs renderizadas por variáveis Liquid {#shorten-urls-rendered-by-liquid-variables}

**Canais compatíveis:** KakaoTalk, LINE, SMS, RCS, WhatsApp

Encurtamos URLs renderizadas por Liquid, incluindo aquelas presentes em propriedades de disparo por API or interface de programação do aplicativo (API). Por exemplo, se {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representar uma URL válida, encurtamos e rastreamos essa URL antes de enviar a mensagem.

### Encurtar URLs no endpoint `/messages/send` {#shorten-urls-in-messagessend-endpoint}

O encurtamento de links também está ativado para mensagens somente por API or interface de programação do aplicativo (API) por meio do [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages). Para uma lista completa dos parâmetros de solicitação, consulte [parâmetros de solicitação]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters).

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `link_shortening_enabled` | Sim | Booleano | Defina `link_shortening_enabled` como `true` para ativar o encurtamento de links. Para usar o rastreamento, um `campaign_id` e um `message_variation_id` devem estar presentes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Encurtar URLs no endpoint /messages/send" }