---
nav_title: Types de données
article_title: Types de données
page_order: 1
page_type: reference
description: "Référence des types de données pris en charge pour les attributs personnalisés, les propriétés d'événement et les catalogues dans Braze."
toc_headers: h2
---

# Types de données {#data-types}

> Cette page regroupe les types de données pris en charge pour les attributs personnalisés, les propriétés d'événement et les catalogues. Chaque type de données personnalisé offre une prise en charge et des contraintes légèrement différentes.

## Définitions {#definitions}

Utilisez ce tableau pour identifier les types de données disponibles pour les attributs de profil utilisateur, les données d'événement ou les éléments de catalogue. Consultez les sections suivantes pour connaître l'utilisation et les contraintes de chaque type.

<table role="presentation" class="definitions-table reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4 reset-td-br-5">
  <thead>
    <tr>
      <th>Type de données</th>
      <th>Définition</th>
      <th>Attributs personnalisés</th>
      <th>Propriétés d'événement</th>
      <th>Catalogues</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Valeur booléenne</td>
      <td>Valeur <code>true</code> ou <code>false</code></td>
      <td>✅ Pris en charge</td>
      <td>✅ Pris en charge</td>
      <td>✅ Pris en charge</td>
    </tr>
    <tr>
      <td>Nombre</td>
      <td>Nombre entier ou décimal</td>
      <td>✅ Pris en charge</td>
      <td>✅ Pris en charge</td>
      <td>✅ Pris en charge</td>
    </tr>
    <tr>
      <td>Chaîne de caractères</td>
      <td>Texte ; 255 caractères maximum</td>
      <td>✅ Pris en charge</td>
      <td>✅ Pris en charge</td>
      <td>✅ Pris en charge</td>
    </tr>
    <tr>
      <td>Heure</td>
      <td>Date et heure dans un format standard (<a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a>)</td>
      <td>✅ Pris en charge</td>
      <td>✅ Pris en charge</td>
      <td>✅ Pris en charge</td>
    </tr>
    <tr>
      <td>Tableau</td>
      <td>Liste ordonnée de valeurs</td>
      <td>✅ Pris en charge</td>
      <td>✅ Pris en charge</td>
      <td>✅ Pris en charge</td>
    </tr>
    <tr>
      <td>Objet</td>
      <td>Données structurées avec des champs nommés (paires clé-valeur imbriquées)</td>
      <td>✅ Pris en charge</td>
      <td>✅ Pris en charge</td>
      <td>✅ Pris en charge</td>
    </tr>
    <tr>
      <td>Tableau d'objets</td>
      <td>Liste d'objets</td>
      <td>✅ Pris en charge</td>
      <td>❌ Non pris en charge</td>
      <td>❌ Non pris en charge</td>
    </tr>
  </tbody>
</table>

### Considérations importantes {#important-considerations}

- **Tableau :** les attributs personnalisés et les propriétés d'événement ont des limites de taille. Les dates ne sont pas prises en charge dans les tableaux des propriétés d'événement. Les catalogues ne prennent en charge que les tableaux de chaînes de caractères, avec un maximum de 100 éléments.
- **Objet :** dans Braze, ce type apparaît sous le nom « attributs personnalisés imbriqués » pour les attributs personnalisés, « objets imbriqués » pour les propriétés d'événement et « objet JSON » pour les catalogues.
- **Heure :** dans les propriétés d'événement, ce type est intitulé « Datetime ».

## Types de données des attributs personnalisés {#custom-attribute-data-types}

