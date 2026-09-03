---
nav_title: Bloquer des données personnalisées
article_title: Bloquer des données personnalisées
page_order: 3
page_type: reference
description: "Cet article de référence explique comment bloquer et supprimer des événements personnalisés et des attributs personnalisés dans Braze."
---

# Bloquer des données personnalisées {#blocklist-custom-data}

> Utilisez le blocage pour arrêter le suivi des données personnalisées qui ne sont plus utiles. Utilisez la suppression pour retirer définitivement les événements personnalisés et les attributs personnalisés des profils utilisateur après les avoir bloqués. Pour le pré-remplissage, la gestion des propriétés et la configuration des types de données, consultez [Gérer les données personnalisées]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data).

## Mise en liste de blocage des données personnalisées {#blocklisting-custom-data}

Il peut arriver que vous identifiiez des attributs personnalisés, des événements personnalisés ou des événements d'achat qui consomment trop de points de donnée, ne sont plus utiles à votre stratégie marketing ou ont été enregistrés par erreur.

Pour empêcher l'envoi de ces données à Braze, vous pouvez mettre un objet de données personnalisé en liste de blocage pendant que votre équipe d'ingénierie travaille à le supprimer du backend de votre application ou de votre site web. La mise en liste de blocage empêche Braze d'enregistrer un objet de données personnalisé particulier à l'avenir, ce qui signifie qu'il n'apparaît pas lorsque vous recherchez un utilisateur spécifique.

### Choisir entre la mise en liste de blocage et la suppression {#choosing-blocklisting-or-deletion}

- **La mise en liste de blocage** conserve les attributs personnalisés, événements ou achats existants sur les profils utilisateur, mais Braze ne traite plus les nouvelles données pour ces objets.
- **La suppression** retire ces données des profils utilisateur. Les attributs personnalisés et événements supprimés sont déplacés dans la **Corbeille** pendant sept jours, durant lesquels vous pouvez les restaurer. Au bout de sept jours, Braze les supprime définitivement. La suppression n'empêche pas l'arrivée de nouvelles données, confirmez donc que votre SDK, votre API ou vos imports CSV n'envoient plus ces données avant de procéder à la suppression.

La mise en liste de blocage transmet les informations de blocage à l'appareil de chaque utilisateur et peut être gourmande en données. Mettre en liste de blocage un très grand nombre d'attributs, d'événements ou d'achats (par exemple, plus de 100) peut affecter les performances de l'application. Si vous ne prévoyez plus d'envoyer ces données à Braze, la suppression est souvent la meilleure approche après avoir arrêté l'envoi depuis l'intégration.

Que vous choisissiez la mise en liste de blocage ou la suppression, ces attributs personnalisés, événements et achats n'apparaissent plus sur la page **Manage Workspace** et sont retirés des filtres de Segment. Si vous supprimez des données personnalisées, Braze retire ces données au niveau utilisateur des profils conformément à [Comment fonctionne la suppression](#how-deletion-works).

Pour mettre des données personnalisées en liste de blocage, vous devez disposer des [permissions utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) indiquées dans le menu déroulant suivant pour votre espace de travail.

{% details Permissions utilisateur pour la mise en liste de blocage des données personnalisées %}

- Afficher les Campaigns
- Modifier les Campaigns
- Archiver les Campaigns
- Afficher les Canvas
- Modifier les Canvas
- Archiver les Canvas
- Afficher les règles de limite de fréquence
- Modifier les règles de limite de fréquence
- Afficher la priorisation des messages
- Modifier la priorisation des messages
- Afficher les Content Blocks
- Afficher les Feature Flags
- Modifier les Feature Flags
- Archiver les Feature Flags
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

Les données en liste de blocage ne sont pas envoyées par le SDK, et le tableau de bord de Braze ne traite pas les données en liste de blocage provenant d'autres sources (par exemple, l'API). Cependant, la mise en liste de blocage ne supprime pas les données des profils utilisateur et ne réduit pas rétroactivement le nombre de points de donnée consommés pour cet objet de données personnalisé. Les données en liste de blocage sont masquées et peuvent toujours être utilisées pour le templating Liquid.

### Mise en liste de blocage des attributs personnalisés, des événements personnalisés et des produits {#blocklisting-custom-attributes-custom-events-and-products}

{% alert important %}
Lorsqu'un événement ou un attribut est mis en liste de blocage, tout Segment, Campaign ou Canvas utilisant cet événement ou attribut est archivé.
{% endalert %}

Pour arrêter le suivi d'un attribut personnalisé, d'un événement ou d'un produit spécifique, suivez ces étapes :

1. Recherchez-le dans les pages **Custom Attributes**, **Custom Events** ou **Products**.
2. Sélectionnez l'attribut personnalisé, l'événement ou le produit. Pour les attributs personnalisés et les événements, vous pouvez en sélectionner jusqu'à 100 à mettre en liste de blocage à la fois.
3. Sélectionnez **Blocklist**.

