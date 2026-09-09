---
nav_title: "Créer une bannière"
article_title: "Créer une bannière"
page_order: 1
description: "Cet article de référence explique comment créer, rédiger, configurer et envoyer des bannières à l'aide de Campaigns et de Canvas Braze."
tool:
  - Campaigns
channel:
  - banners
---

# Créer une bannière {#create-a-banner}

> Découvrez comment créer des bannières lors de la conception de Campaigns et de Canvas dans Braze. Pour des informations plus générales, consultez [À propos des bannières]({{site.baseurl}}/user_guide/channels/banners).

## Prérequis {#prerequisites}

Avant de pouvoir lancer votre Banner, votre équipe de développement doit [configurer les placements dans votre application ou votre site web]({{site.baseurl}}/developer_guide/banners/placements). Vous pouvez tout de même préparer votre campagne Banner en attendant, mais vous ne pourrez pas lancer la campagne tant que les placements ne seront pas configurés.

## Créer un message Banner {#create-a-banner-message}

{% multi_lang_include banners/creating_placements.md section="user" %}

### Étape 2 : Choisir où créer votre message {#step-2-choose-where-to-build-your-message}

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les Campaigns sont plus adaptées aux campagnes de communication ciblées ponctuelles, tandis que les Canvas sont plus adaptés aux parcours utilisateur en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

1. Allez dans **Messagerie** > **Campaigns** et sélectionnez **Créer une campagne**.
2. Sélectionnez **Banner**.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) et des [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) selon vos besoins. Les tags facilitent la recherche de vos campagnes et la création de rapports. Par exemple, lorsque vous utilisez le générateur de rapports, vous pouvez filtrer par les tags pertinents.
5. Sélectionnez l'emplacement que vous avez créé précédemment pour l'associer à votre campagne.
6. Ajoutez des variantes selon vos besoins. Vous pouvez choisir un type de message et une mise en page différents pour chacune. Pour plus d'informations sur les variantes, consultez [Test multivarié et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).
7. Choisissez une date et une heure de début pour votre campagne Banner. Par défaut, les Banners durent indéfiniment. Vous pouvez modifier cela en sélectionnant **Heure de fin** et en spécifiant une date et une heure de fin.

{% alert tip %}
Si tous les messages de votre campagne sont similaires ou ont le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite sélectionner **Copier depuis la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) à l'aide du compositeur de Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape Message dans le générateur de Canvas. Donnez à votre étape un nom clair et significatif.
3. Sélectionnez **Banner** comme canal de communication.
4. Sélectionnez un emplacement pour le Banner.
5. Définissez la priorité. La [priorité du Banner]({{site.baseurl}}/user_guide/channels/banners#priority) détermine l'ordre d'affichage des Banners lorsqu'ils partagent le même emplacement.
6. Définissez une expiration pour le Banner. Celle-ci peut survenir après une durée déterminée à compter de la disponibilité de l'étape, ou à une date et une heure spécifiques. La durée maximale d'expiration est de 31 jours après que l'étape est devenue disponible pour l'utilisateur.

{% endtab %}
{% endtabs %}

### Étape 3 : Composer un Banner {#compose-a-banner}

Ensuite, choisissez comment vous souhaitez commencer :

- **Éditeur par glisser-déposer :** Commencez avec un Banner vierge et construisez visuellement avec des blocs et des lignes.
- **Éditeur HTML :** Commencez avec un Banner vierge et travaillez directement en HTML.
- **Modèles :** Ouvrez la bibliothèque de modèles et sélectionnez un design dans **Modèles Braze** ou **Vos modèles**. Les modèles s'ouvrent dans l'éditeur par glisser-déposer pour personnalisation.

![Options pour choisir l'éditeur par glisser-déposer, l'éditeur HTML ou les modèles pour votre Banner.]({% image_buster /assets/img/banners/choose_banner_editing_experience.png %})

#### Étape 3.1 : Styliser le Banner {#step-31-style-the-banner}

{% tabs %}
{% tab Éditeur par glisser-déposer %}

Vous pouvez glisser-déposer des blocs et des lignes dans la zone de canevas pour commencer à construire votre message. Pour une référence des blocs de l'éditeur de Banner et des liens vers les détails des propriétés partagées, consultez [Blocs éditeur (Banners)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=banners).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Pour personnaliser les propriétés d'arrière-plan, les paramètres de bordure et plus encore de votre message, sélectionnez **Styles**. Si vous souhaitez personnaliser le style uniquement pour un bloc ou une ligne spécifique, sélectionnez-le pour effectuer les modifications.

![Panneau de styles du compositeur de Banner.]({% image_buster /assets/img/banners/banner_card_styles.png %})

{% endtab %}
{% tab Éditeur HTML %}

L'éditeur HTML est idéal pour les équipes qui maintiennent déjà leurs propres modèles HTML ou qui souhaitent un contrôle total sur le balisage et le style. Vous pouvez écrire ou coller du HTML personnalisé directement dans l'éditeur. Les balises de personnalisation Liquid sont entièrement prises en charge, vous pouvez donc référencer des attributs utilisateur, des attributs personnalisés, des éléments de catalogue, et bien plus encore.

{% alert tip %}
Besoin d'aide pour créer le HTML de votre Banner ? Sélectionnez **Ask Operator** dans l'éditeur HTML et décrivez le Banner que vous souhaitez. [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator) génère du HTML que vous pouvez examiner et insérer dans l'éditeur. Pour plus d'informations, consultez [Générer des messages]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages).
{% endalert %}

