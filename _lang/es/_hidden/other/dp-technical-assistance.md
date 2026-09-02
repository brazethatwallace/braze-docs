---
nav_title: Asistencia técnica en materia de protección de datos
article_title: Asistencia técnica de protección de datos en los Servicios Braze
page_order: 1
description: "Esta página proporciona instrucciones técnicas para que puedas gestionar, a través de los Servicios Braze, las solicitudes de los individuos en relación con sus derechos sobre los datos personales."
alias: /help/dp-technical-assistance/
permalink: /dp-technical-assistance/
hide_toc: true
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Asistencia técnica de protección de datos en los Servicios Braze {#data-protection-technical-assistance-in-the-braze-services}

Existe una serie de leyes de protección de datos que regulan lo que las organizaciones pueden hacer con los datos personales ("Leyes de Protección de Datos"), entre ellas el Reglamento General de Protección de Datos de la UE y del Reino Unido ("RGPD"), la Ley de Privacidad del Consumidor de California ("CCPA") y la Ley de Portabilidad y Responsabilidad del Seguro Médico ("HIPAA"). Existen otras leyes y normativas de protección de datos nacionales, estatales y específicas del sector que pueden aplicarse a tu empresa.

Estas Leyes de Protección de Datos conceden a los individuos "derechos de privacidad" sobre sus datos personales. Las organizaciones están obligadas a recibir y responder a las solicitudes de los individuos que ejercen sus derechos de privacidad. Los Servicios Braze pueden ayudarte en el cumplimiento de estas Leyes de Protección de Datos proporcionando características para facilitar ciertas acciones requeridas por dichas leyes. Este documento proporciona instrucciones técnicas para utilizar estas características para gestionar las solicitudes de derechos de privacidad. Te corresponde a ti determinar qué Leyes de Protección de Datos se aplican a tu empresa y actuar de conformidad con ellas.

## Aviso legal {#legal-disclaimer}

Nada de lo que se indica a continuación pretende ser, ni debe interpretarse como, asesoramiento legal por parte de Braze. Te recomendamos buscar el consejo de tu propio asesor en relación con tu situación particular y la forma en que las leyes de protección de datos te aplican a ti y a tu uso de los servicios de Braze.

## Terminología {#terminology}

A los efectos de este documento, cualquier referencia a datos personales también puede entenderse como una referencia a información personal o información de identificación personal ("Datos Personales"). Por simplicidad, generalmente nos basamos en el lenguaje del RGPD al abordar los derechos de los usuarios finales. El lenguaje del RGPD suele ser intercambiable o estar estrechamente alineado con un término o concepto definido en otras leyes de protección de datos.

## Conceptos básicos {#the-basics}

La mayoría de las leyes de privacidad definen tres partes interesadas principales que participan en el tratamiento de datos personales: los interesados, los responsables del tratamiento y los encargados del tratamiento. Cada grupo tiene diferentes derechos y responsabilidades en relación con el uso de datos personales:

- Un interesado es una persona cuyos datos personales están siendo tratados por el encargado o el responsable del tratamiento
- Un responsable del tratamiento es una entidad que determina los fines y los medios del tratamiento de datos personales
- Un encargado del tratamiento es una entidad que trata datos personales en nombre y según las instrucciones del responsable del tratamiento

En relación con los servicios de Braze:

- Los interesados son, por ejemplo, los usuarios finales de tu aplicación para clientes (por ejemplo, tus clientes/consumidores) o tus empleados que son usuarios de la empresa en tu instancia de los servicios de Braze.
- Tú, el cliente de Braze, eres el responsable del tratamiento que decide cómo y por qué se recopilarán y tratarán los datos personales de los interesados dentro de los servicios de Braze.
- Braze es un encargado del tratamiento que trata datos personales en los servicios de Braze en tu nombre y de acuerdo con las instrucciones que recibimos de ti.

Los términos anteriores son del RGPD, pero por ejemplo, los términos comparables en la CCPA son:
- "consumidores" para los interesados.
- "empresas" para los responsables del tratamiento.
- "proveedores de servicios" para los encargados del tratamiento.

A continuación encontrarás información relevante sobre las solicitudes de derechos de privacidad más comunes de los interesados, incluyendo cómo puedes responder a ellas a través de las características técnicas de los servicios de Braze.

## El derecho a ser informado {#the-right-to-be-informed}

El derecho a ser informado abarca tu obligación de proporcionar "información sobre el tratamiento justo", normalmente a través de un aviso de privacidad. Hace hincapié en la necesidad de transparencia sobre cómo utilizas los datos personales.

### Recomendación de Braze {#braze-recommendation}

La mayoría de las leyes de protección de datos hacen hincapié en la necesidad de transparencia en relación con el uso que haces de los datos personales. Esta es responsabilidad de los responsables del tratamiento de datos, quienes normalmente mantienen un aviso de privacidad fácilmente accesible para los usuarios de sus productos y servicios, y que cubre el tratamiento realizado por Braze.

## El derecho de acceso {#the-right-of-access}

Según las leyes de protección de datos, los interesados pueden tener derecho a obtener:

- Confirmación de que sus datos personales están siendo tratados,
- Acceso a sus datos personales, y
- Otra información complementaria según lo determinado por la ley de protección de datos aplicable.

### Recomendación de Braze

Para proporcionar datos personales de Braze en un formato legible por máquina en respuesta a una solicitud de acceso de un interesado, puedes exportar su perfil de usuario final realizando una llamada a la API a las [REST API]({{site.baseurl}}/api/endpoints/export) de Braze con su identificador de usuario (definido por ti como el `external_id` proporcionado a Braze) y/o su identificador de dispositivo.

#### BrazeAI Decisioning Studio™

Para atender una solicitud del derecho de acceso en relación con datos personales en BrazeAI Decisioning Studio™, contacta a tu director de cuentas con los customer_id y/o correos electrónicos correspondientes.

## El derecho de rectificación {#the-right-to-rectification}

Las personas tienen derecho a que sus datos personales se corrijan si son inexactos o están incompletos. Si has divulgado los datos personales en cuestión a terceros, puedes considerar la necesidad de informarles de la rectificación cuando sea posible.

### Recomendación de Braze

En caso de que un interesado te solicite rectificar inexactitudes en los datos personales que estés tratando tú o Braze en tu nombre, puedes utilizar los SDK de Braze o las [REST API]({{site.baseurl}}/api/endpoints/user_data/post_user_track) de Braze para corregir dichos datos personales.

## El derecho de supresión {#the-right-to-erasure}

El derecho de supresión también se conoce como "el derecho al olvido" o "derecho a ser eliminado".

### Recomendación de Braze

#### Eliminación estándar {#standard-deletion}

Una vez que hayas detenido la recopilación de datos, puedes utilizar el [endpoint de la REST API de eliminación de usuarios de Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) para eliminar a un usuario final, lo que eliminará todos los registros de dicho usuario final de los servicios de Braze:

- Para los usuarios finales que tienen un external_id dentro de los servicios de Braze, puedes utilizar ese ID para eliminar los datos de dicho usuario final.
- Para los usuarios finales anónimos que no tienen un external_id dentro de los servicios de Braze, puedes recuperar el identificador de dispositivo de ese usuario final utilizando el SDK de Braze y puedes utilizar el identificador de dispositivo para encontrar el perfil de usuario final asociado a ese dispositivo. A continuación, puedes utilizar la API de eliminación de usuarios para eliminar el perfil asociado a ese usuario final.

Eliminar a un usuario final de los servicios de Braze eliminará permanentemente el perfil de usuario centralizado de Braze para ese usuario final, según lo definido por el `external_id` proporcionado. Esto incluye la información de perfil estructurada que Braze recopiló de forma predeterminada o que configuraste para que los servicios de Braze recopilaran, como la información del dispositivo, el país, el idioma y la dirección de correo electrónico.

Ten en cuenta que la dirección de correo electrónico o el número de teléfono asociados al perfil del usuario final podrían seguir almacenados por Braze, ya que podrían estar asociados al perfil de otro usuario final. Las direcciones de correo electrónico y los números de teléfono no son únicos en los servicios de Braze. Esto significa que tu equipo podría haber configurado Braze para almacenar la misma dirección de correo electrónico o número de teléfono en múltiples perfiles de usuario. Si tu equipo ha configurado Braze de esta manera, ten en cuenta que puede que necesites eliminar todos los perfiles de usuario que representan a un determinado titular de datos para cumplir con una solicitud de eliminación de un titular de datos, y tu equipo tendría que realizar múltiples llamadas a la API para eliminar todos los perfiles de usuario que hacen referencia a un titular de datos en particular.

#### BrazeAI Decisioning Studio™

Para cumplir con una solicitud de derecho de supresión en relación con datos personales en BrazeAI Decisioning Studio™, contacta a tu director de cuentas con los customer_id y/o correos electrónicos correspondientes. Tu director de cuentas puede gestionar la eliminación de todos los datos personales asociados que se encuentren en el almacén de datos.

#### Consideraciones adicionales sobre la eliminación {#additional-deletion-considerations}

<style>
#considerations td {
    word-break: break-word;
    width: 100%;
    font-size: 16px;
}
</style>

