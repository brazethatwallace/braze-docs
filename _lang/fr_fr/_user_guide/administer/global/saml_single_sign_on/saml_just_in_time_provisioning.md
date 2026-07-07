---
nav_title: Provisionnement juste-à-temps SAML
article_title: Provisionnement juste-à-temps SAML
page_order: 1
page_type: tutorial
description: "Cet article vous explique comment configurer le provisionnement juste-à-temps SAML pour permettre aux nouveaux utilisateurs de l'entreprise de créer un compte Braze lors de leur première connexion."

---

# Provisionnement juste-à-temps SAML {#saml-just-in-time-provisioning}

> Le provisionnement juste-à-temps fonctionne avec l'[authentification unique (SSO) SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup) pour permettre aux nouveaux utilisateurs de l'entreprise de créer un compte Braze lors de leur première connexion. Cela évite aux administrateurs de devoir créer manuellement un compte pour un nouvel utilisateur, de choisir ses autorisations, de l'affecter à un espace de travail et d'attendre qu'il active son compte.

Par mesure de sécurité, le provisionnement juste-à-temps SAML (JITP) ne fonctionne que pour les utilisateurs dont les domaines d'e-mail existent déjà dans votre entreprise. Le JITP n'est possible que pour les domaines où il existe déjà au moins un développeur confirmé et non usurpé dans l'entreprise.

Par exemple, supposons que le compte `jon.smith@decorumsoft.com` puisse utiliser le JITP pour se connecter à Decorumsoft. Le compte `jane.smith@decorumsoft.com` possède le même domaine et peut également bénéficier du provisionnement. En revanche, si vous essayez d'utiliser le JITP avec `jon.smith@decorumsoft.eu`, le provisionnement ne sera pas autorisé car il n'existe pas de compte `decorumsoft.eu` dans le tableau de bord de Braze de Decorumsoft.

Pour demander une exception pour une entreprise, contactez l'[Assistance]({{site.baseurl}}/braze_support).

## Conditions préalables {#prerequisites}

Le JITP SAML nécessite que l'authentification unique (SSO) SAML soit configurée et intégrée. Il n'est pas compatible avec Google SSO et n'est pris en charge que pour les flux de connexion initiés par le fournisseur d'identité (IdP-initiated).

## Configuration du provisionnement juste-à-temps SAML (JITP) {#setting-up-saml-just-in-time-provisioning-jitp}

Demandez à un administrateur Braze d'effectuer les étapes suivantes :

1. Accédez à **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité**.
2. Dans la section **SAML SSO**, activez l'option **Automatic user provisioning**.
3. Sélectionnez un espace de travail par défaut dans lequel ajouter le nouvel utilisateur de l'entreprise.
4. Sélectionnez le jeu d'autorisations par défaut à attribuer à ce nouvel utilisateur. Pour savoir comment créer un jeu d'autorisations, consultez [Définir les autorisations des utilisateurs]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).
6. Sélectionnez **Enregistrer les modifications** en bas de la page.
7. Dans les paramètres de votre fournisseur SSO, ajoutez tous les utilisateurs ayant besoin d'accéder à Braze au répertoire de votre fournisseur SSO.
8. Demandez aux utilisateurs d'accéder à Braze via le portail de votre IdP pour leur première connexion. Ensuite, le bouton d'authentification unique SAML s'affichera pour les connexions suivantes.

## Questions fréquentes {#frequently-asked-questions}

### Comment désactiver le JITP SAML ? {#how-do-i-disable-saml-jitp}

Après avoir configuré le JITP, vous devez [contacter l'Assistance]({{site.baseurl}}/braze_support) pour le faire désactiver.

## Résolution des problèmes {#troubleshooting}

### Le bouton d'authentification unique n'apparaît pas avec Microsoft Entra ID {#single-sign-button-doesnt-appear-with-microsoft-entra-id}

Le champ **Sign-On URL** dans le formulaire **Basic SAML Configuration** de Microsoft Entra pour Braze peut amener les utilisateurs à ne voir qu'une option de mot de passe, et non un bouton SSO, lors d'une connexion initiée par l'IdP. Pour éviter ce problème, laissez le champ **Sign-On URL** vide lors de la configuration de Braze dans votre centre d'administration Microsoft Entra.