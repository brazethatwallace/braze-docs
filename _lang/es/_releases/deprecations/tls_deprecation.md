---
nav_title: Suspensión de TLS 1.0 y 1.1
page_order: 2

page_type: update
description: "En este artículo se describe la suspensión de TLS 1.0 y TLS 1.1 por parte de Braze, completada en mayo de 2018."
---
# Suspensión de TLS 1.0 y 1.1 {#tls-10-11-deprecation}

{% alert update %}
Braze eliminó la compatibilidad con las claves de seguridad de la capa de transporte (TLS) tanto en TLS 1.0 como en TLS 1.1, de acuerdo con las recomendaciones del Consejo de Normas de Seguridad de la industria de las tarjetas de pago (PCI). Realizamos esta suspensión de compatibilidad en dos fases, completadas en mayo de 2018.
{% endalert %}

## Contexto {#background}

Braze está eliminando las claves débiles conocidas de seguridad de la capa de transporte (TLS) tanto en TLS 1.0 como en TLS 1.1, de acuerdo con las recomendaciones del Consejo de Normas de Seguridad de la industria de las tarjetas de pago (PCI) en dos fases que concluyen en mayo de 2018.

Este cambio no se realiza en respuesta a ninguna brecha o problema relacionado con la plataforma de Braze, sino como medida de precaución para mantener nuestros estándares de seguridad y datos, los mejores de su clase, y para proteger de forma proactiva a nuestros clientes y a sus consumidores.

