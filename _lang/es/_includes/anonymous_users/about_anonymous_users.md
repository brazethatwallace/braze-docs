Después de [integrar el SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration), los usuarios que inicien tu aplicación por primera vez se considerarán "anónimos" hasta que llames al método `changeUser` y les asignes un `external_id`. Una vez asignado, no puedes volver a hacerlos anónimos. Sin embargo, si desinstalan y vuelven a instalar tu aplicación, volverán a ser anónimos hasta que se llame a `changeUser`.

Si un usuario previamente identificado inicia una sesión en un nuevo dispositivo, Braze fusiona campos específicos del perfil anónimo que aún no existan en el perfil identificado después de que llames a `changeUser` en ese dispositivo utilizando su `external_id`. No todos los datos se transfieren: solo se fusionan los campos que no están ya completados en el perfil identificado. Para consultar la lista completa de campos que se transfieren, consulta [comportamiento de fusión]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

{% if include.section == "user_guide" %}
{% alert tip %}
Para una guía completa, consulta [Configurar ID de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_ids).
{% endalert %}
{% endif %}