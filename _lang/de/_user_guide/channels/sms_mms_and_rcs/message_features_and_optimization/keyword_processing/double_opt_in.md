---
nav_title: Double-Opt-in
article_title: Double-Opt-in
description: "Dieser Referenzartikel behandelt die Double-Opt-in-Funktion und erklärt, wie Sie das Feature aktivieren, Opt-in-Keywords und Antwortnachrichten auswählen und Nutzer:innen über Abo-Aktualisierungen, die über REST API, SDK und Präferenzzentrum-Updates erfolgen, in den Double-Opt-in-Workflow einbinden."
page_type: reference
page_order: 1
channel:
  - SMS
  - MMS
  - RCS
---

# Double-Opt-in {#double-opt-in}

> Die Double-Opt-in-Funktion erfordert, dass Nutzer:innen ihre Opt-in-Absicht ausdrücklich bestätigen, bevor sie SMS-, MMS- oder RCS-Nachrichten empfangen können. Dadurch wird das Messaging auf engagierte Nutzer:innen fokussiert und die Einhaltung von Compliance-Best-Practices unterstützt.

Wenn Double-Opt-in aktiviert ist, erhalten Nutzer:innen eine Nachricht, die ihre ausdrückliche Zustimmung einholt, bevor sie von Ihren Campaigns oder Canvases angeschrieben werden können.

