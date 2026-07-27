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

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

Cette fonctionnalité permet aux marques de contrôler quelles données first-party spécifiques sont partagées avec LinkedIn. Chez Braze, les intégrations avec lesquelles vous pouvez et ne pouvez pas partager vos données first-party sont considérées avec le plus grand sérieux. Pour plus d'informations, consultez notre [politique de confidentialité](https://www.braze.com/privacy).

{% multi_lang_include alerts/early_access_beta_alert.md feature='Audience Sync to LinkedIn' type='beta' %}

## Prérequis {#prerequisites}

Vous devez vous assurer que les éléments suivants ont été créés, complétés ou acceptés avant de configurer votre étape de synchronisation d'audience LinkedIn dans Canvas.

| Exigence | Origine | Description |
| --- | --- | --- |
| Compte publicitaire LinkedIn | [LinkedIn](https://www.linkedin.com/campaignmanager) | Un compte publicitaire LinkedIn actif lié à votre marque.<br><br>Assurez-vous d'avoir accepté toutes les conditions générales LinkedIn pertinentes pour accéder à ce compte et l'utiliser, et que votre administrateur LinkedIn vous a accordé les autorisations appropriées pour gérer les audiences. |
| Conditions et politiques LinkedIn | LinkedIn | Acceptez de vous conformer à l'ensemble des conditions, politiques, directives et documents requis par LinkedIn en lien avec votre utilisation de la synchronisation d'audience LinkedIn, y compris toutes les conditions, politiques, directives et documents incorporés par référence, qui peuvent inclure les éléments suivants de LinkedIn : les conditions d'utilisation des services, l'accord publicitaire, l'accord de traitement des données et les directives de la communauté professionnelle. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Se connecter à LinkedIn {#step-1-connect-to-linkedin}

{% alert important %}
Vous devez disposer de la [permission « Admin »]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) pour connecter LinkedIn à votre compte Braze.
{% endalert %}

Dans le tableau de bord de Braze, accédez à **Technology Partners** et sélectionnez **LinkedIn**. Dans la section **LinkedIn Audience Sync**, sélectionnez **Connect LinkedIn**.

![La page technologique LinkedIn dans Braze comprend une section Aperçu et une section LinkedIn Audience Sync avec le bouton Connect LinkedIn.]({% image_buster /assets/img/linkedin/linkedin3.png %}){: style="max-width:75%;"}

Vous serez alors redirigé vers la page OAuth de LinkedIn pour autoriser Braze à accéder aux permissions liées à votre intégration Audience Sync. Après avoir sélectionné **Confirm**, vous serez redirigé vers Braze pour sélectionner les comptes publicitaires LinkedIn que vous souhaitez synchroniser.

