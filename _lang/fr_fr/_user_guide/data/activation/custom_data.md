---
nav_title: Données personnalisées
article_title: Données personnalisées
page_order: 0
page_type: landing
description: "Les données personnalisées alimentent votre stratégie d'engagement dans Braze. Découvrez les attributs personnalisés, les événements, les catalogues, les types de données et comment préserver l'intégrité de vos données."
---

# Données personnalisées {#custom-data}

> Les données personnalisées sont le moteur de votre stratégie d'engagement. Alors que les attributs standard comme le prénom et le pays sont intégrés par défaut, les données personnalisées vous permettent de capturer les détails uniques qui définissent votre relation avec vos clients — de leur genre de film préféré au moment exact où ils ont finalisé un achat.

En intégrant ces informations dans Braze, vous pouvez aller au-delà des messages génériques pour créer des expériences personnelles, opportunes et pertinentes. Vous pouvez utiliser ces données pour créer des segments précis, personnaliser le contenu des messages avec Liquid et déclencher des parcours automatisés basés sur le comportement en temps réel.

## Attributs et événements {#attributes-and-events}

La décision la plus importante lors de la configuration de vos données est le choix entre un attribut et un événement.

### Attributs personnalisés : qui sont vos utilisateurs {#custom-attributes-who-your-users-are}

Les attributs personnalisés représentent les caractéristiques ou propriétés persistantes de vos utilisateurs. Ils sont idéaux pour stocker des informations qui reflètent un état actuel ou qui changent rarement.

- **Cas d'utilisation :** Vous pouvez utiliser un attribut `loyalty_tier` pour distinguer vos membres « Silver » et « Gold ».
- **Personnalisation :** Les attributs sont parfaits pour la personnalisation. Vous pouvez intégrer la `favorite_category` d'un utilisateur dans la ligne d'objet d'un e-mail pour attirer son attention.
- **Stockage :** Ces données restent sur le profil utilisateur indéfiniment tant que le profil reste actif.

Pour en savoir plus, consultez [Attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/).

### Événements personnalisés : ce que font vos utilisateurs {#custom-events-what-your-users-do}

Les événements personnalisés suivent les actions spécifiques que vos utilisateurs effectuent à un instant donné. Ce sont des interactions à forte valeur ajoutée qui vous aident à comprendre le « quand » et le « à quelle fréquence » du comportement utilisateur.

- **Cas d'utilisation :** Lorsqu'un utilisateur finalise son inscription, vous pouvez enregistrer un événement `completed_registration`.
- **Déclenchement :** Les événements sont le principal moyen de déclencher une livraison par événement. Vous pouvez envoyer une notification push « Bienvenue » dès que l'événement `completed_registration` est enregistré.
- **Métadonnées :** Vous pouvez ajouter des détails supplémentaires à un événement à l'aide de propriétés d'événement, comme le nom de l'article ajouté au panier.
- **Analytique :** Les événements alimentent la segmentation, les rapports et l'analytique, ce qui vous permet de mesurer l'engagement et d'optimiser vos messages.

Pour en savoir plus, consultez [Événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events/).

## Catalogues {#catalogs}

Alors que les attributs et les événements se concentrent sur vos utilisateurs, les catalogues vous permettent d'intégrer des données non liées aux utilisateurs, comme des inventaires de produits, des détails de cours ou des listes d'événements.

En important ces métadonnées via CSV ou API, vous pouvez enrichir vos messages avec des informations qui ne sont pas stockées sur le profil utilisateur. Par exemple, vous pouvez utiliser un catalogue pour notifier automatiquement vos clients lorsqu'un article qu'ils ont consulté précédemment est de nouveau en stock ou a baissé de prix.

Pour en savoir plus, consultez [Catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/).

## Types de données {#data-types}

Braze prend en charge plusieurs types de données pour vos données personnalisées — notamment les types valeur booléenne, nombre, chaîne de caractères, tableau, date/heure et objet — chacun avec des comportements et des options de segmentation spécifiques. Le type de données que vous choisissez détermine la manière dont vous pouvez filtrer et personnaliser dans vos campagnes et segments.

Pour une référence complète des types de données pris en charge pour les attributs personnalisés, les propriétés d'événement et les catalogues, consultez [Types de données]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/).

## Préserver l'intégrité de vos données {#managing-your-data-integrity}

Braze fournit plusieurs outils pour vous aider à gérer vos données personnalisées à mesure que votre stratégie évolue.

### Détection et modification des types de données {#data-type-detection-and-changes}

Braze reconnaît automatiquement le type de données (comme un nombre ou une chaîne de caractères) de la première valeur reçue pour un attribut. Pour garantir la précision, assurez-vous que votre équipe envoie des types de données cohérents dans tous vos environnements. Si vous devez modifier un type de données, gardez à l'esprit que les données existantes sur les profils utilisateur ne seront pas mises à jour rétroactivement, ce qui peut affecter vos segments.

### Liste de blocage et suppression {#blocklist-and-delete}

Si vous constatez que certains attributs ou événements ne sont plus utiles ou ont été ajoutés par erreur, vous pouvez les supprimer de votre espace de travail.

- **Liste de blocage :** Empêche Braze de collecter de nouvelles données pour cet objet. Les données n'apparaissent plus dans les filtres ni les graphiques, mais les données existantes sont conservées sur les profils.
- **Suppression :** Supprime définitivement les données de tous les profils utilisateur. Vous devez placer un objet de données en liste de blocage pendant 7 jours avant qu'il ne devienne éligible à la suppression.

Pour en savoir plus, consultez [Gérer les données personnalisées]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/) et [Bloquer des données personnalisées]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).