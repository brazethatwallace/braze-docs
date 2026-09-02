---
nav_title: Configuration de l'authentification unique (authentification unique) SAML
article_title: Configuration de l'authentification unique (authentification unique) SAML
page_order: 0
page_type: tutorial
toc_headers: h2
description: "Cet article vous explique comment activer l'authentification unique SAML pour votre compte Braze."
---

# Connexion initiée par le fournisseur de services (SP) {#service-provider-sp-initiated-login}

> Cet article vous explique comment activer l'authentification unique SAML pour votre compte Braze et comment obtenir une trace SAML.

## Prérequis {#requirements}

Lors de la configuration, il vous sera demandé de fournir une URL de connexion et une URL ACS (Assertion Consumer Service).

| Prérequis | Détails |
|---|---|
| URL ACS (Assertion Consumer Service) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Pour les domaines de l'Union européenne, l'URL ACS est `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. <br><br> Pour certains IdP, cette URL peut également être désignée sous le nom d'URL de réponse, d'URL de connexion, d'URL d'audience ou d'URI d'audience. |
| Entity ID | `braze_dashboard` par défaut. Si votre IdP nécessite un Entity ID spécifique à l'entreprise, activez **Custom Entity ID** dans **Security Settings** et utilisez `braze_dashboard_<companyID>`. |
| Clé API RelayState | Accédez à **Settings** > **Setup and Testing** > **APIs and Identifiers**, ouvrez l'onglet **API Keys**, puis créez une clé API avec les permissions `sso.saml.login`. Saisissez la clé API générée comme paramètre `RelayState` dans votre IdP. Pour les étapes détaillées, consultez [Configuration de votre RelayState](#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Configuration de l'authentification unique (authentification unique) SAML {#setting-up-saml-sso}

### Étape 1 : Configurer votre fournisseur d'identité {#step-1-configure-your-identity-provider}

Configurez Braze en tant que fournisseur de services (SP) dans votre fournisseur d'identité (IdP) avec les informations suivantes. De plus, configurez le mappage des attributs SAML.

{% alert important %}
Si vous prévoyez d'utiliser Okta comme fournisseur d'identité, assurez-vous d'utiliser l'intégration préconfigurée disponible sur le [site d'Okta](https://www.okta.com/integrations/braze/).
{% endalert %}

| Attribut SAML | Obligatoire ? | Attributs SAML acceptés |
|---|---|---|
|`email` | Obligatoire | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Facultatif | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Facultatif | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 1 : Configurer votre fournisseur d'identité" }

{% alert note %}
Braze ne nécessite que l'attribut `email` dans l'assertion SAML.
{% endalert %}

### Étape 2 : Configurer Braze {#step-2-configure-braze}

Lorsque vous avez terminé de configurer Braze dans votre fournisseur d'identité, celui-ci vous fournit une URL cible et un certificat `x.509` à saisir dans votre compte Braze.

Une fois que votre gestionnaire de compte a activé l'authentification unique (authentification unique) SAML pour votre compte, accédez à **Paramètres** > **Paramètres de l'entreprise** > **Paramètres d'administration** > **Paramètres de sécurité** et basculez la section authentification unique SAML sur **ACTIVÉ**.

Sur la même page, saisissez les informations suivantes :

| Exigence | Détails |
|---|---|
| Nom SAML | Ce nom apparaîtra comme texte du bouton sur l'écran de connexion.<br>Il s'agit généralement du nom de votre fournisseur d'identité, par exemple « Okta ». |
| URL cible | Cette URL est fournie après la configuration de Braze dans votre IdP.<br> Certains IdP la désignent comme URL authentification unique ou endpoint SAML 2.0. |
| Certificat | Le certificat `x.509` fourni par votre fournisseur d'identité. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Configurer Braze" }

### ID d'entité personnalisé {#custom-entity-id}

Par défaut, Braze utilise `braze_dashboard` comme ID d'entité (également appelé Audience ou URI d'audience dans certains IdP). Si votre IdP nécessite un ID d'entité spécifique à l'entreprise :

1. Dans **Paramètres de sécurité**, activez **ID d'entité personnalisé**.
2. Copiez l'ID d'entité généré (`braze_dashboard_<companyID>`).
3. Collez cette valeur dans le champ ID d'entité, Audience ou URI d'audience de votre IdP.
4. Enregistrez les modifications dans Braze et dans votre IdP avant de tester la connexion.

{% alert important %}
Les utilisateurs ne pourront pas se connecter tant que l'ID d'entité ne correspond pas à la fois dans Braze et dans votre IdP. L'ID d'entité personnalisé nécessite une configuration supplémentaire dans votre fournisseur d'identité.
{% endalert %}

Assurez-vous que votre certificat `x.509` respecte le format suivant lors de son ajout au tableau de bord :

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![Paramètres SSO SAML avec le basculeur sélectionné.]({% image_buster /assets/img/samlsso.png %})

### Étape 3 : Se connecter à Braze {#step-3-sign-into-braze}

Enregistrez vos paramètres de sécurité et déconnectez-vous. Ensuite, reconnectez-vous avec votre fournisseur d'identité.

## Utilisation d'un Entity ID personnalisé {#using-a-custom-entity-id}

Par défaut, chaque tableau de bord de Braze utilise l'Entity ID partagé `braze_dashboard`. Un Entity ID personnalisé attribue à votre tableau de bord un identifiant unique, afin que votre fournisseur d'identité puisse vérifier que les demandes de connexion sont bien destinées à ce tableau de bord spécifique. C'est utile si vous configurez l'authentification unique (authentification unique) SAML pour plusieurs entreprises Braze au sein du même fournisseur d'identité.

L'utilisation d'un Entity ID personnalisé est facultative. Si vous ne l'activez pas, votre tableau de bord continue d'utiliser `braze_dashboard`.

{% alert warning %}
L'[application Braze du marketplace Okta](https://www.okta.com/integrations/braze/) préconfigurée impose l'Entity ID partagé `braze_dashboard` et n'est pas compatible avec un Entity ID personnalisé. Si vous avez déjà configuré l'authentification unique SAML avec l'application Braze du marketplace Okta, activer un Entity ID personnalisé sans mettre à jour le champ Entity ID dans Okta via une application SAML personnalisée empêchera la connexion et pourra bloquer l'accès des utilisateurs au tableau de bord. Pour utiliser un Entity ID personnalisé avec Okta, configurez plutôt une application SAML personnalisée.
{% endalert %}

### Étape 1 : Activer l'Entity ID personnalisé {#step-1-turn-on-the-custom-entity-id}

Accédez à **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité** et ouvrez la section Authentification unique SAML. Activez le basculeur **Entity ID personnalisé**. Braze génère un Entity ID unique pour votre tableau de bord au format `braze_dashboard_<COMPANY_ID>`. Si vous ne voyez pas l'option **Entity ID personnalisé**, contactez votre gestionnaire de compte Braze.

### Étape 2 : Mettre à jour votre fournisseur d'identité {#step-2-update-your-identity-provider}

Copiez l'Entity ID généré et collez-le dans le champ Entity ID de l'application Braze de votre fournisseur d'identité. Selon votre fournisseur, ce champ peut être intitulé **Entity ID**, **Audience** ou **Audience URI**.

{% alert important %}
L'Entity ID doit correspondre à la fois dans Braze et dans votre fournisseur d'identité. Tant que les deux côtés n'utilisent pas la même valeur, les utilisateurs ne peuvent pas se connecter avec l'authentification unique SAML. Mettez à jour votre fournisseur d'identité avant d'enregistrer cette page pour éviter de bloquer l'accès des utilisateurs.
{% endalert %}

### Étape 3 : Enregistrer et tester {#step-3-save-and-test}

Enregistrez vos paramètres de sécurité, déconnectez-vous, puis reconnectez-vous via votre fournisseur d'identité pour confirmer que la connexion fonctionne avec l'Entity ID personnalisé.

## Configuration de votre RelayState {#setting-up-your-relaystate}

1. Dans Braze, accédez à **Paramètres** > **Configuration et test** > **API et identifiants**.
2. Dans l'onglet **Clés API**, sélectionnez le bouton **Créer une clé API**.
3. Dans le champ **Nom de la clé API**, saisissez un nom pour votre clé.
4. Développez le menu déroulant **authentification unique** sous **Autorisations** et cochez **authentification unique.saml.login**.
5. Sélectionnez **Créer une clé API**.
6. Dans l'onglet **Clés API**, copiez l'identifiant à côté de la clé API que vous avez créée.
7. Collez la clé API RelayState dans le champ RelayState de votre IdP (il peut également apparaître sous le nom « Relay State » ou « Default Relay State » selon votre IdP).

## Connexion initiée par l'IdP {#idp-initiated-login}

Certains fournisseurs d'identité prennent en charge la connexion initiée par l'IdP, où les utilisateurs commencent depuis le portail de l'IdP au lieu de la page de connexion Braze. La connexion initiée par l'IdP nécessite une clé API RelayState valide et une configuration correcte de l'URL ACS. Guides de configuration spécifiques aux fournisseurs :

- [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)
- [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)
- [Microsoft Entra authentification unique]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)

{% alert note %}
La connexion initiée par l'IdP avec Microsoft Entra authentification unique nécessite de laisser le champ **Sign-On URL** vide. Consultez [Microsoft Entra authentification unique]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso) pour plus de détails.
{% endalert %}

## Comportement de l'authentification unique (authentification unique) {#sso-behavior}

Les membres qui choisissent d'utiliser l'authentification unique (authentification unique) ne peuvent plus utiliser leur mot de passe. Les utilisateurs qui continuent à utiliser leur mot de passe peuvent le faire, sauf si les paramètres suivants l'interdisent.

## Restriction {#restriction}

Vous pouvez restreindre les membres de votre organisation afin qu'ils se connectent uniquement via l'authentification unique (authentification unique) Google ou l'authentification unique (authentification unique) SAML. Pour activer les restrictions, accédez à **Paramètres** > **Paramètres de l'entreprise** > **Paramètres d'administration** > **Paramètres de sécurité** et sélectionnez **Imposer la connexion par authentification unique Google uniquement** ou **Imposer la connexion par authentification unique SAML personnalisé uniquement**.

![Exemple de configuration de la section « Règles d'authentification » avec une longueur minimale de mot de passe de 8 caractères et une réutilisation du mot de passe limitée à 3 fois. Les mots de passe expireront après 180 jours, et les utilisateurs seront déconnectés après 1 440 minutes d'inactivité.]({% image_buster /assets/img/sso3.png %})

En activant les restrictions, les utilisateurs Braze de votre entreprise ne pourront plus se connecter à l'aide d'un mot de passe, même s'ils se sont déjà connectés avec un mot de passe auparavant.

{% alert important %}
Une fois l'authentification unique (authentification unique) imposée, il n'existe aucune option de secours pour se connecter en cas d'échec de l'authentification authentification unique. Avant d'activer l'application du authentification unique, assurez-vous que votre configuration authentification unique est correcte, que tous les certificats sont à jour et renouvelés, et que vos paramètres de sécurité sont correctement gérés afin d'éviter les problèmes de connexion.
{% endalert %}

## Obtenir une trace SAML {#obtaining-a-saml-trace}

Si vous rencontrez des problèmes de connexion liés à l'authentification unique (authentification unique), l'obtention d'une trace SAML peut vous aider à résoudre les problèmes de votre connexion authentification unique en identifiant ce qui est envoyé dans les requêtes SAML.

### Prérequis {#prerequisites}

Pour exécuter une trace SAML, vous aurez besoin d'un traceur SAML. Voici deux options possibles en fonction de votre navigateur :

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### Étape 1 : Ouvrir le traceur SAML {#step-1-open-the-saml-tracer}

Sélectionnez le traceur SAML dans la barre de navigation de votre navigateur. Assurez-vous que **Pause** n'est pas sélectionné, car cela empêcherait le traceur SAML de capturer ce qui est envoyé dans les requêtes SAML. Lorsque le traceur SAML est ouvert, vous verrez la trace se remplir.

![Traceur SAML pour Google Chrome.]({% image_buster /assets/img/saml_tracer_example.png %})

### Étape 2 : Se connecter à Braze à l'aide de l'authentification unique (authentification unique) {#step-2-sign-into-braze-using-sso}

Accédez à votre tableau de bord de Braze et tentez de vous connecter à l'aide de l'authentification unique (authentification unique). Si vous rencontrez une erreur, ouvrez le traceur SAML et réessayez. Une trace SAML a été collectée avec succès s'il existe une ligne avec une URL comme `https://dashboard-XX.braze.com/auth/saml/callback` et une étiquette SAML orange.

