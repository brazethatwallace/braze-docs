---
nav_title: Attributs personnalisés imbriqués
article_title: Attributs personnalisés imbriqués
alias: "/nested_custom_attribute_support/"
page_order: 3
page_type: reference
description: "Cet article de référence explique comment utiliser les attributs personnalisés imbriqués en tant que type de données pour des attributs personnalisés, avec les limitations et des exemples d'utilisation."
---

# Attributs personnalisés imbriqués {#nested-custom-attributes}

> Cette page traite des attributs personnalisés imbriqués, qui vous permettent de définir un ensemble d'attributs en tant que propriété d'un autre attribut. En d'autres termes, lorsque vous définissez un objet d'attribut personnalisé, vous pouvez définir un ensemble d'attributs supplémentaires pour cet objet.

## À propos des attributs imbriqués {#about-nested-attributes}

Les attributs imbriqués vous permettent de créer des Segments plus riches et de personnaliser vos messages à l'aide de données provenant d'un seul objet d'attribut personnalisé.

Dans l'exemple suivant, l'attribut personnalisé `favorite_book` contient les attributs imbriqués `title`, `author` et `publishing_date`. Cet objet peut être utilisé pour cibler des utilisateurs par auteur, filtrer par date de publication ou insérer le titre du livre directement dans un message :

```json
"favorite_book": {
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
}
```


{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## Considérations {#considerations}

- Les attributs personnalisés imbriqués sont destinés aux attributs personnalisés envoyés via le SDK ou l'API Braze.
- Les objets ont une taille maximale de 100&nbsp;Ko. Si une mise à jour entraîne un dépassement de 100&nbsp;Ko pour l'objet, Braze rejette la mise à jour et l'attribut reste inchangé.
- Les noms de clés et les valeurs de chaînes de caractères ont une limite de 255 caractères.
- Les noms de clés ne peuvent pas contenir d'espaces.
- Les points (`.`) et les signes dollar (`$`) ne sont pas des caractères pris en charge dans un payload d'API si vous tentez d'envoyer un attribut personnalisé imbriqué à un profil utilisateur.
- Tous les partenaires Braze ne prennent pas en charge les attributs personnalisés imbriqués. Consultez la [documentation des partenaires]({{site.baseurl}}/partners/home) pour vérifier si des intégrations partenaires spécifiques prennent en charge cette fonctionnalité.
- Les attributs personnalisés imbriqués ne peuvent pas être utilisés comme filtre lors d'un appel à l'API Connected Audience.
- Par défaut, le filtre de Segment **Nested Custom Attributes** inclut les attributs personnalisés de type objet, les attributs de type tableau d'objets et les attributs personnalisés de type tableau. Lorsque vous sélectionnez un attribut, le sélecteur de schéma de propriétés inclut les chemins de tableau (en utilisant la notation `[]`) pour les champs de tableaux imbriqués. Pour masquer les attributs personnalisés de type tableau de niveau supérieur dans ce filtre, contactez le [support Braze]({{site.baseurl}}/braze_support).
- Lors de la prévisualisation de messages dans le tableau de bord à l'aide de **Preview as a Custom User**, vous ne pouvez saisir des données fictives que sous forme de chaîne de caractères ou de tableau de chaînes de caractères — les objets imbriqués ne sont pas pris en charge. Pour prévisualiser un message qui fait référence à des attributs personnalisés imbriqués, sélectionnez un utilisateur existant qui possède déjà l'attribut imbriqué dans son profil. Pour les propriétés d'événement personnalisé imbriquées, vous devez lancer une Campaign en direct ciblant un utilisateur test pour vérifier le rendu.

## Exemple d'API {#api-example}

{% tabs local %}
{% tab Créer %}
Voici un exemple `/users/track` avec un objet « Most Played Song ». Pour capturer les propriétés de la chanson, nous enverrons une requête API qui répertorie `most_played_song` en tant qu'objet, accompagné d'un ensemble de propriétés d'objet.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Mettre à jour %}
Pour mettre à jour un objet existant, envoyez une requête POST à `users/track` avec le paramètre `_merge_objects` dans la requête. Cela effectuera une fusion en profondeur de votre mise à jour avec les données d'objet existantes. La fusion en profondeur garantit que tous les niveaux d'un objet sont fusionnés dans un autre objet, et pas seulement le premier niveau. Dans cet exemple, nous avons déjà un objet `most_played_song` dans Braze, et nous ajoutons maintenant un nouveau champ, `year_released`, à l'objet `most_played_song`.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "most_played_song": {
          "year_released": 1960
      }
    }
  ]
}
```

Une fois cette requête reçue, l'objet d'attribut personnalisé ressemblera à ceci :

```json
{"most_played_song": {
  "song_name": "Solea",
  "artist_name" : "Miles Davis",
  "album_name": "Sketches of Spain",
  "year_released": 1960,
  "genre": "Jazz",
  "play_analytics": {
     "count": 1000,
     "top_10_listeners": true
  }
}}
```

{% alert warning %}
Vous devez définir `_merge_objects` sur `true`, sinon vos objets seront écrasés. `_merge_objects` est défini sur `false` par défaut.
{% endalert %}

{% endtab %}
{% tab Supprimer %}
Pour supprimer un objet d'attribut personnalisé, envoyez une requête POST à `users/track` avec l'objet d'attribut personnalisé défini sur `null`.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": null
    }
  ]
}
```

