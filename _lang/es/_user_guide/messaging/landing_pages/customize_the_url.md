---
nav_title: Personalizar la URL
article_title: Personalizar la URL
description: "Aprende a personalizar las URL de tus páginas de inicio con la marca de tu empresa conectando tu dominio a tu espacio de trabajo de Braze."
page_order: 1
---

# Personalizar las URL de las páginas de inicio {#customize-landing-page-urls}

> Aprende a personalizar las URL de tus páginas de inicio con la marca de tu empresa conectando tu dominio a tu espacio de trabajo de Braze.

## Cómo funciona {#how-it-works}

Cuando [conectas tu dominio a Braze](#connect-your-domain-to-braze), se utilizará como el dominio predeterminado para todas las páginas de inicio. Por ejemplo, si conectas el subdominio `forms.example.com`, las URL de tus páginas de inicio serían `forms.example.com/holiday-sale`.

El número de dominios personalizados que puedes conectar a tu cuenta de Braze depende de tu [nivel de plan]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers). Para aumentar tu límite, ponte en contacto con tu director de cuentas de Braze.

## Conectar tu dominio a Braze {#connect-your-domain-to-braze}

Para conectar un dominio a tu cuenta de Braze, pide a un administrador que siga los pasos a continuación.

1. Ve a **Configuración** > **Configuración de la página de inicio**.
2. Introduce el dominio que deseas conectar y selecciona **Enviar**. Por ejemplo, `forms.example.com`.
3. Copia y pega los registros **TXT** y **CNAME** en la configuración de DNS de tu proveedor de dominios.
4. Vuelve al dashboard de Braze para verificar la conexión.

![Página de configuración de la página de inicio con un registro TXT y dos registros CNAME enumerados con sus respectivos nombres y valores.]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

{% alert note %}
Dependiendo de tu proveedor de dominios, la conexión puede tardar hasta 48 horas. Cuando el proceso se complete, empezaremos a utilizar tu dominio personalizado para tus páginas de inicio en el dashboard de Braze.
{% endalert %}

### Configuración del certificado SSL {#ssl-certificate-setup}

Braze utiliza Cloudflare para aprovisionar automáticamente certificados SSL para tu dominio personalizado a través de un [desafío ACME DNS-01](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge). Este método de validación continua se habilita mediante uno de los registros CNAME que proporcionaste durante la configuración, y permite que la autoridad de certificación (LetsEncrypt) verifique la propiedad de tu dominio a través de registros de DNS sin necesidad de que Braze sea propietario de tu dominio.

## Quitar tu dominio {#remove-your-domain}

Si eres administrador de Braze, puedes quitar un dominio previamente configurado completando los siguientes pasos:

1. Ve a **Configuración** > **Configuración de la página de inicio**.
2. Selecciona **Quitar dominio personalizado**.
3. Confirma la eliminación del dominio.
4. Quita los registros de DNS enumerados de la configuración de tu dominio.

{% alert important %}
Cuando quitas un dominio personalizado, esa URL dejará de ser válida. Cualquier página de inicio que estuviera utilizando este dominio volverá automáticamente al dominio predeterminado establecido por Braze.
{% endalert %}

## Migrar tu dominio {#migrate-your-domain}

Para migrar un dominio personalizado a otro espacio de trabajo:

1. Quita el dominio personalizado.
2. Crea un nuevo dominio personalizado en el espacio de trabajo deseado.
3. Reconfigura el dominio personalizado con los nuevos registros de DNS. Ten en cuenta que tu subdominio no estará disponible durante este proceso.

## Recursos de DNS {#dns-resources}

{% multi_lang_include channels/email/dns_records.md %}

## Solución de problemas {#troubleshooting}

### Mi conexión de dominio falló {#my-domain-connection-failed}

Verifica que tu dominio se haya introducido correctamente y que coincida con lo que enviaste a Braze desde la cuenta de tu proveedor de dominios. Si es correcto y coincide, comprueba los registros TXT y CNAME proporcionados por Braze. Deben coincidir con los registros que introdujiste en la cuenta de tu proveedor de dominios.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Puedo usar subdominios anidados para mi dominio personalizado? {#can-i-use-nested-subdomains-for-my-custom-domain}

Sí, puedes usar subdominios anidados para tus páginas de inicio. Por ejemplo, `forms.braze.com`, `pages.forms.braze.com` o niveles más profundos son todos compatibles. El único requisito es que no puedes usar un dominio apex (como `braze.com`) porque Braze utiliza registros CNAME para la conexión.

### ¿Puedo conectar varios subdominios a mi espacio de trabajo o conectar un subdominio a varios espacios de trabajo? {#can-i-connect-multiple-subdomains-to-my-workspace-or-connect-one-subdomain-to-multiple-workspaces}

No, actualmente solo puedes conectar un subdominio a un espacio de trabajo.

### ¿Puedo usar el mismo subdominio que utilizo actualmente para mi sitio web principal o mi dominio de envío? {#can-i-use-the-same-subdomain-that-i-currently-use-for-my-main-website-or-my-sending-domain}

No, no puedes usar subdominios que ya estén en uso. Aunque estos subdominios son válidos, no se pueden usar para páginas de inicio si ya están asignados a otros propósitos o tienen registros de DNS que entran en conflicto con los registros CNAME requeridos.

### ¿Por qué mi dominio personalizado está atascado en "Conectando" a pesar de tener registros de DNS válidos? {#why-is-my-custom-domain-stuck-on-connecting-despite-valid-dns-records}

Si tu dominio personalizado muestra todos los registros de DNS como "Conectado" pero el estado del dominio permanece en "Conectando" durante más de cuatro horas, es posible que tu organización esté utilizando registros CAA (autorización de autoridad de certificación) o retenciones de zona de Cloudflare que impiden que Braze asegure tu página.

#### Registros CAA {#caa-records}

Los registros CAA restringen qué autoridades de certificación pueden emitir certificados SSL para tu dominio. Si tus registros CAA no incluyen LetsEncrypt, Braze (a través de Cloudflare) no puede emitir el certificado SSL requerido.

Para resolver esto, pide a tu equipo de TI que añada un registro CAA a tu subdominio con los siguientes valores:
- **Tipo de registro:** CAA
- **Valor:** `0 issue "letsencrypt.org"`

Para más información, consulta la [documentación de CAA de LetsEncrypt](https://letsencrypt.org/docs/caa/).

#### Retenciones de zona de Cloudflare {#cloudflare-zone-holds}

Si tu organización utiliza Cloudflare, una función de seguridad de retención de zona puede estar impidiendo que Braze cree tu dominio personalizado.

Para resolver esto, pide a tu equipo de TI que libere temporalmente la retención de zona. Para más información, consulta la [documentación de retención de zona de Cloudflare](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/#release-zone-holds).

#### Reiniciar el proceso de validación {#restarting-the-validation-process}

Después de resolver cualquiera de los problemas, elimina y vuelve a crear tu dominio personalizado en el dashboard de Braze para reiniciar el proceso de validación.

### ¿Puedo usar un proxy inverso para servir páginas de inicio bajo mi dominio principal o un subdirectorio? {#can-i-use-a-reverse-proxy-to-serve-landing-pages-under-my-main-domain-or-a-subdirectory}

No, las etiquetas de Liquid de URL de páginas de inicio no funcionarán correctamente con proxies inversos.