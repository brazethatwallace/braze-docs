---
nav_title: Future Anthem
article_title: Future Anthem
description: "This reference article outlines the partnership between Braze and Future Anthem, a real-time AI platform for sports betting and iGaming personalization."
alias: /partners/future_anthem/
page_type: partner
search_tag: Partner
---

# Future Anthem

> The [Future Anthem](https://www.futureanthem.com/) real-time AI platform powers personalization across sports, casino, bingo, and lottery. Braze customers can enrich player profiles with industry-specific attributes, including favorite game, favorite team, engagement score, next bet recommendation, expected next bet, and more.
>
> Delivered through Real-time Experiences, Dynamic Audiences, and Content Recommendations, every attribute is built on live player behavior, so Braze customers can act in the moment.

_This integration is maintained by Future Anthem._

{% alert important %}
This feature is currently in early access. Contact the Future Anthem Customer Success team to get started.
{% endalert %}

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Future Anthem account | A Future Anthem account. |
| Braze REST API key | A Braze REST API key with permission for the [`users.track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). You can create this in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | The Braze [REST endpoint]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) that matches your instance, such as `rest.iad-01.com`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Use cases

With this integration, you can:

- Identify players with high engagement scores and target them with personalized offers, such as exclusive promotions or VIP rewards.
- Suggest similar games based on the games a player already likes.

## Integration

The Future Anthem Customer Success team helps you set up your integration. Contact your Future Anthem Customer Success contact, and they help you identify the most relevant attributes to send to Braze.

| Example attributes in Future Anthem | Example attributes in Braze |
| ----------------------------------- | --------------------------- |
| ![Future Anthem dashboard showing profile attributes for a player.]({% image_buster /assets/img/future_anthem/future_anthem_example_attributes.png %}) | ![Braze user profile showing custom object attributes synced from Future Anthem.]({% image_buster /assets/img/future_anthem/braze_example_attributes.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Integration" }

## Braze custom attributes

These are the available Braze custom attributes. For more information, see [Future Anthem: Getting Started](https://knowledge.futureanthem.com/getting-started).

{% tabs local %}
{% tab Bet Recommendations %}

| Subcategory | Example (JSON) | Data type |
| ----------- | ---------------- | --------- |
| User preferences | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}` | Object |
| Single bet recommendations | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}` | Object |
| Accumulator bet recommendations (event labels) | `{"Bet_1": "Haaland goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}` | Object |
| Accumulator bet recommendations (numeric odds) | `{"Bet_1": 1.5, "Bet_2": 2}` | Object |
| Bet Builder bet recommendations | `{"Sport":"American Football", "Competition":"NFL", "Event":"Seahawks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"}` | Object |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}
{% tab Bonus Recommendations %}

| Subcategory | Example | Data type |
| ----------- | ------- | --------- |
| NGR (net gaming revenue, lifetime) | 2232 | Number |
| NGR14 (net gaming revenue, last 14 days of activity) | 42 | Number |
| Player profitability score | 130 | Number |
| Engagement score | 0.78 | Number |
| Churn risk score | 0.02 | Number |
| Estimated next bet date | 2024-08-29 | Time |
| Bet and Get bonus value recommendation | 20 | Number |
| Other bonus value recommendations | 0 | Number |
| Future CLTV | 3126 | Number |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}
{% tab Game Recommendations %}

| Subcategory | Example | Data type |
| ----------- | ------- | --------- |
| Recommended For You | Fluffy Favourites, Fishin' Frenzy, Big Bass Bonanza, Rainbow Gold, Wild West | Array |
| Favorite games | Fishin' Frenzy | Array |
| Recommended new games | Sticky Bees, Beware the Deep Megaways, Gold Party, The Flintstones | Array |
| Players like you are playing (collaborative filtering) | Gold Blitz, Big Bass Splash, Rick and Morty, Book of Dead, Gates of Olympus, Luck O' the Irish | Array |
| Because you played (game similarity) | Fluffy Favourites 2, Luck O' the Irish Express, Gold Cash, Aztec Treasure Hunt, Stars Bonanza | Array |
| Up Next (game sequencing) | Fishin' Frenzy The Big Catch, Big Banker, 9 Masks of Fire, Super Lion, Fishin' Bigger Pots of Gold | Array |
| Popular games | Temple of Iris, Fishin' Frenzy, Fishing Reward, Crazy Time, Fluffy Favourites | Array |
| Trending games | Pig Banker, Hyper Gold, Pyramid King, Gold Cash | Array |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}

{% tab Player Cluster %}

| Subcategory | Example | Data type |
| ----------- | ------- | --------- |
| Showcase what cluster the player is in | High Value Game Diverse | String |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}

{% tab Player Sustain (player potential risk) %}

| Subcategory | Example | Data type |
| ----------- | ------- | --------- |
| Risk score | 0.5 | Number |
| Risky player | True | Boolean |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}
{% endtabs %}
