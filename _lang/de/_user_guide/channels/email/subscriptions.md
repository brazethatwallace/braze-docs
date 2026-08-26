---
nav_title: "Abos"
article_title: "Abos"
page_order: 5
description: "Dieser Referenzartikel behandelt die verschiedenen Abo-Status von Nutzer:innen, wie Sie E-Mail-Abos verwalten und wie Sie Nutzer:innen basierend auf ihren Abos segmentieren."
channel:
  - email

---

# E-Mail-Abos {#email-subscriptions}

> Erfahren Sie mehr über globale E-Mail-Abo-Status, Fußzeilen und Abmeldeseiten, Präferenzzentren und Campaign-Targeting. Informationen zu Abo-Gruppen über alle Kanäle hinweg finden Sie unter [Abo-Gruppen]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

Dieses Dokument dient ausschließlich zu Informationszwecken. Es ist nicht als Rechtsberatung gedacht und darf auch nicht als solche herangezogen werden. Der Versand von Marketing- und Transaktions-E-Mails kann bestimmten gesetzlichen Anforderungen unterliegen. Um sicherzustellen, dass Sie alle geltenden Gesetze, Vorschriften und Regelungen einhalten, die für Ihr Unternehmen gelten, sollten Sie den Rat Ihrer Rechtsabteilung und/oder Ihres Compliance-Teams einholen.

## Abo-Status {#subscription-states}

Braze verwendet globale Abo-Status, um zu steuern, welche Nutzer:innen E-Mails erhalten. Definitionen von `opted-in`, `subscribed` und `unsubscribed`, wie sich der globale Status von Abo-Gruppen unterscheidet und wie der Abo-Status auf anderen Kanälen funktioniert, finden Sie unter [Abo-Status]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#email).

### Abgemeldete E-Mail-Adressen {#unsubscribed-email-addresses}

Braze meldet automatisch jede Nutzer:in ab, die sich manuell über eine [angepasste Fußzeile]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer) abmeldet. Wenn die Nutzer:in ihre E-Mail-Adresse aktualisiert und **Resubscribe users when they update their email** in der **Sendekonfiguration** aktiviert ist, wird der normale Versand fortgesetzt.

Wenn eine Nutzer:in eine oder mehrere Ihrer E-Mails als Spam markiert, sendet Braze nur noch Transaktions-E-Mails an diese Nutzer:in. Transaktions-E-Mails beziehen sich auf die Option **Send to all users including unsubscribed users** unter **Target Audience**.

{% alert tip %}
Lesen Sie unsere Best Practices zum [IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming), um Hinweise zur effektiven Reaktivierung Ihrer Nutzer:innen zu erhalten.
{% endalert %}

### Bounces und ungültige E-Mails {#bounces-and-invalid-emails}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}

Wenn eine E-Mail-Adresse einen Hard Bounce verursacht, setzt Braze den Abo-Status der Nutzer:in nicht automatisch auf „Abgemeldet“. Wenn eine Adresse einen Hard Bounce verursacht (ungültig oder nicht vorhanden), markiert Braze sie als ungültig und unternimmt keine weiteren Zustellversuche. Wenn die Nutzer:in ihre E-Mail-Adresse ändert, nimmt Braze den Versand wieder auf. Braze versucht Soft Bounces 72 Stunden lang erneut zuzustellen.

### E-Mail-Abo-Status aktualisieren {#updating-email-subscription-states}

Es gibt vier Möglichkeiten, den E-Mail-Abo-Status einer Nutzer:in zu aktualisieren:

#### SDK-Integration {#sdk-integration}

Verwenden Sie das Braze SDK, um den Abo-Status einer Nutzer:in zu aktualisieren.

#### REST API

Verwenden Sie den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track), um das [`email_subscribe`-Attribut]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) für eine Nutzer:in zu aktualisieren. Um beispielsweise den E-Mail-Abo-Status einer Nutzer:in auf „Abgemeldet“ zu setzen, wenn sie einen angepassten Abmeldelink verwendet, fügen Sie `email_subscribe: "unsubscribed"` in den Nutzerattributen Ihrer Anfrage ein.

#### Nutzerprofil {#user-profile}

