---
nav_title: LinkedIn
article_title: "Synchronisation de l'audience de Canvas avec LinkedIn"
alias: /linkedin_audience_sync/
description: "Cet article de référence vous expliquera comment utiliser Braze Audience Sync sur LinkedIn pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
tool:
  - Canvas
page_order: 4

---

# Synchronisation de l'audience avec LinkedIn {#audience-sync-to-linkedin}

Grâce à la synchronisation de l'audience Braze avec LinkedIn, les marques peuvent ajouter les données utilisateurs de leur intégration Braze aux listes de clients LinkedIn pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore. Les critères que vous utilisez généralement pour déclencher un message (notification push, e-mail, SMS, webhook, etc.) dans un Canvas Braze en fonction de vos données utilisateur peuvent maintenant déclencher une publicité pour cet utilisateur dans vos listes de clients LinkedIn.

**Les cas d'usage courants de la synchronisation de l'audience sont les suivants** :

- Ciblage des utilisateurs à forte valeur ajoutée via plusieurs canaux pour favoriser les achats ou l'engagement
- Reciblage des utilisateurs qui sont moins réactifs aux autres canaux marketing
- Création d'audiences de suppression pour éviter que les utilisateurs ne reçoivent des publicités alors qu'ils sont déjà des consommateurs fidèles de votre marque

Cette fonctionnalité permet aux marques de contrôler quelles données first-party spécifiques sont partagées avec LinkedIn. Chez Braze, les intégrations avec lesquelles vous pouvez et ne pouvez pas partager vos données first-party sont considérées avec le plus grand sérieux. Pour plus d'informations, consultez notre [politique de confidentialité](https://www.braze.com/privacy).

{% multi_lang_include alerts/early_access_beta_alert.md feature='Audience Sync to LinkedIn' type='beta' %}

## Conditions préalables {#prerequisites}

Vous devez vous assurer que les éléments suivants ont été créés, complétés ou acceptés avant de configurer votre étape de synchronisation de l'audience avec LinkedIn dans Canvas.