<table id="considerations">
  <caption>Consideraciones adicionales sobre la eliminación</caption>
<tbody>
  <tr>
    <td>
        <p>Los clientes pueden crear campos personalizados para propiedades del evento y extras de mensaje. Estos campos no están destinados a datos personales, por lo que no se incluyen en el proceso de eliminación predeterminado descrito anteriormente. Sin embargo, si utilizas Braze para ingresar o recopilar datos personales a través de propiedades del evento y extras de mensaje, puedes configurar el proceso de eliminación activado por el endpoint de la REST API de eliminación de usuarios para que también incluya estos campos, de modo que los datos contenidos en estos campos también se eliminen.</p>
        <p>La configuración predeterminada se aplica a nivel de empresa, pero puedes optar por eliminar los siguientes campos cuando se ejecute el proceso de eliminación, a nivel de grupo de aplicaciones/espacio de trabajo:</p>
    <ul>
        <li>PROPERTIES para USERS_BEHAVIORS_CUSTOMEVENT</li>
        <li>PROPERTIES para USERS_BEHAVIORS_PURCHASE</li>
        <li>MESSAGE_EXTRAS para:
            <ul>
            <li>USERS_MESSAGES_CONTENTCARD</li>
            <li>USERS_MESSAGES_EMAIL_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_RETRYSEND_SHARED</li>
            <li>USERS_MESSAGES_WEBHOOK_SEND</li>
            <li>USERS_MESSAGES_SMS_SEND</li>
            <li>Futuros eventos de envío de mensajes</li>
            </ul>
        </li>
    </ul>
    <p>La configuración para esto se puede acceder a través de <b>Configuración de la empresa</b> > <b>Configuración de administrador</b> > <b>Configuración de seguridad</b>. Las preferencias de eliminación de datos se establecen por tipo de evento o categoría. Solo un usuario con permisos de administrador puede realizar cambios en esta configuración. Alternativamente, un administrador puede delegar estos permisos a otro usuario.</p>
    <p>Si un tipo de evento o extra de mensaje se configura para incluirse en el proceso de eliminación, los datos de este campo se eliminarán en adelante para los usuarios para los que estés ejecutando el endpoint de la REST API de eliminación de usuarios. Además, cuando selecciones esta preferencia de eliminación, en el siguiente trabajo de eliminación programado, los datos de estos campos se eliminarán de cualquier conjunto de datos anonimizado existente que contenga estos campos. No será posible restaurar los campos de datos eliminados.</p>
    </td>
  </tr>
