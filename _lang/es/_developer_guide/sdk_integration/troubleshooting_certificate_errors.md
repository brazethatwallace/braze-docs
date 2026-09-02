---
page_order: 1.35
nav_title: Errores de confianza de certificados
article_title: Solución de problemas de errores de confianza de certificados del SDK or kit de desarrollo de software
description: "Soluciona errores de confianza de certificados HTTPS que pueden bloquear la inicialización del SDK or kit de desarrollo de software de Braze en Android, Swift y otros SDK or kit de desarrollo de software."
---

# Solución de problemas de errores de confianza de certificados del SDK or kit de desarrollo de software {#troubleshooting-sdk-certificate-trust-errors}

Si la inicialización del SDK or kit de desarrollo de software falla con errores de confianza de certificados SSL o TLS, esto generalmente significa que el dispositivo, simulador, navegador o servidor no puede validar la cadena de certificados para el endpoint de Braze.

Por ejemplo, en Android u otros entornos basados en JVM, podrías ver:

```
javax.net.ssl.SSLHandshakeException: java.security.cert.CertPathValidatorException: Trust anchor for certification path not found
```

Esto generalmente es un problema de configuración de red o de confianza de certificados en tu entorno, más que un error de integración de SDK or kit de desarrollo de software.

## Causas comunes {#common-causes}

- Un proxy corporativo, firewall o herramienta de inspección de tráfico está interceptando el tráfico HTTPS con un certificado en el que tu entorno de ejecución no confía.
- Falta un certificado raíz o intermedio requerido en el almacén de confianza del dispositivo, simulador, navegador o servidor.
- La configuración de seguridad local bloquea el tráfico HTTPS saliente hacia los endpoints de Braze.
- La configuración de certificados o de seguridad de transporte a nivel de la aplicación bloquea la conexión.

## Pasos de solución de problemas {#troubleshooting-steps}

1. Confirma tu endpoint de SDK or kit de desarrollo de software y el acceso a la red.
   - Verifica que estés usando el [endpoint de SDK or kit de desarrollo de software]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) correcto para tu espacio de trabajo.
   - Verifica que tu entorno pueda alcanzar ese endpoint a través de HTTPS.
2. Compara el comportamiento en diferentes redes.
   - Prueba en una red diferente (por ejemplo, datos móviles en lugar de Wi-Fi corporativo).
   - Si el problema solo ocurre en una red, la causa raíz probablemente sea la configuración del proxy o del firewall.
3. Valida tu configuración de confianza.
   - Confirma que los certificados raíz e intermedios necesarios estén instalados y sean de confianza en el entorno de ejecución donde se ejecuta el SDK or kit de desarrollo de software.
   - Si tu entorno utiliza autoridades de certificación personalizadas, confirma que esos certificados se distribuyan correctamente.
4. Revisa la configuración de seguridad de la plataforma.
   - Si tu aplicación o entorno tiene reglas explícitas de transporte o certificados, confirma que esa configuración permita solicitudes HTTPS a los endpoints de Braze.
5. Trabaja con tu equipo de red o seguridad.
   - Comparte el error completo y la marca de tiempo para que puedan verificar las cadenas de certificados, la configuración de inspección TLS y las reglas de lista de permitidos.

{% alert note %}
Debido a que el tráfico del SDK or kit de desarrollo de software de Braze usa HTTPS, los fallos de confianza en certificados pueden afectar a cualquier SDK or kit de desarrollo de software de Braze (incluidos Android, SWIFT, Web, React Native, Flutter, Unity y Cordova) en entornos con políticas de red restrictivas.
{% endalert %}