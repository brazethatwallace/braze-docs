---
nav_title: Suivi des clics KakaoTalk
article_title: Suivi des clics KakaoTalk
page_order: 3
description: "Cette page explique comment activer le suivi des clics dans vos messages KakaoTalk, tester les liens raccourcis, utiliser votre domaine personnalisé dans les liens suivis, et plus encore."
page_type: reference
alias: /kakaotalk_click_tracking/
channel:
 - KakaoTalk
---

# Suivi des clics KakaoTalk {#kakaotalk-click-tracking}

> Cette page explique comment activer le suivi des clics dans vos messages KakaoTalk, tester les liens raccourcis, utiliser votre domaine personnalisé dans les liens suivis, et plus encore.

Lorsque le suivi des clics KakaoTalk est activé, Braze raccourcit automatiquement vos URL, ajoute des mécanismes de suivi et enregistre les clics en temps réel. Ces données vous permettent de créer des stratégies de segmentation et de reciblage plus ciblées, comme segmenter les utilisateurs en fonction de leur comportement de clic et déclencher des messages en réponse à des clics spécifiques.

Le suivi des clics KakaoTalk peut être utilisé pour les messages texte, image et éléments de liste. Il prend en charge les liens dans les boutons et les actions au clic sur les images. Vous pouvez également personnaliser les URL à l'aide de Liquid et de domaines personnalisés.

## Fonctionnement {#how-it-works}

Vous pouvez gérer les paramètres de suivi des clics KakaoTalk dans la section **Link options** du composeur. Lorsque cette option est activée, les URL sont raccourcies à l'aide du domaine Braze par défaut (`https://brz.ai`) ou du domaine personnalisé spécifié pour le groupe d'abonnement, et personnalisées pour l'utilisateur.

Toutes les URL commençant par `http://` ou `https://` seront raccourcies. Vous pouvez inclure jusqu'à 25 URL dans un message. Les URL raccourcies contenant une personnalisation Liquid (comme le suivi au niveau de l'utilisateur ou les paramètres UTM) seront valides pendant deux mois.

## Configurer le suivi des clics {#set-up-click-tracking}

### Messages texte {#text-messages}

Pour configurer le suivi des clics pour un message texte :

1. Composez un message **Text** et ajoutez une URL dans le champ de texte ou le bouton.
2. Dans la section **Link options** du composeur, vérifiez que **Click Tracking** est coché. Le suivi des clics est activé par défaut pour tous les nouveaux messages.

![Composeur de message texte KakaoTalk affichant la section Link options avec Click Tracking coché.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

### Messages image {#image-messages}

Pour configurer le suivi des clics pour un message image :

1. Composez un message **Image** et définissez le comportement au clic pour ouvrir une URL.
2. Saisissez une URL dans le champ URL.
3. Dans la section **Link options** du composeur, vérifiez que **Click Tracking** est coché.

### Messages éléments de liste {#list-item-messages}

Pour configurer le suivi des clics pour un message éléments de liste :

1. Composez un message **List item** et ajoutez une URL dans le champ **Website URL** pour n'importe quel élément.
2. Dans la section **Link options** du composeur, vérifiez que **Click Tracking** est coché.

## Domaines personnalisés {#custom-domains}

Le suivi des clics KakaoTalk vous permet d'utiliser votre propre domaine pour personnaliser l'apparence de vos URL raccourcies, contribuant ainsi à véhiculer une image de marque cohérente. Pour en savoir plus, consultez [Domaines personnalisés]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains).

## Personnalisation Liquid dans les URL {#liquid-personalization-in-urls}

Vous pouvez construire dynamiquement votre URL directement dans le composeur Braze, ce qui vous permet d'ajouter des paramètres UTM dynamiques à vos URL ou d'envoyer aux utilisateurs des liens uniques (comme les diriger vers leur panier abandonné ou vers un produit spécifique de nouveau en stock).

