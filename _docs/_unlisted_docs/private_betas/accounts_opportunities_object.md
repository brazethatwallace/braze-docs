---
nav_title: Account Objects
article_title: Account Objects
page_type: reference
permalink: /account_object/
hidden: true
description: "Learn how to use account objects to build segments of users based on what account they belong to, then send personalized messages using Liquid tags."
---

# Account objects

> Learn how to use account objects to build segments of users based on what account they belong to, then send personalized messages using Liquid tags.

To import account data, use a [CSV file](#using-a-csv-file) or the Braze API. Using the Braze API, you can [create multiple accounts](#create-multiple-accounts), [create one account](#create-one-account), [delete multiple accounts](#delete-multiple-accounts), and [delete one account](#delete-one-account).

| Audience | How you'll use this article |
|----------|----------------------------|
| Marketers | Import user and account data using CSV, build segments based on account attributes, and personalize messages with account information in Braze. |
| Developers | Use the Braze REST API to create, update, and delete account records programmatically and keep Braze in sync with your data. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Account objects are currently in beta. Contact your Braze account manager if you're interested in participating in this beta.
{% endalert %}

## How it works

Account objects are custom data structures that represent a user's company. They connect to user profiles, so you can build B2B-style segments and personalize messages. Use account fields like company name, industry, role, or deal status with Braze catalogs, segmentation filters, and Liquid tags.

For example, you can target users who work in healthcare and send personalized messages to physicians and hospital administrators to make your message even more relevant.

To use account objects, you import three types of data into Braze:

- **User data:** Individual user profiles used to identify each person in Braze (for example, via `external_id`, email, phone, or user alias). Import user data via CSV.
- **User-account relationship data:** The relationship between a user and an account, including which company they belong to and the role they have at that account. Import this relationship data via CSV.
- **Account data:** The company records itself, such as company name, industry, annual revenue, and other firmographic details. These are the records you target and personalize against in segments and messages. Import account data via CSV or the Braze REST API.

All three data types must be imported for account objects to work. User data identifies people in Braze, user-account relationship data connects those users to specific accounts and roles, and account data provides the company-level attributes used for segmentation and personalization.

## Prerequisites

Before you can use this feature, you must have users in Braze already.

## Import data to Braze

To use account objects within your messages, your user data should already exist in Braze. From there, complete two imports: first, import user-account relationship data to establish account associations and roles (currently via CSV only). Then, import account data with the company-level details used for segmentation and personalization (via CSV or the Braze REST API).

### Step 1: Import user-account relationship data

First, import your user-account relationship data to Braze as a CSV file with the following fields. This helps Braze associate existing users with the correct accounts and roles.

<style>
table td {
    word-break: break-word;
}
</style>

| Field name       | Field type | Required | Description                                                                                           |
|------------------|------------|----------|-------------------------------------------------------------------------------------------------------|
| `account_id`       | String     | Yes      | The account the user belongs to. This is the same as the `id` field from the account object (CRM ID). |
| `external_id`      | String     | Yes      | The user's [external ID](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles) in Braze. |
| `user_alias_name`  | String     | No*      | The user's [alias name](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle#user-aliases) in Braze. |
| `user_alias_label` | String     | No*      | The user's [alias label](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle/#what-happens-when-you-identify-anonymous-users) in Braze. |
| `email`            | String     | No*     | The user's email address. |
| `phone`            | String     | No*      | The users's phone number. |
| `user_role`             | String     | No       | The role the user has at the account, such as "directory" or "employee." |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
<sup>**One of `external_id`, `email`, `phone`, or `user_alias` is required to identify a user.*</sup>

#### Using a CSV file

Upload your CSV with user-account relationships to Braze:

1. Go to **Data Settings** > **Accounts**.
2. Select **Update data**.
3. Under **CSV upload**, select **Users**, then upload your file to Braze.

![The "Upload data" dropdown on the "Accounts" page in Braze.]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/update_account_data_csv.png %})

### Step 2: Import account data

Accounts are companies that your users belong to. Import your account data to Braze as a CSV file with the following fields. Keep in mind, each account must be assigned an ID and a name.

<style>
table td {
    word-break: break-word;
}
</style>

