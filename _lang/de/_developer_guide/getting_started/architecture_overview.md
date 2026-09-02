---
nav_title: Architektonische Übersicht
article_title: Architektonische Übersicht
page_order: 3
description: "Dieser Artikel beschreibt die verschiedenen Teile des Technologie-Stacks von Braze und enthält Links zu relevanten Artikeln."
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

# Die ersten Schritte: Architektonische Übersicht {#getting-started-architectural-overview}

> Dieser Artikel beschreibt die verschiedenen Teile des Technologie-Stacks von Braze und enthält Links zu relevanten Artikeln.

Bei Braze geht es in erster Linie um Daten. Die Braze-Plattform, unterstützt durch das SDK, die REST API und Partnerintegrationen, erlaubt Ihnen, Daten zu aggregieren und darauf zu reagieren.

![Braze hat verschiedene Schichten. Insgesamt besteht es aus dem SDK, der API, dem Dashboard und den Partnerintegrationen. Diese tragen jeweils zu einem Datenaufnahme-Layer, einem Klassifizierungs-Layer, einem Orchestrierungs-Layer, einem Personalisierungs-Layer und einem Aktions-Layer bei. Der Aktions-Layer verfügt über verschiedene Kanäle, darunter Push-Benachrichtigungen, In-App-Nachrichten, Connected Catalog, Webhook, SMS und E-Mail.]({% image_buster /assets/img/getting-started/braze_listen_understand_act.png %}){: style="display:block;margin:auto;" }

