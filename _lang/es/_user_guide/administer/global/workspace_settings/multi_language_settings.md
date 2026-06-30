---
nav_title: Configuración de localización
article_title: Configuración de localización
alias: "/multi_language_support/"
page_order: 4
description: "Este artículo ofrece un resumen de la configuración multilingüe en el panel de Braze y cómo utilizar las configuraciones regionales en tu mensajería."
---

# Configuración de localización {#localization-settings}

> La característica multilingüe te permite utilizar [etiquetas de traducción]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para dirigirte a usuarios de diferentes idiomas y ubicaciones, todo ello en un solo mensaje.

## Requisitos previos {#prerequisites}

{% multi_lang_include messaging/localization/locales.md section='multi-language prerequisites' %}

## Añadir una configuración regional {#add-a-locale}

1. Ve a **Configuración** > **Configuración de localización**.
2. Selecciona **Añadir configuración regional** y, a continuación, selecciona **Configuración regional predeterminada** o **Atributos personalizados**.
3. Introduce un nombre para la configuración regional.
4. [Selecciona un idioma para accesibilidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#language-settings-and-accessibility). Esta configuración permite que las tecnologías de asistencia, como los lectores de pantalla, pronuncien correctamente el texto.
5. Selecciona los atributos de usuario correspondientes a la opción de configuración regional que hayas elegido. Al configurar una configuración regional, puedes seleccionar idiomas de los atributos de usuario predeterminados o de los atributos personalizados. No puedes seleccionar de ambos.

{% tabs %}
{% tab Configuración regional predeterminada %}

Para **Configuración regional predeterminada**, usa los desplegables para seleccionar el idioma que deseas añadir y, opcionalmente, el país que se asociará con el idioma.

![Una ventana llamada "Añadir configuración regional - Idioma y país predeterminados" para especificar el idioma y el país.]({% image_buster /assets/img/multi-language_support/default_option.png %})

{% endtab %}
{% tab Atributos personalizados %}

Para **Atributos personalizados**, usa el desplegable para seleccionar el atributo personalizado asociado y, en el campo de texto, introduce el valor.

![Una ventana llamada "Añadir configuración regional - Atributos personalizados" para especificar el atributo personalizado y el valor.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %})

{% endtab %}
{% endtabs %}

{: start="6"}
6. Selecciona **Añadir configuración regional**.

Para conocer los pasos para usar estas configuraciones regionales en tus mensajes, consulta [Uso de configuraciones regionales]({{site.baseurl}}/locales_in_messages).

## Consideraciones {#considerations}

- Puedes seleccionar hasta dos atributos personalizados en una sola configuración regional, o hasta dos idiomas de atributos de usuario predeterminados. En ambos casos, el segundo atributo es opcional.
- Al editar los valores traducidos en el archivo CSV, evita modificar los valores predeterminados del archivo.
- La clave de configuración regional en tu archivo cargado debe coincidir con la de tu configuración multilingüe.

### Soporte y priorización {#support-and-prioritization}

- Si un usuario coincide tanto con una configuración regional definida por atributos personalizados como con una definida por atributos de usuario predeterminados, se prioriza la configuración regional del atributo personalizado.
- Los atributos personalizados admiten valores de texto (cadena) con coincidencia exacta.
- Si un atributo personalizado se elimina o se cambia su tipo, el usuario ya no podrá pertenecer a esa configuración regional y descenderá en la lista de prioridad de configuraciones regionales a las que pertenezca o recibirá las traducciones de marketing predeterminadas.
- Si una configuración regional no es válida (el atributo personalizado cambió o se eliminó), el error aparecerá en la página de **Asistencia en varios idiomas**.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuántas configuraciones regionales puedo añadir? {#how-many-locales-can-i-add}

Puedes añadir hasta 200 configuraciones regionales.

### ¿Dónde se almacenan los archivos de traducción en Braze? {#where-are-the-translation-files-stored-in-braze}

Los archivos de traducción se almacenan a nivel de Campaign, lo que significa que cada variante de mensaje debe tener traducciones cargadas. Las traducciones también se pueden almacenar en Content Blocks. Cuando el bloque se añade a un mensaje, sus traducciones se incluyen automáticamente.

### ¿El nombre de la configuración regional tiene que seguir un patrón o formato específico? {#does-the-locale-name-have-to-follow-a-specific-pattern-or-format}

No. Puedes usar la convención de nomenclatura que prefieras. El nombre de la configuración regional se usa al seleccionar la configuración regional en el editor y aparecerá en los encabezados del archivo que descargues con los ID de traducción.