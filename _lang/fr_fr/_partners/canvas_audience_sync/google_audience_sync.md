---
nav_title: Google
article_title: "Synchronisation de l'audience de Canvas avec Google"
alias: /google_audience_sync/
description: "Cet article de référence vous explique comment synchroniser l'audience Braze avec Google pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
tool:
  - Canvas
page_order: 3

---

# Synchronisation de l'audience avec Google {#audience-sync-to-google}

{% alert important %}
Google met à jour ses [règles de consentement des utilisateurs de l'Union européenne](https://www.google.com/about/company/user-consent-policy/) en réponse aux changements apportés à la [loi sur les marchés numériques (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), en vigueur à partir du 6 mars 2024. Ce nouveau changement oblige les annonceurs à divulguer certaines informations à leurs utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse, ainsi qu'à obtenir d'eux le consentement nécessaire. Consultez la documentation suivante pour en savoir plus.
{% endalert %}

L'intégration de la synchronisation de l'audience Braze avec Google permet aux marques d'étendre la portée de leurs parcours clients cross-canal à Google Search, Google Shopping, Gmail, YouTube et Google Display. Grâce à vos données clients first-party, vous pouvez diffuser en toute sécurité des publicités basées sur des déclencheurs comportementaux dynamiques, la segmentation, etc. Tous les critères que vous utilisez habituellement pour déclencher un message (par exemple, notification push, e-mail ou SMS) dans le cadre d'un Canvas Braze peuvent être utilisés pour déclencher un message publicitaire à l'intention de cet utilisateur grâce à la fonction [Customer Match](https://support.google.com/google-ads/answer/6379332?hl=en) de Google.

{% alert note %}
L'intégration de Braze Audience Sync to Google est prise en charge pour Google Ads, et non pour Google Ads Manager.
{% endalert %}

Google Ads ne génère plus d'audiences similaires, également appelées « lookalike audiences », pour le ciblage et la création de rapports. Pour en savoir plus, consultez la [documentation de Google Ads](https://support.google.com/google-ads/answer/12463119?).

**Les cas d'usage courants pour la synchronisation des audiences personnalisées sont les suivants :**
- Le ciblage des utilisateurs à forte valeur ajoutée via plusieurs canaux pour stimuler les achats ou l'engagement.
- Le reciblage des utilisateurs qui réagissent moins aux autres canaux de marketing.
- La création d'audiences de suppression pour éviter que les utilisateurs ne reçoivent des publicités alors qu'ils sont déjà des consommateurs fidèles de votre marque.

{% alert note %}
Cette fonctionnalité permet aux marques de contrôler quelles données first-party spécifiques sont partagées avec Google. Chez Braze, les intégrations avec lesquelles vous pouvez ou non partager vos données first-party font l'objet de la plus grande attention. En savoir plus sur notre [politique de confidentialité des données de Braze](https://www.braze.com/privacy).
{% endalert %}

## Conditions préalables {#prerequisites}

Assurez-vous que les éléments suivants sont créés et complétés avant de configurer votre étape Google Audience dans Canvas.

| Condition | Origine | Description |
| ----------- | ------ | ----------- |
| Compte Google Ads | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | Un compte Google Ads actif pour votre marque.<br><br>Si vous souhaitez partager une audience entre plusieurs comptes gérés, vous pouvez télécharger vos audiences dans votre [compte gestionnaire](https://support.google.com/google-ads/answer/6139186). |
| Conditions d'utilisation des annonces Google et règles d'utilisation des annonces Google | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | Vous devez accepter et vous assurer de respecter les [conditions d'utilisation des annonces](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40) de Google et les [règles des annonces de Google](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC), qui incluent la [politique de consentement de l'utilisateur de l'UE](https://www.google.com/about/company/user-consent-policy/), selon ce qui vous est applicable, dans le cadre de votre utilisation de la synchronisation d'audiences Braze.<br><br>Consultez votre équipe juridique sur les nouvelles règles de Google en matière de consentement des utilisateurs de l'UE afin de vous assurer que vous recueillez le consentement approprié pour utiliser les services Google Ads pour vos utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse. |
| Google Customer Match | [Google](https://support.google.com/google-ads/answer/6299717) | Le service Customer Match n'est pas disponible pour tous les annonceurs.<br><br>**Pour utiliser le service Customer Match, votre compte doit disposer des éléments suivants :**<br>• Des antécédents satisfaisants en matière de respect des politiques<br>• De bons antécédents de paiement<br>• Au moins 90 jours d'expérience dans Google Ads<br>• Plus de 50 000 USD de dépenses totales au cours de la vie. Pour les annonceurs dont les comptes sont gérés dans des devises autres que l'USD, le montant de vos dépenses sera converti en USD en utilisant le taux de conversion mensuel moyen pour cette devise.<br><br>Si votre compte ne répond pas à ces critères, il n'est pas éligible au programme Customer Match.<br><br>Contactez votre conseiller Google Ads pour plus d'informations sur la disponibilité de Customer Match pour votre compte. |
| Signaux de consentement de Google | [Google](https://support.google.com/google-ads/answer/14310715) | Si vous souhaitez diffuser des annonces auprès des utilisateurs finaux de l'EEE en utilisant le service Customer Match de Google, vous devez transmettre à Braze les attributs personnalisés suivants (booléens) dans le cadre de la politique de consentement des utilisateurs de l'UE de Google. Vous trouverez plus de détails à la rubrique [Collecte du consentement pour les utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse](#collecting-consent-for-eea-uk-and-switzerland-end-users) : <br> - `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Conditions préalables" }

### Versions requises du SDK {#required-sdk-versions}

Lorsque vous utilisez les SDK de Braze pour collecter des signaux de consentement, assurez-vous de respecter les versions minimales suivantes :

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### Collecte du consentement pour les utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse {#collecting-consent-for-eea-uk-and-switzerland-end-users}

Les règles de Google en matière de consentement des utilisateurs de l'UE exigent que les annonceurs divulguent les éléments suivants à leurs utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse, et qu'ils obtiennent leur consentement à cet égard :

* L'utilisation de cookies ou d'autres moyens de stockage local lorsque la loi l'exige ; et
* La collecte, le partage et l'utilisation de leurs données personnelles pour la personnalisation des publicités.

Cela n'affecte pas les utilisateurs finaux américains ou tout autre utilisateur final situé en dehors de l'EEE, du Royaume-Uni ou de la Suisse. Consultez votre équipe juridique sur les nouvelles règles de Google en matière de consentement des utilisateurs de l'UE afin de vous assurer que vous recueillez le consentement approprié pour utiliser les services de Google Ads pour vos utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse.

En vertu des exigences de la loi sur les marchés numériques (DMA) en vigueur à partir du 6 mars 2024, les annonceurs doivent transmettre le consentement des utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse lorsqu'ils partagent des données avec Google. Dans le cadre de ce changement, vous pouvez collecter les deux signaux de consentement dans Braze sous la forme des attributs personnalisés booléens suivants :

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze synchronisera les données de ces attributs personnalisés avec les [champs de consentement appropriés dans Google](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A).

#### Gestion des consentements révoqués {#managing-revoked-consent}

Pour maintenir vos listes d'audience à jour dans le cas où un utilisateur final de l'EEE a été ajouté à la liste d'audience, puis a ensuite rétracté l'un des deux consentements (`$google_ad_user_data` ou `$google_ad_personalization`), vous devez configurer un Canvas pour supprimer les utilisateurs des listes d'audience existantes à l'aide d'une étape de synchronisation d'audience.

{% alert note %}
Si un utilisateur de l'EEE a précédemment donné son consentement pour les deux signaux, ces données continueront d'être utilisées pour le Customer Match de Google jusqu'à ce que cette liste expire, ou que cet état de consentement soit explicitement mis à jour via la synchronisation de l'audience Google, ou les deux.
{% endalert %}

#### Conseils {#tips}

* Envoyez la valeur en tant que valeur booléenne, et non de chaîne de caractères.
* Le nom de l'attribut est précédé du signe du dollar ($). Braze utilise un signe de dollar au début du nom d'un attribut pour indiquer qu'il s'agit d'une clé spéciale et réservée.
* Saisissez le nom de l'attribut en minuscules.
* Bien que vous ne puissiez pas explicitement définir un utilisateur comme non spécifié, si vous envoyez une valeur `null` ou `nil` ou toute autre valeur qui n'est pas `true` ou `false`, Braze transmettra cet utilisateur à Google en tant que `UNSPECIFIED`.
* Les nouveaux utilisateurs ajoutés ou mis à jour sans spécifier l'un ou l'autre des attributs de consentement seront synchronisés avec Google avec ces attributs de consentement marqués comme non spécifiés.

Si vous tentez de synchroniser un utilisateur de l'EEE sans les champs de consentement nécessaires et le statut accordé, Google rejettera cette tentative et ne diffusera pas d'annonces à cet utilisateur. En outre, si une publicité est diffusée à un utilisateur de l'EEE sans son consentement explicite, vous pouvez en être tenu responsable et encourir un risque financier. Pour éviter cela, nous vous suggérons d'envoyer des campagnes avec des filtres de segmentation qui n'incluent que les utilisateurs de l'EEE, du Royaume-Uni et de la Suisse ayant des attributs de consentement Google `true`. Pour plus de détails concernant la politique de consentement des utilisateurs de l'UE pour les partenaires de chargement de Customer Match, consultez les [FAQ](https://support.google.com/google-ads/answer/14310715) de Google.

### Configurer votre Canvas {#setting-up-your-canvas}

Après votre synchronisation avec Braze, les attributs de consentement suivants seront disponibles sur vos profils utilisateurs et pour la segmentation :

- `$google_ad_user_data`
- `$google_ad_personalization`

Dans tous les Canvas où vous ciblez des utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse en utilisant Google Audience Sync pour ajouter des utilisateurs à une audience, vous devez exclure ces utilisateurs lorsque les deux attributs de consentement ont une valeur qui n'est pas `true`. Vous pouvez le faire en segmentant ces utilisateurs lorsque les valeurs de consentement sont définies sur `true`. Cela garantit également que les analyses plus précises des utilisateurs sont synchronisées, car nous savons que Google rejettera ces utilisateurs des audiences. Notez que si vous utilisez Google Audience Sync pour supprimer des utilisateurs d'une audience, les attributs de consentement ne sont pas nécessaires.

## Intégration {#integration}

### Étape 1 : Connectez votre compte Google {#step-1-connect-google-account}

{% alert important %}
Vous devez disposer de l'[autorisation « Admin »]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) pour connecter Google Ads à votre compte Braze.
{% endalert %}

Pour commencer, allez dans **Intégrations partenaires** > **Partenaires technologiques** > **Google Ads** et sélectionnez **Connect Google Ads**. Une fenêtre modale vous invite à sélectionner l'e-mail associé à votre compte Google Ads, puis à accorder à Braze l'accès à votre compte Google Ads.

Après avoir connecté votre compte Google Ads, vous serez redirigé vers votre page partenaire Google Ads. Vous serez ensuite invité à sélectionner les comptes publicitaires auxquels vous souhaitez accéder dans l'espace de travail de Braze.

![Un GIF qui montre le déroulement d'une connexion réussie d'un compte Google Ads à Braze.]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

#### Exporter les IDFA iOS ou les ID Google Advertising {#export-ios-idfa-or-google-advertising-ids}

Si vous prévoyez d'exporter des IDFA iOS ou des ID Google Advertising dans votre synchronisation d'audience, Google a besoin de votre ID d'application iOS et de votre ID d'application Android au sein des requêtes. Sous Google Audience Sync, sélectionnez **Add Mobile Advertising IDs**, saisissez l'ID de votre application iOS et l'ID de votre application Android (nom du package de l'application), puis enregistrez chacun d'entre eux.

<br><br>
![La page technologique Google Ads mise à jour montre les comptes publicitaires connectés, ce qui vous permet de resynchroniser les comptes et d'ajouter des ID de publicité mobile.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
<br><br>

Si vous avez plusieurs applications dans un même espace de travail, vous pouvez saisir n'importe lequel de vos ID d'application dans la configuration, car les ID de publicité mobile pour vos utilisateurs seront les mêmes dans plusieurs applications. En effet, le GAID Android et l'IDFA iOS sont des identifiants publicitaires universels sur l'appareil et ne sont pas spécifiques à une application. Pour synchroniser les ID de publicité mobile pour les utilisateurs d'une application spécifique, vous pouvez utiliser des filtres de segmentation (« Dernière utilisation d'une application spécifique » ou « Version la plus récente de l'application ») pour cibler ces utilisateurs.

### Étape 2 : Ajouter une étape Google Audience dans Canvas {#step-2-add-a-google-audience-step-in-canvas}

Ajoutez un composant dans votre Canvas, puis sélectionnez **Audience Sync**.

![Menu permettant de sélectionner un composant Canvas dans l'éditeur.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![L'étape de synchronisation de l'audience ajoutée au parcours de l'utilisateur.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Étape 3 : Configuration de la synchronisation {#step-3-sync-setup}

1. Sélectionnez **Custom Audience** pour ouvrir l'éditeur de composants.
2. Sélectionnez **Google** comme partenaire de la synchronisation de l'audience.

![Les paramètres de l'étape de synchronisation de l'audience avec l'option de sélectionner un partenaire pour commencer la synchronisation.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

{: start="3"}
3. Sélectionnez le compte Google Ads souhaité.
4. Dans la liste déroulante **Choose a New or Existing Audience**, saisissez le nom d'une audience nouvelle ou existante.

{% tabs %}
{% tab Créer une nouvelle audience %}

1. Saisissez un nom pour la nouvelle audience personnalisée.
2. Sélectionnez **Add Users to Audience**.
3. Sélectionnez les données first-party des champs d'utilisateurs à envoyer à votre audience. Vous pouvez choisir l'un des deux champs suivants :

- **Customer Contact Info** : contient l'e-mail ou le numéro de téléphone de vos utilisateurs, ou les deux, s'ils existent dans Braze. Google exige qu'il s'agisse d'un seul champ à synchroniser et non d'identifiants distincts. Vous pouvez toujours utiliser ce champ unique si vous n'avez qu'un seul des identifiants.
- **Mobile Advertiser ID** : sélectionnez soit IDFA pour iOS, soit GAID pour Android. En raison des exigences de Google en matière de Customer Match, vous ne pouvez pas avoir les deux ID d'annonceurs mobiles dans les mêmes listes de clients.

{% alert note %}
**À propos de la bannière « Missing Mobile Ad IDs? Let's fix that. » :** lorsque vous vous synchronisez avec une audience en utilisant iOS IDFA ou Android GAID comme champ à faire correspondre, ce message peut apparaître dans l'éditeur d'étape. Il s'agit d'une **information et non d'une erreur**. Il vous rappelle de confirmer que le champ d'ID de publicité mobile sur lequel vous effectuez la correspondance existe dans vos données d'audience (par exemple, que les utilisateurs du parcours Canvas ont l'identifiant correspondant collecté). Vous pouvez l'écarter après avoir vérifié vos données.
{% endalert %}

{: start="4"}
4. Ensuite, enregistrez votre audience en sélectionnant le bouton **Create Audience** en bas de l'éditeur d'étape.

![Vue élargie du composant d'audience personnalisée. Ici, le compte publicitaire souhaité est sélectionné, une nouvelle audience est créée et la case « customer contact info » est cochée.]({% image_buster /assets/img/audience_sync/g_sync.png %})

Les utilisateurs seront avertis en haut de l'éditeur d'étape si l'audience est créée avec succès ou si des erreurs surviennent au cours de ce processus. Les utilisateurs peuvent faire référence à cette audience pour la supprimer plus tard dans le parcours Canvas, car l'audience a été créée en mode brouillon.

![Une alerte qui apparaît après la création d'une nouvelle audience dans le composant Canvas.]({% image_buster /assets/img/audience_sync/g_sync3.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze crée une nouvelle audience personnalisée dès le lancement du Canvas et synchronise ensuite les utilisateurs quasiment en temps réel lorsqu'ils entrent dans l'étape Google Audience.

{% alert important %}
Compte tenu des exigences de Google en matière de Customer Match, vous ne pouvez pas avoir les coordonnées des clients et les ID des annonceurs mobiles dans les mêmes listes de clients. Google Customer Match utilisera ensuite ces informations pour déterminer quels utilisateurs de Google Search, Google Display, YouTube et Gmail peuvent être ciblés. Pour plus de détails sur les exigences de Google Customer Match, consultez leur [documentation](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
{% endalert %}
{% endtab %}
{% tab Synchroniser avec une audience existante %}

Braze offre également la possibilité d'ajouter ou de supprimer des utilisateurs des listes de clients Google existantes afin de s'assurer que ces audiences sont à jour. Pour se synchroniser avec une audience existante :

1. Sélectionnez une audience personnalisée existante à synchroniser.
2. Choisissez si vous voulez **Add to the audience** ou **Remove from the audience**.
3. Braze ajoutera ou supprimera des utilisateurs quasiment en temps réel lorsqu'ils entreront dans l'étape Google Audience.
4. Après avoir configuré votre étape Google Audience, sélectionnez **Done**. Votre étape Google Audience contiendra des détails sur la nouvelle audience.

![Vue élargie du composant d'audience personnalisée. Ici, le compte publicitaire souhaité et l'audience existante sont sélectionnés, ainsi que le bouton radio « Add user to Audience ».]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Lancer le Canvas {#step-4-launch-canvas}

Complétez le reste de votre parcours utilisateur dans Canvas, puis lancez-le ! Si vous avez opté pour la création d'une nouvelle audience, Braze créera l'audience dans Google et ajoutera ensuite des utilisateurs au fur et à mesure qu'ils atteignent cette étape du Canvas. Si vous avez choisi d'ajouter ou de supprimer des utilisateurs d'une audience existante, Braze ajoutera ou supprimera des utilisateurs lorsqu'ils atteindront cette étape de leur parcours utilisateur.

Les utilisateurs passent alors au composant suivant du Canvas, s'il y en a un, ou quittent le Canvas s'il s'agit de la dernière étape du parcours de l'utilisateur.

## Considérations relatives à la synchronisation des utilisateurs et à la limite de débit {#user-syncing-and-rate-limit-considerations}

Lorsque les utilisateurs atteignent le composant de synchronisation de l'audience, Braze synchronise ces utilisateurs en temps quasi réel tout en respectant les limites de débit de l'API Google Ads. Concrètement, Braze essaie de regrouper et de traiter autant d'utilisateurs que possible toutes les 5 secondes avant de les envoyer à Google.

Lorsqu'un client est sur le point d'atteindre la limite de débit de l'API Google Ads, Google fournit à Braze des recommandations de réessai. Si un client de Braze atteint sa limite de débit, le Canvas Braze tentera à nouveau la synchronisation pendant environ 13 heures. Si la synchronisation n'est pas possible, ces utilisateurs sont répertoriés sous l'indicateur Users Errored.

## Présentation des analyses {#understanding-analytics}

Le tableau suivant comprend des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses réalisées au cours de l'étape de synchronisation de l'audience.

| Indicateur | Description |
| ------ | ----------- |
| *Entered* | Nombre d'utilisateurs qui ont franchi cette étape pour être synchronisés avec Google. |
| *Proceeded to Next Step* | Nombre d'utilisateurs ayant avancé au composant suivant, s'il y en a un. Tous les utilisateurs avanceront automatiquement. S'il s'agit de la dernière étape de la branche du Canvas, cet indicateur sera égal à 0. |
| *Users Synced* | Nombre d'utilisateurs dont la synchronisation avec Google a réussi. |
| *User Not Synced* | Nombre d'utilisateurs qui n'ont pas été synchronisés parce qu'il manquait des champs à faire correspondre ou parce que l'attribut de consentement était défini sur `false`. |
| *Users Errored* | Nombre d'utilisateurs qui n'ont pas été synchronisés avec Google en raison d'une erreur, après environ 13 heures de tentatives. En cas d'erreurs spécifiques, telles que les interruptions de service de l'API Google Ads, Canvas tentera de synchroniser pendant environ 13 heures. Si la synchronisation n'est toujours pas possible à ce stade, le champ *User Not Synced* sera rempli. |
| *Users Pending* | Nombre d'utilisateurs dont la synchronisation avec Google est en cours de traitement par Braze. |
| *Exited Canvas* | Nombre d'utilisateurs ayant quitté le Canvas. Un utilisateur quitte le Canvas lorsque la dernière étape d'un Canvas est une étape Google. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Présentation des analyses" }

## Foire aux questions {#frequently-asked-questions}

### Pourquoi ne puis-je pas sélectionner plusieurs champs à faire correspondre dans ma configuration de Google Audience Step ? {#why-can-i-not-select-multiple-fields-to-match-in-my-google-audience-step-configuration}

Google Customer Match a des exigences strictes en ce qui concerne le formatage de ces audiences et les informations sur les clients qui y figurent. Plus précisément, les ID des annonceurs mobiles doivent être chargés séparément des informations de contact des clients (telles que l'e-mail et le numéro de téléphone). Pour plus de détails, consultez la [documentation de Google Customer Match](https://support.google.com/google-ads/answer/7659867?hl=en#undefined).

### Combien de temps faudra-t-il pour que mes audiences se synchronisent dans Google ? {#how-long-will-it-take-for-my-audiences-to-sync-in-google}

Il faut compter entre 6 et 12 heures pour qu'une audience soit synchronisée dans Google.

### J'ai synchronisé une audience, alors pourquoi la taille de l'audience est-elle nulle dans Google ? {#ive-synced-an-audience-so-why-is-the-audience-size-in-google-zero}

Pour des raisons de confidentialité, la taille de la liste d'utilisateurs affichera zéro jusqu'à ce que la liste compte au moins 1 000 membres. Ensuite, la taille sera arrondie aux deux chiffres les plus significatifs.

### Pourquoi la taille de mon audience correspondante dans Google est-elle inférieure au nombre d'utilisateurs synchronisés depuis Braze ? {#why-is-my-matched-audience-size-in-google-lower-than-the-number-of-users-synced-from-braze}

Bien que Braze puisse synchroniser un certain nombre d'utilisateurs vers Google, la taille réelle de l'audience correspondante que vous voyez dans Google Ads peut être nettement inférieure. En effet, Google doit faire correspondre les données utilisateur que vous fournissez (telles que les adresses e-mail ou les numéros de téléphone) avec des comptes Google réels sur sa plateforme.

Même si vos profils utilisateurs Braze contiennent des champs de correspondance valides, les utilisateurs n'apparaissent dans votre audience personnalisée Google que s'ils possèdent un compte Google avec des informations correspondantes.

Pour améliorer votre taux de correspondance :
- Confirmez que vous [formatez correctement vos données](https://support.google.com/google-ads/answer/7659867).
- Fournissez plusieurs identifiants lorsque c'est possible (par exemple, à la fois l'e-mail et le numéro de téléphone).
- Notez qu'il peut falloir entre 48 et 72 heures pour que Google traite et fasse correspondre les utilisateurs, bien que dans certains cas cela puisse prendre plusieurs jours.

La taille finale de l'audience correspondante dépend entièrement du processus de correspondance de Google. Braze n'a pas de visibilité sur la correspondance effectuée par Google une fois que les données ont été transmises à leur plateforme.

### J'ai synchronisé une audience sur Google, mais mes publicités ne sont pas diffusées. {#ive-synced-an-audience-into-google-but-my-ads-are-not-serving}

Vérifiez que vos audiences contiennent au moins 5 000 utilisateurs pour que les publicités puissent commencer à être diffusées.

### Comment résoudre l'erreur « Mobile App IDs Deleted » ? {#how-do-i-resolve-the-mobile-app-ids-deleted-error}

Si vous synchronisez des audiences avec Google, cette erreur se déclenche si vous avez choisi de synchroniser les identifiants mobiles dans le cadre de vos synchronisations, mais que vous avez supprimé les ID de vos applications mobiles depuis la page partenaire de Google. Pour résoudre ce problème, assurez-vous d'avoir ajouté les ID d'applications mobiles appropriés pour iOS et Android à la page partenaire de Google.

### Pourquoi ai-je reçu un e-mail d'identifiants Google Ads non valides alors que le tableau de bord affiche toujours une connexion active ? {#why-did-i-get-a-google-ads-invalid-credentials-email-when-the-dashboard-still-shows-connected}

Braze envoie automatiquement cet e-mail lorsque l'API de Google renvoie une erreur d'autorisation. Cela peut se produire même lorsque **Google Ads** apparaît toujours comme connecté dans le tableau de bord et que les audiences semblent se synchroniser — par exemple, lorsque le compte Google connecté ne dispose pas des autorisations pour une action spécifique demandée par Google, ou lorsque les conditions d'utilisation de Google Ads doivent encore être acceptées pour le compte.

Certaines erreurs d'autorisation se résolvent d'elles-mêmes. Vérifiez les analyses **Audience Sync** de votre Canvas (par exemple, *Users Synced* et *Users Errored*) pour confirmer si les utilisateurs sont toujours synchronisés. Si les problèmes persistent, allez dans **Intégrations partenaires** > **Partenaires technologiques** > **Google Ads**, trouvez **Google Audience Sync** et utilisez **Change Account** pour vous reconnecter avec un compte Google Ads disposant de l'accès requis et de la configuration complète.