| Condition | Origine | Description |
| --- | --- | --- |
| Compte publicitaire LinkedIn | [LinkedIn](https://www.linkedin.com/campaignmanager) | Un compte publicitaire LinkedIn actif lié à votre marque.<br><br>Assurez-vous que vous avez accepté toutes les conditions générales pertinentes de LinkedIn pour accéder à ce compte et l'utiliser, et que votre administrateur LinkedIn vous a accordé les autorisations appropriées pour gérer les audiences. |
| Conditions d'utilisation et politiques de LinkedIn | LinkedIn | Accepter de se conformer à l'ensemble des conditions, politiques, directives et documents requis par LinkedIn liés à votre utilisation de la synchronisation d'audience avec LinkedIn, y compris les conditions, politiques, directives et documents incorporés par référence, qui peuvent inclure, dans le cadre de LinkedIn : les conditions d'utilisation des services, l'accord sur les publicités, l'accord sur le traitement des données et les directives pour la communauté professionnelle. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Se connecter à LinkedIn {#step-1-connect-to-linkedin}

{% alert important %}
Vous devez disposer de l'[autorisation « Admin »]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) pour connecter LinkedIn à votre compte Braze.
{% endalert %}

Dans le tableau de bord de Braze, accédez à **Partenaires technologiques** et sélectionnez **LinkedIn**. Dans la section **LinkedIn Audience Sync**, sélectionnez **Connect LinkedIn**.

![La page technologique LinkedIn dans Braze comprend une section Aperçu et une section LinkedIn Audience Sync avec le bouton Connect LinkedIn.]({% image_buster /assets/img/linkedin/linkedin3.png %}){: style="max-width:75%;"}

Vous serez ensuite redirigé vers la page OAuth de LinkedIn pour autoriser Braze concernant les autorisations liées à votre intégration de synchronisation d'audience. Après avoir sélectionné **Confirm**, vous serez redirigé dans Braze pour sélectionner les comptes publicitaires LinkedIn avec lesquels vous souhaitez vous synchroniser.

![« Braze Self Service » est sélectionné comme compte publicitaire à connecter.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

Une fois la connexion établie, vous serez renvoyé à la page partenaire, où vous pourrez voir quels comptes sont connectés et déconnecter les comptes existants.

![Un compte LinkedIn connecté avec succès.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

Votre connexion LinkedIn sera appliquée au niveau de l'espace de travail Braze. Si votre administrateur LinkedIn vous supprime de votre compte publicitaire LinkedIn, Braze détectera un jeton non valide. Par conséquent, vos Canvas actifs utilisant LinkedIn afficheront des erreurs, et Braze ne sera pas en mesure de synchroniser les utilisateurs.

### Étape 2 : Configurer vos critères d'entrée Canvas {#step-2-configure-your-canvas-entry-criteria}

Lorsque vous créez des audiences pour le suivi publicitaire, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et vous conformer aux lois sur la protection de la vie privée, telles que le droit « Ne pas vendre ou partager » en vertu de la [CCPA](https://oag.ca.gov/privacy/ccpa). Les marketeurs devraient implémenter les filtres pertinents pour l'éligibilité des utilisateurs dans leurs critères d'entrée Canvas. Voici quelques options possibles.

Si vous avez collecté l'[IDFA iOS via le SDK Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewother_sdk_customizations#optional-idfa-collection), vous pourrez utiliser le filtre **Ads Tracking Enabled**. Sélectionnez la valeur `true` afin d'envoyer uniquement les utilisateurs vers les destinations de synchronisation d'audience où ils ont donné leur consentement.

![Une audience d'entrée avec le filtre « Ad Tracking Enabled is true ».]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

Si vous collectez `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, ou tout autre attribut personnalisé pertinent, vous devez les inclure dans les critères d'entrée de votre Canvas en tant que filtre :

![Un Canvas dont l'audience d'entrée est « opted_in_marketing » égal à « true ».]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Pour en savoir plus sur la manière de se conformer à ces lois sur la protection des données au sein de la plateforme Braze, consultez l'[Assistance technique à la protection des données]({{site.baseurl}}/dp-technical-assistance).

### Étape 3 : Ajouter une étape de synchronisation de l'audience avec LinkedIn {#step-3-add-an-audience-sync-step-with-linkedin}

Ajoutez un composant dans votre Canvas et sélectionnez Audience Sync. Cliquez sur le bouton **Custom Audience** pour ouvrir l'éditeur de composants.

![L'éditeur Canvas avec la liste des composants disponibles.]({% image_buster /assets/img/linkedin/linkedin2.png %}){: style="max-width:35%;"} ![Le composant Audience Sync sélectionné.]({% image_buster /assets/img/linkedin/linkedin1.png %}){: style="max-width:29%;"}

### Étape 4 : Configurer la synchronisation {#step-4-sync-setup}

Sélectionnez **LinkedIn** comme partenaire souhaité pour la synchronisation d'audience.

![Les détails de la configuration de la synchronisation de l'audience avec les multiples partenaires à choisir.]({% image_buster /assets/img/linkedin/linkedin.png %}){: style="max-width:70%;"}

Sélectionnez ensuite le compte publicitaire LinkedIn souhaité. Dans la liste déroulante **Choose a New or Existing Audience**, saisissez le nom d'une audience nouvelle ou existante.

![Synchronisation de l'audience sur LinkedIn avec Braze sélectionné comme compte publicitaire.]({% image_buster /assets/img/linkedin/linkedin20.png %})

{% tabs %}
{% tab Créer une nouvelle audience %}

**Créer une nouvelle audience**<br>
Saisissez un nom pour la nouvelle audience, sélectionnez **Add Users to Audience** et sélectionnez les champs que vous souhaitez synchroniser avec LinkedIn. Pour cette intégration, nous prenons actuellement en charge les éléments suivants :
- E-mail
- Nom et prénom
- GAID Android

Ensuite, enregistrez votre audience en cliquant sur le bouton **Create Audience** en bas de l'éditeur d'étape.

![Un exemple d'audience « leads » avec le compte publicitaire Braze sélectionné, l'audience « leads », l'action pour ajouter des utilisateurs à l'audience, et l'e-mail, le GAID Android, et le nom et le prénom comme champs à faire correspondre.]({% image_buster /assets/img/linkedin/linkedin10.png %})

Braze affiche une notification en haut de l'éditeur d'étape si l'audience est créée avec succès ou si des erreurs surviennent. Les utilisateurs peuvent faire référence à cette audience pour la suppression d'utilisateurs plus tard dans le parcours Canvas, car l'audience a été créée en mode brouillon.

![Confirmation de la création de l'audience « leads ».]({% image_buster /assets/img/linkedin/linkedin9.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze synchronise les utilisateurs quasiment en temps réel lorsqu'ils entrent dans le composant de synchronisation de l'audience.

{% endtab %}
{% tab Synchroniser avec une audience existante %}

**Synchroniser avec une audience existante**<br>
Braze offre également la possibilité d'ajouter des utilisateurs à des audiences LinkedIn existantes afin de confirmer que ces audiences sont à jour. Pour synchroniser avec une audience existante, saisissez le nom de l'audience dans le menu déroulant et choisissez **Add to the Audience**. Braze ajoutera ensuite des utilisateurs en temps quasi réel au fur et à mesure qu'ils entreront dans le composant Audience Sync.

![Vue élargie de l'étape Canvas de l'audience personnalisée. Le compte publicitaire souhaité et l'audience existante sont sélectionnés ici.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### Étape 5 : Lancer le Canvas {#step-5-launch-canvas}

Une fois que vous avez configuré votre synchronisation d'audience avec LinkedIn, il vous suffit de lancer le Canvas ! La nouvelle audience sera créée, et les utilisateurs qui passent par l'étape de synchronisation de l'audience seront transférés dans cette audience sur LinkedIn. Si votre Canvas contient des composants subséquents, vos utilisateurs passeront à l'étape suivante de leur parcours utilisateur.

Vous pouvez consulter l'audience sur LinkedIn en accédant à votre compte publicitaire et en sélectionnant **Audiences** dans la section **Assets** de la navigation. À partir de la page **Audiences**, vous pouvez voir la taille de chaque audience après avoir atteint plus de 300 membres.

![Page LinkedIn présentant les indicateurs suivants pour l'audience donnée.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## Considérations relatives à la synchronisation des utilisateurs et à la limite de débit {#user-syncing-and-rate-limit-considerations}

Lorsque les utilisateurs atteignent l'étape de synchronisation de l'audience, Braze les synchronise quasiment en temps réel tout en respectant les limites de débit de l'API de LinkedIn. Braze met en lots et traite autant d'utilisateurs que possible toutes les 5 secondes avant de les envoyer à LinkedIn.

La limite de débit de l'API de LinkedIn n'autorise pas plus de dix requêtes par seconde et 100 000 utilisateurs par demande. Si un client atteint cette limite, Braze relance la synchronisation pour une durée maximale d'environ 13 heures. Si la synchronisation n'est toujours pas possible, Braze répertorie ces utilisateurs sous l'indicateur Users Errored.

## Comprendre les analyses {#understanding-analytics}

Le tableau suivant contient des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses de votre composant de synchronisation de l'audience.

| Indicateur | Description |
| ------ | ----------- |
| Entered | Nombre d'utilisateurs ayant entré ce composant pour être synchronisés avec LinkedIn. |
| Proceeded to Next Step | Nombre d'utilisateurs passés au composant suivant s'il y en a un. Tous les utilisateurs avanceront automatiquement si c'est la dernière étape de la branche Canvas. |
| Users Synced | Nombre d'utilisateurs qui ont été synchronisés avec succès sur LinkedIn. |
| Users Not Synced | Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants. |
| Users Pending | Nombre d'utilisateurs actuellement traités par Braze en vue d'une synchronisation avec LinkedIn. |
| Users Errored | Nombre d'utilisateurs qui n'ont pas été synchronisés avec LinkedIn en raison d'une erreur de l'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton LinkedIn non valide ou la suppression de l'audience dans LinkedIn. |
| Exited Canvas | Nombre d'utilisateurs ayant quitté le Canvas. Cela se produit lorsque la dernière étape d'un Canvas est un composant de synchronisation d'audience. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprendre les analyses" }

{% alert important %}
N'oubliez pas que les indicateurs relatifs aux utilisateurs synchronisés et aux utilisateurs en erreur sont retardés en raison de la vidange en masse et de la relance après 13 heures, respectivement.
{% endalert %}

{% alert important %}
LinkedIn fournit des indicateurs supplémentaires concernant les taux de correspondance au sein de sa plateforme. Pour examiner la correspondance de votre synchronisation d'audience spécifique, sélectionnez les indicateurs de l'étape de synchronisation d'audience pour accéder à la page **Canvas Step Details**.
<br><br>
Sélectionnez le partenaire **LinkedIn**, votre compte publicitaire et l'audience pour voir la taille de l'audience et le taux de correspondance de LinkedIn.

![Exemple d'indicateurs d'étape d'Audience Sync avec 10 000 utilisateurs entrés.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## Foire aux questions {#frequently-asked-questions}

### Combien de temps faudra-t-il pour que les tailles d'audience s'affichent dans LinkedIn ? {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

L'affichage des audiences dans votre compte LinkedIn peut prendre jusqu'à 48 heures.

### Quelle est la taille minimale de l'audience pour que LinkedIn la renseigne dans votre compte publicitaire ? {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

L'audience doit compter au moins 300 membres pour que la taille de l'audience s'affiche dans votre compte LinkedIn.

### Que dois-je faire ensuite si je reçois une erreur de jeton non valide ? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Vous pouvez déconnecter et reconnecter votre compte LinkedIn sur la page partenaire LinkedIn. Confirmez auprès de votre administrateur LinkedIn que vous disposez des autorisations appropriées pour le compte publicitaire avec lequel vous souhaitez vous synchroniser.

### Pourquoi mon Canvas n'est-il pas autorisé à être lancé ? {#why-is-my-canvas-not-allowed-to-launch}

Confirmez que votre compte publicitaire LinkedIn s'est bien connecté à Braze sur la page partenaire LinkedIn. Ensuite, assurez-vous d'avoir sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience et sélectionné les champs à faire correspondre.

### Comment puis-je savoir si les utilisateurs ont été mis en correspondance après les avoir transmis à LinkedIn ? {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

LinkedIn fournit des informations sur les taux de correspondance dans son tableau de bord. Vous pouvez consulter ces informations dans LinkedIn dans la section **Audiences**. Vous pouvez consulter le taux de correspondance de votre audience LinkedIn dans les détails de l'étape Canvas de votre étape de synchronisation de l'audience.

### Combien d'audiences LinkedIn peut-il prendre en charge ? {#how-many-audiences-can-linkedin-support}

Actuellement, il n'y a pas de limite au nombre d'audiences dans votre compte publicitaire LinkedIn.

### Pourquoi un segment est-il bloqué à l'état BUILDING et n'est-il pas mis à jour ? {#why-is-a-segment-stuck-in-building-status-and-not-updated}

Un segment est considéré comme inutilisé et passe à l'état ARCHIVED lorsqu'il n'a pas été utilisé de manière continue pendant 30 jours dans une campagne provisoire ou active. Pour cette raison, un segment peut sembler « bloqué » dans la phase de BUILDING lorsque des mises à jour sont envoyées à un segment ARCHIVED, le poussant ainsi dans l'état BUILDING, et juste avant qu'il ne soit à nouveau archivé, de nouvelles mises à jour sont envoyées au segment inutilisé.