{% alert note %}
Cette approche ne peut pas être utilisée pour supprimer une clé imbriquée à l'intérieur d'un [tableau d'objets]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects).
{% endalert %}

{% endtab %}
{% endtabs %}

## Exemple SDK {#sdk-example}

{% sdk_min_versions android:25.0.0 ios:6.1.0 web:4.7.0 %}

{% tabs local %}
{% tab Android SDK %}

**Créer**
```kotlin
val json = JSONObject()
    .put("song_name", "Solea")
    .put("artist_name", "Miles Davis")
    .put("album_name", "Sketches of Spain")
    .put("genre", "Jazz")
    .put(
        "play_analytics",
        JSONObject()
            .put("count", 1000)
            .put("top_10_listeners", true)
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json)
}
```

**Mettre à jour**
```kotlin
val json = JSONObject()
    .put("year_released", 1960)

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json, true)
}
```

**Supprimer**
```kotlin
braze.getCurrentUser { user ->
    user.unsetCustomUserAttribute("most_played_song")
}
```

{% endtab %}
{% tab Swift SDK %}

**Créer**
```swift
let json: [String: Any?] = [
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": [
    "count": 1000,
    "top_10_listeners": true,
  ],
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json)
```

**Mettre à jour**
```swift
let json: [String: Any?] = [
  "year_released": 1960
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json, merge: true)
```

**Supprimer**
```swift
braze.user.unsetCustomAttribute(key: "most_played_song")
```

{% endtab %}
{% tab Web SDK %}

**Créer**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": {
    "count": 1000,
    "top_10_listeners": true
  }
};
braze.getUser().setCustomUserAttribute("most_played_song", json);
```

**Mettre à jour**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "year_released": 1960
};
braze.getUser().setCustomUserAttribute("most_played_song", json, true);

```

**Supprimer**
```javascript
import * as braze from "@braze/web-sdk";
braze.getUser().setCustomUserAttribute("most_played_song", null);
```

{% endtab %}
{% endtabs %}

## Capturer des dates en tant que propriétés d'objet {#capturing-dates-as-object-properties}

Pour capturer des dates en tant que propriétés d'objet, vous devez utiliser la clé `$time`. Dans l'exemple suivant, un objet « Important Dates » est utilisé pour capturer l'ensemble des propriétés d'objet, `birthday` et `wedding_anniversary`. La valeur de ces dates est un objet avec une clé `$time`, qui ne peut pas être une valeur nulle.

