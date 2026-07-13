---
nav_title: Daten zwischen Workspaces migrieren
article_title: Daten zwischen Workspaces und Instanzen migrieren
page_order: 1
page_type: reference
description: "Erfahren Sie, wie Workspace-Daten isoliert sind, was Braze zwischen Workspaces kopieren oder importieren kann und wie Sie Umzüge zwischen Staging-, Produktions- oder separaten Dashboard-Umgebungen planen."
---

# Daten zwischen Workspaces und Instanzen migrieren {#migrate-data-between-workspaces-and-instances}

> Workspaces halten Ihre Braze-Daten getrennt. Diese Seite erklärt, wie sich diese Isolation auf die Migration auswirkt, was Sie mit Produktfeatures und APIs verschieben können und was Sie außerhalb von Braze neu aufbauen oder handhaben müssen. Eine Migration ist in der Regel eine bereichsübergreifende Aufgabe – nicht nur eine Aufgabe für Unternehmensadministrator:innen. Administrator:innen sind oft für die Workspace-Einrichtung und Kanalkonfiguration zuständig; Entwickler:innen kümmern sich um SDK- und API-Änderungen; Marketer bauen Segmente neu auf und übernehmen Messaging-Inhalte. Jeder Schritt erfordert die entsprechenden [Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) im Quell- und Ziel-Workspace.

Alles, was Sie in Braze speichern – Nutzerprofile, Segmente, Messaging-Inhalte und Engagement-Verlauf – befindet sich innerhalb eines Workspace. Ein Segment, eine Campaign oder ein Canvas kann keine Daten aus einem anderen Workspace lesen oder darauf abzielen. Dashboard-Nutzer:innen verwenden häufig mehrere Workspaces auf demselben Unternehmens-Dashboard für Staging und Produktion, für verschiedene Marken oder für regionale Aufteilungen. Dieses Setup bietet Ihnen Isolation, bedeutet aber auch, dass es keine einzelne Aktion im Dashboard gibt, die alle Workspace-Daten in einen anderen Workspace oder eine andere Braze-Instanz verschiebt.

Für den Planungskontext siehe [Erste Schritte: Workspaces]({{site.baseurl}}/user_guide/get_started/workspaces) und [Workspaces erstellen und verwalten]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces).

## Was Braze nicht automatisch zwischen Workspaces migriert {#what-braze-does-not-automatically-migrate-between-workspaces}

Folgendes wird nicht automatisch migriert, wenn Sie SDKs oder APIs auf einen neuen Workspace (oder eine neue Braze-Dashboard-Umgebung mit eigenen Workspaces) ausrichten:

