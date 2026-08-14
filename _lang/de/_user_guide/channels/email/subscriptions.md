---
nav_title: "Abos"
article_title: "Abos"
page_order: 5
description: "Dieser Referenzartikel behandelt die verschiedenen Abo-Status von Nutzer:innen, wie Sie Abo-Gruppen erstellen und verwalten und wie Sie Nutzer:innen basierend auf ihren Abos segmentieren."
channel:
  - email

---

# E-Mail-Abos {#email-subscriptions}

> Erfahren Sie mehr über Abo-Status von Nutzer:innen, wie Sie Abo-Gruppen erstellen und verwalten und wie Sie Nutzer:innen basierend auf ihren Abos segmentieren.

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

Abo-Gruppen sind Segment-Filter, mit denen Sie Ihre Zielgruppe über die [globalen Abo-Status](#subscription-states) hinaus weiter eingrenzen können. Diese Gruppen ermöglichen es Ihnen, Endnutzer:innen detailliertere Abo-Optionen anzubieten.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

Angenommen, Sie versenden mehrere Kategorien von E-Mail-Campaigns (Werbe-E-Mails, Newsletter oder Produktupdates). In diesem Fall können Sie Abo-Gruppen verwenden, damit Ihre Kund:innen auf einer einzigen Seite über ein [E-Mail-Einstellungscenter](#email-preference-center) auswählen können, welche E-Mail-Kategorien sie abonnieren oder abbestellen möchten. Alternativ könnten Sie Abo-Gruppen nutzen, um Ihren Kund:innen die Wahl zu lassen, wie häufig sie E-Mails von Ihnen erhalten möchten, indem Sie Abo-Gruppen für tägliche, wöchentliche oder monatliche E-Mails erstellen.

Verwenden Sie die [Abo-Gruppen-Endpunkte]({{site.baseurl}}/api/endpoints/subscription_groups), um die Abo-Gruppen, die Sie im Braze-Dashboard auf der Seite **Abo-Gruppe** gespeichert haben, programmatisch zu verwalten.

### Abo-Gruppe erstellen {#creating-a-subscription-group}

1. Gehen Sie zu **Zielgruppe** > **Abo-Gruppenverwaltung**.
2. Wählen Sie **E-Mail-Abo-Gruppe erstellen** aus.
3. Geben Sie Ihrer Abo-Gruppe einen Namen und eine Beschreibung.
4. Wählen Sie **Speichern** aus.

Alle Abo-Gruppen werden automatisch zu Ihrem Einstellungscenter hinzugefügt.

![Felder zum Erstellen einer Abo-Gruppe.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### Segmentierung mit einer Abo-Gruppe {#segmenting-with-a-subscription-group}

Legen Sie beim Erstellen Ihrer Segmente den Namen der Abo-Gruppe als Filter fest, um Nutzer:innen anzusprechen, die sich für Ihre Gruppe angemeldet haben. Dies ist nützlich für monatliche Newsletter, Gutscheine, Mitgliedschaftsstufen und mehr.

![Beispiel für das Targeting von Nutzer:innen im Segment „Inaktive Nutzer:innen“ mit dem Filter für Nutzer:innen in der Abo-Gruppe „Wöchentliche E-Mails“.]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### Abo-Gruppen archivieren {#archiving-subscription-groups}

Archivierte Abo-Gruppen können nicht bearbeitet werden und erscheinen nicht mehr in Segment-Filtern oder in Ihrem Einstellungscenter. Wenn Sie versuchen, eine Gruppe zu archivieren, die als Segment-Filter in einer E-Mail, Campaign oder einem Canvas verwendet wird, erhalten Sie eine Fehlermeldung, die Sie daran hindert, die Gruppe zu archivieren, bis Sie alle Verwendungen entfernt haben.

Um Ihre Gruppe auf der Seite **Abo-Gruppen** zu archivieren, gehen Sie wie folgt vor:

1. Suchen Sie Ihre Gruppe in der Liste der Abo-Gruppen.
2. Wählen Sie **Archivieren** aus dem <i class="fa-solid fa-ellipsis-vertical" aria-label="Weitere Optionen"></i>&nbsp;Dropdown-Menü aus.

Braze verarbeitet keine Statusänderungen für Nutzer:innen in archivierten Gruppen. Wenn Sie beispielsweise Abo-Gruppe 1 archivieren, während Alex diese abonniert hat, bleibt Alex „abonniert“, auch wenn Alex auf einen Abmeldelink klickt. Das spielt keine Rolle, da Abo-Gruppe 1 archiviert ist und Sie keine Nachrichten darüber versenden können.

#### Größen von Abo-Gruppen anzeigen {#viewing-subscription-group-sizes}

Sie können das Diagramm **Abo-Gruppen-Zeitreihe** auf der Seite **Abo-Gruppen** verwenden, um die Größe der Abo-Gruppe basierend auf der Anzahl der Nutzer:innen über einen Zeitraum hinweg anzuzeigen. Diese Abo-Gruppengrößen stimmen auch mit anderen Bereichen von Braze überein, wie z. B. der Berechnung der Segmentgröße.

![Ein Beispiel für ein Diagramm „Abo-Gruppen-Zeitreihe“ vom 2. bis 11. Dezember. Das Diagramm zeigt einen Anstieg von ca. 10 Millionen Nutzer:innen vom 6. zum 7.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

#### Warum sich Abo-Gruppenanzahlen von Segmentanzahlen unterscheiden können {#why-subscription-group-counts-can-differ-from-segment-counts}

Abo-Gruppengrößen stimmen mit Segmenten überein, die nur den Filter **Abo-Gruppe** verwenden. Sie können von einem Segment abweichen, das **E-Mail-Abo-Status** verwendet, da dieser den [globalen E-Mail-Abo-Status](#subscription-states) widerspiegelt und nicht die Mitgliedschaft in einer bestimmten Gruppe, oder das mehrere Filter kombiniert. Beispielsweise kann eine Nutzer:in global für E-Mails abonniert sein, aber von einer bestimmten Abo-Gruppe abgemeldet.

Um den globalen Abo-Status einer Nutzer:in mit ihren Abo-Gruppenmitgliedschaften zu vergleichen, gehen Sie zu ihrem Profil und wählen Sie den Tab **Engagement** aus. Informationen zur Filterung nach globalem Status finden Sie unter [Segmentierung nach Nutzer:innen-Abos](#segmenting-by-user-subscriptions).

#### Abo-Gruppen in der Campaign-Analyse anzeigen {#viewing-subscription-groups-in-campaign-analytics}

Sie können die Anzahl der Nutzer:innen sehen, die ihren Abo-Status (abonniert oder abgemeldet) über eine bestimmte E-Mail-Campaign geändert haben, auf der Analytics-Seite dieser Campaign.

1. Scrollen Sie auf der Seite **Campaign Analytics** Ihrer Campaign nach unten zum Abschnitt **E-Mail-Nachrichten-Performance**.
2. Wählen Sie den Pfeil unter **Abo-Gruppen** aus, um die aggregierte Anzahl der Statusänderungen zu sehen, die von Ihren Kund:innen übermittelt wurden.

![Die Seite „E-Mail-Nachrichten-Performance“ mit der aggregierten Anzahl der von Kund:innen übermittelten Statusänderungen.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

### E-Mail-Abo-Gruppe einer Nutzer:in überprüfen {#checking-a-users-email-subscription-group}

- **Nutzerprofil:** Auf einzelne Nutzerprofile kann über das Braze-Dashboard auf der Seite [Nutzer:innen suchen]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles) zugegriffen werden. Dort können Sie Nutzerprofile nach E-Mail-Adresse, Telefonnummer oder externer Nutzer-ID suchen. Sie können die E-Mail-Abo-Gruppen einer Nutzer:in auch im Tab **Engagement** einsehen.
- **Braze REST API:** Verwenden Sie den [Endpunkt „Abo-Gruppen einer Nutzer:in auflisten“]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) oder den [Endpunkt „Abo-Gruppenstatus einer Nutzer:in auflisten“]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status), um die Abo-Gruppen einzelner Nutzerprofile anzuzeigen.

## E-Mail-Einstellungscenter {#email-preference-center}

Das E-Mail-Einstellungscenter ermöglicht es Ihnen zu verwalten, welche Nutzer:innen Newsletter von Abo-Gruppen erhalten. Sie finden es im Dashboard unter **Abo-Gruppen**. Jede von Ihnen erstellte Abo-Gruppe wird der Liste im Einstellungscenter hinzugefügt.

Weitere Informationen zum Hinzufügen oder Anpassen eines Einstellungscenters finden Sie unter [Einstellungscenter]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

## E-Mail-Abos ändern {#changing-email-subscriptions}

In den meisten Fällen verwalten Nutzer:innen ihr E-Mail-Abo über Links in den E-Mails, die sie erhalten. Fügen Sie am Ende jeder E-Mail eine rechtskonforme Fußzeile mit einem Abmeldelink ein. Wenn Nutzer:innen die Abmelde-URL auswählen, meldet Braze sie ab und zeigt eine Landing-Page an, die die Änderung bestätigt. Verwenden Sie diesen Liquid-Tag: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

{% alert note %}
Sie können den Liquid-Tag {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%} nur in E-Mail-Campaigns und Canvases verwenden. In anderen Messaging-Kanälen können Sie diesen Tag nicht nutzen.
{% endalert %}

Wenn eine Nutzer:in im Präferenzzentrum „Von allen aufgelisteten E-Mail-Typen abmelden“ auswählt, setzt Braze ihren globalen E-Mail-Abo-Status auf `unsubscribed` und meldet sie von allen Gruppen ab.

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
Verwenden Sie einen Double-Opt-in-Prozess, um Ihre Reichweite zu verbessern. Braze sendet eine zusätzliche Bestätigungs-E-Mail, in der eine Nutzer:in ihre Benachrichtigungspräferenzen über einen Link bestätigt. Nach der Bestätigung ist die Nutzer:in opted-in.
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