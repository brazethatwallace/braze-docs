---
nav_title: Erweiterung der Ereignisweiterleitung
article_title: Adobe
description: "Dieser Referenzartikel behandelt die Braze-Erweiterung zur Ereignisweiterleitung, mit der Sie die im Adobe Experience Platform Edge Network erfassten Daten nutzen und sie in Form von serverseitigen Ereignissen an Braze senden können."
page_type: partner
page_order: 2
search_tag: Partner
---

# Track Events API – Erweiterung der Ereignisweiterleitung {#track-events-api-event-forwarding-extension}

> Die Braze Track Events API – [Ereignisweiterleitungserweiterung](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en) – ermöglicht es Ihnen, Daten zu nutzen, die im Adobe Experience Platform Edge Network erfasst wurden, und sie in Form von serverseitigen Ereignissen über die [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-API an Braze zu senden.

Dieses Dokument beschreibt die Anwendungsfälle der Erweiterung, wie Sie sie in Ihren Bibliotheken für die Ereignisweiterleitung installieren und wie Sie ihre Funktionen in einer [Regel](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) für die Ereignisweiterleitung einsetzen.

{% alert note %}
Die Verwendung von Adobe Event Forwarding kann Ihre Braze-Datenpunkt-Nutzung erhöhen. Weitere Informationen finden Sie in der Braze-Dokumentation zu [Datenpunkten]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#billable-data-points).
{% endalert %}

## Anwendungsfälle {#use-cases}

Diese Erweiterung sollte Daten aus dem Edge Network in Braze nutzen, um dessen Kundenanalyse- und Targeting-Funktionen zu verwenden.

Betrachten Sie zum Beispiel ein Einzelhandelsunternehmen mit einer Multichannel-Präsenz (Website und Mobilgeräte), das transaktionale oder konversationelle Eingaben als Event-Daten von seinen Website- und mobilen Plattformen erfasst.

Mithilfe verschiedener [Tag](https://experienceleague.adobe.com/docs/experience-platform/tags/home.html?lang=en)-Regeln werden diese Daten in Realtime an das Edge Network gesendet. Von hier aus sendet die Braze-Event-Forwarding-Erweiterung automatisch relevante Events serverseitig an Braze.

## Rate-Limits

| API | Rate-Limits |
| --- | --- |
| User Track | 50.000 Anfragen pro Minute.<br><br>Weitere Informationen finden Sie in der [User Track API-Dokumentation]({{site.baseurl}}/api/endpoints/user_data/post_user_track#rate-limit).
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rate-Limits" }

## Integration

### Schritt 1: Erforderliche Konfigurationsdetails sammeln {#step-1-gather-required-configuration-details}

Um das Edge Network mit Braze zu verbinden, benötigen Sie Folgendes:

| Schlüssel-Typ | Beschreibung |
| --- | --- |
| Braze-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze-Onboarding-Manager:in oder auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics#endpoints). |
| Braze-Representational State Transfer-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit allen Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 1: Erforderliche Konfigurationsdetails sammeln" }

### Schritt 2: Ein Secret erstellen {#step-2-create-a-secret}

Erstellen Sie ein neues [Ereignisweiterleitungs-Secret](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/secrets.html?lang=en) und setzen Sie den Wert auf Ihren [Braze-API-Schlüssel](https://experienceleague.adobe.com/docs/experience-platform/tags/extensions/server/braze/overview.html?lang=en#configuration-details). Dies wird verwendet, um die Verbindung zu Ihrem Konto zu authentifizieren und den Wert sicher zu halten.

### Schritt 3: Die Braze-Erweiterung installieren und konfigurieren {#step-3-install-and-configure-the-braze-extension}

1. Um die Erweiterung zu installieren, [erstellen Sie eine Eigenschaft für die Ereignisweiterleitung](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en#properties) oder wählen Sie stattdessen eine vorhandene Eigenschaft zur Bearbeitung aus.
2. Wählen Sie dann in der linken Navigation **Extensions** aus. Wählen Sie im Tab **Catalog** die Option **Install** auf der Karte für die Braze-Erweiterung aus.
3. Geben Sie auf dem nächsten Bildschirm Ihre Representational State Transfer-Instanz und Ihren API-Schlüssel ein und wählen Sie anschließend **Save**.

### Schritt 4: Eine Regel zum Senden von Ereignissen erstellen {#step-4-create-a-send-event-rule}

Nachdem Sie die Erweiterung installiert haben, erstellen Sie eine neue [Regel](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) für die Ereignisweiterleitung und konfigurieren Sie die Bedingungen wie gewünscht. Wenn Sie die Aktionen für die Regel konfigurieren, wählen Sie die **Braze**-Erweiterung aus und wählen Sie dann **Send Event** als Aktionstyp.

![Konfigurierte Adobe-Ereignisweiterleitungsregel-Aktion mit Braze Send Event.]({% image_buster /assets/img/efe.png %})

{% tabs local %}
{% tab Nutzeridentifikation %}

| Eingabe | Beschreibung |
| --- | --- |
| Externe Nutzer-ID | Eine lange, zufällige und gut verteilte UUID oder GUID. Wenn Sie eine andere Methode zur Benennung Ihrer Nutzer-IDs wählen, müssen diese ebenfalls lang, zufällig und gut verteilt sein. Erfahren Sie mehr über die [vorgeschlagene Namenskonvention für Nutzer-IDs]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web#naming-best-practices). |
| Braze-Nutzer-ID | Braze-Nutzerbezeichner. |
| Nutzer-Alias | Ein Alias dient als alternativer eindeutiger Bezeichner für Nutzer:innen. Verwenden Sie Aliase, um Nutzer:innen anhand anderer Dimensionen als Ihrer zentralen Nutzer-ID zu identifizieren.<br><br>Das Nutzer-Alias-Objekt besteht aus zwei Teilen: einem `alias_name` für den Bezeichner selbst und einem `alias_label`, der den Typ des Alias angibt. Nutzer:innen können mehrere Aliase mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 4: Eine Regel zum Senden von Ereignissen erstellen" }

{% alert note %}
Um das Ereignis mit einer Nutzer:in zu verknüpfen, müssen Sie entweder das Feld `External User ID`, das Feld `Braze User Identifier` oder den Abschnitt `User Alias` ausfüllen.
{% endalert %}

{% endtab %}
{% tab Event-Daten %}

| Eingabe | Beschreibung | Erforderlich |
| --- | --- | --- |
| Event-Name | Name des Events. | Ja |
| Event-Zeitpunkt | Datum und Uhrzeit als String im ISO-8601-Format oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. | Ja |
| App-Bezeichner | Der App-Bezeichner oder `app_id` ist ein Parameter, der eine Aktivität mit einer bestimmten App in Ihrem Workspace verknüpft. Er gibt an, mit welcher App innerhalb des Workspace Sie interagieren. | Nein |
| Event-Eigenschaften | Ein JSON-Objekt mit angepassten Eigenschaften des Events. | Nein |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 4: Eine Regel zum Senden von Ereignissen erstellen" }

{% alert note %}
Für die Aktion **Braze Send Event** müssen nur ein **Event Name** und eine **Event Time** angegeben werden, aber Sie sollten so viele Informationen wie möglich in das Feld für angepasste Eigenschaften eingeben. Weitere Details finden Sie unter [Event-Objekt]({{site.baseurl}}/api/objects_filters/event_object).
{% endalert %}

{% endtab %}
{% tab Nutzerattribut %}

Nutzerattribute können ein JSON-Objekt sein, das Felder enthält, mit denen ein Attribut mit dem angegebenen Namen und Wert für das angegebene Kundenprofil or Nutzerprofil erstellt oder aktualisiert wird. Die folgenden Eigenschaften werden unterstützt:

| Nutzerattribut | Beschreibung |
| --- | --- |
| Vorname | Vorname der Nutzer:in. |
| Nachname | Nachname der Nutzer:in. |
| Telefon | Telefonnummer der Nutzer:in. |
| E-Mail | E-Mail-Adresse der Nutzer:in. |
| Geschlecht | Einer der folgenden Strings: „M“, „F“, „O“ (andere), „N“ (nicht zutreffend), „P“ (lieber nicht sagen). |
| Ort | Der Ort der Nutzer:in. |
| Land | Das Land der Nutzer:in als String im Format [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Sprache | Die Sprache der Nutzer:in als String im Format [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Geburtsdatum | Das Geburtsdatum der Nutzer:in als String im Format „JJJJ-MM-TT“ (z. B. 1980-12-21). |
| Zeitzone | Name der Zeitzone aus der [IANA-Zeitzonendatenbank](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (z. B. 'America/New_York' oder 'Eastern Time (US & Canada)'). |
| Facebook | Ein Hash mit einem der folgenden Werte: `id` (String), `likes` (String-Array), `num_friends` (Ganzzahl). |
| Twitter | Hash mit einer der folgenden Angaben: id (Ganzzahl), `screen_name` (String, X (ehemals Twitter) Handle), `followers_count` (Ganzzahl), `friends_count` (Ganzzahl), `statuses_count` (Ganzzahl). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 4: Eine Regel zum Senden von Ereignissen erstellen" }

{% alert note %}
Alle in der Konfiguration hinzugefügten Attribute werden jedes Mal gesendet, wenn das Ereignis an Braze gesendet wird, unabhängig davon, ob sich der Wert des Attributs geändert hat. Wenn Sie Nutzerattribute konfigurieren, stellen Sie sicher, dass Sie wissen, wie sich dies auf Ihre Datenpunkt-Nutzung auswirkt.
{% endalert %}

{% endtab %}
{% endtabs %}

### Schritt 5: Eine Regel zum Senden eines Kauf-Events erstellen {#step-5-create-a-send-purchase-event-rule}

Nachdem Sie die Erweiterung installiert haben, erstellen Sie eine neue [Regel](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) für die Ereignisweiterleitung und konfigurieren Sie die Bedingungen wie gewünscht. Wenn Sie die Aktionen für die Regel konfigurieren, wählen Sie die **Braze**-Erweiterung aus und wählen Sie dann **Send Purchase Event** als Aktionstyp.

![Konfigurierte Adobe-Ereignisweiterleitungsregel-Aktion mit Braze Send Purchase Event.]({% image_buster /assets/img/efe2.png %})

{% tabs local %}
{% tab Nutzeridentifikation %}

| Eingabe | Beschreibung |
| --- | --- |
| Externe Nutzer-ID | Eine lange, zufällige und gut verteilte UUID oder GUID. Wenn Sie eine andere Methode zur Benennung Ihrer Nutzer-IDs wählen, müssen diese ebenfalls lang, zufällig und gut verteilt sein. Erfahren Sie mehr über die [vorgeschlagene Namenskonvention für Nutzer-IDs]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web#naming-best-practices). |
| Braze-Nutzer-ID | Braze-Nutzerbezeichner. |
| Nutzer-Alias | Ein Alias dient als alternativer eindeutiger Bezeichner für Nutzer:innen. Verwenden Sie Aliase, um Nutzer:innen anhand anderer Dimensionen als Ihrer zentralen Nutzer-ID zu identifizieren.<br><br>Das Nutzer-Alias-Objekt besteht aus zwei Teilen: einem `alias_name` für den Bezeichner selbst und einem `alias_label`, der den Typ des Alias angibt. Nutzer:innen können mehrere Aliase mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 5: Eine Regel zum Senden eines Kauf-Events erstellen" }

{% alert note %}
Um das Ereignis mit einer Nutzer:in zu verknüpfen, müssen Sie entweder das Feld `External User ID`, das Feld `Braze User Identifier` oder den Abschnitt `User Alias` ausfüllen.
{% endalert %}

{% endtab %}
{% tab Kaufdaten %}

| Eingabe | Beschreibung | Erforderlich |
| --- | --- | --- |
| Produkt-ID | Bezeichner für den Kauf (z. B. Produktname oder Produktkategorie). | Ja |
| Kaufzeitpunkt | Datum und Uhrzeit als String im ISO-8601-Format oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. | Ja |
| Währung | Währung als String im alphabetischen Währungscode-Format nach [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217). | Ja |
| Preis | Der Preis des Objekts. | Ja |
| Menge | Die gekaufte Menge. Wenn nicht angegeben, ist der Standardwert 1. Der Höchstwert muss kleiner als 100 sein. | Nein |
| App-Bezeichner | Der App-Bezeichner oder `app_id` ist ein Parameter, der eine Aktivität mit einer bestimmten App in Ihrem Workspace verknüpft. Er gibt an, mit welcher App innerhalb des Workspace Sie interagieren. | Nein |
| Kauf-Details | Ein JSON-Objekt mit angepassten Eigenschaften des Kaufs. | Nein |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 5: Eine Regel zum Senden eines Kauf-Events erstellen" }

{% alert note %}
Für die Aktion **Send Purchase Event** müssen nur `Product ID`, `Purchase Time`, `Currency` und `Price` angegeben werden, aber Sie sollten so viele Informationen wie möglich in das Feld für Kauf-Details eingeben. Weitere Details finden Sie unter [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object).
{% endalert %}

{% endtab %}
{% tab Nutzerattribute %}

In der Konfigurationsansicht können Sie wählen, ob Attribute mit jedem Ereignis gesendet werden sollen.

Nutzerattribute können ein JSON-Objekt sein, das Felder enthält, mit denen ein Attribut mit dem angegebenen Namen und Wert für das angegebene Kundenprofil or Nutzerprofil erstellt oder aktualisiert wird. Die folgenden Eigenschaften werden unterstützt:

| Nutzerattribut | Beschreibung |
| --- | --- |
| Vorname | Vorname der Nutzer:in. |
| Nachname | Nachname der Nutzer:in. |
| Telefon | Telefonnummer der Nutzer:in. |
| E-Mail | E-Mail-Adresse der Nutzer:in. |
| Geschlecht | Einer der folgenden Strings: „M“, „F“, „O“ (andere), „N“ (nicht zutreffend), „P“ (lieber nicht sagen). |
| Ort | Der Ort der Nutzer:in. |
| Land | Das Land der Nutzer:in als String im Format [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Sprache | Die Sprache der Nutzer:in als String im Format [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Geburtsdatum | Das Geburtsdatum der Nutzer:in als String im Format „JJJJ-MM-TT“ (z. B. 1980-12-21). |
| Zeitzone | Name der Zeitzone aus der [IANA-Zeitzonendatenbank](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (z. B. 'America/New_York' oder 'Eastern Time (US & Canada)'). |
| Facebook | Ein Hash mit einem der folgenden Werte: `id` (String), `likes` (String-Array), `num_friends` (Ganzzahl). |
| Twitter | Hash mit einer der folgenden Angaben: id (Ganzzahl), `screen_name` (String, X (ehemals Twitter) Handle), `followers_count` (Ganzzahl), `friends_count` (Ganzzahl), `statuses_count` (Ganzzahl). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 5: Eine Regel zum Senden eines Kauf-Events erstellen" }

{% alert note %}
Alle in der Konfiguration hinzugefügten Attribute werden jedes Mal gesendet, wenn das Ereignis an Braze gesendet wird, unabhängig davon, ob sich der Wert des Attributs geändert hat. Wenn Sie Nutzerattribute konfigurieren, stellen Sie sicher, dass Sie wissen, wie sich dies auf Ihre Datenpunkt-Nutzung auswirkt.
{% endalert %}

{% endtab %}
{% endtabs %}

### Schritt 6: Daten innerhalb von Braze validieren {#step-6-validate-data-within-braze}

Wenn die Ereignissammlung und die Adobe Experience Platform-Integration erfolgreich waren, sehen Sie die Ereignisse in der Braze-Konsole, wenn Sie [Nutzerprofile anzeigen]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles). Insbesondere werden die an Braze gesendeten neuen Ereignisdaten im Abschnitt **Käufe** oder **Angepasste Events** auf dem [Übersichts-Tab]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#overview-tab) einer bestimmten Nutzer:in angezeigt.