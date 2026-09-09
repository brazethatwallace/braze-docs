---
nav_title: Okta
article_title: Okta
page_order: 3
page_type: tutorial
description: "Cet article vous explique comment configurer Braze pour utiliser Okta pour l'authentification unique."

---

# Okta

> Okta connecte toute personne à n'importe quelle application sur n'importe quel appareil. Il s'agit d'un service de gestion d'identité de qualité professionnelle, conçu pour le cloud, mais compatible avec de nombreuses applications sur site. Avec Okta, votre équipe informatique peut gérer l'accès de n'importe quel employé à toute application ou à tout appareil.

{% alert note %}
L'application Braze préconfigurée disponible sur la marketplace Okta utilise l'Entity ID partagé `braze_dashboard`. Si vous avez besoin d'un Entity ID unique pour ce tableau de bord — par exemple, pour connecter plusieurs tableaux de bord Braze via Okta — configurez une application SAML personnalisée au lieu de l'application de la marketplace, puis suivez les instructions de la section [Utiliser un Entity ID personnalisé]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#using-a-custom-entity-id).
{% endalert %}

## Conditions requises {#requirements}

| Condition | Détails |
| ----------- | ------- |
| Okta activé pour votre compte | Contactez votre gestionnaire de compte Braze pour faire activer cette fonctionnalité pour votre compte. |
| Privilèges d'administrateur Okta | Assurez-vous de disposer des privilèges d'administrateur avant de configurer Okta. |
| Privilèges d'administrateur Braze | Assurez-vous de disposer des privilèges d'administrateur avant de configurer Okta. |
| Clé API RelayState | Pour activer la connexion IdP, accédez à **Paramètres** > **Clés API** et créez une clé API avec les permissions `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions requises" }

## Étape 1 : Configurer Braze {#step-1-configure-braze}

### Étape 1a : Accéder aux paramètres de sécurité dans Braze {#step-1a-navigate-to-security-settings-in-braze}

Une fois que votre gestionnaire de compte a activé l'authentification unique (authentification unique) SAML pour votre compte, rendez-vous dans **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité** et basculez la section authentification unique SAML sur **ON**.

![SSO SAML Okta activé sur la page Paramètres de sécurité.]({% image_buster/assets/img/Okta/okta1.png %})

### Étape 1b : Modifier les paramètres authentification unique SAML {#step-1b-edit-saml-sso-settings}

Depuis le tableau de bord d'administration Okta, Okta vous fournit une URL cible (URL de connexion) et un certificat `x.509`, que vous devez saisir dans la page **Paramètres de sécurité** de votre compte Braze.

![Capture d'écran relative à l'étape 1b : modification des paramètres SSO SAML.]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| Exigence | Détails |
|---|---|
| `SAML Name` | Ce texte apparaîtra sur le bouton de l'écran de connexion. Il s'agit généralement du nom de votre fournisseur d'identité. Par exemple, « Okta ». |
| `Target URL` | Il s'agit de l'URL de connexion fournie par le tableau de bord d'administration Okta. Vous la trouverez en accédant à **Applications** > votre application > onglet **General** > **App Embed Link** > **Embed Link**. |
| `Certificate` | Le certificat `x.509` encodé en PEM est fourni par votre fournisseur d'identité. Vous devez le copier et le coller dans ce champ. Récupérez-le dans Okta en accédant à **SAML Signing Certificates** et en sélectionnant **Actions** > **Download certificate**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 1b : Modifier les paramètres authentification unique SAML" }

Sélectionnez **Save Changes** en bas de la page une fois terminé.

## Étape 2 : Configurer Okta {#step-2-configure-okta}

Dans Okta, sélectionnez l'onglet **Sign On** pour l'application SAML Braze, puis cliquez sur **Edit**.

Ensuite, saisissez la clé API RelayState avec la permission `sso.saml.login` dans le champ **Default Relay State**.

![RelayState par défaut d'Okta dans l'onglet Sign On.]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

Assurez-vous d'enregistrer ces nouveaux paramètres.

{% alert tip %}
Si vous souhaitez que les utilisateurs de votre compte Braze se connectent uniquement via l'authentification unique (authentification unique) SAML, vous pouvez [restreindre l'authentification unique]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) depuis la page **Company Settings**.
{% endalert %}

## Étape 3 : Se connecter {#step-3-log-in}

Vous devriez maintenant pouvoir vous connecter à Braze en utilisant Okta !

![Connexion au tableau de bord de Braze avec l'authentification unique Okta activée.]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}