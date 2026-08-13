---
article_title: Attributs personnalisés
permalink: "/custom_attributes_entitlements/"
hidden: true
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/unlisted_docs/img/logos/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Attributs personnalisés {#braze-learning-course-image_buster-assetsunlisted_docsimglogosbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-attributes}

> Cette page couvre les attributs personnalisés, qui sont un ensemble de caractéristiques uniques de vos utilisateurs. Les attributs personnalisés sont idéaux pour stocker des informations sur vos utilisateurs ou des données relatives à des actions de faible valeur au sein de votre application.

Lorsqu'ils sont stockés dans Braze, les attributs personnalisés peuvent être utilisés pour créer des segments d'audience et personnaliser les messages à l'aide de Liquid. Gardez à l'esprit que nous ne stockons pas d'informations en séries temporelles pour les attributs personnalisés, vous ne pouvez donc pas obtenir de graphiques basés sur ceux-ci comme vous le pouvez pour les événements personnalisés.

## Droits {#entitlements}

Les droits déterminent la capacité de vos attributs personnalisés, qui suit le nombre de noms d'attributs différents que vous définissez. Vous pouvez avoir jusqu'à 1 000 attributs personnalisés par espace de travail. Si vous devez augmenter votre capacité, contactez votre gestionnaire de compte Braze pour plus d'informations.

Lorsque votre espace de travail approche du nombre maximum d'attributs personnalisés, vous recevrez des notifications dans le tableau de bord et par e-mail pour vous aider à rester informé.

Même après avoir atteint la capacité maximale, les attributs personnalisés existants peuvent toujours être reçus. Cependant, vous ne pourrez pas créer de nouveaux attributs personnalisés. Toute donnée reçue pour des attributs personnalisés qui n'existent pas encore ne sera pas traitée.

## Gérer les attributs personnalisés {#managing-custom-attributes}

Pour créer et gérer des attributs personnalisés dans le tableau de bord, accédez à **Paramètres des données** > **Attributs personnalisés**.

![Quatre attributs personnalisés de type booléen.]({% image_buster /assets/unlisted_docs/img/custom_attributes_entitlements/export_custom_attributes.png %})

La colonne **Dernière mise à jour** indique la dernière fois que l'attribut personnalisé a été modifié, par exemple quand il a été mis en liste de blocage ou activé pour la dernière fois.

{% alert important %}
Pour un ciblage correct des messages, assurez-vous que le type de données de votre attribut personnalisé correspond à l'attribut personnalisé réel.
{% endalert %}

Depuis cette page, vous pouvez afficher, gérer, créer ou mettre en liste de blocage des attributs personnalisés existants. Sélectionnez le menu à côté d'un attribut personnalisé pour les actions suivantes :

### Mise en liste de blocage {#blocklisting}

Les attributs personnalisés peuvent être mis en liste de blocage individuellement via le menu d'actions, ou jusqu'à 100 attributs peuvent être sélectionnés et mis en liste de blocage en masse. Si vous bloquez un attribut personnalisé, aucune donnée ne sera collectée concernant cet attribut, les données existantes seront indisponibles sauf si elles sont réactivées, et les attributs bloqués n'apparaîtront pas dans les filtres ou les graphiques. De plus, si l'attribut est actuellement référencé par des filtres ou des déclencheurs dans d'autres zones du tableau de bord de Braze, une fenêtre modale d'avertissement apparaîtra pour expliquer que toutes les instances des filtres ou déclencheurs qui le référencent seront supprimées et archivées.

### Marquer comme donnée d'identification personnelle (PII) {#marking-as-personally-identifiable-information-pii}

Les administrateurs peuvent également créer des attributs personnalisés et les marquer comme PII depuis cette page. Ces attributs ne seront visibles que par les administrateurs et les utilisateurs du tableau de bord disposant de l'autorisation « Afficher les attributs personnalisés marqués comme PII ».

### Ajouter des descriptions {#adding-descriptions}

Vous pouvez ajouter une description à un attribut personnalisé après sa création si vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions) `Manage Events, Attributes, Purchases`. Modifiez l'attribut personnalisé et saisissez ce que vous souhaitez, comme une note pour votre équipe.

### Ajouter des tags {#adding-tags}

