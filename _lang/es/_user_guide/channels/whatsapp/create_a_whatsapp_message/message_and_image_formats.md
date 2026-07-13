---
nav_title: Formatos de mensajes e imágenes
article_title: Formatos de mensajes e imágenes de WhatsApp
description: "Este artículo de referencia cubre la estructura de los mensajes, los límites de los componentes y los requisitos de activos multimedia para crear mensajes y plantillas de WhatsApp."
alias: /whatsapp_media_formats/
page_order: 9
channel:
  - WhatsApp
---

# Formatos de mensajes e imágenes de WhatsApp {#whatsapp-message-and-image-formats}

> Aquí encontrarás los requisitos de estructura de mensajes, componentes y activos multimedia para crear mensajes y plantillas de WhatsApp.

Hay dos tipos de mensajes de WhatsApp en Braze: [mensajes de plantilla](#template-messages) y [mensajes de respuesta](#response-messages).

| Tipo de mensaje | Cuándo se usa | Aprobación de Meta |
|---|---|---|
| Mensajes de plantilla | Comunicación iniciada por la empresa; se envían en cualquier momento | Obligatoria; las plantillas deben enviarse a Meta y aprobarse antes del envío. |
| Mensajes de respuesta | Respuestas a mensajes iniciados por el usuario; solo dentro de la ventana de conversación de 24 horas | No obligatoria |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Formatos de mensajes e imágenes de WhatsApp" }

Los mensajes de plantilla deben enviarse a Meta para su aprobación, lo que puede tardar hasta 24 horas. Una vez aprobados, se pueden enviar en cualquier momento. Los mensajes de respuesta (llamados "mensajes de sesión" en la documentación de Meta) solo se pueden enviar mientras haya una ventana de conversación activa abierta, es decir, dentro de las 24 horas posteriores al último mensaje entrante del usuario.

## Mensajes de plantilla {#template-messages}

Los mensajes de plantilla de WhatsApp son formatos de mensaje preaprobados que se utilizan para la comunicación iniciada por la empresa. En Braze, se construyen a partir de componentes que defines antes de enviarlos a Meta. Todos los mensajes de plantilla se basan en categorías: marketing, utilidad o autenticación.

### Plantillas de marketing {#marketing-templates}

Las plantillas de marketing son el tipo más común utilizado en Braze. Constan de hasta cuatro componentes:

| Componente | Obligatorio | Notas |
|---|---|---|
| Encabezado | No | Admite texto, imagen, video, documento o ubicación. Consulta las [especificaciones multimedia](#media-specifications) para los requisitos de tipo de archivo, tamaño y dimensiones. |
| Cuerpo | Sí | El contenido principal del mensaje |
| Pie de página | No | Texto complementario que se muestra debajo del cuerpo |
| Botones | No | Incluye hasta 10 botones (se admiten todos los tipos de botones) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Plantillas de marketing" }

#### Longitud de caracteres {#character-length}

| Componente | Longitud máxima de caracteres |
|---|---|
| Cuerpo | 1024 caracteres |
| Pie de página | 60 caracteres |
| Etiqueta de botón (URL, teléfono, respuesta rápida) | 25 caracteres |
| Número de teléfono (en botón de teléfono) | 20 caracteres |
| Nombre de plantilla | 512 caracteres (solo minúsculas, alfanuméricos y guiones bajos) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Longitud de caracteres" }

#### Tipos de botones {#button-types}

| Tipo de botón | Comportamiento | Notas |
|---|---|---|
| Respuesta rápida | Envía el texto de la etiqueta del botón como respuesta en la conversación | |
| URL | Abre una URL en el navegador predeterminado del usuario; admite 1 variable añadida al final de la URL (máximo 2000 caracteres) | |
| Número de teléfono | Inicia una llamada al número de teléfono especificado | |
| Copiar código de cupón | Copia un código de cupón al portapapeles del usuario | Siempre requiere aprobación de Meta |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipos de botones" }

#### Formato de parámetros {#parameter-formatting}

Las variables de plantilla pueden usar parámetros con nombre (como {% raw %}`{{first_name}}`{% endraw %}) o parámetros posicionales (como {% raw %}`{{1}}`{% endraw %}). En Braze, las variables se pueden reemplazar con Liquid o texto plano. Incluye siempre valores predeterminados para las variables Liquid; los mensajes con valores de variables faltantes no se enviarán.

### Plantillas de carrusel con tarjetas multimedia {#media-card-carousel-templates}

Las plantillas de carrusel muestran un cuerpo de mensaje seguido de 2 a 10 tarjetas de producto desplazables horizontalmente, cada una con su propio activo multimedia y botones. Solo están disponibles para mensajes de plantilla de marketing.

#### Mensaje de nivel superior {#top-level-message}

| Componente | Obligatorio | Propiedades máximas | Notas |
|---|---|---|---|
| Texto del cuerpo | Sí | 1024 caracteres | Admite variables |
| Tarjetas | Sí | 2-10 tarjetas | El número de tarjetas se fija en la creación de la plantilla. Una plantilla de carrusel aprobada solo se puede enviar con el número exacto de tarjetas definido durante la creación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Mensaje de nivel superior" }

#### Especificaciones por tarjeta {#per-card-specifications}

| Componente | Obligatorio | Notas |
|---|---|---|
| Encabezado (imagen o video) | Sí | Todas las tarjetas deben usar el mismo formato (todas imagen o todas video). Esto incluye la misma estructura de componentes; no puedes mezclar tarjetas con y sin texto del cuerpo o botones.<br><br> Los activos del encabezado de la tarjeta se recortan automáticamente a una proporción ancha según el dispositivo del usuario. |
| Texto del cuerpo | No | Si alguna tarjeta incluye texto del cuerpo, todas las tarjetas deben incluir texto del cuerpo |
| Botones | No | Máximo 2 botones por tarjeta |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Especificaciones por tarjeta" }

#### Longitud de caracteres por tarjeta {#per-card-character-lengths}

| Componente | Longitud máxima de caracteres | Notas |
|---|---|---|
| Texto del cuerpo de la tarjeta | 160 caracteres | |
| Etiqueta de botón | 25 caracteres | |
| Número de teléfono (en botón de teléfono) | 20 caracteres | |
| URL (en botón de URL) | 2000 caracteres; admite 1 variable añadida al final | Los botones de URL se abren en el navegador predeterminado del usuario, fuera de WhatsApp. No se activan webhooks de pedidos ni de conversión a partir de ese punto. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Longitud de caracteres por tarjeta" }

## Mensajes de respuesta {#response-messages}

Los mensajes de respuesta (también llamados "mensajes de sesión" por Meta) solo se pueden enviar dentro de la ventana de conversación de 24 horas. Se abren y se reinician cuando un usuario envía un mensaje a tu empresa.

Los mensajes de respuesta que se redactan directamente en el editor de Campaign o Canvas de Braze no requieren aprobación de Meta.

Braze admite siete diseños de mensajes de respuesta:

| Diseño de mensaje | Descripción |
|---|---|
| Texto | Texto del cuerpo del mensaje en texto plano |
| Multimedia | Mensaje con un adjunto de imagen, video, audio o documento |
| Respuesta rápida | Mensaje con hasta 3 botones de respuesta que se pueden tocar |
| Botón de llamada a la acción (CTA) | Mensaje con un botón de URL o un botón de número de teléfono |
| Mensaje de lista | Mensaje con una lista estructurada y desplazable de opciones seleccionables |
| Mensaje de flujo | Mensaje que solicita a los usuarios completar un formulario o tarea interactiva en WhatsApp, con el resultado regresando a Braze |
| Mensaje de producto de Meta | Mensaje que destaca un solo producto, múltiples productos o un catálogo completo de un catálogo de Meta conectado |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mensajes de respuesta" }

### Componentes de mensaje de lista {#list-message-components}

| Componente | Propiedades máximas |
|---|---|
| Texto del cuerpo | 4096 caracteres |
| Etiqueta de botón (para abrir la lista) | 20 caracteres |
| Número de secciones | Hasta 10 |
| Número de filas por sección | Hasta 10 |
| Título de sección | 24 caracteres |
| Título de fila | 24 caracteres |
| Descripción de fila | 72 caracteres |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Componentes de mensaje de lista" }

### Componentes de respuesta rápida {#quick-reply-components}

| Componente | Propiedades máximas |
| --- | --- |
| Botón | Hasta 3 |
| Etiqueta de botón | 20 caracteres por botón |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Componentes de respuesta rápida" }

## Especificaciones multimedia {#media-specifications}

Las siguientes especificaciones se aplican a todos los archivos multimedia en encabezados de plantillas de WhatsApp, mensajes de respuesta o mensajes multimedia independientes.

{% multi_lang_include alerts/important_alerts.md alert='WhatsApp audio and documents' %}

### Imágenes {#images}

{% multi_lang_include channels/image_specs.md variable_name='WhatsApp images' %}

### Video {#video}

{% multi_lang_include channels/image_specs.md variable_name='WhatsApp videos' %}

#### Compatibilidad con Android {#android-compatibility}

El perfil H.264 "High" codificado con B-frames no es compatible con los clientes de WhatsApp en Android. Usa el perfil H.264 "Main" sin B-frames o el perfil "Baseline" para la mayor compatibilidad. Si recodificas con ffmpeg, usa la bandera `-movflags faststart` para colocar los bloques `moov` antes de los bloques `mdat`.

### Audio {#audio}

Las siguientes especificaciones se aplican a los mensajes multimedia de respuesta y a los mensajes de audio, y se basan en su tipo de audio: mensaje de voz o mensaje de audio básico.

#### Mensaje de voz {#voice-message}

Un mensaje de voz funciona como una nota de voz grabada, con controles de reproducción y soporte de transcripción.

| Propiedad | Especificaciones |
|---|---|
| Formato obligatorio | Solo OGG |
| Códec obligatorio | Solo OPUS (entrada mono) |
| Tamaño de archivo | Máximo 16 MB |
| Icono de reproducción | Este icono solo aparece si el archivo es de 512 KB o menos; los archivos más grandes muestran un icono de descarga |
| Transcripción | Se muestra automáticamente si el usuario tiene habilitadas las transcripciones de voz de WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mensaje de voz" }

#### Mensaje de audio básico {#basic-audio-message}

Las siguientes especificaciones se aplican al uso compartido de archivos de audio estándar (clips de música, anuncios de audio y archivos de sonido).

| Formato | Extensión | Tamaño máximo de archivo | Notas |
|---|---|---|---|
| AAC | .aac | 16 MB | |
| AMR | .amr | 16 MB | |
| MP3 | .mp3 | 16 MB | |
| MP4 Audio | .m4a | 16 MB | |
| OGG (códec OPUS) | .ogg | 16 MB | Los archivos OGG deben usar el códec OPUS. El formato base `audio/ogg` sin OPUS no es compatible.<br><br> Los archivos OGG/OPUS enviados como mensajes de audio básicos mostrarán un icono de micrófono (igual que los mensajes de voz) en lugar de un icono de música. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Mensaje de audio básico" }

#### Consideraciones {#considerations}

{% multi_lang_include alerts/important_alerts.md alert='WhatsApp audio and documents' %}

- No hay soporte de subtítulos para mensajes de audio.
- Un error común son los tipos MIME no coincidentes. Verifica que el tipo MIME de tu archivo coincida con su extensión antes de enviarlo.

### Documentos {#documents}

Las siguientes especificaciones se aplican a los encabezados de plantillas (formato de documento), mensajes multimedia de respuesta y mensajes de documentos.

| Tipo de documento | Tipos de archivo | Tamaño máximo de archivo |
|---|---|---|
| PDF | PDF | 100 MB |
| Microsoft Word | DOC, DOCX | 100 MB |
| Microsoft Excel | XLS, XLSX | 100 MB |
| Microsoft PowerPoint | PPT, PPTX | 100 MB |
| Texto plano | TXT | 100 MB |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Documentos" }

#### Consideraciones

{% multi_lang_include alerts/important_alerts.md alert='WhatsApp audio and documents' %}

- Los subtítulos son opcionales y pueden tener un máximo de 1024 caracteres.
- El nombre de archivo es opcional. WhatsApp usa la extensión del archivo para determinar qué icono de documento mostrar en la conversación.
- Solo los formatos listados son oficialmente compatibles. Otros tipos de archivo pueden enviarse, pero no se garantiza que se muestren correctamente en WhatsApp.

## Referencia rápida: especificaciones multimedia de WhatsApp {#quick-reference-whatsapp-media-specifications}

| Tipo de multimedia | Tipos de archivo | Tamaño máximo de archivo | Disponibilidad de subtítulos |
|---|---|---|---|
| Imagen | JPEG, PNG | 5 MB | Sí (máximo 1024 caracteres) |
| Video | MP4, 3GPP | 16 MB | Sí (máximo 1024 caracteres) |
| Audio (voz) | OGG (OPUS) | 16 MB | No |
| Audio (básico) | AAC, AMR, MP3, M4A, OGG | 16 MB | No |
| Documento | PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, TXT | 100 MB | Sí (máximo 1024 caracteres) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Referencia rápida: especificaciones multimedia de WhatsApp" }