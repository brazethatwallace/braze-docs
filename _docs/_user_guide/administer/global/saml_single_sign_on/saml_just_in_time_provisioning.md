---
nav_title: SAML Just-in-Time provisioning
article_title: SAML Just-in-Time Provisioning
page_order: 1
page_type: tutorial
description: "This article will walk you through how to configure SAML just-in-time provisioning to allow new company users to create a Braze account on their first sign in." 

---

# SAML just-in-time provisioning 

> Just-in-time provisioning works with [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup) to allow new company users to create a Braze account on their first sign in. This eliminates the need for administrators to manually create an account for a new company user, choose their permissions, assign them to a workspace, and wait for them to activate their account.

As a security measure, SAML just-in-time provisioning (JITP) only works for users with email domains that already exist in your company. JITP is only possible for domains where there is already at least one confirmed, non-impersonation developer in the company. 

For example, let's say the account ```jon.smith@decorumsoft.com``` can use JITP to log into Decorumsoft. The account ```jane.smith@decorumsoft.com``` has the same domain and can also be allowed provisioning. However, if you try to use JITP with ```jon.smith@decorumsoft.eu```, provisioning won't be allowed because there isn't a ```decorumsoft.eu``` account within the Decorumsoft Braze dashboard. 

To make an exception for a company, contact [Support]({{site.baseurl}}/braze_support).

## Prerequisites

SAML JITP requires that SAML SSO is set up and integrated. It is not compatible with Google SSO, and is only supported for Identity Provider Initiated (IdP-initiated) login workflows.

| Requirement | Details |
|---|---|
| SAML SSO | Configured and tested before enabling JITP. See [SAML SSO setup]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup). |
| IdP-initiated login | Users must sign in through your IdP portal on first login. SP-initiated login alone does not provision new users. |
| Email domain | The user's email domain must already exist in your company (at least one confirmed, non-impersonation developer with that domain). |
| Company enablement | Braze must enable the `saml_jit_provisioning` feature for your company before the **Automatic user provisioning** toggle appears. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="JITP prerequisites" }

{% alert important %}
SAML just-in-time provisioning must be enabled for your company by Braze. Contact your account manager or [Braze Support]({{site.baseurl}}/braze_support) if the **Automatic user provisioning** toggle isn't available.
{% endalert %}

## How JITP works

When JITP is enabled and a new user signs in through your IdP for the first time:

1. Braze validates the SAML assertion and checks that the user's email domain is allowed for JITP.
2. Braze creates a dashboard user account using the email from the SAML assertion.
3. Braze assigns the default workspace and permission set configured in **Security Settings**.
4. The user can access Braze immediately without a separate invitation or activation step.

JITP doesn't update permissions for existing users. It only creates accounts for users who don't already exist in your company.

## Setting up SAML just-in-time provisioning (JITP)

Have a Braze administrator do the following:

1. Navigate to **Settings** > **Company Settings** > **Admin Settings** > **Security Settings**.
2. In the **SAML SSO** section, toggle on the **Automatic user provisioning** option.
3. Select a default workspace to add a new company user.
4. Select the default permission set to assign to that new company user. To learn how to create a permission set, see [Setting user permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

{% alert note %}
If your company uses granular permissions, review the default permission set after migration to confirm new JITP users receive the intended access.
{% endalert %}

5. Select **Save changes**.
6. In your SSO provider's settings, add all users that need Braze access to your SSO provider's directory.
7. Instruct users to access Braze through your IdP portal for their first login. After this, the SAML single sign-on button displays for future logins.

## Frequently asked questions

### How do I disable SAML JITP?

After setting up JITP, you must [contact Support]({{site.baseurl}}/braze_support) to have it turned off.

### Can JITP assign different permissions per user?

No. All JITP-created users receive the default workspace and permission set configured in **Security Settings**. To assign different access, create users manually or use [SCIM automated user provisioning]({{site.baseurl}}/scim/automated_user_provisioning).

### Does JITP work with SP-initiated login?

No. JITP only runs during IdP-initiated login when a user starts from your identity provider portal.

## Troubleshooting

### User was not provisioned on first SSO sign-in

Check the following:

- JITP is enabled and saved in **Security Settings**.
- The user signed in through the IdP portal (IdP-initiated), not only from the Braze login page.
- The user's email domain already exists in your company.
- The SAML assertion includes a valid `email` attribute that matches the address the user signs in with.

### Single sign-on button doesn't appear with Microsoft Entra ID

The **Sign-On URL** field in Microsoft Entra's **Basic SAML Configuration** form for Braze may cause users to only see a password option, not an SSO button, with IdP-initiated login. To prevent this issue, leave the **Sign-On URL** field blank when configuring Braze in your Microsoft Entra admin center.