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

- Cibler des utilisateurs à forte valeur via plusieurs canaux pour stimuler les achats ou l'engagement
- Recibler les utilisateurs qui réagissent moins aux autres canaux de marketing
- Créer des audiences de suppression pour éviter que les utilisateurs ne reçoivent des publicités alors qu'ils sont déjà des consommateurs fidèles de votre marque
- Créer des audiences similaires (Actalike) pour acquérir de nouveaux utilisateurs plus efficacement

Cette fonctionnalité permet aux marques de contrôler quelles données first-party spécifiques sont partagées avec Pinterest. Chez Braze, les intégrations avec lesquelles vous pouvez et ne pouvez pas partager vos données first-party sont prises en compte avec la plus grande attention. Pour plus d'informations, consultez notre [politique de confidentialité](https://www.braze.com/privacy).

{% alert important %}
**Avis de non-responsabilité d'Audience Sync Pro**<br>
La synchronisation des audiences Braze avec Pinterest est une intégration Audience Sync Pro. Pour plus d'informations sur cette intégration, contactez votre gestionnaire de compte Braze.
{% endalert %}

## Conditions préalables {#prerequisites}
Vous devez vous assurer que les éléments suivants sont créés, complétés et/ou acceptés avant de configurer votre étape d'audience Pinterest dans Canvas.

