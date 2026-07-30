If you see two custom data entries with the same visible name, one entry may include an invisible leading or trailing space.

To troubleshoot and fix this:

1. Go to **Data Settings** > **Custom Attributes** or **Custom Events**, then locate the two entries that appear to have the same name.
2. Confirm whether one name contains hidden whitespace:
    1. Right-click each name and select **Inspect**.
    2. Check the HTML text value in your browser developer tools.
    3. Compare the values (for example, `email` versus ` email`).
    4. If needed, refer to [Inspect and edit pages and styles with Chrome DevTools](https://developer.chrome.com/docs/devtools/inspect-mode).
3. Decide which name should remain as your canonical key, and standardize on that exact spelling and casing.
4. If one entry includes leading or trailing spaces and was created directly in the dashboard, stop using that entry and move to the canonical key:
    - Update any dashboard workflows, CSV imports, and internal runbooks to use the canonical key.
    - [Blocklist custom data]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data) for the incorrect entry when you're ready to retire it.
5. Verify your ingestion paths:
    - API and SDK payloads automatically strip leading and trailing spaces.
    - Dashboard-created names do not auto-trim, so manual entry and governance are required.
