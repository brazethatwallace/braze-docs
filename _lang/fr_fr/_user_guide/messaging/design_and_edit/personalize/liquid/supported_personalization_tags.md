---
nav_title: Étiquettes de personnalisation prises en charge
article_title: Étiquettes de personnalisation Liquid prises en charge
page_order: 1
description: "Cet article de référence présente une liste complète des étiquettes de personnalisation Liquid prises en charge."
search_rank: 1
---

# Étiquettes de personnalisation prises en charge {#supported-personalization-tags}

> Cet article de référence présente une liste complète des étiquettes de personnalisation Liquid prises en charge.

## Résumé des tags pris en charge {#summary-of-supported-tags}

Pour plus de commodité, un résumé des tags de personnalisation pris en charge est fourni ci-dessous. Pour plus de détails sur chaque type de tag et les bonnes pratiques, poursuivez votre lecture.

{% raw %}

| Type de tag de personnalisation | Tags |
| -------------  | ---- |
| Attributs standard (par défaut) | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| Attributs de l'appareil | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/channels/email/subscriptions#changing-email-subscriptions'>Attributs de liste e-mail</a> | `{{${set_user_to_unsubscribed_url}}}` <br>Ce tag remplace l'ancien tag `{{${unsubscribe_url}}}`. Bien que l'ancien tag fonctionne toujours dans les e-mails créés précédemment, nous vous recommandons d'utiliser le nouveau tag à la place. <br><br> `{{${set_user_to_one_click_list_unsubscribe}}}` <br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}` |
| <a href='/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#trigger-messages'>Attributs SMS</a> | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/channels/whatsapp/message_processing/messaging_users'>Attributs WhatsApp</a> | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` <br> `{{whats_app.${inbound_flow_response}}}` <br> `{{whats_app.${inbound_product_id}}}` <br> `{{whats_app.${inbound_catalog_id}}}` <br> `{{whats_app.${inbound_profile_name}}}` |
| Attributs de Campaign et attributs d'étape Canvas | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Attributs Canvas | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| Attributs de carte | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| Événements de géorepérage | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| Propriétés d'événement <br> (Celles-ci sont propres à votre espace de travail.) | `{{event_properties.${your_custom_event_property}}}` |
| Variables de contexte Canvas | `{{context.${your_context_variable}}}` |
| Attributs personnalisés <br> (Ceux-ci sont propres à votre espace de travail.) | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object'>Propriétés de déclencheur API</a> | `{{api_trigger_properties.${your_api_trigger_property}}}` |
| Propriétés d'entrée Canvas | `{{context.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résumé des tags pris en charge" }

{% endraw %}

{% alert note %}
Les propriétés de déclencheur API doivent utiliser deux accolades par tag : {% raw %}`{{api_trigger_properties.${your_api_trigger_property}}}`. Les triples accolades (par exemple `{{{...}}}`){% endraw %} ne constituent pas une syntaxe de personnalisation Braze valide. Consultez [Pourquoi mon Liquid déclenché par API échoue-t-il dans Braze ?]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/faq#why-is-my-api-triggered-liquid-failing-in-braze).
{% endalert %}

### Attributs pris en charge {#supported-attributes}

Les attributs de Campaign, de carte et de Canvas ne sont pris en charge que dans leurs modèles de communication correspondants. Par exemple, `dispatch_id` est pris en charge dans Liquid pour les canaux de communication tels que l'e-mail, les notifications push, les SMS et WhatsApp, mais pas pour les messages in-app ni les bannières.

Consultez [Attributs de Campaign et Canvas selon les sources]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/campaign_and_canvas_attributes_across_sources) pour plus de détails.

### Différences entre les tags Canvas et Campaign {#canvas-and-campaign-tag-differences}

