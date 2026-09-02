---
nav_title: Abo-Gruppen
article_title: Abo-Gruppen
page_order: 4
description: "Erfahren Sie, wie Abo-Gruppen kanalübergreifend in Braze funktionieren, wie Sie sie erstellen und verwalten, und welches kanalspezifische Verhalten für E-Mail, WhatsApp, SMS, MMS, RCS und LINE gilt."
---

# Abo-Gruppen {#subscription-groups}

> Erfahren Sie, wie Abo-Gruppen kanalübergreifend in Braze funktionieren, wie Sie sie im Dashboard erstellen und verwalten, und wo kanalspezifische Regeln gelten.

Abo-Gruppen steuern, welche Nutzer:innen Nachrichten von einer bestimmten Gruppe von Senderessourcen innerhalb eines Kanals empfangen können.

Für E-Mail sind Abo-Gruppen optionale Kategoriefilter zusätzlich zum globalen Abo-Status. Für SMS, WhatsApp und LINE sind Abo-Gruppen Zielgruppenfilter, die für jeden Versand erforderlich sind. Sie ermöglichen granulare Opt-in- und Opt-out-Optionen – etwa Newsletter versus Aktionen oder transaktionale versus Marketing-SMS – ohne den globalen Kanal-Abo-Status einer Nutzer:in zu ändern, sofern ein solcher existiert.

Verwenden Sie die [Endpunkte für Abo-Gruppen]({{site.baseurl}}/api/endpoints/subscription_groups), um Abo-Gruppen in Ihrem Braze-Workspace programmatisch zu verwalten.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## Globaler Abo-Status versus Abo-Gruppen {#global-subscription-state-versus-subscription-groups}

Einige Kanäle haben sowohl einen globalen Abo-Status als auch Abo-Gruppen:

| Kanal | Globaler Abo-Status | Abo-Gruppen |
| --- | --- | --- |
| E-Mail | Opted-in, abonniert oder abgemeldet für alle E-Mails | Optionale Kategorien (z. B. Newsletter oder Aktionen) innerhalb von E-Mail |
| SMS, MMS und RCS | Kein globaler SMS-Status; Abo erfolgt pro Gruppe | Für jeden Versand erforderlich; jede Gruppe enthält Sendetelefonnummern oder RCS-Absender |
| WhatsApp | Kein globaler WhatsApp-Status; Abo erfolgt pro Gruppe | Wird bei der WhatsApp-Integration erstellt; jede Gruppe ist einer Sendetelefonnummer zugeordnet |
| LINE | Kein globaler LINE-Status; Abo erfolgt pro Gruppe | Wird pro LINE-Kanal-Integration erstellt; Folgen oder Entfolgen in der LINE-App bestimmt den Status |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Globaler Abo-Status versus Abo-Gruppen" }

Eine Nutzer:in kann global für E-Mail abonniert sein, während sie sich von einer bestimmten E-Mail-Abo-Gruppe abgemeldet hat. Bei SMS kann eine Nutzer:in gleichzeitig bei einer transaktionalen Gruppe abonniert und bei einer werblichen Gruppe abgemeldet sein.

## Eine Abo-Gruppe erstellen {#create-a-subscription-group}

Wie Sie eine Abo-Gruppe erhalten, hängt vom Kanal ab. E-Mail-Gruppen werden im Dashboard erstellt; SMS-, MMS- und RCS-Gruppen werden beim Onboarding bereitgestellt; WhatsApp- und LINE-Gruppen werden während der Kanal-Integration erstellt. Kanalspezifische Details zur Bereitstellung finden Sie unter [Kanalspezifisches Verhalten](#channel-specific-behavior).

### E-Mail {#email}

1. Navigieren Sie zu **Zielgruppe** > **Abo-Gruppen-Verwaltung**.
2. Wählen Sie **E-Mail-Abo-Gruppe erstellen**.
3. Geben Sie einen Namen und eine Beschreibung ein. Jede Abo-Gruppe in Ihrem Workspace muss einen eindeutigen Namen haben. Wenn Sie einen bereits vorhandenen Namen eingeben, zeigt das Dashboard einen Fehler an und speichert die Gruppe nicht.
4. Wählen Sie **Speichern**.

![Felder zum Erstellen einer Abo-Gruppe.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

## Segmentierung mit Abo-Gruppen {#segment-with-subscription-groups}

Wenn Sie ein Segment erstellen, fügen Sie einen Abo-Gruppen-Filter hinzu, um Nutzer:innen anzusprechen, die sich für diese Gruppe angemeldet haben. Dies ist nützlich für monatliche Newsletter, Coupon-Programme, Mitgliedschaftsstufen und andere kategoriebasierte Versendungen.

![Beispiel für das Targeting von Nutzer:innen im Segment „Inaktive Nutzer:innen“ mit dem Filter für Nutzer:innen in der Abo-Gruppe „Wöchentliche E-Mails“.]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

## Abo-Gruppen archivieren {#archive-subscription-groups}

Archivierte Abo-Gruppen können nicht bearbeitet werden und erscheinen nicht mehr in Segment-Filtern oder Präferenzzentren. Wenn Sie eine Gruppe archivieren, die als Segment-Filter in einer aktiven Campaign, einem Canvas oder einem Segment verwendet wird, erhalten Sie einen Fehler, bis Sie diese Referenzen entfernen.

Um eine Gruppe über die **Abo-Gruppen-Verwaltung** zu archivieren, suchen Sie die Gruppe und wählen Sie **Archivieren** aus dem <i class="fa-solid fa-ellipsis-vertical" aria-label="Mehr Optionen"></i>-Menü.

Braze blockiert Nachrichten an archivierte Gruppen, sodass Sie eine archivierte Abo-Gruppe nicht in neuen oder aktiven Versendungen verwenden können.

Einige Kanäle haben zusätzliche Archivierungsregeln. Informationen zum Workspace- und Re-Integrationsverhalten finden Sie unter [LINE-Abo-Gruppen](#line-subscription-groups).

## Abo-Gruppen einer Nutzer:in prüfen {#check-a-users-subscription-groups}

- **Kundenprofil:** Öffnen Sie ein Profil über [Nutzersuche]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles). Auf dem Tab **Engagement** können Sie Abo-Gruppen und den Status für E-Mail, SMS, WhatsApp und verwandte Kanäle einsehen.
- **REST API:** Verwenden Sie die Endpunkte [Abo-Gruppen einer Nutzer:in auflisten]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) oder [Abo-Gruppenstatus einer Nutzer:in auflisten]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status).

