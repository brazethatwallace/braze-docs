---
nav_title: Bonnes pratiques
article_title: Bonnes pratiques
toc_headers: h2
page_order: 1
page_type: reference
description: "Cette page fournit un aperçu de l'ingestion de données cloud, des bonnes pratiques et des limites du produit."
---

# Bonnes pratiques {#best-practices}

> L'ingestion de données cloud de Braze vous permet d'établir une connexion directe entre votre entrepôt de données ou votre système de stockage de fichiers et Braze, afin de synchroniser les données pertinentes relatives aux utilisateurs ou aux catalogues. Lorsque vous synchronisez ces données avec Braze, vous pouvez les exploiter pour des cas d'usage tels que la personnalisation, le déclenchement ou la segmentation.

## Comprendre la colonne `UPDATED_AT` {#understanding-the-updated_at-column}

{% alert note %}
`UPDATED_AT` est pertinent uniquement pour les intégrations d'entrepôts de données, pas pour les synchronisations S3.
{% endalert %}

Lorsqu'une synchronisation s'exécute, Braze se connecte directement à votre instance d'entrepôt de données, récupère toutes les nouvelles données de la table spécifiée et met à jour les données correspondantes sur votre tableau de bord de Braze. À chaque exécution de la synchronisation, Braze reflète toutes les données mises à jour.

{% alert important %}
Braze CDI synchronisera les lignes strictement en fonction de la valeur `UPDATED_AT`, indépendamment du fait que le contenu de la ligne soit identique à ce qui est actuellement dans Braze. C'est pourquoi nous recommandons d'utiliser `UPDATED_AT` correctement afin de ne synchroniser que les données nouvelles ou mises à jour et d'éviter une consommation inutile de points de donnée.
{% endalert %}

### Exemple : synchronisation récurrente {#example-recurring-sync}

Pour illustrer comment `UPDATED_AT` est utilisé dans une synchronisation CDI, considérons cet exemple de synchronisation récurrente pour la mise à jour d'attributs utilisateur :

- Sources de stockage de fichiers
   - Amazon S3

## Types de données pris en charge {#supported-data-types}

L'ingestion de données cloud prend en charge les types de données suivants :
- Attributs utilisateur, notamment :
   - Attributs personnalisés imbriqués
   - Tableaux d'objets
   - Statuts d'abonnement
- Événements personnalisés
- Événements d'achat
- Éléments de catalogue
- Demandes de suppression d'utilisateurs

### Éviter les problèmes de types de données {#avoiding-data-type-issues}

Lorsque vous utilisez l'ingestion de données cloud pour synchroniser des données provenant de sources externes (telles que Databricks ou Snowflake), assurez-vous que les colonnes de votre source utilisent les types de données corrects avant la synchronisation. Parmi les problèmes courants :

- **Horodatages stockés sous forme de chaînes de caractères :** assurez-vous que vos colonnes de dates utilisent un type timestamp ou datetime dans votre base de données source, et non un type varchar ou string.
- **Nombres stockés sous forme de chaînes de caractères :** convertissez les colonnes numériques en types integer ou float dans votre requête source avant la synchronisation.
- **Types incohérents d'une synchronisation à l'autre :** si le type d'une colonne change entre deux synchronisations, Braze peut rejeter les nouvelles données. Vérifiez que le schéma de votre source reste cohérent.

Pour forcer ou modifier les types de données des attributs personnalisés dans le tableau de bord de Braze, consultez [Gérer les données personnalisées]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data#forcing-data-type-comparisons).

Vous pouvez mettre à jour les données utilisateur par ID externe, alias d'utilisateur, ID Braze, e-mail ou numéro de téléphone. Vous pouvez supprimer des utilisateurs par ID externe, alias d'utilisateur ou ID Braze.

## Ce qui est synchronisé {#what-gets-synced}

À chaque exécution d'une synchronisation, Braze recherche les lignes qui n'ont pas encore été synchronisées. Cette vérification s'effectue à l'aide de la colonne `UPDATED_AT` de votre table ou vue. Braze sélectionne et importe toutes les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur `UPDATED_AT` synchronisée. Les lignes se trouvant exactement à l'horodatage limite peuvent également être resynchronisées si de nouvelles lignes sont ajoutées avec ce même horodatage entre deux exécutions.

