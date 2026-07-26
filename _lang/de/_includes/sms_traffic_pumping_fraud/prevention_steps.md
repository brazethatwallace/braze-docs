### Welche grundlegenden Sofortmaßnahmen sollte mein Unternehmen ergreifen, um diesen Betrug zu verhindern? {#what-immediate-foundational-steps-should-my-company-take-to-prevent-this-fraud}

Der wichtigste Schritt, den Ihr Unternehmen innerhalb Ihrer geschäftskunden-Engagement-Plattform unternehmen kann, ist die Minimierung Ihrer Angriffsfläche durch geografische Einschränkungen.

#### Die Braze-Allowlist für geografische Berechtigungen nutzen {#utilize-the-braze-geographic-permissions-allowlist}

Sie sollten proaktiv prüfen, in welchen Regionen sich Ihre tatsächlichen Zielkund:innen befinden, und eine Allowlist konfigurieren, die den Nachrichtenversand ausdrücklich nur in diese Länder erlaubt. Informationen zur Einrichtung finden Sie unter [Geografische Berechtigungen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions/).

##### Hochrisiko-Ziele blockieren {#block-high-risk-destinations}

Wenn Sie nur in Nordamerika oder Westeuropa geschäftlich tätig sind, gibt es keinen Grund, die Türen zu kostenintensiven internationalen Ländern in anderen Regionen offen zu lassen. Als Faustregel gilt: Deaktivieren Sie proaktiv jedes Land, in dem Sie nicht aktiv vermarkten oder Geschäftstätigkeiten haben, um unnötige Risiken zu eliminieren.

{% if include.detail %}
Prüfen Sie jede Anfrage zur Freischaltung von Routen zu als **Hohes Betrugsrisiko** gekennzeichneten Ländern sorgfältig.

##### Mehrschichtige Verteidigung {#layered-defense}

Geografische Einschränkungen sind ein entscheidender erster Schritt, aber nur eine Ebene in einer umfassenderen Defense-in-Depth-Strategie. Keine einzelne Maßnahme ist ausreichend – die Kombination mehrerer Maßnahmen macht Missbrauch deutlich komplexer und schwieriger in großem Umfang durchzuführen. Über die geografische Allowlist hinaus umfassen wichtige Kontrollen Schutzmaßnahmen wie:

- Clientseitige und serverseitige Validierung zur Sicherstellung der Datenintegrität
- Sinnvolles Rate-Limiting auf anfälligen Endpunkten, um automatisierte Übermittlungen zu verlangsamen
- CSRF-Token, um sicherzustellen, dass Anfragen von Ihren legitimen Formularen stammen
- CAPTCHA, um massenhafte betrügerische Einträge abzuwehren

{% alert note %}
Wir empfehlen, mit Ihrem internen Sicherheitsteam zusammenzuarbeiten, um diese Empfehlungen an Ihre spezifische Infrastruktur anzupassen.
{% endalert %}
{% endif %}