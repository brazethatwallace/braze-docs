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

Talkable bringt die von Fürsprecher:innen gesteuerte Akquise in die Customer Journey, die Braze antreibt. Die Integration überträgt jedes Empfehlungs-Opt-in, das Talkable erfasst, in Echtzeit in das passende Braze-Profil, sodass Willkommens-Flows, Empfehlungs-Journeys, Segmentierung und Lifecycle-Messaging auf Basis vertrauenswürdiger Einwilligungen und Empfehlungskontexte gestartet werden können – ganz ohne manuelle Listenexporte oder Batch-Synchronisierungen.

Talkable erfasst Marketing-Opt-ins in zwei Szenarien:

* **Registrierung als Fürsprecher:in:** Eine Person registriert sich für eine Talkable-Empfehlungskampagne und stimmt dem Erhalt von Marketing-E-Mails zu.
* **E-Mail-Gating für Freund:innen:** Eine empfohlene Person schließt den E-Mail-Gating-Schritt von Talkable ab und stimmt dem Erhalt von Marketing-E-Mails zu.

In beiden Fällen erstellt oder aktualisiert Talkable das passende Braze-Nutzerprofil in Echtzeit und setzt den E-Mail-Abo-Status auf **Opted In**.

### Standardverhalten {#default-behavior}

Talkable sendet Daten nur bei einem diskreten Opt-in-Ereignis an Braze – von einer Person, die in Talkable ausdrücklich zugestimmt hat, entweder als Fürsprecher:in bei der Kampagnenregistrierung oder als Freund:in beim E-Mail-Gating-Opt-in. Talkable führt keine nächtlichen Batches, vollständigen Synchronisierungen oder impliziten Profilaktualisierungen durch. Talkable sendet niemals Profile an Braze, die kein Opt-in gegeben haben.

## Anwendungsfälle {#use-cases}

