---
nav_title: Enviar correos electrónicos a Apple Private Relay
article_title: Enviar correos electrónicos a Apple Private Relay
alias: /email_relay/
page_order: 0
description: "Este artículo cubre el proceso de envío de correos electrónicos a Apple Private Relay."
channel:
  - email
toc_headers: h2
---

# Enviar correos electrónicos a Apple Private Relay {#send-emails-to-apple-private-relay}

> La característica de inicio de sesión único (SSO) de Apple permite a sus usuarios compartir sus direcciones de correo electrónico (`example@icloud.com`) u ocultar sus direcciones de correo electrónico enmascarando lo que se proporciona a las marcas (`tq1234snin@privaterelay.appleid.com`) en lugar de su dirección de correo electrónico personal. Apple reenviará entonces los mensajes enviados a las direcciones de retransmisión a la dirección de correo electrónico real del usuario.

Para enviar correos electrónicos al relé de correo electrónico privado de Apple, registra tus dominios de envío con Apple. Si no configuras tus dominios con Apple, los correos electrónicos enviados a direcciones de retransmisión rebotarán.

Si un usuario decide desactivar el reenvío de correo electrónico al correo electrónico de retransmisión de tu aplicación, Braze recibirá la información de rebote de correo electrónico como de costumbre. Estos usuarios pueden gestionar las aplicaciones que utilizan el inicio de sesión con Apple desde la página de configuración de su ID de Apple (consulta la [documentación de Apple](https://support.apple.com/en-us/HT210426)).

## Configura tu proveedor de correo electrónico {#configure-your-email-provider}

{% tabs %}
{% tab SendGrid %}

Si usas SendGrid como proveedor de correo electrónico, puedes enviar correos electrónicos a Apple sin realizar cambios en el DNS.

1. Inicia sesión en el [Apple Developer Portal](https://developer.apple.com/).
2. Ve a la página **Certificates, Identifiers & Profiles**.
3. Selecciona **Services** > **Sign in with Apple for Email Communication**.
4. En la sección **Email Sources**, añade los dominios y subdominios.
- La dirección debe tener el formato: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>` (un ejemplo es: `bounces+1234567@braze.online.docs.com`).

Si la dirección "From" que deseas es una dirección `abmail`, inclúyela en tu subdominio. Por ejemplo, usa `abmail.docs.braze.com` en lugar de `docs.braze.com`.

{% endtab %}
{% tab SparkPost %}

Para configurar Apple Private Relay para SparkPost, sigue estos pasos:

1. Inicia sesión con Apple.
2. Sigue la [documentación de Apple](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) para registrar los dominios de correo electrónico.
3. Apple verificará automáticamente los dominios, mostrará cuáles están verificados y proporcionará la opción de volver a verificar o eliminar los dominios.

### Cuando el dominio de envío también es el dominio de rebote {#when-the-sending-domain-is-also-the-bounce-domain}

Si un dominio de envío también se usa como dominio de rebote, no podrás almacenar ningún registro y deberás seguir estos pasos adicionales:

1. Si el dominio ya ha sido verificado en SparkPost, **debes** crear registros MX y TXT:

| Instancia | Registro MX                   | Registro TXT                                    |
|-----------|-------------------------------|------------------------------------------------|
| US        | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| EU        | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cuando el dominio de envío también es el dominio de rebote" }

{% alert important %}
Para evitar fallos de SPF, debes crear los registros MX y TXT y esperar a que se propaguen en el DNS **antes** de eliminar el registro CNAME.
{% endalert %}

{:start="2"}
2. Elimina el registro CNAME.
3. Reemplázalo con los registros MX y TXT para un enrutamiento adecuado.
4. Crea tu registro A para que apunte a tu CDN o alojamiento de archivos.

{% endtab %}
{% tab Amazon SES %}

Para configurar Apple Private Relay, lo ideal es que tengas un dominio MAIL FROM personalizado configurado.

1. Inicia sesión con Apple.
2. Sigue la [documentación de Apple](https://developer.apple.com/help/account/capabilities/configure-private-email-relay-service) para registrar los dominios de correo electrónico.

{% alert important %}
Confirma que tu DKIM/SPF coincida con lo que registras según las instrucciones enlazadas.
{% endalert %}

{:start="3"}
3. Apple verificará automáticamente los dominios, mostrará cuáles están verificados y proporcionará la opción de volver a verificar o eliminar los dominios.

{% endtab %}
{% endtabs %}

Si tienes más preguntas, abre un [ticket de soporte]({{site.baseurl}}/braze_support/).