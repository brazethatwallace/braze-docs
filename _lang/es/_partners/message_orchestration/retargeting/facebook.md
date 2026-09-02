---
nav_title: Facebook
article_title: Exportación de audiencias de Facebook
alias: /partners/facebook/
description: "Este artículo de referencia describe la asociación entre Braze y Facebook, una plataforma social líder para que las marcas lleguen a sus clientes y se relacionen con ellos."
page_type: partner
search_tag: Partner
---

# Exportación de audiencias de Facebook {#facebook-audience-export}

> La integración de Braze y Facebook te permite exportar manualmente tus segmentos de Braze a Facebook para crear públicos personalizados de Facebook. Se trata de una exportación de audiencia única y estática, y solo crea nuevos públicos personalizados de Facebook.

Los casos de uso más comunes para exportar públicos personalizados de Facebook incluyen:
- Reorientar a los usuarios en puntos específicos de su ciclo de vida
- Crear listas de exclusión
- Crear [audiencias similares](https://www.facebook.com/business/help/164749007013531?id=401668390442328) para captar nuevos usuarios de forma más eficaz
<br><br>

{% alert note %}
La exportación de audiencia de Facebook utiliza el **token de acceso de usuario** para autorizar las solicitudes.<br><br>
Si utilizas esta función junto con la función [Audience Sync to Facebook]({{site.baseurl}}/audience_sync_facebook), Braze utilizará de forma predeterminada el **token de usuario del sistema** más fiable que ya has generado para autorizar las solicitudes.
{% endalert %}

{% alert note %}
Si estás participando en las pruebas de las cuentas de Meta Work en versión beta, asegúrate de desconectar y volver a conectar tu cuenta a la [página del partner de Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync#step-1-connect-to-facebook).
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| [Facebook Business Administrador](https://www.facebook.com/business/help/113163272211510?id=180505742745347) | Una herramienta centralizada para gestionar los activos de Facebook de tu marca (por ejemplo, cuentas publicitarias, páginas, aplicaciones). |
| [Cuenta publicitaria de Facebook](https://www.facebook.com/business/help/910137316041095?id=420299598837059) | Una cuenta publicitaria de Facebook activa vinculada al administrador comercial de tu marca que quieras usar con las audiencias personalizadas de Braze.<br><br>Asegúrate de que el administrador de tu Facebook Business Administrador te haya concedido permisos de administrador para las cuentas publicitarias de Facebook que planeas usar con Braze, y de que hayas aceptado los términos y condiciones de tu cuenta publicitaria. De lo contrario, no podrás acceder a ninguna cuenta publicitaria de Facebook dentro de Braze. |
| [Términos de audiencias personalizadas de Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php)| Debes aceptar los términos de audiencias personalizadas de Facebook para las cuentas publicitarias de Facebook que planeas usar con Braze.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conectarse a Facebook {#step-1-connect-to-facebook}

1. En el panel de Braze, ve a **Integraciones de partners** > **Partners tecnológicos** y selecciona **Facebook**.

{: start="2"}
2. En el módulo de exportación de Facebook Audience, selecciona **Connect Facebook**. <br><br>![Página de partners tecnológicos de Facebook en la plataforma Braze.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:70%;"}

{: start="3"}
3. En la ventana de diálogo de Facebook oAuth, autoriza a Braze a crear audiencias personalizadas en tus cuentas publicitarias de Facebook. <br><br>![El primer cuadro de diálogo de Facebook que solicita "Conectarse como X", donde X es tu nombre de usuario de Facebook.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![El segundo cuadro de diálogo de Facebook que solicita permiso para administrar anuncios de tus cuentas publicitarias.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

{: start="4"}
4. Después de vincular Braze a tu cuenta de Facebook, selecciona qué cuentas publicitarias deseas sincronizar dentro de tu espacio de trabajo de Braze. <br><br>![Una lista de cuentas publicitarias disponibles que puedes conectar a Facebook.]({% image_buster /assets/img/fb/afb_4.png %}){: style="max-width:70%;"}<br><br> Después de conectarte, vuelves a la página del partner, donde puedes ver qué cuentas están conectadas y desconectar cuentas existentes. <br><br> ![Una versión actualizada de la página de partners tecnológicos de Facebook que muestra las cuentas publicitarias conectadas con éxito.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:70%;"}<br>
<br> Tu conexión con Facebook se aplica a nivel del espacio de trabajo de Braze. Si tu administrador de Facebook te elimina de tu Facebook Business Administrador o del acceso a las cuentas de Facebook conectadas, Braze detecta un token no válido. Como resultado, tus Canvas activos que usan pasos de Facebook Audience mostrarán errores, y Braze no podrá sincronizar usuarios.

{% alert important %}
Para los clientes que previamente han pasado por el proceso de revisión de aplicaciones de Facebook para [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) y [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard), tu token de usuario del sistema sigue siendo válido para el paso de Facebook Audience. No puedes editar ni revocar el token de usuario del sistema de Facebook a través de la página del partner de Facebook. En su lugar, puedes conectar tu cuenta de Facebook para reemplazar tu token de usuario del sistema de Facebook dentro de tu espacio de trabajo de Braze.

<br><br>La nueva configuración de Facebook oAuth también se aplica a las [exportaciones de Facebook a través de Segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook#prerequisites).
{% endalert %}

### Paso 2: Exportar tus usuarios a Facebook {#step-2-export-your-users-into-facebook}

En Braze, la exportación de Facebook Audience es accesible desde la página de **Segments**.

1. En la página de **Segments**, selecciona el Segment que deseas exportar.
2. Selecciona **Datos de usuario** y luego selecciona **Exportar como Facebook Audience**. <br><br>![La sección "Detalles del Segment" de un Segment con "Datos de usuario" seleccionado para mostrar un menú desplegable de opciones que incluye "Exportar como Facebook Audience".]({% image_buster /assets/img/fb/afb_6.png %})

{: start="3"}
3. Si aún no has activado Facebook dentro de Braze, se te solicitará ir a la página de partners tecnológicos de Facebook en el panel. Si ya activaste Facebook a través de **Partners tecnológicos** > **Facebook**, puedes seleccionar tu cuenta publicitaria de Facebook y los campos de usuario a exportar. <br><br> Puedes exportar los siguientes campos:
- IDFA del dispositivo
- Número de teléfono
- Correo electrónico

{% alert note %}
Solo puedes seleccionar un campo de usuario dentro de una sola exportación. Si eliges más de un tipo de datos, Braze creará una audiencia personalizada separada para cada uno.
{% endalert %}

{: start="4"}
4. Después de seleccionar el campo de usuario, selecciona **Exportar Segment**. Al igual que con las exportaciones CSV, recibirás un correo electrónico cuando el Segment haya terminado de exportarse a Facebook.
5. Visualiza la audiencia personalizada en el [Facebook Ads Administrador](https://www.facebook.com/ads/manager/audiences/manage/).

{% alert important %}
Por razones de privacidad del usuario, Facebook no te permite ver:

- Los usuarios exactos que se añadieron con éxito a una audiencia personalizada. [Consulta los detalles de Facebook sobre por qué se ocultan los miembros individuales de la audiencia](https://www.facebook.com/business/help/112061095610075).
- El tamaño de la audiencia personalizada. [Consulta los detalles sobre los cambios en la estimación del tamaño de audiencia de Facebook](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923).
{% endalert %}

#### Configurar la exportación de tu audiencia {#configuring-your-audience-export}

Al crear audiencias de Facebook, es posible que desees incluir o excluir ciertos usuarios según sus preferencias y para cumplir con las leyes de privacidad, como el derecho a no vender o compartir información según la [CCPA](https://oag.ca.gov/privacy/ccpa). Los especialistas en marketing deben implementar los filtros relevantes para la elegibilidad de los usuarios dentro de los criterios de entrada de su Canvas. Las siguientes opciones pueden ayudar.

- Si has recopilado el [IDFA de iOS a través del SDK or kit de desarrollo de software de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection), puedes usar el filtro **Seguimiento de anuncios habilitado**. Selecciona el valor como `true` para enviar usuarios a los destinos de sincronización de audiencias solo donde hayan dado su consentimiento.

![Filtro de entrada de Canvas que muestra Seguimiento de anuncios habilitado configurado como verdadero.]({% image_buster /assets/img/tiktok/tiktok16.png %}){: style="max-width:75%;"}

- Si estás recopilando consentimientos de aceptación, rechazo, `Do Not Sell Or Share` u otros atributos personalizados relevantes, debes incluirlos dentro de los criterios de entrada de tu Canvas como un filtro:

![Un Canvas con un público de entrada de "opted_in_marketing" igual a "true".]({% image_buster /assets/img/tiktok/tiktok13.png %}){: style="max-width:75%;"}


#### Audiencias similares {#lookalike-audiences}

Una vez que hayas exportado con éxito un Segment como Facebook Audience, puedes crear grupos adicionales usando las [audiencias similares](https://www.facebook.com/business/help/164749007013531?id=401668390442328) de Facebook. Esta función analiza los datos demográficos, intereses y otros atributos de tu audiencia elegida, y crea una nueva audiencia de personas con atributos similares.

## Solución de problemas {#troubleshooting}

### Error Validating Access Token

Al utilizar Facebook Export, el error `Error Validating Access Token` aparece si:
- Cambiaste tu contraseña, lo que invalida tu sesión actual
- Facebook cerró tu sesión como medida de seguridad

Para resolver este error, sigue estos pasos:
1. Cierra sesión en Facebook y vuelve a iniciar sesión.
2. En Braze, elimina tus credenciales de Facebook y guarda. Confirma que las credenciales se eliminaron intentando exportar un Segment (el icono de exportación debería estar deshabilitado).
3. Vuelve a agregar y guardar tus credenciales de Facebook.
4. Intenta exportar de nuevo.

Si la exportación no funciona, haz lo siguiente:
1. Elimina tus credenciales de nuevo y guarda.
2. Vuelve a agregar tus credenciales y guarda.
3. Desconecta y vuelve a conectar la integración de Facebook en la página **Technology Partners**.

### Error al exportar un Facebook Audience {#error-when-exporting-a-facebook-audience}

Si recibes un error al exportar un Segment como Facebook Audience, la documentación para desarrolladores de Facebook señala las siguientes causas comunes:

1. **El token de acceso pertenece a un usuario que no es administrador de la aplicación y la cuenta publicitaria:** el usuario de Facebook cuyas credenciales están conectadas a Braze debe tener los permisos adecuados.
2. **La cuenta publicitaria a la que estás exportando no está asociada con tu aplicación:** la cuenta publicitaria de Facebook debe estar vinculada a tu aplicación en la configuración de Facebook.

Utiliza las siguientes verificaciones para comprobar tu configuración:

- **Comprueba que eres administrador de la aplicación:** Ve a [developers.Facebook.com](https://developers.facebook.com/), abre **My Apps** y selecciona la aplicación de tu empresa. Si no ves la aplicación, es posible que tu equipo de desarrollo necesite agregarte. En el panel de la aplicación, ve a **Roles** para confirmar tu rol (Admin, Developer, Tester o Analytics User).
- **Comprueba que tu cuenta publicitaria está asociada con tu aplicación:** En el panel de la aplicación de Facebook, ve a **Settings** > **Advanced**, desplázate hasta **Advertising Accounts** y agrega el ID de la cuenta publicitaria de Facebook que deseas usar para las exportaciones de audiencia de Braze si no aparece en la lista.
- **Comprueba que eres administrador de la cuenta publicitaria:** Ve a [business.Facebook.com](https://business.facebook.com/), abre **Business Settings** desde el menú principal, luego ve a **Accounts** > **Ad accounts** y selecciona la cuenta publicitaria. Confirma tu acceso y que tienes los permisos necesarios para crear Custom Audiences.

Para más detalles, consulta la [documentación de la API de Custom Audience de Facebook](https://developers.facebook.com/docs/) y la [guía del Centro de ayuda para empresas de Facebook sobre Custom Audiences](https://www.facebook.com/business/help).