</tbody>
</table>

#### Análisis {#analytics}

Para mantener la integridad de los análisis de uso de Campaigns y aplicaciones, los datos agregados anónimos no se modificarán cuando se elimine un usuario final. Por ejemplo, Braze no reducirá el número total de sesiones de una aplicación cuando se elimine un usuario final. Las sesiones en las que dicho usuario final visitó la aplicación seguirán incluidas en el número total de visitas a esa aplicación, pero esos datos no estarán conectados de ninguna manera al perfil del usuario final olvidado, lo que garantiza que estos datos anonimizados y agregados no puedan vincularse a un usuario final individual.

Los análisis dentro de los servicios de Braze están vinculados al identificador de usuario final de Braze. Después de que se haya eliminado el perfil del usuario final, el identificador de usuario de Braze se convierte efectivamente en un identificador completamente anonimizado, ya que Braze no puede vincularlo de nuevo a ningún usuario final individual.

#### Una vez que se ha realizado la eliminación {#once-deletion-has-happened}

En general, se espera que hagas esfuerzos razonables para notificar a los titulares de datos cuando hayas cumplido con su solicitud de suprimir sus datos personales. Un usuario final eliminado puede volver a registrarse o interactuar nuevamente con tu aplicación o servicio en una fecha posterior, y Braze no podrá identificarlo como el usuario eliminado u olvidado. Los servicios de Braze no pueden crear listas de identificadores de usuarios eliminados o direcciones de correo electrónico en tu nombre.

## El derecho a la restricción del tratamiento {#the-right-to-restriction-of-processing}

Los interesados pueden tener derecho a "bloquear" o suprimir el tratamiento de sus datos personales en determinadas circunstancias. Restringir el tratamiento significa no llevar a cabo ningún tratamiento al que un interesado se haya opuesto.

### Recomendación de Braze

