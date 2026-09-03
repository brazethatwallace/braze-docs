---
nav_title: Suivi des clics LINE
article_title: Suivi des clics LINE
page_order: 2
description: "Cette page explique comment activer le suivi des clics dans vos messages LINE, tester les liens raccourcis, utiliser votre domaine personnalisé dans les liens suivis, et plus encore."
page_type: reference
alias: /line/click_tracking/
channel:
 - LINE
---

# Suivi des clics LINE {#line-click-tracking}

> Cette page explique comment activer le suivi des clics dans vos messages LINE, tester les liens raccourcis, utiliser votre domaine personnalisé dans les liens suivis, et plus encore.


Lorsque le suivi des clics LINE est activé, Braze raccourcit automatiquement vos URL, ajoute des mécanismes de suivi et enregistre les clics en temps réel. Bien que LINE vous fournisse des données de clics agrégées, Braze offre des informations granulaires au niveau de l'utilisateur, à la fois pertinentes et exploitables. Ces données vous permettent de créer des stratégies de segmentation et de reciblage plus ciblées, comme segmenter les utilisateurs en fonction de leur comportement de clic et déclencher des messages en réponse à des clics spécifiques.

Le suivi des clics LINE peut être utilisé pour les messages texte, les messages enrichis et les messages à base de cartes. Il prend en charge les liens dans les boutons et les zones d'image cliquables ayant une URL comme action au clic. Vous pouvez également personnaliser les URL à l'aide de Liquid et de domaines personnalisés.

## Fonctionnement {#how-it-works}

Vous pouvez gérer les paramètres de suivi des clics LINE dans l'onglet **Settings** lors de la composition d'un message. Lorsque cette option est activée, les URL sont raccourcies à l'aide du domaine Braze par défaut (`https://brz.ai`) ou du domaine personnalisé spécifié pour le groupe d'abonnement, et personnalisées pour l'utilisateur.

Toutes les URL commençant par `http://` ou `https://` seront raccourcies. Vous pouvez inclure jusqu'à 25 URL dans un message. Les URL raccourcies contenant une personnalisation Liquid (comme le suivi au niveau de l'utilisateur ou les paramètres UTM) seront valides pendant deux mois.

## Configuration du suivi des clics {#setting-up-click-tracking}

### Messages texte {#text-messages}

Pour configurer le suivi des clics pour un message texte :

1. Glissez un message **Texte** dans le compositeur et ajoutez une URL dans le champ texte.

![Compositeur de messages LINE avec un message texte contenant une longue URL avant raccourcissement.]({% image_buster /assets/img/line/click_tracking_text_message.png %})

{: start="2"}
2. Accédez à l'onglet **Settings** et confirmez que le **Click Tracking** est activé. Le suivi des clics est activé par défaut pour tous les nouveaux messages.

{% alert note %}
Vous pouvez afficher un aperçu du lien raccourci dans l'onglet **Settings** ou **Preview & Test**. Le lien complet s'affichera dans le compositeur pendant que vous créez votre message.
{% endalert %}

