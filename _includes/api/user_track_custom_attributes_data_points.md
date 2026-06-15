{% assign track_endpoint = include.endpoint | default: "/users/track" %}
{% alert note %}
Each custom attribute sent in a request to `{{ track_endpoint }}` consumes a data point. For more information, see [Data points]({{site.baseurl}}/user_guide/data/infrastructure/data_points/).
{% endalert %}
