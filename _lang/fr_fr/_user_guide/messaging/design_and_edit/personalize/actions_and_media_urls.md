---
nav_title: URL d'action et de média
article_title: Personnaliser les URL d'action et de média avec Liquid
page_order: 2
description: "Cet article de référence explique comment personnaliser les URL d'action et de média à l'aide de Liquid."
---

# Personnaliser les URL d'action et de média avec Liquid {#personalize-action-and-media-urls-with-liquid}

> Personnalisez les destinations des liens et le contenu pour chaque utilisateur qui reçoit votre message en ajoutant des variables Liquid aux URL des boutons, liens, images et vidéos.

## Deep link vers du contenu in-app {#deep-link-to-in-app-content}

{% alert tip %}
**Pour les développeurs :** Pour les instructions d'intégration, consultez [Deep linking Android]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=android) ou [Deep linking Swift]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift). Pour vous aider à choisir un type de lien iOS, consultez le [guide de deep linking iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide). Pour diagnostiquer les problèmes, consultez [Résolution des problèmes de deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).
{% endalert %}

### Qu'est-ce que le deep linking ? {#what-is-deep-linking}

Le deep linking est un moyen de lancer une application native et de lui fournir des informations supplémentaires pour qu'elle effectue une action spécifique ou affiche un contenu spécifique.

Cela se compose de trois parties :

1. Identifier l'application à lancer.
2. Indiquer à l'application quelle action effectuer.
3. Fournir à l'action les données supplémentaires dont elle a besoin.

Les deep links sont des URI personnalisés qui renvoient vers une partie spécifique de l'application et contiennent ces trois éléments. L'élément clé est la définition d'un schéma personnalisé. `http:` est le schéma que presque tout le monde connaît, mais les schémas peuvent commencer par n'importe quel mot. Un schéma doit commencer par une lettre, mais peut ensuite contenir des lettres, des chiffres, des signes plus, des signes moins ou des points. En pratique, il n'existe pas de registre central pour éviter les conflits, il est donc recommandé d'inclure votre nom de domaine dans le schéma. Par exemple, `twitter://` est l'URI iOS pour lancer l'application mobile de X, anciennement Twitter.

Tout ce qui suit les deux-points dans un deep link est du texte libre. C'est à vous de définir sa structure et son interprétation ; cependant, une convention courante consiste à le modéliser d'après les URL `http:`, en incluant un `//` initial et des paramètres de requête (par exemple, `?foo=1&bar=2`). Pour l'exemple précédent, `twitter://user?screen_name=[id]` serait utilisé pour lancer un profil spécifique dans l'application.

{% alert important %}
Pour les applications créées avec des frameworks wrapper (par exemple, Flutter ou Cordova), Braze ne fournit pas de support de deep linking spécifique au wrapper. Vous devez configurer les deep links au niveau natif iOS et Android. Pour Cordova, consultez [Deep linking dans les notifications push]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=cordova).
{% endalert %}

### Schémas d'URI système {#system-uri-schemes}

Les schémas d'URI standard gérés nativement par iOS et Android (tels que `tel:`, `mailto:` et `sms:`) peuvent être saisis directement dans le champ d'URL du deep link sans nécessiter d'intégration de deep link personnalisée dans votre application.

| Schéma | Exemple | Action |
| ------ | ------- | ------ |
| `tel:` | `tel:+18005555555` | Ouvre le composeur téléphonique |
| `mailto:` | `mailto:support@example.com` | Ouvre la composition d'e-mail |
| `sms:` | `sms:+18005555555` | Ouvre la composition de SMS |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schémas d'URI système"}

Ceux-ci fonctionnent pour les comportements au clic des notifications push et les actions des boutons de messages in-app. Aucune configuration supplémentaire du SDK ni modification du code de l'application n'est nécessaire.

### Deep link vers l'application {#deep-link-into-application}

Lors de la composition de notifications push, de messages in-app, de Banners ou de Content Cards, sélectionnez **Deeplink into application** pour ouvrir un écran ou une action spécifique dans votre application. Dans certains éditeurs, cette option apparaît sous le nom **Deep Link Into App**.

Avant d'utiliser cette option, travaillez avec vos développeurs pour définir le format d'URI et configurer votre application pour l'ouvrir. Les schémas personnalisés, tels que `myapp://`, ouvrent directement l'application installée. Les liens universels (iOS) et les App Links (Android) utilisent des URL `https://` qui peuvent ouvrir l'application lorsqu'elle est installée et rediriger vers une page web lorsqu'elle ne l'est pas.

Pour définir ce comportement au clic :

1. Dans l'éditeur de votre Campaign ou Canvas, localisez **On-click behavior** :
   - Pour les notifications push et les Content Cards, accédez à l'onglet **Compose**.
   - Pour les messages in-app, accédez à l'onglet **Compose**. Dans l'éditeur par glisser-déposer, sélectionnez un bloc bouton ou image et ouvrez son panneau de propriétés.
2. Sélectionnez **Deeplink into application** ou **Deep Link Into App**.
3. Saisissez le lien dans le champ URL, par exemple `myapp://products/12345` pour un schéma personnalisé ou `https://example.com/products/12345` pour un lien universel ou un App Link.
4. Envoyez un message de test à un appareil physique. Un test réussi ouvre l'application et redirige vers l'écran ou l'action prévue. Pour un lien universel ou un App Link, testez également sur un appareil sans l'application installée pour confirmer le comportement de repli web attendu.

### Balises UTM et attribution de campagne {#utm-tags-and-campaign-attribution}

#### Qu'est-ce qu'une balise UTM ? {#what-is-a-utm-tag}

