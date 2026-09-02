---
nav_title: Retención de datos
article_title: "Información sobre la retención de datos de Braze"
alias: /data_retention/
description: "Este artículo de referencia cubre la información general sobre retención de datos de Braze."
page_type: reference
page_order: 2.5
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Información sobre la retención de datos de Braze {#braze-data-retention-information}

*Última revisión el 1 de abril de 2024*

> Este artículo cubre la información general sobre retención de datos de Braze.<br><br>Los datos almacenados en Braze se conservan y pueden utilizarse para segmentación, personalización y orientación durante toda la vida de la cuenta del cliente. Esto significa que datos como atributos de perfil de usuario, atributos personalizados, eventos personalizados y compras se almacenan indefinidamente para los usuarios activos, a menos que el cliente los elimine, durante la vigencia del contrato.<br><br>Braze cuenta con características, procesos y API para implementar automáticamente buenas prácticas de higiene de datos orientadas al cumplimiento del RGPD y otras buenas prácticas. Las siguientes secciones describen cómo se gestiona la retención de datos.

## Retención de datos gestionada por los clientes a través del panel o la API de Braze {#data-retention-handled-by-customers-through-brazes-dashboard-or-api}

Braze permite a sus clientes eliminar perfiles de usuario completos y datos de atributos de su espacio de trabajo.

Esto significa que puedes:
- Eliminar perfiles de usuario utilizando el [endpoint de la API de eliminación de usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) de Braze
- Eliminar (anular) o modificar atributos en perfiles de usuario utilizando el [endpoint de la API de seguimiento de usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track) de Braze

Los eventos de comportamiento no se pueden eliminar de un perfil de usuario (eventos personalizados, sesiones, Campaigns, compras). Para eliminar esos eventos, debes eliminar el perfil de usuario completo.

Para cumplir con la normativa de privacidad, es posible que necesites eliminar todos los datos personales relativos a un usuario a petición de este. Puedes encontrar instrucciones en nuestra página de [asistencia técnica de protección de datos]({{site.baseurl}}/help/dp-technical-assistance#the-right-to-erasure).

{% alert note %}
Un usuario puede tener varios perfiles, y es posible que necesites eliminar varios perfiles para eliminar todos los datos relativos a un mismo usuario. Sigue las instrucciones en la página de asistencia técnica de protección de datos sobre cómo eliminar completamente todos los datos de un usuario.
{% endalert %}

## Retención de datos gestionada por Braze para características específicas de los servicios de Braze {#data-retention-handled-by-braze-for-specific-features-of-the-braze-services}

### Base de datos de Braze: archivado/eliminación automática de usuarios perdidos {#braze-database-automatic-archivingdeletion-of-churned-users}

Cada semana, Braze ejecuta un proceso para eliminar a los usuarios inactivos y los usuarios perdidos de los servicios de Braze. En general, se trata de usuarios a los que no se puede contactar (por ejemplo, no tienen dirección de correo electrónico, ni número de teléfono, ni token de notificaciones push, no utilizan tus aplicaciones ni visitan tus sitios web), no tienen actividad registrada en su perfil de usuario, y no han recibido mensajes ni se ha interactuado con ellos a través de Braze. Esto se hace para cumplir con los principios y las mejores prácticas del RGPD. Puedes obtener más información sobre este proceso en nuestra página de <a href="/docs/user_archival">definiciones de archivado de usuarios</a>.

{% alert note %}
Los clientes tienen control total sobre si un usuario es inactivo o perdido, y pueden evitar el archivado de perfiles de usuario registrando un punto de datos a intervalos regulares. Braze Canvas ofrece la posibilidad de hacer esto de forma automática, lo que te permite desactivar eficazmente esta funcionalidad para algunos o todos tus usuarios inactivos o perdidos.
{% endalert %}

### Datos de interacción de Campaigns y Canvas {#campaign-and-canvas-interactions-data}

Los datos de interacción de mensajería se refieren a cómo un usuario interactúa con una Campaign o un Canvas que recibió (por ejemplo, cuando un usuario abre la Campaign A o un usuario recibe la variante A). Estos datos se utilizan para reorientar. Puedes obtener más información sobre la disponibilidad de los datos de interacción de mensajería en [Acerca de la disponibilidad de los datos de interacción de mensajería]({{site.baseurl}}/messaging_interaction_data).

## Retención de datos gestionada por Braze {#data-retention-handled-by-braze}

Las siguientes políticas de retención corresponden al cumplimiento por parte de Braze del RGPD y las normativas de privacidad, y se refieren al almacenamiento transitorio de datos a medida que pasan por nuestros sistemas internos. Estas políticas de retención no afectan a los servicios de Braze y son informativas para tus equipos legales y de privacidad.

### Servidores de Braze: retención a corto plazo con fines de recuperación {#braze-servers-short-term-retention-for-recovery-purposes}

Los datos enviados por Braze a determinados subencargados del tratamiento pueden permanecer en los sistemas internos de Braze hasta 90 días.

### Retención de datos del Data Lake de Braze {#braze-data-lake-data-retention}

Los datos disponibles para los clientes en el panel de Braze son en su mayoría agregados. Los registros detallados se guardan en una base de datos independiente creada por Braze (el "Data Lake"). Los datos del Data Lake se utilizan para informes agregados y otras funcionalidades avanzadas. Braze elimina la información de identificación personal de los datos de eventos almacenados en el Data Lake después de dos años (consulta más información en nuestra página de [retención de datos de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_retention)).

Si utilizas nuestras API para eliminar perfiles de usuario o para eliminar o modificar atributos de los perfiles de usuario, pueden pasar hasta tres semanas para que esos datos se eliminen del Data Lake de Braze. La eliminación de datos en el Data Lake no afecta a la segmentación ni a la personalización, sino que garantiza que los datos se eliminan de todos los sistemas de Braze.

### Servidores de respaldo de Braze {#braze-backup-servers}

Cuando se eliminan datos de tu instancia de producción, los datos permanecen en los servidores de respaldo de Braze durante seis meses y luego se eliminan de acuerdo con nuestros procesos internos.