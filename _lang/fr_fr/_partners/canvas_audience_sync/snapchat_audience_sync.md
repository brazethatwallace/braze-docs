---
nav_title: Snapchat
article_title: Synchronisation de l'audience de Canvas sur Snapchat
description: "Cet article de référence vous explique comment synchroniser l'audience Braze avec Snapchat, pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
page_order: 6
alias: "/audience_sync_snapchat/"

tool:
  - Canvas

---

# Synchronisation de l'audience avec Snapchat {#audience-sync-to-snapchat}

Grâce à la synchronisation de l'audience Braze avec Snapchat, les marques peuvent ajouter les données utilisateurs de leur intégration Braze aux listes de clients Snapchat pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore. Tous les critères que vous utiliseriez normalement pour déclencher un message (notification push, e-mail, SMS, webhook, etc.) dans un Canvas Braze sur la base de vos données utilisateur peuvent désormais être utilisés pour déclencher une publicité à destination de cet utilisateur dans vos listes de clients Snapchat.

**Les cas d'usage courants pour la synchronisation de l'audience incluent :**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

Cette fonctionnalité permet aux utilisateurs de contrôler quelles données first-party spécifiques sont partagées avec Snapchat. Chez Braze, les intégrations avec lesquelles vous pouvez et ne pouvez pas partager vos données first-party sont prises en compte avec la plus grande attention. Pour plus d'informations, consultez notre [politique de confidentialité](https://www.braze.com/privacy).

{% alert important %}
**Avis de non-responsabilité d'Audience Sync Pro**<br>
La synchronisation de l'audience Braze avec Snapchat est une intégration Audience Sync Pro. Pour plus d'informations sur cette intégration, contactez votre gestionnaire de compte Braze.
{% endalert %}

## Prérequis {#prerequisites}

Vous devez vous assurer que les éléments suivants sont créés, complétés et/ou acceptés avant de configurer votre étape de synchronisation d'audience Snapchat dans Canvas.

| Exigence | Origine | Description |
| --- | --- | --- |
| Snapchat Business Manager | Snapchat | Un outil centralisé pour gérer les ressources Snapchat de votre marque (telles que les comptes publicitaires, les pages, les applications). |
| Compte publicitaire Snapchat | Snapchat | Un compte publicitaire Snapchat actif lié au Snapchat Business Manager de votre marque.<br><br>Assurez-vous que l'administrateur de votre Snapchat Business Manager vous a accordé les autorisations d'administrateur pour les comptes publicitaires Snapchat que vous prévoyez d'utiliser avec Braze. |
| Conditions et politiques Snapchat | [Snapchat](https://www.snap.com/en-US/policies) | Acceptez de vous conformer à l'ensemble des conditions, politiques, directives et documentations requises par Snapchat en lien avec votre utilisation de la synchronisation d'audience Snapchat, y compris les conditions, politiques, directives et documentations incorporées par référence, qui peuvent inclure : les Conditions d'utilisation, les Conditions d'utilisation commerciales, les Conditions pour les développeurs, l'Audience Match, les Politiques publicitaires, la Politique de contenu commercial, les Règles de la communauté et la Responsabilité des fournisseurs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Se connecter à Snapchat {#step-1-connect-to-snapchat}

{% alert important %}
Vous devez disposer de la [permission « Admin »]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) pour connecter Snapchat à votre compte Braze.
{% endalert %}

Dans le tableau de bord de Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Snapchat**. Sous Snapchat Audience Sync, sélectionnez **Connecter Snapchat**.

![Page de la technologie Snapchat dans Braze comprenant une section Aperçu et une section Snapchat Audience Sync avec le bouton Connecter Snapchat.]({% image_buster /assets/img/snapchat/snapchat1.png %}){: style="max-width:80%;"}

Vous serez alors redirigé vers la page OAuth de Snapchat pour autoriser Braze à accéder aux permissions liées à votre intégration Audience Sync.

Une fois que vous avez confirmé, vous serez redirigé vers Braze pour sélectionner les comptes publicitaires Snapchat que vous souhaitez synchroniser.

![Liste des comptes publicitaires disponibles que vous pouvez connecter à Snapchat.]({% image_buster /assets/img/snapchat/snapchat2.png %}){: style="max-width:80%;"}

