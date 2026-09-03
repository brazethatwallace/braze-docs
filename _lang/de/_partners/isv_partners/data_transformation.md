---
nav_title: Datentransformation
hidden: true
---

# Braze Datentransformation {#braze-data-transformation}

> Braze [Datentransformation]({{site.baseurl}}/data_transformation) kann einen Webhook von einer Partnerplattform aufnehmen und es Kund:innen ermöglichen, eine Abbildung zu definieren, um die Nutzdaten dieses Webhooks in die gewünschten Nutzerdaten umzuwandeln, z. B. Attribute, Ereignisse oder Käufe in Braze-Nutzerprofilen.

## Wie eine Integration auf Basis der Datentransformation aussieht {#what-a-data-transformation-based-integration-would-look-like}

Eine Partnerintegration auf Basis des Datentransformation-Features könnte ein Transformationscode-Template sein, das über eine öffentliche Dokumentation mit Kund:innen geteilt wird.

Für gemeinsame Kund:innen würde es in etwa so aussehen:

1. Sie melden sich auf Ihrer Plattform an und richten Webhooks ein.
2. Sie arbeiten mit ihrem Braze-Team zusammen, um Zugriff auf Braze Datentransformation zu erhalten, und erstellen eine neue Transformation in ihrem Braze-Dashboard.
3. Die von der Transformation generierte URL wird kopiert.
4. Zurück in Braze senden sie einen Test-Webhook an die kopierte Transformations-URL.
5. In Braze kopieren sie das Transformationscode-Template und fügen es ein.
6. Sie aktivieren die Transformation.
7. Nach der Aktivierung können sie über die Braze-Nutzersuche überprüfen, ob das Nutzerprofil basierend auf dem Webhook aktualisiert wurde, und den Transformationscode nach Bedarf bearbeiten.

{% alert tip %}
Beim Erstellen von Transformationscode-Beispielen wird empfohlen, pro Webhook-Typ, der an Braze gesendet wird, eine eigene Transformation zu erstellen.
{% endalert %}