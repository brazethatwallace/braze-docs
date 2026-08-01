---
nav_title: "Migrer un numéro"
article_title: "Migrer un numéro de téléphone WhatsApp"
page_order: 2
description: "Cet article de référence explique comment migrer votre numéro de téléphone WhatsApp."
page_type: reference
channel:
  - WhatsApp
---

# Migrer un numéro de téléphone WhatsApp {#migrate-a-whatsapp-phone-number}

> Migrez votre numéro de téléphone WhatsApp entre les comptes WhatsApp Business en utilisant l'Embedded Signup de Meta.

## Conditions préalables {#prerequisites}

Votre numéro de téléphone doit répondre aux exigences de Meta pour être éligible à la migration :

- Votre compte Meta Business est vérifié.
- Votre compte WhatsApp Business existant est approuvé.
- Votre compte WhatsApp Business existant dispose d'un moyen de paiement valide dans les **Payment Settings**.
- La vérification en deux étapes est désactivée pour votre numéro de téléphone professionnel. Si vous êtes propriétaire de votre compte WhatsApp Business, vous pouvez désactiver la vérification en deux étapes sur le numéro dans le WhatsApp Manager. Sinon, vous devez demander à votre fournisseur de solutions de la désactiver pour vous.

Pour plus d'informations sur la migration de votre numéro de téléphone WhatsApp, consultez la documentation de Meta sur la [migration des numéros de téléphone entre les comptes WhatsApp Business via l'Embedded Signup](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/).

## Migrer entre les comptes WhatsApp Business {#migrate-between-whatsapp-business-accounts}

1. Dans le WhatsApp Manager, sélectionnez le compte WhatsApp Business (WABA) associé à votre numéro de téléphone, puis accédez à **Account tools** > **Phone numbers**.
2. Sélectionnez **Turn off two-step verification** et suivez les étapes qui s'affichent.<br><br>![WhatsApp Business Manager ouvert sur la page « Phone numbers ».]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> Si vous migrez un numéro de téléphone vers un autre groupe WhatsApp Business et que l'Embedded Signup de Meta exige que le nom d'affichage corresponde, notez le nom d'affichage existant sur la page **Phone Numbers**. Vous saisirez ce nom lors de l'étape suivante.<br><br>![La page Phone Numbers du WhatsApp Business Manager avec un nom d'affichage « Braze » affiché à côté d'un numéro de téléphone.]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. Poursuivez le flux de l'Embedded Signup de Meta jusqu'à la fin.

## Migrer depuis un autre fournisseur de solutions Business (BSP) {#migrate-from-another-business-solution-provider}

Si votre numéro de téléphone WhatsApp est enregistré auprès d'un autre BSP, vous devez migrer le numéro vers un compte WhatsApp Business connecté à Braze avant que Braze puisse envoyer des messages depuis ce numéro.

### Avant de migrer {#before-you-migrate}

- Sachez qu'un numéro de téléphone ne peut être actif que sur un seul BSP à la fois. La migration transfère l'envoi vers Braze ; votre ancien BSP perd l'accès au numéro.
- Vérifiez les contrats et la facturation avec votre fournisseur actuel. L'historique des messages et les modèles peuvent ne pas être transférés automatiquement.
- Désactivez la vérification en deux étapes sur le numéro conformément aux exigences de Meta.
- Si vous avez besoin de numéros distincts pour le support et le marketing, consultez [Intégrations, données et rapports]({{site.baseurl}}/user_guide/channels/whatsapp/faq#integrations-data-and-reporting) dans la FAQ WhatsApp.

### Parcours de migration {#migration-paths}

| Configuration actuelle | Parcours recommandé |
|---|---|
| Numéro sur un autre BSP, migration complète vers Braze | Migrer via l'[Embedded Signup]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup) vers un WABA Braze nouveau ou existant |
| Numéro sur l'intégration native de Braze, passage à la facturation Infobip | [Connecteur BYO WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/byo_connector) (Infobip uniquement) |
| Marketing sur Braze, support sur un autre WABA | Conservez des WABA et des numéros de téléphone séparés ; consultez la [FAQ WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/faq#integrations-data-and-reporting) et [WhatsApp et systèmes externes]({{site.baseurl}}/user_guide/channels/whatsapp/use_cases/whatsapp_and_external_systems) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Parcours de migration" }

## Espaces de travail de développement et de production {#development-and-production-workspaces}

Braze recommande d'utiliser des comptes WhatsApp Business distincts pour le développement et la production lorsque cela est possible :

- Ne liez pas votre numéro de téléphone de production à un espace de travail sandbox ou de développement.
- Utilisez un WABA de test dédié et un numéro de téléphone distinct pour les tests d'intégration.
- Les approbations de modèles s'appliquent par WABA ; approuvez les modèles dans le WABA lié à l'espace de travail depuis lequel vous envoyez.