---
nav_title: Importa tu lista de correo electrónico
article_title: Importa tu lista de correo electrónico a Braze
page_order: 4
page_type: reference
description: "Este artículo de referencia cubre las mejores prácticas para importar tu lista de correo electrónico a Braze."
channel: email

---

# Importa tu lista de correo electrónico a Braze {#importing-email-lists}

> Un paso importante para establecerte como un remitente de correo electrónico exitoso es asegurarte de que tienes una lista de correo electrónico de alta calidad. Una gestión adecuada de la lista de correo electrónico puede mejorar tu capacidad de entrega y proporcionarte resultados de campaña más precisos y limpios.

## Consideraciones antes de importar

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### Valida tus listas de correo electrónico

Antes de importar tu lista de correo electrónico a Braze, valida que tu lista incluya solo direcciones de correo electrónico auténticas. Una tasa de rebote alta puede dañar tu reputación como remitente de correo electrónico.

Los servicios de limpieza de listas de correo electrónico pueden hacer esto por ti determinando si la dirección de correo electrónico sigue la sintaxis correcta y tiene las propiedades físicas de una dirección de correo electrónico, verificando el dominio de correo electrónico y conectándose al servidor de correo electrónico para autenticar si la dirección de correo electrónico existe allí.

### Comprueba si una dirección de correo electrónico ya está asociada a un usuario

Antes de crear un usuario a través de la API o el SDK, llama al punto de conexión [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) y especifica la `email_address` del usuario. Si devuelve un perfil de usuario, ese usuario de Braze ya está asociado a esa dirección de correo electrónico.

Recomendamos encarecidamente que busques direcciones de correo electrónico únicas cuando se crean nuevos usuarios, y evites pasar o importar usuarios con la misma dirección de correo electrónico. De lo contrario, podrías tener consecuencias no deseadas que afecten al envío de mensajes, la segmentación, los informes y otras características.

Por ejemplo, supongamos que tienes perfiles duplicados, pero ciertos atributos personalizados o eventos residen en un solo perfil. Cuando intentas desencadenar Campaigns o Canvas con múltiples criterios, Braze no puede identificar al usuario como elegible porque hay dos perfiles de usuario. O, si una Campaign se dirige a una dirección de correo electrónico compartida por dos usuarios, la página **Buscar usuarios** mostrará ambos perfiles de usuario como si hubieran recibido la Campaign.

### Identifica a tus usuarios comprometidos

Para identificar a tus usuarios más comprometidos, primero elimina a los usuarios que llevan mucho tiempo inactivos. Es una buena práctica no enviar correos electrónicos a usuarios que no han interactuado con un correo electrónico en más de seis meses, ya que esto puede dañar tu reputación como remitente de correo electrónico. Al importar tu lista de correo electrónico, asegúrate de incluir solo a los usuarios que hayan abierto un correo electrónico tuyo en los últimos seis meses.

A largo plazo, también deberías considerar implementar una [política de desactivación]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/).

### Evita las listas de supresión

Si estás migrando desde un proveedor de correo electrónico existente, asegúrate de no importar usuarios de una lista de supresión. Las listas de supresión contienen direcciones de correo electrónico que han cancelado su suscripción, marcado tus correos electrónicos como correo no deseado o han tenido un rebote duro.

## Métodos para importar

Una vez que tengas tu lista de correo electrónico preparada, hay varias formas de importar usuarios a Braze, como a través de la REST API de Braze o archivos CSV. Lee más en nuestro artículo dedicado de [Importación de usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/).