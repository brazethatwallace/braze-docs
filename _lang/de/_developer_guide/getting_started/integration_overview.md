---
nav_title: Überblick über die Integration
article_title: Überblick über die Integration
page_order: 2
description: "Dieser Artikel bietet einen grundlegenden Überblick über den Onboarding-Prozess."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"} Erste Schritte: Überblick über die Integration {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsdk-integration-basics-stylefloatrightwidth120pxborder0-classnoimgbordergetting-started-integration-overview}

> Dieser Artikel bietet einen grundlegenden Überblick über den Onboarding-Prozess.

![Ein Venn-Diagramm mit vier Kreisen – Identifizierung, Integration, Qualitätssicherung und Wartung – mit dem Schwerpunkt „Time to Value“.]({% image_buster /assets/img/getting-started/getting-started-integrate-flower.png %}){: style="max-width:50%;float:right;margin-left:15px;border:none;"}

Als technische Ressource stärken Sie Ihr Team durch die Integration von Braze in Ihren Tech-Stack. Das Onboarding gliedert sich im Wesentlichen in vier Schritte:
* [Identifizierung und Planung](#discovery): Arbeiten Sie mit Ihrem Team zusammen, um den Projektumfang abzustimmen, eine Struktur für Daten und Campaigns zu planen und eine geeignete Workspace-Struktur zu erstellen.
* [Integration](#integration): Führen Sie Ihren Plan aus, indem Sie das SDK und die API integrieren, Messaging-Kanäle aktivieren und den Import und Export von Daten einrichten.
* [Qualitätssicherung](#qa): Bestätigen Sie, dass der Daten- und Nachrichtenaustausch zwischen der Braze-Plattform und Ihrer App oder Website wie erwartet funktioniert.
* [Wartung](#maintenance): Nachdem Sie Braze an Ihr Marketingteam übergeben haben, sorgen Sie weiterhin dafür, dass alles reibungslos läuft.

<br>
{% alert tip %}
Wir wissen, dass jedes Unternehmen seine eigenen Bedürfnisse hat, und Braze ist so konzipiert, dass es eine Vielzahl von Anpassungsmöglichkeiten bietet, die auf Ihre speziellen Anforderungen zugeschnitten werden können. Die Integrationszeit hängt von Ihrem Anwendungsfall ab.
{% endalert %}

## Identifizierung und Planung {#discovery}

In dieser Phase arbeiten Sie mit Ihrem Team zusammen, um den Umfang der Onboarding-Aufgaben festzulegen und sicherzustellen, dass alle Beteiligten auf ein gemeinsames Ziel ausgerichtet sind.

Ihr Team führt eine End-to-End-Planung Ihrer Anwendungsfälle durch, um sicherzustellen, dass alles wie erwartet erstellt werden kann und die richtigen Daten dafür zur Verfügung stehen. In dieser Phase sind Ihr Projektleiter, der CRM-Leiter, die Front- und Backend-Entwickler:innen, die Produktverantwortlichen und die Marketer beteiligt.

Die Identifizierungs- und Planungsphase dauert im Durchschnitt etwa sechs Wochen. Technische Leiter können in dieser Phase mit einem Zeitaufwand von 2–4 Stunden pro Woche rechnen. Entwickler:innen, die mit dem Produkt arbeiten, können davon ausgehen, dass sie in der Identifizierungs- und Planungsphase 10–20 Stunden pro Woche für Braze aufwenden müssen.

{% alert tip %}
Während der Einführungsphase Ihres Unternehmens wird Braze technische Übersichtssitzungen abhalten. Wir empfehlen Entwickler:innen dringend, diese Sitzungen zu besuchen. Technische Übersichtssitzungen bieten Ihnen die Möglichkeit, Gespräche über die Skalierbarkeit der Plattformarchitektur zu führen und praktische Beispiele dafür zu sehen, wie Unternehmen Ihrer Größe mit ähnlichen Anwendungsfällen bereits erfolgreich waren.
{% endalert %}

![Symbole für verschiedene Kanäle, wie E-Mail, Warenkorb, Bilder, Geolocation usw.]({% image_buster /assets/img/getting-started/data-graphic-2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

### Kampagnenplanung {#campaign-planning}

Ihr CRM-Team arbeitet die Messaging-Anwendungsfälle aus, die Sie in naher Zukunft einführen werden. Dazu gehören:
* [Kanal]({{site.baseurl}}/user_guide/channels) (zum Beispiel Push-Benachrichtigungen oder In-App-Nachrichten)
* [Zustellungsmethode]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign) (zum Beispiel geplante Zustellung oder aktionsbasierte Zustellung)
* [Zielgruppe]({{site.baseurl}}/user_guide/audience/segments)
* [Erfolgsmetriken]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)

Eine Neukundenkampagne könnte zum Beispiel so aussehen: eine E-Mail, die täglich um 10 Uhr an ein Segment von Kund:innen gesendet wird, die gestern ihre erste Sitzung protokolliert haben. Das Konversions-Event (die Erfolgsmetrik) ist das Protokollieren einer Sitzung.

<br>
{% alert important %}
Mit der Integration kann erst begonnen werden, wenn der Schritt der Kampagnenplanung abgeschlossen ist. In diesem Schritt wird festgelegt, welche Komponenten von Braze während der Integrationsphase konfiguriert werden müssen.
{% endalert %}

### Erstellen von Datenanforderungen {#creating-data-requirements}

Ihr CRM-Team sollte dann festlegen, welche Daten benötigt werden, um die geplanten Campaigns einzuführen, indem es Datenanforderungen erstellt.

Viele gängige Arten von Nutzerattributen, wie Name, E-Mail-Adresse, Geburtsdatum, Land und Ähnliches, werden nach der Integration des Braze SDK automatisch getrackt. Andere Arten von Daten müssen als angepasste Daten definiert werden.

Als Entwickler:in legen Sie gemeinsam mit Ihrem Team fest, welche zusätzlichen, angepassten Daten getrackt werden sollen. Ihre angepassten Daten haben Einfluss darauf, wie Ihre Nutzerbasis klassifiziert und segmentiert wird. Sie richten eine Event-Taxonomie für Ihren Growth Stack ein, um Ihre Daten so zu strukturieren, dass sie bei der Übertragung in und aus Braze mit Ihren Systemen kompatibel sind.

{% alert tip %}
Halten Sie die Nomenklatur der Daten in allen Tools einheitlich. Ihr Data Warehouse kann zum Beispiel „zeitlich begrenztes Angebot kaufen“ auf eine bestimmte Weise erfassen. Sie müssen entscheiden, ob für dieses Format ein angepasstes Event in Braze erforderlich ist.
{% endalert %}

Erfahren Sie mehr über [automatisch erfasste Daten und angepasste Daten]({{site.baseurl}}/developer_guide/analytics).

### Planung von Anpassungen {#customizations-planning}

Sprechen Sie mit Ihren Marketern über deren gewünschte Anpassungen. Möchten Sie zum Beispiel die Standard-Content Cards von Braze implementieren? Möchten Sie ihr Erscheinungsbild leicht anpassen, damit es Ihren Markenrichtlinien entspricht? Möchten Sie eine völlig neue Benutzeroberfläche für eine Komponente entwickeln und deren Analytics von Braze verfolgen lassen? Unterschiedliche Stufen der Anpassung erfordern einen unterschiedlichen Umfang.

### Zugang zum Dashboard erhalten {#getting-dashboard-access}

Das Braze-Dashboard ist unsere Web-UI-Oberfläche. Marketer nutzen das Dashboard, um ihre Arbeit zu erledigen und Inhalte zu erstellen. Entwickler:innen nutzen das Dashboard, um Einstellungen für die Integration von Apps zu verwalten, wie z. B. API-Schlüssel und Zugangsdaten für Push-Benachrichtigungen.

Ihr Teamadministrator sollte Sie (und alle anderen Teammitglieder, die Zugriff auf Braze benötigen) als Nutzer:innen in Ihrem Dashboard hinzufügen.

### Workspaces und API-Schlüssel {#workspaces-and-api-keys}

Ihr Teamadministrator wird auch verschiedene [Workspaces]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces) erstellen. Workspaces fassen Ihre Daten – Nutzer:innen, Segmente, API-Schlüssel – an einem Ort zusammen. Es empfiehlt sich, lediglich verschiedene Versionen derselben App oder sehr ähnlicher Apps in einem Workspace zusammenzufassen.

Ein wichtiger Aspekt ist, dass Workspaces API-Schlüssel für mehrere Plattformen (z. B. iOS und Android) bereitstellen. Sie verwenden die korrelierten API-Schlüssel, um SDK-Daten mit einem bestimmten Workspace zu verknüpfen. Navigieren Sie zu Ihren Workspaces, um auf den API-Schlüssel für Ihre einzelnen Apps zuzugreifen. Vergewissern Sie sich, dass jeder API-Schlüssel über die erforderlichen Berechtigungen verfügt, um die von Ihnen vorgesehenen Aufgaben auszuführen. Weitere Informationen finden Sie im [Artikel über die API-Bereitstellung]({{site.baseurl}}/api/basics#rest-api-key-permissions).

{% alert important %}
Wichtig ist, dass Sie unterschiedliche Umgebungen für die Entwicklung und die Produktion einrichten. Die Einrichtung einer Testumgebung verhindert, dass Sie während des Onboardings und der QA echtes Geld ausgeben. Um eine Testumgebung zu erstellen, richten Sie einen Test-Workspace ein und stellen Sie sicher, dass Sie dessen API-Schlüssel verwenden, damit nicht der Produktions-Workspace mit Testdaten gefüllt wird.
{% endalert %}

## Integration {#integration}

![Abstrakte Pyramidengrafik, die den Informationsfluss von einer Datenquelle zu einem Gerät darstellt.]({% image_buster /assets/img/getting-started/data-graphic.png %}){: style="max-width:45%;float:right;margin-left:15px;"}

Braze unterstützt iOS-Apps, Android-Apps, Web-Apps und mehr. Sie können sich auch für ein plattformübergreifendes Wrapper-SDK entscheiden, wie z. B. React Native oder Unity. In der Regel dauert eine Integration bei unseren Kund:innen zwischen 1 und 6 Wochen. Viele Kund:innen haben für die Braze-Integration nur eine:n einzige:n Entwickler:in benötigt – abhängig von der Breite der technischen Fähigkeiten und der verfügbaren Kapazität. Letztlich kommt es darauf an, welchen Umfang Ihre spezifische Integration hat und wie viel Zeit Ihr Team dem Braze-Projekt widmet.

Sie brauchen Entwickler:innen, die sich mit Folgendem auskennen:
* Arbeiten in der nativen Schicht Ihrer App oder Website
* Erstellen von Prozessen, die auf unsere REST API zugreifen
* Integrationstests
* JSON-Web-Token-Authentifizierung
* Allgemeine Kenntnisse der Datenverwaltung
* Einrichten von DNS-Einträgen

### CDP-Integrationspartner {#cdp-integration-partners}

Viele Kund:innen sehen im Onboarding von Braze eine Gelegenheit, auch eine geschäftskunden Data Platform (CDP) als Integrationspartner einzubinden. Braze bietet Daten-Tracking und Analytics, während eine CDP zusätzlich Daten-Routing und Orchestrierung bieten kann. Braze unterstützt die nahtlose Integration mit vielen CDPs, darunter u. a. [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle) und [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment).

Wenn Sie eine Side-by-Side-Integration mit einer CDP durchführen, werden die Aufrufe aus dem SDK der CDP dem Braze SDK zugeordnet. Im Wesentlichen ist Folgendes zu beachten:
* Identifizierungsaufrufe auf `changeUser` ([Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)/), [Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)) zuordnen und Attribute festlegen.
* Daten-Flush-Aufrufe auf `requestImmediateDataFlush` ([Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-immediate-data-flush.html?query=abstract%20fun%20requestImmediateDataFlush()), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/requestimmediatedataflush()), [Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestimmediatedataflush)) zuordnen.
* Angepasste Events oder Käufe protokollieren.

Je nachdem, für welche Plattform Sie sich entschieden haben, sind möglicherweise Beispiel-Integrationen zwischen dem Braze SDK und der CDP Ihrer Wahl verfügbar. Weitere Informationen finden Sie in unserer [Liste der CDP-Technologiepartner]({{site.baseurl}}/partners/data_and_analytics).

### Braze-SDK-Integration {#braze-sdk-integration}

Das Braze SDK stellt zwei wichtige Funktionen bereit: Es erfasst und synchronisiert Nutzerdaten in ein konsolidiertes Nutzerprofil und stellt Messaging-Kanäle wie Push-Benachrichtigungen, In-App-Nachrichten und Content Cards bereit.

{% alert tip %}
Wenn das Braze SDK vollständig in Ihre App oder Website integriert ist, eröffnen sich völlig neue Marketing-Möglichkeiten. Wenn Sie die Integration des Braze SDK aufschieben, sind einige der in der Dokumentation beschriebenen Funktionen nicht verfügbar.
{% endalert %}

{% alert note %}
Um eine zusätzliche Sicherheitsebene hinzuzufügen, können Sie die [SDK-Authentifizierung]({{site.baseurl}}/developer_guide/sdk_integration/authentication) aktivieren, um unbefugte SDK-Anfragen zu verhindern. Dieses Feature ist auf allen gängigen Plattformen verfügbar, einschließlich Web, iOS, Android, React Native, Flutter, Unity, Cordova, .NET MAUI (Xamarin) und Expo.
{% endalert %}

Während der SDK-Implementierung werden Sie:

* SDK-Integrationscode für jede Plattform schreiben, die Sie unterstützen möchten.
* Die Messaging-Kanäle für jede Plattform aktivieren und so sicherstellen, dass das Braze SDK die Daten aus Ihren Interaktionen mit Ihren Kund:innen über E-Mail, SMS, Push-Benachrichtigungen und andere Kanäle verfolgt.
* Alle geplanten Anpassungen der UI-Komponenten erstellen (z. B. angepasste Content Cards). Für vollständig angepasste Inhalte müssen Sie Analytics protokollieren, da die automatische Datenerfassung des SDK Ihre neuen Komponenten nicht erkennt. Sie können sich bei dieser Implementierung an unseren Standardkomponenten orientieren.

### Verwendung der Braze API {#using-the-braze-api}

Sie werden unsere REST API zu verschiedenen Zeitpunkten Ihrer Nutzung von Braze für verschiedene Aufgaben verwenden. Die Braze API ist nützlich für:

1. Importieren von historischen Daten; und
2. Kontinuierliche Updates, die nicht in Braze ausgelöst werden. Wenn ein Nutzerprofil beispielsweise auf VIP hochgestuft wird, ohne dass sich die Person bei einer App anmeldet, muss die API diese Information an Braze übermitteln.

Starten Sie mit der [Braze API]({{site.baseurl}}/api/basics).

{% alert important %}
Achten Sie bei der Verwendung der API darauf, dass Sie Ihre Anfragen bündeln und nur Delta-Werte senden. Braze schreibt jedes gesendete Attribut neu. Aktualisieren Sie keine angepassten Attribute, deren Werte sich nicht geändert haben.
{% endalert %}

### Einrichten der Produktanalytik {#setting-up-product-analytics}

Bei Braze dreht sich alles um Daten. Die Daten in Braze werden im Nutzerprofil gespeichert.

Datenpunkte sind eine Struktur, mit der Sie sicherstellen, dass Sie die richtigen Daten und nicht bloß „irgendwelche“ Daten für Ihre Marketer erfassen. Machen Sie sich mit den [Datenpunkten]({{site.baseurl}}/user_guide/data/infrastructure/data_points) vertraut.

### Migrieren alter Nutzerdaten {#migrating-legacy-user-data}

Sie können den Braze-Endpunkt [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) verwenden, um historische Daten zu migrieren, die außerhalb von Braze aufgezeichnet wurden. Beispiele für häufig importierte Daten sind Push-Token und frühere Käufe. Dieser Endpunkt kann für einmalige Importe oder regelmäßige Batch-Updates verwendet werden.

Sie können auch Nutzer:innen importieren und Kundenattributwerte durch einen einmaligen [CSV-Upload]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#importing-a-csv) in das Dashboard aktualisieren. Das Hochladen von CSV-Dateien kann für Marketer hilfreich sein, während unsere REST API mehr Flexibilität ermöglicht.

### Einrichten des Sitzungs-Trackings {#setting-up-session-tracking}

Das Braze SDK generiert Datenpunkte für „Sitzung öffnen“ und „Sitzung schließen“. Außerdem führt das Braze SDK in regelmäßigen Abständen Daten-Flushes durch. Unter den folgenden Links finden Sie die Standardwerte für das Sitzungs-Tracking. Alle Werte können angepasst werden – [Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=swift), [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web).

### Tracking von angepassten Events, Attributen und Kauf-Events {#tracking-custom-events-attributes-and-purchase-events}

Stimmen Sie sich mit Ihrem Team ab, wie Sie Ihr geplantes Datenschema, einschließlich angepasster Events, Nutzerattribute und Kauf-Events, einrichten möchten. Ihr [angepasstes Datenschema]({{site.baseurl}}/user_guide/data/activation/events/custom_events) wird über das Dashboard eingegeben und muss genau dem entsprechen, was Sie während der SDK-Integration implementieren.

{% alert tip %}
Nutzer-IDs – in Braze `external_id` genannt – sollten für alle bekannten Nutzer:innen festgelegt werden. Diese sollten sich nicht ändern und zugänglich sein, wenn eine Person die App öffnet. So können Sie Ihre Nutzer:innen über verschiedene Geräte und Plattformen hinweg verfolgen. Lesen Sie den Artikel [Nutzerlebenszyklus]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) für bewährte Verfahren.
{% endalert %}

### Andere Tools {#other-tools}

Je nach Anwendungsfall müssen Sie möglicherweise weitere Tools einrichten. Beispielsweise müssen Sie möglicherweise ein Tool wie [Geofences]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences) konfigurieren, um Ihre Nutzer-Storys zu realisieren. Wir haben festgestellt, dass Kund:innen, die die Möglichkeit haben, diese zusätzlichen Tools nach Abschluss der wesentlichen Integrationsschritte einzurichten, am erfolgreichsten sind.

