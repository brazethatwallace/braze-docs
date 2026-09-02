---
nav_title: Eagle Eye
article_title: Eagle Eye
description: Aprende a integrar Eagle Eye con Braze.
alias: /partners/eagle_eye/
page_type: partner
search_tag: Partner
---

# Eagle Eye

> [Eagle Eye](https://eagleeye.com/) es una empresa líder en software como servicio (SaaS) y tecnología de IA que habilita a las marcas de comercio minorista, viajes y hostelería para ganarse la fidelización de sus clientes finales potenciando sus actividades de marketing del consumidor en tiempo real, omnicanal y personalizadas, a escala.

_Esta integración está mantenida por Eagle Eye._

## Resumen {#overview}

Eagle Eye Connect es una integración bidireccional entre Braze y AIR que habilita a las marcas a activar los datos de fidelización y promoción directamente en Braze. Los clientes pueden emitir recompensas en AIR a los consumidores que entren en una audiencia en AIR. Esto permite a los especialistas en marketing personalizar la interacción con los clientes utilizando datos en tiempo real, como saldos de puntos, promociones y actividades de recompensa.

## Casos de uso {#use-cases}

- Desencadena Campaigns en Braze basadas en eventos de fidelización, como umbrales de puntos o recompensas obtenidas.
- Enriquece los perfiles de usuario de Braze con datos de fidelización en tiempo real para habilitar una segmentación más personalizada.
- Haz un seguimiento e informa sobre la eficacia de las campañas vinculadas a los canjes de recompensas.
- Emite recompensas en AIR cuando los usuarios entren en Campaigns en Braze.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|--------------------------|-------------|
| Cuenta Eagle Eye AIR | Necesitas una cuenta Eagle Eye AIR activa para beneficiarte de esta asociación. Para empezar, ponte en contacto con el equipo de asociaciones de Eagle Eye en [partnerships@eagleeye.com](mailto:partnerships@eagleeye.com). |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos `users.track`. <br><br>Se puede crear en el panel de Braze desde **Configuración > Claves de API**. |
| Punto de conexión REST or transferencia de estado representacional de Braze | [La URL de tu punto de conexión REST or transferencia de estado representacional]({{site.baseurl}}/api/basics/#endpoints). Tu punto de conexión depende de la URL de Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Saliente vs. entrante {#outbound-vs-inbound}

Las tablas siguientes describen los dos tipos de integraciones compatibles entre Braze y Eagle Eye AIR. Eagle Eye Connect es el middleware que habilita el intercambio de datos entre AIR y sistemas de socios como Braze. Para saber más, consulta la [documentación de Braze de Eagle Eye](https://developer.eagleeye.com/docs/braze).

{% tabs local %}
{% tab outbound %}
<table aria-label="Saliente vs. entrante">
  <caption>Saliente vs. entrante</caption>
  <thead>
    <tr>
      <th>Dirección</th>
      <th>Iniciado por</th>
      <th>Flujo de datos</th>
      <th>Propósito</th>
      <th>Ejemplo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Eagle Eye → Braze</td>
      <td>Eagle Eye</td>
      <td>A la API de Braze</td>
      <td>
        Envía datos de fidelización a los perfiles de usuario de Braze como atributos personalizados mediante eventos personalizados. Dentro de Braze, los datos ingeridos pueden utilizarse para:
        <ul>
          <li>segmentar usuarios, desencadenar Campaigns</li>
          <li>personalizar mensajes</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Envío de puntos de fidelización o estado de nivel a Braze (<code>ee_loyalty.points.current</code>, <code>ee_loyalty.tier.tierId</code>)</li>
          <li>Actualizar el perfil de un usuario cuando recibe o canjea un cupón.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Saliente vs. entrante" }
{% endtab %}

{% tab inbound %}
<table aria-label="Saliente vs. entrante">
  <caption>Saliente vs. entrante</caption>
  <thead>
    <tr>
      <th>Dirección</th>
      <th>Iniciado por</th>
      <th>Flujo de datos</th>
      <th>Propósito</th>
      <th>Ejemplo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Braze → Eagle Eye</td>
      <td>Braze</td>
      <td>A la API de Eagle Eye mediante webhook</td>
      <td>
        Cuando un consumidor entra en una audiencia en Braze desde cualquier fuente, Braze puede desencadenar un webhook de Braze a EE Connect, permitiendo a EE emitir una recompensa (cupón o puntos).<br><br>
        Al finalizar la acción en AIR, Braze recibiría un evento saliente de AIR.
      </td>
      <td>
        <ul>
          <li>Se entregan recompensas (cupones o puntos) a un consumidor por unirse al programa de fidelización</li>
          <li>Se conceden recompensas a un consumidor que haya tenido una entrega tardía</li>
          <li>Recompensas por cumpleaños</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Saliente vs. entrante" }
{% endtab %}
{% endtabs %}

{% alert tip %}
Para obtener más información sobre los datos personalizados que puedes enviar a Braze como atributos o eventos personalizados, consulta la [documentación de Braze de Eagle Eye](https://developer.eagleeye.com/docs/braze#data-model).
{% endalert %}

## Resumen de la integración {#integration-overview}

Actualmente, los conectores entrantes y salientes solo pueden configurarse a través de la API con la ayuda directa del equipo de Eagle Eye; sin embargo, se está preparando una opción de autoservicio en el dashboard de AIR.

Cuando trabajes con tu equipo de Eagle Eye, completarás lo siguiente:

### Paso 1: Proporcionar detalles de configuración {#step-1-provide-configuration-details}

En primer lugar, proporcionarás los siguientes datos a tu equipo de Eagle Eye:

| Tú proporcionas | Descripción |
|------------------------|-------------|
| Credenciales de la API de Braze | Comparte tu punto de conexión REST or transferencia de estado representacional de Braze, identificador de aplicación y clave de API de forma segura con tu contacto de Eagle Eye. |
| Coincidencia de identificadores | Determina y comparte el identificador de usuario principal para las actualizaciones de perfil que sea común en AIR y Braze, como ID externo o correo electrónico. |
| Clave de autenticación | Determina y comparte una clave de autenticación secreta para cada conector entrante y saliente. |
| Código de moneda | Comparte el código de moneda de 3 dígitos para mostrar los importes monetarios de las compras (p. ej., USD). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 1: Proporcionar detalles de configuración" }

### Paso 2: Configurar Eagle Eye Connect {#step-2-configure-eagle-eye-connect}

Tu equipo de Eagle Eye configurará Eagle Eye Connect utilizando los datos que le proporciones junto con las credenciales únicas de la API de AIR y los eventos salientes para los conectores.

### Paso 3: Configurar acciones de comportamiento social en AIR {#step-3-configure-social-behavioral-actions-in-air}

A continuación, configurarás una o varias acciones de comportamiento social en AIR con referencias de acción únicas para emitir puntos o cupones.

### Paso 4: Configurar Braze {#step-4-configure-braze}

En Braze, completarás lo siguiente:

- Configura Campaigns en Braze para emitir recompensas en AIR
- Configura las comunicaciones a los consumidores cuando se reciban eventos de AIR

### Paso 5: Probar tu integración {#step-5-test-your-integration}

Haz llamadas a la API en AIR y observa el flujo de datos de eventos en tu espacio de trabajo de Braze. Valida los datos recibidos de AIR y confirma que los atributos se actualizan como se espera.

Además, añade usuarios a las audiencias y confirma que las recompensas se emiten en AIR.

### Paso 6: Lanzar a producción {#step-6-launch-to-production}

Una vez superadas las pruebas, la integración puede ponerse en vivo para enviar datos continuamente a Braze. Se requieren los mismos pasos de configuración para los entornos de producción en AIR y Braze.

Ponte en contacto con tu administrador del éxito del cliente de Eagle Eye para que te asignen un recurso que configure EE Connect.

## Soporte {#support}

Para obtener soporte sobre integración o solución de problemas, ponte en contacto con el equipo de soporte de Eagle Eye en [support@eagleeye.com](mailto:support@eagleeye.com).