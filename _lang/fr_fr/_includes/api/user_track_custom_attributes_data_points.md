{% assign track_endpoint = include.endpoint | default: "/users/track" %}
{% alert note %}
Chaque attribut personnalisé envoyé dans une requête à `{{ track_endpoint }}` consomme un point de donnée. Pour plus d'informations, consultez [Points de donnée]({{site.baseurl}}/user_guide/data/infrastructure/data_points/).
{% endalert %}