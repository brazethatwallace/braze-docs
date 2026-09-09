---
nav_title: Entrega de mensajes dentro de la aplicación en tiempo real
article_title: Entrega de mensajes dentro de la aplicación en tiempo real
permalink: "/real_time_in_app_messages/"
description: "Esta página cubre el acceso anticipado a la entrega de mensajes dentro de la aplicación en tiempo real, que entrega mensajes dentro de la aplicación a un dispositivo tan pronto como un usuario se vuelve elegible, en lugar de esperar al próximo inicio de sesión."
page_type: reference
hidden: true
noindex: true
---

# Entrega de mensajes dentro de la aplicación en tiempo real {#real-time-in-app-message-delivery}

> Con la entrega en tiempo real, Braze envía un mensaje dentro de la aplicación al dispositivo tan pronto como el usuario se vuelve elegible para recibirlo. Los usuarios ya no necesitan iniciar una nueva sesión para recibir un mensaje dentro de la aplicación para el que se volvieron elegibles a mitad de sesión.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Real-time in-app message delivery' type='early_access' %}

## Cómo funciona {#how-it-works}

Sin la entrega en tiempo real, el SDK solicita los mensajes dentro de la aplicación elegibles al inicio de la sesión y los almacena en caché en el dispositivo. Un usuario que se vuelve elegible a mitad de una sesión no recibe el mensaje hasta que comienza su siguiente sesión. Para obtener más información sobre este comportamiento, consulta [Desencadenar mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages).

Con la entrega en tiempo real, Braze envía el mensaje al dispositivo a través de una conexión en vivo que el SDK mantiene durante la sesión. Braze envía un mensaje en dos casos:

- Un usuario se vuelve elegible para una Campaign de mensaje dentro de la aplicación.
- Un usuario avanza a un paso de mensaje dentro de la aplicación en un Canvas.

La entrega en tiempo real cambia cuándo llega un mensaje al dispositivo. El comportamiento de visualización sigue siendo el mismo: el mensaje espera a su evento desencadenante antes de aparecer.

### Qué significa esto para tus Campaigns {#what-this-means-for-your-campaigns}

| Escenario | Sin entrega en tiempo real | Con entrega en tiempo real |
| --- | --- | --- |
| Un usuario se vuelve elegible para una Campaign de mensaje dentro de la aplicación a mitad de sesión | El mensaje llega al inicio de la siguiente sesión | El mensaje llega durante la sesión actual |
| Un usuario alcanza un paso de mensaje dentro de la aplicación en un Canvas a mitad de sesión | El mensaje llega al inicio de la siguiente sesión | El mensaje llega durante la sesión actual |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comparación de la entrega de mensajes dentro de la aplicación en tiempo real" }

## Requisitos del SDK {#sdk-requirements}

La entrega en tiempo real requiere las siguientes versiones mínimas del SDK:

{% sdk_min_versions swift:18.0.0 android:43.1.1 web:6.12.0 %}

Los dispositivos continúan recibiendo mensajes dentro de la aplicación al inicio de la sesión, independientemente de la versión del SDK.

## Limitaciones actuales {#current-limitations}

- **Las ediciones a una campaña en vivo se aplican en el próximo inicio de sesión:** Si cambias un mensaje dentro de la aplicación que un dispositivo ya ha recibido, ese dispositivo conserva la versión que tiene hasta que comience la próxima sesión del usuario.

## Participar en el acceso anticipado {#participate-in-early-access}

1. Ponte en contacto con tu director de cuentas de Braze para que añadan tu espacio de trabajo al acceso anticipado.
2. Actualiza tu aplicación a la versión mínima del SDK para tu plataforma.
3. Publica la aplicación actualizada para tus usuarios.

La entrega en tiempo real no requiere configuración en el panel, cambios en Campaigns ni cambios en el código del SDK. Una vez que tu espacio de trabajo se añada al acceso anticipado, la entrega en tiempo real se aplica a tus Campaigns de mensajes dentro de la aplicación y Canvas existentes.

## Comparte tus comentarios {#share-feedback}

Braze está desarrollando activamente esta característica, y tus comentarios influyen en lo que se incluirá en la disponibilidad general. Envía a tu director de cuentas tus observaciones sobre los tiempos de entrega, cualquier cosa que se haya comportado de manera diferente a lo esperado y los escenarios que te gustaría que la entrega en tiempo real cubriera a continuación.