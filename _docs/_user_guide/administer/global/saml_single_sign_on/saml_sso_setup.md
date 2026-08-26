---
nav_title: SAML SSO setup
article_title: SAML SSO Setup
page_order: 0
page_type: tutorial
toc_headers: h2
description: "This article will walk you through how to enable SAML single sign-on for your Braze account."

---

# Service Provider (SP) initiated login

> This article will walk you through how to enable SAML single sign-on for your Braze account and how to obtain a SAML trace.

## Requirements

Upon setup, you will be asked to provide a sign-on URL and an Assertion Consumer Service (ACS) URL.  

| Requirement | Details |
|---|---|
| Assertion Consumer Service (ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> For European Union domains, the ASC URL is `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. <br><br> For some IdPs, this can also be referred to as the Reply URL, Sign-On URL, Audience URL, or Audience URI. |
| Entity ID | `braze_dashboard` by default. <br><br> To set up a unique Entity ID for this dashboard, enable a custom Entity ID and use the generated value (`braze_dashboard_<COMPANY_ID>`) instead. For steps, refer to [Using a custom Entity ID](#using-a-custom-entity-id). |
| RelayState API key | Go to **Settings** > **API Keys** and create an API key with `sso.saml.login` permissions, and then input the generated API key as the `RelayState` parameter within your IdP. For detailed steps, refer to [Setting up your RelayState](#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## Setting up SAML SSO

### Step 1: Configure your identity provider

Set up Braze as a service provider (SP) in your identity provider (IdP) with the following information. In addition, set up SAML attribute mapping.

{% alert important %}
If you plan on using Okta as your identity provider, make sure to use the pre-built integration found on the [Okta site](https://www.okta.com/integrations/braze/).
{% endalert %}

| SAML Attribute | Required? | Accepted SAML Attributes |
|---|---|---|
|`email` | Required | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Optional | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Optional | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 1: Configure your identity provider" }

{% alert note %}
Braze only requires `email` in the SAML Assertion.
{% endalert %}

### Step 2: Configure Braze

When you finish setting up Braze in your identity provider, your identity provider will provide you with a target URL and `x.509` certificate to input into your Braze account.

After your account manager turns on SAML SSO for your account, go to **Settings** > **Admin Settings** > **Security Settings** and toggle the SAML SSO section to **ON**.

On the same page, input the following:

| Requirement | Details |
|---|---|
| SAML Name | This will appear as the button text on the login screen.<br>This is typically your identity provider's name, like "Okta." |
| Target URL | This is provided after setting up Braze within your IdP.<br> Some IdPs reference this as the SSO URL or SAML 2.0 Endpoint. |
| Certificate | The `x.509` certificate that is provided by your identity provider.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Configure Braze" }

Make sure that your `x.509` certificate follows this format when adding it to the dashboard:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![SAML SSO settings with the toggle selected.]({% image_buster /assets/img/samlsso.png %})

### Step 3: Sign into Braze

Save your security settings and log out. Then, sign back in with your identity provider.

## Using a custom Entity ID

By default, every Braze dashboard uses the shared Entity ID `braze_dashboard`. A custom Entity ID gives your dashboard a unique identifier, so your identity provider can verify that sign-in requests are meant for this specific dashboard. This is useful if you are setting up SAML SSO across multiple Braze companies in the same identity provider.

Using a custom Entity ID is optional. If you don't enable it, your dashboard continues to use `braze_dashboard`.

{% alert warning %}
The pre-built [Braze Okta marketplace app](https://www.okta.com/integrations/braze/) enforces the shared Entity ID `braze_dashboard` and isn't compatible with a custom Entity ID. If you already have SAML SSO set up with the Braze Okta marketplace app, turning on a custom Entity ID without updating the Entity ID field in Okta through a custom SAML app will break sign-in and can lock users out of the dashboard. To use a custom Entity ID with Okta, set up a custom SAML app instead.
{% endalert %}

### Step 1: Turn on the custom Entity ID

Go to **Settings** > **Admin Settings** > **Security Settings** and open the SAML Single Sign-On section. Turn on the **Custom Entity ID** toggle. Braze generates a unique Entity ID for your dashboard in the format `braze_dashboard_<COMPANY_ID>`. If you don't see the **Custom Entity ID** option, contact your Braze account manager.

### Step 2: Update your identity provider

Copy the generated Entity ID and paste it into the Entity ID field of your identity provider's Braze application. Depending on your provider, this field may be labeled **Entity ID**, **Audience**, or **Audience URI**.

{% alert important %}
The Entity ID must match in both Braze and your identity provider. Until both sides use the same value, users can't sign in with SAML SSO. Update your identity provider before saving this page to avoid locking users out.
{% endalert %}

### Step 3: Save and test

Save your security settings, log out, and then sign back in through your identity provider to confirm sign-in works with the custom Entity ID.

## Setting up your RelayState

1. In Braze, go to **Settings** > **APIs and Identifiers**.
2. In the **API Keys** tab, select the **Create API key** button.
3. In the **API key name** field, enter a name for your key.
4. Extend the **SSO** dropdown under **Permissions** and check **sso.saml.login**.
5. Select **Create API key**.
6. In the **API Keys** tab, copy the identifier next to the API key you created.
7. Paste the RelayState API Key into your IdP's RelayState (it may also appear as "Relay State" or "Default Relay State" depending on your IdP).

## SSO behavior

Members who opt to use SSO will no longer be able to use their password as they did prior. Users who continue to use their password will be able to unless restricted by the following settings.

## Restriction

You can restrict the members of your organization to only sign in with either Google SSO or SAML SSO. To turn on restrictions, go to **Security Settings** and select either **Enforce Google SSO only login** or **Enforce custom SAML SSO only login**.

![Example setup of "Authentication Rules" section with a minimum password length of 8 characters and password reusability of 3 times. The passwords will expire after 180 days, and users will be logged out after 1,440 minutes of inactivity.]({% image_buster /assets/img/sso3.png %})

By turning on restrictions, your company's Braze users will no longer be able to log in using a password, even if they have logged in with a password before.

{% alert important %}
After SSO is enforced, there is no fallback option for logging in if SSO authentication fails. Before enabling SSO enforcement, make sure your SSO configuration is correct, all certificates are current and renewed, and your security settings are properly managed to prevent login issues.
{% endalert %}

## Obtaining a SAML trace

If you experience login issues related to SSO, obtaining a SAML trace can help you troubleshoot your SSO connection by identifying what's sent in the SAML requests.

### Prerequisites

To run a SAML trace, you'll need a SAML tracer. Here are two possible options based on your browser:

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### Step 1: Open the SAML tracer

Select the SAML tracer from your browser's navigation bar. Be sure **Pause** isn't selected as this will prevent the SAML tracer from capturing what's sent in the SAML requests. When the SAML tracer is open, you'll see it populate the trace.

![SAML tracer for Google Chrome.]({% image_buster /assets/img/saml_tracer_example.png %})

### Step 2: Sign into Braze using SSO

Go to your Braze dashboard and attempt to sign in using SSO. If you encounter an error, open the SAML tracer and try again. A SAML trace has been successfully collected if there's a row with a URL like `https://dashboard-XX.braze.com/auth/saml/callback` and an orange SAML tag.

### Step 3: Export and send to Braze

Select **Export**. For **Select cookie-filter profile**, select **None**. Then, select **Export**. This will generate a JSON file that you can send to Braze Support for further troubleshooting.

!["Export SAML-trace preferences" menu with option "None" selected.]({% image_buster /assets/img/export_saml_trace_preferences.png %})

## Troubleshooting

### Is the user's email address correctly set up?

If you're getting the error `ERROR_CODE_SSO_INVALID_EMAIL`, the user's email address isn't valid. Confirm in the SAML trace that the `saml2:Attribute Name="email"` field matches the email address the user is using to log in. If you use Microsoft Entra ID (formerly Azure Active Directory), the attribute mapping is `email = user.userprincipalname`.

The email address is case sensitive and must exactly match the one that was set up in Braze, including the one configured in your identity provider (such as Okta, OneLogin, Microsoft Entra ID, and others).

Other errors that indicate you have issues with the user's email address include:
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST`: The user's email address isn't within the dashboard.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING`: The user's email address is blank or otherwise misconfigured.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` or `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH`: The user's email address doesn’t match the one used to set up SSO.

### Do you have a valid SAML certificate (x.509 certificate)?

You can validate your SAML certificate using [this SAML validation tool](https://www.samltool.com/validate_response.php). Note that an expired SAML certificate is also an invalid SAML certificate.

### Did you upload a correct SAML certificate (x.509 certificate)?

Confirm that the certificate in the `ds:X509Certificate` section of the SAML trace matches the one you uploaded to Braze. This doesn't include the `-----BEGIN CERTIFICATE-----` header and `-----END CERTIFICATE-----` footer.

### Did you mistype or misformat your SAML certificate (x.509 certificate)?

Confirm that there are no white spaces or extra characters in the certificate that you submitted in the Braze dashboard.

When you enter your certificate into Braze, it needs to be Privacy Enhanced Mail (PEM) encoded and formatted correctly (including the `-----BEGIN CERTIFICATE-----` header and `-----END CERTIFICATE-----` footer). 

Here is an example certificate that is correctly formatted:

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### Is the user's session token valid?

Have the affected user [clear their browser's cache and cookies](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser), and then try to log in with SAML SSO again.

### Did you set your RelayState?

If you're getting the error `ERROR_CODE_SSO_INVALID_RELAY_STATE`, your RelayState could be misconfigured or nonexistent. If you haven't already, you need to set your RelayState in your IdP management system. For steps, refer to [Setting up your RelayState](#setting-up-your-relaystate). 

### Does successful SSO sign-in return you to the Braze login page?

This can occur when RelayState isn't configured correctly. Confirm you created an API key (in **Settings** > **API Keys**) for IdP sign-in and set that API key as the `RelayState` parameter in your IdP. RelayState identifies which company account you're signing into. For step-by-step instructions, see [Setting up your RelayState](#setting-up-your-relaystate).

If you still can't sign in, [contact Braze Support]({{site.baseurl}}/braze_support) with a SAML trace if possible. For help capturing a trace, see [Obtaining a SAML trace](#obtaining-a-saml-trace).

### Is the user stuck in a sign-in loop between Okta and Braze?

If a user can't sign in because they're stuck cycling between the Okta SSO and Braze dashboard, you need to go to Okta and set the SSO URL destination to your [Braze instance]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) (for example, `https://dashboard-07.braze.com`). 

If you're using another IdP, check if your company uploaded the correct SAML or x.509 certificate to Braze.

### Are you using a manual integration?

If your company didn't download the Braze app from your IdP's app store, you need to download the pre-built integration. For example, if Okta is your IdP, you'd download the Braze app from their [integration page](https://www.okta.com/integrations/braze/).

## Google SSO

If your company uses Google SSO instead of custom SAML, contact your Braze account manager to enable Google SSO for your workspace. After it's enabled, go to **Security Settings** and select **Enforce Google SSO only login** to require Google Authentication for all company users.

When Google SSO enforcement is turned on, users must sign in with Google Authentication and can no longer use a Braze password. Each user must sign in with the Google account that matches their Braze dashboard email address. If a user selects a different Google account during sign-in, Braze rejects the authentication attempt.

### Troubleshooting Google SSO sign-in

If some users can't sign in with Google SSO, check the following:

- The user's Google account email matches their Braze dashboard email address exactly.
- The user has access to a Google account for their company email address.
- The user isn't suspended in Braze (**Settings** > **Company Users**).

## Next steps

After setting up SAML SSO, you can:

- [Enforce SSO-only login]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#single-sign-on-sso-authentication) in your security settings to restrict users from logging in with a password.
- [Set up SAML just-in-time provisioning]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning) so new users automatically create Braze accounts on their first SSO sign-in.
