---
nav_title: StackAdapt
article_title: StackAdapt
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und StackAdapt."
alias: /partners/stackadapt/
page_type: partner
search_tag: Partner
---

# StackAdapt

> [StackAdapt](https://www.stackadapt.com/) ist die führende KI-gestützte Marketing-Plattform, die von digitalen Marketern genutzt wird, um zielgerichtete, Performance-gesteuerte Werbung auszuliefern.

_Diese Integration wird von StackAdapt gepflegt._

Die Integration von Braze und StackAdapt ermöglicht es Ihnen, Nutzerprofildaten aus Braze mit dem StackAdapt Data Hub zu synchronisieren. Durch die Verbindung der beiden Plattformen können Sie eine einheitliche Sicht auf Ihre Kund:innen schaffen und First-Party-Daten aktivieren, um die Performance von Anzeigen zu verbessern.

## Anwendungsfälle {#use-cases}

- **Passive Nutzer:innen erneut ansprechen:** Identifizieren Sie Nutzer:innen, die sich von E-Mail-Marketing-Listen in Braze abgemeldet haben, und sprechen Sie sie mit programmatischen Anzeigen auf StackAdapt an, um sie über einen anderen Kanal erneut zu erreichen.
- **Multi-Channel-Erlebnisse schaffen:** Erweitern Sie die Journey von Nutzer:innen über E-Mails hinaus. Wenn Nutzer:innen beispielsweise auf eine E-Mail-Campaign in Braze klicken, können Sie ihnen mit StackAdapt eine ergänzende programmatische Anzeige zeigen, die die Nachricht verstärkt und zu weiteren Aktionen anregt.
- **In großem Umfang personalisieren:** Nutzen Sie granulare Datenpunkte aus Braze, wie „Heimatort“ oder „Sprache“, um hochrelevante, lokalisierte und sprachspezifische Anzeigen und E-Mails auszuliefern.
- **Verständnis für Ihre Zielgruppe vertiefen:** Durch die Synchronisierung von Profilattributen können Sie in StackAdapt umfangreichere Zielgruppen-Segmente erstellen, die ein präziseres Targeting und personalisierte Werbeerlebnisse ermöglichen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ------------------- |
| **StackAdapt-Konto** | Sie benötigen ein aktives StackAdapt-Konto mit Berechtigungen zur Verwaltung von Data-Hub-Integrationen. |
| **Braze REST-API-Schlüssel** | Ein Braze REST-API-Schlüssel mit den folgenden Berechtigungen: <br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| **Braze REST-Endpunkt** | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Funktionsweise {#how-it-works}

Der StackAdapt Data Hub stellt eine direkte Verbindung zu Ihrem Braze-Konto her, um Nutzerprofilattribute abzurufen. So können Sie Ihre Braze-Kundendaten direkt in StackAdapt für eine fortschrittliche Zielgruppen-Segmentierung und -Aktivierung nutzen.

### Datenfluss {#data-flow}

1. StackAdapt initiiert eine sichere Verbindung zu Ihrer Braze-Instanz unter Verwendung der bereitgestellten API-Zugangsdaten.
2. StackAdapt ruft Nutzerprofildaten ab – insbesondere die Eigenschaften, die Sie ausgewählt und zugeordnet haben.
3. Die Daten werden normalisiert und in Ihren StackAdapt Data Hub aufgenommen und stehen dann für die Segmentierung und Verwendung in Ihren Campaigns zur Verfügung.
4. Die Integration ermöglicht geplante Datensynchronisierungen (z. B. täglich), damit Ihre StackAdapt-Zielgruppen stets mit den neuesten Profildaten aus Braze aktuell bleiben.

## Synchronisierte Felder {#fields-synced}

StackAdapt kann eine Vielzahl von Braze-Profilfeldern synchronisieren, darunter unter anderem:

{% tabs local %}
{% tab Standardattribute %}
- E-Mail
- Geburtsdatum
- Vorname
- Nachname
- Telefon
- Heimatort
- Land
- Geschlecht
- Zeitzone
- Erstellt am
- Externe ID
- Sprache

{% endtab %}
{% tab Angepasste Attribute %}
Attribute, die spezifisch für Ihre App oder Ihr Unternehmen sind und auf Grundlage Ihrer individuellen Geschäftsanforderungen definiert werden.

{% endtab %}
{% tab Attribution-Daten %}
- Attributierte Anzeige
- Attributierte Anzeigengruppe
- Attribution-Campaign
- Attributierte Quelle

{% endtab %}
{% tab Abo-Status %}
- E-Mail-Abo-Status
- Push-Abo-Status

Es ist entscheidend, die Felder in Braze, die die Zustimmung der Nutzer:innen für Marketing-Kommunikation widerspiegeln (z. B. den E-Mail-Abo-Status), korrekt zuzuordnen, damit Ihre Werbemaßnahmen mit den Präferenzen der Nutzer:innen und den Datenschutzbestimmungen konform bleiben.

{% endtab %}
{% endtabs %}

## Einrichten der Integration {#setting-up-the-integration}

Folgen Sie diesen Schritten, um Ihre Braze-Nutzerprofile zu importieren:

1. Melden Sie sich bei Ihrem StackAdapt-Konto an.
2. Wählen Sie im Navigationsmenü **Data Hub** aus.
3. Wählen Sie **Import Profiles** und dann **Braze** aus der Liste der verfügbaren Integrationen.
4. Geben Sie Ihre Braze-API-Zugangsdaten ein, wenn Sie dazu aufgefordert werden.
- **Braze REST API Key:** Zu finden in Braze unter **Einstellungen** > **API-Schlüssel**. Als bewährte Sicherheitspraxis empfehlen wir, einen eigenen API-Schlüssel für Ihre StackAdapt-Integration zu erstellen.
- **Braze App Key:** Zu finden in Braze unter **Einstellungen** > **API-Schlüssel** oder **Apps verwalten**.
- **Braze REST Endpoint URL:** Die Basis-URL für Ihre Braze-Instanz (z. B. `https://rest.iad-01.braze.com`).
5. Wählen Sie **Connect**, um die Zugangsdaten zu überprüfen.

![Braze-Verbindung in StackAdapt.]({% image_buster /assets/img/stackadapt/stackadapt_braze_connection_settings.png %})

{: start="6"}
6. Wählen Sie Ihre Verbindung und Ihren StackAdapt-Advertiser aus.
7. Konfigurieren Sie Ihre **Property Mappings**. Überprüfen und bestätigen Sie die von StackAdapt vorgeschlagenen Standard-Zuordnungen und vorausgewählten Eigenschaften.
8. (Optional) Wenn Sie weitere Eigenschaften importieren möchten, wählen Sie diese aus, indem Sie die entsprechenden Kontrollkästchen aktivieren und angeben, ob sie PII enthalten und welchen Datentyp sie haben.

![Eigenschaftszuordnungen in StackAdapt.]({% image_buster /assets/img/stackadapt/stackadapt_mappings.png %})

{: start="9"}
9. Fügen Sie Ihre Profile einer **Liste** hinzu oder erstellen Sie eine neue, damit Sie Ihre Profile gruppieren und segmentieren können.
10. Wählen Sie **Activate Integration**, um die erste Datensynchronisierung zu starten.

## Hinweise {#considerations}

- **Import von angepassten Events und Eigenschaften:** Dieses Feature wird noch nicht unterstützt.
- **Datenlatenz:** Es kann bis zu 24 Stunden dauern, alle Nutzerprofildaten zu importieren.
- **Einwilligungsverwaltung:** Stellen Sie sicher, dass Ihre Datenerfassungspraktiken in Braze mit den Datenschutzbestimmungen übereinstimmen und dass Sie die erforderliche Einwilligung zur Verwendung von Kundendaten für Werbezwecke haben. StackAdapt verlässt sich auf den Einwilligungsstatus, der von Ihren Quellsystemen übermittelt wird.
- **Attributkonsistenz:** Um die Effektivität Ihrer Daten zu maximieren, sollten Sie die Benennung und Befüllung der Attribute in Braze konsistent halten, bevor Sie sie mit StackAdapt synchronisieren.