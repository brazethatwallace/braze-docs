---
nav_title: Pinterest
article_title: Synchronisation des audiences Canvas avec Pinterest
description: "Cet article de référence explique comment utiliser la synchronisation d'audience Braze vers Pinterest, pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
page_order: 5
alias: "/audience_sync_pinterest/"

tool:
  - Canvas

---

# Synchronisation d'audience avec Pinterest {#audience-sync-to-pinterest}

En utilisant la synchronisation d'audience Braze vers Pinterest, les marques peuvent choisir d'ajouter des données utilisateur de leur propre intégration Braze aux audiences Pinterest pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore. Tout critère que vous utiliseriez normalement pour déclencher un message (notification push, e-mail, SMS, webhook, etc.) dans un Canvas Braze basé sur vos données utilisateur peut désormais être utilisé pour déclencher une annonce à cet utilisateur dans vos audiences Pinterest.

**Les cas d'usage courants pour la synchronisation d'audience incluent :**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

Cette fonctionnalité permet aux marques de contrôler quelles données first-party spécifiques sont partagées avec Pinterest. Chez Braze, les intégrations avec lesquelles vous pouvez et ne pouvez pas partager vos données first-party sont prises en compte avec la plus grande attention. Pour plus d'informations, consultez notre [politique de confidentialité](https://www.braze.com/privacy).

{% alert important %}
**Avis de non-responsabilité d'Audience Sync Pro**<br>
La synchronisation des audiences Braze avec Pinterest est une intégration Audience Sync Pro. Pour plus d'informations sur cette intégration, contactez votre gestionnaire de compte Braze.
{% endalert %}

## Prérequis {#prerequisites}
Vous devez vous assurer que les éléments suivants sont créés, complétés et/ou acceptés avant de configurer votre étape de synchronisation d'audience Pinterest dans Canvas.

