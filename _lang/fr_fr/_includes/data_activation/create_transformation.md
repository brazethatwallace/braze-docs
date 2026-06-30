Dans le tableau de bord de Braze, accédez à **Paramètres des données** > **Transformation des données**.

Sélectionnez **Créer une transformation** pour nommer votre transformation, puis choisissez votre expérience de modification.

![Détails de la transformation avec la possibilité de choisir « Utiliser un modèle » ou « Partir de zéro » pour votre expérience de modification.]({% image_buster /assets/img/data_transformation/data_transformation10.png %}){: style="max-width:80%;"}

Sélectionnez **Utiliser un modèle** pour parcourir une bibliothèque de modèles, y compris les cas d'utilisation de la Transformation des données. Vous pouvez également sélectionner **Partir de zéro** pour charger un modèle de code par défaut.

Si vous démarrez de zéro, choisissez une destination pour votre transformation. Vous pouvez toujours insérer un modèle de code à partir de la bibliothèque de modèles.

{% details Plus d'informations sur les destinations %}
* **POST : Suivre les utilisateurs :** Transforme les webhooks d'une plateforme source en mises à jour du profil utilisateur, telles que les attributs, les événements ou les achats.
* **PUT : Mettre à jour plusieurs éléments du catalogue :** Transforme les webhooks d'une plateforme source en mises à jour d'éléments du catalogue.
* **DELETE : Supprimer plusieurs éléments du catalogue :** Transforme les webhooks d'une plateforme source en suppressions d'éléments du catalogue.
* **PATCH : Modifier plusieurs éléments du catalogue :** Transforme les webhooks d'une plateforme source en modifications d'éléments du catalogue.
* **POST : Envoyer des messages immédiatement via l'API uniquement :** Transforme les webhooks d'une plateforme source pour envoyer des messages immédiats à des utilisateurs désignés.
{% enddetails %}

{% alert note %}
Vous souhaitez demander des modèles ou des destinations supplémentaires ? N'hésitez pas à laisser un [avis sur le produit]({{site.baseurl}}/user_guide/administrative/access_braze/portal).
{% endalert %}

Après avoir créé votre transformation, vous verrez la vue détaillée de celle-ci. Vous pouvez consulter le dernier webhook reçu pour cette transformation sous **Détails du webhook**, ainsi qu'un espace pour écrire votre code de transformation sous **Code de transformation**.

{% if include.location == "typeform" %}

![Un exemple de détails de webhook et de code de transformation.]({% image_buster /assets/img/typeform/data_transformation_typeform.png %})

{% endif %}

Copiez l'**URL de votre webhook** pour l'utiliser à l'étape suivante.