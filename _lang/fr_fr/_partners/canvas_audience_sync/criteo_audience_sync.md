---
nav_title: Criteo
article_title: Synchronisation d'audience Canvas avec Criteo
description: "Cet article de référence explique comment utiliser la synchronisation d'audience Braze avec Criteo pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
page_order: 1
alias: /audience_sync_criteo/

tool:
  - Canvas
---

# Synchronisation d'audience avec Criteo {#audience-sync-to-criteo}

Grâce à la synchronisation d'audience Braze avec Criteo, les marques peuvent choisir d'ajouter les données utilisateurs de leur propre intégration Braze aux listes de clients Criteo afin de diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore. Tous les critères que vous utiliseriez normalement pour déclencher un message (notification push, e-mail, SMS, webhook, etc.) dans un Canvas Braze sur la base de vos données utilisateur peuvent désormais être utilisés pour déclencher une publicité pour cet utilisateur dans vos listes de clients Criteo.

**Les cas d'usage courants pour la synchronisation d'audience incluent :**

- Cibler des utilisateurs à forte valeur via plusieurs canaux pour stimuler les achats ou l'engagement
- Recibler des utilisateurs qui sont moins réactifs aux autres canaux marketing
- Créer des audiences de suppression pour empêcher les utilisateurs de recevoir des publicités lorsqu'ils sont déjà des consommateurs fidèles de votre marque
- Créer des audiences similaires pour acquérir de nouveaux utilisateurs plus efficacement

Cette fonctionnalité donne aux marques la possibilité de contrôler quelles données first-party spécifiques sont partagées avec Criteo. Chez Braze, les intégrations avec lesquelles vous pouvez et ne pouvez pas partager vos données first-party sont prises en compte avec la plus grande attention. Pour plus d'informations, consultez notre [politique de confidentialité](https://www.braze.com/privacy).

{% alert important %}
**Avis de non-responsabilité d'Audience Sync Pro**<br>
La synchronisation d'audience Braze avec Criteo est une intégration Audience Sync Pro. Pour plus d'informations sur cette intégration, contactez votre gestionnaire de compte Braze. <br>
{% endalert %}

## Conditions préalables {#prerequisites}

Vous devez vous assurer que les éléments suivants ont été créés et/ou complétés avant de configurer votre synchronisation d'audience avec Criteo.

