---
nav_title: Provisionnement juste-à-temps SAML
article_title: Provisionnement juste-à-temps SAML
page_order: 1
page_type: tutorial
description: "Cet article vous explique comment configurer le provisionnement juste-à-temps SAML pour permettre aux nouveaux utilisateurs de l'entreprise de créer un compte Braze lors de leur première connexion."
---

# Provisionnement juste-à-temps SAML {#saml-just-in-time-provisioning}

> Le provisionnement juste-à-temps fonctionne avec l'[authentification unique (authentification unique) SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup) pour permettre aux nouveaux utilisateurs de l'entreprise de créer un compte Braze lors de leur première connexion. Cela évite aux administrateurs de devoir créer manuellement un compte pour un nouvel utilisateur, de choisir ses autorisations, de l'affecter à un espace de travail et d'attendre qu'il active son compte.

Par mesure de sécurité, le provisionnement juste-à-temps SAML (JITP) ne fonctionne que pour les utilisateurs dont les domaines d'e-mail existent déjà dans votre entreprise. Le JITP n'est possible que pour les domaines où il existe déjà au moins un développeur confirmé et non usurpé dans l'entreprise.

Par exemple, supposons que le compte `jon.smith@decorumsoft.com` puisse utiliser le JITP pour se connecter à Decorumsoft. Le compte `jane.smith@decorumsoft.com` possède le même domaine et peut également bénéficier du provisionnement. En revanche, si vous essayez d'utiliser le JITP avec `jon.smith@decorumsoft.eu`, le provisionnement ne sera pas autorisé car il n'existe pas de compte `decorumsoft.eu` dans le tableau de bord de Braze de Decorumsoft.

Pour demander une exception pour une entreprise, contactez l'[Assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Prérequis {#prerequisites}

Le provisionnement SAML JITP nécessite que l'authentification unique (authentification unique) SAML soit configurée et intégrée. Il n'est pas compatible avec le authentification unique Google et n'est pris en charge que pour les flux de connexion initiés par le fournisseur d'identité (IdP-initiated).

| Exigence | Détails |
|---|---|
| Authentification unique (authentification unique) SAML | Configurée et testée avant d'activer le JITP. Voir [Configuration de l'authentification unique (authentification unique) SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup). |
| Connexion initiée par l'IdP | Les utilisateurs doivent se connecter via votre portail IdP lors de leur première connexion. La connexion initiée par le SP seule ne provisionne pas de nouveaux utilisateurs. |
| Domaine e-mail | Le domaine e-mail de l'utilisateur doit déjà exister dans votre entreprise (au moins un développeur confirmé, non usurpé, avec ce domaine). |
| Activation au niveau de l'entreprise | Braze doit activer la fonctionnalité `saml_jit_provisioning` pour votre entreprise avant que le bouton **Automatic user provisioning** n'apparaisse. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis du JITP" }

{% alert important %}
Le provisionnement SAML juste-à-temps doit être activé pour votre entreprise par Braze. Contactez votre gestionnaire de compte ou le [support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) si le bouton **Automatic user provisioning** n'est pas disponible.
{% endalert %}

## Fonctionnement du JITP {#how-jitp-works}

Lorsque le JITP est activé et qu'un nouvel utilisateur se connecte via votre IdP pour la première fois :

1. Braze valide l'assertion SAML et vérifie que le domaine e-mail de l'utilisateur est autorisé pour le JITP.
2. Braze crée un compte utilisateur dans le tableau de bord à partir de l'e-mail contenu dans l'assertion SAML.
3. Braze attribue l'espace de travail et l'ensemble de permissions par défaut configurés dans les **Paramètres de sécurité**.
4. L'utilisateur peut accéder immédiatement à Braze sans étape distincte d'invitation ou d'activation.

Le JITP ne met pas à jour les permissions des utilisateurs existants. Il crée uniquement des comptes pour les utilisateurs qui n'existent pas encore dans votre entreprise.