Les attributs personnalisés prennent en charge les types de données répertoriés dans le tableau [Définitions](#definitions). Les sections suivantes décrivent l'utilisation et la segmentation pour chaque type pris en charge.

{% tabs %}
{% tab Valeur booléenne %}

Vous pouvez bloquer individuellement des attributs personnalisés depuis le menu d'actions, ou sélectionner et bloquer jusqu'à 100 attributs en masse. Lorsqu'un attribut personnalisé est bloqué, aucune donnée n'est collectée pour cet attribut, les données existantes ne sont plus accessibles (sauf réactivation), et les attributs bloqués n'apparaissent pas dans les filtres ni les graphiques. De plus, si l'attribut est actuellement référencé par des filtres ou des déclencheurs dans d'autres zones du tableau de bord de Braze, une fenêtre modale d'avertissement s'affiche pour vous informer que toutes les instances de filtres ou de déclencheurs qui le référencent seront supprimées et archivées.

### Marquer comme information personnelle identifiable (PII) {#marking-as-personally-identifiable-information-pii}

Les administrateurs peuvent également créer des attributs personnalisés et les marquer comme PII depuis cette page. Ces attributs ne sont visibles que par les administrateurs et les utilisateurs du tableau de bord disposant de l'autorisation « View Custom Attributes Marked as PII ».

### Ajouter des descriptions {#adding-descriptions}

Vous pouvez ajouter une description à un attribut personnalisé après sa création si vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions) `Manage Events, Attributes, Purchases`. Modifiez l'attribut personnalisé et saisissez ce que vous souhaitez, par exemple une note pour votre équipe.

### Ajouter des étiquettes {#adding-tags}

Vous pouvez ajouter des étiquettes à un attribut personnalisé après sa création si vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions) « Manage Events, Attributes, Purchases ». Vous pouvez ensuite utiliser ces étiquettes pour filtrer la liste des attributs.

### Supprimer des attributs personnalisés {#removing-custom-attributes}

Il existe deux façons de supprimer des attributs personnalisés des profils utilisateur :

- Sélectionnez le nom de l'attribut personnalisé à supprimer dans une [étape de mise à jour utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update#removing-custom-attributes).
- Définissez la valeur `null` dans votre requête API vers l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

#### Définir la valeur `null` {#setting-the-null-value}

{% alert important %}
Définir un attribut à `null` et le définir à `""` (chaîne vide) ne revient pas au même.
{% endalert %}

- `null` supprime entièrement l'attribut du profil utilisateur. Il n'apparaît plus dans le profil et ne correspond à aucun filtre **IS NOT BLANK**.
- `""` définit l'attribut comme une chaîne vide. L'attribut apparaît dans le profil avec une valeur de chaîne vide, mais ne correspond pas aux filtres **IS NOT BLANK** (il est considéré comme vide).

De plus, `""` n'est valide que pour les attributs de type chaîne de caractères. Si le type de données de l'attribut est défini sur un type autre que chaîne (comme valeur booléenne, nombre ou heure) dans le tableau de bord, l'envoi de `""` n'efface pas la valeur — utilisez `null` à la place.

### Exporter des données {#exporting-data}

Pour exporter la liste des attributs personnalisés sous forme de fichier CSV, sélectionnez **Export all** en haut de la page. Le système génère un fichier CSV et vous envoie un lien de téléchargement par e-mail.

## Consulter les rapports d'utilisation {#viewing-usage-reports}

Le rapport d'utilisation répertorie tous les Canvas, Campaigns et Segments qui utilisent un attribut personnalisé spécifique. Cette liste n'inclut pas les utilisations de Liquid.

Vous pouvez consulter jusqu'à 100 rapports d'utilisation à la fois en cochant les cases correspondant aux attributs personnalisés souhaités, puis en sélectionnant **View usage report**.

### Onglet Values {#values-tab}

Lorsque vous consultez un rapport d'utilisation, sélectionnez l'onglet **Values** pour afficher les principales valeurs des attributs personnalisés sélectionnés, basées sur un échantillon d'environ 250 000 utilisateurs. Comme les résultats sont échantillonnés à partir d'un sous-ensemble d'utilisateurs, l'échantillon n'inclut pas toutes les valeurs existantes. L'onglet **Values** ne doit donc pas être utilisé pour la résolution des problèmes ni pour des cas d'usage nécessitant l'intégration des données de tous les utilisateurs.

![Rapport d'utilisation pour les attributs personnalisés sélectionnés avec un onglet « Values » ouvert montrant un graphique circulaire des valeurs d'attribut de pays, telles que « US » et « PR ».]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## Définir des attributs personnalisés {#setting-custom-attributes}

Voici les méthodes utilisées sur les différentes plateformes pour définir des attributs personnalisés.

{% details Développer pour la documentation par plateforme %}