Vous pouvez ajouter des tags à un attribut personnalisé après sa création si vous disposez de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions) « Manage Events, Attributes, Purchases ». Les tags peuvent ensuite être utilisés pour filtrer la liste des attributs.

### Supprimer des attributs personnalisés {#removing-custom-attributes}

Il existe deux façons de supprimer des attributs personnalisés des profils utilisateur :

* Sélectionnez le nom de l'attribut personnalisé à supprimer dans une [étape Mise à jour utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update#removing-custom-attributes).
* Définissez la valeur `null` dans votre requête API vers l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

### Afficher les rapports d'utilisation {#viewing-usage-reports}

Le rapport d'utilisation répertorie tous les Canvas, Campaigns et Segments utilisant un attribut personnalisé spécifique. Cette liste n'inclut pas les utilisations de Liquid.

Vous pouvez afficher jusqu'à 100 rapports d'utilisation à la fois en cochant les cases à côté des attributs personnalisés concernés, puis en sélectionnant **Afficher le rapport d'utilisation**.

### Exporter des données {#exporting-data}

Pour exporter la liste des attributs personnalisés sous forme de fichier CSV, sélectionnez **Tout exporter** en haut de la page. Le fichier CSV sera généré et un lien de téléchargement vous sera envoyé par e-mail.

## Définir des attributs personnalisés {#setting-custom-attributes}

La liste suivante présente les méthodes utilisées sur différentes plateformes pour définir des attributs personnalisés.

{% details Développer pour la documentation par plateforme %}

- [Android et FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)

{% enddetails %}

## Stockage des attributs personnalisés {#custom-attribute-storage}

Toutes les données stockées dans le **profil utilisateur**, y compris les données d'attributs personnalisés, sont conservées indéfiniment tant que chaque profil est [actif]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#active-users).

## Types de données des attributs personnalisés {#custom-attribute-data-types}

Les attributs personnalisés sont des outils extrêmement flexibles qui permettent un ciblage précis.

Les types de données suivants peuvent être stockés en tant qu'attributs personnalisés :

