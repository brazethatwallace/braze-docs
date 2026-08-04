---
nav_title: FAQ
article_title: FAQ zu SMS, MMS und RCS
page_order: 30
description: "Dieser Artikel beantwortet häufig gestellte Fragen zu SMS-, MMS- und RCS-Messaging."
page_type: FAQ
alias: /sms_mms_rcs_faq/
channel:
  - SMS
  - MMS
  - RCS
---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Dieser Artikel beantwortet häufig gestellte Fragen zu SMS-, MMS- und RCS-Messaging.

## Allgemein {#general}

### Was ist eine `app_id` im SMS-API-Objekt? {#what-is-an-app_id-in-the-sms-api-object}

Der App-Bezeichner-API-Schlüssel oder die `app_id` ist ein Parameter, der Aktivitäten mit einer bestimmten App in Ihrem Workspace verknüpft. Er legt fest, mit welcher App innerhalb des Workspace Sie interagieren. Beispielsweise haben Sie eine `app_id` für Ihre iOS-App, eine `app_id` für Ihre Android-App und eine `app_id` für Ihre Web-Integration.

Für SMS ist der Parameter `app_id` beim Senden von SMS-Nachrichten über die API (z. B. über den Endpunkt `/messages/send`) erforderlich. Er gibt an, welche App in Ihrem Workspace mit der SMS-Aktivität oder dem API-Aufruf verknüpft ist. Sie können jede gültige `app_id` einer in Ihrem Workspace konfigurierten App für SMS-Messaging verwenden, unabhängig davon, ob die Nutzer:innen diese bestimmte App in ihrem Profil haben.

Sie finden Ihre `app_id`, indem Sie zu **Einstellungen** > **App-Einstellungen** navigieren und den Abschnitt **Identification** suchen.

### Was passiert, wenn mehrere Nutzer:innen dieselbe Telefonnummer haben? {#what-happens-if-multiple-users-have-the-same-phone-number}

Wenn mehrere Nutzerprofile, die dieselbe Telefonnummer teilen (für SMS aktiviert), gleichzeitig für eine aktionsbasierte Campaign oder eine Canvas-Komponente infrage kommen, die durch ein eingehendes SMS-Ereignis ausgelöst wird, dedupliziert Braze die Nutzer:innen auf der Ebene der Canvas-Komponente. Dadurch wird verhindert, dass Nutzer:innen mehr als eine SMS für eine Canvas-Komponente erhalten, selbst wenn mehrere Nutzer:innen dieselbe Telefonnummer teilen.

{% alert note %}
Braze dedupliziert bei geplanten Canvases nicht nach Telefonnummer.
{% endalert %}

Braze verwendet den folgenden Ablauf, um das Empfängerprofil zu bestimmen:
- Prüfen, welches Profil zuletzt eine SMS erhalten hat (bis zu 7 Tage zurück); falls eines existiert, wird die Nachricht an diese:n Nutzer:in gesendet.
- Falls keines der Profile in den letzten 7 Tagen eine SMS erhalten hat, wird die Nachricht an das Profil gesendet, das einen Nutzer-Alias „phone“ hat, der mit der Telefonnummer übereinstimmt.
- Falls keines existiert, wird die Nachricht an ein zufälliges Profil aus den verfügbaren gesendet.

Wenn Sie ein „START“- oder „STOP“-Schlüsselwort von der geteilten Telefonnummer erhalten, werden alle Nutzerprofile für SMS abonniert und aktiviert bzw. abgemeldet. Dies gilt auch für API-Statusänderungen. Wenn beispielsweise mehrere Profile mit unterschiedlichen externen IDs dieselben Telefonnummern haben, aktualisiert eine Änderung des Abo-Gruppen-Status über die API alle Profile mit dieser Telefonnummer, auch wenn nur eine externe ID angegeben wird.

{% alert important %}
Wenn Sie Ihre Nutzer:innen gestaffelt in einen Canvas eintreten lassen und unterschiedliche Zeitpläne für jede Canvas-Komponente haben, können Sie Nutzer:innen mit derselben E-Mail-Adresse oder Telefonnummer doppelte Nachrichten senden.
{% endalert %}

Um unnötig große Aktualisierungen zu vermeiden, aktualisiert Braze maximal 100 Nutzerprofile, die einen Bezeichner teilen, wenn eine Abo-Aktualisierung vorgenommen wird. Wenn mehr als 100 Nutzerprofile dieselbe Telefonnummer teilen, werden nicht alle Profile aktualisiert.

### Was sind geteilte Shortcodes? {#what-are-shared-short-codes}