### Abo-Gruppenstatus aktualisieren {#update-subscription-group-status}

Sie können die Abo-Gruppen-Mitgliedschaft einer Nutzer:in über die REST API, das SDK, Nutzerimport, das Kundenprofil, das E-Mail-Präferenzzentrum, den User-Update-Schritt in einem Canvas und andere kanalspezifische Abläufe aktualisieren. Die verfügbaren Methoden hängen vom Kanal ab – siehe jeden [Kanalabschnitt](#channel-specific-behavior) und [SMS-, MMS- und RCS-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#set-a-users-state) für SMS-spezifische Hinweise zum Timing.

## Präferenzzentren {#preference-centers}

E-Mail-Abo-Gruppen können in einem [E-Mail-Präferenzzentrum]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center) angezeigt werden, damit Nutzer:innen ihre E-Mail-Opt-ins auf Kategorieebene an einem Ort verwalten können. Aktive E-Mail-Abo-Gruppen stehen zur Verfügung, wenn Sie ein Präferenzzentrum erstellen; ältere Präferenzzentren listen alle aktiven E-Mail-Gruppen automatisch auf.

Für SMS und WhatsApp verwalten Sie den Abo-Status über die REST API, Opt-in-Abläufe, Schlüsselwörter (SMS), das Kundenprofil und andere kanalspezifische Methoden in jedem [Kanalabschnitt](#channel-specific-behavior).

## Kanalspezifisches Verhalten {#channel-specific-behavior}

### E-Mail-Abo-Gruppen {#email-subscription-groups}

E-Mail-Abo-Gruppen bauen auf den [globalen E-Mail-Abo-Status]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) (Opted-in, abonniert und abgemeldet) auf. Nutzer:innen mit dem globalen Status `unsubscribed` erhalten keine E-Mails, unabhängig von der Abo-Gruppen-Mitgliedschaft.

E-Mail-spezifische Details:

- **Präferenzzentrum:** Jede E-Mail-Abo-Gruppe, die Sie erstellen, kann einem Präferenzzentrum hinzugefügt werden.
- **Campaign Analytics:** Auf der Seite **Email Message Performance** einer Campaign öffnen Sie **Subscription Groups**, um aggregierte An- und Abmeldezahlen für diesen Versand zu sehen.

#### Größe der Abo-Gruppen anzeigen {#viewing-subscription-group-sizes}

In der **Abo-Gruppen-Verwaltung** zeigen Zeitreihen-Charts:

- **Abo-Gruppen-Größe:** Nutzer:innen, die an einem bestimmten Datum bei dieser Gruppe abonniert sind
- **Abo-Gruppen-Größe Abgemeldet:** Nutzer:innen, die sich an einem bestimmten Datum von dieser Gruppe abgemeldet haben

Diese Zahlen spiegeln die Mitgliedschaft in dieser Gruppe wider, nicht den globalen E-Mail-Abo-Status. Sie können sich von einem Segment unterscheiden, das **E-Mail-Abo-Status ist Abgemeldet** verwendet, welcher den [globalen E-Mail-Abo-Status]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) widerspiegelt.

Die heutige Abo-Gruppen-Größe wird standardmäßig nicht berechnet. Wenn Ihr Datumsbereich den heutigen Tag umfasst, wählen Sie **Heutige Statistiken berechnen**, um den heutigen Wert zur Zeitreihe hinzuzufügen. Bei sehr großen Workspaces zeigt Braze möglicherweise geschätzte statt exakter Zahlen an.

