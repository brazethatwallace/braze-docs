---
nav_title: Solución de problemas
article_title: Solución de problemas de SSL
page_order: 5
page_type: reference
description: "Este artículo de referencia cubre consejos de solución de problemas para SSL."
channel: email
---

# Solución de problemas {#troubleshooting}

> Usa estos consejos para identificar problemas comunes de seguimiento de clics con SSL. Las indicaciones de solución de problemas son genéricas porque cada CDN es único. Para problemas de configuración de CDN, certificados o proxy, ponte en contacto con el equipo de soporte de tu CDN, ya que estas configuraciones se realizan fuera del ecosistema de Braze.

## Conceptos clave {#key-concepts}

- **URL con seguimiento:** Envuelve el enlace HTTPS original en tu dominio de seguimiento. Cuando un usuario hace clic en él, el dominio de seguimiento resuelve la solicitud y redirige al destino final. Un CDN te permite rastrear URLs seguras (HTTPS). Sin él, los usuarios pueden encontrar un error de privacidad de "la conexión no es segura".
- **URL sin seguimiento:** Mantiene la URL original intacta, omitiendo el CDN para servir como entorno de control.

## Tasas bajas de apertura de correo electrónico {#low-email-open-rates}

Si de repente experimentas tasas bajas de apertura de correo electrónico, confirma que el certificado SSL esté actualizado. Si ha expirado, debes renovar ese certificado SSL con tu CDN o proveedor de certificados.

## HTTP 403 en enlaces de redirección {#http-403-on-redirect-links}

Si los enlaces de redirección con seguimiento devuelven **403 Forbidden**, el fallo suele ocurrir en tu red de entrega de contenido (CDN) o firewall de aplicaciones web (WAF), por ejemplo, reglas en AWS WAF o Amazon CloudFront que bloquean ciertos agentes de usuario, cadenas de consulta o patrones de redirección. Revisa los registros de solicitudes bloqueadas y las métricas con tu CDN o proveedor de nube. Para AWS, consulta [Solución de problemas con CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/troubleshooting.html).