## Qualitätssicherung {#qa}

Durch eine QA-Prüfung, die Sie während der Integration durchführen, stellen Sie sicher, dass alles wie erwartet funktioniert. Diese QA lässt sich in zwei allgemeine Kategorien einteilen: Datenaufnahme und Messaging-Kanäle.

{% alert important %}
Stellen Sie sicher, dass Ihre Produktions- und Testumgebungen eingerichtet sind, bevor Sie mit der QA beginnen.
{% endalert %}

| **QA der Datenaufnahme** | **QA des Messagings** |
|---------------------------|---------------------------------------------------------------|
| Die Qualitätssicherung bezieht sich auf die Aufnahme, die Speicherung und den Export der Daten. | So stellen Sie sicher, dass Ihre Nachrichten korrekt an Ihre Nutzer:innen gesendet werden und alles hervorragend aussieht. |
| Führen Sie Tests durch, um sicherzustellen, dass die Daten ordnungsgemäß gespeichert werden. | Erstellen Sie Segmente von Nutzer:innen. |
| Vergewissern Sie sich, dass die Sitzungsdaten dem vorgesehenen Workspace in Braze korrekt zugewiesen werden. | Starten Sie Campaigns und Canvases erfolgreich. |
| Bestätigen Sie, dass Beginn und Ende der Sitzung aufgezeichnet werden. | Vergewissern Sie sich, dass die richtigen Campaigns für die richtigen Nutzersegmente angezeigt werden. |
| Bestätigen Sie, dass die Informationen zu den Nutzerattributen in den Nutzerprofilen korrekt erfasst sind. | Vergewissern Sie sich, dass die Push-Token korrekt registriert werden. |
| Testen Sie, ob die angepassten Daten in den Nutzerprofilen korrekt erfasst werden. | Vergewissern Sie sich, dass die Push-Token korrekt entfernt werden. |
| Erstellen Sie anonyme Nutzerprofile. | Testen Sie, ob die Push-Campaigns korrekt an die Geräte gesendet werden und das Engagement protokolliert wird. |
| Bestätigen Sie, dass aus anonymen Nutzerprofilen bekannte Nutzerprofile werden, wenn die Methode `changeUser()` aufgerufen wird. | Testen Sie, ob In-App-Nachrichten zugestellt und Metriken protokolliert werden. |
|                           | Testen Sie, ob Content Cards zugestellt und Metriken protokolliert werden. |
|                           | Ermöglichen Sie Connected-Content (zum Beispiel AccuWeather). |
|                           | Vergewissern Sie sich, dass alle Integrationen von Messaging-Kanälen ordnungsgemäß zusammenarbeiten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Qualitätssicherung" }