En los últimos años, una serie de problemas de seguridad sistemáticos asociados tanto a TLS como a su predecesor, Secure Sockets Layer (SSL), como [POODLE](https://www.us-cert.gov/ncas/alerts/TA14-290A), [Heartbleed](https://en.wikipedia.org/wiki/Heartbleed), [LOGJAM](https://en.wikipedia.org/wiki/Logjam_(computer_security)) y otros, amenazaron el tráfico web cifrado y expusieron partes de Internet a brechas de seguridad. Junto con otras empresas tecnológicas, Braze tomó medidas previas para desactivar protocolos de cifrado y claves débiles a medida que se descubrían ataques; por ejemplo, eliminando la compatibilidad con SSLv3 en 2014.

Más recientemente, el Consejo de Normas de Seguridad de la PCI publicó en abril de 2015 unas directrices relacionadas con el cifrado para [la Norma de Seguridad de Datos de la Industria de Tarjetas de Pago](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard) (PCI-DSS). La directriz excluye SSL 3.0, TLS 1.0 y algunas de las suites de claves compatibles con TLS 1.1 de su lista de protocolos de cifrado criptográfico fuerte, y anima a las empresas a que dejen de admitir esos protocolos o claves para garantizar la seguridad de los usuarios de Internet.

Una suite de claves es una combinación de algoritmos que proporcionan cifrado, autenticación e integridad de las comunicaciones al negociar una conexión segura SSL o TLS. Cuando se descubre que es posible romper una clave determinada —haya o no ataques conocidos en la actualidad—, se considera que la clave tiene "puntos débiles" que podrían habilitar futuros ataques. Al excluir estas claves TLS de los requisitos de cumplimiento de PCI DSS, el Consejo de PCI DSS está exigiendo a los proveedores de servicios que solo admitan las mejores normas de cifrado de su clase. El Consejo de PCI DSS ha fijado el 30 de junio de 2018 como fecha límite para el cumplimiento del requisito de cifrado de abandonar la compatibilidad con TLS 1.0 y TLS 1.1.

## Plan de suspensión de Braze {#brazes-deprecation-plan}
Para cumplir las recomendaciones del Consejo de PCI DSS, Braze aumentará las versiones mínimas de TLS que admitimos en nuestros servicios. Para que te hagas una mejor idea de nuestro plan de cumplimiento y de su impacto potencial en tu marca y en tus usuarios, hay dos fases principales de nuestro plan que debes conocer:

### Fase 1: 1 de octubre de 2017 {#phase-1-october-1-2017}

Braze eliminará la posibilidad de utilizar las siguientes claves del panel web y las REST or transferencia de estado representacional API de Braze:

- `TLS_RSA_WITH_AES_256_CBC_SHA`
- `TLS_RSA_WITH_AES_128_CBC_SHA`
- `TLS_RSA_WITH_AES_256_CBC_SHA256`
- `TLS_RSA_WITH_AES_256_GCM_SHA384`
- `TLS_RSA_WITH_AES_128_CBC_SHA256`
- `TLS_RSA_WITH_AES_128_GCM_SHA256`
- `TLS_RSA_WITH_3DES_EDE_CBC_SHA`

Este cambio no debería afectar a los clientes que acceden al panel de Braze, ya que todos los navegadores web modernos admiten claves más seguras. Sin embargo, si experimentas un error de cifrado SSL al acceder al panel web después del 1 de octubre, podrás solucionar el problema simplemente actualizando a la última versión de tu navegador web.

Tu equipo de ingeniería debe asegurarse de que no utiliza ninguna de estas claves para la comunicación de servidor a servidor con las REST or transferencia de estado representacional API de Braze. Si es así, tendrán que actualizar su código para utilizar claves de cifrado más seguras antes del 1 de octubre para poder seguir utilizando las API de Braze. Sin embargo, para mantener la compatibilidad con dispositivos móviles antiguos y obsoletos que puedan estar utilizando claves débiles, Braze seguirá admitiendo estas claves en las API que reciban datos de nuestros SDK or kit de desarrollo de software.

### Fase 2: 31 de mayo de 2018 {#phase-2-may-31-2018}

Braze desactivará la compatibilidad con TLS 1.0 y TLS 1.1 en todos los servicios de Braze el 31 de mayo de 2018, incluidos el panel de Braze, las REST or transferencia de estado representacional API y las API que se comunican con nuestros SDK or kit de desarrollo de software. También eliminaremos la compatibilidad con las claves enumeradas en la sección anterior en relación con las API que reciben datos del SDK or kit de desarrollo de software. Esto significa que todas las comunicaciones TLS 1.0 y 1.1 hacia y desde Braze no serán compatibles con nuestra red a partir de esta fecha.

Como resultado de este cambio, algunos dispositivos móviles antiguos o anticuados —probablemente los que ejecutan las primeras versiones de Android— pueden perder la capacidad de comunicarse con Braze, lo que les impediría enviar datos a Braze o recibir mensajes dentro de la aplicación desde Braze. Sin embargo, prevemos que el cambio solo afectará a un pequeño número de dispositivos. Los dispositivos afectados también perderán la capacidad de comunicarse con cualquier sitio web o servicio que cumpla la normativa PCI un mes después, el 30 de junio de 2018, fecha fijada por el Consejo de PCI DSS para la eliminación de las claves TLS 1.0 y TLS 1.1.

## Plan de acción {#action-plan}
Si tu marca hace uso de las REST or transferencia de estado representacional API de Braze, habla con tu equipo de ingeniería para asegurarte de que todas las llamadas de servidor a servidor a Braze utilizan TLS 1.2 en la fecha indicada, con el fin de evitar una interrupción del servicio. Ten en cuenta que algunos lenguajes de programación —como Java 7— utilizan versiones anteriores de TLS por defecto, por lo que es posible que tu equipo de ingeniería tenga que realizar algunos cambios en el código para admitir los requisitos de cifrado actualizados.

Los dispositivos de Apple no se verán afectados por la suspensión prevista de Braze, ya que Apple exige TLS 1.2 desde finales de 2016. Lo mismo ocurre con los navegadores web modernos, por lo que no prevemos que estos cambios tengan ningún impacto en el uso del SDK or kit de desarrollo de software Web. Sin embargo, es posible que los dispositivos Android con Android 4.4 (KitKat) o inferior no utilicen TLS 1.2 por defecto, así que toma medidas para actualizar cualquiera de tus integraciones de Android al menos a la versión 2.0.3 del SDK or kit de desarrollo de software de Braze (que utiliza TLS 1.2 por defecto, si un determinado dispositivo puede soportarlo) antes del 31 de mayo de 2018.

Por último, debido a los puntos débiles conocidos de la suite de claves de TLS 1.0 y TLS 1.1, es posible que en el futuro surjan ataques que obliguen a Braze a acelerar nuestro plan de suspensión, con el fin de salvaguardar la seguridad de todos nuestros clientes. Braze supervisará el estado de la seguridad y cualquier ataque relevante asociado a los protocolos TLS 1.0 y 1.1, y te mantendrá informado si nos enteramos de algún ataque que altere el calendario establecido en las secciones anteriores. Pero debido a este impacto potencial, te recomendamos encarecidamente que trabajes con tu equipo de ingeniería para asegurarte de que tus llamadas de API a Braze estén protegidas con TLS 1.2, y que planees actualizar al último SDK or kit de desarrollo de software de Android en los próximos meses.