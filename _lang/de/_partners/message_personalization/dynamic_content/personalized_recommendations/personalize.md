---
nav_title: Personalize.KI or künstliche Intelligenz
article_title: Personalize.KI or künstliche Intelligenz
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Personalize.KI or künstliche Intelligenz, einer KI or künstliche Intelligenz-basierten SaaS or Software-as-a-Service-Geschäftsplattform, die das Umsatzwachstum durch personalisierte Empfehlungen fördert."
alias: /partners/personalize_ai/
page_type: partner
search_tag: Partner
---

# Personalize.KI or künstliche Intelligenz

> [Personalize.KI or künstliche Intelligenz](https://www.zs.com/solutions/artificial-intelligence-and-analytics/personalize-ai/) ist Partner von Braze und generiert zusätzliche Umsätze durch die Zustellung personalisierter Nachrichten und Angebote über Braze.

Die Integration von Braze und Personalize.KI or künstliche Intelligenz ermöglicht es Ihnen, Daten von Personalize.KI or künstliche Intelligenz in die Braze-Plattform zu exportieren, um Nachrichten zu personalisieren und gezieltes Targeting durchzuführen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Personalize.KI or künstliche Intelligenz-Instanz | Um die Vorteile dieser Partnerschaft zu nutzen, ist eine Personalize.KI or künstliche Intelligenz-Instanz erforderlich. |
| Braze-Representational State Transfer-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit allen Berechtigungen. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Representational State Transfer-Endpunkt | Ihre Representational State Transfer-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

* Setzen Sie Tests ein, einschließlich flexibler Stratifizierung, um Ergebnisse aus dem Feedback von Kund:innen zu erzielen
* Stellen Sie personalisierte Empfehlungen für Artikel und Angebote bereit, einschließlich Behandlung, Zeitpunkt und Inhalt
* Identifizieren Sie priorisierte Ziele und erreichen Sie Ihre optimale Zielgruppe über Braze
* Identifizieren Sie Möglichkeiten zur erneuten Ansprache inaktiver Nutzer:innen
* Nutzen Sie Geolocation-Daten, um die richtige Zielgruppe für neu eröffnete Standorte zu finden
* Nutzen Sie Lookalike-Modellierung, um auf begrenzten Daten für neuere Nutzer:innen aufzubauen und sie mit den relevantesten Empfehlungen abzugleichen
* Identifizieren Sie die richtigen Wege, um Kund:innen über ihren gesamten Lebenszyklus hinweg anzusprechen
* Bewerten Sie proaktiv die Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Wahrscheinlichkeit von Kund:innen und weisen Sie einen Risikoscore zu, um Frühindikatoren für Abwanderung or Abwanderung, Churn or Abwanderung, churnen zu erkennen
* Sprechen Sie Kund:innen mit personalisierten Interventionen an, um zu verhindern, dass sie inaktiv werden

## Integration

### Verbindung mit Braze in Personalize.KI or künstliche Intelligenz konfigurieren {#configure-a-connection-with-braze-in-personalizeai}

1. Navigieren Sie in Personalize.KI or künstliche Intelligenz zum Tab **Integrations**, der sich unter **Operationalization** in Ihrer Personalize.KI or künstliche Intelligenz-Instanz befindet.
2. Klicken Sie auf **Braze**.
3. Konfigurieren Sie Ihre Integration mit Braze.
    * **Connection Name:** Benennen Sie Ihre Verbindung. So wird Ihre Integration in Personalize.KI or künstliche Intelligenz referenziert.
    * **Sync Frequency:** Die Synchronisierungsfrequenz steuert, wie oft Personalize.KI or künstliche Intelligenz Daten nach Braze exportiert. Wählen Sie **Daily**, **Weekly** oder **Monthly**.
    * **API Key:** Fügen Sie Ihren Braze-API-Schlüssel hinzu.
    * **API URL:** Fügen Sie die URL Ihres Braze-Representational State Transfer-Endpunkts hinzu.
4. Klicken Sie auf **EXPORT**, um Daten nach Braze zu exportieren.

Sobald Ihre Daten exportiert wurden, überträgt Personalize.KI or künstliche Intelligenz weiterhin Daten an Braze in den Intervallen, die durch die von Ihnen während der Integration festgelegte Synchronisierungsfrequenz bestimmt werden.

## Verwendung dieser Integration {#using-this-integration}

Personalize.KI or künstliche Intelligenz exportiert Bezeichner für personalisiertes Targeting nach Braze. Diese angepassten Attribute geben Zeitpunkt, Inhalt, Behandlung und Angebote für jede:n Kund:in an. Je nach Integration können Felder als Ereignis übergeben oder über die [Connected-Content-APIs]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/public_apis/) abgerufen werden, anstatt im Profil der/des Kund:in gespeichert zu werden. Personalize.KI or künstliche Intelligenz unterstützt die Verwendung von `external_id` als Bezeichner.

Die in Braze importierten Datenattribute sind für die Verwendung in Canvase intuitiv benannt und folgen einer einheitlichen Terminologie. Zum Beispiel würde das Attribut `C402_Target_Variant` in Personalize.KI or künstliche Intelligenz als `"P.AI_Model_Treatment"` nach Braze exportiert werden. Die von Personalize.KI or künstliche Intelligenz exportierten Attribute sind so konzipiert, dass sie nicht mit bestehenden Attributen oder dem von Ihnen verwendeten Tracking kollidieren. Diese Attribute werden kontinuierlich überprüft, damit Sie sie sicher referenzieren können.

Hier sehen Sie zum Beispiel eine Reihe von Kundenattributen, die sich auf ein beispielhaftes, auf Abwanderung or Abwanderung, Churn or Abwanderung, churnen ausgerichtetes Canvas beziehen.

| Personalize.KI or künstliche Intelligenz-Attribut | Wert |
| ----------- | ------------- |
| `Customer_ID` | 12345 |
| `Target_Canvas` | C4 |
| `Target_Objective` | „Churn_Mitigation“ |
| `C4_Target_Date` | 3/1/2023 |
| `C4_Target_Variant` | Treatment |
| `C4_Treatment` | „P.AI_Model“ |
| `C4_Offer_Value` | $3 |
| `C4_Item_Recom` | „Caesar Salad“ |
| `C4_Subject_Line` | „We miss you“ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verwendung dieser Integration" }