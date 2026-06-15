---
nav_title: Captar usuarios inactivos
article_title: Captar usuarios inactivos
page_order: 1
page_type: tutorial
description: "Este artículo práctico aborda el problema de los usuarios inactivos y cómo utilizar eficazmente las campañas de Braze para reactivar la interacción con esos usuarios."
tool:
  - Segments
  - Campaigns

---

# Captar usuarios inactivos

> Si tu audiencia está disminuyendo, es fundamental intentar recuperarla. Con Braze, puedes configurar campañas automatizadas y recurrentes de reactivación de la interacción para captar usuarios inactivos. Puedes elegir el periodo de reactivación y la recurrencia que mejor se adapten a tu aplicación, pero a modo de ejemplo, empezaremos con un plan de reactivación de 14 días.

Para más información sobre cómo segmentar usuarios, consulta nuestro [curso de Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuración de campañas.

## Paso 1: Segmentar usuarios

Primero, crearemos un segmento para dirigirnos a los usuarios que no han utilizado tu aplicación en las últimas dos semanas, usando los siguientes filtros:

- **Última vez que usó la aplicación** hace más de 2 semanas
- **Última vez que usó la aplicación** hace menos de 3 semanas

![]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

Ponle al segmento un nombre fácil de recordar, como "Usuarios inactivos – 2 semanas". Como vamos a configurar la campaña para que se repita semanalmente, queremos asegurarnos de que haya al menos una semana de usuarios captados en el segmento. Por eso hemos seleccionado usuarios que usaron la aplicación por última vez entre dos y tres semanas atrás.

## Paso 2: Crear una campaña

A continuación, haz clic en **Crear campaña** y elige el tipo de campaña que enviaremos a este segmento. En este ejemplo, crearemos una nueva [campaña push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/).

![]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

Nombraremos la campaña "Mensaje a usuarios inactivos - 2 semanas" y luego crearemos el contenido de nuestro mensaje. En este ejemplo, solo nos dirigiremos a usuarios de iOS, pero puedes usar Braze para notificaciones push tanto en Android como en iOS.

Cuanto más reciente sea la última vez que un usuario estuvo en la aplicación, más importante es que el contenido sea oportuno y relevante. Al enviar un mensaje a un usuario después de dos semanas sin usar la aplicación, es importante mostrar contenido relevante y destacar los beneficios de usar la aplicación.

![]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

A continuación, crearemos una planificación recurrente para enviar nuestro mensaje semanal los jueves a las 5:45 pm usando la [entrega en zona horaria local]({{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer) en **Opciones de planificación por tiempo**. Te recomendamos que revises tu gráfico de sesiones para dirigirte a los usuarios justo antes de los periodos de mayor uso. Esto asegura que intentes reactivar la interacción con las personas cuando es más probable que usen la aplicación. Puedes cambiar esto más adelante y probar tu hipótesis inicial.

![]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## Paso 3: Lanzar la campaña

Ahora estás listo para enviar la campaña. Confirma la configuración en la última página del compositor y haz clic en **Lanzar campaña**.