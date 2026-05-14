---
nav_title: URL d'action et de média
article_title: Personnaliser les URL d'action et de média avec Liquid
page_order: 2
description: "Cet article de référence explique comment personnaliser les URL d'action et de média à l'aide de Liquid."
---

# Personnaliser les URL d'action et de média avec Liquid {#personalize-action-and-media-urls-with-liquid}

> Personnalisez les destinations des liens et le contenu pour chaque utilisateur qui reçoit votre message en ajoutant des variables Liquid aux URL des boutons, liens, images et vidéos.

## Lien profond vers du contenu in-app {#deep-link-to-in-app-content}

{% alert tip %}
**Pour les développeurs :** Pour un guide sur le choix entre les schémas personnalisés, les liens universels et d'autres options — y compris quand vous avez besoin d'un fichier AASA, quelles méthodes de délégué d'application implémenter et comment déboguer les problèmes — consultez le [Guide de création de liens profonds iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide/) et la [Résolution des problèmes de création de liens profonds]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting/).
{% endalert %}

### Qu'est-ce que la création de liens profonds ? {#what-is-deep-linking}

La création de liens profonds est un moyen de lancer une application native et de lui fournir des informations supplémentaires pour effectuer une action spécifique ou afficher un contenu spécifique.

Cela comporte trois parties :

1. Identifier quelle application lancer.
2. Indiquer à l'application quelle action effectuer.
3. Fournir à l'action toutes les données supplémentaires dont elle aura besoin.

Les liens profonds sont des URI personnalisés qui renvoient vers une partie spécifique de l'application et contiennent ces trois éléments. L'essentiel est de définir un schéma personnalisé. `http:` est le schéma que presque tout le monde connaît, mais les schémas peuvent commencer par n'importe quel mot. Un schéma doit commencer par une lettre, mais peut ensuite contenir des lettres, des chiffres, des signes plus, des signes moins ou des points. En pratique, il n'existe pas de registre central pour éviter les conflits, il est donc recommandé d'inclure votre nom de domaine dans le schéma. Par exemple, `twitter://` est l'URI iOS pour lancer l'application mobile de X, anciennement Twitter.

Tout ce qui suit les deux-points dans un lien profond est du texte libre. C'est à vous de définir sa structure et son interprétation ; cependant, une convention courante consiste à le modéliser d'après les URL `http:`, en incluant un `//` initial et des paramètres de requête (par exemple, `?foo=1&bar=2`). Pour l'exemple précédent, `twitter://user?screen_name=[id]` serait utilisé pour lancer un profil spécifique dans l'application.

{% alert important %}
Pour les applications créées avec des frameworks wrapper (par exemple, Flutter ou Cordova), Braze ne fournit pas de support de création de liens profonds spécifique au wrapper. Vous devez configurer les liens profonds au niveau des couches natives iOS et Android. Pour Cordova, consultez [Liens profonds dans les notifications push]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=cordova).
{% endalert %}

### Balises UTM et attribution de campagne {#utm-tags-and-campaign-attribution}

#### Qu'est-ce qu'une balise UTM ? {#what-is-a-utm-tag}

Les [balises UTM (Urchin Traffic Manager)](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article) vous permettent d'inclure des détails d'attribution de campagne directement dans les liens. Les balises UTM sont utilisées par Google Analytics pour collecter des données d'attribution de campagne et peuvent servir à suivre les propriétés suivantes :

- `utm_source` : l'identifiant de la source du trafic (par exemple, `my_app`)
- `utm_medium` : le support de la campagne (par exemple, `newsfeed`)
- `utm_campaign` : l'identifiant de la campagne (par exemple, `spring_2016_campaign`)
- `utm_term` : l'identifiant d'un terme de recherche payante qui a amené l'utilisateur vers votre application ou site web (par exemple, `pizza`)
- `utm_content` : un identifiant pour le lien ou contenu spécifique sur lequel l'utilisateur a cliqué (par exemple, `toplink` ou `android_iam_button2`)

Les balises UTM peuvent être intégrées dans les liens HTTP classiques (web) et les liens profonds, et suivies à l'aide de Google Analytics.

##### Calculs des balises UTM {#utm-tag-calculations}