Bei einem geteilten Shortcode kommen alle Textnachrichten – unabhängig davon, welches Unternehmen oder welche Organisation sie sendet – von derselben 5- bis 6-stelligen Telefonnummer auf dem Mobilgerät der Verbraucher:innen an. Geteilte Shortcodes sind zwar relativ kostengünstig und sofort verfügbar, aber Ihr Unternehmen hat keinen dedizierten Shortcode.

Einige Nachteile dieses Ansatzes sind:

- Wenn sich Ihre Kund:innen von den Nachrichten eines anderen Unternehmens abmelden, das einen Shortcode mit Ihnen teilt, werden sie auch von Ihren Nachrichten abgemeldet.
- Wenn ein Unternehmen gegen die Regeln verstößt, werden die Nachrichten aller Unternehmen gesperrt.
- Sicherheitsprobleme

## Abrechnung und Preise {#billing-and-pricing}

### Wie wird SMS abgerechnet? {#how-will-i-be-billed-for-sms}

Neben den Gebühren für Short- und Langcodes stellt Braze ein Kontingent an SMS-Nachrichten für verschiedene Länder bereit. Das heißt, wir legen gemeinsam mit Ihnen eine bestimmte Anzahl von Nachrichtensegmenten für verschiedene Länder fest, die Sie zum Versand von SMS-Campaigns nutzen. Die Abrechnung erfolgt nach der Anzahl der pro Land gesendeten Nachrichtensegmente. Weitere Informationen zur Berechnung von Nachrichtensegmenten finden Sie in unserem Leitfaden zu [Nachrichtensegmenten und Zeichenlimits]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator). Ihr Account Manager wird Sie kontaktieren, wenn Sie sich Ihrem Maximum nähern, und Ihnen relevante Berichte zur Verfügung stellen, damit Sie stets informiert bleiben. Bei weiteren Fragen zu Mehrkosten wenden Sie sich bitte an Ihre Braze-Vertretung.

### Unterscheiden sich die Preise für MMS und SMS? {#does-mms-and-sms-pricing-differ}

MMS und SMS haben unterschiedliche Kosten und werden separat nach Volumen abgerechnet. Wenden Sie sich für Preisinformationen an das Braze-Onboarding-Team.

### Wie kann ich Mehrkosten vermeiden? {#how-can-i-avoid-overages}

Auch wenn wir nicht versprechen können, dass es nie zu Mehrkosten kommt, können Sie folgende Vorsichtsmaßnahmen treffen, um die Wahrscheinlichkeit einer Überschreitung Ihrer zugewiesenen Limits zu verringern:

- Achten Sie auf die Zeichenanzahl in Ihrer SMS. Das unbeabsichtigte Senden von mehr als einem Segment kann zu Mehrkosten führen. Weitere Details finden Sie in unserer [Segment-Aufschlüsselung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).
- Berechnen Sie Ihre SMS-Zeichen sorgfältig unter Berücksichtigung von Liquid oder Connected-Content. Der Braze-SMS-Composer in Ihrem Dashboard schätzt die Nutzung dieser Features nicht ein und berücksichtigt sie nicht.
- Berücksichtigen Sie die Art der Kodierung, die Ihre Nachricht verwendet – wenn Ihre Nachricht GSM-7-Kodierung nutzt, können Sie in der Regel davon ausgehen, dass Sie eine Nachricht mit 128 Zeichen pro Nachrichtensegment senden können. Wenn Ihre Nachricht [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set)-Kodierung nutzt, können Sie in der Regel davon ausgehen, dass Sie eine Nachricht mit 67 Zeichen pro Nachrichtensegment senden können.
- Testen, testen und nochmals testen! Testen Sie Ihre SMS-Nachrichten immer vor dem Versand, insbesondere wenn Sie Liquid und Connected-Content verwenden.

### Wird eine an ein Festnetztelefon gesendete Nachricht trotzdem auf mein SMS-Sendekontingent angerechnet? {#if-a-message-is-sent-to-a-landline-will-the-message-still-count-toward-my-sms-send-count}

In den USA, Kanada und Großbritannien:
- Wenn eine SMS an ein Festnetztelefon gesendet wird, wird sie als **Undelivered** markiert. Beachten Sie, dass Twilio dennoch Gebühren für den Zustellversuch erhebt, sodass Nachrichten, die in Ihren Nachrichtenprotokollen als **Sent**, **Delivered** oder **Undelivered** markiert sind, abgerechnet werden.
- In Großbritannien wandeln einige Mobilfunkanbieter die SMS in eine Sprachnachricht um und stellen die Nachricht so zu.

