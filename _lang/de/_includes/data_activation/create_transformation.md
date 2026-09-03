Gehen Sie im Braze-Dashboard zu **Dateneinstellungen** > **Datentransformation**.

Wählen Sie **Transformation erstellen**, um Ihre Transformation zu benennen, und wählen Sie dann Ihre Bearbeitungserfahrung.

![Details zur Transformation mit der Option „Template verwenden“ oder „Von Grund auf neu beginnen“ für Ihre Bearbeitungserfahrung.]({% image_buster /assets/img/data_transformation/data_transformation10.png %}){: style="max-width:80%;"}

Wählen Sie **Template verwenden**, um eine Template-Bibliothek zu durchsuchen, die auch Anwendungsfälle der Datentransformation enthält. Oder wählen Sie **Von Grund auf neu**, um ein Standard-Code-Template zu laden.

Wenn Sie bei Null anfangen, wählen Sie ein Ziel für Ihre Transformation. Sie können trotzdem ein Code-Template aus der Template-Bibliothek einfügen.

{% details Mehr zu Zielen %}
* **POST: Nutzer:innen tracken:** Wandelt Webhooks von einer Quellplattform in Kundenprofil-Updates um, z. B. Attribute, Ereignisse oder Käufe.
* **PUT: Mehrere Katalogartikel aktualisieren:** Wandelt Webhooks von einer Quellplattform in Aktualisierungen von Katalogartikeln um.
* **DELETE: Mehrere Katalogartikel löschen:** Wandelt Webhooks von einer Quellplattform in Löschungen von Katalogartikeln um.
* **PATCH: Mehrere Katalogartikel bearbeiten:** Wandelt Webhooks von einer Quellplattform in Bearbeitungen von Katalogartikeln um.
* **POST: Nachrichten sofort über API Only senden:** Wandelt Webhooks von einer Quellplattform um, um Sofortnachrichten an bestimmte Nutzer:innen zu senden.
{% enddetails %}

{% alert note %}
{% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="additional templates or destinations" %}
{% endalert %}

Nachdem Sie Ihre Transformation erstellt haben, sehen Sie die Detailansicht der Transformation. Hier können Sie unter **Webhook-Details** den zuletzt empfangenen Webhook für diese Transformation einsehen und unter **Transformationscode** Ihren Transformationscode schreiben.

{% if include.location == "typeform" %}

![Ein Beispiel für Webhook-Details und Transformationscode.]({% image_buster /assets/img/typeform/data_transformation_typeform.png %})

{% endif %}

Kopieren Sie Ihre **Webhook-URL** zur Verwendung im nächsten Schritt.