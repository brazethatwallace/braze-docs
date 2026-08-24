---
# Glossary `name` (singular vs plural) — keep this in sync when adding rows:
# - Default to singular for a feature, channel, mechanism, or abstract concept (campaign, webhook, conversion event).
# - Use plural for user populations (inactive users), data you store as sets (custom attributes, custom events), subscription groups, and fixed phrases (key-value pairs).
# - Keep branded or UI-locked names as published (Content Cards, API campaigns, Canvas, Connected Content, Currents).
# - When unsure, match the canonical doc title; prefer one consistent glossary heading per entry so the list sorts predictably.
page_order: 10
nav_title: Terms to know
article_title: Braze Terms to Know

layout: glossary_page
glossary_top_header: "Terms to Know"
glossary_top_text: "These terms should help you as you begin your journey to better customer and user bonds with Braze. Give this a read before you begin your onboarding."
page_type: glossary
description: "This glossary covers important terms to know as you go through the Braze onboarding process."

glossaries:
  - name: Active user
    description: For campaign targeting, Braze defines an <a href="/docs/user_guide/messaging/campaigns/ideas_and_strategies/active_user_campaigns">active user</a> for a given period as anyone who has a session in that period (users updated via the API also count for that period). For <a href="/docs/user_archival#active-users">user archival</a> and reachability statistics, Braze uses a broader definition that also includes profile updates, messages sent to the user, and interactions with messages.
  - name: Alloys
    description: Alloys are our <a href="/docs/partners/home">Technology Partners</a>.
  - name: Anonymous users
    description: When a user profile is recognized via the SDK, an anonymous user profile is created with the associated <a href="/docs/api/basics#user-ids">Braze user ID</a>.
  - name: API campaigns
    description: <a href="/docs/api/api_campaigns">API campaigns</a> use the Braze dashboard to generate a <code>campaign_id</code> (and variation IDs) while you supply copy, audience, schedule, and assets through the <a href="/docs/api/endpoints/messaging">messaging APIs</a>. They differ from <a href="/docs/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery">API-triggered campaigns</a>, where you trigger a fully configured campaign from the dashboard via API.
  - name: Application program interface (API)
    description: The <a href="/docs/api/basics">Braze API</a> provides a web service where you can record actions taken by your users directly via HTTP, rather than through the mobile SDKs. This allows you to, for example, pass user data to Braze that is not tracked within your app or website.
  - name: App instance
    description: App instances refer to the different sites and apps that are collected in a workspace.
  - name: Braze (the product)
    description: Sometimes referred to as the dashboard, this product controls all of the data and interactions at the heart of the Braze platform. Braze customers use it to manage notifications, set up targeted messaging campaigns, and view analytics. Developers use it to manage settings for integrating apps, such as API keys and push notification credentials.
  - name: Team
    description: Braze admins can divide a subset of dashboard users into <a href="/docs/user_guide/administer/global/user_management/teams">Teams</a> with varying user roles and permissions. This allows Braze admins to limit access to certain features by group membership.
  - name: Campaign
    description: Campaigns are customizable messaging methods to deliver personalized response to your customers. You can <a href="/docs/user_guide/messaging/campaigns">build campaigns</a> using different messaging channels to send your unique messages.
  - name: Canvas
    description: <a href="/docs/user_guide/messaging/canvas">Canvas</a> is a single unified interface where marketers can set up campaigns with multiple messages and steps to form a cohesive journey. Canvas allows you to compare and optimize those experiences using comprehensive analytics for the full user experience.
  - name: Connected Content
    description: <a href="/docs/user_guide/messaging/design_and_edit/personalize/connected_content">Connected Content</a> expands on marketing personalization to boost customer engagement and conversions. You can insert any information accessible using API directly into messages you send to users. Connected Content allows for pulling content either directly from your web server or publicly accessible APIs.
  - name: Content Cards
    description: <a href="/docs/user_guide/channels/content_cards">Content Cards</a> allow you to send a highly targeted, dynamic stream of rich content to your customers right within the apps they love, without interrupting their experience. Content Cards can be sent to iOS, Android, and web users.
  - name: Conversion event
    description: A <a href="/docs/user_guide/messaging/messaging_fundamentals/conversion_events">conversion event</a> is a success metric that records whether a recipient performed a high-value action within a conversion window after receiving your message (or after entering a Canvas or control group, depending on channel and setup). Use conversion events to measure campaign and Canvas performance beyond sends alone.
  - name: Currents
    description: <a href="/docs/user_guide/data/distribution/braze_currents">Currents</a>, our data streaming export, is included in certain Braze packages. Braze Currents allows you to integrate through Data Storage using flat files or to our Behavioral Analytics and Customer Data partners using batched JSON payloads to a designated endpoint.
  - name: Custom attributes
    description: <a href="/docs/user_guide/data/activation/attributes/custom_attributes">Custom attributes</a> are a collection of your users' unique traits. They are best for storing attributes about your users, or information about low-value actions within your application. You can assign custom attributes to users within the dashboard. You can filter and segment your users according to these attributes for both <a href="/docs/developer_guide/analytics/setting_user_attributes?sdktab=swift">Swift</a> and <a href="/docs/developer_guide/analytics/setting_user_attributes?sdktab=android">Android</a> campaigns.
  - name: Custom events
    description: <a href="/docs/user_guide/data/activation/events/custom_events">Custom events</a> are actions taken by your users; they're best suited for tracking high-value user interactions with your application.
  - name: Data point
    description: A data point is counted when a <a href="/docs/user_guide/data/activation/attributes/custom_attributes">custom attribute</a> is set or updated (even if you're updating it with the same value), a <a href="/docs/user_guide/data/activation/events/custom_events">custom event</a> or purchase event is logged, any standard data (for example, <code>email</code>, <code>first_name</code>, <code>last_name</code>, <code>country</code>, or <code>home_city</code>) is logged, when a session starts, and when a session ends.
  - name: Deep linking
    description: <a href="/docs/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls">Deep links</a> are used to direct customers to their next action or engagement. Using deep links, you can connect a message with a targeted piece of content within a website or mobile app.
  - name: Dormant users
    description: A user is considered <a href="/docs/user_archival#dormant-users">dormant</a> when they have had no qualifying activity in the last twelve months—they have not used any app or website in the workspace, have not received any messages from the workspace, and have not been updated in more than twelve months. By default Braze uses a twelve-month window for dormant archival; your company settings can override the number of days.
  - name: Endpoint
    description: An end of a communication channel also known as an API <a href="/docs/api/endpoints">endpoint</a> is used within the Braze messaging API for sending and scheduling messages.
  - name: Exception event
    description: In Canvas, <a href="/docs/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events">exception events</a> are specific actions that remove a user from the journey when they occur (for example, placing an order). They keep follow-up messages relevant after the user completes your goal. See <a href="/docs/user_guide/messaging/canvas/create_a_canvas/exit_criteria">Exit criteria</a> for how exits are evaluated and timed.
  - name: External ID
    description: The <code>external_id</code> is the primary user identifier on a Braze user profile. It ties the same person across channels and devices when you assign IDs from your own systems. Anonymous profiles may not have an <code>external_id</code> until you identify the user. For more information, see <a href="/docs/user_guide/get_started/users_and_segments">Users and segments</a> and <a href="/docs/api/basics#user-ids">User IDs</a>.
  - name: Frequency capping
    description: <a href="/docs/user_guide/messaging/messaging_fundamentals/frequency_capping">Frequency capping</a> allows you to manage communication without overwhelming your audience. It's an automated limit on messages to prevent users from receiving too many communications in a short period of time.
  - name: HIPAA
    description: HIPAA is an acronym for Health Insurance Portability and Accountability Act. Braze is <a href="/docs/developer_guide/disclosures/security_qualifications#hipaa">HIPAA compliant</a>. HIPAA requirements involve administrative, physical, and technical security.
  - name: In-app message
    description: <a href="/docs/user_guide/channels/in_app_messages">In-app messages</a> are mobile messages that appear within your application. They help you get content to your user without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value out of your app.
  - name: Inactive users
    description: A user is considered <a href="/docs/user_archival#inactive-users">inactive</a> when they are unreachable on major messaging channels (for example, email, SMS, push, WhatsApp, and LINE per your configuration), have not used any app or website in the workspace in more than six months, have not received any messages from the workspace in more than six months, and have not been updated in more than six months. Inactive users are candidates for archival along with dormant users. By default Braze uses a six-month window for inactive archival; your company settings can override the number of days.
  - name: IP warming
    description: <a href="/docs/user_guide/channels/email/email_setup/ip_warming">IP warming</a> is the practice of gradually increasing the amount of mail sent out from a dedicated IP. This helps establish a reputation with Internet Service Providers, minimizing the probability of your messages getting flagged.
  - name: Key-value pairs
    description: <a href="/docs/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs">Key-value pairs</a> are linked data items where the key is a unique identifier and the value is the content. They can be used to send extra data payloads to user devices.
  - name: Liquid
    description: Liquid is a commonly-used, customer-facing template language created by Shopify and written in Ruby. <a href="/docs/user_guide/messaging/design_and_edit/personalize/liquid">Liquid</a> is used to load and pull dynamic content. Liquid allows you to use objects, tags, and filters to <a href="/docs/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags">add personal customization</a>.
  - name: Messaging channel
    description: <a href="/docs/user_guide/channels">Messaging channels</a> are ways you can virtually communicate with your customers–through push notifications on their phone or web browser, email, in-app messages, and so much more!
  - name: Monthly active user (MAU)
    description: These are users who have a session within the last 30 days.
  - name: Multichannel messaging
    description: Messaging a user across various mediums, such as a combination of email, web push, and mobile push notifications. <a href="/docs/developer_guide/getting_started/platform_overview#multichannel-messaging">Messaging channels</a> are best used in concert and with regularity to re-engage lost users, retain active users, and energize your brand ambassadors.
  - name: Multivariate testing
    description: <a href="/docs/user_guide/messaging/ab_testing">A/B testing</a> compares a smaller set of message versions; <a href="/docs/user_guide/messaging/ab_testing/create_tests">multivariate testing</a> compares multiple variables at once to see which combination performs best. You can configure both from the dashboard for supported campaign types.
  - name: New user
    description: Braze considers a new user as anyone who has newly installed your app. Alternatively, a new user can also be defined as a user with a user ID that has not been previously identified within Braze.
  - name: Personalization
    description: Using technology to take into account the individual preferences and tendencies of each user when communicating with them. <a href="/docs/user_guide/messaging/design_and_edit/personalize">Personalized messaging</a> helps build valuable customer experiences by tailoring to their preferences.
  - name: Push message
    description: A <a href="/docs/user_guide/channels/push">push message</a>, or push notification, is a notification that appears from a mobile application. Push notifications often appear as pop-up dialogs and banners for both iOS and Android.
  - name: Push token
    description: A push token is a unique key, created and assigned by Apple or Google to create a connection between an app and an iOS, Android, or web device. <a href="/docs/api/objects_filters/user_attributes_object#migrate-push-tokens">Push token migration</a> is the importing of those already-generated keys into Braze.
  - name: Push time to live (TTL)
    description: Also known as <a href="/docs/user_guide/administer/global/workspace_settings/push_settings">Push TTL</a>, time to live refers to the period that campaigns will continue to attempt to be delivered to an offline user.
  - name: Race condition
    description: A <a href="/docs/user_guide/messaging/ab_testing/concepts/race_conditions">race condition</a> is a software engineering concept that describes some undesirable situation that occurs when a system tries to perform several operations simultaneously, but because of the nature of the system, the operations must be done in the correct sequence to be done correctly. <br><br>In the Braze platform, segmenting a triggered campaign on user data recorded at the time of the event may cause a race condition. This happens when a change in the user attribute on which the campaign is segmented hasn't yet been processed for the user at the time segment membership is determined and the campaign is sent and can lead to the user not receiving the campaign.
  - name: Rate limiting
    description: <a href="/docs/user_guide/messaging/messaging_fundamentals/frequency_capping">Rate limiting</a> controls how quickly messages leave Braze (for example, delivery speed per minute or user-centric limits using segment filters). It works alongside frequency capping on the same page, which limits how many messages a user receives in a time window.
  - name: Segmentation
    description: Dashboard <a href="/docs/user_guide/audience/segments">segmentation</a> allows you to create groups or extensions of users based on powerful filters of their in-app behavior, demographic data, and more.
  - name: Software development kit (SDK)
    description: <a href="/docs/developer_guide/getting_started/sdk_overview">SDKs</a> are integrated into your mobile apps, websites, and connected experiences and provide marketing, messaging, and analytics tools. Braze publishes SDK integration guides for platforms such as <a href="/docs/developer_guide/sdk_integration?sdktab=swift">Swift</a> and <a href="/docs/developer_guide/sdk_integration?sdktab=android">Android</a>; for Web and other platforms, follow the integration paths linked from the SDK overview.
  - name: Subscription groups
    description: <a href="/docs/user_guide/audience/subscription_preferences/subscription_groups">Subscription groups</a> layer on top of global subscription states so you can offer granular opt-in choices (for example, newsletters versus promotions). Similar patterns exist for channels such as SMS and WhatsApp; always target a subscription group where your channel requires it.
  - name: Sunsetting
    description: Sunsetting refers to the process of identifying disengaged users and ceasing active messaging to these users without them having to take any action. Creating sunset policies for your <a href="/docs/user_guide/channels/email/best_practices/sunset_policies">email</a> and <a href="/docs/user_guide/channels/push/best_practices#implement-a-sunset-policy-for-unresponsive-users">push</a> messages can help curb impacts to your open rates.
  - name: Tag
    description: <a href="/docs/user_guide/administer/global/workspace_settings/tags">Tags</a> are a tool that help you categorize, organize, and sort your engagement across one or multiple campaigns.
  - name: User alias
    description: <a href="/docs/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#assigning-user-aliases">User aliases</a> are alternative identifiers you can assign to anonymous profiles before an <code>external_id</code> exists, so you can reference the same person across devices or channels until they log in.
  - name: User archival
    description: <a href="/docs/user_archival">User archival</a> refers to users that have been archived. At Braze, this includes both inactive and dormant users. Archival evaluates the inactive and dormant rules in Braze services (see User archival for scheduling, workspace eligibility such as user-count thresholds, and how to customize windows with company settings or Canvas).
  - name: User profile
    description: A <a href="/docs/user_guide/audience/manage_audience/user_profiles">user profile</a> is the central record for each person in Braze, including identifiers, attributes, events, purchases, devices, engagement history, and message history. Profiles power segmentation, personalization, and compliance workflows across channels.
  - name: Webhook
    description: <a href="/docs/user_guide/channels/webhooks">Webhooks</a> allow you to trigger non-app actions such as SMS text message delivery. You can use webhooks to provide other systems and applications with real-time information. The flexibility of this feature allows you to send information to any endpoint.
  - name: Workspace
    description: A <a href="/docs/user_guide/get_started/workspaces">workspace</a> is the container where Braze stores data and where your team builds campaigns, Canvases, and segments. Each workspace holds one or more <a href="/docs/user_guide/get_started/workspaces#understanding-workspaces">app instances</a> (the individual apps and sites that send data into that workspace).

---

