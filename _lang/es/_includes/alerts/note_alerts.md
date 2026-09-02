{% if include.alert == 'Content Cards frequency capping' %}

{% alert note %}
La limitación de frecuencia no se aplica a Content Cards.
{% endalert %}

{% endif %}

{% if include.alert == 'Custom Attributes time attribute' %}

{% alert note %}
Una cadena de fecha como "12-1-2021" o "12/1/2021" se convertirá en un objeto datetime y se tratará como un [atributo de hora]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#time).
{% endalert %}

{% endif %}

{% if include.alert == 'Manage custom data storage' %}

{% alert note %}
Todos los datos de los perfiles de usuario (eventos personalizados, atributos personalizados, datos personalizados) se almacenan mientras esos perfiles estén activos.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment profiles first app use' %}

{% alert note %}
Braze no genera perfiles para los usuarios hasta que han utilizado la aplicación por primera vez, por lo que no puedes dirigirte a usuarios que aún no han abierto tu aplicación.
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify attributes REST API' %}

{% alert note %}
Todos los atributos provienen de la REST or transferencia de estado representacional API de Braze.
{% endalert %}

{% endif %}

{% if include.alert == 'subscription group limit' %}

{% alert note %}
Puedes añadir hasta 450 grupos de suscripción por espacio de trabajo.
{% endalert %}

{% endif %}

{% if include.alert == 'GIF platform support' %}

{% alert note %}
Los GIF no son compatibles con las notificaciones push de Android. Esta es una limitación de la plataforma Android, no una limitación de Braze.
<br><br>
- Para los mensajes dentro de la aplicación y Content Cards en Android, puedes admitir GIF integrando una biblioteca de imágenes de terceros, como [Glide](https://bumptech.github.io/glide/) o [Fresco](https://frescolib.org/).
<br>
- En iOS, las notificaciones push admiten GIF. Los mensajes dentro de la aplicación y Content Cards requieren un proveedor de imágenes GIF personalizado.
{% endalert %}

{% endif %}