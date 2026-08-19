{% if include.alert == 'Content Cards frequency capping' %}

{% alert note %}
La limite de fréquence ne s'applique pas aux Content Cards.
{% endalert %}

{% endif %}

{% if include.alert == 'Custom Attributes time attribute' %}

{% alert note %}
Une chaîne de caractères de date telle que « 12-1-2021 » ou « 12/1/2021 » sera convertie en objet datetime et traitée comme un [attribut time]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#time).
{% endalert %}

{% endif %}

{% if include.alert == 'Manage custom data storage' %}

{% alert note %}
Toutes les données de profil utilisateur (événements personnalisés, attributs personnalisés, données personnalisées) sont conservées tant que ces profils sont actifs.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment profiles first app use' %}

{% alert note %}
Braze ne crée pas de profil pour un utilisateur tant qu'il n'a pas utilisé l'application une première fois. Vous ne pouvez donc pas cibler des utilisateurs qui n'ont pas encore ouvert votre application.
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify attributes REST API' %}

{% alert note %}
Tous les attributs proviennent de la REST API de Braze.
{% endalert %}

{% endif %}

{% if include.alert == 'subscription group limit' %}

{% alert note %}
Vous pouvez ajouter jusqu'à 450 groupes d'abonnement par espace de travail.
{% endalert %}

{% endif %}

{% if include.alert == 'GIF platform support' %}

{% alert note %}
Les GIF ne sont pas pris en charge dans les notifications push Android. Il s'agit d'une limitation de la plateforme Android, et non d'une limitation de Braze.
<br><br>
- Pour les messages in-app et les Content Cards sur Android, vous pouvez prendre en charge les GIF en intégrant une bibliothèque d'images tierce, telle que [Glide](https://bumptech.github.io/glide/) ou [Fresco](https://frescolib.org/).
<br>
- Sur iOS, les notifications push prennent en charge les GIF. Les messages in-app et les Content Cards nécessitent un fournisseur d'images GIF personnalisé.
{% endalert %}

{% endif %}