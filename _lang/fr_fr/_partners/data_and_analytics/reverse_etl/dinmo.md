---
nav_title: DinMo
article_title: DinMo
description: "Cet article de référence décrit le partenariat entre Braze et DinMo, une plateforme de données client composable qui utilise le reverse ETL pour synchroniser les données d'entrepôt dans Braze."
alias: /partners/dinmo/
page_type: partner
search_tag: Partner

---

# DinMo

> [DinMo](https://www.dinmo.com/) est une plateforme de données client (CDP) composable qui connecte votre entrepôt de données cloud à Braze via le reverse ETL (ETL or extraire, transformer, charger). Les équipes marketing peuvent créer des segments d'audience à partir des données de l'entrepôt, synchroniser les attributs utilisateur et les événements dans Braze, et maintenir les statuts d'abonnement à jour sans téléchargement de fichiers CSV ni assistance technique.

_Cette intégration est gérée par DinMo._

L'intégration de Braze et DinMo envoie des segments et des modèles de données depuis votre entrepôt vers Braze via la REST API de Braze. Lorsque vous connectez une destination Braze dans DinMo, les activations envoient les données de vos modèles ou segments vers Braze.

## Prérequis {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte DinMo | Un [compte DinMo](https://www.dinmo.com/) avec la permission de créer des destinations est nécessaire pour tirer parti de ce partenariat. |
| Clé API REST Braze | Une clé API REST Braze avec les [permissions](#api-key-permissions) requises pour les services de destination que vous prévoyez d'utiliser. Vous pouvez la créer dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST Braze | L'URL de votre endpoint REST. Votre endpoint dépend des [endpoints API]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints) de votre instance Braze. |
| URL du tableau de bord de Braze | L'URL du tableau de bord de Braze pour votre instance (par exemple, `https://dashboard.iad-01.braze.com`). Pour plus d'informations, consultez [Endpoints SDK disponibles]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). |
| Entrepôt de données et modèle de données | Avant de commencer l'intégration, connectez votre entrepôt de données dans DinMo et définissez un modèle ou un segment pour les données que vous souhaitez synchroniser avec Braze. Pour plus d'informations, consultez le [guide d'intégration DinMo Braze](https://docs.dinmo.io/integrations/destination-platforms/braze). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Cas d'usage {#use-cases}

Grâce à cette intégration, vous pouvez :

* Synchroniser les attributs utilisateur depuis votre entrepôt de données vers Braze pour personnaliser les Campaigns et les Canvas.
* Envoyer des événements personnalisés et des événements d'achat depuis les données de l'entrepôt vers Braze pour le ciblage comportemental.
* Maintenir l'appartenance aux groupes d'abonnement Braze alignée avec les Segments d'audience définis dans DinMo.
* Exporter les Segments DinMo en tant qu'attributs utilisateur Braze et créer des Segments Braze à partir de ces attributs.

## Autorisations de la clé API {#api-key-permissions}

Accordez les autorisations suivantes à votre clé API REST de Braze en fonction des services de destination que vous utilisez :

| Autorisation | Requis pour |
| --- | --- |
| `users.track` | Synchronisation des attributs utilisateur, envoi d'événements de suivi et validation de la connexion de destination |
| `users.export.ids` | Exportation des ID utilisateur pour les opérations en masse |
| `users.alias.update` | Mise à jour des alias d'utilisateur |
| `subscription.status.set` | Synchronisation des statuts d'abonnement |
| `users.delete` | Mode de synchronisation miroir uniquement (facultatif pour les autres services de destination) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Autorisations de la clé API" }

## Intégration {#integration}

### Étape 1 : Configurer la destination Braze dans DinMo {#step-1-configure-the-braze-destination-in-dinmo}

1. Dans DinMo, accédez à **Destinations** dans la navigation latérale.
2. Sélectionnez **Add a new destination** > **Connect a new platform** > **Braze**.
3. Dans le formulaire de connexion, saisissez les informations suivantes :
   * **Platform Name** : Par exemple, `Braze – Your Company`
   * **REST API URL** : L'endpoint REST de votre instance (par exemple, `https://rest.eu-01.braze.com`)
   * **Dashboard URL** : L'URL du tableau de bord de votre instance (par exemple, `https://dashboard.eu-01.braze.com`)
   * **API Key** : La clé que vous avez copiée depuis Braze
4. Sélectionnez **Connect** pour valider vos identifiants.

{% alert note %}
Vous devez spécifier à la fois l'URL de la REST API et l'URL du tableau de bord. N'incluez pas de barre oblique finale dans l'URL de la REST API.
{% endalert %}

### Étape 2 : Vérifier la connexion {#step-2-verify-the-connection}

Après avoir enregistré la destination, DinMo effectue un appel de test (par exemple, `users.track`) pour confirmer que votre clé API et votre endpoint fonctionnent.

Si la validation échoue, vérifiez les points suivants :

* L'URL de la REST API est correcte et ne comporte pas de barre oblique finale.
* La clé API est valide et dispose des autorisations requises.
* Si votre espace de travail Braze utilise une liste d'adresses IP autorisées, les adresses IP de DinMo y sont incluses.

## Services de destination pris en charge {#supported-destination-services}

Chaque service de destination dans DinMo suit le même flux de travail général : créer une destination Braze, construire un modèle ou un segment DinMo, puis créer une activation pour envoyer des données à Braze. Pour des instructions d'activation étape par étape, consultez [Services de destination Braze de DinMo](https://docs.dinmo.io/integrations/destination-platforms/braze).

Les services de destination suivants sont disponibles :

| Service de destination | Description |
| --- | --- |
| [Synchroniser les attributs utilisateur](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-users-attributes) | Mettre à jour les attributs du profil utilisateur dans Braze et éventuellement insérer de nouveaux utilisateurs. |
| [Envoyer des événements de suivi](https://docs.dinmo.io/integrations/destination-platforms/braze/send-track-events) | Envoyer des événements personnalisés et des événements d'achat à Braze. |
| [Synchroniser les statuts d'abonnement](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-subscription-statuses) | Abonner ou désabonner des utilisateurs dans un groupe d'abonnement Braze en fonction de l'appartenance à un segment DinMo. |
| [Exporter des listes d'utilisateurs](https://docs.dinmo.io/integrations/destination-platforms/braze/export-user-lists) | Synchroniser l'appartenance à un segment avec un attribut utilisateur Braze pour l'utiliser dans la segmentation Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Services de destination pris en charge" }

### Synchroniser les attributs utilisateur {#synchronize-user-attributes}

Utilisez ce service de destination pour mettre à jour les attributs des profils utilisateur Braze existants et, éventuellement, insérer de nouveaux utilisateurs.

Lorsque vous exécutez une activation :

* Si vous activez le mode d'insertion, les nouveaux utilisateurs du modèle sont créés dans Braze (comportement UPSERT).
* Les valeurs d'attribut modifiées depuis la dernière activation sont mises à jour dans Braze.

Si vous n'activez pas le mode d'insertion, DinMo met à jour uniquement les utilisateurs qui existent déjà dans Braze et dont l'ID externe correspond.

Lors de la configuration de l'activation, mappez le champ de votre modèle DinMo qui correspond à l'[ID externe]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web) ou à l'ID Braze de l'utilisateur. Mappez chaque champ DinMo au nom exact de l'attribut dans Braze. Si un attribut n'existe pas dans Braze, DinMo le crée.

Les modes de synchronisation suivants sont disponibles pour les activations d'attributs utilisateur :

| Mode de synchronisation | Description |
| --- | --- |
| UPDATE | Met à jour les enregistrements modifiés pour les utilisateurs qui existent déjà dans Braze. N'insère ni ne supprime d'enregistrements. |
| UPSERT | Insère de nouveaux enregistrements et met à jour les enregistrements modifiés. Ne supprime pas d'enregistrements. |
| MIRROR | Insère, met à jour et supprime des enregistrements dans Braze pour refléter la source. Nécessite la prise en charge des opérations de suppression par le connecteur. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modes de synchronisation des attributs utilisateur" }

{% alert warning %}
Le mode de synchronisation MIRROR supprime définitivement les enregistrements de Braze lorsqu'ils ne sont plus présents dans la source DinMo. Utilisez le mode MIRROR uniquement lorsque votre entrepôt de données est la source de vérité unique et que les suppressions sont intentionnelles. Validez les règles de suppression avant d'exécuter des synchronisations MIRROR en production.
{% endalert %}

### Envoyer des événements de suivi {#send-track-events}

Utilisez ce service de destination pour envoyer des événements personnalisés ou des événements d'achat depuis un modèle d'événement ou un segment DinMo vers Braze. DinMo traite les événements personnalisés et les achats comme des services de destination distincts, car Braze utilise des API différentes pour chaque type.

Chaque enregistrement du modèle représente un type d'événement unique (par exemple, `Purchase`). DinMo envoie uniquement les nouveaux événements à chaque exécution d'activation et ne met pas à jour les événements précédemment envoyés.

Lors de la configuration de l'activation :

1. Spécifiez le nom de l'événement tel qu'il doit apparaître dans Braze. Si l'événement n'existe pas, DinMo le crée.
2. Mappez les champs obligatoires :
   * **Horodatage de l'événement** : horodatage du moment où l'événement s'est produit
   * **ID externe** : ID externe de l'utilisateur associé à l'événement
3. Mappez les propriétés d'événement facultatives aux noms d'attribut Braze.
4. Définissez la planification de la fréquence d'envoi des nouveaux événements à Braze.

### Synchroniser les statuts d'abonnement {#synchronize-subscription-statuses}

Utilisez ce service de destination pour maintenir un groupe d'abonnement Braze aligné avec un segment ou un modèle DinMo.

Avant d'activer ce service :

1. Créez le groupe d'abonnement cible (SMS ou e-mail) dans Braze.
2. Construisez un modèle ou un segment DinMo contenant les utilisateurs qui doivent appartenir à ce groupe d'abonnement.

Lors de la configuration de l'activation, saisissez l'ID exact du groupe d'abonnement depuis Braze. Pour synchroniser plusieurs groupes d'abonnement, créez une activation par groupe.

Lorsque l'activation s'exécute :

* Si les utilisateurs existent déjà dans Braze, ceux qui entrent dans le segment DinMo sont marqués comme abonnés au groupe d'abonnement cible.
* Les utilisateurs qui quittent le segment DinMo sont marqués comme désabonnés du groupe d'abonnement.

DinMo ne modifie pas les utilisateurs qui n'ont jamais fait partie du segment et ne crée pas de nouveaux utilisateurs Braze dans ce service de destination.

### Exporter des listes d'utilisateurs {#export-user-lists}

Utilisez ce service de destination pour représenter un segment DinMo sous forme d'attribut utilisateur Braze. En raison d'une limitation de Braze, DinMo ne crée pas directement de liste Braze. À la place, il définit un attribut utilisateur sur `true` pour les utilisateurs du segment et sur `false` pour les utilisateurs qui quittent le segment.

Lors de la configuration de l'activation, spécifiez le nom de l'audience. DinMo utilise ce nom comme attribut Braze (les espaces sont remplacés par des tirets bas). Vérifiez qu'un attribut portant le même nom n'existe pas déjà dans Braze. Mappez le champ DinMo qui correspond à l'ID externe de l'utilisateur.

Après l'exécution de l'activation, créez un Segment Braze qui filtre les utilisateurs dont l'attribut synchronisé est égal à `true`.

Seuls les utilisateurs possédant un ID externe correspondant à un utilisateur Braze existant sont mis à jour. Ce service de destination ne crée pas de nouveaux utilisateurs.