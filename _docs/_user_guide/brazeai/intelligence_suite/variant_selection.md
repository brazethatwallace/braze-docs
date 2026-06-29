---
nav_title: Variant Selection
article_title: Variant Selection
page_order: 1.6
description: "This article covers BrazeAI™ Variant Selection, a feature that enables your A/B campaigns to automatically optimize for the best engagement."
search_rank: 10
toc_headers: h2
---

# BrazeAI™ Variant Selection {#variant-selection}

> BrazeAI™ Variant Selection is a feature that enables your single send or recurring A/B tests to automatically run an experiment and optimize for the best engagement results. 

{% alert note %}
BrazeAI™ Variant Selection is currently only available for push.
{% endalert %}

## Prerequisites

To use BrazeAI™ Variant Selection, you need the following in your campaign or Canvas:

{% tabs %}
{% tab Campaign %}
- Add at least two message variants.
- If you're not using single send, define at least one conversion event and set your re-eligibility window to 24 hours or longer. Shorter windows aren't supported, as they would affect the integrity of the control variant.
{% endtab %}

{% tab Canvas %}
- Include at least two message variants in a Message step.
- If you're not using single send, have at least one conversion event.
{% endtab %}
{% endtabs %}

## Single send

After you add your second variant, BrazeAI™ Variant Selection automatically turns on, setting optimal parameters for the experiment (we've observed an ~25% uplift when following the optimal parameters), runs your experiment, and then sends the winning variant. You don't need to do anything more.

To customize your experiment, we offer the following customizations:

### Optimization goal

We recommend using opens unless you have a strong conversion event setup with a meaningful amount of conversions, so the algorithm has the data it needs to provide the best results.
- Opens
- Conversion Events

### Experiment duration

We recommend using the default; however, we provide two other options, including the ability to use your own custom duration:
- 4 hours
- 24 hours
- 72 hours
- Custom

### Control group and variant distributions

You can remove a control group or edit the variant distributions, but we recommend using the optimal parameters we set.

![Single Send Variant Optimization Options]({% image_buster /assets/img_archive/braze_ai_variant_selection_single_send_options.png %})

## Recurring

After you add your second variant, BrazeAI™ Variant Selection automatically turns on and continuously optimizes by using a multi-armed bandit statistical test. It sends more messages to the variants that perform better and less to those that perform worse. 

It starts with an even distribution to train and optimize, then twice per day tilt the distribution towards high performing variants and away from low performing ones until it gathers enough evidence to feel confident (95%+) it has chosen the optimal distribution.

## Reporting

![Uplift Reporting]({% image_buster /assets/img_archive/braze_ai_variant_selection_reporting.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

After the test completes for single send, and after a short delay for recurring send, we have reliable data to report. We report any uplift BrazeAI™ Variant Selection could achieve in the dashboard.

{% tabs %}
{% tab Single Send %}
After the training cohort sends, Braze waits for the timeframe in the duration setting and reviews the data. Based on the distribution of the competing variants, we calculate an average of what the performance looks like if no optimization was done, then we calculate the uplift based on the winning variant.

For example (assuming an even distribution):
- Variant 1: 3.5%
- Variant 2: 3%
- Variant 3: 2.5%
- Variant 4: 2%

No optimization open rate is 2.75% (.035*.25 + .03*.25 + 0.025*.25 + 0.02*.25), Variant Selection chooses Variant 1, 3.5%, so the uplift is 27.3%
{% endtab %}

{% tab Recurring %}
Braze routinely analyzes the results when we make adjustments and shows the uplift based on the average of each period's uplift. 

We calculate the periods uplift based on how much we adjust, in a similar fashion to single send. 

For example:
- Variant 1: 3.5%, 25% of the cohort
- Variant 2: 3%, 25% of the cohort
- Variant 3: 2.5%, 25% of the cohort
- Variant 4: 2%, 25% of the cohort

No optimization open rate is 2.75% (.035*.25 + .03*.25 + 0.025*.25 + 0.02*.25). Variant Selection more heavily weighs the higher performers. 

Let's say it does the following:
- Variant 1: 65%
- Variant 2: 15%
- Variant 3: 10%
- Variant 4: 5%

This equates to a chosen open rate of 3.075% (.035*.65 + .03*.15 + 0.025*.1 + 0.02*.05), which is an uplift of 11.8%. We calculate that each period, and then average it out over the course of the optimization period.
{% endtab %}
{% endtabs %}

## Frequently asked questions {#faq}

### Why is re-eligibility in less than 24 hours not available when combined with Variant Selection for recurring campaigns or Canvases?

We don't allow Variant Selection campaigns to have re-eligibility in a too-short window because our testing shows it affects the integrity of the control variant and possibly leads to undesirable distributions.

### Why are my variants showing equal sends during the early stages of my recurring campaign?

Variant Selection only determines the final variant allocations after a training period, where sends are sent evenly across variants. It adjusts over time as it notices performance trends. If you don't want to send evenly during the early stages of your campaign, use fixed variants for a traditional A/B test.

### Does recurring Variant Selection stop optimizing without picking a clear winner?

Yes, it stops optimizing when it has 95% confidence that continuing the experiment won't improve the conversion rate by more than 1% of its current rate.

### Why can't I enable Variant Selection in my Canvas or campaign?

For single send, you can't enable Variant Selection if your Canvas or campaign is composed of a single variant.

For recurring, you can't enable Variant Selection if:
- You haven't added conversion events to your campaign or Canvas.
- You have re-eligibility enabled with a window less than 24 hours.
- Your Canvas or campaign is composed of a single variant.