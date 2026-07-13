---
nav_title: Seen
article_title: Seen
description: "Seen habilita experiencias de video personalizadas a escala, ayudando a las marcas a impulsar una mayor interacción a lo largo del recorrido del cliente."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# Seen

> [Seen](https://seen.io) habilita a las marcas para crear y entregar experiencias de video personalizadas a escala. Con Seen, puedes diseñar un video en torno a tus datos, personalizarlo a escala en la nube y luego distribuirlo donde mejor funcione.
>
> Esta integración envía datos de usuario de Braze a Seen, genera videos personalizados y devuelve activos —como una URL de reproductor única y una miniatura— a Braze para su uso en Campaigns y Canvas.


## Casos de uso {#use-cases}

Seen admite la entrega automatizada y personalizada de video a lo largo del ciclo de vida del cliente, incluyendo:

- **Incorporación**: Da la bienvenida a nuevos usuarios con videos personalizados según su perfil o contexto de registro
- **Conversión y activación**: Refuerza las acciones clave con mensajería de video contextual
- **Fidelización y upsell**: Destaca ofertas personalizadas o hitos de uso
- **Recuperación y prevención del abandono**: Reactiva la interacción de los usuarios inactivos con contenido de video a medida


## Requisitos previos {#prerequisites}

Antes de empezar, asegúrate de que tienes el acceso y los datos de la siguiente tabla.

| Requisito | Descripción |
|--------------|-------------|
| Acceso a la plataforma Seen | Necesitas una suscripción a la plataforma Seen con un proyecto publicado, o una campaña de Seen activa. También necesitas acceso a tu proyecto para recuperar el punto de conexión del proyecto y generar un token de API. |
| URL de webhook de Transformación de datos de Braze | Utiliza la Transformación de datos de Braze para reformatear los datos entrantes de Seen de modo que puedan ser aceptados por el [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze. |
| Datos de usuario de Braze | La personalización del video requiere datos a nivel de usuario. Asegúrate de que los atributos pertinentes están disponibles en Braze y de que pasas **`braze_id`** como identificador único. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }




## Cómo funcionan los proyectos de Seen {#how-seen-projects-work}

Seen utiliza la pestaña [Run](https://docs.seen.io/run) de un proyecto para controlar cómo se procesan los datos entrantes y cómo se generan las salidas de video.

Un flujo de trabajo de proyecto:

- Recibe datos de sistemas externos (como Braze)
- Aplica reglas lógicas y de personalización
- Genera un video y activos asociados
- Devuelve una carga útil de respuesta configurable

La pestaña Run incluye lo siguiente:

- **Create via API**: Abre los detalles de la API del proyecto.
- **Import CSV**: Importa datos de personalización manualmente (no se utiliza en este tutorial).
- **Add webhook**: Define la carga útil de respuesta enviada de vuelta a Braze.
- **View videos**: Muestra los videos generados y el estado de los datos entrantes.

Las respuestas de los webhooks son configurables, así que alinea los campos de salida que devuelve Seen con los atributos que espera tu Transformación de datos de Braze.


## Límite de velocidad {#rate-limit}

La API de Seen acepta 100 llamadas cada 10 segundos.


## Integración {#integration}

En este ejemplo, Braze envía datos de usuario a Seen para generar un video personalizado. A continuación, Seen devuelve una URL de reproductor de video y una URL de miniatura únicas, que se almacenan como [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) en Braze para su uso en [mensajería]({{site.baseurl}}/user_guide/messaging/).

Si tienes varias campañas de video con Seen, repite este proceso para cada campaña.

### Paso 1: Crea una Campaign de webhook para enviar datos a Seen {#step-1-create-a-webhook-campaign-to-send-data-to-seen}

Crea una nueva [Campaign de webhook]({{site.baseurl}}/user_guide/channels/webhooks/) en Braze.

Configura el webhook como se indica a continuación:

- **URL del webhook**:
  `https://next.seen.io/v1/projects/{PROJECT_ID}/data`
  Busca el punto de conexión de tu proyecto en la pestaña Run de tu proyecto en la plataforma Seen.

- **Método HTTP**: POST

- **Cuerpo de la solicitud**: Raw Text
  Utiliza el siguiente ejemplo como punto de partida. Para opciones de campos y límites, consulta [la documentación de creación de datos de Seen](https://docs.seen.io/create-data).

{% raw %}
```json
{
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "id": "{{${braze_id}}}"
}
```
{% endraw %}

- **Encabezados de solicitud**:
  - `Authorization`: Bearer `{Seen_API_TOKEN}`
  - `Content-Type`: `application/json`

  Genera un [token de API](https://docs.seen.io/authorization) en la pestaña Run de tu proyecto en la plataforma Seen. Ponte en contacto con tu administrador del éxito del cliente de Seen si necesitas ayuda.

- Prueba el webhook con un usuario en la pestaña **Test**.
- Tras una prueba exitosa, completa la configuración del webhook.


### Paso 2: Configura un proyecto en la plataforma Seen {#step-2-configure-a-project-in-the-seen-platform}

En tu proyecto de Seen, utiliza la pestaña [Run](https://docs.seen.io/run) para publicar tu video y registrar el webhook de salida. Para una descripción general de la pestaña Run, consulta [Cómo funcionan los proyectos de Seen](#how-seen-projects-work).

1. En la plataforma Seen, crea un proyecto, construye tu video y selecciona **Publish**. Los videos comienzan a generarse a partir de los datos entrantes en cuanto se publica el proyecto.
2. En la pestaña Run, selecciona **Add a webhook**.

#### Requisitos de respuesta del webhook {#webhook-response-requirements}

La carga útil de la respuesta es configurable. Devuelve los campos de la siguiente tabla para que la Transformación de datos de Braze del paso siguiente pueda mapearlos.

| Campo | Descripción |
|-------|-------------|
| `id` | Debe coincidir con el `braze_id` enviado desde Braze |
| `player_url` | URL única para el reproductor de video personalizado |
| `email_thumbnail_url` | URL de la miniatura de video personalizada |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos de respuesta del webhook" }

Si necesitas atributos adicionales, añádelos a la respuesta y mapéalos en Braze.


### Paso 3: Crea una Transformación de datos para recibir datos de Seen {#step-3-create-a-data-transformation-to-receive-data-from-seen}

Utiliza las Transformaciones de datos de Braze para procesar la respuesta de Seen y almacenar los activos de video en el perfil de usuario.

1. Crea los siguientes [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) en Braze:
   - `player_url`
   - `email_thumbnail_url`

2. Ve a **Configuración de datos** > **Transformaciones de datos** y selecciona **Crear transformación**.

3. Configura la transformación:
   - **Empezar desde cero**
   - **Destino** > POST: Track users

4. Comparte la URL del webhook generado con Seen, o añádela al **Webhook** en la pestaña Run de tu proyecto.

5. Utiliza el siguiente código de transformación:

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.id,
      "_update_existing_only": true,
      "player_url": payload.player_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```

{: start="6"}
6. Envía una carga útil de prueba al punto de conexión proporcionado. Puedes enviar datos a tu proyecto en la plataforma Seen (publica el proyecto primero), o enviar la carga útil directamente a Braze con [Postman](https://www.postman.com/) u otra herramienta similar.
7. Selecciona **Validar** para verificar que la transformación funciona según lo previsto.
8. Selecciona **Guardar** y **Activar**.