Le comportement des tags suivants diffère entre Canvas et Campaigns :
{% raw %}
- Le comportement de `dispatch_id` diffère car Braze traite les étapes Canvas comme des événements déclenchés, même lorsqu'elles sont « planifiées » (à l'exception des étapes d'entrée, qui peuvent être planifiées). Pour plus d'informations, consultez [Comportement du dispatch ID]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id).
- L'utilisation du tag `{{campaign.${name}}}` avec Canvas affiche le nom du composant Canvas. Lorsque vous utilisez ce tag avec Campaigns, il affiche le nom de la campagne.
{% endraw %}

#### Noms de Campaign dans les URL {#campaign-names-in-urls}

{% raw %}
Les noms de Campaign et de variante de message peuvent contenir des caractères non sécurisés pour les URL, tels que `%`, des espaces ou `&`. Lorsque vous insérez `{{campaign.${name}}}` ou `{{campaign.${message_name}}}` dans un lien ou une chaîne de requête, comme un paramètre `utm_campaign`, appliquez le filtre [`url_encode`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#url-filters) afin que l'URL soit analysée correctement. Par exemple :

```liquid
https://example.com/?utm_campaign={{ campaign.${name} | url_encode }}
```
{% endraw %}

## Informations sur l'appareil le plus récemment utilisé {#most-recently-used-device-information}

Vous pouvez utiliser les attributs suivants pour l'appareil le plus récent de l'utilisateur sur toutes les plateformes. Si un utilisateur n'a pas utilisé votre application (par exemple, si vous avez importé l'utilisateur via la REST API), alors toutes ces valeurs sont `null`.

{% raw %}

| Tag | Description |
|---|---|
|`{{most_recently_used_device.${browser}}}` | Le navigateur le plus récemment utilisé sur l'appareil de l'utilisateur. Par exemple, « Chrome » et « Safari ». |
|`{{most_recently_used_device.${id}}}` | L'identifiant d'appareil Braze. Sur iOS, il peut s'agir de l'identifiant Apple pour le fournisseur (IDFV) ou d'un UUID. Pour Android et les autres plateformes, il s'agit d'un UUID généré aléatoirement. |
| `{{most_recently_used_device.${carrier}}}` | L'opérateur de téléphonie de l'appareil le plus récemment utilisé, si disponible. Par exemple, « Verizon » et « Orange ». |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | Indique si le suivi publicitaire est activé ou non sur l'appareil. Il s'agit d'une valeur booléenne (`true` ou `false`). |
| `{{most_recently_used_device.${idfa}}}` | Pour les appareils iOS, cette valeur est l'identifiant publicitaire (IDFA) si votre application est configurée avec notre [collecte optionnelle de l'IDFA]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection). Pour les appareils non iOS, cette valeur est null. |
| `{{most_recently_used_device.${google_ad_id}}}` | Pour les appareils Android, cette valeur est l'identifiant publicitaire Google Play si votre application est configurée avec notre collecte optionnelle de l'identifiant publicitaire Google Play. Pour les appareils non Android, cette valeur est null. |
| `{{most_recently_used_device.${roku_ad_id}}}` | Pour les appareils Roku, cette valeur est l'identifiant publicitaire Roku collecté lorsque votre application est configurée avec Braze. Pour les appareils non Roku, cette valeur est null. |
| `{{most_recently_used_device.${model}}}` | Le nom du modèle de l'appareil, si disponible. Par exemple, « iPhone 6S », « Nexus 6P » et « Firefox ». |
| `{{most_recently_used_device.${os}}}` | Le système d'exploitation de l'appareil, si disponible. Par exemple, « iOS 9.2.1 », « Android (Lollipop) » et « Windows ». |
| `{{most_recently_used_device.${platform}}}` | La plateforme de l'appareil, si disponible. Si définie, la valeur est l'une des suivantes : `ios`, `android`, `kindle`, `android_china`, `web` ou `tvos`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Informations sur l'appareil le plus récemment utilisé" }

