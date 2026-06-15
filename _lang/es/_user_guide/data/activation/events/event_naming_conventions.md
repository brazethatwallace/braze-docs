---
nav_title: Convenciones de nomenclatura de eventos
article_title: Convenciones para nombrar eventos
page_order: 4
page_type: reference
description: "Este artículo de referencia cubre las convenciones de nomenclatura de eventos adecuadas y las mejores prácticas."

---

# Convenciones de nomenclatura de eventos {#event-naming-conventions}

> Esta página trata de las convenciones adecuadas para nombrar los eventos y de las mejores prácticas. Al mantener la coherencia en tu taxonomía de eventos y atributos, mantendrás tus datos limpios y utilizables para los usuarios nuevos y existentes de la plataforma Braze. Esto ayuda a evitar problemas posteriores, como desencadenar una campaña a la audiencia equivocada o generar resultados erróneos tras utilizar el evento equivocado.

## Buenas prácticas {#best-practices}

- Mantén clara tu convención de nomenclatura.
- Los nombres de los eventos deben escribirse y formatearse con coherencia.
- Evita dar nombres similares a los eventos.
- Evita las cadenas largas de atributos de eventos, que se truncarán o cortarán en el dashboard de Braze.

## Convenciones de denominación {#naming-conventions}

### Utiliza grupos de eventos {#use-event-groups}

Utiliza grupos para diferenciar las partes de tu producto al nombrar eventos. Al categorizar tu producto en grupos, cualquier usuario puede entender claramente a qué se refiere el evento y qué hace.

### Estructura de nomenclatura de eventos {#event-naming-structure}

La estructura de nombres más común es `group_noun_action`. Los eventos deben ir todos en minúsculas para evitar errores de instrumentación e identificación de propiedades.

### Propiedades {#properties}

Etiqueta un evento y luego identifica las diferencias mediante el uso de propiedades. Esto es útil para eventos que son inherentemente iguales pero tienen diferencias menores, como los canales de una campaña. También podemos ver fácilmente cómo los usuarios fluyen a través de los eventos. Consulta el [objeto de propiedades del evento]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) para ver un ejemplo y contexto adicional.

## Ejemplos {#examples}

Supongamos que formas parte de una empresa de comercio electrónico y te interesa hacer seguimiento de cuándo los clientes se han registrado en tu aplicación y cuándo se han suscrito a tu boletín. Aquí tienes ejemplos de nombres de eventos efectivos:

- `user_signup`
- `newsletter_subscribed`

Estos dos nombres de eventos indican claramente el evento que están rastreando. A medida que crees más eventos personalizados, asegúrate de mantener tus convenciones de nomenclatura comprensibles. Por ejemplo, evita usar nombres de eventos como `signup_event_1`, ya que carece de claridad y no transmite qué está rastreando el evento, en comparación con `user_signup`.