Pour le suivi des clics et des fermetures dans votre HTML personnalisé, vous devez appeler explicitement les méthodes du pont JavaScript. Pour la référence complète, consultez [Code personnalisé et pont JavaScript pour les Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code).

{% endtab %}
{% endtabs %}

{% alert note %}
Pour cibler des utilisateurs dans différentes langues au sein d'une seule campagne Banner, consultez [Messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).
{% endalert %}

#### Étape 3.2 : Définir le comportement au clic (facultatif) {#step-32-define-on-click-behavior-optional}

{% tabs %}
{% tab Éditeur par glisser-déposer %}

Lorsqu'un utilisateur clique sur un lien dans le Banner, vous pouvez choisir de le rediriger plus profondément dans votre application ou vers une autre page web. De plus, vous pouvez choisir d'[enregistrer un attribut ou un événement personnalisé]({{site.baseurl}}/developer_guide/analytics), ce qui met à jour le profil de votre utilisateur avec des données personnalisées lorsqu'il clique sur le Banner. Pour un suivi des clics plus granulaire, attribuez un identifiant personnalisé à chaque élément interactif à l'aide du champ **Identifiant pour le reporting** dans son panneau de propriétés.

{% alert important %}
{::nomarkdown}
Le comportement au clic peut être remplacé si un élément spécifique (comme un bouton, un lien ou une image du Banner) possède son propre comportement au clic. Par exemple, étant donné les comportements au clic suivants :<br><ul><li>Un Banner a un comportement au clic qui redirige vers la page d'accueil d'un site web.</li><li>Une image dans le Banner a un comportement au clic qui redirige vers la page produit d'un site web.</li></ul>Si un utilisateur clique sur l'image, il est redirigé vers la page produit. Cependant, cliquer sur la zone environnante du Banner le redirige vers la page d'accueil.
{:/}
{% endalert %}

{% endtab %}
{% tab Éditeur HTML %}

Dans l'éditeur HTML, le suivi des clics n'est pas automatique. Vous devez appeler `brazeBridge.logClick()` depuis votre HTML pour chaque élément cliquable que vous souhaitez suivre. Par exemple :

```html
<a href="https://example.com" onclick="brazeBridge.logClick()">Shop now</a>
```

Pour la référence complète du pont JavaScript, consultez [Code personnalisé et pont JavaScript pour les Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).

{% endtab %}
{% endtabs %}

#### Étape 3.3 : Configurer le comportement de fermeture (facultatif) {#dismiss-behavior}

{% alert important %}
Les fermetures de Banner nécessitent les versions minimales de SDK suivantes. Les versions antérieures du SDK n'affichent pas les Banners avec la fermeture activée.
{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 reactnative:22.0.0 flutter:20.0.0 %}
{% endalert %}

