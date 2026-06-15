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

## Migrer votre numéro de téléphone WhatsApp {#migrating-your-whatsapp-phone-number}

1. Dans le WhatsApp Manager, sélectionnez le compte WhatsApp Business (WABA) associé à votre numéro de téléphone, puis accédez à **Account tools** > **Phone numbers**.
2. Sélectionnez **Turn off two-step verification** et suivez les étapes qui s'affichent.<br><br>![WhatsApp Business Manager ouvert sur la page « Phone numbers ».]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> Si vous migrez un numéro de téléphone vers un autre groupe WhatsApp Business et que l'Embedded Signup de Meta exige que le nom d'affichage corresponde, notez le nom d'affichage existant sur la page **Phone Numbers**. Vous saisirez ce nom lors de l'étape suivante.<br><br>![La page Phone Numbers du WhatsApp Business Manager avec un nom d'affichage « Braze » affiché à côté d'un numéro de téléphone.]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. Poursuivez le flux de l'Embedded Signup de Meta jusqu'à la fin.