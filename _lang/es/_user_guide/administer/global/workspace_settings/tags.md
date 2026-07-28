---
nav_title: Gestión de etiquetas
article_title: Gestión de etiquetas
page_order: 6
page_type: reference
description: "Este artículo de referencia explica cómo gestionar etiquetas en el panel de Braze, incluyendo la anidación, el cambio de nombre y la organización de etiquetas en Campaigns, Canvas y Segments."
---

# Gestión de etiquetas {#managing-tags}

> Puedes gestionar las etiquetas que utilizas en Campaigns, Canvas y Segments desde una ubicación central. Para renombrar, quitar o añadir etiquetas, ve a **Configuración** > **Gestión de etiquetas**.

Para aprender a añadir etiquetas a Campaigns, Canvas, Segments y datos personalizados, consulta [Etiquetas]({{site.baseurl}}/user_guide/messaging/governance/tags).

## Anidar etiquetas {#nesting-tags}

Para organizar aún más tus etiquetas, puedes anidarlas bajo una etiqueta principal. Por ejemplo, puedes mantener todas las etiquetas de festividades anidadas bajo una etiqueta principal `Holidays`, o todas las etiquetas relacionadas con una etapa de tu embudo de marketing bajo una etiqueta principal `Funnel`.

- **Anidar una nueva etiqueta:** Crea una etiqueta, selecciona **Nest Tag Under** y elige bajo qué etiqueta existente deseas anidar tu nueva etiqueta.
- **Anidar una etiqueta existente:** Ve a la página de **Gestión de etiquetas**, pasa el cursor sobre la fila con tu etiqueta y selecciona **<i class="fas fa-pencil-alt"></i>Edit**. Luego, selecciona **Nest Tag Under** y elige la etiqueta principal.

### La etiqueta principal está en uso pero no aparece en **Nest Tag Under** {#parent-tag-is-in-use-but-missing-from-nest-tag-under}

Cuando una etiqueta principal está aplicada en el panel pero no aparece en el desplegable **Nest Tag Under** mientras creas una nueva etiqueta, vuelve a crear la etiqueta principal como una etiqueta independiente para que sea buscable en la lista. Este comportamiento es esperado cuando la etiqueta principal existe solo como una dependencia anidada en otra parte de tu espacio de trabajo.

![El cuadro de diálogo de nueva etiqueta con la opción Nest Tag Under seleccionada.]({% image_buster /assets/img_archive/tag_nested.png %}){: style="max-width:70%;" }

## Mejores prácticas {#tags-best-practices}

Usa etiquetas para organizar tus Campaigns, Canvas y Segments por objetivos de negocio, etapas del embudo, regiones y más.

La siguiente tabla muestra ejemplos de etiquetas que una aplicación de comercio electrónico podría encontrar útiles:

<style>
table td {
    word-break: break-word;
}
</style>


<table aria-label="Mejores prácticas">
  <caption>Mejores prácticas</caption>
<thead>
  <tr>
    <th>Embudo</th>
    <th>Objetivos de negocio</th>
    <th>Regional</th>
    <th>Campaigns</th>
    <th>Festividades</th>
    <th>Transacciones</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>On-boarding<br>Re-engagement<br>Loyal<br>PowerUser<br>Churn<br>Lost</td>
    <td>HighSpender<br>ActiveUser<br>NewUsers<br>FacebookAttribution<br>FirstAction</td>
    <td>UnitedStates<br>Northeast<br>Midwest<br>South<br>West<br>LATAM<br>AP<br>WesternEurope<br>MiddleEast</td>
    <td>Sales<br>Coupons<br>Events</td>
    <td>MLK<br>SuperBowl<br>PiDay<br>StPatricksDay<br>MarchMadness<br>Easter<br>Passover<br>MothersDay<br>MemorialDay<br>FathersDay<br>FourthJuly<br>LaborDay<br>VeteransDay<br>ColumbusDay<br>PresidentsDay<br>Halloween<br>RoshHashanah<br>Thanksgiving<br>Christmas<br>Hanukkah<br>NewYears</td>
    <td>Transactional<br>Notification<br>ConnectedActionTaken</td>
  </tr>
</tbody>
</table>

## Ejemplos {#use-cases}

Los siguientes son ejemplos comunes del uso de etiquetas para gestionar el ciclo de vida de tu mensajería.

{% tabs %}
{% tab Limitación de frecuencia %}

### Limitación de frecuencia {#throttling}

Limita la frecuencia con la que tus clientes reciben Campaigns de un tipo determinado. Por ejemplo, podrías configurar los siguientes filtros para limitar la frecuencia de las Campaigns promocionales:

`Last received campaign` con la etiqueta `Promo` hace más de 5 días
<br>`OR`<br>
`Has not received campaign` con la etiqueta `Promo`

{% endtab %}
{% tab Informes %}

### Informes {#reporting}

Configura un informe de participación para supervisar el volumen de todas las Campaigns con una etiqueta determinada. Por ejemplo, si deseas monitorear todas tus Campaigns de push, podrías añadir una etiqueta como `Push Reporting` a esas Campaigns y luego configurar un [informe de participación]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#automatically-select-campaigns-or-canvases) para que te envíe un informe de esas Campaigns etiquetadas todos los días.

{% endtab %}
{% endtabs %}