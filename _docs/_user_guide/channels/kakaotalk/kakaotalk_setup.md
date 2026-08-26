---
nav_title: Set up KakaoTalk
article_title: "Set up KakaoTalk"
description: "This reference article outlines how to set up your KakaoTalk channel, including how to set up users, reconcile user IDs, and create test users."
page_order: 0
alias: /kakaotalk_setup/
channel:
  - KakaoTalk
---

# Set up KakaoTalk

> This article covers how to set up the [KakaoTalk messaging channel]({{site.baseurl}}/kakaotalk) in Braze, including how to set up users, reconcile user IDs, and create KakaoTalk test users.

## Prerequisites

| Requirement | Description |
| --- | --- |
| Account with a supported KakaoTalk partner | An account with a supported KakaoTalk partner, [CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/) or [Infobip](https://marketplace.braze.com/partners/infobip), is required to use the KakaoTalk messaging channel. |
| KakaoTalk Business channel | Your KakaoTalk account must be a KakaoTalk Business channel to send KakaoTalk messages through Braze. When you create an account, its default status is basic. To make your account a Business channel, you'll need to verify your business and provide relevant documentation. |
| KakaoTalk Sender Key | A valid KakaoTalk Sender Key. |
| Contact phone number | A contact phone number for your KakaoTalk channel's administrator. |
| Braze cluster IPs allowlisted | IP allowlist registration is required for all customers. Register the Braze IP addresses for your cluster before you integrate KakaoTalk in Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

### Register Braze IP addresses {#register-braze-ip-addresses}

Register the Braze IP addresses for your cluster in your Comm.One dashboard.

1. In your Comm.One dashboard, go to **Account Management (계정 관리)**, select the menu icon, then select **View Details (자세히보기)**.
2. Select **Center & Upload IP Allowlist (센터&업로드 IP 화이트리스트)**.
3. Add the IP addresses for your Braze cluster. For the complete list of IPs by cluster, see [IP allowlisting]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting).

![Comm.One dashboard showing where you can add IP addresses.]({% image_buster /assets/img/kakaotalk/register_braze_ip.png %})

### Types of KakaoTalk accounts

| Account type | Description |
| --- | --- |
| Basic channel | A standard KakaoTalk channel that any organization can set up. It enables broadcast messaging and 1:1 chat through KakaoTalk. |
| [Business channel](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | An upgraded, business-verified KakaoTalk channel that requires an application and verification process. It offers enhanced features, such as {::nomarkdown}<ul><li>Verified badge</li><li>Appearance as a recommended channel</li><li>Support for business messaging</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types of KakaoTalk accounts" }

#### Apply for a business channel 

Before starting the application, gather the following business documentation:
- Korean Business Registration Certificate
- ID of the Business Representative
- Employment Certificate
- Industry-specific Licenses

{% alert important %}
The information on your KakaoTalk Channel (such as channel name, profile image, and others) must exactly match the information on your official submitted documents.
{% endalert %}

After gathering your documentation, follow these steps:

1. Log into the [KakaoTalk Channel Admin Center](https://center-pf.kakao.com/).
2. Select the existing KakaoTalk channel you wish to upgrade.
3. In the **Management (관리)** section, select the option for **Business Channel Application (비즈니스 채널 신청)**.
4. Select the **Apply** or **Request button (신청)** to begin the process.
5. Provide the required information.
6. Wait for a notification with the review results.

## Integrate KakaoTalk

### Connect the KakaoTalk channel to Braze

1. Go to **Partner Integrations** > **Technology Partners** and select your KakaoTalk provider.
2. Gather the required credentials for your provider (See the following section), then enter them into the **Technology Partners** page and save.
3. Use the newly saved credentials for sending.

#### CJ OliveNetworks

Go to your [Comm.One dashboard](https://ums.cjmplace.com/) and gather the following information.

| Field | Location |
| --- | --- |
| **Comm.One Login ID (로그인 아이디)** | Select your profile. |
| **Sender Key (발신프로필 키)** | Go to **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Channel name (카카오톡 채널 프로필명)** | In your Comm.One dashboard, go to **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Sender number (연락처)** | {::nomarkdown}<ol><li>Go to <b>Account Management (계정 관리)</b>, select the menu icon, then select <b>View Details (자세히보기)</b>.</li><li>Go to <b>Business Detailed Information (업체 상세 정보)</b> > <b>Company Information (기업정보)</b></li></ul>{:/} |
| **Credential (ID) & Password (비밀번호)** | Go to the same location for the **Sender number (사업자 등록번호)**, then go to **API** > **Brand Message (브랜드 메시지)**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CJ OliveNetworks" }

{% tabs local %}
{% tab Comm.One Login ID (로그인 아이디) %}

![Comm.One dashboard showing a censored login ID.]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endtab %}
{% tab Sender Key (발신프로필 키) %}

![Comm.One dashboard showing a censored Sender Key.]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% alert important %}
You can integrate a KakaoTalk Sender Key into only one workspace at a time. To use the same Sender Key in a different workspace, you must first archive the KakaoTalk subscription group in the original workspace, then contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) to remove the integration. After Braze removes the integration, you can set up the integration in the new workspace.
{% endalert %}