Une fois la connexion établie, vous serez renvoyé à la page partenaire, où vous pourrez voir quels comptes sont connectés et déconnecter les comptes existants.

![Version mise à jour de la page des partenaires technologiques Snapchat montrant les comptes publicitaires connectés avec succès.]({% image_buster /assets/img/snapchat/snapchat3.png %}){: style="max-width:80%;"}

Votre connexion Snapchat sera appliquée au niveau de l'espace de travail Braze. Si votre administrateur Snapchat vous retire de votre Snapchat Business Manager ou de l'accès aux comptes publicitaires Snapchat connectés, Braze détectera un jeton invalide. Par conséquent, vos Canvas actifs utilisant Snapchat afficheront des erreurs, et Braze ne sera pas en mesure de synchroniser les utilisateurs.

### Étape 2 : Ajouter une étape Audience Sync avec Snapchat {#step-2-add-an-audience-sync-step-with-snapchat}

Ajoutez un composant dans votre Canvas et sélectionnez **Audience Sync**.

![Sélecteur d'étapes Canvas avec l'option du composant Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Carte du composant Audience Sync ajoutée à un parcours Canvas.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Étape 3 : Configuration de la synchronisation {#step-3-sync-setup}

Cliquez sur le bouton **Custom Audience** pour ouvrir l'éditeur de composant.

Sélectionnez **Snapchat** comme partenaire Audience Sync souhaité.

![Éditeur du composant Audience Sync avec Snapchat sélectionné comme partenaire de synchronisation.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Sélectionnez ensuite le compte publicitaire Snapchat souhaité. Dans le menu déroulant **Choose a New or Existing Audience**, saisissez le nom d'une audience nouvelle ou existante.

{% tabs %}
{% tab Créer une nouvelle audience %}

**Créer une nouvelle audience**<br>
Saisissez un nom pour la nouvelle audience, sélectionnez **Add Users to Audience**, puis choisissez les champs que vous souhaitez synchroniser avec Snapchat. Enregistrez ensuite votre audience en cliquant sur le bouton **Create Audience** en bas de l'éditeur d'étape.

![Vue développée de l'étape Canvas Custom Audience. Le compte publicitaire souhaité est sélectionné et une nouvelle audience est créée.]({% image_buster /assets/img/audience_sync/snapchat3.png %})

Braze affiche une notification en haut de l'éditeur d'étape si l'audience est créée avec succès ou si des erreurs surviennent. Les utilisateurs peuvent référencer cette audience pour la suppression d'utilisateurs ultérieurement dans le parcours Canvas, car l'audience a été créée en mode brouillon.

![Alerte qui apparaît après la création d'une nouvelle audience dans le composant Canvas.]({% image_buster /assets/img/audience_sync/snapchat2.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze synchronise les utilisateurs en quasi temps réel dès qu'ils entrent dans le composant Audience Sync.

{% endtab %}
{% tab Synchroniser avec une audience existante %}
**Synchroniser avec une audience existante**<br>
Braze offre également la possibilité d'ajouter des utilisateurs à des audiences Snapchat existantes pour s'assurer qu'elles sont à jour. Pour synchroniser avec une audience existante, saisissez le nom de l'audience existante dans le menu déroulant et sélectionnez **Add to the Audience**. Braze ajoutera alors les utilisateurs en quasi temps réel dès qu'ils entreront dans le composant Audience Sync.

![Vue développée de l'étape Canvas Custom Audience. Le compte publicitaire souhaité et l'audience existante sont sélectionnés.]({% image_buster /assets/img/audience_sync/snapchat.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Lancer le Canvas {#step-4-launch-canvas}

Après avoir configuré votre Audience Sync vers Snapchat, lancez le Canvas ! Une nouvelle audience est créée, et les utilisateurs qui passent par l'étape Audience Sync sont ajoutés à cette audience sur Snapchat. Si votre Canvas contient des composants ultérieurs, vos utilisateurs progressent vers l'étape suivante de leur parcours utilisateur.

Vous pouvez consulter l'audience dans Snapchat en accédant à votre compte de gestionnaire de publicités et en sélectionnant **Audiences** dans la section Assets de la navigation. Depuis la page **Audiences**, vous pouvez voir la taille de chaque audience une fois qu'elle atteint environ 1 000.

![Détails de l'audience pour une audience Snapchat donnée, incluant le nom de l'audience, le type d'audience, la taille de l'audience et la rétention de l'audience en jours.]({% image_buster /assets/img/snapchat/snapchat7.png %})

## Synchronisation des utilisateurs et considérations relatives aux limites de débit {#user-syncing-and-rate-limit-considerations}

Lorsque les utilisateurs atteignent l'étape Audience Sync, Braze les synchronise en quasi temps réel tout en respectant les limites de débit de l'API de Snapchat. Braze regroupe et traite autant d'utilisateurs que possible toutes les 5 secondes avant de les envoyer à Snapchat.

La limite de débit de l'API de Snapchat n'autorise pas plus de dix requêtes par seconde et 100 000 utilisateurs par requête. Si un client atteint cette limite, Braze retente la synchronisation pendant environ 13 heures. Si la synchronisation n'est toujours pas possible, Braze répertorie ces utilisateurs dans l'indicateur Users Errored.

### Comprendre les analyses {#understanding-analytics}

Le tableau suivant présente les indicateurs et descriptions pour vous aider à mieux comprendre les analyses de votre composant Audience Sync.

| Indicateur | Description |
| --- | --- |
| Entered | Nombre d'utilisateurs ayant accédé à ce composant pour être synchronisés vers Snapchat. |
| Proceeded to Next Step | Combien d'utilisateurs sont passés au composant suivant, s'il y en a un ? Tous les utilisateurs avancent automatiquement s'il s'agit de la dernière étape de la branche du Canvas. |
| Users Synced | Nombre d'utilisateurs ayant été synchronisés avec succès vers Snapchat. |
| Users Not Synced | Nombre d'utilisateurs n'ayant pas été synchronisés en raison de champs manquants pour la correspondance. |
| Users Pending | Nombre d'utilisateurs en cours de traitement par Braze pour la synchronisation vers Snapchat. |
| Users Errored | Nombre d'utilisateurs n'ayant pas été synchronisés vers Snapchat en raison d'une erreur d'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton Snapchat invalide ou la suppression de l'audience sur Snapchat. |
| Exited Canvas | Nombre d'utilisateurs ayant quitté le Canvas. Cela se produit lorsque la dernière étape d'un Canvas est un composant Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprendre les analyses" }

{% alert important %}
N'oubliez pas qu'il y aura un délai dans le reporting pour les utilisateurs synchronisés et les indicateurs d'erreurs, en raison respectivement du vidage en masse et des 13 heures de tentatives.
{% endalert %}

## Questions fréquentes {#frequently-asked-questions}

### Combien d'audiences Snapchat peut-il prendre en charge ? {#how-many-audiences-can-snapchat-support}

À l'heure actuelle, vous ne pouvez avoir que 1 000 audiences dans votre compte Snapchat.

Si vous dépassez cette limite, Braze vous informera que nous ne pouvons pas créer de nouvelles audiences. Vous devrez supprimer les audiences que vous n'utilisez plus dans votre compte publicitaire Snapchat.

### Comment savoir si des utilisateurs ont été mis en correspondance après avoir transmis des utilisateurs à Snapchat ? {#how-do-i-know-if-users-have-matched-after-passing-users-to-snapchat}

Snapchat ne fournit pas cette information en raison de ses politiques de confidentialité des données.

### Que dois-je faire si je reçois une erreur de jeton invalide ? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Vous pouvez déconnecter et reconnecter votre compte Snapchat sur la page partenaire Snapchat. Confirmez auprès de l'administrateur de votre Snapchat Business Manager que vous disposez des autorisations appropriées pour le compte publicitaire avec lequel vous souhaitez synchroniser.

### Pourquoi mon Canvas ne peut-il pas être lancé ? {#why-is-my-canvas-not-allowed-to-launch}

Assurez-vous que votre compte publicitaire Snapchat se connecte correctement à Braze sur la page partenaire Snapchat. Vérifiez que vous avez sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience et sélectionné les champs à mettre en correspondance.