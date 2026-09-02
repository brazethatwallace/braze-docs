---
nav_title: Mai
page_order: 8
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Mai 2019."
---

# Mai 2019 {#may-2019}

## Content Cards

Content Cards sind persistente Inhalte, die in den App- und Internet-Erlebnissen der Kund:innen erscheinen.

Mit Content Cards können Sie einen zielgerichteten, dynamischen Stream mit reichhaltigen Inhalten an Ihre Kund:innen senden, und zwar direkt in den Apps, die sie lieben, ohne ihr Erlebnis zu unterbrechen. Oder Sie können Content Cards mit anderen Kanälen wie E-Mail oder Push-Benachrichtigungen kombinieren, um kohärente Marketing-Strategien zu ermöglichen.

![Content-Cards-Feed]({% image_buster /assets/img/cc-feed.png %}){: height="50%" width="50%"}

Darüber hinaus unterstützen Content Cards mehr personalisierte Features, einschließlich Karten-Anheftung, Kartenausblendung, API-basierte Zustellung, angepasste Karten-Ablaufzeiten und Kartenanalyse.

Verwenden Sie sie, um Benachrichtigungszentren, Homepage-Feeds und Feeds für Aktionen zu erstellen.

Sie müssen ein Update or aktualisieren auf eine unterstützte Braze SDK or Software-Development-Kit-Version durchführen:
- iOS: 3.8.0 oder höher
- Android: 2.6.0 oder höher
- Web: 2.2.0 oder höher

[Erfahren Sie hier mehr über Content Cards!]({{site.baseurl}}/user_guide/channels/content_cards)

{% alert Update or aktualisieren %}
Content Cards für Currents und unsere API-Dokumentation für Content Cards werden im Laufe dieser Woche veröffentlicht. Bleiben Sie dran!
{% endalert %}

## Erweiterung der Roku-Plattform {#roku-platform-addition}

Braze hat einen neuen Kanal zu unseren Möglichkeiten hinzugefügt! Durch die Expansion in neue Kanäle können wir unsere Kund:innen in die Lage versetzen, ihre Daten durch das Verständnis des Sehverhaltens anzureichern oder ihren Verbraucher:innen über alle relevanten Kanäle hinweg sinnvolle Erlebnisse zu bieten.

Sie können jetzt [Daten von Roku-Geräten abrufen]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku) und zur Datenanreicherung sowie zum angepassten Event-Tracking nutzen.

## Benachrichtigungseinstellungen für Canvas- oder Campaign-Updates {#notification-preferences-for-canvas-or-campaign-updates}

Diese [neue Benachrichtigung]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences#notification-preferences) informiert Sie per E-Mail, wenn eine Campaign oder ein Canvas aktiviert, aktualisiert, reaktiviert oder deaktiviert wird. Aktivieren Sie dies unter **Benachrichtigungseinstellungen** in Ihrem Braze-Konto.

## Jampp-Technologiepartner-Dokumentation {#jampp-technology-partner-documentation}

Jampp ist eine Performance-Marketing-Plattform für die Akquisition und das Retargeting von Mobile-Kund:innen. Es kombiniert Verhaltensdaten mit prognostischer und programmatischer Technologie, um Umsatz für Werbetreibende zu generieren, indem es persönliche, relevante Anzeigen schaltet, die Verbraucher:innen zum ersten Mal oder häufiger zum Kauf anregen.

Braze-Kund:innen können [sich mit Jampp integrieren]({{site.baseurl}}/partners/jampp), indem sie den Braze-Webhook-Kanal so konfigurieren, dass er Events in Jampp streamt. Dadurch haben Kund:innen die Möglichkeit, ihre Retargeting-Initiativen mit Jampp innerhalb des Ökosystems für mobile Werbung um umfangreichere Datensätze zu erweitern.

## Plattformauswahl für In-App-Nachrichten {#platform-picker-for-in-app-messages}

Mit unserer Plattformauswahl, die diesen Schritt bei der Erstellung von Campaigns hervorhebt, können Sie leichter auswählen, wohin Ihre In-App-Nachrichten gesendet werden und für welche Plattformen sie bestimmt sind.

![Plattformauswahl]({% image_buster /assets/img/iam_platforms.gif %})

## Dispatch-ID-Currents-Feld für E-Mail {#dispatch-id-currents-field-for-email}

{% alert Update or aktualisieren %}
Das Verhalten für `dispatch_id` unterscheidet sich zwischen Canvas und Campaigns, da Braze Canvas-Schritte (mit Ausnahme von Entry-Schritten, die geplant werden können) als getriggerte Ereignisse behandelt, auch wenn sie „geplant“ sind. Erfahren Sie mehr über das [`dispatch_id`-Verhalten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id) in Canvas und Campaigns.

