Dans le tableau de bord de Braze, accédez à **Data Settings** > **Data Transformation**.

Sélectionnez **Create Transformation** pour nommer votre transformation, puis choisissez votre expérience de modification.

![Détails de la transformation avec la possibilité de choisir « Use a template » ou « Start from scratch » pour votre expérience de modification.]({% image_buster /assets/img/data_transformation/data_transformation10.png %}){: style="max-width:80%;"}

Sélectionnez **Use a template** pour parcourir une bibliothèque de modèles, y compris les cas d'usage de Data Transformation. Vous pouvez également sélectionner **Start from scratch** pour charger un modèle de code par défaut.

Si vous démarrez de zéro, choisissez une destination pour votre transformation. Vous pouvez toujours insérer un modèle de code à partir de la bibliothèque de modèles.

{% details Plus d'informations sur les destinations %}
* **POST : Track users :** Transforme les webhooks d'une plateforme source en mises à jour du profil utilisateur, telles que les attributs, les événements ou les achats.
* **PUT : Update multiple catalog items :** Transforme les webhooks d'une plateforme source en mises à jour d'éléments du catalogue.
* **DELETE : Delete multiple catalog items :** Transforme les webhooks d'une plateforme source en suppressions d'éléments du catalogue.
* **PATCH : Edit multiple catalog items :** Transforme les webhooks d'une plateforme source en modifications d'éléments du catalogue.
* **POST : Send messages immediately via API Only :** Transforme les webhooks d'une plateforme source pour envoyer des messages immédiats à des utilisateurs désignés.
{% enddetails %}

{% alert note %}
{% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="additional templates or destinations" %}
{% endalert %}

Après avoir créé votre transformation, vous verrez la vue détaillée de celle-ci. Vous pouvez consulter le dernier webhook reçu pour cette transformation sous **Webhook details**, ainsi qu'un espace pour écrire votre code de transformation sous **Transformation code**.

{% if include.location == "typeform" %}

![Un exemple de détails de webhook et de code de transformation.]({% image_buster /assets/img/typeform/data_transformation_typeform.png %})

{% endif %}

Copiez votre **Webhook URL** pour l'utiliser à l'étape suivante.