In anderen Ländern:
- Twilio gibt einen Fehler aus, und Ihnen wird der versuchte SMS-Versand nicht in Rechnung gestellt.

### Warum warnt mich das Braze-Dashboard, dass mir möglicherweise zusätzliche Nachrichtensegmente berechnet werden, obwohl meine Nachricht unter 160 (GSM-7) oder 70 (UCS-2) Zeichen liegt? {#why-is-the-braze-dashboard-warning-me-i-may-be-charged-for-additional-message-segments-when-my-message-is-under-160-gsm-7-or-70-ucs-2-characters}

Ihnen könnten zusätzliche Nachrichtensegmente berechnet werden, wenn Ihre Nachricht Liquid-Personalisierung enthält. Content-Block-Templating findet erst statt, wenn die Nachricht zum Versand vorbereitet wird. Wenn Sie eine SMS mit einem Content-Block bearbeiten, weiß Braze nicht, was der Content-Block enthalten wird, sondern liefert nur eine grobe Schätzung. Wir empfehlen Nutzer:innen, den Testbereich zu verwenden, um eine Vorschau der Nachricht anzuzeigen und besser einschätzen zu können, was zu erwarten ist.

## Versand und Zustellbarkeit {#sending-and-deliverability}

### Können Links in einer SMS enthalten sein? {#can-you-include-links-in-an-sms}

Sie können jeden beliebigen Link in jede SMS-Campaign einfügen. Es gibt jedoch einige Punkte zu beachten:

- Links können einen großen Teil des 160-Zeichen-Limits für SMS beanspruchen. Wenn Sie einen Link und Text einfügen, kann dies zu zwei SMS-Nachrichten statt nur einer führen.
- Unternehmen verwenden häufig Link-Shortener, um die Auswirkung eines Links auf die Zeichenanzahl zu begrenzen. Wenn jedoch ein gekürzter Link über einen Langcode gesendet wird, können Mobilfunkanbieter die Nachricht blockieren oder ablehnen, da sie die Link-Weiterleitung als verdächtig einstufen könnten.
- Die Verwendung eines [Shortcodes]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) wäre der zuverlässigste Nummerntyp für das Einfügen von Links.

Braze verfügt auch über ein eigenes Link-Shortening-Feature, das Links automatisch kürzt und Click-through-Analytics bereitstellt. Weitere Informationen finden Sie unter [Link-Shortening]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening).

### Muss die Sendegeschwindigkeit von SMS-Nachrichten begrenzt werden? {#do-you-need-to-rate-limit-how-fast-you-send-sms-messages}

Die standardmäßige Parallelitätsrate und der Durchsatz ermöglichen etwa 360.000 Nachrichten pro Stunde pro Shortcode. Zusätzlicher Durchsatz erfordert zusätzliche Shortcodes.

### Wie werden URLs für SMS auf die Allowlist gesetzt? {#how-do-you-allowlist-urls-for-sms}

Bevor Sie SMS-Nachrichten mit URLs an Nutzer:innen in bestimmten Ländern senden (z. B. Schweden oder nordische Länder), müssen Sie diese URLs beim Mobilfunkanbieter registrieren lassen. Wenden Sie sich an Ihre:n Braze-Account-Manager:in, um Unterstützung zu erhalten. Dieser Vorgang dauert etwa fünf Tage.

### Was sind die besten Versandpraktiken, um Spam-Erkennung bei SMS zu vermeiden? {#what-are-the-best-sending-practices-to-avoid-spam-detection-for-sms}

1. Stellen Sie sicher, dass die Opt-in- und Opt-out-Anweisungen klar sind.
2. Stellen Sie sicher, dass Sie (die Marke) eine Beziehung zu den Kund:innen haben.
3. Stellen Sie sicher, dass der Inhalt für die Beziehung relevant ist und dem entspricht, wofür sich die Nutzer:innen angemeldet haben.

Weitere Richtlinien zur Vermeidung von Spam-Erkennung finden Sie unter [SMS-Gesetze und -Vorschriften]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

### Wie viele Zeichen verbraucht ein Emoji? {#how-many-characters-does-an-emoji-use}

Emojis können schwierig sein, da es keine standardisierte Zeichenanzahl für alle Emojis gibt. Es besteht das Risiko, dass das Emoji das Zeichenlimit überschreitet und die SMS in mehrere Nachrichten aufteilt, obwohl sie im Braze-Composer als eine einzige Nachricht angezeigt wird. Beim Testen Ihrer Nachrichten können Sie mit unserem [Segment-Rechner]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator) besser überprüfen, ob eine Nachricht aufgeteilt wird.

