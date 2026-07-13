---
nav_title: "Sondage simple"
article_title: Message in-app de sondage simple
page_order: 6
page_type: reference
description: "Cet article de référence explique comment collecter des attributs utilisateur, des informations et des préférences pour alimenter votre stratégie de campagne à l'aide des sondages par message in-app."
channel:
  - in-app messages
tool:
  - Templates
---

# Sondage simple {#simple-survey}

> Utilisez le modèle de message in-app **Simple Survey** pour collecter des attributs utilisateur, des informations et des préférences qui alimentent votre stratégie de campagne.

Ce type de message est disponible dans l'[éditeur traditionnel]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

Les cas d'utilisation courants des sondages incluent demander aux utilisateurs comment ils souhaitent utiliser votre application, en apprendre davantage sur leurs préférences personnelles, ou recueillir leur avis sur leur satisfaction concernant une fonctionnalité particulière.

![Trois messages de sondage simple : préférences de notification, préférences alimentaires et un sondage de satisfaction client. Les options sélectionnées dans les sondages correspondent à des attributs personnalisés qui seront enregistrés pour cet utilisateur.]({% image_buster /assets/img/iam/iam-survey.png %})

## Exigences du SDK {#supported-sdk-versions}

Ce message in-app ne sera envoyé qu'aux appareils prenant en charge [Flex CSS](https://caniuse.com/flexbox), et doit disposer au minimum des [versions du SDK]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions) suivantes.

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Pour activer les messages in-app HTML via le SDK Web, vous devez fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze.
{% endalert %}

## Créer un sondage {#create}

Lors de la création d'un [message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional), sélectionnez **Simple Survey** pour votre **Message Type**.

Ce modèle de sondage est pris en charge à la fois pour les applications mobiles et les navigateurs web. N'oubliez pas de vérifier que vos SDK sont aux [versions minimales du SDK](#supported-sdk-versions) requises pour cette fonctionnalité.

### Étape 1 : Ajouter votre question de sondage {#step-1-add-your-survey-question}

Pour commencer à créer votre sondage, ajoutez votre question dans le champ **Header** du sondage. Si vous le souhaitez, vous pouvez ajouter un message **Body** facultatif qui apparaîtra sous votre question de sondage.