![Onglet « Settings » du compositeur de messages LINE avec le « Click Tracking » activé et un aperçu de message texte contenant une URL raccourcie : https://olaf.brz.ai/p/9rcfdqdD]({% image_buster /assets/img/line/click_tracking_settings.png %})

### Messages enrichis {#rich-messages}

Pour configurer le suivi des clics pour un message enrichi :

1. Glissez un **Rich message** dans le compositeur et sélectionnez un modèle.
2. Sélectionnez **URI** pour le **On-click behavior** de la zone cliquable concernée.
3. Saisissez une URL dans le champ **Open URL**.

![Compositeur de messages LINE avec un message enrichi comportant deux zones cliquables ayant chacune une URL.]({% image_buster /assets/img/line/rich_message_click_tracking.png %})

{: start="4"}
4. Accédez à l'onglet **Settings** et confirmez que le **Click Tracking** est activé. Le suivi des clics est activé par défaut pour tous les nouveaux messages.

### Messages à base de cartes {#card-based-messages}

Pour configurer le suivi des clics pour un message à base de cartes :

1. Glissez un **Card-based message** dans le compositeur.
2. Sélectionnez **URI** pour le **On-click behavior** de la carte ou des boutons concernés.

![Compositeur de messages LINE avec un message à base de cartes comportant deux boutons ayant chacun une URL.]({% image_buster /assets/img/line/card_based_message_click_tracking.png %})

{: start="3"}
3. Accédez à l'onglet **Settings** et confirmez que le **Click Tracking** est activé. Le suivi des clics est activé par défaut pour tous les nouveaux messages.

{% alert note %}
Les URL dans les champs **Title** ou **Description** ne seront pas raccourcies, car ces champs ne sont pas cliquables dans LINE.
{% endalert %}

## Domaines personnalisés {#custom-domains}

Le suivi des clics LINE vous permet d'utiliser votre propre domaine pour personnaliser l'apparence de vos URL raccourcies, contribuant ainsi à véhiculer une image de marque cohérente. Pour plus d'informations, consultez [Domaines personnalisés]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains).

## Personnalisation Liquid dans les URL {#liquid-personalization-in-urls}

Vous pouvez construire dynamiquement votre URL directement dans le compositeur Braze, ce qui vous permet d'ajouter des paramètres UTM dynamiques à vos URL ou d'envoyer aux utilisateurs des liens uniques (par exemple, diriger les utilisateurs vers leur panier abandonné ou vers un produit spécifique de nouveau en stock).
Vous pouvez générer dynamiquement des URL en utilisant n'importe quelle balise de personnalisation Liquid prise en charge.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Vous pouvez également raccourcir les variables Liquid personnalisées, comme illustré dans l'exemple suivant :

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Raccourcir les URL rendues par des variables Liquid {#shorten-urls-rendered-by-liquid-variables}

Braze raccourcit les URL rendues par Liquid, y compris celles incluses dans les propriétés de déclencheur d'API. Par exemple, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} représente une URL valide, nous raccourcissons et suivons cette URL avant d'envoyer le message LINE.

## Tests {#testing}

Avant de lancer votre Campaign ou Canvas, il est recommandé de prévisualiser et de tester votre message au préalable. Pour ce faire, accédez à l'onglet **Test** pour prévisualiser et envoyer un message LINE à des groupes de test de contenu ou à un utilisateur individuel.

Cette prévisualisation sera mise à jour avec la personnalisation pertinente et l'URL raccourcie.

{% alert important %}
Si un brouillon est créé dans un Canvas actif, une URL raccourcie ne sera pas générée. L'URL raccourcie réelle est générée lorsque le brouillon du Canvas est rendu actif.
{% endalert %}

## Rapports {#reporting}

Le tableau de performance LINE comprend la colonne **Total Clicks** qui affiche le nombre d'événements de clics par variante et le taux de clics associé. Pour plus de détails sur les indicateurs LINE, consultez [Performance des messages LINE]({{site.baseurl}}/user_guide/channels/line/reporting).

![Performance d'une étape Canvas LINE.]({% image_buster /assets/img/line/line_step_performance.png %}){: style="max-width:30%;"}

Les données de clics sont automatiquement reportées dans le tableau de bord d'analyse.

![Tableau de bord d'analyse des performances LINE.]({% image_buster /assets/img/line/line_performance.png %})

## Reciblage des utilisateurs {#retargeting-users}

Vous pouvez recibler les utilisateurs qui ont cliqué sur une URL dans un message LINE en utilisant les filtres de segmentation et les déclencheurs suivants :

- Déclencheurs par événement
    - Interagir avec une Campaign
    - Interagir avec une étape

![Déclencheur de livraison par événement LINE.]({% image_buster /assets/img/line/line_action_based.png %})

- Filtres de segmentation
    - A cliqué/ouvert une Campaign
    - A cliqué/ouvert une Campaign ou un Canvas avec une étiquette
    - A cliqué/ouvert une étape

![Groupe de filtres affichant les trois filtres de segmentation : « A cliqué/ouvert une Campaign », « A cliqué/ouvert une Campaign ou un Canvas avec une étiquette » et « A cliqué/ouvert une étape ».]({% image_buster /assets/img/line/line_segmentation_filters.png %})

## Questions fréquentes {#frequently-asked-questions}

### Les liens que je reçois lors d'un envoi de test sont-ils de vraies URL ? {#are-the-links-i-receive-when-test-sending-real-urls}

Oui, de vraies URL sont générées lors d'un envoi de test. Cependant, l'URL exacte envoyée dans une Campaign lancée peut différer de celle envoyée lors d'un envoi de test.

### Puis-je ajouter des paramètres UTM à une URL avant qu'elle ne soit raccourcie ? {#can-i-add-utm-parameters-to-a-url-before-it-is-shortened}

Oui, des paramètres statiques et dynamiques peuvent être ajoutés.

### Combien de temps les URL raccourcies restent-elles valides ? {#how-long-do-shortened-urls-remain-valid}

Les URL personnalisées sont valides pendant deux mois à compter de l'enregistrement de l'URL.

### Le SDK Braze doit-il être installé pour raccourcir les URL ? {#does-the-braze-sdk-need-to-be-installed-in-order-to-shorten-urls}

Non, le suivi des clics fonctionne sans aucune intégration SDK.

### Puis-je savoir quels utilisateurs individuels cliquent sur une URL ? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Oui. Lorsque le suivi des clics est activé, vous pouvez recibler les utilisateurs qui ont cliqué sur des URL en utilisant les [filtres de reciblage LINE](#retargeting-users).

### Le suivi des clics fonctionne-t-il avec les deep links ou les liens universels ? {#does-click-tracking-work-with-deep-links-or-universal-links}

Le suivi des clics ne fonctionne pas avec les deep links. Vous pouvez raccourcir les liens universels de fournisseurs tels que Branch ou Appsflyer, mais Braze n'est pas en mesure de résoudre les problèmes qui pourraient survenir en faisant cela (tels que la rupture de l'attribution ou l'échec de la redirection).

### Les aperçus dans l'application LINE comptent-ils comme des clics ? {#do-previews-on-the-line-app-count-as-clicks}

Non, ils ne contribuent pas au taux de clics pour les messages LINE.