1. Suchen Sie die Nutzer:in über **Nutzer:innen suchen**.
2. Wählen Sie unter **Engagement** die Option **Unsubscribed**, **Subscribed** oder **Opted In**, um den Abo-Status der Nutzer:in zu ändern.

Das Nutzerprofil zeigt auch einen Zeitstempel an, wann das Abo der Nutzer:in zuletzt geändert wurde. Ein Zeitstempel wird aufgezeichnet, wenn der Status **Opted-in** oder **Unsubscribed** ist, aber nicht, wenn der Status **Subscribed** ist – beispielsweise hat ein neu erstelltes Profil, das sich nie explizit an- oder abgemeldet hat, keinen Abo-Zeitstempel.

#### Präferenzzentrum {#preference-center}

Fügen Sie [Präferenzzentrum](#email-preference-center)-Liquid am Ende Ihrer E-Mails ein, damit Nutzer:innen sich an- oder abmelden können. Braze verwaltet die Aktualisierungen des Abo-Status über das Präferenzzentrum.

### E-Mail-Abo-Status überprüfen {#checking-email-subscription-state}

![Nutzerprofil für John Doe mit dem E-Mail-Abo-Status „Abonniert“.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Sie können den E-Mail-Abo-Status einer Nutzer:in auf folgende Weise überprüfen:

1. **REST-API-Export:** Verwenden Sie die Endpunkte [Nutzer:innen nach Segment exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) oder [Nutzer:innen nach Bezeichner exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier), um einzelne Nutzerprofile im JSON-Format zu exportieren.
2. **Nutzerprofil:** Suchen Sie das Profil der Nutzer:in auf der Seite [Nutzer:innen suchen]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles), wählen Sie dann den Tab **Engagement**, um den Abo-Status der Nutzer:in einzusehen und manuell zu aktualisieren.

Wenn eine Nutzer:in ihre E-Mail-Adresse aktualisiert, wird ihr Abo-Status auf „Abonniert“ gesetzt. Wenn die aktualisierte E-Mail-Adresse bereits an anderer Stelle in einem Braze-Workspace existiert, übernimmt die Nutzer:in den Abo-Status von dieser bestehenden Nutzer:in, es sei denn, **Resubscribe users when they update their email setting** ist in der **Sendekonfiguration** aktiviert.

Um Änderungen des Abo-Status nachzuvollziehen, überprüfen Sie die **Email Subscription-State Changes** in den Nutzerprofil-Protokollen, um den Verlauf und die Quelle einzusehen. Die folgenden Quellen können eine Änderung des E-Mail-Abo-Status auslösen:

| Quelle | Beschreibung |
| ------ | ----------- |
| SDK | Nutzerattribut-Update, gesendet über ein Braze SDK |
| REST API | Nutzerattribut-Update, gesendet über den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-Endpunkt |
| Dashboard | Abo-Status manuell auf der Nutzerprofil-Seite geändert |
| CSV-Import | Abo-Status während eines Nutzer-CSV-Imports festgelegt |
| Präferenzzentrum | Nutzer:in hat ihre Präferenz über ein von Braze gehostetes Präferenzzentrum aktualisiert |
| Abo-Seite | Nutzer:in hat einen Abmeldelink in einer E-Mail ausgewählt und ist auf der Braze-Abo-Seite gelandet |
| List-Unsubscribe | Nutzer:in hat sich über den nativen List-Unsubscribe-Header des E-Mail-Clients abgemeldet |
| Canvas-Nutzeraktualisierungsschritt | Abo-Status durch einen [Nutzeraktualisierungsschritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update) in einem Canvas aktualisiert |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Quellen für Aktualisierungen des E-Mail-Abo-Status" }

Wenn sich der globale E-Mail-Abo-Status einer Nutzer:in ändert, überträgt Braze diesen Status auf andere Profile, die dieselbe E-Mail-Adresse verwenden – bis zu 100 Profile pro Änderung. Braze garantiert keine Übertragung, wenn mehr als 100 Profile dieselbe E-Mail-Adresse verwenden. Wenn Nutzer:innen, die eine E-Mail-Adresse teilen, unterschiedliche Abo-Status aufweisen, wenden Sie sich an den Braze-Support.

## Abo-Gruppen {#subscription-groups}

E-Mail-Abo-Gruppen ermöglichen es Nutzer:innen, sich für bestimmte E-Mail-Kategorien (z. B. Newsletter oder Aktionen) an- oder abzumelden, ohne ihren globalen E-Mail-Abo-Status zu ändern. Von Ihnen erstellte Gruppen können Sie Ihrem [Präferenzcenter]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center) hinzufügen.