![« Braze Self Service » est sélectionné comme compte publicitaire à connecter.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

Une fois la connexion établie, vous serez renvoyé à la page partenaire, où vous pourrez voir quels comptes sont connectés et déconnecter les comptes existants.

![Un compte LinkedIn connecté avec succès.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

Votre connexion LinkedIn sera appliquée au niveau de l'espace de travail Braze. Si votre administrateur LinkedIn vous retire de votre compte publicitaire LinkedIn, Braze détectera un jeton invalide. Par conséquent, vos Canvas actifs utilisant LinkedIn afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs.

### Étape 2 : Configurer vos critères d'entrée dans le Canvas {#step-2-configure-your-canvas-entry-criteria}

Lors de la création d'audiences pour le suivi publicitaire, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et pour vous conformer aux lois sur la protection de la vie privée, telles que le droit de « Ne pas vendre ou partager » en vertu du [CCPA](https://oag.ca.gov/privacy/ccpa). Les marketeurs doivent implémenter les filtres pertinents pour l'éligibilité des utilisateurs dans leurs critères d'entrée du Canvas. Les options suivantes peuvent vous aider.

Si vous avez collecté l'[IDFA iOS via le SDK Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection), vous pourrez utiliser le filtre **Ads Tracking Enabled**. Sélectionnez la valeur `true` pour n'envoyer que les utilisateurs ayant donné leur consentement vers les destinations Audience Sync.

![Une audience d'entrée avec le filtre « Ad Tracking Enabled is true ».]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

Si vous collectez des `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, ou tout autre attribut personnalisé pertinent, vous devez les inclure dans vos critères d'entrée du Canvas en tant que filtre :

![Un Canvas avec une audience d'entrée où « opted_in_marketing » est égal à « true ».]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Pour en savoir plus sur la conformité à ces lois de protection des données au sein de la plateforme Braze, consultez l'[Assistance technique pour la protection des données]({{site.baseurl}}/dp-technical-assistance).

### Étape 3 : Ajouter une étape Audience Sync avec LinkedIn {#step-3-add-an-audience-sync-step-with-linkedin}

Ajoutez un composant dans votre Canvas et sélectionnez Audience Sync. Cliquez sur le bouton **Custom Audience** pour ouvrir l'éditeur de composant.

![L'éditeur de Canvas avec la liste des composants disponibles.]({% image_buster /assets/img/linkedin/linkedin2.png %}){: style="max-width:35%;"} ![Le composant Audience Sync sélectionné.]({% image_buster /assets/img/linkedin/linkedin1.png %}){: style="max-width:29%;"}

### Étape 4 : Configuration de la synchronisation {#step-4-sync-setup}

Sélectionnez **LinkedIn** comme partenaire Audience Sync souhaité.

![Les détails de « Set up Audience Sync » avec les différents partenaires disponibles.]({% image_buster /assets/img/linkedin/linkedin.png %}){: style="max-width:70%;"}

Sélectionnez ensuite le compte publicitaire LinkedIn souhaité. Dans le menu déroulant **Choose a New or Existing Audience**, saisissez le nom d'une audience nouvelle ou existante.

![Audience Sync vers LinkedIn avec Braze sélectionné comme compte publicitaire.]({% image_buster /assets/img/linkedin/linkedin20.png %})

{% tabs %}
{% tab Créer une nouvelle audience %}

**Créer une nouvelle audience**<br>
Saisissez un nom pour la nouvelle audience, sélectionnez **Add Users to Audience**, et choisissez les champs que vous souhaitez synchroniser avec LinkedIn. Pour cette intégration, nous prenons actuellement en charge les éléments suivants :
- E-mail
- Prénom et nom
- Android GAID

Ensuite, enregistrez votre audience en cliquant sur le bouton **Create Audience** en bas de l'éditeur d'étape.

![Un exemple d'audience « leads » avec le compte publicitaire Braze sélectionné, l'audience « leads », l'action d'ajouter des utilisateurs à l'audience, et l'e-mail, l'Android GAID, le prénom et le nom comme champs de correspondance.]({% image_buster /assets/img/linkedin/linkedin10.png %})

Braze affiche une notification en haut de l'éditeur d'étape si l'audience est créée avec succès ou si des erreurs surviennent. Les utilisateurs peuvent référencer cette audience pour la suppression d'utilisateurs plus tard dans le parcours Canvas, car l'audience a été créée en mode brouillon.

![Confirmation que l'audience « leads » a été créée.]({% image_buster /assets/img/linkedin/linkedin9.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze synchronise les utilisateurs en quasi temps réel à mesure qu'ils entrent dans le composant Audience Sync.

{% endtab %}
{% tab Synchroniser avec une audience existante %}

**Synchroniser avec une audience existante**<br>
Braze offre également la possibilité d'ajouter des utilisateurs à des audiences LinkedIn existantes pour s'assurer qu'elles sont à jour. Pour synchroniser avec une audience existante, saisissez le nom de l'audience existante dans le menu déroulant et sélectionnez **Add to the Audience**. Braze ajoutera alors les utilisateurs en quasi temps réel à mesure qu'ils entrent dans le composant Audience Sync.

![Vue étendue de l'étape Custom Audience du Canvas. Le compte publicitaire souhaité et l'audience existante sont sélectionnés ici.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### Étape 5 : Lancer le Canvas {#step-5-launch-canvas}

Après avoir configuré votre Audience Sync vers LinkedIn, lancez le Canvas ! La nouvelle audience est créée, et les utilisateurs qui passent par l'étape Audience Sync sont ajoutés à cette audience sur LinkedIn. Si votre Canvas contient des composants ultérieurs, vos utilisateurs progressent vers l'étape suivante de leur parcours utilisateur.

Vous pouvez consulter l'audience sur LinkedIn en accédant à votre compte publicitaire et en sélectionnant **Audiences** dans la section **Assets** de la navigation. Depuis la page **Audiences**, vous pouvez voir la taille de chaque audience après avoir atteint plus de 300 membres.

![Page LinkedIn listant les indicateurs suivants pour l'audience donnée.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## Synchronisation des utilisateurs et considérations relatives aux limites de débit {#user-syncing-and-rate-limit-considerations}

Lorsque les utilisateurs atteignent l'étape Audience Sync, Braze les synchronise en quasi temps réel tout en respectant les limites de débit de l'API de LinkedIn. Braze regroupe et traite autant d'utilisateurs que possible toutes les 5 secondes avant de les envoyer à LinkedIn.

La limite de débit de l'API de LinkedIn n'autorise pas plus de dix requêtes par seconde et 100 000 utilisateurs par requête. Si un client atteint cette limite, Braze retente la synchronisation pendant environ 13 heures. Si la synchronisation n'est toujours pas possible, Braze répertorie ces utilisateurs dans l'indicateur Users Errored.

## Comprendre l'analyse {#understanding-analytics}

Le tableau suivant présente les indicateurs et descriptions pour vous aider à mieux comprendre l'analyse de votre composant Audience Sync.

| INDICATEUR | DESCRIPTION |
| ------ | ----------- |
| Entrés | Nombre d'utilisateurs qui sont entrés dans ce composant pour être synchronisés avec LinkedIn. |
| Passés à l'étape suivante | Combien d'utilisateurs ont avancé vers le composant suivant s'il y en a un ? Tous les utilisateurs avanceront automatiquement s'il s'agit de la dernière étape de la branche du Canvas. |
| Utilisateurs synchronisés | Nombre d'utilisateurs qui ont été synchronisés avec succès vers LinkedIn. |
| Utilisateurs non synchronisés | Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants pour la correspondance. |
| Utilisateurs en attente | Nombre d'utilisateurs actuellement en cours de traitement par Braze pour la synchronisation vers LinkedIn. |
| Utilisateurs en erreur | Nombre d'utilisateurs qui n'ont pas été synchronisés vers LinkedIn en raison d'une erreur d'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton LinkedIn invalide ou la suppression de l'audience sur LinkedIn. |
| Sortis du Canvas | Nombre d'utilisateurs qui sont sortis du Canvas. Cela se produit lorsque la dernière étape d'un Canvas est un composant Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprendre l'analyse" }

{% alert important %}
N'oubliez pas qu'il y aura un délai dans le reporting pour les indicateurs d'utilisateurs synchronisés et d'utilisateurs en erreur, en raison respectivement du vidage en masse et des 13 heures de tentatives.
{% endalert %}

{% alert important %}
LinkedIn fournit des indicateurs supplémentaires concernant les taux de correspondance au sein de sa plateforme. Pour consulter la correspondance de votre Audience Sync spécifique, sélectionnez les indicateurs de l'étape Audience Sync pour accéder à la page **Détails de l'étape du Canvas**.
<br><br>
Sélectionnez le partenaire **LinkedIn**, votre compte publicitaire et l'audience pour voir la taille de l'audience et le taux de correspondance depuis LinkedIn.

![Un exemple d'indicateurs de l'étape Audience Sync avec 10 000 utilisateurs entrés.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## Questions fréquemment posées {#frequently-asked-questions}

### Combien de temps faut-il pour que les tailles d'audience s'affichent dans LinkedIn ? {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

Il peut y avoir un délai allant jusqu'à 48 heures pour visualiser les audiences dans votre compte LinkedIn.

### Quelle est la taille minimale d'audience pour que LinkedIn l'affiche dans votre compte publicitaire ? {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

L'audience doit comprendre au moins 300 membres pour que la taille de l'audience s'affiche dans votre compte LinkedIn.

### Que dois-je faire si je reçois une erreur de jeton invalide ? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Vous pouvez déconnecter et reconnecter votre compte LinkedIn sur la page partenaire LinkedIn. Confirmez auprès de votre administrateur LinkedIn que vous disposez des autorisations appropriées pour le compte publicitaire avec lequel vous souhaitez synchroniser.

### Pourquoi mon Canvas ne peut-il pas être lancé ? {#why-is-my-canvas-not-allowed-to-launch}

Vérifiez que votre compte publicitaire LinkedIn a été connecté avec succès à Braze sur la page partenaire LinkedIn. Ensuite, assurez-vous d'avoir sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience et sélectionné les champs à faire correspondre.

### Comment savoir si des utilisateurs ont été mis en correspondance après avoir transmis des utilisateurs à LinkedIn ? {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

LinkedIn fournit des informations sur les taux de correspondance dans son tableau de bord. Vous pouvez les consulter sur LinkedIn dans la section **Audiences**. Vous pouvez vérifier le taux de correspondance de votre audience LinkedIn dans les détails de l'étape Canvas de votre étape Audience Sync.

### Combien d'audiences LinkedIn peut-il prendre en charge ? {#how-many-audiences-can-linkedin-support}

Actuellement, il n'y a pas de limite au nombre d'audiences dans votre compte publicitaire LinkedIn.

### Pourquoi un segment est-il bloqué au statut BUILDING et ne se met-il pas à jour ? {#why-is-a-segment-stuck-in-building-status-and-not-updated}

Un segment est considéré comme inutilisé et passe au statut ARCHIVED lorsqu'il n'est pas utilisé de manière continue pendant 30 jours dans une campagne brouillon ou active. De ce fait, un segment peut sembler « bloqué » au statut BUILDING lorsque des mises à jour sont transmises à un segment ARCHIVED, le faisant passer à l'état BUILDING, et juste avant qu'il ne soit à nouveau archivé, de nouvelles mises à jour sont transmises au segment inutilisé.