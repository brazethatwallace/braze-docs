{% if include.alert == 'User profile external_id' %}

{% alert warning %}
No asignes un `external_id` a un perfil de usuario antes de poder identificarlo de forma única. Después de identificar a un usuario, no puedes revertirlo a anónimo.
<br><br>
Un `external_id` puede actualizarse utilizando el [endpoint `/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename). Sin embargo, cualquier intento de establecer un `external_id` diferente durante la sesión de un usuario creará un nuevo perfil de usuario con el nuevo `external_id` asociado. No se transmitirá ningún dato entre los dos perfiles.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment Currents multiple connectors' %}

{% alert warning %}
Si tienes intención de crear más de uno de los mismos conectores de Currents (por ejemplo, dos conectores de eventos de participación en mensajes), deben estar en espacios de trabajo diferentes. Dado que la integración de Braze Segment Currents no puede aislar los eventos de diferentes aplicaciones en un único espacio de trabajo, no hacerlo provocará una deduplicación de datos innecesaria y pérdida de datos.
{% endalert %}

{% endif %}

{% if include.alert == 'Canvas race condition audience trigger' %}

{% alert warning %}
Evita configurar una campaña basada en acciones o un Canvas con el mismo desencadenante que el filtro de audiencia (como un atributo modificado o la realización de un evento personalizado). Puede producirse una [condición de carrera]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions) en la que el usuario no se encuentre en la audiencia en el momento en que realice el evento desencadenante, lo que significa que no recibirá la campaña ni entrará en el Canvas.
{% endalert %}

{% endif %}