---
nav_title: CataBoom
article_title: CataBoom
description: "Erfahren Sie, wie Sie gamifizierte CataBoom-Erlebnisse über Catapult, Request Unique URLs und Connected-Content mit Braze verbinden."
alias: /partners/cataboom/
page_type: partner
search_tag: Partner
---

# CataBoom

> [CataBoom](https://www.cataboom.com/) ist eine Gamification-Plattform. Marken nutzen sie, um interaktive digitale Erlebnisse zu erstellen und zu starten, darunter Glücksrad-Spiele, Quizze und Sofortgewinn-Spiele. Diese Erlebnisse vertiefen das Engagement und sammeln First-Party-Daten.

*Diese Integration wird von CataBoom gepflegt.*

## Über diese Integration {#about-this-integration}

Verwenden Sie die Integration von Braze und CataBoom, um personalisierte Spiel-Links zu Ihren Nachrichten hinzuzufügen. Sie können Nutzer:innen-Bezeichner und Attribute in Echtzeit zwischen Catapult-Campaigns und Braze übergeben. Anschließend können Sie mit diesen Daten personalisierte Campaigns, Trigger und Folge-Journeys erstellen.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
| --- | --- |
| Catapult-Konto | Ein Catapult-Konto ist erforderlich, um diese Integration zu nutzen. |
| Braze-REST-API-Schlüssel (optional) | Wenn Sie Catapult-Webhooks verwenden, benötigen Sie einen Braze-REST-API-Schlüssel mit den Nutzerdaten-Berechtigungen, die Ihr Anwendungsfall erfordert. Erstellen Sie den Schlüssel in Braze unter **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**. |
| Braze-REST-Endpunkt (optional) | Wenn Sie Catapult-Webhooks verwenden, nutzen Sie die REST-Endpunkt-URL, die der Braze-URL für [Ihre Braze-Instanz]({{site.baseurl}}/api/basics/#endpoints) entspricht. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## 1. Schritt: Erstellen Sie Ihr Spielerlebnis {#step-1-create-your-game-experience}

Erstellen Sie Ihr Spielerlebnis in der Catapult-Plattform. Die folgenden Schritte zeigen ein einfaches Glücksrad-Setup, das die Request Unique URL API auf der Seite **Link Configuration** verwendet. CataBoom bietet mehr als 200 Spieloptionen, darunter zufallsbasierte Mechaniken, geschicklichkeitsbasierte Mechaniken und Hilfsmittel wie Stempelkarten und Sammel-und-Gewinn-Spiele. Sie können einen ähnlichen Ablauf für andere Spieltypen verwenden. Weitere Informationen zu CataBoom und Catapult finden Sie auf [der CataBoom-Website](https://www.cataboom.com).

1. Erstellen Sie die Campaign.

Wählen Sie oben rechts **New Campaign** aus. Geben Sie einen Campaign-Namen ein, wählen Sie einen URL-Slug und wählen Sie Ihre Spielkategorie und Ihren Spieltyp aus.

![CataBoom-Dashboard-Formular „New Campaign“ mit Feldern für Campaign-Name, URL, Spielkategorie und Spieltyp.]({% image_buster /assets/img/cataboom/new_campaign.png %})

{: start="2"}
2. Aktivieren Sie die Request Unique URL API.

Wählen Sie im linken Menü **Link Configuration** aus.

Aktivieren Sie auf der Seite **Link Configuration** die Option **Request Unique URL API**. Diese Option erstellt eine System-zu-System-URL, die Sie später in Braze verwenden können, z. B. in einer Content-Card.

![CataBoom-Seite „Link Configuration“ mit aktivierter Request Unique URL API und sichtbarer API-URL.]({% image_buster /assets/img/cataboom/link_configuration.png %})

{: start="3"}
3. Setzen Sie das Play-Tracking auf Account ID.

Wählen Sie im linken Menü **Play Control** aus.

Setzen Sie auf der Seite **Play Control** unter **Play Tracking** die Option **Play Count Tracked By** auf **Account ID Parameter**.

Sie können für jede:n Spieler:in eine Account ID für Tracking, Spiellimits, Webhooks und anderes spielerspezifisches Verhalten übergeben. Andere Systeme bezeichnen die Account ID häufig als Member ID, Player ID, Loyalty ID oder ähnlich.

![CataBoom-Seite „Play Control“ mit „Play Count Tracked By“ auf „Account ID Parameter“ gesetzt.]({% image_buster /assets/img/cataboom/play_control.png %})

Sie haben nun genug konfiguriert, um einen Test in Braze durchzuführen. Die optionalen Schritte unten vervollständigen ein typisches vollständiges Spiel-Setup. Catapult bietet außerdem viele weitere Einstellungen, mit denen Sie das Gameplay anpassen können.

{: start="4"}
4. Fügen Sie Ihre Kreativmaterialien hinzu (optional).

Wählen Sie im linken Menü **Creative** aus.

Laden Sie Ihre Assets hoch. Catapult unterstützt die vollständige Branding-Kontrolle für Ihr Spielerlebnis.

![CataBoom-Seite „Creative“ mit Aktionen zum Herunterladen und Hochladen von Grafiken sowie einer Spielvorschau.]({% image_buster /assets/img/cataboom/creative.png %})

{: start="5"}
5. Konfigurieren Sie Preise für zufallsbasierte Spiele (optional).

Wählen Sie im linken Menü **Summary** aus.

Erweitern Sie auf der Seite **Summary** den Bereich **Prize Options**.

Catapult unterstützt zeitgesteuerte Preise, wahrscheinlichkeitsbasierte Preise oder beides. Verwenden Sie zur Konfiguration **Timed Prizes and Codes**, **Prize Control and Odds Setup** oder beides nach Bedarf.

Die folgenden Screenshots zeigen **Prize Options** in der Campaign-Zusammenfassung und eine einfache Wahrscheinlichkeitskonfiguration mit einer 50-%-Gewinnwahrscheinlichkeit auf Level 1.

![CataBoom-Seite „Summary“ mit erweitertem Bereich „Prize Options“.]({% image_buster /assets/img/cataboom/prize_options_summary.png %})

![CataBoom-Seite „Odds“ mit Preisstufen, Prozentsätzen und Level-Steuerungen.]({% image_buster /assets/img/cataboom/prize_odds.png %})

## 2. Schritt: Erstellen Sie eine Nachricht in Braze {#step-2-create-a-message-in-braze}

Dieses Beispiel zeigt, wie Sie eine **Content-Card** erstellen, die die Request Unique URL von der Seite **Link Configuration** verwendet.

1. Fügen Sie Connected-Content für die Play-URL hinzu.

Fügen Sie in Ihrer Content-Card Text und dynamischen Content nach Bedarf hinzu. Umschließen Sie Ihre CataBoom Request Unique URL mit einem [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)-Tag. Fügen Sie einen `AccountID`-Abfrageparameter hinzu, der ein Braze-Personalisierungs-Tag verwendet, das dem Bezeichner entspricht, den Sie in Catapult nutzen. Das Beispiel verwendet {% raw %}`{{${user_id}}}`{% endraw %}.

Ersetzen Sie die Basis-URL sowie die Abfrageparameter `username` und `password` durch die Werte von der Seite **Link Configuration** Ihrer Campaign in Catapult.

{% raw %}
```liquid
{% connected_content https://secure.cataboom.com/dplayurl/YOUR_CAMPAIGN_SLUG?username=YOUR_API_USERNAME&password=YOUR_API_PASSWORD&AccountID={{${user_id}}} :save result %}
```
{% endraw %}

Verwenden Sie das gespeicherte `result` in Ihrer Card (z. B. als Link-URL oder im Nachrichtentext). Folgen Sie dem Antwortformat der CataBoom-API für Ihre Campaign. Weitere Informationen zu Abfrageparametern und Liquid in URLs finden Sie unter [Einen API-Aufruf durchführen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/).

![Braze Content-Card-Composer mit Connected-Content im Nachrichtenfeld und einer mobilen Vorschau der Card.]({% image_buster /assets/img/cataboom/braze_content_card.png %})

Connected-Content fordert einen eindeutigen Play-Link an, wenn Nutzer:innen die Content-Card öffnen. Sie können weitere Abfrageparameter für individuellere Erlebnisse hinzufügen.