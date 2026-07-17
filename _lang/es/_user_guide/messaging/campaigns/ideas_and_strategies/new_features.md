---
nav_title: Conocimiento de características y nueva versión de la aplicación
article_title: Conocimiento de características y nueva versión de la aplicación
page_order: 9
page_type: reference
description: "Este artículo de referencia explica cómo mantener a tus usuarios informados y entusiasmados cuando lanzas nuevas características o versiones."
tool: Campaigns

---

# Conocimiento de características y nueva versión de la aplicación {#feature-awareness-and-new-app-version}

> Este artículo de referencia aborda cómo usar la plataforma Braze para mantener a tus clientes al día sobre las nuevas características y versiones de tu aplicación.

Trabajas duro para actualizar y mejorar continuamente tu aplicación, y quieres que tus usuarios experimenten estas emocionantes nuevas características y versiones. Aprende cómo enseñar a tus usuarios sobre las nuevas características que aún no han utilizado, y anímalos a explorar la aplicación para aprovechar al máximo lo que tienes para ofrecer.

Las campañas de conocimiento de características son una excelente manera de animar a los usuarios a mantenerse comprometidos con tu aplicación mientras continúas mejorando su funcionalidad. Mantener a los usuarios al día es una gran forma de mantenerlos activos, mejorar las valoraciones y asegurar la interacción de los usuarios.

## Filtrar por las versiones más recientes de la aplicación {#filtering-by-most-recent-app-versions}

Los SDK de Braze rastrean automáticamente la versión más reciente de la aplicación de un usuario. Estas versiones se pueden usar en filtros y Segments para determinar qué usuarios deben recibir un mensaje o una Campaign.

![El panel de opciones de segmentación en el paso Usuarios objetivo del flujo de trabajo de creación de Campaigns. La sección Filtros adicionales incluye el siguiente filtro "Most Recent App Version Number for Android Stopwatch (Android) is below 3.7.0 (134.0.0.0)".]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

{% alert note %}
Puede tomar tiempo para que las versiones actuales de la aplicación se completen. La versión de la aplicación en el perfil de usuario se actualiza cuando la información es capturada por el SDK, lo cual depende de cuándo los usuarios abren sus aplicaciones. Si el usuario no abre la aplicación, la versión actual no se actualizará. <br><br> Estos filtros tampoco se aplican retroactivamente. Es recomendable usar "mayor que" o "igual a" para versiones actuales y futuras, pero usar filtros de versiones pasadas puede causar comportamientos inesperados.
{% endalert %}

### Número de versión de la aplicación {#app-version-number}

Usa el filtro **Número de versión de la aplicación** para segmentar usuarios por la versión y el número de compilación de la aplicación.

Este filtro admite comparaciones numéricas para segmentar un rango de versiones de la aplicación. Por ejemplo, puedes segmentar usuarios cuya aplicación esté "por debajo", "por encima" o "sea igual a" la versión "1.2.3", lo cual puede ser útil para promover una nueva característica que requiera una actualización de la aplicación.

Este nuevo filtro puede reemplazar el filtro heredado "Nombre de versión de la aplicación", que requería listar explícitamente cada versión anterior o usar una expresión regular.

**Cómo funciona**

* Cada parte de la versión `major.minor.patch` enviada en la versión de tu aplicación se compara como números enteros
* Si los números principales son iguales, se comparan los números secundarios, y así sucesivamente.

**Importante**

* Las aplicaciones Android tienen tanto un [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) legible para humanos como un [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) interno. El filtro Número de versión de la aplicación usa `versionCode` porque se garantiza que se incrementa con cada lanzamiento en la tienda de aplicaciones.
* Esto puede causar confusión cuando el `versionName` y el `versionCode` de tu aplicación se desincronizan, especialmente porque ambos campos se pueden ver desde el panel de Braze. Como buena práctica, verifica que el `versionName` y el `versionCode` de tu aplicación se incrementen juntos.
* Si necesitas filtrar por el campo legible `versionName` en su lugar (poco común), usa el filtro Nombre de versión de la aplicación.

#### Requisitos del SDK {#sdk-requirements}

Los valores para este filtro se recopilan a partir del SDK de Braze para Android v3.6.0+ y el SDK para iOS v3.21.0+. Aunque este filtro tiene requisitos de SDK, aún podrás segmentar usuarios que estén en versiones más bajas (antiguas) de tu aplicación usando esta característica.

Para Android, este número de versión se basa en el [Package Long Version Code](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) de la aplicación.

Para iOS, este número de versión se basa en el [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) de la aplicación.

{% alert tip %}
Este filtro mostrará valores después de que los usuarios actualicen sus aplicaciones a las versiones compatibles del SDK de Braze. Hasta entonces, el filtro no mostrará ninguna versión cuando se seleccione.
{% endalert %}

#### Caso de uso {#use-case}

En el siguiente escenario, supongamos que primero actualizaste a los SDK de Braze que admiten este filtro en la versión `2.0.0` de tu aplicación.

Una vez que Braze reciba datos de la versión 2.0.0 de tu aplicación, puedes segmentar usuarios con versiones anteriores o posteriores.

| Filtro  | Versión de la aplicación del usuario  | Resultado |
| :------------- | :----------- | :--------- |
| Menor que 2.0.0 | 1.0.0 | El usuario está en el segmento, aunque su SDK de Braze no admitía el filtro "Número de versión de la aplicación". |
| Mayor que 2.0.0 | 2.5.1 | El usuario y todas las instalaciones futuras estarán en el segmento. |
| Mayor que 2.0.0 | 1.9.9 | El usuario no está en el segmento. |
| Menor o igual que 2.0.0 | 3.0.1 | El usuario no está en el segmento. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Caso de uso" }

### Nombre de versión de la aplicación {#app-version-name}

Usa el filtro "Nombre de versión de la aplicación" para segmentar usuarios por el "nombre de compilación" visible para el usuario de la aplicación.

Este filtro admite coincidencias con "es", "no es" y expresiones regulares. Por ejemplo, puedes segmentar usuarios que tengan una aplicación que no sea la versión "1.2.3-test-build".

Para Android, este nombre de versión se basa en el [Package Version Name](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) de la aplicación. Para iOS, este nombre de versión se basa en el [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) de la aplicación.

### No han usado una característica {#have-not-used-feature}

Cuando lanzas una nueva versión de la aplicación e introduces nuevas características, es posible que los usuarios no noten el nuevo contenido. Ejecutar una campaña de conocimiento de características es una excelente manera de enseñar a los usuarios sobre nuevas características o características que nunca han usado. Para hacerlo, debes crear un [atributo personalizado]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) que se asigne a los usuarios que nunca han completado una determinada acción dentro de tu aplicación, o usar un [evento personalizado]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) para rastrear una acción particular. Puedes usar este atributo (o evento) para segmentar a los usuarios a los que deseas enviar la Campaign.

{% alert tip %}
¿Buscas reorientar a una porción específica de tu audiencia? Consulta [Campaigns de reorientación]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns) para aprender cómo reorientar Campaigns aprovechando las acciones previas de tus usuarios.
{% endalert %}