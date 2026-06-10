{% multi_lang_include developer_guide/prerequisites/roku.md %}

## Wiping previously-stored data

The Roku SDK doesn't include a `wipeData` method. To produce a clean-slate state functionally equivalent to `wipeData()` on other Braze SDKs, clear the four Braze registry sections, then re-initialize the SDK.

The Braze Roku SDK persists data across the following registry sections:

| Section | Contents |
|---------|----------|
| `braze.section.device_id` | The device UUID used to identify this device in Braze. |
| `braze.section.user_id` | The external user ID, if one has been set. |
| `braze.section.session` | The active session UUID, start time, and end time. |
| `braze.section.config` | Cached SDK configuration and feature flag data. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Wiping previously-stored data" }

### Step 1: Clear the registry sections

Use [`roRegistry.Delete()`](https://developer.roku.com/docs/references/brightscript/components/roregistry.md) to delete each Braze section, then call `Flush()` to persist the changes:

```brightscript
sub WipeBrazeData()
    registry = CreateObject("roRegistry")
    registry.Delete("braze.section.device_id")
    registry.Delete("braze.section.user_id")
    registry.Delete("braze.section.session")
    registry.Delete("braze.section.config")
    registry.Flush()
end sub
```

### Step 2: Re-initialize the Braze SDK

When you [initialize the Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku) again, the SDK handles the missing registry data gracefully:

- The device ID section is empty, so the SDK generates a new UUID and treats the device as anonymous.
- The user ID section is empty, so the SDK defaults to an anonymous user (an empty string `""`).
- The session section is empty, so the SDK starts a new session.
- The config section is empty, so the SDK re-fetches the configuration from the server.

{% alert note %}
The Roku SDK doesn't generate any server-side delete request when you clear the registry. If you also need to remove the user from Braze, send a request to [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) using the user's `external_id` or `braze_id`.
{% endalert %}
