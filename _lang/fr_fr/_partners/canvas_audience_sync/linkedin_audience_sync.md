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

## Prérequis {#prerequisites}

Vous devez vous assurer que les éléments suivants ont été créés, complétés ou acceptés avant de configurer votre étape de synchronisation d'audience LinkedIn dans Canvas.

| Condition | Origine | Description |
| --- | --- | --- |
| Audience Sync Pro | Braze | LinkedIn est un partenaire [Audience Sync Pro]({{site.baseurl}}/partners/canvas_audience_sync/overview#audience-sync-pro). Sélectionnez LinkedIn dans vos attributions Audience Sync Pro sur la page **Technology Partners** avant de connecter un compte publicitaire. Contactez votre gestionnaire de compte Braze pour obtenir des détails sur l'achat. |
| Compte publicitaire LinkedIn | [LinkedIn](https://www.linkedin.com/campaignmanager) | Un compte publicitaire LinkedIn actif lié à votre marque.<br><br>Assurez-vous d'avoir accepté toutes les conditions générales LinkedIn pertinentes pour accéder à ce compte et l'utiliser. Votre administrateur LinkedIn doit vous attribuer l'un des rôles suivants sur le compte publicitaire : Account Billing Admin, Account Manager, Campaign Manager ou Creative Manager. |
| Conditions et politiques LinkedIn | LinkedIn | Vous acceptez de respecter l'ensemble des conditions, politiques, directives et documents requis par LinkedIn en lien avec votre utilisation de la synchronisation d'audience LinkedIn, y compris toutes les conditions, politiques, directives et documents intégrés par référence, qui peuvent inclure les éléments suivants de LinkedIn : les conditions d'utilisation des services, l'accord publicitaire, l'accord de traitement des données et les directives de la communauté professionnelle. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Se connecter à LinkedIn {#step-1-connect-to-linkedin}

{% alert important %}
Vous devez disposer de la [permission « Admin »]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) pour connecter LinkedIn à votre compte Braze.
{% endalert %}

Dans le tableau de bord de Braze, accédez à **Partenaires technologiques** et sélectionnez **LinkedIn**. Dans la section **LinkedIn Audience Sync**, sélectionnez **Connect LinkedIn**.

Vous êtes alors redirigé vers la page OAuth de LinkedIn pour autoriser Braze à accéder aux permissions liées à votre intégration Audience Sync. Après avoir sélectionné **Confirm**, vous êtes redirigé vers Braze pour sélectionner les comptes publicitaires LinkedIn que vous souhaitez synchroniser.

![« Braze Self Service » est sélectionné comme compte publicitaire à connecter.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

Lorsque la connexion est établie avec succès, vous êtes renvoyé vers la page partenaire, où vous pouvez voir quels comptes sont connectés et déconnecter les comptes existants.

![Un compte LinkedIn connecté avec succès.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

Votre connexion LinkedIn est appliquée au niveau de l'espace de travail Braze. Si votre administrateur LinkedIn vous retire de votre compte publicitaire LinkedIn, Braze détecte un jeton invalide. Par conséquent, vos Canvas actifs utilisant LinkedIn affichent des erreurs, et Braze ne peut pas synchroniser les utilisateurs.

### Étape 2 : Configurer vos critères d'entrée dans le Canvas {#step-2-configure-your-canvas-entry-criteria}

Lors de la création d'audiences pour le suivi publicitaire, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et pour vous conformer aux lois sur la protection de la vie privée, telles que le droit de « ne pas vendre ou partager » en vertu du [CCPA](https://oag.ca.gov/privacy/ccpa). Les marketeurs doivent implémenter les filtres pertinents pour l'éligibilité des utilisateurs dans leurs critères d'entrée dans le Canvas. Les options suivantes peuvent vous aider.

Si vous avez collecté l'[IDFA iOS via le SDK Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection), vous pouvez utiliser le filtre **Ads Tracking Enabled**. Sélectionnez la valeur `true` pour n'envoyer que les utilisateurs ayant donné leur consentement vers les destinations Audience Sync. Les identifiants publicitaires iOS ne sont pas pris en charge comme champs de correspondance pour LinkedIn Audience Sync.

![Une audience d'entrée avec le filtre « Ad Tracking Enabled is true ».]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

Si vous collectez des `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, ou tout autre attribut personnalisé pertinent, vous devez les inclure dans vos critères d'entrée dans le Canvas en tant que filtre :

![Un Canvas avec une audience d'entrée où « opted_in_marketing » est égal à « true ».]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Pour en savoir plus sur la conformité à ces lois sur la protection des données au sein de la plateforme Braze, consultez l'[Assistance technique relative à la protection des données]({{site.baseurl}}/dp-technical-assistance).

### Étape 3 : Ajouter une étape Audience Sync avec LinkedIn {#step-3-add-an-audience-sync-step-with-linkedin}

Ajoutez un composant dans votre Canvas et sélectionnez Audience Sync. Cliquez sur le bouton **Custom Audience** pour ouvrir l'éditeur de composant.

### Étape 4 : Configuration de la synchronisation {#step-4-sync-setup}

1. Sélectionnez **LinkedIn** comme partenaire Audience Sync souhaité.
2. Sélectionnez le compte publicitaire LinkedIn souhaité.
3. Sous le menu déroulant **Choose a New or Existing Audience**, saisissez le nom d'une nouvelle audience ou d'une audience existante.

{% tabs %}
{% tab Créer une nouvelle audience %}

#### Créer une nouvelle audience {#create-a-new-audience}

Saisissez un nom pour la nouvelle audience, sélectionnez **Add Users to Audience**, et choisissez les champs que vous souhaitez synchroniser avec LinkedIn. Pour cette intégration, Braze prend actuellement en charge les éléments suivants :
- E-mail
- Prénom et nom (les deux sont obligatoires lorsque vous utilisez la correspondance par nom)
- Android GAID

Les identifiants publicitaires iOS ne sont pas pris en charge comme champs de correspondance pour LinkedIn.

Ensuite, enregistrez votre audience en cliquant sur le bouton **Create Audience** en bas de l'éditeur d'étape.

![Un exemple d'audience « leads » avec le compte publicitaire Braze sélectionné, l'audience « leads », l'action d'ajouter des utilisateurs à l'audience, et l'e-mail, l'Android GAID ainsi que le prénom et le nom comme champs de correspondance.]({% image_buster /assets/img/linkedin/linkedin10.png %})

Braze affiche une notification en haut de l'éditeur d'étape si l'audience est créée avec succès ou si des erreurs surviennent. Vous pouvez utiliser cette audience pour retirer des utilisateurs ultérieurement dans le parcours Canvas après l'avoir enregistrée dans l'éditeur d'étape.

![Confirmation que l'audience « leads » a été créée.]({% image_buster /assets/img/linkedin/linkedin9.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze synchronise les utilisateurs au fur et à mesure qu'ils entrent dans l'étape Audience Sync, sous réserve du [traitement par lots et de la latence]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency).

{% endtab %}
{% tab Synchroniser avec une audience existante %}

#### Synchroniser avec une audience existante {#sync-with-an-existing-audience}

Braze offre également la possibilité d'ajouter ou de retirer des utilisateurs d'audiences LinkedIn existantes afin de confirmer que ces audiences sont à jour. Pour synchroniser avec une audience existante, saisissez le nom de l'audience existante dans le menu déroulant, puis choisissez **Add to the Audience** ou **Remove from the Audience**. Braze synchronise les utilisateurs au fur et à mesure qu'ils entrent dans l'étape Audience Sync, sous réserve du [traitement par lots et de la latence]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency).

![Vue étendue de l'étape Canvas Custom Audience. Le compte publicitaire souhaité et l'audience existante sont sélectionnés ici.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### Étape 5 : Lancer le Canvas {#step-5-launch-canvas}

Après avoir configuré votre Audience Sync vers LinkedIn, lancez le Canvas ! La nouvelle audience est créée et les utilisateurs qui passent par l'étape Audience Sync sont transmis à cette audience sur LinkedIn. Si votre Canvas contient des composants suivants, vos utilisateurs avancent à l'étape suivante de leur parcours utilisateur.

Vous pouvez consulter l'audience sur LinkedIn en accédant à votre compte publicitaire et en sélectionnant **Audiences** sous la section **Assets** de la navigation. Depuis la page **Audiences**, vous pouvez voir la taille de chaque audience après avoir atteint plus de 300 membres.

![Page LinkedIn listant les indicateurs suivants pour l'audience donnée.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## Synchronisation des utilisateurs et considérations sur les limites de débit {#user-syncing-and-rate-limit-considerations}

Lorsque les utilisateurs atteignent l'étape Audience Sync, Braze les place en file d'attente pour le traitement par lots avant de les envoyer à LinkedIn. Consultez [Traitement par lots et latence]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency) pour savoir comment Braze envoie les lots.

Braze envoie jusqu'à 2 000 utilisateurs par requête à LinkedIn. Si les limites de débit de l'API de LinkedIn s'appliquent à votre compte, Braze relance la synchronisation pendant environ 13 heures. Si la synchronisation reste impossible, Braze répertorie ces utilisateurs sous l'indicateur Users Errored.

## Comprendre l'analytique {#understanding-analytics}

Le tableau suivant présente les indicateurs et descriptions pour vous aider à mieux comprendre l'analytique de votre composant Audience Sync.

| INDICATEUR | DESCRIPTION |
| ------ | ----------- |
| Entrés | Nombre d'utilisateurs qui sont entrés dans ce composant pour être synchronisés vers LinkedIn. |
| Passés à l'étape suivante | Combien d'utilisateurs ont avancé vers le composant suivant s'il y en a un ? Tous les utilisateurs avancent automatiquement s'il s'agit de la dernière étape dans la branche du Canvas. |
| Utilisateurs synchronisés | Nombre d'utilisateurs qui ont été synchronisés avec succès vers LinkedIn. |
| Utilisateurs non synchronisés | Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants pour la correspondance. |
| Utilisateurs en attente | Nombre d'utilisateurs en cours de traitement par Braze pour la synchronisation vers LinkedIn. |
| Utilisateurs en erreur | Nombre d'utilisateurs qui n'ont pas été synchronisés vers LinkedIn en raison d'une erreur d'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton LinkedIn invalide ou si l'audience a été supprimée sur LinkedIn. |
| Sortis du Canvas | Nombre d'utilisateurs qui sont sortis du Canvas. Cela se produit lorsque la dernière étape d'un Canvas est un composant Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprendre l'analytique" }

{% alert important %}
N'oubliez pas qu'il y a un délai dans le reporting des indicateurs d'utilisateurs synchronisés et d'utilisateurs en erreur en raison du traitement par lots et des 13 heures de tentatives, respectivement.
{% endalert %}

{% alert important %}
LinkedIn fournit des indicateurs supplémentaires concernant les taux de correspondance au sein de sa plateforme. Pour consulter la correspondance de votre Audience Sync spécifique, sélectionnez les indicateurs de l'étape Audience Sync pour accéder à la page **Détails de l'étape du Canvas**.
<br><br>
Sélectionnez le partenaire **LinkedIn**, votre compte publicitaire et l'audience pour voir la taille de l'audience et le taux de correspondance depuis LinkedIn.

![Un exemple d'indicateurs de l'étape Audience Sync avec 10 000 utilisateurs entrés.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## Questions fréquemment posées {#frequently-asked-questions}

### Combien de temps faut-il pour que les tailles d'audience soient renseignées dans LinkedIn ? {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

Il peut y avoir un délai allant jusqu'à 48 heures avant de pouvoir visualiser les audiences dans votre compte LinkedIn.

### Quelle est la taille minimale d'audience pour que LinkedIn la renseigne dans votre compte publicitaire ? {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

L'audience doit comprendre au moins 300 membres pour que la taille de l'audience soit renseignée dans votre compte LinkedIn.

### Que dois-je faire si je reçois une erreur de jeton invalide ? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Vous pouvez déconnecter puis reconnecter votre compte LinkedIn sur la page partenaire LinkedIn. Vérifiez auprès de votre administrateur LinkedIn que vous disposez des autorisations appropriées pour le compte publicitaire avec lequel vous souhaitez synchroniser.

### Pourquoi mon Canvas ne peut-il pas être lancé ? {#why-is-my-canvas-not-allowed-to-launch}

Vérifiez que votre compte publicitaire LinkedIn a été connecté avec succès à Braze sur la page partenaire LinkedIn. Ensuite, assurez-vous d'avoir sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience et sélectionné les champs à faire correspondre.

### Comment savoir si des utilisateurs ont été mis en correspondance après les avoir transmis à LinkedIn ? {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

LinkedIn fournit des informations sur les taux de correspondance dans son tableau de bord. Vous pouvez les consulter sur LinkedIn dans la section **Audiences**. Vous pouvez consulter le taux de correspondance de votre audience LinkedIn dans les détails de l'étape Canvas de votre étape Audience Sync.

### Combien d'audiences LinkedIn peut-il prendre en charge ? {#how-many-audiences-can-linkedin-support}

Actuellement, il n'y a aucune limite quant au nombre d'audiences dans votre compte publicitaire LinkedIn.

### Pourquoi un segment est-il bloqué au statut BUILDING et n'est-il pas mis à jour ? {#why-is-a-segment-stuck-in-building-status-and-not-updated}

Un segment est considéré comme inutilisé et passe au statut ARCHIVED après ne pas avoir été utilisé en continu pendant 30 jours dans une campagne brouillon ou active. De ce fait, un segment peut sembler « bloqué » en BUILDING lorsque des mises à jour sont transmises à un segment ARCHIVED, le faisant ainsi passer à l'état BUILDING, et juste avant qu'il ne soit à nouveau archivé, de nouvelles mises à jour sont transmises au segment inutilisé.