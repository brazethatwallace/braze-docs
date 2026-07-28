---
nav_title: SCIM
article_title: SCIM Endpoints
search_tag: Endpoint
page_order: 5
layout: dev_guide
alias: /scim/

description: "This landing page lists the Braze SCIM endpoints."
page_type: landing

guide_top_header: "SCIM Endpoints"
guide_top_text: "The [System for Cross-domain Identity Management (SCIM)](http://www.simplecloud.info/) specification is designed to make managing user identities in cloud-based applications and services easier by providing a defined schema for representing users and groups. Use the Braze SCIM endpoints to manage automated user provisioning."

guide_featured_title: ""
guide_featured_list:
  - name: "POST: Create Dashboard User Account"
    link: /docs/post_create_user_account
    image: /assets/img/braze_icons/plus-circle.svg
  - name: "GET: Look Up Existing Dashboard User Account by Resource ID"
    link: /docs/get_see_user_account_information
    image: /assets/img/braze_icons/eye.svg
  - name: "GET: Search Existing Dashboard User Account by Email"
    link: /docs/api/endpoints/scim/get_search_existing_dashboard_user
    image: /assets/img/braze_icons/eye.svg
  - name: "PUT: Update Dashboard User Account"
    link: /docs/post_update_existing_user_account
    image: /assets/img/braze_icons/pencil-01.svg
  - name: "DELETE: Remove Dashboard User Account"
    link: /docs/delete_existing_dashboard_user
    image: /assets/img/braze_icons/trash-01.svg
---


{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' subject='endpoints' %}

## How to export a list of users with dashboard access

Use this workflow to audit users who have access to your Braze dashboard.

1. Download the Security Event report from **Settings** > **Admin Settings** > **Security Settings** > **Security Event Download**.
2. Extract the user emails from the report.
3. For each email, use [GET: Search Existing Dashboard User Account by Email]({{site.baseurl}}/api/endpoints/scim/get_search_existing_dashboard_user) to retrieve the user details.
4. If needed, use the returned resource `id` with [GET: Look Up an Existing Dashboard User Account by Resource ID]({{site.baseurl}}/api/endpoints/scim/get_see_user_account_information) for additional user details.

For the full SCIM endpoint list, see [SCIM Endpoints]({{site.baseurl}}/api/endpoints/scim). For more information about the report source, see [Downloading a security event report]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report).
