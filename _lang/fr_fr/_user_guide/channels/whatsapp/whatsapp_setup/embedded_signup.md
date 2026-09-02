---
nav_title: Inscription intégrée
article_title: Inscription intégrée WhatsApp
page_order: 1
description: "Cet article de référence explique comment accéder au flux d'inscription intégrée WhatsApp dans Braze, ce qu'il faut préparer avant l'inscription Meta et ce qui se passe une fois l'inscription terminée."
page_type: reference
channel:
  - WhatsApp
---

# Inscription intégrée WhatsApp {#whatsapp-embedded-signup}

> Utilisez l'inscription intégrée pour connecter Braze à un compte WhatsApp Business (WABA) via le flux d'inscription hébergé par Meta.

Le flux d'inscription intégrée WhatsApp s'ouvre lorsque vous [intégrez WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) pour la première fois dans votre espace de travail Braze, et lorsque vous [ajoutez un compte WhatsApp Business ou un numéro de téléphone]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) à une intégration existante.

{% alert note %}
Vous pouvez ajouter [plusieurs comptes WhatsApp Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/multiple_business_accounts) à un espace de travail Braze. Cependant, chaque compte WhatsApp Business spécifique ne peut être ajouté qu'à un seul espace de travail Braze.
{% endalert %}

## Accéder au workflow {#accessing-the-workflow}

1. Accédez à **Partner Integrations** > **Technology Partners**.
2. Recherchez et sélectionnez **WhatsApp**.
3. Sélectionnez l'option qui correspond à votre cas d'usage :
   - **Première intégration :** Sélectionnez **Begin Integration**.
   - **Compte ou numéro supplémentaire :** Sur la page **WhatsApp Messaging Integration**, sélectionnez **Add account or number** ou **Add WhatsApp Business Account**.

Le flux d'inscription intégrée de Meta est le même une fois que vous l'avez lancé depuis l'un ou l'autre point d'entrée. Votre espace de travail peut également afficher des onglets d'intégration, tels que **Native Integration** ou **BYO Connector - Infobip**, en fonction de votre configuration. Sélectionnez l'onglet qui correspond à votre configuration avant de commencer.

## Préparer l'inscription {#prepare-for-signup}

Lorsque vous sélectionnez **Begin Integration**, Braze ouvre une fenêtre d'onboarding. Parcourez chaque diapositive, puis sélectionnez à nouveau **Begin Integration** pour lancer l'inscription intégrée Meta.

Avant de commencer, préparez les éléments suivants :

- **Accès au Meta Business gestionnaire :** La plupart des entreprises utilisent Meta Business gestionnaire pour gérer les pages Facebook, les publicités et les ressources professionnelles associées. Si vous n'y avez pas accès, demandez à un administrateur de vous accorder les autorisations nécessaires ou créez un compte Business gestionnaire lors de l'inscription.
- **Numéro de téléphone :** Utilisez un numéro qui répond aux [exigences de Meta pour les numéros de téléphone WhatsApp](https://developers.facebook.com/docs/whatsapp/phone-numbers). Vous recevrez un code de vérification à usage unique par SMS ou appel téléphonique lors de l'inscription.

{% alert important %}
Vous n'effectuerez l'inscription intégrée initiale qu'une seule fois par chemin d'intégration, alors saisissez vos informations professionnelles avec le plus de précision possible.
{% endalert %}

## Processus d'inscription intégrée WhatsApp {#whatsapp-embedded-signup-workflow}

Après que Braze a lancé l'inscription intégrée Meta, connectez-vous avec un compte Meta ayant accès au Business gestionnaire de votre entreprise. Meta héberge les écrans d'inscription ; Braze ne contrôle ni leur mise en page ni leurs libellés.

{% alert note %}
Meta peut modifier les écrans d'inscription intégrée sans préavis. Si le processus diffère de cet article, suivez les instructions de Meta et consultez la [documentation de Meta sur l'inscription intégrée](https://developers.facebook.com/docs/whatsapp/embedded-signup/embed-the-flow).
{% endalert %}

De manière générale, Meta vous guide à travers les étapes suivantes :

1. **Connexion et octroi des autorisations.** Authentifiez-vous auprès de Meta et autorisez Braze à se connecter à votre compte WhatsApp Business.
2. **Sélection de votre portefeuille d'entreprise.** Connectez le portefeuille Business gestionnaire qui doit posséder le compte WhatsApp Business. Si vous ne voyez pas le portefeuille attendu, vérifiez vos autorisations Meta.
3. **Connexion ou création d'un compte WhatsApp Business.** Créez un nouveau compte ou sélectionnez un compte inutilisé lorsque vous y êtes invité. Ne sélectionnez pas un compte WhatsApp Business activement connecté à un autre fournisseur de communication ; cette connexion ne fonctionnera pas dans Braze. Pour [migrer un numéro depuis un autre fournisseur]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number), contactez votre équipe Braze avant de commencer.
4. **Fourniture des informations d'entreprise et d'affichage.** Saisissez le nom du compte, le nom d'affichage et la catégorie que Meta demande pour votre compte WhatsApp Business.
5. **Vérification de votre numéro de téléphone.** Ajoutez le numéro que vous souhaitez utiliser pour la communication WhatsApp et effectuez la vérification par SMS ou appel téléphonique.

Lorsque Meta termine l'inscription intégrée, le contrôle revient à Braze.

## Finaliser l'intégration Braze {#complete-the-braze-integration}

Après l'inscription intégrée, Braze exécute automatiquement les étapes de configuration. Sur la page **WhatsApp Messaging Integration**, vous pouvez voir des messages de progression tels que **Sign-up flow completed, integration with WhatsApp in progress** pendant que Braze effectue les opérations suivantes :

- Récupère l'identifiant de votre compte WhatsApp Business et les numéros de téléphone depuis Meta
- Ajoute l'utilisateur système Braze à votre compte WhatsApp Business
- Enregistre les numéros de téléphone et s'abonne aux événements webhook
- Crée un [groupe d'abonnement]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) Braze pour chaque numéro connecté

Attendez que l'intégration soit terminée avant d'envoyer des messages. Si la configuration échoue, consultez l'erreur sur la page d'intégration et reportez-vous à la section [Configuration de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) pour obtenir des conseils généraux.

## Étapes suivantes {#next-steps}

- [Acquérir ou migrer un numéro de téléphone WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers)
- [Créer un message WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)
- [Gérer les groupes d'abonnement]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)