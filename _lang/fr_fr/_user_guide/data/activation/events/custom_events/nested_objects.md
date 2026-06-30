---
nav_title: Objets imbriqués
article_title: Objets imbriqués dans les événements personnalisés
page_order: 1
page_type: reference
description: "Cet article décrit comment envoyer des données JSON imbriquées en tant que propriétés d'événements personnalisés et d'achats, et comment utiliser ces objets imbriqués dans votre envoi de messages."
---

# Objets imbriqués dans les événements personnalisés {#nested-objects-in-custom-events}

> Cette page explique comment envoyer des données JSON imbriquées en tant que propriétés d'événements personnalisés et d'achats, et comment utiliser ces objets imbriqués dans votre envoi de messages.

Vous pouvez utiliser des objets imbriqués (c'est-à-dire des objets qui se trouvent à l'intérieur d'un autre objet) pour envoyer des données JSON imbriquées en tant que propriétés d'événements personnalisés et d'achats. Ces données imbriquées peuvent être utilisées pour créer des modèles d'informations personnalisées dans les messages, déclencher l'envoi de messages et segmenter les utilisateurs.

## Restrictions {#considerations}

- Les données imbriquées sont prises en charge pour les [événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events) et les [événements d'achat]({{site.baseurl}}/user_guide/data/activation/events/purchase_events), mais pas pour les autres types d'événements.
- Les objets de propriétés d'événement contenant des valeurs de type tableau ou objet peuvent avoir une charge utile de propriétés d'événement allant jusqu'à 100 Ko.
- Les schémas de propriétés d'événement ne peuvent pas être générés pour les événements d'achat.
- Les schémas de propriétés d'événement sont générés par échantillonnage des événements personnalisés des dernières 24 heures.

### Versions minimales du SDK {#minimum-sdk-versions}

Les versions suivantes du SDK prennent en charge les objets imbriqués :

{% sdk_min_versions swift:5.0.0 android:20.0.0 web:3.3.0 %}

## Étape 1 : Générer un schéma {#step-1-generate-a-schema}

Vous pouvez accéder aux données imbriquées de votre événement personnalisé en générant un schéma pour chaque événement comportant des propriétés d'événement imbriquées. Pour générer un schéma :

1. Accédez à **Paramètres des données** > **Événements personnalisés**.
2. Sélectionnez **Gérer les propriétés** pour les événements comportant des propriétés imbriquées.
3. Sélectionnez le bouton <i class="fas fa-arrows-rotate"></i> pour générer le schéma. Pour afficher le schéma, sélectionnez le bouton <i class="fas fa-plus"></i> plus.

![Sélectionnez le bouton pour générer le schéma. Pour afficher le schéma, sélectionnez le bouton plus.]({% image_buster /assets/img_archive/schema_generation_example.png %}){: style="max-width:80%;"}

Si de nouvelles propriétés sont envoyées ultérieurement, elles ne figureront pas dans le schéma tant que celui-ci n'aura pas été régénéré. Les schémas peuvent être régénérés toutes les 24 heures.

## Étape 2 : Utiliser l'objet imbriqué {#step-2-use-the-nested-object}

Vous pouvez référencer les données imbriquées lors de la segmentation et de la personnalisation. Notez qu'un schéma n'est pas requis. Consultez les sections suivantes pour des exemples d'utilisation :

- [Corps de la requête API](#api-request-body)
- [Modèles Liquid](#liquid-templating)
- [Déclenchement de messages](#message-triggering)
- [Segmentation](#segmentation)
- [Personnalisation](#personalization)

### Corps de la requête API {#api-request-body}

{% tabs %}
{% tab Music Example %}

Voici un exemple `/users/track` avec un événement personnalisé « Created Playlist ». Après la création d'une playlist, capturez les propriétés de la playlist en envoyant :
- Une requête API qui liste « songs » comme propriété
- Un tableau des propriétés imbriquées des chansons

```
...
"properties": {
  "songs": [
    {
      "title": "Smells Like Teen Spirit",
      "artist": "Nirvana",
      "album": {
        "name": "Nevermind",
        "yearReleased": "1991"
      }
    },
    {
      "title": "While My Guitar Gently Weeps",
      "artist": "the Beatles",
      "album": {
        "name": "The Beatles",
        "yearReleased": "1968"
      }
    }
  ]
}
...
```
{% endtab %}
{% tab Restaurant Example%}

Voici un exemple `/users/track` avec un événement personnalisé « Ordered ». Après la finalisation d'une commande, capturez les propriétés de cette commande en envoyant :
- Une requête API qui liste `r_details` comme propriété
- Les propriétés imbriquées de cette commande

```
...
"properties": {
  "r_details": {
    "name": "SandwichEmperor",
    "identifier": "12345678",
    "location" : {
      "city": "Montclair",
      "state": "NJ"
    }
  }
}
...
```
{% endtab %}
{% endtabs %}

{% alert note %}
Pour les propriétés d'événement personnalisé imbriquées, si l'année est inférieure à 0 ou supérieure à 3000, Braze ne stocke pas ces valeurs sur l'utilisateur.
{% endalert %}

### Modèles Liquid {#liquid-templating}

Voici comment créer un modèle Liquid qui référence les propriétés imbriquées demandées dans la [requête API précédente](#api-request-body).

{% tabs %}
{% tab Music Example %}
Modèle Liquid dans un message déclenché par l'événement « Created Playlist » :

{% raw %}
`{{event_properties.${songs}[0].album.name}}` : "Nevermind"<br>
`{{event_properties.${songs}[1].title}}` : "While My Guitar Gently Weeps"
{% endraw %}

{% endtab %}
{% tab Restaurant Example %}
Modèle Liquid dans un message déclenché par l'événement « Ordered » :

{% raw %}
`{{event_properties.${r_details}.location.city}}` : "Montclair"
{% endraw %}

{% endtab %}
{% endtabs %}

### Déclenchement de messages {#message-triggering}

Pour utiliser ces propriétés afin de déclencher une campagne, sélectionnez votre événement personnalisé ou achat, puis ajoutez un filtre **Propriété imbriquée**. Notez que le déclenchement de messages n'est pas encore pris en charge pour les messages in-app, mais les propriétés imbriquées dans la personnalisation Liquid des messages s'afficheront tout de même.

{% tabs %}
{% tab Music Example %}

Déclenchement d'une campagne avec des propriétés imbriquées de l'événement « Created Playlist » :

![Un utilisateur choisissant une propriété imbriquée pour les filtres de propriétés sur un événement personnalisé.]({% image_buster /assets/img/nested_object2.png %})

La condition de déclenchement `songs[].album.yearReleased` « est » « 1968 » correspondra à un événement dans lequel l'une des chansons possède un album sorti en 1968. La notation entre crochets `[]` permet de parcourir les tableaux, et la correspondance est établie si **n'importe quel** élément du tableau parcouru correspond à la propriété d'événement.

{% alert important %}
Le filtre **n'est pas égal à** ne correspond que si aucune des propriétés de votre tableau n'est égale à la valeur fournie. <br><br>Par exemple, supposons que le Canvas A possède un filtre de propriété imbriquée d'événement personnalisé basé sur l'action **est égal à** « smartwatch », et que le Canvas B possède un filtre de propriété imbriquée d'événement personnalisé basé sur l'action **n'est pas égal à** « simphone ». Si vos propriétés contiennent « smartwatch » et « simphone », les deux Canvas se déclencheront. En revanche, si l'une de vos propriétés contient « simphone » ou « sim only », aucun des deux Canvas ne se déclenchera.
{% endalert %}

{% endtab %}
{% tab Restaurant Example %}

Déclenchement d'une campagne avec des propriétés imbriquées de l'événement « Ordered » :

![Un utilisateur ajoutant le filtre de propriété r_details.name est SandwichEmperor pour un événement personnalisé.]({% image_buster /assets/img/nested_object1.png %})

`r_details.name` : "SandwichEmperor"<br>
`r_details.location.city` : "Montclair"
{% endtab %}
{% endtabs %}

{% alert note %}
Si votre propriété d'événement contient les caractères `[]` ou `.`, échappez-les en encadrant la portion concernée avec des guillemets doubles. Par exemple, `"songs[].album".yearReleased` correspondra à un événement avec la propriété littérale `"songs[].album"`.
{% endalert %}

### Segmentation {#segmentation}

Pour segmenter les utilisateurs en fonction de propriétés d'événement imbriquées, vous devez utiliser les [Extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension). Après avoir généré un schéma, l'explorateur d'objets imbriqués s'affichera dans la section de segmentation.

![Capture d'écran liée à la segmentation.]({% image_buster /assets/img_archive/nested_event_properties_segmentation.png %})

La segmentation utilise la même notation que le déclenchement (voir [Déclenchement de messages](#message-triggering)).

Pour modifier ou créer des Extensions de segments, vous devez disposer de la permission « Modifier les segments ».

### Personnalisation {#personalization}

À l'aide de la fenêtre modale **Ajouter une personnalisation**, sélectionnez **Propriétés d'événement avancées** comme type de personnalisation. Cela permet d'ajouter des propriétés d'événement imbriquées après la génération d'un schéma.

![À l'aide de la fenêtre modale Ajouter une personnalisation, sélectionnez Propriétés d'événement avancées comme type de personnalisation. Cela permet d'ajouter des propriétés d'événement imbriquées après la génération d'un schéma.]({% image_buster /assets/img_archive/nested_event_properties_personalization.png %}){: style="max-width:70%;"}

## Tester les objets imbriqués dans les messages {#testing-nested-objects-in-messages}

L'outil **Prévisualisation et test** du tableau de bord ne prend pas en charge l'ajout de données fictives pour les objets imbriqués ou les attributs personnalisés imbriqués. Pour tester les messages qui référencent des données imbriquées via Liquid, vous pouvez prévisualiser les messages avec des attributs imbriqués en tant qu'utilisateur existant possédant cet attribut imbriqué, ou prévisualiser les messages avec des propriétés d'événement personnalisé en lançant une campagne en production vers des utilisateurs test.

### Attributs personnalisés imbriqués {#nested-custom-attributes}

1. Importez les attributs imbriqués dans le profil de l'utilisateur test via l'API.
2. Dans votre campagne ou Canvas, accédez à **Prévisualisation et test**.
3. Sélectionnez **Prévisualiser en tant qu'utilisateur** et recherchez l'utilisateur test. Le Liquid sera résolu en utilisant les attributs imbriqués réels du profil de cet utilisateur.

### Propriétés d'événement imbriquées {#nested-event-properties}

Les propriétés d'événement imbriquées ne peuvent pas être prévisualisées dans le tableau de bord car elles nécessitent un déclenchement d'événement en temps réel. Pour tester :

1. Créez une campagne ou une étape du Canvas qui cible uniquement vos utilisateurs test et qui est déclenchée par (ou référence) l'événement personnalisé avec des propriétés imbriquées.
2. Lancez la campagne vers votre audience test.
3. Enregistrez l'événement personnalisé avec le payload d'objet imbriqué sur le profil de votre utilisateur test (via l'API ou le SDK).
4. Vérifiez que le message s'affiche correctement avec les valeurs des propriétés imbriquées.

## Questions fréquentes {#frequently-asked-questions}

### L'utilisation d'objets imbriqués entraîne-t-elle la consommation de points de donnée supplémentaires ? {#does-using-nested-objects-log-additional-data-points}

La façon dont nous comptabilisons les points de donnée ne change pas avec l'ajout de cette fonctionnalité. La segmentation basée sur des objets imbriqués utilise les Extensions de segments, qui ne consomment pas de points de donnée supplémentaires.

### Quelle quantité de données imbriquées peut être envoyée ? {#how-much-nested-data-can-be-sent}

Si une ou plusieurs propriétés de l'événement contiennent des données imbriquées, le payload maximum pour l'ensemble des propriétés combinées d'un événement est de 100 Ko. Toute requête dépassant cette limite de taille sera rejetée.