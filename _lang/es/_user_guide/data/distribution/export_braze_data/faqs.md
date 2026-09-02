---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre exportación
page_order: 7
page_type: FAQ
description: "Este artículo cubre algunas preguntas frecuentes sobre las exportaciones API y CSV."

---

# Preguntas más frecuentes {#frequently-asked-questions}

> Esta página ofrece respuestas a algunas de las preguntas más frecuentes sobre las exportaciones API y CSV.

## ¿Puedes hacer que ciertas exportaciones aparezcan en tu contenedor de S3 y otras no? {#can-you-make-certain-exports-appear-in-your-s3-bucket-and-others-not}

No. Si has proporcionado credenciales de S3, todas tus exportaciones aparecerán en tu contenedor de S3; de lo contrario, si no se proporcionan credenciales, todas las exportaciones aparecerán en un contenedor de S3 perteneciente a Braze.

## ¿Tengo que añadir credenciales de S3 a Braze para exportar datos? {#do-i-have-to-add-s3-credentials-to-braze-to-export-data}

No. Si no añades credenciales de S3, tus exportaciones aparecerán en un contenedor de S3 perteneciente a Braze.

## ¿Qué ocurre si configuras las credenciales de S3 en el panel pero no seleccionas "Make this the default data export destination"? {#what-happens-if-you-set-up-s3-credentials-in-the-dashboard-but-dont-select-make-this-the-default-data-export-destination}

La casilla de verificación **Make this the default data export destination** influye en si las exportaciones van a S3 o a Azure, suponiendo que hayas añadido credenciales para ambos.

## ¿El destino predeterminado de exportación de datos afecta a Braze Currents? {#does-the-default-data-export-destination-affect-braze-currents}

No. Currents utiliza su propio conector y su propia configuración de almacenamiento. Elegir un destino predeterminado de exportación para las exportaciones CSV y basadas en API no cambia dónde se escriben los datos de Currents.

## ¿Por qué he recibido varios archivos al exportar perfiles de usuario a S3? {#why-did-i-receive-multiple-files-when-exporting-user-profiles-to-s3}

Este es el comportamiento esperado para espacios de trabajo con muchos usuarios. Braze divide tu exportación en varios archivos en función del número de usuarios de tu espacio de trabajo. Por lo general, se genera un archivo por cada 5000 usuarios. Ten en cuenta que si estás exportando un segmento pequeño dentro de un espacio de trabajo grande, es posible que recibas varios archivos.

## ¿Por qué veo duplicados cuando exporto usuarios por segmento a través de la REST or transferencia de estado representacional API? {#why-do-i-see-duplicates-when-i-export-users-by-segment-through-rest-api}

Se trata de un caso muy poco frecuente causado por la arquitectura subyacente del proveedor de la base de datos. Los duplicados se eliminan cada semana; sin embargo, la mayoría de las semanas no se elimina ningún duplicado.

## ¿Cómo abro informes CSV en Excel? {#how-do-i-open-csv-reports-in-excel}

Aunque los archivos CSV suelen abrirse automáticamente en Excel de forma predeterminada, puede que no siempre sea así. Consulta los artículos de solución de problemas de [Windows](https://support.microsoft.com/en-us/windows/change-which-programs-windows-7-uses-by-default-62fd162f-8c82-0436-806f-c60d69dcf495) y [Apple](https://support.apple.com/guide/mac-help/choose-an-app-to-open-a-file-on-mac-mh35597/mac) para conocer los pasos para establecer Excel como tu programa predeterminado.

Para convertir un CSV a XLSX o XLS, o eliminar la coma entre los valores de datos, consulta [esta guía para importar archivos CSV en Excel](https://www.ablebits.com/office-addins-blog/convert-csv-excel/#import-csv-wizard).

Si notas que los ceros iniciales se eliminan de los ID de usuario en tu exportación CSV, esto ocurre porque Excel trata los números de un CSV como datos en lugar de texto. Para resolverlo, ejecuta el [Asistente de importación de texto de Excel](https://www.ablebits.com/office-addins-blog/converting-csv-excel-issues/#leading-zeros).