{% tabs %}
{% tab Éditeur par glisser-déposer %}

Cochez la case **Le Banner peut être fermé** dans la section **Comportement de fermeture** pour permettre aux utilisateurs de fermer le Banner. C'est utile lorsque vous souhaitez promouvoir une offre à durée limitée auprès d'une large audience tout en laissant les utilisateurs non intéressés masquer le message.

Lorsque la fermeture est activée, vous pouvez personnaliser le bouton de fermeture dans la section **Comportement de fermeture** :

| Paramètre | Description |
|---------|-------------|
| **Taille du bouton** | La taille du bouton de fermeture affiché sur le Banner. |
| **Couleur du bouton** | La couleur du bouton de fermeture. |
| **Libellé ARIA** | Le libellé accessible pour le bouton de fermeture, utilisé par les lecteurs d'écran. Par défaut « Fermer » si laissé vide. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paramètres du bouton de fermeture" }

Lorsqu'un utilisateur ferme un Banner, celui-ci ne réapparaît plus pour cet utilisateur, même s'il remplit toujours les critères de ciblage de la campagne.

{% endtab %}
{% tab Éditeur HTML %}

Dans l'éditeur HTML, la fermeture est gérée dans votre HTML à l'aide de `brazeBridge.closeMessage()`. Associez-le à `brazeBridge.logClick()` pour également enregistrer l'action de fermeture comme un événement de clic. Par exemple :

```html
<a href="#" onclick="brazeBridge.logClick(); brazeBridge.closeMessage();">&#x2715; Close</a>
```

Lorsqu'un utilisateur ferme un Banner de cette manière, celui-ci ne réapparaît plus pour cet utilisateur, même s'il remplit toujours les critères de ciblage de la campagne.

Pour la référence complète du pont JavaScript, consultez [Code personnalisé et pont JavaScript pour les Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).

{% endtab %}
{% endtabs %}

#### Étape 3.4 : Ajouter des propriétés personnalisées (facultatif) {#custom-properties}

Vous pouvez ajouter des propriétés personnalisées à un Banner pour y associer des métadonnées structurées, telles que des chaînes de caractères ou des objets JSON. Ces propriétés n'affectent pas l'affichage du Banner, mais peuvent être [accessibles via le SDK Braze]({{site.baseurl}}/developer_guide/banners/placements) pour modifier le comportement ou l'apparence de votre application. Par exemple, vous pourriez :

{% multi_lang_include banners/metadata_use_cases.md %}

Les propriétés personnalisées fonctionnent de la même manière dans l'éditeur par glisser-déposer et dans l'éditeur HTML. Pour ajouter une propriété personnalisée, sélectionnez **Paramètres** > **Propriétés** > **Ajouter une propriété**.

![La page des propriétés affichant l'option d'ajouter la première propriété personnalisée à une campagne Banner.]({% image_buster /assets/img/banners/add_property.png %})

Pour chaque propriété que vous souhaitez ajouter, remplissez les champs suivants :

| Champ | Description | Exemple |
|-------|-------------|---------|
| Type de propriété | Le type de données pour la propriété. Les types pris en charge incluent chaîne de caractères, booléen, nombre, horodatage, URL d'image et objet JSON. | String |
| Clé de la propriété | L'identifiant unique de la propriété. Cette clé est utilisée dans le SDK pour accéder à la propriété. | `color` |
| Valeur | La valeur attribuée à la propriété. Elle doit correspondre au type de propriété sélectionné. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 3.4 : Ajouter des propriétés personnalisées (facultatif)" }

Lorsque vous avez terminé, sélectionnez **Terminé**.

![La page des propriétés avec une propriété de type chaîne ayant une clé color et une valeur #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

#### Étape 3.5 : Personnaliser avec le contenu connecté (facultatif) {#step-35-personalize-with-connected-content-optional}

{% multi_lang_include alerts/early_access_beta_alert.md feature='Connected Content for Banners' %}

Comme les Banners s'affichent en ligne lors d'une actualisation de session, le contenu connecté dans ce canal fonctionne différemment des autres canaux :

- Seules les requêtes GET sont prises en charge.
- Tous les emplacements d'une même actualisation (jusqu'à 10) partagent un budget de rendu d'environ deux secondes. Si un appel est lent, expire ou si le budget est dépassé, le résultat du contenu connecté pour cet emplacement est traité comme nul. Les Banners ne réessaient pas.

