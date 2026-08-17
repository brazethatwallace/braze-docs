{% if include.schema == "history" %}

| Spaltenname     | Datentyp     | Beschreibung |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Ihr Braze-Workspace-Bezeichner |
| `USER_ID` | VARCHAR | Der eindeutige Braze-Nutzer:innen-Bezeichner |
| `APP_ID` | VARCHAR | Die spezifische App innerhalb Ihres Workspace |
| `EXTERNAL_USER_ID` | VARCHAR | Ihr eigener Nutzer:innen-Bezeichner (falls festgelegt) |
| `TIME` | NUMBER | Unix-Zeitstempel (Sekunden) der Profilaktualisierung |
| `TIME_MS` | NUMBER | Unix-Zeitstempel (Millisekunden) der Profilaktualisierung |
| `UPDATE_SOURCE` | VARCHAR | Die Quelle der Attributaktualisierung (API, SDK, Dashboard usw.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Wann die Daten zuletzt in Snowflake aktualisiert wurden |
| `CUSTOM_ATTRIBUTES` | VARIANT | JSON-Objekt mit allen angepassten Attributen (Schlüssel-Wert-Paare) |
| `ARCHIVED` | BOOLEAN | Ob das Nutzerprofil archiviert ist |
| `EFF_DT` | TIMESTAMP_NTZ | Gültigkeitsdatum: Wann dieser Attributzustand begann |
| `END_DT` | TIMESTAMP_NTZ | Enddatum: Wann dieser Attributzustand endete (NULL für den aktuellen Zustand) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESHISTORYVIEWSHARED schema" }

{% elsif include.schema == "latest" %}

| Spaltenname     | Datentyp     | Beschreibung |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Ihr Braze-Workspace-Bezeichner |
| `USER_ID` | VARCHAR | Der eindeutige Braze-Nutzer:innen-Bezeichner |
| `EXTERNAL_USER_ID` | VARCHAR | Ihr eigener Nutzer:innen-Bezeichner (falls festgelegt) |
| `TIME` | NUMBER | Unix-Zeitstempel (Sekunden) der Profilaktualisierung |
| `TIME_MS` | NUMBER | Unix-Zeitstempel (Millisekunden) der Profilaktualisierung |
| `UPDATE_SOURCE` | VARCHAR | Die Quelle der Attributaktualisierung (API, SDK, Dashboard usw.) |
| `ARCHIVED` | BOOLEAN | Ob das Nutzerprofil archiviert ist |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Wann die Daten zuletzt in Snowflake aktualisiert wurden |
| `APP_ID` | VARCHAR | Die spezifische App innerhalb Ihres Workspace |
| `CUSTOM_ATTRIBUTES` | OBJECT | JSON-Objekt mit allen angepassten Attributen (Schlüssel-Wert-Paare) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATECUSTOMATTRIBUTEVIEWSHARED schema" }

{% alert note %}
Diese Ansicht verwendet den Typ `OBJECT` für `CUSTOM_ATTRIBUTES` anstelle von `VARIANT`. Verwenden Sie dieselbe JSON-Zugriffssyntax (`:attribute_name::TYPE`), um einzelne Attribute abzufragen.
{% endalert %}

{% endif %}