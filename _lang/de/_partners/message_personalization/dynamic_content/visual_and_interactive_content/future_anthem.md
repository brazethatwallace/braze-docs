---
nav_title: Future Anthem
article_title: Future Anthem
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Future Anthem, einer Realtime-KI-Plattform für Sportwetten- und iGaming-Personalisierung."
alias: /partners/future_anthem/
page_type: partner
search_tag: Partner
---

# Future Anthem

> Die Realtime-KI-Plattform von [Future Anthem](https://www.futureanthem.com/) ermöglicht Personalisierung in den Bereichen Sport, Casino, Bingo und Lotterie. Braze-Kund:innen können Spielerprofile mit branchenspezifischen Attributen anreichern, darunter Lieblingsspiel, Lieblingsteam, Engagement-Score, Empfehlung für die nächste Wette, erwartete nächste Wette und mehr.
>
> Bereitgestellt über Realtime-Erlebnisse, dynamische Zielgruppen und Inhaltsempfehlungen basiert jedes Attribut auf dem Live-Verhalten der Spieler:innen, sodass Braze-Kund:innen im richtigen Moment handeln können.

_Diese Integration wird von Future Anthem gepflegt._

{% alert important %}
Dieses Feature befindet sich derzeit im Early Access. Wenden Sie sich an das Future Anthem Customer-Success-Team, um loszulegen.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Future-Anthem-Konto | Ein Konto bei Future Anthem. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit Berechtigung für den [`users.track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Diesen können Sie im Braze-Dashboard unter **Settings** > **API Keys** erstellen. |
| Braze-REST-Endpunkt | Der Braze-[REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), der zu Ihrer Instanz passt, z. B. `rest.iad-01.com`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Anwendungsfälle {#use-cases}

Mit dieser Integration können Sie:

- Spieler:innen mit hohen Engagement-Scores identifizieren und mit personalisierten Angeboten ansprechen, z. B. exklusiven Aktionen oder VIP-Rewards.
- Ähnliche Spiele vorschlagen, basierend auf den Spielen, die eine Spielerin oder ein Spieler bereits mag.

## Integration

Das Future Anthem Customer-Success-Team hilft Ihnen bei der Einrichtung Ihrer Integration. Wenden Sie sich an Ihren Future Anthem Customer-Success-Kontakt – das Team hilft Ihnen, die relevantesten Attribute zu ermitteln, die an Braze gesendet werden sollen.

| Beispiel-Attribute in Future Anthem | Beispiel-Attribute in Braze |
| ----------------------------------- | --------------------------- |
| ![Future-Anthem-Dashboard mit Profilattributen für einen Spieler.]({% image_buster /assets/img/future_anthem/future_anthem_example_attributes.png %}) | ![Braze-Nutzerprofil mit angepassten Objektattributen, die von Future Anthem synchronisiert wurden.]({% image_buster /assets/img/future_anthem/braze_example_attributes.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Integration" }

## Angepasste Attribute in Braze {#braze-custom-attributes}

Dies sind die verfügbaren angepassten Attribute in Braze. Weitere Informationen finden Sie unter [Future Anthem: Erste Schritte](https://knowledge.futureanthem.com/getting-started).

{% tabs local %}
{% tab Bet Recommendations %}

| Unterkategorie | Beispiel (JSON) | Datentyp |
| ----------- | ---------------- | --------- |
| Nutzerpräferenzen | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}` | Objekt |
| Empfehlungen für Einzelwetten | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}` | Objekt |
| Akkumulator-Wettempfehlungen (Event-Labels) | `{"Bet_1": "Haaland goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}` | Objekt |
| Akkumulator-Wettempfehlungen (numerische Quoten) | `{"Bet_1": 1.5, "Bet_2": 2}` | Objekt |
| Bet-Builder-Wettempfehlungen | `{"Sport":"American Football", "Competition":"NFL", "Event":"Seahawks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"}` | Objekt |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}
{% tab Bonus Recommendations %}

| Unterkategorie | Beispiel | Datentyp |
| ----------- | ------- | --------- |
| NGR (Nettospielertrag, Lifetime) | 2232 | Zahl |
| NGR14 (Nettospielertrag, letzte 14 Aktivitätstage) | 42 | Zahl |
| Spieler-Profitabilitäts-Score | 130 | Zahl |
| Engagement-Score | 0.78 | Zahl |
| Churn-Risiko-Score | 0.02 | Zahl |
| Geschätztes nächstes Wettdatum | 2024-08-29 | Zeit |
| Bet-and-Get-Bonuswert-Empfehlung | 20 | Zahl |
| Weitere Bonuswert-Empfehlungen | 0 | Zahl |
| Zukünftiger CLTV | 3126 | Zahl |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}
{% tab Game Recommendations %}

| Unterkategorie | Beispiel | Datentyp |
| ----------- | ------- | --------- |
| Für Sie empfohlen | Fluffy Favourites, Fishin' Frenzy, Big Bass Bonanza, Rainbow Gold, Wild West | Array |
| Lieblingsspiele | Fishin' Frenzy | Array |
| Empfohlene neue Spiele | Sticky Bees, Beware the Deep Megaways, Gold Party, The Flintstones | Array |
| Spieler:innen wie Sie spielen (kollaboratives Filtern) | Gold Blitz, Big Bass Splash, Rick and Morty, Book of Dead, Gates of Olympus, Luck O' the Irish | Array |
| Weil Sie gespielt haben (Spielähnlichkeit) | Fluffy Favourites 2, Luck O' the Irish Express, Gold Cash, Aztec Treasure Hunt, Stars Bonanza | Array |
| Up Next (Spielabfolge) | Fishin' Frenzy The Big Catch, Big Banker, 9 Masks of Fire, Super Lion, Fishin' Bigger Pots of Gold | Array |
| Beliebte Spiele | Temple of Iris, Fishin' Frenzy, Fishing Reward, Crazy Time, Fluffy Favourites | Array |
| Trendspiele | Pig Banker, Hyper Gold, Pyramid King, Gold Cash | Array |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}

{% tab Player Cluster %}

| Unterkategorie | Beispiel | Datentyp |
| ----------- | ------- | --------- |
| Zeigt, in welchem Cluster sich der Spieler befindet | High Value Game Diverse | String |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}

{% tab Player Sustain (potenzielles Spielerrisiko) %}

| Unterkategorie | Beispiel | Datentyp |
| ----------- | ------- | --------- |
| Risiko-Score | 0.5 | Zahl |
| Riskanter Spieler | True | Boolescher Wert |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}
{% endtabs %}