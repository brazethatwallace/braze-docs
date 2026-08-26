Braze añade los siguientes encabezados a las solicitudes salientes de contenido conectado. La mayoría se establecen solo cuando no los has proporcionado previamente en la etiqueta. Los encabezados que proporcionas con `:headers`, credenciales u opciones de etiqueta se envían tal cual.

| Encabezado | Cuándo lo establece Braze |
| --- | --- |
| `User-Agent` | Si no lo has establecido previamente, Braze envía `Braze Sender <version>`. La cadena de versión puede cambiar. Si filtras el tráfico por `User-Agent`, permite todos los valores que comiencen con `Braze Sender`. Para enviar un valor consistente, establece `User-Agent` en `:headers`. |
| `X-Braze-Sender-Version` | Siempre se establece con la versión del remitente de contenido conectado. |
| `Accept-Encoding` | Si no lo has establecido previamente, Braze envía `gzip`. |
| `Authorization` | Si la URL incluye un nombre de usuario y una contraseña (`user:pass@host`), Braze añade un encabezado `Authorization` de tipo Basic derivado de esas credenciales. Un encabezado `Authorization` explícito lo sobrescribe. Prefiere [`:basic_auth`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#using-basic-authentication) o `:headers` en lugar de incluir credenciales en la URL. |
| `Host` | Nombre de host de la URL de la solicitud (por ejemplo, `www.example.com` para `https://www.example.com/abc/123`), a menos que establezcas un encabezado `Host`. |
| `Content-Length` | Tamaño del cuerpo de la solicitud en bytes cuando hay un cuerpo presente. |
| `BrazeToBraze` | Se establece como `true` solo para solicitudes a endpoints REST de Braze. Se omite para otros destinos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Encabezados de solicitud saliente que Braze añade al contenido conectado" }