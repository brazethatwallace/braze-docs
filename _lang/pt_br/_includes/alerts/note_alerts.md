{% if include.alert == 'Content Cards frequency capping' %}

{% alert note %}
A limitação de frequência não se aplica aos Content Cards.
{% endalert %}

{% endif %}

{% if include.alert == 'Custom Attributes time attribute' %}

{% alert note %}
Uma string de data como "12-1-2021" ou "12/1/2021" será convertida em um objeto datetime e tratada como um [atributo de tempo]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% endif %}

{% if include.alert == 'Manage custom data storage' %}

{% alert note %}
Todos os dados do perfil de usuário (eventos personalizados, atributos personalizados, dados personalizados) são armazenados enquanto esses perfis estiverem ativos.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment profiles first app use' %}

{% alert note %}
A Braze não gera perfis para os usuários até que eles tenham usado o app pela primeira vez, portanto, não é possível direcionar usuários que ainda não abriram o app.
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify attributes REST API' %}

{% alert note %}
Todos os atributos são originados da REST API da Braze.
{% endalert %}

{% endif %}

{% if include.alert == 'subscription group limit' %}

{% alert note %}
Você pode adicionar até 350 grupos de inscrições por espaço de trabalho.
{% endalert %}

{% endif %}

{% if include.alert == 'GIF platform support' %}

{% alert note %}
GIFs não são compatíveis com notificações por push no Android. Essa é uma limitação da plataforma Android, não da Braze.
<br><br>
- Para mensagens no app e Content Cards no Android, você pode oferecer suporte a GIFs integrando uma biblioteca de imagens de terceiros, como [Glide](https://bumptech.github.io/glide/) ou [Fresco](https://frescolib.org/).
<br>
- No iOS, as notificações por push são compatíveis com GIFs. Mensagens no app e Content Cards exigem um provedor de imagens GIF personalizado.
{% endalert %}

{% endif %}