{% alert important %}
CDI suit le nombre de lignes à la dernière valeur `UPDATED_AT` synchronisée. Si de nouvelles lignes sont ajoutées avec ce même horodatage entre deux exécutions, CDI passe à une limite inclusive (`>=`) et resynchronise toutes les lignes à cet horodatage, y compris celles déjà traitées. Pour éviter les synchronisations en double et la consommation inutile de points de donnée, utilisez des valeurs `UPDATED_AT` uniques entre les exécutions de synchronisation. Pour en savoir plus, consultez [Éviter la resynchronisation des lignes avec des horodatages dupliqués](#avoid-resyncing-rows-with-duplicate-timestamps).
{% endalert %}

Dans votre entrepôt de données, ajoutez les utilisateurs et attributs suivants à votre table, en définissant l'heure `UPDATED_AT` sur le moment où vous ajoutez ces données :

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>payload</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

Lors de la prochaine synchronisation planifiée, Braze synchronise toutes les lignes dont l'horodatage `UPDATED_AT` est postérieur au dernier horodatage synchronisé. Braze met à jour ou ajoute les champs, vous n'avez donc pas besoin de synchroniser l'intégralité du profil utilisateur à chaque fois. Après la synchronisation, les profils utilisateur reflètent les nouvelles mises à jour :

**Synchronisation récurrente, deuxième exécution le 20 juillet 2022 à 12 h**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>payload</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

Une nouvelle ligne a été ajoutée pour `customer_9012`, mais sa valeur `UPDATED_AT` (`2022-07-16 00:25:30`) est antérieure à l'horodatage enregistré (`2022-07-19 09:07:23`), elle ne sera donc pas synchronisée. Cependant, la ligne existante pour `customer_5678` a une valeur `UPDATED_AT` égale à l'horodatage enregistré, elle est donc resynchronisée en raison de la limite inclusive. Pour plus de détails sur ce comportement, consultez [Assurez-vous que l'heure UPDATED_AT n'est pas identique à l'heure de votre synchronisation](#make-sure-the-updated_at-time-isnt-the-same-time-as-your-sync). La valeur `UPDATED_AT` enregistrée reste `2022-07-19 09:07:23`.

**Synchronisation récurrente, troisième exécution le 21 juillet 2022 à 12 h**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>payload</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"xyz",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-21 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-20T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

Lors de cette troisième exécution, une nouvelle ligne a été ajoutée pour `customer_1234` avec une valeur `UPDATED_AT` (`2022-07-21 08:30:00`) postérieure à l'horodatage enregistré. Cette nouvelle ligne ainsi que la ligne existante pour `customer_5678` (dont la valeur `UPDATED_AT` est égale à l'horodatage enregistré) sont toutes deux synchronisées. La valeur `UPDATED_AT` enregistrée est désormais définie sur `2022-07-21 08:30:00`.

{% alert note %}
Les valeurs `UPDATED_AT` peuvent même être postérieures à l'heure de début d'exécution d'une synchronisation donnée. Cependant, cela n'est pas recommandé, car cela repousse le dernier horodatage `UPDATED_AT` « dans le futur » et les synchronisations suivantes ne synchroniseront pas les valeurs antérieures.
{% endalert %}

## Utiliser un horodatage UTC pour la colonne `UPDATED_AT` {#use-a-utc-timestamp-for-the-updated_at-column}

La colonne `UPDATED_AT` doit être en UTC pour éviter les problèmes liés aux changements d'heure. Privilégiez les fonctions exclusivement UTC, comme `SYSDATE()` au lieu de `CURRENT_DATE()`, dans la mesure du possible.

## Éviter la re-synchronisation de lignes avec des horodatages en double {#avoid-resyncing-rows-with-duplicate-timestamps}

CDI suit le nombre de lignes au dernier horodatage `UPDATED_AT` synchronisé. Si CDI détecte que de nouvelles lignes ont été ajoutées avec ce même horodatage depuis la dernière exécution, il utilise une limite inclusive (`>=`) pour re-sélectionner toutes les lignes à cet horodatage, y compris celles déjà traitées. Sinon, CDI utilise une limite exclusive (`>`) et ne sélectionne que les lignes strictement postérieures à la dernière valeur synchronisée.

Par exemple, si une synchronisation traite cinq lignes avec `UPDATED_AT = 2025-04-01 00:00:00`, et qu'une sixième ligne est ajoutée ultérieurement avec le même horodatage, la synchronisation suivante détecte le changement de nombre et re-synchronise les six lignes. Cela peut entraîner des données en double et une consommation inutile de points de donnée.

Pour éviter cela :

- Si vous configurez une synchronisation avec une `VIEW`, n'utilisez pas `CURRENT_TIMESTAMP` comme valeur par défaut. Cela entraînerait la synchronisation de toutes les données à chaque exécution, car le champ `UPDATED_AT` serait évalué au moment de l'exécution de la requête.
- Si vous avez des pipelines ou des requêtes de longue durée qui écrivent des données dans votre table source, évitez de les exécuter en même temps qu'une synchronisation, ou évitez d'utiliser le même horodatage pour chaque ligne insérée.
- Utilisez une transaction pour écrire toutes les lignes qui partagent le même horodatage.
- Utilisez des valeurs `UPDATED_AT` uniques et croissantes de manière monotone pour éviter que des lignes ne soient re-sélectionnées après avoir été traitées.

### Exemple : gestion des mises à jour ultérieures {#example-managing-subsequent-updates}

Cet exemple illustre le processus général de synchronisation des données pour la première fois, puis de mise à jour des seules données modifiées (deltas) lors des mises à jour suivantes. Supposons que nous ayons une table `EXAMPLE_DATA` contenant des données utilisateur. Le jour 1, elle contient les valeurs suivantes :

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table aria-label="Exemple : gestion des mises à jour ultérieures">
  <caption>Exemple : gestion des mises à jour ultérieures</caption>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td>823</td>
            <td>blue</td>
            <td>380</td>
            <td>FALSE</td>
        </tr>
        <tr>
            <td>23456</td>
            <td>28</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td>384</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td>red</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td>813</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

Pour obtenir ces données dans le format attendu par CDI, vous pouvez exécuter la requête suivante :

```sql
SELECT
    CURRENT_TIMESTAMP AS UPDATED_AT,
    EXTERNAL_ID AS EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT(
            'attribute_1', attribute_1,
            'attribute_2', attribute_2,
            'attribute_3', attribute_3,
            'attribute_4', attribute_4
        )
    ) AS PAYLOAD
FROM EXAMPLE_DATA;
```

Rien de tout cela n'ayant été synchronisé avec Braze auparavant, ajoutez l'ensemble à la table source pour CDI :

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>payload</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
  </tbody>
</table>

Une synchronisation s'exécute et Braze enregistre que vous avez synchronisé toutes les données disponibles jusqu'à « 2023-03-16 15:00:00 ». Ensuite, le matin du jour 2, un processus ETL s'exécute et certains champs de votre table d'utilisateurs sont mis à jour (indiqués par *) :

<table aria-label="Exemple : gestion des mises à jour ultérieures">
  <caption>Exemple : gestion des mises à jour ultérieures. * indique un champ mis à jour depuis la dernière synchronisation.</caption>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td style="background-color: #FFFF00;">145*</td>
            <td style="background-color: #FFFF00;">red*</td>
            <td>380</td>
            <td style="background-color: #FFFF00;">TRUE*</td>
        </tr>
        <tr>
            <td>23456</td>
            <td style="background-color: #FFFF00;">15*</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td style="background-color: #FFFF00;">495*</td>
            <td style="background-color: #FFFF00;">FALSE*</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td style="background-color: #FFFF00;">green*</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td style="background-color: #FFFF00;">693*</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

Vous devez maintenant ajouter uniquement les valeurs modifiées dans la table source CDI. Ces lignes peuvent être ajoutées en complément plutôt que de remplacer les anciennes. La table se présente désormais comme suit :

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>payload</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "145", "ATTRIBUTE_2":"red", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "15"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_3":"495", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_2":"green"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_3":"693"}</code></td>
    </tr>
  </tbody>
</table>

CDI ne synchronisera que les nouvelles lignes, de sorte que la prochaine synchronisation ne portera que sur les cinq dernières lignes.

## Conseils supplémentaires {#additional-tips}

### N'écrivez que les attributs nouveaux ou mis à jour pour minimiser la consommation {#only-write-new-or-updated-attributes-to-minimize-consumption}

À chaque exécution d'une synchronisation, Braze recherche les lignes qui n'ont pas encore été synchronisées. Cette vérification repose sur la colonne `UPDATED_AT` de votre table ou vue. Braze sélectionne et importe toutes les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur `UPDATED_AT` synchronisée, que ces lignes soient identiques ou non à ce qui figure actuellement sur le profil utilisateur. Les lignes situées à l'horodatage limite peuvent également être re-synchronisées si de nouvelles lignes partagent cet horodatage. C'est pourquoi nous recommandons de ne synchroniser que les attributs que vous souhaitez ajouter ou mettre à jour.

La consommation de points de données est identique avec CDI et avec les autres méthodes d'ingestion comme les REST API ou les SDK. Il vous revient donc de vous assurer que seuls les attributs nouveaux ou mis à jour figurent dans vos tables sources.

### Séparez `EXTERNAL_ID` de la colonne `payload` {#separate-external_id-from-payload-column}

L'objet `payload` ne doit contenir ni ID externe ni aucun autre type d'identifiant.

### Supprimer un attribut {#remove-an-attribute}

Vous pouvez le définir sur `null` si vous souhaitez omettre un attribut du profil d'un utilisateur. Si vous souhaitez qu'un attribut reste inchangé, ne l'envoyez pas à Braze tant qu'il n'a pas été mis à jour. Pour supprimer entièrement un attribut, utilisez `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`.

### Effectuez des mises à jour incrémentales {#make-incremental-updates}

Effectuez des mises à jour incrémentales de vos données afin d'éviter les écrasements involontaires lorsque des mises à jour simultanées sont effectuées.

{% alert important %}
* **Mises à jour d'attributs différents :** dans la grande majorité des cas, si deux mises à jour ne concernent pas les mêmes attributs d'un utilisateur, elles produisent des résultats entièrement indépendants. Par exemple, si vous mettez à jour l'attribut `Color` d'un utilisateur et que vous mettez séparément à jour son attribut `Size`, les deux mises à jour devraient être appliquées correctement, même si elles surviennent à quelques secondes d'intervalle.
* **Mises à jour du même attribut :** des conditions de concurrence peuvent survenir lorsque plusieurs mises à jour ciblent le même attribut au cours d'une même exécution de synchronisation. Dans ces rares cas, une mise à jour peut écraser l'autre. La meilleure façon d'éviter ce comportement est de s'assurer que les données sources de votre synchronisation CDI reflètent uniquement l'état le plus récent de chaque utilisateur, ou que toutes les mises à jour pour un utilisateur donné ou une paire utilisateur+attribut sont contenues dans une seule ligne.
* **Opérateurs de tableau d'objets :** les seules exceptions aux mises à jour indépendantes concernent les opérateurs `$add`, `$remove` et `$update` pour les tableaux d'objets, où les mises à jour portant sur le même tableau peuvent interagir entre elles.
* **Événements :** les conditions de concurrence n'affectent pas les événements, car chaque événement est unique et possède un horodatage qui lui est associé.
{% endalert %}

La meilleure façon d'éviter ce comportement est de s'assurer que les données sources de votre synchronisation CDI reflètent uniquement l'état le plus récent de chaque utilisateur, ou que toutes les mises à jour pour un utilisateur donné ou une paire utilisateur+attribut sont contenues dans une seule ligne.

### Créer une chaîne JSON à partir d'une autre table {#create-a-json-string-from-another-table}

Si vous préférez stocker chaque attribut dans sa propre colonne en interne, vous devez convertir ces colonnes en une chaîne JSON pour alimenter la synchronisation avec Braze. Pour ce faire, vous pouvez utiliser une requête comme :

{% tabs local %}
{% tab Snowflake %}
Utilisez cette requête dans Snowflake pour formater les colonnes sources en champs CDI.
```sql
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    )as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab Redshift %}
Utilisez cette requête dans Redshift pour formater les colonnes sources en champs CDI.
```sql
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    ) as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab BigQuery %}
Utilisez cette requête dans BigQuery pour formater les colonnes sources en champs CDI.
```sql
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (attribute_1 string,
     attribute_2 STRING,
     attribute_3 NUMERIC,
     my_user_id STRING);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        'attribute_1' AS attribute_1,
        'attribute_2'AS attribute_2,
        'yet_another_attribute'AS attribute_3
      )
    ) as PAYLOAD
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Databricks %}
Utilisez cette requête dans Databricks pour formater les colonnes sources en champs CDI.
```sql
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (
    attribute_1 string,
    attribute_2 STRING,
    attribute_3 NUMERIC,
    my_user_id STRING
);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        attribute_1,
        attribute_2,
        attribute_3
      )
    ) as PAYLOAD
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Microsoft Fabric %}
Utilisez cette requête dans Microsoft Fabric pour formater les colonnes sources en champs CDI.
```sql
CREATE TABLE [braze].[users] (
    attribute_1 VARCHAR,
    attribute_2 VARCHAR,
    attribute_3 VARCHAR,
    attribute_4 VARCHAR,
    user_id VARCHAR
)
GO

CREATE VIEW [braze].[user_update_example]
AS SELECT
    user_id as EXTERNAL_ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[users] ;
```
{% endtab %}

