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

# Captar usuarios inactivos {#capture-lapsing-users}

> Si tu audiencia está disminuyendo, es fundamental intentar recuperarla. Con Braze, puedes configurar campañas automatizadas y recurrentes de reactivación de la interacción para captar usuarios inactivos. Puedes elegir el periodo de reactivación y la recurrencia que mejor se adapten a tu aplicación, pero a modo de ejemplo, empezaremos con un plan de reactivación de 14 días.

Para más información sobre cómo segmentar usuarios, consulta nuestro [curso de Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuración de campañas.

## Paso 1: Segmentar usuarios {#step-1-segment-users}

Primero, crearemos un Segment para dirigirnos a los usuarios que no han utilizado tu aplicación en las últimas dos semanas, usando los siguientes filtros:

- **Last Used App** hace más de 2 semanas
- **Last Used App** hace menos de 3 semanas

![Captura de pantalla relacionada con el paso 1: segmentar usuarios.]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

Asigna al Segment un nombre fácil de recordar, como "Lapsed Users – 2 Weeks". Como estamos configurando la Campaign para que se repita semanalmente, queremos asegurarnos de que haya al menos una semana de usuarios capturados en el Segment. Por eso hemos seleccionado usuarios que usaron la aplicación por última vez entre dos y tres semanas atrás.

## Paso 2: Crea una Campaign {#step-2-create-a-campaign}

A continuación, haz clic en **Create Campaign** y elige el tipo de Campaign que enviaremos a este Segment. En este ejemplo, crearemos una nueva [Campaign push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message).

![A continuación, haz clic en Create Campaign y elige el tipo de Campaign que enviaremos a este Segment. En este ejemplo, crearemos una nueva Campaign push.]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

Nombraremos la Campaign "Message to Lapsed Users - 2 Weeks" y luego crearemos el contenido de nuestro mensaje. En este ejemplo, solo nos dirigiremos a usuarios de iOS, pero puedes usar Braze para notificaciones push en Android e iOS.

Cuanto más cercano sea el último momento en que un usuario estuvo en la aplicación, más importante es ser oportuno y relevante. Al enviar un mensaje a un usuario después de dos semanas sin usar la aplicación, es importante mostrar contenido relevante y destacar los beneficios de usar la aplicación.

![Captura de pantalla relacionada con el paso 2: crea una Campaign.]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

A continuación, crearemos un horario recurrente para enviar nuestro mensaje semanal los jueves a las 5:45 p. m. usando la [entrega en zona horaria local]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer) en **Time-Based Scheduling Options**. Recomendamos que revises tu gráfico de sesiones para dirigirte a los usuarios justo antes de los períodos de mayor uso. Esto garantiza que intentes reactivar a las personas cuando es más probable que usen la aplicación. Puedes cambiar esto más adelante y probar tu hipótesis inicial.

![A continuación, crearemos un horario recurrente para enviar nuestro mensaje semanal los jueves a las 5:45 p. m. usando la entrega en zona horaria local en Time-Based Scheduling Options. Recomendamos que revises tu gráfico de sesiones para dirigirte a los usuarios justo antes de los períodos de mayor uso. Esto garantiza que intentes reactivar a las personas cuando es más probable que usen la aplicación. Puedes cambiar esto más adelante y probar tu hipótesis inicial.]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## Paso 3: Lanza la campaign {#step-3-launch-the-campaign}

Ahora estás listo para enviar la campaign. Confirma la configuración en la última página del creador y haz clic en **Launch Campaign**.