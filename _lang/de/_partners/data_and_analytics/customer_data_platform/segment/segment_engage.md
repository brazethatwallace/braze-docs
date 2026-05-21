---
nav_title: Segment Engage
article_title: Segment Engage
page_order: 3
alias: /partners/segment_personas/
alias: /partners/segment_engage/
alias: /partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/

description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Segment, einer Customer Data Platform, die Informationen zwischen den Quellen in Ihrem Marketing-Stack sammelt und weiterleitet."
page_type: partner
search_tag: Partner

---

# Segment Engage

> [Segment](https://segment.com) ist eine Customer Data Platform, mit der Sie Ihre Kundendaten sammeln, bereinigen und aktivieren können. Dieser Referenzartikel gibt eine Übersicht über die Verbindung zwischen [Braze und Segment Engage](https://segment.com/docs/destinations/braze/#Engage) und beschreibt die Anforderungen und Prozesse für die ordnungsgemäße Implementierung und Nutzung.

Die Integration von Braze und Segment ermöglicht es Ihnen, mit [Engage](https://segment.com/docs/engage/), dem integrierten Audience-Builder von Segment, Segmente von Nutzer:innen auf der Grundlage von Daten zu erstellen, die Sie bereits über verschiedene Quellen gesammelt haben. Diese Zielgruppen werden dann als Kohorte mit Braze synchronisiert oder im Nutzerprofil durch [angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) oder [angepasste Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) gekennzeichnet, die zur Erstellung von Braze-Segmenten für das Retargeting in Kampagnen und Canvas verwendet werden können.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Segment-Konto | Um diese Partnerschaft nutzen zu können, ist ein [Segment-Konto](https://app.segment.com/login) erforderlich. |
| Braze-Cloud-Ziel | Sie müssen in Ihrer Segment-Integration bereits [Braze als Ziel eingerichtet]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) haben.<br><br>Dazu gehört die Angabe des richtigen Braze-Rechenzentrums und des REST-API-Schlüssels in Ihren [Verbindungseinstellungen]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Braze-Datenimport-Schlüssel | Um Engage-Zielgruppen als Kohorten mit Braze zu synchronisieren, müssen Sie einen Datenimport-Schlüssel generieren.<br><br>Der Kohortenimport befindet sich im Early Access. Wenden Sie sich an Ihren Customer-Success-Manager, um Zugang zu diesem Feature zu erhalten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Kohorten-Ziel-Integration {#cohorts-destination-integration}

### 1. Schritt: Erstellen Sie eine Engage-Zielgruppe {#step-1-create-an-engage-audience}
1. Navigieren Sie in Segment zum Tab **Audiences** in Engage und klicken Sie auf **New**.
2. Erstellen Sie Ihre Zielgruppe. Ein Blitzsymbol in der oberen Ecke der Seite zeigt an, ob die Zielgruppe in Realtime aktualisiert wird.
3. Wählen Sie anschließend Braze als Ihr Ziel aus.
4. Zeigen Sie eine Vorschau Ihrer Zielgruppe an, indem Sie auf **Review & Create** klicken. Standardmäßig fragt Segment alle historischen Daten ab, um den aktuellen Wert des berechneten Merkmals und der Zielgruppe festzulegen. Um diese Daten auszulassen, deaktivieren Sie die Option **Historical Backfill**.

### 2. Schritt: Erfassen Sie Ihren Kohorten-Datenimport-Schlüssel {#step-2-capture-your-cohort-data-import-key}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Segment**.

Hier finden Sie Ihren REST-Endpunkt und können Ihren Braze-Datenimport-Schlüssel generieren. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden ungültig machen.

### 3. Schritt: Verbinden Sie das Braze-Kohorten-Ziel {#step-3-connect-the-braze-cohorts-destination}
Folgen Sie den [Anweisungen von Segment](https://segment.com/docs/connections/destinations/catalog/actions-braze-cohorts/#getting-started) zur Einrichtung des Kohorten-Ziels, um Ihre Engage-Zielgruppen als Kohorten mit Braze zu synchronisieren.

### 4. Schritt: Erstellen Sie ein Braze-Segment aus der Engage-Zielgruppe {#step-4-create-a-braze-segment-from-the-engage-audience}
Navigieren Sie in Braze zu **Segments**, erstellen Sie ein neues Segment und wählen Sie **Segment Cohorts** als Filter. Von hier aus können Sie auswählen, welche Segment-Kohorte Sie einbeziehen möchten. Nachdem das Segment-Kohorten-Segment erstellt wurde, können Sie es als Zielgruppen-Filter bei der Erstellung einer Campaign oder eines Canvas auswählen.

![]({% image_buster /assets/img/segment/segment3.png %})

## Cloud-Modus-Integration {#cloud-mode-integration}

### 1. Schritt: Erstellen Sie ein berechnetes Merkmal oder eine Zielgruppe in Segment {#step-1-create-a-segment-computed-trait-or-audience}

1. Navigieren Sie in Segment zum Tab **Computed Traits** oder **Audiences** in **Engage** und klicken Sie auf **New**.
2. Erstellen Sie Ihr berechnetes Merkmal oder Ihre Zielgruppe. Ein Blitzsymbol in der oberen Ecke der Seite zeigt an, ob die Berechnung in Realtime aktualisiert wird.
3. Wählen Sie anschließend **Braze** als Ihr Ziel aus.
4. Zeigen Sie eine Vorschau Ihrer Zielgruppe an, indem Sie auf **Review & Create** klicken. Standardmäßig fragt Segment alle historischen Daten ab, um den aktuellen Wert des berechneten Merkmals und der Zielgruppe festzulegen. Um diese Daten auszulassen, deaktivieren Sie die Option **Historical Backfill**.
5. Passen Sie in den Einstellungen für das berechnete Merkmal oder die Zielgruppe die Verbindungseinstellungen an, je nachdem, wie Sie Ihre Daten an Braze senden möchten.

#### Berechnete Merkmale und Zielgruppen {#computed-traits-and-audiences}

[Berechnete Merkmale](https://segment.com/docs/engage/audiences/computed-traits/) und [Zielgruppen](https://segment.com/docs/Engage/audiences/) können als angepasste Attribute oder angepasste Events an Braze gesendet werden.
- Merkmale und Zielgruppen, die über den `identify`-Aufruf gesendet werden, erscheinen in Braze als angepasste Attribute.
- Merkmale und Zielgruppen, die über den `track`-Aufruf gesendet werden, erscheinen in Braze als angepasste Events.

Sie können wählen, welche Methode Sie verwenden möchten (oder beide verwenden), wenn Sie das berechnete Merkmal mit dem Braze-Ziel verbinden.

{% tabs %}
{% tab Identify %}

Sie können berechnete Merkmale und Zielgruppen als `identify`-Aufrufe an Braze senden, um angepasste Attribute in Braze zu erstellen.

Wenn Sie beispielsweise ein von Engage berechnetes Merkmal für „Zuletzt angesehener Artikel“ haben, finden Sie `last_product_viewed_item` im Braze-Profil der Nutzer:in unter **Custom Attributes**. Wäre dies stattdessen eine Engage-Zielgruppe, würden Sie Ihre Zielgruppe unter **Custom Attributes** als `true` aufgeführt finden.

| Berechnetes Merkmal | Zielgruppen |
| -------------- | --------- |
| ![Der Abschnitt für angepasste Attribute in einem Nutzerprofil listet „last_product_viewed_item“ als „Sweater“ auf.]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![Der Abschnitt für angepasste Attribute in einem Nutzerprofil führt „dormant_shopper“ als „true“ auf.]({% image_buster /assets/img/segment/dormant-identify-braze.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Berechnete Merkmale und Zielgruppen" }

{% endtab %}
{% tab Track %}

Sie können berechnete Merkmale und Zielgruppen als `track`-Aufrufe an Braze senden, um angepasste Events in Braze zu erstellen.

Um das vorherige Beispiel fortzusetzen: Wenn eine Nutzer:in ein berechnetes Merkmal für „Zuletzt angesehener Artikel“ hat, erscheint dieses in den Braze-Profilen der Nutzer:innen als `Trait Computed` mit der entsprechenden Anzahl und dem letzten Zeitstempel unter **Custom Events**. Wäre dies stattdessen eine Engage-Zielgruppe, würden Sie Ihre Zielgruppe, die Anzahl und den letzten Zeitstempel unter **Custom Attributes** als `true` finden.

| Berechnetes Merkmal | Zielgruppen |
| -------------- | --------- |
| ![Der Abschnitt für angepasste Events in einem Nutzerprofil listet „Trait Computed“ „1“ Mal auf, wobei der letzte Zeitpunkt „vor 20 Stunden“ ist.]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![Der Abschnitt für angepasste Attribute in einem Nutzerprofil listet „Audience Entered“ „1“ Mal auf, wobei der letzte Zeitpunkt „9. März um 1:45 Uhr“ ist.]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Berechnete Merkmale und Zielgruppen" }

{% endtab %}
{% endtabs %}

### 2. Schritt: Segmentieren Sie Nutzer:innen in Braze {#step-2-segment-users-in-braze}

Um in Braze ein Segment dieser Nutzer:innen zu erstellen, navigieren Sie zu **Segments** unter **Engagement**, erstellen Sie ein neues Segment und benennen Sie es. Gehen Sie dann je nach verwendetem Aufruf wie folgt vor:
- **Identify**: Wählen Sie **custom attribute** als Filter und suchen Sie Ihr angepasstes Attribut. Verwenden Sie dann die Option „matches regex“ (Merkmal) oder die Option „equals“ (Zielgruppe) und geben Sie die entsprechende Variable ein.
- **Track**: Wählen Sie **custom event** als Filter und suchen Sie Ihr angepasstes Event. Verwenden Sie dann die Option „more than“, „less than“ oder „exactly“ und geben Sie den gewünschten Wert ein. Dies hängt davon ab, wie Sie Ihr Segment definieren möchten.

Nach dem Speichern können Sie dieses Segment bei der Erstellung von Canvas oder Kampagnen im Schritt „Targeting von Nutzer:innen“ referenzieren.

## Synchronisationszeit {#sync-time}

Obwohl die Standardeinstellung für die Verbindung von Braze zu Segment Engage `Realtime` ist, gibt es einige Filter, die die Persona von der Realtime-Synchronisierung ausschließen, einschließlich einiger zeitbasierter Filter, die die Größe Ihrer Zielgruppe zum Zeitpunkt des Nachrichtenversands einschränken.

## Testen mit dem Segment-Debugger {#segment-debugger-testing}

Das Dashboard von Segment bietet ein „Debugger“-Feature, mit dem Kund:innen testen können, ob die Daten von einer „Quelle“ wie erwartet an ein „Ziel“ übertragen werden.

Dieses Feature stellt eine Verbindung zum Braze-[`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) her, d. h. es kann nur für identifizierte Nutzer:innen verwendet werden (Nutzer:innen, die bereits eine Nutzer-ID für ihr Braze-Nutzerprofil haben).

Dies funktioniert nicht bei einer Side-by-Side-Integration von Braze. Es werden keine Serverdaten übertragen, wenn Sie nicht die korrekten Braze-REST-API-Informationen eingegeben haben.