Étant donné la grande variété d'opérateurs, de noms de modèles et de systèmes d'exploitation, nous vous conseillons de tester minutieusement tout code Liquid qui dépend conditionnellement de l'une de ces valeurs. Ces valeurs sont `null` si elles ne sont pas disponibles sur un appareil donné.

## Informations sur l'application ciblée {#targeted-app-information}

Pour les messages in-app, vous pouvez utiliser les attributs d'application suivants dans Liquid. Les valeurs sont basées sur la clé API du SDK que vos applications utilisent pour demander l'envoi de messages.

|Étiquette | Description |
|------------------|---|
| `{{app.${api_id}}}` | La clé API de l'application qui demande le message. Par exemple, vous utilisez cette clé en conjonction avec le Liquid `abort_message()` pour éviter d'envoyer des messages in-app à certaines applications, telles que les plateformes TV ou les builds de développement qui utilisent une clé API SDK distincte.|
| `{{app.${name}}}` | Le nom de l'application (tel que défini dans le tableau de bord de Braze) qui demande le message. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Informations sur l'application ciblée" }

Par exemple, ce code Liquid interrompt un message si les applications qui le demandent ne correspondent pas à l'une des deux clés API de la liste :

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## Informations sur l'appareil ciblé {#targeted-device-information}

Pour les notifications push, les messages in-app et les Banners, vous pouvez utiliser les attributs suivants de l'appareil qui reçoit le message dans vos modèles. Une notification push, un message in-app ou un Banner peut inclure les attributs de l'appareil sur lequel l'utilisateur lit le message. Ces attributs ne fonctionnent pas pour les Content Cards ni pour les e-mails. Pour les e-mails, les messages sont rendus avant l'envoi, de sorte que l'appareil sur lequel l'utilisateur ouvre l'e-mail est inconnu à ce moment-là.

|Tag | Description |
|------------------|---|
| `{{targeted_device.${id}}}` | Il s'agit de l'identifiant d'appareil Braze. Sur iOS, il peut s'agir de l'Apple Identifier for Vendor (IDFV) ou d'un UUID. Pour Android et les autres plateformes, il s'agit d'un UUID généré aléatoirement. Par exemple, si un utilisateur possède cinq appareils, une tentative d'envoi est effectuée pour les cinq appareils, chacun utilisant l'identifiant d'appareil correspondant. Si un message est configuré pour être envoyé à l'appareil le plus récemment utilisé par l'utilisateur, une seule tentative d'envoi est effectuée vers l'appareil le plus récemment utilisé identifié par Braze. |
| `{{targeted_device.${carrier}}}` | L'opérateur téléphonique de l'appareil le plus récemment utilisé, si disponible. Par exemple, « Verizon » et « Orange ». |
| `{{targeted_device.${idfa}}}` | Pour les appareils iOS, cette valeur est l'Identifier for Advertising (IDFA) si votre application est configurée avec notre [collecte optionnelle de l'IDFA]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection). Pour les appareils non iOS, cette valeur est null. |
| `{{targeted_device.${google_ad_id}}}` | Pour les appareils Android, cette valeur est le Google Play Advertising Identifier si votre application est configurée avec notre [collecte optionnelle du Google Play Advertising ID]. Pour les appareils non Android, cette valeur est null. |
| `{{targeted_device.${roku_ad_id}}}` | Pour les appareils Roku, cette valeur est le Roku Advertising Identifier collecté lorsque votre application est configurée avec Braze. Pour les appareils non Roku, cette valeur est null. |
| `{{targeted_device.${model}}}` | Le nom du modèle de l'appareil, si disponible. Par exemple, « iPhone 6S », « Nexus 6P » et « Firefox ». |
| `{{targeted_device.${os}}}` | Le système d'exploitation de l'appareil, si disponible. Par exemple, « iOS 9.2.1 », « Android (Lollipop) » et « Windows ». |
| `{{targeted_device.${platform}}}` | La plateforme de l'appareil, si disponible. Si définie, la valeur est l'une des suivantes : `ios`, `android`, `kindle`, `android_china`, `web` ou `tvos`. Vous pouvez également utiliser le tag de personnalisation `most_recently_used_device`. |
| `{{targeted_device.${foreground_push_enabled}}}` | Cette valeur est `true` lorsque l'appareil ciblé est activé pour les notifications push au premier plan, `false` dans le cas contraire. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Informations sur l'appareil ciblé" }

