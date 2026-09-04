---
nav_title: Enlaces para añadir al calendario
article_title: Enlaces para añadir al calendario
page_order: 1
page_type: tutorial
description: "Este artículo describe cómo incluir un enlace para añadir al calendario en tus campañas de correo electrónico."
channel: email

---

# Enlaces para añadir al calendario {#add-to-calendar-links}

> Al promocionar un evento, una oferta o una cita, puedes ayudar a los usuarios a guardar fácilmente el evento en su calendario añadiendo un enlace "añadir al calendario" a tus correos electrónicos.

Redacta tu correo electrónico y elige dónde aparecerán las dos opciones de calendario: un enlace para Google Calendar y otro para otros calendarios (como iCal o Outlook). Usa un texto de enlace como "Añadir a Google Calendar" y "Añadir a iCal o Outlook".

La forma de adjuntar las URL depende del editor de correo electrónico que utilices:

- **Editor de arrastrar y soltar:** En un bloque **Paragraph**, selecciona las palabras que deseas enlazar, abre el control **Link** en la barra de herramientas y pega la URL del [formato de URL](#url-format). También puedes usar un bloque **Button**, configurar **Link type** en **Open web page** y pegar la URL en **URL**.
- **Editor HTML:** Usa los controles de enlace de texto enriquecido para el texto enlazado, o añade etiquetas `<a href="...">` en tu HTML para cada URL de calendario.

## Formato de URL {#url-format}

Añade la siguiente URL a tus enlaces, reemplazando los marcadores de posición. La única diferencia entre estas dos URL es que Google Calendar necesita un parámetro adicional: `&format=gcal`.

{% tabs %}
{% tab Google Calendar %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCal o Outlook %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION
```

{% endtab %}
{% endtabs %}

Reemplaza lo siguiente:

- `EVENT_SUBJECT`: Título del evento
- `EVENT_LOCATION`: Ubicación del evento
- `START_TIME`: La hora de inicio del evento en formato ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) como UTC
- `END_TIME`: La hora de finalización del evento en formato ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) como UTC
- `EVENT_DESCRIPTION`: Descripción del evento

Reemplaza los espacios con el código de escape HTML `%20`. Por ejemplo, un asunto de "Meet Braze" sería "Meet%20Braze".

Aquí tienes un ejemplo de una URL de "Añadir a Google Calendar":

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### Parámetros adicionales {#additional-parameters}

Los siguientes parámetros son opcionales y se pueden usar para definir aspectos adicionales de un evento.

- **Nombre del organizador:** `&organizer=name`
- **Adjuntar URL relacionada con el evento:** `&attach=http://www.example.com/`
- **Duración:** `duration=30M`, como alternativa a la hora de finalización del evento (dtend), especifica una duración como 1H o 30M
- **Hora de alarma del recordatorio, en minutos:** `&reminder=15`
- **Evento de todo el día:** `&allday=1`
- **UID:** parámetro opcional para codificar de forma fija el identificador único del evento, lo que permite a algunas aplicaciones de calendario actualizar el evento con el tiempo. La cadena @ics.agical.io se añade automáticamente al valor.

También puedes añadir parámetros adicionales para eventos recurrentes:
- **Eventos semanales:** `&recur=weekly`
- **Eventos mensuales:** `&recur=monthly`
- **Fin de la recurrencia:** `&recuruntil=END_DATE`, donde `END_DATE` es la fecha y hora en que finaliza la recurrencia en formato ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) como UTC

## Comportamiento del enlace {#link-behavior}

Cuando un usuario hace clic en el enlace, los calendarios transforman automáticamente las marcas de tiempo UTC en las URL para reflejar la zona horaria del usuario configurada en su calendario.

Por ejemplo, si abres el enlace de ejemplo "Añadir a Google Calendar" y tu calendario está configurado en CST, la hora del evento se rellenará previamente según lo que sean las 3 pm UTC en CST (10 am).

### Google Calendar {#google-calendar}

Al hacer clic, Google Calendar se abre en una nueva pestaña o ventana con los detalles del evento prerrellenados en la invitación y listos para que el usuario los guarde. Esto ocurre tanto en dispositivos móviles como en escritorio.

![Cuadro de diálogo de Google Calendar para añadir un evento con los detalles del evento agregados y listos para guardar.]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal o Outlook {#ical-or-outlook}

Al hacer clic en escritorio, se descarga un archivo ICS en la ubicación de descarga predeterminada de tu navegador (normalmente la carpeta **Descargas**). El usuario luego necesita abrir el archivo ICS, lo que abre iCal o Outlook y solicita al usuario que añada el evento a su calendario.

![Calendario de iCal con un cuadro de diálogo para añadir un nuevo evento, que solicita al usuario seleccionar un calendario y confirmar.]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

![Calendario de iCal con el evento añadido.]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

En dispositivos móviles, el comportamiento depende del dispositivo y la aplicación de correo electrónico.

{% alert note %}
En iPhone, la aplicación Mail y Microsoft Outlook descargan el archivo ICS en el dispositivo cuando los usuarios pulsan el enlace de iCal, pero esas aplicaciones no abren Calendario desde el enlace. Para añadir el evento, abre el archivo descargado desde **Archivos**, **Descargas** o la vista de adjuntos (según la aplicación), y luego completa los pasos en Calendario. La ubicación específica depende de la aplicación de correo electrónico y la configuración de iOS.
{% endalert %}

En algunas otras aplicaciones de correo electrónico o navegadores móviles, mantener presionado el enlace puede mostrar una opción para añadir el evento a un calendario.

![Ventana emergente de iOS al mantener presionado un enlace de calendario, que incluye un botón para "Añadir al calendario".]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

Para más información, consulta:
* [Crear eventos para Google Calendar](https://developers.google.com/calendar/api/guides/create-events)
* [Crear un enlace de Añadir al calendario en un mensaje de correo electrónico](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)