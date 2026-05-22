---
nav_title: Provisionnement automatisé des utilisateurs
article_title: Provisionnement automatisé des utilisateurs
page_order: 3
page_type: reference
description: "Cet article de référence décrit les informations que vous devez fournir pour le provisionnement automatisé des utilisateurs et explique comment et où utiliser le jeton SCIM (System for Cross-domain Identity Management) que vous avez généré."
alias: /scim/automated_user_provisioning/

---

# Provisionnement automatisé des utilisateurs {#automated-user-provisioning}

> Le provisionnement automatisé des utilisateurs vous permet de créer et de gérer les utilisateurs de Braze via une API au lieu de le faire manuellement dans le tableau de bord. Braze prend en charge cette fonctionnalité via le système SCIM (System for Cross-domain Identity Management). Cet article vous explique quelles informations fournir, comment générer votre jeton SCIM et où trouver votre endpoint API SCIM.

## Accès aux paramètres de provisionnement SCIM {#accessing-scim-provisioning-settings}

1. Dans le tableau de bord de Braze, accédez à **Settings** > **Admin Settings** > **SCIM Provisioning**, puis sélectionnez **Configure SCIM integration**.
2. Dans l'étape **Braze configuration**, sélectionnez une méthode de provisionnement et fournissez les paramètres d'accès.

