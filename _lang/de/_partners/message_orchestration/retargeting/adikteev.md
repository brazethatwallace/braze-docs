---
nav_title: Adikteev
article_title: Adikteev Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Prognose
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Adikteev, einer Engine zur Nutzerbindung, die Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Prognose mit Full Service App-Retargeting kombiniert."
alias: /partners/adikteev/
page_type: partner
search_tag: Partner

---

# Adikteev Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Prognose {#adikteev-churn-prediction}

> [Adikteev](https://www.adikteev.com/churn-prediction) ist eine Engine zur Nutzerbindung, die Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Prognose mit Full Service App-Retargeting kombiniert.

_Diese Integration wird von Adikteev gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Adikteev ermöglicht es Ihnen, die Nutzerbindung zu steigern, indem Sie die Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Prognose-Technologie von Adikteev in Braze-CRM or Customer-Relationship-Management [-System] (CRM)-Campaigns nutzen, um risikoreiche Nutzersegmente vorrangig anzusprechen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Adikteev-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein Adikteev-Konto erforderlich. |
| Braze-Representational State Transfer-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit der Berechtigung `users.track`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **APIs und Bezeichner** erstellt werden. |
| Braze-Representational State Transfer-Endpunkt | [Ihre Representational State Transfer-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

{% tabs %}
{% tab Zielgruppen-Filterung %}
Verfeinerung Ihrer Zielgruppen-Segmente auf Basis des Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Risikos.<br> Die Namen und Werte der angepassten Attribute, die von Adikteev gesendet werden, sind konfigurierbar.

![Ein Screenshot, der ein Beispiel zeigt, wie ein von Adikteev gesendetes angepasstes Attribut als Zielgruppen-Segment-Filter verwendet wird.]({% image_buster /assets/img/adikteev/audience.png %})
{% endtab %}
{% tab Nachrichten-Targeting %}
Anpassung Ihrer Braze-Messaging-Campaigns auf Basis des Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Risikos der Empfänger:innen.

![Ein Screenshot, der ein Beispiel zeigt, wie ein von Adikteev gesendetes angepasstes Attribut als Targeting-Filter für eine Campaign verwendet wird.]({% image_buster /assets/img/adikteev/campaign.png %})
{% endtab %}
{% endtabs %}

## Integration

### 1. Schritt: Teilen Sie den Event-Stream Ihrer App {#step-1-share-the-event-stream-of-your-app}

Um die Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Prognose für Ihre App-Zielgruppe zu starten, müssen Sie bei Adikteev die Event-Postbacks Ihrer mobilen Messplattform aktivieren. Folgen Sie den Anweisungen auf der [Adikteev-Support-Website](https://help.adikteev.com/hc/en-us/sections/8185123408914-Data-stream-activation), um dies einzurichten.

### 2. Schritt: Erstellen Sie Ihren Braze-Representational State Transfer-API-Schlüssel {#step-2-create-your-braze-rest-api-key}

Navigieren Sie in Braze zu **Einstellungen** > **APIs und Bezeichner**. Wählen Sie **Neuen API-Schlüssel erstellen**, geben Sie den gewünschten API-Schlüssel-Namen ein und stellen Sie sicher, dass die folgende Berechtigung hinzugefügt wird:

- `users.track`

### 3. Schritt: Informationen an das Adikteev-Team übermitteln {#step-3-provide-information-to-the-adikteev-team}

Um die Integration abzuschließen, müssen Sie Ihren Representational State Transfer-API-Schlüssel und Ihre Representational State Transfer-Endpunkt-URL an Ihren Adikteev Account Manager:in übermitteln. Adikteev wird die Verbindung herstellen und Sie nach Abschluss der Einrichtung kontaktieren, um die Integration zu bestätigen.

## Batching und Rate-Limits {#batching-and-rate-limits}

Der Endpunkt `user.track` wird verwendet, um Details zu Ihren Nutzer:innen zu Update or aktualisieren or aktualisieren. In der [API-Dokumentation]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) finden Sie ausführliche Informationen zu den Rate-Limits des Endpunkts, zur Stapelverarbeitung von Anfragen und zu den Anfragedetails.

{% alert tip %}
Denken Sie daran, dass API-Aufrufe nur zum Update or aktualisieren or aktualisieren von Daten erfolgen sollten, die sich geändert haben, um die Gesamtzahl der API-Aufrufe zu reduzieren. Mit anderen Worten: Update or aktualisieren or aktualisieren Sie nur Nutzer:innen, bei denen sich das Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Segment geändert hat.
{% endalert %}

## Bezeichner für Nutzer:innen und Geräte {#user-and-device-identifiers}

Nutzerprofile in Braze können mit jeder Art von Nutzer:innen- oder Geräte-Bezeichnern verknüpft werden. Die Liste der verfügbaren Optionen hängt davon ab, wie Sie die Datenerfassung in Braze integriert haben. Für Adikteev müssen Sie einen gemeinsamen Bezeichner zwischen Ihrem MMP und Ihren Nutzerprofilen in Braze finden, um die Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Segment-Informationen korrekt zu übermitteln.

## Datenspeicherung und -löschung {#data-retention-and-deletion}

Erfolgt kein Update or aktualisieren, werden das Attribut und sein Wert auf unbestimmte Zeit in den Braze-Nutzerprofilen aufbewahrt.

Um ein Profilattribut zu entfernen, setzen Sie es auf `null`.

## Anfrage-Payloads {#request-payloads}

Der von Adikteev an Braze gesendete Payload ist anpassbar und kann so konfiguriert werden, dass er den Anforderungen der Kund:innen entspricht. Dazu gehört die Konfiguration der verwendeten Bezeichner, des Namens des angepassten Attributs und ob Adikteev neue Nutzer:innen in Braze anlegen oder nur bestehende Nutzer:innen Update or aktualisieren or aktualisieren kann.

## Support und Fehlerbehebung {#support-and-troubleshooting}

Kontaktieren Sie Ihren Adikteev Account Manager:in, wenn Sie Fragen zur Integration haben oder Unterstützung bei Ihren Anwendungsfällen benötigen.