---
nav_title: Espacios de trabajo
article_title: "Cómo empezar: Espacios de trabajo"
page_order: 3
page_type: reference
description: "Todo lo que haces en la plataforma Braze ocurre dentro de un espacio de trabajo. Este artículo describe cómo funcionan y qué consideraciones importantes hay que tener en cuenta al planificar los espacios de trabajo en Braze."
---

# Cómo empezar: Espacios de trabajo {#get-started-workspaces}

> Todo lo que haces en la plataforma Braze ocurre dentro de un espacio de trabajo. Los espacios de trabajo actúan como silos separados de datos y te permiten mantener separadas diferentes marcas o actividades. Varias versiones de tu sitio web o aplicación móvil pueden enviar datos al mismo espacio de trabajo. Nos referimos a los diferentes sitios y aplicaciones que se reúnen dentro de un espacio de trabajo como "instancias de la aplicación".

## Comprender los espacios de trabajo {#understanding-workspaces}

Los espacios de trabajo tienen dos objetivos fundamentales:

- **Unificar los datos de los usuarios:** Cuando varias instancias de la aplicación se encuentran en un espacio de trabajo, puedes recopilar y dirigir los datos del usuario fácilmente a través de diferentes versiones de tu aplicación, como iOS, Android y web. De este modo, siempre dispondrás de información actualizada sobre cada usuario, independientemente de la plataforma que utilice.
- **Separar actividades distintas:** Los espacios de trabajo también permiten mantener separadas distintas marcas o actividades. Por ejemplo, si tienes varias submarcas con diferentes bases de usuarios, es beneficioso crear espacios de trabajo separados para cada una.

{% alert tip %}
Este enfoque es especialmente útil para empresas como las de juegos para móviles, que pueden gestionar espacios de trabajo individuales para cada uno de sus juegos, o sitios de comercio electrónico que quieren espacios de trabajo separados para cada región en la que operan.
{% endalert %}

## Planificación de los espacios de trabajo {#planning-workspaces}

Debes crear instancias de aplicación distintas para cada versión de tu aplicación en cada plataforma. A la hora de decidir qué instancias de aplicación incluir en un espacio de trabajo, piensa en los usuarios a los que deseas dirigirte y agrúpalos en consecuencia.

El atractivo de tener varias instancias de la aplicación en un mismo espacio de trabajo puede ser tentador, ya que te permite limitar la tasa de mensajería en toda tu cartera de aplicaciones. Sin embargo, como práctica recomendada, sugerimos que solo se agrupen en un espacio de trabajo diferentes versiones de la misma aplicación (o de aplicaciones muy similares).

### Espacios de trabajo compartidos {#shared-workspaces}

Ejemplos comunes de casos en los que querrías tener varias instancias de aplicaciones en el mismo espacio de trabajo:

- Cuando tienes varias aplicaciones casi idénticas en diferentes plataformas
- Cuando tienes diferentes revisiones principales de la aplicación, pero quieres seguir atrayendo a los mismos usuarios cuando se actualizan
- Cuando existen diferentes versiones de la aplicación en las que un mismo usuario puede entrar o salir (por ejemplo, de gratuita a premium)

#### Impacto en los filtros de segmentación {#impact-on-segmentation-filters}

Cualquier aplicación que elijas tener en un espacio de trabajo tendrá sus datos agregados. Esto tendrá un impacto notable en los siguientes filtros de segmentación en Braze (esta no es una lista exhaustiva):

- Última aplicación usada
- Primera aplicación usada
- Recuento de sesiones
- Dinero gastado en la aplicación
- Suscripción push (Esto se convierte en una situación de todo o nada: si tus usuarios se dan de baja de una aplicación, se dan de baja de todas las aplicaciones del espacio de trabajo).
- Suscripción por correo electrónico (Esto se convierte en una situación de todo o nada y puede dejarte expuesto a problemas de cumplimiento).

{% alert note %}
La agregación de datos entre instancias de aplicaciones en estos filtros es la razón por la que no recomendamos alojar aplicaciones sustancialmente diferentes en el mismo espacio de trabajo. ¡Esto puede dificultar la segmentación!
{% endalert %}

### Espacios de trabajo separados {#separate-workspaces}

Otras veces, puede que desees tener varios espacios de trabajo separados. Algunos ejemplos habituales son:

- Espacios de trabajo separados para los entornos de desarrollo y producción de la misma aplicación
- Diferentes submarcas, por ejemplo, una empresa de juegos para móviles que ofrece varios juegos
- Diferentes localizaciones de la misma aplicación o sitio web que operan en diferentes países o se dirigen a diferentes idiomas

### Consideraciones importantes {#important-considerations}

Recuerda que los espacios de trabajo actúan como silos separados de datos. Todos los datos, ya sean datos de usuario o activos de marketing, se almacenan en un espacio de trabajo. Estos datos no pueden compartirse fácilmente fuera de ese espacio de trabajo.

A continuación se enumeran todos los elementos clave que se configuran dentro de un espacio de trabajo:

- [Instancias de la aplicación](#app-instances)
- [Equipos](#teams)
- [Permisos de usuario de la empresa](#company-user-permissions) (pero no usuarios de la empresa)
- [Conectores de Currents](#currents-connectors)
- [Perfiles de usuario](#user-profiles) y los datos de usuario asociados
- [Segments, Campaigns y Canvas](#segments-campaigns-and-canvases)

#### Instancias de la aplicación {#app-instances}

Debes crear instancias de aplicación distintas para cada versión de tu aplicación en cada plataforma. Por ejemplo, si tienes versiones Free y Pro de tu aplicación tanto en iOS como en Android, crea cuatro instancias de aplicación en tu espacio de trabajo (aplicación gratuita para iOS, aplicación gratuita para Android, aplicación pro para iOS y aplicación pro para Android). Esto te dará cuatro claves de API para utilizar, una para cada instancia de la aplicación.

#### Equipos {#teams}

Los [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) pueden configurarse en función de la ubicación de la base de clientes, el idioma y los atributos personalizados, de modo que los miembros del equipo y los que no lo son tengan diferente acceso a las funciones de mensajería y a los datos de los clientes.

#### Permisos de usuario de la empresa {#company-user-permissions}

Los espacios de trabajo tienen definiciones independientes de acceso y permisos de usuario. Los [permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) te permiten crear controles granulares sobre a qué tiene acceso un usuario individual del dashboard o un equipo dentro de un mismo espacio de trabajo.

#### Conectores de Currents {#currents-connectors}

La herramienta [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) es una transmisión de datos en tiempo real de tus eventos de interacción que es la exportación más sólida y granular de la plataforma Braze. Los conectores de Currents se incluyen con determinados paquetes de Braze, y es posible que hayas recibido uno inicialmente, asumiendo un único espacio de trabajo.

A la hora de decidir entre crear espacios de trabajo separados o combinados, es importante pensar en el número de conectores de Currents que tienes, ya que los conectores de Currents no se comparten entre espacios de trabajo.

Por ejemplo, si tienes espacios de trabajo separados para los entornos de desarrollo y producción de la misma aplicación, activa tu conector de Currents en el espacio de trabajo de producción. Para habilitar Currents en ambos espacios de trabajo, tendrás que comprar un conector de Currents adicional.

#### Perfiles de usuario {#user-profiles}

Todos los datos persistentes asociados a un usuario se almacenan en su [perfil de usuario]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/). Sin embargo, los perfiles de usuario también son un gran recurso para la solución de problemas y las pruebas, ya que puedes acceder fácilmente a información sobre el historial de interacción de un usuario, su pertenencia a un segmento, su dispositivo y su sistema operativo.

#### Segments, Campaigns y Canvas {#segments-campaigns-and-canvases}

Un Segment, una Campaign o un Canvas no pueden hacer referencia ni acceder a datos alojados en otro espacio de trabajo. Por el contrario, cuando varias aplicaciones se encuentran en el mismo espacio de trabajo, todas las aplicaciones tendrán sus datos agregados. Esto tendrá un [impacto en los filtros de Braze](#impact-on-segmentation-filters).

### Resumen de cada enfoque {#overview-of-each-approach}

En la tabla siguiente se describen las ventajas e inconvenientes de estos dos enfoques de la planificación del espacio de trabajo:

- **Espacios de trabajo y perfiles de usuario separados:** Un espacio de trabajo tiene una instancia de aplicación y una persona tiene un perfil de usuario para esa instancia de aplicación.
- **Espacios de trabajo y perfiles de usuario compartidos:** Un espacio de trabajo tiene varias instancias de aplicación y una persona tiene un perfil de usuario para todas esas instancias de aplicación.

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
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
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
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
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
        <th scope="col">Ventajas</th>
        <th scope="col">Inconvenientes</th>
        <th scope="col">Ventajas</th>
        <th scope="col">Inconvenientes</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <th scope="row">Segmentación</th>
        <td>La forma más segura de mantener las comunicaciones separadas. Se garantiza que las Campaigns se dirijan únicamente a perfiles de usuario específicos.</td>
        <td>Imposibilidad de enviar mensajes de promoción cruzada aunque sepas que un usuario tiene otro perfil de usuario en un espacio de trabajo diferente.</td>
        <td>Puedes enviar mensajes de promoción cruzada si sabes que un usuario tiene varias aplicaciones en tu espacio de trabajo.<br><br>Puedes hacer referencia a datos de usuario de distintas aplicaciones. Por ejemplo, Juan tiene un atributo X relevante para la aplicación 1 y un atributo Y relevante para la aplicación 2, y ambos pueden referenciarse en una Campaign.</td>
        <td>Más margen para el error humano: podrías dirigirte accidentalmente a usuarios de varias instancias de la aplicación.<br><br>Para enviar mensajes dentro de la aplicación, debes tener eventos personalizados específicos de la aplicación para que una Campaign no se muestre en otra aplicación por accidente. Por ejemplo, <code>app_1_action</code> frente a <code>app_2_action</code>.</td>
    </tr>
    <tr>
        <th scope="row">Eventos y atributos personalizados</th>
        <td>Se garantiza que los atributos y eventos personalizados son específicos de una instancia de aplicación.</td>
        <td>No se puede realizar un seguimiento del comportamiento de los usuarios en los distintos espacios de trabajo.<br><br><b>Consejo:</b> Para ello, puedes aprovechar varios conectores de Currents.</td>
        <td>Puedes realizar un seguimiento del comportamiento del usuario en todas las instancias de la aplicación en el espacio de trabajo.</td>
        <td>Los atributos y eventos personalizados se aplicarían a todas las instancias de la aplicación, lo que podría dificultar saber qué datos de un perfil de usuario son relevantes para qué instancia de la aplicación. Por ejemplo, ¿es "date_of_parking" relevante para la aplicación 1 o la aplicación 2? Para evitarlo, asegúrate de utilizar convenciones de nomenclatura bien estructuradas.</td>
    </tr>
    <tr>
        <th scope="row">Limitación de frecuencia</th>
        <td>La limitación de frecuencia puede definirse por separado para cada instancia de aplicación (en función del espacio de trabajo).</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>La limitación de frecuencia se aplica a todas las Campaigns, no a cada aplicación, lo que hace más difícil evitar el exceso de mensajes a los clientes.</td>
    </tr>
    <tr>
        <th scope="row">Estado de suscripción de los perfiles de usuario</th>
        <td>El estado de suscripción de cada perfil de usuario es único para cada instancia de la aplicación.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Los estados de suscripción de un perfil de usuario se combinan en todas las instancias de la aplicación.<br><br><b>Consejo:</b> En su lugar, podrías utilizar <a href='/docs/user_guide/data/activation/attributes/custom_attributes'>atributos personalizados</a> para gestionar las suscripciones de tus usuarios.</td>
    </tr>
    <tr>
        <th scope="row">Permisos de usuario de la empresa</th>
        <td>N/A</td>
        <td>La actualización de los <a href='/docs/user_guide/administer/global/user_management/permissions'>permisos de usuario</a> de un usuario del dashboard debe hacerse por separado para cada espacio de trabajo al que el usuario necesite acceder.</td>
        <td>Los <a href='/docs/user_guide/administer/global/user_management/permissions'>permisos de usuario</a> pueden configurarse una vez para un usuario del dashboard, y tendrá los mismos permisos para todas las instancias de la aplicación en el espacio de trabajo.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <th scope="row">Duplicación de contenidos</th>
        <td>N/A</td>
        <td>No se pueden duplicar Segments, Campaigns de push o de tarjeta de contenido, ni Canvas entre espacios de trabajo.</td>
        <td>Puedes <a href='{{site.baseurl}}/user_guide/messaging/governance/copy_across_workspaces/'>duplicar Campaigns entre espacios de trabajo</a> para los siguientes canales compatibles: SMS, mensajes dentro de la aplicación, correo electrónico, plantillas de correo electrónico y Content Blocks. <br><br>Puedes duplicar Segments, Campaigns y Canvas para reutilizar el contenido de una instancia de aplicación a otra.</td>
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

## Buenas prácticas {#best-practices}

### Configurar un espacio de trabajo de pruebas {#set-up-a-testing-workspace}

Como práctica recomendada, siempre que tengas previsto configurar un espacio de trabajo de producción (un espacio de trabajo que enviará mensajes a usuarios reales), también deberías configurar un espacio de trabajo de pruebas. Un espacio de trabajo de pruebas es un duplicado de tu espacio de trabajo de producción sin ningún dato real de usuario.

Esto se considera una buena práctica por varias razones:

- **Aislamiento de los cambios:** Te permite probar nuevas funciones, configuraciones o actualizaciones en un entorno aislado sin afectar a tu entorno de producción en vivo. De este modo, si algo sale mal durante las pruebas, tu entorno de producción no se verá afectado.
- **Pruebas precisas:** Permite realizar pruebas más precisas, ya que los datos del entorno de pruebas pueden controlarse y manipularse sin preocuparse por los datos del mundo real.
- **Depuración:** Es más fácil depurar problemas en un entorno de pruebas, ya que puedes manipular libremente el entorno sin preocuparte de afectar al entorno de producción.
- **Formación:** Los nuevos miembros del equipo pueden familiarizarse con el espacio de trabajo en un entorno seguro en el que los errores no tendrán consecuencias en el mundo real.

{% alert tip %}
El orden en que configures un espacio de trabajo de pruebas y un espacio de trabajo de producción puede depender de tus necesidades y circunstancias específicas. Sin embargo, suele ser una buena idea configurar primero un espacio de trabajo de pruebas. Esto te permite probar funciones, configuraciones y actualizaciones antes de implementarlas en el espacio de trabajo de producción. Cuando estés satisfecho con las pruebas y los resultados, podrás establecer tu espacio de trabajo de producción.
{% endalert %}

### Añadir administradores {#add-administrators}

Deberías tener más de un usuario de Braze con permisos de administrador para un mismo espacio de trabajo. Esto garantiza que haya suficientes personas en tu organización para gestionar los permisos de otros usuarios.

## Próximos pasos {#next-steps}

Una vez que hayas determinado tu plan de espacio de trabajo, es hora de crear tu espacio de trabajo y añadir instancias de aplicaciones. Para conocer los pasos a seguir, consulta [Crear y administrar espacios de trabajo]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces/).