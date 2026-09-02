---
nav_title: "API-Bezeichnertypen"
article_title: "API-Bezeichnertypen"
page_order: 2.2
toc_headers: h2
description: "Dieser Referenzartikel behandelt die verschiedenen Arten von API-Bezeichnern, die im Braze-Dashboard vorhanden sind, wo Sie sie finden können und wofür sie verwendet werden."
page_type: reference
---

# API-Bezeichnertypen {#api-identifier-types}

> Dieser Referenzleitfaden behandelt die verschiedenen Arten von API-Bezeichnern, die im Braze-Dashboard zu finden sind, ihren Zweck, wo Sie sie finden und wie sie typischerweise verwendet werden. Informationen zu Representational State Transfer-API-Schlüsseln oder Workspace-API-Schlüsseln finden Sie in der [API-Übersicht]({{site.baseurl}}/api/basics).

Die folgenden Bezeichner können verwendet werden, um über die externe API von Braze auf Ihr Template, Ihr Canvas, Ihre Campaign oder Ihr Segment zuzugreifen. Alle Nachrichten sollten in [UTF-8](https://en.wikipedia.org/wiki/UTF-8) kodiert sein.

## App-Bezeichner {#app-identifier}

Der App-Bezeichner oder `app_id` ist ein Parameter, der Aktivitäten einer bestimmten App in Ihrem Workspace zuordnet. Er gibt an, mit welcher App innerhalb des Workspace Sie interagieren. So haben Sie beispielsweise eine `app_id` für Ihre iOS-App, eine `app_id` für Ihre Android-App und eine `app_id` für Ihre Internet-Integration. Bei Braze kann es vorkommen, dass Sie mehrere Apps für dieselbe Plattform über die verschiedenen von Braze unterstützten Plattformtypen hinweg haben.

### Wo finde ich ihn? {#where-can-i-find-it}

Es gibt zwei Möglichkeiten, Ihre `app_id` zu finden:

{% tabs local %}
{% tab App-Bezeichner %}
Gehen Sie zu **Einstellungen** > **APIs und Bezeichner** > **App-Bezeichner**. Ihr API-Schlüssel für jede App ist in der Spalte **Bezeichner** aufgeführt.
{% endtab %}

{% tab App-Einstellungen %}
Gehen Sie zu **Einstellungen** > **App-Einstellungen**. Ihr API-Schlüssel wird neben dem Feld **API Key** im Einstellungsbereich angezeigt.

{% endtab %}
{% endtabs %}

### Wofür kann er verwendet werden? {#what-can-it-be-used-for}

App-Bezeichner werden bei Braze bei der Integration des SDK or Software-Development-Kit verwendet und dienen außerdem dazu, in Representational State Transfer API-Aufrufen auf eine bestimmte App zu verweisen. Mit der `app_id` können Sie viele Dinge tun, zum Beispiel Daten für ein angepasstes Event abrufen, das in einer bestimmten App aufgetreten ist, Deinstallationsstatistiken, Statistiken zu neuen Nutzer:innen, täglich aktive:r Nutzer:in; täglich aktiv-Statistiken und Statistiken zu Sitzungsstarts für eine bestimmte App abrufen.

{% alert tip %}
Manchmal werden Sie aufgefordert, eine `app_id` anzugeben, obwohl Sie nicht mit einer App arbeiten, da es sich um ein veraltetes Feld handelt, das spezifisch für eine bestimmte Plattform ist. In diesem Fall können Sie dieses Feld weglassen, indem Sie eine beliebige Zeichenkette als Platzhalter für diesen erforderlichen Parameter einfügen.
{% endalert %}

### Mehrere App-Bezeichner {#multiple-app-identifiers}

Bei der SDK or Software-Development-Kit-Einrichtung besteht der häufigste Anwendungsfall für mehrere App-Bezeichner darin, diese Bezeichner für Debug- und Release-Build-Varianten zu trennen.

Um in Ihren Builds einfach zwischen mehreren App-Bezeichnern zu wechseln, empfehlen wir, für jede relevante [Build-Variante](https://developer.android.com/studio/build/build-variants.html) eine separate `braze.xml`-Datei zu erstellen. Eine Build-Variante ist eine Kombination aus Build-Typ und Produktvariante. Standardmäßig wird ein neues Android-Projekt mit den Build-Typen `debug` und `release` und ohne Produktvarianten konfiguriert.

Erstellen Sie für jede relevante Build-Variante eine neue `braze.xml` in `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">{YOUR_BUILD_VARIANT_API_KEY}</string>
</resources>
```
Wenn die Build-Variante kompiliert wird, verwendet sie den neuen Bezeichner.

## Template-Bezeichner {#template-identifier}

Ein [Template]({{site.baseurl}}/api/endpoints/templates)-Bezeichner oder eine Template-ID ist ein zufällig generierter Schlüssel, den Braze für ein bestimmtes Template innerhalb des Dashboards erstellt. Template-IDs sind für jedes Template eindeutig und können verwendet werden, um Templates über die API zu referenzieren.

Templates sind ideal, wenn Ihr Unternehmen das HTML-Design für Campaigns extern erstellen lässt. Nachdem die Templates erstellt wurden, haben Sie ein Template, das nicht an eine bestimmte Campaign gebunden ist, sondern auf eine Reihe von Campaigns angewendet werden kann, wie z. B. einen Newsletter.

### Wo finde ich ihn?

Sie können Ihren Template-Bezeichner auf zwei Arten finden:

{% tabs local %}
{% tab Templates %}
Gehen Sie zu **Templates**, wählen Sie eine Template-Seite aus und wählen Sie dann ein bereits vorhandenes Template. Wenn das gewünschte Template noch nicht existiert, erstellen Sie eines und speichern Sie es. Unten auf der jeweiligen Template-Seite finden Sie Ihren Template-Bezeichner.
{% endtab %}

{% tab API-Schlüssel %}
Gehen Sie zu **Einstellungen** > **APIs und Bezeichner**. Hier bietet Braze eine Suche unter **Zusätzliche API-Bezeichner** an, mit der Sie nach bestimmten Bezeichnern suchen können.

{% endtab %}
{% endtabs %}

### Wofür kann er verwendet werden?

- Templates über die API Update or aktualisieren or aktualisieren
- Informationen zu einem bestimmten Template abrufen

## Canvas-Bezeichner {#canvas-identifier}

Ein [Canvas]({{site.baseurl}}/user_guide/messaging/canvas)-Bezeichner oder eine Canvas-ID ist ein zufälliger Schlüssel, der von Braze für ein bestimmtes Canvas im Dashboard generiert wird. Canvas-IDs sind für jedes Canvas eindeutig und können verwendet werden, um Canvase über die API zu referenzieren.

Beachten Sie, dass bei einem Canvas mit Varianten sowohl eine übergeordnete Canvas-ID als auch einzelne Varianten-Canvas-IDs existieren, die unter dem Haupt-Canvas verschachtelt sind.

### Wo finde ich ihn?

Sie finden Ihren Canvas-Bezeichner im Dashboard. Gehen Sie zu **Messaging** > **Canvas** und wählen Sie ein bestehendes Canvas aus. Falls das gewünschte Canvas noch nicht existiert, erstellen Sie eines und speichern Sie es. Klicken Sie unten auf einer einzelnen Canvas-Seite auf **Analyze Variants**. Es erscheint ein Fenster mit dem Canvas-API-Bezeichner am unteren Rand.

### Wofür kann er verwendet werden?

- Analytics für eine bestimmte Nachricht verfolgen
- Übergeordnete, aggregierte Statistiken zur Canvas-Performance abrufen
- Details zu einem bestimmten Canvas abrufen
- Mit Currents Daten auf Nutzer:innenebene abrufen, um einen ganzheitlichen Ansatz für Canvase zu verfolgen
- Mit API-getriggerter Zustellung Statistiken für transaktionale Nachrichten erfassen

## Campaign-Bezeichner {#campaign-identifier}

Ein [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns)-Bezeichner oder eine Campaign-ID ist ein zufälliger Schlüssel, der von Braze für eine bestimmte Campaign im Dashboard generiert wird. Campaign-IDs sind für jede Campaign eindeutig und können verwendet werden, um Campaigns über die API zu referenzieren.

Beachten Sie: Wenn Sie eine Campaign mit Varianten haben, gibt es sowohl eine übergeordnete Campaign-ID als auch einzelne Varianten-Campaign-IDs, die unter der Haupt-Campaign verschachtelt sind.

### Wo finde ich den Bezeichner?

Sie können Ihre Campaign-ID auf zwei Arten finden:

{% tabs local %}
{% tab Campaigns %}
Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie eine bestehende Campaign aus. Falls die gewünschte Campaign noch nicht existiert, erstellen Sie eine und speichern Sie sie. Am Ende der einzelnen Campaign-Seite finden Sie Ihren **Campaign API Identifier**.

{% endtab %}

{% tab API-Schlüssel %}
Gehen Sie zu **Einstellungen** > **APIs und Bezeichner**. Hier bietet Braze eine Suche unter **Additional API Identifiers** an, mit der Sie nach bestimmten Bezeichnern suchen können.

{% endtab %}
{% endtabs %}

### Wofür kann er verwendet werden?

- Analytics für eine bestimmte Nachricht verfolgen
- Übergeordnete aggregierte Statistiken zur Campaign-Performance abrufen
- Details zu einer bestimmten Campaign abrufen
- Mit Currents Daten auf Nutzer:innen-Ebene für einen ganzheitlichen Ansatz bei Campaigns einbinden
- Mit API-getriggerter Zustellung Statistiken für transaktionale Nachrichten erfassen
- Um auf der **Campaigns**-Seite [nach einer bestimmten Campaign zu suchen]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/search_campaigns), indem Sie den Filter `api_id:YOUR_API_ID` verwenden

## Segment-Bezeichner {#segment-identifier}

Ein [Segment]({{site.baseurl}}/user_guide/audience/segments)-Bezeichner oder eine Segment-ID ist ein zufälliger Schlüssel, der von Braze für ein bestimmtes Segment innerhalb des Dashboards generiert wird. Segment-IDs sind für jedes Segment eindeutig und können verwendet werden, um Segments über die API zu referenzieren.

### Wo finde ich ihn?

Sie können Ihre Segment-ID auf zwei Arten finden:

{% tabs local %}
{% tab Segments %}
Gehen Sie zu **Zielgruppe** > **Segments** und wählen Sie ein bereits vorhandenes Segment aus. Falls das gewünschte Segment noch nicht existiert, erstellen Sie eines und speichern Sie es. Am Ende der individuellen Segment-Seite finden Sie Ihren Segment-Bezeichner.

{% endtab %}

{% tab API-Schlüssel %}
Gehen Sie zu **Einstellungen** > **APIs und Bezeichner**. Hier bietet Braze eine Suche unter **Zusätzliche API-Bezeichner** an, mit der Sie nach bestimmten Bezeichnern suchen können.

{% endtab %}
{% endtabs %}

### Wofür kann er verwendet werden?

- Details zu einem bestimmten Segment abrufen
- Analytics eines bestimmten Segments abrufen
- Ermitteln, wie oft ein angepasstes Event für ein bestimmtes Segment aufgezeichnet wurde
- Eine Campaign über die API an Mitglieder eines Segments spezifizieren und senden

## Sendebezeichner {#send-identifier}

Ein Sendebezeichner, oder eine Sende-ID, ist ein Schlüssel, der entweder von Braze generiert oder von Ihnen für einen bestimmten Nachrichtenversand erstellt wird und unter dem die Analytics verfolgt werden sollen. Der Sendebezeichner ermöglicht es Ihnen, Analytics für eine bestimmte Instanz eines Campaign-Versands über den [`/sends/data_series`-Endpunkt]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) abzurufen.

