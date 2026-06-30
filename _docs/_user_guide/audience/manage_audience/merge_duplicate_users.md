---
nav_title: Merge duplicate users
article_title: Merge Duplicate Users
description: "Learn how to find and merge duplicate users in your Braze dashboard."
page_order: 4
---

# Merge duplicate users

> Learn how to find and merge duplicate users, so you can maximize the effectiveness of your campaigns and Canvases.

## REST API: Identify and merge users

The tools on this page merge duplicate profiles in the dashboard. You can also combine or re-point profiles through Braze's [User Data endpoints]({{site.baseurl}}/api/endpoints/user_data/):

- [POST: Identify users]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) (`/users/identify`): Combines an alias-only, email-only, or phone number-only profile with a profile that has an `external_id`.
- [POST: Merge users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) (`/users/merge`): Merges one user profile into another, including when both profiles already have an `external_id`. Review [Prerequisites]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#prerequisites) and [Merge behavior]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior) before you call this endpoint.

When an anonymous profile is matched to an existing identified profile (for example through an SDK `changeUser()` call or `/users/identify`), Braze orphans the anonymous profile and copies only certain fields onto the identified profile. For more information, see [What happens when you identify anonymous users]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#what-happens-when-you-identify-anonymous-users).

User merges are difficult to undo. If you're planning a complex merge across multiple `external_id` values or large profile migrations, contact your Braze customer success manager for guidance before you rely on `/users/merge`.

Braze handles three user types differently when merging: users marked for deletion, test users, and Global Control Group users. For details, see [User merge behavior]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior/).

## Individual merging

If a user search returns duplicate profiles, you can merge each profile individually from the user's profile in the Braze dashboard.

### Step 1: Search for a duplicate profile

In Braze, select **Audience** > **User Search**.

![The "User Search" tile highlighted in the navigation menu.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

Enter a unique identifier, such as an email address or phone number, for the duplicate profile, then select **Search**.

![The "User Search" page in the Braze dashboard.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### Step 2: Merge duplicates

To begin the merge process, select **Merge duplicates**.

![One of the duplicate user's profiles.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

Choose which user profile to keep and which to merge, then select **Merge profiles**. Repeat this process until you've merged all duplicate profiles.


{% alert warning %}
Duplicate user profiles cannot be recovered after merging.
{% endalert %}

## Bulk merging

When you bulk merge duplicate users, Braze finds profiles with matching identifiers (such as an email address) and keeps one profile. Braze first prioritizes profiles with an `external_id`, then applies your **Resolving ties** settings: **Resolve ties using** and **Prioritization**. If there are no profiles with an `external_id`, Braze uses **Resolve ties using** and **Prioritization** across profiles without an `external_id`. Braze only merges users when these settings identify one profile to keep. For example, if **Resolve ties using** is **Updated date** and both profiles have the same last updated timestamp, Braze can't resolve the tie, so those users aren't merged.

### Step 1: Go to Manage Audience

In the Braze dashboard, select **Audience** > **Manage Audience**.

![The "Manage Audience" tile highlighted in the navigation menu.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### Step 2: Preview the results (optional)

To preview your results before merging your duplicates, select **Generate list of duplicates**.

![The "Manage Audience" page with "Generate list of duplicates" highlighted.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze generates your preview and sends it to your email address as a CSV file.

The CSV includes a **Created from** column that shows how each profile was first created (for example, through the [SDK]({{site.baseurl}}/developer_guide/sdk_integration/), [REST API]({{site.baseurl}}/api/basics/), or [CSV import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)). This helps you understand the profile's source before you merge duplicates.

When reviewing duplicate rows, compare **Created from** with identifiers such as `external_id`, email address, and phone number. Use this context to decide which profile should be kept as the primary profile before you select **Merge all duplicates**.

The **Created from** field is especially useful when duplicate profiles contain similar values but come from different ingestion paths. It gives your team more context for merge decisions and helps reduce accidental merges of profiles you would prefer to keep separate until further review.


In the following example, Braze uses the user's external ID to flag duplicate profiles and identify which one to keep. If these profiles are bulk merged, Braze uses the profile with an external ID as the user's new primary profile.

{% tabs local %}
{% tab example csv file %}
| Email Address    | External ID | Phone Number   | Braze ID              | Identifier for rule | Created from | Profile to keep | Profile to merge |
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | ------------ | --------------- | ---------------- |
| jane.doe@example.com   | 123-external-id | 555 123-4567 | example-id-12345 | email               | sdk          | TRUE            | FALSE            |
| john.doe@example.com   |                 | 555 123-4567 | example-id-12346 | email               | rest         | FALSE           | TRUE             |
| jordan.do@example.com |                 | 555 123-4567 | example-id-12347 | email               | csv          | FALSE           | TRUE             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 2: Preview the results (optional)" }
{% endtab %}
{% endtabs %}

#### Merge behavior

Braze will fill empty fields on the kept profile with values from the merged profile. For a list of the fields that will be filled, refer to [Merge behavior]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

### Step 3: Merge your duplicates

If you're satisfied with the results of your preview, select **Merge all duplicates**.

{% alert warning %}
Duplicate user profiles cannot be recovered after merging.
{% endalert %}


## Rules-based merging

You can use rules to control how duplicate profiles are resolved when running a merge so the most relevant user profile is kept. When rules are set, Braze will keep profiles that match your criteria.

### Step 1: Define your rules

1. Go to **Audience** > **Manage Audience** > **Edit rules**.
2. In the **Profile to keep** section of the **Edit rules** panel, select the **Identifier** for the profiles that will be kept when merging duplicates. This can be the email address or phone number.
3. In the **Resolving ties** section, select the criteria to determine how to solve ties between profiles with matching criteria from **Profile to keep**. You can select the following:<br>
- **Resolve ties using**: Created date, Updated date, Last session
- **Prioritization**: Newest, Oldest

![The "Edit rules" panel with sections to select options for "Profile to keep" and "Resolving ties".]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

For example, you could keep the profile that has a phone number. If multiple users have the same phone number, you could resolve ties using the **Updated date** field and prioritize the most recently updated user.

### Step 2: Preview the results (optional)

After saving your rules, you can preview how they'll work by selecting **Generate a list of duplicates**. Braze will generate your preview and send it to your email address as a CSV file that shows which users would be kept and merged if your rules were applied. 

### Step 3: Merge duplicates

If you're satisfied with the results of your preview, return to the **Manage Audience** page and select **Merge all duplicates**.

{% alert warning %}
Duplicate user profiles cannot be recovered after merging.
{% endalert %}

## Scheduled merging

Similar to rules-based merging, scheduled merging allows you to automate the merging of user profiles on a daily basis using preconfigured rules.

![The "Manage Audience" page with "schedule" button.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

After the feature is turned on, Braze will automatically assign a timeslot to perform the merge process daily at approximately 12 am in the user's company time zone. You can turn off scheduled merging at any time. Braze will notify the admins of your workspace 24 hours before the scheduled merge occurs, providing a reminder and time to review the configuration.

{% alert warning %}
Duplicate user profiles cannot be recovered after merging.
{% endalert %}

## Why are multiple user profiles associated with the same email address?

Braze stores multiple user profiles that share the same email address when profiles are created through different identifiers, imports, or anonymous sessions before identification. This is expected behavior when users don't share a single `external_id`.

Before you merge duplicates, use the [Export user profile by identifier endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) to confirm which profiles exist for an email address and which fields each profile contains. You can also search by email in **Audience** > **User Search** to review duplicates in the dashboard.

## Related articles

- [User merge behavior]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior/)
- [POST: Merge users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)
- [Delete users]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/)
