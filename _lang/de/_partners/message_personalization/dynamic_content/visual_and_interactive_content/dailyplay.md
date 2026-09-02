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

Die Integration von Braze und DailyPlay ermöglicht es Ihnen, Spiele bereitzustellen und die Performance von Spielen und Rewards über verschiedene Zielgruppen-Segments hinweg zu verfolgen. Die Spiele und Reward-Systeme von DailyPlay arbeiten mit der Orchestrierungs-Engine von Braze zusammen, sodass Sie passive Zielgruppen in aktive Teilnehmer:innen verwandeln können.

Sie können Gameplay-Meilensteine, Reward-Einlösungen und Engagement-Metriken an Braze senden, um Zielgruppen-Segments aufzubauen und automatisiertes, kanalübergreifendes Messaging basierend auf In-Game-Verhalten zu triggern. Mit dieser Integration können Sie:

- **Nutzerprofile anreichern:** Übergeben Sie Gameplay-Metriken, Punktestände und Reward-Status an Nutzerprofile in Braze.
- **Erweiterte Segmentierung freischalten:** Erstellen Sie Zielgruppen-Segments basierend auf In-Game-Verhalten, z. B. Top-Scorer, kürzliche Gewinner:innen oder Nutzer:innen, die kurz davor stehen, einen Reward freizuschalten.
- **Realtime-Campaigns automatisieren:** Triggern Sie personalisierte kanalübergreifende Nachrichten (Push, E-Mail, In-App) basierend auf Spiel-Interaktionen, um wiederholtes Spielen, Markentreue und einen höheren LTV zu fördern.

## Anwendungsfälle {#use-cases}

- **Inaktive Kund:innen erneut ansprechen:** Senden Sie inaktiven Kund:innen einen Link zu einem Spiel mit der Chance, einen Rabatt als Reward zu gewinnen.
- **Aktivitäten rund um Produkte und Trends:** Erstellen Sie personalisierte Spiele, die ein neues Produkt, eine Saison, einen Trend oder ein Event hervorheben.
- **Gezielte Spiele einsetzen:** Kombinieren Sie die Segmentierung und das Targeting von Braze mit der DailyPlay-Personalisierung, um ansprechende Spielinhalte für verschiedene Ziele und Ergebnisse zu erstellen.
- **Onboarding und Aktivierung:** Binden Sie einen DailyPlay-Rubbellos- oder Sofortgewinn-Spiellink in Ihre Braze-Willkommensserie ein, um einen Erstkauf oder die Vervollständigung des Profils zu fördern.
- **Bindung und Treue:** Wenn Verbraucher:innen einen Meilenstein in der Kundenbindung erreichen oder eine wichtige Aktion ausführen, die in Braze getrackt wird, triggern Sie ein personalisiertes DailyPlay-Spiel, das ihre Leistung feiert und stufenspezifische Rewards freischaltet.
- **Abwanderung-Prävention und Rückgewinnung:** Identifizieren Sie Nutzer:innen, die in Braze abzuwandern drohen, und senden Sie ihnen ein unkompliziertes DailyPlay-Spiel, um ihre Aufmerksamkeit zurückzugewinnen und sie wieder zu Ihrer App oder Website zu führen.

## Voraussetzungen {#prerequisites}