| Field name                  | Field type | Required | Description                                                                        |
|-----------------------------|------------|----------|------------------------------------------------------------------------------------|
| `id`                          | String     | Yes      | The account's ID in your Customer Relationship Management (CRM) platform. |
| `name`                        | String     | Yes      | The name of the account.                                                                |
| `type`                        | String     | No       | The type of account, such as a customer, partner, or reseller                                                                                   |
| `annual_revenue`              | String     | No       | Annual revenue of the account.                                                      |
| `industry`                    | String     | No       | Industry in which the account operates.                                             |
| `number_of_employees`         | String     | No       | Number of employees, supports for ranges.                                           |
| `address`                     | String     | No       | Street address of the account.                                                      |
| `city`                        | String     | No       | City where the account is located.                                                  |
| `state`                       | String     | No       | State where the account is located.                                                 |
| `postal_code`                 | String     | No       | Postal code for the account's address.                                              |
| `country`                     | String     | No       | Country where the account is located.                                               |
| `notes`                       | String     | No       | Additional notes about the account.                                                 |
| `website`                     | String     | No       | Website URL for the account.                                                        |
| `main_phone`                  | String     | No       | Main phone number for the account.                                                  |
| `created_date`                | Time       | No       | Date when the account was created.                                                  |
| `account_owner_email_address` | String     | No       | An internal account owner (such as "Tom from Company A sales owns Company B").      |
| `parent_account_id`           | String     | No       | ID of the parent account, if applicable (such as linking to a parent company's ID). |
| `sic_code`                    | String     | No       | Standard industry classification code.                                              |
| Custom fields                 | N/A        | No       | Custom fields that are defined and managed by you.                                                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
{% alert note %}
While some fields are optional, include them when possible because they are reserved field names and help keep your data organized.
{% endalert %}

Next, import your account data to Braze by uploading a CSV file or using the Braze REST API. You can view this data in **Data Settings**. You can't edit this data in the in-browser editor.

#### Use a CSV file {#using-a-csv-file}

To import your data through CSV:

1. Go to **Data Settings** > **Accounts**.
2. Select **Update data**.
3. Under **CSV upload**, select **Account Data**, then upload your file to Braze.

![The "Upload data" dropdown on the "Accounts" page in Braze.]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/update_account_data_csv.png %})

## Use the Braze API {#using-the-braze-api}

APIs (Application Programming Interfaces) allow different software systems to communicate programmatically. When you interact with the Braze API, you send HTTP requests to specific endpoints. Endpoints are structured URLs that accept instructions and return responses. The HTTP method tells Braze what action to perform, and the request body contains the data.

For account management, the Braze API uses these HTTP methods:

| Method | Purpose | Behavior |
|--------|---------|----------|
| `PUT` | Create or update resources | Adds a new account record if one doesn't exist. Updates the existing record if one does. `PUT` is designed to be idempotent, so you can sync the same data multiple times without creating duplicates. |
| `DELETE` | Remove resources | Permanently removes the specified account record and its associations from Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

The Braze API gives you programmatic control over account data at scale. You can automate account management workflows, sync account information directly from your data sources, and keep Braze aligned with your source of truth without manual uploads or edits. This helps reduce operational overhead and maintain accurate, timely account data for segmentation and personalization.

