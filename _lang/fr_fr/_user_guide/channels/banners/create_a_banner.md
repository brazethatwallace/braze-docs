---
nav_title: "Créer une bannière"
article_title: "Créer une bannière"
page_order: 1
description: "Cet article de référence explique comment créer, rédiger, configurer et envoyer des bannières à l'aide de campagnes et de Canvas Braze."
tool:
  - Campaigns
channel:
  - banners
---

# Créer une bannière {#create-a-banner}

> Découvrez comment créer des bannières lors de la conception de campagnes et de Canvas dans Braze. Pour des informations plus générales, consultez [À propos des bannières]({{site.baseurl}}/user_guide/channels/banners/).

## Conditions préalables {#prerequisites}

Avant de pouvoir lancer votre bannière, votre équipe de développement doit [configurer les emplacements dans votre application ou votre site web]({{site.baseurl}}/developer_guide/banners/placements/). Vous pouvez tout de même préparer votre campagne de bannière en attendant, mais vous ne pourrez pas la lancer tant que les emplacements ne seront pas configurés.

## Créer un message de type bannière {#create-a-banner-message}

{% multi_lang_include banners/creating_placements.md section="user" %}

### Étape 2 : Choisir où créer votre message {#step-2-choose-where-to-build-your-message}

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes conviennent mieux aux messages ciblés ponctuels, tandis que les Canvas sont plus adaptés aux parcours utilisateur en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

1. Accédez à **Messaging** > **Campaigns** et sélectionnez **Create Campaign**.
2. Sélectionnez **Banner**.
3. Donnez à votre campagne un nom clair et explicite.
4. Ajoutez des [équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) et des [étiquettes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) si nécessaire. Les étiquettes facilitent la recherche de vos campagnes et la création de rapports. Par exemple, avec le Générateur de rapports, vous pouvez filtrer par étiquettes pertinentes.
5. Sélectionnez l'emplacement que vous avez créé précédemment pour l'associer à votre campagne.
6. Ajoutez des variantes si nécessaire. Vous pouvez choisir un type de message et une disposition différents pour chacune. Pour en savoir plus sur les variantes, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).
7. Choisissez une date et une heure de début pour votre campagne de bannière. Par défaut, les bannières durent indéfiniment. Vous pouvez modifier ce comportement en sélectionnant **End Time** et en spécifiant une date et une heure de fin.