Informationen zu Fußzeilen, Abmeldeseiten und globalem E-Mail-Abo-Management finden Sie unter [E-Mail-Abos]({{site.baseurl}}/user_guide/channels/email/subscriptions).

### WhatsApp-Abo-Gruppen {#whatsapp-subscription-groups}

WhatsApp-Abo-Gruppen werden erstellt, wenn Sie [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) über das Technology Partner Portal in Ihren Workspace integrieren.

| Status | Definition |
| --- | --- |
| Abonniert | Nutzer:in hat explizit bestätigt, dass sie WhatsApp-Nachrichten von Ihrem Unternehmen erhalten möchte. Nutzer:innen können über die Braze-Abo-API oder Ihren Opt-in-Ablauf abonniert werden. |
| Abgemeldet | Nutzer:in hat nicht zugestimmt oder wurde aus der Gruppe entfernt. Abgemeldete Nutzer:innen erhalten keine WhatsApp-Nachrichten von Telefonnummern in dieser Gruppe. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="WhatsApp-Abo-Status" }

WhatsApp erfordert ein explizites Opt-in. Opt-in-Schlüsselwörter werden auf diesem Kanal nicht unterstützt – Sie verwalten Einwilligung und Abo-Status selbst. Informationen zu Opt-in- und Opt-out-Abläufen finden Sie unter [WhatsApp-Opt-ins und -Opt-outs]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs).

Informationen zu Archivierungsschritten, Canvas-Aktualisierungen und REST-API-Beispielen finden Sie unter [WhatsApp-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).

### SMS-, MMS- und RCS-Abo-Gruppen {#sms-mms-and-rcs-subscription-groups}

SMS-, MMS- und RCS-Abo-Gruppen bilden die Grundlage für den Versand über diese Kanäle. Jede Gruppe ist eine Sammlung von [Sendeentitäten]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) – wie Shortcodes, Langcodes, alphanumerische Absender-IDs oder RCS-verifizierte Absender – für einen bestimmten Nachrichtenzweck (z. B. transaktional versus werblich).

| Status | Definition |
| --- | --- |
| Abonniert | Nutzer:in ist abonniert, um Nachrichten von dieser Abo-Gruppe zu erhalten – über die Abo-API, Opt-in-Schlüsselwörter oder andere unterstützte Abläufe. Mit aktiviertem [Double-Opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) müssen Nutzer:innen bestätigen, bevor der Status auf „abonniert“ aktualisiert wird. |
| Abgemeldet | Nutzer:in hat sich per Schlüsselwort oder API-Aktualisierung abgemeldet. Abgemeldete Nutzer:innen erhalten keine SMS, MMS oder RCS von Absendern in dieser Gruppe. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS- und RCS-Abo-Status" }

Wenn Sie eine SMS- oder RCS-Nachricht versenden, wählen Sie im Composer eine Abo-Gruppe aus. Braze fügt einen Zielgruppenfilter hinzu, sodass nur abonnierte Nutzer:innen angesprochen werden. Braze versendet keine SMS oder RCS an Nutzer:innen, die nicht bei der ausgewählten Gruppe abonniert sind. Um eine SMS-Testnachricht zu erhalten, muss die Empfänger:in der Abo-Gruppe angehören, die Sie für den Test auswählen. Weitere Details finden Sie unter [SMS-FAQs]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages).

Abo-Gruppen für SMS werden beim Onboarding bereitgestellt. Informationen zu MMS-Tags, RCS-Absender-Einrichtung, geografischen Berechtigungen, RCS-Migration und erweiterter Opt-out-Verarbeitung finden Sie unter [SMS-, MMS- und RCS-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups).

### LINE-Abo-Gruppen {#line-subscription-groups}

Jede LINE-Abo-Gruppe ist mit einer LINE-Kanal-Integration verbunden.

| Status | Definition |
| --- | --- |
| Abonniert | Nutzer:in ist dem LINE-Kanal in der LINE-App gefolgt. Nach der Integration abonniert Braze Nutzer:innen automatisch, wenn sie folgen. |
| Abgemeldet | Nutzer:in ist dem Kanal nicht gefolgt oder hat ihn entfolgt. Abgemeldete Nutzer:innen erhalten keine LINE-Nachrichten von dieser Gruppe. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE-Abo-Status" }

LINE ist die maßgebliche Quelle für den Abo-Status. Braze verarbeitet Follow- und Unfollow-Ereignisse, um Profile zu aktualisieren.

LINE-Abo-Gruppen können nicht zwischen Workspaces verschoben werden. Wenn Sie eine Gruppe archivieren und den Kanal in einem anderen Workspace erneut integrieren, erstellt Braze eine neue Abo-Gruppe im Ziel-Workspace.

Informationen zum Archivierungsverhalten, zur Nutzerabstimmung und zu Integrationsschritten finden Sie unter [LINE-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups) und [LINE-Einrichtung]({{site.baseurl}}/user_guide/channels/line/line_setup).