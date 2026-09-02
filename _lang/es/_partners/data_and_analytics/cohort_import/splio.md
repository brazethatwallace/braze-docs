---
nav_title: Splio
article_title: Splio
alias: /partners/splio/
description: "Este artículo de referencia describe la asociación entre Braze y Splio, que te permite enviar campañas más específicas, encontrar nuevas oportunidades de productos y aumentar los ingresos."
page_type: partner
search_tag: Partner

---

# Splio

> [Splio](https://splio.com/) es una herramienta de creación de audiencias que te permite aumentar el número de campañas y los ingresos sin perjudicar la experiencia del cliente, y proporciona análisis para hacer un seguimiento del rendimiento de las campañas de CRM or administración de las relaciones con el cliente tanto online como offline.

La integración de Braze y Splio te permite planificar y ejecutar mejores estrategias de CRM or administración de las relaciones con el cliente, enviar campañas más específicas, encontrar nuevas oportunidades de productos y aumentar los ingresos.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta Splio | Necesitas una cuenta Splio para esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración de importación de datos {#data-import-integration}

Para integrar Braze y Splio, debes configurar la plataforma Splio, exportar una campaña Splio existente y crear un segmento de cohorte en Braze para dirigirte a los usuarios en futuras campañas.

### Paso 1: Obtener la clave de importación de datos de Braze {#step-1-get-the-braze-data-import-key}

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Splio**.

Encuentra tu punto de conexión REST y genera tu clave de importación de datos de Braze. Después de generar la clave, puedes crear una nueva clave o invalidar una existente.<br><br>![La página del socio tecnológico Splio con el punto de conexión REST y la clave de importación de datos.]({% image_buster /assets/img/tinyclues/tinyclues_6.png %}){: style="max-width:90%;"}

Para completar la integración, proporciona la clave de importación de datos y el punto de conexión REST or transferencia de estado representacional a tu equipo de operaciones de datos de Splio. Splio establece la conexión y se pone en contacto contigo una vez finalizada la configuración.

### Paso 2: Exportar una campaña desde la plataforma Splio {#step-2-export-a-campaign-from-the-splio-platform}

Cada vez que quieras crear una cohorte de usuarios de Splio en Braze, primero debes exportarla desde la plataforma Splio.

En Splio, selecciona las campañas que quieras exportar y haz clic en **Export Campaigns**. Después de exportar, la audiencia se carga automáticamente en tu cuenta de Braze.

![Exportar campañas desde la plataforma Splio.]({% image_buster /assets/img/tinyclues/tinyclues_1.png %})

### Paso 3: Crear un segmento a partir de la audiencia personalizada de Splio {#step-3-create-a-segment-from-the-splio-custom-audience}

En Braze, ve a **Segments**, asigna un nombre a tu segmento de cohorte Splio y selecciona **Splio Cohorts** como filtro. Desde aquí, elige qué cohorte de Splio quieres incluir. Después de crear tu segmento de cohorte Splio, puedes seleccionarlo como filtro de audiencia al crear una campaña o Canvas.

![Crear un segmento de cohorte Splio en Braze.]({% image_buster /assets/img/tinyclues/tinyclues_3.png %}){: style="max-width:90%;"}<br><br>
![En el constructor de segmentos de Braze, el filtro de atributos de usuario "Splio cohort" se establece en "includes" y "Primary cohort".]({% image_buster /assets/img/tinyclues/tinyclues_4.png %}){: style="max-width:90%;"}

¿Tienes problemas para localizar tu cohorte? Consulta la sección de [solución de problemas](#troubleshooting) para orientarte.

{% alert important %}
Solo se añaden o eliminan de una cohorte los usuarios que ya existen en Braze. La importación de cohortes no crea nuevos usuarios en Braze.
{% endalert %}

## Uso de esta integración {#using-this-integration}

Para utilizar tu segmento Splio, crea una campaña en Braze o un Canvas y selecciona el segmento como tu audiencia objetivo.

![En el constructor de campañas de Braze, en el paso de segmentación, el filtro "Selecciona a usuarios por segmento" está configurado como "Splio cohort".]({% image_buster /assets/img/tinyclues/tinyclues_5.png %}){: style="max-width:90%;"}

## Coincidencia de usuarios {#user-matching}

Braze empareja a los usuarios identificados por su `external_id` o `alias`. Los usuarios anónimos se emparejan por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden emparejarse por su `device_id`, y deben emparejarse por su `external_id` o `alias`.

## Solución de problemas {#troubleshooting}

Si no encuentras la cohorte correcta en la lista, consulta los detalles de tu campaña en Splio y verifica el nombre comprobando el **Export File Name**.

![La parte inferior de la página de detalles de la campaña muestra el nombre de tu cohorte.]({% image_buster /assets/img/tinyclues/tinyclues_2.png %}){: style="max-width:30%;"}

Si tienes problemas para recuperar tu audiencia, ponte en contacto con el [equipo de Splio](mailto:support-team@splio.com) para obtener ayuda.