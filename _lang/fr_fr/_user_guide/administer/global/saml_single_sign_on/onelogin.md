---
nav_title: OneLogin
article_title: OneLogin
page_order: 4
page_type: tutorial
description: "Cet article vous expliquera comment configurer Braze pour utiliser OneLogin pour une authentification unique."

---

# OneLogin

> [OneLogin](https://www.onelogin.com/) est une plateforme d'identité en nuage qui offre une solution complète de gestion des identités des utilisateurs. OneLogin s'intègre aux applications cloud et sur site utilisant SAML 2.0, pour l'authentification unique (SSO), provisionnement utilisateur, authentification multifacteurs, etc.

## Conditions

Lors de la configuration, il vous sera demandé de fournir une URL de connexion et une URL d'Assertion Consumer Service (ACS).

| Condition | Détails |
|---|---|
| Domaine Braze | Vous aurez besoin de votre domaine Braze pour configurer Braze dans OneLogin. Si votre instance est `US-01`, vous devrez saisir votre URL de tableau de bord dans le tableau de bord OneLogin. <br><br> Par exemple, si votre URL de tableau de bord est `https://dashboard-01.braze.com`, vous devez saisir `dashboard-01.braze.com`.  |
| Clé API RelayState | Pour activer l'identifiant IdP, accédez à **Paramètres** > **Clés API** et créez une clé API avec les autorisations `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Identifiant initié par l'IdP dans OneLogin

### Étape 1 : Configurer l'application Braze

1. Connectez-vous à [OneLogin](https://app.onelogin.com/login). Cliquez sur **Administration**.![Page d'administration OneLogin.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Allez dans **Apps** > **Add Apps** dans la barre de navigation supérieure. Recherchez « Braze » et sélectionnez l'application Braze.![Résultats de recherche pour Braze dans OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Enregistrez l'application Braze dans votre société.![]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. Une fois enregistrée, accédez à **Configuration** et ajoutez votre **domaine Braze** et votre clé API **RelayState**.![Onglet Configuration de OneLogin pour l'application Braze.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze attend les assertions SAML dans un [format spécifique]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup/#configure-your-identity-provider). Sous **Parameters**, les attributs pris en charge par Braze devraient être pré-remplis. Vérifiez qu'ils sont corrects.![Paramètres SAML de Braze dans OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Copiez le **Certificate** et le **SAML 2.0 Endpoint (HTTP)** nécessaires pour configurer le tableau de bord de Braze depuis l'onglet **SSO**.![Certificats à copier depuis l'onglet SSO de l'application Braze dans OneLogin.]({% image_buster /assets/img/onelogin_6.jpg %})

### Étape 2 : Configurer OneLogin dans Braze

Une fois que vous avez configuré Braze dans OneLogin, celui-ci vous fournira une URL cible (`SAML 2.0 Endpoint (HTTP)`) et un certificat `x.509` que vous saisirez dans votre compte Braze.

Une fois que votre gestionnaire de compte a activé l'authentification unique (SSO) SAML pour votre compte, accédez à **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité** et basculez la section SSO SAML sur **ON**.

Sur cette page, saisissez les informations suivantes :

| Condition | Détails |
|---|---|
| `SAML Name` | Ce nom apparaîtra comme texte du bouton sur l'écran de connexion. Il s'agit généralement du nom de votre fournisseur d'identité, par exemple « OneLogin ». |
| `Target URL` | Il s'agit de l'URL `SAML 2.0 Endpoint (HTTP)` fournie par OneLogin. |
| `Certificate` | Le certificat `x.509` encodé au format PEM est fourni par OneLogin. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Paramètres SSO SAML avec le basculement sélectionné.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Si vous souhaitez que les utilisateurs de votre compte Braze se connectent uniquement via l'authentification unique (SSO) SAML, vous pouvez [restreindre l'authentification par authentification unique]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup/#restriction) depuis la page **Paramètres de l'entreprise**.
{% endalert %}