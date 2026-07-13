---
nav_title: Facebook
article_title: "Synchronisation de l'audience Canvas avec Facebook"
description: "Cet article de référence explique comment utiliser la synchronisation d'audience Braze vers Facebook pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
page_order: 2
alias: /audience_sync_facebook/

tool:
  - Canvas

---

# Synchronisation de l'audience avec Facebook {#audience-sync-to-facebook}

> Grâce à la synchronisation d'audience Braze vers Facebook, vous pouvez choisir d'ajouter les données de vos propres utilisateurs issues de votre intégration Braze aux audiences personnalisées de Facebook afin de diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore.

Tous les critères que vous utiliseriez habituellement pour déclencher un message (notification push, e-mail, SMS ou webhook) dans un Canvas Braze sur la base de vos données utilisateur peuvent désormais être utilisés pour déclencher une publicité auprès de cet utilisateur dans Facebook à l'aide d'audiences personnalisées. Par exemple, lorsque vous configurez une synchronisation d'audience avec Facebook, vous êtes en mesure d'utiliser une grande variété de champs first-party comme l'e-mail, le téléphone, le prénom et le nom de famille.

**Les cas d'usage courants pour la synchronisation des audiences personnalisées sont les suivants** :

- Cibler des utilisateurs à forte valeur ajoutée via plusieurs canaux pour favoriser les achats ou l'engagement.
- Recibler les utilisateurs qui réagissent moins aux autres canaux marketing.
- Créer des audiences de suppression pour éviter que les utilisateurs ne reçoivent des publicités alors qu'ils sont déjà des consommateurs fidèles de votre marque.
- Créer des audiences similaires (lookalike) pour acquérir de nouveaux utilisateurs plus efficacement.