{% alert note %}
Verwenden Sie bei der QA Ihrer SDK-Integration den [SDK-Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging), um Probleme zu beheben, ohne die ausführliche Protokollierung für Ihre App zu aktivieren.
{% endalert %}

### Übergabe von Braze an Marketer {#passing-braze-off-to-marketers}

Nach der Integration Ihrer Plattform oder Website werden Sie Ihr Marketingteam einbeziehen wollen, um ihm die Verantwortung für die Plattform zu übertragen. Dieser Prozess sieht in jedem Unternehmen anders aus, kann aber Folgendes umfassen:

* Zusammenstellen komplexer [Liquid-Logik]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid#about-liquid)
* Unterstützung beim [IP-Warming für E-Mails]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)
* Sicherstellen, dass andere Beteiligte verstehen, welche Arten von Daten getrackt werden

### Für die Zukunft entwickeln {#develop-for-the-future}

Haben Sie schon einmal eine Codebasis geerbt und hatten keine Ahnung, was sich die ursprünglichen Entwickler:innen dabei gedacht haben? Schlimmer noch: Haben Sie schon einmal Code geschrieben, ihn vollständig verstanden und waren dann völlig verwirrt, als Sie ein Jahr später darauf zurückkamen?

Beim Onboarding von Braze werden die gemeinsamen Entscheidungen, die Sie in Bezug auf Daten, Nutzerprofile, den Umfang der Integrationen, die Funktionsweise von Anpassungen und mehr getroffen haben, noch frisch in Ihrem Gedächtnis und daher offensichtlich sein. Wenn Ihr Team Braze erweitern möchte oder wenn Ihrem Braze-Projekt andere technische Ressourcen zugewiesen werden, werden diese Informationen nicht mehr so präsent sein.

