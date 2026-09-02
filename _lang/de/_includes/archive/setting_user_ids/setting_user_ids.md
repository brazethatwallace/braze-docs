Für alle Nutzer:innen sollten Nutzer-IDs festgelegt werden. Diese sollten unveränderlich und zugänglich sein, wenn eine Nutzer:in die App öffnet. Die richtige Benennung Ihrer Nutzer-IDs von Anfang an ist einer der **wichtigsten** Schritte bei der Einrichtung von Nutzer-IDs. Wir empfehlen dringend die Verwendung des Braze-Standards für UUIDs und GUIDs (siehe folgender Abschnitt). Wir empfehlen Ihnen außerdem dringend, diesen Bezeichner anzugeben, da Sie damit Folgendes tun können:

- Ihre Nutzer:innen geräte- und plattformübergreifend tracken und so die Qualität Ihrer verhaltensbezogenen und demografischen Daten verbessern.
- Daten über Ihre Nutzer:innen mithilfe unserer [Nutzerdaten-API]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data) importieren.
- Bestimmte Nutzer:innen über unsere [Messaging-API]({{site.baseurl}}/api/endpoints/messaging) sowohl für allgemeine als auch für transaktionsbezogene Nachrichten ansprechen.

{% alert note %}
Wenn ein solcher Bezeichner nicht verfügbar ist, weist Braze Ihren Nutzer:innen einen eindeutigen Bezeichner zu, aber Ihnen fehlen dann die für Nutzer-IDs aufgeführten Möglichkeiten. Sie sollten es vermeiden, Nutzer-IDs für Nutzer:innen festzulegen, für die Sie keinen eindeutigen Bezeichner haben, der mit ihnen als Individuum verknüpft ist. Die Übergabe eines Gerätebezeichners bietet keinen Vorteil gegenüber dem automatischen anonymen Nutzer-Tracking, das Braze standardmäßig anbietet.
{% endalert %}

{% alert warning %}
Wenn Sie einen identifizierbaren Wert als Nutzer-ID verwenden möchten, **empfehlen wir Ihnen dringend**, zur zusätzlichen Sicherheit unser [SDK or Software-Development-Kit-Authentifizierungs-Feature]({{site.baseurl}}/developer_guide/authentication) hinzuzufügen, um einen Identitätswechsel zu verhindern.
{% endalert %}