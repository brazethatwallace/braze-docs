---
nav_title: Extole
article_title: Extole
description: "Cet article décrit le partenariat entre Braze et Extole, une entreprise de marketing de recommandation, qui vous permet de récupérer des événements et attributs client à partir des programmes de parrainage et de croissance dans Braze"
alias: /partners/extole/
page_type: partner
search_tag: Partner

---

# Extole

> [Extole](https://www.extole.com/), une entreprise SaaS leader de l'industrie du marketing de parrainage, permet de créer et d'optimiser des programmes de marketing de recommandation efficaces pour augmenter l'acquisition de clients.

_Cette intégration est maintenue par Extole._

## À propos de l'intégration {#about-the-integration}

Avec l'intégration de Braze et Extole, vous pouvez extraire des événements et attributs client des programmes de parrainage et de croissance d'Extole vers Braze, vous permettant ainsi de créer des campagnes marketing plus personnalisées qui augmentent l'acquisition, l'engagement et la fidélité des clients. Vous pouvez également extraire dynamiquement les attributs de contenu Extole, tels que les liens et codes de partage personnalisés, dans les communications Braze.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Extole | Un compte Extole est requis pour profiter de ce partenariat. |
| Clé d'API REST Braze | Une clé d'API REST Braze avec la permission `users.track`. Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| URL de l'API Braze | Votre URL d'API Braze est spécifique à votre [instance Braze]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

Les cas d'utilisation suivants illustrent quelques façons d'utiliser l'intégration d'Extole avec Braze. Travaillez avec votre équipe de mise en œuvre Extole et vos gestionnaires de la satisfaction client pour développer une option qui répond aux besoins spécifiques de votre entreprise.

- Utilisez les événements personnalisés de vos programmes de recommandation et d'engagement pour déclencher une campagne Braze ou un Canvas
- Créez des segments personnalisés, des tableaux de bord et des rapports en utilisant les données de vos programmes alimentés par Extole
- Désabonnez ou abonnez automatiquement les utilisateurs à votre liste marketing dans Braze

## Intégration {#integration}

Suivez les étapes ci-dessous pour que votre intégration soit rapidement opérationnelle. L'équipe de mise en œuvre d'Extole et les gestionnaires de la satisfaction client vous accompagneront tout au long de ce processus et répondront à toutes vos questions.

### Connectez-vous à votre compte Braze {#connect-to-your-braze-account}

1. Sélectionnez l'intégration Braze sur la page [Partenaires](https://my.extole.com/partners) de votre compte My Extole.
2. Dans l'intégration Braze, sélectionnez **Install** pour établir la connexion entre Extole et Braze.
3. Remplissez les champs obligatoires, en commençant par votre clé d'API REST Braze.
4. Entrez votre URL d'API Braze. Cette URL dépend de l'instance à laquelle votre compte Braze est provisionné.
5. Ajoutez tous les événements Extole que vous souhaitez envoyer à Braze. Les événements par défaut, les propriétés d'événement et les attributs utilisateur sont décrits dans le [tableau des événements Extole](https://dev.extole.com/docs/braze#extole-program-events).
6. Ajoutez tous les états de récompense que vous souhaitez envoyer à Braze en plus de l'état `FULFILLED`. Reportez-vous au [tableau des récompenses Extole](https://dev.extole.com/docs/braze#extole-rewards) pour obtenir les descriptions des états de récompense disponibles.
7. Sélectionnez votre mappage de clé d'ID externe Braze. C'est ainsi qu'Extole met à jour les profils utilisateur dans Braze. Vous pouvez mapper la clé d'ID externe de Braze à `email_address` ou à `partner_user_id` pour l'utilisateur. Nous recommandons d'utiliser `external_id` plutôt que `email_address`, car cette option est plus sûre.
8. Enregistrez vos paramètres pour terminer la connexion. Désormais, les événements Extole peuvent être transférés vers votre compte Braze.

### Événements du programme Extole {#extole-program-events}

Vous trouverez ci-dessous les événements par défaut, les propriétés d'événement et les attributs utilisateur qu'Extole enverra à Braze. Contactez vos gestionnaires de mise en œuvre ou de satisfaction client Extole pour identifier et ajouter des événements Extole supplémentaires à votre intégration.

| Événement | Description | Propriétés d'événement | Attributs utilisateur |
| ----------- | ----------- | ----------- | ----------- |
| `extole_created_share_link` | Un participant crée son lien de partage en entrant son e-mail dans l'expérience de partage Extole. | Nom de l'événement  <br>Heure de l'événement  <br>Partenaire (Extole)  <br>Entonnoir (référent ou ami)  <br>Programme | <br>ID externe <br>E-mail  <br>Lien de partage |
| `extole_shared` | Un participant partage son lien de recommandation avec un ami. | Nom de l'événement  <br>Heure de l'événement  <br>Partenaire (Extole)  <br>ID externe  <br>Entonnoir (référent ou ami)  <br>Programme  <br>Canal de partage | E-mail <br>Prénom <br>Nom de famille |
| `outcome` – Le résultat est dynamique en fonction de la configuration de votre programme (comme `extole_shipped`, `extole_converted`) | Un participant a converti ou complété l'événement de résultat souhaité configuré pour le programme. | Dynamique par programme | E-mail <br>Prénom <br>Nom de famille |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Événements du programme Extole" }

### États d'abonnement Extole {#extole-subscription-states}

| État d'abonnement | Description | Propriétés d'événement | Attributs utilisateur |
| ----------- | ----------- | ----------- | ----------- |
| `subscribed` | Un participant a choisi de recevoir des messages marketing. | N/A | E-mail  <br>Type de liste  <br>ID externe  <br>Abonnement e-mail (inscrit) |
| `unsubscribed` | Un participant a choisi de ne plus recevoir de communications par e-mail d'Extole. | E-mail  <br>ID externe  <br>État d'abonnement (désabonné)  <br>ID de groupe d'abonnement  | Type de liste |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="États d'abonnement Extole" }

### Récompenses Extole {#extole-rewards}

Par défaut, Extole enverra les événements de récompense dans l'état `FULFILLED` à Braze afin que vous puissiez déclencher des notifications de récompense via une campagne Braze ou un Canvas. Reportez-vous au tableau suivant pour les états de récompense supplémentaires.

| État de récompense | Description | Propriétés d'événement | Attributs utilisateur |
| ----------- | ----------- | ----------- | ----------- |
| `FULFILLED` | L'état par défaut. Une valeur a été attribuée à la récompense (comme un bon de réduction ou une carte-cadeau) par un fournisseur de récompenses Extole. | E-mail <br>Valeur nominale  <br>Code de coupon  <br>Type de valeur nominale  | E-mail <br>Prénom  <br>Nom de famille |
| `EARNED` | Une récompense a été créée et associée à une personne. | E-mail <br>Valeur nominale  <br>Code de coupon  <br>Type de valeur nominale  | E-mail <br>Prénom  <br>Nom de famille |
| `SENT` | La récompense a été attribuée et envoyée au destinataire par e-mail ou directement sur un appareil. | E-mail <br>Valeur nominale  <br>Code de coupon  <br>Type de valeur nominale  | E-mail <br>Prénom  <br>Nom de famille |
| `REDEEMED` | La récompense a été utilisée par le destinataire, comme en témoigne un événement de conversion ou d'utilisation envoyé à Extole. | E-mail <br>Valeur nominale  <br>Code de coupon  <br>Type de valeur nominale  | E-mail <br>Prénom  <br>Nom de famille |
| `FAILED` | Un problème a empêché la récompense d'être émise ou envoyée, nécessitant une intervention. | E-mail <br>Valeur nominale  <br>Code de coupon  <br>Type de valeur nominale  | E-mail <br>Prénom  <br>Nom de famille |
| `CANCELED` | La récompense a été désactivée et retournera dans l'inventaire. | E-mail <br>Valeur nominale  <br>Type de valeur nominale  | E-mail <br>Prénom  <br>Nom de famille |
| `REVOKED` | La récompense attribuée a été invalidée. Par exemple, Extole a demandé une carte-cadeau auprès d'un fournisseur, puis a déterminé que la carte avait été envoyée par erreur. Si le fournisseur prend en charge la révocation de la récompense, Extole demandera le remboursement des fonds, et la récompense ne sera plus valide. | E-mail <br>Valeur nominale   <br>Type de valeur nominale  | E-mail <br>Prénom  <br>Nom de famille |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Récompenses Extole" }


## Personnalisation {#customization}

### Rechercher et créer des utilisateurs dans Braze {#find-and-create-users-in-braze}

Pour certains cas d'utilisation, tels qu'un nouvel abonnement e-mail ou SMS où Extole ne dispose pas d'un ID externe (ID utilisateur), Extole peut vérifier l'identifiant de l'utilisateur à l'aide de l'[endpoint Exporter le profil utilisateur par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) de Braze. Extole ajoutera et mettra à jour tous les attributs de profil si l'utilisateur existe dans Braze. Si la requête ne renvoie pas de profil utilisateur, Extole utilisera l'endpoint `/users/track` pour créer un alias d'utilisateur avec l'adresse e-mail de l'utilisateur comme nom d'alias.

## Utilisation de cette intégration {#using-this-integration}

Après avoir connecté vos comptes, les événements commenceront automatiquement à circuler d'Extole vers Braze sans aucune action de votre part. Une vue en temps réel des événements envoyés à Braze est disponible dans le centre des webhooks sortants d'Extole pour la résolution des problèmes.