Para ver si el problema es específico del seguimiento de clics, desactiva el seguimiento de clics para un enlace de prueba (consulta [Desactivar el seguimiento de clics enlace por enlace]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/#turning-off-click-tracking-on-a-link-to-link-basis)). Si la URL de destino carga cuando el seguimiento de clics está desactivado pero devuelve 403 cuando está activado, concéntrate en la configuración de tu dominio de seguimiento de clics, CDN y WAF.

## Problemas con el registro de dominio {#domain-registry-issues}

Ejecuta un comando dig para confirmar que apuntas el seguimiento de enlaces al CDN. En tu terminal ejecuta `dig CNAME link_tracking_subdomain`. En `ANSWER SECTION`, se indica a dónde apunta tu CNAME. Si apunta al proveedor de servicios de correo electrónico (SendGrid, SparkPost o Amazon SES) y no a tu CDN, reconfigura tu registro de dominio para que apunte a tu CDN.

## Problemas con el CDN {#cdn-issues}

Si los enlaces de correo electrónico en vivo se rompen durante la configuración, probablemente apuntaste el DNS hacia tu CDN antes de una configuración adecuada. Esto puede aparecer como un error de "enlace incorrecto". Ponte en contacto con tu proveedor de CDN y revisa su documentación para solucionar la configuración.

Si ves un mensaje de error indicando que tu conexión no es privada, esto puede indicar que tu SSL o CDN no está configurado correctamente. Ejecuta un comando `dig` en tu terminal (por ejemplo, `dig CNAME your_link_tracking_subdomain`). En `ANSWER SECTION`, si el resultado apunta a tu ESP en lugar de a tu CDN, el problema es una mala configuración. Para que el seguimiento de clics SSL de Braze funcione, el CNAME debe apuntar a tu CDN. Coordina con el equipo que administra tu configuración de SSL y CDN para obtener más asistencia.

## Estado de habilitación de SSL {#ssl-enablement-status}

Si completas la configuración de SSL y los enlaces siguen apareciendo como HTTP, ponte en contacto con tu administrador del éxito del cliente de Braze para confirmar que Braze habilitó SSL. Braze habilita SSL solo después de que se completen todos los pasos de configuración.

### Amazon SES {#amazon-ses}

Si estás usando Amazon SES como tu proveedor de servicios de correo electrónico, los siguientes problemas de configuración pueden impedir que Braze habilite SSL o causar errores durante la configuración:

- **Discrepancia de región:** Confirma que el origen de tu CDN apunte al dominio de seguimiento de AWS para tu clúster de Braze. Los clústeres de EE. UU. usan `r.us-east-1.awstrack.me`. Los clústeres de la UE usan `r.eu-central-1.awstrack.me`. Usar la región incorrecta puede bloquear la habilitación de SSL.
- **Encabezado de host:** Amazon SES requiere que tu CDN reenvíe el encabezado de host correcto. Habilita el encabezado `X-Forwarded-Host` en tu dominio de seguimiento de clics. Para más información, consulta la sección [Amazon SES](#amazon-ses).
- **Configuración de proxy:** Una configuración de proxy o CDN que sobrescriba o entre en conflicto con el encabezado de host puede causar que la habilitación de SSL falle. Revisa la configuración del proxy con tu proveedor de CDN para confirmar que no interfiera con el reenvío del encabezado de host.
- **Registro alias de Route 53:** Si usas Route 53 para administrar el DNS de tu dominio, crea un [registro alias en Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) que apunte a tu distribución de CDN (por ejemplo, `d111111abcdef8.cloudfront.net`). Usar un CNAME estándar en lugar de un registro alias puede devolver errores HTTP 400.
- **Reenvío de encabezados deshabilitado:** Si la habilitación de SSL sigue fallando después de configurar `X-Forwarded-Host`, intenta deshabilitar el reenvío de encabezados en tu CDN o proxy. Algunas configuraciones resuelven el problema cuando el reenvío se desactiva por completo. Trabaja con tu equipo de TI o proveedor de CDN para probar esta configuración.

## Problemas con el seguimiento de clics {#click-tracking-issues}

Los problemas comunes de redirección suelen ser resultado de una configuración incorrecta entre el CDN que aloja el dominio de seguimiento y sus certificados SSL asociados o registros DNS CNAME. Estas malas configuraciones a menudo causan que los usuarios reciban un error de privacidad de "la conexión no es segura" o un fallo `404` después de hacer clic en un enlace de correo electrónico con seguimiento.

Usa la siguiente plantilla para probar la configuración del CDN de tu dominio de seguimiento, que es el mecanismo que soporta los análisis de los enlaces dentro de tus correos electrónicos.

1. Copia y pega la siguiente plantilla en una Campaign de correo electrónico HTML de Braze.

{% details Plantilla de solución de problemas de seguimiento de clics %}
{% raw %}
```html
<!DOCTYPE html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="color-scheme" content="light dark">
    <meta name="supported-color-schemes" content="light dark">
    <title>Click Tracking Test</title>
    <style>
        /* Base Dark Mode (Default) */
        body {
            margin: 0;
            padding: 0;
            background-color: #2b0562;
            font-family: 'Helvetica Neue', Arial, sans-serif;
            color: #ffd1e9;
        }

        .email-container {
            width: 100%;
            max-width: 600px;
            margin: 40px auto;
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px solid #F3697F;
            border-radius: 16px;
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #E83F21 0%, #F3697F 100%);
            padding: 40px 20px 50px 20px;
            text-align: center;
        }

        .logo {
            display: block;
            margin: 0 auto 25px auto;
            border: 0;
            outline: none;
            text-decoration: none;
        }

        .header h1 {
            color: #ffffff;
            margin: 0;
            font-size: 26px;
            font-weight: 800;
            letter-spacing: -0.5px;
        }

        .content {
            padding: 40px 40px 20px 40px;
            line-height: 1.8;
            font-size: 15px;
        }

        .troubleshoot {
            margin: 0 40px 40px 40px;
            padding: 25px;
            background-color: rgba(253, 167, 216, 0.1);
            border-radius: 12px;
            font-size: 14px;
            border: 1px dashed #F3697F;
        }

        .troubleshoot h2 {
            margin-top: 0;
            font-size: 18px;
            color: #ffffff;
        }

        .btn-section {
            padding: 0 40px 40px 40px;
            text-align: center;
        }

        .btn {
            display: inline-block;
            padding: 16px 32px;
            border-radius: 12px;
            font-weight: 700;
            text-decoration: none;
            margin: 10px;
            font-size: 14px;
        }

        .btn-tracked {
            background-color: #F3697F;
            color: #ffffff;
        }

        .btn-untracked {
            border: 2px solid #FDA7D8;
            color: #FDA7D8;
            background-color: transparent;
        }

        .footer {
            text-align: center;
            font-size: 12px;
            color: #FDA7D8;
            padding-bottom: 40px;
            opacity: 0.6;
        }

        /* Light Mode Overrides */
        @media (prefers-color-scheme: light) {
            body { background-color: #F7FCFF !important; color: #2b0562 !important; }
            .email-container { background-color: #ffffff !important; border: 1px solid #FDA7D8 !important; box-shadow: 0 4px 20px rgba(43, 5, 98, 0.1); }
            .content { color: #2b0562 !important; }
            .troubleshoot { background-color: #F7FCFF !important; border-color: #F3697F !important; color: #2b0562 !important; }
            .troubleshoot h2 { color: #E83F21 !important; }
            .btn-untracked { color: #F3697F !important; border-color: #F3697F !important; }
            .footer { color: #2b0562 !important; }
            strong { color: #E83F21 !important; }
        }

        /* Mobile Optimization */
        @media only screen and (max-width: 480px) {
            .btn { display: block !important; margin: 10px 0 !important; width: auto !important; }
            .content, .troubleshoot { padding: 25px !important; }
        }
    </style>
</head>
{%- capture url -%}https://example.com{%- endcapture -%}
<body>
    <center>
        <table class="email-container" role="presentation" width="600" border="0" cellpadding="0" cellspacing="0">
            <tr>
                <td class="header">
                    <img src="https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/60aecba96a93150c749b4d57/original.png?1622068137"
                         width="150"
                         alt="Logo"
                         class="logo">
                    <h1>Testing Click Tracking Functionality</h1>
                </td>
            </tr>
            <tr>
                <td class="content">
                    <p>
                        Use this template to test the <strong>CDN configuration</strong> of your tracking domain—the mechanism supporting analytics for links within your emails.
                    </p>
                    <p>
                        A <strong>Tracked URL</strong> wraps the original HTTPS link in your tracking domain. When a user clicks it, the tracking domain resolves the request and redirects to the final destination. A CDN allows you to track secure (HTTPS) URLs; without it, users may encounter a "connection is not secure" privacy error. An <strong>Untracked URL</strong> maintains the original URL intact, bypassing the CDN to serve as a control environment.
                    </p>
                    <p>
                        Common redirection issues typically result from an improper configuration between the CDN hosting the tracking domain and the <strong>associated SSL certificate or DNS CNAME records.</strong>
                    </p>
                    <p>
                        <i style="font-size: 13px;">This template uses "example.com" as the destination URL. To test your own domain, replace the URL in the <strong>capture</strong> tag located on line 125.</i>
                    </p>
                </td>
            </tr>
            <tr>
                <td class="btn-section">
                    <a href="{{url}}" class="btn btn-tracked">Tracked URL</a>

                    <a href="{{url}}"
                       class="btn btn-untracked"
                       clicktracking="off"
                       data-msys-clicktrack="0"
                       ses:no-track="true">
                       Untracked URL
                    </a>
                </td>
            </tr>
            <tr>
                <td>
                    <div class="troubleshoot">
                        <h2>Troubleshooting the Test</h2>
                        <ul>
                            <li><strong>Tracked URL Fails / Untracked Works:</strong> This indicates a CDN or SSL certificate issue. Verify that your SSL certificate is valid and correctly bound to your tracking domain.</li>
                            <li><strong>Privacy Error (HTTPS):</strong> Ensure your CDN is configured to handle port 443 traffic and that the certificate matches your tracking CNAME.</li>
                            <li><strong>Both URLs Fail:</strong> Check the destination URL or your internal network firewall settings.</li>
                            <li>For more information, visit: <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/channels/email/email_setup/ssl">SSL at Braze</a></li>
                        </ul>
                    </div>
                </td>
            </tr>
        </table>
        <div class="footer">
            Braze :: 63 Madison Avenue, 13th Floor :: New York, NY 10016
        </div>
    </center>
</body>
</html>
```
{% endraw %}
{% enddetails %}

{: start="2"}
2. Configura tu URL. Reemplaza la URL en la etiqueta `capture` cerca de la parte superior del cuerpo de la plantilla (donde se establece `https://example.com`). Por ejemplo, reemplaza `https://example.com` con `https://braze.com/docs`.
3. Envíate un correo electrónico de prueba y selecciona ambos botones.
4. Verifica que el comportamiento esperado y los criterios de éxito sean los descritos en la plantilla.

Si tu URL sin seguimiento funciona pero tu URL con seguimiento falla, es posible que tengas un problema de configuración. Para solucionarlo, consulta la documentación de tu ESP y proveedor de CDN específicos. También puedes revisar [SSL en Braze]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/) para conocer los requisitos detallados sobre el aprovisionamiento de certificados.

Usa la siguiente tabla para diagnosticar errores comunes al probar el seguimiento de clics.

| Código de error | Solución de problemas |
| --- | --- |
| `"Your connection is not private" (NET::ERR_CERT_COMMON_NAME_INVALID)` | Verifica que tu dominio de seguimiento tenga un certificado SSL válido. |
| `"This site can't be reached" (DNS_PROBE_FINISHED_NXDOMAIN)` | Revisa tu configuración de DNS. Asegúrate de que tu subdominio de seguimiento esté configurado según la configuración recomendada por tu CDN y ESP. |
| `525 / 526 SSL Error` | Verifica que la configuración de SSL en tu CDN (como Cloudflare) coincida con la capacidad de tu Origin. |
| `404 Not Found` | Verifica que tu CDN esté configurado para reenviar la ruta completa de la URL al ESP, en lugar de apuntar a un directorio raíz vacío. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Códigos de error y solución de problemas" }