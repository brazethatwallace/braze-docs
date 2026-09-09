---
nav_title: Aperçu
page_order: 0
noindex: true
---

# Exemple de mise en page : Aperçu

> La mise en page d'aperçu permet de créer une option de navigation spécifique en haut d'une page, offrant aux utilisateurs la possibilité de cliquer sur un bouton pour accéder à une partie précise de la page ou à une tout autre page.

La page des [journaux des modifications du SDK]({{site.baseurl}}/developer_guide/changelogs) ou la [page des détails créatifs des messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types) sont des exemples classiques de la mise en page du sélecteur.

## Composants requis

1. Notation d'ouverture et de fermeture YAML. Autrement dit, --- avant le contenu et --- après.
2. Guillemets autour de certains contenus de paramètres. (Paramètres d'en-tête, paramètres de texte, contenu comportant des tirets ou d'autres caractères spéciaux.)
3. Notation des tags de glossaire (il s'agit d'étiquettes de filtre)

## Paramètres obligatoires

|Paramètre | Type de contenu | Détails |
|---|---|---|
| `page_order`| numérique | Ordonne la page au sein de la section. Cet ordre sera reflété dans la navigation de gauche. |
| `nav-title`| Alphanumérique | Titre qui apparaîtra dans la navigation de gauche. |
|`layout`| Alphanumérique - Sans espaces | Sélectionnez une mise en page dans la [section des mises en page](https://github.com/Appboy/braze-docs/tree/develop/_layouts) de la documentation. |
| `guide_top_header`|Alphanumérique | Donnez un titre à votre page.|
| `guide_top_text`|Alphanumérique | Décrivez votre page, ce texte apparaîtra directement au-dessus des boutons et de leur titre. Des guillemets sont requis autour du contenu. |
| `guide_featured_title`| Alphanumérique | Donnez un titre à vos cartes. Ce titre apparaîtra directement au-dessus des boutons.
| `guide_featured_list`| YAML supplémentaire, Alphanumérique | Voir [Format de liste du guide](#guide-listing-format) ci-dessous. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paramètres obligatoires" }

### Format de liste du guide

|Paramètre | Type de contenu | Détails |
|---|---|---|
|`name`| Alphanumérique | Nommez la case. |
| `link`| URL ou chemin | Lien vers la destination de la case. Doit contenir l'URL complète ou (si c'est un lien interne) `/docs...`  |
|`image`| Chemin | Lien vers l'emplacement de l'image. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Format de liste du guide" }

Exemple de format :

```yaml
- name: Modal
  link: /docs/user_guide/channels/in_app_messages/message_types/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
```

```yaml
---
nav_title: Détails créatifs
page_order: 4
layout: featured
guide_top_header: "Détails créatifs"
guide_top_text: "Faites preuve de créativité avec nos messages in-app ! Mais vous devez d'abord connaître certaines directives ! Après tout, il faut connaître les règles pour pouvoir les enfreindre ! Consultez les spécifications créatives de chaque type de message ou les détails créatifs généraux ci-dessous."

guide_featured_title: "Spécifications créatives par type de message"
guide_featured_list:
- name: Fenêtre modale
  link: /docs/user_guide/channels/in_app_messages/message_types/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Contextuel
  link: /docs/user_guide/channels/in_app_messages/message_types/#slideup
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: Plein écran
  link: /docs/user_guide/channels/in_app_messages/message_types/#full-screen
  image: /assets/img/braze_icons/expand-05.svg
---

# Détails créatifs {#general}

Les messages in-app de Braze ont des spécifications créatives à la fois globales et individuelles. Pour plus d'informations sur nos types de messages in-app plus personnalisables, consultez notre page [Personnaliser]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/).

{% alert important %}
  Ces détails ne s'appliquent qu'à notre génération la plus récente de messages in-app (génération 3). Si vous n'utilisez pas notre dernière génération de messages in-app, consultez notre documentation sur les [générations précédentes de messages in-app]({{ site.baseurl }}/help/best_practices/in-app_messages/previous_in-app_message_generations/).
{% endalert %}