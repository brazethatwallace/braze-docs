---
nav_title: Custom event properties
article_title: Custom Event Properties
page_order: 0
page_type: reference
description: "This article describes custom event properties, their expected format, how to use them, and custom event property storage."
---

# Custom event properties

> This article describes custom event properties, their expected format, how to use them for messaging and segmentation, and custom event property storage.

Custom event properties are custom event metadata or attributes that describe a specific occurrence of an event. These properties can be used for further qualifying trigger conditions, increasing personalization in messaging, tracking conversions, and generating more sophisticated analytics through raw data export.

Custom event properties aren't stored on the Braze profile and therefore don't log data points (see [Data points](#data-points) for exceptions).

## Viewing event property values for a user

To view the value of a custom event property for a specific user, the following options are available depending on your setup:

- **Currents:** If customer behavior events are enabled, event properties are included in the Currents export.
- **Event User Log:** If the user is a test user and performed the event recently, the event and its properties will appear in **Settings** > **Event User Log**.
- **Segmentation:** If custom event property storage is enabled for that property, you can create a segment using the event property filter to check if the user qualifies.

{% alert important %}
Each custom event or purchase can have up to 256 distinct custom event properties. If a custom event or purchase is logged with more than 256 properties, only the first 256 will be captured and available for use.
{% endalert %}

## Expected format {#expected-format}

Property values must be an object: keys are the property names (non-empty strings, 255 characters or fewer, no leading `$`), and values are the property values. For supported data types, format requirements, and payload limits, see [Data types]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#event-property-data-types).

You can change the data type of your custom event property, but be aware of the impacts of [changing data types]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#changing-custom-attribute-or-event-data-type) after data has been collected.

### Reserved keys

You cannot use reserved keys as event property names. Using a reserved key in the `properties` object returns the error "Invalid 'properties' field".

| Property | Reserved Key |
| --- | --- |
| Custom events | `time` and `event_name` | 
| Purchase events |`time`, `product_id`, `quantity`, `event_name`, `price`, `currency` | 
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reserved keys" }

## Using custom event properties

Custom event properties can be used to qualify campaign triggers, track conversions, and personalize messaging.

### Trigger messages

Use custom event properties to further narrow your audience for a particular campaign or Canvas. For example, if you have an eCommerce application and want to send a message to a user when they abandon their cart, you can add a custom event property of `price` to improve your target audience and allow for increased campaign personalization.

![Custom event property filters for an abandoned card. Two filters are combined with an AND operator to send this campaign to users who abandoned their card with a price between 100 and 200 dollars]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"){: style="max-width:70%;"}

Nested custom event properties are also supported in [action-based delivery]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

![Custom event property filters for an abandoned card. One filter is selected if any items in the cart have a price more than 100 dollars.]({% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"){: style="max-width:70%;"}

### Personalize messages

You can also use custom event properties for personalization within the messaging template. Any campaign using [action-based delivery]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) with a trigger event can use custom event properties from that event for messaging personalization.

#### Considerations with filters

- **API calls:** When making API calls and using the "is blank" filter, a custom event property is considered "blank" if excluded from the call. For example, if you include `"event_property": ""`, your users are considered "not blank".
- **Integers:** When filtering for a number custom event property and the number is very large, don't use the "exactly" filter. If a number is too large, it may be rounded at a certain length, so your filter won't work as expected.

#### Type coercion for comparisons

When using event properties in Liquid conditional statements, you may encounter the error `Liquid error: comparison of String with 0 failed` if you're comparing an integer event property using operators like greater than, less than, or equal to. This happens because Liquid treats the property as a string by default.

To fix this, use the `plus: 0` filter to coerce the property to a number before comparison:

{% raw %}
```liquid
{% assign time_spent = {{event_properties.${time_spent}}} | plus: 0 %}
{% if time_spent >= 100 %}
  Great job completing the level quickly!
{% endif %}
```
{% endraw %}

For example, if you have a gaming app and want to send a message to users who completed a level, you could further personalize your message with a property for the time it took users to complete that level.

The following message is personalized for three different segments using [conditional logic]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic). The custom event property called `time_spent` can be included in the message by calling ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% assign time_spent = {{event_properties.${time_spent}}} | plus: 0 %}
{% if time_spent < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif time_spent < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
If the user doesn't have an internet connection, triggered in-app messages with templated custom event properties (for example, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) fail and don't display.
{% endalert %}

For a full list of Liquid tags that cause in-app messages to deliver as templated in-app messages, see [Frequently asked questions]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages).

#### Canvas

In Canvas, `context` and `event_properties` serve different purposes:

- **`context`**: Properties from the event or API call that triggered Canvas entry. Use `context` in any Message step, including the first.
- **`event_properties`**: Properties from a custom event or purchase that occurs during the journey. Use them only in the first Message step after an [Action Paths]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) step—not on the Everyone Else path, and not in later Message steps.