| Exigence | Origine | Description |
| --- | --- | --- |
| Centre d'affaires Pinterest | [Pinterest](https://www.pinterest.com/business/hub/) | Un outil centralisé pour gérer les ressources Pinterest de votre marque (tels que les comptes publicitaires, les pages, les applications). |
| Compte publicitaire Pinterest | [Pinterest](https://ads.pinterest.com/) | Un compte publicitaire Pinterest actif lié au Centre d'affaires Pinterest de votre marque.<br><br>Assurez-vous que l'administrateur du Centre d'affaires Pinterest vous a accordé les autorisations d'administrateur pour les comptes publicitaires Pinterest que vous prévoyez d'utiliser avec Braze. |
| Conditions et politiques Pinterest | Pinterest | Acceptez de vous conformer à toutes les conditions, politiques, directives et documentations requises par Pinterest relatives à votre utilisation de la synchronisation d'audience Pinterest, y compris toutes les conditions, politiques, directives et documentations incorporées par référence, qui peuvent inclure : les Conditions de service, les Conditions de service pour les entreprises, la Politique de confidentialité, les Conditions de service pour les développeurs et les API, les Conditions relatives aux données publicitaires, les Directives publicitaires, l'Accord de services publicitaires, les Directives communautaires et les Directives de marque. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Se connecter à Pinterest {#step-1-connect-to-pinterest}

{% alert important %}
Vous devez disposer de l'[autorisation « Admin »]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) pour connecter Pinterest à votre compte Braze.
{% endalert %}

Dans le tableau de bord de Braze, allez dans **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Pinterest**. Sous Synchronisation d'audience Pinterest, sélectionnez **Connect Pinterest**.

![Page technologique Pinterest dans Braze comprenant une section Aperçu et une section Synchronisation d'audience Pinterest avec le bouton Connect Pinterest.]({% image_buster /assets/img/pinterest/pinterest1.png %}){: style="max-width:80%;"}

Vous serez ensuite redirigé vers la page OAuth de Pinterest pour autoriser Braze à gérer les comptes publicitaires et les audiences.

Après avoir sélectionné **Confirm**, vous serez redirigé vers Braze pour sélectionner les comptes publicitaires Pinterest que vous souhaitez synchroniser.

![Une liste de comptes publicitaires disponibles que vous pouvez connecter à Pinterest.]({% image_buster /assets/img/pinterest/pinterest2.png %}){: style="max-width:80%;"}

Une fois la connexion établie, vous retournerez à la page partenaire, où vous pourrez voir quels comptes sont connectés et déconnecter les comptes existants.

![Une version mise à jour de la page des partenaires technologiques Pinterest montrant les comptes publicitaires connectés avec succès.]({% image_buster /assets/img/pinterest/pinterest3.png %}){: style="max-width:80%;"}

Votre connexion Pinterest sera appliquée au niveau de l'espace de travail Braze. Si votre administrateur Pinterest vous retire du Centre d'affaires Pinterest ou de l'accès aux comptes Pinterest connectés, Braze détectera un jeton non valide. En conséquence, vos Canvas actifs utilisant des composants d'audience Pinterest afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs.

### Étape 2 : Ajouter une étape de synchronisation d'audience avec Pinterest {#step-2-add-an-audience-sync-step-with-pinterest}

Ajoutez un composant dans votre Canvas et sélectionnez **Audience Sync**.

![Sélecteur d'étape Canvas avec l'option du composant Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Carte du composant Audience Sync ajoutée à un parcours Canvas.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Étape 3 : Configuration de la synchronisation {#step-3-sync-setup}

Cliquez sur le bouton **Custom Audience** pour ouvrir l'éditeur de composants.

Sélectionnez **Pinterest** comme partenaire de synchronisation d'audience souhaité.

![Éditeur du composant Audience Sync avec Pinterest sélectionné comme partenaire de synchronisation.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Ensuite, sélectionnez le compte publicitaire Pinterest souhaité. Sous le menu déroulant **Choose a New or Existing Audience**, saisissez le nom d'une audience nouvelle ou existante.

{% tabs %}
{% tab Créer une nouvelle audience %}

**Créer une nouvelle audience**<br>
Saisissez un nom pour la nouvelle audience, sélectionnez **Add Users to Audience**, et sélectionnez les champs que vous souhaitez synchroniser avec Pinterest. Ensuite, enregistrez votre audience en cliquant sur le bouton **Create Audience** en bas de l'éditeur d'étape.

![Vue élargie de l'étape Canvas Custom Audience. Le compte publicitaire souhaité est sélectionné et une nouvelle audience est créée ici.]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

Braze affiche une notification en haut de l'éditeur d'étape si l'audience est créée avec succès ou si des erreurs surviennent. Les utilisateurs peuvent faire référence à cette audience pour la suppression d'utilisateurs plus tard dans le parcours Canvas, car l'audience a été créée en mode brouillon.

![Une alerte qui apparaît après la création d'une nouvelle audience dans le composant Canvas.]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze synchronise les utilisateurs en quasi-temps réel lorsqu'ils entrent dans l'étape de synchronisation d'audience.
{% endtab %}
{% tab Synchroniser avec une audience existante %}
**Synchroniser avec une audience existante**<br>
Braze offre également la possibilité d'ajouter des utilisateurs aux audiences Pinterest existantes pour s'assurer que ces audiences sont à jour. Pour synchroniser avec une audience existante, saisissez le nom de l'audience existante dans le menu déroulant et ajoutez-la à l'audience. Braze ajoutera ensuite les utilisateurs en quasi-temps réel lorsqu'ils entreront dans l'étape de synchronisation d'audience.

![Vue élargie de l'étape Canvas Custom Audience. Le compte publicitaire souhaité et l'audience existante sont sélectionnés ici.]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Lancer le Canvas {#step-4-launch-canvas}

Une fois que vous avez configuré la synchronisation d'audience avec Pinterest, lancez le Canvas ! La nouvelle audience sera créée et les utilisateurs qui passeront par l'étape de synchronisation d'audience seront transférés vers cette audience sur Pinterest. Si votre Canvas contient des composants ultérieurs, vos utilisateurs passeront à l'étape suivante de leur parcours utilisateur.

Vous pouvez consulter l'audience sur Pinterest en accédant à votre compte gestionnaire de publicités et en sélectionnant Audiences dans le menu déroulant Ads. Depuis la page Audience, vous pouvez voir la taille de chaque audience une fois qu'elle atteint environ 100.

![Détails d'une audience Pinterest donnée, notamment le nom, l'ID, le type et la taille de l'audience.]({% image_buster /assets/img/pinterest/pinterest11.png %})

## Considérations relatives à la synchronisation des utilisateurs et à la limite de débit {#user-syncing-and-rate-limit-considerations}

Lorsque les utilisateurs atteignent l'étape de synchronisation d'audience, Braze les synchronise en quasi-temps réel tout en respectant les limites de débit de l'API marketing de Pinterest. Braze met en lot et traite autant d'utilisateurs que possible toutes les 5 secondes avant de les envoyer à Pinterest.

La limite de débit de l'API Segment de Pinterest n'autorise pas plus de sept requêtes par seconde et par utilisateur, et 1 900 utilisateurs par requête. Si un client atteint cette limite, Braze retente la synchronisation pendant environ 13 heures. Si la synchronisation n'est toujours pas possible, Braze répertorie ces utilisateurs sous l'indicateur Users Errored.

## Comprendre les analyses {#understanding-analytics}

Le tableau suivant comprend des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses de votre composant de synchronisation d'audience.

| Indicateur | Description |
| --- | --- |
| Entrés | Nombre d'utilisateurs qui sont entrés dans ce composant pour être synchronisés avec Pinterest. |
| Passés à l'étape suivante | Nombre d'utilisateurs passés au composant suivant s'il y en a un. Tous les utilisateurs avanceront automatiquement s'il s'agit de la dernière étape de la branche Canvas. |
| Utilisateurs synchronisés | Nombre d'utilisateurs qui ont été synchronisés avec succès sur Pinterest. |
| Utilisateurs non synchronisés | Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants à faire correspondre. |
| Utilisateurs en attente | Nombre d'utilisateurs actuellement traités par Braze pour la synchronisation avec Pinterest. |
| Utilisateurs en erreur | Nombre d'utilisateurs qui n'ont pas été synchronisés avec Pinterest en raison d'une erreur d'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton Pinterest non valide ou la suppression de l'audience sur Pinterest. |
| Sortis du Canvas | Nombre d'utilisateurs ayant quitté le Canvas. Cela se produit lorsque la dernière étape d'un Canvas est un composant de synchronisation d'audience. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprendre les analyses" }

{% alert important %}
N'oubliez pas qu'il y aura un délai dans la génération des rapports pour les utilisateurs synchronisés et les indicateurs d'erreurs, en raison du vidage en masse et de la période de 13 heures de nouvelles tentatives, respectivement.
{% endalert %}

## Foire aux questions {#frequently-asked-questions}

### Combien de temps faudra-t-il pour que mes audiences se remplissent dans Pinterest ? {#how-long-will-it-take-for-my-audiences-to-populate-in-pinterest}

La taille de l'audience sera mise à jour dans les 24 à 48 heures sur la page **Audiences** du gestionnaire de publicités de Pinterest.

### Comment puis-je savoir si les utilisateurs ont été mis en correspondance après les avoir transférés à Pinterest ? {#how-do-i-know-if-users-have-matched-after-passing-users-to-pinterest}

Pinterest ne fournit pas ces informations en raison de ses propres politiques de confidentialité des données.

### Que dois-je faire si je reçois une erreur de jeton non valide ? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Confirmez auprès de l'administrateur de votre Centre d'affaires Pinterest que vous disposez des autorisations appropriées pour le compte publicitaire que vous souhaitez synchroniser. Vous pouvez également déconnecter et reconnecter votre compte Pinterest sur la page partenaire Pinterest.

### Pourquoi mon Canvas n'est-il pas autorisé à être lancé ? {#why-is-my-canvas-not-allowed-to-launch}

Assurez-vous que votre compte Pinterest se connecte avec succès à Braze sur la page partenaire Pinterest. Vérifiez que vous avez sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience et sélectionné les champs à faire correspondre.

### Pourquoi ne puis-je pas sélectionner mon compte publicitaire pour mon étape de synchronisation d'audience ? {#why-cant-i-select-my-ad-account-for-my-audience-sync-step}

Vérifiez que votre jeton a été généré avec les autorisations de compte correctes. Notez que si vous avez trop d'audiences dans votre compte publicitaire Pinterest, le menu déroulant permettant de sélectionner votre compte publicitaire peut dépasser le temps imparti. Dans ce cas, nous vous recommandons de réduire le nombre d'audiences dans votre compte publicitaire.