---
nav_title: Solución de problemas
article_title: Solución de problemas de exportación
page_order: 6
page_type: reference
description: "Este artículo de referencia aborda situaciones habituales de solución de problemas para exportaciones tanto en flujos de trabajo CSV como API."
---

# Solución de problemas de exportación

> Esta página cubre situaciones comunes de solución de problemas para exportaciones tanto en flujos de trabajo CSV como API.

Utiliza las pestañas para seleccionar si deseas exportar al **contenedor de S3 predeterminado de Braze** o a un **socio de almacenamiento en la nube**.

{% sdktabs %}
{% sdktab Default export %}

Cuando no tienes un socio de almacenamiento marcado como destino de exportación predeterminado, Braze utiliza su propio contenedor de Amazon S3 para almacenar tus archivos de exportación. Los archivos en esta configuración son temporales y caducan a las cuatro horas.

## Exportaciones CSV
Cuando exportas un archivo CSV desde el dashboard, Braze envía por correo electrónico un enlace de descarga al usuario que ha iniciado sesión. Ese enlace apunta a un archivo ZIP alojado en el contenedor de S3 de Braze. Dentro del ZIP hay varios archivos más pequeños que, juntos, conforman tu exportación.

Debes haber iniciado sesión en el panel de Braze para utilizar el enlace, y el archivo solo estará disponible durante cuatro horas. Después de eso, el enlace deja de funcionar y los datos se eliminan. Si se producen fallos repetidos con exportaciones muy grandes (más de 500 000 usuarios), es posible que la exportación falle. En ese caso, intenta dividir tu exportación en grupos o campos más pequeños, o considera configurar un socio de almacenamiento.

### Errores comunes

- Si ves un error `AccessDenied`, es posible que el archivo ya haya caducado o que hayas intentado abrirlo antes de que estuviera listo. Los informes más grandes tardan más en generarse, así que espera unos minutos y vuelve a intentarlo.
- Un error `ExpiredToken` significa que el plazo de cuatro horas ha vencido. Vuelve a ejecutar la exportación para generar un nuevo enlace.
- El mensaje `Looks like the file doesn't exist anymore` suele aparecer cuando se envía el correo electrónico, pero el archivo no ha terminado de cargarse en S3. Por lo general, esperar unos minutos resuelve el problema.
- Los apóstrofos que se añaden al principio de ciertos campos (como `-`, `=`, `+` o `@`) son un comportamiento esperado. Por ejemplo, `-1943` se convierte en `'-1943` en el CSV. Braze hace esto para evitar que los programas de hojas de cálculo interpreten erróneamente los datos. Esto no se aplica a las exportaciones JSON, como las devueltas por el [punto de conexión `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/).

## Exportaciones API
Cuando exportas a través de las API de exportación sin almacenamiento en la nube, Braze escribe los archivos en su contenedor de S3. No recibirás ningún correo electrónico; en su lugar, la respuesta de la API incluye una URL de descarga temporal. La exportación se presenta como un archivo ZIP que contiene varios archivos JSON, cada uno con un usuario por línea.

Al igual que las exportaciones CSV, los enlaces de la API caducan a las cuatro horas. Si haces clic en el enlace demasiado pronto, es posible que aparezcan errores porque el archivo aún no está listo. Puedes proporcionar un `callback_endpoint` en tu solicitud si deseas que Braze te avise cuando el archivo esté disponible.

Las exportaciones API de gran tamaño también pueden agotar el tiempo de espera. Si eso ocurre, intenta realizar solicitudes más pequeñas o conecta un socio de almacenamiento para gestionar el volumen.

### Errores comunes
- `AccessDenied` o `ExpiredToken` normalmente significan que el enlace ha caducado o aún no estaba listo. Vuelve a ejecutar la exportación o espera un poco más.

{% endsdktab %}

{% sdktab Cloud storage connected %}

Cuando conectas un socio de almacenamiento (como Amazon S3, Google Cloud Storage o Azure Blob) y lo marcas como tu destino de exportación predeterminado desde la página **Socios tecnológicos** del dashboard, Braze escribe tus exportaciones directamente en tu contenedor. Esta configuración suele ser más fiable para exportaciones de mayor tamaño.

## Exportaciones CSV
Con las exportaciones CSV, Braze te envía un enlace de descarga por correo electrónico. Ese enlace caduca tras un breve periodo de tiempo (normalmente unas cuatro horas). Cuando tienes un socio de almacenamiento conectado y marcado como tu destino de exportación predeterminado, Braze también entrega una copia de la exportación a tu contenedor conectado. Esa copia reside en tu propia infraestructura, donde la caducidad y la retención siguen tus políticas de almacenamiento.

En el almacenamiento en la nube, las exportaciones CSV se agrupan en un archivo ZIP. Dentro del ZIP hay varios archivos CSV más pequeños. Las exportaciones grandes suelen dividirse en fragmentos (por ejemplo, unos 5000 usuarios cada uno), y el tamaño de los fragmentos puede variar. Los archivos más pequeños no indican que falten datos. Si el enlace enviado por correo electrónico falla, pero la copia en tu almacenamiento funciona, siempre puedes recuperar tus datos directamente desde tu contenedor.

### Errores comunes

- `AccessDenied` significa que Braze no pudo escribir en tu contenedor. Comprueba que tus credenciales y permisos siguen siendo válidos.
- `ExpiredToken` aparece si Braze ha perdido el acceso a tu contenedor. Actualiza tus credenciales en el panel de Braze.
- Si algunos archivos parecen más pequeños de lo esperado, es un comportamiento normal. El proceso de exportación divide los archivos intencionadamente para garantizar la estabilidad.
- Los apóstrofos que se añaden al principio de ciertos campos (como `-`, `=`, `+` o `@`) son un comportamiento esperado. Por ejemplo, `-1943` se convierte en `'-1943` en el CSV. Braze hace esto para evitar que los programas de hojas de cálculo interpreten erróneamente los datos. Esto no se aplica a las exportaciones JSON, como las devueltas por el [punto de conexión `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/).

## Exportaciones API
Cuando exportas datos a través de las API con un socio de almacenamiento conectado, los archivos exportados se escriben en tu contenedor. No se envía ningún correo electrónico. Los objetos subyacentes permanecen en tu almacenamiento y siguen tu configuración de retención, aunque las URL de descarga que devuelve Braze puedan seguir teniendo una duración limitada. Cada archivo ZIP contiene objetos JSON, uno por línea. Las exportaciones de gran tamaño pueden dividirse en varios archivos ZIP en lugar de un único ZIP, lo que generalmente hace que este método sea más fiable para exportaciones pesadas.

### Errores comunes

- `AccessDenied` ocurre cuando Braze no puede escribir en tu contenedor o los objetos se han eliminado posteriormente. Comprueba los permisos y confirma que ningún elemento externo esté borrando archivos.
- `ExpiredToken` significa que las credenciales de acceso de Braze a tu contenedor están desactualizadas. Actualízalas en el dashboard.
- Si faltan archivos o son más pequeños de lo esperado, primero confirma que nada fuera de Braze esté eliminando objetos. Los tamaños de archivo más pequeños son un comportamiento esperado.

{% endsdktab %}
{% endsdktabs %}