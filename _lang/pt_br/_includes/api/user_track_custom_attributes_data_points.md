{% assign track_endpoint = include.endpoint | default: "/users/track" %}
{% alert note %}
Cada atributo personalizado enviado em uma solicitação para `{{ track_endpoint }}` consome um ponto de dados. Para saber mais, consulte [Pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points/).
{% endalert %}