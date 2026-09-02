Los ID de usuario deben establecerse para cada uno de tus usuarios. Deben ser inmutables y accesibles cuando un usuario abra la aplicación. Nombrar correctamente tus ID de usuario desde el principio es uno de los pasos **más cruciales** a la hora de configurar los ID de usuario. Te recomendamos encarecidamente que utilices el estándar de Braze de UUID y GUID (detallado en la siguiente sección). También te recomendamos encarecidamente que proporciones este identificador, ya que te permitirá:

- Realizar el seguimiento de tus usuarios en distintos dispositivos y plataformas, mejorando la calidad de tus datos de comportamiento y demográficos.
- Importar datos sobre tus usuarios utilizando nuestra [API de datos de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).
- Dirigirte a usuarios específicos con nuestra [API de mensajería]({{site.baseurl}}/api/endpoints/messaging), tanto para mensajes generales como transaccionales.

{% alert note %}
Si no dispones de un identificador de este tipo, Braze asignará un identificador único a tus usuarios, pero carecerás de las capacidades indicadas para los ID de usuario. Debes evitar configurar ID de usuario para usuarios de los que no dispongas de un identificador único vinculado a ellos como individuos. Pasar un identificador de dispositivo no ofrece ninguna ventaja frente al seguimiento automático de usuarios anónimos que Braze ofrece de forma predeterminada.
{% endalert %}

{% alert warning %}
Si quieres incluir un valor identificable como tu ID de usuario, para mayor seguridad, **te recomendamos encarecidamente** que añadas nuestra característica de [autenticación del SDK or kit de desarrollo de software]({{site.baseurl}}/developer_guide/authentication) para evitar la suplantación de identidad de usuarios.
{% endalert %}