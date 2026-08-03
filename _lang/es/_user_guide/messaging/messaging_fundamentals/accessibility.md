---
nav_title: Accesibilidad
article_title: Crea mensajes accesibles en Braze
page_order: 0.5
page_type: reference
description: "Este artículo de referencia explica por qué es importante la accesibilidad en el contenido de marketing, cómo funciona el idioma de accesibilidad (HTML lang) en Braze a través de los canales y cómo puedes crear mensajes accesibles en Braze."
---

# Crea mensajes accesibles en Braze {#build-accessible-messages-in-braze}

> Comprende por qué es importante tener en cuenta la accesibilidad en tu contenido de marketing y cómo puedes crear mensajes accesibles en Braze. Para más orientación, consulta nuestro curso [Fundamentos de mensajería accesible](https://learning.braze.com/accessible-messaging-foundations) en Braze Learning.

El contenido de marketing que excluye a personas con discapacidades, incluso de forma involuntaria, puede impedir que millones de personas interactúen con tu marca. La accesibilidad en el marketing consiste en permitir que todos experimenten tu marketing, comprendan tu comunicación y tengan la oportunidad de invertir en tu producto, servicio o marca, o convertirse en seguidores de ellos.

Al diseñar tus mensajes, tómate el tiempo extra para considerar cómo puedes hacer que tus diseños sean accesibles para todos tus clientes.

{% alert important %}
Este contenido está pensado como orientación general y no garantiza el cumplimiento de estándares de accesibilidad como las WCAG. Braze ofrece herramientas que apoyan la creación de mensajes más accesibles, pero es tu responsabilidad asegurarte de que tu contenido final cumpla con los requisitos aplicables. La accesibilidad es un tema complejo con muchas partes en movimiento. Muchas empresas trabajan con especialistas o consultores en accesibilidad para garantizar que sus prácticas de contenido, diseño y desarrollo satisfagan las necesidades de todos los usuarios.
{% endalert %}

## Accesibilidad en Braze {#accessibility-at-braze}

Apoyar la comunicación accesible significa mantenerse abierto, curioso y dispuesto a aprender. En Braze, nos importa ayudar a las personas a conectarse, y sabemos que hacer espacio para todos es parte de hacerlo bien. La accesibilidad no es algo que consideremos "terminado", y agradecemos la oportunidad de seguir aprendiendo.

{% multi_lang_include accessibility/feedback.md %}

## Áreas de discapacidad a considerar {#areas-of-disability-to-consider}

*Esta sección está parcialmente adaptada de [W3C: Diverse Abilities and Barriers](https://www.w3.org/WAI/people-use-web/abilities-barriers/).*

{% tabs local %}
{% tab Visual %}

Las discapacidades visuales pueden ir desde una pérdida de visión leve o moderada en uno o ambos ojos, hasta una pérdida sustancial o completa de la visión en ambos ojos. Algunas personas tienen una sensibilidad reducida o nula a ciertos colores, o una mayor sensibilidad a los colores brillantes.

Para interactuar con tu contenido, estos usuarios necesitan la capacidad de:

- Ampliar o reducir el tamaño del texto y las imágenes
- Personalizar la configuración de fuentes, colores y espaciado
- Escuchar la síntesis de texto a voz del contenido (es decir, usar un lector de pantalla)
- Escuchar audiodescripciones de video
- Leer texto usando Braille actualizable

{% alert note %}
- A nivel mundial, al menos 2200 millones de personas tienen una deficiencia visual de cerca o de lejos (consulta [WHO](https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment))
- Aproximadamente 1 de cada 12 hombres y 1 de cada 200 mujeres tienen algún grado de deficiencia en la visión del color, lo que representa unas 300 millones de personas en el mundo (consulta [NHS](https://www.nhs.uk/conditions/colour-vision-deficiency/))
{% endalert %}

{% endtab %}
{% tab Auditiva %}

Las discapacidades auditivas pueden incluir una pérdida auditiva de leve a moderada en uno o ambos oídos. Incluso una pérdida parcial de la audición puede ser problemática en lo que respecta al contenido de audio.

Para comprender tu contenido, estos usuarios dependen de:

- Transcripciones y subtítulos del contenido de audio
- Reproductores multimedia que muestren subtítulos y ofrezcan opciones para ajustar el tamaño del texto y los colores de los subtítulos
- Opciones para detener, pausar y ajustar el volumen del contenido de audio (independientemente del volumen del sistema)
- Audio en primer plano de alta calidad que se distinga claramente de cualquier ruido de fondo

{% alert note %}
- Una de cada ocho personas en Estados Unidos (13 %, o 30 millones) de 12 años o más tiene pérdida auditiva en ambos oídos, según exámenes auditivos estándar
- Aproximadamente el 15 % de los adultos estadounidenses (37,5 millones) de 18 años o más reportan alguna dificultad auditiva (consulta [NIH](https://www.nidcd.nih.gov/health/statistics/quick-statistics-hearing))
{% endalert %}

{% endtab %}
{% tab Física %}

Las discapacidades físicas pueden incluir debilidad y limitaciones en el control muscular o la sensibilidad, trastornos articulares, dolor que impide el movimiento y miembros amputados.

Estos usuarios dependen del soporte de teclado para activar funcionalidades (incluso si no usan un teclado estándar). Para interactuar con tu contenido, estos usuarios necesitan:

- Áreas de clic amplias
- Tiempo suficiente para completar tareas
- Indicadores visibles del foco actual
- Mecanismos para saltar bloques de contenido, como encabezados de página o barras de navegación

{% alert note %}
Casi 2 millones de personas en EE. UU. viven con la pérdida de una extremidad (consulta [Amputee Coalition](https://www.amputee-coalition.org/limb-loss-resource-center/resources-filtered/resources-by-topic/limb-loss-statistics/limb-loss-statistics/#1))
{% endalert %}

{% endtab %}
{% tab Cognitiva %}

Las discapacidades cognitivas, de aprendizaje y neurológicas involucran la neurodiversidad y los trastornos neurológicos, así como los trastornos conductuales y de salud mental que no son necesariamente neurológicos. Pueden afectar cualquier parte del sistema nervioso e impactar en la capacidad de las personas para oír, moverse, ver, hablar y comprender información.

Dependiendo de las necesidades individuales, estos usuarios dependen de:

- Contenido claramente estructurado
- Etiquetado consistente de formularios, botones y otros contenidos
- Destinos de enlaces predecibles e interacción general predecible
- Diferentes formas de navegar, como menús y barras de búsqueda
- Configuración para desactivar contenido parpadeante, intermitente o que distraiga de alguna otra forma
- Texto más sencillo respaldado por imágenes


{% alert note %}
- Una de cada cinco personas en Estados Unidos tiene problemas de aprendizaje y atención (consulta [LDA](https://ldaamerica.org/lda_today/the-state-of-learning-disabilities-today/#:~:text=LD%20Today,have%20learning%20and%20attention%20issues.))
- Aproximadamente entre el 10 y el 20 % de la población mundial se considera neurodivergente (consulta [Deloitte](https://www2.deloitte.com/us/en/insights/topics/talent/neurodiversity-in-the-workplace.html))
- Aproximadamente 1 de cada 100 niños tiene autismo en todo el mundo (consulta [WHO](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders))
{% endalert %}

{% endtab %}
{% endtabs %}

## Buenas prácticas {#best-practices}

Crear contenido accesible no tiene por qué ser abrumador. Pequeñas decisiones bien pensadas pueden marcar una gran diferencia. Esta sección recorre consejos prácticos que ayudan a más personas a leer, navegar e interactuar con tus mensajes con éxito. Ya sea que estés ajustando tu texto, dando estilo a tus botones o añadiendo texto alternativo a las imágenes, cada mejora contribuye a una experiencia más inclusiva. Vamos a ello.

### Contenido {#content}

#### Estructura y flujo {#structure-and-flow}

Empecemos por los cimientos. Cuando tu contenido tiene una estructura clara, es más fácil de seguir para todos, especialmente para las personas que dependen de lectores de pantalla o la navegación por teclado.

- **Divide tu contenido en secciones:** Usar encabezados, viñetas y listas ayuda a las personas a comprender y escanear rápidamente tu contenido, incluso cuando tienen prisa.
- **No te saltes niveles de encabezado:** Los encabezados dan estructura a tu contenido, ayudando a los lectores a comprender rápidamente cómo se relacionan las secciones entre sí. Cuando te saltas niveles de encabezado (por ejemplo, pasando directamente de un H2 a un H4), rompes esta estructura lógica. Esto dificulta que los usuarios, especialmente quienes usan lectores de pantalla, naveguen y comprendan tu mensaje con claridad. Sigue siempre una jerarquía lógica y secuencial de encabezados (H1 a H2 a H3, y así sucesivamente) para asegurarte de que tu contenido se mantenga organizado, accesible y fácil de seguir para todos.

#### Legibilidad {#readability}

Una vez que tu estructura está en su lugar, el siguiente paso es asegurarte de que tus palabras sean realmente fáciles de leer. Esto significa mantener las cosas simples, escaneables y cómodas de leer en distintos dispositivos y necesidades de usuario.

- **Escribe oraciones cortas y claras:** Las oraciones cortas son fáciles de entender para todos, especialmente para personas que usan lectores de pantalla o que tienen dificultades para procesar información compleja. Escribe a un nivel de lectura de séptimo grado en Estados Unidos. Puedes usar recursos como [Hemingway App](https://hemingwayapp.com/) para verificar el nivel de lectura de tu texto.
- **Elige tamaños de fuente y espaciado legibles:** El texto demasiado pequeño puede ser difícil de leer, especialmente en dispositivos móviles. Usa al menos 14px para el texto del cuerpo. Haz los encabezados más grandes para que los usuarios puedan ver claramente la diferencia. Un espaciado adicional entre líneas (alrededor de 1.5 de altura de línea) y entre párrafos mejora la legibilidad, especialmente para personas con necesidades visuales o cognitivas.
- **Evita el texto justificado:** El texto justificado crea un espaciado desigual entre palabras, lo que dificulta la lectura para personas con dislexia o discapacidades cognitivas. Considera alinear a la izquierda el contenido que ocupe más de dos líneas para idiomas de izquierda a derecha, o alinear a la derecha para [idiomas de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).
- **Usa negritas, cursivas y mayúsculas con moderación:** Enfatizar demasiado texto dificulta la lectura, especialmente para personas con dislexia o discapacidades visuales. Mantenlo simple.

#### Claridad y usabilidad {#clarity-and-usability}

Finalmente, hablemos de los detalles más finos: las cosas que ayudan a los usuarios no solo a ver tu contenido, sino a comprenderlo e interactuar con él.

- **Etiqueta claramente los enlaces y botones:** Asegúrate de que el texto de tus [enlaces](#links) y [botones](#buttons) explique claramente qué sucederá a continuación. Esto ayuda a las personas que usan lectores de pantalla o navegan con teclado a saber qué esperar.
- **Usa símbolos y emojis con moderación:** Los caracteres especiales y emojis pueden hacer tu contenido más divertido, pero pueden resultar confusos cuando los lee un lector de pantalla. Úsalos con moderación y asegúrate de que no reemplacen texto claro y descriptivo.
- **Prueba la truncación:** Siempre prueba tu texto [enviando un mensaje de prueba]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages) a un dispositivo para asegurarte de que tu texto no se trunque. Si tu mensaje se está cortando, esto perjudica tanto a ti como a tu audiencia, ya que impide que tu contenido les llegue.

### Idioma de accesibilidad {#accessibility-language}

El **idioma de accesibilidad** indica a los lectores de pantalla y otras herramientas de asistencia en qué idioma está tu contenido. Para los canales que envían una página HTML completa o un correo electrónico, Braze puede añadir una etiqueta de idioma (`lang`) cuando la configuras en el editor o a través de Liquid. Esto cumple con el [Criterio de conformidad 3.1.1 de WCAG 2.1: Idioma de la página (Nivel A)](https://www.w3.org/WAI/WCAG21/Understanding/language-of-page.html).

Si dejas el idioma de accesibilidad en blanco y no hay un valor predeterminado seguro disponible, Braze omite la etiqueta de idioma. Si no se establece ningún idioma, las herramientas de asistencia suelen recurrir al idioma del teléfono o la computadora de la persona. Si este difiere del idioma del mensaje, la pronunciación puede sonar incorrecta.

Campaigns y Canvas usan los mismos editores para estas opciones, a menos que una característica no esté disponible para tu espacio de trabajo.

#### Configurar el idioma de accesibilidad {#configure-accessibility-language}

Cuando tu editor lo incluya, ve a la sección **Accesibilidad** en la configuración del mensaje. Elige un idioma del menú desplegable o usa Liquid (por ejemplo {% raw %}`{{accessibility_language}}`{% endraw %} cuando los [mensajes multilingües]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) están activados y la **Configuración de localización** está establecida).

#### Mensajes multilingües {#multi-language-messages}

En **Configuración de localización**, establece un idioma de accesibilidad para cada configuración regional para que Liquid pueda completar {% raw %}`{{accessibility_language}}`{% endraw %} en los envíos localizados. Si ese valor ya está seleccionado para los nuevos mensajes depende del canal. Para flujos de trabajo de CSV y traducción, comienza con [Configuración de idioma y accesibilidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#language-settings-and-accessibility).

#### Compatibilidad de canales y editores {#channel-and-editor-support}

Usa esta tabla para comparar canales. Los valores predeterminados pueden diferir, así que verifica lo que tu audiencia realmente recibe.

| Canal | Qué debes saber |
| --- | --- |
| Correo electrónico (arrastrar y soltar, plantilla completa) | Establece el idioma en el editor. Con mensajes multilingües, una plantilla de correo electrónico completa puede coincidir con el idioma de cada configuración regional automáticamente. Si solo usas Content Blocks (fila única), esos atajos no funcionan de la misma manera: elige el idioma tú mismo donde el editor lo permita. |
| Correo electrónico (código HTML) | Braze no añade una etiqueta de idioma por ti. Añádela en tu HTML si la necesitas. |
| In-App Messages (arrastrar y soltar) | Cuando eliges un idioma en **Accesibilidad**, Braze añade ese idioma al HTML externo del mensaje para que los lectores de pantalla traten todo el mensaje en ese idioma. Con los mensajes multilingües activados, los nuevos mensajes pueden usar de forma predeterminada los idiomas de tu configuración regional. La **vista previa** podría no mostrar ningún idioma hasta que elijas uno en **Configuración**. |
| Banners | Mismo comportamiento que los In-App Messages. |
| Páginas de destino | Puedes establecer el idioma en la página en vivo. Elige un idioma o usa Liquid si tu cuenta permite Liquid en páginas de destino. Los valores predeterminados también difieren de los In-App Messages y Banners: verifica la página publicada. |
| Content Cards | Las tarjetas usan un campo **Idioma** para aplicaciones en lugar de un idioma de accesibilidad explícito. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Compatibilidad de canales y editores" }

Cuando escribes HTML tú mismo, puedes añadir una etiqueta de idioma en parte del mensaje (por ejemplo, una frase en otro idioma). Para más patrones, consulta [HTML personalizado](#custom-html).

#### Referencia de estándares {#standards-reference}

Cuando Braze añade una etiqueta de idioma a nivel raíz en HTML, sigue la regla HTML [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang). Las herramientas de prueba suelen buscar [`html-has-lang`](https://dequeuniversity.com/rules/axe/4.2/html-has-lang). Content Cards usan tu campo de **idioma** en lugar de ese patrón HTML.

### Botones {#buttons}

Usa **botones** para indicar una acción, como enviar un formulario o reproducir un carrusel. Si estás navegando a una nueva URL, considera usar un [enlace](#links) en su lugar.

#### Escribe texto claro y orientado a la acción {#write-clear-action-oriented-text}

Al igual que el texto de los enlaces, las etiquetas de los botones deben describir claramente la acción. Un texto de botón efectivo es específico y orientado a la acción. Por ejemplo, "Enviar pedido" indica claramente a los usuarios qué sucederá cuando hagan clic, mientras que simplemente "Enviar" puede ser ambiguo. Cada etiqueta debe describir con precisión su acción prevista, para que los lectores de pantalla y todos los usuarios puedan comprender y predecir fácilmente el resultado al interactuar con tus botones.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Buen texto de botón <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Texto de botón deficiente <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Enviar pedido"</td>
      <td>"Enviar"</td>
    </tr>
    <tr>
      <td>"Crear cuenta"</td>
      <td>"Registrarse"</td>
    </tr>
    <tr>
      <td>"Descargar nuestro folleto"</td>
      <td>"Descargar"</td>
    </tr>
    <tr>
      <td>"Ver detalles del producto"</td>
      <td>"Más información"</td>
    </tr>
    <tr>
      <td>"Suscribirse a actualizaciones"</td>
      <td>"Suscribirse"</td>
    </tr>
  </tbody>
</table>

Mantén el texto de los botones conciso para evitar la truncación. Si el texto de un botón es demasiado largo, puede cortarse con puntos suspensivos en lugar de ajustarse.

#### Usa suficiente contraste de color {#use-sufficient-color-contrast}

El texto de los botones debe ser fácil de leer contra el color de fondo del botón. Verifica que el texto de tu botón cumpla con los [mínimos de contraste](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) AA de WCAG 2.2:

- Relación de contraste de 4.5:1 para texto de tamaño normal (la mayoría de los botones)
- Relación de contraste de 3:1 para texto grande (normalmente 18pt o más)

Un alto contraste ayuda a que los botones sigan siendo legibles y clicables para todos, incluidos los usuarios con discapacidades visuales o quienes ven tu mensaje en entornos difíciles. Para más orientación, consulta la sección [Contraste de color](#color-contrast).

#### Haz que los botones sean fáciles de tocar {#make-buttons-easy-to-tap}

Asegúrate de que tus botones (y enlaces) sean lo suficientemente grandes y estén lo suficientemente separados para los usuarios en dispositivos móviles. Los [objetivos táctiles](#touch-targets) pequeños o amontonados pueden ser frustrantes o imposibles de usar para usuarios con discapacidades motoras.

### Enlaces {#links}

Usa enlaces para la navegación, como dirigir a los usuarios a una página externa.

#### Escribe texto de enlace descriptivo {#write-descriptive-link-text}

Escribe texto de enlace que describa claramente a dónde llevará el enlace al usuario. Los usuarios de lectores de pantalla a menudo saltan de enlace en enlace como forma de escanear el contenido, así que asegúrate de que el texto de tu enlace pueda entenderse por sí solo. Evita frases como "haz clic aquí", "más" y "haz clic para más detalles", ya que son ambiguas cuando se leen fuera de contexto.

Por ejemplo, considera cómo podrías escribir un enlace para ver un informe meteorológico.

| Malo | Mejor | Óptimo |
| --- | --- | --- |
| Haz clic aquí | Haz clic aquí para acceder al clima de hoy | El clima de hoy |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Escribe texto de enlace descriptivo" }

Como con todo el contenido, mantenlo directo con la menor cantidad de palabras adicionales posible.

#### Evita dar estilo de botón a los enlaces {#avoid-styling-links-like-buttons}

Los editores de arrastrar y soltar de Braze generan HTML semántico de forma predeterminada, por lo que los enlaces no tienen estilo de botón allí. Sin embargo, si estás trabajando con [HTML personalizado](#custom-html) o haciendo cambios a nivel de código, ten esto en cuenta:

- Los **enlaces (`<a>`)** responden a la tecla <kbd>Enter</kbd>.
- Los **botones (`<button>`)** responden tanto a la tecla <kbd>Enter</kbd> como a la tecla <kbd>Espacio</kbd>.

Dar estilo de botón a un enlace puede confundir a las personas que navegan con teclado: podrían intentar presionar <kbd>Espacio</kbd> y esperar que funcione.

Usa el elemento correcto para la acción:

- Usa `<button>` para acciones, como enviar un formulario o abrir un modal.
- Usa `<a>` para navegación, como enlazar a otra página o archivo.

{% raw %}

```html
<!-- Recommended: A true button for an action -->
<button type="button">Download report</button>

<!-- Not recommended: A link styled as a button -->
<a href="#" class="btn">Download report</a>
```

{% endraw %}

### Objetivos táctiles {#touch-targets}

Los objetivos táctiles son cualquier parte de tu mensaje que los usuarios tocan para realizar una acción, como botones, enlaces o iconos. Estos elementos deben ser lo suficientemente grandes y estar lo suficientemente separados para que las personas puedan tocarlos fácilmente, especialmente en dispositivos móviles.

Cuando los objetivos táctiles son demasiado pequeños o están demasiado juntos, puede ser frustrante o imposible para los usuarios con dificultades de movilidad o destreza interactuar con tu mensaje. Mejorar esto puede ayudar a reducir errores y crear una experiencia más fluida para todos.

Esto es lo que debes tener en cuenta:
- **Usa un tamaño adecuado de objetivo táctil.** Apunta a un tamaño mínimo de objetivo táctil de 44 x 44 píxeles. Esto se alinea con las directrices de WCAG 2.2 para [objetivos táctiles](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) y los estándares comunes de usabilidad móvil.
- **Dale espacio a cada objetivo.** Si los objetivos táctiles están demasiado juntos, como enlaces apilados o botones agrupados estrechamente, puede ser fácil fallar o tocar el incorrecto. Añade espaciado o relleno entre elementos para evitarlo.
- **No dependas solo de los elementos visuales.** Incluso los iconos pequeños pueden hacerse más usables con relleno adicional, permitiéndoles cumplir los requisitos de tamaño mínimo sin alterar el diseño.
- **Previsualiza en dispositivos móviles.** Prueba tu mensaje en diferentes tamaños de pantalla y asegúrate de que los elementos interactivos sean fáciles de usar.

Mejorar los objetivos táctiles es una de las formas más efectivas de hacer tu mensaje más accesible en dispositivos móviles, y es una buena experiencia de usuario para todos.

### Imágenes {#images}

#### Proporciona texto alternativo {#provide-alt-text}

El texto alternativo (texto alt) es una breve descripción del contenido o función de una imagen que los lectores de pantalla y otras tecnologías de asistencia proporcionan a los usuarios. Para cada imagen significativa, escribe texto alternativo descriptivo para que los usuarios que no pueden ver los elementos visuales aún comprendan tu mensaje o llamada a la acción.

#### Evita imágenes de texto {#avoid-images-of-text}

Siempre que sea posible, evita colocar texto dentro de imágenes: los lectores de pantalla no pueden leer texto basado en imágenes, y los usuarios no pueden ajustar fácilmente el tamaño de fuente o el color para una mejor visibilidad. Considera estos consejos:

- **Elimina texto donde puedas:** Mueve cualquier texto descriptivo o promocional de la imagen a un campo de texto en tu mensaje. De esta manera, los usuarios pueden redimensionarlo o cambiar su color según sea necesario usando las preferencias de su dispositivo o navegador.
- **Prueba la legibilidad y el contraste:** Si debes mantener texto en la imagen, sigue las buenas prácticas de [contraste de color](#color-contrast) y usa una [fuente de escala grande](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html#dfn-large-scale). Esto significa que el texto debe tener al menos 18 puntos (aproximadamente 24 píxeles) para texto sin negrita o 14 puntos (aproximadamente 18 píxeles) si está en negrita. Usar estos tamaños ayuda a que el texto siga siendo legible sin obligar a los usuarios a hacer zoom, y mejora el contraste general y la legibilidad del contenido. Prueba para confirmar que sigue siendo legible en pantallas más pequeñas.
- **Proporciona texto alternativo:** Para texto esencial que debe permanecer en la imagen, incluye texto alternativo que describa las palabras.

Cuando las imágenes contienen texto que no se puede editar, los usuarios con discapacidades visuales pierden la flexibilidad de hacer ajustes de lectura. Al separar el texto de las imágenes, ayudas a más usuarios a leer e interactuar con tu mensaje cómodamente.

#### Consejos para escribir texto alternativo {#tips-for-writing-alt-text}

- [Describe lo que realmente hay en la imagen](#tip-1)
- [Mantenlo breve, pero específico](#tip-2)
- [Evita "imagen de" o "foto de"](#tip-3)
- [Refleja el texto que aparece en la imagen](#tip-4)
- [Limítate al contexto relevante, sin jerga de marketing adicional](#tip-5)
- [Considera el propósito de la imagen](#tip-6)

##### Describe lo que realmente hay en la imagen {#tip-1}

Los usuarios de lectores de pantalla dependen del texto alternativo para comprender el contenido o función de una imagen. Evita el "lenguaje de marketing" genérico que no coincide con lo que se muestra visualmente.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Buenos ejemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Ejemplos deficientes <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Mujer sonriente con chaqueta de mezclilla azul, sosteniendo una bolsa de compras."</td>
      <td>"¡Es hora de darte un gusto!" (No menciona lo que realmente hay en la imagen)</td>
    </tr>
    <tr>
      <td>"Hombre con camiseta negra, apoyado en una bicicleta en una calle de la ciudad."</td>
      <td>"¡Abraza tu mejor vida ahora!" (Ignora la bicicleta y el entorno urbano)</td>
    </tr>
    <tr>
      <td>"Edificio de apartamentos azul con un cartel de 'Se alquila' al frente."</td>
      <td>"¡La clave para un mañana mejor!" (No refleja el apartamento ni el cartel)</td>
    </tr>
  </tbody>
</table>

##### Mantenlo breve, pero específico {#tip-2}

Un texto alternativo conciso facilita el procesamiento para los usuarios. Incluye suficiente detalle para transmitir el propósito, pero omite lo innecesario. Como regla general, mantén el texto alternativo en 125 caracteres o menos. Si se necesita algo más que una frase breve u oración, considera usar uno de los [métodos de descripción larga](https://www.w3.org/WAI/tutorials/images/complex/) de W3C.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Buenos ejemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Ejemplos deficientes <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Zapatillas rojas para correr sobre fondo blanco"</td>
      <td>"Zapatillas para correr que son extremadamente cómodas y perfectas para tu estilo de vida activo en un vibrante tono de rojo." (Demasiado largo y lleno de contenido promocional innecesario)</td>
    </tr>
    <tr>
      <td>"Cuatro computadoras portátiles en un soporte de exhibición"</td>
      <td>"Descubre el impulsor de productividad definitivo que redefine cómo trabajas cada día, de todas las formas imaginables." (No describe lo que realmente se muestra)</td>
    </tr>
    <tr>
      <td>"Grupo de amigos comiendo helado en un día soleado"</td>
      <td>"Captura la felicidad pura con el dulce más dulce: ¡la vida es mejor con nuestra marca de helado!" (Demasiado abstracto y centrado en la marca)</td>
    </tr>
  </tbody>
</table>

##### Evita "imagen de" o "foto de" {#tip-3}

Los lectores de pantalla ya anuncian que es una imagen. Ve directamente a describir el tema.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Buenos ejemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Ejemplos deficientes <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Mesa preparada para brunch con panqueques, fruta y café."</td>
      <td>"Imagen de una mesa preparada para brunch"</td>
    </tr>
    <tr>
      <td>"Valla publicitaria al borde de la carretera con texto en negrita 'Gran inauguración'"</td>
      <td>"Foto de una valla publicitaria al lado de una carretera"</td>
    </tr>
    <tr>
      <td>"Paisaje de montaña nevada al atardecer"</td>
      <td>"Foto de nieve y montañas"</td>
    </tr>
  </tbody>
</table>

##### Refleja el texto que aparece en la imagen {#tip-4}

Si una imagen incluye texto esencial, incluye esa información en el texto alternativo para que los usuarios no se la pierdan.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Buenos ejemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Ejemplos deficientes <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Banner que dice 'Rebajas de verano: 50% de descuento en toda la ropa de baño.'"</td>
      <td>"Banner promocionando una oferta." (No menciona el descuento real)</td>
    </tr>
    <tr>
      <td>"Logo con el texto 'Café Toscana' en fuente cursiva"</td>
      <td>"Imagen de logo de un café." (No incluye el texto 'Café Toscana')</td>
    </tr>
    <tr>
      <td>"Anuncio que dice 'Entradas para concierto disponibles ahora: comienza el 5 de junio'"</td>
      <td>"Anuncio de concierto." (Sin detalles del evento)</td>
    </tr>
  </tbody>
</table>

##### Limítate al contexto relevante, sin jerga de marketing adicional {#tip-5}

No rellenes el texto alternativo con términos SEO o llamadas a la acción que no estén directamente relacionadas con la imagen. Proporciona valor para quienes no pueden ver la imagen.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Buenos ejemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Ejemplos deficientes <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Computadora portátil mostrando el gráfico de análisis del panel de Braze"</td>
      <td>"¡Impulsa las conversiones y dispara el ROI con la mejor plataforma del mundo!" (Añade lenguaje de marketing innecesario)</td>
    </tr>
    <tr>
      <td>"Conjunto de patio trasero con cuatro sillas y una mesa de vidrio"</td>
      <td>"¡Organiza una increíble fiesta de verano para todos tus amigos y familiares ahora!" (Describe un escenario, no la imagen)</td>
    </tr>
    <tr>
      <td>"Teléfono móvil mostrando una aplicación de pronóstico del clima con 75°F en pantalla"</td>
      <td>"Experimenta innovaciones en tiempo real en seguimiento del clima que cambian las reglas del juego" (No refleja lo que se muestra visualmente)</td>
    </tr>
  </tbody>
</table>

##### Considera el propósito de la imagen {#tip-6}

Si una imagen funciona como un enlace o llamada a la acción, describe la acción prevista ("Comprar", "Enlace a", "Suscribirse"), no solo la etiqueta o el producto mostrado.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Buenos ejemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Ejemplos deficientes <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Comprar la colección de otoño"</td>
      <td>"Colección de otoño" (Falta la acción prevista)</td>
    </tr>
    <tr>
      <td>"Enlace a eBook gratuito"</td>
      <td>"eBook gratuito" (No deja claro que es un enlace)</td>
    </tr>
    <tr>
      <td>"Suscribirse a la lista de correo"</td>
      <td>"Lista de correo" (No describe lo que el usuario puede hacer)</td>
    </tr>
  </tbody>
</table>

Si la imagen no tiene un propósito, hazlo saber también. Las imágenes decorativas, como los logos, deben tener una etiqueta alt vacía (`alt=""`) para que los lectores de pantalla sepan que deben omitirla. Sin ella, generalmente se lee el nombre del archivo de imagen en su lugar.

#### Cómo los clientes de correo electrónico muestran el texto alternativo {#how-email-clients-display-alt-text}

La visualización y representación del texto alternativo en los mensajes de correo electrónico está controlada por el cliente de correo electrónico del destinatario (como Gmail, Outlook o Apple Mail), no por Braze. Si notas diferencias en cómo aparece el texto alternativo en diferentes clientes de correo electrónico o plataformas, por ejemplo, el texto alternativo mostrándose de forma diferente en Gmail en escritorio versus la aplicación móvil de Gmail, esto se debe a cómo cada cliente elige representar el mismo HTML.

Aunque puedes incluir texto alternativo de cualquier longitud en tu HTML de correo electrónico, algunos clientes de correo electrónico pueden truncar u ocultar el texto alternativo que es demasiado largo para caber dentro de las dimensiones de la imagen. Si tienes preguntas sobre el comportamiento del texto alternativo en un cliente de correo electrónico específico, contacta a [Soporte]({{site.baseurl}}/support_contact).

### Videos {#videos}

Los videos son atractivos, pero si no son accesibles, corres el riesgo de excluir a parte de tu audiencia. Usa los siguientes consejos para hacer tu contenido de video más inclusivo:

- [Proporciona subtítulos](#closed-captions)
- [Proporciona controles de reproducción](#playback-controls)
- [Evita la reproducción automática](#no-auto-play)
- [Evita contenido con destellos o parpadeos](#no-seizures)

#### Proporciona subtítulos {#closed-captions}

Incluye subtítulos en tus videos para que los usuarios puedan seguir los diálogos, efectos de sonido y otro contenido de audio. Los subtítulos ayudan a:

- Personas sordas o con dificultades auditivas
- Espectadores que ven el video sin sonido
- Hablantes no nativos que prefieren leer junto con el audio

Los subtítulos se pueden activar o desactivar, permitiendo a los usuarios elegir lo que mejor les funcione.

{% alert note %}
Braze no genera automáticamente subtítulos para tus videos. Es tu responsabilidad añadir subtítulos precisos a tus archivos de video antes de incluirlos en tu mensaje.
{% endalert %}


#### Proporciona controles de reproducción {#playback-controls}

Asegúrate de que tu video incrustado incluya controles de reproducción accesibles, como reproducir, pausar, silenciar y buscar, para que los usuarios puedan interactuar con él de la manera que mejor les funcione.

#### Evita la reproducción automática {#no-auto-play}

Siempre que sea posible, evita configurar los videos para que se reproduzcan automáticamente. La reproducción automática puede ser molesta o desorientadora para:

- Usuarios que dependen de lectores de pantalla o navegación por teclado
- Personas con sensibilidad al movimiento
- Cualquier persona en un entorno silencioso (como un lugar de trabajo o una situación nocturna)

Permite que los usuarios elijan cuándo reproducir un video incluyendo controles claros.

#### Evita contenido con destellos o parpadeos {#no-seizures}

No incluyas videos con efectos de destellos o parpadeos, especialmente a alta frecuencia. Estos pueden provocar convulsiones en usuarios con epilepsia fotosensible y causar malestar en otros.

### Contraste de color {#color-contrast}

Un contraste de color suficiente ayuda a garantizar que tus mensajes sean fáciles de leer para todos, incluidas las personas con baja visión o quienes ven tu contenido en condiciones de brillo o entornos difíciles. Apunta a relaciones de contraste que cumplan con los [requisitos de nivel AA de WCAG 2.2](https://www.w3.org/TR/WCAG/#contrast-minimum):

- Relación de contraste de 4.5:1 para texto normal (piensa en texto del cuerpo, botones y enlaces)
- Relación de contraste de 3:1 para texto grande (piensa en encabezados y etiquetas más grandes)

Puedes probar tus opciones de color usando la [herramienta de verificación de contraste de WebAim](https://webaim.org/resources/contrastchecker/).

{% alert note %}
Los editores de Braze te permiten seleccionar combinaciones de colores personalizadas. Ten en cuenta que ciertas opciones de color pueden afectar negativamente a la accesibilidad. Elige tus colores con cuidado para asegurarte de que tu contenido sea legible y cumpla con las normas de accesibilidad.
{% endalert %}


### HTML personalizado {#custom-html}

Si usas HTML personalizado en tu mensajería:

- Usa [HTML semántico](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML). Esto significa usar los elementos HTML correctos para su propósito previsto en lugar de dar estilo a un elemento para que parezca otro. La mayoría de los elementos HTML tienen su propio soporte de accesibilidad incorporado.
- Para el idioma a nivel de documento donde Braze puede añadir metadatos HTML en la exportación, consulta [Idioma de accesibilidad](#accessibility-language); el comportamiento varía según el canal. Cuando marcas el contenido tú mismo, establece el [atributo `lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang) dentro de tu HTML para identificar el idioma en el que está tu contenido. Los lectores de pantalla usan diferentes bibliotecas de sonido para cada idioma basándose en la pronunciación y características de ese idioma. Si esto no se especifica, un lector de pantalla asume que el contenido está escrito en el idioma predeterminado que el usuario eligió al configurar el lector de pantalla. Si el mensaje no está realmente en el idioma predeterminado, entonces el lector de pantalla podría no pronunciar el mensaje correctamente.

{% raw %}
```html
<html lang="en-us">
```
{% endraw %}

{% alert note %}
Cuando uses el editor de correo electrónico de arrastrar y soltar, establece el idioma desde la pestaña **Configuración** cuando ese control esté disponible. Las plantillas completas y los correos electrónicos solo con bloques de contenido pueden usar diferentes valores predeterminados para el idioma de accesibilidad; consulta [Idioma de accesibilidad](#accessibility-language). Otros canales también se cubren en esa sección.
{% endalert %}

- Usa [atributos ARIA](#aria-attributes) para dar contexto adicional. Estos atributos proporcionan información adicional a las tecnologías de asistencia, ayudando a aclarar el rol, estado o propiedades de los elementos de la interfaz de usuario que de otro modo podrían no ser claros.

### Atributos ARIA {#aria-attributes}

Cuando usas código personalizado en los editores de Braze, puedes usar Aplicaciones de Internet Enriquecidas Accesibles ([ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)) para proporcionar soporte de accesibilidad adicional para los usuarios que dependen de tecnología de asistencia. Los roles y atributos ARIA ayudan a los lectores de pantalla a interpretar tu contenido con mayor claridad, especialmente cuando usas elementos que no transmiten significado por sí mismos (como `<div>` o `<span>`).

{% alert important %}
Aunque ARIA está diseñado para hacer el contenido web más accesible, si se usa incorrectamente, puede hacer más daño que bien. ARIA no reemplaza al HTML semántico, lo complementa, así que solo usa ARIA cuando los elementos HTML nativos no satisfagan tus necesidades.
{% endalert %}

Aquí tienes algunos ejemplos que son especialmente útiles en contextos de mensajería:

- [aria-label](#aria-label)
- [aria-labelledby](#aria-labelledby)
- [aria-hidden="true"](#aria-hiddentrue)
- [role="presentation"](#rolepresentation)
- [aria-live="polite"](#aria-livepolite)

#### aria-label {#aria-label}

`aria-label` añade un nombre accesible a elementos que no tienen texto visible. Si estás usando un icono sin texto (como una papelera o una "X" para cerrar), alguien que use un lector de pantalla no sabrá qué hace, a menos que lo etiquetes. `aria-label` le da voz a ese icono.

{% raw %}
```html
<button aria-label="Close message">
  <svg ...></svg>
</button>
```
{% endraw %}

#### aria-labelledby {#aria-labelledby}

`aria-labelledby` conecta un elemento con algo que ya tiene una etiqueta visible. Así que si tienes un banner o región que debe leerse en voz alta con un título, puedes usar `aria-labelledby` para decirle a la tecnología de asistencia: "Usa ese encabezado de allí para nombrar esta parte."

{% raw %}
```html
<h2 id="banner-title">Important Update</h2>
<div role="region" aria-labelledby="banner-title">...</div>
```
{% endraw %}

#### aria-hidden="true" {#aria-hiddentrue}

`aria-hidden="true"` oculta cosas de los lectores de pantalla. Es útil para texto o elementos visuales que no transmiten un significado importante, como un destello, una marca de verificación o un emoji usado puramente por estilo.

Esto mantiene la experiencia más limpia para los usuarios de lectores de pantalla, que de otro modo podrían escuchar contenido redundante o confuso. También es útil para ocultar cosas como contenido de acordeón fuera de pantalla que aún no se ha expandido.

{% raw %}
```html
<span aria-hidden="true">✔️</span>
```
{% endraw %}

En general, es mejor usar `alt=""` para [imágenes decorativas](#images) e iconos en lugar de `aria-hidden="true"`. Mientras que el HTML semántico es ampliamente compatible con todos los lectores de pantalla y software de asistencia, el soporte de ARIA varía. Incluso si usas `aria-hidden`, deberías incluir igualmente un atributo alt vacío.

#### role="presentation" {#rolepresentation}

`role="presentation"` le dice a la tecnología de asistencia que ignore los elementos que son solo de diseño, como las tablas de maquetación. Por ejemplo, los correos electrónicos a menudo usan tablas solo para alinear elementos. Sin este rol, los lectores de pantalla podrían asumir que tu maquetación es una tabla de datos y comenzar a leer números de fila y columna.

{% raw %}
```html
<table role="presentation">...</table>
```
{% endraw %}

Los correos electrónicos creados en el editor de arrastrar y soltar tienen los elementos de presentación marcados automáticamente con el atributo ARIA `role="presentation"`.

#### aria-live="polite" {#aria-livepolite}

`aria-live="polite"` anuncia actualizaciones cuando el contenido cambia sin necesidad de interacción del usuario. Úsalo cuando muestres actualizaciones dinámicas dentro de un mensaje, como éxitos, errores u otras notificaciones.

{% raw %}
```html
<div aria-live="polite">Your preferences have been saved.</div>
```
{% endraw %}

## Pruebas automatizadas de accesibilidad {#automated-accessibility-testing}

Para ayudarte a identificar y corregir problemas de accesibilidad de forma temprana, Braze ofrece pruebas automatizadas de accesibilidad en las siguientes áreas:

- [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision#accessibility-testing) para correos electrónicos
- [Escáner de accesibilidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message#accessibility-scanner) para mensajes creados con nuestro editor HTML (por ejemplo, mensajes HTML dentro de la aplicación, Content Blocks HTML, [pies de correo electrónico personalizados]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer), [páginas de adhesión voluntaria por correo electrónico]({{site.baseurl}}/user_guide/channels/email/subscriptions#creating-a-custom-opt-in-page) y [páginas de cancelación de suscripción por correo electrónico]({{site.baseurl}}/user_guide/channels/email/subscriptions#creating-a-custom-unsubscribe-page)).

Estas pruebas verifican tu mensaje según el estándar de las Pautas de Accesibilidad al Contenido en la Web ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), un conjunto de estándares técnicos reconocidos internacionalmente para contenido accesible. Cualquier problema que pueda detectarse automáticamente se marca y categoriza por gravedad para ayudarte a priorizar.

{% alert note %}
Inbox Vision funciona tanto para correos electrónicos HTML como de arrastrar y soltar. El escáner solo se ejecuta en contenido creado con el editor HTML.
{% endalert %}

### Qué pueden y qué no pueden detectar las pruebas automatizadas {#what-automated-testing-can-and-cant-catch}

Las pruebas automatizadas de accesibilidad son un excelente punto de partida, pero no pueden detectarlo todo. Algunos problemas necesitan un ojo humano para evaluarse correctamente, especialmente cuando el contexto o el diseño visual influyen en cómo los usuarios experimentan tu correo electrónico.

Es posible que veas algunos problemas marcados como **Necesita revisión**. Son casos en los que el verificador no puede determinar con certeza si algo representa un problema de accesibilidad. Cuando eso ocurra, te recomendamos revisarlo manualmente.

Algunos ejemplos de lo que las herramientas automatizadas no pueden detectar de forma fiable incluyen:

- Si el orden de enfoque de los elementos interactivos sigue una secuencia lógica
- Si el contenido es completamente operable con un teclado, sin necesidad de un ratón
- Si el texto alternativo describe de forma significativa una imagen
- Si los encabezados se utilizan correctamente para organizar el contenido
- Si los enlaces y botones están claramente etiquetados y son fáciles de entender
- Si los objetivos táctiles son lo suficientemente grandes y están espaciados adecuadamente
- Si el texto sobre imágenes de fondo cumple los requisitos de contraste de color
- Si las instrucciones o etiquetas son claras y útiles para todos los usuarios

Estas limitaciones no son exclusivas de Braze: son comunes a todas las herramientas automatizadas de accesibilidad. Las comprobaciones automatizadas no pueden simular cada tecnología de asistencia, lector de pantalla o necesidad del usuario. Por eso la accesibilidad no es una verificación puntual, sino una práctica continua.

Incluso si tu mensaje supera todas las comprobaciones automatizadas, sigue siendo importante:

- Revisar cuidadosamente los problemas marcados, especialmente los etiquetados como **Necesita revisión**.
- Probar manualmente cuando sea posible, especialmente para patrones de diseño e interacción.
- Usar herramientas como lectores de pantalla, navegación solo con teclado y zoom del navegador para simular diferentes necesidades de acceso.

Al combinar las pruebas automatizadas con una revisión manual cuidadosa, detectarás más problemas potenciales y crearás Campaigns más inclusivas y usables para cada destinatario.