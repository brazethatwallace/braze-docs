{% alert note %}
Für RCS-Nachrichten werden Linkverkürzung und Klick-Tracking auf URL-Ebene für URLs im Nachrichtentext unterstützt, jedoch nicht für URLs in vorgeschlagenen Aktionen. Klicks auf URLs vorgeschlagener Aktionen werden als RCS-Klick-Ereignisse erfasst, aber die Felder `URL` und `SHORT_URL` sind in Currents und Snowflake null.
{% endalert %}