### Étape 3 : Exporter et envoyer à Braze {#step-3-export-and-send-to-braze}

Sélectionnez **Export**. Pour **Select cookie-filter profile**, sélectionnez **None**. Ensuite, sélectionnez **Export**. Cela générera un fichier JSON que vous pourrez envoyer au support Braze pour une résolution des problèmes plus approfondie.

![Menu « Export SAML-trace preferences » avec l'option « None » sélectionnée.]({% image_buster /assets/img/export_saml_trace_preferences.png %})

## Résolution des problèmes {#troubleshooting}

### L'adresse e-mail de l'utilisateur est-elle correctement configurée ? {#is-the-users-email-address-correctly-set-up}

Si vous obtenez l'erreur `ERROR_CODE_SSO_INVALID_EMAIL`, l'adresse e-mail de l'utilisateur n'est pas valide. Vérifiez dans la trace SAML que le champ `saml2:Attribute Name="email"` correspond à l'adresse e-mail que l'utilisateur utilise pour se connecter. Si vous utilisez Microsoft Entra ID (anciennement Azure Active Directory), le mappage d'attribut est `email = user.userprincipalname`.

L'adresse e-mail est sensible à la casse et doit correspondre exactement à celle qui a été configurée dans Braze, y compris celle configurée dans votre fournisseur d'identité (comme Okta, OneLogin, Microsoft Entra ID, et autres).

D'autres erreurs qui indiquent des problèmes avec l'adresse e-mail de l'utilisateur incluent :
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST` : L'adresse e-mail de l'utilisateur n'existe pas dans le tableau de bord.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING` : L'adresse e-mail de l'utilisateur est vide ou autrement mal configurée.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` ou `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH` : L'adresse e-mail de l'utilisateur ne correspond pas à celle utilisée pour configurer l'authentification unique (authentification unique).

### Disposez-vous d'un certificat SAML valide (certificat x.509) ? {#do-you-have-a-valid-saml-certificate-x509-certificate}

Vous pouvez valider votre certificat SAML à l'aide de [cet outil de validation SAML](https://www.samltool.com/validate_response.php). Notez qu'un certificat SAML expiré est également un certificat SAML invalide.

### Avez-vous téléchargé un certificat SAML correct (certificat x.509) ? {#did-you-upload-a-correct-saml-certificate-x509-certificate}

Vérifiez que le certificat dans la section `ds:X509Certificate` de la trace SAML correspond à celui que vous avez téléchargé sur Braze. Cela n'inclut pas l'en-tête `-----BEGIN CERTIFICATE-----` ni le pied de page `-----END CERTIFICATE-----`.

### Avez-vous mal saisi ou mal formaté votre certificat SAML (certificat x.509) ? {#did-you-mistype-or-misformat-your-saml-certificate-x509-certificate}

Vérifiez qu'il n'y a pas d'espaces blancs ou de caractères supplémentaires dans le certificat que vous avez soumis dans le tableau de bord de Braze.

Lorsque vous saisissez votre certificat dans Braze, il doit être encodé au format Privacy Enhanced Mail (PEM) et correctement formaté (y compris l'en-tête `-----BEGIN CERTIFICATE-----` et le pied de page `-----END CERTIFICATE-----`).

Voici un exemple de certificat correctement formaté :

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### Le jeton de session de l'utilisateur est-il valide ? {#is-the-users-session-token-valid}

Demandez à l'utilisateur concerné de [vider le cache et les cookies de son navigateur](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser), puis de réessayer de se connecter avec l'authentification unique (authentification unique) SAML.

### Avez-vous défini votre RelayState ? {#did-you-set-your-relaystate}

Si vous obtenez l'erreur `ERROR_CODE_SSO_INVALID_RELAY_STATE`, votre RelayState pourrait être mal configuré ou inexistant. Si ce n'est pas déjà fait, vous devez définir votre RelayState dans votre système de gestion IdP. Pour les étapes, consultez [Configuration de votre RelayState](#setting-up-your-relaystate).

### Une connexion authentification unique réussie vous ramène-t-elle à la page de connexion de Braze ? {#does-successful-sso-sign-in-return-you-to-the-braze-login-page}

Cela peut se produire lorsque le RelayState n'est pas configuré correctement. Vérifiez que vous avez créé une clé API (dans **Paramètres** > **Configuration et test** > **API et identifiants**) pour la connexion IdP et que vous avez défini cette clé API comme paramètre `RelayState` dans votre IdP. Le RelayState identifie le compte d'entreprise auquel vous vous connectez. Pour des instructions étape par étape, consultez [Configuration de votre RelayState](#setting-up-your-relaystate).

Si vous ne parvenez toujours pas à vous connecter, [contactez le support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) avec une trace SAML si possible. Pour savoir comment capturer une trace, consultez [Obtenir une trace SAML](#obtaining-a-saml-trace).

### L'utilisateur est-il bloqué dans une boucle de connexion entre Okta et Braze ? {#is-the-user-stuck-in-a-sign-in-loop-between-okta-and-braze}

Si un utilisateur ne peut pas se connecter parce qu'il est bloqué dans un cycle entre l'authentification unique (authentification unique) Okta et le tableau de bord de Braze, vous devez accéder à Okta et définir l'URL de destination authentification unique vers votre [instance Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) (par exemple, `https://dashboard-07.braze.com`).

Si vous utilisez un autre IdP, vérifiez si votre entreprise a téléchargé le bon certificat SAML ou x.509 sur Braze.

### Utilisez-vous une intégration manuelle ? {#are-you-using-a-manual-integration}

Si votre entreprise n'a pas téléchargé l'application Braze depuis la boutique d'applications de votre IdP, vous devez télécharger l'intégration préconfigurée. Par exemple, si Okta est votre IdP, vous devez télécharger l'application Braze depuis leur [page d'intégration](https://www.okta.com/integrations/braze/).

## Google authentification unique

Si votre entreprise utilise Google authentification unique au lieu de l'authentification unique (authentification unique) SAML personnalisée, contactez votre gestionnaire de compte Braze pour activer Google authentification unique pour votre espace de travail. Une fois activé, accédez à **Paramètres** > **Paramètres de l'entreprise** > **Paramètres d'administration** > **Paramètres de sécurité** et sélectionnez **Enforce Google authentification unique only login** pour exiger l'authentification Google pour tous les utilisateurs de l'entreprise.

Lorsque l'imposition de Google authentification unique est activée, les utilisateurs doivent se connecter avec l'authentification Google et ne peuvent plus utiliser de mot de passe Braze. Chaque utilisateur doit se connecter avec le compte Google correspondant à son adresse e-mail du tableau de bord de Braze. Si un utilisateur sélectionne un autre compte Google lors de la connexion, Braze rejette la tentative d'authentification.

### Résolution des problèmes de connexion Google authentification unique {#troubleshooting-google-sso-sign-in}

Si certains utilisateurs ne parviennent pas à se connecter avec Google authentification unique, vérifiez les points suivants :

- L'adresse e-mail du compte Google de l'utilisateur correspond exactement à son adresse e-mail du tableau de bord de Braze.
- L'utilisateur a accès à un compte Google pour son adresse e-mail professionnelle.
- L'utilisateur n'est pas suspendu dans Braze (**Paramètres** > **Utilisateurs de l'entreprise**).

## Prochaines étapes {#next-steps}

Après avoir configuré l'authentification unique (authentification unique) SAML, vous pouvez :

- [Imposer la connexion uniquement par authentification unique]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#single-sign-on-sso-authentication) dans vos paramètres de sécurité pour empêcher les utilisateurs de se connecter avec un mot de passe.
- [Configurer le provisionnement juste-à-temps SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning) afin que les nouveaux utilisateurs créent automatiquement des comptes Braze lors de leur première connexion authentification unique.