![Onglet Rédiger de l'éditeur de sondage simple, avec des champs pour un en-tête, un corps facultatif et un texte d'aide facultatif.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:90%"}

{% alert tip %}
Ces champs peuvent inclure à la fois du Liquid et des emojis, alors laissez libre cours à votre créativité !
{% endalert %}

### Étape 2 : Configurer les choix {#single-multiple-choice}

Vous pouvez ajouter jusqu'à 12 choix dans un sondage.

Sélectionnez soit **Single-choice selection** soit **Multiple-choice selection**. Le **Helper text** se mettra automatiquement à jour lorsque vous basculez entre les deux options pour indiquer aux utilisateurs combien de choix ils peuvent sélectionner.

Ensuite, déterminez si vous allez [collecter des attributs personnalisés](#custom-attributes) ou [enregistrer uniquement les réponses](#no-attributes).

![Menu déroulant des choix avec « Log attributes upon submission » sélectionné.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

#### Collecter des attributs personnalisés {#custom-attributes}

Sélectionnez **Log attributes upon submission** pour collecter des attributs basés sur la soumission de l'utilisateur. Vous pouvez utiliser cette option pour créer de nouveaux segments et des campagnes de reciblage. Par exemple, dans un [sondage de satisfaction](#user-satisfaction), vous pourriez envoyer un e-mail de suivi à tous les utilisateurs qui n'étaient pas satisfaits.

Pour ajouter un attribut personnalisé à chaque choix, sélectionnez un nom d'attribut personnalisé dans le menu déroulant (ou créez-en un nouveau), puis saisissez la valeur à définir lorsque ce choix est soumis. Vous pouvez également créer un nouvel attribut personnalisé dans votre [page Paramètres]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data).

Le type de données de vos attributs personnalisés est important selon la façon dont vous avez configuré votre sondage.

- **Sélection à choix multiples :** Le type de données de l'attribut personnalisé doit être un tableau. Si l'attribut personnalisé est défini sur un type de données différent, les réponses ne seront pas enregistrées.
- **Sélection à choix unique :** Le type de données de l'attribut personnalisé doit être une chaîne de caractères. Les attributs personnalisés qui ne sont pas de type chaîne de caractères n'apparaîtront pas dans le menu déroulant, et les réponses ne seront pas enregistrées.

{% alert important %}
Lorsque la collecte d'attributs personnalisés est activée, les choix qui partagent le même nom d'attribut personnalisé seront combinés dans un tableau.
{% endalert %}

##### Exemple {#example}

Par exemple, dans un [sondage de préférences de notification](#notification-preferences), vous pourriez faire de chaque choix un attribut booléen (vrai/faux) pour permettre aux utilisateurs de sélectionner les sujets qui les intéressent. Si un utilisateur coche le choix « Promotions », cela mettra à jour son [profil utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) avec l'attribut personnalisé `Promotions Topic` défini sur `true`. S'il laisse le choix non coché, ce même attribut restera inchangé.

Vous pouvez ensuite utiliser le filtre `Custom Attribute` pour créer un segment d'utilisateurs avec l'attribut personnalisé `Promotions Topic` `is` `true` afin de vous assurer que seuls les utilisateurs intéressés par vos promotions recevront les campagnes pertinentes.

#### Enregistrer uniquement les réponses {#no-attributes}

Alternativement, vous pouvez choisir **Log responses only (no attributes)**. Lorsque cette option est sélectionnée, les réponses au sondage sont enregistrées comme des clics sur des boutons, mais les attributs personnalisés ne sont pas enregistrés dans le profil de l'utilisateur. Cela signifie que vous pouvez toujours consulter les indicateurs de clics pour chaque option du sondage (voir [Analyse](#analytics)), mais ce choix ne sera pas reflété dans leur profil utilisateur.

Ces indicateurs de clics ne sont pas disponibles pour le reciblage.

### Étape 4 : Choisir le comportement après soumission {#step-4-choose-submission-behavior}

Une fois qu'un utilisateur a soumis sa réponse, vous pouvez éventuellement afficher une page de confirmation, ou simplement fermer le message.

Une page de confirmation est un excellent endroit pour remercier les utilisateurs de leur temps ou fournir des informations supplémentaires. Vous pouvez personnaliser l'appel à l'action sur cette page pour guider les utilisateurs vers une autre page de votre application ou site web.

Modifiez le texte de votre bouton et le comportement au clic dans la section **Submit Button** en bas de l'onglet **Survey** :

![Comportement au clic défini sur « Submit responses and display confirmation page ».]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Si vous choisissez d'ajouter une page de confirmation, passez à l'onglet **Confirmation Page** pour personnaliser votre message :

![Onglet Confirmation Page de l'éditeur de sondage simple. Les champs disponibles sont l'en-tête, le corps facultatif, le texte du bouton et le comportement au clic du bouton.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:90%"}

Si vous souhaitez guider les utilisateurs vers une autre page de votre application ou site web, modifiez le **comportement au clic** du bouton.

### Étape 5 : Styliser votre message (facultatif) {#styling}

Vous pouvez personnaliser la couleur de la police et la couleur d'accentuation du message à l'aide du sélecteur **Color Theme**.

![Onglet Rédiger de l'éditeur de sondage simple avec le sélecteur Color Theme développé après qu'un utilisateur a cliqué sur la palette de couleurs.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analyser les résultats {#analytics}

Une fois votre campagne lancée, vous pouvez analyser les résultats en temps réel pour voir la répartition de chaque choix sélectionné. Si vous avez activé la [collecte d'attributs personnalisés](#custom-attributes), vous pourrez également créer de nouveaux segments ou des campagnes de suivi pour les utilisateurs ayant répondu au sondage.

{% alert note %}
Les choix de sondage supprimés apparaîtront toujours dans les analyses, mais ne seront pas affichés comme choix pour les nouveaux utilisateurs.
{% endalert %}

Vous pouvez trouver les indicateurs de performance de votre sondage en développant le menu déroulant **Results** pour une variante spécifique dans la section **In-App Message Performance** de l'analyse. Voici un aperçu de ce que vous verrez :

- **Engagement du sondage** montre comment les utilisateurs ont interagi avec le sondage dans son ensemble, y compris le nombre total de soumissions, de rejets et de clics dans le corps du message.
- **Résultats du sondage** affiche une répartition du nombre d'utilisateurs ayant sélectionné chaque option de réponse, ainsi que le pourcentage du total des soumissions que chaque choix représente.
- **Indicateurs de la page de confirmation** (si activée) incluent le nombre d'utilisateurs ayant vu l'écran de confirmation, cliqué sur son bouton ou l'ayant rejeté sans interagir.

Pour les définitions des indicateurs de sondage, consultez le [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary) et filtrez par « In-App Message ».

Consultez [Rapports des messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) pour une répartition des indicateurs de votre campagne.

### Currents {#currents}

Les choix sélectionnés seront automatiquement transmis à Currents, sous le champ `button_id` des [**événements de clic de message in-app**]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#api_fzzdoylmrtwe). Chaque choix sera envoyé avec son identifiant universel unique (UUID).

## Cas d'utilisation {#use-cases}

{% tabs %}
{% tab Satisfaction des utilisateurs %}

### Satisfaction des utilisateurs {#user-satisfaction}

**Objectif :** Mesurer la satisfaction des clients et envoyer des campagnes de reconquête aux utilisateurs ayant attribué des scores faibles.

Pour configurer cela, utilisez un sondage à choix unique avec cinq options allant de « 😡 Très insatisfait » à « 😍 Très satisfait ». Chaque choix est associé à l'attribut personnalisé `customer_satisfaction`, avec une valeur numérique de 1 à 5, où 1 indique le moins satisfait et 5 le plus satisfait. Notez que ces valeurs numériques sont stockées sous forme de chaînes de caractères, car les attributs personnalisés de type chaîne de caractères sont requis pour la sélection à choix unique.

| Choix | Attribut | Valeur |
|-------|----------|--------|
| 😡 Très insatisfait | `customer_satisfaction` | 1 |
| 😟 Insatisfait | `customer_satisfaction` | 2 |
| 🙂 Ni satisfait ni insatisfait | `customer_satisfaction` | 3 |
| 😊 Satisfait | `customer_satisfaction` | 4 |
| 😍 Très satisfait | `customer_satisfaction` | 5 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Satisfaction des utilisateurs" }

Lorsqu'un utilisateur soumet le sondage, la valeur sélectionnée est enregistrée comme attribut personnalisé. Vous pouvez ensuite créer des campagnes de suivi à l'aide de filtres d'audience. Par exemple, ciblez des messages de reconquête vers les utilisateurs dont l'attribut `customer_satisfaction` est « 1 » ou « 2 ».

{% endtab %}
{% tab Préférences de notification %}

### Préférences de notification {#notification-preferences}

**Objectif :** Permettre aux utilisateurs de s'inscrire à des types de notifications spécifiques.

Pour configurer cela, utilisez un sondage à choix multiples où chaque choix représente un sujet de notification. Au lieu d'attribuer le même attribut avec des valeurs différentes, chaque choix est associé à un attribut booléen distinct qui reflète l'intérêt de l'utilisateur pour ce sujet. Si un utilisateur sélectionne un choix, l'attribut correspondant est défini sur `true`. S'il n'est pas sélectionné, l'attribut reste inchangé.

| Choix | Attribut | Valeur |
|-------|----------|--------|
| Mises à jour produit | `wants_product_updates` | `true` |
| Promotions | `wants_promotions` | `true` |
| Invitations événements | `wants_event_invites` | `true` |
| Sondages et retours | `wants_surveys` | `true` |
| Conseils et tutoriels | `wants_tips` | `true` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Préférences de notification" }

{% endtab %}
{% tab Identifier les objectifs des clients %}

### Identifier les objectifs des clients {#identify-customer-goals}

**Objectif :** Identifier les principales raisons pour lesquelles les utilisateurs visitent votre application.

Pour configurer cela, utilisez un sondage à choix unique avec chaque option représentant un objectif ou une intention courante. Chaque choix est associé à l'attribut personnalisé `product_goal` avec une valeur correspondant à l'intention sélectionnée par l'utilisateur.

| Choix | Attribut | Valeur |
|-------|----------|--------|
| Vérifier un statut | `product_goal` | `status` |
| Mettre à niveau mon compte | `product_goal` | `upgrade` |
| Planifier un rendez-vous | `product_goal` | `schedule` |
| Assistance client | `product_goal` | `support` |
| Simple navigation | `product_goal` | `browse` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Identifier les objectifs des clients" }

Lorsqu'un utilisateur soumet le sondage, la valeur sélectionnée est enregistrée comme attribut personnalisé dans son profil. Vous pouvez ensuite utiliser ces données pour personnaliser les expériences futures ou segmenter les utilisateurs en fonction de leur objectif principal.

{% endtab %}
{% tab Améliorer les taux de conversion %}

### Améliorer les taux de conversion {#improve-conversion-rates}

**Objectif :** Comprendre pourquoi les clients ne passent pas à une version supérieure ou n'achètent pas.

Pour configurer cela, utilisez un sondage à choix unique avec chaque option représentant un obstacle courant à la mise à niveau. Chaque choix est associé à l'attribut personnalisé `upgrade_reason` avec une valeur correspondante qui reflète la sélection de l'utilisateur.

| Choix | Attribut | Valeur |
|-------|----------|--------|
| Trop cher | `upgrade_reason` | `expensive` |
| Pas assez de valeur | `upgrade_reason` | `value` |
| Difficile à utiliser | `upgrade_reason` | `difficult` |
| Utilise un concurrent | `upgrade_reason` | `competitor` |
| Autre raison | `upgrade_reason` | `other` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Améliorer les taux de conversion" }

Lorsqu'un utilisateur soumet le sondage, la valeur sélectionnée est enregistrée dans son profil. Vous pouvez ensuite cibler ces utilisateurs avec des campagnes adaptées à leur objection spécifique, comme des offres de réduction ou des améliorations de l'ergonomie.

{% endtab %}
{% tab Fonctionnalités préférées %}

### Fonctionnalités préférées {#favorite-features}

**Objectif :** Comprendre quelles fonctionnalités les clients apprécient le plus.

Pour configurer cela, utilisez un sondage à choix multiples où chaque option représente une fonctionnalité de votre application. Chaque choix est associé à l'attribut personnalisé `favorite_features`, et lorsque l'utilisateur soumet le sondage, l'attribut est défini sur un tableau des valeurs sélectionnées.

| Choix | Attribut | Valeur |
|-------|----------|--------|
| Favoris | `favorite_features` | `bookmarks` |
| Application mobile | `favorite_features` | `mobile` |
| Partage de posts | `favorite_features` | `sharing` |
| Assistance client | `favorite_features` | `support` |
| Personnalisation | `favorite_features` | `custom` |
| Prix / Valeur | `favorite_features` | `value` |
| Communauté | `favorite_features` | `community` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fonctionnalités préférées" }

Comme ce sondage utilise la sélection à choix multiples, le profil de l'utilisateur sera mis à jour avec une liste de toutes les valeurs de fonctionnalités sélectionnées.

{% endtab %}
{% endtabs %}