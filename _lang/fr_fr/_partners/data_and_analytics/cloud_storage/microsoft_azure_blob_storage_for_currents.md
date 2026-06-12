---
nav_title: Microsoft Azure Blob Storage
article_title: Microsoft Azure Blob Storage
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "Cet article de référence décrit le partenariat entre Braze Currents et Microsoft Azure Blob Storage, un stockage d'objets massivement évolutif pour les données non structurées."
page_type: partner
tool: Currents
search_tag: Partner

---

# Microsoft Azure Blob Storage

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) est un stockage d'objets massivement évolutif pour les données non structurées offert par Microsoft dans le cadre de la suite de produits Azure.

{% alert important %}
Si vous changez de fournisseur de stockage en nuage, contactez votre gestionnaire de la satisfaction client Braze pour obtenir de l'aide sur la configuration et la validation de votre nouvelle intégration.
{% endalert %}

L'intégration de Braze et Microsoft Azure Blob Storage vous permet de réexporter des données vers Azure et de diffuser des données Currents. Vous pouvez ensuite utiliser un processus ETL (extraire, transformer, charger) pour transférer vos données vers d'autres emplacements.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Microsoft Azure et compte de stockage Azure | Un compte Microsoft Azure et un compte de stockage Azure sont nécessaires pour tirer parti de ce partenariat. |
| Currents | Pour exporter des données vers Currents, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. Currents n'est pas requis si vous ne configurez que l'archivage des messages. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Pour intégrer Microsoft Azure Blob Storage, vous devez disposer d'un compte de stockage et d'une chaîne de connexion permettant à Braze d'exporter des données vers Azure ou de diffuser des données Currents.

### Étape 1 : Créer un compte de stockage {#step-1-create-a-storage-account}

Dans Microsoft Azure, accédez à **Storage Accounts** dans la barre latérale et cliquez sur **+ Add** pour créer un nouveau compte de stockage. Fournissez ensuite un nom de compte de stockage. Les autres paramètres par défaut n'ont pas besoin d'être modifiés. Enfin, sélectionnez **Review + create**.

Même si vous disposez déjà d'un compte de stockage, nous vous recommandons d'en créer un nouveau spécifiquement pour vos données Braze.

![]({% image_buster /assets/img/azure-currents-step-1.png %})

### Étape 2 : Obtenir la chaîne de connexion {#step-2-get-the-connection-string}

Une fois le compte de stockage déployé, accédez au menu **Access Keys** depuis le compte de stockage et notez la chaîne de connexion.

Microsoft fournit deux clés d'accès pour maintenir les connexions en utilisant une clé tout en régénérant l'autre. Vous n'avez besoin que de la chaîne de connexion de l'une d'entre elles.

{% alert note %}
Braze utilise la chaîne de connexion de ce menu, pas la clé.
{% endalert %}

![]({% image_buster /assets/img/azure-currents-step-2.png %})

### Étape 3 : Créer un conteneur de service Blob {#step-3-create-a-blob-service-container}

Accédez au menu **Blobs** dans la section **Blob Service** de votre compte de stockage. Créez un conteneur de service Blob dans le compte de stockage que vous avez créé précédemment.

Fournissez un nom pour votre conteneur de service Blob. Les autres paramètres par défaut n'ont pas besoin d'être modifiés.

![]({% image_buster /assets/img/azure-currents-step-3.png %})

### Étape 4 : Configurer Currents {#step-4-set-up-currents}

Dans Braze, accédez à **Currents > + Create Current > Azure Blob Data Export** et fournissez le nom de votre intégration et l'adresse e-mail de contact.

Fournissez ensuite votre chaîne de connexion, le nom du conteneur et le préfixe BlobStorage (facultatif).

![La page Currents du stockage Blob Microsoft Azure dans Braze. Cette page comporte des champs pour le nom de l'intégration, l'adresse e-mail de contact, la chaîne de connexion, le nom du conteneur et le préfixe.]({% image_buster /assets/img/maz.png %})

Enfin, faites défiler la page vers le bas et sélectionnez les événements d'engagement lié aux messages ou les événements de comportement client que vous souhaitez exporter. Une fois terminé, lancez votre Current.

### Étape 5 : Configurer l'exportation de données Azure {#step-5-set-up-azure-data-export}

La configuration suivante définit les informations d'identification utilisées pour :
1. Les exportations de segments via l'API
2. Les exportations CSV (Campaign, Segment, exportation de données utilisateur Canvas via le tableau de bord)
3. Les rapports d'engagement

Dans Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** > **Microsoft Azure** et fournissez votre chaîne de connexion, le nom du conteneur de stockage Azure et le préfixe de stockage Azure.

Ensuite, assurez-vous que la case **Make this the default data export destination** est cochée afin que vos données exportées soient envoyées vers Azure. Une fois terminé, enregistrez votre intégration.

![La page d'exportation des données Microsoft Azure dans Braze. Cette page comporte des champs pour la chaîne de connexion, le nom du conteneur et le préfixe.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
Il est important de maintenir votre chaîne de connexion à jour ; si les informations d'identification de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si cela persiste pendant plus de **48 heures**, les événements du connecteur seront abandonnés et les données seront définitivement perdues.
{% endalert %}

## Comportement à l'exportation {#export-behavior}

Les utilisateurs qui ont intégré une solution de stockage de données en nuage et qui tentent d'exporter des API, des rapports de tableau de bord ou des rapports CSV constateront le comportement suivant :

- Toutes les exportations d'API ne renverront pas d'URL de téléchargement dans le corps de la réponse et devront être récupérées via le stockage de données.
- Tous les rapports de tableau de bord et les rapports CSV seront envoyés à l'adresse e-mail de l'utilisateur pour téléchargement (aucune autorisation de stockage requise) et sauvegardés sur le stockage de données.

{% alert important %}
**Exigence relative au format JSON** : pour les exportations JSON, Braze utilise le format JSONL (JSON délimité par des nouvelles lignes), où chaque ligne contient un objet JSON distinct. Ce format diffère du JSON standard, qui est un tableau ou un objet JSON unique. Chaque ligne du fichier exporté est un objet JSON valide, mais le fichier dans son ensemble n'est pas un document JSON unique valide. Lorsque vous traitez ces fichiers, analysez chaque ligne individuellement en tant qu'objet JSON distinct plutôt que d'essayer d'analyser l'ensemble du fichier en tant que document JSON unique.

Les exportations Currents utilisent le format Apache Avro (fichiers `.avro`), et non JSON. Cette exigence de format JSON s'applique aux exportations de données du tableau de bord et aux exportations d'API qui utilisent le format JSON.
{% endalert %}

## FAQ

### Braze peut-il fournir des adresses IP à ajouter à une liste d'autorisation pour Azure Blob Storage ? {#can-braze-provide-ip-addresses-to-allowlist-for-azure-blob-storage}

Braze ne publie pas de liste fixe d'adresses IP autorisées pour les exportations Currents ou les exportations du tableau de bord vers Azure Blob Storage. Braze écrit dans votre conteneur en utilisant la chaîne de connexion et le nom du conteneur que vous fournissez, et Azure contrôle l'accès réseau via les paramètres de votre compte de stockage (par exemple, les règles de pare-feu du compte de stockage ou les endpoints privés).

Si votre équipe de sécurité exige des restrictions basées sur les adresses IP, utilisez les fonctionnalités réseau d'Azure sur votre compte de stockage plutôt qu'une liste d'adresses IP fournie par Braze. Pour les étapes de configuration, consultez la [documentation de Microsoft sur la sécurisation d'Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security).