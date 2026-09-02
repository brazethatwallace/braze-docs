---
nav_title: Kurzmitteilungsdienst or SMS-Versand
article_title: Kurzmitteilungsdienst or SMS-Versand
page_order: 4
alias: /sms_message_sending/
description: "Erfahren Sie mehr über Abo-Gruppen, Nachrichtenabrechnung und die Grundlagen der Schlüsselwortverarbeitung für den Kurzmitteilungsdienst or SMS-Versand."
page_type: reference
channel:
  - SMS

---

# Kurzmitteilungsdienst or SMS-Nachrichtenversand {#sms-message-sending}

> Erfahren Sie mehr über die Grundlagen von Abos, Abrechnung und Schlüsselwortverarbeitung, die beim Versand von Kurzmitteilungsdienst or SMS-Nachrichten mit Braze relevant sind.

## Grundlagen des Kurzmitteilungsdienst or SMS-Versands {#sms-sending-basics}

### Abo-Gruppe auswählen {#select-your-subscription-group}

Senden Sie Kurzmitteilungsdienst or SMS-Nachrichten über eine [Abo-Gruppe]({{site.baseurl}}/sms_rcs_subscription_groups). Eine Abo-Gruppe enthält Telefonnummern für den Versand, wie Shortcodes, Langcodes und alphanumerische Sender-IDs, für einen bestimmten Messaging-Zweck. Verwenden Sie separate Abo-Gruppen für Anwendungsfälle wie transaktionsbezogenes und aktionsbezogenes Messaging.

### Nachricht verfassen {#compose-the-message}

Informationen zu Nachrichtenfeldern, Zeichenlimits, Personalisierung, Medien und Linkverkürzung finden Sie unter [Kurzmitteilungsdienst or SMS-, MMS- oder RCS-Nachricht erstellen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create#sms-and-mms-fields-and-settings).

### Nachrichtensegmente und Zeichenlimits verstehen {#understand-message-segments-and-character-limits}

Kurzmitteilungsdienst or SMS-Nachrichten verwenden GSM-7- oder UCS-2-Codierung und werden pro Nachrichtensegment abgerechnet. Informationen zu Codierungsregeln, Segmentgrößen und dem Segmentrechner finden Sie unter [Kurzmitteilungsdienst or SMS- und RCS-Abrechnungsrechner]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).

### Schlüsselwort-Anpassung (optional) {#keyword-customization-optional}

Vorschriften erfordern Antworten auf Opt-in-, Opt-out- und Hilfe- oder Info-Schlüsselwörter. Definieren Sie Schlüsselwörter, Antworten und sprachspezifische Schlüsselwort-Sets über die [Schlüsselwortverarbeitung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing).

Best Practices für den Versand, einschließlich Anleitungen für den Versand in mehrere Länder und für hohe Volumen, finden Sie unter [Best Practices für Kurzmitteilungsdienst or SMS, MMS und RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/best_practices).