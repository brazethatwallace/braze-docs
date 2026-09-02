---
nav_title: aliasage de lien
article_title: aliasage de lien
alias: /link_aliasing/
page_order: 3
description: "Cet article décrit le fonctionnement de l'aliasage de lien et fournit des exemples de ce à quoi vos liens ressembleront."
channel:
  - email

---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}Aliasing de lien {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomlink-aliasing-stylefloatrightwidth120pxborder0-classnoimgborderlink-aliasing}

> Utilisez l'aliasage de lien pour créer des noms reconnaissables, générés par l'utilisateur, afin d'identifier les liens envoyés dans les e-mails depuis Braze. Ces liens sont disponibles pour le reciblage par segmentation, le déclenchement basé sur les actions et l'analyse des liens.

## À propos de l'aliasage de lien {#about-link-aliasing}

Avec l'aliasage de lien, vous pouvez créer des noms personnalisés pour identifier et suivre les liens envoyés dans vos e-mails. De cette façon, vous pouvez utiliser efficacement ces alias de lien reconnaissables dans vos e-mails pour suivre l'engagement et analyser les performances des Campaigns, sans avoir besoin de référencer le lien complet.

Avec l'aliasage de lien, vous pouvez :

- **Recibler les utilisateurs qui ont cliqué sur des liens spécifiques :** Identifier et cibler les utilisateurs qui ont cliqué sur un lien.
- **Créer des déclencheurs basés sur une action :** Envoyer un e-mail lorsqu'un utilisateur clique sur un lien.
- **Analyser les indicateurs :** Comparer combien d'utilisateurs ont cliqué sur le lien A par rapport au lien B.

### Fonctionnement {#how-it-works}

