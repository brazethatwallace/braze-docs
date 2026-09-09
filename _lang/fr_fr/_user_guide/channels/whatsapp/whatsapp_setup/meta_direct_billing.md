---
nav_title: Facturation directe Meta
article_title: Facturation directe Meta
page_order: 7
description: "Cet article de référence explique comment configurer la facturation directe Meta afin de payer les coûts de messagerie WhatsApp avec votre propre carte de débit ou de crédit au lieu d'une ligne de crédit Braze ou partenaire."
page_type: reference
channel:
  - WhatsApp
alias: /whatsapp_meta_direct_billing/
hidden: true
noindex: true
---

# Facturation directe Meta {#meta-direct-billing}

> La facturation directe Meta vous permet de payer les coûts de messagerie WhatsApp directement avec votre propre carte de débit ou de crédit, au lieu de passer par une ligne de crédit Braze ou partenaire.

## Prérequis {#prerequisites}

Avant de configurer la facturation directe Meta, assurez-vous de disposer des éléments suivants :

| Exigence | Description |
| --- | --- |
| Accès à l'espace de travail Braze | Vous devez avoir accès à **Intégrations partenaires** > **Partenaires technologiques** dans Braze pour démarrer le flux d'inscription intégré. |
| Compte Meta Business gestionnaire | La facturation est configurée dans Meta Business gestionnaire, sous **Facturation et paiements**. |
| Carte de débit ou de crédit | Une carte valide est nécessaire pour finaliser la configuration. La facturation mensuelle peut apparaître comme option sur certains comptes, mais n'est pas garantie. |
| Informations commerciales complètes | Le nom de votre entreprise, votre adresse et votre devise doivent être renseignés et exacts. Meta vérifie ces informations avant d'activer la messagerie. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Configuration {#setup}

### Étape 1 : Sélectionner la facturation directe Meta {#step-1-select-meta-direct-billing}

1. Dans Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques**, recherchez **WhatsApp** et ouvrez la page **WhatsApp Messaging Integration**.
2. Sélectionnez l'onglet **Meta Direct Billing**. Cela signifie que votre relation de facturation est directement avec Meta, et non via Braze ou une ligne de facturation Infobip. Il est donc important de sélectionner cet onglet avant de continuer, plutôt que d'essayer de le modifier ultérieurement.
3. Sous **Add a WhatsApp Business Account or phone number**, sélectionnez **Add account or number**. Cela lance l'inscription intégrée de Meta, où vous vous connecterez à Meta, sélectionnerez votre portefeuille d'entreprise, créerez ou sélectionnerez votre compte WhatsApp Business (WABA) et vérifierez votre numéro de téléphone.

### Étape 2 : Accéder à Billing & payments {#step-2-go-to-billing-payments}

Après avoir terminé l'inscription intégrée de Meta, effectuez l'une des actions suivantes :

- Sélectionnez **Add payment method**, ce qui vous redirige vers Meta Business gestionnaire.
- Dans Meta Business gestionnaire, accédez à **Billing & payments** > **Accounts**, puis sélectionnez votre WABA.

### Étape 3 : Ajouter un mode de paiement {#step-3-add-a-payment-method}

1. Sélectionnez **Add payment method**.
2. Dans la fenêtre qui s'ouvre, confirmez le champ **Business location and currency** (par exemple, **Canada, US Dollars USD**), qui détermine la devise de facturation. Sélectionnez **Edit** si une modification est nécessaire.
3. Sous **Select payment method**, vous pouvez voir des lignes de crédit existantes. Celles-ci ne sont pas disponibles pour votre utilisation ; ne les sélectionnez pas. Pour plus de détails, consultez [Restrictions des lignes de facturation](#billing-line-restrictions).

![La fenêtre de sélection du mode de paiement avec l'option Carte de débit ou de crédit sélectionnée et les lignes de crédit Infobip et Braze existantes non sélectionnées.]({% image_buster /assets/img/whatsapp/payment_methods.png %}){: style="max-width:40%;"}

{: start="4"}
4. Sous **Add payment method**, sélectionnez **Debit or credit card**, puis sélectionnez **Next**.
5. Saisissez les détails de votre carte, puis sélectionnez **Save**.
6. Votre carte apparaît sous **Payment methods**, marquée **Default**, avec le numéro de carte masqué et la date d'expiration affichés.

{% alert note %}
Fermer la fenêtre de configuration après avoir ajouté votre mode de paiement ne déconnecte pas votre numéro de téléphone. Le numéro associé est conservé.
{% endalert %}

### Étape 4 : Confirmer vos informations commerciales {#step-4-confirm-your-business-information}

Meta vérifie le nom de votre entreprise, votre adresse et votre devise avant d'activer la messagerie. Des informations commerciales incomplètes ou inexactes peuvent entraîner l'échec des messages ou une erreur d'informations commerciales non valides.

## Restrictions des lignes de facturation {#billing-line-restrictions}

Les lignes de crédit affichées dans la liste des modes de paiement (par exemple, « Infobip Limited » ou « BRAZE INC. ») appartiennent à cette entreprise spécifique, pas à vous. Elles apparaissent en raison de la manière dont votre compte est connecté, mais elles ne peuvent pas être sélectionnées.

## Ressources Meta {#meta-resources}

- [Centre d'aide Meta Business : Facturation et paiements](https://business.facebook.com/business/help/535561817791563)
- [Centre d'aide Meta Business : Ajouter un mode de paiement](https://www.facebook.com/business/help/832746984379005)