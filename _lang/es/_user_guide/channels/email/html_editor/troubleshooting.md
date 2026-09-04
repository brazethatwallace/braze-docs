---
nav_title: Solución de problemas
article_title: Solución de problemas de correos electrónicos HTML
page_order: 9
description: "Diagnostica problemas de renderizado y del editor de correos electrónicos HTML utilizando un índice de síntomas y pasos estándar de solución de problemas."
channel: email
---

# Solución de problemas de correos electrónicos HTML {#troubleshoot-html-emails}

> Usa esta página para resolver problemas comunes del editor de correos electrónicos HTML y de los envíos de prueba. Para Inbox Vision y capacidad de entrega, consulta [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) y [Configuración de correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup).

## Empieza aquí: identifica tu síntoma {#start-here-match-your-symptom}

Busca tu síntoma en la siguiente tabla para navegar a la sección correspondiente.

| Síntoma | Ir a |
| --- | --- |
| El HTML del correo electrónico de prueba se ve mal | [El HTML se muestra incorrectamente en los correos electrónicos de prueba](#html-renders-incorrectly-in-test-emails) |
| El editor se comporta de forma extraña en Chrome | [Conflictos de extensiones](#extension-conflicts) |
| El correo electrónico se ve diferente en distintos clientes | [Renderizado de correo electrónico](#email-rendering) |
| El correo electrónico muestra código Liquid o enlaces rotos | [HTML desbalanceado en plantillas Liquid](#unbalanced-html-in-liquid-templates) |
| La vista previa de Inbox Vision no coincide con el correo electrónico enviado | [Inlining de CSS](#css-inlining) |
| Espacios en blanco o líneas después de las imágenes en correos electrónicos de prueba | [Espacio en blanco debajo de las imágenes](#white-space-under-images) |
| Los análisis de clics no incluyen parámetros de consulta | [Limitaciones de los análisis de clics en enlaces](#link-click-analytics-limitations) |
| Los superíndices causan un espaciado de línea inconsistente | [Problemas de altura de línea con superíndices](#superscript-line-height-issues) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Síntoma de correo electrónico HTML" }

## Ruta de investigación estándar {#standard-investigation-path}

Usa este flujo de trabajo cuando el renderizado del correo electrónico HTML o el comportamiento del editor no coincida con lo que esperas. Empieza en el paso 1.

1. Valida tu marcado HTML en el editor o en un validador externo.
2. Envía un [correo electrónico de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) y anota qué clientes de correo electrónico o navegadores muestran el problema.
3. Previsualiza con [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) para comparar el renderizado entre clientes.
4. Descarta [conflictos con extensiones del navegador](#extension-conflicts) si el propio editor se comporta de forma incorrecta.
5. Si el problema persiste, abre un [ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) con capturas de pantalla de Inbox Vision y los clientes afectados.

## El HTML se renderiza incorrectamente en los correos electrónicos de prueba {#html-renders-incorrectly-in-test-emails}

### Síntoma {#symptom}

Un [correo electrónico de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) no se ve como esperas desde el editor.

Revisa primero tu configuración HTML y después consulta [conflictos de extensiones](#extension-conflicts), [renderizado de correo electrónico](#email-rendering), [inlining de CSS](#css-inlining) y [espacio en blanco debajo de las imágenes](#white-space-under-images).

### Conflictos de extensiones {#extension-conflicts}

Ciertas extensiones del navegador pueden causar problemas con el editor de correo electrónico. Un ejemplo es [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en) cuando se usa con Google Chrome. Si estás usando una de estas extensiones, deberías:

- Editar los correos electrónicos de Braze en un navegador que no tenga Grammarly como extensión del navegador.
- Ponerte en contacto con tu director de cuentas de Braze y solicitar cambiar tus editores de correo electrónico a solo HTML o texto plano.

La vista de texto plano elimina tu editor `WYSIWYG` (lo que ves es lo que obtienes), así que primero deberías confirmar que todos los miembros del equipo se sienten cómodos con HTML antes de hacer esta solicitud.

### Renderizado de correo electrónico {#email-rendering}

Los correos electrónicos se renderizan de forma diferente según los navegadores y los clientes de correo electrónico, así que toma nota de con qué navegadores y clientes de correo electrónico estás experimentando problemas.

- Previsualiza tus correos electrónicos usando [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) para ver cómo se ven en diferentes navegadores y clientes de correo electrónico.
- Una vez que hayas identificado qué navegadores o clientes de correo electrónico están causando problemas, informa a tu equipo de desarrolladores de que necesitarán modificar su HTML y hacer ajustes para adaptarse a esos navegadores o clientes de correo electrónico.
- Si el problema es específico de [cómo se muestra el texto alternativo]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text), ten en cuenta que este comportamiento lo controla el cliente de correo electrónico del destinatario, no Braze.

### HTML desbalanceado en plantillas Liquid {#unbalanced-html-in-liquid-templates}

#### Síntoma

Algunos usuarios reciben una versión modificada del correo electrónico en la que el código Liquid se muestra en el mensaje, los enlaces están rotos o el espaciado se ve incorrecto.

Braze utiliza un analizador HTML interno para preparar los correos electrónicos antes de enviarlos. Este analizador admite características como la generación de preencabezados, la colocación de píxeles de seguimiento, la creación de plantillas de enlaces y el aliasing de enlaces. Cuando las etiquetas HTML no están balanceadas dentro de sus bloques lógicos Liquid o Content Blocks correspondientes, el analizador puede modificar el HTML subyacente de formas inesperadas. Esto puede provocar:

- Saltos de línea del renderizado de Liquid que aparecen en algunos clientes de correo electrónico
- Espaciado extraño por etiquetas `<p>` añadidas al cuerpo del correo electrónico
- Contenido de la etiqueta `<head>` movido al preencabezado
- Renderizado inconsistente entre sistemas operativos móviles
- Código específico de páginas móviles aceleradas eliminado de los cuerpos de correo electrónico páginas móviles aceleradas, lo que causa fallos de validación
- Enlaces rotos cuando se utilizan muchos parámetros de consulta o media queries diferentes

#### Balancear HTML dentro de bloques Liquid {#balance-html-within-liquid-blocks}

Asegúrate de que todas las etiquetas HTML se abran y cierren dentro de su bloque lógico Liquid o Content Block correspondiente. Esto evita que el analizador interno interprete el HTML como inválido y lo modifique.

#### Ejemplo desbalanceado {#unbalanced-example}

{% raw %}
```liquid
<img src={% if ${language} == 'en' %}"https://example.com/images/banner-en.png" style="width: 100%"{% elsif ${language} == 'de' %}"https://example.com/images/banner-de.png"{% else %}"https://example.com/images/banner-default.png" {% endif %} />
```
{% endraw %}

En este ejemplo, la etiqueta de apertura `<img` comienza fuera de cualquier bloque Liquid, y diferentes partes de los atributos de la etiqueta están divididas entre sentencias condicionales Liquid. Esta estructura confunde al analizador, que no puede determinar dónde comienza o termina la etiqueta.

#### Ejemplo balanceado {#balanced-example}

{% raw %}
```liquid
{% if ${language} == 'en' %}
  <img src="https://example.com/images/banner-en.png" style="width: 100%;" />
{% elsif ${language} == 'de' %}
  <img src="https://example.com/images/banner-de.png" style="width: 100%;" />
{% else %}
  <img src="https://example.com/images/banner-default.png" style="width: 100%;" />
{% endif %}
```
{% endraw %}

En la versión balanceada, cada rama Liquid contiene una etiqueta `<img>` completa e independiente. Este enfoque garantiza que el analizador procese cada rama correctamente.

#### Correcciones adicionales {#additional-fixes}

Si estás experimentando problemas de renderizado con media queries o muchos parámetros de consulta, intenta desactivar el inlining de CSS en la configuración de tu correo electrónico. Esto puede resolver conflictos entre el analizador HTML y reglas CSS complejas.

### Inlining de CSS {#css-inlining}

Hay ocasiones en las que las vistas previas en Inbox Vision aún no coinciden con lo que se envía con Braze. Esto puede deberse a la diferencia en el inlining de CSS realizado por Braze y por otras herramientas. Si sospechas que este es el caso, desactiva el inlining de CSS.

### Espacio en blanco debajo de las imágenes {#white-space-under-images}

#### Síntoma

Aparecen espacios en blanco o líneas después de las imágenes en los correos electrónicos de prueba.

Si notas espacios en blanco o líneas que aparecen después de las imágenes en tus correos electrónicos de prueba, esto suele deberse a cómo los clientes de correo electrónico renderizan los elementos de nivel inline. Las imágenes son de nivel inline de forma predeterminada y se alinean con la línea base, lo que permite a los navegadores acomodar los descendentes (la parte de letras como «g» o «y» que se extiende por debajo de la línea base). Esto crea un pequeño espacio que aparece como espacio en blanco.

Para solucionarlo, añade `display: block;` al CSS de tu imagen:

```html
<style>
  img {
    display: block;
  }
</style>
```

Alternativamente, aplica el estilo directamente a imágenes específicas:

```html
<img src="https://example.com/image.jpg" style="display: block;" alt="Image description" />
```

## Limitaciones de los análisis de clics en enlaces {#link-click-analytics-limitations}

### Síntoma

Los análisis de clics para correos electrónicos con muchos parámetros de consulta únicos no coinciden con tus expectativas. Es posible que veas recuentos de clics agregados para URL sin parámetros después de los primeros 100 enlaces únicos.

### Cómo funciona el seguimiento de clics en enlaces {#how-link-click-tracking-works}

Braze realiza el seguimiento de clics tanto en URL parametrizadas (con parámetros de consulta) como en URL base sin parámetros. Para los primeros 100 enlaces parametrizados únicos en los que se hace clic en una Campaign de correo electrónico o un Canvas, Braze recopila y reporta datos para ambos:

- La URL parametrizada completa (por ejemplo, `https://example.com?user_id=12345`)
- La URL base sin parámetros (por ejemplo, `https://example.com`)

Después de que se haga clic en los primeros 100 enlaces parametrizados únicos, Braze solo incrementa los recuentos de clics para la URL base sin parámetros. Esto significa que:

- Los análisis de clics se agregan en el dominio base y la ruta en lugar de en combinaciones individuales de parámetros de consulta
- Aún puedes realizar el seguimiento de la participación significativa basándote en las rutas de los enlaces
- El seguimiento de clics a nivel de usuario individual sigue funcionando con normalidad

Este comportamiento evita que los análisis se inflen con miles de combinaciones únicas de parámetros de consulta, al tiempo que se capturan los patrones generales de participación con los enlaces.

### Qué significa esto para tus Campaigns {#what-this-means-for-your-campaigns}

Si dependes de parámetros de consulta únicos para realizar el seguimiento del comportamiento específico de los usuarios en plataformas externas (por ejemplo, `https://example.com?user_id=USER_ID`), ten en cuenta que los análisis de clics de Braze solo conservarán esos parámetros para los primeros 100 enlaces únicos en los que se haga clic. Después de ese umbral, los clics siguen registrándose en tus análisis, pero se atribuyen a la URL sin parámetros.

Los datos de clics a nivel de usuario siguen disponibles a través de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) o el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), independientemente de cuántos enlaces parametrizados únicos se hayan clicado.

### Problemas de altura de línea con superíndices {#superscript-line-height-issues}

#### Síntoma

El texto con superíndices aparece con un espaciado de línea inconsistente, donde las líneas parecen más juntas o más separadas de lo previsto. Este es un problema de renderizado común en los clientes de correo electrónico y no es específico de Braze.

El uso de superíndices en correos electrónicos puede causar un comportamiento inesperado en la altura de línea porque los distintos clientes de correo electrónico manejan el texto en superíndice de maneras diferentes.

#### Resolución {#resolution}

Usa el editor HTML para controlar el estilo de los superíndices y los elementos circundantes.

Para definir explícitamente la altura de línea, añade CSS en línea para establecer el `line-height` del texto:

```html
<p style="line-height: 1.5;">Example text with superscript<sup style="line-height: inherit;">1</sup></p>
```

Para ajustar la alineación vertical, usa la propiedad `vertical-align` para alinear el superíndice sin alterar la altura de línea:

```html
<sup style="vertical-align: top; font-size: smaller;">1</sup>
```

Si los superíndices siguen causando problemas, usa un `<span>` como alternativa a `<sup>` para tener más control:

```html
<span style="font-size: smaller; vertical-align: top;">1</span>
```
