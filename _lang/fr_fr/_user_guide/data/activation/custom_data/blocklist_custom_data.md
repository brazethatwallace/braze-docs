---
nav_title: Bloquer des données personnalisées
article_title: Bloquer des données personnalisées
page_order: 3
page_type: reference
description: "Cet article de référence explique comment bloquer et supprimer des événements personnalisés et des attributs personnalisés dans Braze."
---

# Bloquer des données personnalisées {#blocklist-custom-data}

> Utilisez le blocage pour arrêter le suivi des données personnalisées qui ne sont plus utiles. Utilisez la suppression pour retirer définitivement les événements personnalisés et les attributs personnalisés des profils utilisateur après les avoir bloqués. Pour le pré-remplissage, la gestion des propriétés et la configuration des types de données, consultez [Gérer les données personnalisées]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data).

## Bloquer des données personnalisées {#blocklisting-custom-data}

Il peut arriver que vous identifiiez des attributs personnalisés, des événements personnalisés ou des événements d'achat qui enregistrent trop de points de donnée, ne sont plus utiles à votre stratégie marketing ou ont été enregistrés par erreur.

Pour empêcher l'envoi de ces données à Braze, vous pouvez bloquer un objet de données personnalisées pendant que votre équipe technique travaille à le supprimer du backend de votre application ou site web. Le blocage empêche un objet de données personnalisées particulier d'être enregistré par Braze à l'avenir, ce qui signifie qu'il n'apparaîtra pas lors de la recherche d'un utilisateur spécifique.

### Choisir entre blocage et suppression {#choosing-blocklisting-or-deletion}

- **Blocage** : conserve les attributs personnalisés, événements ou achats existants sur les profils utilisateur, mais Braze ne traite plus les nouvelles données pour ces objets.
- **Suppression** : retire ces données des profils utilisateur. Les attributs personnalisés et événements supprimés passent à l'état **Mis à la corbeille** pendant sept jours, durant lesquels vous pouvez les restaurer. Après sept jours, Braze les supprime définitivement. La suppression n'empêche pas l'arrivée de nouvelles données : vérifiez donc que votre SDK, votre API ou vos imports CSV n'envoient plus ces données avant de procéder à la suppression.

Le blocage transmet les informations de blocage à l'appareil de chaque utilisateur, ce qui peut être gourmand en données. Bloquer un très grand nombre d'attributs, d'événements ou d'achats (par exemple, plus de 100) peut affecter les performances de l'application. Si vous ne prévoyez plus d'envoyer ces données à Braze, la suppression est souvent la meilleure approche une fois que vous avez arrêté l'intégration qui les envoie.

Que vous choisissiez le blocage ou la suppression, ces attributs personnalisés, événements et achats n'apparaissent plus sur la page **Gérer l'espace de travail** et sont retirés des filtres de Segment. Si vous supprimez des données personnalisées, Braze retire ces données au niveau utilisateur des profils conformément à la section [Fonctionnement de la suppression](#how-deletion-works).

Pour bloquer des données personnalisées, vous devez disposer des [autorisations utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) indiquées dans le menu déroulant suivant pour votre espace de travail.

{% details Autorisations utilisateur pour le blocage de données personnalisées %}

- Afficher les campagnes
- Modifier les campagnes
- Archiver les campagnes
- Afficher les Canvas
- Modifier les Canvas
- Archiver les Canvas
- Afficher les règles de limite de fréquence
- Modifier les règles de limite de fréquence
- Afficher la priorisation des messages
- Modifier la priorisation des messages
- Afficher les Content Blocks
- Afficher les indicateurs de fonctionnalité
- Modifier les indicateurs de fonctionnalité
- Archiver les indicateurs de fonctionnalité
- Afficher les Segments
- Modifier les Segments
- Afficher les modèles IAM
- Modifier les modèles IAM
- Archiver les modèles IAM
- Afficher les modèles d'e-mail
- Modifier les modèles d'e-mail
- Archiver les modèles d'e-mail
- Afficher les modèles de webhook
- Modifier les modèles de webhook
- Afficher les modèles de lien
- Modifier les modèles de lien
- Afficher les ressources de la bibliothèque multimédia
- Modifier les ressources de la bibliothèque multimédia
- Supprimer les ressources de la bibliothèque multimédia
- Afficher les emplacements
- Modifier les emplacements
- Archiver les emplacements
- Afficher les codes de promotion
- Modifier les codes de promotion
- Exporter les codes de promotion
- Afficher les centres de préférences
- Modifier les centres de préférences
- Afficher les rapports
- Modifier les rapports

{% enddetails %}

Les données bloquées ne sont pas envoyées par le SDK, et le tableau de bord de Braze ne traite pas les données bloquées provenant d'autres sources (par exemple, l'API). Cependant, le blocage ne supprime pas les données des profils utilisateur et ne diminue pas rétroactivement le nombre de points de donnée générés par cet objet de données personnalisées. Les données bloquées sont masquées mais peuvent toujours être utilisées pour le templating Liquid.

### Bloquer des attributs personnalisés, des événements personnalisés et des produits {#blocklisting-custom-attributes-custom-events-and-products}

{% alert important %}
Lorsqu'un événement ou un attribut est bloqué, tout Segment, toute Campaign ou tout Canvas utilisant cet événement ou attribut est archivé.
{% endalert %}

Pour arrêter le suivi d'un attribut personnalisé, d'un événement ou d'un produit spécifique, suivez ces étapes :

1. Recherchez-le dans les pages **Attributs personnalisés**, **Événements personnalisés** ou **Produits**.
2. Sélectionnez l'attribut personnalisé, l'événement ou le produit. Pour les attributs personnalisés et les événements, vous pouvez en sélectionner jusqu'à 100 à bloquer en une seule fois.
3. Sélectionnez **Bloquer**.