Cette fonctionnalité permet aux marques de contrôler quelles données first-party spécifiques sont partagées avec Facebook. Chez Braze, les intégrations avec lesquelles vous pouvez ou non partager vos données first-party font l'objet de la plus grande attention. Pour plus d'informations, consultez notre [politique de confidentialité](https://www.braze.com/privacy).

## Considérations relatives à la synchronisation des utilisateurs et à la limite de débit {#user-syncing-and-rate-limit-considerations}

Lorsque les utilisateurs atteignent l'étape de synchronisation de l'audience, Braze les synchronise quasiment en temps réel tout en respectant les limites de débit de l'API marketing de Facebook. Braze met en lots et traite autant d'utilisateurs que possible toutes les 5 secondes avant de les envoyer à Facebook.

La limite de débit de l'API marketing de Facebook ne permet pas plus de &#126;190 000 requêtes API par compte publicitaire sur une période d'une heure. Si un client atteint cette limite, Braze retente la synchronisation pendant environ &#126;13 heures. Si la synchronisation n'est toujours pas possible, Braze répertorie ces utilisateurs dans l'indicateur Utilisateurs en erreur.

## Conditions préalables {#prerequisites}

Vous devrez confirmer que vous avez créé et complété les éléments suivants avant de configurer votre étape Facebook Audience dans Canvas.

| Condition | Origine | Description |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook](https://www.facebook.com/business/help/113163272211510) | Un outil centralisé pour gérer les ressources Facebook de votre marque (par exemple, les comptes publicitaires, les pages et les applications). |
| Compte publicitaire Facebook | [Facebook](https://www.facebook.com/business/help/910137316041095) | Un compte publicitaire Facebook actif lié au gestionnaire d'entreprise de votre marque.<br><br>Assurez-vous que l'administrateur de votre Facebook Business Manager vous a accordé les autorisations « Manage Campaigns » ou « Manage ad accounts » pour les comptes publicitaires Facebook que vous prévoyez d'utiliser avec Braze. Assurez-vous également que vous avez accepté les conditions générales de votre compte publicitaire. |
| Conditions des audiences personnalisées de Facebook | [Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Acceptez les conditions des audiences personnalisées de Facebook pour vos comptes publicitaires Facebook que vous prévoyez d'utiliser avec Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Se connecter à Facebook {#step-1-connect-to-facebook}

{% alert important %}
Vous devez disposer de l'[autorisation « Admin »]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) pour connecter Facebook à votre compte Braze.
{% endalert %}

Dans le tableau de bord de Braze, allez dans **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Facebook**. Sous Facebook Audience Export, sélectionnez **Connect Facebook**.

![Page technologique Facebook dans Braze comprenant une section Aperçu et une section Facebook Audience Export avec le bouton Connect Facebook.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:85%;"}

Une fenêtre de dialogue Facebook oAuth s'affiche pour autoriser Braze à créer des audiences personnalisées dans vos comptes publicitaires Facebook.

![La première boîte de dialogue Facebook demandant de « Se connecter en tant que X », où X est votre nom d'utilisateur Facebook.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![La deuxième boîte de dialogue Facebook demandant l'autorisation de gérer les publicités pour vos comptes publicitaires.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

Après avoir relié Braze à votre compte Facebook, sélectionnez les comptes publicitaires que vous souhaitez synchroniser dans votre espace de travail Braze. Une fois connecté, vous revenez à la page partenaire, où vous pouvez voir quels comptes sont connectés et déconnecter les comptes existants.

![Une version mise à jour de la page des partenaires technologiques Facebook montrant les comptes publicitaires connectés avec succès.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:85%;"}

Votre connexion Facebook est appliquée au niveau de l'espace de travail Braze. Si votre administrateur Facebook vous supprime de votre Facebook Business Manager ou de l'accès aux comptes Facebook connectés, Braze détectera un jeton invalide. En conséquence, vos Canvas actifs utilisant des composants Facebook Audience afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs.

{% alert important %}
Pour les clients qui ont déjà suivi le processus de révision de l'application Facebook pour la [gestion des publicités](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) et l'[accès standard à la gestion des publicités](https://developers.facebook.com/docs/marketing-api/access#standard), votre jeton d'utilisateur système sera toujours valide pour le composant Facebook Audience. Vous ne pourrez pas modifier ou révoquer le jeton d'utilisateur système Facebook via la page partenaire Facebook. Au lieu de cela, vous pouvez connecter votre compte Facebook pour remplacer votre jeton d'utilisateur système Facebook dans votre espace de travail Braze.

<br><br>La configuration Facebook oAuth s'appliquera également aux [exportations Facebook utilisant des Segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook#prerequisites).
{% endalert %}

### Étape 2 : Accepter les conditions de service des audiences personnalisées {#step-2-accept-custom-audiences-terms-of-service}

Avant de créer votre Canvas, vous devez accepter les conditions de service de Facebook aux liens suivants :

- **Customer List Custom Audiences Terms pour votre compte personnel :** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- **Facebook Business Tools Terms pour votre compte professionnel :** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

![Un exemple des conditions à accepter pour les audiences personnalisées de listes de clients.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}){: style="max-width:85%;"}
![Un exemple des conditions à accepter pour les outils professionnels Facebook.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}){: style="max-width:85%;"}

Consultez la [section FAQ](#terms) pour plus de détails sur la vérification de votre compte Facebook lors de l'intégration.

### Étape 3 : Ajouter un composant Facebook Audience dans Canvas {#step-3-add-a-facebook-audience-component-in-canvas}

Ajoutez un composant dans votre Canvas et sélectionnez **Facebook Audience**.

![Une liste de composants à ajouter au Canvas.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Le composant Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Étape 4 : Configuration de la synchronisation {#step-4-sync-setup}

Cliquez sur le bouton **Custom Audience** pour ouvrir l'éditeur de composants. Ensuite, sélectionnez **Facebook** comme partenaire de synchronisation d'audience.

![Configuration de la synchronisation d'audience avec des options pour le choix d'un partenaire.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Sélectionnez le compte publicitaire Facebook souhaité. Dans la liste déroulante **Choose a New or Existing Audience**, saisissez le nom d'une audience nouvelle ou existante.

{% tabs %}
{% tab Créer une nouvelle audience %}

1. Saisissez un nom pour la nouvelle audience personnalisée.
2. Sélectionnez **Add Users to Audience**, puis choisissez les champs que vous souhaitez synchroniser avec Facebook.
3. Ensuite, sélectionnez **Create Audience** pour enregistrer votre audience.

![Configuration de la synchronisation d'audience avec les informations d'e-mail, de téléphone, de prénom et de nom de famille à faire correspondre.]({% image_buster /assets/img/audience_sync/fb_sync.png %})

Vous serez informé en haut de l'éditeur d'étape si l'audience est créée avec succès ou si une erreur se produit au cours de ce processus. Vous pouvez également faire référence à cette audience pour la suppression d'utilisateurs plus tard dans le parcours Canvas, car l'audience a été créée en mode brouillon.

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze crée la nouvelle audience personnalisée dès le lancement du Canvas et synchronise ensuite les utilisateurs quasiment en temps réel lorsqu'ils entrent dans l'étape de synchronisation d'audience.

{% endtab %}
{% tab Synchroniser avec une audience existante %}

Braze offre la possibilité d'ajouter ou de supprimer des utilisateurs des audiences personnalisées Facebook existantes afin de confirmer que ces audiences sont à jour. Pour synchroniser avec une audience existante, procédez comme suit :

1. Saisissez le nom de l'audience existante dans le menu déroulant.
2. Choisissez si vous voulez **Add to the Audience** ou **Remove from the Audience**.
3. Braze ajoutera ou supprimera des utilisateurs en temps quasi réel lorsqu'ils entreront dans l'étape Facebook Audience.

![Configuration de la synchronisation d'audience pour supprimer les informations relatives à l'e-mail, au téléphone, au prénom et au nom de famille.]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
Facebook interdit de supprimer des utilisateurs des audiences personnalisées lorsque la taille des audiences est trop faible (généralement moins de 1 000 utilisateurs). Par conséquent, Braze n'est pas en mesure de synchroniser les utilisateurs pour une suppression de l'étape de synchronisation d'audience tant que l'audience n'atteint pas la taille appropriée.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 5 : Lancer le Canvas {#step-5-launch-canvas}

Après avoir configuré votre composant Facebook Audience, il est temps de lancer le Canvas ! La nouvelle audience personnalisée est créée et les utilisateurs qui passent par l'étape Facebook Audience sont transférés dans cette audience personnalisée sur Facebook. Si votre Canvas contient des étapes ultérieures, vos utilisateurs passeront ensuite à l'étape suivante de leur parcours utilisateur.

L'onglet **History** de l'audience personnalisée dans le gestionnaire d'audience Facebook reflétera le nombre d'utilisateurs envoyés à l'audience depuis Braze. Si un utilisateur franchit à nouveau l'étape, il est renvoyé vers Facebook.

![Détails de l'audience et onglet History pour une audience Facebook donnée comprenant un tableau Audience History avec des colonnes pour l'activité, les détails de l'activité, les éléments modifiés, la date et l'heure.]({% image_buster /assets/img/fb_audience_sync/audience_history.png %}){: style="max-width:80%;"}

## Comprendre les analyses {#understanding-analytics}

Le tableau suivant comprend des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses de votre composant de synchronisation d'audience.

| Indicateur | Description |
| --- | --- |
| Entrés | Nombre d'utilisateurs qui sont entrés dans ce composant pour être synchronisés avec Facebook. |
| Passés à l'étape suivante | Nombre d'utilisateurs qui ont avancé au composant suivant, s'il y en a un. Tous les utilisateurs avanceront automatiquement s'il s'agit de la dernière étape de la branche du Canvas. |
| Utilisateurs synchronisés | Nombre d'utilisateurs qui ont été synchronisés avec succès avec Facebook. |
| Utilisateurs non synchronisés | Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants à faire correspondre. Les champs sont mis en correspondance à l'aide d'un opérateur « OU », ce qui signifie que tant qu'un utilisateur possède l'un des champs dans Facebook, Facebook mettra l'utilisateur en correspondance même si tous les autres champs ne correspondent pas. |
| Utilisateurs en attente | Nombre d'utilisateurs actuellement traités par Braze pour la synchronisation avec Facebook. |
| Utilisateurs en erreur | Nombre d'utilisateurs qui n'ont pas été synchronisés avec Facebook en raison d'une erreur d'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton Facebook invalide ou la suppression de l'audience personnalisée sur Facebook. |
| Sortis du Canvas | Nombre d'utilisateurs qui ont quitté le Canvas. Cela se produit lorsque la dernière étape d'un Canvas est une étape Facebook. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprendre les analyses" }

{% alert important %}
Il y a un délai dans les rapports pour les indicateurs des utilisateurs synchronisés et des utilisateurs en erreur en raison du traitement interne.
{% endalert %}

## Foire aux questions {#frequently-asked-questions}

### Combien de temps faut-il pour que mes audiences soient générées dans le tableau de bord de mon partenaire de synchronisation d'audience ? {#how-long-does-it-take-for-my-audiences-to-populate-in-my-audience-sync-partner-dashboard}

Le temps nécessaire pour générer une audience dépend du partenaire spécifique. Tous les réseaux traiteront les requêtes de Braze et tenteront de faire correspondre les utilisateurs. La mise à jour des audiences personnalisées peut prendre jusqu'à 24 heures.

### Que dois-je faire si je reçois une erreur de jeton invalide ? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Vous pouvez simplement déconnecter et reconnecter votre compte Facebook sur la page partenaire Facebook. Confirmez auprès de l'administrateur de votre Facebook Business Manager que vous disposez des autorisations appropriées pour le compte publicitaire avec lequel vous souhaitez effectuer la synchronisation.

### Pourquoi mon Canvas n'est-il pas autorisé à être lancé ? {#why-is-my-canvas-not-allowed-to-launch}

- Assurez-vous que votre jeton d'utilisateur système est authentifié et qu'il a accès aux comptes publicitaires souhaités dans Facebook Business Manager.
- Assurez-vous d'avoir sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience personnalisée et sélectionné les champs à faire correspondre.
- Vous avez peut-être atteint la limite de 500 audiences personnalisées sur Facebook. Rendez-vous dans le gestionnaire d'audiences Facebook pour en supprimer certaines inutiles avant de créer de nouvelles audiences personnalisées à l'aide de Canvas.

### Comment puis-je savoir si les utilisateurs ont été mis en correspondance après les avoir transférés à Facebook ? {#how-do-i-know-if-users-have-matched-after-passing-users-to-facebook}

Facebook ne fournit pas cette information pour des raisons de confidentialité.

### Braze prend-il en charge les audiences personnalisées basées sur la valeur ? {#does-braze-support-value-based-custom-audiences}

Pour l'instant, les audiences personnalisées basées sur la valeur ne sont pas prises en charge par Braze. {% multi_lang_include product_feedback_cta.md context="gap" feature="value-based custom audience sync" %}

### Braze procède-t-il au hachage des données avant de les envoyer aux partenaires d'Audience Sync ? {#does-braze-hash-data-before-sending-it-to-audience-sync-partners}

Une fois les données d'e-mail normalisées, Braze les hache avec SHA256.

**IDFA/AAID/téléphone :** Braze effectue le hachage avec SHA256. Les types d'audience que nous synchronisons sont toujours l'un des suivants :

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256.

En termes de fréquence, Braze ne hachera les informations personnelles identifiables (IPI) des utilisateurs que lorsque ceux-ci entreront dans l'étape Audience Sync du parcours utilisateur, en préparation de la synchronisation.

### Comment résoudre un problème lié à la synchronisation d'une audience personnalisée similaire basée sur la valeur ? {#how-do-i-resolve-an-issue-with-syncing-a-value-based-lookalike-custom-audience}

À l'heure actuelle, les audiences personnalisées similaires basées sur la valeur ne sont pas prises en charge par Braze. Si vous tentez de synchroniser avec cette audience, cela peut provoquer des erreurs au niveau de l'étape de synchronisation d'audience. Pour résoudre ce problème, suivez ces étapes :

1. Accédez à votre tableau de bord du gestionnaire de publicités Facebook et sélectionnez **Audiences**.
2. Sélectionnez **Create audience** > **Custom audience**.
3. Sélectionnez **Customer list**.
4. Téléchargez votre CSV ou liste sans la colonne **Value**. Sélectionnez **No, continue with a customer list that doesn't include customer value**.
5. Terminez la création de votre audience personnalisée.
6. Dans Braze, mettez à jour l'étape de synchronisation d'audience Facebook avec l'audience personnalisée que vous avez créée.

### J'ai reçu un e-mail relatif aux conditions de service des audiences personnalisées de Facebook. Que dois-je faire pour résoudre ce problème ? {#ive-received-an-email-related-to-facebook-custom-audience-terms-of-service-what-should-i-do-to-resolve-this}

Pour utiliser la synchronisation d'audience vers Facebook, vous devez accepter ces conditions de service.

- Si votre compte publicitaire est directement associé à votre compte Facebook personnel, vous pouvez accepter les conditions de service depuis votre compte personnel ici : `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- Si votre compte publicitaire est lié au compte Business Manager de votre entreprise, vous devez accepter les conditions de service dans votre compte Facebook Business Manager ici : `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

Après avoir accepté les conditions de service des audiences personnalisées Facebook, procédez comme suit :

1. Actualisez votre jeton d'accès Facebook avec Braze en déconnectant et reconnectant votre compte Facebook.
2. Réactivez votre étape de synchronisation d'audience Facebook en modifiant et en mettant à jour votre Canvas.

Ensuite, Braze peut synchroniser les utilisateurs dès qu'ils atteignent l'étape de synchronisation d'audience Facebook.

### Qu'est-il advenu des filtres **Connected Facebook** et **Number of Facebook Friends Using App** ? {#what-happened-to-the-connected-facebook-and-number-of-facebook-friends-using-app-filters}

Les filtres de segmentation Braze **Number of Facebook Friends Using App** et **Connected Facebook** sont obsolètes. Facebook et les SDK Braze ne collectent plus les données sous-jacentes sur lesquelles ces filtres reposaient.

Remplacez les filtres obsolètes par des attributs personnalisés, des événements personnalisés ou des Segments basés sur l'engagement — par exemple, la connexion Facebook ou le lien social au lieu de **Connected Facebook**, ou les recommandations, invitations et partages au lieu de **Number of Facebook Friends Using App**.

Pour le reciblage Canvas, faites correspondre les utilisateurs avec l'e-mail, le téléphone, le prénom et le nom de famille, comme démontré dans l'[étape 4 : Configuration de la synchronisation](#step-4-sync-setup). Pour élargir la portée, synchronisez un Segment à forte valeur avec Facebook et créez une audience similaire dans Meta Ads Manager.

## Résolution des problèmes {#troubleshooting}

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 40%;
}
table th:nth-child(2) {
    width: 40%;
}
table td {
    word-break: break-word;
}
</style>

<table aria-label="Résolution des problèmes">
  <thead>
    <tr>
      <th>Erreur</th>
      <th>Description</th>
      <th>Marche à suivre</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Invalid Token</b></td>
      <td>Les causes typiques sont les suivantes : l'utilisateur qui a connecté l'intégration change de mot de passe, les identifiants expirent, etc.</td>
      <td>Allez dans <b>Intégrations partenaires</b> > <b>Facebook</b> et déconnectez puis reconnectez votre compte. Consultez <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>cette section de résolution des problèmes</a> pour connaître les étapes supplémentaires de vérification de votre compte Facebook.</td>
    </tr>
    <tr>
      <td><b>Audience Size Too Low</b></td>
      <td>Cette erreur peut se produire si vous avez créé une étape de synchronisation d'audience qui supprime des utilisateurs de vos audiences. Si la taille de votre audience se rapproche de zéro, le réseau peut signaler que la taille de l'audience est trop petite pour être diffusée.</td>
      <td>Utilisez une stratégie de synchronisation d'audience qui ajoute et supprime régulièrement des utilisateurs, sans épuiser complètement la taille de l'audience.</td>
    </tr>
    <tr>
      <td><b>Audience Does Not Exist</b></td>
      <td>L'étape de synchronisation d'audience utilise une audience qui n'existe pas ou qui a été supprimée. Cela peut également se déclencher si vous n'avez plus les autorisations nécessaires pour accéder à l'audience.</td>
      <td>Demandez à un administrateur de vérifier sur la plateforme partenaire si l'audience existe toujours. <br><br>Si elle existe, confirmez que l'utilisateur qui a connecté l'intégration a l'autorisation d'accéder à l'audience. Si ce n'est pas le cas, l'utilisateur doit se voir accorder l'accès à cette audience. <br><br>Si l'audience a été supprimée intentionnellement, ajoutez une audience active et créez une nouvelle audience sur l'étape.</td>
    </tr>
    <tr>
      <td><b>Ad Account Access Attempt</b></td>
      <td>Vous ne disposez pas des autorisations pour le compte publicitaire ou l'audience que vous avez sélectionné.</td>
      <td>Travaillez avec les administrateurs de votre compte publicitaire pour obtenir l'accès et les autorisations nécessaires.</td>
    </tr>
    <tr>
      <td><b>Terms of Service Not Accepted</b></td>
      <td>Pour certaines destinations d'Audience Sync, comme Facebook, le réseau publicitaire exige que vous acceptiez des conditions de service spécifiques pour utiliser la fonctionnalité Audience Sync. Cette erreur se déclenche si vous n'avez pas accepté les conditions appropriées. Par conséquent, il se peut que vous ayez également reçu un e-mail de Braze avec ce sujet : « Your authorization credentials for Facebook are invalid ».</td>
      <td>Vérifiez que vous avez accepté les conditions requises par Facebook.</td>
    </tr>
    <tr>
      <td><b>All Users Are Erroring Out</b></td>
      <td>Si tous les utilisateurs obtiennent une erreur lors d'une étape alors qu'il a été confirmé que ces utilisateurs ont des valeurs pour les champs sélectionnés de l'étape, cela peut indiquer un problème avec votre compte Facebook.</td>
      <td>Suivez les étapes de <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>cette section de résolution des problèmes</a> pour vérifier que votre compte ne présente aucun problème.
      </td>
    </tr>
    <tr>
      <td><b>Failed to create audience</b></td>
      <td>Sur la page Facebook Technology Partner, vous voyez « Connected », mais il y a une erreur à l'étape Facebook Audience Sync lors de la synchronisation d'une audience : « Failed to create audience 'audience name' ». L'autorisation de votre compte Facebook a échoué. Visitez la page des partenaires technologiques pour reconnecter votre compte.</td>
      <td>Suivez les étapes de <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>cette section de résolution des problèmes</a> pour vérifier que votre compte ne présente aucun problème.
      </td>
    </tr>
    <tr>
      <td><b>Compte publicitaire absent du menu déroulant</b></td>
      <td>Lorsque vous configurez l'étape Facebook Audience, un compte publicitaire attendu n'apparaît pas dans le sélecteur de comptes publicitaires.</td>
      <td>Confirmez que votre application Facebook a terminé la <a href="https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management">révision d'application</a> pour <code>ads_management</code> avec le niveau d'accès requis par Facebook pour l'utilisation de l'API marketing. Dans <a href="https://business.facebook.com/">Facebook Business Manager</a>, confirmez que le jeton d'utilisateur système dispose des autorisations appropriées et est associé aux comptes publicitaires que vous utilisez dans Braze, et que les conditions du compte publicitaire sont acceptées. <br><br>Si le menu déroulant fonctionne sur un nouveau Canvas mais pas sur un Canvas que vous avez déjà modifié, essayez d'actualiser votre navigateur (ou de vider votre cache) et confirmez que vous êtes connecté en tant qu'utilisateur ayant toujours accès à ces comptes publicitaires.</td>
    </tr>
    <tr>
      <td><b>Erreur de validation du jeton d'accès</b></td>
      <td>Vous voyez une erreur concernant la validation du jeton d'accès Facebook lors de la connexion de Braze à Facebook ou lors de la synchronisation des audiences.</td>
      <td>Déconnectez-vous de Facebook dans votre navigateur. Dans Braze, allez dans <b>Intégrations partenaires</b> &gt; <b>Facebook</b>, supprimez les identifiants Facebook enregistrés, puis reconnectez Facebook. Sur la page des partenaires technologiques de Facebook pour Braze, déconnectez et reconnectez l'intégration si l'option est disponible. <br><br>Si les problèmes persistent, suivez la section <a href="#audit-your-facebook-account">Auditer votre compte Facebook</a>.</td>
    </tr>
    <tr>
      <td><b>Erreurs d'autorisation d'exportation ou de synchronisation d'audience</b></td>
      <td>L'exportation ou la synchronisation d'une audience Facebook échoue avec des erreurs d'autorisation, d'administration ou de compte publicitaire.</td>
      <td>Dans <a href="https://developers.facebook.com/">Meta for Developers</a>, ouvrez votre application et confirmez que votre utilisateur a un rôle <b>Admin</b> sous <b>App roles</b>. Sous <b>App settings</b> &gt; <b>Advanced</b>, confirmez que <b>Advertising accounts</b> inclut les comptes que vous utilisez avec Braze. Dans <a href="https://business.facebook.com/latest/settings">Business settings</a>, confirmez que l'utilisateur connecté ou l'utilisateur système a accès au bon compte publicitaire.</td>
    </tr>
  </tbody>
</table>

### Auditer votre compte Facebook {#audit-your-facebook-account}

Si vous rencontrez d'autres problèmes avec votre intégration, reportez-vous aux sections et étapes suivantes pour auditer votre compte Facebook.

#### Vérifier les autorisations du compte {#review-account-permissions}

1. Consultez la [documentation de Facebook](https://www.facebook.com/business/help/186007118118684?id=829106167281625) sur la manière de gérer ces autorisations dans leur plateforme. Pour Facebook Business Manager, vous devez au moins avoir un rôle d'**administrateur** ou d'**employé** Business Manager avec accès aux comptes publicitaires nécessaires.
2. En tant qu'**employé**, confirmez que l'administrateur vous accorde toutes les autorisations de **gestion du compte publicitaire** pour chaque compte publicitaire afin de créer une audience ou de synchroniser des utilisateurs avec l'audience.
3. Une fois cette autorisation accordée, vous devez déconnecter et reconnecter votre compte.

#### Accepter les conditions de service {#terms}

Acceptez toutes les conditions de service en attente de Facebook. Facebook vous demandera périodiquement, à vous (l'utilisateur) et au gestionnaire d'entreprise, de réapprouver ses conditions de service.

1. L'utilisateur connecté doit accepter toutes les conditions de service pour chacun de ses comptes publicitaires :
- Custom Audience TOS pour votre compte Facebook personnel :
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`

![Un compte disposant de toutes les autorisations de contrôle pour gérer un compte publicitaire.]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

Pour trouver votre ID de compte et d'entreprise, procédez comme suit :

1. Accédez à votre [compte Facebook Ads Manager](https://adsmanager.facebook.com/).
2. Confirmez que vous utilisez le bon compte publicitaire en le vérifiant dans le menu déroulant.
3. Dans l'URL, trouvez l'ID du compte après `act=` et l'ID de l'entreprise après `business_id=`

![L'URL avec l'ID du compte et l'ID de l'entreprise mis en évidence.]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. Lisez et sélectionnez **Accept** pour les conditions des audiences personnalisées. Nous vous recommandons de confirmer pour quel compte les conditions de service sont signées en utilisant le menu déroulant en haut des conditions.

![Le menu déroulant qui indique le compte qui signe les conditions de service.]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5. Vous devez sélectionner **Accept** pour les conditions de service. Ensuite, vous verrez apparaître ce message : « You have accepted these terms of service on behalf of Braze ».
6. Actualisez votre jeton d'accès Facebook avec Braze en déconnectant et reconnectant votre compte Facebook.
7. Réactivez votre étape de synchronisation d'audience Facebook en modifiant et en mettant à jour votre Canvas. Braze pourra alors synchroniser les utilisateurs dès qu'ils atteindront l'étape Facebook Audience.
8. Si le problème persiste, essayez d'utiliser un autre utilisateur disposant d'autorisations d'administration pour accepter manuellement les conditions via le gestionnaire de publicités.

#### Achever les tâches en suspens {#complete-any-pending-tasks}

Vérifiez si vous avez des tâches en attente avec Facebook qui pourraient vous empêcher d'utiliser les services Facebook Ads :

1. [Connectez-vous au gestionnaire de publicités Facebook](https://adsmanager.facebook.com/).
2. Sélectionnez le compte publicitaire avec lequel vous rencontrez des problèmes.
3. Dans la navigation, sélectionnez votre **Account Overview**. <br> ![La navigation avec Account Overview sélectionné.]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. Vérifiez s'il y a des alertes qui doivent être traitées. <br> ![Un compte avec une carte de crédit expirée.]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. Vérifiez s'il y a des tâches de configuration à effectuer. <br> ![Un compte dont la configuration est partiellement terminée.]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### Se connecter avec un autre utilisateur {#connect-with-a-different-user}

Dans le cadre d'une autre étape de résolution des problèmes, nous recommandons qu'un autre utilisateur administrateur essaie de connecter son compte en procédant comme suit :

1. Déconnectez l'intégration actuelle.
2. Un utilisateur distinct disposant de droits d'administration connecte son compte utilisateur Facebook.