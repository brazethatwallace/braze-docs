---
nav_title: Kognitiv Inspire
article_title: Kognitiv Inspire
description: "Kognitiv Inspire es un sistema tecnológico de fidelización que te permite implementar y evaluar tu estrategia de fidelización, ofreciendo capacidades innovadoras y comunicaciones personalizadas con los miembros para mejorar la eficacia del programa."
alias: /partners/kognitiv/
page_type: partner
search_tag: Partner
---

# Kognitiv Inspire

> [Kognitiv Inspire](http://kognitiv.com) es un sistema tecnológico de fidelización que ayuda a desbloquear experiencias de cliente inigualables a través de programas de fidelización basados en resultados que amplifican la interacción con los clientes, aumentan el gasto y celebran el comportamiento leal.

_Esta integración está mantenida por Kognitiv Inspire._

## Sobre la integración {#about-the-integration}

La integración de Braze y Kognitiv te permite implementar y evaluar tu estrategia de fidelización, ofreciendo capacidades innovadoras y comunicaciones personalizadas a los miembros para mejorar la eficacia del programa.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta Kognitiv | Para beneficiarte de esta asociación es necesario disponer de una cuenta [Kognitiv](http://kognitiv.com). |
| Clave de API de Kognitiv | Una clave de API REST de Kognitiv. Puedes crearla en la página **API Security Tokens**. |
| Punto de conexión REST de Braze | La URL de tu punto de conexión REST. Tu punto de conexión dependerá de la URL de Braze para [tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso {#use-cases}

- **Inscripción personalizada en programas de fidelización**: Impulsa a tus miembros en su recorrido de fidelización con una inscripción al programa sin complicaciones y una notificación de bienvenida personalizada entregada a través de su canal preferido.
- **Emisión de recompensas y notificación de interacción**: Mantén viva la chispa de la fidelización emitiendo recompensas y notificaciones que celebren los hitos de cada miembro.
- **Categorización y segmentación estratégica de los miembros**: Permite una interacción más personalizada clasificando y segmentando a los miembros en función del gasto, la interacción y reglas de negocio simples o complejas adaptadas a las necesidades específicas de tu marca.
- **Notificación en tiempo real de elegibilidad para promociones**: Haz que cada miembro se sienta especial con notificaciones instantáneas de su elegibilidad para promociones exclusivas.

## Integración {#integration}

Utiliza los webhooks de Kognitiv para enviar solicitudes a Braze cuando se produzcan eventos de fidelización. Los siguientes ejemplos ilustran cómo utilizar Kognitiv y Braze para emitir una recompensa, registrar a un usuario de Kognitiv en Braze y enviarle un correo electrónico de bienvenida.

{% raw %}
### Emisión de recompensas en Braze {#braze-issue-reward}

El siguiente ejemplo de Kognitiv emite una recompensa para los miembros. Kognitiv Inspire comunicará ese evento de emisión de recompensas a Braze como un evento personalizado a través de webhooks. Para enviar un correo electrónico de seguimiento para comunicar la recompensa, crea una campaña o Canvas que se active a partir de ese evento personalizado.

**URL del webhook**: `<braze-api-rest-endpoint>`
**Cuerpo de la solicitud**: `Raw Text`

- **Método HTTP**: POST
- **Encabezados de solicitud**:
  - **Authorization**: Bearer `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### Cuerpo de la solicitud {#request-body}

```json
{
  "events" : [
    {
    "external_id" : "{{memberId}}",
    "app_id" : "93ec5a59-3752-4a45-8559-55b61209ba38",
    "name" : "rewards_issued",
    "time" : "{{issuedDate}}",
    "issued_date" : "{{issuedDate}}",
    "issued_location_name" : "{{issuedLocationName}}",
    "reward_type" : "{{rewardType}}"
    }
  ]
}
```

### Crear un usuario y enviar un correo electrónico de bienvenida {#create-a-user-and-send-a-welcome-email}

El siguiente ejemplo de Kognitiv crea un nuevo usuario en Braze cuando se inscribe en KLS. Para programar un correo electrónico de bienvenida para este usuario, crea una campaña o Canvas en Braze que se active en función de atributos personalizados específicos.

**URL del webhook**: `<braze-api-rest-endpoint>` <br>
**Cuerpo de la solicitud**: `Raw Text`

- **Método HTTP**: POST
- **Encabezados de solicitud**:
  - **Authorization**: Bearer `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### Cuerpo de la solicitud

```json
{
  "attributes": [
    {
      "app_id": "93ec5a59-3752-4a45-855b6109ba38",
      "bio": "Software Architect",
      "country": "{{memberAddressCO}}",
      "email": "{{memberEmail}}",
      "email_subscribe": "opted_in",
      "external_id": "{{memberId}}",
      "first_name": "{{memberFirstName}}",
      "home_city": "{{memberAddressCity}}",
      "time_zone": "America/Chicago",
      "total_points_balance": "{{memberPointsAvailable}}",
      "CreatedKLS": "{{issuedTimestamp}}",
      "email_contact_allowed" : "{{memberEmailContactAllowed}}",
      "sms_contact_allowed" : "{{memberSmsContactAllowed}}",
      "date_joined": "{{issuedDate}}"
    }
  ]
}
```
{% endraw %}

## Documentación y características de integración de Kognitiv Inspire {#kognitiv-inspire-documentation-and-integration-features}

Una vez que integres Braze con Kognitiv Inspire, Kognitiv te permite acceder a su amplia cartera de API, a las funciones de webhook de vanguardia y a las sólidas capacidades de importación y exportación de datos para una transferencia masiva sin problemas. Para obtener más información sobre las funciones y capacidades de integración de Kognitiv Inspire, consulta la [guía de recursos](https://info.kognitivloyalty.com) de Kognitiv o ponte en contacto con ellos para una demostración guiada.

### Puntos de conexión {#endpoints}

**Autorización de la REST API**
- Región de EE. UU.: `https://app.kognitivloyalty.com/Auth/connect/token`
- Región CA/EMEA: `https://ca.kognitivloyalty.com/Auth/connect/token`
- Región APAC: `https://aus.kognitivloyalty.com/Auth/connect/token`

**REST API (URL base)**
- Región de EE. UU.: `https://app.kognitivloyalty.com/api`
- Región CA/EMEA: `https://ca.kognitivloyalty.com/api`
- Región APAC: `https://aus.kognitivloyalty.com/api`

**Puntos de conexión de servicios web (URL base)**
- Región de EE. UU.: `https://app.kognitivloyalty.com/WS`
- Región CA/EMEA: `https://ca.kognitivloyalty.com/WS`
- Región APAC: `https://aus.kognitivloyalty.com/WS`

Para obtener más información sobre la configuración de tokens de acceso y puntos de conexión SFTP, ponte en contacto con Kognitiv para una demostración.