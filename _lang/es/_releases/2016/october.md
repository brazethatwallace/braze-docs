---
nav_title: Octubre
page_order: 3
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de octubre de 2016."
---

# Octubre de 2016 {#october-2016}

## Nueva configuración de seguridad {#new-security-settings}
Hemos añadido funciones de seguridad mejoradas a Braze, como reglas de caducidad de contraseñas, reglas de longitud de contraseñas, reglas de complejidad de contraseñas, listas de IP permitidas para iniciar sesión en el dashboard y autenticación de dos factores.

> Actualización: La **Configuración de seguridad** de Braze, a la que se accede desde la página **Configuración de empresa**, también incluye reglas para la reutilización y caducidad de contraseñas.

## Descarga CSV tras la importación {#csv-download-after-import}
Ahora los usuarios de la empresa pueden descargar CSV de usuarios importados recientemente. Esto te da más visibilidad en la sincronización de datos de tus sistemas. Más información sobre [la importación de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/).

## Filtro de aniversario {#anniversary-filter}
Además del [filtro de cumpleaños]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/), Braze ahora admite un filtro de aniversario que te ofrece la posibilidad de dirigirte a usuarios en función de una fecha del calendario para hitos de fidelización, avisos de recarga, ¡y mucho más! Accede a esta característica seleccionando el filtro "Date of Custom Attribute" en la página Segments. Más información sobre [los filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters).

## Actualizaciones de limitación de frecuencia {#frequency-capping-updates}
Antes, una campaña o Canvas que ignorara las restricciones de limitación de frecuencia seguía contando para los límites de frecuencia. Hemos cambiado el comportamiento para que, por defecto, las nuevas campañas y Canvas que no respeten los límites de frecuencia tampoco cuenten para ellos. Esto es configurable para cada campaña y Canvas. Más información sobre [la limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping).

## Perfiles de color de los mensajes dentro de la aplicación {#in-app-message-color-profiles}
Hemos añadido [perfiles de color]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) para los mensajes dentro de la aplicación, lo que permite a los clientes reutilizar los esquemas de color de la marca al crear nuevos mensajes en Braze.