{% alert note %}
Si vous n'avez pas capturé les dates en tant que propriétés d'objet initialement, nous vous recommandons de renvoyer ces données en utilisant la clé `$time` pour tous les utilisateurs. Sinon, cela peut entraîner des Segments incomplets lors de l'utilisation de l'attribut `$time`. Cependant, si la valeur de `$time` dans un attribut personnalisé imbriqué n'est pas correctement formatée, l'ensemble de l'attribut personnalisé imbriqué ne sera pas mis à jour.
{% endalert %}

```json
{
  "attributes": [
    {
      "external_id": "time_with_nca_test",
      "important_dates": {
        "birthday": {"$time" : "1980-01-01"},
        "wedding_anniversary": {"$time" : "2020-05-28"}
      }
    }
  ]
}
```

{% alert note %}
Pour les attributs personnalisés imbriqués, si l'année est inférieure à 0 ou supérieure à 3000, Braze ne stocke pas ces valeurs sur l'utilisateur.
{% endalert %}

## Modèles Liquid {#liquid-templating}

L'exemple de modèle Liquid suivant montre comment référencer les propriétés d'objet d'attribut personnalisé enregistrées à partir de la requête API précédente et les utiliser dans vos messages.

Utilisez la balise de personnalisation `custom_attribute` et la notation par points pour accéder aux propriétés d'un objet. Spécifiez le nom de l'objet (et la position dans le tableau si vous référencez un tableau d'objets), suivi d'un point, suivi du nom de la propriété.

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` — "Miles Davis"
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` — "Solea"
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` — "1000"
{% endraw %}

Pour utiliser le Liquid d'attribut personnalisé imbriqué dans votre message :

1. Accédez à une Campaign ou un Canvas, puis ouvrez l'étape de message où vous souhaitez ajouter la personnalisation.
2. Dans le compositeur de message, insérez l'extrait de code Liquid à l'endroit où vous souhaitez que la valeur apparaisse.
3. Utilisez **Aperçu et test** avec un utilisateur existant qui possède déjà l'attribut personnalisé imbriqué sur son profil pour confirmer que la valeur s'affiche comme prévu.

### Personnalisation {#personalization}

Vous pouvez utiliser **Add Personalization** pour insérer un attribut personnalisé imbriqué dans votre message.

Pour ouvrir **Add Personalization** :

1. Accédez à une Campaign ou un Canvas, puis ouvrez l'étape de message où vous souhaitez ajouter la personnalisation.
2. Dans le compositeur de message, sélectionnez **Personalization** pour ouvrir le panneau latéral **Add Personalization**, où vous pouvez choisir les options de personnalisation.

Pour configurer la personnalisation d'attribut personnalisé imbriqué :

1. Dans **Personalization Type**, sélectionnez **Nested Custom Attributes**.
2. Dans **Top Level Attribute**, sélectionnez le chemin de l'attribut personnalisé imbriqué que vous souhaitez insérer.
   Par exemple, sélectionnez `preferences.neighborhood_office`.
3. Facultatif : dans **Default value**, saisissez une valeur de repli pour les utilisateurs qui n'ont pas leur propre valeur pour cet attribut.
4. Vérifiez l'extrait de code **Liquid Snippet** généré pour confirmer qu'il correspond au chemin attendu.
5. Sélectionnez **Insert**.

Pour cet exemple, Braze insère la valeur imbriquée de `preferences.neighborhood_office` dans votre message. Les valeurs par défaut sont des valeurs de repli que votre message inclut pour les utilisateurs qui n'ont pas leur propre valeur pour un attribut.

{% alert tip %}
Vérifiez qu'un schéma a été généré si vous ne voyez pas l'option d'insertion d'attributs personnalisés imbriqués.
{% endalert %}

## Générer et régénérer les schémas {#regenerate-schema}

Pour utiliser les attributs personnalisés imbriqués dans la segmentation et la personnalisation, vous devez générer un schéma pour l'attribut. Une fois qu'un schéma a été généré, vous pouvez le régénérer selon vos besoins. Pour des informations plus détaillées sur les schémas, consultez [Générer un schéma à l'aide de l'explorateur d'objets imbriqués]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes#generate-schema).

### Générer un schéma {#generate-a-schema}

Après avoir créé un attribut personnalisé imbriqué et envoyé des données à Braze, vous pouvez générer le schéma :

1. Accédez à **Data Settings** > **Custom Attributes**.
2. Recherchez votre attribut personnalisé imbriqué.
3. Dans la colonne **Attribute Name** correspondant à votre attribut, sélectionnez <i class="fas fa-arrows-rotate"></i> **Generate Schema**.

Une fois le schéma généré, l'icône <i class="fas fa-arrows-rotate"></i> se transforme en une icône <i class="fas fa-plus"></i> plus que vous pouvez sélectionner pour afficher et gérer le schéma.

### Régénérer un schéma {#regenerate-a-schema}

Pour régénérer le schéma de votre attribut personnalisé imbriqué :

1. Accédez à **Data Settings** > **Custom Attributes**.
2. Recherchez votre attribut personnalisé imbriqué.
3. Dans la colonne **Attribute Name** correspondant à votre attribut, sélectionnez <i class="fas fa-plus"></i> **Manage schema** pour gérer le schéma.
4. Une fenêtre modale apparaîtra. Sélectionnez **Regenerate Schema**.

Vous ne pouvez pas lancer une autre régénération tant qu'une tâche de schéma est déjà **en cours** (l'option est indisponible tant que le statut est **Generating**). Une seule tâche de génération de schéma peut s'exécuter à la fois par entreprise. La régénération du schéma ne détecte que les nouveaux objets et ne supprime pas les objets qui existent déjà dans le schéma.

{% alert important %}
Pour réinitialiser le schéma d'un tableau d'objets avec un objet existant, vous devez créer un nouvel attribut personnalisé. La régénération du schéma ne supprime pas les objets existants.
{% endalert %}

Si les données n'apparaissent pas comme prévu après la régénération du schéma, il est possible que l'attribut ne soit pas ingéré assez fréquemment. Les données utilisateur sont échantillonnées à partir des données précédemment envoyées à Braze pour l'attribut imbriqué concerné. Si l'attribut n'est pas ingéré suffisamment, il ne sera pas pris en compte pour le schéma.

## Déclencher des modifications d'attributs personnalisés imbriqués {#trigger-nested-custom-attribute-changes}

Vous pouvez déclencher une action lorsqu'un objet d'attribut personnalisé imbriqué change. Cette option n'est pas disponible pour les modifications apportées aux tableaux d'objets. Si vous ne voyez pas d'option pour afficher l'explorateur de chemins, vérifiez que vous avez généré un schéma.

Par exemple, dans une Campaign basée sur une action, vous pouvez ajouter une nouvelle action de déclenchement pour **Modifier la valeur de l'attribut personnalisé** afin de cibler les utilisateurs qui ont modifié leurs préférences de bureau de quartier.

Pour configurer ce déclencheur dans une Campaign basée sur une action :

1. Créez ou modifiez une Campaign, puis définissez le type de réception sur **Livraison par événement**.
2. Dans les paramètres de déclenchement, sélectionnez **Modifier la valeur de l'attribut personnalisé**.
3. Sélectionnez le chemin de l'attribut personnalisé imbriqué que vous souhaitez surveiller.
   Par exemple, sélectionnez `preferences.neighborhood_office`.
4. Sélectionnez la condition de déclenchement souhaitée, telle que **toute nouvelle valeur**.
5. Terminez la configuration du message et de l'audience de votre Campaign, puis lancez la Campaign.

## Résolution des problèmes {#troubleshooting}

### Valeurs d'attributs personnalisés imbriqués non appliquées de manière cohérente {#nested-custom-attribute-values-not-applied-consistently}

Si vous constatez que les valeurs d'attributs personnalisés imbriqués ne sont pas ajoutées de manière cohérente aux profils utilisateur, le problème est souvent lié à des incompatibilités de types de données.

Pour diagnostiquer et résoudre ce problème :

1. **Comparez des exemples d'utilisateurs :** Obtenez un exemple d'utilisateur réussi et un exemple non réussi pour lesquels l'attribut personnalisé imbriqué aurait dû être défini.
2. **Examinez la structure des données :** Affichez et comparez les valeurs de l'attribut personnalisé sur les deux profils :
   - Les propriétés sont-elles stockées sous un objet ?
   - Les propriétés sont-elles stockées sous forme de tableau de propriétés ?
3. **Vérifiez le filtre de segmentation :** Comparez la structure de données stockée avec la manière dont l'attribut personnalisé imbriqué est référencé dans vos filtres de segmentation.
4. **Vérifiez le type de données :** Pour identifier le type de données d'un attribut personnalisé :
   - Accédez à **Data Settings** > **Custom Attributes**.
   - Recherchez l'attribut personnalisé de niveau supérieur qui contient l'attribut imbriqué que vous souhaitez vérifier.
   - Si la ligne affiche **Generate Schema**, sélectionnez-le pour générer d'abord le schéma.
   - Une fois le schéma généré, sélectionnez l'icône plus dans la colonne **Attribute Name** pour cet attribut.
   - Dans la fenêtre modale **Edit schema**, examinez les attributs imbriqués et leurs valeurs correspondantes dans la colonne **Data type**.

Si vous constatez que le type de données ne correspond pas au format prévu sur l'ensemble des profils utilisateur, supprimez la valeur incorrectement formatée des profils utilisateur concernés et renvoyez l'attribut dans le format correct en utilisant la requête API ou la méthode SDK appropriée.

## Comportement de la segmentation avec les tableaux d'objets {#segmentation-behavior-with-arrays-of-objects}

Lorsque vous utilisez plusieurs filtres `Nested Custom Attribute` avec une logique ET pour segmenter sur un tableau d'objets, chaque filtre est évalué indépendamment sur l'ensemble des éléments du tableau. Un utilisateur est qualifié pour le Segment si _n'importe quel_ élément du tableau satisfait chaque filtre individuel — les filtres n'ont pas besoin de correspondre au _même_ élément.

Par exemple, supposons qu'un utilisateur possède le tableau suivant :

```json
{
  "orders": [
    {"product": "Shoes", "price": 80},
    {"product": "Hat", "price": 25}
  ]
}
```

Un Segment avec les filtres ET suivants :

- `orders[].price` est supérieur à 50
- `orders[].price` est inférieur à 30

Cet utilisateur serait qualifié car le premier filtre correspond à l'élément « Shoes » (80 > 50) et le second filtre correspond à l'élément « Hat » (25 < 30). Même si aucun élément individuel ne satisfait les deux conditions, l'utilisateur entre tout de même dans le Segment.

Si vous avez besoin que toutes les conditions correspondent au même élément au sein d'un tableau, utilisez la [segmentation multi-critères]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes#use-multi-criteria-segmentation) sur le même chemin, ou restructurez vos données pour éviter la correspondance inter-éléments.

## Points de donnée {#data-points}

Toute clé envoyée consomme un point de donnée. Par exemple, cet objet initialisé dans le profil utilisateur compte comme sept (7) points de donnée :

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "year_released": 1960,
        "genre": "Jazz",
        "play_analytics": {
          "count": 1000,
          "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% alert note %}
La mise à jour d'un attribut personnalisé de type objet à `null` consomme également un point de donnée.
{% endalert %}