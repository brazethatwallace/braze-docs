---
nav_title: Talkable
article_title: Talkable
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Talkable, einer Empfehlungsmarketing-Plattform, die Marketing-E-Mail-Opt-ins aus Empfehlungskampagnen in Echtzeit mit Braze synchronisiert."
alias: /partners/talkable/
page_type: partner
search_tag: Partner
---

# Talkable

> [Talkable](https://www.talkable.com/) hilft Verbrauchermarken, zufriedene Kund:innen in einen skalierbaren Empfehlungskanal zu verwandeln. Mit der Braze-Integration fließen Marketing-E-Mail-Opt-ins, die in Talkable-Empfehlungskampagnen erfasst werden, in Echtzeit in Braze, sodass Ihr Team die Einwilligung, den Kontext und die Kampagnendaten erhält, die Sie benötigen, um jede:n neue:n Fürsprecher:in und Freund:in willkommen zu heißen, zu segmentieren und anzusprechen.

_Diese Integration wird von Talkable gepflegt._

## Über die Integration {#about-the-integration}

Talkable bringt die von Fürsprecher:innen gesteuerte Akquise in die Customer Journey ein, die Braze unterstützt. Die Integration überträgt jedes von Talkable erfasste Empfehlungs-Opt-in in Realtime an das passende Braze-Profil, sodass Willkommens-Flows, Empfehlungs-Journeys, Segmentierung und Lifecycle-Messaging auf Basis vertrauenswürdiger Einwilligung und Empfehlungskontext gestartet werden können – ganz ohne manuelle Listenexporte oder Batch-Synchronisierungen.

Talkable erfasst Marketing-Opt-ins in zwei Szenarien:

* **Registrierung als Fürsprecher:in:** Eine Fürsprecherin oder ein Fürsprecher meldet sich für eine Talkable-Empfehlungskampagne an und stimmt dem Erhalt von Marketing-E-Mails zu.
* **E-Mail-Gating für Freund:innen:** Eine eingeladene Person durchläuft den E-Mail-Gating-Schritt von Talkable und entscheidet sich für den Empfang von Marketing-E-Mails (Opt-in).

In beiden Fällen erstellt oder aktualisiert Talkable das passende Braze-Kundenprofil or Nutzerprofil in Realtime und setzt den E-Mail-Abo-Status der Nutzerin oder des Nutzers auf **Opted In**.

### Standardverhalten {#default-behavior}

Talkable sendet Daten nur dann an Braze, wenn ein konkretes Opt-in-Ereignis von einer Person vorliegt, die in Talkable ausdrücklich eingewilligt hat – entweder durch Registrierung als Fürsprecher:in für eine Kampagne oder durch Opt-in während des E-Mail-Gatings. Talkable führt keine nächtlichen Batches, vollständigen Synchronisierungen oder impliziten Profilaktualisierungen durch. Talkable sendet niemals Profile an Braze, die kein Opt-in erteilt haben.

## Anwendungsfälle {#use-cases}

- Trigger or triggern or triggern Sie ein Braze-Willkommens-Canvas, sobald sich ein:e Fürsprecher:in für eine Talkable-Empfehlungskampagne registriert.
- Aktivieren Sie geworbene Freund:innen mit einem freundespezifischen Canvas und einem personalisierten Erstkaufangebot, sobald ein:e Freund:in ein Opt-in erteilt.
- Segmentieren Sie nach Empfehlungskontext mithilfe von Fürsprecher:innen- und Freundesmarkierungen sowie Campaign-Metadaten, die als angepasste Braze-Attribute gesendet werden.
- Leiten Sie Empfehlungs-Opt-ins in eine festgelegte Braze-Abo-Gruppe weiter, um einen datenschutzkonformen Newsletterversand sicherzustellen.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
| --- | --- |
| Ein Talkable-Konto | Eine Talkable-Website mit mindestens einer konfigurierten Campaign ist erforderlich, um diese Partnerschaft nutzen zu können. |
| Ein Braze-Representational State Transfer-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit `users.track`-Berechtigungen. Erstellen Sie diesen Schlüssel im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. Weitere Informationen finden Sie unter [Representational State Transfer-API-Schlüssel erstellen]({{site.baseurl}}/api/basics#creating-rest-api-keys). |
| Ein Braze-Representational State Transfer-Endpunkt | Ihre Braze-Representational State Transfer-Endpunkt-URL (zum Beispiel `https://rest.iad-01.braze.com`). Sowohl US- (`.com`) als auch EU-Braze-Cluster (`.eu`) werden unterstützt. Weitere Informationen finden Sie unter [Representational State Transfer-API-Endpunkte]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Braze-App in Talkable installieren {#step-1-install-the-braze-app-in-talkable}

1. Melden Sie sich in Ihrem Talkable-Admin an, öffnen Sie das Menü und navigieren Sie zu **All Site Settings** > **App Store**.
2. Suchen Sie **Braze** und wählen Sie **Install**.
3. Geben Sie Ihren Braze-Representational State Transfer-Endpunkt und einen Representational State Transfer-API-Schlüssel mit `users.track`-Berechtigungen ein und wählen Sie **Save**.

### 2. Schritt: E-Mail-Opt-in-Aktion konfigurieren {#step-2-configure-the-email-opt-in-action}

1. Öffnen Sie in der Talkable-Braze-App die Aktion **Email opt-in**.
2. (Optional) Geben Sie einen Braze-Abo-Gruppen-Bezeichner ein, fügen Sie angepasste Attribute hinzu und/oder konfigurieren Sie einen Nutzer-Alias. Weitere Informationen finden Sie unter [Talkable anpassen](#customizing-talkable).
3. Wählen Sie **Save**. Lassen Sie die Aktion deaktiviert, damit Sie die Konfiguration mit einem Test-Payload überprüfen können, bevor Live-Opt-in-Ereignisse synchronisiert werden.

### 3. Schritt: Mit einem Beispiel-Payload testen {#step-3-test-with-a-sample-payload}

1. Wählen Sie in Talkable **Send sample payload** bei der Aktion **Email opt-in**, um eine Testanfrage an Braze zu senden.
2. Gehen Sie in Braze zu **Audience** > **User Search** und suchen Sie nach der Test-E-Mail-Adresse.
3. Bestätigen Sie, dass das Profil mit **Email Subscribe** auf **Opted In** gesetzt existiert und dass alle konfigurierten angepassten Attribute, Abo-Gruppen-Zuordnungen oder Nutzer-Aliase wie erwartet angezeigt werden.

### 4. Schritt: Aktion für Live-Traffic aktivieren {#step-4-enable-the-action-for-live-traffic}

Wenn das Testprofil in Braze korrekt aussieht, kehren Sie zu Talkable zurück und aktivieren Sie die Aktion **Email opt-in**.

Ab diesem Zeitpunkt synchronisiert jedes Talkable-Opt-in-Ereignis das passende Profil in Echtzeit mit Braze.

## Standardmäßig an Braze gesendete Nutzerattribute {#default-user-attributes-sent-to-braze}

Bei jedem Opt-in-Ereignis erstellt oder aktualisiert Talkable das zugehörige Braze-Kundenprofil or Nutzerprofil mit den folgenden Standard-Nutzerattributen von Braze. Leere Werte werden weggelassen.

| Braze-Attribut | Typ | Hinweise |
| --- | --- | --- |
| `email_subscribe` | String | Wird bei jedem Talkable-Opt-in-Ereignis auf **Opted In** gesetzt. |
| `email` | String | Primärer Bezeichner, der zum Abgleich mit dem Braze-Profil verwendet wird. |
| `phone` | String | Wird nur als Nutzerattribut erfasst. Braze erwartet das E.164-Format; der Wert wird so gesendet, wie er in Talkable gespeichert ist. |
| `first_name` | String | Der Vorname der Person. |
| `last_name` | String | Der Nachname der Person. |
| Abo-Gruppen-Registrierung | Nicht zutreffend | Talkable registriert die Nutzer:innen als abonniert, wenn eine Abo-Gruppe konfiguriert ist. |
| Nutzer-Alias | Nicht zutreffend | Wird nur hinzugefügt, wenn ein Nutzer-Alias konfiguriert ist. Weitere Informationen finden Sie unter [Talkable anpassen](#customizing-talkable). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Standardmäßig an Braze gesendete Nutzerattribute" }

## Talkable anpassen {#customize-talkable}

Die folgenden optionalen Anpassungen sind verfügbar. Konfigurieren Sie eine beliebige Kombination; sie sind unabhängig voneinander.

### Opt-ins in eine Braze-Abo-Gruppe aufnehmen {#enroll-opt-ins-in-a-braze-subscription-group}

1. Kopieren Sie in Braze eine Abo-Gruppen-ID unter **Zielgruppe** > **Abo-Gruppenverwaltung**. Weitere Informationen finden Sie unter [Nutzerabos verwalten]({{site.baseurl}}/user_guide/channels/email/subscriptions).
2. Fügen Sie die ID in der Talkable-Aktion **E-Mail-Opt-in** in das Feld **Subscription group identifier** ein.

Talkable nimmt jedes Opt-in als abonniert in diese Abo-Gruppe auf und beschränkt Empfehlungs-Opt-ins auf diese Gruppe statt auf ein globales Abo. Talkable fügt nur Abos hinzu und entfernt sie nie.

### Angepasste Attribute senden {#send-custom-attributes}

Fügen Sie im Payload-Editor der Aktion ein beliebiges Schlüssel-Wert-Paar hinzu. Der eingegebene Schlüssel wird zum Attributnamen im Braze-Kundenprofil or Nutzerprofil.

Werte werden als Liquid-Template verarbeitet. Folgende Variablen stehen zur Verfügung:

{% raw %}
| Variable | Inhalt |
| --- | --- |
| `{{ person }}` | Die:der Fürsprechende oder Freund:in, die:der sich angemeldet hat (`email`, `first_name`, `last_name`, `phone_number`, `username`, `is_advocate`, `custom_properties` und mehr). |
| `{{ ip }}` | Die IP-Adresse, von der aus das Opt-in erfolgte. |
| `{{ campaign }}` | Die ursprüngliche Talkable-Campaign (`name`, `type`, `tag_names` und mehr). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid-Template-Variablen" }
{% endraw %}

{% raw %}
Beispiel: Fügen Sie `talkable_is_advocate` = `{{ person.is_advocate }}` und `talkable_campaign_name` = `{{ campaign.name }}` hinzu, um in Braze nach Empfehlungskontext zu segmentieren.
{% endraw %}

### Nutzer:innen mit Braze-Nutzer-Aliassen identifizieren {#identify-users-with-braze-user-aliases}

Fügen Sie im Payload-Editor `user_alias.alias_name` (z. B. {% raw %}`{{ person.username }}`{% endraw %}) und `user_alias.alias_label` (z. B. `username`) hinzu. Weitere Informationen finden Sie unter [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object).

Wenn beide Felder vorhanden sind, identifiziert das System die:den Nutzer:in zusätzlich zur E-Mail über den Alias, und Braze erstellt ein neues Alias-Profil, falls keine Übereinstimmung gefunden wird.

{% alert note %}
Beide Alias-Felder sind erforderlich. Wenn nur eines der Felder `alias_name` oder `alias_label` gesetzt ist, sendet Talkable keinen Nutzer-Alias, und das Profil wird nur anhand der E-Mail zugeordnet.
{% endalert %}

## Nutzer:innen in Braze finden und erstellen {#find-and-create-users-in-braze}

* Standardmäßig gleicht Braze das Profil anhand der E-Mail-Adresse ab. Wenn kein übereinstimmendes Profil existiert, erstellt Braze ein neues.
* Wenn ein Nutzer-Alias konfiguriert ist, gleicht Braze auch anhand dieses Alias ab und erstellt ein neues Alias-Profil, falls keine Übereinstimmung gefunden wird.
* Externe IDs werden von dieser Integration nicht verwendet. Um Talkable-Opt-ins an ein bestehendes, extern identifiziertes Profil anzuhängen, konfigurieren Sie einen Nutzer-Alias, dessen Alias-Label mit dem bekannten Alias dieses Profils übereinstimmt.

## Talkable mit Braze verwenden {#use-talkable-with-braze}

### Synchronisierte:n Nutzer:in finden {#find-a-synced-user}

Gehen Sie zu **Audience** > **Nutzersuche** und suchen Sie nach E-Mail, um ein von Talkable erstelltes oder aktualisiertes Profil anzuzeigen.

Standardfelder (E-Mail, Telefonnummer, Vorname oder Nachname) und alle von Ihnen konfigurierten angepassten Attribute werden im Profil angezeigt; **Email Subscribe** zeigt **Opted In** an.

### Ein Empfehlungssegment erstellen {#build-a-referral-segment}

1. Erstellen Sie ein Segment, das nach **Email Subscribe** gleich **Opted In** gefiltert ist.
2. Verfeinern Sie es mit den von Talkable gesendeten angepassten Attributen – zum Beispiel `talkable_is_advocate` gleich `true`, um Fürsprecher:innen anzusprechen, oder `talkable_campaign_name` gleich Ihrer Campaign, um ein bestimmtes Empfehlungsprogramm anzusprechen.

### Lifecycle-Messaging Trigger or triggern or triggern {#trigger-lifecycle-messaging}

1. Erstellen Sie einen Canvas oder eine Campaign mit aktionsbasierter Zustellung. Die folgenden Braze-Trigger or triggern-Typen funktionieren mit dieser Integration:
* **Update or aktualisieren Subscription Status** (zum Beispiel, wenn das E-Mail-Abo **Opted In** wird)
* **Update or aktualisieren Subscription Group Status** (wenn eine Abo-Gruppe konfiguriert ist)
* **Change Custom Attribute Value** (für jedes angepasste Talkable-Attribut, das Sie senden).
2. Personalisieren Sie Nachrichten mit den angepassten Talkable-Attributen im Profil (Campaign-Name, Belohnungswert, Empfehler:in usw.).

## Überlegungen {#considerations}

* **Nur E-Mail-Opt-in:** Telefonnummern werden als Standard-Nutzerattribut erfasst, aber die Integration legt keinen Kurzmitteilungsdienst or SMS-Abo-Status fest. Talkable synchronisiert keine Kurzmitteilungsdienst or SMS-Opt-ins.
* **Telefonnummernformat:** Braze erwartet Telefonnummern im internationalen Format (E.164).
* **Realtime-Synchronisierung, ereignisgesteuert:** Talkable sendet pro Opt-in-Ereignis eine Anfrage (eine Nutzer:in pro Anfrage). Es gibt keine Bündelung und keine periodische Vollsynchronisierung; das Volumen entspricht Ihrem Empfehlungs-Opt-in-Volumen.
* **Zuverlässige Zustellung:** Wenn Braze vorübergehend einen Fehler zurückgibt, führt Talkable automatisch einen Retry durch. Bei persistenten Fehlern wird eine E-Mail-Benachrichtigung an die Administrator:in der Website gesendet.

## Fehlerbehebung {#troubleshooting}

| Fehler | Wahrscheinliche Ursache | Lösung |
| --- | --- | --- |
| 401 Unauthorized | Der Representational State Transfer-API-Schlüssel verfügt nicht über die Berechtigung `users.track`, oder der Endpunkt zeigt auf den falschen Cluster. | Erstellen Sie den Schlüssel mit der Berechtigung `users.track` neu und bestätigen Sie, dass der Representational State Transfer-Endpunkt zu Ihrem Braze-Cluster passt. |
| Representational State Transfer-Endpunkt wird bei der Installation abgelehnt | Die URL ist kein Braze-Representational State Transfer-Endpunkt. | Verwenden Sie den Representational State Transfer-Endpunkt Ihres Clusters, zum Beispiel `https://rest.iad-01.braze.com`. Eine Dashboard-URL funktioniert nicht. |
| Profil erstellt, aber nicht in einer Abo-Gruppe | Keine Abo-Gruppen-ID konfiguriert. | Geben Sie die Abo-Gruppen-ID in der Aktion **Email opt-in** ein. |
| Nutzer-Alias wird nicht angewendet | Nur eines der beiden Alias-Felder (Name oder Label) ist ausgefüllt. | Füllen Sie beide Felder in der Aktion aus: Alias-Name und Alias-Label. |
| Profil wird nicht angezeigt | Es wurde noch keine Beispielanfrage gesendet, oder die Aktion ist deaktiviert. | Wählen Sie **Send sample payload** in Talkable und stellen Sie sicher, dass die Aktion **Email opt-in** aktiviert ist. |
| Anfragen werden nach einer Schlüsselrotation nicht mehr gesendet | Der gespeicherte API-Schlüssel wurde in Braze widerrufen oder ersetzt. | Öffnen Sie im Talkable **App Store** die Braze-App, fügen Sie den neuen Representational State Transfer-API-Schlüssel ein und wählen Sie **Save**; testen Sie erneut mit **Send sample payload**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehlerbehebung" }

Weitere Informationen zur Talkable-Integration finden Sie in der [Talkable-Braze-Integrationsdokumentation](https://docs.talkable.com/email_marketing_and_automation/braze/). Um den Talkable-Support zu kontaktieren, senden Sie eine E-Mail an [support@talkable.com](mailto:support@talkable.com).