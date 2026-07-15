---
nav_title: Google
article_title: Sincronización de audiencias de Canvas con Google
alias: /google_audience_sync/
description: "En este artículo de referencia se explica cómo utilizar Braze Audience Sync con Google para ofrecer anuncios basados en desencadenantes de comportamiento, segmentación y más."
tool:
  - Canvas
page_order: 3

---

# Sincronización de audiencias con Google {#audience-sync-to-google}

{% alert important %}
Google está actualizando su [Política de consentimiento del usuario de la UE](https://www.google.com/about/company/user-consent-policy/) en respuesta a los cambios en la [Ley de Mercados Digitales (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), que está en vigor desde el 6 de marzo de 2024. Este nuevo cambio obliga a los anunciantes a revelar cierta información a sus usuarios finales del EEE, Reino Unido y Suiza, así como a obtener de ellos el consentimiento necesario. Consulta la siguiente documentación para obtener más información.
{% endalert %}

La integración de Braze Audience Sync con Google permite a las marcas ampliar el alcance de sus recorridos del cliente multicanal a Google Search, Google Shopping, Gmail, YouTube y Google Display. Utilizando tus datos propios de clientes, puedes entregar de forma segura anuncios basados en desencadenantes dinámicos de comportamiento, segmentación y más. Cualquier criterio que utilices normalmente para desencadenar un mensaje (por ejemplo, push, correo electrónico o SMS) como parte de un Canvas de Braze puede utilizarse para desencadenar un anuncio dirigido a ese usuario con [Customer Match](https://support.google.com/google-ads/answer/6379332?hl=en) de Google.

{% alert note %}
La integración de Braze Audience Sync con Google es compatible con Google Ads, no con Google Ads Manager.
{% endalert %}

Google Ads ya no genera audiencias similares, también conocidas como "audiencias parecidas", para la segmentación y los informes. Consulta la [documentación de Google Ads](https://support.google.com/google-ads/answer/12463119?) para obtener más información.

**Los ejemplos comunes para sincronizar audiencias personalizadas incluyen:**
- Dirigirse a usuarios de alto valor a través de múltiples canales para impulsar las compras o la participación.
- Reorientar a los usuarios menos receptivos a otros canales de marketing.
- Crear audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles de tu marca.

{% alert note %}
Esta función permite a las marcas controlar qué datos propios específicos se comparten con Google. En Braze, las integraciones con las que puedes y no puedes compartir tus datos propios se tienen muy en cuenta. Más información sobre nuestra [política de privacidad de datos de Braze](https://www.braze.com/privacy).
{% endalert %}

## Requisitos previos {#prerequisites}

Asegúrate de que los siguientes elementos están creados y completados antes de configurar tu paso de Google Audience en Canvas.

| Requisito | Origen | Descripción |
| ----------- | ------ | ----------- |
| Cuenta de Google Ads | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | Una cuenta de Google Ads activa para tu marca.<br><br>Si quieres compartir una audiencia en varias cuentas gestionadas, puedes cargar tus audiencias en tu [cuenta de administrador](https://support.google.com/google-ads/answer/6139186). |
| Condiciones y políticas de Google Ads | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | Debes aceptar y garantizar el cumplimiento de [las condiciones de publicidad de Google](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40) y de [las políticas de publicidad de Google](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC), que incluyen la [Política de consentimiento del usuario de la UE](https://www.google.com/about/company/user-consent-policy/), según te sean aplicables, en el uso que hagas de Braze Audience Sync.<br><br>Consulta con tu equipo jurídico la nueva Política de consentimiento del usuario de la UE de Google para asegurarte de que obtienes el consentimiento adecuado para utilizar los servicios de Google Ads para tus usuarios finales del EEE, Reino Unido y Suiza. |
| Google Customer Match | [Google](https://support.google.com/google-ads/answer/6299717) |  Customer Match no está disponible para todos los anunciantes.<br><br>**Para utilizar Customer Match, tu cuenta debe tener:**<br>• Un buen historial de cumplimiento de la política<br>• Un buen historial de pagos<br>• Al menos 90 días de historial en Google Ads<br>• Más de 50 000 USD de gasto total durante toda la vida. Para los anunciantes cuyas cuentas se gestionen en divisas distintas del dólar estadounidense, el importe de sus gastos se convertirá a dólares estadounidenses utilizando el tipo de cambio medio mensual de esa divisa.<br><br>Si tu cuenta no cumple estos criterios, actualmente no es elegible para utilizar Customer Match.<br><br>Ponte en contacto con tu representante de Google Ads para obtener más información sobre la disponibilidad de Customer Match para tu cuenta. |
| Señales de consentimiento de Google | [Google](https://support.google.com/google-ads/answer/14310715) |  Si deseas publicar anuncios para usuarios finales del EEE mediante el servicio Customer Match de Google, deberás pasar a Braze los siguientes atributos personalizados (booleanos) como parte de la Política de consentimiento del usuario de la UE de Google. Puedes encontrar más información en [Recopilación del consentimiento de los usuarios finales del EEE, Reino Unido y Suiza](#collecting-consent-for-eea-uk-and-switzerland-end-users): <br> - `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos previos" }

### Versiones de SDK necesarias {#required-sdk-versions}

Cuando utilices los SDK de Braze para recoger señales de consentimiento, asegúrate de que cumples las siguientes versiones mínimas:

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### Recopilación del consentimiento de los usuarios finales del EEE, Reino Unido y Suiza {#collecting-consent-for-eea-uk-and-switzerland-end-users}

La Política de consentimiento del usuario de la UE de Google exige a los anunciantes que revelen lo siguiente a sus usuarios finales del EEE, Reino Unido y Suiza, así como que obtengan su consentimiento para ello:

* El uso de cookies u otro tipo de almacenamiento local cuando sea legalmente necesario.
* La recogida, uso compartido y utilización de sus datos personales para la personalización de anuncios.

Esto no afecta a los usuarios finales estadounidenses ni a ningún otro usuario final situado fuera del EEE, el Reino Unido o Suiza. Consulta con tu equipo jurídico la nueva Política de consentimiento del usuario de la UE de Google para asegurarte de que obtienes el consentimiento adecuado para utilizar los servicios de Google Ads para tus usuarios finales del EEE, Reino Unido y Suiza.

Según los requisitos de la Ley de Mercados Digitales (DMA) en vigor a partir del 6 de marzo de 2024, los anunciantes deben pasar el consentimiento de los usuarios finales del EEE, Reino Unido y Suiza cuando compartan datos con Google. Como parte de este cambio, puedes recopilar ambas señales de consentimiento en Braze como los siguientes atributos personalizados booleanos:

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze sincronizará los datos de estos atributos personalizados con los [campos de consentimiento correspondientes en Google](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A).

#### Gestión del consentimiento revocado {#managing-revoked-consent}

Para mantener actualizadas tus listas de audiencia en caso de que un usuario final del EEE haya sido añadido a la lista de audiencia y posteriormente se haya retractado de cualquiera de los dos consentimientos (`$google_ad_user_data` o `$google_ad_personalization`), debes configurar un Canvas para eliminar usuarios de las listas de audiencia existentes mediante un paso de Audience Sync.

{% alert note %}
Si un usuario del EEE ha dado previamente su consentimiento para ambas señales, esos datos seguirán utilizándose para Google Customer Match hasta que la lista caduque, o hasta que se actualice explícitamente el estado del consentimiento a través de Google Audience Sync, o ambas cosas.
{% endalert %}

#### Consejos {#tips}

* Envía el valor como tipo booleano, no como tipo cadena.
* Antepón el signo de dólar ($) al nombre del atributo. Braze utiliza un signo de dólar al principio del nombre de un atributo para indicar que se trata de una clave especial y reservada.
* Introduce el nombre del atributo en minúsculas.
* Aunque no puedes establecer explícitamente un usuario como no especificado, si envías un valor `null` o `nil` o cualquier valor que no sea `true` o `false`, Braze pasará este usuario a Google como `UNSPECIFIED`.
* Los nuevos usuarios añadidos o actualizados sin especificar ninguno de los atributos de consentimiento se sincronizarán con Google con dichos atributos marcados como no especificados.

Si intentas sincronizar a un usuario del EEE sin los campos de consentimiento necesarios y el estado concedido, Google lo rechazará y no publicará anuncios para este usuario. Además, si se muestra un anuncio a un usuario del EEE sin su consentimiento explícito, puedes ser responsable y correr riesgos financieros. Para evitarlo, te sugerimos enviar campañas con filtros de segmento que solo incluyan a los usuarios del EEE, Reino Unido y Suiza con atributos de consentimiento de Google en `true`. Para obtener más información sobre la Política de consentimiento del usuario de la UE para los socios de carga de Customer Match, consulta las [preguntas frecuentes](https://support.google.com/google-ads/answer/14310715) de Google.

### Configuración de tu Canvas {#setting-up-your-canvas}

Después de sincronizarte con Braze, los siguientes atributos de consentimiento estarán disponibles en tus perfiles de usuario y para la segmentación:

- `$google_ad_user_data`
- `$google_ad_personalization`

En cualquier Canvas en el que te dirijas a usuarios finales del EEE, Reino Unido y Suiza utilizando Google Audience Sync para añadir usuarios a una audiencia, debes excluir a estos usuarios siempre que ambos atributos de consentimiento tengan cualquier valor que no sea `true`. Puedes hacerlo segmentando a estos usuarios cuando los valores de consentimiento estén configurados en `true`. Esto también garantiza la sincronización de los análisis más precisos de los usuarios, porque sabemos que Google rechazará a estos usuarios de las audiencias. Ten en cuenta que si utilizas Google Audience Sync para eliminar usuarios de una audiencia, los atributos de consentimiento no son necesarios.

## Integración {#integration}

### Paso 1: Conectar la cuenta de Google {#step-1-connect-google-account}

{% alert important %}
Debes tener el [permiso "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar Google Ads a tu cuenta de Braze.
{% endalert %}

Para empezar, ve a **Integraciones de socios** > **Socios tecnológicos** > **Google Ads** y selecciona **Connect Google Ads**. Se te pedirá mediante un modal que selecciones el correo electrónico asociado a tu cuenta de Google Ads y, a continuación, que concedas a Braze acceso a tu cuenta de Google Ads.

Tras conectar correctamente tu cuenta de Google Ads, volverás a la página del partner de Google Ads. A continuación, se te pedirá que selecciones a qué cuentas de anuncios quieres acceder en el espacio de trabajo de Braze.

![Un GIF que muestra el flujo de trabajo de una conexión exitosa de una cuenta de Google Ads a Braze.]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

#### Exportar IDFA de iOS o ID de publicidad de Google {#export-ios-idfa-or-google-advertising-ids}

Si piensas exportar IDFA de iOS o ID de publicidad de Google en tu sincronización de audiencias, Google requiere el ID de tu aplicación de iOS y el ID de tu aplicación de Android dentro de las solicitudes. En Google Audience Sync, selecciona **Add Mobile Advertising IDs**, introduce el ID de tu aplicación para iOS y el ID de tu aplicación para Android (nombre del paquete de la aplicación), y guarda cada uno de ellos.

<br><br>
![La página actualizada de la tecnología de Google Ads muestra las cuentas de anuncios conectadas, lo que te permite volver a sincronizar cuentas y añadir ID de publicidad para móviles.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
<br><br>

Si tienes varias aplicaciones en un mismo espacio de trabajo, puedes introducir cualquiera de los ID de tus aplicaciones en la configuración, porque los ID de los anuncios para móviles de tus usuarios serán los mismos en las distintas aplicaciones. Esto se debe a que tanto el GAID de Android como el IDFA de iOS son identificadores universales de anuncios en el dispositivo y no son específicos de una aplicación. Para sincronizar los ID de anuncios para móviles de los usuarios de una aplicación específica, puedes utilizar filtros de segmento ("Última aplicación específica utilizada" o "Versión más reciente de la aplicación") para dirigirte a estos usuarios.

### Paso 2: Añadir un paso de Google Audience en Canvas {#step-2-add-a-google-audience-step-in-canvas}

Añade un componente en tu Canvas y, a continuación, selecciona **Audience Sync**.

![El menú para seleccionar un componente Canvas en el editor.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![El paso Audience Sync añadido al recorrido del usuario.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Paso 3: Configuración de la sincronización {#step-3-sync-setup}

1. Selecciona **Custom Audience** para abrir el editor de componentes.
2. Selecciona **Google** como partner de Audience Sync.

![La configuración del paso Audience Sync con la opción de seleccionar un partner para iniciar la sincronización.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

{: start="3"}
3. Selecciona la cuenta de anuncios de Google deseada.
4. En el desplegable **Choose a New or Existing Audience**, introduce el nombre de una audiencia nueva o existente.

{% tabs %}
{% tab Crear una nueva audiencia %}

1. Introduce un nombre para la nueva audiencia personalizada.
2. Selecciona **Add Users to Audience**.
3. Selecciona los datos de campo de usuario propios que vas a enviar a tu audiencia. Puedes elegir cualquiera de los dos:

- **Customer Contact Info**: Contiene el correo electrónico o el número de teléfono de tus usuarios, o ambos, si existen en Braze. Google exige que sea un único campo para sincronizar en lugar de identificadores separados. Puedes seguir utilizando este campo único si solo tienes uno de los identificadores.
- **Mobile Advertiser ID**: Selecciona IDFA de iOS o GAID de Android. Debido a los requisitos de Google Customer Match, no puedes tener ambos ID de anunciante móvil en las mismas listas de clientes.

{% alert note %}
**Acerca del banner "Missing Mobile Ad IDs? Let's fix that.":** Cuando sincronizas con una audiencia utilizando IDFA de iOS o GAID de Android como campo a emparejar, puede aparecer este mensaje en el editor de pasos. Es **informativo, no un error**. Te recuerda que debes confirmar que el campo de ID de anuncio móvil con el que estás haciendo la coincidencia existe en tus datos de audiencia (por ejemplo, que los usuarios de la ruta de Canvas tienen recogido el identificador correspondiente). Puedes descartarlo después de verificar tus datos.
{% endalert %}

{: start="4"}
4. A continuación, guarda tu audiencia seleccionando el botón **Create Audience** en la parte inferior del editor de pasos.

![Vista ampliada del componente Canvas de audiencia personalizada. Aquí se selecciona la cuenta de anuncios deseada, se crea una nueva audiencia y se marca la casilla "customer contact info".]({% image_buster /assets/img/audience_sync/g_sync.png %})

Los usuarios recibirán una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si surgen errores durante este proceso. Los usuarios pueden hacer referencia a esta audiencia para la eliminación de usuarios más adelante en el recorrido de Canvas, ya que la audiencia se creó en modo borrador.

![Una alerta que aparece después de crear una nueva audiencia en el componente Canvas.]({% image_buster /assets/img/audience_sync/g_sync3.png %})

Cuando lances un Canvas con una nueva audiencia, Braze creará una nueva audiencia personalizada al lanzar el Canvas y, posteriormente, sincronizará a los usuarios casi en tiempo real cuando entren en el paso de Google Audience.

{% alert important %}
Dados los requisitos de Customer Match de Google, no puedes tener información de contacto de clientes e ID de anunciantes móviles en las mismas listas de clientes. Google Customer Match utilizará esta información para determinar quién es segmentable en Google Search, Google Display, YouTube y Gmail. Para más detalles sobre los requisitos de Google Customer Match, consulta su [documentación](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
{% endalert %}
{% endtab %}
{% tab Sincronizar con una audiencia existente %}

Braze también ofrece la posibilidad de añadir o eliminar usuarios de las listas de clientes de Google existentes para garantizar que estas audiencias estén actualizadas. Para sincronizar con una audiencia existente:

1. Selecciona una audiencia personalizada existente para sincronizarla.
2. Elige si quieres **Add to the audience** o **Remove from the audience**.
3. Braze añadirá o eliminará usuarios casi en tiempo real a medida que entren en el paso de Google Audience.
4. Después de configurar el paso de Google Audience, selecciona **Done**. Tu paso de Google Audience incluirá detalles sobre la nueva audiencia.

![Vista ampliada del componente Canvas de audiencia personalizada. Aquí se seleccionan la cuenta de anuncios deseada y la audiencia existente, así como el botón de opción "Add user to Audience".]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### Paso 4: Lanzar Canvas {#step-4-launch-canvas}

Completa el resto de tu recorrido de usuario en Canvas y ¡lánzalo! Si has optado por crear una nueva audiencia, Braze creará la audiencia dentro de Google y luego añadirá usuarios a medida que lleguen a este paso en tu Canvas. Si has seleccionado añadir o eliminar usuarios de una audiencia existente, Braze añadirá o eliminará usuarios cuando lleguen a este paso de su recorrido de usuario.

A continuación, los usuarios pasarán al siguiente componente del Canvas, si existe, o saldrán del Canvas si se trata del último paso del recorrido del usuario.

## Sincronización de usuarios y consideraciones sobre el límite de velocidad {#user-syncing-and-rate-limit-considerations}

A medida que los usuarios lleguen al componente de Audience Sync, Braze sincronizará a estos usuarios casi en tiempo real respetando los límites de velocidad de la API de Google Ads. Lo que esto significa en la práctica es que Braze intentará procesar por lotes el mayor número de usuarios cada 5 segundos antes de enviarlos a Google.

Cuando un cliente esté a punto de alcanzar el límite de velocidad de la API de Google Ads, Google proporcionará información a Braze sobre las recomendaciones de reintento. Si un cliente de Braze alcanza su límite de velocidad, Braze Canvas reintentará la sincronización durante un máximo de &#126;13 horas. Si la sincronización no es posible, estos usuarios aparecen en la lista de la métrica Users Errored.

## Comprender los análisis {#understanding-analytics}

La tabla siguiente incluye métricas y descripciones que te ayudarán a comprender mejor los análisis de tu paso de Audience Sync.

| Métrica | Descripción |
| ------ | ----------- |
| *Entered* | Número de usuarios que han entrado en este paso para sincronizarse con Google. |
| *Proceeded to Next Step* | Cuántos usuarios avanzaron al siguiente componente, si lo hay. Todos los usuarios avanzarán automáticamente. Si este es el último paso en la rama de Canvas, esta métrica será 0. |
| *Users Synced* | Número de usuarios que se han sincronizado correctamente con Google. |
| *User Not Synced* | Número de usuarios que no se han sincronizado debido a que faltan campos para coincidir o a que el atributo de consentimiento estaba configurado en `false`. |
| *Users Errored* | Número de usuarios que no se sincronizaron con Google debido a un error, tras &#126;13 horas de reintentos. En caso de errores específicos, como interrupciones del servicio de la API de Google Ads, Canvas reintentará la sincronización durante un máximo de &#126;13 horas. Si la sincronización sigue sin ser posible en ese momento, se rellenará el campo *User Not Synced*. |
| *Users Pending* | Número de usuarios que Braze está procesando actualmente para sincronizar con Google. |
| *Exited Canvas* | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso de un Canvas es un paso de Google. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprender los análisis" }

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Por qué no puedo seleccionar varios campos para que coincidan en mi configuración de pasos de Google Audience? {#why-can-i-not-select-multiple-fields-to-match-in-my-google-audience-step-configuration}

Google Customer Match tiene requisitos estrictos sobre cómo se formatean estas audiencias y qué información del cliente se incluye. En concreto, los ID de anunciante móvil deben cargarse por separado de la información de contacto del cliente (como el correo electrónico y el número de teléfono). Para obtener más información, consulta la [documentación de Google sobre Customer Match](https://support.google.com/google-ads/answer/7659867?hl=en#undefined).

### ¿Cuánto tardarán mis audiencias en sincronizarse en Google? {#how-long-will-it-take-for-my-audiences-to-sync-in-google}

Una audiencia puede tardar entre 6 y 12 horas en sincronizarse con Google.

### He sincronizado una audiencia, ¿por qué el tamaño de la audiencia en Google es cero? {#ive-synced-an-audience-so-why-is-the-audience-size-in-google-zero}

Por motivos de privacidad, el tamaño de la lista de usuarios mostrará cero hasta que la lista tenga al menos 1000 miembros. Después, el tamaño se redondeará a los dos dígitos más significativos.

### ¿Por qué el tamaño de mi audiencia coincidente en Google es menor que el número de usuarios sincronizados desde Braze? {#why-is-my-matched-audience-size-in-google-lower-than-the-number-of-users-synced-from-braze}

Aunque Braze puede sincronizar un número determinado de usuarios con Google, el tamaño real de la audiencia coincidente que ves en Google Ads puede ser significativamente menor. Esto se debe a que Google necesita hacer coincidir los datos de usuario que proporcionas (como direcciones de correo electrónico o números de teléfono) con cuentas de Google reales en su plataforma.

Aunque tus perfiles de usuario de Braze contengan campos de coincidencia válidos, los usuarios solo aparecen en tu audiencia personalizada de Google si tienen una cuenta de Google con información coincidente.

Para mejorar tu tasa de coincidencia:
- Confirma que estás [formateando tus datos correctamente](https://support.google.com/google-ads/answer/7659867).
- Proporciona múltiples identificadores cuando sea posible (por ejemplo, tanto correo electrónico como número de teléfono).
- Ten en cuenta que Google puede tardar entre 48 y 72 horas en procesar y hacer coincidir a los usuarios, aunque en algunos casos puede tardar varios días.

El tamaño final de la audiencia coincidente depende completamente del proceso de coincidencia de Google. Braze no tiene visibilidad sobre la coincidencia de Google una vez que los datos se han pasado a su plataforma.

### He sincronizado una audiencia en Google, pero mis anuncios no se publican. {#ive-synced-an-audience-into-google-but-my-ads-are-not-serving}

Comprueba que tus audiencias contienen al menos 5000 usuarios para que los anuncios puedan empezar a servirse.

### ¿Cómo resuelvo el error "Mobile App IDs Deleted"? {#how-do-i-resolve-the-mobile-app-ids-deleted-error}

Si estás sincronizando audiencias con Google, este error se desencadenará si has seleccionado sincronizar identificadores móviles como parte de tus sincronizaciones, pero has eliminado los ID de tus aplicaciones móviles de la página del partner de Google. Para resolver este problema, asegúrate de que has añadido los ID de aplicación móvil adecuados para iOS y Android a la página del partner de Google.

### ¿Por qué recibí un correo electrónico de credenciales no válidas de Google Ads cuando el panel todavía muestra que está conectado? {#why-did-i-get-a-google-ads-invalid-credentials-email-when-the-dashboard-still-shows-connected}

Braze envía este correo electrónico automáticamente cuando la API de Google devuelve un error de autorización. Esto puede ocurrir incluso cuando **Google Ads** todavía aparece conectado en el panel y las audiencias parecen estar sincronizándose; por ejemplo, cuando la cuenta de Google conectada no tiene permiso para una acción específica que Google solicitó, o cuando los términos de servicio de Google Ads aún necesitan ser aceptados para la cuenta.

Algunos errores de autorización se resuelven por sí solos. Comprueba los análisis de **Audience Sync** de tu Canvas (por ejemplo, *Users Synced* y *Users Errored*) para confirmar si los usuarios siguen sincronizándose. Si los problemas continúan, ve a **Integraciones de socios** > **Socios tecnológicos** > **Google Ads**, busca **Google Audience Sync** y usa **Change Account** para reconectar con una cuenta de Google Ads que tenga el acceso necesario y la configuración completada.