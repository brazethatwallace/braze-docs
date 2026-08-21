{% if include.schema == "history" %}

| Column name     | Data type     | Description |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Your Braze workspace identifier |
| `USER_ID` | VARCHAR | The unique Braze user identifier |
| `APP_ID` | VARCHAR | The specific app within your workspace |
| `EXTERNAL_USER_ID` | VARCHAR | Your own user identifier (if set) |
| `TIME` | NUMBER | Unix timestamp (seconds) of the profile update |
| `TIME_MS` | NUMBER | Unix timestamp (milliseconds) of the profile update |
| `UPDATE_SOURCE` | VARCHAR | The source of the attribute update (API, SDK, dashboard, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | When the data was last updated in Snowflake |
| `CUSTOM_ATTRIBUTES` | VARIANT | JSON object containing all custom attributes (key-value pairs) |
| `ARCHIVED` | BOOLEAN | Whether the user profile is archived |
| `EFF_DT` | TIMESTAMP_NTZ | Effective date: when this attribute state began |
| `END_DT` | TIMESTAMP_NTZ | End date: when this attribute state ended (NULL for current state) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESHISTORYVIEWSHARED schema" }

{% elsif include.schema == "latest" %}

| Column name     | Data type     | Description |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Your Braze workspace identifier |
| `USER_ID` | VARCHAR | The unique Braze user identifier |
| `EXTERNAL_USER_ID` | VARCHAR | Your own user identifier (if set) |
| `TIME` | NUMBER | Unix timestamp (seconds) of the profile update |
| `TIME_MS` | NUMBER | Unix timestamp (milliseconds) of the profile update |
| `UPDATE_SOURCE` | VARCHAR | The source of the attribute update (API, SDK, dashboard, etc.) |
| `ARCHIVED` | BOOLEAN | Whether the user profile is archived |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | When the data was last updated in Snowflake |
| `APP_ID` | VARCHAR | The specific app within your workspace |
| `CUSTOM_ATTRIBUTES` | OBJECT | JSON object containing all custom attributes (key-value pairs) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATECUSTOMATTRIBUTEVIEWSHARED schema" }

{% alert note %}
This view uses `OBJECT` type for `CUSTOM_ATTRIBUTES` instead of `VARIANT`. Use the same JSON accessor syntax (`:attribute_name::TYPE`) to query individual attributes.
{% endalert %}

{% endif %}