| Exigence | Origine | Description |
| --- | --- | --- |
| Pinterest Business Hub | [Pinterest](https://www.pinterest.com/business/hub/) | Un outil centralisé pour gérer les ressources Pinterest de votre marque (telles que les comptes publicitaires, les pages, les applications). |
| Compte publicitaire Pinterest | [Pinterest](https://ads.pinterest.com/) | Un compte publicitaire Pinterest actif lié au Pinterest Business Hub de votre marque.<br><br>Assurez-vous que l'administrateur de votre Pinterest Business Hub vous a accordé les autorisations d'administrateur pour les comptes publicitaires Pinterest que vous prévoyez d'utiliser avec Braze. |
| Conditions et politiques Pinterest | Pinterest | Acceptez de vous conformer à l'ensemble des conditions, politiques, directives et documentations requises par Pinterest en lien avec votre utilisation de la synchronisation d'audience Pinterest, y compris les conditions, politiques, directives et documentations incorporées par référence, qui peuvent inclure : les Conditions d'utilisation, les Conditions d'utilisation commerciales, la Politique de confidentialité, les Conditions d'utilisation des développeurs et de l'API, les Conditions relatives aux données publicitaires, les Directives publicitaires, le Contrat de services publicitaires, les Règles de la communauté et les Directives de marque. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Se connecter à Pinterest {#step-1-connect-to-pinterest}

{% alert important %}
Vous devez disposer de la [permission « Admin »]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) pour connecter Pinterest à votre compte Braze.
{% endalert %}

Dans le tableau de bord de Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Pinterest**. Sous Pinterest Audience Sync, sélectionnez **Connect Pinterest**.

![Page de la technologie Pinterest dans Braze comprenant une section Aperçu et une section Pinterest Audience Sync avec le bouton Connect Pinterest.]({% image_buster /assets/img/pinterest/pinterest1.png %}){: style="max-width:80%;"}

Vous serez alors redirigé vers la page OAuth de Pinterest pour autoriser Braze à gérer les comptes publicitaires et les audiences.

Après avoir sélectionné **Confirm**, vous serez redirigé vers Braze pour sélectionner les comptes publicitaires Pinterest que vous souhaitez synchroniser.

![Une liste des comptes publicitaires disponibles que vous pouvez connecter à Pinterest.]({% image_buster /assets/img/pinterest/pinterest2.png %}){: style="max-width:80%;"}

Une fois la connexion établie, vous reviendrez à la page partenaire, où vous pourrez voir quels comptes sont connectés et déconnecter les comptes existants.

![Une version mise à jour de la page des partenaires technologiques Pinterest montrant les comptes publicitaires connectés avec succès.]({% image_buster /assets/img/pinterest/pinterest3.png %}){: style="max-width:80%;"}

Votre connexion Pinterest sera appliquée au niveau de l'espace de travail Braze. Si votre administrateur Pinterest vous retire de votre Pinterest Business Hub ou de l'accès aux comptes Pinterest connectés, Braze détectera un jeton invalide. Par conséquent, vos Canvas actifs utilisant des composants Pinterest Audience afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs.

### Étape 2 : Ajouter une étape Audience Sync avec Pinterest {#step-2-add-an-audience-sync-step-with-pinterest}

Ajoutez un composant dans votre Canvas et sélectionnez **Audience Sync**.

![Sélecteur d'étapes Canvas avec l'option du composant Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Carte du composant Audience Sync ajoutée à un parcours Canvas.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Étape 3 : Configuration de la synchronisation {#step-3-sync-setup}

Cliquez sur le bouton **Custom Audience** pour ouvrir l'éditeur de composant.

Sélectionnez **Pinterest** comme partenaire Audience Sync souhaité.

![Éditeur du composant Audience Sync avec Pinterest sélectionné comme partenaire de synchronisation.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Sélectionnez ensuite le compte publicitaire Pinterest souhaité. Dans le menu déroulant **Choose a New or Existing Audience**, saisissez le nom d'une audience nouvelle ou existante.

{% tabs %}
{% tab Créer une nouvelle audience %}

**Créer une nouvelle audience**<br>
Saisissez un nom pour la nouvelle audience, sélectionnez **Add Users to Audience**, puis choisissez les champs que vous souhaitez synchroniser avec Pinterest. Enregistrez ensuite votre audience en cliquant sur le bouton **Create Audience** en bas de l'éditeur d'étape.

![Vue développée de l'étape Canvas Custom Audience. Le compte publicitaire souhaité est sélectionné et une nouvelle audience est créée.]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

Braze affiche une notification en haut de l'éditeur d'étape si l'audience est créée avec succès ou si des erreurs surviennent. Les utilisateurs peuvent référencer cette audience pour la suppression d'utilisateurs ultérieurement dans le parcours Canvas, car l'audience a été créée en mode brouillon.

![Une alerte qui apparaît après la création d'une nouvelle audience dans le composant Canvas.]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze synchronise les utilisateurs en quasi temps réel dès qu'ils entrent dans l'étape Audience Sync.
{% endtab %}
{% tab Synchroniser avec une audience existante %}
**Synchroniser avec une audience existante**<br>
Braze offre également la possibilité d'ajouter des utilisateurs à des audiences Pinterest existantes pour s'assurer qu'elles sont à jour. Pour synchroniser avec une audience existante, saisissez le nom de l'audience existante dans le menu déroulant et ajoutez-la à l'audience. Braze ajoutera ensuite les utilisateurs en quasi temps réel dès qu'ils entreront dans l'étape Audience Sync.

![Vue développée de l'étape Canvas Custom Audience. Le compte publicitaire souhaité et une audience existante sont sélectionnés.]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Lancer le Canvas {#step-4-launch-canvas}

Après avoir configuré votre Audience Sync vers Pinterest, lancez le Canvas ! La nouvelle audience est créée, et les utilisateurs qui passent par l'étape Audience Sync sont ajoutés à cette audience sur Pinterest. Si votre Canvas contient des composants ultérieurs, vos utilisateurs progressent vers l'étape suivante de leur parcours utilisateur.

Vous pouvez consulter l'audience sur Pinterest en accédant à votre compte de gestionnaire de publicités et en sélectionnant Audiences dans le menu déroulant Ads. Depuis la page Audience, vous pouvez voir la taille de chaque audience une fois qu'elle atteint environ ~100.

![Détails de l'audience pour une audience Pinterest donnée, comprenant le nom de l'audience, l'ID de l'audience, le type d'audience et la taille de l'audience.]({% image_buster /assets/img/pinterest/pinterest11.png %})

## Synchronisation des utilisateurs et considérations relatives aux limites de débit {#user-syncing-and-rate-limit-considerations}

Lorsque les utilisateurs atteignent l'étape Audience Sync, Braze les synchronise en quasi temps réel tout en respectant les limites de débit de l'API Marketing de Pinterest. Braze regroupe et traite autant d'utilisateurs que possible toutes les 5 secondes avant de les envoyer à Pinterest.

La limite de débit de l'API Segment de Pinterest n'autorise pas plus de sept requêtes par seconde et par utilisateur, et 1 900 utilisateurs par requête. Si un client atteint cette limite, Braze retente la synchronisation pendant environ 13 heures. Si la synchronisation n'est toujours pas possible, Braze répertorie ces utilisateurs dans l'indicateur Users Errored.

## Comprendre les analyses {#understanding-analytics}

Le tableau suivant comprend les indicateurs et les descriptions pour vous aider à mieux comprendre les analyses de votre composant Audience Sync.

| Indicateur | Description |
| --- | --- |
| Entrés | Nombre d'utilisateurs qui sont entrés dans ce composant pour être synchronisés avec Pinterest. |
| Passés à l'étape suivante | Combien d'utilisateurs ont avancé vers le composant suivant s'il y en a un ? Tous les utilisateurs avanceront automatiquement s'il s'agit de la dernière étape de la branche du Canvas. |
| Utilisateurs synchronisés | Nombre d'utilisateurs qui ont été synchronisés avec succès avec Pinterest. |
| Utilisateurs non synchronisés | Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants pour la correspondance. |
| Utilisateurs en attente | Nombre d'utilisateurs actuellement en cours de traitement par Braze pour la synchronisation avec Pinterest. |
| Utilisateurs en erreur | Nombre d'utilisateurs qui n'ont pas été synchronisés avec Pinterest en raison d'une erreur d'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton Pinterest invalide ou la suppression de l'audience sur Pinterest. |
| Sortis du Canvas | Nombre d'utilisateurs qui sont sortis du Canvas. Cela se produit lorsque la dernière étape d'un Canvas est un composant Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprendre les analyses" }

{% alert important %}
N'oubliez pas qu'il y aura un délai dans le reporting pour les indicateurs d'utilisateurs synchronisés et d'erreurs en raison respectivement du vidage en masse et des 13 heures de tentatives.
{% endalert %}

## Questions fréquentes {#frequently-asked-questions}

### Combien de temps faudra-t-il pour que mes audiences soient renseignées dans Pinterest ? {#how-long-will-it-take-for-my-audiences-to-populate-in-pinterest}

La taille de l'audience sera mise à jour dans un délai de 24 à 48 heures sur la page **Audiences** dans le gestionnaire de publicités de Pinterest.

### Comment savoir si des utilisateurs ont été mis en correspondance après avoir transmis des utilisateurs à Pinterest ? {#how-do-i-know-if-users-have-matched-after-passing-users-to-pinterest}

Pinterest ne fournit pas cette information en raison de ses propres politiques de confidentialité des données.

### Que dois-je faire si je reçois une erreur de jeton invalide ? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Confirmez auprès de l'administrateur de votre Pinterest Business Hub que vous disposez des autorisations appropriées pour le compte publicitaire que vous souhaitez synchroniser. Vous pouvez également déconnecter et reconnecter votre compte Pinterest sur la page partenaire Pinterest.

### Pourquoi mon Canvas ne peut-il pas être lancé ? {#why-is-my-canvas-not-allowed-to-launch}

Assurez-vous que votre compte Pinterest est correctement connecté à Braze sur la page partenaire Pinterest. Vérifiez que vous avez sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience et sélectionné les champs à mettre en correspondance.

### Pourquoi ne puis-je pas sélectionner mon compte publicitaire pour mon étape Audience Sync ? {#why-cant-i-select-my-ad-account-for-my-audience-sync-step}

Vérifiez que votre jeton a été généré avec les autorisations de compte appropriées. Notez que si vous avez trop d'audiences dans votre compte publicitaire Pinterest, le menu déroulant pour sélectionner votre compte publicitaire peut expirer. Dans ce cas, nous recommandons de réduire le nombre d'audiences dans votre compte publicitaire.