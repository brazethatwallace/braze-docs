---
nav_title: "Obtenir un numéro"
article_title: "Obtenir un numéro de téléphone WhatsApp"
page_order: 1
description: "Cet article de référence explique comment obtenir un numéro de téléphone auprès de Twilio et d'Infobip."
page_type: reference
channel:
  - WhatsApp
---

# Obtenir un numéro de téléphone WhatsApp {#acquire-a-whatsapp-phone-number}

> Pour utiliser le canal de communication WhatsApp, vous aurez besoin d'un numéro de téléphone conforme aux exigences de WhatsApp pour son [API Cloud](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) ou son [API On-Premises](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers).

Vous devez obtenir votre numéro de téléphone vous-même, car Braze ne le fournira pas pour vous. Vous pouvez soit acheter un téléphone physique avec une carte SIM auprès de votre fournisseur de téléphonie professionnelle, soit utiliser l'un de nos partenaires : Twilio ou Infobip. **Vous devez disposer de votre propre compte Twilio ou Infobip, car cela ne peut pas être fait via Braze.**

## Exigences de l'API WhatsApp {#whatsapp-api-requirements}

Votre numéro de téléphone doit répondre aux exigences suivantes de l'API WhatsApp :

- Être détenu par votre entreprise
- Avoir un indicatif de pays et de zone (comme les numéros fixes et mobiles)
- Être en mesure de recevoir des appels vocaux ou des SMS
- Être accessible lors de la configuration du compte (pour recevoir les codes de vérification)
- Ne pas être un code court
- Ne pas avoir été utilisé précédemment avec la plateforme WhatsApp Business
- Ne pas être connecté à un compte WhatsApp personnel

{% alert note %}
Braze recommande fortement d'utiliser un numéro que votre entreprise possède et auquel elle a un accès complet et permanent. Lors du processus d'inscription intégrée WhatsApp, vous devez avoir accès aux messages envoyés à ce numéro pour le vérifier. Il est possible que vous deviez vérifier le numéro à nouveau ultérieurement, vous devez donc en conserver l'accès.
{% endalert %}

## Obtenir un numéro de téléphone Twilio {#acquiring-a-twilio-phone-number}

### Étape 1 : Acheter un numéro de téléphone depuis la console ou l'API Twilio {#step-1-buy-a-phone-number-from-the-twilio-console-or-api}

1. Depuis la console Twilio, accédez à **Develop** > **Phone Numbers** > **Manage** > **Buy a number**. Si vous ne voyez pas cette option, sélectionnez **Explore Products**, faites défiler jusqu'à **Super Networks**, puis sélectionnez **Phone Number** > **Buy a number**. <br><br>![Console Twilio avec l'onglet « Develop » ouvert et l'option « Buy a number ».]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. Entrez l'indicatif régional ou la localité souhaitée (si vous en avez un). Trouvez un numéro, puis sélectionnez **Buy**. <br><br> ![Un bouton pour acheter le numéro de téléphone affiché.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. Après avoir acheté votre numéro de téléphone, accédez à **Active Numbers** et sélectionnez le numéro de téléphone que vous venez d'acheter. <br><br>![« Active Numbers » affichant le numéro de téléphone acheté.]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### Étape 2 : Configurer votre numéro de téléphone {#step-2-configure-your-phone-number}

Configurez votre numéro de téléphone Twilio pour recevoir les codes de vérification par e-mail. **Ne liez pas votre numéro de téléphone à WhatsApp dans la console Twilio.**

{% alert warning %}
Ne liez pas votre numéro de téléphone à WhatsApp dans la console Twilio. Si vous le faites, le numéro sera enregistré sur le compte WhatsApp Business de Twilio, ce qui vous empêchera de le connecter à Braze via le flux d'inscription intégrée.
{% endalert %}

1. Dans la console Twilio, accédez à la [page Active Numbers](https://www.twilio.com/console/phone-numbers/incoming) et sélectionnez le numéro de téléphone que vous avez acheté.
2. Accédez à la section **Voice Configuration** et dans le menu déroulant **Configure with**, sélectionnez **Webhook, TwiML Bin, Function, Studio Flow, Proxy Service**.
3. Dans la ligne **A call comes in**, sélectionnez **Webhook** et définissez l'URL sur `https://twimlets.com/voicemail?Email=YOUR_EMAIL_ADDRESS`, en remplaçant `YOUR_EMAIL_ADDRESS` par votre adresse e-mail.

### Étape 3 : Compléter le flux d'inscription intégrée {#step-3-complete-the-embedded-sign-up-workflow}

1. Une fois Twilio configuré, accédez à votre tableau de bord de Braze > **Partenaires technologiques** > **WhatsApp** et sélectionnez **Begin integration** ou **Add WhatsApp Business Account**, selon ce qui s'affiche, pour déclencher le [flux d'inscription intégrée]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup).<br><br>À l'étape **Add a phone number for WhatsApp**, sélectionnez **Phone call** pour la méthode de vérification de votre numéro de téléphone. <br><br>![Section avec les options pour vérifier votre numéro de téléphone par SMS ou par appel téléphonique.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. Attendez quelques minutes que le code de vérification soit envoyé à votre boîte de réception, puis entrez le code de vérification et terminez votre configuration.

## Obtenir un numéro de téléphone Infobip {#acquiring-an-infobip-phone-number}

1. Dans la console Infobip, accédez à **Channels and Numbers** et sélectionnez **Numbers**.<br><br>![Section « Channels and Numbers » d'Infobip avec « Numbers » listé en dessous.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. Sélectionnez **Buy Number** > le pays où vous souhaitez envoyer des messages > **SMS**.<br><br>![Bouton pour acheter un numéro.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. Selon le pays sélectionné, vous devrez peut-être compléter un processus d'inscription supplémentaire (comme sélectionner une option 10DLC ou numéro gratuit pour les numéros de téléphone américains). Assurez-vous de sélectionner l'option disponible.<br><br>![Une page vous demandant de sélectionner le type de numéro : 10DLC ou numéro gratuit.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. Sélectionnez l'offre disponible, puis poursuivez les étapes restantes et attendez que votre demande soit traitée. Vous pouvez vérifier le statut en accédant à **Numbers** > **My Request**. <br><br>![Une offre avec des informations incluant les frais et la couverture.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. Selon le pays sélectionné, attendez que l'équipe Infobip vous contacte pour les détails d'inscription (comme pour le 10DLC aux États-Unis).<br><br>

6. Lorsque votre numéro de téléphone est prêt dans Infobip, accédez à votre tableau de bord de Braze > **Partenaires technologiques** > **WhatsApp** et sélectionnez **Begin integration** ou **Add WhatsApp Business Account**, selon ce qui s'affiche, pour déclencher le [flux d'inscription intégrée]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup).<br><br> À l'étape **Add a phone number for WhatsApp**, sélectionnez **Text message** pour la méthode de vérification de votre numéro de téléphone.<br><br>![Section avec les options pour vérifier votre numéro de téléphone par SMS ou par appel téléphonique.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Consultez les [journaux d'analyse](https://www.infobip.com/docs/analyze/analyze-logs) d'Infobip dans leur portail client pour obtenir le code de vérification, qui peut prendre quelques minutes à apparaître, puis entrez le code de vérification et terminez la configuration.