{% endraw %}

Étant donné la grande variété d'opérateurs, de noms de modèles et de systèmes d'exploitation, nous vous conseillons de tester minutieusement toute logique qui dépend conditionnellement de l'une de ces valeurs. Ces valeurs sont `null` si elles ne sont pas disponibles sur un appareil donné.

De plus, pour les notifications push, il est possible que Braze ne puisse pas déterminer l'appareil associé à la notification push dans certaines circonstances, par exemple si le jeton push a été importé via l'API, ce qui entraîne des valeurs `null` pour ces messages.

![Exemple d'utilisation d'une valeur par défaut « there » lors de l'utilisation d'une variable de prénom dans un message push.]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### Utiliser la logique conditionnelle au lieu d'une valeur par défaut {#using-conditional-logic-instead-of-a-default-value}

Dans certaines circonstances, vous pouvez choisir d'utiliser la [logique conditionnelle]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic) au lieu de définir une valeur par défaut. La logique conditionnelle vous permet d'envoyer des messages qui diffèrent en fonction de la valeur d'un attribut personnalisé. De plus, vous pouvez utiliser la logique conditionnelle pour [interrompre les messages]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) destinés aux clients dont les valeurs d'attribut sont null ou vides.

#### Cas d'usage {#use-case}

Par exemple, imaginons que vous envoyez une notification de solde de récompenses à vos clients. Il n'existe pas de bonne façon de gérer les clients avec des soldes faibles ou null en utilisant des valeurs par défaut.

Dans ce cas, deux options peuvent mieux fonctionner que la définition d'une valeur par défaut :

1. Interrompre le message pour les clients avec des soldes faibles, null ou vides.

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. Envoyer un message complètement différent à ces clients, par exemple :

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

Dans ce cas d'usage, un utilisateur dont le prénom est vide ou null reçoit le message « Thanks for downloading ». Vous devriez inclure une [valeur par défaut]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) pour le prénom afin de vous assurer que votre client ne voit pas de Liquid en cas d'erreur.

{% endraw %}

## Étiquettes de variables {#variable-tags}

Vous pouvez utiliser l'étiquette `assign` pour créer une variable dans le composeur de messages. Nous vous recommandons d'utiliser un nom unique pour votre variable. Si vous créez une variable avec un nom similaire aux étiquettes de personnalisation prises en charge (comme `language`), cela peut affecter votre logique de communication.

