---
nav_title: OneLogin
article_title: OneLogin
page_order: 4
page_type: tutorial
description: "Cet article vous explique comment configurer Braze pour utiliser OneLogin pour l'authentification unique."

---

# OneLogin

> [OneLogin](https://www.onelogin.com/) est une plateforme d'identité cloud qui offre une solution complète de gestion des identités utilisateur. OneLogin s'intègre aux applications cloud et sur site via SAML 2.0, pour l'authentification unique (SSO), le provisionnement utilisateur, l'authentification multifacteur, et plus encore.

## Prérequis {#requirements}

Lors de la configuration, il vous sera demandé de fournir une URL de connexion et une URL ACS (Assertion Consumer Service).

| Prérequis | Détails |
|---|---|
| URL Assertion Consumer Service (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Pour les domaines de l'Union européenne, l'URL ACS est `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. |
| Entity ID | `braze_dashboard` par défaut. Si votre IdP nécessite un Entity ID propre à l'entreprise, activez **Custom Entity ID** dans **Paramètres de sécurité** et utilisez `braze_dashboard_<companyID>`. |
| Domaine Braze | Vous aurez besoin de votre domaine Braze pour configurer Braze dans OneLogin. Si votre instance est `US-01`, vous devrez saisir l'URL de votre tableau de bord dans le tableau de bord OneLogin. <br><br> Par exemple, si l'URL de votre tableau de bord est `https://dashboard-01.braze.com`, vous devez saisir `dashboard-01.braze.com`.  |
| Clé API RelayState | Pour activer la connexion IdP, accédez à **Paramètres** > **Configuration et test** > **API et identifiants**, ouvrez l'onglet **Clés API**, puis créez une clé API avec les permissions `sso.saml.login`. Pour les étapes détaillées, consultez [Configuration de votre RelayState]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Connexion initiée par l'IdP dans OneLogin {#idp-initiated-login-within-onelogin}

### Étape 1 : Configurer l'application Braze {#step-1-configure-the-braze-app}

1. Connectez-vous à [OneLogin](https://app.onelogin.com/login). Cliquez sur **Administration**.![Page d'administration OneLogin.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Allez dans **Apps** > **Add Apps** dans la barre de navigation supérieure. Recherchez « Braze » et sélectionnez l'application Braze.![Résultats de recherche pour Braze dans OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Enregistrez l'application Braze dans votre entreprise.![Enregistrement de l'application Braze dans OneLogin.]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. Une fois enregistrée, allez dans **Configuration** et ajoutez votre **Braze Domain** et la clé API **RelayState**. Si votre IdP nécessite un Entity ID spécifique à l'entreprise, configurez également l'**ACS URL** (`https://<SUBDOMAIN>.braze.com/auth/saml/callback`) et l'Entity ID à partir de la [configuration de l'authentification unique (SSO) SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#requirements).![Onglet Configuration de OneLogin pour l'application Braze.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze s'attend à ce que les assertions SAML soient dans un [format spécifique]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#step-1-configure-your-identity-provider). Sous **Parameters**, les attributs pris en charge par Braze devraient être pré-remplis. Vérifiez qu'ils sont corrects.![Paramètres SAML de Braze dans OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Copiez le **Certificate** et le **SAML 2.0 Endpoint (HTTP)** nécessaires pour configurer le tableau de bord de Braze depuis l'onglet **SSO**.![Certificats à copier depuis l'onglet SSO de l'application Braze dans OneLogin.]({% image_buster /assets/img/onelogin_6.jpg %})

### Étape 2 : Configurer OneLogin dans Braze {#step-2-configure-onelogin-within-braze}

Une fois que vous avez configuré Braze dans votre OneLogin, celui-ci vous fournira une URL cible (`SAML 2.0 Endpoint (HTTP)`) et un certificat `x.509` à saisir dans votre compte Braze.

Après que votre gestionnaire de compte a activé l'authentification unique (SSO) SAML pour votre compte, allez dans **Paramètres** > **Paramètres de l'entreprise** > **Paramètres d'administration** > **Paramètres de sécurité** et basculez la section Authentification unique (SSO) SAML sur **ON**.

Sur cette page, saisissez les informations suivantes :

| Exigence | Détails |
|---|---|
| `SAML Name` | Ceci apparaîtra comme texte du bouton sur l'écran de connexion. Il s'agit généralement du nom de votre fournisseur d'identité, comme « OneLogin ». |
| `Target URL` | Il s'agit de l'URL `SAML 2.0 Endpoint (HTTP)` fournie par OneLogin. |
| `Certificate` | Le certificat `x.509` encodé au format PEM est fourni par votre OneLogin. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Configurer OneLogin dans Braze" }

Si votre IdP nécessite un Entity ID spécifique à l'entreprise, activez **Custom Entity ID** dans les **Paramètres de sécurité**, copiez la valeur générée et collez-la dans le champ Entity ID de OneLogin. Consultez [Entity ID personnalisé]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#custom-entity-id) dans l'article sur la configuration de l'authentification unique (SSO) SAML.

![Paramètres d'authentification unique (SSO) SAML avec le basculement sélectionné.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Si vous souhaitez que les utilisateurs de votre compte Braze se connectent uniquement via l'authentification unique (SSO) SAML, vous pouvez [restreindre l'authentification par authentification unique]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) depuis **Paramètres** > **Paramètres de l'entreprise** > **Paramètres d'administration** > **Paramètres de sécurité**.
{% endalert %}

## Étapes suivantes {#next-steps}

Une fois l'authentification unique (SSO) OneLogin opérationnelle :

- [Imposer la connexion uniquement par SSO SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) si la connexion par mot de passe doit être désactivée.
- [Configurer le provisionnement juste-à-temps SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning) pour créer automatiquement les utilisateurs du tableau de bord lors de leur première connexion via l'IdP.
- Utiliser [Obtenir une trace SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#obtaining-a-saml-trace) si des utilisateurs rencontrent des erreurs de connexion.