For more information on HTTP methods and how REST APIs work, refer to the following resources:
- [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods) on MDN Web Docs
- [REST API Tutorial](https://restapitutorial.com/)
- [Braze API overview](https://www.braze.com/docs/api/basics)

{% alert note %}
Use an API key with catalogs permissions to authenticate requests to the `/business/accounts` endpoint.
{% endalert %}

This section covers how to use the Braze API to:
- [Create multiple accounts](#create-multiple-accounts)
- [Create one account](#create-one-account)
- [Delete multiple accounts](#delete-multiple-accounts)
- [Delete one account](#delete-one-account)

### Create multiple accounts {#create-multiple-accounts}

Because `PUT` is idempotent, you can send the same request multiple times and Braze updates existing records rather than creating duplicates. This makes it a reliable choice for keeping account records in Braze up to date.

The following code snippet sends a `PUT` request to the `/business/accounts` endpoint. The `accounts` array contains multiple company objects, each mapped to the account fields defined in [Step 2: Import account data](#step-2-import-account-data). Braze processes each object and either creates or updates the corresponding record in your **Accounts** page. This operation is asynchronous. Braze queues the request and processes it in the background, making it well-suited for bulk imports where immediate confirmation isn't required.

To create multiple accounts, send a `PUT` request to `/business/accounts`. If an account doesn't exist, Braze adds a new item in the **Accounts** page. Each request can support up to 50 accounts. Note that this operation is asynchronous.

Your request should be similar to the following:

```plaintext
curl -X PUT https://YOUR_REST_API_URL/business/accounts \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
          "accounts": [
              {
                  "id": "ACC001",
                  "name": "Acme Corporation",
                  "type": "Customer",
                  "annual_revenue": "$5,000,000",
                  "industry": "Manufacturing",
                  "number_of_employees": "150",
                  "address": "123 Industrial Way",
                  "city": "Metropolis",
                  "state": "NY",
                  "postal_code": "10001",
                  "country": "USA",
                  "notes": "Key client in the manufacturing sector",
                  "website": "http://www.acme.com",
                  "main_phone": "+1-212-555-1234",
                  "created_date": "2023-01-15T09:30:00Z",
                  "account_owner_email_address": "owner@acme.com",
                  "parent_account_id": "",
                  "sic_code": "2011"
              },
              {
                  "id": "ACC002",
                  "name": "Global Solutions",
                  "type": "Partner",
                  "annual_revenue": "$10,000,000",
                  "industry": "Technology",
                  "number_of_employees": "500",
                  "address": "456 Tech Park",
                  "city": "Silicon Valley",
                  "state": "CA",
                  "postal_code": "94043",
                  "country": "USA",
                  "notes": "Important partner for software solutions",
                  "website": "http://www.globalsolutions.com",
                  "main_phone": "+1-650-555-5678",
                  "created_date": "2023-02-20T14:45:00Z",
                  "account_owner_email_address": "partner@globalsolutions.com",
                  "parent_account_id": "ACC001",
                  "sic_code": "7372"
              },
              {
                  "id": "ACC003",
                  "name": "Oceanic Ventures",
                  "type": "Customer",
                  "annual_revenue": "$3,200,000",
                  "industry": "Retail",
                  "number_of_employees": "75",
                  "address": "789 Ocean Blvd",
                  "city": "Miami",
                  "state": "FL",
                  "postal_code": "33101",
                  "country": "USA",
                  "notes": "Expanding presence in retail markets",
                  "website": "http://www.oceanicventures.com",
                  "main_phone": "+1-305-555-6789",
                  "created_date": "2023-03-05T08:15:00Z",
                  "account_owner_email_address": "contact@oceanicventures.com",
                  "parent_account_id": "",
                  "sic_code": "5941"
              }
          ]
      }'
```

### Create one account {#create-one-account}

Like creating multiple accounts, this operation uses the `PUT` method. The difference is that the account ID is included directly in the endpoint URL rather than the request body. This gives you precise control over a single record.

The following code snippet sends a `PUT` request to `/business/accounts/ACC001`, where `ACC001` is the unique identifier for the account. This operation is synchronous. Braze processes the request immediately and returns a response as soon as it's complete. This is well-suited for real-time integrations. For example, when account information changes in your system, you can reflect that update in Braze right away for targeting or personalization.

To create one account, send a `PUT` request to `/business/accounts/:account_id`. If the account doesn't exist, Braze creates a new account record. This operation is synchronous.

Your request should be similar to the following:

```plaintext
curl -X PUT https://YOUR_REST_API_URL/business/accounts/ACC001 \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "accounts": [
            {
                "name": "Braze",
                "type": "Customer",
                "annual_revenue": "$5,000,000",
                "industry": "Manufacturing",
                "number_of_employees": "150",
                "address": "123 Industrial Way",
                "city": "Metropolis",
                "state": "NY",
                "postal_code": "10001",
                "country": "USA",
                "notes": "Key client in the manufacturing sector",
                "website": "http://www.acme.com",
                "main_phone": "+1-212-555-1234",
                "created_date": "2023-01-15T09:30:00Z",
                "account_owner_email_address": "owner@acme.com",
                "parent_account_id": "",
                "sic_code": "2011"
            }
        ]
      }'
```

### Delete multiple accounts {#delete-multiple-accounts}

The `DELETE` method removes account records from Braze. Unlike `PUT`, `DELETE` requests are not reversible. Once an account is deleted, the association between users and that account is removed.

The following code snippet sends a `DELETE` request to `/business/accounts` with a list of account IDs in the request body. Braze processes each ID and removes the corresponding account record. This operation is asynchronous. Braze queues the removals and processes them in the background. Use this for bulk cleanup tasks, such as when a group of accounts has churned, been consolidated, or is no longer relevant for segmentation in Braze.

To delete multiple accounts, send a `DELETE` request to `/business/accounts` with a body containing a list of account IDs. Note that this operation is asynchronous.

Your request should be similar to the following:

```plaintext
curl -X DELETE https://YOUR_REST_API_URL/business/accounts \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "accounts": [
      { "id": "ACC001" },
      { "id": "ACC002" },
      { "id": "ACC003" }
    ]
  }'
```

### Delete one account {#delete-one-account}

Like creating one account, this operation targets a specific account by including its ID directly in the endpoint URL. This gives you precise control over a single record without affecting others.

The following code snippet sends a `DELETE` request to `/business/accounts/ACC001`. This operation is synchronous. Braze processes the request immediately and returns a response as soon as it's complete. Use this when an individual account is closed, merged, or needs to be removed from Braze for compliance or data hygiene purposes.

To delete a single account, send a `DELETE` request to `/business/accounts/:account_id`. Note that this operation is synchronous.

Your request should be similar to the following:

```plaintext
curl -X DELETE https://YOUR_REST_API_URL/business/accounts/ACC001 \
  -H "Authorization: Bearer YOUR-REST-API-KEY"
```

## Using objects in messages

After you've [imported your data to Braze](#importing-data-to-braze), you can use account objects to build a segment and send personalized messages to users using Liquid.

### Step 1: Build a segment

Next, build a segment that combines user data and account data. For this example, you target directors at healthcare companies to increase registration for a new webinar at your health promotion company.

1. Go to **Audience** > **Segments**, then select **Create Segment**.
2. Give your segment a name.
3. In the **Segment Builder**, select the **Business** filter and set up the following segmentation filters. When you're finished, select **Save**.

| Filter                          | Description                                      |
|---------------------------------|--------------------------------------------------|
| `Role is exactly director`      | Targets users whose role is specifically Director |
| `Accounts industry matches regex healthcare` | Matches users in accounts with industries related to healthcare |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Currently, to use multiple account filters, select **Add Criteria** instead of using the **OR/AND** dropdown.
{% endalert %}

![Segmentation filters set up to create a segment for users who are directors at healthcare companies.]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/build_segment.png %})

{% alert note %}
Segmentation works only on the first 1,000 account records that match the criteria. You can have up to one business filter per segment, and all criteria must be in one filter.
{% endalert %}

### Step 2: Use Liquid to personalize

Now you can personalize your message to send users information about opportunities. In this example, draft a message to your directors and link them to the webinar. You can also use a Braze catalog to pull industry-specific imagery for personalization.

#### Step 2.1: Personalize with account information

Select **Business** as the personalization type, then select **Name** to personalize the message with the user’s company name.

The following is copied to your clipboard.

{% raw %}
```javascript
{% business %}
{{ business_accounts[0].name }}
```
{% endraw %}

Braze generates the {% raw %}`{% business %}`{% endraw %} tag, which sets an array named `business_accounts` that contains account information for the associated account.

Adjust the auto-generated output to create your message.

In the example below, move the call to the {% raw %}`{% business %}`{% endraw %} tag to the top of the message and personalize with the user's first name. Use the account name to personalize the message. The Liquid output stays the same, but you place it in different parts of the message.

{% raw %}
```javascript
{% business %}

Hi {{${first_name}}},

We would love to invite you and your peers at {{ business_accounts[0].name }} to join our latest webinar named "Creating Optimal Health Outcomes for Patients".  Click the link below to register.
```
{% endraw %}

The output is similar to the following:

{% raw %}
```javascript
Hi John,

We would love to invite you and your peers at Sunshine Health to join our latest webinar named "Creating Optimal Health Outcomes for Patients". Click the link below to register.
```
{% endraw %}

#### Step 2.2: Connect with catalogs

Next, further personalize your message by using Braze catalogs to add and store an image that corresponds to the healthcare company.

For this example, assume you have the following:

- A catalog set up called `industry_assets`
- The ID for each catalog entry is the name of an industry that corresponds to industries in your accounts
- The image URL links for a primary and a secondary image.

The following is an example of the Liquid used for this personalization.
{% raw %}
```javascript
//Make a call to the business tag.  This sets the accounts array and prepares us to pull account data out.
{% business %}

//Assign the user's accounts industry to a variable called industry.  This step isn't required but it makes everything easier to read.
{% assign industry = {{business_accounts[0].industry}} %}

//Make a catalog_items call to the industry_assets catalog and ask for the industry item (in this case, it will ask for "healthcare")
{% catalog_items industry_assets industry %}

// Get the hero image for the "healthcare" industry
{{items[0].hero_image}}
```
{% endraw %}

## Frequently Asked Questions (FAQ) {#faq}

### Can I add custom fields?

Yes. You can add custom fields to accounts. If you have your own lead scoring method, you can also use a custom field on your account object to track this.

### Can a user be associated with more than one account?

No. Currently, each user can only have one account association.

### Can one user profile contain multiple emails?

No. A user profile cannot have more than one email, such as a personal and work email.
