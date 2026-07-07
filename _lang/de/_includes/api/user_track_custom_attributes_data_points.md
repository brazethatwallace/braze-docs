{% assign track_endpoint = include.endpoint | default: "/users/track" %}
{% alert note %}
Jedes angepasste Attribut, das in einer Anfrage an `{{ track_endpoint }}` gesendet wird, verbraucht einen Datenpunkt. Weitere Informationen finden Sie unter [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points/).
{% endalert %}