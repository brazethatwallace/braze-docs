---
nav_title: Automated IP warming
article_title: Automated IP Warming
page_order: 1
page_type: reference
description: "This reference article covers automated IP warming and how to monitor your IP warming."
channel: email
---

# Automated IP warming

> Use automated IP warming to gradually ramp email volume from new dedicated IPs to build sender reputation with inbox providers.

## How it works

You can use automated IP warming to gradually increase your daily send volume, allowing inbox providers to learn and trust your sending patterns. When you add a domain to your workspace, you can select the **Automated IP Warming** tile in the **Pick up where you left off** section of your home dashboard. This tile remains for 60 days while your workspace is in the new-sender onboarding window.

Each automated IP warming plan is tied to one from address. That from address maps to a sending subdomain and an IP pool. If the pool contains multiple dedicated IPs, Braze warms them together in a single plan.

Braze sends to your most engaged subscribers first, which allows daily volume to grow at a pace that matches best practices. Then, Braze tracks engagement and deliverability signals. If Braze detects any issues, the system adjusts your schedule automatically.

After you complete at least one plan, you can view completed plans at **Settings** > **Email Preferences** > **Automated IP warming**.

{% alert note %}
If you only see a single-plan experience in your dashboard, your workspace may not have access to multiple IP warming plans yet. Contact your Braze account team for availability.
{% endalert %}

## Prerequisites

To perform automated IP warming, you must have the following:

- Verified subdomain and active IP addresses
- Permissions to view and launch an IP warmup
    - "View Usage Data" to view the IP warming section
    - "View Email Templates" to view and select the email templates for IP warming
    - "Manage Email Settings" to launch the IP warmup
- "Access Campaigns" 
- "Approve and Deny Campaigns" if the approval workflow for campaigns is turned on 
    - Braze automatically approves the campaigns created from automated IP warming on your behalf.

{% alert important %}
This feature may not be supported depending on your email infrastructure.
{% endalert %}

## Set up an automated IP warming plan

### Step 1: Set a schedule

1. If your workspace supports multiple IP warming plans, enter a unique **Plan name**. Plan names can contain letters, numbers, hyphens, and underscores only, and must be unique in your workspace. A plan name is required before you can launch.
2. In the **Sending information** section, select the **From address** to warm IP addresses for. Braze displays the associated **IP pool** and the number of **IP addresses in pool** for that from address.
3. Enter the **Current daily send volume** and **Target send volume**. Braze suggests a target send volume of up to 2 million sends per IP in the selected pool. If your current daily send volume is 0, the first day of your schedule starts at up to 50 sends per IP, capped at 500 total.
4. Select the start date for automated IP warming. This date must be at least one day after the plan is launched.
5. Enter the send time. This sends the messages in the company's time zone.
6. Select **Next: Segments** to continue the setup.

