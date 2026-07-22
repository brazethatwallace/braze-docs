---
nav_title: Celebrus
article_title: Integración de Celebrus
description: "Integración de Braze y Celebrus."
---

# Celebrus

> Celebrus se integra fácilmente con el SDK de Braze en canales web y de aplicaciones móviles, facilitando la población de Braze con datos de actividad del canal. Esto incluye información exhaustiva sobre el tráfico de visitantes a través de activos digitales durante periodos específicos. <br><br>Además, Celebrus captura datos de perfil enriquecidos para cada cliente individual, que pueden sincronizarse con Braze. Esto te permite crear estrategias eficaces de comunicación y análisis de Braze basadas en datos propios completos, precisos y detallados. Esta capacidad se ve reforzada por las señales basadas en aprendizaje automático de Celebrus, que permiten una captura de datos sin complicaciones y sin necesidad de un etiquetado exhaustivo. Con un sólido gráfico de identidades propias, todos los datos son accesibles al instante para su uso inmediato.

_Esta integración está mantenida por Celebrus._

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta Celebrus | Se necesita una cuenta Celebrus para beneficiarse de esta asociación. |
| Almacén de datos (opcional) | Al utilizar el conector Celebrus para atributos personalizados de Braze, debes disponer de un almacén de datos compatible con la integración de ingesta de datos en la nube (CDI) de Braze y configurar CDI en el panel de Braze. |
| Configuración del SDK de Braze (opcional) | Cuando utilices el conector Celebrus para el SDK de Braze, debes pasar el punto final de SDK y la clave de API de SDK. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Implementación {#implementation}
Después de instalar tu implementación de Celebrus, utiliza los conectores de Celebrus para Braze para integrar los datos de Celebrus en Braze. Hay dos elementos en la integración de Celebrus para Braze: el SDK de Braze y los atributos personalizados de Braze. Puedes desplegar cualquiera de los dos, o ambos, en función de cómo utilices Braze y de los ejemplos que necesites.

Si aún no tienes implementado el SDK de Braze en tu canal web, puedes utilizar Celebrus para desplegar el SDK de Braze. Celebrus añadirá el SDK de Braze a las páginas web y configurará la identidad de Braze para el visitante web utilizando el gráfico de identidad de Celebrus. Los atributos de los clientes pueden sincronizarse con Braze mediante ingesta de datos en la nube (CDI). Esto requiere un almacén de datos compatible con Braze CDI, así como la configuración del CDI en Braze.

### Conector Celebrus para el SDK de Braze {#celebrus-connector-for-braze-sdk}

El conector Celebrus para el SDK de Braze proporciona datos de canal de alto nivel de aplicaciones web y móviles para Braze. En el SDK de Braze, el `System Identity` de Celebrus del gráfico de identidad de Celebrus se utilizará como identificador para la integración de Braze. Se admiten otros identificadores para sincronizar atributos personalizados a través del conector Celebrus para atributos personalizados de Braze.

El conector despliega y configura el SDK de Braze en tu canal, por lo que tendrás que configurar algunos ajustes en la transmisión de datos del SDK de Braze y proporcionar los valores de estos tres ajustes:

```
    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
```

{% alert important %}
El conector Celebrus para el SDK de Braze insertará e inicializará el SDK de Braze para identificar al usuario y añadir el identificador al gráfico de identidad de Celebrus. Este conector no registrará datos en el perfil de usuario ni desencadenará otros métodos del SDK de Braze. <br><br>Puedes llamar a los métodos que desees directamente dentro de tu base de código para registrar datos a través del [SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) o aprovechar otras características compatibles con el SDK de Braze.
{% endalert%}

### Conector Celebrus para atributos personalizados de Braze {#celebrus-connector-for-braze-custom-attributes}

#### Paso 1: Configurar detalles de conexión en Celebrus {#step-1-configure-connected-details-in-celebrus}

El conector Celebrus para atributos personalizados de Braze envía atributos personalizados a una base de datos intermedia, preformateados de la forma en que Braze espera recibirlos. En Celebrus configuras los detalles de conexión para la base de datos, que dependerán del tipo de base de datos que estés utilizando (como Snowflake o Redshift).

#### Paso 2: Configurar la ingesta de datos en la nube en tu panel de Braze {#step-2-configure-cloud-data-ingestion-in-your-braze-dashboard}

Esta integración utiliza la ingesta de datos en la nube de Braze. Sigue las instrucciones en [Integraciones de almacenes de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations) para establecer y configurar los [ajustes de ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) según el tipo de almacén que estés utilizando.

#### Paso 3: Sincronizar datos de Celebrus a Braze {#step-3-sync-data-from-celebrus-to-braze}

Celebrus captura y asigna identificadores únicos a un individuo, como correo electrónico, teléfono, `external_id` o alias de usuario, y los envía a Braze a través de CDI. Esto permite sincronizar con Braze los datos de un mismo individuo.

Celebrus utiliza los identificadores definidos para enviar los atributos del cliente definidos en el generador de perfiles de Celebrus, pero solo cuando cambian los valores de los atributos. Ten en cuenta que los nombres de atributos definidos en el generador de perfiles de Celebrus se utilizan en Braze de forma predeterminada. Así que asegúrate de actualizar estos nombres para que se adhieran a las [convenciones de nomenclatura de Braze]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).

{% alert important %}
Por ahora, esta versión no admite eventos ni compras.<br><br> Esta integración envía atributos como valores de cadena, por lo que algunos atributos son listas (como las señales). Por ahora, las listas no pueden convertirse en arrays. No hay atributos anidados.
{% endalert%}