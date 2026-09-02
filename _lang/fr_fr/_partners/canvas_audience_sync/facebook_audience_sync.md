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

## Synchronisation des utilisateurs et considérations relatives aux limites de débit {#user-syncing-and-rate-limit-considerations}

Lorsque les utilisateurs atteignent l'étape Audience Sync, Braze les synchronise en quasi-temps réel tout en respectant les limites de débit de l'API Marketing de Facebook. Braze regroupe et traite autant d'utilisateurs que possible toutes les 5 secondes avant de les envoyer à Facebook.

La limite de débit de l'API Marketing de Facebook n'autorise pas plus de &#126;190 000 requêtes API par compte publicitaire sur une période d'une heure. Si un client atteint cette limite, Braze retente la synchronisation pendant environ &#126;13 heures. Si la synchronisation n'est toujours pas possible, Braze répertorie ces utilisateurs dans l'indicateur Users Errored.

## Prérequis {#prerequisites}

Vous devrez confirmer que les éléments suivants ont été créés et complétés avant de configurer votre étape Facebook Audience dans Canvas.

| Exigence | Origine | Description |
| ----------- | ------ | ----------- |
| Facebook Business gestionnaire | [Facebook](https://www.facebook.com/business/help/113163272211510) | Un outil centralisé pour gérer les ressources Facebook de votre marque (par exemple, les comptes publicitaires, les pages et les applications). |
| Compte publicitaire Facebook | [Facebook](https://www.facebook.com/business/help/910137316041095) | Un compte publicitaire Facebook actif lié au Business gestionnaire de votre marque.<br><br>Assurez-vous que l'administrateur de votre Facebook Business gestionnaire vous a accordé les autorisations « Gérer les campagnes » ou « Gérer les comptes publicitaires » pour les comptes publicitaires Facebook que vous prévoyez d'utiliser avec Braze. Assurez-vous également d'avoir accepté les conditions générales de votre compte publicitaire. |
| Conditions d'utilisation des audiences personnalisées Facebook | [Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Acceptez les conditions d'utilisation des audiences personnalisées de Facebook pour les comptes publicitaires Facebook que vous prévoyez d'utiliser avec Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Se connecter à Facebook {#step-1-connect-to-facebook}

{% alert important %}
Vous devez disposer de la [permission « Admin »]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) pour connecter Facebook à votre compte Braze.
{% endalert %}

Dans le tableau de bord de Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Facebook**. Sous Facebook Audience Export, sélectionnez **Connect Facebook**.

![Page de la technologie Facebook dans Braze comprenant une section Aperçu et une section Facebook Audience Export avec le bouton Connect Facebook.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:85%;"}

Une fenêtre de dialogue oAuth Facebook apparaît pour autoriser Braze à créer des audiences personnalisées dans vos comptes publicitaires Facebook.

![La première boîte de dialogue Facebook invitant à « Se connecter en tant que X », où X est votre nom d'utilisateur Facebook.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![La deuxième boîte de dialogue Facebook demandant l'autorisation de gérer les publicités pour vos comptes publicitaires.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

Après avoir lié Braze à votre compte Facebook, sélectionnez les comptes publicitaires que vous souhaitez synchroniser au sein de votre espace de travail Braze. Une fois connecté, vous serez redirigé vers la page partenaire, où vous pourrez voir quels comptes sont connectés et déconnecter les comptes existants.

![Version mise à jour de la page des partenaires technologiques Facebook montrant les comptes publicitaires connectés avec succès.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:85%;"}

Votre connexion Facebook est appliquée au niveau de l'espace de travail Braze. Si votre administrateur Facebook vous retire de votre Facebook Business gestionnaire ou de l'accès aux comptes Facebook connectés, Braze détectera un jeton invalide. Par conséquent, vos Canvas actifs utilisant des composants Facebook Audience afficheront des erreurs, et Braze ne sera pas en mesure de synchroniser les utilisateurs.

{% alert important %}
Pour les clients ayant déjà effectué le processus de vérification de l'application Facebook pour [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) et [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard), votre jeton d'utilisateur système restera valide pour le composant Facebook Audience. Vous ne pourrez pas modifier ni révoquer le jeton d'utilisateur système Facebook via la page partenaire Facebook. En revanche, vous pouvez connecter votre compte Facebook pour remplacer votre jeton d'utilisateur système Facebook au sein de votre espace de travail Braze.

<br><br>La configuration oAuth Facebook s'appliquera également aux [exportations Facebook utilisant Segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook#prerequisites).
{% endalert %}

### Étape 2 : Accepter les conditions d'utilisation des audiences personnalisées {#step-2-accept-custom-audiences-terms-of-service}

Avant de créer votre Canvas, vous devez accepter les conditions d'utilisation Facebook suivantes aux liens ci-dessous :

- **Conditions relatives aux audiences personnalisées à partir de listes de clients pour votre compte personnel :** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- **Conditions relatives aux outils commerciaux Facebook pour votre compte professionnel :** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

![Exemple des conditions à accepter pour les audiences personnalisées à partir de listes de clients.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}){: style="max-width:85%;"}
![Exemple des conditions à accepter pour les outils commerciaux Facebook.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}){: style="max-width:85%;"}

Consultez la [section FAQ](#terms) pour plus de détails sur l'audit de votre compte Facebook lors de l'intégration.

### Étape 3 : Ajouter un composant Facebook Audience dans Canvas {#step-3-add-a-facebook-audience-component-in-canvas}

Ajoutez un composant dans votre Canvas et sélectionnez **Facebook Audience**.

![Liste des composants à ajouter au Canvas.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Le composant Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Étape 4 : Configuration de la synchronisation {#step-4-sync-setup}

Sélectionnez le bouton **Custom Audience** pour ouvrir l'éditeur de composant. Ensuite, sélectionnez **Facebook** comme partenaire Audience Sync.

![« Set up Audience Sync » avec les options de choix d'un partenaire.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Sélectionnez le compte publicitaire Facebook souhaité. Dans le menu déroulant **Choose a New or Existing Audience**, saisissez le nom d'une audience nouvelle ou existante.

{% tabs %}
{% tab Créer une nouvelle audience %}

1. Saisissez un nom pour la nouvelle audience personnalisée.
2. Sélectionnez **Add Users to Audience** et choisissez les champs que vous souhaitez synchroniser avec Facebook.
3. Ensuite, sélectionnez **Create Audience** pour enregistrer votre audience.

![Configuration de la synchronisation d'audience avec les informations d'e-mail, de téléphone, de prénom et de nom de famille à faire correspondre.]({% image_buster /assets/img/audience_sync/fb_sync.png %})

Vous êtes notifié en haut de l'éditeur d'étape si l'audience est créée avec succès ou si une erreur survient au cours de ce processus. Vous pouvez également référencer cette audience pour la suppression d'utilisateurs ultérieurement dans le parcours Canvas, car l'audience a été créée en mode brouillon.

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze crée la nouvelle audience personnalisée au lancement du Canvas, puis synchronise les utilisateurs en quasi-temps réel à mesure qu'ils entrent dans l'étape Audience Sync.

Chaque étape Audience Sync correspond à l'audience Facebook configurée pour cette étape. Lorsque le Canvas s'exécute à nouveau (par exemple, selon une planification récurrente), Braze synchronise les utilisateurs éligibles vers cette même audience — il ne crée pas une nouvelle audience Facebook à chaque exécution du Canvas.

{% endtab %}
{% tab Synchroniser avec une audience existante %}

Braze offre la possibilité d'ajouter ou de supprimer des utilisateurs d'audiences personnalisées Facebook existantes afin de confirmer que ces audiences sont à jour. Pour synchroniser avec une audience existante, procédez comme suit :

1. Saisissez le nom de l'audience existante dans le menu déroulant.
2. Choisissez si vous souhaitez **Add to the Audience** ou **Remove from the Audience**.
3. Braze ajoutera ou supprimera des utilisateurs en quasi-temps réel à mesure qu'ils entrent dans l'étape Facebook Audience.

![Configuration de la synchronisation d'audience pour supprimer les informations d'e-mail, de téléphone, de prénom et de nom de famille.]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
Facebook interdit la suppression d'utilisateurs d'audiences personnalisées lorsque la taille de l'audience est trop faible (généralement moins de 1 000 utilisateurs). Par conséquent, Braze ne peut pas synchroniser les utilisateurs pour une suppression depuis l'étape Audience Sync tant que l'audience n'a pas atteint la taille appropriée.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 5 : Lancer le Canvas {#step-5-launch-canvas}

Après avoir configuré votre composant Facebook Audience, il est temps de lancer le Canvas ! La nouvelle audience personnalisée est créée, et les utilisateurs qui passent par l'étape Facebook Audience sont transmis à cette audience personnalisée sur Facebook. Si votre Canvas contient des étapes ultérieures, vos utilisateurs passeront alors à l'étape suivante de leur parcours utilisateur.

L'onglet **History** de l'audience personnalisée dans le Facebook Audience gestionnaire reflétera le nombre d'utilisateurs envoyés à l'audience depuis Braze. Si un utilisateur entre à nouveau dans l'étape, il est renvoyé à Facebook.

![Détails de l'audience et onglet History pour une audience Facebook donnée, comprenant un tableau d'historique d'audience avec des colonnes pour l'activité, les détails de l'activité, les éléments modifiés, ainsi que la date et l'heure.]({% image_buster /assets/img/fb_audience_sync/audience_history.png %}){: style="max-width:80%;"}

## Comprendre les analyses {#understanding-analytics}

Le tableau suivant comprend les indicateurs et les descriptions pour vous aider à mieux comprendre les analyses de votre composant Audience Sync.

| Indicateur | Description |
| --- | --- |
| Entrés | Nombre d'utilisateurs qui sont entrés dans ce composant pour être synchronisés avec Facebook. |
| Passés à l'étape suivante | Nombre d'utilisateurs qui sont passés au composant suivant, s'il y en a un. Tous les utilisateurs avancent automatiquement s'il s'agit de la dernière étape de la branche Canvas. |
| Utilisateurs synchronisés | Nombre d'utilisateurs qui ont été synchronisés avec succès avec Facebook. |
| Utilisateurs non synchronisés | Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants pour la correspondance. Les champs sont mis en correspondance à l'aide d'un opérateur « OR », ce qui signifie que tant qu'un utilisateur possède l'un des champs dans Facebook, Facebook établira la correspondance avec l'utilisateur même s'il n'y a pas de correspondance sur tous les autres champs. |
| Utilisateurs en attente | Nombre d'utilisateurs en cours de traitement par Braze pour la synchronisation avec Facebook. |
| Utilisateurs en erreur | Nombre d'utilisateurs qui n'ont pas été synchronisés avec Facebook en raison d'une erreur d'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton Facebook invalide ou la suppression de l'audience personnalisée sur Facebook. |
| Sortis du Canvas | Nombre d'utilisateurs qui sont sortis du Canvas. Cela se produit lorsque la dernière étape d'un Canvas est une étape Facebook. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprendre les analyses" }

{% alert important %}
Il y a un délai dans le reporting pour les indicateurs d'utilisateurs synchronisés et d'utilisateurs en erreur en raison du traitement interne.
{% endalert %}

## Questions fréquemment posées {#frequently-asked-questions}

### Combien de temps faut-il pour que mes audiences apparaissent dans le tableau de bord de mon partenaire Audience Sync ? {#how-long-does-it-take-for-my-audiences-to-populate-in-my-audience-sync-partner-dashboard}

Le temps nécessaire pour remplir une audience dépend du partenaire spécifique. Tous les réseaux traitent les requêtes de Braze et tentent de faire correspondre les utilisateurs. La mise à jour des audiences personnalisées peut prendre jusqu'à 24 heures.

### Que dois-je faire si je reçois une erreur de jeton invalide ? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Vous pouvez simplement déconnecter et reconnecter votre compte Facebook sur la page partenaire Facebook. Confirmez auprès de l'administrateur de votre Facebook Business gestionnaire que vous disposez des autorisations appropriées pour le compte publicitaire avec lequel vous souhaitez synchroniser.

### Pourquoi mon Canvas ne peut-il pas être lancé ? {#why-is-my-canvas-not-allowed-to-launch}

- Assurez-vous que le jeton de votre utilisateur système est authentifié et a accès aux comptes publicitaires souhaités dans Facebook Business gestionnaire.
- Assurez-vous d'avoir sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience personnalisée et sélectionné les champs à faire correspondre.
- Vous avez peut-être atteint la limite de 500 audiences personnalisées sur Facebook. Accédez au gestionnaire d'audiences Facebook pour en supprimer certaines inutiles avant de créer de nouvelles audiences personnalisées à l'aide de Canvas.

### Comment savoir si des utilisateurs ont été mis en correspondance après avoir transmis des utilisateurs à Facebook ? {#how-do-i-know-if-users-have-matched-after-passing-users-to-facebook}

Facebook ne fournit pas cette information pour des raisons de confidentialité.

### Braze prend-il en charge les audiences personnalisées basées sur la valeur ? {#does-braze-support-value-based-custom-audiences}

Pour le moment, les audiences personnalisées basées sur la valeur ne sont pas prises en charge par Braze. {% multi_lang_include product_feedback_cta.md context="gap" feature="value-based custom audience sync" %}

### Braze hache-t-il les données avant de les envoyer aux partenaires Audience Sync ? {#does-braze-hash-data-before-sending-it-to-audience-sync-partners}

Une fois les données d'e-mail normalisées, Braze les hache avec SHA256.

**IDFA/AAID/téléphone :** Braze hache avec SHA256. Les types d'audiences que nous synchronisons sont toujours l'un des suivants :

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256.

En termes de fréquence, Braze ne hache les données d'identification personnelle (PII) des utilisateurs que lorsque ceux-ci entrent dans l'étape Audience Sync du parcours utilisateur, en préparation de la synchronisation.

### Comment résoudre un problème de synchronisation d'une audience personnalisée similaire basée sur la valeur ? {#how-do-i-resolve-an-issue-with-syncing-a-value-based-lookalike-custom-audience}

Pour le moment, les audiences personnalisées similaires basées sur la valeur ne sont pas prises en charge par Braze. Si vous tentez de synchroniser vers cette audience, cela peut provoquer des erreurs dans votre étape Audience Sync. Pour résoudre ce problème, suivez ces étapes :

1. Accédez à votre tableau de bord Facebook Ad gestionnaire et sélectionnez **Audiences**.
2. Sélectionnez **Créer une audience** > **Audience personnalisée**.
3. Sélectionnez **Liste de clients**.
4. Téléchargez votre CSV ou votre liste sans la colonne **Value**. Sélectionnez **No, continue with a customer list that doesn't include customer value**.
5. Terminez la création de votre audience personnalisée.
6. Dans Braze, mettez à jour l'étape Facebook Audience Sync avec l'audience personnalisée que vous avez créée.

### J'ai reçu un e-mail concernant les conditions d'utilisation des audiences personnalisées Facebook. Que dois-je faire pour résoudre ce problème ? {#ive-received-an-email-related-to-facebook-custom-audience-terms-of-service-what-should-i-do-to-resolve-this}

Pour utiliser Audience Sync vers Facebook, vous devez accepter ces conditions d'utilisation.

- Si votre compte publicitaire est directement associé à votre compte Facebook personnel, vous pouvez accepter les conditions d'utilisation depuis votre compte personnel ici : `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- Si votre compte publicitaire est lié au compte Business gestionnaire de votre entreprise, vous devez accepter les conditions d'utilisation dans votre compte Facebook Business gestionnaire ici : `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

Après avoir accepté les conditions d'utilisation des audiences personnalisées Facebook, procédez comme suit :

1. Actualisez votre jeton d'accès Facebook avec Braze en déconnectant et reconnectant votre compte Facebook.
2. Réactivez votre étape Facebook Audience Sync en modifiant et en mettant à jour votre Canvas.

Ensuite, Braze peut synchroniser les utilisateurs dès qu'ils atteignent l'étape Facebook Audience Sync.

### Qu'est-il advenu des filtres **Connected Facebook** et **Number of Facebook Friends Using App** ? {#what-happened-to-the-connected-facebook-and-number-of-facebook-friends-using-app-filters}

Les filtres de segmentation Braze **Number of Facebook Friends Using App** et **Connected Facebook** sont obsolètes. Facebook et les SDK Braze ne collectent plus les données sous-jacentes sur lesquelles ces filtres reposaient.

Remplacez les filtres obsolètes par des attributs personnalisés, des événements personnalisés ou des Segments basés sur l'engagement — par exemple, la connexion Facebook ou le lien social au lieu de **Connected Facebook**, ou les recommandations, invitations et partages au lieu de **Number of Facebook Friends Using App**.

Pour le reciblage Canvas, faites correspondre les utilisateurs avec l'e-mail, le téléphone, le prénom et le nom de famille, comme démontré dans l'[étape 4 : Configuration de la synchronisation](#step-4-sync-setup). Pour élargir la portée, synchronisez un Segment à forte valeur vers Facebook et créez une audience similaire dans Meta Ads gestionnaire.

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
      <th>Étapes de résolution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Jeton invalide</b></td>
      <td>Les causes typiques sont le changement de mot de passe par l'utilisateur qui a connecté l'intégration, l'expiration des identifiants, etc.</td>
      <td>Accédez à <b>Partner Integrations</b> > <b>Facebook</b> et déconnectez puis reconnectez votre compte. Consultez <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>cette section de résolution des problèmes</a> pour des étapes supplémentaires afin d'auditer votre compte Facebook.</td>
    </tr>
    <tr>
      <td><b>Taille d'audience trop faible</b></td>
      <td>Cette erreur peut survenir si vous avez créé une étape Audience Sync qui supprime des utilisateurs de vos audiences. Si la taille de votre audience approche zéro, le réseau peut signaler que la taille de l'audience est trop petite pour être diffusée.</td>
      <td>Utilisez une stratégie Audience Sync qui ajoute et supprime régulièrement des utilisateurs, sans vider complètement l'audience.</td>
    </tr>
    <tr>
      <td><b>L'audience n'existe pas</b></td>
      <td>L'étape Audience Sync utilise une audience qui n'existe pas ou qui a été supprimée. Cela peut également se déclencher si vous n'avez plus les autorisations nécessaires pour accéder à l'audience.</td>
      <td>Demandez à un administrateur de vérifier sur la plateforme partenaire si l'audience existe toujours. <br><br>Si elle existe, vérifiez si l'utilisateur qui a connecté l'intégration dispose des autorisations pour cette audience. Si ce n'est pas le cas, l'accès à cette audience doit lui être accordé. <br><br>Si l'audience a été intentionnellement supprimée, ajoutez une audience active et créez une nouvelle audience dans l'étape.</td>
    </tr>
    <tr>
      <td><b>Tentative d'accès au compte publicitaire</b></td>
      <td>Vous ne disposez pas des autorisations pour le compte publicitaire ou l'audience que vous avez sélectionné.</td>
      <td>Travaillez avec les administrateurs de votre compte publicitaire pour obtenir les accès et autorisations appropriés.</td>
    </tr>
    <tr>
      <td><b>Conditions d'utilisation non acceptées</b></td>
      <td>Pour certaines destinations Audience Sync, comme Facebook, le réseau publicitaire exige l'acceptation de conditions d'utilisation spécifiques pour utiliser la fonctionnalité Audience Sync. Cette erreur se déclenche si vous n'avez pas accepté les conditions appropriées. Par conséquent, vous avez peut-être également reçu un e-mail de Braze avec l'objet suivant : « Your authorization credentials for Facebook are invalid. »</td>
      <td>Vérifiez que vous avez accepté les conditions requises par Facebook.</td>
    </tr>
    <tr>
      <td><b>Tous les utilisateurs génèrent des erreurs</b></td>
      <td>Si tous les utilisateurs génèrent des erreurs sur une étape alors que vous avez confirmé que ces utilisateurs ont des valeurs pour les champs sélectionnés dans l'étape, cela pourrait indiquer un problème avec votre compte Facebook.</td>
      <td>Suivez les étapes de <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>cette section de résolution des problèmes</a> pour vérifier votre compte et identifier d'éventuels problèmes.
      </td>
    </tr>
    <tr>
      <td><b>Échec de la création de l'audience</b></td>
      <td>Sur la page de partenaire technologique Facebook, vous voyez « Connected », mais une erreur apparaît sur l'étape Facebook Audience Sync lors de la synchronisation d'une audience : « Failed to create audience 'audience name' ». L'autorisation de votre compte Facebook a échoué. Rendez-vous sur la page des partenaires technologiques pour reconnecter votre compte.</td>
      <td>Suivez les étapes de <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>cette section de résolution des problèmes</a> pour vérifier votre compte et identifier d'éventuels problèmes.
      </td>
    </tr>
    <tr>
      <td><b>Compte publicitaire absent du menu déroulant</b></td>
      <td>Lorsque vous configurez l'étape Facebook Audience, un compte publicitaire attendu n'apparaît pas dans le sélecteur de comptes publicitaires.</td>
      <td>Vérifiez que votre application Facebook a terminé la <a href="https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management">vérification d'application</a> pour <code>ads_management</code> avec le niveau d'accès requis par Facebook pour l'utilisation de l'API Marketing. Dans <a href="https://business.facebook.com/">Facebook Business gestionnaire</a>, vérifiez que le jeton de l'utilisateur système dispose des bonnes autorisations, qu'il est associé aux comptes publicitaires que vous utilisez dans Braze et que les conditions des comptes publicitaires sont acceptées. <br><br>Si le menu déroulant fonctionne sur un nouveau Canvas mais pas sur un Canvas que vous avez déjà modifié, essayez d'actualiser votre navigateur (ou de vider votre cache) et vérifiez que vous êtes connecté en tant qu'utilisateur ayant toujours accès à ces comptes publicitaires.</td>
    </tr>
    <tr>
      <td><b>Erreur de validation du jeton d'accès</b></td>
      <td>Vous voyez une erreur concernant la validation du jeton d'accès Facebook lors de la connexion de Braze à Facebook ou lors de la synchronisation des audiences.</td>
      <td>Déconnectez-vous de Facebook dans votre navigateur. Dans Braze, accédez à <b>Partner Integrations</b> &gt; <b>Facebook</b>, supprimez les identifiants Facebook enregistrés, puis reconnectez Facebook. Sur la page des partenaires technologiques de Facebook pour Braze, déconnectez et reconnectez l'intégration si l'option est disponible. <br><br>Si les problèmes persistent, suivez les étapes de la section <a href="#audit-your-facebook-account">Auditer votre compte Facebook</a>.</td>
    </tr>
    <tr>
      <td><b>Erreurs d'autorisation d'exportation ou de synchronisation d'audience</b></td>
      <td>L'exportation ou la synchronisation d'une audience Facebook échoue avec des erreurs d'autorisation, d'administration ou de compte publicitaire.</td>
      <td>Dans <a href="https://developers.facebook.com/">Meta for Developers</a>, ouvrez votre application et vérifiez que votre utilisateur dispose d'un rôle <b>Admin</b> sous <b>App roles</b>. Sous <b>App settings</b> &gt; <b>Advanced</b>, vérifiez que <b>Advertising accounts</b> inclut les comptes que vous utilisez avec Braze. Dans <a href="https://business.facebook.com/latest/settings">Business settings</a>, vérifiez que l'utilisateur connecté ou l'utilisateur système a accès au bon compte publicitaire.</td>
    </tr>
  </tbody>
</table>

### Auditer votre compte Facebook {#audit-your-facebook-account}

Si vous rencontrez des problèmes supplémentaires avec votre intégration, consultez les sections et étapes suivantes pour auditer votre compte Facebook.

#### Vérifier les autorisations du compte {#review-account-permissions}

1. Consultez [la documentation de Facebook](https://www.facebook.com/business/help/186007118118684?id=829106167281625) sur la gestion de ces autorisations dans leur plateforme. Pour Facebook Business gestionnaire, vous devez disposer au minimum d'un rôle **Admin** ou **employé** dans Business gestionnaire avec accès aux comptes publicitaires nécessaires.
2. En tant qu'**employé**, vérifiez que l'administrateur vous accorde les autorisations complètes **Manage Ad Account** pour chaque compte publicitaire afin de créer une audience ou de synchroniser des utilisateurs vers l'audience.
3. Une fois ces autorisations accordées, vous devez déconnecter puis reconnecter votre compte.

#### Accepter les conditions d'utilisation {#terms}

Acceptez toutes les conditions d'utilisation (TOS) en attente de Facebook. Facebook exige périodiquement que vous (l'utilisateur) et le gestionnaire d'entreprise réapprouviez leurs conditions d'utilisation.

1. L'utilisateur connecté doit accepter toutes les conditions d'utilisation pour chacun de ses comptes publicitaires :
- Conditions d'utilisation des audiences personnalisées pour votre compte Facebook personnel :
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`

![Un compte disposant des autorisations de contrôle total pour gérer un compte publicitaire.]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

Pour trouver votre identifiant de compte et votre identifiant d'entreprise, suivez ces étapes :

1. Accédez à votre [compte Facebook Ads gestionnaire](https://adsmanager.facebook.com/).
2. Vérifiez que vous utilisez le bon compte publicitaire en le confirmant dans le menu déroulant.
3. Dans l'URL, trouvez l'identifiant du compte après `act=` et l'identifiant de l'entreprise après `business_id=`

![L'URL avec l'identifiant du compte et l'identifiant de l'entreprise mis en évidence.]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. Lisez et sélectionnez **Accept** pour les conditions d'utilisation des audiences personnalisées. Nous vous recommandons de vérifier pour quel compte les conditions d'utilisation sont signées en utilisant le menu déroulant en haut des conditions.

![Le menu déroulant affichant le compte qui signe les conditions d'utilisation.]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5. Vous devez sélectionner **Accept** pour les conditions d'utilisation. Ensuite, vous verrez ce message : « You have accepted these terms of service on behalf of Braze ».
6. Actualisez votre jeton d'accès Facebook avec Braze en déconnectant puis reconnectant votre compte Facebook.
7. Réactivez votre étape Facebook Audience Sync en modifiant et en mettant à jour votre Canvas. Braze pourra alors synchroniser les utilisateurs dès qu'ils atteindront l'étape Facebook Audience.
8. Si le problème persiste, essayez d'utiliser un autre utilisateur disposant d'autorisations d'administrateur pour accepter manuellement les conditions via Ads gestionnaire.

#### Effectuer les tâches en attente {#complete-any-pending-tasks}

Vérifiez si vous avez des tâches en attente avec Facebook qui pourraient vous empêcher d'utiliser les services Facebook Ads :

1. [Connectez-vous à Facebook Ads gestionnaire](https://adsmanager.facebook.com/).
2. Sélectionnez le compte publicitaire avec lequel vous rencontrez des problèmes.
3. Dans la navigation, sélectionnez votre **Account Overview**. <br> ![La navigation avec Account Overview sélectionné.]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. Vérifiez s'il y a des alertes à traiter. <br> ![Un compte avec une carte de crédit expirée.]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. Vérifiez s'il y a des tâches de configuration à terminer. <br> ![Un compte avec une configuration partiellement terminée.]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### Se connecter avec un autre utilisateur {#connect-with-a-different-user}

Comme étape de résolution supplémentaire, nous recommandons qu'un autre utilisateur administrateur essaie de connecter son compte en procédant comme suit :

1. Déconnectez l'intégration actuelle.
2. Un autre utilisateur disposant d'autorisations d'administrateur connecte son compte utilisateur Facebook.