![Example schedule details.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Step 2: Select and rank segments

1. Next, select the segments to target. During IP warming, Braze starts sending to your highest engaged users and gradually increases send volume over time and slowly adds in segments with less engagement. 
2. Then, drag and drop the segments to rank them from high to low engagement. High engagement includes recipients who consistently open and click on your emails. Low engagement includes recipients who are inconsistent in their engagement with your emails or haven't engaged with your emails in a very long time.
3. Select **Next: Messages** to continue the setup.

![Two segments selected to target for automated IP warming.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Step 3: Select the messages to send

1. Select **Select email templates**.
2. Choose the email templates for the messages to send. The content you send during IP warming should encourage opens and clicks. We recommend choosing content that has had good reception in the past. For example, you can use promotional offers to encourage immediate engagement and purchases.
3. Select **Select templates**. Braze calculates the number of required templates before you can launch. We recommend providing more templates than the minimum required to allow the system to adjust for deliverability issues without stopping.
4. After adding the required number of templates, select **Next: Summary**.

{% alert important %}
Changes made to the campaigns created from the IP warming tool (such as changing the scheduled date, segment, volume) are not reflected on the IP warming **Summary** page.
{% endalert %}

### Step 4: Select conversion events

You can define up to four of the following conversion events to track. These conversion events cannot be updated after the automated IP warming plan has launched.

- Starts session
- Places order
- Performs custom event
- Upgrade app
- Opens email
- Clicks email

Next, select the conversion deadline, which is the maximum time that can pass between a user entering a campaign and the conversion event.

![Conversion settings showing conversion event selection and conversion deadline.]({% image_buster /assets/img/automated_ip_warming_conversions.png %})

### Step 5: Review and launch

Review the details of your IP warming plan. Then, select **Launch**.

## Multiple IP warmups

Use multiple automated IP warming plans when you need to warm more than one from address or IP pool.

| Scenario | Recommendation |
| --- | --- |
| Multiple dedicated IPs in one IP pool | Create one plan and select the from address for that pool |
| Multiple IP pools or from addresses | Create a separate plan for each from address |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Multiple IP warming scenarios" }

### Warm multiple IPs in one pool

When you select a from address in [Step 1: Set a schedule](#step-1-set-a-schedule), Braze shows the associated IP pool and IP addresses in pool. Braze uses the IP count when it builds your ramp schedule and suggests your target send volume.

If your **Current daily send volume** is 0, the first scheduled day starts at up to 50 sends per IP in the pool, capped at 500 total. Braze suggests a **Target send volume** of up to 2 million sends per IP in the pool.

### Warm multiple IP pools

To warm more than one from address or IP pool:

1. Go to **Settings** > **Email Preferences** > **Automated IP warming**.
2. Select **New IP warming plan**.
3. Enter a unique **Plan name**.
4. Complete the setup for that from address.
5. Repeat for each additional from address or IP pool you need to warm.

Track each plan from the **Automated IP warming** table. Each plan has its own schedule, segments, templates, campaigns, and tracker. Plans can be in **Draft**, **In progress**, **Completed**, or **Stopped** status.

{% alert important %}
Avoid sending large non-warming campaigns from the same from address or IP pool while an automated IP warming plan is active. Additional sends during warming can affect deliverability signals and make it challenging to isolate issues.
{% endalert %}

## During active IP warming

IP warming campaigns are created 1 to 2 days in advance, unless you are launching an IP warmup the next day. These campaigns are automatically named with the following format: `IP Warming Day [X] - [Date] - [Template Name]`.

When the targeted daily send goal is reached, the system stops sending for that day to protect your reputation. 

The system monitors your health based on the following industry benchmarks: 

- Delivery rate drops less than or equal to 90%
- Open rate less than 10%
- Bounces greater than 5%
- Spam complaint rates greater than 0.04%

If stats are under our benchmarks, the system holds volume the next day rather than increasing the volume to mitigate risk to your sender reputation.

## Stop an IP warmup plan

Braze allows you to stop the IP warming and the creation of future campaigns, but if a campaign is already active or scheduled for the next 24 to 48 hours, you may need to stop the specific campaign manually. Stopping an IP warming plan also stops all associated campaigns.

However, when stopped, the IP warmup cannot be resumed. Instead, you must set up a new plan to pick up from where you left off by:

- Downloading the existing data for your stopped plan to keep for your record
- Updating the **Current daily send volume** to the most recent volume
- Adding a filter to a segment if you plan to use the same segment from the last IP warmup by excluding users that have already received previous campaigns

## When an IP warmup completes

IP warming is marked as completed when the last day of IP warming ends at midnight in your company’s time zone. For example, if the last campaign sent in the IP warming plan sends at 8 pm, then the plan is marked as done after four hours.

Completed plans remain available from **Settings** > **Email Preferences** > **Automated IP warming**. If your workspace uses the single-plan experience, the tracker also stays on the home dashboard for 90 days after the plan ends. After 90 days, the home dashboard tracker is removed.

Downloading the data includes these standard email metrics:

- _Sent_	
- _Delivered_	
- _Bounces_	
- _Spam reports_	
- _Total opens_	
- _Unique opens_	
- _Clicked_	
- _Unsubscribed_

If a day includes multiple campaigns used to meet volume requirements, these are aggregated in the daily view.

![IP warming tracker with send volume for the week of January 16.]({% image_buster /assets/img/automated_ip_warming_example.png %})