Braze rapporte le _Total des clics_ pour tous les liens d'une campagne ou d'une étape du canvas, ce qui peut inclure des liens sans balises UTM. Cela signifie que vous pouvez voir un résultat différent (souvent inférieur) dans vos liens de suivi de campagne Google Analytics par rapport au _Total des clics_ affiché dans les performances de votre campagne ou le Générateur de rapports.

#### Utiliser les balises UTM avec Braze {#using-utm-tags-with-braze}

Si vous souhaitez utiliser des balises UTM avec des liens HTTP classiques (web) (par exemple, pour l'attribution de campagne de vos campagnes e-mail) et que votre organisation utilise déjà Google Analytics, vous pouvez utiliser le [générateur d'URL de Google](https://ga-dev-tools.google/ga4/campaign-url-builder/) pour générer des liens UTM. Ces liens peuvent être facilement intégrés dans le contenu de vos campagnes Braze comme n'importe quel autre lien.

Pour utiliser des balises UTM dans les liens profonds vers votre application, celle-ci doit avoir le [SDK Google Analytics](https://developers.google.com/analytics/devguides/collection/) approprié intégré et correctement configuré pour gérer les liens profonds. Vérifiez auprès de vos développeurs si vous n'êtes pas sûr de cela.

Une fois le SDK Analytics intégré et configuré, les balises UTM peuvent être utilisées avec les liens profonds dans les campagnes Braze. Pour configurer les balises UTM pour votre campagne, incluez les balises UTM nécessaires dans l'URL de destination ou les liens profonds. Les exemples suivants montrent comment utiliser les balises UTM dans les notifications push et les messages in-app.

##### Attribuer les ouvertures push et les clics sur les messages in-app avec les balises UTM {#attribute-push-opens-and-in-app-message-clicks-with-utm-tags}

{% tabs %}
{% tab Ouvertures push %}

Pour inclure des balises UTM dans vos liens profonds pour les notifications push, définissez le comportement au clic du message push comme un lien profond, puis écrivez l'adresse du lien profond et incluez les balises UTM souhaitées de la manière suivante :

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![]({% image_buster /assets/img_archive/push_utm_tags.png %})

{% endtab %}
{% tab Clics sur les messages in-app %}

Pour inclure des balises UTM dans les liens profonds de vos messages in-app, utilisez ce qui suit :

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![]({% image_buster /assets/img_archive/iam_utm_tags.png %})

{% endtab %}
{% endtabs %}

## Utiliser la personnalisation Liquid dans les URL {#use-liquid-personalization-in-urls}

Vous pouvez construire dynamiquement votre URL directement dans le compositeur Braze, ce qui vous permet d'ajouter des paramètres UTM dynamiques à vos URL ou d'envoyer aux utilisateurs des liens uniques (comme diriger les utilisateurs vers leur panier abandonné ou vers un produit spécifique de nouveau en stock).

### Créer une URL avec des balises de personnalisation Liquid prises en charge {#create-a-url-with-supported-liquid-personalization-tags}

Les URL peuvent être générées dynamiquement grâce à n'importe quelle [balise de personnalisation Liquid prise en charge]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Nous prenons également en charge le raccourcissement des variables Liquid personnalisées. Voici quelques exemples :

### Créer une URL à l'aide de variables Liquid {#create-a-url-using-liquid-variables}

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Raccourcir les URL générées par des variables Liquid {#shorten-urls-rendered-by-liquid-variables}

**Canaux pris en charge :** KakaoTalk, LINE, SMS, RCS, WhatsApp

Nous raccourcissons les URL générées par Liquid, y compris celles incluses dans les propriétés de déclenchement API. Par exemple, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} représente une URL valide, nous raccourcissons et suivons cette URL avant d'envoyer le message.

### Raccourcir les URL dans l'endpoint `/messages/send` {#shorten-urls-in-messagessend-endpoint}

Le raccourcissement de liens est également activé pour les messages API uniquement via l'[endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Pour une liste complète des paramètres de requête, consultez les [paramètres de requête]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `link_shortening_enabled` | Oui | Valeur booléenne | Définissez `link_shortening_enabled` sur `true` pour activer le raccourcissement de liens. Pour utiliser le suivi, un `campaign_id` et un `message_variation_id` doivent être présents. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Shorten URLs in /messages/send endpoint" }