Obwohl es keine ausdrückliche Anforderung des Telephone Consumer Protection Act von 1991 (TCPA) ist, empfiehlt Braze, Double-Opt-in zu konfigurieren, um sicherzustellen, dass Nutzer:innen sich bewusst sind und zustimmen, Teil Ihres SMS-, MMS- oder RCS-Programms zu sein. Weitere Informationen zur Compliance finden Sie unter [Gesetze, Vorschriften und Missbrauchsprävention für SMS, MMS und RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

## Double-Opt-in-Workflows {#double-opt-in-workflows}

Double-Opt-in ermöglicht es Ihnen, eine ausdrückliche Einwilligung durch eingehende und ausgehende Opt-in-Campaigns einzuholen.

### Ausgehend {#outbound}

Wenn Nutzer:innen ihre Telefonnummer angeben, erhalten sie eine Nachricht, die um ihre Einwilligung bittet.

![Screenshot einer ausgehenden SMS-Nachricht, in der die Marke schreibt: „Willkommen bei BRAND-Textupdates! 1 Nachricht pro Woche mit den neuesten Angeboten. Antworten Sie mit Y für das Opt-in.“, die Nutzer:innen mit „Y“ antworten und die Marke daraufhin antwortet: „Danke! Sie haben jetzt das Opt-in für BRAND-Benachrichtigungen erteilt. Hier ist ein Promo-Code SMS10 für 10 % Rabatt auf Ihren ersten Einkauf!“]({% image_buster /assets/img/double_opt_in_outbound.png %}){:style="max-width:40%;"}

### Eingehend {#inbound}

Wenn Nutzer:innen eine Nachricht mit einem Opt-in-Schlüsselwort senden, erhalten sie eine Nachricht, die um ihre Einwilligung bittet.

![Screenshot einer eingehenden SMS-Nachricht, in der Nutzer:innen „JOIN“ senden und die Antwort erhalten: „Antworten Sie mit Y, um zu bestätigen, dass Sie unserem SMS-Programm beitreten möchten. 3 Nachrichten/Woche, schreiben Sie jederzeit STOP zum Beenden“, und dann mit „Y“ antworten.]({% image_buster /assets/img/double_opt_in_inbound.png %}){:style="max-width:40%;"}

## Double-Opt-in aktivieren {#enabling-double-opt-in}

Um das Double-Opt-in zu aktivieren, navigieren Sie zur Tabelle **Global Keywords** in der entsprechenden Abo-Gruppe und klicken Sie auf **Edit** in der **Opt-In Keyword Category**. Wählen Sie anschließend Ihre Opt-in-Methode (**Opt-In** oder **Double Opt-In**). Wenn Sie **Double Opt-In** auswählen, wird die Seite erweitert und zeigt zusätzliche [konfigurierbare Felder](#configurable-fields) an.

![Der Abschnitt „Opt-In Method“ bietet zwei Opt-in-Methoden zur Auswahl: „Opt-In“ und „Double Opt-In“.]({% image_buster /assets/img/double_opt_in_method.png %}){:style="max-width:50%;"}

### Konfigurierbare Felder {#configurable-fields}

| Kategorie   |    Felder    | Beschreibung
| ----------- |----------- |----------------
| Opt-In Prompt | Keywords | Dies sind die Schlüsselwörter, die Nutzer:innen per SMS senden können, um ihre Opt-in-Absicht zu signalisieren. `START` ist ein erforderliches Schlüsselwort. Diese Opt-in-Anfrage wird auch an Nutzer:innen gesendet, wenn ihr Abo-Status durch Quellen aktualisiert wird, die im Abschnitt [Abo-Quellen](#subscription-sources) aufgeführt sind.
| | Reply Message | Dies ist die erste Antwort, die Nutzer:innen erhalten, nachdem sie ein Opt-in-Schlüsselwort gesendet haben (zum Beispiel: „Antworten Sie mit Y, um zu bestätigen, dass Sie Nachrichten von dieser Nummer erhalten möchten. Es können Nachrichten- und Datengebühren anfallen.“)
| Double Opt-In Confirmation | Keywords | Dies sind die Schlüsselwörter, mit denen Nutzer:innen antworten können, um ihre Opt-in-Absicht zu bestätigen. Mindestens ein Schlüsselwort ist erforderlich. Diese Schlüsselwörter sollten im Feld **Opt-In Prompt Reply Message** angegeben werden.
| | Reply Message | Dies ist die Bestätigungsantwort, die Nutzer:innen erhalten, nachdem sie ihr Opt-in ausdrücklich bestätigt haben und nun Nachrichten empfangen können. Der Abo-Gruppenstatus der Nutzer:innen wird auf `Subscribed` gesetzt.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Konfigurierbare Felder" }

Wenn Nutzer:innen eine Opt-in-Anfrage erhalten, haben sie 30 Tage Zeit, ihre Opt-in-Absicht zu bestätigen. Wenn Nutzer:innen sich nach Ablauf des 30-Tage-Fensters anmelden möchten, müssen sie ein Opt-in-Schlüsselwort senden, um den Double-Opt-in-Workflow erneut zu starten.

![Die konfigurierbaren Felder umfassen zwei Abschnitte: „Opt-In Prompt“ und „Double Opt-In Confirmation“, jeweils mit den Feldern „Keywords“ und „Reply Message“.]({% image_buster /assets/img/double_opt_in_fields.png %})

## Abo-Gruppenstatus {#subscription-group-status}

Erst nachdem Nutzer:innen den Double-Opt-in-Workflow abgeschlossen haben, wird ihr [Abo-Gruppenstatus]({{site.baseurl}}/sms_rcs_subscription_groups) auf `Subscribed` aktualisiert. Wenn Nutzer:innen den Workflow beginnen, ihn aber nicht abschließen, bleiben sie `Unsubscribed` und können keine Nachrichten aus dieser Abo-Gruppe erhalten.

Nutzer:innen können auch in den Double-Opt-in-Workflow aufgenommen werden, wenn sie über [andere Quellen abonniert]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) wurden (z. B. REST API, SDK).

## Abo-Quellen {#subscription-sources}

Nutzer:innen können den Double-Opt-in-Workflow auch über Abo-Aktualisierungen betreten, die außerhalb eingehender Nachrichten erfolgen. Zu diesen Quellen gehören Updates über die REST API, das SDK und das Präferenzzentrum. Wenn Nutzer:innen den Double-Opt-in-Workflow über diese Quellen betreten, erhalten sie die **Opt-In Prompt Reply Message**.

{% alert important %}
Wenn Nutzer:innen über andere Quellen als eingehende Nachrichten in den Double-Opt-in-Workflow eingebunden werden, erhalten sie höchstens eine Opt-in-Anfrage-Antwortnachricht in einem rollierenden 24-Stunden-Zeitraum, unabhängig davon, wie oft sie in diesen Workflow eingebunden werden.
{% endalert %}

Jede Abo-Quelle hat ein unterschiedliches Registrierungsverhalten, wie in der folgenden Tabelle beschrieben.

| Quelle | Double-Opt-in-Registrierungsverhalten |
| ----------- | ----------- |
| SDK | Nutzer:innen werden automatisch in den Double-Opt-in-Workflow aufgenommen, wenn sie sich über das Braze SDK anmelden. |
| REST API | Nutzer:innen können in den Workflow aufgenommen werden, wenn der Abo-Status über `/subscription/status/set`, `/v2/subscription/status/set` oder `/users/track` gesetzt wird und der optionale Parameter `use_double_opt_in_logic` als `true` übergeben wird (zum Beispiel [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed", "use_double_opt_in_logic": true}]). Wenn dieser Parameter weggelassen wird, werden Nutzer:innen nicht in den Double-Opt-in-Workflow aufgenommen. <br><br>Wenn `use_double_opt_in_logic` mit der REST API verwendet wird und kein Nutzerprofil mit der angegebenen Telefonnummer verknüpft ist, wird der Abo-Status nicht aktualisiert und die Nutzer:innen können nicht in den Double-Opt-in-Workflow aufgenommen werden. |
| Shopify | Nutzer:innen werden nicht in den Double-Opt-in-Workflow aufgenommen, wenn ihr Abo-Status durch unsere Shopify-Integration gesetzt wird. |
| Nutzerimport | Nutzer:innen werden nicht in den Double-Opt-in-Workflow aufgenommen, wenn ihr Abo-Status durch den Nutzerimport gesetzt wird. |
| [Präferenzzentrum]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center) | Nutzer:innen werden automatisch in den Double-Opt-in-Workflow aufgenommen, wenn sie sich über ein Präferenzzentrum anmelden. |
| Nutzeraktualisierungsschritt | Nutzer:innen können in den Double-Opt-in-Workflow aufgenommen werden, wenn ihr Abo-Status über den Nutzeraktualisierungsschritt gesetzt wird und der optionale Parameter `use_double_opt_in_logic` als `true` übergeben wird. Wenn dieser Parameter weggelassen wird, werden Nutzer:innen nicht in den Double-Opt-in-Workflow aufgenommen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abo-Quellen" }

## Unterstützung mehrerer Sprachen {#multi-language-support}
Für eingehende Nachrichten wird Double-Opt-in für alle Sprachen unterstützt, die in der Abo-Gruppe definiert sind. Das bedeutet, dass Sie Ihre automatischen Antworten in verschiedenen Sprachen definieren können und Braze die automatische Antwort sendet, die einer bestimmten Sprache zugeordnet ist, wenn ein passendes Schlüsselwort empfangen wird.

Nutzer:innen, die den Double-Opt-in-Workflow über Abo-Aktualisierungen starten, die außerhalb eingehender Nachrichten erfolgen (z. B. SDK, REST API, Shopify), erhalten nur die englischen Schlüsselwörter.