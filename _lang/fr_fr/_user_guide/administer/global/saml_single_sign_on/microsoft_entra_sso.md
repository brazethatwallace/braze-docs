---
nav_title: SSO Microsoft Entra
article_title: SSO Microsoft Entra
page_order: 2
page_type: tutorial
description: "Cet article vous explique comment configurer les fonctionnalités d'authentification unique (SSO) Microsoft Entra avec Braze."

---

# SSO Microsoft Entra {#microsoft-entra-sso}

> [Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/braze-tutorial) est le service cloud de gestion des identités et des accès de Microsoft, qui aide vos employés à se connecter et à accéder aux ressources. Vous pouvez utiliser Entra SSO pour contrôler l'accès à vos applications et à leurs ressources, en fonction de vos besoins métier.

## Exigences {#requirements}

Lors de la configuration, il vous est demandé de fournir une URL Assertion Consumer Service (ACS).

| Exigence | Détails |
|---|---|
| URL Assertion Consumer Service (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> Pour certains fournisseurs d'identité, cette URL peut également être appelée URL de réponse, URL d'audience ou URI d'audience. |
| Entity ID | `braze_dashboard`|
| Clé API RelayState | Pour activer la connexion via le fournisseur d'identité, accédez à **Paramètres** > **Configuration et test** > **API et identifiants**, sélectionnez l'onglet **Clés API**, puis créez une clé API avec les permissions `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exigences" }

## Connexion initiée par le fournisseur de services (SP) avec Microsoft Entra SSO {#service-provider-sp-initiated-login-within-microsoft-entra-sso}

### Étape 1 : Ajouter Braze depuis la galerie {#step-1-add-braze-from-the-gallery}

1. Dans votre centre d'administration Microsoft Entra, accédez à **Identity** > **Applications** > **Enterprise Applications**, puis sélectionnez **New application**.
2. Recherchez **Braze** dans la zone de recherche, sélectionnez-le dans le panneau de résultats, puis sélectionnez **Add**.

### Étape 2 : Configurer Microsoft Entra SSO {#step-2-configure-microsoft-entra-sso}

1. Dans votre centre d'administration Microsoft Entra, accédez à la page d'intégration de votre application Braze et sélectionnez **Single sign-on**.
2. Sur la page **Select a single sign-on method**, sélectionnez **SAML** comme méthode.
3. Sur la page **Set up Single Sign-On with SAML**, sélectionnez l'icône de modification pour **Basic SAML Configuration**.
4. Configurez l'application en mode initié par l'IdP en saisissant une **Reply URL** qui combine votre [instance Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) avec le format suivant : `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.
5. Configurez le RelayState en saisissant votre clé API de Relay State générée dans le champ **Relay State**.

{% alert important %}
**Ne définissez pas** le champ **Sign-On URL**. Laissez ce champ vide pour éviter tout problème avec votre SSO SAML initié par l'IdP.
{% endalert %}

{: start="6"}
6. Formatez les assertions SAML dans le format spécifique attendu par Braze. Consultez les onglets suivants sur les attributs utilisateur et les revendications utilisateur pour comprendre comment ces attributs et valeurs doivent être formatés.

{% tabs %}
{% tab Attributs utilisateur %}
Vous pouvez gérer les valeurs de ces attributs depuis la section **User Attributes** sur la page **Application Integration**.

Utilisez les paires d'attributs suivantes :

- `givenname` = `user.givenname`
- `surname`= `user.surname`
- `emailaddress` = `user.mail`
- `name` = `user.userprincipalname`
- `email` = `user.userprincipalname`
- `first_name` = `user.givenname`
- `last_name` = `user.surname`
- `Unique User Identifier` = `user.userprincipalname`

{% alert important %}
Le champ e-mail doit correspondre à ce qui est configuré pour vos utilisateurs dans Braze. Dans la plupart des cas, il s'agit de `user.userprincipalname` ; cependant, si vous avez une configuration différente, travaillez avec votre administrateur système pour vous assurer que ces champs correspondent exactement.
{% endalert %}

{% endtab %}
{% tab Revendications utilisateur %}

Sur la page **Set up Single Sign-On with SAML**, sélectionnez **Edit** pour ouvrir la boîte de dialogue **User Attributes**. Modifiez ensuite les revendications utilisateur selon le format approprié.

Utilisez les paires de noms de revendication suivantes :

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
Le champ e-mail doit correspondre à ce qui est configuré pour vos utilisateurs dans Braze. Dans la plupart des cas, il s'agit de `user.userprincipalname` ; cependant, si vous avez une configuration différente, travaillez avec votre administrateur système pour vous assurer que ces champs correspondent exactement.
{% endalert %}

Vous pouvez gérer ces revendications et valeurs utilisateur depuis la section **Manage claim**.

{% endtab %}
{% endtabs %}

{: start="8"}
8. Accédez à la page **Set up Single Sign-On with SAML**, puis faites défiler jusqu'à la section **SAML Signing Certificate** et téléchargez le **Certificate (Base64)** approprié en fonction de vos besoins.
9. Accédez à la section **Set up Braze** et copiez les URL appropriées pour les utiliser dans la [configuration Braze](#step-3).

### Étape 3 : Configurer Microsoft Entra SSO dans Braze {#step-3}

Après avoir configuré Braze dans le centre d'administration Microsoft Entra, Microsoft Entra fournit une URL cible (URL de connexion) et un certificat **x.509**, que vous saisissez dans votre compte Braze.

Une fois que votre gestionnaire de compte a activé l'authentification unique (SSO) SAML pour votre compte, procédez comme suit :

1. Accédez à **Paramètres** > **Paramètres de l'entreprise** > **Paramètres d'administration** > **Paramètres de sécurité** et basculez la section SSO SAML sur **ON**.
2. Sur la même page, ajoutez les éléments suivants :

| Exigence | Détails |
|---|---|
| `SAML Name` | Ce nom apparaîtra comme texte du bouton sur l'écran de connexion. Il s'agit généralement du nom de votre fournisseur d'identité, comme « Microsoft Entra ». |
| `Target URL` | Il s'agit de l'URL de connexion fournie par Microsoft Entra. |
| `Certificate` | Le certificat `x.509` encodé en PEM est fourni par votre fournisseur d'identité. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 3 : Configurer Microsoft Entra SSO dans Braze" }

{% alert tip %}
Si vous souhaitez que les utilisateurs de votre compte Braze se connectent uniquement via l'authentification unique (SSO) SAML, vous pouvez [restreindre l'authentification par authentification unique]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) sur la page **Paramètres de sécurité** sous **Règles d'authentification**.
{% endalert %}