{% endtabs %}

### Utilisez l'horodatage `UPDATED_AT` {#use-the-updated_at-timestamp}

Braze utilise l'horodatage `UPDATED_AT` pour suivre les données qui ont été synchronisées avec succès. CDI suit également le nombre de lignes au dernier horodatage synchronisé. Si de nouvelles lignes sont ajoutées avec le même horodatage entre deux exécutions, CDI re-synchronise toutes les lignes portant cet horodatage, ce qui peut entraîner des données en double. Pour plus de détails et de conseils, consultez [Éviter la re-synchronisation de lignes avec des horodatages en double](#avoid-resyncing-rows-with-duplicate-timestamps).

### Configuration des tables {#table-configuration}

Nous disposons d'un [dépôt GitHub](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion) public permettant aux clients de partager des bonnes pratiques ou des extraits de code. Pour contribuer vos propres extraits, créez une pull request !

### Formatage des données {#data-formatting}

Les exigences de configuration des tables pour l'ingestion de données cloud et les exigences de formatage du payload sont documentées dans [Configuration des tables pour l'ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).

Utilisez cette page pour distinguer :

- Les exigences relatives aux tables sources (colonnes requises, colonnes d'identification et comportement de `UPDATED_AT`)
- Les exigences relatives au payload (quels champs doivent correspondre au format d'objet `/users/track` pour chaque type de données)

### Éviter les délais d'expiration pour les requêtes d'entrepôt de données {#avoid-timeouts-for-data-warehouse-queries}

Nous recommandons que les requêtes soient achevées en moins d'une heure pour des performances optimales et pour éviter les erreurs potentielles. Si les requêtes dépassent ce délai, envisagez de revoir la configuration de votre entrepôt de données. L'optimisation des ressources allouées à votre entrepôt peut contribuer à améliorer la vitesse d'exécution des requêtes.

## Limitations du produit {#product-limitations}

| Limitation            | Description                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nombre d'intégrations | Il n'y a pas de limite au nombre d'intégrations que vous pouvez configurer. Cependant, vous ne pourrez configurer qu'une seule intégration par table ou vue.                                             |
| Nombre de lignes         | Par défaut, chaque exécution peut synchroniser jusqu'à 500 millions de lignes. Braze interrompt toute synchronisation dépassant 500 millions de nouvelles lignes. Si vous avez besoin d'une limite plus élevée, contactez votre gestionnaire du succès des clients Braze ou le support Braze. |
| Attributs par ligne     | Chaque ligne doit contenir un identifiant utilisateur unique et un objet JSON comprenant jusqu'à 250 attributs. Chaque clé de l'objet JSON compte comme un attribut (c'est-à-dire qu'un tableau compte comme un seul attribut). |
| Taille du payload           | Chaque ligne peut contenir un payload d'une taille maximale de 1 Mo. Braze rejette les payloads supérieurs à 1&nbsp;Mo et enregistre l'erreur « Payload was greater than 1MB » dans le journal de synchronisation avec l'ID externe associé et le payload tronqué. |
| Type de données              | Vous pouvez synchroniser des attributs utilisateur, des événements et des achats via l'ingestion de données cloud.                                                                                                  |
| Région Braze           | Ce produit est disponible dans toutes les régions Braze. N'importe quelle région Braze peut se connecter à n'importe quelle région de données source.                                                                              |
| Région source       | Braze se connectera à votre entrepôt de données ou environnement cloud dans n'importe quelle région ou chez n'importe quel fournisseur cloud.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limitations du produit" }

<br><br>