![Credentials for a Braze KakaoTalk channel.]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% endtab %}
{% tab Channel name (카카오톡 채널 프로필명) %}

![Comm.One dashboard showing a censored channel name.]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endtab %}
{% tab Credential (ID) & Password (비밀번호) %}

![Comm.One dashboard showing a censored credential ID and password.]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Only the channels mapped to a single common ID can be registered.
{% endalert %}

![Fields on the Technology Partners page for CJ OliveNetworks.]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

#### Infobip

Go to your Infobip dashboard and the [KakaoTalk Channel Admin Center](https://center-pf.kakao.com/) to gather the following information.

| Field | Location |
| --- | --- |
| **API Base URL** | In the Infobip portal, go to **Developer Tools** > **API Keys**. |
| **API Key** | In the Infobip portal, go to **Developer Tools** > **API Keys**. |
| **Sender name / Sender key** | In the Infobip portal, go to **Channels and Numbers** > **Channels**, then select the **Senders** tab. |
| **Sender profile UUID** | In the KakaoTalk Channel Admin Center, go to **Channels** and find the **Search ID** in the channel information window. |
| **Channel name** | In the KakaoTalk Channel Admin Center, find the **channel name** in the same channel information window. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Infobip" }

##### API key and base URL

1. In the Infobip portal, select **Developer Tools** > **API Keys**.
2. On the **API keys** page, copy the **API base URL**.

![Infobip API Keys page showing the API base URL.]({% image_buster /assets/img/kakaotalk/infobip_api_keys_page.png %})

{: start="3"}
3. Select **CREATE API KEY**.
4. Enter the **Name**, select the **Expiration date**, then select the API scopes required for KakaoTalk. These scopes control which Infobip API actions your key can perform.

![Infobip Create API Key page showing the name, expiration date, and API scopes fields.]({% image_buster /assets/img/kakaotalk/infobip_api_key_scopes.png %})

{: start="5"}
5. Select **CREATE** to generate the key.
6. Copy the generated key. You can return to this page to update the name, expiration date, or API scopes.

##### Sender profile UUID and channel name

1. In the [KakaoTalk Channel Admin Center](https://center-pf.kakao.com/), select **Channels**.
2. In the **Channel Information** window, find the **Channel name** and **Search id** (sender UUID).
3. Enter the **Customer center contact information**. This is required when sending ad messages.

![KakaoTalk channel information window showing the Customer Center contact information fields.]({% image_buster /assets/img/kakaotalk/kakao_customer_center_contact.png %})

{: start="4"}
4. To view a different channel, select the channel icon at the top of the menu.
5. In the **My channel** list, select the channel you want to view, then repeat the previous steps.

## Set user profiles

User profiles must have phone numbers in E.164 format to message them through KakaoTalk. Phone numbers are shown on the user profile. KakaoTalk requires phone numbers to be in E.164 format (for example, `+821025749774`). This differs from some other messaging channels that may accept phone numbers in multiple formats.

### Import phone numbers

Import phone numbers by [uploading a CSV or using the API]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/) to create a user. Ensure phone numbers are in E.164 format before importing.