{% alert important %}
In the first Message step of a Canvas, use `context` instead of `event_properties`, or add an Action Paths step before the Message step. Exception: for in-app messages, you can use `event_properties` in the first Message step when that event is the Canvas entry trigger.
{% endalert %}

For more information, see [Context and event properties]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) and [Canvas entry properties and event properties](#canvas-entry-properties-and-event-properties).

### Segmentation

Use event property segmentation to target users based on custom events taken and the properties associated with those events. This increases your filtering options when segmenting by purchase and custom events.

Event properties for custom events are updated in real-time for any segment that uses them. You can manage properties by going to **Data Settings** > **Custom Events** and selecting **Manage properties** for the associated custom event. Custom event properties used in certain segment filters have a maximum look-back history of 30 days.

#### Adding event properties for segmentation

You need the "Edit Custom Event Property Segmentation" [user permission]({{site.baseurl}}/user_guide/data/infrastructure/data_points#viewing-data-point-usage) to create segments based on event property recency and frequency.

By default, you can have 20 segmentable event properties per workspace. Contact your Braze account manager to increase this limit.

To add event properties for segmentation, do the following:

1. Go to your custom event and select **Manage properties**.
2. Select the **Enable segmentation** toggle to add the event property for segmentation. You can access additional filtering options when segmenting.

The event property segmentation filters include:

{% multi_lang_include data_activation/custom_event_property_filters.md %}

![A filter group that has 'Abandoned Cart' with property 'number of items' and value 2 more than 1 time in the last 30 calendar days.]({% image_buster /assets/img/nested_object3.png %})

Data is logged only for a given event property after you enable it, and event properties are available only from that date moving forward.

#### Data points

In regards to subscription usage, custom event properties enabled for segmentation with the following filters are all counted as separate data points in addition to the data point counted by the custom event itself:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Canvas entry properties and event properties

{% multi_lang_include canvas/entry_event_properties.md %}

### Nested objects {#nested-objects}

You can use nested objects (objects inside of another object) to send nested JSON data as properties of custom events and purchases. This nested data can be used for templating personalized information in messages, triggering message sends, and segmenting users.

To learn more, refer to our dedicated page on [Nested objects]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

## Custom event property storage

Custom event properties are designed to help you increase targeting precision and make messages feel even more personalized. Custom event properties can be stored within Braze in both the short and long term.

You can segment based on the values of event properties in two ways:

1. **Within 30 days:** You can use event property segmentation based on the frequency and recency of specific event property values within Braze segments. This option impacts data usage.<br><br>
2. **Within and beyond 30 days:** To cover both short-term and long-term event property segmentation, you can use [Segment Extensions]({{site.baseurl}}/user_guide/audience/segments/segment_extension). This feature segments users based on custom events and event properties tracked within the past two years. This option does not impact data usage.

Contact your Braze customer success manager for recommendations on the best approach depending on your specific needs.