- [Android et FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=unity)
- [.NET MAUI (anciennement Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)

{% enddetails %}

## Stockage des attributs personnalisés {#custom-attribute-storage}

Toutes les données stockées dans le **profil utilisateur**, y compris les données d'attributs personnalisés, sont conservées indéfiniment tant que chaque profil est [actif]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#active-users).

## Types de données des attributs personnalisés

Les attributs personnalisés sont des outils extrêmement flexibles qui permettent un ciblage précis.

Les types de données suivants peuvent être stockés en tant qu'attributs personnalisés :

- [Valeurs booléennes](#booleans)
- [Nombres](#numbers)
- [Chaînes de caractères](#strings)
- [Tableaux](#arrays)
- [Heure](#time)
- [Objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support)
- [Tableaux d'objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects)

### Valeurs booléennes (vrai/faux) {#booleans}

Les attributs booléens sont utiles pour stocker des données binaires simples sur vos utilisateurs, comme les statuts d'abonnement. Vous pouvez rechercher des utilisateurs dont une variable est explicitement définie sur vrai ou faux, ainsi que ceux pour lesquels aucun enregistrement de cet attribut n'existe encore.

Pour les attributs de type **valeur booléenne**, les options de segmentation suivantes sont disponibles.

| Options de segmentation | Filtre déroulant | Options de saisie | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si la valeur booléenne **est** soit vraie, fausse, vraie ou non définie, ou fausse ou non définie | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET** ou **FALSE OR NOT SET** | Si ce filtre spécifie `coffee_drinker`, un utilisateur correspondra à ce filtre dans les circonstances suivantes : <br> {::nomarkdown}<ul><li>Si ce filtre est <code>true</code> et que l'utilisateur a la valeur <code>coffee_drinker</code></li><li>Si ce filtre est <code>false</code> et que l'utilisateur n'a pas la valeur <code>coffee_drinker</code></li><li>Si ce filtre est <code>true or not set</code> et que l'utilisateur a la valeur <code>coffee_drinker</code> ou aucune valeur</li><li>Si ce filtre est <code>false or not set</code> et que l'utilisateur n'a pas <code>coffee_drinker</code> ou aucune valeur</li></ul>{:/} |
| Vérifier si la valeur booléenne **existe** dans le profil d'un utilisateur et n'est pas nulle | **IS NOT BLANK**  | **N/A** | Si ce filtre spécifie `coffee_drinker` et qu'un utilisateur a une valeur pour l'attribut `coffee_drinker`, l'utilisateur correspondra à ce filtre. |
| Vérifier si la valeur booléenne **n'existe pas** dans le profil d'un utilisateur ou est nulle | **IS BLANK**  | **N/A** | Si ce filtre spécifie `coffee_drinker` et qu'un utilisateur n'a pas l'attribut `coffee_drinker` ou que la valeur de `coffee_drinker` est nulle, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Booleans (true/false) #booleans" }

{% endtab %}
{% tab Nombres %}

{% alert tip %}
Les dépenses ne doivent pas être enregistrées par cette méthode. Elles doivent plutôt être enregistrées via les [événements d'achat]({{site.baseurl}}/user_guide/data/activation/events/purchase_events).
{% endalert %}

Pour les attributs de type **nombre**, les options de segmentation suivantes sont disponibles.

| Options de segmentation | Filtre déroulant | Options de saisie | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut numérique **est exactement** un **nombre**| **EXACTLY** | **NUMBER** | Si ce filtre spécifie `10` et qu'un profil utilisateur a la valeur `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **n'est pas égal à** un **nombre**| **DOES NOT EQUAL** | **NUMBER** | Si ce filtre spécifie `10` et qu'un profil utilisateur n'a pas la valeur `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **est supérieur à** un **nombre**| **MORE THAN** | **NUMBER** | Si ce filtre spécifie `10` et qu'un profil utilisateur a une valeur supérieure à `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **est inférieur à** un **nombre**| **LESS THAN** | **NUMBER** | Si ce filtre spécifie `10` et qu'un profil utilisateur a une valeur inférieure à `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **existe** dans le profil d'un utilisateur et n'est pas nul | **IS NOT BLANK** | **N/A** | Si un profil utilisateur contient l'attribut numérique spécifié, quelle que soit la valeur, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **n'existe pas** dans le profil d'un utilisateur ou est nul | **IS BLANK** | **N/A** | Si un profil utilisateur ne contient pas l'attribut numérique spécifié ou si la valeur de l'attribut est nulle, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Booleans (true/false) #booleans" }

#### Détails des attributs numériques {#number-attribute-details}

- Les filtres « Exactement 0 » et « Inférieur à » incluent les utilisateurs avec des champs NULL
  - Pour exclure les utilisateurs sans valeur pour les attributs personnalisés, vous devez inclure le filtre **is not blank**.

{% endtab %}
{% tab Chaînes de caractères %}

Les attributs de type chaîne de caractères peuvent contenir jusqu'à 255 caractères. Notez que si vous saisissez des valeurs avec des espaces entre, avant ou après les mots, Braze vérifiera également ces mêmes espaces.

Pour les attributs de type **chaîne de caractères**, les options de segmentation suivantes sont disponibles.

| Options de segmentation | Filtre déroulant | Options de saisie | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut de chaîne **correspond partiellement** à une chaîne saisie **OU** à une expression régulière | **MATCHES REGEX** | **STRING** **OU** **REGULAR EXPRESSION** <br>Non sensible à la casse ; maximum de 32 764 caractères |
| Vérifier si l'attribut de chaîne **ne correspond pas partiellement** à une chaîne saisie **OU** à une expression régulière | **DOES NOT MATCH REGEX** * | **STRING** **OU** **REGULAR EXPRESSION**<br>Non sensible à la casse ; maximum de 32 764 caractères |
| Vérifier si l'attribut de chaîne **existe** dans le profil d'un utilisateur et n'est pas une chaîne vide | **IS NOT BLANK** | **N/A** | Si ce filtre spécifie `favorite_genre` et qu'un profil utilisateur possède l'attribut `favorite_genre`, l'utilisateur correspondra à ce filtre quelle que soit la valeur de l'attribut. Par exemple, l'utilisateur peut avoir `sci-fi`, `romance` ou toute autre valeur.|
| Vérifier si l'attribut de chaîne **n'existe pas** dans le profil d'un utilisateur | **BLANK** | **N/A** | Si ce filtre spécifie `favorite_genre` et qu'un profil utilisateur ne possède pas l'attribut `favorite_genre`, l'utilisateur correspondra à ce filtre.|
| Vérifier si la chaîne correspond exactement à **l'une** des chaînes saisies | **IS ANY OF** | **STRING**<br>Sensible à la casse ; plusieurs chaînes autorisées (256 maximum) | Si ce filtre spécifie `book`, `bookmark` et `reading light`, et qu'un profil utilisateur contient au moins l'une de ces chaînes, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut de chaîne **ne correspond exactement à aucune** des chaînes saisies | **IS NONE OF** |**STRING**<br>Sensible à la casse ; plusieurs chaînes autorisées (256 maximum) | Si ce filtre spécifie `book`, `bookmark` et `reading light`, et qu'un profil utilisateur ne contient aucune de ces chaînes, l'utilisateur correspondra au filtre.|
| Vérifier si l'attribut de chaîne **correspond partiellement à l'une** des chaînes saisies | **CONTAINS ANY OF** | **STRING**<br>Sensible à la casse ; plusieurs chaînes autorisées (256 maximum) | Si ce filtre spécifie `gold` et qu'un profil utilisateur contient `gold` dans n'importe quelle chaîne, comme `gold_tier` ou `former_gold_tier`, l'utilisateur correspondra au filtre. |
| Vérifier si l'attribut de chaîne **ne correspond partiellement à aucune** des chaînes saisies | **DOESN'T CONTAIN ANY OF** | **STRING**<br>Sensible à la casse ; plusieurs chaînes autorisées (256 maximum) | Si ce filtre spécifie `gold` et qu'un profil utilisateur ne contient `gold` dans aucune chaîne, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

{% multi_lang_include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

{% alert important %}
Lors de la segmentation avec le filtre **DOES NOT MATCH REGEX**, vous devez déjà avoir un attribut personnalisé avec une valeur assignée dans ce profil utilisateur. Braze recommande d'utiliser la logique « OR » pour vérifier si un attribut personnalisé est vide afin de s'assurer que les utilisateurs sont correctement ciblés.
{% endalert %}

{% endtab %}
{% tab Tableaux %}

Les tableaux ont une taille maximale de 100&nbsp;Ko. La longueur par défaut d'un attribut est de 500 éléments maximum (par exemple, si vous envoyez un attribut tel que « Films regardés » défini à 500, lorsqu'un utilisateur regarde un 501e film, le premier film est supprimé et le plus récent est ajouté). Notez que si vous saisissez des valeurs avec des espaces entre, avant ou après les mots, Braze vérifiera également ces mêmes espaces.

Les attributs personnalisés de type tableau ne peuvent pas être importés via l'[import CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import). Pour charger des valeurs de tableau, utilisez l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ou l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/cloud_ingestion).

{% alert note %}
L'option d'augmenter la longueur maximale ne sera pas disponible si l'attribut est configuré pour détecter automatiquement le type de données ; le type de données doit être défini sur tableau.
{% endalert %}

Pour les attributs de type **tableau**, les options de segmentation suivantes sont disponibles.

| Options de segmentation | Filtre déroulant | Options de saisie | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut de tableau **inclut une valeur qui correspond exactement** à une valeur saisie| **INCLUDES VALUE** | **STRING** | Si ce filtre spécifie `sci-fi` et qu'un profil utilisateur a la valeur `sci-fi`, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de tableau **n'inclut pas une valeur qui correspond exactement** à une valeur saisie| **DOESN'T INCLUDE VALUE** | **STRING** | Si ce filtre spécifie `sci-fi` et qu'un profil utilisateur n'a pas la valeur `sci-fi`, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de tableau **contient une valeur qui correspond partiellement** à une valeur saisie **OU** à une expression régulière | **MATCHES REGEX** | **STRING** **OU** **REGULAR EXPRESSION**<br>Maximum de 32 764 caractères | |
| Vérifier si l'attribut de tableau **a une valeur** ou n'est pas vide | **HAS A VALUE** | **N/A** | Si ce filtre spécifie `favorite_genres` et qu'un profil utilisateur contient `favorite_genres` avec n'importe quelle valeur, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut de tableau **est vide** ou n'existe pas | **IS EMPTY** | **N/A** | Si ce filtre spécifie `favorite_genres` et qu'un profil utilisateur ne contient pas `favorite_genres` ou contient `favorite_genres` mais sans valeurs, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de tableau **inclut une valeur qui correspond exactement à l'une** des valeurs saisies | **INCLUDES ANY OF** | **STRING**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 maximum) | Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur contient n'importe quelle combinaison de `sci-fi`, `fantasy` ou `romance`, y compris une seule d'entre elles (comme uniquement `sci-fi`). Un utilisateur peut avoir `horror` ou une autre valeur dans sa chaîne s'il possède également l'une des valeurs `sci-fi`, `fantasy` ou `romance`.|
| Vérifier si l'attribut de tableau **n'inclut pas une valeur qui correspond exactement à l'une** des valeurs saisies | **INCLUDES NONE OF** | **STRING**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 maximum) | Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur ne contient aucune combinaison de `sci-fi`, `fantasy` ou `romance`, l'utilisateur correspondra à ce filtre. L'utilisateur peut avoir `horror` ou une autre valeur s'il ne possède aucune des valeurs `sci-fi`, `fantasy` ou `romance`.|
| Vérifier si l'attribut de tableau **contient une valeur qui correspond partiellement à l'une** des valeurs saisies | **VALUES CONTAIN ANY OF** | **STRING**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 maximum) | Si ce filtre spécifie `gold` et qu'un tableau de profil utilisateur contient `gold` dans au moins une chaîne, l'utilisateur correspondra à ce filtre. Cela inclut des valeurs de chaîne comme `gold_tier`, `former_gold_tier` et d'autres.|
| Vérifier si l'attribut de tableau **ne contient pas une valeur qui correspond partiellement à l'une** des valeurs saisies | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 maximum) | Si ce filtre spécifie `gold` et qu'un tableau de profil utilisateur ne contient `gold` dans aucune chaîne, l'utilisateur correspondra à ce filtre. Cela signifie que les utilisateurs avec des valeurs de chaîne comme `gold_tier` et `former_gold_tier` ne correspondront pas à ce filtre.|
| Vérifier si l'attribut de tableau **inclut toutes** les valeurs saisies | **IS ALL OF** | **STRING**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 maximum) | Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur possède toutes ces valeurs, l'utilisateur correspondra à ce filtre. L'utilisateur peut également avoir `horror` ou d'autres valeurs et correspondre à ce filtre.|
| Vérifier si l'attribut de tableau **n'inclut pas toutes** les valeurs saisies | **ISN'T ALL OF** | **STRING**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 maximum)|  Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur ne possède pas toutes ces valeurs, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

{% alert tip %}
Pour en savoir plus sur l'utilisation des expressions régulières (regex), consultez ces ressources :

- [Expressions régulières compatibles Perl (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Regex avec Braze]({{site.baseurl}}/user_guide/audience/segments/regex)
- [Débogueur et testeur de regex](https://www.regex101.com/)
- [Tutoriel regex](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

{% endtab %}
{% tab Heure %}

Les attributs de type heure sont utiles pour stocker la dernière fois qu'une action spécifique a été effectuée, afin de proposer des messages de réengagement ciblés à vos utilisateurs.

Les filtres temporels utilisant des dates relatives (par exemple, il y a plus d'un jour, il y a moins de 2 jours) mesurent 1 jour comme 24 heures. Toute Campaign utilisant ces filtres inclura tous les utilisateurs par tranches de 24 heures. Par exemple, `last used app more than 1 day ago` capturera tous les utilisateurs qui « ont utilisé l'application pour la dernière fois il y a plus de 24 heures » à partir du moment exact où la Campaign est exécutée. Il en va de même pour les Campaigns avec des plages de dates plus longues — cinq jours à partir de l'activation signifient les 120 heures précédentes.

Pour cibler les utilisateurs dont un attribut de type heure se situe dans une plage temporelle, utilisez deux filtres d'audience : `in more than` pour la borne inférieure et `in less than` pour la borne supérieure. Un seul filtre ne peut pas exprimer les deux côtés de cette plage. Par exemple, pour cibler les utilisateurs dont un attribut de type heure se situe dans les prochaines 24 heures (entre maintenant et un jour à partir de maintenant), appliquez `in more than 0 days` et `in less than 1 day`.

{% alert warning %}
La dernière date à laquelle un événement personnalisé ou un événement d'achat s'est produit est automatiquement enregistrée et ne doit pas être enregistrée à nouveau via un attribut personnalisé de type heure.
{% endalert %}

Pour les attributs de type **heure**, les options de segmentation suivantes sont disponibles.

| Options de segmentation | Filtre déroulant | Options de saisie | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut de type heure **est avant** une **date sélectionnée**| **BEFORE** | **CALENDAR DATE SELECTOR** | Si ce filtre spécifie `2024-01-31` et qu'un profil utilisateur a une date antérieure à `2024-1-31`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut de type heure **est après** une **date sélectionnée**| **AFTER** | **CALENDAR DATE SELECTOR** | Si ce filtre spécifie `2024-01-31` et qu'un profil utilisateur a une date postérieure à `2024-1-31`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut de type heure remonte à **plus de X** **jours** | **MORE THAN** | **NUMBER OF DAYS AGO** | Si ce filtre spécifie `7` et qu'un profil utilisateur a une date remontant à plus de sept jours, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut de type heure remonte à **moins de X** **jours**| **LESS THAN** | **NUMBER OF DAYS AGO** | Si ce filtre spécifie `7` et qu'un profil utilisateur a une date remontant à moins de sept jours, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de type heure est **dans plus de X** **jours dans le futur** | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** | Si ce filtre spécifie `7` et qu'un profil utilisateur a une date dans plus de sept jours dans le futur, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de type heure est **dans moins de X** **jours dans le futur** | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE**  | Si ce filtre spécifie `7` et qu'un profil utilisateur a une date dans moins de sept jours dans le futur, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de type heure **existe** dans le profil d'un utilisateur et n'est pas nul | **IS NOT BLANK** | **N/A** | Si ce filtre spécifie un attribut de type heure présent dans un profil utilisateur, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de type heure **n'existe pas** dans le profil d'un utilisateur ou est nul | **IS BLANK** | **N/A** | Si ce filtre spécifie un attribut de type heure absent du profil utilisateur, l'utilisateur correspondra à ce filtre. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

#### Détails des attributs de type heure {#time-attribute-details}

{% multi_lang_include data_activation/day_of_recurring_event_filter.md %}

{% endtab %}
{% tab Objets %}

Vous pouvez utiliser des attributs personnalisés imbriqués pour envoyer des objets comme type de données pour les attributs personnalisés. Pour plus d'informations, consultez [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).

{% endtab %}
{% tab Tableaux d'objets %}

Utilisez un tableau d'objets pour regrouper des attributs liés. Pour plus de détails, consultez [Tableau d'objets]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects).

{% endtab %}
{% endtabs %}

Vous pouvez modifier le type de données de votre attribut personnalisé, mais vous devez être conscient des impacts. Consultez [Modifier le type de données d'un attribut personnalisé ou d'un événement](#changing-custom-attribute-or-event-data-type) pour en savoir plus.

### Opérateurs consolidés {#consolidated-operators}

Nous avons consolidé la liste des opérateurs disponibles pour les filtres d'attributs, les filtres d'attributs personnalisés et les filtres d'attributs personnalisés imbriqués. Si vous avez des filtres existants utilisant ces opérateurs, ils seront automatiquement mis à jour pour utiliser les nouveaux opérateurs.

| Type de données | Ancien opérateur | Nouvel opérateur | Valeur |
| --- | --- | --- | --- |
| Chaîne de caractères | equals | is any of | Au moins 1 valeur |
| Chaîne de caractères | does not equal | is none of | Au moins 1 valeur |
| Tableau | includes value | includes any of | Au moins 1 valeur |
| Tableau | doesn't include value | includes none of | Au moins 1 valeur |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Consolidated operators #consolidated-operators" }

## Types de données des propriétés d'événement {#event-property-data-types}

Lorsque vous enregistrez un événement, vous pouvez y associer des informations supplémentaires (par exemple, le nom du produit ou le prix) sous forme de propriétés d'événement. Chaque propriété a un nom et une valeur. Les valeurs des propriétés d'événement prennent en charge les types de données du tableau [Définitions](#definitions) (le type Heure est intitulé « Datetime » dans les propriétés d'événement).

### Format attendu {#expected-format}

Les valeurs des propriétés sont envoyées sous forme d'objet : les clés sont les noms des propriétés et les valeurs sont les valeurs des propriétés. Les noms de propriétés doivent être des chaînes non vides de 255 caractères maximum, sans signe dollar (`$`) en début.

Règles spécifiques aux propriétés d'événement :

- **Heure (Datetime) :** utilisez le format [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Non pris en charge dans les tableaux.
- **Tableau :** les dates ne sont pas prises en charge dans les tableaux.
- **Objet imbriqué :** voir [Objets imbriqués]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).
- **Payload :** les objets de propriétés d'événement contenant des valeurs de tableau ou d'objet peuvent atteindre 102 400 octets (100&nbsp;Ko).

Vous pouvez modifier le type de données de votre propriété d'événement personnalisé, mais soyez conscient des impacts de la [modification des types de données](#changing-custom-attribute-or-event-data-type) après la collecte des données.

Pour le comportement complet des propriétés d'événement, les clés réservées et l'utilisation dans les déclencheurs et la personnalisation, consultez [Propriétés d'événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).

## Événements d'achat et chiffre d'affaires {#purchase-events-and-revenue}

Les données d'achat et de chiffre d'affaires sont enregistrées via les [événements d'achat]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) ou les événements eCommerce recommandés.

{% alert note %}
Les événements recommandés ont des schémas prédéfinis avec des types de données définis. Pour plus de détails, consultez [Événements eCommerce recommandés]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events).
{% endalert %}

L'enregistrement d'événements d'achat établit la valeur vie client (LTV) pour chaque profil utilisateur, et ces données sont consultables sur la page de chiffre d'affaires sous forme de séries temporelles. Vous pouvez segmenter selon le montant dépensé, la date du dernier achat, le nombre d'achats dans une fenêtre temporelle, et plus encore.

### Types de données des propriétés d'événement d'achat {#purchase-event-property-data-types}

Les valeurs des propriétés d'événement d'achat (l'objet `properties` d'un achat) prennent en charge les types de données du tableau [Définitions](#definitions), avec la même structure et les mêmes règles de nommage que les [propriétés d'événement](#expected-format).

{% include data_activation/purchase_event_property_data_types.md %}

Pour le schéma complet de l'objet d'achat et des exemples, consultez [Objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object). Pour l'enregistrement des événements d'achat, les filtres de segmentation et tous les détails, consultez [Événements d'achat]({{site.baseurl}}/user_guide/data/activation/events/purchase_events).

## Modifier le type de données d'un attribut personnalisé ou d'un événement {#changing-custom-attribute-or-event-data-type}

Pour modifier le type de données d'un attribut personnalisé ou d'un événement :

1. Accédez à **Data Settings** et sélectionnez **Custom Attributes** ou **Custom Events**.
2. Trouvez votre attribut ou événement dans la liste, puis sélectionnez <i class="fa fa-ellipsis-v" aria-label="Plus d'actions"></i> **More actions**.
3. Sélectionnez un nouveau **Data type** dans le menu déroulant.
4. Sélectionnez **Save**.

Si vous modifiez le type de données d'un attribut personnalisé ou d'un événement (par exemple, en changeant `time` en `string`), tenez compte des points suivants :

- **Les filtres ne sont pas automatiquement mis à jour.** Les Segments, Campaigns, Canvas ou autres emplacements utilisant l'attribut ou l'événement modifié ne sont pas mis à jour. Avant de modifier le type de données, arrêtez toutes les Campaigns ou Canvas qui utilisent l'attribut dans des Segments ou des filtres, et supprimez l'attribut des filtres qui le référencent.
- **Les données utilisateur existantes ne sont pas mises à jour rétroactivement.** Si l'attribut modifié était présent dans un profil utilisateur avant le changement, cette valeur conserve l'ancien type de données. Les utilisateurs peuvent sortir des Segments contenant l'attribut modifié car le filtre recherche le nouveau type de données. Mettez à jour ces profils utilisateur (par exemple, avec l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)) pour qu'ils correspondent au nouveau type et réintègrent le Segment si nécessaire.
- **Les nouvelles données doivent correspondre au nouveau type.** Les appels API envoyant l'ancien type de données pour l'attribut modifié ne sont pas acceptés. Envoyez le nouveau type de données.

{% alert important %}
La possibilité d'empêcher la détection automatique de mettre à jour le type de données d'un attribut personnalisé est actuellement en accès anticipé. Contactez votre gestionnaire de la satisfaction client si vous souhaitez participer.
{% endalert %}

## Types de données des catalogues {#catalog-data-types}

Les catalogues prennent en charge les types répertoriés dans le tableau [Définitions](#definitions). Le tableau suivant détaille chaque type, comment il peut être créé ou mis à jour, ainsi que le format et des exemples.

| Type de données | Description | Disponible via import CSV | Disponible via API et CDI |
| --- | --- | --- | --- |
| Chaîne de caractères | Une séquence de caractères (par exemple, noms, descriptions, ID). | ✅ Oui | ✅ Oui |
| Nombre | Une valeur numérique, entière ou décimale (par exemple, prix, quantités, notes). | ✅ Oui | ✅ Oui |
| Valeur booléenne | Une valeur `true` ou `false`. | ✅ Oui | ✅ Oui |
| Heure | Date et heure au format [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) ou horodatage Unix en secondes. | ✅ Oui | ✅ Oui |
| Objet JSON (Objet) | Objet imbriqué avec des paires clé-valeur. Affiché dans la plateforme mais ne peut être créé ou mis à jour que via l'API ou CDI. | ❌ Non | ✅ Oui |
| Tableau de chaînes (Tableau) | Une liste de chaînes de caractères. Affiché dans la plateforme mais ne peut être créé ou mis à jour que via l'API ou CDI. Maximum de 100 éléments. | ❌ Non | ✅ Oui |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Types de données des catalogues #catalog-data-types" }

### Format et exemples {#format-and-examples}

| Type de données | Format | Exemple |
| --- | --- | --- |
| Chaîne de caractères | Texte | <code>"Hello World"</code> |
| Heure | ISO 8601 ou horodatage Unix (secondes) | <code>"2024-03-15T14:30:00Z"</code> |
| Valeur booléenne | <code>true</code> ou <code>false</code> | <code>true</code> |
| Nombre | Entier ou décimal | <code>42</code> ou <code>19.99</code> |
| Objet | Objet JSON | <code>{"key": "value", "price": 10}</code> |
| Tableau | Tableau de chaînes de caractères | <code>["red", "blue", "green"]</code> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Format et exemples" }

Pour la création et la mise à jour des catalogues, consultez [Créer un catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/create).