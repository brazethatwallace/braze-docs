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
Si estás participando en las pruebas de las cuentas de Meta Work en versión beta, asegúrate de desconectar y volver a conectar tu cuenta a la [página del partner de Facebook]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook).
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| [Facebook Business Manager](https://www.facebook.com/business/help/113163272211510?id=180505742745347) | Una herramienta centralizada para gestionar los activos de Facebook de tu marca (por ejemplo, cuentas de anuncios, páginas, aplicaciones). |
| [Cuenta publicitaria de Facebook](https://www.facebook.com/business/help/910137316041095?id=420299598837059) | Una cuenta de anuncios de Facebook activa vinculada al administrador de empresas de tu marca que quieras utilizar con los públicos personalizados de Braze.<br><br>Asegúrate de que el administrador de tu empresa en Facebook te ha concedido permisos de administrador para las cuentas de anuncios de Facebook que piensas utilizar con Braze, y de que has aceptado los términos y condiciones de tu cuenta de anuncios. De lo contrario, no podrás acceder a ninguna cuenta de anuncios de Facebook dentro de Braze. |
| [Términos de los públicos personalizados de Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php)| Debes aceptar los términos de públicos personalizados de Facebook para las cuentas de anuncios de Facebook que pienses utilizar con Braze.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conéctate a Facebook {#step-1-connect-to-facebook}

1. En el panel de Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Facebook**.

{: start="2"}
2. En el módulo de exportación de audiencia de Facebook, selecciona **Connect Facebook**. <br><br>![Página de socios tecnológicos de Facebook en la plataforma Braze.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:70%;"}

{: start="3"}
3. En la ventana de diálogo oAuth de Facebook, autoriza a Braze a crear públicos personalizados en tus cuentas de anuncios de Facebook. <br><br>![El primer cuadro de diálogo de Facebook te pide conectarte como X, donde X es tu nombre de usuario de Facebook.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![El segundo cuadro de diálogo de Facebook que solicita permiso para gestionar los anuncios de tus cuentas publicitarias.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

{: start="4"}
4. Una vez que Braze esté vinculado a tu cuenta de Facebook, selecciona las cuentas de anuncios que deseas sincronizar en tu espacio de trabajo de Braze. <br><br>![Una lista de las cuentas de anuncios disponibles que puedes conectar a Facebook.]({% image_buster /assets/img/fb/afb_4.png %}){: style="max-width:70%;"}<br><br> Después de conectarte, volverás a la página del partner, donde podrás ver qué cuentas están conectadas y desconectar las existentes. <br><br> ![Una versión actualizada de la página de socios tecnológicos de Facebook que muestra las cuentas de anuncios conectadas correctamente.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:70%;"}<br>
<br> Tu conexión a Facebook se aplica a nivel del espacio de trabajo de Braze. Si tu administrador de Facebook te elimina de tu Facebook Business Manager o del acceso a las cuentas de Facebook conectadas, Braze detectará un token no válido. Como resultado, tus Canvas activos que utilicen pasos de audiencia de Facebook mostrarán errores y Braze no podrá sincronizar usuarios.

{% alert important %}
Para los clientes que hayan pasado previamente por el proceso de revisión de la aplicación de Facebook para [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) y [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard), su token de usuario del sistema seguirá siendo válido para el paso de audiencia de Facebook. No podrás editar ni revocar el token de usuario del sistema de Facebook a través de la página del partner de Facebook. En su lugar, puedes conectar tu cuenta de Facebook para sustituir tu token de usuario del sistema de Facebook dentro de tu espacio de trabajo de Braze.

<br><br>La nueva configuración de Facebook oAuth también se aplica a las [exportaciones de Facebook a través de segmentos]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook#prerequisites).
{% endalert %}

### Paso 2: Exporta tus usuarios a Facebook {#step-2-export-your-users-into-facebook}

En Braze, se puede acceder a la exportación de audiencia de Facebook a través de la página **Segments**.

1. En la página **Segments**, selecciona el segmento que deseas exportar.
2. Selecciona **User Data** y, a continuación, **Export as Facebook Audience**. <br><br>![La sección "Detalles del segmento" de un segmento con "User Data" seleccionado para mostrar un desplegable de opciones que incluye "Export as Facebook Audience".]({% image_buster /assets/img/fb/afb_6.png %})

{: start="3"}
3. Si aún no has activado Facebook en Braze, se te pedirá que vayas a la página de socios tecnológicos de Facebook en el panel. Si ya has activado Facebook a través de **Socios tecnológicos** > **Facebook**, podrás seleccionar tu cuenta de anuncios de Facebook y los campos de usuario para exportar. <br><br> Puedes exportar los siguientes campos:
- IDFA del dispositivo
- Número de teléfono
- Correo electrónico

{% alert note %}
Solo puedes seleccionar un campo de usuario en una única exportación. Si eliges más de un tipo de datos, Braze creará un público personalizado distinto para cada uno.
{% endalert %}

{: start="4"}
4. Después de seleccionar el campo del usuario, selecciona **Export Segment**. Al igual que las exportaciones CSV, recibirás un correo electrónico cuando el segmento haya terminado de exportarse a Facebook.
5. Consulta la audiencia personalizada en el [administrador de anuncios de Facebook](https://www.facebook.com/ads/manager/audiences/manage/).

{% alert important %}
Por motivos de privacidad de los usuarios, Facebook no te permite ver:

- Los usuarios exactos que se han añadido correctamente a un público personalizado. [Consulta los detalles de Facebook sobre por qué los miembros individuales de la audiencia están ocultos](https://www.facebook.com/business/help/112061095610075).
- El tamaño del público personalizado. [Consulta los detalles sobre los cambios en la estimación del tamaño de la audiencia de Facebook](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923).
{% endalert %}

#### Configuración de la exportación de audiencia {#configuring-your-audience-export}

Al crear audiencias de Facebook, es posible que desees incluir o excluir a determinados usuarios en función de sus preferencias y para cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" en virtud de la [CCPA](https://oag.ca.gov/privacy/ccpa). Los especialistas en marketing deben implementar los filtros pertinentes para la elegibilidad de los usuarios dentro de sus criterios de entrada en Canvas. A continuación enumeramos algunas opciones.

- Si has recopilado el [IDFA de iOS a través del SDK de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection), podrás utilizar el filtro **Ads Tracking Enabled**. Selecciona el valor como `true` para enviar solo a los usuarios a los destinos de Audience Sync en los que hayan dado su consentimiento.

![Filtro de entrada de Canvas que muestra Ads Tracking Enabled configurado como true.]({% image_buster /assets/img/tiktok/tiktok16.png %}){: style="max-width:75%;"}

- Si estás recopilando opt ins, opt outs, `Do Not Sell Or Share` u otros atributos personalizados relevantes, debes incluirlos dentro de tus criterios de entrada de Canvas como un filtro:

![Un Canvas con una audiencia de entrada de "opted_in_marketing" es igual a "true".]({% image_buster /assets/img/tiktok/tiktok13.png %}){: style="max-width:75%;"}


#### Audiencias similares {#lookalike-audiences}

Una vez que hayas exportado correctamente un segmento como audiencia de Facebook, puedes crear grupos adicionales utilizando [audiencias similares](https://www.facebook.com/business/help/164749007013531?id=401668390442328) de Facebook. Esta función examina los datos demográficos, los intereses y otros atributos de la audiencia elegida y crea una nueva audiencia de personas con atributos similares.

## Solución de problemas {#troubleshooting}

### Error al validar el token de acceso {#error-validating-access-token}

Al utilizar la exportación de Facebook, el error `Error Validating Access Token` aparece si:
- Has cambiado tu contraseña, lo que invalida tu sesión actual
- Facebook cerró tu sesión como medida de seguridad

Para resolver este error, sigue estos pasos:
1. Cierra sesión en Facebook y vuelve a iniciar sesión.
2. En Braze, elimina tus credenciales de Facebook y guarda. Confirma que se han eliminado las credenciales intentando exportar un segmento (el icono de exportación debe estar desactivado).
3. Vuelve a añadir y guardar tus credenciales de Facebook.
4. Intenta exportar de nuevo.

Si la exportación no funciona, haz lo siguiente:
1. Vuelve a eliminar tus credenciales y guarda.
2. Vuelve a añadir tus credenciales y guarda.
3. Desconecta y vuelve a conectar la integración de Facebook en la página de **Socios tecnológicos**.

### Error al exportar una audiencia de Facebook {#error-when-exporting-a-facebook-audience}

Si recibes un error al exportar un segmento como audiencia de Facebook, la documentación para desarrolladores de Facebook señala las siguientes causas comunes:

1. **El token de acceso pertenece a un usuario que no es administrador de la aplicación ni de la cuenta de anuncios:** el usuario de Facebook cuyas credenciales están conectadas a Braze debe tener los permisos adecuados.
2. **La cuenta de anuncios a la que estás exportando no está asociada a tu aplicación:** la cuenta de anuncios de Facebook debe estar vinculada a tu aplicación en la configuración de Facebook.

Utiliza las siguientes comprobaciones para verificar tu configuración:

- **Comprueba que eres administrador de la aplicación:** ve a [developers.facebook.com](https://developers.facebook.com/), abre **My Apps** y selecciona la aplicación de tu empresa. Si no ves la aplicación, es posible que tu equipo de desarrollo necesite añadirte. En el panel de la aplicación, ve a **Roles** para confirmar tu rol (Admin, Developer, Tester o Analytics User).
- **Comprueba que tu cuenta de anuncios está asociada a tu aplicación:** en el panel de la aplicación de Facebook, ve a **Settings** > **Advanced**, desplázate hasta **Advertising Accounts** y añade el ID de la cuenta de anuncios de Facebook que deseas utilizar para las exportaciones de audiencia de Braze si aún no aparece en la lista.
- **Comprueba que eres administrador de la cuenta de anuncios:** ve a [business.facebook.com](https://business.facebook.com/), abre **Business Settings** en el menú principal y, a continuación, ve a **Accounts** > **Ad accounts** y selecciona la cuenta de anuncios. Confirma tu acceso y que tienes los permisos necesarios para crear públicos personalizados.

Para más detalles, consulta la [documentación de la API de públicos personalizados de Facebook](https://developers.facebook.com/docs/) y la [guía del Centro de ayuda para empresas de Facebook sobre públicos personalizados](https://www.facebook.com/business/help).