## Abo-Gruppen und Opt-in/Opt-out {#subscription-groups-and-opt-inopt-out}

### Wie erstellt man eine Logik für selektive SMS-Opt-ins, damit Nutzer:innen in der richtigen Abo-Gruppe sind? {#how-do-you-create-logic-for-selective-opt-ins-to-sms-so-users-are-in-the-right-subscription-group}

Angepasste Keywords werden als angepasste Events geschrieben, sodass Sie Segmente basierend auf den Keywords erstellen sollten, die Kund:innen per SMS senden können. Wenn sich ein:e Nutzer:in beispielsweise für VIP-Nachrichten per SMS anmeldet, aber nicht für Benachrichtigungen, können Sie ein VIP-Segment und ein Benachrichtigungs-Segment erstellen und die/den Nutzer:in dann dem entsprechenden Segment zuweisen.

### Wenn ein:e Nutzer:in „Stop“ an unseren Shortcode sendet, wird er/sie von der Abo-Gruppe abgemeldet? {#if-a-user-texts-stop-to-our-short-code-are-they-unsubscribed-from-the-subscription-group}

Wie sieht das im Nutzerprofil aus? Die Abo-Gruppe wird auf 2 Striche (- -) zurückgesetzt, und es werden angepasste Events für das Anmelden und Abmelden erstellt.

### Wenn ein:e Nutzer:in abgemeldet ist und ein Keyword an unseren Short- und Langcode sendet, erhält er/sie die Antwort, die wir für dieses Keyword in Braze konfiguriert haben? {#if-a-user-is-opted-out-and-sends-a-keyword-to-our-short-and-long-code-do-they-receive-the-response-we-configured-for-that-keyword-in-braze}

Wenn ein:e Nutzer:in abgemeldet ist und ein Keyword aus einer der [Standard-Keyword-Kategorien]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout) sendet, erhält er/sie die Antwort für dieses Keyword. Wenn ein:e Nutzer:in abgemeldet ist und ein [angepasstes Keyword]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling) sendet, erhält er/sie die Antwort für dieses Keyword nicht.

### Erfassen SMS-Event-Eigenschaften Keywords innerhalb eines Satzes? {#will-sms-event-properties-capture-keywords-in-a-sentence}

Damit ein Keyword innerhalb eines Satzes erkannt wird (zum Beispiel „bitte hör auf mir zu schreiben“), müssen Sie eine Liquid-Anweisung in der Nachricht verwenden, um das bestimmte Wort zu erkennen. Event-Eigenschaften haben ein Zeichenlimit von 256; ansonsten gibt es kein Zeichenlimit.

## Testen {#testing}

### Zählen Test-SMS für die Limits? {#do-test-text-messages-count-toward-limits}

Ja. Behalten Sie das beim Testen von Nachrichten im Hinterkopf.

### Muss ein:e Nutzer:in Teil einer SMS-Abo-Gruppe sein, um SMS-Testnachrichten zu erhalten? {#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages}

Ja. Nutzer:innen müssen eine gültige Telefonnummer haben, Teil der für den Testversand verwendeten SMS-Abo-Gruppe sein und mindestens ein Land unter **Geographic Permissions** für SMS ausgewählt haben.

### Gibt es eine Möglichkeit zu sehen, ob ein Alias in einem Nutzerprofil vorhanden ist? {#is-there-a-way-to-see-if-an-alias-exists-on-a-user-profile}

Aliase sind im Nutzerprofil nicht sichtbar. Sie müssten die Endpunkte zum [Exportieren von Nutzerdaten]({{site.baseurl}}/api/endpoints/export) verwenden, um zu bestätigen, dass Aliase gesetzt wurden.

## MMS

### Gibt es Änderungen an Currents-Daten beim Senden einer MMS? {#are-there-any-changes-to-currents-data-when-sending-an-mms}

Nein, beim Senden einer MMS-Nachricht wird dasselbe Maß an Insights bereitgestellt.

### Kann ich die Reihenfolge steuern, in der das Bild und der Nachrichtentext einer MMS zugestellt werden? {#can-i-control-the-order-in-which-the-image-and-message-body-of-an-mms-are-delivered}

Braze hat keine Kontrolle über die Anzeigereihenfolge, wenn sowohl ein Nachrichtentext als auch Bilder in einer MMS-Nachricht enthalten sind. Dies hängt von mehreren Faktoren ab, darunter unter anderem:

- Der Carrier, der die Nachricht empfängt
- Das Gerät, das die Nachricht empfängt
- Die Gesamtgröße der Nachricht

