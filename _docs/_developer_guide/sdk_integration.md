---
nav_title: Integrate the SDK
article_title: Integrate the Braze SDK
description: "Learn how to integrate the Braze SDK."
page_order: 2.0
---

# ![Braze Logo]({% image_buster /assets/Braze_Primary_Icon_BLACK.svg %}){: style="float:right;width:120px;border:0;" class="noimgborder"}Integrate the Braze SDK

> Learn how to integrate the Braze SDK. Each SDK is hosted in its own public GitHub repository, which includes fully-buildable sample apps you can use to test Braze features or implement alongside your own applications. To learn more, see [References, Repositories, and Sample Apps]({{site.baseurl}}/developer_guide/references). For more general information about the SDK, see [Getting started: Integration overview]({{site.baseurl}}/developer_guide/getting_started/integration_overview).

For mirrored SDK README content in docs, see [Repository guides]({{site.baseurl}}/developer_guide/sdk_repository_guides).

{% alert tip %}
After integrating the SDK, you can enable [SDK Authentication]({{site.baseurl}}/developer_guide/sdk_integration/authentication) to add an additional layer of security by preventing unauthorized SDK requests. SDK Authentication is available for Web, Android, Swift, React Native, Flutter, Unity, Cordova, .NET MAUI (Xamarin), and Expo.
{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/sdk_integration.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/sdk_integration.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/sdk_integration.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/sdk_integration.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/sdk_integration.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/sdk_integration.md %}
{% endsdktab %}

{% sdktab roku %}
## Integrating the Roku SDK

### Step 1: Add files

Braze SDK files can be found in the `sdk_files` directory in the [Braze Roku SDK repository](https://github.com/braze-inc/braze-roku-sdk).

1. Add `BrazeSDK.brs` to your app in the `source` directory.
2. Add `BrazeTask.brs` and `BrazeTask.xml` to your app in the `components` directory.

### Step 2: Add references

Add a reference to `BrazeSDK.brs` in your main scene using the following `script` element:

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### Step 3: Configure

Within `main.brs`, set the Braze configuration on the global node:

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

You can find your [SDK endpoint]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) and API key within the Braze dashboard.

### Step 4: Initialize Braze

Initialize the Braze instance:

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Optional configurations

### Logging

To debug your Braze integration, you can view the Roku debug console for Braze logs. Refer to [Debugging code](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) from Roku Developers to learn more.

{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/sdk_integration.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/sdk_integration.md %}
{% endsdktab %}

{% sdktab chatgpt apps %}
{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}
{% endsdktab %}

{% sdktab vega %}
{% multi_lang_include developer_guide/vega/sdk_integration.md %}
{% endsdktab %}
{% endsdktabs %}

{% alert note %}
While performing QA on your SDK integration, use the [SDK Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging) to get troubleshoot issues without turning on verbose logging for your app.
{% endalert %}
