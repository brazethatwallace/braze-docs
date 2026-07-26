---
nav_title: Lemnisk
article_title: Integration von Lemnisk mit Braze
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Lemnisk, einer KI-gestützten, auf einer geschäftskunden Data Platform basierenden Plattform für Marketing-Automatisierung, die es Ihnen erlaubt, die bei Lemnisk aus verschiedenen Quellen gesammelten Nutzerdaten in Braze zu streamen, um sie mit den Tools von Braze über verschiedene Kanäle und Ziele hinweg zu aktivieren."
alias: /partners/lemnisk/
page_type: partner
search_tag: Partner

---

# Lemnisk

> [Lemnisk](https://www.lemnisk.co/) ist eine KI-gestützte geschäftskunden Data Platform (CDP) und Marketing-Automatisierungslösung, die die Erfassung, Vereinheitlichung und Aktivierung von Kundendaten aus verschiedenen, isolierten Quellen in Echtzeit ermöglicht. Sie stellt diese vereinheitlichten Daten nahtlos über verschiedene MarTech- und Geschäftsplattformen hinweg bereit und bietet gleichzeitig robuste Realtime-Analytics, um jede Phase des Kundendaten-Lebenszyklus zu verfolgen.

_Diese Integration wird von Lemnisk gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Lemnisk und Braze erlaubt es Marken und Unternehmen, das volle Potenzial von Braze auszuschöpfen, indem sie als CDP-geführte Intelligenzschicht fungiert, die Nutzerdaten plattformübergreifend in Realtime zusammenführt und die gesammelten Informationen und Verhaltensdaten der Nutzer:innen in Echtzeit an Braze sendet. Lemnisk liefert angereicherte Kundenprofile direkt in Braze, indem es Verhaltenssignale und persönliche Attribute zusammenführt, mit denen Sie Ihr Messaging mit tieferem Kontext personalisieren können.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Lemnisk-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein [Lemnisk-Konto](https://www.lemnisk.co/) erforderlich. |
| Externe API in Lemnisk | Wenden Sie sich an Ihren Lemnisk CSM, um die **External API** für Ihr Konto aktivieren zu lassen. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit der Berechtigung `users.track`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST-Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihr Konto]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration von Lemnisk {#integrating-lemnisk}

### Schritt 1: Erstellen einer externen Braze-API {#create-a-braze-external-api}

Gehen Sie in Lemnisk zum Kanal External API. Wählen Sie **Add New External API**. Wir richten nun den Endpunkt [Track Users]({{site.baseurl}}/api/endpoints/user_data/post_user_track) als External API ein.

![Starten des Erstellungsprozesses für eine External API in Lemnisk]({% image_buster /assets/img/lemnisk/open_external_api.png %})

Geben Sie unter **Basic Details** einen Namen, eine Beschreibung, einen Kanal und einen Kanalbezeichner ein.

![Eingabe der grundlegenden Konfigurationsdetails für eine neue External API in Lemnisk]({% image_buster /assets/img/lemnisk/ext_api_basic_details.png %})

Geben Sie unter **External API details** die entsprechenden Details für Ihren `users.track`-Endpunkt ein. Mit {% raw %}`{{}}`{% endraw %} können Sie mehrere Felder auf Engagement-Ebene definieren, sodass Sie für verschiedene Kampagnen unterschiedliche Werte festlegen können.

![Ausfüllen der Endpunkt- und Payload-Details für die External API]({% image_buster /assets/img/lemnisk/ext_api_ext_api_details.png %})

Um die Einrichtung Ihrer Track-Users-Konfiguration abzuschließen, wählen Sie **Save**. Sie werden automatisch auf die Seite **Test API** weitergeleitet.

### Schritt 2: Testen der Konfiguration {#step-2-test-the-configuration}

Geben Sie auf der Seite **Test API** einige Testwerte für die API-Parameter in Ihrer JSON-Strukturansicht ein und wählen Sie dann **Test Configuration**.

Wenn Ihre Zugangsdaten und API-Definitionen korrekt sind, gibt Braze eine Erfolgsantwort zurück.

![Testen einer External-API-Konfiguration mit einer Beispiel-Payload und einer Erfolgsantwort]({% image_buster /assets/img/lemnisk/test_ext_api.png %})

Als Nächstes überprüfen Sie, ob Ihre Ereignisse erfolgreich an Braze gesendet werden. Gehen Sie im Braze-Dashboard zu **Zielgruppe** > **Nutzer:innen suchen** und geben Sie dann einen der Bezeichner aus Ihrer External-API-Konfiguration ein (z. B. eine E-Mail-Adresse). Wenn alles korrekt funktioniert, wird das Profil aufgelistet, das Ihren Test-API-Trigger erhalten hat.

![Anzeigen des Profils und der Aktivitätsübersicht einer Nutzerin bzw. eines Nutzers in Braze]({% image_buster /assets/img/lemnisk/braze_cov.png %})

### Schritt 3: Triggern von Nutzer:innen-Ereignissen in Braze {#step-3-trigger-user-events-in-braze}

1. Erstellen Sie in Lemnisk ein neues Segment. Sie könnten zum Beispiel ein Segment erstellen, das Informationen an Braze sendet, sobald Nutzer:innen ein Lead-Formular absenden.
2. Gehen Sie in Ihrem neuen Segment zu **External API** > **Add Engagement**.
3. Geben Sie unter **Engagement Creation** die grundlegenden Details ein und wählen Sie die Konfiguration aus, [die Sie zuvor erstellt haben](#create-a-braze-external-api).
4. Unter **Configure Parameters** finden Sie die Eingaben für die Braze-Parameter, die Sie auf Engagement-Ebene freigegeben haben. Im folgenden Beispiel werden _Name of the User_, _Product ID_ und _Event Time_ angezeigt.
    ![Erstellen eines Engagements zum Senden von Nutzerdaten an Braze]({% image_buster /assets/img/lemnisk/create_an_engagement.png %})
5. Geben Sie die relevanten Personalisierungsvariablen für die gewählten Parameter ein und wählen Sie dann **Save**.
6. Wenn Sie fertig sind, aktivieren Sie das Engagement.