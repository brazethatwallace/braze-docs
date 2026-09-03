## Testing preference centers {#testing-preference-centers}

Preference center links are generated for each user at send time and are tied to a live campaign or Canvas send. Test sends and editor previews do not support saving subscription changes. This is expected behavior.

### What you'll see

- **Test sends:** Preference center Liquid tags may not resolve to a valid link. If the page loads, the **Save Preferences** button is disabled, and subscription changes are not saved.
- **Drag-and-drop editor Preview tab:** You can preview layout and styling, but you cannot test saving preferences from the editor.

### How to test end-to-end

To verify that preference center links and buttons work before a full launch:

1. Create a campaign or Canvas email step that includes your preference center Liquid tag.
2. Target only your test users or a small internal segment.
3. Launch the message and open the email from a real inbox (not **Send Test**).
4. Select the preference center link, update subscription groups, and select **Save Preferences**.
5. Confirm the changes on the user's profile in the Braze dashboard.

{% if include.section == "api" %}
As an alternative for API-built preference centers, use the [Generate preference center URL endpoint]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) to retrieve a working URL for a specific user outside of a test send.
{% endif %}

For other test-send limitations, see [Send test messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages#limitations).

### Preview, test send, and live send

| Method | Preview layout | Save subscription changes |
| --- | --- | --- |
| Drag-and-drop editor **Preview** tab | Yes | No |
| Campaign or Canvas **Send Test** | Partial (email arrives) | No |
| Live send to a test user or segment | Yes | Yes |
| [Generate preference center URL]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) API | Yes | Yes |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Preview, test send, and live send" }
