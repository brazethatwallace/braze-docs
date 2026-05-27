---
nav_title: DailyPlay
article_title: DailyPlay
description: "Erfahren Sie, wie Sie die Markenspiele und Rewards von DailyPlay mit Braze verbinden, um Spieldaten zu synchronisieren, Zielgruppen zu segmentieren und personalisierte Campaigns zu triggern."
alias: /partners/dailyplay/
page_type: partner
search_tag: Partner
---

# DailyPlay

> [DailyPlay](https://dailyplay.ai/) ist eine Gamification-Plattform. Nutzen Sie sie, um personalisierte Markenspiele und integrierte Reward-Systeme zu starten, die das Engagement vertiefen und die Bindung verbessern.

*Diese Integration wird von DailyPlay gepflegt.*

## Über diese Integration {#about-this-integration}

Die Integration von Braze und DailyPlay ermöglicht es Ihnen, Spiele und Reward-Performance über Zielgruppen-Segmente hinweg bereitzustellen und zu verfolgen. Die Spiele und Reward-Systeme von DailyPlay arbeiten mit der Orchestrierungs-Engine von Braze zusammen, sodass Sie passive Zielgruppen in aktive Teilnehmer:innen verwandeln können.

Sie können Spiel-Meilensteine, Reward-Einlösungen und Engagement-Metriken an Braze senden, um Zielgruppen-Segmente zu erstellen und automatisierte, kanalübergreifende Nachrichten basierend auf dem Spielverhalten zu triggern. Mit dieser Integration können Sie:

- **Nutzerprofile anreichern:** Übergeben Sie Spielmetriken, Punktestände und Reward-Status an Nutzerprofile in Braze.
- **Erweiterte Segmentierung freischalten:** Erstellen Sie Zielgruppen-Segmente basierend auf dem Spielverhalten, z. B. Top-Scorer, aktuelle Gewinner:innen oder Nutzer:innen, die kurz davor stehen, einen Reward freizuschalten.
- **Realtime-Campaigns automatisieren:** Triggern Sie personalisierte kanalübergreifende Nachrichten (Push, E-Mail, In-App) basierend auf Spielinteraktionen, um wiederholtes Spielen, Markentreue und einen höheren Lifetime-Value zu fördern.

## Anwendungsfälle {#use-cases}

- **Inaktive Kund:innen erneut ansprechen:** Senden Sie einen Link zu einem Spiel mit der Chance, einen Rabatt-Reward zu gewinnen, an inaktive Kund:innen.
- **Aktivität rund um Produkte und Trends:** Erstellen Sie personalisierte Spiele, die ein neues Produkt oder eine Feiertagssaison, einen Trend oder ein Event präsentieren.
- **Gezielte Spiele bereitstellen:** Kombinieren Sie Braze-Segmentierung und -Targeting mit DailyPlay-Personalisierung, um ansprechende Spielinhalte für verschiedene Ziele und Ergebnisse zu erstellen.
- **Onboarding und Aktivierung:** Betten Sie einen DailyPlay-Rubbellos- oder Sofort-Enthüllungs-Spiellink in Ihre Braze-Willkommensserie ein, um einen Erstkauf oder die Profilvervollständigung zu incentivieren.
- **Bindung und Loyalität:** Wenn Verbraucher:innen einen Loyalitäts-Meilenstein erreichen oder eine wichtige Aktion ausführen, die in Braze verfolgt wird, triggern Sie ein personalisiertes DailyPlay-Spiel, das ihre Leistung feiert und stufenspezifische Rewards freischaltet.
- **Churn-Prävention und Rückgewinnung:** Identifizieren Sie Nutzer:innen, die in Braze abzuwandern drohen, und liefern Sie dann ein niedrigschwelliges DailyPlay-Spiel, um ihre Aufmerksamkeit zurückzugewinnen und sie zurück zu Ihrer App oder Website zu führen.

## Voraussetzungen {#prerequisites}


| Anforderung | Beschreibung |
| --- | --- |
| DailyPlay-Konto | Ein DailyPlay-Konto ist erforderlich, um diese Integration zu nutzen. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit `users.track`-Berechtigungen. Erstellen Sie diesen Schlüssel in Braze unter **Settings** > **APIs and Identifiers** > **API Keys**. Weitere Informationen finden Sie unter [API-Schlüssel]({{site.baseurl}}/api/api_key/). |
| Braze REST-Endpunkt | Die REST-Endpunkt-URL für [Ihre Braze-Instanz]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### 1. Schritt: Verbindung erstellen {#step-1-create-a-connection}

1. Gehen Sie im [DailyPlay-Dashboard](https://app.dailyplay.ai/connections) zur Seite **Connections** und wählen Sie **Add Connection**.

![DailyPlay-Connections-Seite mit aktiven Braze-Verbindungen und Trigger-Statistiken.]({% image_buster /assets/img/dailyplay/connections_page.png %}){: style="max-width:70%;"}

{: start="2"}
2. Wählen Sie unter **Provider** die Option **Braze**. Geben Sie einen Namen, Ihren Braze REST-API-Schlüssel, die App-ID und den REST-Endpunkt ein und wählen Sie dann **Create Connection**.

![DailyPlay-Modal „Add Connection“ mit ausgewähltem Braze und Zugangsdatenfeldern für API-Schlüssel, App-ID und REST-Endpunkt.]({% image_buster /assets/img/dailyplay/add_connection.png %}){: style="max-width:60%;"}

### 2. Schritt: Stream erstellen {#step-2-create-a-stream}

Gehen Sie zur Seite **Streams** und erstellen Sie einen neuen Stream.

1. Fügen Sie die in [Schritt 1](#schritt-1-verbindung-erstellen) erstellte Braze-Verbindung zum neuen Stream hinzu.
2. Konfigurieren Sie die zu verfolgenden Trigger-Events, z. B. **Stream Access**, **Play Start**, **Play Complete** und **Prize Redemption**.
3. Erstellen Sie Spiele und fügen Sie sie dem Stream hinzu.
4. Kopieren Sie den Braze-Integrationscode für den Stream.

![DailyPlay-Modal „Manage Connections“ mit Braze-Trigger-Events und dem Einbettungscode für Braze-E-Mail-Templates.]({% image_buster /assets/img/dailyplay/manage_connections.png %}){: style="max-width:70%;"}

### 3. Schritt: Campaign in Braze erstellen {#step-3-create-a-campaign-in-braze}

Fügen Sie den Code aus Schritt 2 in Ihre Campaign in Braze ein.

Wenn Nutzer:innen Spiele im Stream spielen, triggert DailyPlay ein Event und sendet es über Ihren Braze REST-Endpunkt an Braze.

### 4. Schritt: Aktionen überprüfen und Ihren Funnel erweitern {#step-4-inspect-actions-and-expand-your-funnel}

Nutzer:innen, die Aktionen in DailyPlay-Streams abschließen, erhalten angepasste Attribute und angepasste Events in ihrem Braze-Profil.

Erstellen Sie eine [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/) oder ein [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/) mit einem [aktionsbasierten]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/) Trigger, der die für Ihren Anwendungsfall erforderlichen angepassten DailyPlay-Events oder angepassten Attribute verwendet.

## DailyPlay mit Braze verwenden {#use-dailyplay-with-braze}

Um ein bestimmtes Kundensegment anzusprechen, führen Sie diese Schritte aus, nachdem Sie die Integrationseinrichtung abgeschlossen haben.

### 1. Schritt: DailyPlay-Konfiguration einrichten {#step-1-set-up-your-dailyplay-configuration}

Folgen Sie den obigen Integrationsschritten, um Ihre Braze-Verbindung und Ihren DailyPlay-Stream einzurichten. Kopieren Sie den Integrationscode.

### 2. Schritt: Braze-Campaign oder Canvas erstellen {#step-2-create-a-braze-campaign-or-canvas}

Erstellen Sie eine Campaign oder ein Canvas mit einem aktionsbasierten Trigger. Wählen Sie die für Ihren Anwendungsfall erforderlichen angepassten DailyPlay-Events oder angepassten Attribute aus.

Sie können [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) verwenden, um Eigenschaften zu referenzieren, die DailyPlay in Ihrem Nachrichtentext sendet.

**Beispiel für angepasstes Attribut:**

{% raw %}
```liquid
Your score was {{custom_attribute.${dailyplay}.last_game_score}}
```
{% endraw %}

**Beispiel für angepasstes Event:**

Verwenden Sie die Punkt-Notation, um Eigenschaften des Trigger-Events zu referenzieren:

{% raw %}
```liquid
{{event_properties.${dailyplay_play_complete}.properties.score}}
```
{% endraw %}

## Fehlerbehebung {#troubleshooting}

Weitere Anleitungen zur Einrichtung und häufig gestellte Fragen finden Sie in der [DailyPlay-Braze-Integrationsdokumentation](https://docs.dailyplay.ai/connections/braze/).