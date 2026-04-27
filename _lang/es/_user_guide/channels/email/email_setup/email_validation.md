---
nav_title: Validación del correo electrónico
article_title: Validación de correo electrónico
alias: "/email_validation/"
page_order: 3
page_type: reference
description: "Este artículo de referencia cubre las reglas de validación de la parte local y del host para las direcciones de correo electrónico."
channel: email

---

# Validación del correo electrónico

> Este artículo de referencia cubre las reglas de validación de la parte local y del host para las direcciones de correo electrónico. La validación se utiliza para las direcciones de correo electrónico del panel, las direcciones de correo electrónico del usuario final (tus clientes) y las direcciones de origen y de responder a de un mensaje de correo electrónico.

## Cómo funciona

Braze valida una dirección de correo electrónico cuando se actualiza, se importa mediante API, se carga en formato CSV, se modifica mediante SDK o se modifica en el panel. Las direcciones de correo electrónico no pueden incluir espacios en blanco. Si usas la API, los espacios en blanco devuelven un error `400`.

Braze rechaza ciertos caracteres y marca la dirección como no válida. Si un correo electrónico rebota, Braze marca la dirección como no válida y no cambia el estado de la suscripción. Si el cuerpo del correo electrónico contiene caracteres [ASCII](https://en.wikipedia.org/wiki/ASCII) no estándar, Braze no envía el correo electrónico.

{% details Caracteres aceptados %}
- Letras (A-Z)
- Números (0-9)
- Símbolos
	- -
	- &#94;
	- +
	- $
	- '
	- &
	- #
	- /
	- %
	- *
	- =
	- `
	- |
	- ~
	- !
	- ?
	- . (sólo entre letras u otros caracteres)
{% enddetails %}

{% details Caracteres no aceptados %}
- Espacios en blanco (ASCII y Unicode)
{% enddetails %}

Esta validación es una comprobación de sintaxis, no un servicio de validación. Uno de los objetivos de este proceso es admitir caracteres internacionales (como UTF-8) en la parte local de la dirección de correo electrónico.

Braze valida la sintaxis tanto de la parte local como de la parte del host de una dirección de correo electrónico. La parte local es todo lo que está antes de la arroba (@); la parte del host es todo lo que está después. La parte local puede comenzar y terminar con cualquier carácter permitido excepto un punto (.). Este proceso no considera si el dominio tiene un servidor MX válido o si existe un usuario en ese dominio.

{% alert important %}
Si la parte del dominio contiene caracteres ASCII no estándar, deberá estar [codificada en Punycode](https://www.punycoder.com/) antes de proporcionarla a Braze.
{% endalert %}

Si Braze recibe una solicitud para agregar un usuario con una dirección de correo electrónico no válida, la API devuelve un error. Para una carga de CSV, Braze crea el usuario pero omite la dirección de correo electrónico no válida.

## Reglas de validación de la parte local

### Validación general de correo electrónico

Para la mayoría de los dominios, la parte local debe seguir estos parámetros:
- Puede contener cualquier letra, número, incluyendo letras y números Unicode, así como los siguientes caracteres: (+) (&) (#) (_) (-) (^) o (/)
- Puede contener, pero no puede comenzar ni terminar con el siguiente carácter: (.)
- No puede contener comillas dobles (")
- Debe tener entre 1 y 64 caracteres de longitud

La siguiente expresión regular se puede usar para validar si una dirección de correo electrónico se considerará válida:
```
/\A([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])(([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~\.]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])*([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}]))?\z/
```

### Direcciones de Gmail

Si la parte del dominio es Gmail, la parte local debe tener al menos dos caracteres de longitud y seguir la validación de expresión regular indicada anteriormente.

### Dominios de Microsoft

Si el dominio del host incluye "msn", "hotmail", "outlook" o "live", Braze utiliza la siguiente expresión regular para validar la parte local: `/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

La parte local de la dirección de Microsoft debe seguir estos parámetros:

- Puede comenzar con un carácter (a-z), un guion bajo (_) o un número (0-9).
- Puede contener cualquier carácter alfanumérico (a-z o 0-9) o un guion bajo (_)
- Puede contener los siguientes caracteres: (.) o (-)
- No puede comenzar con un punto (.)
- No puede contener dos o más puntos consecutivos (.)
- No puede terminar con un punto (.)

La prueba de validación verifica si la parte local que precede al "+" coincide con la expresión regular.

## Reglas de validación de la parte del host

La parte del host no puede ser una dirección IPv4 o IPv6. El dominio de nivel superior (como .com, .org, .net) no puede ser completamente numérico.

La siguiente expresión regular se utiliza para validar el dominio:<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

El nombre de dominio debe cumplir estos parámetros:

- Consta de dos o más etiquetas separadas por puntos
	- Cada parte de un nombre de dominio se denomina "etiqueta". Por ejemplo, el nombre de dominio "example.com" consta de la etiqueta "example" y la etiqueta "com".
- Debe contener al menos un punto (.)
- No puede contener dos o más puntos consecutivos
- Cada etiqueta separada por puntos debe:
	- Contener solo caracteres alfanuméricos (a-z o 0-9) y el guion (-)
	- Comenzar con un carácter alfanumérico (a-z o 0-9)
	- Terminar con un carácter alfanumérico (a-z o 0-9)
	- Contener de 1 a 63 caracteres

### Validación adicional requerida

La etiqueta final del dominio debe ser un dominio de nivel superior (TLD) válido, determinado por todo lo que está después del último punto (.). Este TLD debe aparecer en la [lista de TLD de ICANN](https://data.iana.org/TLD/tlds-alpha-by-domain.txt). El validador de Braze solo verifica la sintaxis. No detecta errores tipográficos ni direcciones inexistentes.

{% alert important %}
Unicode se acepta solo para la parte local de la dirección de correo electrónico. Unicode no se acepta para la parte del dominio, pero puede estar codificado en Punycode.
{% endalert %}