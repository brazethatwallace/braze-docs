{% assign track_endpoint = include.endpoint | default: "/users/track" %}
{% alert note %}
Cada atributo personalizado enviado en una solicitud a `{{ track_endpoint }}` consume un punto de datos. Para más información, consulta [Puntos de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points/).
{% endalert %}