Les URL peuvent être générées dynamiquement grâce à n'importe quelle balise de personnalisation Liquid prise en charge.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Vous pouvez également raccourcir des variables Liquid définies de manière personnalisée, comme illustré dans l'exemple suivant :

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

Braze raccourcit les URL rendues par Liquid, y compris celles incluses dans les propriétés de déclenchement API. Par exemple, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} représente une URL valide, Braze raccourcira et suivra cette URL avant d'envoyer le message KakaoTalk.

## Tests {#testing}

Avant de lancer votre campagne ou votre Canvas, il est recommandé de prévisualiser et de tester votre message au préalable. Pour ce faire, accédez à l'onglet **Test** pour prévisualiser et envoyer un message KakaoTalk à des groupes de test de contenu ou à un utilisateur individuel.

La prévisualisation sera mise à jour avec la personnalisation pertinente et l'URL raccourcie.

{% alert important %}
Si un brouillon est créé au sein d'un Canvas actif, une URL raccourcie ne sera pas générée. L'URL raccourcie réelle est générée lorsque le brouillon du Canvas est rendu actif.
{% endalert %}

## Rapports {#reporting}

Le tableau de performance KakaoTalk inclut la colonne **Total Clicks** qui affiche un décompte des événements de clic par variante et un taux de clics associé. Pour plus de détails sur les indicateurs KakaoTalk, consultez [Rapports KakaoTalk]({{site.baseurl}}/kakaotalk_reporting).

Les données de clics sont automatiquement reportées dans le tableau de bord d'analyse.

## Recibler les utilisateurs {#retarget-users}

Vous pouvez recibler les utilisateurs qui ont cliqué sur une URL dans un message KakaoTalk en utilisant les filtres de segmentation et déclencheurs suivants :

- Déclencheurs basés sur l'action
    - Interact with Campaign
    - Interact with Step

- Filtres de segmentation
    - Clicked/Opened Campaign
    - Clicked/Opened Campaign or Canvas with Tag
    - Clicked/Opened Step

## Questions fréquemment posées {#frequently-asked-questions}

### Les liens que je reçois lors d'un envoi test sont-ils de vraies URL ? {#are-the-links-i-receive-when-test-sending-real-urls}

Oui, de vraies URL sont générées lors d'un envoi test. Cependant, l'URL exacte envoyée dans une campagne lancée peut différer de celle envoyée lors d'un envoi test.

### Puis-je ajouter des paramètres UTM à une URL avant qu'elle ne soit raccourcie ? {#can-i-add-utm-parameters-to-a-url-before-it-is-shortened}

Oui, des paramètres statiques et dynamiques peuvent être ajoutés.

### Combien de temps les URL raccourcies restent-elles valides ? {#how-long-do-shortened-urls-remain-valid}

Les URL personnalisées sont valides pendant deux mois à compter de l'enregistrement de l'URL.

### Le SDK Braze doit-il être installé pour raccourcir les URL ? {#does-the-braze-sdk-need-to-be-installed-in-order-to-shorten-urls}

Non, le suivi des clics fonctionne sans aucune intégration SDK.

### Puis-je savoir quels utilisateurs individuels cliquent sur une URL ? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Oui. Lorsque le suivi des clics est activé, vous pouvez recibler les utilisateurs qui ont cliqué sur des URL en utilisant les [filtres de reciblage KakaoTalk](#retargeting-users).

### Le suivi des clics fonctionne-t-il avec les liens profonds ou les liens universels ? {#does-click-tracking-work-with-deep-links-or-universal-links}

Le suivi des clics s'applique aux URL web. Pour les liens profonds, vous pouvez définir un lien profond directement comme type d'action au clic pour les boutons dans KakaoTalk — ceux-ci ne passent pas par le raccourcissement d'URL ni le suivi des clics. Si vous préférez utiliser des liens universels de fournisseurs tels que Branch or branche ou Appsflyer, ceux-ci peuvent être raccourcis, mais Braze n'est pas en mesure de résoudre les problèmes qui pourraient survenir (comme la rupture de l'attribution ou l'échec de la redirection).