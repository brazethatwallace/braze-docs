---
nav_title: Simon AI
article_title: Simon AI
description: "Usa la integración de Braze y Simon AI para crear y sincronizar audiencias sofisticadas con Braze para orquestación, en tiempo real y sin código."
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Simon AI

> La plataforma de marketing agéntico [Simon AI][1] ayuda a los equipos de marketing a lograr una verdadera personalización uno a uno. Combina un CDP componible con agentes de IA que operan directamente en Snowflake AI Data Cloud para actuar como el equipo de datos y ejecución de un especialista en marketing.

Usa la integración de Braze y Simon AI para crear y sincronizar audiencias avanzadas con Braze para orquestación en tiempo real y sin código. Con esta integración, puedes aprovechar la resolución de identidades, la unificación de datos de clientes y la segmentación impulsada por IA de Simon AI para potenciar campañas de Braze más personalizadas e impactantes.

## Requisitos previos {#prerequisites}

Para empezar, necesitas autenticar tu cuenta de Braze dentro de tu cuenta de Simon AI.

| Requisito | Descripción |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simon AI | Debes tener una cuenta de Simon AI existente para aprovechar la integración de Braze desde Simon AI. |
| Clave de API REST de Braze | Una clave de API REST de Braze con los permisos `users.track`, `campaigns.trigger.schedule.create` y `campaigns.trigger.send`. <br><br> Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| URL del panel de Braze | [Tu URL de endpoint REST][3]. Tu endpoint dependerá de la URL de Braze para tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Ejemplos {#use-cases}

- Desencadenar un Canvas o correo electrónico de Braze
- Pasar y mantener propiedades de Segment
- Sincronizar rasgos y propiedades de contacto

{% alert note %}
Al usar la integración de Simon y Braze, Simon solo envía deltas en cada sincronización a Braze, evitando costos por datos irrelevantes. Consulta [Sincronizar rasgos y propiedades de contacto](#sync-traits-and-contact-properties) para más información.
{% endalert %}

## Integración {#integration}

### Autenticar tu cuenta de Braze en Simon AI {#authenticate-your-braze-account-in-simon-ai}

Para usar la integración de Braze, primero autentica tu cuenta de Braze en Simon:

1. Desde el menú de navegación, haz clic en **Integrations** y luego desplázate hasta Braze.
2. Introduce tu [clave de API REST][2] de Braze y tu [URL del panel][3].
3. Haz clic en **Save Changes**.

Una conexión exitosa muestra **Connected** en la ventana.

![Pantalla de integración en Simon AI][8]{: style="max-width:70%"}

### Añadir acciones de Braze a Flows o Journeys en Simon AI {#add-braze-actions-to-flows-or-journeys-in-simon-ai}

Después de autenticar tu cuenta de Braze en Simon AI, puedes añadir acciones de Braze a [Flows][4] y [Journeys][5].

Hay tres acciones disponibles:

- **Sync Simon segment attribute**: sincroniza los detalles de tu segmento con un atributo personalizado nuevo o existente en Braze.
- **Trigger a Braze Canvas**: desencadena un Canvas de Braze que aproveche los datos de tu segmento de Simon.
- **Send a Braze campaign**: lanza una Campaign completa de Braze desde Simon.

![Menú desplegable que muestra la lista de acciones de Braze disponibles en Simon AI.][9]{: style="max-width:60%"}

Algunas acciones solo están disponibles para tipos específicos de Flow o solo para Journeys. Obtén más información en [docs.simondata.com][6].

### Sincronizar rasgos y propiedades de contacto {#sync-traits-and-contact-properties}

Para minimizar el consumo de datos, puedes elegir rasgos específicos para sincronizar de forma predeterminada, en lugar de actualizar todos los campos para todos los clientes en un segmento.

{% alert note %}
Para empezar con la sincronización de rasgos, envía una solicitud en el [Centro de soporte de Simon](https://docs.simondata.com/docs/support-center). Tu director de cuentas te avisará cuando puedas continuar con los siguientes pasos.
{% endalert %}

Después de que tu director de cuentas active los rasgos de contacto:

1. En Simon, expande **Admin Center** en la navegación izquierda y selecciona **Sync Contact Traits**.
2. Elige **Braze**. Las propiedades de contacto se muestran aquí, anidadas por conjunto de datos.
3. Selecciona los campos que deseas sincronizar cuando uses la integración de Simon y Braze:
   1. **Number of traits** indica cuántos rasgos están disponibles para elegir en ese conjunto de datos. Puedes elegir todos o expandir la fila para seleccionar campos individuales.
   2. Edita el **Downstream name** si deseas que los nombres de los campos aparezcan de forma diferente cuando lleguen a Braze.
   3. Si es la primera vez que integras con Braze desde Simon, haz clic en **Backfill all contacts**. El relleno retroactivo envía todos los puntos de datos a Braze la primera vez que usas una acción en un flow o journey para asegurarte de que todos tus datos estén completamente sincronizados. Luego, en las sincronizaciones posteriores, solo los rasgos que elijas en esta pantalla se envían a Braze. Esto ayuda a asegurarte de que solo se te cobre por los datos que necesitas.

![Selección de rasgos de sincronización en Simon AI.][10]

[1]: https://www.simon.ai/
[2]: {{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys
[3]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
[4]: https://docs.simondata.com/docs/campaigns-flows
[5]: https://docs.simondata.com/docs/campaigns-journeys-two
[6]: https://docs.simondata.com
[7]: https://docs.simondata.com/docs/support-center
[8]: {% image_buster /assets/img/simon_data/ConnecttoBraze.png %}
[9]: {% image_buster /assets/img/simon_data/BrazeActions.png %}
[10]: {% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %}