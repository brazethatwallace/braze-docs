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
{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

{% alert note %}
Esta función permite a las marcas controlar qué datos propios específicos se comparten con Google. En Braze, las integraciones con las que puedes y no puedes compartir tus datos propios se tienen muy en cuenta. Más información sobre nuestra [política de privacidad de datos de Braze](https://www.braze.com/privacy).
{% endalert %}

## Requisitos previos {#prerequisites}

Asegúrate de que los siguientes elementos estén creados y completados antes de configurar tu paso de Google Audience en Canvas.

| Requisito | Origin | Descripción |
| ----------- | ------ | ----------- |
| Cuenta de Google Ads | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | Una cuenta activa de Google Ads para tu marca.<br><br>Si deseas compartir una audiencia entre varias cuentas administradas, puedes cargar tus audiencias en tu [cuenta de administrador](https://support.google.com/google-ads/answer/6139186). |
| Términos de Google Ads y Políticas de Google Ads | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | Debes aceptar y asegurarte de cumplir con los [Términos de anuncios de Google](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40) y las [Políticas de anuncios de Google](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC), que incluyen la [Política de consentimiento del usuario de la UE](https://www.google.com/about/company/user-consent-policy/), según corresponda, en tu uso de Braze Audience Sync.<br><br>Consulta con tu equipo legal sobre la nueva Política de consentimiento del usuario de la UE de Google para asegurarte de que estás recopilando el consentimiento adecuado para utilizar los servicios de Google Ads para tus usuarios finales del EEE, Reino Unido y Suiza. |
| Google Customer Match | [Google](https://support.google.com/google-ads/answer/6299717) | Customer Match no está disponible para todos los anunciantes.<br><br>**Para usar Customer Match, tu cuenta debe tener:**<br>• Un buen historial de cumplimiento de políticas<br>• Un buen historial de pagos<br>• Al menos 90 días de historial en Google Ads<br>• Más de 50 000 USD de gasto total acumulado. Para los anunciantes cuyas cuentas se administran en monedas distintas al USD, el monto de gasto se convertirá a USD utilizando la tasa de conversión mensual promedio para esa moneda.<br><br>Si tu cuenta no cumple con estos criterios, actualmente no es elegible para usar Customer Match.<br><br>Comunícate con tu representante de Google Ads para obtener más orientación sobre la disponibilidad de Customer Match para tu cuenta. |
| Señales de consentimiento de Google | [Google](https://support.google.com/google-ads/answer/14310715) | Si deseas mostrar anuncios a usuarios finales del EEE utilizando el servicio Customer Match de Google, deberás pasar a Braze los siguientes atributos personalizados (booleanos) como parte de la Política de consentimiento del usuario de la UE de Google. Puedes encontrar más detalles en [Recopilación de consentimiento para usuarios finales del EEE, Reino Unido y Suiza](#collecting-consent-for-eea-uk-and-switzerland-end-users): <br> - `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos previos" }

### Versiones mínimas del SDK requeridas {#required-sdk-versions}

Al usar los SDK de Braze para recopilar señales de consentimiento, asegúrate de cumplir con las siguientes versiones mínimas:

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### Recopilación de consentimiento para usuarios finales del EEE, Reino Unido y Suiza {#collecting-consent-for-eea-uk-and-switzerland-end-users}

La Política de consentimiento del usuario de la UE de Google requiere que los anunciantes divulguen lo siguiente a sus usuarios finales del EEE, Reino Unido y Suiza, así como que obtengan su consentimiento para lo siguiente:

* El uso de cookies u otro almacenamiento local cuando sea legalmente requerido; y
* La recopilación, el intercambio y el uso de sus datos personales para la personalización de anuncios.

Esto no afecta a los usuarios finales de EE. UU. ni a ningún otro usuario final ubicado fuera del EEE, el Reino Unido o Suiza. Consulta con tu equipo legal sobre la nueva Política de consentimiento del usuario de la UE de Google para asegurarte de que estás recopilando el consentimiento adecuado para utilizar los servicios de Google Ads para tus usuarios finales del EEE, Reino Unido y Suiza.

Según los requisitos de la Ley de Mercados Digitales (DMA) vigentes desde el 6 de marzo de 2024, los anunciantes deben pasar el consentimiento de los usuarios finales del EEE, Reino Unido y Suiza al compartir datos con Google. Como parte de este cambio, puedes recopilar ambas señales de consentimiento en Braze como los siguientes atributos personalizados booleanos:

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze sincronizará los datos de estos atributos personalizados con los [campos de consentimiento correspondientes en Google](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A).

#### Gestión del consentimiento revocado {#managing-revoked-consent}

Para mantener tus listas de audiencia actualizadas en caso de que un usuario final del EEE haya sido añadido a la lista de audiencia y posteriormente haya retirado cualquiera de los dos consentimientos (`$google_ad_user_data` o `$google_ad_personalization`), debes configurar un Canvas para eliminar usuarios de las listas de audiencia existentes utilizando un paso de Audience Sync.

{% alert note %}
Si un usuario del EEE proporcionó previamente consentimiento para ambas señales, esos datos seguirán siendo utilizados para Customer Match de Google hasta que esa lista expire, o hasta que el estado de consentimiento se actualice explícitamente a través de Google Audience Sync, o ambos.
{% endalert %}

#### Consejos {#tips}

* Envía el valor como tipo booleano, no como tipo cadena.
* Usa el signo de dólar ($) como prefijo del nombre del atributo. Braze utiliza un signo de dólar al inicio del nombre de un atributo para indicar que se trata de una clave especial y reservada.
* Ingresa el nombre del atributo en minúsculas.
* Aunque no puedes establecer explícitamente a un usuario como no especificado, si envías un valor `null` o `nil` o cualquier valor que no sea `true` o `false`, Braze pasará este usuario a Google como `UNSPECIFIED`.
* Los nuevos usuarios añadidos o actualizados sin especificar ninguno de los atributos de consentimiento se sincronizarán con Google con esos atributos de consentimiento marcados como no especificados.

Si intentas sincronizar un usuario del EEE sin los campos de consentimiento necesarios y el estado otorgado, Google rechazará esto y no mostrará anuncios a este usuario. Además, si se muestra un anuncio a un usuario del EEE sin su consentimiento explícito, podrías ser responsable y estar en riesgo financiero. Para evitar esto, te sugerimos enviar Campaigns con filtros de Segment que solo incluyan usuarios del EEE, Reino Unido y Suiza con atributos de consentimiento de Google establecidos en `true`. Para más detalles sobre la Política de consentimiento del usuario de la UE para partners de carga de Customer Match, consulta las [preguntas frecuentes](https://support.google.com/google-ads/answer/14310715) de Google.

### Configuración de tu Canvas {#setting-up-your-canvas}

Después de sincronizar con Braze, los siguientes atributos de consentimiento estarán disponibles en tus perfiles de usuario y para segmentación:

- `$google_ad_user_data`
- `$google_ad_personalization`

En cualquier Canvas en el que estés segmentando usuarios finales del EEE, Reino Unido y Suiza utilizando Google Audience Sync para añadir usuarios a una audiencia, debes excluir a estos usuarios siempre que ambos atributos de consentimiento tengan cualquier valor que no sea `true`. Puedes hacerlo segmentando a estos usuarios cuando los valores de consentimiento estén establecidos en `true`. Esto también garantiza que los análisis más precisos de los usuarios se sincronicen, ya que sabemos que Google rechazará a estos usuarios de las audiencias. Ten en cuenta que si estás utilizando Google Audience Sync para eliminar usuarios de una audiencia, los atributos de consentimiento no son obligatorios.

## Integración {#integration}

### Paso 1: Conectar la cuenta de Google {#step-1-connect-google-account}

{% alert important %}
Debes tener el [permiso "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar Google Ads a tu cuenta de Braze.
{% endalert %}

Para empezar, ve a **Integraciones de partners** > **Partners tecnológicos** > **Google Ads** y selecciona **Conectar Google Ads**. Se te mostrará un modal para seleccionar el correo electrónico asociado a tu cuenta de Google Ads y luego conceder a Braze acceso a tu cuenta de Google Ads.

Después de conectar correctamente tu cuenta de Google Ads, volverás a la página del partner de Google Ads. A continuación, se te pedirá que selecciones a qué cuentas de anuncios deseas acceder en el espacio de trabajo de Braze.

![Un GIF que muestra el flujo de trabajo de una conexión exitosa de una cuenta de Google Ads a Braze.]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

#### Exportar IDFA de iOS o ID de publicidad de Google {#export-ios-idfa-or-google-advertising-ids}

Si planeas exportar IDFA de iOS o ID de publicidad de Google en tu sincronización de audiencia, Google requiere tu ID de aplicación de iOS y tu ID de aplicación de Android dentro de las solicitudes. En Google Audience Sync, selecciona **Añadir ID de publicidad móvil**, introduce tu ID de aplicación de iOS y tu ID de aplicación de Android (nombre del paquete de la aplicación), y guarda cada uno.

<br><br>
![La página de tecnología de Google Ads actualizada que muestra las cuentas de anuncios conectadas, permitiéndote volver a sincronizar cuentas y añadir ID de publicidad móvil.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
<br><br>

Si tienes varias aplicaciones en un solo espacio de trabajo, puedes introducir cualquiera de tus ID de aplicación en la configuración, ya que los ID de publicidad móvil de tus usuarios serán los mismos en varias aplicaciones. Esto se debe a que tanto el GAID de Android como el IDFA de iOS son identificadores de publicidad universales en el dispositivo y no son específicos de la aplicación. Para sincronizar los ID de publicidad móvil de usuarios de una aplicación específica, puedes usar filtros de Segment ("Última aplicación específica utilizada" o "Versión más reciente de la aplicación") para segmentar a estos usuarios.

### Paso 2: Añadir un paso de Google Audience en Canvas {#step-2-add-a-google-audience-step-in-canvas}

Añade un componente en tu Canvas y luego selecciona **Audience Sync**.

![El menú para seleccionar un componente de Canvas en el editor.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![El paso de Audience Sync añadido al recorrido del usuario.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Paso 3: Configuración de la sincronización {#step-3-sync-setup}

1. Selecciona **Custom Audience** para abrir el editor de componentes.
2. Selecciona **Google** como partner de Audience Sync.

![La configuración del paso de Audience Sync con la opción de seleccionar un partner para iniciar la sincronización.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

{: start="3"}
3. Selecciona la cuenta de anuncios de Google deseada.
4. En el desplegable **Elegir una audiencia nueva o existente**, introduce el nombre de una audiencia nueva o existente.

{% tabs %}
{% tab Crear una audiencia nueva %}

1. Introduce un nombre para la nueva audiencia personalizada.
2. Selecciona **Añadir usuarios a la audiencia**.
3. Selecciona los datos de campo de usuario de datos propios que deseas enviar a tu audiencia. Puedes elegir entre:

- **Información de contacto del cliente**: Contiene los correos electrónicos o números de teléfono de tus usuarios, o ambos, si existen en Braze. Google requiere que sea un solo campo para sincronizar en lugar de identificadores separados. Aún puedes usar este campo único si solo tienes uno de los identificadores.
- **ID de anunciante móvil**: Selecciona IDFA de iOS o GAID de Android. Debido a los requisitos de Customer Match de Google, no puedes tener ambos ID de anunciante móvil en las mismas listas de clientes.

{% alert note %}
**Acerca del banner "¿Faltan ID de publicidad móvil? Vamos a solucionarlo.":** Cuando sincronizas con una audiencia usando IDFA de iOS o GAID de Android como campo de coincidencia, este mensaje puede aparecer en el editor de pasos. Es **informativo, no un error**. Te recuerda que confirmes que el campo de ID de publicidad móvil con el que estás haciendo la coincidencia existe en los datos de tu audiencia (por ejemplo, que los usuarios en la ruta de Canvas tengan el identificador correspondiente recopilado). Puedes descartarlo después de haber verificado tus datos.
{% endalert %}

{: start="4"}
4. A continuación, guarda tu audiencia seleccionando el botón **Crear audiencia** en la parte inferior del editor de pasos.

![Vista expandida del componente de Canvas de audiencia personalizada. Aquí se selecciona la cuenta de anuncios deseada, se crea una nueva audiencia y se marca la casilla de verificación de información de contacto del cliente.]({% image_buster /assets/img/audience_sync/g_sync.png %})

Los usuarios recibirán una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si surgen errores durante este proceso. Los usuarios pueden hacer referencia a esta audiencia para la eliminación de usuarios más adelante en el recorrido de Canvas, ya que la audiencia se creó en modo borrador.

![Una alerta que aparece después de crear una nueva audiencia en el componente de Canvas.]({% image_buster /assets/img/audience_sync/g_sync3.png %})

Cuando lanzas un Canvas con una nueva audiencia, Braze creará una nueva audiencia personalizada al lanzar el Canvas y posteriormente sincronizará a los usuarios en tiempo casi real a medida que entren en el paso de Google Audience.

{% alert important %}
Dados los requisitos de Customer Match de Google, no puedes tener información de contacto del cliente e ID de anunciante móvil en las mismas listas de clientes. Google Customer Match utilizará esta información para determinar quién es segmentable dentro de Google Search, Google Display, YouTube y Gmail. Para más detalles sobre los requisitos de Google Customer Match, consulta su [documentación](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
{% endalert %}
{% endtab %}
{% tab Sincronizar con una audiencia existente %}

Braze también ofrece la posibilidad de añadir o eliminar usuarios de listas de clientes de Google existentes para garantizar que estas audiencias estén actualizadas. Para sincronizar con una audiencia existente:

1. Selecciona una audiencia personalizada existente para sincronizar.
2. Elige si deseas **Añadir a la audiencia** o **Eliminar de la audiencia**.
3. Braze añadirá o eliminará usuarios en tiempo casi real a medida que entren en el paso de Google Audience.
4. Después de configurar tu paso de Google Audience, selecciona **Done**. Tu paso de Google Audience incluirá detalles sobre la nueva audiencia.

![Vista expandida del componente de Canvas de audiencia personalizada. Aquí se seleccionan la cuenta de anuncios deseada y la audiencia existente, así como el botón de opción de añadir usuario a la audiencia.]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### Paso 4: Lanzar Canvas {#step-4-launch-canvas}

¡Completa el resto del recorrido del usuario dentro de Canvas y luego lánzalo! Si has optado por crear una nueva audiencia, Braze creará la audiencia dentro de Google y luego añadirá usuarios a medida que lleguen a este paso en tu Canvas. Si has seleccionado añadir o eliminar usuarios de una audiencia existente, Braze añadirá o eliminará usuarios cuando lleguen a este paso en su recorrido de usuario.

Los usuarios avanzarán al siguiente componente de Canvas si hay uno, o saldrán de Canvas si es el último paso del recorrido del usuario.

## Sincronización de usuarios y consideraciones sobre límites de velocidad {#user-syncing-and-rate-limit-considerations}

A medida que los usuarios llegan al componente de Audience Sync, Braze sincronizará a estos usuarios casi en tiempo real, respetando los límites de velocidad de la API de Google Ads. Lo que esto significa en la práctica es que Braze intentará agrupar y procesar la mayor cantidad de usuarios posible cada 5 segundos antes de enviarlos a Google.

Una vez que un cliente está cerca de alcanzar el límite de velocidad de la API de Google Ads, Google proporcionará a Braze recomendaciones de reintento. Si un cliente de Braze alcanza su límite de velocidad, Braze reintentará la sincronización en el Canvas durante un máximo de &#126;13 horas. Si la sincronización no es posible, estos usuarios se incluirán en la métrica de usuarios con errores.

## Comprender los análisis {#understanding-analytics}

La siguiente tabla incluye métricas y descripciones para ayudarte a comprender mejor los análisis de tu paso de sincronización de audiencia.

| Métrica | Descripción |
| ------ | ----------- |
| *Ingresados* | Número de usuarios que ingresaron a este paso para ser sincronizados con Google. |
| *Avanzaron al siguiente paso* | Cuántos usuarios avanzaron al siguiente componente, si lo hay. Todos los usuarios avanzan automáticamente. Si este es el último paso en la rama del Canvas, esta métrica será 0. |
| *Usuarios sincronizados* | Número de usuarios que se han sincronizado correctamente con Google. |
| *Usuarios no sincronizados* | Número de usuarios que no se han sincronizado debido a campos faltantes para la coincidencia o porque el atributo de consentimiento se estableció en `false`. |
| *Usuarios con errores* | Número de usuarios que no se sincronizaron con Google debido a un error, después de &#126;13 horas de reintentos. Para errores específicos, como interrupciones del servicio de la API de Google Ads, Canvas reintentará la sincronización durante un máximo de &#126;13 horas. Si la sincronización aún no es posible en ese momento, se completará el campo *Usuarios no sincronizados*. |
| *Usuarios pendientes* | Número de usuarios que Braze está procesando actualmente para sincronizar con Google. |
| *Salieron del Canvas* | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso en un Canvas es un paso de Google. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprender los análisis" }

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Por qué no puedo seleccionar varios campos para hacer coincidir en la configuración de mi paso de Google Audience? {#why-can-i-not-select-multiple-fields-to-match-in-my-google-audience-step-configuration}

Google Customer Match tiene requisitos estrictos sobre cómo se formatean estas audiencias y qué información del cliente se incluye. Específicamente, los ID de anunciantes móviles deben cargarse por separado de la información de contacto del cliente (como correo electrónico y número de teléfono). Para más detalles, consulta la [documentación de Google Customer Match](https://support.google.com/google-ads/answer/7659867?hl=en#undefined).

### ¿Cuánto tiempo tardará en sincronizarse mi audiencia en Google? {#how-long-will-it-take-for-my-audiences-to-sync-in-google}

Una audiencia puede tardar entre 6 y 12 horas en sincronizarse en Google.

### He sincronizado una audiencia, pero ¿por qué el tamaño de la audiencia en Google es cero? {#ive-synced-an-audience-so-why-is-the-audience-size-in-google-zero}

Por motivos de privacidad, el tamaño de la lista de usuarios mostrará cero hasta que la lista tenga al menos 1000 miembros. Después de eso, el tamaño se redondeará a los dos dígitos más significativos.

### ¿Por qué el tamaño de mi audiencia coincidente en Google es menor que el número de usuarios sincronizados desde Braze? {#why-is-my-matched-audience-size-in-google-lower-than-the-number-of-users-synced-from-braze}

Aunque Braze puede sincronizar un cierto número de usuarios a Google, el tamaño real de la audiencia coincidente que ves en Google Ads puede ser significativamente menor. Esto se debe a que Google necesita hacer coincidir los datos de usuario que proporcionas (como direcciones de correo electrónico o números de teléfono) con cuentas de Google reales en su plataforma.

Incluso si tus perfiles de usuario de Braze contienen campos de coincidencia válidos, los usuarios solo aparecen en tu Google Custom Audience si tienen una cuenta de Google con información coincidente.

Para mejorar tu tasa de coincidencia:
- Confirma que estás [formateando tus datos correctamente](https://support.google.com/google-ads/answer/7659867).
- Proporciona múltiples identificadores cuando sea posible (por ejemplo, tanto correo electrónico como número de teléfono).
- Ten en cuenta que Google puede tardar entre 48 y 72 horas en procesar y hacer coincidir usuarios, aunque en algunos casos podría tardar varios días.

El tamaño final de la audiencia coincidente depende completamente del proceso de coincidencia de Google. Braze no tiene visibilidad sobre la coincidencia de Google una vez que los datos se han enviado a su plataforma.

### He sincronizado una audiencia en Google, pero mis anuncios no se están publicando. {#ive-synced-an-audience-into-google-but-my-ads-are-not-serving}

Verifica que tus audiencias contengan al menos 5000 usuarios para que los anuncios puedan comenzar a publicarse.

### ¿Cómo resuelvo el error "Mobile App IDs Deleted"? {#how-do-i-resolve-the-mobile-app-ids-deleted-error}

Si estás sincronizando audiencias con Google, este error se activará si seleccionaste sincronizar identificadores móviles como parte de tus sincronizaciones pero eliminaste los ID de aplicación móvil de la página del partner de Google. Para resolver este problema, asegúrate de haber agregado los ID de aplicación móvil apropiados para iOS y Android en la página del partner de Google.

### ¿Por qué recibí un correo electrónico de credenciales no válidas de Google Ads cuando el panel aún muestra que está conectado? {#why-did-i-get-a-google-ads-invalid-credentials-email-when-the-dashboard-still-shows-connected}

Braze envía este correo electrónico automáticamente cuando la API de Google devuelve un error de autorización. Esto puede ocurrir incluso cuando **Google Ads** todavía aparece como conectado en el panel y las audiencias parecen estar sincronizándose; por ejemplo, cuando la cuenta de Google conectada no tiene permiso para una acción específica que Google solicitó, o cuando los términos de servicio de Google Ads aún necesitan ser aceptados para la cuenta.

Algunos errores de autorización se resuelven por sí solos. Revisa los análisis de **Audience Sync** de tu Canvas (por ejemplo, *Users Synced* y *Users Errored*) para confirmar si los usuarios aún se están sincronizando. Si los problemas continúan, ve a **Partner Integrations** > **Technology Partners** > **Google Ads**, busca **Google Audience Sync** y usa **Change Account** para reconectarte con una cuenta de Google Ads que tenga el acceso requerido y la configuración completada.