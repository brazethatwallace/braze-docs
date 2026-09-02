---
nav_title: Espacios de trabajo
article_title: "Cómo empezar: Espacios de trabajo"
page_order: 3
page_type: reference
description: "Todo lo que haces en la plataforma Braze ocurre dentro de un espacio de trabajo. Este artículo describe cómo funcionan y qué consideraciones importantes hay que tener en cuenta."
---

# Cómo empezar: Espacios de trabajo {#get-started-workspaces}

> Todo lo que haces en la plataforma Braze ocurre dentro de un espacio de trabajo. Los espacios de trabajo actúan como silos separados de datos y te permiten mantener separadas diferentes marcas o actividades. Varias versiones de tu sitio web o aplicación móvil pueden enviar datos al mismo espacio de trabajo. Nos referimos a los diferentes sitios y aplicaciones que se reúnen dentro de un espacio de trabajo como "instancias de la aplicación".

## Entendiendo los espacios de trabajo {#understanding-workspaces}

Los espacios de trabajo cumplen dos propósitos clave:

- **Unificar datos de usuario:** Cuando varias instancias de la aplicación están en un espacio de trabajo, puedes recopilar y segmentar datos de usuario fácilmente a través de diferentes versiones de tu aplicación, como iOS, Android y web. Esto asegura que siempre tengas información actualizada sobre cada usuario, independientemente de la plataforma que esté usando.
- **Separar actividades distintas:** Los espacios de trabajo también proporcionan un medio para mantener separadas marcas o actividades distintas. Por ejemplo, si tienes varias submarcas con diferentes bases de usuarios, es beneficioso crear espacios de trabajo separados para cada una.

{% alert tip %}
Este enfoque es particularmente útil para empresas como las de videojuegos móviles, que pueden gestionar espacios de trabajo individuales para cada uno de sus juegos, o sitios de eCommerce que quieran espacios de trabajo separados para cada región en la que operan.
{% endalert %}

## Planificación de espacios de trabajo {#planning-workspaces}

Debes crear instancias de la aplicación independientes para cada versión de tu aplicación en cada plataforma. Al decidir qué instancias de la aplicación incluir en un espacio de trabajo, piensa en los usuarios a los que deseas dirigirte y agrúpalos en consecuencia.

Tener múltiples instancias de la aplicación en un solo espacio de trabajo puede resultar atractivo, ya que te permite aplicar límites de velocidad a la mensajería en todo tu portafolio de aplicaciones. Sin embargo, como práctica recomendada, sugerimos agrupar en un mismo espacio de trabajo solo las diferentes versiones de las mismas aplicaciones (o muy similares).

### Espacios de trabajo compartidos {#shared-workspaces}

Ejemplos comunes en los que querrías tener múltiples instancias de la aplicación en el mismo espacio de trabajo:

- Cuando tienes múltiples aplicaciones casi idénticas en diferentes plataformas
- Cuando tienes diferentes revisiones principales de la aplicación, pero quieres seguir interactuando con los mismos usuarios cuando se actualicen
- Cuando tienes diferentes versiones de la aplicación entre las que el mismo usuario podría moverse (como de gratuita a premium)

#### Impacto en los filtros de segmentación {#impact-on-segmentation-filters}

Las aplicaciones que elijas tener en un espacio de trabajo tendrán sus datos agregados. Esto tendrá un impacto notable en los siguientes filtros de segmentación en Braze (esta no es una lista exhaustiva):

- Última aplicación utilizada
- Primera aplicación utilizada
- Recuento de sesiones
- Dinero gastado en la aplicación
- Suscripción push (Se convierte en una situación de todo o nada; si tus usuarios cancelan la suscripción de una aplicación, se cancelará la suscripción de todas las aplicaciones en el espacio de trabajo).
- Suscripción de correo electrónico (Se convierte en una situación de todo o nada y puede dejarte expuesto a problemas de cumplimiento).

{% alert note %}
La agregación de datos entre instancias de la aplicación en estos filtros es la razón por la que no recomendamos alojar aplicaciones sustancialmente diferentes dentro del mismo espacio de trabajo. ¡Puede hacer que la segmentación sea complicada!
{% endalert %}

### Espacios de trabajo separados {#separate-workspaces}

En otros casos, es posible que desees tener múltiples espacios de trabajo separados. Ejemplos comunes incluyen:

- Espacios de trabajo separados para los entornos de desarrollo y producción de la misma aplicación
- Diferentes submarcas, por ejemplo, una empresa de juegos móviles que ofrece varios juegos
- Diferentes localizaciones de la misma aplicación o sitio web que operan en diferentes países o se dirigen a diferentes idiomas

### Consideraciones importantes {#important-considerations}

Recuerda que los espacios de trabajo actúan como silos de datos separados. Todos los datos, ya sean datos de usuario o activos de marketing, se almacenan dentro de un espacio de trabajo. Estos datos no se pueden compartir fácilmente fuera de ese espacio de trabajo.

Los siguientes son elementos clave que se configuran dentro de un espacio de trabajo:

- [Instancias de la aplicación](#app-instances)
- [Equipos](#teams)
- [Permisos de usuario de la empresa](#company-user-permissions) (pero no los usuarios de la empresa)
- [Conectores de Currents](#currents-connectors)
- [Perfiles de usuario](#user-profiles) y los datos de usuario asociados
- [Segments, Campaigns y Canvas](#segments-campaigns-and-canvases)

#### Instancias de la aplicación {#app-instances}

Debes crear instancias de la aplicación independientes para cada versión de tu aplicación en cada plataforma. Por ejemplo, si tienes versiones gratuita y profesional de tu aplicación tanto en iOS como en Android, crea cuatro instancias de la aplicación dentro de tu espacio de trabajo (aplicación gratuita de iOS, aplicación gratuita de Android, aplicación profesional de iOS y aplicación profesional de Android). Esto te dará cuatro claves de API para usar, una para cada instancia de la aplicación.

#### Equipos {#teams}

Los [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) se pueden configurar según la ubicación de la base de clientes, el idioma y los atributos personalizados, de modo que los miembros del equipo y los no miembros tengan diferente acceso a las características de mensajería y a los datos de clientes.

#### Permisos de usuario de la empresa {#company-user-permissions}

Los espacios de trabajo tienen definiciones de acceso y permisos de usuario independientes. Los [permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) te permiten crear controles granulares sobre lo que un usuario individual del panel o un equipo puede acceder dentro de un solo espacio de trabajo.

#### Conectores de Currents {#currents-connectors}

La herramienta [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) es una transmisión de datos en tiempo real de tus eventos de participación que es la exportación más robusta y granular de la plataforma Braze. Los conectores de Currents están incluidos en ciertos paquetes de Braze, y es posible que inicialmente hayas recibido uno, asumiendo un único espacio de trabajo.

Cuando estés decidiendo entre crear espacios de trabajo separados o combinados, es importante pensar en la cantidad de conectores de Currents que tienes, ya que los conectores de Currents no se comparten entre espacios de trabajo.

Por ejemplo, si tienes espacios de trabajo separados para los entornos de desarrollo y producción de la misma aplicación, activa tu conector de Currents en el espacio de trabajo de producción. Para habilitar Currents en ambos espacios de trabajo, necesitarás adquirir un conector de Currents adicional.

#### Perfiles de usuario {#user-profiles}

Todos los datos persistentes asociados con un usuario se almacenan en su [perfil de usuario]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles). Sin embargo, los perfiles de usuario también son un excelente recurso para la solución de problemas y las pruebas, ya que puedes acceder fácilmente a información sobre el historial de participación de un usuario, su membresía en Segments, dispositivo y sistema operativo.

#### Segments, Campaigns y Canvas {#segments-campaigns-and-canvases}

Un Segment, Campaign o Canvas no puede hacer referencia ni acceder a datos alojados en otro espacio de trabajo. Por el contrario, cuando hay múltiples aplicaciones en el mismo espacio de trabajo, todas las aplicaciones tendrán sus datos agregados. Esto tendrá un [impacto en los filtros en Braze](#impact-on-segmentation-filters).

### Resumen de cada enfoque {#overview-of-each-approach}

La siguiente tabla describe los beneficios y desventajas de estos dos enfoques para la planificación de espacios de trabajo:

- **Espacios de trabajo y perfiles de usuario separados:** Un espacio de trabajo tiene una instancia de la aplicación y una persona tiene un perfil de usuario para esa instancia de la aplicación.
- **Espacios de trabajo y perfiles de usuario compartidos:** Un espacio de trabajo tiene múltiples instancias de la aplicación y una persona tiene un perfil de usuario para todas esas instancias de la aplicación.

<style type="text/css">
  table {
    width: 100%;
  }
  th, td {
    padding: 8px;
    text-align: left;
    border: 1px solid black;
    word-break: break-word !important;
  }
  th {
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  }
  th[colspan="2"] {
    background-color: #fffae6;
  }
  th:last-child[colspan="2"] {
    background-color: #deebff;
  }
  td:nth-child(2), td:nth-child(3) {
    background-color: #fffae6;
  }
  td:nth-child(4), td:nth-child(5) {
    background-color: #deebff;
  }
  th:nth-child(2), th:nth-child(3) {
    background-color: #fffae6;
  }
  th:nth-child(4), th:nth-child(5) {
    background-color: #deebff;
  }
  th:first-child, td:first-child {
    min-width: 150px;
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  }
</style>

<table aria-label="Resumen de cada enfoque">
  <caption>Resumen de cada enfoque</caption>
    <thead>
    <tr>
        <th></th>
        <th colspan="2" scope="colgroup">Espacios de trabajo separados</th>
        <th colspan="2" scope="colgroup">Espacios de trabajo compartidos</th>
    </tr>
    <tr>
        <th></th>
        <th scope="col">Beneficios</th>
        <th scope="col">Desventajas</th>
        <th scope="col">Beneficios</th>
        <th scope="col">Desventajas</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <th scope="row">Segmentación</th>
        <td>La forma más segura de mantener las comunicaciones separadas. Se garantiza que las Campaigns se dirijan solo a perfiles de usuario específicos.</td>
        <td>No es posible enviar mensajería de promoción cruzada aunque sepas que un usuario tiene otro perfil de usuario en un espacio de trabajo diferente.</td>
        <td>Puedes enviar mensajería de promoción cruzada si sabes que un usuario tiene múltiples aplicaciones en tu espacio de trabajo.<br><br>Puedes hacer referencia a datos de usuario de todas las aplicaciones. Por ejemplo, Juan tiene el atributo X relevante para la aplicación 1, y el atributo Y relevante para la aplicación 2, y ambos pueden referenciarse en una Campaign.</td>
        <td>Más margen para el error humano: podrías dirigirte accidentalmente a usuarios en múltiples instancias de la aplicación.<br><br>Para enviar mensajes dentro de la aplicación, necesitas eventos personalizados específicos de la aplicación para que una Campaign no se muestre en otra aplicación por accidente. Por ejemplo, <code>app_1_action</code> versus <code>app_2_action</code>.</td>
    </tr>
    <tr>
        <th scope="row">Eventos y atributos personalizados</th>
        <td>Se garantiza que los atributos y eventos personalizados sean específicos de una instancia de la aplicación.</td>
        <td>No se puede rastrear el comportamiento del usuario entre espacios de trabajo.<br><br><b>Consejo:</b> puedes aprovechar múltiples conectores de Currents para lograr esto.</td>
        <td>Puedes rastrear el comportamiento del usuario en todas las instancias de la aplicación en el espacio de trabajo.</td>
        <td>Los atributos y eventos personalizados se aplicarían a todas las instancias de la aplicación, lo que podría dificultar determinar qué datos en un perfil de usuario son relevantes para qué instancia de la aplicación. Por ejemplo, ¿"date_of_parking" es relevante para la aplicación 1 o la aplicación 2? Para combatir esto, asegúrate de utilizar convenciones de nomenclatura bien estructuradas.</td>
    </tr>
    <tr>
        <th scope="row">Limitación de frecuencia</th>
        <td>La limitación de frecuencia se puede definir por separado para cada instancia de la aplicación (según el espacio de trabajo).</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>La limitación de frecuencia se aplica a todas las Campaigns, no por aplicación, lo que dificulta prevenir el envío excesivo de mensajes a los clientes.</td>
    </tr>
    <tr>
        <th scope="row">Estado de suscripción para perfiles de usuario</th>
        <td>El estado de suscripción de cada perfil de usuario es único para cada instancia de la aplicación.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Los estados de suscripción de un perfil de usuario se combinan entre las instancias de la aplicación.<br><br><b>Consejo:</b> podrías usar <a href='/docs/user_guide/data/activation/attributes/custom_attributes'>atributos personalizados</a> para gestionar las suscripciones de tus usuarios.</td>
    </tr>
    <tr>
        <th scope="row">Permisos de usuario de la empresa</th>
        <td>N/A</td>
        <td>La actualización de los <a href='/docs/user_guide/administer/global/user_management/permissions'>permisos de usuario</a> para un usuario del panel debe hacerse por separado para cada espacio de trabajo al que el usuario necesite acceso.</td>
        <td>Los <a href='/docs/user_guide/administer/global/user_management/permissions'>permisos de usuario</a> se pueden configurar una sola vez para un usuario del panel, y tendrá los mismos permisos para todas las instancias de la aplicación en el espacio de trabajo.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <th scope="row">Duplicación de contenido</th>
        <td>N/A</td>
        <td>Algunos contenidos, como Segments y campañas de tarjeta de contenido, no se pueden copiar entre espacios de trabajo.</td>
        <td>Puedes <a href='{{site.baseurl}}/user_guide/messaging/governance/copy_across_workspaces'>copiar Campaigns, Canvas y páginas de destino entre espacios de trabajo</a>. El contenido compatible incluye Campaigns y Canvas para canales elegibles, así como páginas de destino, plantillas de correo electrónico, conmutadores de características y Content Blocks.<br><br>Puedes duplicar Segments, Campaigns, Canvas y páginas de destino para reutilizar contenido de una instancia de la aplicación a otra.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <th scope="row">Análisis</th>
        <td>Las estadísticas globales serán precisas en la página de inicio.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Las estadísticas globales se agregarán para todas las instancias de la aplicación en el espacio de trabajo en la página de inicio.</td>
    </tr>
    </tbody>
</table>

{% alert note %}
Para saber cómo difieren los MAU al ver todas las aplicaciones en comparación con una sola aplicación, consulta [MAU]({{site.baseurl}}/user_guide/analytics/dashboards/home#monthly-active-users).
{% endalert %}

## Buenas prácticas {#best-practices}

### Configurar un espacio de trabajo de pruebas {#set-up-a-testing-workspace}

Como buena práctica, siempre que planees configurar un espacio de trabajo de producción (un espacio de trabajo que enviará mensajes a usuarios reales), también deberías configurar un espacio de trabajo de pruebas. Un espacio de trabajo de pruebas es un duplicado de tu espacio de trabajo de producción sin datos de usuarios reales.

Esto se considera una buena práctica por varias razones:

- **Aislamiento de cambios:** Te permite probar nuevas características, configuraciones o actualizaciones en un entorno aislado sin afectar tu entorno de producción en vivo. De esta forma, si algo sale mal durante las pruebas, tu entorno de producción no se ve afectado.
- **Pruebas precisas:** Permite realizar pruebas más precisas, ya que los datos en el entorno de pruebas pueden controlarse y manipularse sin preocuparse por los datos reales.
- **Depuración:** Es más fácil depurar problemas en un entorno de pruebas, ya que puedes manipular libremente el entorno sin preocuparte por impactar el entorno de producción.
- **Formación:** Los nuevos miembros del equipo pueden familiarizarse con el espacio de trabajo en un entorno seguro donde los errores no tendrán consecuencias reales.

{% alert tip %}
El orden en que configuras un espacio de trabajo de pruebas y uno de producción puede depender de tus necesidades y circunstancias específicas. Sin embargo, generalmente es buena idea configurar primero el espacio de trabajo de pruebas. Esto te permite probar características, configuraciones y actualizaciones antes de que se implementen en el espacio de trabajo de producción. Una vez que estés satisfecho con las pruebas y los resultados, puedes establecer tu espacio de trabajo de producción.
{% endalert %}

### Añadir administradores {#add-administrators}

Deberías tener más de un usuario de Braze con permisos de administrador para un mismo espacio de trabajo. Esto asegura que haya suficientes personas en tu organización para gestionar los permisos de otros usuarios.

## Próximos pasos {#next-steps}

Después de determinar tu plan de espacio de trabajo, es momento de crear tu espacio de trabajo y añadir instancias de la aplicación. Para conocer los pasos, consulta [Crear y gestionar espacios de trabajo]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces).