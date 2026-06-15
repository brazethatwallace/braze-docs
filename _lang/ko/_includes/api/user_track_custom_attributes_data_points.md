{% assign track_endpoint = include.endpoint | default: "/users/track" %}
{% alert note %}
`{{ track_endpoint }}`에 대한 요청에서 전송되는 각 커스텀 속성은 데이터 포인트를 소비합니다. 자세한 내용은 [데이터 포인트]({{site.baseurl}}/user_guide/data/infrastructure/data_points/)를 참조하세요.
{% endalert %}