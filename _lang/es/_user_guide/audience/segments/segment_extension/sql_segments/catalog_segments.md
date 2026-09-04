---
nav_title: "Segmentos de catálogo"
article_title: "Segmentos de catálogo"
page_order: 0
page_type: reference
alias: "/catalog_segments/"
description: "Este artículo describe cómo crear segmentos de catálogo, que utilizan datos de catálogo en extensiones de segmento SQL para crear audiencias de usuarios."
tool: Segments
---

# Segmentos de catálogo {#catalog-segments}

> Los segmentos de catálogo son un tipo de extensión de segmento SQL que se crea combinando datos de catálogo con datos de eventos personalizados o compras. Se pueden referenciar en un segmento y luego segmentar mediante Campaigns y Canvas.

Los segmentos de catálogo utilizan SQL para unir datos de catálogos y datos de eventos personalizados o compras. Para ello, debes tener un campo identificador común en tus catálogos y tus eventos personalizados o compras. Por ejemplo, el valor de un ID de artículo en un catálogo debe coincidir con el valor de una propiedad en un evento personalizado.

## Crear un segmento de catálogo {#creating-a-catalog-segment}

1. Ve a **Extensiones de segmento** > **Crear nueva extensión** > **Empezar con plantilla** y selecciona una plantilla. <br>![Modal con la opción de crear un segmento de catálogo para eventos, compras o segmentos RFM.]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2. El editor SQL se rellena automáticamente con una plantilla. <br>![Editor SQL con una plantilla pregenerada.]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>Esta plantilla une los datos de eventos de usuario con los datos de catálogo para segmentar a los usuarios que interactuaron con determinados artículos del catálogo.

3. Usa la pestaña **Variables** para proporcionar los campos necesarios para tu plantilla antes de generar tu segmento. <br>Para que Braze identifique a los usuarios en función de su interacción con los artículos del catálogo, debes hacer lo siguiente: <br> - Seleccionar un catálogo que contenga un campo de catálogo <br> - Seleccionar un evento personalizado que contenga una propiedad de evento <br> - Hacer coincidir los valores de tu campo de catálogo y propiedad de evento

Aquí tienes las directrices para seleccionar las variables:

| Campo de variable | Descripción |
| --- | --- |
| `Catalog` | El nombre del catálogo que estás utilizando para segmentar usuarios. |
| `Catalog field` | El campo de tu catálogo que contiene los mismos valores que tu `Custom event property`. Suele ser un tipo de ID. En el caso de uso de comercio electrónico, sería `shopify_id`. |
| `Custom event` | El nombre de tu evento personalizado, que es el mismo evento que contiene una propiedad con valores que coinciden con tu `Catalog field`. En el caso de uso de comercio electrónico, sería `Made Order`. |
| `Custom event property` | El nombre de la propiedad de tu evento personalizado, que coincide en valores con tu `Catalog field`. En el ejemplo de caso de uso de comercio electrónico, sería `Shopify_ID.` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Crear un segmento de catálogo" }

{: start="4"}
4. Si es necesario, completa los campos opcionales adicionales para tu caso de uso a fin de segmentar por un valor de campo particular dentro de tu catálogo:
- `Catalog field`: Un campo particular (nombre de columna) dentro de este catálogo
- `Value`: Un valor específico dentro de ese campo o columna <br><br> Usando la aplicación de salud como ejemplo, supongamos que dentro del catálogo de cada médico que puedes reservar, hay un campo llamado `specialty` que contiene un valor como `vision` o `dental`. Para segmentar a los usuarios que han visitado a cualquier médico con el valor `dental`, puedes seleccionar `specialty` como el `Catalog field` y seleccionar `dental` como el `Value`.

5. Después de crear una extensión de segmento SQL, te recomendamos hacer clic en **Ejecutar vista previa** para ver si tu consulta devuelve usuarios o si hay errores. Para más información sobre [previsualizar resultados de consultas]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#step-3-preview-the-query), administrar [extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#managing-your-segment-extensions) y más, consulta [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).

