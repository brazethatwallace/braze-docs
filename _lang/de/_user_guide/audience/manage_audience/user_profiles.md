---
nav_title: Nutzerprofile
article_title: Nutzerprofile
page_order: 2
page_type: reference
tool:
  - Dashboard
description: "Dieser Referenzartikel beschreibt, wie Sie auf das Profil einer Nutzerin oder eines Nutzers im Dashboard zugreifen, Anwendungsfälle für Profile und was jedes Profil enthält."

---

# Nutzerprofile {#user-profiles}

> Nutzerprofile sind eine hervorragende Möglichkeit, Informationen über bestimmte Nutzer:innen zu finden. Alle persistenten Daten, die mit einer Nutzerin oder einem Nutzer verknüpft sind, werden in ihrem Nutzerprofil gespeichert.

## Auf Profile zugreifen {#access-profiles}

Um auf das Profil von Nutzer:innen zuzugreifen, gehen Sie zur Seite **Search Users** und suchen Sie nach Nutzer:innen anhand einer der folgenden Angaben:

- Externe Nutzer-ID
- Braze-ID
- E-Mail
- Telefonnummer
- Push-Token
- Nutzer-Alias im Format „[user_alias]:[alias_name]“, z. B. „amplitude_id:user_123“

Wenn eine Übereinstimmung gefunden wird, können Sie die Informationen einsehen, die Sie für diese:n Nutzer:in mit dem Braze SDK erfasst haben. Falls Ihre Suche mehrere Nutzerprofile zurückgibt, können Sie jedes Profil einzeln zusammenführen oder eine Massenzusammenführung durchführen. Eine vollständige Anleitung finden Sie unter [Doppelte Nutzer:innen zusammenführen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

{% alert note %}
**Search Users** ist nicht dasselbe wie **User Lookup** im Segment- oder Campaign-Composer. **User Lookup** prüft, ob bestimmte Nutzer:innen zu Ihrer Zielgruppe passen, und akzeptiert nur `external_id` oder `braze_id`. **Search Users** auf dieser Seite unterstützt E-Mail, Telefonnummer, Push-Token und Nutzer-Alias. Weitere Informationen finden Sie unter [Segments testen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).
{% endalert %}

{% alert important %}
Wenn eine Telefonnummer für die Suche verwendet wird, wird sie in das [`E.164`](https://en.wikipedia.org/wiki/e.164)-Format umgewandelt. Nutzer:innen, deren Telefonnummern nicht in das `E.164`-Format umgewandelt werden können (z. B. weil die Telefonnummer eine ungültige Landesvorwahl oder Ortsvorwahl hat), können nicht über die Telefonnummer gesucht werden.
{% endalert %}

![Suchergebnisse mit einem Banner „Multiple users match your search criteria“ und zwei Buttons „Previous“ und „Next“.]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## Anwendungsfälle {#use-cases}

Nutzerprofile sind eine hervorragende Ressource für die Fehlerbehebung und das Testen, da Sie leicht auf Informationen über den Engagement-Verlauf, die Segment-Zugehörigkeit, das Gerät und das Betriebssystem von Nutzer:innen zugreifen können.

Wenn beispielsweise Nutzer:innen ein Problem melden und Sie nicht sicher sind, welches Gerät und Betriebssystem sie verwenden, können Sie den [Tab „Übersicht“](#overview-tab) nutzen, um diese Informationen zu finden (sofern Sie deren E-Mail-Adresse oder Nutzer-ID haben). Sie können auch die Sprache von Nutzer:innen einsehen, was hilfreich sein kann, wenn Sie eine [mehrsprachige Campaign]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) untersuchen, die sich nicht wie erwartet verhalten hat.

Sie können den [Tab „Engagement“](#engagement-tab) verwenden, um zu überprüfen, ob bestimmte Nutzer:innen eine Campaign erhalten haben. Darüber hinaus können Sie, wenn diese Nutzer:innen die Campaign erhalten haben, sehen, wann sie sie erhalten haben. Sie können auch überprüfen, ob Nutzer:innen sich in einem bestimmten Segment befinden und ob sie für Push, E-Mail oder beides ein Opt-in erteilt haben. Diese Informationen sind für die Fehlerbehebung nützlich. Sie sollten diese Informationen beispielsweise prüfen, wenn Nutzer:innen eine Campaign nicht erhalten, die Sie erwartet hätten, oder eine Campaign erhalten, die Sie nicht erwartet hätten.

## Elemente des Nutzerprofils {#elements-of-user-profile}

Es gibt fünf Hauptbereiche im Profil von Nutzer:innen.

- **Übersicht:** Grundlegende Informationen über Nutzer:innen, Sitzungsdaten, angepasste Attribute, angepasste Events, Käufe und das letzte Gerät, auf dem sich die Person angemeldet hat.
- **Engagement:** Informationen über die Kontakteinstellungen von Nutzer:innen, empfangene Campaigns, Segments, Kommunikationsstatistiken, Install-Attribution und zufällige Bucket-Nummer.
- **Event-Verlauf:** Angepasste Events und Käufe der letzten 30 Tage, mit vollständigen Event-Eigenschaften als JSON.
- **Messaging-Verlauf:** Aktuelle Messaging-bezogene Ereignisse für diese:n Nutzer:in aus den letzten 30 Tagen.
- **Feature-Flag-Berechtigung:** Überprüfen Sie, für welche Feature-Flags Nutzer:innen derzeit über Rollouts, Canvas-Schritte und Experimente berechtigt sind.

{% tabs %}
{% tab Übersicht %}

### Übersicht {#overview-tab}

Der Tab **Übersicht** enthält grundlegende Informationen über Nutzer:innen und deren Interaktionen mit Ihrer App oder Website.

| Übersichtskategorie | Enthält |
| --- | --- |
| Profil | Geschlecht, Altersgruppe, Standort, Sprache, Gebietsschema, Zeitzone und Geburtstag. |
| Sitzungsübersicht | Wie viele Sitzungen stattfanden, wann die erste und letzte Sitzung war und in welchen Apps. |
| Angepasste Attribute | Welche angepassten Attribute dieser Person zugeordnet sind und deren zugehörige Werte, einschließlich verschachtelter angepasster Attribute. |
| Letzte Geräte | Auf wie vielen Geräten sich die Person angemeldet hat, Details zu jedem Gerät und die zugehörigen Werbe-IDs (falls vorhanden). |
| Angepasste Events | Welche angepassten Events diese:r Nutzer:in ausgeführt hat, wie oft und wann das jeweilige Event zuletzt ausgeführt wurde. |
| Käufe | Lifetime-Umsatz, der dieser Person zugeordnet ist, der letzte Kauf, die Gesamtzahl der Käufe und eine Liste jedes einzelnen Kaufs. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tab „Übersicht“" }

Weitere Informationen zu diesen Daten finden Sie unter [SDK-Datenerfassung]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection).

{% endtab %}
<a id="engagement-tab"></a>
{% tab Engagement %}

### Engagement {#engagement-tab}

Der Tab **Engagement** enthält Informationen über die Interaktionen von Nutzer:innen mit den Nachrichten, die Sie über Braze gesendet haben.

| Engagement-Kategorie | Enthält |
| --- | --- |
| Kontakteinstellungen | Abo-Status für E-Mail, SMS und Push sowie die Abo-Gruppen, denen diese:r Nutzer:in für diese drei Kanäle zugeordnet ist. Dieser Bereich enthält auch Changelog-Informationen für Push-Token. Weitere Informationen zur Einrichtung von Abos und Opt-ins finden Sie unter [E-Mail]({{site.baseurl}}/user_guide/channels/email/subscriptions), [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) und [Push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states). |
| Empfangene Campaigns | **Empfangene Campaigns** zeigt kanalspezifische Sende- und Anzeigezeitpunkte. Die meisten Kanäle protokollieren einen Versand, wenn Braze die Nachricht an den Zustellungsanbieter übergibt, auch wenn die Nachricht letztlich nicht zugestellt wird. **Content Cards** sind anders: Campaigns erscheinen hier erst, nachdem die Person die Karte in der App angesehen hat. Eine Aufschlüsselung nach Kanal finden Sie unter [Wann Campaigns unter „Empfangene Campaigns“ erscheinen](#when-campaigns-appear-in-campaigns-received). <br><br>Wenn eine Nachricht empfangen, geöffnet oder angeklickt wird, aktualisiert Braze die Daten für alle Profile, die denselben Kanalbezeichner wie das Profil teilen, das die Interaktion protokolliert hat (z. B. dieselbe E-Mail-Adresse für E-Mail oder dieselbe Telefonnummer für SMS oder WhatsApp). Nutzer:innen, die einen Bezeichner mit jemandem teilen, der die Nachricht empfangen, geöffnet oder angeklickt hat, können diesen Filter erfüllen, auch wenn sie ursprünglich nicht in der Campaign waren oder die Nachricht nicht direkt erhalten haben.<br><br>Diese Listen verwenden [Messaging-Interaktionsdaten]({{site.baseurl}}/api/data_retention/messaging_interaction_data) (einschließlich Ablaufregeln), um zu bestimmen, was für Retargeting und Verlauf angezeigt wird.<br><br> Wählen Sie eine Campaign aus der Liste aus, um sie anzuzeigen. |
| Segments | Segments, in denen diese:r Nutzer:in enthalten ist. Wählen Sie ein Segment aus der Liste aus, um es anzuzeigen. |
| Kommunikationsstatistiken | Wann diese:r Nutzer:in zuletzt Nachrichten von Ihnen über die einzelnen Kanäle erhalten hat. |
| Install-Attribution | Informationen darüber, wie und wann Nutzer:innen Ihre App installiert haben. Erfahren Sie mehr über das [Verstehen von Nutzerinstallationen]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/install_attribution). |
| Sonstiges | Die [zufällige Bucket-Nummer]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) der Person. |
| Empfangene Canvas-Nachrichten | Canvas-Nachrichten, die diese:r Nutzer:in erhalten hat, und wann. Die Sendezeitpunkte folgen denselben Kanalregeln wie **Empfangene Campaigns**; siehe [Wann Campaigns unter „Empfangene Campaigns“ erscheinen](#when-campaigns-appear-in-campaigns-received).<br><br> Wenn eine Nachricht empfangen, geöffnet oder angeklickt wird, aktualisiert Braze die Daten für alle Profile, die denselben Kanalbezeichner wie das Profil teilen, das die Interaktion protokolliert hat (z. B. dieselbe E-Mail-Adresse für E-Mail oder dieselbe Telefonnummer für SMS oder WhatsApp). Nutzer:innen, die einen Bezeichner mit jemandem teilen, der die Nachricht empfangen, geöffnet oder angeklickt hat, können diesen Filter erfüllen, auch wenn sie ursprünglich nicht in der Campaign waren oder die Nachricht nicht direkt erhalten haben.<br><br> Wählen Sie eine Nachricht aus der Liste aus, um sie anzuzeigen. |
| Prognosen | [Churn-Prognose]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) und [Event-Prognose]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events) für diese:n Nutzer:in. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tab „Engagement“" }

{% endtab %}
<a id="event-history-tab"></a>
{% tab Event-Verlauf %}

### Event-Verlauf {#event-history-tab}

{% alert note %}
Um den Tab **Event-Verlauf** anzuzeigen, benötigen Sie die [Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) **Search Users**, **View User Event Properties** und **View PII**, da Event-Eigenschaften personenbezogene Daten enthalten können.
{% endalert %}

Der Tab **Event-Verlauf** zeigt die angepassten Events und Käufe, die Nutzer:innen protokolliert haben. Verwenden Sie ihn, um zu überprüfen, ob Event-Daten korrekt eingehen, und um Probleme auf Nutzerebene direkt im Dashboard zu beheben – ohne Datenexporte oder externe Tools.

| Event-Verlauf-Kategorie | Enthält |
| --- | --- |
| Event-Liste | Angepasste Events und Käufe der letzten 30 Tage (bis zu 100 neueste), sortiert nach Aktualität. |
| Event-Typ | Ob die Zeile ein **angepasstes Event** oder ein **Kauf** ist. |
| Zeitstempel | Wann das Event protokolliert wurde. |
| Event-Name | Der Name des angepassten Events oder Kaufs. |
| Event-Eigenschaften | Vollständige Event-Eigenschaften für das Event, dargestellt als JSON. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tab „Event-Verlauf“" }

{% endtab %}
{% endtabs %}

### Wann Campaigns unter „Empfangene Campaigns“ erscheinen {#when-campaigns-appear-in-campaigns-received}

Im Allgemeinen listet Braze eine Campaign unter **Empfangene Campaigns** auf, nachdem versucht wurde, die Nachricht zu senden. Eine Zustellung an das Gerät oder den Posteingang der Person ist nicht erforderlich, damit ein Versand protokolliert wird. **Empfangene Canvas-Nachrichten** folgt denselben kanalspezifischen Regeln für jeden Canvas-Nachrichtentyp.

- **E-Mail:** Braze protokolliert einen Versand, wenn die Nachricht an Ihren E-Mail-Anbieter (ESP) übergeben wird. Nach dieser Übergabe wird die Nachricht nicht aufgrund von Liquid-Logik, Rate-Limiting oder weil die Person als nicht erreichbar markiert ist, abgebrochen. Die nächsten Ereignisse sind oft eine Zustellung oder ein Bounce.
- **Push:** Braze protokolliert einen Versand, wenn die Nachricht an den Push-Anbieter übergeben wird (z. B. Apple Push Notification service (APNs) oder Firebase Cloud Messaging (FCM)). Der Anbieter versucht in der Regel, sofort zuzustellen; wenn das Gerät nicht verfügbar ist (z. B. offline), kann der Anbieter es erneut versuchen, bis die Nachricht abläuft.
- **In-App Messages:** Braze protokolliert einen Versand, wenn die Campaign gestartet wird.
- **Content Cards:** Wann Braze ein _Gesendet_-Event aufzeichnet, hängt vom Zustellungstyp und Ihrer **Card Creation**-Einstellung ab. Eine Content-Card-Campaign erscheint unter **Empfangene Campaigns** im Nutzerprofil erst, nachdem die Person die Karte in der App angesehen hat. Die vollständige Aufschlüsselung finden Sie unter [Wann Versendungen protokolliert werden]({{site.baseurl}}/user_guide/channels/content_cards/reporting#when-sends-are-logged) und [Empfangene Campaigns und Retargeting-Filter]({{site.baseurl}}/user_guide/channels/content_cards/reporting#campaigns-received-and-retargeting-filters) im Artikel zum Content-Card-Reporting.
- **SMS, WhatsApp und Webhooks:** Braze protokolliert einen Versand, wenn die Nachricht den Zustellungspfad für den jeweiligen Kanal betritt (z. B. den SMS- oder WhatsApp-Anbieter oder Ihren Webhook-Endpunkt).

{% alert note %}
Diese Beschreibungen beziehen sich darauf, wann ein Versand für **Empfangene Campaigns** protokolliert wird. Sie sind getrennt von [Nachrichtenabbrüchen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages), die eine Nachricht stoppen können, bevor sie einen Anbieter erreicht.
{% endalert %}

![Der Tab „Engagement“ eines Nutzerprofils mit Kontakteinstellungen und Kommunikationsstatistiken.]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### Tab „Messaging-Verlauf“ {#messaging-history-tab}

Der Tab **Messaging-Verlauf** des Nutzerprofils zeigt aktuelle Messaging-bezogene Ereignisse (ca. 40) für einzelne Nutzer:innen aus den letzten 30 Tagen. Diese Ereignisse umfassen die Nachrichten, die der Person gesendet wurden, die sie empfangen und mit denen sie interagiert hat, und mehr.

Die Daten in diesem Tab werden nach einer Zusammenführung von Nutzer:innen nicht aktualisiert. Außerdem erscheinen Ereignisse, die mit über die API gesendeten Nachrichten verknüpft sind (z. B. der [Endpunkt /messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#creating-new-users-with-api-sends)), nicht in diesem Tab, wenn in diesen Sendungen keine Campaign-ID angegeben ist.

{% alert important %}
Im Tab **Messaging-Verlauf** sind RCS-Ereignisse bei den SMS-Ereignissen enthalten. RCS-Ereignisse werden nicht separat angezeigt.
{% endalert %}

![Der Tab „Messaging-Verlauf“ zeigt, welche Campaigns und Canvases Nutzer:innen empfangen haben.]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### Ereignisse anzeigen und verstehen {#viewing-and-understanding-events}

Für jedes Ereignis in der Tabelle **Messaging-Verlauf** können Sie den Messaging-Kanal, den Ereignistyp, den Zeitstempel des Ereignisses, die zugehörige Campaign oder Canvas-Nachricht und die Gerätedaten der Person sehen. Um nach bestimmten Ereignissen zu filtern, klicken Sie auf **Filter** und wählen Sie Ereignisse aus der Liste aus.

##### Nachrichten-Engagement-Ereignisse {#message-engagement-events}

Die folgenden Nachrichten-Engagement-Ereignisse sind für E-Mail, SMS, Push, In-App Messages, Content Cards und Webhooks verfügbar. Weitere Informationen darüber, wie bestimmte Ereignisse getrackt werden, finden Sie im [Glossar der Nachrichten-Engagement-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

| Kanal | Verfügbare Engagement-Ereignisse |
| --- | --- |
| E-Mail | Bounce<br>Klick<br>Verzögerungsereignisse<br>Zustellung<br>Als Spam markieren<br>Öffnung (siehe [Hinweis zum E-Mail-Öffnungsereignis](#note-on-email-open-event))<br>Versand<br>Soft Bounce<br>Abmeldung |
| SMS | Carrier-Versand<br>Zustellung<br>Zustellungsfehler<br>Eingehender Empfang<br>Ablehnung<br>Versand |
| Push | Bounce<br>Beeinflusste Öffnung<br>iOS Foreground<br>Öffnung<br>Versand |
| In-App-Nachricht | Klick<br>Impression |
| Content Cards | Klick<br>Verwerfen<br>Impression<br>Versand |
| Webhooks | Versand |
| WhatsApp | Abbruch<br>Zustellung<br>Fehler<br>Frequency-Capping<br>Eingehender Empfang<br>Gelesen<br>Versand |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nachrichten-Engagement-Ereignisse" }

##### Nachrichtenabbruch-Ereignisse {#message-abort-events}

Nachrichtenabbruch-Ereignisse treten auf, wenn eine an Nutzer:innen gesendete Nachricht aufgrund von bedingter Logik in [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) oder [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content) oder aufgrund von Liquid-Rendering-Timeouts abgebrochen wurde.

Abbruch-Ereignisse sind für die folgenden Kanäle verfügbar:

- E-Mail
- SMS
- Push
- Webhooks

Abbruch-Ereignisse sind derzeit nicht für In-App Messages und Content Cards verfügbar.

##### Frequency-Capping-Ereignisse {#frequency-cap-events}

Ein Frequency-Capping-Ereignis tritt auf, wenn Nutzer:innen für den Empfang einer Nachricht qualifiziert sind, diese aber aufgrund von [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)-Einstellungen nicht tatsächlich erhalten. Sie können die Frequency-Capping-Einstellungen unter **Einstellungen** > **Frequency-Capping-Regeln** anpassen.

##### Leere Ziele {#blank-destinations}

Einige Nachrichtenversendungen können im Messaging-Verlauf mit leeren Zielen erscheinen (gekennzeichnet durch „—“). Dies liegt daran, dass einige Kanäle, wie Content Cards und Webhooks, beim Nachrichtenversand keine Gerätedaten erfassen.

Content-Card-Versendungen werden protokolliert, wenn die Karte zur Ansicht verfügbar ist. Da Content Cards auf mehreren Geräten angesehen werden können, werden Gerätedaten beim Versand nicht protokolliert. Stattdessen werden diese Informationen bei der Impression protokolliert (wenn die Karte tatsächlich angesehen wird). Webhooks werden an einen Systemendpunkt gesendet (nicht an ein Gerät), daher sind Gerätedaten nicht relevant.

#### Hinweis zum E-Mail-Öffnungsereignis {#note-on-email-open-event}

Das Tracking von E-Mail-Öffnungen ist in jedem Tool fehleranfällig, einschließlich Braze. Mit einer Vielzahl von Datenschutzfunktionen, die von verschiedenen E-Mail-Clients angeboten werden und entweder das automatische Laden von Bildern blockieren oder sie proaktiv auf dem Server laden, sind E-Mail-Öffnungsereignisse sowohl für falsch positive als auch für falsch negative Ergebnisse anfällig.

Während E-Mail-Öffnungsstatistiken in der Gesamtbetrachtung nützlich sein können, z. B. um die Wirksamkeit verschiedener Betreffzeilen zu vergleichen, sollten Sie nicht davon ausgehen, dass ein einzelnes Öffnungsereignis für einzelne Nutzer:innen aussagekräftig ist.

#### Warum sind bestimmte Felder im Tab „Messaging-Verlauf“ leer? {#why-are-certain-fields-blank-in-the-message-history-tab}

Einige Felder können im Tab **Messaging-Verlauf** von Nutzer:innen in den folgenden Szenarien fehlen:

- Wenn bei einem Ereignis Daten für **Gesendete Nachricht** fehlen, bedeutet dies, dass die Campaign keine Nachrichtenvarianten hat.
- Wenn bei einem Ereignis Daten für **Campaign/Canvas** und **Gesendete Nachricht** fehlen, bedeutet dies, dass diese Nachricht über eine API-Campaign (nicht API-getriggerte Campaigns) gesendet wurde, die `campaign_id` und `message_variation_id` nicht angegeben hat. Diese Felder sind optional und können im Anfragekörper weggelassen werden. Wenn diese Felder angegeben werden, werden die Informationen in den Messaging-Verlaufsprotokollen angezeigt.
   - Wenn eine bestimmte Nachricht im Messaging-Verlauf vollständig fehlt, aber im Protokoll **Empfangene Campaigns** erscheint, hat die Person die Campaign wahrscheinlich erhalten, bevor sie als aktuelle:r Nutzer:in identifiziert wurde. Wenn ein bestehendes Profil verwaist ist, wird das Protokoll **Empfangene Campaigns** übertragen, der Messaging-Verlauf jedoch nicht.
- Wenn Daten für **Campaign/Canvas** fehlen, wurde möglicherweise ein manueller Test gesendet. Manuelle Tests werden im Tab **Messaging-Verlauf** protokolliert, aber die Campaign oder der Canvas, die/der gesendet wurde, wird nicht protokolliert.
- Wenn Nutzer:innen in einer Seed-Gruppe oder einer anderen internen Testzielgruppe sind, kann der **Messaging-Verlauf** im Vergleich zu Produktionsversendungen eingeschränkte Campaign- oder Canvas-Metadaten anzeigen.

## Verwandte Artikel {#related-articles}

- [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)
- [POST: Nutzerprofil nach Bezeichner exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [POST: Nutzer:innen löschen]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)