Les [balises UTM (Urchin Traffic gestionnaire)](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article) vous permettent d'inclure des détails d'attribution de campagne directement dans les liens. Les balises UTM sont utilisées par Google Analytics pour collecter des données d'attribution de campagne et peuvent être utilisées pour suivre les propriétés suivantes :

- `utm_source` : L'identifiant de la source du trafic (par exemple, `my_app`)
- `utm_medium` : Le support de la campagne (par exemple, `newsfeed`)
- `utm_campaign` : L'identifiant de la campagne (par exemple, `spring_2016_campaign`)
- `utm_term` : L'identifiant d'un terme de recherche payant qui a amené l'utilisateur vers votre application ou site web (par exemple, `pizza`)
- `utm_content` : Un identifiant pour le lien ou contenu spécifique sur lequel l'utilisateur a cliqué (par exemple, `toplink` ou `android_iam_button2`)

Les balises UTM peuvent être intégrées dans les liens HTTP (web) classiques et les deep links, et suivies à l'aide de Google Analytics.

##### Calculs des balises UTM {#utm-tag-calculations}

Braze rapporte le _Total des clics_ pour tous les liens d'une Campaign ou d'une étape Canvas, ce qui peut inclure des liens sans balises UTM. Cela signifie que vous pouvez voir un résultat différent (souvent inférieur) dans le suivi de vos liens de campagne Google Analytics par rapport au _Total des clics_ affiché dans les performances de votre campagne ou le générateur de rapports.

#### Utiliser les balises UTM avec Braze {#using-utm-tags-with-braze}

Si vous souhaitez utiliser des balises UTM avec des liens HTTP (web) classiques (par exemple, pour l'attribution de campagne de vos campagnes e-mail) et que votre organisation utilise déjà Google Analytics, vous pouvez utiliser le [générateur d'URL de Google](https://ga-dev-tools.google/ga4/campaign-url-builder/) pour générer des liens UTM. Ces liens peuvent être facilement intégrés dans le contenu de vos Campaigns Braze comme n'importe quel autre lien.

Pour utiliser des balises UTM dans les deep links vers votre application, celle-ci doit avoir le [SDK Google Analytics](https://developers.google.com/analytics/devguides/collection/) approprié intégré et correctement configuré pour gérer les deep links. Vérifiez auprès de vos développeurs si vous n'êtes pas sûr de cela.

Une fois le SDK Analytics intégré et configuré, les balises UTM peuvent être utilisées avec les deep links dans les Campaigns Braze. Pour configurer les balises UTM pour votre campagne, incluez les balises UTM nécessaires dans l'URL de destination ou les deep links. Les exemples suivants montrent comment utiliser les balises UTM dans les notifications push et les messages in-app.

##### Attribuer les ouvertures push et les clics de messages in-app avec les balises UTM {#attribute-push-opens-and-in-app-message-clicks-with-utm-tags}

{% tabs %}
{% tab Ouvertures push %}

Pour inclure des balises UTM dans vos deep links pour les notifications push, définissez le comportement au clic du message push comme un deep link, puis écrivez l'adresse du deep link et incluez les balises UTM souhaitées de la manière suivante :

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![Capture d'écran relative à l'attribution des ouvertures push et des clics de messages in-app avec les balises UTM.]({% image_buster /assets/img_archive/push_utm_tags.png %})

{% endtab %}
{% tab Clics de messages in-app %}

Pour inclure des balises UTM dans les deep links de vos messages in-app, utilisez ce qui suit :

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![Capture d'écran relative à l'attribution des ouvertures push et des clics de messages in-app avec les balises UTM.]({% image_buster /assets/img_archive/iam_utm_tags.png %})

{% endtab %}
{% endtabs %}

## Utiliser la personnalisation Liquid dans les URL {#use-liquid-personalization-in-urls}

Vous pouvez construire dynamiquement votre URL directement dans le compositeur Braze, ce qui vous permet d'ajouter des paramètres UTM dynamiques à vos URL ou d'envoyer aux utilisateurs des liens uniques (comme les diriger vers leur panier abandonné ou vers un produit spécifique de nouveau en stock).

### Créer une URL avec des balises de personnalisation Liquid prises en charge {#create-a-url-with-supported-liquid-personalization-tags}

Les URL peuvent être générées dynamiquement grâce à l'utilisation de n'importe quelles [balises de personnalisation Liquid prises en charge]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Nous prenons également en charge le raccourcissement des variables Liquid définies de manière personnalisée, comme dans les exemples suivants :

### Créer une URL à l'aide de variables Liquid {#create-a-url-using-liquid-variables}

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Raccourcir les URL rendues par des variables Liquid {#shorten-urls-rendered-by-liquid-variables}

**Canaux pris en charge :** KakaoTalk, LINE, SMS, RCS, WhatsApp

Nous raccourcissons les URL rendues par Liquid, y compris celles incluses dans les propriétés de déclenchement par API. Par exemple, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} représente une URL valide, nous raccourcissons et suivons cette URL avant d'envoyer le message.

### Raccourcir les URL dans l'endpoint `/messages/send` {#shorten-urls-in-messagessend-endpoint}

Le raccourcissement de liens est également activé pour les messages API uniquement via l'[endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages). Pour une liste complète des paramètres de requête, consultez les [paramètres de requête]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters).

| Paramètre | Obligatoire | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `link_shortening_enabled` | Oui | Booléen | Définissez `link_shortening_enabled` sur `true` pour activer le raccourcissement de liens. Pour utiliser le suivi, un `campaign_id` et un `message_variation_id` doivent être présents. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Raccourcir les URL dans l'endpoint /messages/send" }