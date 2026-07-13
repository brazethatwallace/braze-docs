---
nav_title: Odicci
article_title: Odicci
description: "Schritt-für-Schritt-Anleitung zur Integration von Odicci mit Braze für personalisierte Marketing-Campaigns"
alias: /partners/odicci/
page_type: partner
search_tag: Partner
---

# Integration von Odicci mit Braze {#integrate-odicci-with-braze}

> Erfahren Sie, wie Sie Braze mit [Odicci](https://www.odicci.com/) integrieren können, einer Plattform, die es Unternehmen ermöglicht, Kund:innen durch loyalitätsgetriebene Omnichannel-Erlebnisse zu gewinnen, zu binden und zu halten.

{% alert tip %}
Weitere Ressourcen und FAQs finden Sie im [Odicci Help Center](https://help.odicci.com).
{% endalert %}

## Anwendungsfälle {#use-cases}

Sie können die Odicci-Plattform mit Braze verbinden, um nahtlose Datenfreigabe und Campaign-Verwaltung zu ermöglichen. Dies umfasst:

- Automatische Übermittlung der in Odicci-Erlebnissen gesammelten Zielgruppendaten an Braze.
- Triggern personalisierter Marketing-Campaigns basierend auf Nutzer:innen-Interaktionen.
- Abbildung von Feldern zwischen Odicci und Braze, um eine genaue Datensynchronisierung zu gewährleisten.

## Beispiel {#example}

Ein Einzelhändler nutzt die spielerischen Erlebnisse von Odicci, um E-Mail-Adressen für eine Marketing-Campaign zu sammeln.

1. Eine Kundin oder ein Kunde schließt ein Spiel in Odicci ab und gibt dabei ihre bzw. seine E-Mail-Adresse an.
2. Odicci synchronisiert diese Daten automatisch mit Braze.
3. Braze triggert eine personalisierte „Danke“-E-Mail und fügt einen Rabattcode hinzu.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Ein Odicci-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Odicci-Konto mit Zugriff auf den Bereich **Integrations**. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit den Berechtigungen `users.track` und `campaigns.list`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration von Odicci {#integrating-odicci}

### 1. Schritt: Aktivieren Sie die Integration in Odicci {#step-1-enable-the-integration-in-odicci}

1. Melden Sie sich bei Ihrem Odicci-Konto an.
2. Navigieren Sie zum Bereich **Settings > Integrations**.
3. Suchen Sie die **Braze**-Integration und klicken Sie auf **Connect**.

   ![Braze-Integration verbinden]({% image_buster /assets/img/odicci/braze_connect.png %})

4. Geben Sie Ihren Braze REST-API-Schlüssel in das vorgesehene Feld ein.
5. Speichern Sie die Einstellungen, um die Integration auf Kontoebene zu aktivieren.

### 2. Schritt: Beziehen Sie Ihren Braze REST-API-Schlüssel {#step-2-obtain-your-braze-rest-api-key}

1. Melden Sie sich bei Ihrem Braze-Konto an.
2. Gehen Sie zu **Entwicklungskonsole > REST API Keys**.
3. Erstellen Sie einen neuen API-Schlüssel oder kopieren Sie einen vorhandenen Schlüssel mit der Berechtigung `users.track`.

### 3. Schritt: Aktivieren Sie die Integration auf Erlebnisebene {#step-3-activate-the-integration-at-the-experience-level}

1. Erstellen oder öffnen Sie ein **Experience** in Odicci Studio.
2. Navigieren Sie zu **Studio > Settings > Integrations**.
3. Suchen Sie das Kontrollkästchen **Braze** und aktivieren Sie es, um die Integration für das Erlebnis einzuschalten.
4. Speichern Sie Ihre Änderungen.

### 4. Schritt: Felder zuordnen {#step-4-map-fields}

1. Nachdem Sie die Integration aktiviert haben, bleiben Sie im Bereich **Studio > Settings > Integrations**.
2. Ordnen Sie die Felder aus Ihrem Odicci-Erlebnis (z. B. `Email`, `Name`) den entsprechenden Feldern in Braze zu.
3. Speichern Sie Ihre Konfiguration.

   ![Konfiguration der Feldzuordnung]({% image_buster /assets/img/odicci/braze_field_mapping.png %})

### 5. Schritt: Testen Sie die Integration {#step-5-test-the-integration}

1. Führen Sie das Erlebnis in Odicci aus, um Testdaten zu sammeln.
2. Überprüfen Sie, ob die Daten korrekt mit Braze synchronisiert werden, indem Sie das Braze-Dashboard oder die Datenprotokolle prüfen.
3. Stellen Sie sicher, dass die zugeordneten Felder in Braze korrekt befüllt sind.

## Fehlerbehebung {#troubleshooting}

Wenn Sie Probleme mit der Integration haben, ziehen Sie die folgenden Lösungen in Betracht. Für weitere Unterstützung wenden Sie sich an den [Odicci-Support](https://help.odicci.com).

### API-Schlüssel nicht gültig {#api-key-not-valid}

Überprüfen Sie Ihren Braze-API-Schlüssel und stellen Sie sicher, dass er über die erforderlichen Berechtigungen verfügt. Geben Sie den API-Schlüssel anschließend erneut in den Odicci-Integrationseinstellungen ein.

### Daten werden nicht synchronisiert {#data-not-syncing}

Überprüfen Sie, ob die Felder im Abschnitt **Field Mapping** korrekt konfiguriert sind. Stellen Sie dann sicher, dass der API-Schlüssel über die Berechtigung für Nutzerdatenimporte verfügt.

### Campaign wird nicht getriggert {#campaign-not-triggering}

Überprüfen Sie die Braze-Campaign-Einstellungen, um sicherzustellen, dass die richtige Zielgruppe oder die richtigen Triggerbedingungen festgelegt sind.