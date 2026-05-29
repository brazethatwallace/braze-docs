{% if include.section == "multi-language prerequisites" %}

| Característica | Permisos de usuario obligatorios |
| --- | --- |
| Configuraciones regionales de varios idiomas | Necesitas estos permisos para crear y administrar configuraciones regionales de varios idiomas:<br><br> {::nomarkdown} <ul><li>Editar configuración de localización</li><li>Eliminar configuración de localización</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Table" }

{% endif %}

{% if include.section == "Preview" %}

## Vista previa de tus configuraciones regionales {#preview-your-locales}

En el menú desplegable **Preview message as user** de la pestaña **Test**, selecciona **Custom user** e introduce diferentes idiomas para obtener una vista previa del mensaje y comprobar si se traduce según lo esperado.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Preguntas más frecuentes {#frequently-asked-questions}

#### ¿Puedo realizar cambios en la copia traducida de una de mis configuraciones regionales? {#can-i-make-a-change-to-the-translated-copy-in-one-of-my-locales}
Sí. Primero, realiza la edición en el archivo CSV y, a continuación, vuelve a cargar el archivo para aplicar los cambios a la copia traducida.

#### ¿Puedo anidar etiquetas de traducción? {#can-i-nest-translation-tags}
No.

#### ¿Puedo añadir estilos HTML en las etiquetas de traducción? {#can-i-add-html-styling-in-the-translation-tags}
Sí, pero asegúrate de que el estilo HTML no se traduzca junto con el contenido.

#### ¿Qué validaciones o comprobaciones adicionales realiza Braze? {#what-validations-or-extra-checks-does-braze-do}

| Escenario | Validación en Braze |
|---|---|
| Al archivo de traducción le faltan configuraciones regionales asociadas al mensaje actual. | Este archivo de traducción no se cargará. |
| Al archivo de traducción le faltan bloques de texto, como un texto dentro de etiquetas de traducción Liquid, del mensaje de correo electrónico actual. | Este archivo de traducción no se cargará. |
| El archivo de traducción incluye el texto predeterminado que no coincide con los bloques de texto del mensaje de correo electrónico actual. | Este archivo de traducción no se cargará. Corrige esto en tu CSV antes de intentar cargarlo de nuevo. |
| El archivo de traducción incluye configuraciones regionales que no existen en la configuración de **Asistencia en varios idiomas**. | Estas configuraciones regionales no se guardarán en Braze. |
| El archivo de traducción incluye bloques de texto que no existen en el mensaje actual (como el borrador actual en el momento de cargar las traducciones). | Los bloques de texto que no existan en el mensaje actual no se guardarán del archivo de traducción en Braze. |
| Se elimina una configuración regional del mensaje después de que esa configuración ya se haya cargado en el mensaje como parte del archivo de traducción. | Al eliminar la configuración regional, se eliminarán todas las traducciones asociadas a dicha configuración en tu mensaje. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="What validations or extra checks does Braze do?" }

{% endif %}