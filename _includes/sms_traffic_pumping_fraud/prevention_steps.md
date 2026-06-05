### What immediate foundational steps should my company take to prevent this fraud?

The most critical step your company can take within your customer engagement platform is to minimize your attack surface using geographic limitations.

#### Utilize the Braze Geographic Permissions allowlist

You should proactively audit the regions where your actual target customers reside and configure an allowlist to explicitly permit messaging only to those countries. For setup steps, see [Geographic permissions]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions/).

##### Block high-risk destinations

If you only do business in North America or Western Europe, there's no reason to leave the doors open to high-cost international countries in other regions. As a rule of thumb, proactively disable any country where you don't actively market or have operations to eliminate unnecessary exposure.

{% if include.detail %}
Thoughtfully consider any request to open routes to flagged **High Fraud Risk** countries.

##### Layered defense

Geographic restrictions are a critical first step, but are only one layer in a broader defense-in-depth strategy. No single control is sufficient—combining multiple measures makes abuse significantly more complex and difficult to execute at scale. Beyond geographic allowlisting, key controls include protections such as:

- Client-side and server-side validation to enforce data integrity
- Sensible rate limiting on vulnerable endpoints to slow automated submissions
- CSRF tokens to ensure requests originate from your legitimate forms
- CAPTCHA to deter bulk fraudulent entries

{% alert note %}
We recommend collaborating with your internal Security team to tailor these suggestions to your specific infrastructure.
{% endalert %}
{% endif %}