## Configuration de l'approvisionnement juste-à-temps (JITP) SAML {#setting-up-saml-just-in-time-provisioning-jitp}

Demandez à un administrateur Braze d'effectuer les opérations suivantes :

1. Accédez à **Paramètres** > **Paramètres de l'entreprise** > **Paramètres d'administration** > **Paramètres de sécurité**.
2. Dans la section **Authentification unique (authentification unique) SAML**, activez l'option **Approvisionnement automatique des utilisateurs**.
3. Sélectionnez un espace de travail par défaut dans lequel ajouter un nouvel utilisateur de l'entreprise.
4. Sélectionnez l'ensemble d'autorisations par défaut à attribuer à ce nouvel utilisateur de l'entreprise. Pour savoir comment créer un ensemble d'autorisations, consultez [Définir les autorisations des utilisateurs]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

{% alert note %}
Si votre entreprise utilise des autorisations granulaires, vérifiez l'ensemble d'autorisations par défaut après la migration pour confirmer que les nouveaux utilisateurs JITP reçoivent l'accès prévu.
{% endalert %}

{: start="5"}
5. Sélectionnez **Enregistrer les modifications**.
6. Dans les paramètres de votre fournisseur authentification unique, ajoutez tous les utilisateurs ayant besoin d'un accès à Braze au répertoire de votre fournisseur authentification unique.
7. Demandez aux utilisateurs d'accéder à Braze via le portail de votre IdP pour leur première connexion. Ensuite, le bouton d'authentification unique SAML s'affiche pour les connexions suivantes.

## Questions fréquemment posées {#frequently-asked-questions}

### Comment désactiver le JITP SAML ? {#how-do-i-disable-saml-jitp}

Après avoir configuré le JITP, vous devez [contacter le support]({{site.baseurl}}/user_guide/administer/personal/braze_support) pour le faire désactiver.

### Le JITP peut-il attribuer des permissions différentes par utilisateur ? {#can-jitp-assign-different-permissions-per-user}

Non. Tous les utilisateurs créés par JITP reçoivent l'espace de travail par défaut et l'ensemble de permissions configurés dans **Paramètres de sécurité**. Pour attribuer un accès différent, créez les utilisateurs manuellement ou utilisez le [provisionnement automatisé des utilisateurs SCIM]({{site.baseurl}}/scim/automated_user_provisioning).

### Le JITP fonctionne-t-il avec la connexion initiée par le SP ? {#does-jitp-work-with-sp-initiated-login}

Non. Le JITP ne s'exécute que lors d'une connexion initiée par l'IdP, lorsqu'un utilisateur se connecte depuis le portail de votre fournisseur d'identité.

## Résolution des problèmes {#troubleshooting}

### L'utilisateur n'a pas été provisionné lors de la première connexion authentification unique {#user-was-not-provisioned-on-first-sso-sign-in}

Vérifiez les points suivants :

- Le JITP est activé et enregistré dans **Paramètres de sécurité**.
- L'utilisateur s'est connecté via le portail IdP (initié par l'IdP), et non uniquement depuis la page de connexion de Braze.
- Le domaine d'e-mail de l'utilisateur existe déjà dans votre entreprise.
- L'assertion SAML inclut un attribut `email` valide correspondant à l'adresse avec laquelle l'utilisateur se connecte.

### Le bouton d'authentification unique n'apparaît pas avec Microsoft Entra ID {#single-sign-on-button-doesnt-appear-with-microsoft-entra-id}

Le champ **Sign-On URL** dans le formulaire **Basic SAML Configuration** de Microsoft Entra pour Braze peut amener les utilisateurs à ne voir qu'une option de mot de passe, et non un bouton authentification unique, lors d'une connexion initiée par l'IdP. Pour éviter ce problème, laissez le champ **Sign-On URL** vide lors de la configuration de Braze dans votre centre d'administration Microsoft Entra.