Braze identifie de manière unique les liens dans les e-mails en ajoutant un paramètre supplémentaire appelé `lid` (également connu sous le nom d'identifiant de lien) à chaque URL de lien. Cette valeur `lid` permet à Braze de suivre, surveiller et agréger les interactions des utilisateurs avec le lien, même si les autres paramètres de l'URL peuvent différer. Cela permet de fournir des informations sur la façon dont les utilisateurs interagissent avec le contenu de vos Campaigns par e-mail.

Les identifiants de lien seront également mis à jour si une Campaign par e-mail, un Canvas contenant un message e-mail ou un Content Block est dupliqué.

## Créer un alias de lien {#creating-a-link-alias}

{% alert important %}
**Link Management** apparaît dans le compositeur d'e-mail de la campagne ou du Canvas lorsque Braze active la gestion des liens pour votre compte. Pour créer et modifier des **alias de lien**, l'aliasage de lien doit être activé. Si **Link Management** est absent, contactez votre gestionnaire de compte pour activer l'aliasage de lien.
{% endalert %}

Pour créer un alias de lien, ouvrez le corps de votre e-mail dans le composant de campagne ou de Canvas, puis ouvrez **Link Management** depuis la zone **Content**. Les compositeurs par glisser-déposer et HTML utilisent la même disposition de barre latérale :

### Éditeur glisser-déposer {#drag-and-drop-editor}

1. Sélectionnez **Edit Email Body** pour ouvrir le compositeur par glisser-déposer.
2. Dans la barre latérale du compositeur, sélectionnez **Content** (à côté de **Sending Settings** et **Preview & Test**). Pour en savoir plus sur cette disposition, consultez [Créer un e-mail par glisser-déposer]({{site.baseurl}}/user_guide/channels/email/drag_and_drop).
3. Dans le sous-menu **Content**, sélectionnez **Link Management** (il apparaît sous **Design and Build**). Si le sous-menu est réduit, développez-le à l'aide de la commande fléchée dans la barre latérale.

### Éditeur HTML {#html-editor}

1. Accédez au corps de votre e-mail dans le compositeur.
2. Dans la barre latérale du compositeur, sélectionnez **Content**.
3. Dans le sous-menu **Content**, sélectionnez **Link Management** sous **Design and Build**.

Dans **Link Management** :

1. Braze génère automatiquement des alias de lien par défaut uniques pour chacun de vos liens.
2. Donnez un nom à l'alias. Les alias doivent avoir un nom unique par variante de campagne d'e-mail ou par composant Canvas.

Vous pouvez également définir un alias qui sera utilisé pour référencer un lien spécifique dans le cadre du reporting ou de la segmentation.

![Page Link Management avec quatre alias de lien.]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
L'aliasage de lien est pris en charge uniquement dans les attributs `href` au sein des balises d'ancrage HTML où il est possible d'ajouter un paramètre de requête en toute sécurité. Il est recommandé d'inclure un point d'interrogation (?) à la fin de votre lien afin que Braze puisse facilement ajouter la valeur `lid`. Sans l'ajout de la valeur `lid`, Braze ne reconnaîtra pas l'URL pour l'aliasage de lien.
{% endalert %}

{% alert important %}
Dans l'éditeur glisser-déposer, votre lien doit inclure un point d'interrogation (`?`) avant le symbole dièse (`#`) dans votre URL pour que l'alias de lien apparaisse dans l'onglet **Link Management**.
{% endalert %}

## Gestion des alias de lien {#managing-link-aliases}

Pour consulter l'ensemble de vos alias de lien suivis, procédez comme suit :

1. Accédez à **Paramètres** > **Préférences e-mail** sous **Paramètres de l'espace de travail**.
2. Sélectionnez l'onglet **Paramètres d'aliasage de lien**.

Vous pouvez y trier, rechercher et désactiver le suivi des alias de lien.

![Page des alias de lien suivis affichant les alias de lien actifs et inactifs associés à différentes campagnes.]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
Utilisez les endpoints [Lister les alias de lien pour une campagne]({{site.baseurl}}/get_campaign_link_alias) et [Lister les alias de lien pour un Canvas]({{site.baseurl}}/get_canvas_link_alias) pour extraire l'`alias` défini dans chaque variante de message d'une campagne ou d'un composant Canvas spécifique à l'e-mail.
{% endalert %}

Braze recommande d'évaluer les liens présents dans l'e-mail, d'ajouter des modèles de lien et de mettre en place une convention de nommage adaptée à la segmentation et au reporting. Cela vous aide à garder le suivi de tous les liens.

Lorsque l'aliasage de lien est activé, les messages, les Content Blocks et les modèles de lien ne sont pas modifiés. Les messages existants utilisant des modèles de lien ou des Content Blocks restent identiques. Cependant, lorsque vous mettez à jour un message, le balisage d'alias de lien s'applique à l'ensemble des liens, ce qui signifie que vous devrez réappliquer les modèles de lien pour que les liens soient visibles.

## Comment les liens sont mis à jour avec l'aliasage de lien {#how-links-are-updated-with-link-aliasing}

Les tableaux suivants fournissent des exemples de liens dans le corps d'un e-mail, les résultats de l'aliasage de lien et des explications sur la façon dont le lien original est mis à jour avec l'aliasage de lien.

### Permalien {#permalink}

**Logique :** Braze insère un point d'interrogation (?) et ajoute le premier paramètre de requête dans l'URL.

| Lien dans le corps de l'e-mail    | Lien avec aliasing                     |
|-----------------------|----------------------------------------|
| `https://www.braze.com` | `https://www.braze.com?lid=slfdldtqdhdk` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permalien" }

### Lien avec plusieurs paramètres de requête {#link-with-more-query-parameters}

**Logique :** Braze détecte d'autres paramètres de requête et ajoute `lid=` à la fin de l'URL.

| Lien dans le corps de l'e-mail                                            | Lien avec aliasing                                                             |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| `https://www.braze.com?utm_campaign=retention&utm_source=email` | `https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Lien avec plusieurs paramètres de requête" }

### Lien HTML {#html-link}

**Logique :** Braze reconnaît qu'un lien est une URL et qu'un point d'interrogation (?) est déjà présent, le paramètre de requête `lid` est donc ajouté après le point d'interrogation.

| Lien dans le corps de l'e-mail                                                | Lien avec aliasing                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Lien HTML" }

### Lien avec ancre {#link-with-anchor}

**Logique :** Braze s'attend à ce que l'URL utilise une structure standard où les ancres (#) sont présentes après un point d'interrogation (?). Comme Braze lit de gauche à droite, le point d'interrogation et la valeur `lid` sont ajoutés avant l'ancre.

| Lien dans le corps de l'e-mail                               | Lien avec aliasing                                                |
|--------------------------------------------------|-------------------------------------------------------------------|
| `https://www.braze.com#bookmark1?utm_source=email` | `https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Lien avec ancre" }

### Lien avec ancre et balise capture {#link-with-anchor-and-capture-tag}

**Logique :** Lors de l'utilisation de l'aliasage de lien avec des URL contenant des ancres (#), Braze s'attend à ce que l'ancre soit placée après les paramètres de requête. Cela signifie que la valeur `lid` doit être ajoutée **avant** l'ancre pour un suivi correct, et comme Braze lit l'URL de gauche à droite, le point d'interrogation (?) et le `lid` doivent précéder l'ancre.

| Lien dans le corps de l'e-mail                                                                        | Lien avec aliasing                                                                                           |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions?lid={{link_alias}}#special-offer">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Lien avec ancre et balise capture" }

## Suivi des alias de lien {#tracking-link-aliases}

Dans la barre latérale du compositeur, sélectionnez **Contenu** > **Gestion des liens** (sous **Conception et création**), puis sélectionnez les alias que vous souhaitez **suivre**. Les alias suivis sont disponibles dans les filtres de segmentation qui font référence aux alias de lien (voir [Filtres de segmentation](#segmentation-filters)). Vous pouvez également envoyer des messages basés sur des actions ou faire avancer des utilisateurs dans un Canvas lorsqu'ils cliquent sur un alias de lien dans un e-mail — voir [Filtres basés sur des actions](#action-based-filters). Le paramètre **suivi** ne modifie pas la prise en compte des clics sur ce lien dans les rapports de performance des e-mails.

{% alert tip %}
Pour suivre les indicateurs d'engagement des liens, assurez-vous que votre lien commence par HTTP ou HTTPS. Pour désactiver le suivi des clics pour des liens spécifiques, consultez [Liens universels et App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis).
{% endalert %}

Braze vous permet de sélectionner un nombre illimité de liens à suivre, mais vous ne pouvez recibler les utilisateurs que sur les liens les plus récents qu'ils ont ouverts. Les profils utilisateur incluent les 100 liens les plus récemment cliqués. Par exemple, si vous suivez 500 liens et qu'un utilisateur clique sur les 500, vous pouvez recibler ou créer des Segments basés sur les 100 liens les plus récemment cliqués.

![L'onglet Gestion des liens avec deux liens sélectionnés.]({% image_buster /assets/img/link_management_dnd.png %})

{% alert note %}
Braze ne suit que les 100 derniers alias de lien cliqués au niveau du profil.
{% endalert %}

### Filtres basés sur des actions {#action-based-filters}

Lorsque l'aliasage de lien est activé pour votre espace de travail, vous pouvez créer des messages basés sur des actions ciblant n'importe quel lien (suivi ou non suivi) ou recibler des utilisateurs en fonction de leur clic sur un alias dans n'importe quelle Campaign ou composant Canvas.

![Options basées sur des actions pour cibler les utilisateurs ayant cliqué sur un alias dans un composant Canvas ou ayant interagi avec une Campaign.]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

- Si une Campaign est archivée, le suivi des liens est désactivé et cet alias de lien ne peut pas être utilisé dans un autre filtre.
- Si un lien a le suivi activé et a été cliqué dans une Campaign, vous pouvez retrouver la Campaign comme option disponible dans le filtre de segmentation, même si le suivi des liens a été désactivé depuis, tant qu'au moins un lien de ce message est encore suivi.
- Vous ne pouvez sélectionner un lien suivi comme filtre que s'il se trouve dans un Canvas actif (lancé), en utilisant le menu déroulant du filtre **A cliqué sur un alias dans une étape Canvas**. Si le lien est suivi dans un brouillon de Canvas, vous ne pouvez pas sélectionner le lien suivi comme filtre.

Pour définir des liens comme non suivis, accédez à **Paramètres** > **Préférences e-mail** > **Paramètres d'aliasage de lien**.

### Filtres de segmentation {#segmentation-filters}

Dans Braze, si vous avez un alias de lien dans votre e-mail et qu'un utilisateur clique dessus, l'événement est enregistré dans le profil de l'utilisateur avec l'alias.

Si vous utilisez le filtre de segmentation « A cliqué sur un alias dans n'importe quelle Campaign ou étape Canvas » et que vous décidez ensuite de renommer cet alias de lien, les données de clic précédentes dans le profil utilisateur ne sont **pas** mises à jour, ce qui signifie qu'elles affichent toujours l'ancien alias de lien. Ainsi, si vous ciblez des utilisateurs en fonction du nouvel alias de lien, cela n'inclut pas les données de l'ancien alias de lien.

Si vous utilisez le filtre de segmentation « A cliqué sur un alias dans une Campaign » ou « A cliqué sur un alias dans un Canvas », celui-ci filtre vos utilisateurs selon qu'ils ont cliqué sur un alias spécifique dans une Campaign ou un Canvas spécifique. Si plusieurs utilisateurs partagent la même adresse e-mail et que l'alias de lien est cliqué, tous les autres utilisateurs partageant cette adresse e-mail voient leur profil utilisateur mis à jour. Ces profils sont également mis à jour par les événements de réception et d'ouverture, et pas seulement par les événements de clic.

Les filtres de segmentation suivants s'appliquent aux événements de clic qui sont suivis au moment où l'événement est traité. Cela signifie que les liens non suivis ne suppriment pas les données existantes et que le suivi d'un lien ne remplit pas rétroactivement les données. Pour plus de détails, voir [Filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

#### Arrêt du suivi des liens {#untracking-links}

Arrêter le suivi d'un lien ne réaffecte pas les Segments existants avec le filtre vers l'alias non suivi. Les anciennes données restent dans les profils utilisateur jusqu'à ce qu'elles soient remplacées par des données plus récentes.

Les liens dans les messages archivés sont automatiquement retirés du suivi. Cependant, si des messages archivés sont désarchivés, les liens devront être à nouveau suivis. Lorsque les alias de lien sont suivis, les rapports de liens sont indexés par alias plutôt que par domaines de premier niveau ou URLs complètes.

Pour afficher tous les liens de votre Campaign e-mail et le total de leurs clics respectifs, accédez à **Analyse des messages** > **Performance e-mail** > **Aperçu et carte de chaleur**, puis activez le basculeur **Afficher la carte de chaleur**.

![Panneau du tableau des liens par total de clics avec les alias de lien et leur total de clics.]({% image_buster /assets/img/link_alias_total_clicks.png %}){: style="max-width:60%;"}

### Événement de clic e-mail {#email-clicks-event}

Si vous exportez vos données d'engagement avec Currents, un événement de clic e-mail sera légèrement différent si l'aliasage de lien est activé. Il comportera deux champs supplémentaires pour l'[événement de clic e-mail]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-click-events) lorsque l'aliasage de lien est activé : `link_id` et `link_alias`.

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique ID of this event,
  "user_id": (string) Braze user ID of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) ID of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) ID of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) ID of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click and Open events only),
  "ip_pool": (string) IP pool used for message sending,
  "link_id": (string) unique value generated by Braze for the URL,
  "link_alias": (string) alias name set when the message was sent
}
```

{% alert update %}
Le comportement de `dispatch_id` diffère entre Canvas et Campaigns car Braze traite les étapes Canvas (sauf les étapes d'entrée, qui peuvent être planifiées) comme des événements déclenchés, même lorsqu'elles sont « planifiées ». En savoir plus sur le [comportement de `dispatch_id`]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id) dans Canvas et Campaigns.

_Mise à jour notée en août 2019._
{% endalert %}

## aliasage de lien dans les Content Blocks {#link-aliasing-in-content-blocks}

Les nouveaux Content Blocks auront leurs liens modifiés : Braze ajoutera un `lid={{placeholder}}` à chaque lien le cas échéant. Cette valeur de marque substitutive est résolue lors de l'insertion dans une variante de message e-mail.

Pour modifier les liens dans les Content Blocks existants créés avant que Braze n'active l'aliasage de lien, dupliquez les Content Blocks existants, puis modifiez les liens dans les Content Blocks dupliqués.

Lorsqu'un Content Block sans valeur `lid` est inséré dans un nouveau message, les liens de ce Content Block ne sont pas suivis avec un alias. Lorsqu'un nouveau Content Block est inséré dans une « ancienne » variante de message, les liens de cette variante de message seront reconnus par l'aliasage de lien. Les liens du Content Block sont également reconnus. Cependant, les « anciens » Content Blocks ne peuvent pas imbriquer de « nouveaux » Content Blocks.

{% alert tip %}
Pour les Content Blocks, Braze recommande de créer des copies des Content Blocks existants à utiliser dans les nouveaux messages. Cela peut être fait par duplication en masse pour éviter les scénarios où vous pourriez référencer un Content Block pour lequel l'aliasage de lien n'a pas été activé dans un nouveau message.
{% endalert %}

## aliasage de lien pour les URL générées par Liquid {#link-aliasing-for-urls-generated-by-liquid}

Pour les URL générées par Liquid (par exemple, `assign` dans le HTML, des valeurs extraites d'un Content Block ou du Liquid dans un attribut personnalisé), Braze a besoin d'un emplacement clair pour insérer le paramètre de requête `lid`. Dans la plupart des cas, lorsque du Liquid reste dans l'URL, Braze ne déduit pas s'il faut commencer une nouvelle chaîne de requête avec `?` ou rejoindre une requête existante avec `&`, à moins que vous n'ajoutiez vous-même ce délimiteur.

Procédez comme suit :

- Si l'URL ne contient **pas** déjà une chaîne de requête, ajoutez `?` après le Liquid (par exemple, `{{my_url}}?`).
- Si l'URL contient **déjà** `?` et des paramètres de requête, ajoutez `&` après le Liquid (par exemple, `{{my_url}}&`).

{% alert note %}
Lorsque vous utilisez des [modèles de liens]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template) avec des URL générées par Liquid, Braze peut normaliser de manière conservatrice l'URL rendue après l'exécution du Liquid lorsqu'elle contient exactement deux caractères `?` utilisés comme séparateurs de requête. Le second `?` peut être réécrit en `&` afin que Braze modifie le moins possible l'URL. <br><br>Braze n'essaie pas de corriger tous les cas de `?` en double, et le traitement des URL plus complexes reste intentionnellement limité. Ajoutez d'abord le bon `?` ou `&` dans votre balisage, et considérez toute normalisation comme un garde-fou limité — et non comme un substitut à des URL bien formées ou pour faire reconnaître les liens dans **Link Management** lorsqu'aucun délimiteur n'est présent.
{% endalert %}

Sans un `?` ou `&` final (ou un autre point d'insertion pris en charge), l'aliasage de lien ne reconnaît pas l'URL, **Link Management** ne la liste pas et les modèles de liens ne s'appliquent pas.

### Fragments d'URL (`#`) et paramètres de suivi {#url-fragments-and-tracking-parameters}

Le fragment (`#` et tout ce qui suit) n'est pas envoyé au serveur lors d'une requête de lien normale. Braze insère `lid` dans la chaîne de requête, qui doit apparaître avant le `#`. Si votre `href` contient du Liquid et un fragment `#` mais pas de `?` ou `&` avant le `#`, Braze ne peut pas ajouter `lid` de manière sûre, et le lien peut ne pas apparaître dans **Link Management** ou être suivi en tant qu'alias de lien.

Cela est particulièrement courant dans l'éditeur par glisser-déposer lorsqu'une URL de bouton mélange du Liquid avec un schéma basé sur un hash (par exemple, un chemin statique, puis `#`, puis des paires clé-valeur supplémentaires). Dans ce cas, ajoutez `?` immédiatement avant le `#` afin que la chaîne de requête (y compris `lid`) soit analysée avant le fragment.

{% raw %}
```text
https://example.com/campaign/to/abc123?#user_id={{${user_id}}}&source=email
```
{% endraw %}

Dans l'exemple précédent, le `?` avant `#` fournit à Braze un segment de requête auquel ajouter `lid`. Sans cela, le lien peut ne pas apparaître dans **Link Management**.

Sans identification de l'endroit où ajouter les paramètres de requête, l'aliasage de lien ne reconnaît pas ces URL et les modèles de liens ne s'appliquent pas. Si vous voyez des erreurs telles que **Failed to be assigned an LID** pour une URL dynamique, vérifiez que le `href` utilise le schéma `?` ou `&` montré dans les exemples de cette section.

### Considérations pour l'éditeur par glisser-déposer {#drag-and-drop-editor-considerations}

Dans l'éditeur par glisser-déposer, les champs contenant un lien (comme l'**URL** d'un bouton) valident le `href` sous-jacent avant l'exécution du Liquid. Les espaces, sauts de ligne et autres caractères non compatibles avec les URL peuvent provoquer un comportement inattendu lorsque Braze ajoute des modèles de liens ou des paramètres d'aliasage de lien. Lorsque vous avez besoin de Liquid conditionnel pour la destination, définissez l'URL dans un bloc HTML (voir la section suivante) et référencez une seule variable dans le champ **URL** de l'éditeur par glisser-déposer au lieu d'y placer directement du Liquid complexe.

### Exemple avec un Content Block {#content-block-example}

{% raw %}
Si un Content Block contient un lien tel que `https://www.braze.com/{{custom_attribute.${offer_id}}}` sans `?` ou `&` final, Braze ne sait pas où ajouter `lid`, et le lien n'est donc pas pris en compte pour **Link Management**. Ajoutez `?` ou `&` à la fin de l'URL dans le Content Block (selon qu'une chaîne de requête existe déjà ou non), enregistrez le Content Block, et le lien pourra être reconnu.
{% endraw %}

### Rapports lorsque l'URL varie par utilisateur {#reporting-when-the-url-varies-per-user}

Chaque `href` distinct dans le message correspond à **un** identifiant de lien et un alias de lien pour **Link Management** et les rapports basés sur les alias. Lorsque les alias de lien sont suivis, les rapports e-mail dans le tableau de bord sont indexés par l'alias plutôt que par chaque URL résolue possible.

Utilisez d'abord les approches suivantes dans Braze :

- **Analyse des e-mails de Campaign et Canvas :** Consultez les clics agrégés par lien depuis **Message Analytics** > **Email Performance** > **Preview & Heatmap** avec **Show Heatmap** activé, comme décrit dans [Liens non suivis](#untracking-links).
- **Clics par destinataire dans le Query Builder :** Exécutez le [modèle du Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates#email-templates) **Email URLs clicked** pour une Campaign ou un Canvas. Le modèle fait apparaître les liens dépersonnalisés pour les comptages résumés ; l'export CSV inclut les identifiants des utilisateurs ayant cliqué, le lien sur lequel ils ont cliqué et un horodatage. (Les URL dépersonnalisées suppriment les tags Liquid pour la vue résumée ; consultez la description du modèle pour plus de détails.)
- **Ventilations par alias dans le composeur :** Si vous avez besoin que chaque destination (par exemple, chaque `offer_id`) apparaisse comme sa propre ligne dans **Link Management** et dans les rapports basés sur les alias, utilisez des valeurs `href` distinctes (et donc des alias distincts) — par exemple, des liens distincts par branche — au lieu d'un seul lien dont le chemin change par utilisateur.

Si vous utilisez également des exports de streaming d'engagement, les événements de clic e-mail incluent un champ **`url`** ; consultez [Événement de clics e-mail](#email-clicks-event) sur cette page pour savoir comment ce payload est lié à l'aliasage de lien.

### Exemple {#example}

Utilisez ce schéma lorsque l'URL assignée n'a pas de paramètres de requête :

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Visit Braze</a>
```
{% endraw %}

Si l'URL assignée contient déjà `?` et des paramètres de requête, ajoutez `&` après le Liquid au lieu de `?` :

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?campaign=test" %}

<a href="{{link_with_params}}&">Visit Braze</a>
```
{% endraw %}

### URL avec du Liquid conditionnel {#urls-with-conditional-liquid}

Lorsque des tags Liquid conditionnels sont utilisés dans un `href` (par exemple, pour définir une URL avec {% raw %}`{% if %}`, `{% elsif %}` ou `{% unless %}`{% endraw %}), l'aliasage de lien ne s'applique pas à ces liens. Cela signifie que ces liens n'apparaissent pas dans **Link Management** et ne reçoivent pas de `lid` pour le suivi des clics.

**Recommandé :** Construisez l'URL finale dans un bloc HTML avec `assign` (ou {% raw %}`{% capture %}`{% endraw %}), puis référencez cette variable partout où vous avez besoin du lien. Dans l'éditeur par glisser-déposer, collez la variable dans le champ **URL** du bouton avec un `?` ou `&` final selon le cas — par exemple, `{{url}}?`.

{% raw %}
```liquid
{% if {{custom_attribute.${account_tier}}} == "pro" %}
{% assign url = "https://example.com/pro/verify" %}
{% else %}
{% assign url = "https://example.com/retail/account" %}
{% endif %}
```
{% endraw %}

Dans le champ **URL** du bouton (éditeur par glisser-déposer) ou en HTML, pointez le `href` vers la variable avec un délimiteur :

{% raw %}
```liquid
<a href="{{ url }}?">Go to account</a>
```
{% endraw %}

Vous pouvez également capturer l'URL dans une seule variable :

{% raw %}
```liquid
{% capture url %}
  {%- if condition -%}
    https://example.com/url1
  {%- else -%}
    https://example.com/url2
  {%- endif -%}
{% endcapture %}

<a href="{{ url }}?">Go to account</a>
```
{% endraw %}

## Résolution des problèmes {#troubleshooting}

### Destinations qui n'acceptent pas le paramètre `lid` {#destinations-that-dont-accept-the-lid-parameter}

Lorsque vous envoyez un message de test depuis l'éditeur d'e-mail, Braze ajoute {% raw %}`lid={{placeholder}}`{% endraw %} à vos liens (la marque substitutive devient une valeur unique au moment de l'envoi). Si le site ou l'API de destination ne tolère pas les paramètres de requête supplémentaires, le lien peut fonctionner dans l'éditeur, mais échouer lorsqu'il est ouvert depuis l'e-mail.

Sans la valeur `lid`, Braze ne traite pas l'URL comme un lien avec aliasing pour le suivi et la segmentation. Nous vous recommandons de mettre à jour votre backend ou votre site afin qu'il ignore le paramètre de requête `lid` lorsqu'il est présent. Cela préserve l'aliasage de lien, le reporting et les cas d'usage de Segments décrits dans cet article.

Vous pouvez également désactiver l'aliasage de lien dans le tableau de bord pendant que vous planifiez une modification du backend. Accédez à **Paramètres** > **Préférences e-mail** > **Paramètres d'aliasage de lien**.

Si vous ne pouvez pas modifier vos systèmes de destination, contactez le [support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) pour désactiver l'aliasage de lien pour votre espace de travail. Tenez compte des considérations suivantes si l'aliasage de lien est désactivé pour votre espace de travail :

- Les nouveaux e-mails et Content Blocks ne recevront généralement pas de nouveau balisage d'aliasage de lien (comme le paramètre de requête `lid`).
- Les messages existants qui ont été créés lorsque l'aliasage de lien était activé peuvent encore contenir du balisage d'aliasage de lien dans le HTML. Vous devrez peut-être supprimer manuellement les paramètres `lid` résiduels là où vous ne les souhaitez plus.
- Si vous modifiez une Campaign existante, une étape d'e-mail Canvas ou un Content Block, vous devrez peut-être ajouter à nouveau les modèles de lien afin que les liens modélisés s'affichent correctement.
- Le reporting des clics pour les envois effectués lorsque l'aliasage de lien était activé peut ne pas correspondre proprement au reporting après la désactivation de la fonctionnalité.
- Les Segments qui utilisent des filtres basés sur l'aliasage de lien (par exemple, les filtres **Clicked Alias**) peuvent cesser de renvoyer les audiences attendues.