Après avoir créé une variable, vous pouvez la référencer dans votre logique de communication ou votre message. Cette étiquette est particulièrement utile lorsque vous souhaitez reformater du contenu renvoyé par notre fonctionnalité de [contenu connecté]({% image_buster /assets/img_archive/personalized_firstname_.png %}). Vous pouvez en savoir plus dans la documentation de Shopify sur les [étiquettes de variables](https://docs.shopify.com/themes/liquid/tags/variable-tags).

{% alert important %}
Les chaînes de caractères encadrées par des guillemets simples à l'intérieur d'une étiquette `assign` sont traitées comme des chaînes littérales. Les étiquettes de personnalisation Liquid à l'intérieur de guillemets simples ne sont pas interpolées. Par exemple :

{% raw %}
```liquid
{% assign name_intro = 'My name is {{${first_name}}}' %}
{{ name_intro }}
```
{% endraw %}

Cela affiche le texte littéral {% raw %}`My name is {{${first_name}}}`{% endraw %} au lieu du prénom de l'utilisateur.

Pour inclure de la personnalisation, utilisez des variables ou concaténez des chaînes de caractères avec le filtre [`append`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#string-filters). Pour le templating d'URL avec personnalisation, consultez les [modèles de liens]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template).
{% endalert %}

{% alert tip %}
Vous vous retrouvez à assigner les mêmes variables dans chaque message ? Au lieu de réécrire l'étiquette `assign` à chaque fois, vous pouvez enregistrer cette étiquette en tant que bloc de contenu et la placer en haut de votre message.

1. [Créez un bloc de contenu]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#create-a-content-block).
2. Donnez un nom à votre bloc de contenu (sans espaces ni caractères spéciaux).
3. Sélectionnez **Modifier** en bas de la page.
4. Saisissez vos étiquettes `assign`.

Tant que le bloc de contenu se trouve en haut de votre message, chaque fois que la variable est insérée dans votre message en tant qu'objet, elle fait référence à l'attribut personnalisé que vous avez choisi.
{% endalert %}

### Cas d'usage

Imaginons que vous permettez à vos clients d'échanger leurs points de récompense contre des prix après avoir accumulé 100 points de récompense. Vous souhaitez donc envoyer un message uniquement aux clients dont le solde de points serait supérieur ou égal à 100 s'ils effectuaient cet achat supplémentaire :

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

## Étiquettes d'itération {#iteration-tags}

{% raw %}
Les étiquettes d'itération peuvent être utilisées pour exécuter un bloc de code de manière répétée. Le cas d'usage ci-dessous utilise l'étiquette `for`.

### Cas d'usage

Imaginons que vous organisez une promotion sur les baskets Nike et que vous souhaitez envoyer un message aux clients qui ont exprimé un intérêt pour Nike. Vous disposez d'un tableau de marques de produits consultées sur le profil de chaque client. Ce tableau peut contenir jusqu'à 25 marques de produits, mais vous souhaitez uniquement envoyer un message aux clients qui ont consulté un produit Nike parmi leurs 5 consultations de produits les plus récentes.

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

Dans ce cas d'usage, nous vérifions les cinq premiers éléments du tableau des marques de baskets consultées. Si l'un de ces éléments est Converse, nous créons la variable `converse_viewer` et la définissons sur true.

Ensuite, nous envoyons le message de promotion lorsque `converse_viewer` est true. Sinon, nous interrompons le message.

Il s'agit d'un exemple simple de la façon dont les étiquettes d'itération peuvent être utilisées dans le composeur de messages de Braze. Vous trouverez plus d'informations dans la documentation de Shopify sur les [étiquettes d'itération](https://docs.shopify.com/themes/liquid/tags/iteration-tags).

## Étiquettes de syntaxe {#syntax-tags}

Les étiquettes de syntaxe peuvent être utilisées pour contrôler le rendu de Liquid. Vous pouvez utiliser l'étiquette `echo` pour retourner une expression. Cela revient à encadrer une expression avec des accolades, sauf que vous pouvez utiliser cette étiquette à l'intérieur d'étiquettes Liquid. Vous pouvez également utiliser l'étiquette `liquid` pour avoir un bloc de Liquid sans aucun délimiteur sur chaque étiquette. Chaque étiquette doit être sur sa propre ligne lorsque vous utilisez l'étiquette `liquid`. Consultez la documentation de Shopify sur les [étiquettes de syntaxe](https://shopify.dev/api/liquid/tags#syntax-tags) pour plus d'informations et d'exemples.

Avec le [contrôle des espaces](https://shopify.github.io/liquid/basics/whitespace/), vous pouvez supprimer les espaces autour de vos étiquettes, ce qui vous aide à mieux contrôler l'apparence de la sortie Liquid.

## Codes de statut HTTP {#http-personalization}

Vous pouvez utiliser le statut HTTP d'un appel de [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) en l'enregistrant d'abord en tant que variable locale, puis en utilisant la clé `__http_status_code__`. Par exemple :

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
Cette clé n'est ajoutée automatiquement à l'objet de contenu connecté que si l'endpoint renvoie un objet JSON. Si l'endpoint renvoie un tableau ou un autre type, cette clé ne peut pas être définie automatiquement dans la réponse.
{% endalert %}

## Envoyer des messages en fonction de la langue, de la locale la plus récente et du fuseau horaire {#send-messages-based-on-language-most-recent-locale-and-time-zone}

Dans certaines situations, vous pouvez souhaiter envoyer des messages spécifiques à des locales particulières. Par exemple, le portugais brésilien est généralement différent du portugais européen.

### Cas d'usage : localiser en fonction de la locale la plus récente {#use-case-localize-based-on-recent-locale}

Voici un cas d'usage montrant comment utiliser la locale la plus récente pour affiner la localisation d'un message internationalisé.

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

Dans ce cas d'usage, les clients dont la locale la plus récente est `pt_BR` reçoivent un message en portugais brésilien, et ceux dont la locale la plus récente est `pt_PT` reçoivent un message en portugais européen. Les clients qui ne remplissent pas les deux premières conditions mais dont la langue est définie sur le portugais reçoivent un message dans le type de portugais par défaut de votre choix.

### Cas d'usage : cibler les utilisateurs par fuseau horaire {#use-case-target-users-by-time-zone}

Vous pouvez également cibler les utilisateurs en fonction de leur fuseau horaire. Par exemple, envoyez un message s'ils se trouvent dans le fuseau EST et un autre s'ils sont dans le fuseau PST. Pour ce faire, enregistrez l'heure actuelle en UTC et comparez une instruction if/else avec l'heure actuelle de l'utilisateur afin d'envoyer le bon message pour le bon fuseau horaire. Vous devez configurer la Campaign pour qu'elle s'envoie dans le fuseau horaire local de l'utilisateur, afin qu'il la reçoive au bon moment.

Consultez le cas d'usage suivant pour savoir comment rédiger un message distribué entre 14 h et 15 h avec un contenu spécifique pour chaque fuseau horaire.

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

## Envoyer des messages avec un nombre aléatoire {#send-messages-with-a-random-number}

{% raw %}
La balise `{% random %}` renvoie un nombre aléatoire. Vous pouvez l'utiliser pour une logique de type A/B, un échantillonnage ou pour varier le contenu des messages.

| Balise | Description |
|-------|--------------|
| `{% random %}` | Un float compris entre 0 et 1 (0 inclus, 1 exclu). |
| `{% random 10 %}` (argument entier) | Un entier allant de 0 jusqu'à l'entier spécifié, sans l'inclure. Par exemple, `{% random 10 %}` renvoie un entier de 0 à 9. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Envoyer des messages avec un nombre aléatoire" }

{% endraw %}

### Cas d'usage : envoyer des variantes aléatoires aux utilisateurs {#use-case-send-users-random-variants}

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

## Étiquette de panier d'achat eCommerce {#shopping-cart-tag}

L'étiquette `shopping_cart` accède au contenu du panier d'un utilisateur dans les cas d'usage eCommerce Canvas de [panier abandonné]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20cart#abandoned-cart) et de [paiement abandonné]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20checkout#abandoned-checkout). Remplacez `CART_ID` par la valeur réelle de l'ID du panier, comme {% raw %}`{{context.${cart_id}}}`{% endraw %}.

{% raw %}
```liquid
{% shopping_cart CART_ID :abort_if_not_abandoned false %}
```
{% endraw %}

Le paramètre `abort_if_not_abandoned` dans cet exemple s'applique uniquement au cas d'usage de [paiement abandonné]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20checkout#abandoned-checkout) lorsqu'il est utilisé avec l'événement `ecommerce.checkout_started`. Il ne s'applique pas aux cas d'usage de panier abandonné. Pour plus de détails, consultez [`abort_if_not_abandoned`]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20checkout#abort-if-not-abandoned).

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags