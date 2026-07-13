---
nav_title: "Nummer erwerben"
article_title: "Eine WhatsApp-Telefonnummer erwerben"
page_order: 1
description: "Dieser Referenzartikel beschreibt, wie Sie eine Telefonnummer über Twilio und Infobip erwerben."
page_type: reference
channel:
  - WhatsApp
---

# Eine WhatsApp-Telefonnummer erwerben {#acquire-a-whatsapp-phone-number}

> Um den WhatsApp-Messaging-Kanal zu nutzen, benötigen Sie eine Telefonnummer, die den Anforderungen von WhatsApp für die [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) oder die [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) entspricht.

Sie müssen Ihre Telefonnummer selbst erwerben, da Braze die Nummer nicht für Sie bereitstellt. Sie können entweder ein physisches Telefon mit SIM-Karte über Ihren geschäftlichen Telefonanbieter kaufen oder einen unserer Partner nutzen: Twilio oder Infobip. **Sie müssen über ein eigenes Twilio- oder Infobip-Konto verfügen, da dies nicht über Braze erfolgen kann.**

## WhatsApp-API-Anforderungen {#whatsapp-api-requirements}

Ihre Telefonnummer muss diese WhatsApp-API-Anforderungen erfüllen:

- Im Besitz Ihres Unternehmens
- Über eine Landes- und Ortsvorwahl verfügen (wie bei Festnetz- und Mobilfunknummern)
- Sprachanrufe oder SMS empfangen können
- Während der Kontoeinrichtung erreichbar sein (um Verifizierungscodes zu empfangen)
- Kein Shortcode
- Nicht zuvor mit der WhatsApp Business Platform verwendet
- Nicht mit einem persönlichen WhatsApp-Konto verbunden

{% alert note %}
Braze empfiehlt dringend, eine Nummer zu verwenden, die Ihrem Unternehmen gehört und auf die Sie dauerhaft vollen Zugriff haben. Während des WhatsApp-Embedded-Sign-up-Prozesses benötigen Sie Zugriff auf Nachrichten, die an diese Nummer gesendet werden, um sie zu verifizieren. Möglicherweise müssen Sie die Nummer später erneut verifizieren, daher müssen Sie den Zugriff darauf beibehalten.
{% endalert %}

## Eine Twilio-Telefonnummer erwerben {#acquiring-a-twilio-phone-number}

### Schritt 1: Eine Telefonnummer über die Twilio-Konsole oder API kaufen {#step-1-buy-a-phone-number-from-the-twilio-console-or-api}

1. Gehen Sie in der Twilio-Konsole zu **Develop** > **Phone Numbers** > **Manage** > **Buy a number**. Wenn Sie diese Option nicht sehen, wählen Sie **Explore Products**, scrollen Sie zu **Super Networks** und wählen Sie dann **Phone Number** > **Buy a number**. <br><br>![Twilio-Konsole mit geöffnetem Tab „Develop“ und der Option „Buy a number“.]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. Geben Sie Ihre gewünschte Vorwahl oder Ihren Standort ein (falls vorhanden). Suchen Sie eine Nummer und wählen Sie dann **Buy**. <br><br> ![Ein Button zum Kauf der aufgelisteten Telefonnummer.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. Gehen Sie nach dem Kauf Ihrer Telefonnummer zu **Active Numbers** und wählen Sie die gerade gekaufte Telefonnummer aus. <br><br>![„Active Numbers“ mit der gekauften Telefonnummer.]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### Schritt 2: Ihre Telefonnummer konfigurieren {#step-2-configure-your-phone-number}

Konfigurieren Sie Ihre Twilio-Telefonnummer so, dass Verifizierungscodes per E-Mail empfangen werden. **Verknüpfen Sie Ihre Telefonnummer nicht mit WhatsApp in der Twilio-Konsole.**

{% alert warning %}
Verknüpfen Sie Ihre Telefonnummer nicht mit WhatsApp in der Twilio-Konsole. Wenn Sie dies tun, wird die Nummer beim WhatsApp Business Account von Twilio registriert, was Sie daran hindert, sie über den Embedded-Sign-up-Workflow mit Braze zu verbinden.
{% endalert %}

1. Gehen Sie in der Twilio-Konsole zur Seite [Active Numbers](https://www.twilio.com/console/phone-numbers/incoming) und wählen Sie die gekaufte Telefonnummer aus.
2. Gehen Sie zum Abschnitt **Voice Configuration** und wählen Sie im Dropdown **Configure with** die Option **Webhook, TwiML Bin, Function, Studio Flow, Proxy Service**.
3. Wählen Sie in der Zeile **A call comes in** die Option **Webhook** und setzen Sie die URL auf `https://twimlets.com/voicemail?Email=YOUR_EMAIL_ADDRESS`, wobei Sie `YOUR_EMAIL_ADDRESS` durch Ihre E-Mail-Adresse ersetzen.

### Schritt 3: Den Embedded-Sign-up-Workflow abschließen {#step-3-complete-the-embedded-sign-up-workflow}

1. Nachdem Twilio konfiguriert ist, gehen Sie in Ihrem Braze-Dashboard zu **Technologie-Partner** > **WhatsApp** und wählen Sie **Begin integration** oder **Add WhatsApp Business Account** (je nachdem, was angezeigt wird), um den [Embedded-Sign-up-Workflow]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup) auszulösen.<br><br>Wählen Sie im Schritt **Add a phone number for WhatsApp** die Option **Phone call**, um Ihre Telefonnummer zu verifizieren. <br><br>![Abschnitt mit den Optionen zur Verifizierung Ihrer Telefonnummer per SMS oder Telefonanruf.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. Warten Sie einige Minuten, bis der Verifizierungscode an Ihren E-Mail-Posteingang gesendet wird, geben Sie dann den Verifizierungscode ein und schließen Sie die Einrichtung ab.

## Eine Infobip-Telefonnummer erwerben {#acquiring-an-infobip-phone-number}

1. Gehen Sie in der Infobip-Konsole zu **Channels and Numbers** und wählen Sie **Numbers**.<br><br>![Infobip-Abschnitt „Channels and Numbers“ mit darunter aufgeführtem „Numbers“.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. Wählen Sie **Buy Number** > das Land, in das Sie Nachrichten senden möchten > **SMS**.<br><br>![Button zum Kauf einer Nummer.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. Je nach ausgewähltem Land müssen Sie möglicherweise einen zusätzlichen Registrierungsprozess durchlaufen (z. B. die Auswahl einer 10DLC- oder gebührenfreien Option für US-Telefonnummern). Stellen Sie sicher, dass Sie die verfügbare Option auswählen.<br><br>![Eine Seite, auf der Sie den Nummerntyp auswählen: entweder 10DLC oder gebührenfrei.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. Wählen Sie das verfügbare Angebot aus, fahren Sie dann mit den restlichen Schritten fort und warten Sie, bis Ihre Anfrage bearbeitet wird. Sie können den Status überprüfen, indem Sie zu **Numbers** > **My Request** gehen. <br><br>![Ein Angebot mit Informationen zu Gebühren und Abdeckung.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. Je nach ausgewähltem Land warten Sie darauf, dass das Infobip-Team Sie bezüglich der Registrierungsdetails kontaktiert (z. B. für 10DLC in den USA).<br><br>

6. Wenn Ihre Telefonnummer in Infobip bereit ist, gehen Sie in Ihrem Braze-Dashboard zu **Technologie-Partner** > **WhatsApp** und wählen Sie **Begin integration** oder **Add WhatsApp Business Account** (je nachdem, was angezeigt wird), um den [Embedded-Sign-up-Workflow]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup) auszulösen.<br><br> Wählen Sie im Schritt **Add a phone number for WhatsApp** die Option **Text message**, um Ihre Telefonnummer zu verifizieren.<br><br>![Abschnitt mit den Optionen zur Verifizierung Ihrer Telefonnummer per SMS oder Telefonanruf.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Überprüfen Sie die [Analyze Logs](https://www.infobip.com/docs/analyze/analyze-logs) von Infobip in deren Kundenportal auf den Verifizierungscode, der möglicherweise einige Minuten benötigt, um zu erscheinen. Geben Sie dann den Verifizierungscode ein und schließen Sie die Einrichtung ab.