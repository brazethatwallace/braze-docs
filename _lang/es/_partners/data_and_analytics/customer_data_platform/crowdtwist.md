---
nav_title: Oracle Crowdtwist
article_title: Crowdtwist
description: "Este artículo describe la asociación entre Braze y Oracle Crowdtwist, mediante plantillas de Transformación de datos de Braze especialmente creadas y los objetos Data Push de Crowdtwist."
alias: /partners/crowdtwist/
page_type: partner
search_tag: Partner
---

# Oracle Crowdtwist

> [Oracle Crowdtwist](https://www.oracle.com/uk/cx/marketing/customer-loyalty/) es una solución líder de fidelización de clientes nativa en la nube que permite a las marcas ofrecer experiencias del cliente personalizadas. Su solución ofrece más de 100 vías de participación listas para usar, lo que permite a los especialistas en marketing desarrollar rápidamente una visión más completa del cliente.

La característica Data Push de Oracle Crowdtwist permite pasar metadatos de usuarios o eventos cada vez que se produce una actualización en la plataforma de Crowdtwist.

Esta guía describe cómo integrar las fuentes Live Push de perfil de usuario, actividad de usuario y canje de usuario de Oracle Crowdtwist en tu entorno Braze. Existen dos tipos adicionales de Data Push que no se tratan explícitamente en esta documentación, pero su configuración sigue los mismos principios que se describen en esta guía.

* [Live Push de perfil de usuario](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/PushUserProfile-withTiersv2.html): Incluye la creación de nuevos perfiles y la actualización de los existentes.

* [Live Push de actividad de usuario](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html): Incluye datos sobre la finalización de la actividad de los usuarios.

* [Live Push de canje de usuario](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserRedemption.html): Incluye datos sobre los canjes de recompensas de los usuarios.

Utilizando una plantilla de Transformación de datos de Braze, puedes filtrar los elementos del Data Push que no son relevantes para Braze y asignar los valores necesarios en Braze para que puedan ser aprovechados por los "destinos" disponibles.

Por ejemplo, utiliza un Data Push para pasar eventos personalizados y atributos relevantes a Braze, como cuando un usuario cambia de nivel de fidelización o canjea una recompensa. También puedes utilizarlo para registrar atributos personalizados en Braze en cuanto se actualicen esos datos en el perfil de usuario de un miembro, como el saldo de puntos de un usuario.

## Requisitos previos {#prerequisites}


| Requisito | Descripción |
| --- | --- |
| Cuenta de Oracle Crowdtwist | Se requiere una [cuenta de Oracle Crowdtwist](https://www.oracle.com/uk/cx/marketing/customer-loyalty/) para aprovechar esta integración. |
| Endpoint de transformación de datos de Braze | Esta integración se basa en la [herramienta de transformación de datos]({{site.baseurl}}/user_guide/data/unification/data_transformation) de Braze. Cuando creas una transformación de datos, Braze genera un endpoint único que puedes agregar como destino para el Data Push de Crowdtwist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Braze y Oracle Crowdtwist han creado [plantillas de Transformación de datos]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation?redirected=1#step-2-create-a-transformation) para ayudar a nuestros clientes a desarrollar sus propias Transformaciones de datos que aprovechan los eventos de perfil de usuario, canje de usuario y actividad de usuario.

## Paso 1: Crear una transformación de datos a partir de la plantilla de Oracle Crowdtwist {#step-1-create-data-transformation-from-oracle-crowdtwist-template}

Navega a **Configuración de datos > Transformación de datos > Crear transformaciones > Usar una plantilla** > y selecciona la plantilla "BRAZE <> CROWDTWIST" de tu preferencia.

Encontrarás cuatro plantillas: una para transformar eventos de perfil de usuario, actividad de usuario y canje de usuario, respectivamente, y una plantilla maestra que utiliza lógica condicional para aplicarse a varios eventos de Data Push.

Como se muestra en la [documentación de Data Push de Oracle Crowdtwist](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/DataPush.html), los objetos de Data Push contienen diferentes metadatos, por lo que cada uno requiere su propio código de transformación para crear los objetos de Braze adecuados. La plantilla maestra ilustra cómo configurar una única transformación de datos para aceptar cada uno de los tres tipos de objetos y crea una salida apropiada con los valores de cada objeto.

## Paso 2: Actualizar y probar la plantilla {#step-2-update-and-test-template}

En esta sección, verás las plantillas anotadas. El cuerpo de estas plantillas está diseñado para aplicarse al destino `/users/track`. Las anotaciones están marcadas por `//` al inicio de línea y texto en verde, y puedes eliminarlas sin afectar el funcionamiento del código de transformación.

La transformación utiliza JavaScript, que construye un objeto llamado "brazecall". Este objeto es donde creas el cuerpo de la solicitud que se envía a un endpoint de la REST API de Braze. Para obtener orientación sobre las estructuras requeridas de las solicitudes a estos destinos, consulta los enlaces en la sección "destinos".

{% alert note %}
Observa que los "valores" de cada "clave" comienzan con `payload.`. El payload representa el objeto de datos recibido de Oracle Crowdtwist. Utiliza la notación de puntos de JavaScript para elegir qué dato deseas usar para completar los elementos de tu objeto de Braze. Por ejemplo, cuando ves `external_id: payload.thirdPartyId`, esto significa que el ID externo de Braze se establece mediante el valor `third_party_id` almacenado en Oracle Crowdtwist. Para obtener más información sobre el esquema o la composición de los objetos procedentes de Oracle Crowdtwist, consulta la [documentación de Oracle](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html).
{% endalert %}

{% alert important %}
Utiliza los objetos enviados desde Oracle Crowdtwist para crear usuarios en Braze. Al incluir la clave `update_existing_only` con el valor `false`, si un objeto de atributo o evento incluye un identificador que no existe en Braze, Braze crea un perfil de usuario con los atributos incluidos en el objeto de evento o atributo. Si prefieres que Oracle Crowdtwist solo actualice perfiles que ya existen en Braze, establece este atributo en `true` en cada objeto de atributo o evento.
{% endalert %}

### Plantillas de transformación de datos {#data-transformation-templates}
{% tabs %}
{% tab Plantilla de evento de perfil de usuario%}
```javascript
let brazecall = {
 "attributes": [
   {
     //You must include an appropriate identifier for your attribute or event object from data available in Oracle Crowdtwist. This could be an external ID, Braze ID, user alias, phone, or email address for attribute or event objects.
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
   // **Important** To allow Oracle Crowdtwist events to create users in Braze, set the value of "_update_existing_only" to false. Otherwise, set this value to true in your event and attribute objects.
     "_update_existing_only": false,
     "crowdtwist_loyalty_points": payload.redeemablePoints,
 //In this example, the "tierInfo" object from Crowdtwist is transformed into a Braze Nested Custom Attribute. Use the "_merge_objects" value to avoid duplications in a data point efficient manner.
 //The "tierinfo_current_level" attribute is a flat Braze custom attribute, while the following "tierInfo" value is a nested object mirroring the Crowdtwist payload; the difference in capitalization is intentional.
     "tierinfo_current_level": payload.tierInfo.currentLevel,
     "_merge_objects" : true,
     "tierInfo" : {
       "resetDate": payload.tierInfo.resetDate,
       "dateReached":payload.tierInfo.dateReached,
        "scoreNeededToReach": payload.tierInfo.scoreNeededToReach,
        "nextLevel":{
        "minValue":payload.tierInfo.nextLevel.minValue,
        "maxValue":payload.tierInfo.nextLevel.maxValue,
        "title":payload.tierInfo.nextLevel.title
     }
     }
   }
 ]
,
//Below we show how to create both custom attributes and events from a single Crowdtwist User Profile object.
 "events": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "name": "assignedByEvent",
//Below we can see how to write a timestamp in your object, which is a required value for some objects, like the Event Object.
     "time": new Date().toISOString(),
     "properties": {
       "assigned_by_event": payload.tierInfo.assignedByEvent,
       "date_assigned": payload.tierInfo.dateAssigned
     },
           "_update_existing_only": false
   }
 ]
};
// After the /users/track request is assigned to brazecall, return brazecall to create an output.
return brazecall;

```

{% endtab %}
{% tab Plantilla de evento de actividad de usuario %}
```javascript
let brazecall = {
"events": [
   {
     "external_id": payload.thirdPartyId,
     "_update_existing_only": false,
     "activityId": payload.activityId,
     "name": payload.activityName,
     "time": new Date().toISOString(),
     "properties": {
       "description": payload.description,
       "date_assigned": payload.dateAwarded
     }
   }
 ]
};
return brazecall;
```
{% endtab %}
{% tab Plantilla de evento de canje %}
```javascript
let brazecall = {
 "attributes": [
   {
   "external_id": payload.thirdPartyId,
   //A user redemption event may not have a third party id, in which case you can instead provide the opportunity to include a user alias.
   "user_alias": { "alias_name" : "crowdtwist_redemption_username", "alias_label" : payload.userName},
   "_update_existing_only": false,
   "redeemed_coupon": payload.couponCode,
   "total_points_redeemed": payload.totalPointsRedeemed
      }
]
}
return brazecall;

```
{%endtab%}
{% tab Plantilla maestra %}
```javascript
//The master template uses JavaScript's conditional operators to determine the output of the Data Transformation. This example shows how to apply JavaScript to your transformation to allow for a dynamic range of sources or inputs.

 // We open the transformation with a simple "if" function. We're checking if the value "payload.tierInfo" is present. "tierInfo" is a value that is always populated in the User Profile Live Push object, but is not present in the others.

if (payload.tierInfo) {
let brazecall = {
 "attributes": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "_update_existing_only": false,
     "crowdtwist_loyalty_points": payload.redeemablePoints,
     "tierinfo_current_level": payload.tierInfo.currentLevel,
     "_merge_objects" : true,
     "tierInfo" : {
       "resetDate": payload.tierInfo.resetDate,
       "dateReached":payload.tierInfo.dateReached,
        "scoreNeededToReach": payload.tierInfo.scoreNeededToReach,
        "nextLevel":{
        "minValue":payload.tierInfo.nextLevel.minValue,
        "maxValue":payload.tierInfo.nextLevel.maxValue,
        "title":payload.tierInfo.nextLevel.title
     }
     }
   }
 ]
,
 "events": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "name": "assignedByEvent",
     "time": new Date().toISOString(),
     "properties": {
       "assigned_by_event": payload.tierInfo.assignedByEvent,
       "date_assigned": payload.tierInfo.dateAssigned
     },
           "_update_existing_only": false
   }
 ]
};
return brazecall;
//Now we use an "else if" operator to change the "brazecall" body if the object is a User Activity event by checking if the unique key "activityId" has been populated.
} else if (payload.activityId) {
 let brazecall = {
"events": [
   {
     "external_id": payload.thirdPartyId,
     "_update_existing_only": false,
     "activityId": payload.activityId,
     "name": payload.activityName,
     "time": new Date().toISOString(),
     "properties": {
       "description": payload.description,
       "date_assigned": payload.dateAwarded
     }
   }
 ]
};
return brazecall;
//Finally, this conditional statement triggers if the Data Push object is a User Redemption event, based on whether a value populates in the key "rewardId".
} else if (payload.rewardId) {
 let brazecall = {
 "attributes": [
   {
   "external_id": payload.thirdPartyId,
   "_update_existing_only": false,
   "redeemed_coupon": payload.couponCode,
   "total_points_redeemed": payload.totalPointsRedeemed
      }
]
}
return brazecall;
} else {
 //Include this error message to help with troubleshooting in the log if a call fails. Replace the text in the parentheses with anything that might be clearer to your team based on your Data Transformation.
 throw new Error("No appropriate Identifiers found");
}

```
{% endtab %}
{% endtabs %}

### Destinos {#destinations}

Las plantillas de esta guía están creadas para entregar al destino "Track Users", pero puedes diseñar tu plantilla para enviar a cualquiera de los endpoints listados en la [guía de transformación de datos de Braze]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation#step-2-create-a-transformation), con el apoyo de la [documentación de la REST API]({{site.baseurl}}/api/home) asociada.

### Pruebas {#testing}

Después de modificar la plantilla a tu gusto, debes validar que funciona correctamente. En el editor de transformación, selecciona **Validate** para generar una vista previa en la sección **Output** y confirmar que Braze acepta la solicitud mapeada para el destino elegido.

Cuando estés satisfecho con el objeto que ves en el campo **Output**, selecciona **Activate** para que el endpoint de transformación de datos esté listo para recibir datos.

Encontrarás la URL del webhook de tu transformación de datos en el panel de detalles de la transformación. Cópiala y úsala para la configuración dentro del Integration Hub de Oracle Crowdtwist.

{% alert important %}
Los endpoints de transformación de datos de Braze tienen un límite de velocidad de 1000 solicitudes por minuto. Considera la velocidad a la que deseas que estos datos estén disponibles en Braze y habla con tu director de cuentas de Braze si necesitas un límite de velocidad más alto para la transformación de datos.
{% endalert %}

Las transformaciones de datos son una herramienta muy dinámica y puedes diseñarlas para fines que van más allá de lo descrito en este documento con conocimientos de JavaScript y con la guía de nuestra documentación de la REST API. Para obtener soporte o solución de problemas en cambios complejos a tus plantillas de transformación de datos, habla con tu CSM para conocer la orientación disponible para ti.