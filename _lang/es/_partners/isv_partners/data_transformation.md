---
nav_title: Transformación de datos
hidden: true
---

# Transformación de datos de Braze {#braze-data-transformation}

> [Transformación de datos]({{site.baseurl}}/data_transformation) de Braze puede recibir un webhook de una plataforma de un partner y permitir que un cliente defina un mapeado para convertir la carga útil de ese webhook en los datos de usuario deseados, como atributos, eventos o compras en perfiles de usuario de Braze.

## Cómo sería una integración basada en Transformación de datos {#what-a-data-transformation-based-integration-would-look-like}

Una integración de un partner basada en la característica de Transformación de datos podría ser una plantilla de código de transformación compartida con los clientes a través de documentación pública.

Para los clientes en común, se vería algo así:

1. Inician sesión en tu plataforma y configuran los webhooks.
2. Trabajan con su equipo de Braze para obtener acceso a Transformación de datos de Braze y crean una nueva transformación dentro de su panel de Braze.
3. Se copia la URL generada por la transformación.
4. De vuelta en Braze, envían un webhook de prueba a la URL de transformación copiada.
5. En Braze, copian y pegan la plantilla de código de transformación.
6. Habilitan la transformación.
7. Una vez habilitada, pueden verificar a través de la herramienta de búsqueda de usuarios de Braze que el perfil de usuario se haya actualizado en función del webhook y editar el código de transformación según lo deseen.

{% alert tip %}
Se recomienda crear una transformación por cada tipo de webhook enviado a Braze al desarrollar ejemplos de código de transformación.
{% endalert %}