- [Booléens](#booleans)
- [Nombres](#numbers)
- [Chaînes de caractères](#strings)
- [Tableaux](#arrays)
- [Horodatage](#time)
- [Objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support)
- [Tableaux d'objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects)

### Booléens (vrai/faux) {#booleans}

Les attributs booléens sont utiles pour stocker des données binaires simples sur vos utilisateurs, comme les statuts d'abonnement. Vous pouvez trouver des utilisateurs dont une variable est explicitement définie sur vrai ou faux, en plus de ceux qui n'ont aucun enregistrement de cet attribut.

| Options de segmentation | Filtre déroulant | Options de saisie | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si la valeur booléenne **est** soit vraie, fausse, vraie ou non définie, ou fausse ou non définie | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET** ou **FALSE OR NOT SET** | Si ce filtre spécifie `coffee_drinker`, un utilisateur correspondra à ce filtre dans les circonstances suivantes : <br> {::nomarkdown}<ul><li>Si ce filtre est <code>true</code> et que l'utilisateur a la valeur <code>coffee_drinker</code></li><li>Si ce filtre est <code>false</code> et que l'utilisateur n'a pas la valeur <code>coffee_drinker</code></li><li>Si ce filtre est <code>true or not set</code> et que l'utilisateur a la valeur <code>coffee_drinker</code> ou aucune valeur</li><li>Si ce filtre est <code>false or not set</code> et que l'utilisateur n'a pas <code>coffee_drinker</code> ou aucune valeur</li></ul>{:/} |
| Vérifier si la valeur booléenne **existe** dans le profil d'un utilisateur et n'est pas nulle | **IS NOT BLANK**  | **N/A** | Si ce filtre spécifie `coffee_drinker` et qu'un utilisateur a une valeur pour l'attribut `coffee_drinker`, l'utilisateur correspondra à ce filtre. |
| Vérifier si la valeur booléenne **n'existe pas** dans le profil d'un utilisateur ou est nulle | **IS BLANK**  | **N/A** | Si ce filtre spécifie `coffee_drinker` et qu'un utilisateur n'a pas l'attribut `coffee_drinker` ou que la valeur de `coffee_drinker` est nulle, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Nombres {#numbers}

Les attributs numériques incluent les [entiers](https://en.wikipedia.org/wiki/Integer) et les [nombres à virgule flottante](https://en.wikipedia.org/wiki/Floating-point_arithmetic), et ont une grande variété de cas d'utilisation. Les attributs personnalisés numériques incrémentaux sont utiles pour stocker le nombre de fois qu'une action ou un événement donné s'est produit sans compter dans votre quota de données. Les nombres standard ont toutes sortes d'utilisations, comme l'enregistrement de :

- Pointure de chaussure
- Tour de taille
- Nombre de fois qu'un utilisateur a consulté une fonctionnalité ou catégorie de produit donnée

{% alert tip %}
Les dépenses ne doivent pas être enregistrées par cette méthode. Elles doivent plutôt être enregistrées via nos [méthodes d'achat](#purchase-revenue-tracking).
{% endalert %}

| Options de segmentation | Filtre déroulant | Options de saisie | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut numérique **est exactement** un **nombre** | **EXACTLY** | **NUMBER** | Si ce filtre spécifie `10` et qu'un profil utilisateur a la valeur `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **n'est pas égal à** un **nombre** | **DOES NOT EQUAL** | **NUMBER** | Si ce filtre spécifie `10` et qu'un profil utilisateur n'a pas la valeur `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **est supérieur à** un **nombre** | **MORE THAN** | **NUMBER** | Si ce filtre spécifie `10` et qu'un profil utilisateur a une valeur supérieure à `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **est inférieur à** un **nombre** | **LESS THAN** | **NUMBER** | Si ce filtre spécifie `10` et qu'un profil utilisateur a une valeur inférieure à `10`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **existe** dans le profil d'un utilisateur et n'est pas nul | **IS NOT BLANK** | **N/A** | Si un profil utilisateur contient l'attribut numérique spécifié, quelle que soit la valeur, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut numérique **n'existe pas** dans le profil d'un utilisateur ou est nul | **IS BLANK** | **N/A** | Si un profil utilisateur ne contient pas l'attribut numérique spécifié ou si la valeur de l'attribut est nulle, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Détails des attributs numériques {#number-attribute-details}

- Les filtres « Exactement 0 » et « Inférieur à » incluent les utilisateurs avec des champs NULL
  - Pour exclure les utilisateurs sans valeur pour les attributs personnalisés, vous devez inclure le filtre **is not blank**.

### Chaînes de caractères (caractères alphanumériques) {#strings}

Les attributs de type chaîne de caractères sont utiles pour stocker les saisies utilisateur, comme une marque préférée, un numéro de téléphone ou une dernière chaîne de recherche dans votre application. Les attributs de type chaîne de caractères peuvent contenir jusqu'à 255 caractères.

Notez que si vous saisissez des valeurs avec des espaces entre, avant ou après les mots, Braze vérifiera également ces mêmes espaces.

| Options de segmentation | Filtre déroulant | Options de saisie | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut de type chaîne **correspond exactement** à une chaîne saisie | **EQUALS** | **STRING**<br>Sensible à la casse | Si ce filtre spécifie `book` et qu'un profil utilisateur a un attribut de type chaîne pour `last_item_purchased` contenant `book`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut de type chaîne **correspond partiellement** à une chaîne saisie **OU** à une expression régulière | **MATCHES REGEX** | **STRING** **OU** **EXPRESSION RÉGULIÈRE** <br>Non sensible à la casse ; maximum de 32 764 caractères |
| Vérifier si l'attribut de type chaîne **ne correspond pas partiellement** à une chaîne saisie **OU** à une expression régulière | **DOES NOT MATCH REGEX** * | **STRING** **OU** **EXPRESSION RÉGULIÈRE**<br>Non sensible à la casse ; maximum de 32 764 caractères |
| Vérifier si l'attribut de type chaîne **ne correspond pas** à une chaîne saisie | **DOES NOT EQUAL** | **STRING**<br>Non sensible à la casse  | Si ce filtre spécifie `book` et qu'un profil utilisateur a un attribut de type chaîne pour `last_item_purchased` qui ne contient pas `book`, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de type chaîne **existe** dans le profil d'un utilisateur et n'est pas une chaîne vide | **IS NOT BLANK** | **N/A** | Si ce filtre spécifie `favorite_genre` et qu'un profil utilisateur possède l'attribut `favorite_genre`, l'utilisateur correspondra à ce filtre quelle que soit la valeur de l'attribut. Par exemple, l'utilisateur peut avoir `sci-fi`, `romance` ou une autre valeur.|
| Vérifier si l'attribut de type chaîne **n'existe pas** dans le profil d'un utilisateur | **BLANK** | **N/A** | Si ce filtre spécifie `favorite_genre` et qu'un profil utilisateur ne possède pas l'attribut `favorite_genre`, l'utilisateur correspondra à ce filtre.|
| Vérifier si la chaîne correspond exactement à **l'une** des chaînes saisies | **IS ANY OF** | **STRING**<br>Sensible à la casse ; plusieurs chaînes autorisées (256 maximum) | Si ce filtre spécifie `book`, `bookmark` et `reading light`, et qu'un profil utilisateur contient au moins l'une de ces chaînes, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut de type chaîne **ne correspond exactement à aucune** des chaînes saisies | **IS NONE OF** |**STRING**<br>Sensible à la casse ; plusieurs chaînes autorisées (256 maximum) | Si ce filtre spécifie `book`, `bookmark` et `reading light`, et qu'un profil utilisateur ne contient aucune de ces chaînes, l'utilisateur correspondra au filtre.|
| Vérifier si l'attribut de type chaîne **correspond partiellement à l'une** des chaînes saisies | **CONTAINS ANY OF** | **STRING**<br>Sensible à la casse ; plusieurs chaînes autorisées (256 maximum) | Si ce filtre spécifie `gold` et qu'un profil utilisateur contient `gold` dans n'importe quelle chaîne, comme `gold_tier` ou `former_gold_tier`, l'utilisateur correspondra au filtre. |
| Vérifier si l'attribut de type chaîne **ne correspond partiellement à aucune** des chaînes saisies | **DOESN'T CONTAIN ANY OF** | **STRING**<br>Sensible à la casse ; plusieurs chaînes autorisées (256 maximum) | Si ce filtre spécifie `gold` et qu'un profil utilisateur ne contient pas `gold` dans aucune chaîne, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Une chaîne de date telle que « 12-1-2021 » ou « 12/1/2021 » sera convertie en objet datetime et traitée comme un [attribut de type horodatage]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#time).
{% endalert %}

{% alert important %}
Lors de la segmentation avec le filtre **DOES NOT MATCH REGEX**, vous devez déjà avoir un attribut personnalisé avec une valeur assignée dans ce profil utilisateur. Braze suggère d'utiliser la logique « OU » pour vérifier si un attribut personnalisé est vide afin de s'assurer que les utilisateurs sont correctement ciblés.
{% endalert %}

### Tableaux {#arrays}

Les attributs de type tableau sont adaptés pour stocker des listes d'informations liées à vos utilisateurs. Par exemple, stocker les 100 derniers contenus consultés par un utilisateur dans un tableau permettrait une segmentation par centres d'intérêt spécifiques.

Par défaut, la longueur maximale d'un tableau pour un attribut est fixée à 25 et peut être augmentée jusqu'à 100 pour un tableau individuel. Par exemple, si vous envoyez un attribut tel que « Films regardés » et qu'il est défini à 100, lorsqu'un utilisateur regarde un 101e film, le premier film sera supprimé du tableau et le film le plus récent sera ajouté.

Si vous souhaitez augmenter ce maximum, contactez votre gestionnaire du succès des clients. Votre administrateur de tableau de bord peut ensuite augmenter la longueur maximale des tableaux individuels au-delà de 100 depuis l'onglet **Attributs personnalisés** de la page **Gérer les paramètres**.

Notez que si vous saisissez des valeurs avec des espaces entre, avant ou après les mots, Braze vérifiera également ces mêmes espaces.

{% alert note %}
L'option d'augmenter la longueur maximale ne sera pas disponible si l'attribut est configuré pour détecter automatiquement le type de données ; le type de données doit être défini sur tableau.
{% endalert %}

| Options de segmentation | Filtre déroulant | Options de saisie | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut de type tableau **inclut une valeur qui correspond exactement** à une valeur saisie | **INCLUDES VALUE** | **STRING** | Si ce filtre spécifie `sci-fi` et qu'un profil utilisateur a la valeur `sci-fi`, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de type tableau **n'inclut pas une valeur qui correspond exactement** à une valeur saisie | **DOESN'T INCLUDE VALUE** | **STRING** | Si ce filtre spécifie `sci-fi` et qu'un profil utilisateur n'a pas la valeur `sci-fi`, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de type tableau **contient une valeur qui correspond partiellement** à une valeur saisie **OU** à une expression régulière | **MATCHES REGEX** | **STRING** **OU** **EXPRESSION RÉGULIÈRE**<br>Maximum de 32 764 caractères | |
| Vérifier si l'attribut de type tableau **a une valeur** ou n'est pas vide | **HAS A VALUE** | **N/A** | Si ce filtre spécifie `favorite_genres` et qu'un profil utilisateur contient `favorite_genres` avec n'importe quelle valeur, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut de type tableau **est vide** ou n'existe pas | **IS EMPTY** | **N/A** | Si ce filtre spécifie `favorite_genres` et qu'un profil utilisateur ne contient pas `favorite_genres` ou contient `favorite_genres` mais sans valeurs, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de type tableau **inclut une valeur qui correspond exactement à l'une** des valeurs saisies | **INCLUDES ANY OF** | **STRING**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 maximum) | Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur a n'importe quelle combinaison de `sci-fi`, `fantasy` ou `romance`, y compris une seule d'entre elles (comme uniquement `sci-fi`). Un utilisateur peut avoir `horror` ou une autre valeur dans sa chaîne s'il a également l'une des valeurs `sci-fi`, `fantasy` ou `romance`.|
| Vérifier si l'attribut de type tableau **n'inclut pas une valeur qui correspond exactement à l'une** des valeurs saisies | **INCLUDES NONE OF** | **STRING**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 maximum) | Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur n'a aucune combinaison de `sci-fi`, `fantasy` ou `romance`, l'utilisateur correspondra à ce filtre. L'utilisateur peut avoir `horror` ou une autre valeur s'il n'a aucune des valeurs `sci-fi`, `fantasy` ou `romance`.|
| Vérifier si l'attribut de type tableau **contient une valeur qui correspond partiellement à l'une** des valeurs saisies | **VALUES CONTAIN ANY OF** | **STRING**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 maximum) | Si ce filtre spécifie `gold` et qu'un tableau de profil utilisateur contient `gold` dans au moins une chaîne, l'utilisateur correspondra à ce filtre. Cela inclut des valeurs de chaîne comme `gold_tier`, `former_gold_tier` et d'autres.|
| Vérifier si l'attribut de type tableau **ne contient pas une valeur qui correspond partiellement à l'une** des valeurs saisies | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 maximum) | Si ce filtre spécifie `gold` et qu'un tableau de profil utilisateur ne contient pas `gold` dans aucune chaîne, l'utilisateur correspondra à ce filtre. Cela signifie que les utilisateurs avec des valeurs de chaîne comme `gold_tier` et `former_gold_tier` ne correspondront pas à ce filtre.|
| Vérifier si l'attribut de type tableau **inclut toutes** les valeurs saisies | **IS ALL OF** | **STRING**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 maximum) | Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur a toutes ces valeurs, l'utilisateur correspondra à ce filtre. L'utilisateur peut également avoir `horror` ou d'autres valeurs et correspondre à ce filtre.|
| Vérifier si l'attribut de type tableau **n'inclut pas toutes** les valeurs saisies | **ISN'T ALL OF** | **STRING**<br>Sensible à la casse ; plusieurs valeurs autorisées (256 maximum) | Si ce filtre spécifie `sci-fi, fantasy, romance` et qu'un profil utilisateur n'a pas toutes ces valeurs, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Pour en savoir plus sur l'utilisation des expressions régulières (regex), consultez ces ressources :
- [Expressions régulières compatibles Perl (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Regex avec Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex)
- [Débogueur et testeur de regex](https://www.regex101.com/)
- [Tutoriel regex](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Horodatage {#time}

Les attributs de type horodatage sont utiles pour stocker la dernière fois qu'une action spécifique a été effectuée, afin de proposer des messages de réengagement ciblés à vos utilisateurs.

Les filtres temporels utilisant des dates relatives (par exemple, il y a plus d'un jour, il y a moins de 2 jours) mesurent 1 jour comme 24 heures. Toute Campaign que vous exécutez avec ces filtres inclura tous les utilisateurs par tranches de 24 heures. Par exemple, `last used app more than 1 day ago` capturera tous les utilisateurs qui « ont utilisé l'application pour la dernière fois il y a plus de 24 heures » à partir du moment exact où la Campaign est exécutée. Il en sera de même pour les Campaigns définies avec des plages de dates plus longues — cinq jours à partir de l'activation signifieront les 120 heures précédentes.

Par exemple, pour créer un segment qui cible les utilisateurs avec un attribut de type horodatage entre 24 et 48 heures dans le futur, appliquez les filtres `in more than 1 day in the future` et `in less than 2 days in the future`.

{% alert warning %}
La dernière date à laquelle un événement personnalisé ou un événement d'achat s'est produit est automatiquement enregistrée et ne doit pas être enregistrée à nouveau via un attribut personnalisé de type horodatage.
{% endalert %}

| Options de segmentation | Filtre déroulant | Options de saisie | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si l'attribut de type horodatage **est avant** une **date sélectionnée** | **BEFORE** | **SÉLECTEUR DE DATE CALENDRIER** | Si ce filtre spécifie `2024-01-31` et qu'un profil utilisateur a une date avant `2024-1-31`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut de type horodatage **est après** une **date sélectionnée** | **AFTER** | **SÉLECTEUR DE DATE CALENDRIER** | Si ce filtre spécifie `2024-01-31` et qu'un profil utilisateur a une date après `2024-1-31`, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut de type horodatage date de **plus de X** **jours** | **MORE THAN** | **NOMBRE DE JOURS** | Si ce filtre spécifie `7` et qu'un profil utilisateur a une date datant de plus de sept jours, l'utilisateur correspondra à ce filtre. |
| Vérifier si l'attribut de type horodatage date de **moins de X** **jours** | **LESS THAN** | **NOMBRE DE JOURS** | Si ce filtre spécifie `7` et qu'un profil utilisateur a une date datant de moins de sept jours, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de type horodatage est **dans plus de X** **jours dans le futur** | **IN MORE THAN** | **NOMBRE DE JOURS DANS LE FUTUR** | Si ce filtre spécifie `7` et qu'un profil utilisateur a une date dans plus de sept jours dans le futur, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de type horodatage est **dans moins de X** **jours dans le futur** | **IN LESS THAN** | **NOMBRE DE JOURS DANS LE FUTUR**  | Si ce filtre spécifie `7` et qu'un profil utilisateur a une date dans moins de sept jours dans le futur, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de type horodatage **existe** dans le profil d'un utilisateur et n'est pas nul | **IS NOT BLANK** | **N/A** | Si ce filtre spécifie un attribut de type horodatage présent dans un profil utilisateur, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'attribut de type horodatage **n'existe pas** dans le profil d'un utilisateur ou est nul | **IS BLANK** | **N/A** | Si ce filtre spécifie un attribut de type horodatage qui n'est pas dans un profil utilisateur, l'utilisateur correspondra à ce filtre. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Détails des attributs de type horodatage {#time-attribute-details}

{% multi_lang_include data_activation/day_of_recurring_event_filter.md %}

### Objets {#objects}

Vous pouvez utiliser des attributs personnalisés imbriqués pour envoyer des objets comme type de données pour les attributs personnalisés. Pour plus d'informations, consultez [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).

### Tableaux d'objets {#arrays-of-objects}

Utilisez un tableau d'objets pour regrouper des attributs liés. Pour plus de détails, consultez notre article sur les [tableaux d'objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects).

### Opérateurs consolidés {#consolidated-operators}

Nous avons consolidé la liste des opérateurs disponibles pour les filtres d'attributs, les filtres d'attributs personnalisés et les filtres d'attributs personnalisés imbriqués. Si vous avez des filtres existants utilisant ces opérateurs, ils seront automatiquement mis à jour pour utiliser les nouveaux opérateurs.

| Type de données | Ancien opérateur | Nouvel opérateur | Valeur |
| --- | --- | --- | --- |
| Chaîne de caractères | equals | is any of | Au moins 1 valeur |
| Chaîne de caractères | does not equal | is none of | Au moins 1 valeur |
| Tableau | includes value | includes any of | Au moins 1 valeur |
| Tableau | doesn't include value | includes none of | Au moins 1 valeur |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Suivi des achats et du chiffre d'affaires {#purchase-revenue-tracking}

L'utilisation de nos méthodes d'achat pour enregistrer les achats in-app établit la valeur vie client (LTV) pour chaque profil utilisateur individuel. Ces données sont consultables sur notre page de chiffre d'affaires en séries temporelles.

| Options de segmentation | Filtre déroulant | Options de saisie | Exemples |
| ---------------------| --------------- | ------------- | -------- |
| Vérifier si le montant total dépensé **est supérieur à** un **nombre** | **GREATER THAN** | **NUMBER** | Si ce filtre spécifie `500` et qu'un profil utilisateur a une valeur supérieure à `500`, l'utilisateur correspondra à ce filtre. |
| Vérifier si le montant total dépensé **est inférieur à** un **nombre** | **LESS THAN** | **NUMBER** | Si ce filtre spécifie `500` et qu'un profil utilisateur a une valeur inférieure à `500`, l'utilisateur correspondra à ce filtre.|
| Vérifier si le montant total dépensé **est exactement** un **nombre** | **EXACTLY** | **NUMBER** | Si ce filtre spécifie `500` et qu'un profil utilisateur a la valeur `500`, l'utilisateur correspondra à ce filtre. |
| Vérifier si le dernier achat a eu lieu **après la date X** | **AFTER** | **TIME** | Si ce filtre spécifie `2024/31/1` et que le dernier achat d'un utilisateur a eu lieu après `2024/31/1`, l'utilisateur correspondra à ce filtre.|
| Vérifier si le dernier achat a eu lieu **avant la date X** | **BEFORE** | **TIME** | Si ce filtre spécifie `2024/31/1` et que le dernier achat d'un utilisateur a eu lieu avant `2024/31/1`, l'utilisateur correspondra à ce filtre.|
| Vérifier si le dernier achat a eu lieu **il y a plus de X jours** | **MORE THAN** | **TIME** | Si ce filtre spécifie `7` et que le dernier achat d'un utilisateur a eu lieu il y a plus de sept jours, l'utilisateur correspondra à ce filtre.|
| Vérifier si le dernier achat a eu lieu **il y a moins de X jours** | **LESS THAN** | **TIME** |  Si ce filtre spécifie `7` et que le dernier achat d'un utilisateur a eu lieu il y a moins de sept jours, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'achat a eu lieu **plus de X (max = 50) fois** | **MORE THAN** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** |  Si ce filtre spécifie `7` fois et `21` jours, et qu'un utilisateur a effectué plus de sept achats au cours des 21 derniers jours, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'achat a eu lieu **moins de X (max = 50) fois** | **LESS THAN** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** | Si ce filtre spécifie `7` fois et `21` jours, et qu'un utilisateur a effectué moins de sept achats au cours des 21 derniers jours, l'utilisateur correspondra à ce filtre.|
| Vérifier si l'achat a eu lieu **exactement X (max = 50) fois** | **EXACTLY** | au cours des **Y derniers jours (Y = 1,3,7,14,21,30)** | Si ce filtre spécifie `7` fois et `21` jours, et qu'un utilisateur a effectué sept achats au cours des 21 derniers jours, l'utilisateur correspondra à ce filtre.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Si vous souhaitez segmenter sur le nombre de fois qu'un achat spécifique a eu lieu, vous devez également enregistrer cet achat individuellement en tant qu'[attribut personnalisé incrémental]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes#incrementingdecrementing-custom-attributes).
{% endalert %}

Vous pouvez modifier le type de données de votre attribut personnalisé, mais vous devez être conscient des impacts du [changement de type de données]({{site.baseurl}}/help/help_articles/data/change_custom_data_type).