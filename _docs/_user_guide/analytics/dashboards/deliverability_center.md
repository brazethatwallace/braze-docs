---
nav_title: Deliverability Center
article_title: Deliverability Center
alias: "/deliverability_center/"
page_order: 4
description: "This reference article covers how to set up the Deliverability Center, a feature that allows marketers to view their email sending domains and IP reputations and understand their email deliverability."
channel:
  - email

---

# Deliverability Center

> The Deliverability Center provides more insight into your email performance by supporting the use of [Gmail Postmaster Tools](https://www.gmail.com/postmaster/) to track data on emails sent and gather data about your sending domain.

Email deliverability is the core of campaign success. Using the Deliverability Center in the Braze dashboard, you can view your domains by **IP Reputation** or **Delivery Errors** to discover and troubleshoot any potential issues with email deliverability. 

To access the Deliverability Center, you need the [user permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) in the following dropdown for your workspace.

{% details User permissions for the Deliverability Center %}

- View Campaigns
- Edit Campaigns
- Archive Campaigns
- View Canvases
- Edit Canvases
- Archive Canvases
- View Frequency Capping Rules
- Edit Frequency Capping Rules
- View Message Prioritization
- Edit Message Prioritization
- View Content Blocks
- View Feature Flags
- Edit Feature Flags
- Archive Feature Flags
- View Segments
- Edit Segments
- View IAM Templates
- Edit IAM Templates
- Archive IAM Templates
- View Email Templates
- Edit Email Templates
- Archive Email Templates
- View Webhook Templates
- Edit Webhook Templates
- Archive Webhook Templates
- View Email Link Templates
- Edit Email Link Templates
- View Media Library Assets
- Edit Media Library Assets
- Delete Media Library Assets
- View Locations
- Edit Locations
- Archive Locations
- View Promotion Codes
- Edit Promotion Codes
- Export Promotion Codes
- View Preference Centers
- Edit Preference Centers
- View Reports
- Edit Reports
- View Usage Data

{% enddetails %}

## Set up your Google Postmaster account

Before connecting to the Deliverability Center, you'll need to set up a Google Postmaster Tools account. You can use a work or personal Gmail account to set up your Google Postmaster. 

1. Go to the [Google Postmaster Tools dashboard](https://postmaster.google.com/managedomains?pli=1).
2. At the bottom of the page, select <i class="fas fa-plus-circle"></i> **Add domain**.
3. Enter your root (parent) domain to authenticate your email. Be sure the TXT record is tied to this root (parent) domain, **not** the subdomain you're using through Braze. Verifying the root (parent) domain lets you later add subdomains in Postmaster Tools without creating additional TXT records. For example, by verifying `braze.com`, you can later add `demo.braze.com` as a separate subdomain in Postmaster Tools to see subdomain-level metrics.
4. Google generates a TXT record that can be added directly to your domain's DNS. This is generally owned by whoever manages your DNS. For information and guidance on how to update your specific DNS, check out [Verify your domain (host-specific steps)](https://support.google.com/a/topic/1409901).
5. Select **Next**. <br>![An example domain "demo.braze.com" to authenticate an email.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. After the TXT record is added to the DNS, return to the Google Postmaster Tools dashboard and select **Verify**. This step confirms you own the domain, so you can access Gmail deliverability metrics in your Postmaster account. <br>![A prompt to verify ownership of the domain "demo.braze.com".]({% image_buster /assets/img_archive/domain_verification.png %})
7. After verifying the root (parent) domain, add your sending subdomains to Google Postmaster.

{% alert note %}
If your subdomains aren't included in the Deliverability Center for Google Postmaster, this can be a result of only adding the root (parent) domain to Google Postmaster. After the root domains are verified in Google Postmaster, you can add your subdomains, which are verified automatically. This process allows Google to report back on metrics on the subdomain-level, which can then be pulled into the Braze Deliverability Center.
{% endalert %}

## Integrate Google Postmaster {#integrating-google-postmaster}

{% alert important %}
**Google Postmaster Tools v2 migration**<br>
Google is deprecating the old Postmaster Tools (v1) and has released a next-generation version (v2) with a modern user interface and new dashboards, including a Compliance dashboard to help monitor adherence to Gmail's sender guidelines. All users must migrate to v2 by October 31, 2026.<br><br>
To re-authorize your Google Postmaster Tool connection, go to **Partner Integrations** > **Technology Partners**, open **Google Postmaster**, and select **Change Account** to re-authenticate with the new v2 permissions. When finished, you are upgraded to v2 and gain access to new dashboards and data.<br><br>
For more information, refer to [Google's announcement about the new Postmaster Tools](https://support.google.com/mail/answer/16594218?hl=en).
{% endalert %}

Before setting up your Deliverability Center, check that your domains have been [added to the Gmail Postmaster Tools](https://support.google.com/mail/answer/9981691?hl=en).

Follow these steps to integrate with Google Postmaster and set up your Deliverability Center:

1. Go to **Analytics** > **Email Performance**.
2. Select the **Deliverability Center** tab. <br>![A Deliverability Center with Google Postmaster unconnected.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Select **Connect with Google Postmaster**. 
4. Select your Google Account and then select **Allow** to allow Braze to view email traffic metrics for the domains registered with the Postmaster Tools. 

Your verified domains display in the Deliverability Center. 

![Two verified domains for Google Postmaster with a medium and low reputation.]({% image_buster /assets/img_archive/deliverability_center2.png %})

You can also access Google Postmaster in the Braze dashboard by going to **Partner Integrations** > **Technology Partners** > **Google Postmaster**. After integrating, Braze pulls reputation and error data for the last 30 days. The data may not be immediately available and could take several minutes to populate.

### Invalid or expired authorization

If you receive an alert that Google Postmaster Tools authorization credentials are invalid, email sending from Braze is **not** affected. Only the connection between Braze and Google Postmaster breaks, which stops Gmail reputation and error data from syncing to the Deliverability Center until you reconnect.

To restore the integration, go to **Partner Integrations** > **Technology Partners**, open **Google Postmaster**, select **Disconnect**, then run through the connection flow again (same steps as in [Integrating Google Postmaster](#integrating-google-postmaster)).

### Metrics and definitions

The following metrics and definitions apply to Google Postmaster Tools.

#### IP reputation 

To help understand the ratings for IP reputation, refer to this table:

| Reputation Rating | Definition |
| ----- | ---------- |
| High | Has a good track record of generating low spam complaints (such as users clicking the "spam" button). |
| Medium/Fair | Known to generate positive engagement but occasionally receives spam complaints. Most of the emails from this domain are sent to the inbox, except when spam complaints increase. |
| Low | Known to receive elevated rates of spam complaints regularly. Emails from this sender are likely be filtered to the spam folder. |
| Bad | Has a history of receiving elevated rates of spam complaints. Emails from this domain are almost always be rejected at connection time or filtered to the spam folder. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="IP reputation" }

{% alert important %}
The spam complaint data shown in Braze is based on feedback loop (FBL) reports from email providers who share them, such as Microsoft, Yahoo, and Comcast. When users at these providers report mail as spam, those complaints are sent back to Braze.<br><br>
However, Gmail and iCloud do not operate traditional feedback loops and do not report spam complaints back to Braze. This means:<br>
- Spam complaints from Gmail users are not included in Braze metrics or available in Snowflake or Currents data.<br>
- You can view Gmail spam data only as aggregate percentages in [Gmail Postmaster Tools](https://www.gmail.com/postmaster/), not as individual addresses.<br>
- If you see high spam rates in Gmail Postmaster Tools, those numbers do not match your Braze spam complaint metrics because Gmail doesn't share that data with senders.
{% endalert %}

#### Domain reputation 

Use the following table to help monitor and understand your domain reputation ratings to help avoid being filtered into a spam folder.

| Reputation Rating | Definition |
| ----- | ---------- |
| High | Has a good track record of very low spam complaints. Complies with Gmail’s sender guidelines. Emails are rarely filtered into the spam folder. Has a good track record of a very low spam rate. Complies with [Gmail's sender guidelines](https://developers.google.com/gmail/markup/registering-with-google). |
| Medium/Fair | Known to generate positive engagement, but has occasionally received a low volume of spam complaints. Most of the emails from this domain reach the inbox (except when there is a notable increase in spam levels). |
| Low | Known to receive spam complaints regularly. Emails from this sender are likely be filtered to the spam folder. |
| Bad | Has a history of receiving elevated rates of spam complaints. Emails from this domain are almost always be rejected at connection time or filtered to the spam folder. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Domain reputation" }

#### Authentication

Use the authentication dashboard to review the percentage of emails that have passed Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM), and Domain-based Message Authentication, Reporting and Conformance (DMARC).

| Graph Type | Definition |
| ----- | ---------- |
| SPF | Shows the percentage of emails that passed SPF versus all emails from the domain that attempted SPF. This excludes any spoofed mail. |
| DKIM | Shows the percentage of emails that passed DKIM versus all emails from the domain that attempted DKIM. |
| DMARC | Shows the percentage of emails that passed DMARC alignment versus all emails received from the domain that passed either SPF or DKIM. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Authentication" }

#### Encryption

Refer to this table to understand what percentage of your inbound and outbound traffic is encrypted.

| Term | Definition |
| ----- | ---------- |
| TLS Inbound | Shows the percentage of incoming mail (to Gmail) that passed TLS versus all mail received from that domain. |
| TLS Outbound | Shows the percentage of outgoing mail (from Gmail) accepted over TLS versus all mail sent to that domain. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Encryption" }

For more ideas on improving deliverability, read [Deliverability pitfalls and spam traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps). Be sure to reference our [Email best practices]({{site.baseurl}}/user_guide/channels/email/best_practices) for things you should check for before sending an email campaign.

## Set up Microsoft Smart Network Data Services (SNDS)

If Microsoft is your main mailbox provider, you can view Microsoft SNDS data in the Deliverability Center. This includes dedicated sending IPs for workspaces that use Amazon SES, SendGrid, or SparkPost. Use this data to monitor IP health and understand how Microsoft inbox providers are rating your sending.

Microsoft SNDS provides IP-level data on spam complaints and sending volume as reported by Microsoft inbox providers such as Outlook, Hotmail, and Live.

{% alert important %}
If you don't see your data in the Deliverability Center, contact [Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) with a list of your IP addresses.
{% endalert %}

### Amazon SES

For workspaces that send email through Amazon SES, the Deliverability Center displays Microsoft SNDS metrics for your dedicated sending IPs. Braze backfills up to 90 days of historical SNDS data when this feature is turned on for your workspace.

![An example of results from Microsoft SNDS, including sample IPs, recipients, RCPT commands, data commands, filter result, and complaint rate.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Metrics and definitions

The following metrics apply to Microsoft SNDS.

#### Recipients

This metric refers to the number of recipients on messages transmitted by the IP.

#### DATA commands

This metric tracks the number of DATA commands sent by the IP. DATA commands are part of the SMTP protocol used to send mail.

#### Filter results

Refer to this table to understand the filter results 

| Result | Definition |
| ----- | ---------- |
| Green | Judged to be spam by Microsoft’s spam filter up to 10% of the given time frame. |
| Yellow | Judged to be spam by Microsoft’s spam filter between 10% and 90% of the given time frame. |
| Red | Judged to be spam by Microsoft’s spam filter up to more than 90% of the given time frame.| 
{: .reset-td-br-1 .reset-td-br-2 aria-label="Filter results" }

#### Complaint rate

This is the fraction of the time that a message received from the IP is complained about by a Hotmail or Windows Live user during the activity period. Users have the option of reporting almost all messages as junk via the web user interface. 

To calculate the complaint rate, divide the number of complaints by the number of message recipients.  

| Result | Definition |
| ----- | ---------- |
| Less than 0.3% | The ideal complaint rate. |
| More than 0.3% | Review your sign-up process, and ensure your unsubscribe link is working. Also, consider whether the mail could be better personalized to your audience. |
| More than 100% | Note that SNDS displays complaints for the day they were reported, not retroactively against the day the complained-about mail was delivered. | 
{: .reset-td-br-1 .reset-td-br-2 aria-label="Complaint rate" }

#### Spam trap hits and trap message period

{% alert important %}
Microsoft no longer includes spam trap hit counts or trap message period data in SNDS reports. For more information, see [Microsoft's SNDS announcement](https://substrate.office.com/ip-domain-management-snds/snds).
{% endalert %}

Spam trap hits were the number of messages sent to "trap accounts," which are accounts maintained by Outlook.com that don't solicit any mail.

The trap message period start and end columns showed when the first and last messages sent to trap accounts were received from the IP during the activity period.

{% alert tip %}
If you're looking for records related to one of your verified domains in Braze, note that the Deliverability Center lists your data from Google Postmaster or Microsoft SNDS, meaning it's likely that either platform doesn't have any data to share with Braze. Alternatively, try maintaining consistent email delivery, as this can lead to a higher reputation. 
{% endalert %}

## Spam complaints and feedback loops

An email feedback loop (FBL) allows email senders to receive reports when recipients mark messages as spam. However, Gmail and iCloud do not offer traditional feedback loops, which means Braze (through SparkPost or SendGrid) does not receive spam complaint data from these providers. 

Because spam complaint data is not available from Gmail and iCloud, it's important to use other tools to monitor your email health and reputation with these major providers:

- Use [Google Postmaster Tools](https://www.gmail.com/postmaster/) to monitor domain and IP reputation, spam rates, and user engagement. You can integrate Google Postmaster with Braze as described in [Integrate Google Postmaster](#integrating-google-postmaster).
- Apple does not provide a public Postmaster tool equivalent to Google's. Focus on maintaining strong engagement metrics and following email best practices.

To maintain good deliverability with all providers, implement a [sunset policy]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies) to automatically stop sending to unengaged users. This helps prevent your emails from being marked as spam and protects your sender reputation.
