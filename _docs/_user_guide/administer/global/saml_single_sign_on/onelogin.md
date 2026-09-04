---
nav_title: OneLogin
article_title: OneLogin
page_order: 4
page_type: tutorial
description: "This article will walk you through how to configure Braze to use OneLogin for single sign-on."

---

# OneLogin

> [OneLogin](https://www.onelogin.com/) is a cloud identity platform that provides a comprehensive solution for managing user identities. OneLogin integrates with cloud and on-premise applications using SAML 2.0, for Single Sign-On (SSO), user provisioning, multi-factor authentication, and more.

## Requirements

Upon setup, you will be asked to provide a sign-on URL and an Assertion Consumer Service (ACS) URL.  

| Requirement | Details |
|---|---|
| Assertion Consumer Service (ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> For European Union domains, the ACS URL is `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. |
| Entity ID | `braze_dashboard` by default. If your IdP requires a company-specific Entity ID, enable **Custom Entity ID** in **Security Settings** and use `braze_dashboard_<companyID>`. |
| Braze Domain | You will need your Braze domain to set up Braze within OneLogin. If your instance is `US-01`, you will need to input your dashboard URL into the OneLogin dashboard. <br><br> For example, if your dashboard URL is `https://dashboard-01.braze.com`, you need to input `dashboard-01.braze.com`.  |
| RelayState API key | To enable IdP login, go to **Settings** > **Setup and Testing** > **APIs and Identifiers**, open the **API Keys** tab, and create an API key with `sso.saml.login` permissions. For steps, refer to [Setting up your RelayState]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## IdP-initiated login within OneLogin

### Step 1: Configure the Braze app

1. Log into [OneLogin](https://app.onelogin.com/login). Click **Administration**.![OneLogin Administration page.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Go to **Apps** > **Add Apps** in the top navigation bar. Search for "Braze" and select the Braze app.![Search results for Braze in OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Save the Braze app to your Company.![2. Go to Apps > Add Apps in the top navigation bar. Search for "Braze" and select the Braze app.!Search results for Braze in OneLogin.]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. When saved, go to **Configuration** and add your **Braze Domain** and **RelayState** API key. If your IdP requires a company-specific Entity ID, also configure the **ACS URL** (`https://<SUBDOMAIN>.braze.com/auth/saml/callback`) and Entity ID from [SAML SSO setup]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#requirements).![OneLogin Configuration tab for the Braze app.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze expects the SAML assertions in a [specific format]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#step-1-configure-your-identity-provider). Under **Parameters** the attributes supported by Braze should be pre-populated. Verify that they are correct.![Braze SAML parameters in OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Copy the **Certificate** and **SAML 2.0 Endpoint (HTTP)** needed to set up the Braze dashboard from under the **SSO** tab.![Certificates to copy from the Braze app SSO tab in OneLogin.]({% image_buster /assets/img/onelogin_6.jpg %})

### Step 2: Configure OneLogin within Braze

Once you have set up Braze within your OneLogin, they will provide a target URL (`SAML 2.0 Endpoint (HTTP)`) and `x.509` certificate to input into your Braze account.

After your account manager has enabled SAML SSO for your account, go to **Settings** > **Company Settings** > **Admin Settings** > **Security Settings** and toggle the SAML SSO section to **ON**.

On this page, input the following:

| Requirement | Details |
|---|---|
| `SAML Name` | This will appear as the button text on the login screen. This is typically your identity provider's name, like "OneLogin". |
| `Target URL` | This is the `SAML 2.0 Endpoint (HTTP)` URL provided by OneLogin.|
| `Certificate` | The `x.509` PEM encoded certificate is provided by your OneLogin. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Configure OneLogin within Braze" }

If your IdP requires a company-specific Entity ID, turn on **Custom Entity ID** in **Security Settings**, copy the generated value, and paste it into OneLogin's Entity ID field. See [Custom Entity ID]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#custom-entity-id) in the SAML SSO setup article.

![SAML SSO settings with the toggle selected.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
If you want your Braze account users to only sign in with SAML SSO, you can [restrict single sign-on authentication]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) from **Settings** > **Company Settings** > **Admin Settings** > **Security Settings**.
{% endalert %}

## Next steps

After OneLogin SSO is working:

- [Enforce SAML SSO-only login]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) if password login should be disabled.
- [Set up SAML just-in-time provisioning]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning) to auto-create dashboard users on first IdP sign-in.
- Use [Obtaining a SAML trace]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#obtaining-a-saml-trace) if users encounter login errors.