### Wo finde ich ihn?

API- und API-getriggerte Campaigns, die als Broadcast gesendet werden, generieren automatisch einen Sendebezeichner, wenn kein Sendebezeichner angegeben wird. Wenn Sie Ihren eigenen Sendebezeichner festlegen möchten, müssen Sie zunächst einen über den [`/sends/id/create`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids) erstellen. Der Bezeichner darf nur aus ASCII-Zeichen bestehen und maximal 64 Zeichen lang sein. Sie können einen Sendebezeichner über mehrere Sendungen derselben Campaign hinweg wiederverwenden, wenn Sie die Analytics dieser Sendungen zusammenfassen möchten.

### Wofür kann er verwendet werden?
Senden und Verfolgen der Nachrichten-Performance auf programmatischem Weg, ohne dass für jeden Versand eine Campaign erstellt werden muss.

## Abo-Gruppenbezeichner {#subscription-group-identifier}

Ein Abo-Gruppenbezeichner, oder Abo-Gruppen-ID, ist ein von Braze generierter Schlüssel für eine bestimmte Abo-Gruppe. IDs sind für jede Abo-Gruppe eindeutig und können verwendet werden, um Abo-Gruppen über die API zu referenzieren.

### Wo finde ich ihn?

Gehen Sie zu **Zielgruppe** > **Abos** und kopieren Sie die ID neben der jeweiligen Abo-Gruppe.

### Wofür kann er verwendet werden?

- Abo-Gruppen einer Nutzer:in auflisten
- Den Abo-Gruppenstatus einer Nutzer:in abrufen
- Den Abo-Gruppenstatus einer Nutzer:in Update or aktualisieren or aktualisieren