![Plusieurs attributs personnalisés sélectionnés et bloqués sur la page Attributs personnalisés.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

Vous pouvez bloquer jusqu'à 300 attributs personnalisés et 300 événements personnalisés. Pour empêcher la collecte de certains attributs d'appareil, consultez notre [guide SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer#blocking-data-collection).

{% alert important %}
Les attributs personnalisés ou événements personnalisés ayant le statut **Mis à la corbeille** sont comptabilisés dans la limite de blocage tant qu'ils ne sont pas supprimés.
{% endalert %}

Lorsqu'un événement personnalisé ou un attribut est bloqué, les règles suivantes s'appliquent :

- Aucune donnée envoyée à Braze n'est traitée, et les événements et attributs bloqués ne comptent plus comme des points de donnée
- Les données existantes ne sont pas disponibles sauf si elles sont réactivées
- Les événements et attributs bloqués n'apparaissent pas dans les filtres ni les graphiques
- Les références aux données bloquées dans les brouillons de Canvas actifs se chargent comme des valeurs invalides, ce qui peut provoquer des erreurs
- Tout ce qui utilise l'événement ou l'attribut bloqué est archivé

Pour ce faire, Braze envoie les informations de blocage à chaque appareil. C'est un point important à considérer si vous envisagez de bloquer un très grand nombre d'événements et d'attributs (des centaines de milliers ou des millions), car il s'agit d'une opération gourmande en données.

### Considérations relatives au blocage {#considerations-for-blocklisting}

Bloquer un grand nombre d'événements et d'attributs est possible, mais déconseillé. En effet, chaque fois qu'un événement est exécuté ou qu'un attribut est (potentiellement) envoyé à Braze, cet événement ou attribut doit être vérifié par rapport à l'ensemble de la liste de blocage.

Jusqu'à 300 éléments sont envoyés au SDK pour le blocage. Si vous bloquez plus de 300 éléments, ces données sont envoyées depuis le SDK. Si vous n'avez pas besoin d'utiliser l'événement ou l'attribut à l'avenir, envisagez de le supprimer du code de votre application lors de votre prochaine mise à jour. Les modifications apportées à la liste de blocage peuvent prendre quelques minutes pour se propager. Vous pouvez réactiver tout événement ou attribut bloqué à tout moment.

## Supprimer des données personnalisées {#deleting-custom-data}

Lorsque vous créez des campagnes et des Segments ciblés, il se peut que vous n'ayez plus besoin d'un événement personnalisé ou d'un attribut personnalisé. Par exemple, si vous avez utilisé un attribut personnalisé spécifique dans le cadre d'une campagne ponctuelle, vous pouvez supprimer ces données après les avoir [bloquées](#blocklisting-custom-attributes-custom-events-and-products) et avoir retiré leurs références de votre application. Vous pouvez supprimer tous les types de données (tels que les chaînes de caractères, les nombres et les attributs personnalisés imbriqués).

{% alert important %}
Vous devez être [administrateur Braze]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#admin) pour supprimer des données personnalisées.
{% endalert %}

Pour supprimer un événement personnalisé ou un attribut personnalisé, procédez comme suit :

1. Accédez à **Paramètres des données** > **Attributs personnalisés** ou **Événements personnalisés**, selon le type de données que vous souhaitez supprimer.
2. Accédez aux données personnalisées et sélectionnez <i class="fa-solid fa-ellipsis-vertical" aria-label="Actions"></i>&nbsp;**Actions** > **Bloquer**.
3. Une fois vos données personnalisées bloquées depuis 7 jours, sélectionnez <i class="fa-solid fa-ellipsis-vertical" aria-label="Actions"></i>&nbsp;**Actions** > **Supprimer**.

### Fonctionnement de la suppression {#how-deletion-works}

Lorsque vous supprimez des données personnalisées, voici ce qui se passe :

- **Pour les attributs personnalisés :** supprime définitivement les données de l'attribut du profil de chaque utilisateur.
- **Pour les événements personnalisés :** supprime définitivement les métadonnées de l'événement du profil de chaque utilisateur.

Lorsqu'un attribut ou un événement est sélectionné pour suppression, son statut passe à **Mis à la corbeille**. Pendant les sept jours suivants, il est possible de restaurer l'attribut ou l'événement. Si vous ne le restaurez pas après sept jours, les données sont définitivement supprimées. Si vous restaurez l'attribut ou l'événement, il revient à l'état bloqué.

La suppression n'empêche pas l'enregistrement ultérieur des objets de données personnalisées sur les profils utilisateur. Assurez-vous donc que les données personnalisées ne sont plus enregistrées avant de supprimer l'événement ou l'attribut.

### Points importants {#things-to-know}

Lors de la suppression de données personnalisées, gardez à l'esprit les points suivants :

* **La suppression est définitive.** Les données ne peuvent pas être récupérées.
* Les données sont supprimées de la plateforme Braze et des profils utilisateur.
* Vous pouvez « réutiliser » le nom de l'attribut personnalisé ou de l'événement personnalisé après la suppression. Si vous constatez que des données personnalisées « réapparaissent » dans Braze après la suppression, cela peut être dû à une intégration qui n'a pas été arrêtée et qui continue d'envoyer des données avec le même nom.
* Vous devrez peut-être bloquer à nouveau un élément si votre suppression entraîne la réapparition de données personnalisées. Le statut de blocage n'est pas conservé car les données personnalisées sont supprimées.
* La suppression de données personnalisées n'enregistre aucun [point de donnée]({{site.baseurl}}/user_guide/data/infrastructure/data_points) et ne génère pas non plus de nouveaux points de donnée.