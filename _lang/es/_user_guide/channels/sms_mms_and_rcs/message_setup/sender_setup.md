---
nav_title: Configuración de remitentes
article_title: Remitentes de SMS, MMS y RCS
page_order: 2
description: "Este artículo ofrece un resumen de los códigos y remitentes disponibles para enviar mensajes SMS, MMS y RCS."
page_type: reference
alias: /sending_phone_numbers/
channel:
  - SMS
  - MMS
  - RCS
---

{% multi_lang_include channels/sms/short_and_long_codes.md %}

## Requisitos específicos de MMS {#mms-specific-requirements}

### Requisitos de remitente MMS {#mms-sender-requirements}

> MMS y SMS están vinculados al canal SMS de Braze. Para acceder a MMS en tu cuenta, es necesario adquirir SMS para quienes aún no lo hayan hecho. Los clientes existentes de SMS pueden acceder a MMS después de adquirirlo.

MMS es compatible actualmente con códigos abreviados de EE. UU. (números de 5-6 dígitos), códigos largos de EE. UU. y CA (números de 10 dígitos) y números de clientes de EE. UU. y Canadá. MMS es compatible con números gratuitos a través de ciertos proveedores de servicios.

Es posible enviar MMS a números fuera de EE. UU. y Canadá, pero los mensajes MMS se convertirán en un mensaje SMS con un enlace al activo multimedia.

### Códigos abreviados MMS {#mms-short-codes}

Algunos usuarios pueden no implementar o usar códigos abreviados MMS, pero estarán disponibles si se necesitan en una fecha posterior.

Para los usuarios que obtuvieron sus códigos abreviados antes de que Braze fuera compatible con MMS, todos los clientes existentes con códigos abreviados de EE. UU. son elegibles para habilitar MMS de forma instantánea. Ponte en contacto con tu administrador del éxito del cliente si esta situación aplica para ti y deseas que se habilite MMS.

{% alert important %}
Al habilitar MMS para códigos abreviados que anteriormente no tenían MMS habilitado, es posible que los códigos abreviados necesiten ser aprobados nuevamente en un proceso de aprobación que podría tardar semanas. Es importante tener en cuenta este plazo al decidir habilitar MMS.
{% endalert %}

#### Mejores prácticas para códigos abreviados MMS {#mms-short-code-best-practices}

- En Braze, recomendamos encarecidamente mantener la mensajería transaccional y la promocional separadas, cada una con códigos abreviados diferentes. Dado que MMS está vinculado al canal SMS, y el canal SMS está altamente regulado, los clientes podrían verse obligados a pagar una penalización monetaria por el uso indebido del canal y que su código abreviado sea suspendido (lo cual es irreversible). Mantener la mensajería transaccional y la promocional vinculadas a códigos abreviados diferentes protege su mensajería transaccional.
- Si los clientes ya tienen un código abreviado dedicado a la mensajería promocional, y tiene MMS habilitado, no necesitan un código abreviado separado para MMS.

### Códigos largos MMS {#mms-long-codes}

Los clientes pueden enviar MMS con códigos largos. Para hacerlo, debes asegurarte de que tus códigos largos tengan MMS habilitado. Esto se puede hacer inicialmente durante la configuración, o más adelante desde tu cuenta.

Los mensajes MMS no se pueden enviar con un ID de remitente alfanumérico.

### Límites de mensajes MMS y rendimiento {#mms-message-limits-and-throughput}

El rendimiento de MMS es de un segmento por segundo a través de un código largo.

Los operadores imponen sus propios límites de tamaño de archivo, que determinan el éxito de los envíos MMS. Estos límites pueden variar según la geografía y el operador, por lo que Braze recomienda no exceder los 600&nbsp;KB para tu activo multimedia e incluir también un cuerpo de mensaje. También recomendamos hacer pruebas para confirmar que tu contenido multimedia puede entregarse a través de los operadores de tus usuarios.

#### Límites de tamaño de archivo por operador {#carrier-file-size-limits}

| Tamaño&nbsp;de&nbsp;archivo | Manejo del operador |
| --- | --- |
| 300&nbsp;KB | Todos los operadores deberían manejar de forma fiable los mensajes MMS de este tamaño. |
| 600&nbsp;KB | Este se considera el tamaño máximo estándar de archivo para MMS en la mayoría de los operadores. |
| 1&nbsp;MB | La mayoría de los operadores de EE. UU. y Canadá pueden manejar mensajes MMS de este tamaño, aunque esto puede variar según el operador. Algunos operadores pueden permitir tamaños de archivo mayores. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Límites de tamaño de archivo por operador" }

#### Tipos de archivo aceptados {#accepted-file-types}

Braze acepta archivos JPEG, GIF, PNG y VCF, y te permite adjuntar un único activo multimedia a tu mensaje MMS.