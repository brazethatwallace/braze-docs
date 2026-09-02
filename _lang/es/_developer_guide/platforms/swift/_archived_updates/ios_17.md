---
nav_title: Guía de actualización a iOS 17
article_title: Guía de actualización a iOS 17
page_order: 7
platform:
  - iOS
description: "Este artículo contiene información sobre la versión iOS 17 para ayudarte a actualizar tu SDK fácilmente."
hidden: true
noindex: true
---

# Guía de actualización a iOS 17 {#ios-17-upgrade-guide}

> ¿Tienes curiosidad por saber cómo se está preparando Braze para el próximo lanzamiento de iOS? Este artículo resume nuestra información sobre la versión iOS 17 para ayudarte a crear una experiencia fluida para ti y tus usuarios.

## Compatibilidad con iOS 17 y Xcode 15 {#ios-17-and-xcode-15-compatibility}

Tanto el SDK Swift como el SDK Objective-C de Braze son retrocompatibles con Xcode 14 y Xcode 15, y compatibles con dispositivos iOS 17.

## Cambios en iOS 17 {#changes-in-ios-17}

### Seguimiento de enlaces y eliminación de parámetros UTM {#link-tracking-and-utm-parameter-stripping}

Uno de los cambios importantes de iOS 17 es el bloqueo de los parámetros UTM en Safari. Los parámetros UTM son fragmentos de código que se añaden a las URL y que se utilizan con frecuencia en las campañas de marketing para medir la eficacia del correo electrónico, los SMS y otros canales de mensajería.

Este cambio no afecta al seguimiento de clics por correo electrónico de Braze ni a los envíos con acortamiento de enlaces SMS.

### Transparencia del seguimiento de la aplicación {#app-tracking-transparency}

Apple anunció su compromiso de ampliar el alcance de [la Transparencia del Seguimiento de Anuncios (ATT)](https://support.apple.com/en-us/HT212025), que permite a los usuarios controlar si una aplicación puede acceder a su actividad en aplicaciones y sitios web pertenecientes a otras empresas. La versión iOS 17 contiene dos características clave de ATT: manifiestos de privacidad y firma de código.

#### Manifiestos de privacidad {#privacy-manifests}

Apple exige ahora un archivo de manifiesto de privacidad que describa el motivo por el que tu aplicación y los SDK de terceros recopilan datos, junto con sus métodos de recopilación de datos. A partir de iOS 17.2, Apple bloqueará todos los puntos finales de seguimiento declarados en tu aplicación hasta que el usuario final acepte el aviso de ATT.

Braze ha publicado su propio manifiesto de privacidad, junto con nuevas API flexibles que redirigen automáticamente los datos declarados de seguimiento a puntos finales dedicados de `-tracking`. Para más información, consulta el [manifiesto de privacidad de Braze]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=swift#swift_privacy-manifest).

#### Firma de código {#code-signing}

La firma de código permite a los desarrolladores que utilizan un SDK de terceros en su aplicación validar que el mismo desarrollador lo firmó en versiones anteriores en Xcode.

### SDK de Braze y privacidad {#braze-sdk-and-privacy}

Apple también ha anunciado que publicará una lista de SDK de terceros que se consideran "que afectan a la privacidad" a finales de 2023. Se espera que estos SDK tengan un impacto especialmente alto en la privacidad de los usuarios según Apple.

A diferencia de los SDK de seguimiento tradicionales, diseñados para supervisar a los usuarios en varios sitios web y aplicaciones, el SDK de Braze se centra en la mensajería de datos propios y en las experiencias de usuario.

Aunque no esperamos que el SDK de Braze se incluya en esta lista, tenemos la intención de seguir de cerca esta situación y publicar las actualizaciones necesarias.