![Une page permettant de configurer l'intégration SCIM, avec des sections pour sélectionner une méthode de provisionnement et fournir des paramètres d'accès.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3. Dans l'étape **IdP configuration**, suivez les étapes indiquées dans la plateforme pour la méthode de provisionnement que vous avez sélectionnée.

{% tabs %}
{% tab Okta - Braze app %}

{% multi_lang_include early_access_beta_alert.md feature='The Okta integration' %}

Utilisez l'option **Okta - Braze app** si vous avez configuré l'application Braze pour l'authentification unique (SSO) SAML dans Okta. Si vous avez configuré une application personnalisée pour le SSO, suivez les instructions dans l'onglet [Okta - Custom app integration]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning/?tab=okta%20-%20custom%20app%20integration#step-1-set-up-scim-provisioning).

## Étape 1 : Configurer le provisionnement SCIM {#step-1-set-up-scim-provisioning}

### Étape 1.1 : Activer SCIM {#step-11-enable-scim}

1. Dans Okta, accédez à **Applications** > **Applications**, puis sélectionnez **Create App Integration**. Sélectionnez **SAML 2.0** comme méthode de connexion.
2. Renseignez les informations suivantes (disponibles dans l'étape [**IdP configuration**](#accessing-scim-provisioning-settings)) pour créer une application personnalisée :
- Logo de l'application
- URL d'authentification unique
- URL de l'audience (SP entity ID)
3. Sélectionnez **Finish**.
4. Sélectionnez l'onglet **General**.
5. Dans la section **App Settings**, sélectionnez **Edit**.
6. Dans le champ **Provisioning**, sélectionnez **SCIM**.

### Étape 1.2 : Désactiver la visibilité de l'application {#step-12-disable-application-visibility}

1. Dans le champ **Application visibility**, cochez la case **Do not display application icon to user**. Cela empêche les utilisateurs d'accéder au SSO via l'application, qui est uniquement destinée au SCIM.
2. Sélectionnez **Save**.

### Étape 1.3 : Configurer l'intégration SCIM {#step-13-set-up-the-scim-integration}

1. Sélectionnez l'onglet **Provisioning**.
2. Dans **Settings** > **Integration** > **SCIM Connection**, sélectionnez **Edit** et renseignez les valeurs des champs qui apparaissent dans le tableau de la page **Setup SCIM provisioning**.

### Étape 1.4 : Tester les identifiants API {#step-14-test-the-api-credentials}

Sélectionnez **Test API Credentials**. Un message de vérification apparaît si l'intégration est réussie et vous pouvez enregistrer.

### Étape 1.5 : Activer le provisionnement vers l'application {#step-15-enable-provisioning-to-the-app}

1. Dans **Provisioning** > **Settings** > **To App** > **Provisioning to App**, sélectionnez **Edit**.
2. Activez les options suivantes :
    - Create Users
    - Update Users Attributes
    - Deactivate Users
3. Vérifiez et configurez la section **Attribute Mapping** avec les mappages qui apparaissent dans le tableau de la page **Setup SCIM provisioning**.

## Étape 2 : Affecter des utilisateurs à l'application {#step-2-assign-users-to-the-app}

1. Sélectionnez l'onglet **Assignment**.
2. Sélectionnez **Assign** et choisissez une option.
3. Affectez l'application aux personnes qui doivent avoir accès à Braze.
4. Sélectionnez **Done** lorsque vous avez terminé l'affectation.

{% endtab %}
{% tab Okta - Custom app integration %}

{% multi_lang_include early_access_beta_alert.md feature='The Okta integration' %}

Utilisez l'option **Okta - Custom app integration** si vous avez configuré une application personnalisée pour le SSO. Si vous avez configuré l'application Braze pour l'authentification unique (SSO) SAML dans Okta, suivez les instructions dans l'onglet [Okta - Braze app]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning/?tab=okta%20-%20braze%20app#step-1-set-up-scim-provisioning).

## Étape 1 : Configurer le provisionnement SCIM

### Étape 1.1 : Activer SCIM

1. Dans Okta, accédez à votre application Braze.
2. Sélectionnez l'onglet **General**.
3. Dans la section **App Settings**, sélectionnez **Edit**.
4. Dans le champ **Provisioning**, sélectionnez **SCIM**.
5. Sélectionnez **Save**.

### Étape 1.2 : Configurer l'intégration SCIM {#step-12-set-up-scim-integration}

1. Sélectionnez l'onglet **Provisioning**.
2. Dans **Settings** > **Integration** > **SCIM Connection**, sélectionnez **Edit** et renseignez les valeurs des champs qui apparaissent dans le tableau de la page **Setup SCIM provisioning**.
3. Testez les identifiants API en sélectionnant **Test API Credentials**.
4. Sélectionnez **Save**.

### Étape 1.3 : Activer le provisionnement vers l'application {#step-13-enable-provisioning-to-the-app}

1. Dans **Provisioning** > **Settings** > **To App** > **Provisioning to App**, sélectionnez **Edit**.
2. Activez les options suivantes :
    - Create Users
    - Update Users Attributes
    - Deactivate Users
3. Vérifiez et configurez la section **Attribute Mapping** avec les mappages qui apparaissent dans le tableau de la page **Setup SCIM provisioning**.

## Étape 2 : Affecter des utilisateurs à l'application

1. Sélectionnez l'onglet **Assignment**.
2. Sélectionnez **Assign** et choisissez une option.
3. Affectez l'application aux personnes qui doivent avoir accès à Braze.
4. Sélectionnez **Done**.

{% endtab %}
{% tab Entra ID %}

{% multi_lang_include early_access_beta_alert.md feature='The Entra ID integration' %}

## Étape 1 : Configurer l'application de provisionnement SCIM {#step-1-set-up-scim-provisioning-app}

### Étape 1.1 : Se connecter au centre d'administration Microsoft Entra {#step-11-log-into-microsoft-entra-admin-center}

Connectez-vous à votre centre d'administration Microsoft Entra.

### Étape 1.2 : Créer et configurer votre application SCIM {#step-12-create-and-set-up-your-scim-app}

1. Dans le menu de navigation, accédez à **Entra ID** > **Enterprise apps**.
2. Sélectionnez **New application**.
3. Sélectionnez **Create your own application**.
4. Dans le panneau, saisissez un nom pour votre application.
5. Dans la section **What are you looking to do with your application?**, sélectionnez **Integrate application you don't find in the gallery (Non-gallery)**.
6. Sélectionnez **Create**.

### Étape 1.3 : Configurer l'intégration SCIM {#step-13-set-up-scim-integration}

1. Accédez à la section **Manage** > **Provisioning** de votre application SCIM.
2. Sélectionnez **Connect your application** ou **New configuration** et renseignez les valeurs des champs qui apparaissent dans le tableau de la page **Setup SCIM provisioning**.

### Étape 1.4 : Activer le provisionnement vers l'application {#step-14-enable-provisioning-to-the-app}

1. Accédez à la section **Manage** > **Attribute mapping (Preview)** de votre application SCIM.
2. Sélectionnez **Provision Microsoft Entra ID Users**.
3. Vérifiez et configurez la section **Attribute Mapping** pour qu'elle corresponde aux attributs qui apparaissent dans le tableau de la page **Setup SCIM provisioning**.
4. Fermez la page **Attribute Mapping**.

## Étape 2 : Affecter des utilisateurs à l'application

1. Accédez à **Manage** > **Users and Groups**.
2. Sélectionnez **Add user/group**.
3. Sélectionnez **None Selected** pour affecter des utilisateurs à l'application.
4. Sélectionnez le bouton **Select** pour confirmer l'affectation.

{% endtab %}
{% tab Custom %}

## Étape 1 : Configurer vos paramètres SCIM {#step-1-configure-your-scim-settings}

- **Espace de travail par défaut :** Sélectionnez l'espace de travail dans lequel les nouveaux utilisateurs doivent être ajoutés par défaut. Si vous ne spécifiez pas d'espace de travail dans votre [requête API SCIM]({{site.baseurl}}/post_create_user_account/), Braze affecte les utilisateurs à cet espace de travail.
- **Origine du service :** Saisissez le domaine d'origine de vos requêtes SCIM. Braze l'utilise dans l'en-tête `X-Request-Origin` pour vérifier la provenance des requêtes.
- **Liste d'adresses IP autorisées (facultatif) :** Vous pouvez restreindre les requêtes SCIM à des adresses IP spécifiques. Saisissez une liste ou une plage d'adresses IP séparées par des virgules. L'en-tête `X-Request-Origin` de chaque requête est utilisé pour vérifier l'adresse IP de la requête par rapport à la liste autorisée.

![Formulaire de paramètres de provisionnement SCIM avec trois champs : espace de travail par défaut, origine du service et liste d'adresses IP autorisées (facultatif). Le bouton « Generate SCIM Token » est désactivé.]({% image_buster /assets/img/scim_unfilled.png %})

## Étape 2 : Générer un jeton SCIM {#step-2-generate-a-scim-token}

Après avoir renseigné les champs requis, cliquez sur **Generate SCIM token** pour générer un jeton SCIM et afficher votre endpoint API SCIM. Veillez à copier le jeton SCIM avant de quitter la page. **Ce jeton n'apparaît qu'une seule fois.**

![Champs endpoint API SCIM et jeton SCIM affichés avec des valeurs masquées et des boutons de copie. Sous le champ du jeton se trouve un bouton « Reset Token ».]({% image_buster /assets/img/scim.png %})

Braze exige que toutes les requêtes SCIM contiennent le jeton porteur (bearer token) de l'API SCIM, transmis via un en-tête HTTP `Authorization`.

{% endtab %}
{% endtabs %}