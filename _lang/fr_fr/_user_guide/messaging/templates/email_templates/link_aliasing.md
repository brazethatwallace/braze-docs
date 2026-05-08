---
nav_title: Aliasage de lien
article_title: Aliasage de lien
alias: /link_aliasing/
page_order: 3
description: "Cet article décrit le fonctionnement de l'aliasage de lien et fournit des exemples de ce à quoi vos liens ressembleront."
channel:
  - email

---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}Aliasage de lien {#braze-learning-course-imagebuster-assetsimgblicon3png-httpslearningbrazecomlink-aliasing-stylefloatrightwidth120pxborder0-classnoimgborderlink-aliasing}

> Utilisez l'aliasage de lien pour créer des noms reconnaissables, générés par l'utilisateur, afin d'identifier les liens envoyés dans les e-mails depuis Braze. Ces liens sont disponibles pour le reciblage par segmentation, le déclenchement basé sur les actions et l'analyse des liens.

## À propos de l'aliasage de lien {#about-link-aliasing}

L'aliasage de lien vous permet de créer des noms générés par l'utilisateur pour identifier et suivre les liens envoyés dans les e-mails. Vous pouvez ainsi utiliser efficacement ces alias de lien reconnaissables dans vos e-mails pour suivre l'engagement et analyser les performances des campagnes, sans avoir besoin de référencer le lien complet.

Avec l'aliasage de lien, vous pouvez :

- **Recibler les utilisateurs qui ont cliqué sur des liens spécifiques :** identifier et cibler les utilisateurs qui ont cliqué sur un lien.
- **Créer des déclencheurs basés sur les actions :** envoyer un e-mail lorsqu'un utilisateur clique sur un lien.
- **Analyser les indicateurs :** comparer combien d'utilisateurs ont cliqué sur le lien A par rapport au lien B.

### Comment ça fonctionne {#how-it-works}

Braze identifie de manière unique les liens dans les e-mails en ajoutant un paramètre supplémentaire appelé `lid` (également connu sous le nom d'identifiant de lien) à chaque URL de lien. Cette valeur `lid` permet à Braze de suivre, surveiller et agréger les interactions des utilisateurs avec le lien, même si les autres paramètres de l'URL peuvent différer. Cela permet de fournir des informations sur la façon dont les utilisateurs interagissent avec le contenu de vos campagnes par e-mail.

Les identifiants de lien seront également mis à jour si une campagne par e-mail, un Canvas avec un message e-mail ou un Content Block est dupliqué.

## Créer un alias de lien {#creating-a-link-alias}

Pour créer un alias de lien, suivez ces étapes :

1. Dans votre Campaign ou composant Canvas, accédez au corps de votre e-mail.
2. Sélectionnez l'onglet **Link Management**.
3. Braze génère automatiquement des alias de lien par défaut uniques pour chacun de vos liens.
4. Donnez un nom à l'alias. Les alias doivent être nommés de manière unique par variante de Campaign par e-mail ou composant Canvas.

Vous pouvez également définir un alias qui sera utilisé pour référencer un lien spécifique lors du traitement des rapports ou de la segmentation.

![Page Link Management avec quatre alias de lien.]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
L'aliasage de lien est uniquement pris en charge dans les attributs `href` au sein des balises d'ancrage HTML où il est possible d'ajouter un paramètre de requête en toute sécurité. Il est recommandé d'inclure un point d'interrogation (?) à la fin de votre lien afin que Braze puisse facilement ajouter la valeur `lid`. Sans l'ajout de la valeur `lid`, Braze ne reconnaîtra pas l'URL pour l'aliasage de lien.
{% endalert %}

## Gérer les alias de lien {#managing-link-aliases}

Pour afficher tous vos alias de lien suivis, procédez comme suit :

1. Accédez à **Paramètres** > **Préférences des e-mails** sous **Paramètres de l'espace de travail**.
2. Sélectionnez l'onglet **Link Aliasing Settings**.

{% alert important %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/user_guide/administer/personal/the_braze_dashboard/), ces paramètres se trouvent sous **Gérer les paramètres**.
{% endalert %}

Ici, vous pouvez trier, rechercher et désactiver le suivi des alias de lien.

![Page Tracked Link Aliases affichant les alias de lien actifs et inactifs associés à diverses campagnes.]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
Utilisez les endpoints [Lister les alias de lien pour une Campaign]({{site.baseurl}}/get_campaign_link_alias/) et [Lister les alias de lien pour un Canvas]({{site.baseurl}}/get_canvas_link_alias/) pour extraire l'`alias` défini dans chaque variante de message d'une Campaign ou d'un composant Canvas spécifique aux e-mails.
{% endalert %}

Braze recommande d'évaluer les liens dans l'e-mail, d'ajouter des modèles de lien et de fournir une convention de nommage adaptée à la segmentation et aux rapports. Cela vous aide à garder une trace de tous les liens.

Lorsque l'aliasage de lien est activé, les messages, les Content Blocks et les modèles de lien ne sont pas modifiés. Tous les messages existants utilisant des modèles de lien ou des Content Blocks resteront identiques. Cependant, lorsque vous mettez à jour un message, le balisage d'alias de lien s'appliquera à tous les liens, vous devrez donc réappliquer les modèles de lien pour que les liens soient visibles.

## Comment les liens sont mis à jour avec l'aliasage de lien {#how-links-are-updated-with-link-aliasing}

Les tableaux suivants fournissent des exemples de liens dans le corps d'un e-mail, les résultats de l'aliasage de lien et des explications sur la façon dont le lien original est mis à jour avec l'aliasage de lien.

### Permalien {#permalink}

**Logique :** Braze insère un point d'interrogation (?) et ajoute le premier paramètre de requête dans l'URL.

| Lien dans le corps de l'e-mail | Lien avec aliasage |
|-----------------------|----------------------------------------|
| `https://www.braze.com` | `https://www.braze.com?lid=slfdldtqdhdk` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Lien avec des paramètres de requête supplémentaires {#link-with-more-query-parameters}

**Logique :** Braze détecte d'autres paramètres de requête et ajoute `lid=` à la fin de l'URL.

| Lien dans le corps de l'e-mail | Lien avec aliasage |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| `https://www.braze.com?utm_campaign=retention&utm_source=email` | `https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Lien HTML {#html-link}

**Logique :** Braze reconnaît qu'un lien est une URL et qu'un point d'interrogation (?) est déjà présent, le paramètre de requête `lid` est donc ajouté après le point d'interrogation.

| Lien dans le corps de l'e-mail | Lien avec aliasage |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Lien avec ancre {#link-with-anchor}

**Logique :** Braze s'attend à ce que l'URL utilise une structure standard où les ancres (#) sont présentes après un point d'interrogation (?). Comme Braze lit de gauche à droite, le point d'interrogation et la valeur `lid` sont ajoutés avant l'ancre.

| Lien dans le corps de l'e-mail | Lien avec aliasage |
|--------------------------------------------------|-------------------------------------------------------------------|
| `https://www.braze.com#bookmark1?utm_source=email` | `https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Lien avec ancre et balise de capture {#link-with-anchor-and-capture-tag}

**Logique :** Lors de l'utilisation de l'aliasage de lien avec des URL contenant des ancres (#), Braze s'attend à ce que l'ancre soit placée après les paramètres de requête. Cela signifie que la valeur `lid` doit être ajoutée **avant** l'ancre pour un suivi correct, et comme Braze lit l'URL de gauche à droite, le point d'interrogation (?) et le `lid` doivent précéder l'ancre.

| Lien dans le corps de l'e-mail | Lien avec aliasage |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions?lid={{link_alias}}#special-offer">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Suivi des alias de lien {#tracking-link-aliases}

Dans l'onglet **Link Management**, sélectionnez les alias que vous souhaitez marquer comme « suivis » à des fins de segmentation et pour qu'ils apparaissent dans les filtres de segmentation. Notez que les alias suivis sont uniquement destinés à la segmentation et n'auront aucun impact sur le suivi de votre lien à des fins de rapport.

{% alert tip %}
Pour suivre les indicateurs d'engagement des liens, assurez-vous que votre lien commence par HTTP ou HTTPS. Pour désactiver le suivi des clics pour des liens spécifiques, consultez [Liens universels et App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/#turning-off-click-tracking-on-a-link-to-link-basis).
{% endalert %}

Braze vous permet de sélectionner un nombre illimité de liens à suivre, mais vous ne pouvez recibler les utilisateurs que sur les liens les plus récents sur lesquels ils ont cliqué. Les profils utilisateur incluent les 100 liens les plus récemment cliqués. Par exemple, si vous suivez 500 liens et qu'un utilisateur clique sur les 500, vous pouvez recibler ou créer des segments basés sur les 100 liens les plus récemment cliqués.

![L'onglet Link Management avec deux liens sélectionnés.]({% image_buster /assets/img/link_management_dnd.png %})

{% alert note %}
Braze ne suit que les 100 derniers alias de lien cliqués au niveau du profil.
{% endalert %}

### Filtres basés sur les actions {#action-based-filters}

Vous pouvez créer des messages basés sur les actions ciblant n'importe quel lien (suivi ou non suivi) ou recibler les utilisateurs selon qu'ils ont cliqué sur un alias dans n'importe quelle Campaign par e-mail ou composant Canvas.

![Options basées sur les actions pour cibler les utilisateurs qui ont cliqué sur un alias dans un composant Canvas ou interagi avec une Campaign.]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

### Filtres de segmentation {#segmentation-filters}

Dans Braze, si vous avez un alias de lien dans votre e-mail et qu'un utilisateur clique dessus, l'événement est enregistré dans le profil de l'utilisateur avec l'alias.

Si vous utilisez le filtre de segmentation « A cliqué sur un alias dans n'importe quelle Campaign ou étape Canvas » et que vous décidez ensuite de renommer cet alias de lien, les données de clics précédentes dans le profil utilisateur ne sont **pas** mises à jour, ce qui signifie qu'elles affichent toujours l'ancien alias de lien. Ainsi, si vous ciblez des utilisateurs en fonction du nouvel alias de lien, cela n'inclura pas les données de l'ancien alias de lien.

Si vous utilisez le filtre de segmentation « A cliqué sur un alias dans une Campaign » ou « A cliqué sur un alias dans un Canvas », ce filtre sélectionne vos utilisateurs selon qu'ils ont cliqué sur un alias spécifique dans une Campaign ou un Canvas spécifique. Si plusieurs utilisateurs partagent la même adresse e-mail et que l'alias de lien est cliqué, tous les autres utilisateurs partageant cette adresse e-mail voient leur profil utilisateur mis à jour. Ces profils sont également mis à jour par les événements de réception et d'ouverture, pas seulement par les événements de clic.

Les filtres de segmentation suivants s'appliquent aux événements de clic qui sont suivis au moment où l'événement est traité. Cela signifie que le fait de ne plus suivre des liens ne supprimera pas les données existantes et que le suivi d'un lien ne remplira pas rétroactivement les données. Pour plus de détails, consultez [Filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/).

#### Arrêt du suivi des liens {#untracking-links}

L'arrêt du suivi d'un lien ne réaffectera pas les segments existants avec le filtre vers l'alias non suivi. Les anciennes données resteront dans les profils utilisateur jusqu'à ce qu'elles soient remplacées par des données plus récentes.

Les liens dans les messages archivés ne sont plus suivis automatiquement. Cependant, si des messages archivés sont désarchivés, les liens devront être suivis à nouveau. Lorsque les alias de lien sont suivis, les rapports de lien sont indexés par l'alias au lieu des domaines de premier niveau ou des URL complètes.

Pour afficher tous les liens de votre Campaign par e-mail et leurs clics totaux respectifs, accédez à **Message Analytics** > **Email Performance** > **Preview & Heatmap**, et sélectionnez le bouton bascule **Show Heatmap**.

![Panneau Link Table by Total Clicks avec les alias de lien et leurs clics totaux.]({% image_buster /assets/img/link_alias_total_clicks.png %}){: style="max-width:60%;"}

### Événement de clic sur un e-mail {#email-clicks-event}

Si vous exportez vos données d'engagement avec Currents, un événement de clic sur un e-mail sera légèrement différent si l'aliasage de lien est activé. Il comportera deux champs supplémentaires pour l'[événement de clic sur un e-mail]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-clicks-events/) lorsque l'aliasage de lien est activé : `link_id` et `link_alias`.

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
Le comportement de `dispatch_id` diffère entre Canvas et les Campaigns car Braze traite les étapes Canvas (à l'exception des étapes d'entrée, qui peuvent être planifiées) comme des événements déclenchés, même lorsqu'elles sont « planifiées ». En savoir plus sur le [comportement de `dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/) dans Canvas et les Campaigns.

_Mise à jour notée en août 2019._
{% endalert %}

## Aliasage de lien dans les Content Blocks {#link-aliasing-in-content-blocks}

Les nouveaux Content Blocks verront leurs liens modifiés, Braze ajoutant un `lid={{placeholder}}` à chaque lien le cas échéant. Cette valeur de marque substitutive est résolue lors de l'insertion dans une variante de message e-mail.

Pour modifier les liens dans les Content Blocks existants qui ont été créés avant que Braze n'active l'aliasage de lien, dupliquez les Content Blocks existants, puis modifiez les liens dans les Content Blocks dupliqués.

Lorsqu'un Content Block sans valeur `lid` est inséré dans un nouveau message, les liens de ce Content Block ne sont pas suivis avec un alias. Lorsqu'un nouveau Content Block est inséré dans une « ancienne » variante de message, les liens de cette variante de message seront reconnus par l'aliasage de lien. Les liens du Content Block sont également reconnus. Cependant, les « anciens » Content Blocks ne peuvent pas imbriquer de « nouveaux » Content Blocks.

{% alert tip %}
Pour les Content Blocks, Braze recommande de créer des copies des Content Blocks existants à utiliser dans les nouveaux messages. Cela peut être fait par duplication en masse pour éviter les scénarios où vous pourriez référencer un Content Block qui n'a pas été activé pour l'aliasage de lien dans un nouveau message.
{% endalert %}

## Aliasage de lien pour les URL générées par Liquid {#link-aliasing-for-urls-generated-by-liquid}

Pour les URL générées par Liquid, telles que les instructions `assign` dans le HTML ou depuis un Content Block, vous devez ajouter un point d'interrogation (`?`) à la balise Liquid. Cela permet à Braze d'ajouter des paramètres de requête (`lid=somevalue`) afin que l'aliasage de lien puisse fonctionner correctement.

Sans identifier où ajouter les paramètres de requête, l'aliasage de lien ne reconnaît pas ces URL et les modèles de lien ne s'appliquent pas.

### Exemple {#example}

Consultez cet exemple d'aliasage de lien pour le formatage recommandé du lien :

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Click Here</a>
```
{% endraw %}

Si le lien contient des paramètres incluant un point d'interrogation (`?`), vous pouvez le remplacer dans la balise d'ancrage par une esperluette (`&`), comme dans cet exemple :

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?param_1&param_2" %}

<a href="{{link_with_params}}&">Click Here</a>
```
{% endraw %}

### URL avec Liquid conditionnel {#urls-with-conditional-liquid}

Lorsque des balises Liquid conditionnelles sont utilisées à l'intérieur d'un `href` (par exemple, pour définir conditionnellement une URL en utilisant {% raw %}`{% if %}`, `{% unless %}`{% endraw %}), l'aliasage de lien ne s'applique pas à ces liens. Cela signifie que ces liens n'apparaissent pas dans **Link Management** et ne reçoivent pas de `lid` pour le suivi des clics.

Vous pouvez utiliser le bloc {% raw %}`{% capture %}`{% endraw %} pour construire l'URL en dehors du `href`, puis la référencer en tant que variable comme dans l'exemple suivant :

{% raw %}
```liquid
  {%- if condition -%}
    https://example.com/url1
  {%- else -%}
    https://example.com/url2
  {%- endif -%}
{%- endcapture -%}

<a href="{{ url }}?">Click here</a>
```
{% endraw %}