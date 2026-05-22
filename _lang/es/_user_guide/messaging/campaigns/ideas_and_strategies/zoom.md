---
nav_title: Automatizar el registro en Zoom
article_title: Automatizar el registro en Zoom
page_order: 1
page_type: tutorial
description: "Este artículo describe cómo automatizar el registro de asistentes en Zoom en tus campañas de correo electrónico, push y mensajes dentro de la aplicación."
channel: 
  - email
  - push
  - in-app messages

---

# Automatizar el registro en Zoom

> Los seminarios web se han convertido en algo habitual para los clientes de Braze en los últimos años. Al organizar un seminario web en Zoom, los usuarios deben introducir su información en una página de inicio de Zoom para registrarse. 

A continuación se describe un flujo de usuario recomendado:
1. Programa un seminario web en Zoom y genera un `webinarId`.
2. Usa Braze para promocionar seminarios web de Zoom a través de canales de correo electrónico, push y mensajes dentro de la aplicación. 
3. Incluye un botón de llamada a la acción en estas comunicaciones que añada automáticamente a los usuarios al seminario web.

Esto se puede lograr utilizando las [API de Zoom](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetingRegistrantCreate) para añadir automáticamente a un usuario a un seminario web mediante un clic en un botón dentro de un correo electrónico, push o mensaje dentro de la aplicación. Usa el siguiente punto de conexión, sustituyendo el ID del seminario web en la solicitud de API. 

POST: `/meetings/{webinarId}/registrants`

Para más información, consulta el [punto de conexión para añadir registrantes a un seminario web](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate) de Zoom.<br><br>

{% tabs %}
{% tab Email %}

Crea una campaña de correo electrónico con un botón de llamada a la acción en el cuerpo del mensaje. Cuando un usuario haga clic en el botón, redirige al usuario a la página de inicio del seminario web (con los parámetros apropiados incluidos en el enlace de redirección). 

Usando los parámetros de la URL para pasar datos de usuario, crea una llamada a la API que se ejecute cuando la página se cargue para añadir al usuario al seminario web.

![Mensaje de correo electrónico con plantillas Liquid utilizadas para incluir nombre, apellido, dirección de correo electrónico y ciudad.]({% image_buster /assets/img/zoom/zoom1.png %})

Los usuarios quedan registrados en el seminario web con los datos que ya existen en su perfil de Braze.

{% endtab %}
{% tab Push %}

1. Crea una campaña push<br><br>

	Configura el comportamiento al hacer clic en el botón para que enlace a la página de inicio del seminario web.<br>

	![Enlace al seminario web cuando se hace clic en un botón.]({% image_buster /assets/img/zoom/zoom2.png %})<br><br>

	Un ejemplo sencillo de una página de inicio para usuarios que se registran mediante un clic en el botón desde un push. Informa al usuario de en qué se ha registrado y confirma su registro:<br>

	![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>


2. Crea una campaña webhook desencadenada por el mensaje dentro de la aplicación o el clic en el botón.<br><br>
 	Usando los datos de usuario existentes en su perfil de Braze, registra al usuario en el seminario web.<br>

	![Una campaña basada en acciones que se enviará a los usuarios que hicieron clic en un botón de una campaña específica.]({% image_buster /assets/img/zoom/zoom6.png %})<br><br>

	Ejemplo de llamada webhook al punto de conexión de Zoom.<br>
	{% raw %}
	```http
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}

3. Los usuarios quedan registrados en el seminario web con los datos que ya existen en su perfil de Braze.

{% endtab %}
{% tab In-app message %}

1. Crea una campaña de mensaje dentro de la aplicación<br><br>

	Configura el comportamiento al hacer clic en el botón para que enlace a la página de inicio del seminario web.<br>

	![Enlace al seminario web cuando se hace clic en un botón.]({% image_buster /assets/img/zoom/zoom3.png %})<br><br>

	Un ejemplo sencillo de una página de inicio para usuarios que se registran mediante un clic en el botón desde un mensaje dentro de la aplicación. Informa al usuario de en qué se ha registrado y confirma su registro:<br>

	![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>

2. Crea una campaña webhook desencadenada por el mensaje dentro de la aplicación o el clic en el botón.<br><br>
	Usando los datos de usuario existentes en su perfil de Braze, registra al usuario en el seminario web.<br>

	![Una campaña basada en acciones que se enviará a los usuarios que hicieron clic en un botón de una campaña específica.]({% image_buster /assets/img/zoom/zoom5.png %})<br><br>

	Ejemplo de llamada webhook al punto de conexión de Zoom.<br>
	{% raw %}
	```http
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}
3. Los usuarios quedan registrados en el seminario web con los datos que ya existen en su perfil de Braze.

{% endtab %}
{% endtabs %}