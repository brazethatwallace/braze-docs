{% alert note %}
**Datumsfelder verstehen:**
- `TIME` und `TIME_MS`: Stellen den Zeitpunkt dar, zu dem das Kundenprofil or Nutzerprofil-Update or aktualisieren in Braze erfolgte (in Sekunden bzw. Millisekunden). Bei nachträglich aufgefüllten Daten entsprechen diese Werte dem Zeitpunkt der Auffüllung.
- `SF_UPDATED_AT`: Stellt den Zeitpunkt dar, zu dem die Daten zuletzt in Snowflake gespeichert wurden. Dieses Feld ist besonders nützlich, um die Aktualität der Daten zu bestimmen – also den Zeitpunkt, zu dem die Zeile zuletzt mit Ihrem Data Warehouse synchronisiert wurde.
{% endalert %}