Weitere Informationen zum Erstellen von Gruppen, Segmentierung, Archivierung und kanalspezifischem Verhalten finden Sie unter [Abo-Gruppen]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups).

## E-Mail-Einstellungscenter {#email-preference-center}

Das E-Mail-Einstellungscenter ermöglicht es Ihnen zu verwalten, welche Nutzer:innen Newsletter von Abo-Gruppen erhalten. Sie finden es im Dashboard unter **Abo-Gruppen**. Jede von Ihnen erstellte Abo-Gruppe wird der Liste im Einstellungscenter hinzugefügt.

Weitere Informationen zum Hinzufügen oder Anpassen eines Einstellungscenters finden Sie unter [Einstellungscenter]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

## E-Mail-Abos ändern {#changing-email-subscriptions}

In den meisten Fällen verwalten Nutzer:innen ihr E-Mail-Abo über Links in den E-Mails, die sie erhalten. Fügen Sie am Ende jeder E-Mail eine rechtskonforme Fußzeile mit einem Abmeldelink ein. Wenn Nutzer:innen die Abmelde-URL auswählen, meldet Braze sie ab und zeigt eine Landing-Page an, die die Änderung bestätigt. Verwenden Sie diesen Liquid-Tag: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

{% alert note %}
Sie können den Liquid-Tag {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%} nur in E-Mail-Campaigns und Canvases verwenden. In anderen Messaging-Kanälen können Sie diesen Tag nicht nutzen.
{% endalert %}

Wenn eine Nutzer:in im Präferenzzentrum „Von allen aufgelisteten E-Mail-Typen abmelden“ auswählt, setzt Braze ihren globalen E-Mail-Abo-Status auf `unsubscribed` und meldet sie von allen Gruppen ab.

Empfängerseitige E-Mail-Abmeldungen – Abmeldelinks, List-Unsubscribe, Einreichungen über das Präferenzzentrum und ESP-gemeldete Abmeldungen – erscheinen in der Snowflake-Tabelle `USERS_MESSAGES_EMAIL_UNSUBSCRIBE`. Abmeldungen über die REST API sind in dieser Tabelle nicht enthalten; stattdessen erzeugen sie [`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events)- oder [`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events)-Ereignisse. Das Tabellenschema finden Sie unter [USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED).

### Angepasste Fußzeilen erstellen {#custom-footer}

Wenn Sie nicht die Standard-Fußzeile verwenden möchten, erstellen Sie eine Workspace-weite angepasste E-Mail-Fußzeile und binden Sie diese mit {% raw %}`{{${email_footer}}}`{% endraw %} in jede E-Mail ein.

So müssen Sie nicht für jedes E-Mail-Template oder jede E-Mail-Campaign eine neue Fußzeile erstellen. Die Schritte finden Sie unter [Angepasste E-Mail-Fußzeile]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer).

#### Abo-Status für chinesische IP-Adressen verwalten {#managing-subscription-states-for-chinese-ip-addresses}

Wenn Sie mit chinesischen IP-Adressen rechnen, verlassen Sie sich nicht ausschließlich auf einen Abmeldelink, um `unsubscribed`-Listen zu pflegen. Bieten Sie alternative Abmeldewege an, wie z. B. ein Support-Ticket oder eine E-Mail-Adresse einer Vertretung.

### Angepasste Abmeldeseite erstellen {#creating-a-custom-unsubscribe-page}

Wenn Nutzer:innen eine Abmelde-URL in einer E-Mail auswählen, öffnen sie eine Standard-Landing-Page, die die Abo-Änderung bestätigt.

Um stattdessen eine angepasste Landing-Page zu verwenden:

1. Gehen Sie zu **E-Mail-Präferenzen** > **Abo-Seiten und -Fußzeilen**.
2. Fügen Sie den HTML-Code für Ihre angepasste Seite hinzu.