### Erfordert MMS einen separaten Onboarding-Prozess? {#does-mms-require-a-separate-onboarding-process}

Nein. MMS ist jetzt in unserem SMS-Onboarding-Prozess enthalten. Bestehende Kund:innen, die das Onboarding bereits durchlaufen haben, können nach Abschluss der folgenden Schritte mit dem Senden von MMS-Campaigns beginnen:

1. MMS erwerben.
2. Das Braze-Onboarding-Team kontaktieren und die Aktivierung des MMS-Features anfordern. Dadurch wird MMS aktiviert und eine SMS/MMS-Abo-Gruppe wird für Sie erstellt oder aktualisiert.

Anschließend stellt das Braze-Onboarding-Team sicher, dass Ihre Short- und Langcodes (in den USA und Kanada) für MMS aktiviert sind. Außerdem werden Ihre Abo-Gruppen aktualisiert, um Ihre aktuellen Nummern anzuzeigen, die für MMS hinzugefügt oder aktiviert wurden. Nach Abschluss dieser Schritte können Sie MMS-Nachrichten sofort über unseren nativen SMS-Composer senden.

### Warum kann ich MMS in meinem Dashboard nicht finden, obwohl das Feature aktiviert ist? {#why-cant-i-find-mms-on-my-dashboard-even-though-the-feature-is-enabled}

MMS wird im Braze-Dashboard nur angezeigt, wenn eine Abo-Gruppe als „MMS-fähig“ gilt. Dies wird durch ein MMS-Tag bei der Auswahl der Abo-Gruppe im Composer einer SMS/MMS-Nachricht angezeigt. Das bedeutet, dass mindestens eine Nummer in der Abo-Gruppe in der Lage ist, eine MMS-Nachricht zu senden.

Darüber hinaus kann es in bestimmten Situationen erforderlich sein, dass Twilio die Aktivierung von Shortcodes, die ursprünglich nicht für MMS aktiviert waren, erneut genehmigt. Dieser Genehmigungsprozess kann Wochen dauern.

## RCS

### Warum wird meine RCS-Nachricht auf iOS-Geräten nicht korrekt dargestellt? {#why-doesnt-my-rcs-message-render-accurately-on-ios-devices}

RCS-Nachrichten können auf einem iOS-Gerät je nach Betriebssystem und Messaging-App unterschiedlich dargestellt werden. Auf iOS-Geräten können folgende Verhaltensweisen auftreten:

- Vorgeschlagene Aktionen aus verschiedenen RCS-Nachrichten im selben Konversationsthread können gruppiert und in der falschen Reihenfolge angezeigt werden.
- Rich-Card-Buttons und vorgeschlagene Aktionen, die sich außerhalb der Rich Card befinden, können auch nach dem Tippen auf einen Rich-Card-Button oder eine vorgeschlagene Aktion sichtbar bleiben.

{% alert note %}
Braze sendet den von Ihnen erstellten RCS-Payload, während der Messaging-Client steuert, wie vorgeschlagene Aktionen sortiert, gruppiert und ausgeblendet werden. Testen Sie RCS-Nachrichten – insbesondere solche, die Rich Cards mit vorgeschlagenen Aktionen oder vorgeschlagenen Antworten verwenden – unbedingt auf Android- und iOS-Geräten, bevor Sie sie senden.
{% endalert %}

### Kann ich vorab aufgezeichnete Sprachnachrichten mit RCS senden? {#can-i-send-pre-recorded-voicemails-with-rcs}

Ja, Sie können Mediennachrichten verwenden, um Audio-Dateien zu unterstützen.

### Warum stimmen REST-API-SMS-Opt-ins nicht mit **Total Opt-Ins** in der SMS/MMS/RCS-Performance überein? {#why-do-rest-api-sms-opt-ins-not-match-total-opt-ins-on-smsmmsrcs-performance}

**Total Opt-Ins** und **Total Opt-Outs** im Dashboard [SMS/MMS/RCS-Performance]({{site.baseurl}}/user_guide/analytics/dashboards) zählen Abo-Änderungen, die durch eingehende SMS-Keyword-Verarbeitung ausgelöst werden (z. B. wenn ein:e Nutzer:in ein Opt-in-Keyword an Ihren Shortcode sendet). Sie umfassen nicht jedes Abo-Update, das über die REST API, das Dashboard oder andere Quellen vorgenommen wird.

Um Opt-ins und Opt-outs nach Quelle zu analysieren, verwenden Sie den [Abfrage-Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) auf `USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED` und filtern Sie nach `STATE_CHANGE_SOURCE` (z. B. **Rest API** versus **Inbound Message**).