{% alert tip %}
Si tous les messages de votre campagne sont similaires ou ont le même contenu, rédigez votre message avant d'ajouter des variantes supplémentaires. Vous pourrez ensuite sélectionner **Copy from Variant** dans le menu déroulant **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) à l'aide du compositeur de Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape Message dans le générateur de Canvas. Donnez à votre étape un nom clair et explicite.
3. Sélectionnez **Banner** comme canal de communication.
4. Sélectionnez un emplacement pour la bannière.
5. Définissez la priorité de la bannière. La [priorité des bannières]({{site.baseurl}}/user_guide/channels/banners/#priority) détermine l'ordre d'affichage des bannières lorsqu'elles partagent le même emplacement.
6. Définissez une expiration pour la bannière. Celle-ci peut intervenir après une durée déterminée suivant la disponibilité de l'étape, ou à une date et une heure précises.

{% endtab %}
{% endtabs %}

### Étape 3 : Rédiger une bannière {#compose-a-banner}

Pour rédiger votre bannière, vous pouvez choisir de :

- Partir d'un modèle vierge
- Utiliser un modèle de bannière Braze
- Sélectionner un modèle de bannière enregistré

![Option de choisir une bannière vierge ou un modèle.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### Étape 3.1 : Styliser la bannière {#step-31-style-the-banner}

Vous pouvez glisser-déposer des blocs et des lignes dans la zone de travail pour commencer à créer votre message. Pour une référence des blocs de l'éditeur de bannières et des liens vers les détails des propriétés partagées, consultez [Blocs de l'éditeur (bannières)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=banners).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Pour personnaliser les propriétés d'arrière-plan, les paramètres de bordure et autres éléments de votre message, sélectionnez **Styles**. Si vous souhaitez personnaliser le style d'un bloc ou d'une ligne spécifique uniquement, sélectionnez-le pour effectuer les modifications.

![Panneau de styles du compositeur de bannière.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Étape 3.2 : Définir le comportement au clic (facultatif) {#step-32-define-on-click-behavior-optional}

Lorsqu'un utilisateur clique sur un lien dans la bannière, vous pouvez choisir de le diriger plus en profondeur dans votre application ou de le rediriger vers une autre page web. De plus, vous pouvez choisir de [journaliser un attribut personnalisé ou un événement]({{site.baseurl}}/developer_guide/analytics/), ce qui met à jour le profil de l'utilisateur avec des données personnalisées lorsqu'il clique sur la bannière. Pour un suivi des clics plus granulaire, attribuez un identifiant personnalisé à chaque élément interactif à l'aide du champ **Identifier for Reporting** dans son panneau de propriétés.

{% alert important %}
{::nomarkdown}
Le comportement au clic peut être remplacé si un élément spécifique (comme un bouton, un lien ou une image de la bannière) possède son propre comportement au clic. Par exemple, avec les comportements au clic suivants :<br><ul><li>Une bannière a un comportement au clic qui redirige vers la page d'accueil d'un site web.</li><li>Une image dans la bannière a un comportement au clic qui redirige vers la page produit d'un site web.</li></ul>Si un utilisateur clique sur l'image, il est redirigé vers la page produit. En revanche, un clic sur la zone environnante de la bannière le redirige vers la page d'accueil.
{:/}
{% endalert %}

#### Étape 3.3 : Configurer le comportement de fermeture (facultatif) {#dismiss-behavior}

Cochez la case **Banner can be dismissed** dans la section **Dismiss Behavior** pour permettre aux utilisateurs de fermer la bannière. Cette option est utile dans les cas où vous souhaitez promouvoir une vente à durée limitée auprès de tous les utilisateurs de l'application, tout en leur permettant de fermer le message s'ils ne sont pas intéressés.

Lorsque la fermeture est activée, vous pouvez personnaliser le bouton de fermeture dans la section **Dismiss Behavior** :

| Paramètre | Description |
|---------|-------------|
| **Button size** | La taille du bouton de fermeture affiché sur la bannière. |
| **Button color** | La couleur du bouton de fermeture. |
| **ARIA label** | Le libellé accessible du bouton de fermeture, utilisé par les lecteurs d'écran. La valeur par défaut est « Close » si le champ est laissé vide. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paramètres du bouton de fermeture" }

Lorsqu'un utilisateur ferme une bannière, celle-ci ne s'affiche plus pour cet utilisateur, même s'il remplit toujours les critères de ciblage de la campagne.

#### Étape 3.4 : Ajouter des propriétés personnalisées (facultatif) {#custom-properties}

Vous pouvez ajouter des propriétés personnalisées à une bannière pour y associer des métadonnées structurées, telles que des chaînes de caractères ou des objets JSON. Ces propriétés n'affectent pas l'affichage de la bannière, mais peuvent être [consultées via le SDK Braze]({{site.baseurl}}/developer_guide/banners/placements/) pour modifier le comportement ou l'apparence de votre application. Par exemple, vous pourriez :

- Envoyer des métadonnées pour vos analyses tierces ou vos intégrations.
- Utiliser des métadonnées telles qu'un `timestamp` ou un objet JSON pour déclencher une logique conditionnelle.
- Contrôler le comportement d'une bannière en fonction de métadonnées incluses comme `ratio` ou `format`.

Pour ajouter une propriété personnalisée, sélectionnez **Settings** > **Properties** > **Add property**.

![La page des propriétés affichant l'option d'ajouter la première propriété personnalisée à une campagne de bannière.]({% image_buster /assets/img/banners/add_property.png %})

Pour chaque propriété que vous souhaitez ajouter, remplissez les champs suivants :

| Champ | Description | Exemple |
|-------|-------------|---------|
| Type de propriété | Le type de données de la propriété. Les types pris en charge incluent chaîne de caractères, valeur booléenne, nombre, horodatage, URL d'image et objet JSON. | Chaîne de caractères |
| Clé de propriété | L'identifiant unique de la propriété. Cette clé est utilisée dans le SDK pour accéder à la propriété. | `color` |
| Valeur | La valeur attribuée à la propriété. Elle doit correspondre au type de propriété sélectionné. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ajouter des propriétés personnalisées" }

Lorsque vous avez terminé, sélectionnez **Done**.

![La page des propriétés avec une propriété de type chaîne de caractères ayant pour clé color et pour valeur #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

### Étape 4 : Finaliser votre campagne ou Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Définir la priorité de la bannière (facultatif) {#set-banner-priority-optional}

La [priorité des bannières]({{site.baseurl}}/user_guide/channels/banners/#priority) détermine l'ordre d'affichage des bannières lorsqu'elles partagent le même emplacement. Pour définir manuellement la priorité :

1. Sélectionnez **Set exact priority**.
2. Glissez-déposez les campagnes pour les ordonner selon la priorité souhaitée.
3. Sélectionnez **Apply Sort**.

{% alert tip %}
Si vous avez plusieurs campagnes de bannière utilisant le même ID d'emplacement, nous vous recommandons d'utiliser le tri par priorité en glisser-déposer pour définir la priorité exacte.
{% endalert %}

#### Configurer la rééligibilité (facultatif) {#re-eligibility}

Par défaut, les utilisateurs qui ferment une bannière ne sont jamais rééligibles pour cette campagne. Pour permettre aux utilisateurs ayant fermé la bannière de la revoir, accédez à l'étape **Contrôles de l'envoi** et sélectionnez **Allow users to become re-eligible to receive campaign**. Lorsque cette option est activée, définissez une période de temporisation en minutes, heures, jours ou semaines.

Le décompte commence à partir du moment où l'utilisateur ferme la bannière. Une fois la période écoulée, l'utilisateur redevient automatiquement éligible, sans qu'il soit nécessaire de relancer la campagne. La rééligibilité est suivie par utilisateur et par campagne.

#### Choisir votre audience {#choose-your-audience}

1. Dans **Audience cible**, choisissez des segments ou des filtres pour affiner votre audience. Vous obtenez automatiquement un aperçu de la population approximative du segment. L'appartenance exacte au segment est calculée avant l'envoi du message.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2. Dans **Assign Conversions**, suivez la fréquence à laquelle les utilisateurs effectuent des actions spécifiques après avoir reçu une campagne en définissant des événements de conversion avec une fenêtre pouvant aller jusqu'à 30 jours pour comptabiliser l'action comme une conversion.

#### Choisir les événements de conversion {#choose-conversion-events}

Braze vous permet de suivre les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), c'est-à-dire la fréquence à laquelle les utilisateurs effectuent des actions spécifiques après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion est comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}

{% tab Canvas %}

Si ce n'est pas déjà fait, complétez les sections restantes de votre composant Canvas. Pour plus de détails sur la finalisation de votre Canvas, la mise en œuvre de [tests multivariés]({{site.baseurl}}/user_guide/messaging/ab_testing/) et de la [Sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/), et bien plus encore, consultez l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation Canvas.

Pour contrôler la rééligibilité des étapes de bannière dans un Canvas, utilisez les paramètres de réentrée du Canvas. Pour en savoir plus, consultez [Rééligibilité pour les campagnes et Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/).

{% endtab %}
{% endtabs %}

### Étape 5 : Tester votre message (facultatif) {#step-5-test-your-message-optional}

{% multi_lang_include banners/testing.md page="campaigns" %}

### Étape 6 : Vérifier et déployer {#step-6-review-and-deploy}

Après avoir terminé la création de votre campagne ou Canvas, vérifiez ses détails, [testez-la]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/), puis envoyez-la quand vous êtes prêt.