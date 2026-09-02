---
nav_title: Zustimmung verwalten
article_title: Zustimmung verwalten
page_order: 1
page_type: reference
description: "In diesem Referenzartikel finden Sie Tipps für die Verwaltung von Einwilligungen mit Braze."
---

# Zustimmung verwalten {#manage-consent}

> In diesem Referenzartikel finden Sie Tipps, wie Sie die Zustimmung Ihrer Nutzer:innen mit Braze verwalten können.

Braze kann keine spezifischen Ratschläge zur Auslegung von Gesetzen und Vorschriften oder zur Handhabung des Zustimmungsmanagements geben, da dies von der Auslegung des Gesetzes durch Ihr Rechtsteam abhängt. Wir bieten jedoch eine Reihe von Tools zur Unterstützung des Abo- und Einwilligungsmanagements.

Ihre Herangehensweise sollte von der Strenge abhängen, die Ihr juristisches Team aufgrund seiner Auslegung des Gesetzes verlangt. Hier sind einige Optionen, die Sie in Betracht ziehen können, aufgelistet von den strengsten bis zu den am wenigsten strengen:

- **Teams:** Verwenden Sie [Braze-Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) für echte Governance. Dazu müssen Sie allen Nutzerprofilen ein angepasstes Attribut hinzufügen, um den Status der Zustimmung, das Datum der Zustimmung oder beides anzugeben. Sie müssen dann alle Campaigns und Canvase in das vorgesehene Team migrieren und die Berechtigungen der Nutzer:innen auf dem Dashboard entsprechend anpassen.
- **Kundenprofil or Nutzerprofil-Attribut:** Fügen Sie ein Zustimmungsattribut zu allen Nutzerprofilen hinzu. Dieses Attribut zeigt an, ob eine Nutzerin oder ein Nutzer die Zustimmung erteilt hat oder nicht. In Zukunft können Sie dann ein Segment von Nutzer:innen, die zugestimmt haben (z. B. `consent = true`), in alle Ihre Campaigns und Canvase einbeziehen.
- **Kanalspezifische Abo-Gruppen:** Verwalten Sie Abo-Gruppen für bestimmte Kanäle (Push-Benachrichtigungen, E-Mail usw.), um die Zustimmung zu steuern. Markieren Sie Nutzer:innen zunächst als abgemeldet von diesen Kanälen und setzen Sie sie erst auf „Abonniert“, nachdem sie ihre Zustimmung erteilt haben.

{% alert important %}
Wenden Sie sich an Ihr Rechtsteam, um den geeigneten Ansatz für die Einhaltung der Anforderungen an das Zustimmungsmanagement in Ihrer Organisation zu bestimmen.
{% endalert %}