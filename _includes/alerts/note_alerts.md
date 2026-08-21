{% if include.alert == 'Content Cards frequency capping' %}

{% alert note %}
Frequency capping doesn't apply to Content Cards.
{% endalert %}

{% endif %}

{% if include.alert == 'Custom Attributes time attribute' %}

{% alert note %}
A date string such as "12-1-2021" or "12/1/2021" will be converted to a datetime object and treated as a [time attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% endif %}

{% if include.alert == 'Manage custom data storage' %}

{% alert note %}
All user profile data (custom events, custom attributes, custom data) is stored as long as those profiles are active.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment profiles first app use' %}

{% alert note %}
Braze doesn't generate profiles for users until they've used the app for the first time, so you can't target users who haven't opened your app yet.
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify attributes REST API' %}

{% alert note %}
All attributes are sourced from the Braze REST API.
{% endalert %}

{% endif %}

{% if include.alert == 'subscription group limit' %}

{% alert note %}
You can add up to 450 subscription groups per workspace.
{% endalert %}

{% endif %}

{% if include.alert == 'GIF platform support' %}

{% alert note %}
GIFs are not supported in Android push notifications. This is an Android platform limitation, not a Braze limitation.
<br><br>
- For in-app messages and Content Cards on Android, you can support GIFs by integrating a third-party image library, such as [Glide](https://bumptech.github.io/glide/) or [Fresco](https://frescolib.org/). 
<br>
- On iOS, push notifications support GIFs. In-app messages and Content Cards require a custom GIF image provider.
{% endalert %}

{% endif %}