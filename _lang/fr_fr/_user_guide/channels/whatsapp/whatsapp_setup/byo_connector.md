---
nav_title: Connecteur BYO WhatsApp
article_title: Connecteur Bring Your Own WhatsApp
page_order: 2
description: "Cet article de référence fournit un guide étape par étape pour configurer un connecteur Bring Your Own WhatsApp, qui donne à Braze l'accès à votre Infobip WhatsApp Business Manager."
page_type: reference
channel:
  - WhatsApp
---

# Connecteur Bring Your Own WhatsApp {#bring-your-own-whatsapp-connector}

> Le connecteur Bring Your Own (BYO) WhatsApp offre un partenariat entre Braze et Infobip, dans lequel vous donnez à Braze l'accès à votre Infobip WhatsApp Business Manager (WABA). Cela vous permet de gérer et de payer les coûts d'envoi de messages directement avec Infobip tout en utilisant Braze pour la segmentation, la personnalisation et l'orchestration des campagnes. Braze conserve toutes les fonctionnalités existantes offertes par le canal WhatsApp, telles que les messages sortants, le traitement des messages entrants, les flux WhatsApp et l'analytique.

## Conditions préalables {#requirements}

| Condition | Description |
| --- | --- |
| Compte Infobip | Un compte Infobip est requis pour utiliser le connecteur BYO WhatsApp. |
| Crédits de messages ou d'actions | Vous consommez des crédits d'actions Braze lorsque vous envoyez des messages WhatsApp. |
| Conditions WhatsApp | Remplissez toutes les [conditions WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#prerequisites). |
| Numéro de téléphone | Nous vous suggérons d'[acquérir un numéro de téléphone via Infobip](https://www.infobip.com/docs/numbers/getting-started) pour plus de commodité. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Configuration {#set-up}

Avant de configurer le connecteur BYO WhatsApp, confirmez que les envois précédents de votre WhatsApp Business Account n'ont pas été effectués via Infobip.

### Cas pris en charge {#supported-cases}

- Le WhatsApp Business Account et le numéro de téléphone n'ont jamais été connectés à un partenaire auparavant.
- Le WhatsApp Business Account est connecté directement à Braze via l'intégration native.
    - Suivez les étapes de la [migration de numéro de téléphone WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number) pour migrer vos numéros de téléphone vers un nouveau WhatsApp Business Account, un numéro à la fois.
- Le WhatsApp Business Account est connecté à un fournisseur de solutions différent de Braze et Infobip.
    - Suivez les étapes de la [migration de numéro de téléphone WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number) pour migrer vos numéros de téléphone vers un nouveau WhatsApp Business Account, un numéro à la fois.

## Étape 1 : Récupérer les informations du compte Infobip {#step-1}

1. Dans Infobip, identifiez le compte que vous souhaitez utiliser avec votre WhatsApp Business Account.
2. Accédez à **Developer Tools** > **API Keys** et sélectionnez **Create API Key**.

![Page « Create API key » avec une date de création du « 16/12/2025 » et une date d'expiration du « 16/12/36 ».]({% image_buster /assets/img/whatsapp/byo_connector/create_api_key.png %})

{: start="3"}
3. Donnez à la clé un nom significatif, tel que « Braze - Mon nom d'espace de travail - Mon nom WABA ».
4. Ajoutez une date d'expiration lointaine pour éviter les problèmes liés à l'expiration du jeton.
    - Pensez à générer une nouvelle clé API et à reconnecter votre WABA avant la date d'expiration.
5. Sélectionnez ces portées :
- `Message:send`
- `Whatsapp:manage`
- `Whatsapp:message:send`
- `Account-management:manage`
- `Subscriptions:manage`
- `Metrics:manage`
6. Après avoir créé la clé, copiez la clé API.
    - La clé ne peut être copiée que pendant un temps limité après sa création. Vous pouvez répéter ces étapes pour créer une nouvelle clé si vous devez connecter un autre WhatsApp Business Account à l'avenir.

![« Braze Example API Key » avec 6 portées ajoutées.]({% image_buster /assets/img/whatsapp/byo_connector/api_key.png %})

{: start="7"}
7. Copiez l'URL de base de l'API du compte.

![Page « API keys » avec une URL de base de l'API mise en surbrillance.]({% image_buster /assets/img/whatsapp/byo_connector/api_base_url.png %})

## Étape 2 : Démarrer l'inscription intégrée {#step-2-start-the-embedded-signup}

1. Dans Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** > **WhatsApp**.
2. Sélectionnez l'onglet **BYO Connector - Infobip**.

![La page Partenaires technologiques WhatsApp.]({% image_buster /assets/img/whatsapp/byo_connector/byo_tab_tech_parners.png %})

{: start="3"}
3. Saisissez la clé API et l'URL de base de l'[étape 1](#step-1).
4. Sélectionnez **Connect**.
5. Suivez le [flux d'inscription intégrée]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup#whatsapp-embedded-signup-workflow) en tenant compte de ces considérations :
- Vous ne pouvez pas sélectionner le même portefeuille d'entreprise utilisé par un autre fournisseur de solutions métier.
- Vous ne pouvez pas sélectionner un numéro de téléphone utilisé par un autre fournisseur de solutions métier.
- Vous devez créer un nouveau WABA, et non en sélectionner un existant.

{% alert note %}
Pour recevoir le code de vérification, accédez à votre tableau de bord Infobip > **Analyze** > **Logs**, et récupérez le code à partir du message SMS entrant.
{% endalert %}

![Journaux de messages affichant un message SMS entrant avec le code de vérification.]({% image_buster /assets/img/whatsapp/byo_connector/verification_code.png %})

Une fois la configuration terminée, votre numéro de téléphone est répertorié en tant que groupe d'abonnement sous votre WhatsApp Business Group. Le WhatsApp Business Group contient le nom du compte Infobip et l'URL de base de l'API auxquels il est connecté. Les comptes connectés via l'intégration native n'ont pas de nom de compte Infobip.

{% alert note %}
Connectez chaque WhatsApp Business Account à un seul compte Infobip. Chaque fois que vous connectez un numéro de téléphone ou un groupe d'abonnement supplémentaire, si le WhatsApp Business Account est déjà connecté à un compte Infobip, vous devez saisir à nouveau les identifiants API du compte existant.
{% endalert %}

## Étape 3 : Envoi de messages {#step-3-sending-messages}

Suivez le processus d'envoi de l'intégration native, notamment :
- [Inscrire des utilisateurs au groupe d'abonnement]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)
- [Créer un message WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)

## Résolution des problèmes de configuration {#troubleshooting-setup}

### Impossible de récupérer l'ID du WhatsApp Business Account {#couldnt-retrieve-whatsapp-business-account-id}

Confirmez que votre WhatsApp Business Account n'est pas connecté à un autre espace de travail Braze.

### Impossible de partager l'ID du WhatsApp Business Account avec Infobip {#couldnt-share-whatsapp-business-account-id-with-infobip}

1. Confirmez que votre WhatsApp Business Account n'est pas connecté à Braze ou à un autre partenaire.
2. Confirmez qu'aucun numéro de téléphone de votre WhatsApp Business Account n'est connecté à un autre compte Infobip. Pour les numéros importés, vous pouvez trouver le numéro dans Infobip et sélectionner **Cancel number**.

## Considérations {#considerations}

Bien que toutes les fonctionnalités existantes avec Braze soient prises en charge, les cas d'utilisation suivants ne sont actuellement pas pris en charge.

| Cas d'utilisation | Raison |
| --- | --- |
| Traitement des messages entrants dans Braze et Infobip | Cela empêche les chaînes logiques déclenchées par l'un ou l'autre système, générant par conséquent des fils de messages en double et potentiellement contradictoires. |
| Envoi de messages depuis Braze et Infobip | Pour les WhatsApp Business Accounts connectés à Braze, tous les envois proviennent de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Considérations" }