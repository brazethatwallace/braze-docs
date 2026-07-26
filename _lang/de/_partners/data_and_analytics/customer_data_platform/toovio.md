---
nav_title: Toovio
article_title: Toovio
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Toovio, einem Data-as-a-Service-Unternehmen, das Ihnen hilft, Ihre verwertbaren Daten zu entdecken und die wichtigsten Elemente zu nutzen, um auf der Grundlage vordefinierter Ziele zusätzliche Ergebnisse zu erzielen."
alias: /partners/toovio/
page_type: partner
search_tag: Partner

---

# Toovio

> [Toovio](https://toovio.com/) ist ein auf künstliche Intelligenz gestützter Data-as-a-Service-Anbieter, der Ihnen hilft, Ihre verwertbaren Daten zu entdecken und die wichtigsten Elemente zu nutzen, um auf der Grundlage vordefinierter Ziele zusätzliche Ergebnisse zu erzielen.

_Diese Integration wird von Toovio gepflegt._

## Über die Integration {#about-the-integration}

Die Partnerschaft zwischen Braze und Toovio ermöglicht das Triggern von Nachrichten nahezu in Realtime, die Bereitstellung von Tools zur Steigerung der Performance und den Zugriff auf die fortschrittlichen Tools von Toovio zur Messung von Campaigns.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Toovio-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Toovio-Konto. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Currents | Braze-Currents ermöglicht es Braze-Clients, Ereignis- oder Verhaltensdaten an einen Braze-Datenpartner (AWS S3, Google Cloud Storage oder Microsoft Azure Blob Storage) zu streamen, um sie außerhalb der Braze-Plattform zu verarbeiten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Die folgende Integration erlaubt es Toovio, Trigger zu generieren, die auf bestimmte Kund:innen abzielen und nahezu in Realtime zu kommunizieren. Von Toovio ermittelte Trigger werden über den Braze-[`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) an Braze übermittelt.

### 1. Schritt: Datenpartner definieren {#step-1-define-data-partner}

Ein Ablageort für den Currents-Feed muss mit Toovio geteilt werden; dies erlaubt Toovio den Zugriff auf und die Verarbeitung von Ereignis- und Verhaltensdaten der Nutzer:innen.

### 2. Schritt: Eine getriggerte Campaign einrichten {#step-2-set-up-a-triggered-campaign}

Erstellen Sie eine über die Braze-API [getriggerte Campaign]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) auf der Grundlage der Kund:innen-Events, die Toovio als Targeting verwenden wird. Zusätzlich sollten Nutzer:innen-Attribute und -Werte definiert werden, die die Campaign triggern sollen.

### 3. Schritt: Richten Sie Ihr Toovio-Konto ein {#step-3-set-up-your-toovio-account}

Kontaktieren Sie Toovio unter [info@toovio.com](mailto:info@toovio.com?subject=New%20Customer%20Request) mit dem Betreff „New geschäftskunden Request“, um ein Konto einzurichten. Toovio arbeitet mit den Clients zusammen, um Trigger und die zugrunde liegenden Modelle einzurichten.