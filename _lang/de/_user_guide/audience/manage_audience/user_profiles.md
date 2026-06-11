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

Um auf das Profil einer Nutzerin oder eines Nutzers zuzugreifen, gehen Sie zur Seite **Nutzer:innen suchen** und suchen Sie nach einer Nutzerin oder einem Nutzer anhand eines der folgenden Kriterien:

- Externe Nutzer-ID
- Braze-ID
- E-Mail
- Telefonnummer
- Push-Token
- Nutzer-Alias im Format „[user_alias]:[alias_name]“, z. B. „amplitude_id:user_123“

Wenn eine Übereinstimmung gefunden wird, können Sie die Informationen einsehen, die Sie für diese Nutzerin oder diesen Nutzer mit dem Braze SDK erfasst haben. Wenn Ihre Suche hingegen mehrere Nutzerprofile zurückgibt, können Sie jedes Profil einzeln zusammenführen oder eine Massenzusammenführung durchführen. Eine vollständige Anleitung finden Sie unter [Doppelte Nutzer:innen zusammenführen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/).

{% alert note %}
**Nutzer:innen suchen** ist nicht dasselbe wie **Nutzer:innen-Lookup** im Segment- oder Campaign-Composer. **Nutzer:innen-Lookup** prüft, ob eine bestimmte Nutzerin oder ein bestimmter Nutzer Ihrer Zielgruppe entspricht, und akzeptiert nur `external_id` oder `braze_id`. **Nutzer:innen suchen** auf dieser Seite unterstützt E-Mail, Telefonnummer, Push-Token und Nutzer-Alias. Weitere Informationen finden Sie unter [Segmente testen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#testing-segments).
{% endalert %}

{% alert important %}
Wenn eine Telefonnummer für die Suche verwendet wird, wird sie in das [`E.164`](https://en.wikipedia.org/wiki/e.164)-Format umgewandelt. Nutzer:innen, deren Telefonnummern nicht in das `E.164`-Format umgewandelt werden können (z. B. weil die Telefonnummer eine ungültige Landesvorwahl oder Ortsvorwahl hat), können nicht über die Telefonnummer gesucht werden.
{% endalert %}

![Suchergebnisse mit einem Banner, das „Mehrere Nutzer:innen entsprechen Ihren Suchkriterien“ anzeigt, und zwei Buttons mit den Beschriftungen „Zurück“ und „Weiter“.]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## Anwendungsfälle {#use-cases}

Nutzerprofile sind eine hervorragende Ressource für die Fehlerbehebung und das Testen, da Sie einfach auf Informationen über den Engagement-Verlauf, die Segmentzugehörigkeit, das Gerät und das Betriebssystem einer Nutzerin oder eines Nutzers zugreifen können.

Wenn beispielsweise eine Nutzerin oder ein Nutzer ein Problem meldet und Sie nicht sicher sind, welches Gerät und Betriebssystem verwendet wird, können Sie den [Tab „Übersicht“](#overview-tab) nutzen, um diese Informationen zu finden (sofern Sie die E-Mail-Adresse oder Nutzer-ID haben). Sie können auch die Sprache einer Nutzerin oder eines Nutzers einsehen, was hilfreich sein kann, wenn Sie eine [mehrsprachige Campaign]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/) beheben, die sich nicht wie erwartet verhalten hat.

Sie können den [Tab „Engagement“](#engagement-tab) verwenden, um zu überprüfen, ob eine bestimmte Nutzerin oder ein bestimmter Nutzer eine Campaign erhalten hat. Darüber hinaus können Sie, wenn diese Nutzerin oder dieser Nutzer die Campaign erhalten hat, sehen, wann sie empfangen wurde. Sie können auch überprüfen, ob eine Nutzerin oder ein Nutzer in einem bestimmten Segment enthalten ist und ob ein Opt-in für Push, E-Mail oder beides vorliegt. Diese Informationen sind nützlich für die Fehlerbehebung. Sie sollten diese Informationen beispielsweise prüfen, wenn eine Nutzerin oder ein Nutzer eine Campaign nicht erhält, die Sie erwartet haben, oder eine Campaign erhält, die Sie nicht erwartet haben.

## Elemente des Nutzerprofils {#elements-of-user-profile}

Ein Nutzerprofil besteht aus vier Hauptbereichen.

- **Übersicht:** Grundlegende Informationen über die Nutzerin oder den Nutzer, Sitzungsdaten, angepasste Attribute, angepasste Events, Käufe und das letzte Gerät, auf dem sich die Nutzerin oder der Nutzer angemeldet hat.
- **Engagement:** Informationen über die Kontakteinstellungen der Nutzerin oder des Nutzers, empfangene Campaigns, Segmente, Kommunikationsstatistiken, Install-Attribution und zufällige Bucket-Nummer.
- **Nachrichtenverlauf:** Aktuelle Messaging-bezogene Ereignisse für diese Nutzerin oder diesen Nutzer aus den letzten 30 Tagen.
- **Feature-Flag-Berechtigung:** Überprüfen Sie, für welche Feature-Flags eine Nutzerin oder ein Nutzer derzeit über Rollouts, Canvas-Schritte und Experimente berechtigt ist.

### Tab „Übersicht“ {#overview-tab}

Der Tab **Übersicht** enthält grundlegende Informationen über eine Nutzerin oder einen Nutzer und deren Interaktionen mit Ihrer App oder Website.

| Übersichtskategorie | Enthält |
| --- | --- |
| Profil | Geschlecht, Altersgruppe, Standort, Sprache, Gebietsschema, Zeitzone und Geburtstag. |
| Sitzungsübersicht | Wie viele Sitzungen stattgefunden haben, wann die erste und letzte Sitzung war und in welchen Apps. |
| Angepasste Attribute | Welche angepassten Attribute dieser Nutzerin oder diesem Nutzer zugeordnet sind und deren zugehörige Werte, einschließlich verschachtelter angepasster Attribute. |
| Letzte Geräte | Auf wie vielen Geräten sich angemeldet wurde, Details zu jedem Gerät und die zugehörigen Werbe-IDs (falls vorhanden). |
| Angepasste Events | Welche angepassten Events diese Nutzerin oder dieser Nutzer durchgeführt hat, wie oft und wann das jeweilige Event zuletzt durchgeführt wurde. |
| Käufe | Lifetime-Umsatz, der dieser Nutzerin oder diesem Nutzer zugeordnet ist, der letzte Kauf, die Gesamtanzahl der Käufe und eine Liste jedes Kaufs. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tab „Übersicht“" }

Weitere Informationen zu diesen Daten finden Sie unter [SDK-Datenerfassung]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/).

![Der Tab „Übersicht“ eines Nutzerprofils.]({% image_buster /assets/img_archive/user_profile2.png %})

### Tab „Engagement“ {#engagement-tab}

Der Tab **Engagement** enthält Informationen über die Interaktionen einer Nutzerin oder eines Nutzers mit den Nachrichten, die Sie über Braze gesendet haben.

| Engagement-Kategorie | Enthält |
| --- | --- |
| Kontakteinstellungen | Abo-Status für E-Mail, SMS und Push sowie die Abo-Gruppen, denen diese Nutzerin oder dieser Nutzer für diese drei Kanäle zugeordnet ist. Dieser Abschnitt enthält auch Changelog-Informationen für Push-Token. Informationen zur Einrichtung von Abos und Opt-ins finden Sie unter [E-Mail]({{site.baseurl}}/user_guide/channels/email/subscriptions/), [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) und [Push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/). |
| Empfangene Campaigns | **Empfangene Campaigns** zeigt den kanalspezifischen Sende- und Anzeigezeitpunkt an. Die meisten Kanäle protokollieren einen Versand, wenn Braze die Nachricht an den Zustellungsanbieter übergibt, auch wenn die Nachricht letztendlich nicht zugestellt wird. **Content Cards** sind anders: Campaigns erscheinen hier erst, nachdem die Nutzerin oder der Nutzer die Karte in der App angesehen hat. Eine Aufschlüsselung nach Kanal finden Sie unter [Wann Campaigns unter „Empfangene Campaigns“ erscheinen](#when-campaigns-appear-in-campaigns-received). Wenn eine Nachricht empfangen, geöffnet oder angeklickt wird, aktualisiert Braze die Daten für alle Profile, die denselben Kanalbezeichner wie das Profil teilen, das die Interaktion protokolliert hat (z. B. dieselbe E-Mail-Adresse für E-Mail oder dieselbe Telefonnummer für SMS oder WhatsApp). Nutzer:innen, die einen Bezeichner mit jemandem teilen, der die Nachricht empfangen, geöffnet oder angeklickt hat, können diesem Filter entsprechen, auch wenn sie ursprünglich nicht in der Campaign waren oder die Nachricht nicht direkt erhalten haben.<br><br>Wählen Sie eine Campaign aus der Liste aus, um sie anzuzeigen. |
| Segmente | Segmente, in denen diese Nutzerin oder dieser Nutzer enthalten ist. Wählen Sie ein Segment aus der Liste aus, um es anzuzeigen. |
| Kommunikationsstatistiken | Wann diese Nutzerin oder dieser Nutzer zuletzt Nachrichten von Ihnen über jeden Kanal erhalten hat. |
| Install-Attribution | Informationen darüber, wie und wann eine Nutzerin oder ein Nutzer Ihre App installiert hat. Mehr erfahren unter [Install-Attribution verstehen]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/install_attribution/). |
| Sonstiges | Die [zufällige Bucket-Nummer]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/) der Nutzerin oder des Nutzers. |
| Empfangene Canvas-Nachrichten | Canvas-Nachrichten, die diese Nutzerin oder dieser Nutzer erhalten hat, und wann. Der Sendezeitpunkt folgt denselben kanalspezifischen Regeln wie **Empfangene Campaigns**; siehe [Wann Campaigns unter „Empfangene Campaigns“ erscheinen](#when-campaigns-appear-in-campaigns-received). Wenn eine Nachricht empfangen, geöffnet oder angeklickt wird, aktualisiert Braze die Daten für alle Profile, die denselben Kanalbezeichner wie das Profil teilen, das die Interaktion protokolliert hat (z. B. dieselbe E-Mail-Adresse für E-Mail oder dieselbe Telefonnummer für SMS oder WhatsApp). Nutzer:innen, die einen Bezeichner mit jemandem teilen, der die Nachricht empfangen, geöffnet oder angeklickt hat, können diesem Filter entsprechen, auch wenn sie ursprünglich nicht in der Campaign waren oder die Nachricht nicht direkt erhalten haben.<br><br>Wählen Sie eine Nachricht aus der Liste aus, um sie anzuzeigen. |
| Prognosen | [Churn-Prognose]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/)- und [Event-Prognose]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/)-Scores für diese Nutzerin oder diesen Nutzer. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tab „Engagement“" }

### Wann Campaigns unter „Empfangene Campaigns“ erscheinen {#when-campaigns-appear-in-campaigns-received}

Im Allgemeinen listet Braze eine Campaign unter **Empfangene Campaigns** auf, nachdem versucht wurde, die Nachricht zu senden. Eine Zustellung an das Gerät oder den Posteingang der Nutzerin oder des Nutzers ist nicht erforderlich, damit ein Versand protokolliert wird. **Empfangene Canvas-Nachrichten** folgt denselben kanalspezifischen Regeln für jeden Canvas-Nachrichtentyp.

- **E-Mail:** Braze protokolliert einen Versand, wenn die Nachricht an Ihren E-Mail-Anbieter (ESP) übergeben wird. Nach dieser Übergabe wird die Nachricht nicht aufgrund von Liquid-Logik, Rate-Limiting oder weil die Nutzerin oder der Nutzer als nicht erreichbar markiert ist, abgebrochen. Die nächsten Ereignisse sind in der Regel eine Zustellung oder ein Bounce.
- **Push:** Braze protokolliert einen Versand, wenn die Nachricht an den Push-Anbieter übergeben wird (z. B. Apple Push Notification service (APNs) oder Firebase Cloud Messaging (FCM)). Der Anbieter versucht in der Regel, sofort zuzustellen; wenn das Gerät nicht verfügbar ist (z. B. offline), kann der Anbieter es erneut versuchen, bis die Nachricht abläuft.
- **In-App-Nachrichten:** Braze protokolliert einen Versand, wenn die Campaign gestartet wird.
- **Content Cards:** Wann Braze ein _Gesendet_-Ereignis protokolliert, hängt vom Zustellungstyp und Ihrer Einstellung **Kartenerstellung** ab. Eine Content-Card-Kampagne erscheint unter **Empfangene Campaigns** im Nutzerprofil erst, nachdem die Nutzerin oder der Nutzer die Karte in der App angesehen hat. Die vollständige Aufschlüsselung finden Sie unter [Wann Sendungen protokolliert werden]({{site.baseurl}}/user_guide/channels/content_cards/reporting/#when-sends-are-logged) und [Empfangene Campaigns und Retargeting-Filter]({{site.baseurl}}/user_guide/channels/content_cards/reporting/#campaigns-received-and-retargeting-filters) im Artikel zur Content-Card-Berichterstattung.
- **SMS, WhatsApp und Webhooks:** Braze protokolliert einen Versand, wenn die Nachricht den Zustellungspfad für den jeweiligen Kanal betritt (z. B. den SMS- oder WhatsApp-Anbieter oder Ihren Webhook-Endpunkt).

{% alert note %}
Diese Beschreibungen beziehen sich darauf, wann ein Versand für **Empfangene Campaigns** protokolliert wird. Sie sind getrennt von [Nachrichtenabbrüchen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/), die eine Nachricht stoppen können, bevor sie einen Anbieter erreicht.
{% endalert %}

![Der Tab „Engagement“ eines Nutzerprofils mit Kontakteinstellungen und Kommunikationsstatistiken.]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### Tab „Nachrichtenverlauf“ {#messaging-history-tab}

Der Tab **Nachrichtenverlauf** des Nutzerprofils zeigt aktuelle Messaging-bezogene Ereignisse (ca. 40) für eine einzelne Nutzerin oder einen einzelnen Nutzer aus den letzten 30 Tagen. Diese Ereignisse umfassen die Nachrichten, die der Nutzerin oder dem Nutzer gesendet, zugestellt und mit denen interagiert wurde, und mehr.

{% alert note %}
Die Daten in diesem Tab werden nach einer Zusammenführung von Nutzer:innen nicht aktualisiert. Außerdem werden Ereignisse, die mit über die API gesendeten Nachrichten verknüpft sind (z. B. der [Endpunkt `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#creating-new-users-with-api-sends)), in diesem Tab nicht angezeigt, wenn in diesen Sendungen keine Campaign-ID angegeben ist.
{% endalert %}

![Der Tab „Nachrichtenverlauf“, der zeigt, welche Campaigns und Canvases eine Nutzerin oder ein Nutzer erhalten hat.]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### Ereignisse anzeigen und verstehen {#viewing-and-understanding-events}

Für jedes Ereignis in der Tabelle **Nachrichtenverlauf** können Sie den Messaging-Kanal, den Event-Typ, den Zeitstempel des Ereignisses, die zugehörige Campaign oder Canvas-Nachricht und die Gerätedaten der Nutzerin oder des Nutzers einsehen. Um nach bestimmten Ereignissen zu filtern, klicken Sie auf **Filter** und wählen Sie Ereignisse aus der Liste aus.

##### Nachrichten-Engagement-Ereignisse {#message-engagement-events}

Die folgenden Nachrichten-Engagement-Ereignisse sind für E-Mail, SMS, Push, In-App-Nachrichten, Content Cards und Webhooks verfügbar. Um mehr darüber zu erfahren, wie bestimmte Ereignisse getrackt werden, lesen Sie das [Glossar der Nachrichten-Engagement-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).

| Kanal | Verfügbare Engagement-Ereignisse |
| --- | --- |
| E-Mail | Bounce<br>Klick<br>Verzögerungsereignisse<br>Zustellung<br>Als Spam markieren<br>Öffnung (siehe [Hinweis zum E-Mail-Öffnungsereignis](#note-on-email-open-event))<br>Senden<br>Soft Bounce<br>Abmelden |
| SMS | Carrier-Senden<br>Zustellung<br>Zustellungsfehler<br>Eingehender Empfang<br>Ablehnung<br>Senden |
| Push | Bounce<br>Beeinflusste Öffnung<br>iOS Foreground<br>Öffnung<br>Senden |
| In-App-Nachricht | Klick<br>Impression |
| Content Cards | Klick<br>Verwerfen<br>Impression<br>Senden |
| Webhooks | Senden |
| WhatsApp | Abbruch<br>Zustellung<br>Fehler<br>Frequency-Capping<br>Eingehender Empfang<br>Gelesen<br>Senden |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nachrichten-Engagement-Ereignisse" }

##### Nachrichtenabbruch-Ereignisse {#message-abort-events}

Nachrichtenabbruch-Ereignisse treten auf, wenn eine an eine Nutzerin oder einen Nutzer gesendete Nachricht aufgrund bedingter Logik in [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/) oder [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content/#aborting-messages) oder durch Liquid-Rendering-Timeouts abgebrochen wurde.

Abbruch-Ereignisse sind für die folgenden Kanäle verfügbar:

- E-Mail
- SMS
- Push
- Webhooks

Abbruch-Ereignisse sind derzeit nicht für In-App-Nachrichten und Content Cards verfügbar.

##### Frequency-Capping-Ereignisse {#frequency-cap-events}

Ein Frequency-Capping-Ereignis tritt auf, wenn eine Nutzerin oder ein Nutzer für den Empfang einer Nachricht qualifiziert ist, diese aber aufgrund von [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping)-Einstellungen nicht tatsächlich erhält. Sie können die Frequency-Capping-Einstellungen unter **Einstellungen** > **Frequency-Capping-Regeln** anpassen.

##### Leere Ziele {#blank-destinations}

Einige Nachrichtensendungen können im Nachrichtenverlauf mit leeren Zielen erscheinen (gekennzeichnet durch „—“). Dies liegt daran, dass einige Kanäle, wie Content Cards und Webhooks, beim Nachrichtenversand keine Gerätedaten erfassen.

Content-Card-Sendungen werden protokolliert, wenn die Karte zur Ansicht verfügbar ist. Da Content Cards auf mehreren Geräten angezeigt werden können, werden Gerätedaten beim Senden nicht protokolliert. Stattdessen werden diese Informationen bei der Impression protokolliert (wenn die Karte tatsächlich angezeigt wird). Webhooks werden an einen Systemendpunkt gesendet (nicht an ein Gerät), daher sind Gerätedaten nicht relevant.

#### Hinweis zum E-Mail-Öffnungsereignis {#note-on-email-open-event}

Das Tracking von E-Mail-Öffnungen ist in jedem Tool, einschließlich Braze, fehleranfällig. Mit einer Vielzahl von Datenschutzfunktionen, die von verschiedenen E-Mail-Clients angeboten werden und entweder das automatische Laden von Bildern blockieren oder sie proaktiv auf dem Server laden, sind E-Mail-Öffnungsereignisse sowohl für falsch-positive als auch für falsch-negative Ergebnisse anfällig.

Während E-Mail-Öffnungsstatistiken in der Gesamtbetrachtung nützlich sein können, z. B. um die Wirksamkeit verschiedener Betreffzeilen zu vergleichen, sollten Sie nicht davon ausgehen, dass ein einzelnes Öffnungsereignis für eine einzelne Nutzerin oder einen einzelnen Nutzer aussagekräftig ist.

#### Warum sind bestimmte Felder im Tab „Nachrichtenverlauf“ leer? {#why-are-certain-fields-blank-in-the-message-history-tab}

Einige Felder können im Tab **Nachrichtenverlauf** einer Nutzerin oder eines Nutzers in den folgenden Szenarien fehlen:

- Wenn bei einem Ereignis Daten für **Gesendete Nachricht** fehlen, bedeutet dies, dass die Campaign keine Nachrichtenvarianten hat.
- Wenn bei einem Ereignis Daten für **Campaign/Canvas** und **Gesendete Nachricht** fehlen, bedeutet dies, dass diese Nachricht über eine API-Kampagne (nicht API-getriggerte Campaigns) gesendet wurde, die `campaign_id` und `message_variation_id` nicht angegeben hat. Diese Felder sind optional und können im Anfragekörper weggelassen werden. Wenn diese Felder angegeben werden, werden die Informationen in die Nachrichtenverlaufsprotokolle übernommen.
   - Wenn eine bestimmte Nachricht im Nachrichtenverlauf vollständig fehlt, aber im Protokoll **Empfangene Campaigns** erscheint, hat die Nutzerin oder der Nutzer die Campaign wahrscheinlich erhalten, bevor sie oder er als aktuelle Nutzerin oder aktueller Nutzer identifiziert wurde. Wenn ein bestehendes Profil verwaist ist, wird das Protokoll **Empfangene Campaigns** übertragen, der Nachrichtenverlauf jedoch nicht.
- Wenn Daten für **Campaign/Canvas** fehlen, wurde möglicherweise ein manueller Test gesendet. Manuelle Tests werden im Tab **Nachrichtenverlauf** protokolliert, aber die Campaign oder der Canvas, die bzw. der gesendet wurde, wird nicht protokolliert.

## Verwandte Artikel {#related-articles}

- [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)
- [POST: Nutzerprofil nach Bezeichner exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)
- [POST: Nutzer:innen löschen]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)