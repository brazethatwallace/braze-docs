---
nav_title: Enlaces para añadir al calendario
article_title: Enlaces para añadir al calendario
page_order: 1
page_type: tutorial
description: "Este artículo describe cómo incluir un enlace para añadir al calendario en tus campañas de correo electrónico."
channel: email

---

# Enlaces para añadir al calendario

> Al promocionar un evento, una oferta o una cita, puedes ayudar a los usuarios a guardar fácilmente el evento en su calendario añadiendo un enlace "añadir al calendario" a tus correos electrónicos.

Para hacerlo, redacta tu correo electrónico y determina dónde quieres colocar tus enlaces. Luego añade dos opciones: una para Google Calendar y otra para otros calendarios (como iCal o Outlook). Por ejemplo, "Añadir a Google Calendar" y "Añadir a iCal o Outlook".

![Cuadro de diálogo de enlace al añadir un enlace en el dashboard. La pestaña "Link Info" está seleccionada y el texto está configurado como "Add to Google Calendar".]({% image_buster /assets/img_archive/calendar_1.png %}){: style="max-width:50%"}

## Formato de URL

Añade la siguiente URL a tus enlaces, reemplazando los marcadores de posición. La única diferencia entre estas dos URLs es que Google Calendar necesita un parámetro adicional: `&format=gcal`.

{% tabs %}
{% tab Google Calendar %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCal or Outlook %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION
```

{% endtab %}
{% endtabs %}

Reemplaza lo siguiente:

- `EVENT_SUBJECT`: Título del evento
- `EVENT_LOCATION`: Ubicación del evento
- `START_TIME`: Hora de inicio del evento en formato ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) en UTC
- `END_TIME`: Hora de finalización del evento en formato ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) en UTC
- `EVENT_DESCRIPTION`: Descripción del evento

Reemplaza los espacios con el código de escape HTML `%20`. Por ejemplo, un asunto de "Meet Braze" sería "Meet%20Braze".

Aquí tienes un ejemplo de una URL "Añadir a Google Calendar":

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### Parámetros adicionales

Los siguientes parámetros son opcionales y se pueden usar para definir aspectos adicionales de un evento.

- **Nombre del organizador:** `&organizer=name`
- **Adjuntar URL relacionada con el evento:** `&attach=http://www.example.com/`
- **Duración:** `duration=30M`, como alternativa a la hora de finalización del evento (dtend), especifica una duración como 1H o 30M
- **Hora de alarma de recordatorio, en minutos:** `&reminder=15`
- **Evento de todo el día:** `&allday=1`
- **UID:** parámetro opcional para codificar de forma fija el identificador único del evento, lo que permite a algunas aplicaciones de calendario actualizar el evento con el tiempo. La cadena @ics.agical.io se añade automáticamente al valor.

También puedes añadir parámetros adicionales para eventos recurrentes:
- **Eventos semanales:** `&recur=weekly`
- **Eventos mensuales:** `&recur=monthly`
- **Fin de la recurrencia:** `&recuruntil=END_DATE`, donde `END_DATE` es la fecha y hora en que termina la recurrencia en formato ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) en UTC

## Comportamiento del enlace

Cuando un usuario hace clic en el enlace, los calendarios transforman automáticamente las marcas de tiempo UTC en las URLs para reflejar la zona horaria del usuario configurada en su calendario.

Por ejemplo, si abres el enlace de ejemplo "Añadir a Google Calendar" y tu calendario está configurado en CST, la hora del evento se completará automáticamente según lo que las 3 pm UTC representan en CST (10 am).

### Google Calendar

Al hacer clic, Google Calendar se abre en una nueva pestaña o ventana con los detalles del evento completados previamente en la invitación y listos para que el usuario los guarde. Esto ocurre tanto en móvil como en escritorio.

![Cuadro de diálogo de Google Calendar para añadir un evento con los detalles del evento completados y listos para guardar.]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal o Outlook

Al hacer clic en escritorio, se descarga un archivo ICS. El usuario luego necesita abrir el archivo ICS, lo que abrirá iCal o Outlook y le pedirá que añada el evento a su calendario.

![Calendario de iCal con un cuadro de diálogo para añadir un nuevo evento, que solicita al usuario seleccionar un calendario y confirmar.]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

![Calendario de iCal con el evento añadido.]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

En móvil, los usuarios necesitan mantener presionado el enlace, lo que les pedirá que lo añadan a su calendario.

![Ventana emergente de iOS al mantener presionado un enlace de calendario, que incluye un botón para "Añadir al calendario".]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

Para más información, consulta:
* [Create events for Google Calendar](https://developers.google.com/calendar/api/guides/create-events)
* [Create an Add to calendar link in an email message](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)