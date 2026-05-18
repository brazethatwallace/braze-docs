---
nav_title: Grouparoo
page_order: 1
description: "Cet article présente le partenariat entre Braze et Grouparoo, un outil de reverse ETL open source utilisé pour alimenter les outils de marketing, de vente et d'assistance avec les données de votre entrepôt de données."
page_type: update

---

# Grouparoo

{% alert update %}
La prise en charge de Grouparoo a été arrêtée en avril 2022.
{% endalert %}

> [Grouparoo](https://www.grouparoo.com/) est un outil de reverse ETL open source qui synchronise les données de votre entrepôt avec les outils de marketing, de vente et d'assistance. Son interface utilisateur centrée sur le modèle permet aux membres non techniques de l'équipe de configurer et de planifier les synchronisations de données.

L'intégration de Braze et Grouparoo synchronise les données de l'entrepôt avec Braze. Les planifications de synchronisation automatique permettent de maintenir les communications avec les clients à jour grâce à des informations actualisées.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte et projet Grouparoo | Un compte et un projet Grouparoo sont requis pour profiter de ce partenariat.<br><br>Cette intégration peut être utilisée avec l'édition gratuite pour la communauté et les solutions d'entreprise fournies par Grouparoo. La configuration se fait dans l'interface utilisateur de configuration de Grouparoo. |
| Clé REST API Braze | Une clé REST API Braze avec des autorisations sur les utilisateurs et le suivi. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST Braze | [L'URL de votre endpoint REST](https://www.grouparoo.com/). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Créer une application Braze dans Grouparoo {#step-1-create-a-braze-app-in-grouparoo}

Dans Grouparoo, accédez à **Apps** et sélectionnez **Braze** pour créer une nouvelle application Braze. Dans la boîte de dialogue modale qui apparaît, saisissez votre clé API Braze et votre endpoint REST.

![]({% image_buster /assets/img/grouparoo/add-app.png %})

### Étape 2 : Configurer un modèle et une source de données {#step-2-set-up-a-model-and-data-source}

Cette intégration nécessite que vous ayez configuré un modèle et une source de données avant de passer à l'étape suivante. Si ce n'est pas le cas, consultez la documentation de Grouparoo pour apprendre à configurer un [modèle](https://www.grouparoo.com/docs/config/models) et une [source de données](https://www.grouparoo.com/docs/config/sources).

### Étape 3 : Créer une destination Braze dans Grouparoo {#step-3-create-a-braze-destination-in-grouparoo}

#### Sélectionner le mode de synchronisation {#select-sync-mode}

Dans Grouparoo, sélectionnez votre modèle dans la barre de navigation. Ensuite, faites défiler jusqu'à la section **Destinations** et cliquez sur **Add new Destination**.

Sélectionnez ensuite l'application **Braze** que vous avez créée, nommez la destination et choisissez le mode de synchronisation souhaité parmi les suivants :
- **Sync** : ajoutez, mettez à jour et supprimez des utilisateurs de l'entreprise si nécessaire. Cette option recherche les nouveaux enregistrements, les modifications apportées aux enregistrements existants et les suppressions.
- **Additive** : ajoutez et mettez à jour les utilisateurs de l'entreprise si nécessaire, mais ne supprimez personne. Cette option recherche les nouveaux utilisateurs à ajouter à Braze et les modifications apportées aux utilisateurs existants de l'entreprise, mais elle ne fait pas de suivi des suppressions.
- **Enrich** : mettez à jour uniquement les utilisateurs qui existent déjà dans Braze. N'ajoutez ni ne supprimez d'utilisateurs. Cette option met uniquement à jour les utilisateurs existants dans Braze.

#### Mappage des champs de propriété {#property-field-mapping}

Vous devez ensuite mapper les champs de propriété de Grouparoo vers les champs de propriété de Braze.

![Exemple de champs de mappage de propriété. L'userID Grouparoo est configuré pour mapper vers external_id. Les champs email, firstName et lastName sont définis sur les champs Grouparoo équivalents « email », « first_name » et « last_name ».]({% image_buster /assets/img/grouparoo/mapping.png %}){: style="max-width:80%;"}

Assurez-vous que le champ Braze `external_id` est mappé sur la clé primaire de votre table source. Mappez le reste des champs selon les besoins de votre cas d'utilisation.

Section **Send Record Properties** : liste des champs de profil utilisateur prédéfinis disponibles pour le mappage de données. N'importe lequel d'entre eux peut être synchronisé à partir des propriétés de Grouparoo.

Section **Optional Braze User Profile Fields** : créez des champs de profil utilisateur Braze personnalisés facultatifs. Si vous cliquez sur **Add New Braze User Profile Field**, vous verrez toutes les propriétés disponibles que vous pouvez mapper vers Braze. Le nom de tout nouveau champ que vous créez sera identique à celui de la propriété Grouparoo, mais vous pouvez le renommer.

#### Groupes Grouparoo {#grouparoo-groups}

Outre le mappage, vous pouvez également choisir d'ajouter des groupes Grouparoo aux groupes d'abonnement Braze.

![Sous « Braze Subscription Groups » dans la fenêtre de configuration de la destination Grouparoo, le groupe Grouparoo « High value with recent automotive purchase » sera ajouté au groupe d'abonnement Braze « High value with recent automotive purchase ».]({% image_buster /assets/img/grouparoo/lists.png %}){: style="max-width:80%;"}

{% alert important %}
Vous trouverez plus de détails et de mises à jour sur cette intégration dans la [documentation de Grouparoo](https://www.grouparoo.com/docs/integrations/grouparoo-braze).
{% endalert %}