![Plusieurs attributs personnalisés sélectionnés et mis en liste de blocage sur la page Custom Attributes.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

Vous pouvez mettre en liste de blocage jusqu'à 300 attributs personnalisés et 300 événements personnalisés. Pour empêcher la collecte de certains attributs d'appareil, consultez notre [guide SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview#blocking-data-collection).

{% alert important %}
Les attributs personnalisés ou événements personnalisés ayant le statut **Trashed** sont comptabilisés dans la limite de mise en liste de blocage jusqu'à leur suppression définitive.
{% endalert %}

Lorsqu'un événement personnalisé ou un attribut est mis en liste de blocage, les conséquences suivantes s'appliquent :

- Aucune donnée envoyée à Braze n'est traitée, et les événements et attributs en liste de blocage ne sont plus comptabilisés comme points de donnée
- Les données existantes ne sont pas disponibles sauf en cas de réactivation
- Les événements et attributs en liste de blocage n'apparaissent pas dans les filtres ni dans les graphiques
- Les références à des données en liste de blocage dans les brouillons de Canvas actifs se chargent en tant que valeurs invalides, ce qui peut provoquer des erreurs
- Tout ce qui utilise l'événement ou l'attribut en liste de blocage est archivé

Pour ce faire, Braze transmet les informations de mise en liste de blocage à chaque appareil. C'est un point important à considérer lorsque vous envisagez de mettre en liste de blocage un très grand nombre d'événements et d'attributs (des centaines de milliers ou des millions), car il s'agit d'une opération gourmande en données.

### Considérations relatives à la mise en liste de blocage {#considerations-for-blocklisting}

Mettre en liste de blocage un grand nombre d'événements et d'attributs est possible, mais déconseillé. En effet, chaque fois qu'un événement est effectué ou qu'un attribut est (potentiellement) envoyé à Braze, cet événement ou attribut doit être vérifié par rapport à l'ensemble de la liste de blocage.

Jusqu'à 300 éléments sont envoyés au SDK pour la mise en liste de blocage. Si vous mettez en liste de blocage plus de 300 éléments, ces données sont envoyées depuis le SDK. Si vous n'avez plus besoin d'utiliser l'événement ou l'attribut à l'avenir, envisagez de le retirer du code de votre application lors de votre prochaine version. Les modifications apportées à la liste de blocage peuvent prendre quelques minutes pour se propager. Vous pouvez réactiver tout événement ou attribut en liste de blocage à tout moment.

## Suppression de données personnalisées {#deleting-custom-data}

Lorsque vous créez des Campaigns et des Segments ciblés, il se peut que vous n'ayez plus besoin d'un événement personnalisé ou d'un attribut personnalisé. Par exemple, si vous avez utilisé un attribut personnalisé spécifique dans le cadre d'une Campaign ponctuelle, vous pouvez supprimer ces données après les avoir [ajoutées à la liste de blocage](#blocklisting-custom-attributes-custom-events-and-products) et supprimer ses références de votre application. Vous pouvez supprimer tout type de données (comme les chaînes de caractères, les nombres et les attributs personnalisés imbriqués).

{% alert important %}
Vous devez être un [administrateur Braze]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#admin) pour supprimer des données personnalisées.
{% endalert %}

Pour supprimer un événement personnalisé ou un attribut personnalisé, procédez comme suit :

1. Accédez à **Paramètres des données** > **Attributs personnalisés** ou **Événements personnalisés**, selon le type de données que vous souhaitez supprimer.
2. Accédez aux données personnalisées et sélectionnez <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Actions** > **Ajouter à la liste de blocage**.
3. Une fois vos données personnalisées ajoutées à la liste de blocage depuis 7 jours, sélectionnez <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Actions** > **Supprimer**.

### Fonctionnement de la suppression {#how-deletion-works}

Lorsque vous supprimez des données personnalisées, voici ce qui se passe :

- **Pour les attributs personnalisés :** supprime définitivement les données de l'attribut du profil de chaque utilisateur.
- **Pour les événements personnalisés :** supprime définitivement les métadonnées de l'événement du profil de chaque utilisateur.

Lorsqu'un attribut ou un événement est sélectionné pour la suppression, son statut passe à **Corbeille**. Pendant les sept jours suivants, il est possible de restaurer l'attribut ou l'événement. Si vous ne le restaurez pas après sept jours, les données sont définitivement supprimées. Si vous restaurez l'attribut ou l'événement, il reprend l'état « ajouté à la liste de blocage ».

La suppression n'empêche pas l'enregistrement ultérieur des objets de données personnalisées sur les profils utilisateur. Assurez-vous donc que les données personnalisées ne sont plus enregistrées avant de supprimer l'événement ou l'attribut.

### Points importants {#things-to-know}

Lors de la suppression de données personnalisées, gardez à l'esprit les points suivants :

* **La suppression est définitive.** Les données ne peuvent pas être récupérées.
* Les données sont supprimées de la plateforme Braze et des profils utilisateur.
* Vous pouvez « réutiliser » le nom de l'attribut personnalisé ou de l'événement personnalisé après la suppression. Cela signifie que si vous constatez que des données personnalisées « réapparaissent » dans Braze après la suppression, cela peut être dû à une intégration qui n'a pas été arrêtée et qui envoie des données avec le même nom de données personnalisées.
* Vous devrez peut-être ajouter à nouveau un élément à la liste de blocage si votre suppression entraîne la réapparition de données personnalisées. Le statut de la liste de blocage n'est pas conservé, car les données personnalisées sont supprimées.
* La suppression de données personnalisées ne consomme aucun [point de donnée]({{site.baseurl}}/user_guide/data/infrastructure/data_points) et ne génère pas non plus de nouveaux points de donnée à utiliser.