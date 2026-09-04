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

L'intégration de Braze et Microsoft Azure Blob Storage vous permet de réexporter des données vers Azure et de diffuser des données Currents. Vous pouvez ensuite utiliser un processus ETL (ETL) pour transférer vos données vers d'autres emplacements.

## Prérequis {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Microsoft Azure et un compte de stockage Azure | Un compte Microsoft Azure et un compte de stockage Azure sont nécessaires pour tirer parti de ce partenariat. |
| Currents | Pour exporter des données vers Currents, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) pour votre compte. Currents n'est pas nécessaire si vous configurez uniquement l'archivage des messages. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

Pour intégrer Microsoft Azure Blob Storage, vous devez disposer d'un compte de stockage et d'un conteneur afin de permettre à Braze d'exporter des données vers Azure ou de diffuser des données Currents. Braze prend en charge deux méthodes d'authentification :

- [Méthode par chaîne de connexion](#connection-string-auth-method)
- [Méthode par principal de service avec certificat](#certificate-service-principal-auth-method) (Currents uniquement)

## Méthode d'authentification par chaîne de connexion {#connection-string-auth-method}

### Étape 1 : Créer un compte de stockage {#step-1-create-a-storage-account}

Dans Microsoft Azure, accédez à **Storage Accounts** dans la barre latérale et cliquez sur **+ Add** pour créer un nouveau compte de stockage. Ensuite, indiquez un nom de compte de stockage. Les autres paramètres par défaut n'auront pas besoin d'être modifiés. Enfin, sélectionnez **Review + create**.

Même si vous disposez déjà d'un compte de stockage, nous vous recommandons d'en créer un nouveau spécifiquement pour vos données Braze.

![La page de création de compte de stockage Microsoft Azure sur l'onglet Basics, avec le champ du nom du compte de stockage mis en évidence.]({% image_buster /assets/img/azure-currents-step-1.png %})

### Étape 2 : Obtenir la chaîne de connexion {#step-2-get-the-connection-string}

Une fois le compte de stockage déployé, accédez au menu **Access Keys** depuis le compte de stockage et notez la chaîne de connexion.

Microsoft fournit deux clés d'accès pour maintenir les connexions en utilisant une clé pendant la régénération de l'autre. Vous n'avez besoin de la chaîne de connexion que de l'une d'entre elles.

{% alert note %}
Braze utilise la chaîne de connexion de ce menu, pas la clé.
{% endalert %}

![La page des clés d'accès d'un compte de stockage Azure, avec le champ de la chaîne de connexion sous key1 mis en évidence.]({% image_buster /assets/img/azure-currents-step-2.png %})

### Étape 3 : Créer un conteneur de service blob {#step-3-create-a-blob-service-container}

Accédez au menu **Blobs** dans la section **Blob Service** de votre compte de stockage. Créez un conteneur de service blob dans le compte de stockage que vous avez créé précédemment.

Indiquez un nom pour votre conteneur de service blob. Les autres paramètres par défaut n'auront pas besoin d'être modifiés.

![La page Blobs d'un compte de stockage Azure sous Blob Service, avec l'option d'ajouter un conteneur.]({% image_buster /assets/img/azure-currents-step-3.png %})

### Étape 4 : Configurer Currents {#step-4-set-up-currents}

Dans Braze, accédez à **Currents > + Create Current > Azure Blob Data Export** et indiquez le nom de votre intégration ainsi qu'un e-mail de contact.

{% multi_lang_include currents/contact_email_notifications.md %}

Ensuite, fournissez votre chaîne de connexion, le nom du conteneur et le préfixe BlobStorage (facultatif).

![La page Currents de stockage Microsoft Azure Blob dans Braze. Cette page contient des champs pour le nom de l'intégration, l'e-mail de contact, la chaîne de connexion, le nom du conteneur et le préfixe.]({% image_buster /assets/img/maz.png %})

Enfin, faites défiler jusqu'en bas de la page et sélectionnez les événements d'engagement liés aux messages ou les événements de comportement client que vous souhaitez exporter. Une fois terminé, lancez votre Current.

### Étape 5 : Configurer l'exportation de données Azure {#step-5-set-up-azure-data-export}

Les éléments suivants configurent les identifiants utilisés pour :
1. Les exportations de Segment via l'API
2. Les exportations CSV (exportation de données utilisateur de Campaign, Segment et Canvas via le tableau de bord)
3. Les rapports d'engagement

Dans Braze, accédez à **Partner Integrations** > **Technology Partners** > **Microsoft Azure** et fournissez votre chaîne de connexion, le nom du conteneur de stockage Azure et le préfixe de stockage Azure.

Ensuite, assurez-vous que la case **Make this the default data export destination** est cochée, afin que vos données exportées soient envoyées vers Azure. Une fois terminé, enregistrez votre intégration.

![La page d'exportation de données Microsoft Azure dans Braze. Cette page contient des champs pour la chaîne de connexion, le nom du conteneur et le préfixe.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
Il est important de maintenir votre chaîne de connexion à jour. Si les identifiants de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si cette situation persiste pendant plus de 48 heures, les événements du connecteur seront supprimés et les données seront définitivement perdues.
{% endalert %}

## Méthode d'authentification par principal de service avec certificat {#certificate-service-principal-auth-method}

Cette méthode s'authentifie auprès de Microsoft Entra ID à l'aide d'un certificat, puis écrit dans votre conteneur en utilisant le contrôle d'accès basé sur les rôles Azure (RBAC) sans clé de compte partagée. Elle est disponible uniquement pour Braze Currents.

{% alert note %}
Vous ne téléchargez que le certificat public vers Microsoft Entra ID — votre clé privée n'est jamais envoyée à Azure. Braze stocke votre certificat et votre clé privée chiffrés au repos, n'accorde l'accès que via le rôle [Storage Blob Data Contributor](#cert-sp-4) que vous attribuez, et vous pouvez révoquer cet accès à tout moment en supprimant le certificat de l'inscription de votre application dans Azure.
{% endalert %}

Avant de commencer, [créez un compte de stockage](#step-1-create-a-storage-account) et un [conteneur de service blob](#step-3-create-a-blob-service-container) comme décrit dans la [méthode par chaîne de connexion](#connection-string-auth-method).

### Étape 1 : Inscrire une application {#cert-sp-1}

Dans Microsoft Azure, accédez à **Microsoft Entra ID** > **App registrations** > **+ New registration**. Fournissez un nom (par exemple, `braze-currents`), puis sélectionnez **Register**. Pour des étapes détaillées, consultez la documentation Microsoft [Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app).

Sur la page **Overview** de l'inscription de votre nouvelle application, notez les valeurs suivantes. Vous les fournirez toutes les deux à Braze à l'[étape 6](#cert-sp-6).

- **Application (client) ID**
- **Directory (tenant) ID**

### Étape 2 : Créer un certificat {#cert-sp-2}

Braze s'authentifie à l'aide d'un certificat : vous téléchargez le **certificat public** vers Azure et fournissez à Braze le **certificat accompagné de sa clé privée**.

Pour générer un certificat auto-signé et une clé privée RSA 2048 bits non chiffrée, exécutez :

```bash
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem \
  -days 730 -nodes -subj "/CN=braze-currents"
```

Cela crée deux fichiers :

| Fichier | Objectif |
| ------- | -------- |
| `cert.pem` | Votre certificat public. Téléchargez-le vers Azure à l'étape suivante. |
| `key.pem` | Votre clé privée. Ne téléchargez jamais ce fichier vers Azure. Vous le fournirez à Braze à l'[étape 6](#cert-sp-6). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fichiers de certificat" }

{% alert important %}
La clé privée doit être non chiffrée — elle ne peut pas être protégée par une phrase de passe. Ne téléchargez que le certificat public vers Azure ; ne téléchargez jamais votre clé privée.
{% endalert %}

**Vous avez déjà un certificat ?** Si vous disposez d'un certificat existant sous forme de fichier `.pfx` — par exemple, provenant d'Azure Key Vault, de votre autorité de certification ou de la [méthode PowerShell de Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-self-signed-certificate) — convertissez-le au format requis par Braze au lieu d'en générer un nouveau :

```bash
# The public certificate to upload to Azure (Step 3)
openssl pkcs12 -in your-cert.pfx -nokeys -out cert.pem

# The certificate and its unencrypted private key to give to Braze (Step 6)
openssl pkcs12 -in your-cert.pfx -nodes -out braze-currents.pem
```

Saisissez le mot de passe de votre fichier `.pfx` lorsque vous y êtes invité. L'option `-nodes` exporte la clé privée non chiffrée, comme l'exige Braze.

### Étape 3 : Télécharger le certificat {#cert-sp-3}

Dans l'inscription de votre application, accédez à **Certificates & secrets** > **Certificates** > **Upload certificate**, puis téléchargez le fichier `cert.pem` que vous avez créé à l'étape précédente. Ajoutez une description et sélectionnez **Add**. Pour des étapes détaillées, consultez la documentation Microsoft [Add and manage app credentials in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials).

Notez la date d'expiration de votre certificat. Consultez [Mise à jour des identifiants Azure pour Currents](#updating-currents-credentials).

### Étape 4 : Accorder l'accès à votre compte de stockage {#cert-sp-4}

Ensuite, accordez à l'inscription de votre application la permission d'écrire dans votre conteneur.

Accédez à votre compte de stockage et sélectionnez **Access Control (IAM)** > **+ Add** > **Add role assignment**. Puis :

1. Dans l'onglet **Role**, sélectionnez **[Storage Blob Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/storage#storage-blob-data-contributor)**.
2. Dans l'onglet **Members**, sélectionnez **User, group, or service principal**, sélectionnez **+ Select members**, puis recherchez le nom de l'inscription d'application que vous avez créée à l'[étape 1](#cert-sp-1).
3. Sélectionnez **Review + assign**.

Pour des étapes détaillées, consultez la documentation Microsoft [Assign an Azure role for access to blob data](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access).

![L'onglet des attributions de rôles du contrôle d'accès (IAM) pour un compte de stockage, montrant un principal de service et un groupe auxquels le rôle Storage Blob Data Contributor est attribué.]({% image_buster /assets/img/azure-currents-cert-sp-1.png %})

{% alert note %}
Attribuez le rôle au niveau du **compte de stockage** plutôt que sur un conteneur individuel.
{% endalert %}

{% alert important %}
Sans cette attribution de rôle, Braze peut s'authentifier auprès de Microsoft Entra ID mais ne pourra pas écrire dans votre conteneur.
{% endalert %}

### Étape 5 : Obtenir l'endpoint de votre compte {#cert-sp-5}

Depuis votre compte de stockage, accédez à **Settings** > **Endpoints** et notez l'endpoint **Blob service**. Il ressemble à `https://<your-storage-account>.blob.core.windows.net`.

![La page des endpoints du compte de stockage avec l'endpoint Blob service mis en évidence.]({% image_buster /assets/img/azure-currents-cert-sp-2.png %})

{% alert note %}
L'authentification par principal de service avec certificat ne prend en charge que le cloud public Azure. Votre endpoint blob doit se terminer par `.blob.core.windows.net`.
{% endalert %}

### Étape 6 : Configurer Currents {#cert-sp-6}

Braze a besoin d'un seul fichier PEM contenant votre certificat et sa clé privée non chiffrée. Si vous avez généré un nouveau certificat à l'[étape 2](#cert-sp-2), combinez les deux fichiers en un seul :

```bash
cat cert.pem key.pem > braze-currents.pem
```

Si vous avez converti un fichier `.pfx` existant à l'[étape 2](#cert-sp-2), vous disposez déjà de ce fichier `braze-currents.pem`.

Dans Braze, accédez à **Currents** > **+ Create Current** > **Azure Blob Data Export**, puis fournissez le nom de votre intégration et une adresse e-mail de contact.

{% multi_lang_include currents/contact_email_notifications.md %}

Pour **Credentials**, sélectionnez **Certificate Service Principal** et fournissez les informations suivantes :

| Champ | Valeur |
| ----- | ------ |
| Tenant ID | Le **Directory (tenant) ID** de l'[étape 1](#cert-sp-1). |
| Client ID | L'**Application (client) ID** de l'[étape 1](#cert-sp-1). |
| Account Endpoint | L'endpoint **Blob service** de l'[étape 5](#cert-sp-5). |
| Certificate | Le fichier `braze-currents.pem` contenant votre certificat et sa clé privée non chiffrée. |
| Container Name | Le nom de votre conteneur blob. |
| Prefix | Facultatif. Un préfixe de chemin pour vos données exportées dans le conteneur. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Champs du principal de service avec certificat" }

![La page Azure Blob Data Export dans Braze avec Certificate Service Principal sélectionné, affichant les champs Tenant ID, Client ID, Account Endpoint, Certificate, Container Name et Prefix.]({% image_buster /assets/img/azure-currents-cert-sp-3.png %})

Lorsque vous enregistrez, Braze valide les identifiants que vous avez saisis.

Enfin, faites défiler jusqu'en bas de la page et sélectionnez les événements d'engagement lié aux messages ou les événements de comportement client que vous souhaitez exporter. Une fois terminé, lancez votre Current.

## Mise à jour des identifiants Azure pour Currents {#updating-currents-credentials}

Vous pouvez mettre à jour les identifiants Azure sur un connecteur Braze Currents existant sans interrompre l'intégration ni perdre les données déjà exportées vers votre conteneur.

Pour actualiser les identifiants — ou pour basculer entre les méthodes **Connection String** et **Certificate Service Principal** — terminez les étapes côté Azure pour la méthode choisie, décrites plus haut dans cet article. Ensuite, dans Braze, accédez à **Currents**, localisez votre connecteur Azure Blob dans la liste, sélectionnez **Edit Current**, mettez à jour les **Credentials**, puis sélectionnez **Update Current**. Braze valide les identifiants que vous saisissez ; votre connecteur continue de fonctionner et les données déjà présentes dans votre conteneur restent disponibles. Pour en savoir plus, consultez [Mise à jour de Currents dans Configurer Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#updating-currents).

{% alert important %}
Il est important de maintenir votre certificat à jour. Si votre certificat expire, le connecteur cesse d'envoyer des événements jusqu'à ce que vous fournissiez un certificat valide, et une interruption prolongée peut entraîner une perte de données.
{% endalert %}

## Comportement de l'exportation {#export-behavior}

Les utilisateurs qui ont intégré une solution de stockage de données dans le cloud et qui tentent d'exporter des API, des rapports de tableau de bord ou des rapports CSV constateront le comportement suivant :

- Toutes les exportations d'API ne renverront pas d'URL de téléchargement dans le corps de la réponse et devront être récupérées via le stockage de données.
- Tous les rapports de tableau de bord et les rapports CSV seront envoyés par e-mail à l'utilisateur pour téléchargement (aucune autorisation de stockage requise) et sauvegardés dans le stockage de données.

{% alert important %}
**Exigence de format JSON** : Pour les exportations JSON, Braze utilise le format [JSONL](https://jsonlines.org/) (JSON délimité par des retours à la ligne), où chaque ligne contient un objet JSON distinct. Ce format diffère du JSON standard, qui est un tableau ou un objet JSON unique. Chaque ligne du fichier exporté est un objet JSON valide, mais le fichier dans son ensemble n'est pas un document JSON unique valide. Lors du traitement de ces fichiers, analysez chaque ligne individuellement comme un objet JSON distinct plutôt que de tenter d'analyser l'ensemble du fichier comme un seul document JSON. <br><br> Les exportations Currents utilisent le format [Apache Avro](https://avro.apache.org/) (fichiers `.avro`), et non JSON. Cette exigence de format JSON s'applique aux exportations de données du tableau de bord et aux exportations d'API qui utilisent le format JSON.
{% endalert %}

## FAQ

### Braze peut-il fournir des adresses IP à ajouter à une liste d'autorisation pour Azure Blob Storage ? {#can-braze-provide-ip-addresses-to-allowlist-for-azure-blob-storage}

Braze ne publie pas de liste fixe d'adresses IP autorisées pour les exportations Currents ou les exportations du tableau de bord vers Azure Blob Storage. Braze écrit dans votre conteneur en utilisant les identifiants et le nom du conteneur que vous fournissez, et Azure contrôle l'accès réseau via les paramètres de votre compte de stockage (par exemple, les règles de pare-feu du compte de stockage ou les endpoints privés).

Si votre équipe de sécurité exige des restrictions basées sur les adresses IP, utilisez les fonctionnalités réseau d'Azure sur votre compte de stockage plutôt qu'une liste d'adresses IP fournie par Braze. Pour les étapes de configuration, consultez la [documentation de Microsoft sur la sécurisation d'Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security).