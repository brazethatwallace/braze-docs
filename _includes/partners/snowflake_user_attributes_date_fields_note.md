{% alert note %}
**Understanding date fields:**
- `TIME` and `TIME_MS`: Represent when the user profile update occurred in Braze (in seconds and milliseconds, respectively). For backfilled data, these values are the time of the backfill.
- `SF_UPDATED_AT`: Represents when the data was last persisted in Snowflake. This field is most useful for determining data freshness—when the row was most recently synced to your data warehouse.
{% endalert %}