| Bereich | Verhalten |
| --- | --- |
| **Nutzerprofile** | Profile werden nicht als Paket übertragen. Erstellen oder importieren Sie Nutzer:innen im Ziel-Workspace neu (siehe [Nutzerprofildaten](#user-profile-data)). |
| **Segmente und Filter** | Segmentdefinitionen verbleiben im Quell-Workspace. Bauen Sie Segmente im Ziel-Workspace mit derselben Logik neu auf, wo dies möglich ist. |
| **Messaging-Verlauf** | Der Campaign- und Canvas-Empfangsverlauf eines Profils ist an den Quell-Workspace gebunden. Er erscheint nicht auf einem neuen Profil in einem anderen Workspace, es sei denn, Sie modellieren ihn selbst (z. B. über angepasste Attribute), wie in den [Braze-Onboarding-FAQs]({{site.baseurl}}/user_guide/onboarding_faq) beschrieben. |
| **Kanalspezifische Konfiguration** | Versanddomains, SMS-Abos, WhatsApp-Nummern und ähnliche Einstellungen sind Workspace-bezogen. Konfigurieren Sie sie im Ziel-Workspace neu, wo zutreffend. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Was Braze nicht automatisch zwischen Workspaces migriert" }

{% alert important %}
Wenn Sie separate Workspaces für Staging und Produktion verwenden, denken Sie daran, dass [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)-Konnektoren nicht zwischen Workspaces geteilt werden. Planen Sie, welcher Workspace die Produktionsexporte besitzt. Weitere Details finden Sie unter [Erste Schritte: Workspaces]({{site.baseurl}}/user_guide/get_started/workspaces#currents-connectors).
{% endalert %}

## Was Sie verschieben oder neu erstellen können {#what-you-can-move-or-recreate}

### Campaign-, Canvas- und Landing-Page-Inhalte {#campaign-canvas-and-landing-page-content}

Sie können viele Campaign-, Canvas- und Landing-Page-Definitionen als Entwürfe in einen anderen Workspace kopieren. Unterstützte Kanäle, ausgelassene Felder und Liquid-Einschränkungen sind in [Campaigns, Canvases und Landing-Pages zwischen Workspaces kopieren]({{site.baseurl}}/user_guide/messaging/governance/copy_across_workspaces) dokumentiert. Aktualisieren Sie nach dem Kopieren Segmente, Trigger und alle Workspace-spezifischen Referenzen, bevor Sie starten oder veröffentlichen.

### Nutzerprofildaten {#user-profile-data}

Typische Ansätze:

- **REST API:** Verwenden Sie [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), um Nutzer:innen im Ziel-Workspace mit den benötigten Bezeichnern und Attributen zu erstellen oder zu aktualisieren. Dies ist dasselbe Muster, das für die [Migration von Legacy-Nutzerdaten]({{site.baseurl}}/developer_guide/getting_started/integration_overview#migrating-legacy-user-data) beim Einbringen historischer Daten in Braze beschrieben wird.
- **CSV-Import:** Für Marketer-gesteuerte Importe siehe [Nutzer:innen importieren]({{site.baseurl}}/user_guide/audience/manage_audience/import_users) und [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).
- **Cloud-Datenaufnahme:** Um Attribute aus einem Warehouse in den Ziel-Workspace zu synchronisieren, siehe [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).
- **Exporte aus dem Quell-Workspace:** Verwenden Sie [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) oder [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment), um Daten zu extrahieren, die Sie verschieben dürfen, und ordnen Sie sie dann `users/track` oder CSV für das Ziel zu. Beachten Sie Ihre Datenaufbewahrungs-, Datenschutz- und vertraglichen Verpflichtungen beim Exportieren und erneuten Laden von Daten.

{% alert note %}
Das Zusammenführen doppelter Profile mit dem Endpunkt [Nutzer:innen zusammenführen]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) oder [doppelte Nutzer:innen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users) im Dashboard gilt innerhalb eines einzelnen Workspace, nicht über zwei Workspaces hinweg.
{% endalert %}

### Nutzerexportfelder, die nicht auf Standard-Profil-APIs abgebildet werden können {#user-export-fields-that-dont-map-to-standard-profile-apis}

Wenn Sie Nutzer:innen in einem Ziel-Workspace aus einem [Nutzerexport]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) neu aufbauen, können einige Exportfelder nicht über die REST API oder CSV in die Standard-Profilfelder von Braze zurückgeschrieben werden (so wie das SDK und der Server sie befüllen). Sie können die Werte oft stattdessen als angepasste Attribute speichern. Beachten Sie die folgenden Einschränkungen.

#### Geräteinformationen (`devices`) {#device-information-devices}

Gerätedatensätze im Export werden vom SDK befüllt. Sie können diese Daten nicht über die REST API in die Standard-Gerätefelder von Braze migrieren.

Wenn Sie diese Informationen benötigen, bevor Nutzer:innen eine Sitzung in einer App starten, die auf den Ziel-Workspace ausgerichtet ist, senden Sie sie als angepasste Attribute, wenn Sie die Nutzer:innen importieren. Standard-Segmentierungsfilter und Liquid-Referenzen, die auf integrierten Gerätedaten basieren, verwenden die exportierten Gerätedaten erst, wenn Nutzer:innen eine Sitzung in einer App-Instanz öffnen, die mit dem neuen Workspace verbunden ist (wenn das SDK die Standard-Gerätefelder aktualisiert).

{% alert note %}
Dies ist getrennt von der [Push-Token-Migration](#push-tokens), die das Feld `push_tokens` auf [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) verwendet.
{% endalert %}

#### Gesamtsitzungen und App-bezogene Sitzungsdaten (`apps` und verschachtelte `sessions`) {#total-sessions-and-per-app-session-data-apps-and-nested-sessions}

Sitzungssummen und verschachtelte Sitzungsdaten aus dem `apps`-Objekt in einem Export können nicht in dieselben integrierten Felder reimportiert werden. Um Legacy-Zähler zu erhalten (z. B. Gesamtsitzungen aus dem Quell-Workspace), speichern Sie sie in angepassten Attributen und segmentieren Sie im Ziel-Workspace nach diesen Feldern.

Sie können `date_of_first_session` und `date_of_last_session` über [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) oder CSV-Import setzen. Für akzeptierte Formate siehe das [Nutzerattribut-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) und [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).

#### Zufällige Bucket-Nummer (`random_bucket`) {#random-bucket-random_bucket}

Jede:r Nutzer:in erhält in ihrem Workspace eine [zufällige Bucket-Nummer]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-update-events). Dieser Wert kann nicht reimportiert werden; Nutzer:innen erhalten eine neue zufällige Bucket-Nummer im Ziel-Workspace.

Wenn Sie sich auf die alte Nummer für Holdouts oder Stichproben verlassen (z. B. Ausschluss von Nutzer:innen, deren `random_bucket` unter einem Schwellenwert liegt), speichern Sie den exportierten Wert als angepasstes Attribut und erstellen Sie Segmente oder Filter auf diesem Attribut anstelle des integrierten Felds für die zufällige Bucket-Nummer.

#### Partner-Attributionsfelder (`attributed_*`) {#partner-attribution-fields-attributed_}

Attributionsfelder aus Partnerintegrationen (die `attributed_*`-Felder in einem Export) können nicht über die REST API auf die Standard-Attributionsfelder von Braze gesetzt werden. Ordnen Sie sie angepassten Attributen im Ziel-Workspace zu, wenn Sie sie für Segmentierung oder Messaging benötigen.

### Push-Token {#push-tokens}

Wenn Nutzer:innen bereits Push-Token von einem früheren Anbieter oder einer früheren App-Version haben, können Sie Token für mobile Apps über die API importieren oder sich nach der Integration auf das SDK verlassen. Web-Push-Token haben API-Einschränkungen. Vollständige Details und Beispiele finden Sie unter [Push-Token migrieren]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens).

### WhatsApp

Telefonnummern und Abo-Gruppen können mit einem speziellen Übertragungsablauf zwischen Workspaces verschoben werden. Siehe [WhatsApp-Telefonnummern und Abo-Gruppen zwischen Workspaces übertragen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/transfer_between_workspaces).

### Engagement- und Analytics-Daten außerhalb von Braze {#engagement-and-analytics-data-outside-braze}

Wenn Sie bei der Konsolidierung von Umgebungen einen historischen Datensatz von Sendungen, Öffnungen oder Klicks benötigen, sind [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) und andere Exporte der unterstützte Weg, diese Daten in Ihr Warehouse oder Ihre Tools zu übertragen. Diese Daten werden nicht als native nutzerbezogene Nachrichtenhistorie in einem anderen Workspace wieder in Braze aufgenommen.

## Bevor Sie SDK- oder API-Schlüssel ändern {#before-you-change-sdk-or-api-keys}

Wenn Sie Ihre App oder Website auf einen neuen Workspace ausgerichtet haben:

- Nutzer:innen, die die App oder Website öffnen, können neue Profile im neuen Workspace erstellen. Sie übernehmen nicht automatisch den vorherigen Workspace-spezifischen Verlauf.
- Wenn dieselbe Person in beiden Workspaces existieren könnte, können [duplikatähnliche Szenarien]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces#should-i-create-a-new-workspace-when-im-releasing-an-updated-app) auftreten (z. B. überlappende Push-Reichweite). Bevorzugen Sie einen bewussten Daten- und Targeting-Plan gegenüber dem unbeabsichtigten Teilen von Produktions- und Staging-Schlüsseln.

{% alert tip %}
Für Workspace- oder App-Instanz-Löschungslimits, spezielle Kontoumzüge oder die Planung umfangreicher Migrationen [kontaktieren Sie den Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) mit Ihren Dashboard-Links und einer Zusammenfassung der Quell- und Ziel-Workspaces.
{% endalert %}