| Condition | Origine | Description |
| --- | --- | --- |
| Compte publicitaire Criteo | [Criteo](https://marketing.criteo.com/) | Un compte publicitaire Criteo actif lié à votre marque.<br><br>Assurez-vous que votre administrateur Criteo vous a accordé les autorisations appropriées pour accéder aux audiences. |
| [Directives publicitaires de Criteo](https://www.criteo.com/advertising-guidelines/)<br>et<br>[Directives de sécurité de la marque Criteo](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | En tant que client actif de Criteo, vous devez vous assurer que vous pouvez respecter les directives publicitaires et de sécurité de la marque de Criteo avant de lancer toute campagne Criteo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Se connecter à Criteo {#step-1-connect-to-criteo}

{% alert important %}
Vous devez disposer de l'[autorisation « Admin »]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) pour connecter Criteo à votre compte Braze.
{% endalert %}

Dans le tableau de bord de Braze, allez dans **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Criteo**. Sous Criteo Audience Export, sélectionnez **Connect Criteo**.

![Page de la technologie Criteo dans Braze comprenant une section Aperçu et une section Criteo avec le bouton Connect Criteo.]({% image_buster /assets/img/criteo/criteo5.png %}){: style="max-width:80%;"}

Une page oAuth Criteo s'affiche pour autoriser Braze à obtenir les permissions liées à votre intégration de synchronisation d'audience.

Une fois que vous avez confirmé, vous serez redirigé vers Braze pour sélectionner les comptes publicitaires Criteo que vous souhaitez synchroniser.

![Une liste de comptes publicitaires disponibles que vous pouvez connecter à Criteo.]({% image_buster /assets/img/criteo/criteo7.png %}){: style="max-width:80%;"}

Une fois la connexion établie, vous revenez à la page partenaire, où vous pouvez voir quels comptes sont connectés et déconnecter les comptes existants.

![Une version mise à jour de la page des partenaires technologiques de Criteo montrant les comptes publicitaires connectés avec succès.]({% image_buster /assets/img/criteo/criteo4.png %}){: style="max-width:80%;"}

Votre connexion Criteo sera appliquée au niveau de l'espace de travail Braze. Si votre administrateur Criteo vous supprime de votre compte publicitaire Criteo, Braze détectera un jeton invalide. En conséquence, vos Canvas actifs utilisant Criteo afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs.

### Étape 2 : Configurer vos critères d'entrée de Canvas {#step-2-configure-your-canvas-entry-criteria}

Lors de la création d'audiences pour le suivi publicitaire, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et afin de respecter les lois sur la confidentialité, telles que le droit « Ne pas vendre ou partager » en vertu du [CCPA](https://oag.ca.gov/privacy/ccpa). Les marketeurs devraient mettre en œuvre les filtres pertinents pour l'éligibilité des utilisateurs dans leurs critères d'entrée de Canvas. Voici quelques options possibles.

Si vous avez collecté l'[IDFA iOS via le SDK Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection), vous pourrez utiliser le filtre Ads Tracking Enabled. Sélectionnez la valeur comme vraie pour n'envoyer les utilisateurs que dans les destinations de synchronisation d'audience où ils ont donné leur consentement.

![Filtre d'entrée Canvas avec Ads Tracking Enabled défini sur vrai.]({% image_buster /assets/img/criteo/criteo11.png %})

Si vous collectez des `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, ou tout autre attribut personnalisé pertinent, vous devez les inclure dans les critères d'entrée de votre Canvas en tant que filtre :

![Filtre d'entrée Canvas utilisant des attributs personnalisés d'abonnement pour l'éligibilité de l'audience.]({% image_buster /assets/img/criteo/criteo12.png %})

Pour en savoir plus sur la manière de se conformer à ces lois sur la protection des données au sein de la plateforme Braze, consultez l'[Assistance technique à la protection des données]({{site.baseurl}}/dp-technical-assistance).

### Étape 3 : Ajouter une étape de synchronisation d'audience avec Criteo {#step-3-add-an-audience-sync-step-with-criteo}

Ajoutez un composant dans votre Canvas et sélectionnez **Audience Sync**.

![Workflow des étapes précédentes pour ajouter un composant d'audience Criteo dans Canvas.]({% image_buster /assets/img/criteo/criteo9.png %}){: style="max-width:35%;"} ![Workflow des étapes précédentes pour ajouter un composant d'audience Criteo dans Canvas.]({% image_buster /assets/img/criteo/criteo10.png %}){: style="max-width:28%;"}

### Étape 4 : Configuration de la synchronisation {#step-4-sync-setup}

Cliquez sur le bouton **Custom Audience** pour ouvrir l'éditeur de composants.

Sélectionnez **Criteo** comme partenaire de synchronisation d'audience souhaité.

![Éditeur de l'étape de synchronisation d'audience avec Criteo sélectionné comme partenaire.]({% image_buster /assets/img/criteo/criteo6.png %})

Sélectionnez ensuite le compte publicitaire Criteo souhaité. Dans la liste déroulante **Choose a New or Existing Audience**, saisissez le nom d'une audience nouvelle ou existante.

{% tabs %}
{% tab Créer une nouvelle audience %}
**Créer une nouvelle audience**<br>
Saisissez un nom pour la nouvelle audience, sélectionnez **Add Users to Audience** et sélectionnez les champs que vous souhaitez synchroniser avec Criteo. Ensuite, enregistrez votre audience en cliquant sur le bouton **Create Audience** en bas de l'éditeur d'étape.

![Vue élargie de l'étape Canvas d'audience personnalisée. Le compte publicitaire souhaité est sélectionné et une nouvelle audience est créée ici.]({% image_buster /assets/img/criteo/criteo3.png %})

Braze affiche une notification en haut de l'éditeur d'étape si l'audience est créée avec succès ou si des erreurs surviennent. Les utilisateurs peuvent faire référence à cette audience pour la suppression d'utilisateurs plus tard dans le parcours Canvas, car l'audience a été créée en mode brouillon.

![Une alerte qui apparaît après la création d'une nouvelle audience dans le composant Canvas.]({% image_buster /assets/img/criteo/criteo1.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze synchronise les utilisateurs quasiment en temps réel lorsqu'ils entrent dans le composant de synchronisation d'audience.
{% endtab %}
{% tab Synchroniser avec une audience existante %}
**Synchroniser avec une audience existante**<br>
Braze offre également la possibilité d'ajouter des utilisateurs aux audiences Criteo existantes afin de s'assurer que ces audiences sont à jour. Pour effectuer une synchronisation avec une audience existante, saisissez le nom de l'audience existante dans le menu déroulant et sélectionnez **Add to the Audience**. Braze ajoutera ensuite les utilisateurs en temps quasi réel au fur et à mesure qu'ils entreront dans le composant de synchronisation d'audience.

![Vue élargie de l'étape Canvas d'audience personnalisée. Le compte publicitaire souhaité et l'audience existante sont sélectionnés ici.]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### Étape 5 : Lancer le Canvas {#step-5-launch-canvas}

Une fois que vous avez configuré la synchronisation d'audience avec Criteo, lancez simplement le Canvas ! La nouvelle audience sera créée, et les utilisateurs qui passeront par l'étape de synchronisation d'audience seront intégrés à cette audience sur Criteo. Si votre Canvas contient des composants ultérieurs, vos utilisateurs passeront ensuite à l'étape suivante de leur parcours utilisateur.

Vous pouvez voir l'audience dans Criteo en accédant à votre compte gestionnaire de publicités, puis en sélectionnant Segments dans la **Audience Library** de la navigation. Sur la page **Segments**, vous pouvez voir la taille de chaque audience après qu'elle a atteint environ 1 000.

![La bibliothèque d'audiences affichant le segment, l'ID, la source, le type, la taille, l'utilisation actuelle et la dernière mise à jour.]({% image_buster /assets/img/criteo/criteo.png %})

## Considérations relatives à la synchronisation des utilisateurs et à la limite de débit {#user-syncing-and-rate-limit-considerations}

Lorsque les utilisateurs atteignent l'étape de synchronisation d'audience, Braze les synchronise quasiment en temps réel tout en respectant les limites de débit de l'API de Criteo. Braze met en lots et traite autant d'utilisateurs que possible toutes les cinq secondes avant de les envoyer à Criteo.

La limite de débit de l'API de Criteo n'autorise pas plus de 250 requêtes par minute. Si un client atteint cette limite, Braze retente la synchronisation pendant environ 13 heures. Si la synchronisation n'est toujours pas possible, Braze répertorie ces utilisateurs sous l'indicateur Users Errored.

## Comprendre les analyses {#understanding-analytics}

Le tableau suivant comprend des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses de votre composant de synchronisation d'audience.

| Indicateur | Description |
| --- | --- |
| Entrés | Nombre d'utilisateurs ayant entré ce composant pour être synchronisés avec Criteo. |
| Passés à l'étape suivante | Nombre d'utilisateurs passés au composant suivant s'il y en a un. Tous les utilisateurs avanceront automatiquement s'il s'agit de la dernière étape de la branche Canvas. |
| Utilisateurs synchronisés | Nombre d'utilisateurs qui ont été synchronisés avec succès avec Criteo. |
| Utilisateurs non synchronisés | Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants à faire correspondre. |
| Utilisateurs en attente | Nombre d'utilisateurs actuellement traités par Braze pour être synchronisés avec Criteo. |
| Utilisateurs en erreur | Nombre d'utilisateurs qui n'ont pas été synchronisés avec Criteo en raison d'une erreur d'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton Criteo invalide ou la suppression de l'audience dans Criteo. |
| Sortis du Canvas | Nombre d'utilisateurs ayant quitté le Canvas. Cela se produit lorsque la dernière étape d'un Canvas est un composant de synchronisation d'audience. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprendre les analyses" }

{% alert important %}
N'oubliez pas qu'il y aura un délai dans le reporting des indicateurs d'utilisateurs synchronisés et d'utilisateurs en erreur, en raison respectivement du vidage en masse et de la relance après 13 heures.
{% endalert %}

## Foire aux questions {#frequently-asked-questions}

### Que dois-je faire si je reçois une erreur de jeton invalide ? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}
Vous pouvez simplement déconnecter et reconnecter votre compte Criteo sur la page partenaire Criteo. Assurez-vous auprès de votre administrateur Criteo que vous disposez des autorisations appropriées pour le compte publicitaire avec lequel vous souhaitez synchroniser.

### Pourquoi mon Canvas n'est-il pas autorisé à être lancé ? {#why-is-my-canvas-not-allowed-to-launch}

Confirmez que votre compte publicitaire Criteo s'est bien connecté à Braze sur la page partenaire Criteo. Ensuite, vérifiez que vous avez sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience et sélectionné les champs à faire correspondre.

### Comment puis-je savoir si les utilisateurs ont été appariés après les avoir transmis à Criteo ? {#how-do-i-know-if-users-have-matched-after-passing-users-to-criteo}

Criteo ne fournit pas ces informations en raison de ses propres politiques de confidentialité des données.

### Combien d'audiences Criteo peut-il prendre en charge ? {#how-many-audiences-can-criteo-support}

Pour l'instant, vous ne pouvez avoir que 1 000 audiences au sein de votre compte Criteo. Si vous dépassez cette limite, Braze vous informera de l'impossibilité de créer de nouvelles audiences. Vous devrez supprimer les audiences que vous n'utilisez plus dans votre compte publicitaire Criteo.