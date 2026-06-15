---
nav_title: SMS-Versand
article_title: SMS-Versand
page_order: 4
alias: /sms_message_sending/
description: "Dieser Referenzartikel behandelt die Grundlagen und Best Practices des SMS-Versands."
page_type: reference
channel:
  - SMS

---

# SMS-Nachrichtenversand {#sms-message-sending}

> Messaging kann kompliziert sein, muss es aber nicht. Die folgenden Abschnitte erläutern die Grundlagen des SMS-Nachrichtenversands bei Braze, einschließlich der Bedeutung von Abo-Gruppen, der Anforderungen für SMS-Nachrichten-Segmente und Nachrichtentexte sowie der verfügbaren erweiterten Anpassungsoptionen.

## Grundlagen des SMS-Versands {#sms-sending-basics}

### Abo-Gruppe auswählen {#select-your-subscription-group}

SMS-Nachrichten müssen über eine [Abo-Gruppe]({{site.baseurl}}/sms_rcs_subscription_groups/) gesendet werden. Eine Abo-Gruppe ist eine Sammlung von Sende-Telefonnummern (wie Shortcodes, Langcodes und/oder alphanumerische Sender-IDs), die für einen bestimmten Messaging-Zweck verwendet werden. Sie müssen eine Abo-Gruppe festlegen, um sicherzustellen, dass nur abonnierte Nutzer:innen angesprochen werden. Einige Kunden stellen möglicherweise fest, dass sie mehrere Abo-Gruppen für verschiedene Anwendungsfälle haben, z. B. für transaktionsbezogenes SMS-Messaging und werbliches SMS-Messaging.<br><br>

### Nachrichtentext eingeben {#input-message-body}

Ein SMS-Nachrichtentext akzeptiert bis zu 1.600 Zeichen, einschließlich Emojis, Liquid und Connected-Content. Ein einzelner Campaign-Versand kann zu mehreren Nachrichten-Segment-Sendungen führen. SMS-Nachrichtentexte in Braze können entweder im [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38)- oder im [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set)-Codierungsstandard verfasst werden. Falls ein UCS-2-Zeichen (z. B. ein Emoji) verwendet wird, wird der Nachrichtentext automatisch für diesen Codierungsstandard formatiert.<br><br>

### Nachrichten-Segmente und Zeichenlimits verstehen {#understand-message-segments-and-character-limits}

SMS-Nachrichten-Segmente sind die Art und Weise, wie die SMS-Branche Nachrichten zählt. Ein Nachrichten-Segment ist eine Gruppierung von bis zu einer definierten Anzahl von Zeichen (160 für GSM-7-Codierung; 67 für UCS-2-Codierung), die in einem einzelnen SMS-Versand gesendet wird. Wenn Sie eine SMS mit 161 Zeichen in GSM-7-Codierung versenden, werden Sie feststellen, dass zwei (2) Nachrichten-Segmente gesendet wurden. Das Senden mehrerer Nachrichten-Segmente kann zu zusätzlichen Kosten führen.<br><br>

### Schlüsselwort-Anpassung (optional) {#keyword-customization-optional}

Vorschriften verlangen, dass es Antworten auf alle Opt-in-, Opt-out- und Hilfe-/Info-SMS-Schlüsselwortantworten gibt. Mit Braze können Sie Ihre eigenen Schlüsselwörter definieren, um Opt-in-, Opt-out- und Hilfe-Antworten auszulösen, Ihre eigenen Antworten verwalten, die an Nutzer:innen gesendet werden, und Schlüsselwort-Sets für verschiedene Sprachen festlegen. Weitere Informationen finden Sie in unserer Sammlung zur [Schlüsselwortverarbeitung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/).

{% alert tip %}
Möchten Sie erfahren, wie Sie eine SMS-Campaign erstellen? Lesen Sie unsere Schritt-für-Schritt-Anleitung zum [Erstellen einer SMS-, MMS- oder RCS-Nachricht]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/).
{% endalert %}

Best Practices für den Versand, einschließlich Anleitungen für den Versand in mehrere Länder und für hohe Volumina, finden Sie unter [Best Practices für SMS, MMS und RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/best_practices/).