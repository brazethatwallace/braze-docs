---
nav_title: TikTok
article_title: "Synchronisation de l'audience de Canvas sur TikTok"
alias: /tiktok_audience_sync/
description: "Cet article de référence explique comment utiliser Braze Audience Sync sur TikTok pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
tool:
  - Canvas
page_order: 8

---

# Synchronisation de l'audience sur TikTok {#audience-sync-to-tiktok}

Grâce à Braze Audience Sync to TikTok, les marques peuvent ajouter les données utilisateurs de leur propre intégration Braze à TikTok Audiences pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore. Tout critère que vous utiliseriez normalement pour déclencher un message (notification push, e-mail, SMS, webhook, etc.) dans un Canvas Braze.

**Les cas d'usage courants de la synchronisation d'audience sont les suivants** :

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

Cette fonctionnalité permet aux marques de contrôler quelles données first-party spécifiques sont partagées avec TikTok. Chez Braze, les intégrations avec lesquelles vous pouvez ou non partager vos données first-party font l'objet de la plus grande attention. Pour plus d'informations, consultez notre [politique de confidentialité](https://www.braze.com/privacy).

{% alert important %}
**Avis de non-responsabilité d'Audience Sync Pro**<br>
La synchronisation d'audiences Braze avec TikTok est une intégration Audience Sync Pro. Pour plus d'informations sur cette intégration, contactez votre gestionnaire de compte Braze.
{% endalert %}

## Prérequis {#prerequisites}

Vous devez vous assurer que les éléments suivants sont créés, complétés et/ou acceptés avant de configurer votre étape TikTok Audience dans Canvas.

| Exigence | Origine | Description |
| ----------- | ------ | ----------- |
| Compte TikTok for Business Center | [TikTok](https://business.tiktok.com/) | Un outil centralisé pour gérer les ressources TikTok de votre marque (telles que les comptes publicitaires, les pages, les applications). |
| Compte publicitaire TikTok | [TikTok](https://ads.tiktok.com/) | Un compte publicitaire TikTok actif lié au compte Business Center de votre marque.<br><br>Assurez-vous que l'administrateur de votre TikTok Business Center vous a accordé les autorisations d'administrateur pour les comptes publicitaires TikTok que vous prévoyez d'utiliser avec Braze. |
| Conditions et politiques TikTok | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Acceptez de vous conformer à l'ensemble des conditions, politiques, directives et documents requis par TikTok en lien avec votre utilisation de TikTok Audience Sync, y compris les conditions, politiques, directives et documents incorporés par référence, qui peuvent inclure : les conditions générales d'utilisation commerciale, les conditions publicitaires, la politique de confidentialité, les conditions relatives aux audiences personnalisées, les conditions d'utilisation pour les développeurs, l'accord de partage de données pour les développeurs, les politiques publicitaires, les directives de marque et les directives communautaires. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Se connecter à TikTok {#step-1-connect-to-tiktok}

{% alert important %}
Vous devez disposer de la [permission « Admin »]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#admin) pour connecter TikTok à votre compte Braze.
{% endalert %}

Dans le tableau de bord de Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **TikTok**. Sous TikTok Audience Sync, sélectionnez **Connect TikTok**.

![Page technologique TikTok dans Braze comprenant une section Aperçu et une section TikTok Audience Sync avec le bouton Connected TikTok.]({% image_buster /assets/img/tiktok/tiktok1.png %}){: style="max-width:75%;"}

Vous serez alors redirigé vers la page OAuth de TikTok pour autoriser Braze à gérer les comptes publicitaires et les audiences. Après avoir sélectionné **Confirm**, vous serez redirigé vers Braze pour choisir les comptes publicitaires TikTok que vous souhaitez synchroniser.

![Page d'autorisation OAuth TikTok demandant l'accès pour la gestion des audiences Braze.]({% image_buster /assets/img/tiktok/tiktok2.png %}){: style="max-width:75%;"}

Une fois la connexion établie, vous reviendrez sur la page partenaire. Vous pourrez y voir les comptes connectés et déconnecter les comptes existants.

![Page partenaire TikTok dans Braze affichant les comptes publicitaires TikTok connectés.]({% image_buster /assets/img/tiktok/tiktok3.png %}){: style="max-width:75%;"}

Votre connexion TikTok sera appliquée au niveau de l'espace de travail Braze. Si votre administrateur TikTok vous retire de votre TikTok Business Center ou de l'accès aux comptes TikTok connectés, Braze détectera un jeton invalide. Par conséquent, vos Canvas actifs utilisant les composants TikTok Audience afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs.

### Étape 2 : Ajouter un composant TikTok Audience dans Canvas {#step-2-add-a-tiktok-audience-component-in-canvas}

Ajoutez un composant dans votre Canvas et sélectionnez **Audience Sync**.

![Sélecteur d'étapes Canvas avec l'option du composant Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Carte du composant Audience Sync ajoutée à un parcours Canvas.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Étape 3 : Configuration de la synchronisation {#step-3-sync-setup}

Cliquez sur le bouton **Custom Audience** pour ouvrir l'éditeur de composant.

Sélectionnez **TikTok** comme partenaire Audience Sync souhaité.

![Éditeur du composant Audience Sync avec TikTok sélectionné comme partenaire de synchronisation.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Sélectionnez ensuite le compte publicitaire TikTok souhaité. Dans le menu déroulant **Choose a New or Existing Audience**, saisissez le nom d'une audience nouvelle ou existante.

![Éditeur TikTok Audience Sync affichant la sélection du compte publicitaire et le menu déroulant des audiences.]({% image_buster /assets/img/tiktok/tiktok11.png %})

{% tabs %}
{% tab Créer une nouvelle audience %}

**Créer une nouvelle audience**<br>
Saisissez un nom pour la nouvelle audience, sélectionnez **Add Users to Audience**, puis choisissez les champs que vous souhaitez synchroniser avec TikTok. Enregistrez ensuite votre audience en cliquant sur le bouton **Create Audience** en bas de l'éditeur d'étape.

![Formulaire de création d'une nouvelle audience dans l'étape TikTok Audience Sync avec les champs de correspondance sélectionnés.]({% image_buster /assets/img/audience_sync/tiktok3.png %})

Braze affiche une notification en haut de l'éditeur d'étape si l'audience est créée avec succès ou si des erreurs surviennent. Les utilisateurs peuvent référencer cette audience pour la suppression d'utilisateurs ultérieurement dans le parcours Canvas, car l'audience a été créée en mode brouillon.

![Notification de succès dans l'étape Audience Sync après la création d'une nouvelle audience TikTok.]({% image_buster /assets/img/audience_sync/tiktok2.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze synchronise les utilisateurs en quasi temps réel à mesure qu'ils entrent dans l'étape d'audience.

{% endtab %}
{% tab Synchroniser avec une audience existante %}

**Synchroniser avec une audience existante**<br>
Braze offre également la possibilité d'ajouter des utilisateurs à des audiences TikTok existantes pour s'assurer qu'elles restent à jour. Pour synchroniser avec une audience existante, saisissez le nom de l'audience existante dans le menu déroulant et sélectionnez **Add to the Audience**. Braze ajoutera alors les utilisateurs en quasi temps réel à mesure qu'ils entrent dans l'étape TikTok Audience.

![Vue étendue de l'étape Canvas Custom Audience. Le compte publicitaire souhaité et l'audience existante sont sélectionnés ici.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Lancer le Canvas {#step-4-launch-canvas}
Après avoir configuré votre composant TikTok Audience, lancez le Canvas ! Une nouvelle audience est créée, et les utilisateurs qui passent par le composant TikTok Audience sont ajoutés à cette audience sur TikTok. Si votre Canvas contient des composants ultérieurs, vos utilisateurs progressent vers l'étape suivante de leur parcours utilisateur.

Vous pouvez consulter l'audience dans TikTok en accédant à votre **Ads Manager Account** et en sélectionnant **Audiences** dans le menu déroulant **Assets**. Depuis la page **Audience**, vous pouvez voir la taille de chaque audience une fois qu'elle atteint &#126;1 000.

![Page TikTok listant les indicateurs suivants pour l'audience donnée.]({% image_buster /assets/img/tiktok/tiktok5.png %})

## Synchronisation des utilisateurs et considérations relatives aux limites de débit {#user-syncing-and-rate-limit-considerations}

Lorsque les utilisateurs atteignent l'étape Audience Sync, Braze les synchronise en quasi-temps réel tout en respectant les limites de débit de l'API Marketing de TikTok. Braze regroupe et traite autant d'utilisateurs que possible toutes les 5 secondes avant de les envoyer à TikTok.

La limite de débit de l'API Segment de TikTok n'autorise pas plus de 50 requêtes par seconde et 10 000 utilisateurs par requête. Si un client atteint cette limite, Braze retente la synchronisation pendant environ &#126;13 heures. Si la synchronisation n'est toujours pas possible, Braze répertorie ces utilisateurs dans l'indicateur Users Errored.

## Comprendre l'analytique {#understanding-analytics}

Le tableau suivant présente les indicateurs et descriptions pour vous aider à mieux comprendre l'analytique de votre composant Audience Sync.

| Indicateur | Description |
| ------ | ----------- |
| Entered | Nombre d'utilisateurs ayant accédé à ce composant pour être synchronisés vers TikTok. |
| Proceeded to Next Step | Nombre d'utilisateurs ayant avancé vers le composant suivant, s'il en existe un. Tous les utilisateurs avancent automatiquement s'il s'agit de la dernière étape de la branche du Canvas. |
| Users Synced | Nombre d'utilisateurs ayant été synchronisés avec succès vers TikTok. Notez que cela ne correspond pas nécessairement aux utilisateurs mis en correspondance sur TikTok. |
| Users Not Synced | Nombre d'utilisateurs n'ayant pas été synchronisés en raison de champs manquants pour la mise en correspondance. |
| Users Pending | Nombre d'utilisateurs en cours de traitement par Braze pour la synchronisation vers TikTok. |
| Users Errored | Nombre d'utilisateurs n'ayant pas été synchronisés vers TikTok en raison d'une erreur d'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton TikTok invalide ou la suppression de l'audience sur TikTok. |
| Exited Canvas | Nombre d'utilisateurs ayant quitté le Canvas. Cela se produit lorsque la dernière étape d'un Canvas est un composant Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprendre l'analytique" }

{% alert important %}
N'oubliez pas qu'il y aura un délai dans le reporting pour les indicateurs d'utilisateurs synchronisés et d'utilisateurs en erreur, en raison respectivement du vidage en masse et des 13 heures de tentatives.
{% endalert %}

## Questions fréquentes {#frequently-asked-questions}

### Que dois-je faire si je reçois une erreur de jeton invalide ? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Vous pouvez déconnecter puis reconnecter votre compte TikTok sur la page partenaire TikTok. Assurez-vous auprès de l'administrateur de votre TikTok Business Center que vous disposez des autorisations appropriées pour le compte publicitaire que vous souhaitez synchroniser.

### Pourquoi mon Canvas ne peut-il pas être lancé ? {#why-is-my-canvas-not-allowed-to-launch}

Vérifiez que votre compte TikTok est correctement connecté à Braze sur la page partenaire TikTok. Ensuite, assurez-vous d'avoir sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience et choisi les champs à faire correspondre.

### Comment savoir si des utilisateurs ont été mis en correspondance après avoir transmis des utilisateurs à TikTok ? {#how-do-i-know-if-users-have-matched-after-passing-users-to-tiktok}

TikTok ne fournit pas cette information en raison de ses politiques de confidentialité des données.

### Combien de temps faudra-t-il pour que mes audiences soient renseignées dans TikTok ? {#how-long-will-it-take-for-my-audiences-to-populate-in-tiktok}

La taille de l'audience sera mise à jour sous 24 à 48 heures sur la page Audiences du gestionnaire de publicités TikTok.

### Quel est le nombre maximum d'audiences que je peux avoir dans mon compte publicitaire TikTok ? {#what-is-the-maximum-number-of-audiences-i-can-have-in-my-tiktok-ad-account}

Vous pouvez avoir jusqu'à 400 audiences par compte publicitaire TikTok.

### Pourquoi la taille de mon audience ou le taux de correspondance dans TikTok est-il supérieur au nombre d'utilisateurs synchronisés dans Braze avec Audience Sync ? {#why-is-my-audience-size-or-match-rate-in-tiktok-higher-than-the-users-synced-in-braze-with-audience-sync}

Cela s'explique par le fait que, dans TikTok, un même identifiant peut être associé à plusieurs utilisateurs TikTok. Ce phénomène se produit le plus souvent lorsque les clients utilisent des identifiants publicitaires mobiles (IDFA iOS et GAID Android), car un même appareil peut avoir plusieurs utilisateurs TikTok connectés.

De plus, TikTok comptabilise également les utilisateurs Pangle comme des utilisateurs mis en correspondance, ce qui peut dans certains cas entraîner un taux de correspondance plus élevé. Cependant, lorsque vous utilisez l'audience pour la diffusion publicitaire, la taille réelle de l'audience livrable peut ne pas être aussi élevée que le nombre d'utilisateurs mis en correspondance, car elle dépend du placement et d'autres facteurs d'influence.

### Pourquoi est-ce que je reçois un e-mail avec l'objet « Audience Does Not Exist For Canvas » ? {#why-am-i-receiving-an-email-with-the-subject-audience-does-not-exist-for-canvas}

Cela peut se produire si l'audience que vous avez choisi de synchroniser n'est pas une audience en streaming (par exemple, s'il s'agit d'une audience similaire ou d'une audience basée sur un fichier utilisateur). Essayez de créer une nouvelle audience via l'étape Canvas Braze Audience Sync.