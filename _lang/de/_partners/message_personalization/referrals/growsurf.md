---
date_published: "2026-09-08"
nav_title: GrowSurf
article_title: GrowSurf
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und GrowSurf, einer Plattform für Empfehlungs- und Affiliate-Programme, die Teilnehmerdaten mit Braze synchronisiert, um Segmentierung und Liquid-Personalisierung zu ermöglichen."
alias: /partners/growsurf/
page_type: partner
search_tag: Partner
---

# GrowSurf

> [GrowSurf](https://www.growsurf.com/) sendet Daten von Empfehlungs- und Affiliate-Programmteilnehmer:innen an Braze-Nutzerprofile. Die Integration fügt Empfehlungslinks, Teilnehmerdetails, Empfehlungsanzahlen, Einladungsanzahlen, Impression-Anzahlen und Meilenstein-Fortschritte als angepasste Attribute hinzu, die Sie für die Braze-Segmentierung und Liquid-Personalisierung verwenden können.

_Diese Integration wird von GrowSurf gepflegt._

## Über die Integration {#about-the-integration}

GrowSurf ist eine Software für Empfehlungs- und Affiliate-Programme. Die unidirektionale Integration stellt die Empfehlungsdaten von GrowSurf-Teilnehmer:innen in Braze bereit, sodass Sie Teilnehmer:innen segmentieren, Nachrichten mit Empfehlungslinks und -fortschritten personalisieren und zeitnahe Programmkommunikation über Braze versenden können.

## Anwendungsfälle {#use-cases}

- Fügen Sie den Empfehlungslink jedes Teilnehmers/jeder Teilnehmerin zu Braze-Nachrichten hinzu.
- Erstellen Sie Segmente basierend auf Empfehlungsstatus, Empfehlungsanzahlen und Meilenstein-Fortschritt.
- Personalisieren Sie Campaigns und Canvases mit Teilnehmer- und Empfehlungsattributen.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
| --- | --- |
| Ein GrowSurf-Konto | Für diese Integration ist ein kostenpflichtiger GrowSurf-Plan erforderlich. |
| Ein Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit `users.track`-Berechtigungen. Erstellen Sie diesen Schlüssel im Braze-Dashboard unter **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**. Weitere Informationen finden Sie unter [REST-API-Schlüssel erstellen]({{site.baseurl}}/api/basics#creating-rest-api-keys). |
| Ein Braze-REST-Endpunkt | Ihre Braze-REST-Endpunkt-URL (zum Beispiel `https://rest.iad-01.braze.com`). Weitere Informationen finden Sie unter [REST-API-Endpunkte]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Befolgen Sie diese Schritte, um ein GrowSurf-Programm mit Braze zu verbinden. Eine schrittweise Anleitung finden Sie in der [GrowSurf-Braze-Integrationsdokumentation](https://docs.growsurf.com/integrations/braze).

### Schritt 1: Einen Braze-REST-API-Schlüssel erstellen {#step-1-create-a-braze-rest-api-key}

1. Gehen Sie in Braze zu **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**.
2. Erstellen Sie einen REST-API-Schlüssel mit `users.track`-Berechtigungen.
3. Kopieren Sie den API-Schlüssel und notieren Sie sich den REST-Endpunkt für denselben Braze-Workspace.

### Schritt 2: Braze in GrowSurf verbinden {#step-2-connect-braze-in-growsurf}

1. Gehen Sie in GrowSurf zu **Program Editor** > **4. Options** > **Integrations** > **Braze**.
2. Wählen Sie den passenden Braze-REST-Endpunkt aus.
3. Geben Sie den REST-API-Schlüssel ein und wählen Sie **Submit**.

### Schritt 3: Die erste Teilnehmer-Synchronisierung überprüfen {#step-3-verify-the-first-participant-sync}

1. Fügen Sie eine:n Testteilnehmer:in in GrowSurf hinzu oder aktualisieren Sie diese:n.
2. Gehen Sie in Braze zu **Zielgruppe** > **Nutzersuche** und suchen Sie nach E-Mail, um das zugehörige Nutzerprofil zu öffnen.
3. Bestätigen Sie, dass die angepassten `grsf_`-Attribute im Profil erscheinen.

## GrowSurf-Attribute in Braze {#growsurf-attributes-in-braze}

GrowSurf stellt 15 Empfehlungsattribute in Braze bereit. Die erste Synchronisierung sendet den vollständigen Satz. Danach sendet GrowSurf Updates, wenn sich Teilnehmerdaten ändern. Wenn ein Wert in GrowSurf entfernt wird, wird das entsprechende Braze-Attribut ebenfalls gelöscht. Zahlenwerte werden als Nummern gesendet.

### String-Attribute {#string-attributes}

| Angepasstes Attribut | Beschreibung |
| --- | --- |
| `grsf_share_url` | Die Empfehlungs-URL des Teilnehmers/der Teilnehmerin. |
| `grsf_participant_id` | Die GrowSurf-ID des Teilnehmers/der Teilnehmerin. |
| `grsf_referral_status` | Der Empfehlungsstatus des Teilnehmers/der Teilnehmerin. |
| `grsf_participant_first_name` | Der Vorname des Teilnehmers/der Teilnehmerin. |
| `grsf_participant_last_name` | Der Nachname des Teilnehmers/der Teilnehmerin. |
| `grsf_referrer_first_name` | Der Vorname der empfehlenden Person. |
| `grsf_referrer_last_name` | Der Nachname der empfehlenden Person. |
| `grsf_referrer_email` | Die E-Mail-Adresse der empfehlenden Person. |
| `grsf_next_milestone` | Der nächste Meilenstein, auf den der/die Teilnehmer:in hinarbeitet. |
| `grsf_next_monthly_milestone` | Der nächste monatliche Meilenstein, auf den der/die Teilnehmer:in hinarbeitet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="String-Attribute" }

### Zahlen-Attribute {#number-attributes}

| Angepasstes Attribut | Beschreibung |
| --- | --- |
| `grsf_total_referral_count` | Die Gesamtanzahl der Empfehlungen des Teilnehmers/der Teilnehmerin. |
| `grsf_monthly_referral_count` | Die Empfehlungsanzahl des Teilnehmers/der Teilnehmerin für den aktuellen Monat. |
| `grsf_prev_monthly_referral_count` | Die Empfehlungsanzahl des Teilnehmers/der Teilnehmerin für den vorherigen Monat. |
| `grsf_total_invite_count` | Die Gesamtanzahl der Einladungen des Teilnehmers/der Teilnehmerin. |
| `grsf_total_impression_count` | Die Gesamtanzahl der Impressions des Empfehlungslinks des Teilnehmers/der Teilnehmerin. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zahlen-Attribute" }

## GrowSurf mit Braze verwenden {#use-growsurf-with-braze}

Verwenden Sie GrowSurf-Empfehlungsattribute für die Braze-Segmentierung und Liquid-Personalisierung. GrowSurf aktualisiert diese Attribute, wenn ein:e Teilnehmer:in hinzugefügt wird oder sich deren Empfehlungsdaten ändern. Sie können auch Teilnehmer:innen synchronisieren, die bereits in Ihrem Programm waren.

### Schritt 1: Segmente erstellen {#step-1-build-segments}

1. Erstellen Sie in Braze ein Segment mit den relevanten angepassten `grsf_`-Attributen.
2. Zielen Sie auf Teilnehmer:innen ab oder schließen Sie diese aus – basierend auf Empfehlungsstatus, Empfehlungsanzahlen oder Meilenstein-Fortschritt.

### Schritt 2: Nachrichten personalisieren {#step-2-personalize-messages}

1. Fügen Sie das angepasste Attribut `grsf_share_url` mit Liquid zu einer Braze-Nachricht hinzu: {% raw %}`{{custom_attribute.${grsf_share_url}}}`{% endraw %}.

{: start="2"}
2. Verwenden Sie andere `grsf_`-Attribute, um Empfehlungsstatus, Anzahlen und Meilenstein-Fortschritte zu personalisieren.

## Hinweise {#considerations}

- GrowSurf sendet nur angepasste Attribute. Es werden keine angepassten Events, Käufe oder Abo-Änderungen gesendet.
- GrowSurf identifiziert Braze-Profile anhand der E-Mail-Adresse der Teilnehmer:innen. Wenn kein übereinstimmendes Profil vorhanden ist, erstellt Braze ein reines E-Mail-Profil.
- Wenn dieselbe E-Mail-Adresse zu Teilnehmer:innen in mehr als einem verbundenen GrowSurf-Programm gehört, erscheinen die zuletzt synchronisierten Programmdaten in diesem Braze-Profil.
- Verbinden Sie Braze, bevor Sie Teilnehmer:innen importieren. Um bestehende Teilnehmer:innen zu synchronisieren, verwenden Sie die Synchronisierungsoption für bestehende Teilnehmer:innen in GrowSurf.

## Fehlerbehebung {#troubleshooting}

- Bestätigen Sie, dass der Braze-REST-API-Schlüssel `users.track`-Berechtigungen hat und der ausgewählte REST-Endpunkt zum selben Braze-Workspace gehört.
- Wenn ein:e Teilnehmer:in nicht synchronisiert werden kann, überprüfen Sie, ob die Person eine gültige E-Mail-Adresse hat.
- Prüfen Sie die GrowSurf-Aktivitätsprotokolle des Teilnehmers/der Teilnehmerin auf das Synchronisierungsergebnis.
- GrowSurf wiederholt temporäre Braze-Fehler automatisch. Wenn GrowSurf ein Update nicht bestätigen kann, sendet es beim nächsten Mal, wenn dieses Braze-Profil synchronisiert wird, alle Empfehlungsattribute. Wenn der API-Schlüssel oder der REST-Endpunkt ungültig ist, korrigieren Sie die Einstellungen und verbinden Sie die Integration erneut.

Weitere Details zur Fehlerbehebung finden Sie in der [GrowSurf-Braze-Integrationsdokumentation](https://docs.growsurf.com/integrations/braze#troubleshooting).