* [Datenaufnahme](#ingestion): Braze bezieht Daten aus einer Vielzahl von Quellen.
* [Klassifizierung](#classification): Ihr Marketing-Team segmentiert Ihre Nutzerbasis dynamisch anhand dieser Metriken.
* [Orchestrierung](#orchestration): Braze koordiniert auf intelligente Weise Nachrichten an verschiedene Zielgruppen-Segmente zum idealen Zeitpunkt.
* [Aktion](#action): Ihr Marketing-Team arbeitet mit den Daten und erstellt Inhalte über eine Vielzahl von Messaging-Kanälen wie SMS und E-Mail.
* [Personalisierung](#personalization): Die Daten werden in Realtime mit personalisierten Informationen über Ihre Zielgruppe transformiert.
* [Export](#exporting-data): Anschließend verfolgt Braze das Engagement Ihrer Nutzer:innen mit diesen Nachrichten und speist es zurück in die Plattform, wodurch ein Kreislauf entsteht. Sie erhalten Insights in diese Daten durch Realtime-Berichte und Analytics.

All dies zusammen sorgt für erfolgreiche Interaktionen zwischen Ihrer Nutzerbasis und Ihrer Marke, damit Sie Ihre Ziele erreichen können. Braze bietet das alles im Rahmen eines vertikal integrierten Stacks. Lassen Sie uns jede Schicht einzeln untersuchen.

## Datenaufnahme {#ingestion}

Braze basiert auf einer Streaming-Daten-Architektur, die Snowflake, Kafka, MongoDB und Redis nutzt. Daten aus verschiedenen Quellen können über SDK und API in Braze geladen werden. Die Plattform kann alle Daten in Realtime verarbeiten, unabhängig davon, wie verschachtelt oder strukturiert sie sind. Die Daten in Braze werden im Kundenprofil gespeichert.

{% alert tip %}
Braze kann die Daten von Nutzer:innen während ihrer gesamten Journey mit Ihnen verfolgen – von dem Zeitpunkt, an dem sie anonym sind, bis zu dem Zeitpunkt, an dem sie in Ihrer App angemeldet und bekannt sind. Für alle Ihre Nutzer:innen sollten Nutzer-IDs festgelegt werden, die in Braze `external_id`s heißen. Diese sollten sich nicht ändern und zugänglich sein, wenn Nutzer:innen die App öffnen, damit Sie sie über verschiedene Geräte und Plattformen hinweg verfolgen können. Lesen Sie den [Artikel zum Nutzer:innen-Lebenszyklus]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) für bewährte Verfahren.
{% endalert %}

![Braze importiert Backend-Datenquellen aus der API, Frontend-Datenquellen aus dem SDK, Data-Warehouse-Daten aus der Braze Cloud-Datenaufnahme und aus Partnerintegrationen. Diese Daten werden über die Braze-API exportiert.]({% image_buster /assets/img/getting-started/import-export.png %}){: style="display:block;margin:auto;" }

{% alert note %}
Diese personenbezogene Datenbank mit Nutzerprofilen ermöglicht eine interaktive Geschwindigkeit in Realtime. Braze berechnet Werte vor, wenn Daten eintreffen, und speichert die Ergebnisse in einem leichtgewichtigen Dokumentenformat, um schnell abrufbar zu sein. Und weil die Plattform von Anfang an so konzipiert wurde, ist sie ideal für die meisten Messaging-Anwendungsfälle – insbesondere in Kombination mit anderen Datenkonzepten wie Connected-Content, Produktkatalogen und verschachtelten Attributen.
{% endalert %}

### Aufschlüsselung der Datenquellen {#data-source-breakdown}

Braze setzt für verschiedene Features unterschiedliche Systeme zur Speicherung von Daten ein. Für die Datenverwaltung und Fehlerbehebung ist es wichtig zu verstehen, welche Features welche Datenquellen verwenden.

#### MongoDB-basierte Features {#mongodb-powered-features}
- Angepasste Events (verfolgt durch SDK und API)
- Angepasste Attribute
- Nutzerprofile
- Kauf-Events
- Die meisten Features der Segmentierung und des Targetings

#### Snowflake-basierte Features {#snowflake-powered-features}
- [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)
- [Vorhersagesuite]({{site.baseurl}}/user_guide/brazeai)
- [KI-personalisierte Artikelempfehlungen]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai)
- [Geschätzte tatsächliche Öffnungsrate]({{site.baseurl}}/user_guide/channels/email/reporting#estimated-real-open-rate) (verwendet keine angepassten Events)

{% alert important %}
**Überlegungen zur Datenlöschung:** Angepasste Events werden in MongoDB gespeichert und sind von den Snowflake-Daten getrennt. Wenn Sie fehlerhafte Daten angepasster Events entfernen müssen, müssen Sie dies in MongoDB vornehmen. Snowflake-basierte Features (wie SQL-Segmenterweiterungen und andere Snowflake-basierte Features) verwenden Daten aus Snowflake, die separat verarbeitet werden. Das Löschen von Daten aus einem System führt nicht automatisch zum Löschen dieser Daten aus dem anderen System.
{% endalert %}

### Backend-Datenquellen über die Braze-API {#backend-data-sources-through-the-braze-api}
Braze kann über unsere [REST API]({{site.baseurl}}/api/endpoints/user_data) Daten aus Nutzer:innen-Datenbanken, Offline-Transaktionen und Data Warehouses abrufen.

### Frontend-Datenquellen über das Braze SDK {#frontend-data-sources-through-braze-sdk}
Braze erfasst über das [Braze SDK]({{site.baseurl}}/user_guide/get_started/sdk_overview) automatisch First-Party-Daten aus Frontend-Datenquellen, z. B. aus Nutzergeräten. Das SDK behandelt neue (anonyme) Nutzer:innen und verwaltet die Daten ihres Nutzerprofils während ihres gesamten Lebenszyklus.

### Partnerintegrationen {#partner-integrations}
Braze hat über 150 Technologie-Partner, die wir „Alloys“ nennen. Sie können Ihre Daten-Feeds durch ein sinnvolles, robustes Netzwerk [interoperabler Technologien und Daten-APIs]({{site.baseurl}}/partners/home) ergänzen.

### Direkte Warehouse-Anbindung über Braze Cloud-Datenaufnahme {#direct-warehouse-connection-through-braze-cloud-data-ingestion}
Sie können Kundendaten von Ihrem Data Warehouse über [Braze Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) in wenigen Minuten in die Plattform streamen und so relevante Nutzerattribute, Events und Käufe synchronisieren. Die Cloud-Datenaufnahme-Integration unterstützt komplexe Datenstrukturen, einschließlich verschachtelter JSON und Arrays von Objekten.

Cloud-Datenaufnahme kann Daten von Snowflake, Amazon Redshift, Databricks und Google BigQuery synchronisieren.

## Klassifizierung {#classification}
Die Klassifizierungsschicht ermöglicht es Ihrem Team, Zielgruppen, sogenannte [Segmente]({{site.baseurl}}/user_guide/audience/segments), auf der Grundlage von Daten, die Braze durchlaufen, dynamisch zu klassifizieren und aufzubauen.

{% alert note %}
Die Klassifizierung, Orchestrierung und Personalisierung sind die Ebenen, auf denen Ihr Marketing-Team einen Großteil seiner Arbeit erledigen wird. Die Schnittstelle zu diesen Ebenen erfolgt meist über das Braze-Dashboard, unsere Weboberfläche. Entwickler:innen spielen eine Rolle beim Einrichten und Anpassen dieser Ebenen.
{% endalert %}

Viele gängige Arten von Nutzerattributen wie Name, E-Mail, Geburtsdatum, Land und andere werden vom SDK standardmäßig automatisch getrackt. Als Entwickler:in arbeiten Sie mit Ihrem Team zusammen, um zu definieren, welche zusätzlichen, angepassten Daten für Ihren Anwendungsfall sinnvoll zu tracken sind. Ihre angepassten Daten haben Einfluss darauf, wie Ihre Nutzerbasis klassifiziert und segmentiert wird. Sie werden dieses Datenmodell während des Implementierungsprozesses einrichten.

Erfahren Sie mehr über [automatisch erfasste Daten und angepasste Daten]({{site.baseurl}}/developer_guide/analytics).

## Orchestrierung {#orchestration}
Die Orchestrierungsschicht erlaubt es Ihrem Marketing-Team, Nutzer-Journeys auf der Grundlage Ihrer Nutzerdaten und des früheren Engagements zu gestalten. Diese Arbeit wird hauptsächlich über unsere Dashboard-Oberfläche erledigt, aber Sie haben auch die Möglichkeit, [Campaigns über die API]({{site.baseurl}}/api/api_campaigns) zu starten. Sie können Braze beispielsweise über Ihr Backend mitteilen, wann die Nachrichten und Campaigns, die Ihre Marketer im Dashboard entworfen haben, versendet werden sollen, und sie gemäß Ihrer Backend-Logik triggern. Ein Beispiel für eine API-getriggerte Nachricht könnte das Zurücksetzen von Passwörtern oder Versandbestätigungen sein.

{% alert note %}
API-getriggerte Campaigns sind ideal für erweiterte transaktionale Anwendungsfälle. Sie erlauben Marketern die Verwaltung von Campaign-Texten, multivariaten Tests und Wiederzulassungsregeln im Braze-Dashboard und triggern gleichzeitig die Zustellung dieser Inhalte von Ihren Servern und Systemen. Die API-Anfrage zum Triggern der Nachricht kann auch zusätzliche Daten enthalten, die in Realtime in die Nachricht eingefügt werden.
{% endalert %}


### Feature-Flags {#feature-flags}
Braze ermöglicht Ihnen, Funktionen für eine Auswahl von Nutzer:innen über [Feature-Flags]({{site.baseurl}}/developer_guide/feature_flags) aus der Ferne zu aktivieren oder zu deaktivieren. So können Ihre Marketer mit Messaging für Features, die Sie noch nicht für die gesamte Zielgruppe eingeführt haben, das richtige Segment Ihrer Nutzerbasis ansprechen. Darüber hinaus können Feature-Flags dazu verwendet werden, ein Feature in der Produktion ein- und auszuschalten, ohne zusätzliche Code-Bereitstellung oder Updates im App Store. So können Sie neue Features sicher und zuverlässig einführen.

## Personalisierung {#personalization}
Die Personalisierungsebene bietet Ihnen die Möglichkeit, dynamische Inhalte in Ihren Nachrichten zuzustellen. Durch den Einsatz von Liquid, einer weit verbreiteten Sprache für die Personalisierung, kann Ihr Team dynamisch auf vorhandene Daten zurückgreifen, um die auf jede Empfänger:in zugeschnittene Nachricht anzuzeigen. Darüber hinaus können Sie mithilfe von [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) beliebige Informationen, die auf Ihrem Webserver oder über eine API verfügbar sind, direkt in die von Ihnen versendeten Nachrichten, wie Push-Benachrichtigungen oder E-Mails, einfügen. Connected-Content baut auf Liquid auf und verwendet eine vertraute Syntax.

Und da dieser dynamische Content programmierbar ist, können Marketer berechnete Werte, Antworten aus anderen Aufrufen oder Artikel aus dem Produktkatalog einbeziehen. Nachdem Sie diese Systeme während der Implementierung eingerichtet haben, kann Ihr Marketing-Team dies mit wenig bis gar keiner Unterstützung durch technische Teams tun.

## Aktion {#action}
Die Aktionsschicht ermöglicht das eigentliche Messaging an Ihre Nutzer:innen. Der Zweck der Aktionsschicht ist es, die richtige Nachricht zum richtigen Zeitpunkt an die richtigen Nutzer:innen zu senden, und zwar auf der Grundlage der Daten, die über alle zuvor besprochenen Schichten verfügbar sind. Die Nachrichtenübermittlung erfolgt innerhalb Ihrer App oder Website (z. B. durch das Versenden von In-App-Nachrichten oder durch grafische Elemente wie Content-Card-Karusselle und Banner) oder außerhalb Ihres App-Erlebnisses (z. B. durch das Versenden von Push-Benachrichtigungen oder E-Mails).

### Messaging-Kanäle {#messaging-channels}
Braze wurde entwickelt, um mit seinem kanalagnostischen, nutzerzentrierten Datenmodell eine sich entwickelnde technologische Landschaft zu bewältigen. Das Dashboard verwaltet die Zustellung von Nachrichten und die Auslöser für Transaktionen. So können Ihre Marketer beispielsweise eine SMS-Nachricht triggern, die einen Gutschein für einen Ihrer neu eröffneten Standorte anbietet, wenn Nutzer:innen den Geofence in der Nähe dieses Standorts betreten, oder Nutzer:innen eine E-Mail schicken, um sie über die neue Staffel ihrer Lieblingssendung zu informieren.

Das [Braze SDK]({{site.baseurl}}/user_guide/get_started/sdk_overview) ermöglicht zusätzliche Messaging-Kanäle: Push, In-App-Nachrichten und Content Cards. Sie integrieren das SDK in Ihre App oder Website, damit Ihr Marketing-Team das Braze-Dashboard nutzen kann, um seine Campaigns über alle unterstützten Messaging-Kanäle zu koordinieren.

![Diagramm der über das SDK verfügbaren Braze-Messaging-Kanäle.]({% image_buster /assets/img/getting_started/channels.png %})

## Daten exportieren {#exporting-data}
Entscheidend ist, dass alle Interaktionen von Endnutzer:innen mit Braze erfasst werden, sodass Sie Ihr Engagement und Ihre Reichweite messen können. Nachdem Braze Ihre Daten aus all diesen Quellen aggregiert hat, können diese mithilfe verschiedener Tools zurück in Ihren Technologie-Stack exportiert werden, um den Kreislauf zu schließen.

### Currents
[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) ist ein optionales Braze-Add-on, das einen granularen Streaming-Export bietet, der kontinuierlich andere Ziele in Ihrem Stack speist. Currents ist ein Roh-Daten-Feed pro Nutzer:in und Event, der Daten alle fünf Minuten oder alle 15.000 Events exportiert – je nachdem, was zuerst eintritt. Beispiele für nachgelagerte Ziele für Currents sind unter anderem Segment, S3, Redshift und Mixpanel.

### Snowflake Data Sharing {#snowflake-data-sharing}
Die Funktion [Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) von Snowflake ermöglicht es Braze, Ihnen sicheren Zugriff auf Daten in unserem Snowflake-Portal zu gewähren – ohne sich Gedanken über Reibungsverluste im Workflow, Fehlerquellen und unnötige Kosten machen zu müssen, die bei typischen Datenanbieterbeziehungen auftreten. Der gesamte Datenaustausch erfolgt über die einzigartige Dienstschicht und den Metadatenspeicher von Snowflake: Es werden keine Daten tatsächlich zwischen Konten kopiert oder übertragen. Dies ist ein wichtiges Konzept, da gemeinsam genutzte Daten keinen Speicherplatz in einem Verbraucher:innenkonto beanspruchen und daher nicht zu Ihren monatlichen Datenspeicherkosten beitragen. Die einzigen Kosten für Verbraucher:innen entstehen durch die Rechenressourcen (d. h. virtuelle Warehouses), die zum Abfragen der gemeinsam genutzten Daten verwendet werden.

### Braze-Export-APIs {#braze-export-apis}
Die Braze-API stellt [Endpunkte]({{site.baseurl}}/api/endpoints/export) bereit, mit denen Sie aggregierte Analytics-Daten programmatisch exportieren sowie individuelle Nutzerdaten exportieren können. Diese Daten können für Zielgruppen und Segments jeder Größe exportiert werden.

### CSVs {#csvs}
Zu guter Letzt gibt es die Möglichkeit, Ihre aggregierten Daten direkt aus dem Dashboard als [CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data) herunterzuladen. Die CSV-Option ermöglicht es Ihren Teammitgliedern, Daten ganz einfach aus Braze zu exportieren.

{% alert tip %}
Während der CSV-Export ein Basislimit von 500.000 Zeilen hat, unterliegen die APIs in dieser Hinsicht keiner Begrenzung.
{% endalert %}

## Alles zusammenführen {#putting-it-all-together}
Eine Ihrer Nutzer:innen, nennen wir sie Mel, hat gerade Ihre Produktankündigung erhalten. Hinter den Kulissen haben alle Ebenen der Braze-Plattform zusammengearbeitet, um sicherzustellen, dass dieser Prozess reibungslos ablief.

Mels Informationen wurden über einen CSV-Import von Ihrer bisherigen Customer-Engagement-Plattform in Braze übertragen. Jedes Mal, wenn Mel nach der Integration mit Ihrer App interagierte, wurden weitere Daten zu ihrem Kundenprofil hinzugefügt.

Ihre Produktankündigung wurde an alle Kund:innen gesendet, die einen ähnlichen Artikel in Ihrer App mit „Gefällt mir“ markiert hatten. Sie haben diese Daten als angepasstes Event definiert. Das SDK hat dieses Event erfasst und Ihre Nutzerbasis entsprechend segmentiert. Braze hat den besten Zeitpunkt für den Versand dieser Ankündigung orchestriert und die Ankündigung personalisiert, indem Mel mit ihrem bevorzugten Namen angesprochen wurde.

Als Mel die Ankündigung öffnet, fügt sie Ihr neues Produkt zu ihrer Wunschliste hinzu. Braze erfasst automatisch, dass sie auf die E-Mail geklickt hat. Das SDK erfasst, dass sie Ihr neues Produkt auf die Wunschliste gesetzt hat. Jedes Mal, wenn sie mit Ihrer Marke interagieren, erfahren Sie und Ihre Nutzer:innen mehr voneinander.

![Diagramm, das zeigt, wie Braze Nutzeraktionen über verschiedene Messaging-Kanäle hinweg erfasst.]({% image_buster /assets/img/getting-started/putting-it-all-together.png %})