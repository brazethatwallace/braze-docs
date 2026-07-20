{% alert note %}
As mentioned in [Shopify overview]({{site.baseurl}}/shopify_overview/), if you want to use a third-party capture form, your developers need to integrate Braze SDK code. This will let you capture the email address and global email subscription status from form submissions. Specifically, you need to implement and test these methods to your `theme.liquid` file:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Sets the email address on the user profile
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Updates the global email subscription status
{% endalert %}