- Lösen Sie einen Braze-Willkommens-Canvas aus, sobald sich eine Person für eine Talkable-Empfehlungskampagne registriert.
- Aktivieren Sie empfohlene Freund:innen mit einem spezifischen Canvas und einem personalisierten Erstkaufangebot, sobald eine empfohlene Person ein Opt-in gibt.
- Segmentieren Sie nach Empfehlungskontext mithilfe von Fürsprecher:innen- und Freund:innen-Flags sowie Kampagnen-Metadaten, die als angepasste Braze-Attribute gesendet werden.
- Leiten Sie Empfehlungs-Opt-ins in eine bestimmte Braze-Abo-Gruppe für Compliance-konformen Newsletter-Versand weiter.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
| --- | --- |
| Ein Talkable-Konto | Eine Talkable-Website mit mindestens einer konfigurierten Kampagne ist erforderlich, um diese Partnerschaft zu nutzen. |
| Ein Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit `users.track`-Berechtigungen. Erstellen Sie diesen Schlüssel im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. Weitere Informationen finden Sie unter [REST-API-Schlüssel erstellen]({{site.baseurl}}/api/basics/#creating-rest-api-keys). |
| Ein Braze-REST-Endpunkt | Ihre Braze-REST-Endpunkt-URL (zum Beispiel `https://rest.iad-01.braze.com`). Sowohl US- (`.com`) als auch EU-Braze-Cluster (`.eu`) werden unterstützt. Weitere Informationen finden Sie unter [REST-API-Endpunkte]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Braze-App in Talkable installieren {#step-1-install-the-braze-app-in-talkable}

1. Melden Sie sich in Ihrem Talkable-Admin an, öffnen Sie das Menü und navigieren Sie zu **All Site Settings** > **App Store**.
2. Suchen Sie **Braze** und wählen Sie **Install**.
3. Geben Sie Ihren Braze-REST-Endpunkt und einen REST-API-Schlüssel mit `users.track`-Berechtigungen ein und wählen Sie **Save**.

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

## Standard-Nutzerattribute, die an Braze gesendet werden {#default-user-attributes-sent-to-braze}

Bei jedem Opt-in-Ereignis erstellt oder aktualisiert Talkable das passende Braze-Nutzerprofil mit den folgenden Standard-Braze-Nutzerattributen. Leere Werte werden ausgelassen.

| Braze-Attribut | Typ | Hinweise |
| --- | --- | --- |
| `email_subscribe` | String | Wird bei jedem Talkable-Opt-in-Ereignis auf **Opted In** gesetzt. |
| `email` | String | Primärer Bezeichner zum Abgleich des Braze-Profils. |
| `phone` | String | Wird nur als Nutzerattribut erfasst. Braze erwartet das E.164-Format; wird so gesendet, wie in Talkable gespeichert. |
| `first_name` | String | Der Vorname der Person. |
| `last_name` | String | Der Nachname der Person. |
| Abo-Gruppen-Zuordnung | Nicht zutreffend | Wird nur hinzugefügt, wenn eine Abo-Gruppe konfiguriert ist. Die Person wird als abonniert eingetragen. |
| Nutzer-Alias | Nicht zutreffend | Wird nur hinzugefügt, wenn ein Nutzer-Alias konfiguriert ist. Weitere Informationen finden Sie unter [Talkable anpassen](#customizing-talkable). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Standard-Nutzerattribute, die an Braze gesendet werden" }

## Talkable anpassen {#customize-talkable}

Die folgenden optionalen Anpassungen sind verfügbar. Konfigurieren Sie eine beliebige Kombination; sie sind unabhängig voneinander.

### Opt-ins in eine Braze-Abo-Gruppe aufnehmen {#enroll-opt-ins-in-a-braze-subscription-group}

1. Kopieren Sie in Braze eine Abo-Gruppen-ID unter **Audience** > **Subscription Group Management**. Weitere Informationen finden Sie unter [Nutzer-Abos verwalten]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/).
2. Fügen Sie die ID in der Talkable-Aktion **Email opt-in** in das Feld **Subscription group identifier** ein.

Talkable trägt jedes Opt-in als abonniert in diese Abo-Gruppe ein und beschränkt Empfehlungs-Opt-ins auf diese Gruppe statt auf ein globales Abo. Talkable fügt nur Abos hinzu; es entfernt niemals welche.

### Angepasste Attribute senden {#send-custom-attributes}

Fügen Sie im Payload-Editor der Aktion ein beliebiges Schlüssel-Wert-Paar hinzu. Der eingegebene Schlüssel wird zum Attributnamen im Braze-Nutzerprofil.

Werte werden als Liquid-Templates verarbeitet. Die folgenden Variablen stehen zur Verfügung:

{% raw %}
| Variable | Inhalt |
| --- | --- |
| `{{ person }}` | Die Person (Fürsprecher:in oder Freund:in), die das Opt-in gegeben hat (`email`, `first_name`, `last_name`, `phone_number`, `username`, `is_advocate`, `custom_properties` und mehr). |
| `{{ ip }}` | Die IP-Adresse, von der das Opt-in erfolgte. |
| `{{ campaign }}` | Die ursprüngliche Talkable-Kampagne (`name`, `type`, `tag_names` und mehr). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid-Template-Variablen" }
{% endraw %}

{% raw %}
Beispiel: Fügen Sie `talkable_is_advocate` = `{{ person.is_advocate }}` und `talkable_campaign_name` = `{{ campaign.name }}` hinzu, um in Braze nach Empfehlungskontext zu segmentieren.
{% endraw %}

### Nutzer:innen mit Braze-Nutzer-Aliasen identifizieren {#identify-users-with-braze-user-aliases}

Fügen Sie im Payload-Editor `user_alias.alias_name` (zum Beispiel {% raw %}`{{ person.username }}`{% endraw %}) und `user_alias.alias_label` (zum Beispiel `username`) hinzu. Weitere Informationen finden Sie unter [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/).

Wenn beide Felder vorhanden sind, identifiziert das System die Person zusätzlich zur E-Mail über den Alias, und Braze erstellt ein neues Alias-Profil, wenn keine Übereinstimmung gefunden wird.

{% alert note %}
Beide Alias-Felder sind erforderlich. Wenn nur eines der Felder `alias_name` oder `alias_label` gesetzt ist, sendet Talkable keinen Nutzer-Alias und das Profil wird nur per E-Mail abgeglichen.
{% endalert %}

## Nutzer:innen in Braze finden und erstellen {#find-and-create-users-in-braze}

* Standardmäßig gleicht Braze das Profil anhand der E-Mail-Adresse ab. Wenn kein passendes Profil existiert, erstellt Braze ein neues.
* Wenn ein Nutzer-Alias konfiguriert ist, gleicht Braze auch über diesen Alias ab und erstellt ein neues Alias-Profil, wenn keine Übereinstimmung gefunden wird.
* Externe IDs werden von dieser Integration nicht verwendet. Um Talkable-Opt-ins an ein bestehendes extern identifiziertes Profil anzuhängen, konfigurieren Sie einen Nutzer-Alias, dessen Label mit dem bekannten Alias dieses Profils übereinstimmt.

## Talkable mit Braze verwenden {#use-talkable-with-braze}

### Synchronisierte:n Nutzer:in finden {#find-a-synced-user}

Gehen Sie zu **Audience** > **User Search** und suchen Sie per E-Mail, um ein von Talkable erstelltes oder aktualisiertes Profil anzuzeigen.

Standardfelder (E-Mail, Telefon, Vorname oder Nachname) und alle konfigurierten angepassten Attribute werden im Profil angezeigt; **Email Subscribe** zeigt **Opted In**.

### Empfehlungs-Segment erstellen {#build-a-referral-segment}

1. Erstellen Sie ein Segment, das nach **Email Subscribe** gleich **Opted In** gefiltert ist.
2. Verfeinern Sie mit den angepassten Attributen, die Talkable sendet – zum Beispiel `talkable_is_advocate` gleich `true`, um Fürsprecher:innen anzusprechen, oder `talkable_campaign_name` gleich Ihrem Kampagnennamen, um ein bestimmtes Empfehlungsprogramm anzusprechen.

### Lifecycle-Messaging auslösen {#trigger-lifecycle-messaging}

1. Erstellen Sie einen Canvas oder eine Campaign mit aktionsbasierter Zustellung. Die folgenden Braze-Trigger-Typen funktionieren mit dieser Integration:
* **Update Subscription Status** (zum Beispiel E-Mail-Abo wird **Opted In**)
* **Update Subscription Group Status** (wenn eine Abo-Gruppe konfiguriert ist)
* **Change Custom Attribute Value** (für jedes angepasste Talkable-Attribut, das Sie senden).
2. Personalisieren Sie Nachrichten mit den angepassten Talkable-Attributen im Profil (Kampagnenname, Belohnungswert, Empfehlende:r usw.).

## Hinweise {#considerations}

* **Nur E-Mail-Opt-in:** Telefonnummern werden als Standard-Nutzerattribut erfasst, aber die Integration setzt keinen SMS-Abo-Status. Talkable synchronisiert keine SMS-Opt-ins.
* **Telefonformat:** Braze erwartet Telefonnummern im internationalen Format (E.164).
* **Realtime-ereignisgesteuerte Synchronisierung:** Talkable sendet eine Anfrage pro Opt-in-Ereignis (eine Person pro Anfrage). Es gibt kein Batching und keine periodische vollständige Synchronisierung; das Volumen entspricht Ihrem Empfehlungs-Opt-in-Volumen.
* **Zuverlässige Zustellung:** Wenn Braze vorübergehend einen Fehler zurückgibt, wiederholt Talkable den Versuch automatisch. Bei persistenten Fehlern wird eine E-Mail-Benachrichtigung an die Administrator:innen der Website gesendet.

## Fehlerbehebung {#troubleshooting}

| Fehler | Wahrscheinliche Ursache | Lösung |
| --- | --- | --- |
| 401 Unauthorized | Der REST-API-Schlüssel hat keine `users.track`-Berechtigungen, oder der Endpunkt verweist auf den falschen Cluster. | Erstellen Sie den Schlüssel mit `users.track`-Berechtigungen neu und bestätigen Sie, dass der REST-Endpunkt mit Ihrem Braze-Cluster übereinstimmt. |
| REST-Endpunkt bei der Installation abgelehnt | Die URL ist kein Braze-REST-Endpunkt. | Verwenden Sie den REST-Endpunkt Ihres Clusters, zum Beispiel `https://rest.iad-01.braze.com`. Eine Dashboard-URL funktioniert nicht. |
| Profil erstellt, aber nicht in einer Abo-Gruppe | Keine Abo-Gruppen-ID konfiguriert. | Geben Sie die Abo-Gruppen-ID bei der Aktion **Email opt-in** ein. |
| Nutzer-Alias nicht angewendet | Nur eines der beiden Alias-Felder (Name oder Label) ist ausgefüllt. | Geben Sie beide Felder bei der Aktion ein: Alias-Name und Alias-Label. |
| Profil wird nicht angezeigt | Beispielanfrage noch nicht gesendet oder die Aktion ist deaktiviert. | Wählen Sie **Send sample payload** in Talkable und stellen Sie sicher, dass die Aktion **Email opt-in** aktiviert ist. |
| Anfragen werden nach einer Schlüsselrotation nicht mehr gesendet | Der gespeicherte API-Schlüssel wurde in Braze widerrufen oder ersetzt. | Öffnen Sie im Talkable **App Store** die Braze-App, fügen Sie den neuen REST-API-Schlüssel ein und wählen Sie **Save**; testen Sie erneut mit **Send sample payload**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehlerbehebung" }

Weitere Informationen zur Talkable-Integration finden Sie in der [Talkable-Braze-Integrationsdokumentation](https://docs.talkable.com/email_marketing_and_automation/braze/). Um den Talkable-Support zu kontaktieren, senden Sie eine E-Mail an [support@talkable.com](mailto:support@talkable.com).