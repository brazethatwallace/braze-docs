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
{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

{% alert note %}
Cette fonctionnalité permet aux marques de contrôler quelles données first-party spécifiques sont partagées avec Google. Chez Braze, les intégrations avec lesquelles vous pouvez ou non partager vos données first-party font l'objet de la plus grande attention. En savoir plus sur notre [politique de confidentialité des données de Braze](https://www.braze.com/privacy).
{% endalert %}

## Prérequis {#prerequisites}

Assurez-vous que les éléments suivants sont créés et complétés avant de configurer votre étape Google Audience dans Canvas.

| Exigence | Origine | Description |
| ----------- | ------ | ----------- |
| Compte Google Ads | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | Un compte Google Ads actif pour votre marque.<br><br>Si vous souhaitez partager une audience entre plusieurs comptes gérés, vous pouvez charger vos audiences dans votre [compte administrateur](https://support.google.com/google-ads/answer/6139186). |
| Conditions Google Ads et Règles Google Ads | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | Vous devez accepter et vous assurer de respecter les [conditions publicitaires de Google](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40) et les [règles publicitaires de Google](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC), y compris la [politique de consentement des utilisateurs de l'UE](https://www.google.com/about/company/user-consent-policy/), le cas échéant, dans le cadre de votre utilisation de Braze Audience Sync.<br><br>Consultez votre équipe juridique au sujet de la nouvelle politique de consentement des utilisateurs de l'UE de Google afin de vous assurer que vous recueillez le consentement approprié pour utiliser les services Google Ads pour vos utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse. |
| Google Customer Match | [Google](https://support.google.com/google-ads/answer/6299717) | Customer Match n'est pas disponible pour tous les annonceurs.<br><br>**Pour utiliser Customer Match, votre compte doit disposer de :**<br>• Un bon historique de conformité aux règles<br>• Un bon historique de paiement<br>• Au moins 90 jours d'historique dans Google Ads<br>• Plus de 50 000 USD de dépenses totales cumulées. Pour les annonceurs dont les comptes sont gérés dans des devises autres que l'USD, le montant de vos dépenses sera converti en USD en utilisant le taux de conversion mensuel moyen pour cette devise.<br><br>Si votre compte ne remplit pas ces critères, il n'est actuellement pas éligible à l'utilisation de Customer Match.<br><br>Contactez votre conseiller Google Ads pour obtenir des informations supplémentaires sur la disponibilité de Customer Match pour votre compte. |
| Signaux de consentement Google | [Google](https://support.google.com/google-ads/answer/14310715) | Si vous souhaitez diffuser des publicités auprès d'utilisateurs finaux de l'EEE en utilisant le service Customer Match de Google, vous devrez transmettre à Braze les attributs personnalisés suivants (booléens) dans le cadre de la politique de consentement des utilisateurs de l'UE de Google. Plus de détails sont disponibles dans la section [Recueil du consentement pour les utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse](#collecting-consent-for-eea-uk-and-switzerland-end-users) : <br> - `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prérequis" }

### Versions minimales du SDK requises {#required-sdk-versions}

Lorsque vous utilisez les SDK Braze pour recueillir les signaux de consentement, assurez-vous de respecter les versions minimales suivantes :

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### Recueil du consentement pour les utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse {#collecting-consent-for-eea-uk-and-switzerland-end-users}

La politique de consentement des utilisateurs de l'UE de Google exige que les annonceurs divulguent les informations suivantes à leurs utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse, et obtiennent leur consentement pour :

* L'utilisation de cookies ou d'autres moyens de stockage local lorsque la loi l'exige ; et
* La collecte, le partage et l'utilisation de leurs données personnelles à des fins de personnalisation des publicités.

Cela n'affecte pas les utilisateurs finaux aux États-Unis ni les autres utilisateurs finaux situés en dehors de l'EEE, du Royaume-Uni ou de la Suisse. Consultez votre équipe juridique au sujet de la nouvelle politique de consentement des utilisateurs de l'UE de Google afin de vous assurer que vous recueillez le consentement approprié pour utiliser les services Google Ads pour vos utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse.

En vertu des exigences du Digital Markets Act (DMA) en vigueur depuis le 6 mars 2024, les annonceurs doivent transmettre le consentement des utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse lors du partage de données avec Google. Dans le cadre de ce changement, vous pouvez recueillir les deux signaux de consentement dans Braze sous forme d'attributs personnalisés booléens :

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze synchronisera les données de ces attributs personnalisés vers les [champs de consentement appropriés dans Google](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A).

#### Gestion du consentement révoqué {#managing-revoked-consent}

Pour maintenir vos listes d'audience à jour dans le cas où un utilisateur final de l'EEE a été ajouté à la liste d'audience, puis a ensuite retiré l'un des deux consentements (`$google_ad_user_data` ou `$google_ad_personalization`), vous devez configurer un Canvas pour retirer les utilisateurs des listes d'audience existantes à l'aide d'une étape Audience Sync.

{% alert note %}
Si un utilisateur de l'EEE a précédemment donné son consentement pour les deux signaux, ces données continueront d'être utilisées pour le service Customer Match de Google jusqu'à l'expiration de cette liste, ou jusqu'à ce que le statut de consentement soit explicitement mis à jour via Google Audience Sync, ou les deux.
{% endalert %}

#### Conseils {#tips}

* Envoyez la valeur sous forme de type booléen, et non de type chaîne de caractères.
* Préfixez le signe dollar ($) pour le nom de l'attribut. Braze utilise un signe dollar au début d'un nom d'attribut pour indiquer qu'il s'agit d'une clé spéciale et réservée.
* Saisissez le nom de l'attribut en minuscules.
* Bien que vous ne puissiez pas définir explicitement un utilisateur comme non spécifié, si vous envoyez une valeur `null` ou `nil` ou toute valeur qui n'est ni `true` ni `false`, Braze transmettra cet utilisateur à Google avec le statut `UNSPECIFIED`.
* Les nouveaux utilisateurs ajoutés ou mis à jour sans spécifier l'un ou l'autre des attributs de consentement seront synchronisés vers Google avec ces attributs de consentement marqués comme non spécifiés.

Si vous tentez de synchroniser un utilisateur de l'EEE sans les champs de consentement requis et le statut accordé, Google rejettera cet utilisateur et ne lui diffusera pas de publicités. De plus, si une publicité est diffusée à un utilisateur de l'EEE sans son consentement explicite, vous pourriez être tenu responsable et encourir des risques financiers. Pour éviter cela, nous vous recommandons d'envoyer des Campaigns avec des filtres de Segment qui n'incluent que les utilisateurs de l'EEE, du Royaume-Uni et de la Suisse ayant des attributs de consentement Google définis sur `true`. Pour plus de détails concernant la politique de consentement des utilisateurs de l'UE pour les partenaires de chargement Customer Match, consultez la [FAQ](https://support.google.com/google-ads/answer/14310715) de Google.

### Configuration de votre Canvas {#setting-up-your-canvas}

Après la synchronisation avec Braze, les attributs de consentement suivants seront disponibles sur vos profils utilisateur et pour la segmentation :

- `$google_ad_user_data`
- `$google_ad_personalization`

Dans tout Canvas où vous ciblez des utilisateurs finaux de l'EEE, du Royaume-Uni et de la Suisse à l'aide d'un Google Audience Sync pour ajouter des utilisateurs à une audience, vous devez exclure ces utilisateurs chaque fois que les deux attributs de consentement ont une valeur autre que `true`. Vous pouvez le faire en segmentant ces utilisateurs lorsque les valeurs de consentement sont définies sur `true`. Cela garantit également une analyse plus précise des utilisateurs synchronisés, car nous savons que Google rejettera ces utilisateurs des audiences. Notez que si vous utilisez Google Audience Sync pour retirer des utilisateurs d'une audience, les attributs de consentement ne sont pas requis.

## Intégration {#integration}

### Étape 1 : Connecter un compte Google {#step-1-connect-google-account}

{% alert important %}
Vous devez disposer de la [permission « Admin »]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) pour connecter Google Ads à votre compte Braze.
{% endalert %}

Pour commencer, accédez à **Intégrations partenaires** > **Partenaires technologiques** > **Google Ads** et sélectionnez **Connect Google Ads**. Une fenêtre modale vous invitera à sélectionner l'adresse e-mail associée à votre compte Google Ads, puis à accorder à Braze l'accès à votre compte Google Ads.

Une fois votre compte Google Ads connecté avec succès, vous serez redirigé vers la page partenaire Google Ads. Vous serez ensuite invité à sélectionner les comptes publicitaires auxquels vous souhaitez accéder dans l'espace de travail Braze.

![Un GIF montrant le flux de travail d'une connexion réussie d'un compte Google Ads à Braze.]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

#### Exporter les IDFA iOS ou les identifiants publicitaires Google {#export-ios-idfa-or-google-advertising-ids}

Si vous prévoyez d'exporter des IDFA iOS ou des identifiants publicitaires Google dans votre synchronisation d'audience, Google exige que votre identifiant d'application iOS et votre identifiant d'application Android soient inclus dans les requêtes. Sous Google Audience Sync, sélectionnez **Add Mobile Advertising IDs**, saisissez votre identifiant d'application iOS et votre identifiant d'application Android (nom du package de l'application), puis enregistrez chacun d'entre eux.

<br><br>
![La page technologique Google Ads mise à jour montrant les comptes publicitaires connectés, vous permettant de resynchroniser les comptes et d'ajouter des identifiants publicitaires mobiles.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
<br><br>

Si vous avez plusieurs applications dans un même espace de travail, vous pouvez saisir n'importe lequel de vos identifiants d'application dans la configuration, car les identifiants publicitaires mobiles de vos utilisateurs seront les mêmes pour toutes les applications. En effet, le GAID Android et l'IDFA iOS sont des identifiants publicitaires universels au niveau de l'appareil et ne sont pas spécifiques à une application. Pour synchroniser les identifiants publicitaires mobiles des utilisateurs d'une application spécifique, vous pouvez utiliser des filtres de Segment (« Last Used Specific App » ou « Most Recent App Version ») pour cibler ces utilisateurs.

### Étape 2 : Ajouter une étape Google Audience dans Canvas {#step-2-add-a-google-audience-step-in-canvas}

Ajoutez un composant dans votre Canvas, puis sélectionnez **Audience Sync**.

![Le menu de sélection d'un composant Canvas dans l'éditeur.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![L'étape Audience Sync ajoutée au parcours utilisateur.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Étape 3 : Configuration de la synchronisation {#step-3-sync-setup}

1. Sélectionnez **Custom Audience** pour ouvrir l'éditeur de composant.
2. Sélectionnez **Google** comme partenaire Audience Sync.

![Les paramètres de l'étape Audience Sync avec l'option de sélectionner un partenaire pour démarrer la synchronisation.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

{: start="3"}
3. Sélectionnez le compte publicitaire Google souhaité.
4. Dans le menu déroulant **Choose a New or Existing Audience**, saisissez le nom d'une audience nouvelle ou existante.

{% tabs %}
{% tab Créer une nouvelle audience %}

1. Saisissez un nom pour la nouvelle audience personnalisée.
2. Sélectionnez **Add Users to Audience**.
3. Sélectionnez les données first-party des champs utilisateur à envoyer à votre audience. Vous pouvez choisir entre :

- **Customer Contact Info** : contient les adresses e-mail ou les numéros de téléphone de vos utilisateurs, ou les deux, s'ils existent dans Braze. Google exige que ce soit un champ unique pour la synchronisation plutôt que des identifiants séparés. Vous pouvez toujours utiliser ce champ unique si vous ne disposez que d'un seul des identifiants.
- **Mobile Advertiser ID** : sélectionnez soit l'IDFA iOS, soit le GAID Android. En raison des exigences de Google Customer Match, vous ne pouvez pas avoir les deux identifiants publicitaires mobiles dans les mêmes listes de clients.

{% alert note %}
**À propos du bandeau « Missing Mobile Ad IDs? Let's fix that. » :** lorsque vous synchronisez vers une audience en utilisant l'IDFA iOS ou le GAID Android comme champ de correspondance, ce message peut apparaître dans l'éditeur d'étape. Il s'agit d'un message **informatif, pas d'une erreur**. Il vous rappelle de confirmer que le champ d'identifiant publicitaire mobile sur lequel vous effectuez la correspondance existe dans les données de votre audience (par exemple, que les utilisateurs dans le parcours Canvas ont l'identifiant correspondant collecté). Vous pouvez le fermer après avoir vérifié vos données.
{% endalert %}

{: start="4"}
4. Ensuite, enregistrez votre audience en sélectionnant le bouton **Create Audience** en bas de l'éditeur d'étape.

![Vue étendue du composant Canvas Custom Audience. Ici, le compte publicitaire souhaité est sélectionné, une nouvelle audience est créée et la case « customer contact info » est cochée.]({% image_buster /assets/img/audience_sync/g_sync.png %})

Les utilisateurs seront notifiés en haut de l'éditeur d'étape si l'audience est créée avec succès ou si des erreurs surviennent au cours de ce processus. Les utilisateurs peuvent référencer cette audience pour la suppression d'utilisateurs plus tard dans le parcours Canvas, car l'audience a été créée en mode brouillon.

![Une alerte qui apparaît après la création d'une nouvelle audience dans le composant Canvas.]({% image_buster /assets/img/audience_sync/g_sync3.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze crée une nouvelle audience personnalisée au lancement du Canvas, puis synchronise les utilisateurs en quasi temps réel à mesure qu'ils atteignent l'étape Google Audience.

{% alert important %}
Compte tenu des exigences de Google Customer Match, vous ne pouvez pas avoir des informations de contact client et des identifiants publicitaires mobiles dans les mêmes listes de clients. Google Customer Match utilisera ensuite ces informations pour déterminer qui peut être ciblé dans Google Search, Google Display, YouTube et Gmail. Pour plus de détails sur les exigences de Google Customer Match, consultez leur [documentation](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
{% endalert %}
{% endtab %}
{% tab Synchroniser avec une audience existante %}

Braze offre également la possibilité d'ajouter ou de supprimer des utilisateurs des listes de clients Google existantes afin de s'assurer que ces audiences sont à jour. Pour synchroniser avec une audience existante :

1. Sélectionnez une audience personnalisée existante à synchroniser.
2. Choisissez si vous souhaitez **ajouter à l'audience** ou **supprimer de l'audience**.
3. Braze ajoutera ou supprimera des utilisateurs en quasi temps réel à mesure qu'ils atteignent l'étape Google Audience.
4. Après avoir configuré votre étape Google Audience, sélectionnez **Done**. Votre étape Google Audience inclura les détails de la nouvelle audience.

![Vue étendue du composant Canvas Custom Audience. Ici, le compte publicitaire souhaité et l'audience existante sont sélectionnés, ainsi que le bouton radio « Add user to Audience ».]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Lancer le Canvas {#step-4-launch-canvas}

Complétez le reste de votre parcours utilisateur dans Canvas, puis lancez-le ! Si vous avez choisi de créer une nouvelle audience, Braze créera l'audience dans Google, puis ajoutera les utilisateurs à mesure qu'ils atteindront cette étape dans votre Canvas. Si vous avez choisi d'ajouter ou de supprimer des utilisateurs d'une audience existante, Braze ajoutera ou supprimera les utilisateurs lorsqu'ils atteindront cette étape dans leur parcours utilisateur.

Les utilisateurs passeront ensuite au composant suivant du Canvas s'il y en a un, ou quitteront le Canvas s'il s'agit de la dernière étape du parcours utilisateur.

## Synchronisation des utilisateurs et considérations relatives aux limites de débit {#user-syncing-and-rate-limit-considerations}

Lorsque les utilisateurs atteignent le composant Audience Sync, Braze synchronise ces utilisateurs en quasi temps réel tout en respectant les limites de débit de l'API Google Ads. Concrètement, Braze tente de regrouper et de traiter autant d'utilisateurs que possible toutes les 5 secondes avant de les envoyer à Google.

Lorsqu'un client approche de la limite de débit de l'API Google Ads, Google fournit à Braze des recommandations de nouvelle tentative. Si un client Braze atteint sa limite de débit, le Canvas Braze réessaiera la synchronisation pendant environ &#126;13 heures. Si la synchronisation n'est pas possible, ces utilisateurs sont répertoriés dans l'indicateur Users Errored.

## Comprendre l'analyse {#understanding-analytics}

Le tableau suivant présente les indicateurs et descriptions pour vous aider à mieux comprendre l'analyse de votre étape Audience Sync.

| Indicateur | Description |
| ------ | ----------- |
| *Entered* | Nombre d'utilisateurs ayant accédé à cette étape pour être synchronisés avec Google. |
| *Proceeded to Next Step* | Nombre d'utilisateurs ayant avancé vers le composant suivant, s'il y en a un. Tous les utilisateurs avancent automatiquement. S'il s'agit de la dernière étape de la branche Canvas, cet indicateur sera de 0. |
| *Users Synced* | Nombre d'utilisateurs ayant été synchronisés avec succès avec Google. |
| *User Not Synced* | Nombre d'utilisateurs n'ayant pas été synchronisés en raison de champs manquants pour la correspondance ou parce que l'attribut de consentement a été défini sur `false`. |
| *Users Errored* | Nombre d'utilisateurs n'ayant pas été synchronisés avec Google en raison d'une erreur, après environ 13 heures de tentatives. Pour des erreurs spécifiques, comme des interruptions du service de l'API Google Ads, Canvas réessaiera la synchronisation pendant environ 13 heures. Si la synchronisation n'est toujours pas possible à ce stade, l'indicateur *User Not Synced* sera renseigné. |
| *Users Pending* | Nombre d'utilisateurs en cours de traitement par Braze pour la synchronisation avec Google. |
| *Exited Canvas* | Nombre d'utilisateurs ayant quitté le Canvas. Cela se produit lorsque la dernière étape d'un Canvas est une étape Google. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprendre l'analyse" }

## Questions fréquentes {#frequently-asked-questions}

### Pourquoi ne puis-je pas sélectionner plusieurs champs à faire correspondre dans la configuration de mon étape Google Audience ? {#why-can-i-not-select-multiple-fields-to-match-in-my-google-audience-step-configuration}

Google Customer Match impose des exigences strictes concernant le format de ces audiences et les informations client incluses. Plus précisément, les identifiants d'annonceurs mobiles doivent être téléchargés séparément des coordonnées du client (telles que l'e-mail et le numéro de téléphone). Pour plus de détails, consultez la [documentation Google Customer Match](https://support.google.com/google-ads/answer/7659867?hl=en#undefined).

### Combien de temps faut-il pour que mes audiences soient synchronisées dans Google ? {#how-long-will-it-take-for-my-audiences-to-sync-in-google}

La synchronisation d'une audience dans Google peut prendre entre 6 et 12 heures.

### J'ai synchronisé une audience, mais pourquoi la taille de l'audience dans Google est-elle de zéro ? {#ive-synced-an-audience-so-why-is-the-audience-size-in-google-zero}

Pour des raisons de confidentialité, la taille de la liste d'utilisateurs affichera zéro tant que la liste ne compte pas au moins 1 000 membres. Au-delà, la taille sera arrondie aux deux chiffres les plus significatifs.

### Pourquoi la taille de mon audience correspondante dans Google est-elle inférieure au nombre d'utilisateurs synchronisés depuis Braze ? {#why-is-my-matched-audience-size-in-google-lower-than-the-number-of-users-synced-from-braze}

Bien que Braze puisse synchroniser un certain nombre d'utilisateurs vers Google, la taille réelle de l'audience correspondante que vous voyez dans Google Ads peut être nettement inférieure. En effet, Google doit faire correspondre les données utilisateur que vous fournissez (telles que les adresses e-mail ou les numéros de téléphone) avec les comptes Google réels sur sa plateforme.

Même si vos profils utilisateur Braze contiennent des champs de correspondance valides, les utilisateurs n'apparaissent dans votre audience Google Custom Audience que s'ils possèdent un compte Google avec des informations correspondantes.

Pour améliorer votre taux de correspondance :
- Vérifiez que vous [formatez correctement vos données](https://support.google.com/google-ads/answer/7659867).
- Fournissez plusieurs identifiants lorsque c'est possible (par exemple, à la fois l'e-mail et le numéro de téléphone).
- Notez que Google peut mettre entre 48 et 72 heures pour traiter et faire correspondre les utilisateurs, bien que dans certains cas cela puisse prendre plusieurs jours.

La taille finale de l'audience correspondante dépend entièrement du processus de correspondance de Google. Braze n'a aucune visibilité sur la correspondance effectuée par Google une fois que les données ont été transmises à sa plateforme.

### J'ai synchronisé une audience dans Google, mais mes publicités ne sont pas diffusées. {#ive-synced-an-audience-into-google-but-my-ads-are-not-serving}

Vérifiez que vos audiences contiennent au moins 5 000 utilisateurs pour que les publicités puissent commencer à être diffusées.

### Comment résoudre l'erreur « Mobile App IDs Deleted » ? {#how-do-i-resolve-the-mobile-app-ids-deleted-error}

Si vous synchronisez des audiences vers Google, cette erreur se déclenche lorsque vous avez choisi de synchroniser des identifiants mobiles dans le cadre de vos synchronisations, mais que vous avez supprimé vos identifiants d'application mobile de la page partenaire Google. Pour résoudre ce problème, assurez-vous d'avoir ajouté les identifiants d'application mobile appropriés pour iOS et Android sur la page partenaire Google.

### Pourquoi ai-je reçu un e-mail d'identifiants Google Ads invalides alors que le tableau de bord indique toujours une connexion active ? {#why-did-i-get-a-google-ads-invalid-credentials-email-when-the-dashboard-still-shows-connected}

Braze envoie automatiquement cet e-mail lorsque l'API de Google renvoie une erreur d'autorisation. Cela peut se produire même lorsque **Google Ads** apparaît toujours comme connecté dans le tableau de bord et que les audiences semblent se synchroniser — par exemple, lorsque le compte Google connecté ne dispose pas des autorisations nécessaires pour une action spécifique demandée par Google, ou lorsque les conditions d'utilisation de Google Ads doivent encore être acceptées pour le compte.

Certaines erreurs d'autorisation se résolvent d'elles-mêmes. Consultez les analyses **Audience Sync** de votre Canvas (par exemple, *Users Synced* et *Users Errored*) pour vérifier si les utilisateurs continuent de se synchroniser. Si les problèmes persistent, accédez à **Partner Integrations** > **Technology Partners** > **Google Ads**, recherchez **Google Audience Sync**, puis utilisez **Change Account** pour vous reconnecter avec un compte Google Ads disposant des accès requis et dont la configuration est terminée.