Pour de meilleurs résultats :

- Gardez vos endpoints rapides et [mettez en cache les réponses]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) autant que possible.
- Limitez le nombre d'URL de contenu connecté uniques parmi les emplacements qui s'affichent ensemble.
- Évitez d'enchaîner les appels où une réponse de contenu connecté détermine l'URL de l'appel suivant. Chaque appel supplémentaire s'ajoute au budget partagé.
- Utilisez des instructions de garde Liquid ou le [filtre `default`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) pour gérer les résultats nuls et éviter les Banners vides.

### Étape 4 : Construire le reste de votre campagne ou Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Définir la priorité du Banner (facultatif) {#set-banner-priority-optional}

La [priorité du Banner]({{site.baseurl}}/user_guide/channels/banners#priority) détermine l'ordre d'affichage des Banners lorsqu'ils partagent le même emplacement. Pour définir manuellement la priorité :

1. Sélectionnez **Set exact priority**.
2. Glissez-déposez les campagnes pour les ordonner avec la bonne priorité.
3. Sélectionnez **Apply Sort**.

{% alert tip %}
Si vous avez plusieurs campagnes Banner utilisant le même ID d'emplacement, nous vous recommandons d'utiliser le trieur de priorité par glisser-déposer pour définir la priorité exacte.
{% endalert %}

#### Configurer la rééligibilité (facultatif) {#re-eligibility}

Par défaut, les utilisateurs qui ferment un Banner ne sont jamais rééligibles pour cette campagne. Pour permettre aux utilisateurs ayant fermé le Banner de le revoir, rendez-vous à l'étape **Contrôles de réception** et sélectionnez **Autoriser les utilisateurs à redevenir éligibles pour recevoir la campagne**. Lorsque cette option est activée, définissez une fenêtre de refroidissement en minutes, heures, jours ou semaines.

Le compte à rebours commence lorsque l'utilisateur ferme le Banner. Après l'expiration de la fenêtre, l'utilisateur est automatiquement rééligible, sans qu'il soit nécessaire de relancer la campagne. La rééligibilité est suivie par utilisateur et par campagne.

#### Choisir votre audience {#choose-your-audience}

1. Dans **Audiences cibles**, choisissez des Segments ou des filtres pour affiner votre audience. Vous recevez automatiquement un aperçu de la population approximative du Segment. L'appartenance exacte au Segment est calculée avant l'envoi du message.

{% multi_lang_include audience/target_audiences.md %}

{:start="2"}
2. Dans **Attribuer des conversions**, suivez la fréquence à laquelle les utilisateurs effectuent des actions spécifiques après avoir reçu une campagne en définissant des événements de conversion avec une fenêtre allant jusqu'à 30 jours pour comptabiliser l'action comme une conversion.

#### Choisir les événements de conversion {#choose-conversion-events}

Braze vous permet de suivre les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), c'est-à-dire la fréquence à laquelle les utilisateurs effectuent des actions spécifiques après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion est comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}

{% tab Canvas %}

Si vous ne l'avez pas encore fait, complétez les sections restantes de votre composant Canvas. Pour plus de détails sur la construction du reste de votre Canvas, y compris les tests multivariés et [Optimiser avec BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), consultez [Créer votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).

Pour contrôler la rééligibilité des étapes Banner dans Canvas, utilisez les paramètres de réentrée dans Canvas. Pour plus d'informations, consultez [Rééligibilité pour les campagnes et Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

{% endtab %}
{% endtabs %}

### Étape 5 : Tester votre message (facultatif) {#step-5-test-your-message-optional}

{% multi_lang_include banners/testing.md page="campaigns" %}

### Étape 6 : Vérifier et déployer {#step-6-review-and-deploy}

Après avoir terminé la construction de votre campagne ou Canvas, vérifiez ses détails, [testez-la]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages), puis envoyez-la quand vous êtes prêt.