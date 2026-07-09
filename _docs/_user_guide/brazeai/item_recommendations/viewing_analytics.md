---
nav_title: Analytics
article_title: "Item recommendation analytics"
description: "Learn about item recommendation analytics and how to view them in Braze."
page_order: 1.3
---

# Item recommendation analytics

> Learn about item recommendation analytics and how to view them in Braze.

## View analytics

You can view analytics for your recommendation to see which items users were recommended and how accurate the recommendation model was.

1. Go to **Analytics** > **Item Recommendation**.
2. Select your recommendation from the list.

## Available metrics

### Audience

These are metrics related to your recommendation audience, which includes precision, coverage, and personalization rate (for **AI Personalized** recommendations) or recommendation type (for other recommendation types).

![Recommendation audience metrics showing precision, coverage, and recommendation types split between personalized and most popular items.]({% image_buster /assets/img/item_recs_analytics_1.png %})

Refer to the following table for more information:

| Metric              | Description |
| ------------------- | ---------- |
| **Precision**           | The percentage of time the model correctly guessed the next item a user purchased. Precision is heavily dependent on your specific catalog size and mix, and should be used as a guide to understand how often the model is correct.<br><br>In past testing, we have seen models perform well with precision numbers ranging from 6-20%. This metric updates when the model next retrains.  |
| **Coverage**            | What percentage of available items in the catalog are recommended to at least one user. You can expect to see higher item coverage with personalized item recommendations over most popular ones. |
| **Personalization rate** | For **AI Personalized** recommendations, the percentage of users with personalized recommendations stored on their profile, calculated against the total number of users who have performed the configured event in the past 24 months. Users who performed the event but don't have enough data to generate a personalized recommendation receive most popular items as a fallback when messaged. |
| **Recommendation type** | For **Most Recent**, **Most Popular**, and **Trending** recommendations, the percentage of users who receive that recommendation type versus the fallback of most popular items. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Audience" }

### Items

This table includes metrics about your personalized, most recent, and most popular items from your catalog.

![Side-by-side tables listing items assigned to users, separated by personalized recommendations and most popular recommendations.]({% image_buster /assets/img/item_recs_analytics_2.png %})

Refer to the following table for more information:

| Metric              | Description |
| ------------------- | ---------- |
| **Personalized items**<br><br>**Most recent items** | This column lists each item in the catalog in descending order of most often recommended to users. This column also shows how many users were assigned each item by the model.<br><br>Either **Personalized** or **Most recent** items will be listed depending on the [recommendation type]({{site.baseurl}}/user_guide/brazeai/item_recommendations). |
| **Most Popular items** | This column lists each item in the catalog in descending order of popularity. Popularity here refers to items in the catalog that users interact with most often in the entire workspace. Most popular is used as the fallback when personalized or most recent cannot be calculated for an individual user. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Items" }

### Overview

This is an overview of your chosen recommendation configuration, which includes when the recommendation was last updated.

![Recommendation overview table displaying type, catalog, event type, custom event name, property name, and last updated date.]({% image_buster /assets/img/item_recs_analytics_3.png %}){: style="max-width:50%" }