Erstellen Sie eine Ressource, um die Informationen festzuhalten, die Sie in den technischen Übersichtssitzungen gelernt haben. Diese Ressource hilft Ihnen, Zeit beim Onboarding neuer Entwickler:innen für Ihr Team zu sparen (oder kann von Ihnen selbst als Referenz herangezogen werden, wenn Sie Ihre aktuelle Braze-Implementierung erweitern müssen).

## Wartung {#maintenance}

Nach der Übergabe an Ihre Marketer werden Sie weiterhin für die Wartung zuständig sein. Achten Sie auf iOS- und Android-Updates, die sich auf das Braze SDK auswirken könnten, und stellen Sie sicher, dass Ihre Drittanbieter auf dem neuesten Stand sind.

Aktualisierungen an der Braze-Plattform können Sie über das Braze [GitHub](https://github.com/braze-inc/) verfolgen. Gelegentlich erhält Ihr Administrator auch E-Mails über dringende Updates und Fehlerbehebungen direkt von Braze.

## SDK-Rate-Limits {#sdk-rate-limits}

### Monthly Active Users CY 24-25, Universal MAU, Web MAU und Mobile MAU {#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau}

Für Kund:innen, die Monthly Active Users CY 24-25, Universal MAU, Web MAU und Mobile MAU erworben haben, setzt Braze serverseitige Rate-Limits für API-Anfragen durch, die von unseren SDKs zur Aktualisierung von Sitzungen, Nutzerattributen, Events und anderen Nutzerprofildaten verwendet werden. Dies dient der Stabilität der Plattform und der Aufrechterhaltung eines schnellen, zuverlässigen Dienstes.

* Die stündlichen Rate-Limits richten sich nach dem erwarteten SDK-Traffic auf Ihrem Konto, der der Anzahl der monatlich aktiven Nutzer:innen (MAU), die Sie erworben haben, der Branche, der Saisonalität oder anderen Faktoren entsprechen kann. Wenn das stündliche Rate-Limit erreicht ist, drosselt Braze die Anfragen bis zur nächsten Stunde.
* Alle Rate-Limit-Anfragen werden vom SDK automatisch erneut versucht.
* SDK-Anfragen korrelieren mit der Menge der angepassten Daten, die in Ihrer Implementierung gesammelt werden. Wenn Sie ständig nahe an Ihrem stündlichen Rate-Limit liegen oder es erreichen, sollten Sie Folgendes in Betracht ziehen:
    * Überprüfen Sie Ihre SDK-Integration, um eine übermäßige Datenerfassung zu reduzieren.
    * Blockieren Sie angepasste Daten, die für Ihre Marketing-Anwendungsfälle nicht unbedingt erforderlich sind.
* Burst-Rate-Limits sind kurzlebige Rate-Limits, die angewendet werden, wenn in einem sehr kurzen Zeitraum (d. h. innerhalb von Sekunden) eine große Anzahl von Anfragen eintrifft. Sie müssen nicht eingreifen, wenn Burst-Limits auftreten – das SDK wird es kurz darauf erneut versuchen.
* Konstante Rate-Limits kontrollieren das anhaltende Anfragevolumen über einen rollierenden Zeitraum, der länger ist als das Burst-Fenster (z. B. mehrere Minuten), und tragen dazu bei, den laufenden Datenverkehr zwischen Burst-Limits und Ihrem stündlichen Rate-Limit auszugleichen.

### Ihre Rate-Limits finden {#finding-your-rate-limits}

Um die aktuellen Limits auf der Grundlage des erwarteten SDK-Durchsatzes zu finden, gehen Sie zu **Einstellungen** > **APIs und Bezeichner** > **API- und SDK-Limits**.

Die historische Nutzung finden Sie unter **Einstellungen** > **APIs und Bezeichner** > **API- und SDK-Dashboard**.

### Höhere Rate-Limits anfordern {#requesting-higher-rate-limits}

Sollten Sie ein höheres Braze-Rate-Limit benötigen, wenden Sie sich bitte an den Braze-Support oder Ihren geschäftskunden-Success-Manager und geben Sie dabei die folgenden Details an:

* Ob Sie eine vorübergehende oder dauerhafte Erhöhung benötigen.
* Warum Sie die Erhöhung benötigen.
* Welche Endpunkte und Umgebungen betroffen sind.
* Ihr voraussichtliches Traffic-Volumen und Ihren Zeitplan, einschließlich Startdatum, Dauer und Spitzenzeiten.
* Ob Sie Aufrufe bündeln oder den Datenverkehr über einen längeren Zeitraum verteilen können.

Nachdem Sie Ihre Anfrage eingereicht haben, prüft Braze diese und informiert Sie über das Ergebnis.

### Änderungen und Support {#changes-and-support}

Braze kann Rate-Limits ändern, um die Systemstabilität zu schützen oder einen höheren Datendurchsatz auf Ihrem Konto zu ermöglichen. Wenden Sie sich an den Braze-Support oder Ihren geschäftskunden-Success-Manager, wenn Sie Fragen zu Rate-Limits haben und wissen möchten, wie sich diese auf Ihr Unternehmen auswirken.