{% alert note %}
Si estás creando un segmento SQL que utiliza la tabla `CATALOGS_ITEMS_SHARED`, debes especificar un ID de catálogo. Por ejemplo:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Determinar si necesitas invertir SQL {#determining-if-you-need-to-invert-sql}

Aunque no es posible consultar directamente a los usuarios con cero eventos, puedes usar **Invertir SQL** para segmentar a estos usuarios.

Por ejemplo, para segmentar a los usuarios que tienen menos de tres compras, primero escribe una consulta para seleccionar a los usuarios que tienen tres o más compras. Luego, selecciona **Invertir SQL** para segmentar a los usuarios con menos de tres compras (incluidos aquellos con cero compras).

![Extensión de segmento llamada "Clicked 1-4 emails in the last 30 days" con la opción de invertir SQL seleccionada.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:70%;"}

{% alert important %}
A menos que tu objetivo específico sea segmentar a usuarios con cero eventos, no necesitarás invertir SQL. Si **Invertir SQL** está seleccionado, confirma que la característica es necesaria y que el segmento coincide con tu audiencia deseada. Por ejemplo, si una consulta segmenta a usuarios con al menos un evento, solo segmentará a usuarios con cero eventos cuando se invierta.
{% endalert %}

## Actualizar la pertenencia al segmento {#refreshing-segment-membership}

Para actualizar la pertenencia al segmento de cualquier segmento de catálogo, abre el segmento de catálogo y selecciona **Acciones** > **Actualizar** > **Sí, actualizar**.

{% alert tip %}
Si creaste un segmento en el que esperas que los usuarios entren y salgan regularmente, actualiza manualmente el segmento de catálogo que utiliza antes de segmentar ese segmento en una campaña o Canvas.
{% endalert %}

### Designar la configuración de actualización {#designating-refresh-settings}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

## Ejemplos {#use-cases}

{% tabs local %}
{% tab Health %}

### Aplicación de salud {#health-app}

Supongamos que tienes una aplicación de salud y quieres segmentar a los usuarios que han reservado una visita con el dentista. También tienes lo siguiente:

- Un catálogo `Doctors` que contiene los diferentes médicos que un paciente puede reservar, cada uno asignado con un `doctor ID`
- Un evento personalizado `Booked Visit` con una propiedad `doctor ID` que comparte los mismos valores que el campo `doctor ID` en tu catálogo
- Un campo `speciality` dentro de tu catálogo que contiene el valor `dental`

Configurarías un segmento de catálogo utilizando las siguientes variables:

| Variable | Propiedad |
| --- | --- |
| `Catalog` | Doctors |
| `Catalog field` | doctor ID |
| `Custom event` | Booked Visit |
| `Custom event property` | doctor ID |
| `(Under Filter SQL Results) Catalog field` | Specialty |
| `(Under Filter SQL Results) Value` | Dental |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aplicación de salud" }

{% endtab %}
{% tab software como servicio (SaaS) %}

### Plataforma software como servicio (SaaS) {#saas-platform}

Supongamos que tienes una plataforma software como servicio (SaaS) B2B y quieres segmentar a los usuarios que son empleados de un cliente existente. También tienes lo siguiente:

- Un catálogo `Accounts` que contiene las diferentes cuentas que actualmente utilizan tu plataforma software como servicio (SaaS), cada una asignada con un `account ID`
- Un evento personalizado `Event Attendance` con una propiedad "account ID" que comparte los mismos valores que el campo "account ID" en tu catálogo
- Un campo `Classification` dentro de tu catálogo que contiene el valor `enterprise`

Configurarías un segmento de catálogo utilizando las siguientes variables:

| Variable | Propiedad |
| --- | --- |
| `Catalog` | Accounts |
| `Catalog field ` | account ID |
| `Custom event` | Event Attendance |
| `Custom event property` | account ID |
| `(Under Filter SQL Results) Catalog field` | Classification |
| `(Under Filter SQL Results) Value` | Enterprise |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plataforma software como servicio (SaaS)" }

{% endtab %}
{% endtabs %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Ejecutar un segmento de catálogo consume créditos de extensión de segmento SQL? {#does-running-a-catalog-segment-consume-sql-segment-extension-credits}

Sí, los segmentos de catálogo funcionan con SQL y consumen créditos de extensión de segmento SQL. Para más información, consulta [Uso de segmentos SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#credits).

### ¿Crear un segmento de catálogo consume las asignaciones de extensión de segmento SQL? {#does-creating-a-catalog-segment-consume-sql-segment-extension-allotments}

Sí. De la misma manera que las extensiones de segmento SQL cuentan para tu asignación de extensiones de segmento, los segmentos de catálogo también cuentan para esa asignación.

### Tengo un caso de uso de segmento de catálogo que la plantilla actual no cubre. ¿Cómo debo configurarlo? {#i-have-a-catalog-segment-use-case-that-the-current-template-doesnt-serve-how-should-i-set-that-up}

Ponte en contacto con tu administrador de soporte al cliente o con el [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) para obtener orientación adicional.