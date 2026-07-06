### Externe Schriftarten-Domains {#external-font-domains}

Beim Erstellen angepasster {{ include.page_type }}-Seiten bereinigt Braze HTML-Eingaben, um Cross-Site-Scripting-Angriffe (XSS) zu verhindern. Im Rahmen dieser Sicherheitsmaßnahme werden externe Ressourcen-URLs – einschließlich Schriftarten-URLs – entfernt, es sei denn, sie stammen von einer der folgenden zulässigen Domains:

- `assets.appboycdn.com`
- `braze-images.com`
- `cdn.braze.com`
- `cdn.braze.eu`
- `fonts.googleapis.com`
- `fonts.gstatic.com`

Wenn Sie angepasste Schriftarten auf Ihrer {{ include.page_type }}-Seite verwenden möchten, referenzieren Sie Schriftarten von einer dieser Domains oder verwenden Sie stattdessen [websichere Schriftarten](https://www.w3schools.com/cssref/css_websafe_fonts.php).

Best Practices zur Verwaltung von E-Mail-Listen finden Sie unter [E-Mail-Abos]({{site.baseurl}}/user_guide/channels/email/subscriptions).