{% assign track_endpoint = include.endpoint | default: "/users/track" %}
{% alert note %}
`{{ track_endpoint }}` へのリクエストで送信される各カスタム属性は、1データポイントを消費します。詳細については、[データポイント]({{site.baseurl}}/user_guide/data/infrastructure/data_points/)を参照してください。
{% endalert %}