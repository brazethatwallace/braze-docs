---
nav_title: "Telefonnummern von Nutzer:innen"
article_title: Kurzmitteilungsdienst or SMS-Telefonnummern von Nutzer:innen
page_order: 3
description: "Dieser Referenzartikel behandelt die Formatierung von Kurzmitteilungsdienst or SMS-Telefonnummern, den Import von Telefonnummern sowie das Hinzufügen von Nutzer:innen zu Kurzmitteilungsdienst or SMS-Abo-Gruppen."
page_type: reference
alias: /user_phone_numbers/
channel:
  - SMS
  - MMS
  - RCS
---

# Telefonnummern von Nutzer:innen {#user-phone-numbers}

> Dieser Artikel behandelt verschiedene Themen rund um die Telefonnummern Ihrer Nutzer:innen bzw. Kund:innen. Wenn Sie Informationen zu Ihren eigenen Nummern suchen, lesen Sie unseren Artikel zu [Sende-Telefonnummern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).

## Empfohlenes Format {#recommended-format}

Wir empfehlen, Telefonnummern im [`E.164`](https://en.wikipedia.org/wiki/e.164)-Format zu importieren, um die Genauigkeit sicherzustellen – insbesondere wenn Sie in mehrere Regionen mit unterschiedlichen Landes- oder Ortsvorwahlen senden&#8212;auch für US-amerikanische Telefonnummern.

- **US-Nummern:** Alle US-Nummern müssen gültige, 10-stellige Telefonnummern mit einer gültigen Vorwahl sein. Wenn bei einer 10-stelligen Telefonnummer das `+` und die Landesvorwahl fehlen, ordnet Braze sie als US-Nummer zu. Puerto-ricanische Telefonnummern erfordern weiterhin ein `+` und eine Landesvorwahl, obwohl sie das 10-stellige Format mit US-Vorwahlen verwenden.
- **Internationale Nummern:** Alle internationalen Nummern sollten mit einem `+` beginnen, gefolgt von der Landesvorwahl und dann der Telefonnummer. Zum Beispiel: `+442071838750`.

![Beispiel einer gültigen internationalen Telefonnummer im E.164-Format.]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

Hier sind einige Beispiele, die die Unterschiede zwischen lokaler und `E.164`-Formatierung zeigen:

| Land | Lokal | Landesvorwahl | `E.164` |
|---|---|---|---|
| USA | `4155552671` | 1 | `+14155552671` |
| Großbritannien | `2071838750` | 44 | `+442071838750` |
| Brasilien | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Empfohlenes Format" }

## Telefonnummern importieren {#import-phone-numbers}

Beim Importieren von Telefonnummern ist es wichtig, dass Sie das [empfohlene Format](#recommended-format) einhalten. Um Telefonnummern zu importieren, verwenden Sie eine der folgenden Methoden:

- [Eine CSV-Datei in Braze hochladen]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)
- [Den `/users/track`-Endpunkt verwenden]({{site.baseurl}}/api/endpoints/user_data/post_user_track)

{% alert important %}
Die Telefonnummern von Nutzer:innen werden in Braze als Zeichenfolge aus Ziffern angezeigt. Wenn Sie eine Nummer importieren, die neben dem vorangestellten {% raw %}`+`{% endraw %} Nicht-Ziffern enthält (z. B. `,`, `-` oder `(`), werden die Nicht-Ziffern bei der Darstellung in Braze entfernt. Beispielsweise wird `+1 (724) 123-4567` nach dem Import als `+17241234567` angezeigt.
{% endalert %}

## Validierung von Telefonnummern {#phone-number-validation}

Braze verwendet Googles [libphonenumber](https://github.com/google/libphonenumber)-Bibliothek zur Validierung von Telefonnummern. Wenn neue Mobilfunknummernpräfixe eingeführt werden, wird die Unterstützung hinzugefügt, sobald die zugrunde liegende Bibliothek aktualisiert wird. Braze pflegt keine separate Liste gültiger Präfixe.

### Umgang mit ungültigen Telefonnummern {#handling-invalid-phone-numbers}

Wenn eine Telefonnummer als ungültig eingestuft wird, markiert Braze die Telefonnummer der Nutzer:innen als ungültig und unternimmt keinen weiteren Versuch, Nachrichten an diese Telefonnummer zu senden. Eine ungültige Telefonnummer wird im **Engagement-Tab** eines Nutzerprofils markiert.

![Beispielfehlermeldung für ungültige Telefonnummern in Braze.]({% image_buster /assets/img/sms/invalid_banner.png %}){: style="max-width:50%;border: 0;"}

Eine Telefonnummer wird aus folgenden Gründen als ungültig eingestuft:

- **Anbieterfehler**: Vom Kurzmitteilungsdienst or SMS- und RCS-Anbieter wurde ein permanenter Fehler zurückgegeben. Dies weist darauf hin, dass die angegebene Telefonnummer falsch formatiert ist oder dauerhaft keine Kurzmitteilungsdienst or SMS- oder RCS-Nachrichten empfangen kann.
- **Deaktiviert**: Die Telefonnummer wurde deaktiviert, weil ein:e Mobilfunkteilnehmer:in den Vertrag gekündigt und die Nummer beim Anbieter freigegeben hat (und die Nummer möglicherweise recycelt und neuen Nutzer:innen zugewiesen wird). Eine deaktivierte Telefonnummer kann auch dann als ungültig markiert werden, wenn Sie keine Kurzmitteilungsdienst or SMS- oder RCS-Nachrichten an diese Telefonnummer gesendet haben.

Diese ungültigen Telefonnummern können über [Kurzmitteilungsdienst or SMS- und RCS-Endpunkte]({{site.baseurl}}/api/endpoints/sms) verwaltet werden.

{% alert note %}
Wenn mehrere Nutzerprofile dieselbe Telefonnummer haben und diese Telefonnummer als ungültig markiert wird, werden alle bestehenden Nutzerprofile mit dieser Nummer als ungültig angezeigt. Neu erstellte Nutzerprofile werden anfänglich niemals als ungültig markiert.
{% endalert %}

Sie können beim [Erstellen eines Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#step-4-add-filters-to-your-segment) auch Nutzer:innen mit ungültigen Telefonnummern ein- oder ausschließen.

## Abgelehnte Kurzmitteilungsdienst or SMS-Sends von der Segmentierung ausschließen {#exclude-rejected-sms-sends-from-segmentation}

{% alert important %}
Kurzmitteilungsdienst or SMS-Ablehnungen können je nach Ihrem Braze-Vertrag und Kurzmitteilungsdienst or SMS-Anbieter auf Ihr Kurzmitteilungsdienst or SMS-Kontingent angerechnet werden. Informationen zu Abrechnungsfolgen finden Sie unter [Reporting]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting).
{% endalert %}

Um Nutzer:innen mit abgelehnten Kurzmitteilungsdienst or SMS-Sends aus Ihren Segmenten auszuschließen, verwenden Sie [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) und gehen Sie wie folgt vor:

1. Gehen Sie zu **Audience** > **Segment Extensions**.
2. Wählen Sie **Create New Extension** > **Full refresh** oder **Incremental refresh** aus.
3. Schreiben Sie eine SQL-Abfrage, die Nutzer:innen mit Kurzmitteilungsdienst or SMS-Ablehnungen identifiziert. Sie können beispielsweise das Ereignis `USERS_MESSAGES_SMS_REJECTION_SHARED` abfragen, um Nutzer:innen zu finden, die Kurzmitteilungsdienst or SMS-Ablehnungen erhalten haben.
4. Speichern Sie Ihre Segmenterweiterung.
5. Wenn Sie Ihr Kurzmitteilungsdienst or SMS-Segment erstellen, fügen Sie einen Filter hinzu, um Nutzer:innen in dieser Segmenterweiterung auszuschließen.

## Nutzer:innen zu Kurzmitteilungsdienst or SMS- und RCS-Abo-Gruppen hinzufügen {#add-users-to-sms-and-rcs-subscription-groups}

Damit Nutzer:innen eine Kurzmitteilungsdienst or SMS- oder RCS-Nachricht erhalten können, müssen sie über eine gültige Telefonnummer verfügen und sich für eine Abo-Gruppe angemeldet haben. Abo-Gruppen sind an das Kurzmitteilungsdienst or SMS- oder RCS-Programm gebunden, das Sie betreiben (stellen Sie sicher, dass Sie die [gesetzlichen Anforderungen für Kurzmitteilungsdienst or SMS, MMS und RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) einhalten und die Einwilligung jeder Kundin und jedes Kunden dokumentiert haben). Weitere Informationen finden Sie unter [Kurzmitteilungsdienst or SMS- und RCS-Abo-Gruppen]({{site.baseurl}}/sms_rcs_subscription_groups).

## Beschaffung und Überprüfung durch Drittanbieter {#third-party-sourcing-and-verification}

Braze nutzt Tools von Drittanbietern, um ungültige Nummern zu ermitteln. Braze ist nicht verantwortlich für Ausfälle oder fehlerhafte Informationen dieser Dienste. Dieses Tool sollte daher nicht als einzige Methode zur Einhaltung von Vorschriften bei der Überprüfung ungültiger Nummern verwendet werden.

## Erfassung von Telefonnummern {#phone-number-capture}

Um Telefonnummern über In-App-Nachrichten zu erfassen, lesen Sie den Artikel [Anmeldeformular für Kurzmitteilungsdienst or SMS, RCS und WhatsApp]({{site.baseurl}}/phone_number_capture).