_Update im August 2019 vermerkt._
{% endalert %}

In dem Bestreben, unsere Currents-Funktionen weiter zu verbessern, fügen wir `dispatch_id` als Feld zu den E-Mail-Ereignissen von Currents für alle Konnektoren hinzu.

Die `dispatch_id` ist die eindeutige ID, die für jede von der Braze-Plattform gesendete Übertragung bzw. Sendung generiert wird.

Während alle Kund:innen, die eine geplante Nachricht erhalten, dieselbe `dispatch_id` erhalten, bekommen Kund:innen, die entweder aktionsbasierte oder API-getriggerte Nachrichten erhalten, eine eindeutige `dispatch_id` pro Nachricht. Mit dem Feld `dispatch_id` können Sie feststellen, welche Instanz einer wiederkehrenden Campaign für die Konversion verantwortlich ist. So erhalten Sie mehr Insights und Informationen darüber, welche Arten von Campaigns dazu beitragen, Ihre Geschäftsziele zu erreichen.

## Feature zur Kampagnensortierung „Nur eigene anzeigen“ {#only-show-mine-campaign-sorting-feature}

Wenn Nutzer:innen in der Kampagnentabelle das Kontrollkästchen `Only Show Mine` aktivieren, werden die Ergebnisse nach Campaigns gefiltert, die nur von den angemeldeten Nutzer:innen erstellt wurden. Zusätzlich können Nutzer:innen die Suchleiste nutzen, indem sie `created_by_me:true` eingeben.

Außerdem ist die Seitenleiste des Kampagnen-Rasters jetzt in der Größe veränderbar!

## Nutzer:innen nach Alias löschen {#delete-users-by-alias}

Sie können jetzt den Endpunkt `users/delete` verwenden, um [Nutzer:innen nach Alias zu löschen]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)!

## Eindeutige Berechnung für Klicks und Öffnungen von E-Mails {#unique-calculation-for-email-clicks-and-opens}

Eindeutige Klicks und eindeutige Öffnungen für E-Mails werden jetzt in einem 7-Tage-Zeitfenster pro Nutzer:in erfasst und angezeigt und innerhalb dieses 7-Tage-Fensters um 1 erhöht, und zwar für jede `dispatch_id`.

Mit `dispatch_id` können wiederkehrende Nachrichten die tatsächliche Anzahl eindeutiger Öffnungen oder eindeutiger Klicks jeder Nachricht widerspiegeln. Jetzt, da `dispatch_id` in Currents verfügbar ist, wird es für Kund:innen einfach sein, diese Daten abzugleichen.

Alle Nutzer:innen, die auch Mailjet verwenden, werden einen Anstieg dieser Zahlen feststellen, da der bisherige Zeitrahmen für die Eindeutigkeit über 30 Tage betrug. Sie sollten vor drei (3) Wochen auf diese Änderung aufmerksam gemacht worden sein. Für SendGrid-Kund:innen sollte es keinen Unterschied geben.

Sie können nach diesen aktualisierten Begriffen in unserem [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary) suchen.

{% alert Update or aktualisieren %}
Das Verhalten für `dispatch_id` unterscheidet sich zwischen Canvas und Campaigns, da Braze Canvas-Schritte (mit Ausnahme von Entry-Schritten, die geplant werden können) als getriggerte Ereignisse behandelt, auch wenn sie „geplant“ sind. [Erfahren Sie mehr über das [`dispatch_id`-Verhalten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id) in Canvas und Campaigns.

_Update im August 2019 vermerkt._
{% endalert %}

## Kanal mit dem größten Engagement {#most-engaged-channel}

{% alert Update or aktualisieren %}
Ab der [Produktversion im November 2019]({{site.baseurl}}/help/release_notes/2019/november#intelligence-suite) wurde „Most Engaged Channel“ in [„Intelligent Channel“]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel) umbenannt.
{% endalert %}

Der Filter „Most Engaged Channel“ wählt den Teil Ihrer Zielgruppe aus, für den der ausgewählte Messaging-Kanal der „beste“ Kanal ist. In diesem Fall bedeutet „beste“ „hat die höchste Wahrscheinlichkeit eines Engagements, wenn man den Verlauf der Nutzer:innen betrachtet“. Sie können E-Mail, Web-Push oder Mobile-Push (das jedes verfügbare mobile Betriebssystem oder Gerät einschließt) als Kanal auswählen.

Sehen Sie sich diesen neuen Filter in unserer [Bibliothek für Segmentierungsfilter]({{site.baseurl }}/user_guide/engagement_tools/segments/segmentation_filters/) an.