| Anforderung | Beschreibung |
| --- | --- |
| DailyPlay-Konto | Für diese Integration ist ein DailyPlay-Konto erforderlich. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit `users.track`-Berechtigungen. Erstellen Sie diesen Schlüssel in Braze unter **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**. Weitere Informationen finden Sie unter [API-Schlüssel]({{site.baseurl}}/api/basics). |
| Braze-REST-Endpunkt | Die REST-Endpunkt-URL für [Ihre Braze-Instanz]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Verbindung erstellen {#step-1-create-a-connection}

1. Gehen Sie im [DailyPlay-Dashboard](https://app.dailyplay.ai/connections) zur Seite **Connections** und wählen Sie **Add Connection**.

![DailyPlay-Connections-Seite mit aktiven Braze-Verbindungen und Trigger-Statistiken.]({% image_buster /assets/img/dailyplay/connections_page.png %}){: style="max-width:70%;"}

{: start="2"}
2. Wählen Sie unter **Provider** die Option **Braze**. Geben Sie einen Namen, Ihren Braze REST-API-Schlüssel, die App-ID und den REST-Endpunkt ein und wählen Sie dann **Create Connection**.

![DailyPlay-Modal „Add Connection“ mit ausgewähltem Braze und Zugangsdatenfeldern für API-Schlüssel, App-ID und REST-Endpunkt.]({% image_buster /assets/img/dailyplay/add_connection.png %}){: style="max-width:60%;"}

### Schritt 2: Stream erstellen {#step-2-create-a-stream}

Gehen Sie zur Seite **Streams** und erstellen Sie einen neuen Stream.

1. Fügen Sie die in Schritt 1 erstellte Braze-Verbindung zum neuen Stream hinzu.
2. Konfigurieren Sie die zu verfolgenden Trigger-Events, z. B. **Stream Access**, **Play Start**, **Play Complete** und **Prize Redemption**.
3. Erstellen Sie Spiele und fügen Sie sie dem Stream hinzu.
4. Kopieren Sie den Braze-Integrationscode für den Stream.

![DailyPlay-Modal „Manage Connections“ mit Braze-Trigger-Events und dem Einbettungscode für Braze-E-Mail-Templates.]({% image_buster /assets/img/dailyplay/manage_connections.png %}){: style="max-width:70%;"}

### Schritt 3: Campaign in Braze erstellen {#step-3-create-a-campaign-in-braze}

Fügen Sie den Code aus Schritt 2 in Ihre Campaign in Braze ein.

Wenn Nutzer:innen Spiele im Stream spielen, triggert DailyPlay ein Event und sendet es über Ihren Braze REST-Endpunkt an Braze.

### Schritt 4: Aktionen überprüfen und Ihren Funnel erweitern {#step-4-inspect-actions-and-expand-your-funnel}

Nutzer:innen, die Aktionen in DailyPlay-Streams abschließen, erhalten angepasste Attribute und angepasste Events in ihrem Braze-Profil.

Erstellen Sie eine [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) oder ein [Canvas]({{site.baseurl}}/user_guide/messaging/canvas) mit einem [aktionsbasierten]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) Trigger, der die für Ihren Anwendungsfall erforderlichen angepassten DailyPlay-Events oder angepassten Attribute verwendet.

## DailyPlay mit Braze verwenden {#use-dailyplay-with-braze}

Um ein bestimmtes Kundensegment anzusprechen, führen Sie nach Abschluss der Integrationseinrichtung die folgenden Schritte aus.

### Schritt 1: DailyPlay-Konfiguration einrichten {#step-1-set-up-your-dailyplay-configuration}

Befolgen Sie die Integrationsschritte in diesem Abschnitt, um Ihre Braze-Verbindung und Ihren DailyPlay-Stream einzurichten. Kopieren Sie den Integrationscode.

### Schritt 2: Braze-Campaign oder Canvas erstellen {#step-2-create-a-braze-campaign-or-canvas}

Erstellen Sie eine Campaign oder ein Canvas mit einem aktionsbasierten Trigger. Wählen Sie die angepassten Events oder angepassten Attribute von DailyPlay aus, die für Ihren Anwendungsfall erforderlich sind.

Sie können [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) verwenden, um in Ihrem Nachrichtentext auf Eigenschaften zu verweisen, die DailyPlay sendet.

**Beispiel für ein angepasstes Attribut:**

{% raw %}
```liquid
Your score was {{custom_attribute.${dailyplay}.last_game_score}}
```
{% endraw %}

**Beispiel für ein angepasstes Event:**

Verwenden Sie die Punktnotation, um auf Eigenschaften des Trigger-Events zu verweisen:

{% raw %}
```liquid
{{event_properties.${dailyplay_play_complete}.properties.score}}
```
{% endraw %}

## Fehlerbehebung {#troubleshooting}

Weitere Hinweise zur Einrichtung und häufig gestellte Fragen finden Sie in der [Dokumentation zur DailyPlay-Braze-Integration](https://docs.dailyplay.ai/connections/braze/).