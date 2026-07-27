---
nav_title: Tags de personalização compatíveis
article_title: Tags de personalização Liquid compatíveis
page_order: 1
description: "Este artigo de referência abrange uma lista completa de tags de personalização Liquid compatíveis."
search_rank: 1
---

# Tags de personalização compatíveis {#supported-personalization-tags}

> Este artigo de referência abrange uma lista completa de tags de personalização Liquid compatíveis.

## Resumo das tags suportadas {#summary-of-supported-tags}

Para sua conveniência, um resumo das tags de personalização suportadas é fornecido. Para mais detalhes sobre cada tipo de tag e práticas recomendadas, continue lendo.

{% raw %}

| Tipo de tag de personalização | Tags |
| -------------  | ---- |
| Atributos padrão (default) | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| Atributos do dispositivo | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/channels/email/subscriptions#changing-email-subscriptions'>Atributos da lista de e-mails</a> | `{{${set_user_to_unsubscribed_url}}}` <br>Esta tag substitui a tag anterior `{{${unsubscribe_url}}}`. Embora a tag antiga ainda funcione em e-mails criados anteriormente, recomendamos que você use a tag mais recente. <br><br> `{{${set_user_to_one_click_list_unsubscribe}}}` <br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}` |
| <a href='/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#trigger-messages'>Atributos de SMS</a> | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/channels/whatsapp/message_processing/messaging_users'>Atributos do WhatsApp</a> | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` <br> `{{whats_app.${inbound_flow_response}}}` <br> `{{whats_app.${inbound_product_id}}}` <br> `{{whats_app.${inbound_catalog_id}}}` <br> `{{whats_app.${inbound_profile_name}}}` |
| Atributos de Campaign e atributos de etapa do Canvas | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Atributos do Canvas | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| Atributos do cartão | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| Eventos de geofencing | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| Propriedades do evento <br> (São personalizadas para o seu espaço de trabalho.) | `{{event_properties.${your_custom_event_property}}}` |
| Variáveis de contexto do Canvas | `{{context.${your_context_variable}}}` |
| Atributos personalizados <br> (São personalizados para o seu espaço de trabalho.) | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object'>Propriedades de disparo da API</a> | `{{api_trigger_properties.${your_api_trigger_property}}}` |
| Propriedades de entrada do Canvas | `{{context.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Resumo das tags suportadas" }

{% endraw %}

{% alert note %}
As propriedades de disparo da API devem usar duas chaves por tag: {% raw %}`{{api_trigger_properties.${your_api_trigger_property}}}`. Chaves triplas (por exemplo, `{{{...}}}`){% endraw %} não são uma sintaxe de personalização válida da Braze. Consulte [Por que meu Liquid disparado por API está falhando na Braze?]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/faq#why-is-my-api-triggered-liquid-failing-in-braze).
{% endalert %}

### Atributos suportados {#supported-attributes}

Os atributos de Campaign, cartão e Canvas são suportados apenas em seus modelos de mensagem correspondentes. Por exemplo, `dispatch_id` é suportado em Liquid para canais de envio de mensagens como e-mail, push, SMS e WhatsApp, mas não para mensagens no app ou Banners.

Consulte [Atributos de Campaign e Canvas entre fontes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/campaign_and_canvas_attributes_across_sources) para mais detalhes.

### Diferenças entre tags do Canvas e de Campaign {#canvas-and-campaign-tag-differences}

O comportamento das tags a seguir difere entre Canvas e Campaigns:
{% raw %}
- O comportamento de `dispatch_id` difere porque a Braze trata as etapas do Canvas como eventos disparados, mesmo quando são "agendadas" (exceto para etapas de entrada, que podem ser agendadas). Para saber mais, consulte [Comportamento do dispatch ID]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id).
- Usar a tag `{{campaign.${name}}}` com Canvas exibe o nome do componente do Canvas. Ao usar essa tag com Campaigns, ela exibe o nome da Campaign.
{% endraw %}

#### Nomes de Campaign em URLs {#campaign-names-in-urls}

{% raw %}
Os nomes de Campaign e de variantes de mensagem podem conter caracteres que não são seguros para URLs, como `%`, espaços ou `&`. Ao inserir `{{campaign.${name}}}` ou `{{campaign.${message_name}}}` em um link ou string de consulta, como um parâmetro `utm_campaign`, aplique o filtro [`url_encode`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#url-filters) para que a URL seja analisada corretamente. Por exemplo:

```liquid
https://example.com/?utm_campaign={{ campaign.${name} | url_encode }}
```
{% endraw %}

## Informações do dispositivo usado mais recentemente {#most-recently-used-device-information}

Você pode usar os seguintes atributos como template para o dispositivo mais recente do usuário em todas as plataformas. Se um usuário não tiver usado seu aplicativo (por exemplo, se você importou o usuário via REST API), todos esses valores serão `null`.

{% raw %}

| Tag | Descrição |
|---|---|
|`{{most_recently_used_device.${browser}}}` | O navegador usado mais recentemente no dispositivo do usuário. Exemplos incluem "Chrome" e "Safari". |
|`{{most_recently_used_device.${id}}}` | O identificador de dispositivo da Braze. No iOS, pode ser o Apple Identifier for Vendor (IDFV) ou um UUID. Para Android e outras plataformas, é um UUID gerado aleatoriamente. |
| `{{most_recently_used_device.${carrier}}}` | A operadora de telefonia do dispositivo usado mais recentemente, se disponível. Exemplos incluem "Verizon" e "Orange". |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | Se o dispositivo tem o rastreamento de anúncios ativado ou não. Este é um valor booleano (`true` ou `false`). |
| `{{most_recently_used_device.${idfa}}}` | Para dispositivos iOS, este valor é o Identifier for Advertising (IDFA) se o seu aplicativo estiver configurado com nossa [coleta opcional de IDFA]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection). Para dispositivos que não são iOS, este valor é null. |
| `{{most_recently_used_device.${google_ad_id}}}` | Para dispositivos Android, este valor é o Google Play Advertising Identifier se o seu aplicativo estiver configurado com nossa coleta opcional do Google Play Advertising ID. Para dispositivos que não são Android, este valor é null. |
| `{{most_recently_used_device.${roku_ad_id}}}` | Para dispositivos Roku, este valor é o Roku Advertising Identifier que é coletado quando o seu aplicativo está configurado com a Braze. Para dispositivos que não são Roku, este valor é null. |
| `{{most_recently_used_device.${model}}}` | O nome do modelo do dispositivo, se disponível. Exemplos incluem "iPhone 6S", "Nexus 6P" e "Firefox". |
| `{{most_recently_used_device.${os}}}` | O sistema operacional do dispositivo, se disponível. Exemplos incluem "iOS 9.2.1", "Android (Lollipop)" e "Windows". |
| `{{most_recently_used_device.${platform}}}` | A plataforma do dispositivo, se disponível. Se definido, o valor é um dos seguintes: `ios`, `android`, `kindle`, `android_china`, `web` ou `tvos`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Informações do dispositivo usado mais recentemente" }

Como existe uma grande variedade de operadoras, nomes de modelos e sistemas operacionais de dispositivos, recomendamos que você teste minuciosamente qualquer Liquid que dependa condicionalmente de qualquer um desses valores. Esses valores serão `null` se não estiverem disponíveis em um dispositivo específico.

## Informações do app direcionado {#targeted-app-information}

Para mensagens no app, você pode usar os seguintes atributos de app dentro do Liquid. Os valores são baseados em qual chave da API SDK seus apps usam para solicitar o envio de mensagens.

|Tag | Descrição |
|------------------|---|
| `{{app.${api_id}}}` | A chave de API do app que está solicitando a mensagem. Por exemplo, você usa essa chave em conjunto com o Liquid `abort_message()` para evitar o envio de mensagens no app para determinados apps, como plataformas de TV ou builds de desenvolvimento que usam uma chave da API SDK separada.|
| `{{app.${name}}}` | O nome do app (conforme definido no dashboard da Braze) que está solicitando a mensagem. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Informações do app direcionado" }

Por exemplo, este código Liquid interrompe uma mensagem se os apps solicitantes não forem uma das duas chaves de API na lista:

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## Informações do dispositivo direcionado {#targeted-device-information}

Para notificações por push, mensagens no app e Banners, você pode usar templates com os seguintes atributos do dispositivo que recebe a mensagem. Uma notificação por push, mensagem no app ou Banner pode incluir atributos do dispositivo no qual o usuário lê a mensagem. Esses atributos não funcionam para Content Cards ou e-mails. No caso de e-mails, as mensagens são renderizadas antes do envio, então o dispositivo em que o usuário abre o e-mail é desconhecido nesse momento.

|Tag | Descrição |
|------------------|---|
| `{{targeted_device.${id}}}` | Este é o identificador de dispositivo da Braze. No iOS, pode ser o Apple Identifier for Vendor (IDFV) ou um UUID. Para Android e outras plataformas, é um UUID gerado aleatoriamente. Por exemplo, se um usuário tem cinco dispositivos, uma tentativa de envio ocorre para todos os cinco dispositivos, cada um usando o identificador de dispositivo correspondente. Se uma mensagem estiver configurada para enviar ao dispositivo usado mais recentemente pelo usuário, apenas uma tentativa de envio ocorre para o dispositivo mais recente identificado pela Braze. |
| `{{targeted_device.${carrier}}}` | A operadora de telefonia do dispositivo usado mais recentemente, se disponível. Exemplos incluem "Verizon" e "Orange". |
| `{{targeted_device.${idfa}}}` | Para dispositivos iOS, esse valor é o Identifier for Advertising (IDFA) se o seu app estiver configurado com nossa [coleta opcional de IDFA]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection). Para dispositivos que não são iOS, esse valor é nulo. |
| `{{targeted_device.${google_ad_id}}}` | Para dispositivos Android, esse valor é o Google Play Advertising Identifier se o seu app estiver configurado com nossa [coleta opcional do Google Play Advertising ID]. Para dispositivos que não são Android, esse valor é nulo. |
| `{{targeted_device.${roku_ad_id}}}` | Para dispositivos Roku, esse valor é o Roku Advertising Identifier coletado quando o seu app é configurado com a Braze. Para dispositivos que não são Roku, esse valor é nulo. |
| `{{targeted_device.${model}}}` | O nome do modelo do dispositivo, se disponível. Exemplos incluem "iPhone 6S", "Nexus 6P" e "Firefox". |
| `{{targeted_device.${os}}}` | O sistema operacional do dispositivo, se disponível. Exemplos incluem "iOS 9.2.1", "Android (Lollipop)" e "Windows". |
| `{{targeted_device.${platform}}}` | A plataforma do dispositivo, se disponível. Se definido, o valor é um dos seguintes: `ios`, `android`, `kindle`, `android_china`, `web` ou `tvos`. Você também pode usar a tag de personalização `most_recently_used_device`. |
| `{{targeted_device.${foreground_push_enabled}}}` | Esse valor é `true` quando o dispositivo direcionado está habilitado para push em primeiro plano, e `false` caso contrário. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Informações do dispositivo direcionado" }

{% endraw %}

Como existe uma grande variedade de operadoras, nomes de modelos e sistemas operacionais de dispositivos, recomendamos que você teste minuciosamente qualquer lógica que dependa condicionalmente de algum desses valores. Esses valores são `null` se não estiverem disponíveis em um dispositivo específico.

Além disso, para notificações por push, é possível que a Braze não consiga identificar o dispositivo associado à notificação por push em determinadas circunstâncias, como quando o token por push foi importado via API, resultando em valores `null` para essas mensagens.

![Exemplo de uso de um valor padrão "there" ao usar uma variável de nome em uma mensagem push.]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### Usando lógica condicional em vez de um valor padrão {#using-conditional-logic-instead-of-a-default-value}

Em algumas circunstâncias, você pode optar por usar [lógica condicional]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic) em vez de definir um valor padrão. A lógica condicional permite enviar mensagens que variam com base no valor de um atributo personalizado. Além disso, você pode usar lógica condicional para [interromper mensagens]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) para clientes com valores de atributo nulos ou em branco.

#### Caso de uso {#use-case}

Por exemplo, digamos que você está enviando uma notificação de saldo de recompensas para clientes. Não há uma boa maneira de lidar com clientes com saldos baixos e nulos usando valores padrão.

Nesse caso, há duas opções que podem funcionar melhor do que definir um valor padrão:

1. Interromper a mensagem para clientes com saldos baixos, nulos e em branco.

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. Enviar uma mensagem completamente diferente para esses clientes, como:

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

Nesse caso de uso, um usuário com nome em branco ou nulo recebe a mensagem "Thanks for downloading". Você deve incluir um [valor padrão]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) para o nome para garantir que seu cliente não veja Liquid no caso de um erro.

{% endraw %}

## Tags de variáveis {#variable-tags}

Você pode usar a tag `assign` para criar uma variável no criador de mensagem. Recomendamos usar um nome exclusivo para sua variável. Se você criar uma variável com um nome semelhante às tags de personalização compatíveis (como `language`), isso pode afetar sua lógica de envio de mensagens.

Depois de criar uma variável, você pode referenciá-la na sua lógica de envio de mensagens ou na mensagem. Essa tag é útil quando você deseja reformatar o conteúdo retornado pelo nosso recurso de [Connected Content]({% image_buster /assets/img_archive/personalized_firstname_.png %}). Você pode ler mais na documentação da Shopify sobre [tags de variáveis](https://docs.shopify.com/themes/liquid/tags/variable-tags).

{% alert important %}
Strings entre aspas simples dentro de uma tag `assign` são tratadas como strings literais. Tags de personalização Liquid dentro de aspas simples não são interpoladas. Por exemplo:

{% raw %}
```liquid
{% assign name_intro = 'My name is {{${first_name}}}' %}
{{ name_intro }}
```
{% endraw %}

Isso retorna o texto literal {% raw %}`My name is {{${first_name}}}`{% endraw %} em vez do nome do usuário.

Para incluir personalização, use variáveis ou concatene strings com o filtro [`append`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#string-filters). Para templates de URL com personalização, consulte [modelos de link]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template).
{% endalert %}

{% alert tip %}
Você está sempre atribuindo as mesmas variáveis em cada mensagem? Em vez de escrever a tag `assign` repetidamente, você pode salvar essa tag como um bloco de conteúdo e colocá-la no topo da sua mensagem.

1. [Crie um bloco de conteúdo]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#create-a-content-block).
2. Dê um nome ao seu bloco de conteúdo (sem espaços ou caracteres especiais).
3. Selecione **Editar** na parte inferior da página.
4. Digite suas tags `assign`.

Desde que o bloco de conteúdo esteja no topo da sua mensagem, toda vez que a variável for inserida na mensagem como um objeto, ela fará referência ao atributo personalizado escolhido.
{% endalert %}

### Caso de uso

Digamos que você permite que seus clientes troquem seus pontos de recompensas por prêmios depois de acumularem 100 pontos. Então, você só quer enviar mensagens para clientes que teriam um saldo de pontos maior ou igual a 100 se fizessem essa compra adicional:

{% raw %}
```liquid
{% assign new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Make a purchase to bring your rewards points to {{new_points_balance}} and cash in today!
{% else %}
{% abort_message('not enough points') %}
{% endif %}
```
{% endraw %}

## Tags de iteração {#iteration-tags}

{% raw %}
Tags de iteração podem ser usadas para executar um bloco de código repetidamente. O caso de uso abaixo apresenta a tag `for`.

### Caso de uso

Digamos que você está fazendo uma promoção de tênis Nike e quer enviar mensagens para clientes que demonstraram interesse na Nike. Você tem um array de marcas de produtos visualizadas no perfil de cada cliente. Esse array pode conter até 25 marcas de produtos, mas você só quer enviar mensagens para clientes que visualizaram um produto Nike como uma das 5 visualizações de produtos mais recentes.

```liquid
{% for items in {{custom_attribute.${Brands Viewed}}} limit:5 %}
{% if {{items}} contains 'Converse' %}
{% assign converse_viewer = true %}
{% endif %}
{% endfor %}
{% if converse_viewer == true %}
Sale on Converse!
{% else %}
{% abort_message() %}
{% endif %}
```

Neste caso de uso, verificamos os cinco primeiros itens no array de marcas de tênis visualizadas. Se um desses itens for converse, criamos a variável `converse_viewer` e a definimos como true.

Em seguida, enviamos a mensagem de promoção quando `converse_viewer` é true. Caso contrário, interrompemos a mensagem.

Este é um exemplo simples de como tags de iteração podem ser usadas no criador de mensagem da Braze. Para saber mais, consulte a documentação da Shopify sobre [tags de iteração](https://docs.shopify.com/themes/liquid/tags/iteration-tags).

## Tags de sintaxe {#syntax-tags}

Os tags de sintaxe podem ser usados para controlar como o Liquid é renderizado. Você pode usar o tag `echo` para retornar uma expressão. Isso é o mesmo que envolver uma expressão usando chaves, exceto que você pode usar esse tag dentro de tags Liquid. Você também pode usar o tag `liquid` para ter um bloco de Liquid sem nenhum delimitador em cada tag. Cada tag precisa estar em sua própria linha ao usar o tag `liquid`. Confira a documentação da Shopify sobre [tags de sintaxe](https://shopify.dev/api/liquid/tags#syntax-tags) para mais informações e exemplos.

Com o [controle de espaços em branco](https://shopify.github.io/liquid/basics/whitespace/), você pode remover espaços em branco ao redor dos seus tags, ajudando a controlar ainda mais a aparência da saída do Liquid.

## Códigos de status HTTP {#http-personalization}

Você pode utilizar o status HTTP de uma chamada de [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) salvando-o primeiro como uma variável local e depois usando a chave `__http_status_code__`. Por exemplo:

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
Essa chave só é adicionada automaticamente ao objeto de Conteúdo conectado se o endpoint retornar um objeto JSON. Se o endpoint retornar um array ou outro tipo, essa chave não pode ser definida automaticamente na resposta.
{% endalert %}

## Enviar mensagens com base no idioma, local mais recente e fuso horário {#send-messages-based-on-language-most-recent-locale-and-time-zone}

Em algumas situações, você pode querer enviar mensagens específicas para determinados locais. Por exemplo, o português brasileiro é normalmente diferente do português europeu.

### Caso de uso: Localizar com base no local mais recente {#use-case-localize-based-on-recent-locale}

Veja um caso de uso de como você pode usar o local mais recente para localizar ainda mais uma mensagem internacionalizada.

{% raw %}

```liquid
{% if ${language} == 'en' %}
Message in English
{% elsif  ${language} == 'fr' %}
Message in French
{% elsif  ${language} == 'ja' %}
Message in Japanese
{% elsif  ${language} == 'ko' %}
Message in Korean
{% elsif  ${language} == 'ru' %}
Message in Russian
{% elsif ${most_recent_locale} == 'pt_BR' %}
Message in Brazilian Portuguese
{% elsif ${most_recent_locale} == 'pt_PT' %}
Message in European Portuguese
{% elsif  ${language} == 'pt' %}
Message in default Portuguese
{% else %}
Message in default language
{% endif %}
```

Nesse caso de uso, clientes com o local mais recente `pt_BR` recebem uma mensagem em português brasileiro, e clientes com o local mais recente `pt_PT` recebem uma mensagem em português europeu. Clientes que não atendem às duas primeiras condições, mas têm o idioma definido como português, recebem uma mensagem no tipo de português que você definir como padrão.

### Caso de uso: Direcionar usuários por fuso horário {#use-case-target-users-by-time-zone}

Você também pode direcionar usuários pelo fuso horário. Por exemplo, enviar uma mensagem se eles estiverem no fuso EST e outra se estiverem no PST. Para isso, salve o horário atual em UTC e compare com uma instrução if/else usando o horário atual do usuário para enviar a mensagem certa para o fuso horário certo. Você deve configurar a Campaign para enviar no fuso local do usuário, para que ele receba a Campaign no horário correto.

Veja o caso de uso a seguir para saber como escrever uma mensagem que é entregue entre 14h e 15h com uma mensagem específica para cada fuso horário.

```liquid
{% assign hour_in_utc = 'now' | date: '%H' | plus:0 %}
{% if hour_in_utc >= 19 && hour_in_utc < 20 %}
It is between 2:00:00 pm and 2:59:59 pm ET!
{% elsif hour_in_utc >= 22 && hour_in_utc < 23 %}
It is between 2:00:00 pm and 2:59:59 pm PT!
{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}

## Enviar mensagens com um número aleatório {#send-messages-with-a-random-number}

{% raw %}
A tag `{% random %}` retorna um número aleatório. Você pode usá-la para lógica no estilo de testes A/B, amostragem ou variação do conteúdo de mensagens.

| Tag | Descrição |
|-------|--------------|
| `{% random %}` | Um float entre 0 e 1 (incluindo 0, excluindo 1). |
| `{% random 10 %}` (argumento inteiro) | Um inteiro variando de 0 até, mas não incluindo, o inteiro especificado. Por exemplo, `{% random 10 %}` retorna um inteiro de 0 a 9. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Enviar mensagens com um número aleatório" }

{% endraw %}

### Caso de uso: enviar variantes aleatórias para os usuários {#use-case-send-users-random-variants}

{% raw %}
```liquid
{% capture roll_str %}{% random %}{% endcapture %}
{% assign roll = roll_str | plus: 0 %}
{% if roll < 0.5 %}
Show variant A
{% else %}
Show variant B
{% endif %}
```
{% endraw %}

## Tag de carrinho de compras de eCommerce {#shopping-cart-tag}

A tag `shopping_cart` acessa o conteúdo do carrinho de um usuário nos casos de uso de eCommerce de [carrinho abandonado]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20cart#abandoned-cart) e [checkout abandonado]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20checkout#abandoned-checkout) no Canvas. Substitua `CART_ID` pelo valor real do ID do carrinho, como {% raw %}`{{context.${cart_id}}}`{% endraw %}.

{% raw %}
```liquid
{% shopping_cart CART_ID :abort_if_not_abandoned false %}
```
{% endraw %}

O parâmetro `abort_if_not_abandoned` neste exemplo se aplica apenas ao caso de uso de [checkout abandonado]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20checkout#abandoned-checkout) quando usado com o evento `ecommerce.checkout_started`. Ele não é aplicável a casos de uso de carrinho abandonado. Para mais detalhes, consulte [`abort_if_not_abandoned`]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20checkout#abort-if-not-abandoned).

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags