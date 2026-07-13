---
nav_title: Importación de cohortes de Heap
article_title: Importación de cohortes de Heap
description: "Este artículo de referencia detalla la integración entre Braze y Heap, una plataforma de información digital, que permite importar datos de Heap a Braze, crear cohortes de usuarios, así como exportar datos de Braze a Heap para crear segmentos."
alias: /partners/heap_cohort_import/
page_type: partner
search_tag: Partner

---

# Importación de cohortes de Heap {#heap-cohort-import}

> [Heap](https://heap.io/), una plataforma de información digital, te centra en las oportunidades de tu experiencia digital que más afectan a tu negocio, eliminando fricciones, deleitando a tus clientes y acelerando los ingresos.

La integración de Braze y Heap te permite [importar datos de Heap a Braze](#data-import-integration), crear cohortes de usuarios, así como [exportar datos de Braze a Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap) para crear segmentos.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Heap | Se necesita una cuenta de [Heap](https://heap.io/about) para aprovechar esta integración. |
| Clave de importación de datos de Braze | Se puede obtener en el panel de Braze desde **Integraciones de socios** > **Socios tecnológicos** y luego seleccionando **Heap**. |
| Endpoint REST de Braze | [La URL de tu endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Tu endpoint dependerá de la URL de Braze de tu instancia. |
| Braze Currents | Para exportar datos de Braze a Heap, necesitas que [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) esté habilitado en tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Ejemplos {#use-cases}

- Reactiva a los usuarios que han abandonado un embudo: desencadena mensajes de reactivación cuando los usuarios abandonan el embudo de compra o suscripción.
- Personaliza la experiencia de prueba: identifica los puntos de fricción en tu experiencia de prueba y envía recordatorios en el momento adecuado para volver a captar a los usuarios durante una prueba y ayudarles a obtener valor.
- Impulsa una mayor participación en anuncios y ofertas: dirige las promociones, actualizaciones y anuncios de nuevos servicios a las audiencias pertinentes.

## Integración de la importación de datos {#data-import-integration}

Utiliza la integración de Heap con Braze para sincronizar automáticamente las cohortes definidas en Heap con Braze.

### Paso 1: Obtener la clave de importación de datos de Braze {#step-1-get-the-braze-data-import-key}

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Heap**.

En esta página, puedes encontrar tu clave de importación de datos y un endpoint REST. Toma nota de estos dos valores y proporciónaselos a tu director de cuentas de Heap para terminar de configurar la integración.

![Página de partner tecnológico de Heap en Braze que muestra la clave de importación de datos y el endpoint.]({% image_buster /assets/img/heap/heap2.png %}){: style="max-width:90%;"}

### Paso 2: Segmentar usuarios importados en Braze {#step-2-segment-imported-users-in-braze}

En Braze, ve a **Segments**, asigna un nombre a tu segmento de cohortes de Heap y selecciona **Heap Cohorts** como filtro. Desde aquí, puedes elegir qué cohorte de Heap deseas incluir. Una vez creado tu segmento de cohorte de Heap, puedes seleccionarlo como filtro de audiencia al crear una Campaign o Canvas.

![En el creador de segmentos de Braze, el filtro de atributos de usuario "Heap cohort" se establece en "includes" y "Heap Test Cohort".]({% image_buster /assets/img/heap/heap1.png %}){: style="max-width:90%;"}

### Uso de esta integración {#using-this-integration}

Para utilizar tu segmento de Heap, crea una Campaign o Canvas en Braze y selecciona el segmento como tu público objetivo.

![En el constructor de Campaign de Braze, en el paso de segmentación, el filtro "Selecciona a usuarios por segmento" está establecido en "Heap cohort".]({% image_buster /assets/img/heap/heap3.png %}){: style="max-width:90%;"}

{% alert important %}
Solo se añadirán o eliminarán de una cohorte los usuarios que ya existan en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

## Detalles de la integración {#integration-details}

La estructura de la carga útil de los datos exportados es la misma que la de los conectores HTTP personalizados, que puede consultarse en el [repositorio de ejemplos de conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).

## Coincidencia de usuarios {#user-matching}

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden coincidir por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.