Fügen Sie einen Link zur erneuten Anmeldung ein (z. B. {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}), damit Nutzer:innen eine versehentliche Abmeldung rückgängig machen können. Wie bei {% raw %}`${set_user_to_unsubscribed_url}`{% endraw %} können Sie diesen Tag nur in E-Mail-Campaigns und Canvases verwenden.

Sie können Nutzer:innen auch auf Ihre Website weiterleiten und den Status über die Braze REST API aktualisieren (z. B. mit einem Link mit {% raw %}`?user_id={{${user_id}}}`{% endraw %} und anschließendem Aufruf von [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status)).

{% alert note %}
Wenn Sie die Dashboard-Fußzeile anstelle eines reinen HTML-Content-Blocks verwenden, muss das Template dennoch {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} enthalten, um gespeichert werden zu können. Um vorübergehend eine andere Abmelde-URL zu verwenden, können Sie den Standard-Tag auskommentieren. Ein Beispiel: {% raw %}`<!-- {{${set_user_to_unsubscribed_url}}} -->`{% endraw %}.
{% endalert %}

![Angepasste Abmeldeseite mit der Vorschau „Sorry to see you go!“.]({% image_buster /assets/img/custom_unsubscribe.png %})

### Angepasste Opt-in-Seite erstellen {#creating-a-custom-opt-in-page}

Verwenden Sie eine angepasste Opt-in-Seite, damit Nutzer:innen ihre Benachrichtigungspräferenzen vor dem Abo bestätigen und steuern können. Diese zusätzliche Kommunikation kann dazu beitragen, dass E-Mail-Campaigns nicht in Spam-Ordnern landen.

1. Gehen Sie zu **Einstellungen** > **E-Mail-Präferenzen**.
2. Wählen Sie **Abo-Seiten und -Fußzeilen**.
3. Passen Sie das Styling im Abschnitt **Angepasste Opt-in-Seite** an, um zu sehen, wie Ihren Nutzer:innen angezeigt wird, dass sie abonniert wurden.

Nutzer:innen erreichen diese Seite über den Tag {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}. Wie bei anderen E-Mail-Abo-Liquid-Tags können Sie diesen Tag nur in E-Mail-Campaigns und Canvases verwenden.

{% alert tip %}
Verwenden Sie einen Double-Opt-in-Prozess, um Ihre Reichweite zu verbessern. Braze sendet eine zusätzliche Bestätigungs-E-Mail, in der Nutzer:innen ihre Benachrichtigungspräferenzen über einen Link bestätigen. Nach der Bestätigung sind die Nutzer:innen opted-in.
{% endalert %}

![Angepasste Opt-in-E-Mail mit der Nachricht „Glad to see you still want to hear from us“.]({% image_buster /assets/img/custom_optin.png %})

## Abos und Campaign-Targeting {#subscriptions-and-campaign-targeting}

Standardmäßig richtet Braze Campaigns mit Push- oder E-Mail-Nachrichten an Nutzer:innen, die abonniert oder opted-in sind. Ändern Sie dies unter **Target Audience**, indem Sie das Dropdown neben **Send to these users:** auswählen.

Braze unterstützt drei Targeting-Status:

- Nutzer:innen, die abonniert oder opted-in sind (Standard).
- Nur Nutzer:innen, die opted-in sind.
- Alle Nutzer:innen, einschließlich derjenigen, die sich abgemeldet haben.

{% alert important %}
Es liegt in Ihrer Verantwortung, bei der Verwendung dieser Targeting-Einstellungen alle geltenden [Spam-Gesetze]({{site.baseurl}}/help/best_practices/spam_regulations#spam-regulations) einzuhalten.
{% endalert %}

## Nach Nutzer-Abos segmentieren {#segmenting-by-user-subscriptions}

Verwenden Sie die Filter „E-Mail-Abo-Status“ und „Push-Abo-Status“, um Nutzer:innen nach Abo-Status zu segmentieren.

Nutzen Sie dies, um Nutzer:innen anzusprechen, die sich weder an- noch abgemeldet haben, und ermutigen Sie sie zu einem expliziten Opt-in. Erstellen Sie ein Segment mit dem Filter „E-Mail-/Push-Abo-Status ist Abonniert“ und senden Sie Campaigns an Nutzer:innen, die abonniert, aber nicht opted-in sind.

![E-Mail-Abo-Status als Segment-Filter verwendet.]({% image_buster /assets/img_archive/not_optin.png %})