Los servicios de Braze no admiten la restricción del tratamiento de categorías individuales de datos personales. Si un interesado te ha solicitado restringir el tratamiento de determinados subconjuntos de sus datos personales, debes utilizar las [API de Braze]({{site.baseurl}}/api/home) para exportar el perfil o perfiles completos de ese usuario final y luego [eliminarlo]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) de Braze. Las API de Braze se pueden utilizar para volver a importar estos datos en caso de que el usuario final te permita posteriormente tratar esos subconjuntos específicos de sus datos personales. Además, debes recomendar a tu usuario final que desinstale o cierre sesión en todas y cada una de tus aplicaciones que utilicen el SDK de Braze para dejar de recopilar cualquier dato adicional sobre el interesado.

Para los clientes que solo utilizan BrazeAI Decisioning Studio™, ya no debes enviar datos a Decisioning Studio.

## El derecho a la portabilidad de los datos {#the-right-to-data-portability}

El derecho a la portabilidad de los datos permite a los interesados obtener y reutilizar sus datos personales para sus propios fines en diferentes servicios. Los datos personales deben proporcionarse en un formato que sea estructurado, legible por máquina y de uso común.

### Recomendación de Braze

De forma similar al derecho de acceso, puedes usar la [REST API]({{site.baseurl}}/api/endpoints/export) de Braze para exportar los datos personales de un usuario final y proporcionárselos al interesado conforme a su solicitud. Además, habla con tu director de cuentas con los `customer_id`(s) y/o correo(s) electrónico(s) pertinentes para solicitar una copia de cualquier dato personal almacenado en BrazeAI Decisioning Studio.

## El derecho de oposición {#the-right-to-object}

Las personas pueden tener derecho a oponerse a:

- el tratamiento basado en intereses legítimos o en la realización de una tarea de interés público/ejercicio de autoridad oficial (incluida la elaboración de perfiles);
- el marketing directo (incluida la elaboración de perfiles); y
- el tratamiento con fines de investigación científica/histórica y estadísticas.

### Recomendación de Braze

Braze ofrece la posibilidad de marcar un perfil de usuario como dado de baja de SMS, correos electrónicos o notificaciones push tanto a través de nuestras [REST API]({{site.baseurl}}/api/home) como a través de los SDK de [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=android) y [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=web). Si recibes objeciones de los interesados para recibir dichos mensajes, puedes utilizar las API de Braze para cancelar la suscripción de esos usuarios finales.

Si eso no es suficiente, para evitar el tratamiento de datos personales del usuario final por parte de Braze, el perfil del usuario final debe eliminarse de la misma manera que se especifica en el apartado «Derecho de supresión».

## Derechos relacionados con la toma de decisiones automatizada y la elaboración de perfiles {#rights-related-to-automated-decision-making-and-profiling}

Algunas leyes de protección de datos prohíben, o permiten a los interesados optar por no participar en, la toma de decisiones automatizada o la elaboración de perfiles en determinadas circunstancias, en particular para decisiones que "producen un efecto legal o un efecto significativamente similar en el individuo".

### Recomendación de Braze

Braze no realiza ninguna acción de elaboración de perfiles automatizada ni de toma de decisiones con ramificaciones legales o equivalentes para los interesados. Si consideras que tu propio uso de los servicios de Braze tendrá impactos legales o equivalentes y has recibido una objeción al respecto, puedes optar por eliminar el perfil de usuario de la misma manera que en el "Derecho de supresión".

## Publicidad segmentada {#targeting-advertising}

Según algunas leyes de privacidad estatales de EE. UU., los sujetos de datos pueden oponerse al uso de sus datos personales con fines de publicidad segmentada.

### Recomendación de Braze

Al crear audiencias con el fin de dirigir anuncios a tus sujetos de datos, debes asegurarte de haber excluido a cualquier sujeto de datos que se haya opuesto a la publicidad segmentada, por ejemplo, consumidores de California que hayan ejercido su derecho a "No vender ni compartir" en virtud de la CCPA.

Para más información sobre cómo crear audiencias para sincronizar con plataformas de terceros, consulta [Audience sync]({{site.baseurl}}/partners/canvas_audience_sync).

## El derecho a la no discriminación {#the-right-to-non-discrimination}

Los titulares de los datos tienen derecho a ejercer sus derechos de privacidad sin discriminación.

### Recomendación de Braze

En su uso de los servicios de Braze, los clientes deben asegurarse de no discriminar a los titulares de los datos que hayan ejercido sus derechos de privacidad. Por ejemplo, recomendamos que los titulares de los datos que hayan ejercido sus derechos de privacidad no sean segmentados en audiencias ni sean objeto de segmentación de una manera que pueda discriminarlos.