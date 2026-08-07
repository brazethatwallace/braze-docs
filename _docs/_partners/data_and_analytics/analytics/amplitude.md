---
nav_title: Amplitude
article_title: Amplitude
description: "Customer guidance for listing and using Amplitude cohorts with Braze."
page_type: partner
search_tag: Partner
noindex: true
---

# Amplitude

> For setup and integration options, see the [Amplitude partner hub]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/).

## FAQ

### Is it possible to pull a list of Amplitude cohorts?

Braze does not provide an API to export a catalog of every Amplitude cohort definition. Use these approaches instead:

1. **In Amplitude:** View and manage cohorts in the Amplitude dashboard before you sync them to Braze.
2. **In Braze:** After a cohort syncs, target users with the **Amplitude Cohorts** segment filter (**Segments** > create or edit a segment). Synced cohort names are prefixed with `[Amplitude]` and include the cohort ID.
3. **For import setup:** See [Amplitude cohort import]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import/) and [Amplitude Audiences troubleshooting]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/#we-do-not-have-enough-data-yet-for-this-filter-when-syncing-a-cohort).

For cohort sync errors, confirm user ID alignment and API keys in Amplitude before troubleshooting in Braze.
