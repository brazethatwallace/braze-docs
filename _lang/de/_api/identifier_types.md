---
nav_title: "API-Bezeichnertypen"
article_title: "API-Bezeichnertypen"
page_order: 2.2
toc_headers: h2
description: "Dieser Referenzartikel behandelt die verschiedenen Arten von API-Bezeichnern, die im Braze-Dashboard vorhanden sind, wo Sie sie finden können und wofür sie verwendet werden."
page_type: reference

---

# API-Bezeichnertypen {#api-identifier-types}

> Dieser Referenzleitfaden behandelt die verschiedenen Arten von API-Bezeichnern, die im Braze-Dashboard zu finden sind, ihren Zweck, wo Sie sie finden und wie sie typischerweise verwendet werden. Informationen zu REST-API-Schlüsseln oder Workspace-API-Schlüsseln finden Sie in der [API-Übersicht]({{site.baseurl}}/api/api_key).

Die folgenden Bezeichner können verwendet werden, um über die externe API von Braze auf Ihr Template, Ihr Canvas, Ihre Campaign oder Ihr Segment zuzugreifen. Alle Nachrichten sollten in [UTF-8](https://en.wikipedia.org/wiki/UTF-8) kodiert sein.

## App-Bezeichner {#app-identifier}

Der App-Bezeichner oder `app_id` ist ein Parameter, der eine Aktivität mit einer bestimmten App in Ihrem Workspace verknüpft. Er gibt an, mit welcher App innerhalb des Workspace Sie interagieren. Zum Beispiel haben Sie eine `app_id` für Ihre iOS-App, eine `app_id` für Ihre Android-App und eine `app_id` für Ihre Internet-Integration. Bei Braze kann es vorkommen, dass Sie mehrere Apps für dieselbe Plattform auf den verschiedenen von Braze unterstützten Plattformtypen haben.

### Wo kann ich ihn finden? {#where-can-i-find-it}

Es gibt zwei Möglichkeiten, Ihre `app_id` zu finden:

{% tabs local %}
{% tab App Identifiers %}
Gehen Sie zu **Einstellungen** > **APIs und Bezeichner** > **App-Bezeichner**. Ihr API-Schlüssel für jede App ist in der Spalte **Bezeichner** aufgeführt.
{% endtab %}

{% tab App Settings %}
Gehen Sie zu **Einstellungen** > **App Settings**. Ihr API-Schlüssel ist neben dem Feld **API-Schlüssel** im Bereich „Einstellungen“ aufgeführt.

{% endtab %}
{% endtabs %}

### Wofür kann er verwendet werden? {#what-can-it-be-used-for}

App-Bezeichner bei Braze werden bei der Integration des SDK verwendet und dienen auch dazu, eine bestimmte App in REST-API-Aufrufen zu referenzieren. Mit der `app_id` können Sie viele Dinge tun, z. B. Daten für ein angepasstes Event abrufen, das für eine bestimmte App aufgetreten ist, Deinstallationsstatistiken, Statistiken über neue Nutzer:innen, DAU-Statistiken und Statistiken über den Sitzungsbeginn für eine bestimmte App abrufen.

{% alert tip %}
Manchmal werden Sie zur Eingabe einer `app_id` aufgefordert, obwohl Sie nicht mit einer App arbeiten, da es sich um ein Legacy-Feld für eine bestimmte Plattform handelt. Sie können dieses Feld auslassen, indem Sie einen beliebigen String als Platzhalter für diesen erforderlichen Parameter einfügen.
{% endalert %}

### Mehrere App-Bezeichner {#multiple-app-identifiers}

Bei der Einrichtung des SDK ist der häufigste Anwendungsfall für mehrere App-Bezeichner die Trennung dieser Bezeichner für Debug- und Release-Build-Varianten.

Um einfach zwischen mehreren App-Bezeichnern in Ihren Builds zu wechseln, empfehlen wir, für jede relevante [Build-Variante](https://developer.android.com/studio/build/build-variants.html) eine eigene `braze.xml`-Datei zu erstellen. Eine Build-Variante ist eine Kombination aus Build-Typ und Produkt-Flavor. Standardmäßig wird ein neues Android-Projekt mit den Build-Typen `debug` und `release` und ohne Produkt-Flavors konfiguriert.

Erstellen Sie für jede relevante Build-Variante eine neue `braze.xml` in `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">{YOUR_BUILD_VARIANT_API_KEY}</string>
</resources>
```
Wenn die Build-Variante kompiliert wird, verwendet sie den neuen Bezeichner.

## Template-Bezeichner {#template-identifier}

Ein [Template]({{site.baseurl}}/api/endpoints/templates)-Bezeichner oder eine Template-ID ist ein zufälliger Schlüssel, der von Braze für ein bestimmtes Template innerhalb des Dashboards generiert wird. Template-IDs sind für jedes Template eindeutig und können verwendet werden, um Templates über die API zu referenzieren.

Templates sind ideal, wenn Ihr Unternehmen Ihre HTML-Designs für Campaigns in Auftrag gibt. Nach der Erstellung der Templates verfügen Sie über ein Template, das nicht speziell für eine Campaign, sondern für eine Reihe von Campaigns verwendet werden kann, z. B. einen Newsletter.

### Wo kann ich ihn finden?

Sie können Ihre Template-ID auf zwei Arten finden:

{% tabs local %}
{% tab Templates %}
Gehen Sie zu **Templates**, wählen Sie eine Template-Seite aus und wählen Sie dann ein bereits vorhandenes Template. Wenn das gewünschte Template noch nicht existiert, erstellen Sie eines und speichern Sie es. Unten auf der Seite des einzelnen Templates finden Sie Ihren Template-Bezeichner.
{% endtab %}

{% tab API Keys %}
Gehen Sie zu **Einstellungen** > **APIs und Bezeichner**. Hier bietet Braze eine Suche nach **zusätzlichen API-Bezeichnern** an, mit der Sie bestimmte Bezeichner nachschlagen können.

{% endtab %}
{% endtabs %}

### Wofür kann er verwendet werden?

- Templates über die API aktualisieren
- Informationen über ein bestimmtes Template abrufen

## Canvas-Bezeichner {#canvas-identifier}

Ein [Canvas]({{site.baseurl}}/user_guide/messaging/canvas)-Bezeichner oder eine Canvas-ID ist ein zufälliger Schlüssel, der von Braze für ein bestimmtes Canvas innerhalb des Dashboards generiert wird. Canvas-IDs sind für jedes Canvas eindeutig und können verwendet werden, um Canvases über die API zu referenzieren.

Beachten Sie, dass es bei einem Canvas mit Varianten sowohl eine übergeordnete Canvas-ID als auch individuelle Varianten-Canvas-IDs gibt, die unter dem Haupt-Canvas verschachtelt sind.

### Wo kann ich ihn finden?

Ihre Canvas-ID finden Sie im Dashboard. Gehen Sie zu **Messaging** > **Canvas** und wählen Sie ein bereits vorhandenes Canvas aus. Wenn das gewünschte Canvas noch nicht existiert, erstellen Sie es und speichern Sie es. Klicken Sie unten auf einer einzelnen Canvas-Seite auf **Analyze Variants**. Es erscheint ein Fenster mit dem Canvas-API-Bezeichner am unteren Rand.

### Wofür kann er verwendet werden?

- Analytics für eine bestimmte Nachricht verfolgen
- Aggregierte Statistiken zur Canvas-Performance auf hoher Ebene erfassen
- Details zu einem bestimmten Canvas abrufen
- Mit Currents Daten auf Nutzer:innen-Ebene für einen ganzheitlichen Ansatz bei Canvases einbringen
- Mit API-getriggerter Zustellung Statistiken für transaktionale Nachrichten erfassen

## Campaign-Bezeichner {#campaign-identifier}

Ein [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns)-Bezeichner oder eine Campaign-ID ist ein zufälliger Schlüssel, der von Braze für eine bestimmte Campaign innerhalb des Dashboards generiert wird. Campaign-IDs sind für jede Campaign eindeutig und können verwendet werden, um Campaigns über die API zu referenzieren.

Beachten Sie, dass es bei einer Campaign mit Varianten sowohl eine übergeordnete Campaign-ID als auch individuelle Varianten-Campaign-IDs gibt, die unter der Haupt-Campaign verschachtelt sind.

### Wo kann ich ihn finden?

Sie können Ihre Campaign-ID auf zwei Arten finden:

{% tabs local %}
{% tab Campaigns %}
Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie eine bereits vorhandene Campaign aus. Wenn die gewünschte Campaign noch nicht existiert, erstellen Sie eine und speichern Sie sie. Unten auf der Seite der einzelnen Campaign finden Sie Ihren **Campaign API Identifier**.

{% endtab %}

{% tab API Keys %}
Gehen Sie zu **Einstellungen** > **APIs und Bezeichner**. Hier bietet Braze eine Suche nach **zusätzlichen API-Bezeichnern** an, mit der Sie bestimmte Bezeichner nachschlagen können.

{% endtab %}
{% endtabs %}

### Wofür kann er verwendet werden?

- Analytics für eine bestimmte Nachricht verfolgen
- Aggregierte Statistiken zur Campaign-Performance auf hoher Ebene erfassen
- Details zu einer bestimmten Campaign abrufen
- Mit Currents Daten auf Nutzer:innen-Ebene für einen ganzheitlichen Ansatz bei Campaigns einbringen
- Mit API-getriggerter Zustellung Statistiken für transaktionale Nachrichten erfassen
- Zum [Suchen nach einer bestimmten Campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns#search-syntax) auf der Seite **Campaigns** mithilfe des Filters `api_id:YOUR_API_ID`

## Segment-Bezeichner {#segment-identifier}

Ein [Segment]({{site.baseurl}}/user_guide/audience/segments)-Bezeichner oder eine Segment-ID ist ein zufälliger Schlüssel, der von Braze für ein bestimmtes Segment innerhalb des Dashboards generiert wird. Segment-IDs sind für jedes Segment eindeutig und können verwendet werden, um Segmente über die API zu referenzieren.

### Wo kann ich ihn finden?

Sie können Ihre Segment-ID auf zwei Arten finden:

{% tabs local %}
{% tab Segments %}
Gehen Sie zu **Zielgruppe** > **Segments** und wählen Sie ein bereits bestehendes Segment aus. Wenn das gewünschte Segment noch nicht vorhanden ist, erstellen Sie es und speichern Sie es. Unten auf der Seite des einzelnen Segments finden Sie Ihren Segment-Bezeichner.

{% endtab %}

{% tab API Keys %}
Gehen Sie zu **Einstellungen** > **APIs und Bezeichner**. Hier bietet Braze eine Suche nach **zusätzlichen API-Bezeichnern** an, mit der Sie bestimmte Bezeichner nachschlagen können.

{% endtab %}
{% endtabs %}

### Wofür kann er verwendet werden?

- Details zu einem bestimmten Segment abrufen
- Analytics eines bestimmten Segments abrufen
- Abrufen, wie oft ein angepasstes Event für ein bestimmtes Segment aufgezeichnet wurde
- Eine Campaign an Mitglieder eines Segments über die API bestimmen und senden

## Sende-Bezeichner {#send-identifier}

Ein Sende-Bezeichner oder eine Sende-ID ist ein Schlüssel, der entweder von Braze generiert oder von Ihnen für einen bestimmten Nachrichtenversand erstellt wird und unter dem die Analytics verfolgt werden sollen. Der Sende-Bezeichner ermöglicht es Ihnen, Analytics für eine bestimmte Instanz eines Campaign-Versands über den [`/sends/data_series`-Endpunkt]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) abzurufen.

### Wo kann ich ihn finden?

API- und API-getriggerte Campaigns, die als Broadcast gesendet werden, generieren automatisch einen Sende-Bezeichner, wenn keiner angegeben wird. Wenn Sie einen eigenen Sende-Bezeichner angeben möchten, müssen Sie zunächst einen über den [`/sends/id/create`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids) erstellen. Der Bezeichner muss ausschließlich aus ASCII-Zeichen bestehen und darf höchstens 64 Zeichen lang sein. Sie können einen Sende-Bezeichner für mehrere Sendungen derselben Campaign wiederverwenden, wenn Sie die Analytics für diese Sendungen zusammenfassen möchten.

### Wofür kann er verwendet werden?
Nachrichten-Performance programmgesteuert senden und verfolgen, ohne dass für jeden Versand eine Campaign erstellt werden muss.

## Abo-Gruppen-Bezeichner {#subscription-group-identifier}

Ein Abo-Gruppen-Bezeichner oder eine Abo-Gruppen-ID ist ein Schlüssel, der von Braze für eine bestimmte Abo-Gruppe generiert wird. IDs sind für jede Abo-Gruppe eindeutig und können verwendet werden, um Abo-Gruppen über die API zu referenzieren.

### Wo kann ich ihn finden?

Gehen Sie zu **Zielgruppe** > **Abonnements** und kopieren Sie die ID neben der jeweiligen Abo-Gruppe.

### Wofür kann er verwendet werden?

- Abo-Gruppen einer Nutzer:in auflisten
- Abo-Gruppenstatus einer Nutzer:in abrufen
- Abo-Gruppenstatus einer Nutzer:in aktualisieren