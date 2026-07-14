---
nav_title: Solución de problemas
article_title: Solución de problemas de correos electrónicos HTML
page_order: 9
description: "Diagnostica problemas de renderizado y del editor de correos electrónicos HTML utilizando un índice de síntomas y pasos estándar de solución de problemas."
channel: email
---

# Solución de problemas de correos electrónicos HTML {#troubleshoot-html-emails}

> Usa esta página para resolver problemas comunes del editor de correos electrónicos HTML y de los envíos de prueba. Para Inbox Vision y capacidad de entrega, consulta [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) y [Configuración de correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup).

## Empieza aquí: identifica tu síntoma {#start-here-match-your-symptom}

Busca tu síntoma en la tabla para navegar a la sección correspondiente.

| Síntoma | Ir a |
| --- | --- |
| El HTML del correo electrónico de prueba se ve mal | [El HTML se renderiza incorrectamente en los correos electrónicos de prueba](#html-renders-incorrectly-in-test-emails) |
| El editor se comporta de forma extraña en Chrome | [Conflictos de extensiones](#extension-conflicts) |
| El correo electrónico se ve diferente en distintos clientes | [Renderizado de correo electrónico](#email-rendering) |
| La vista previa de Inbox Vision no coincide con el correo enviado | [Inlining de CSS](#css-inlining) |
| Espacio en blanco o líneas después de las imágenes en correos de prueba | [Espacio en blanco debajo de las imágenes](#white-space-under-images) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Síntoma de correo electrónico HTML" }

## Ruta de investigación estándar {#standard-investigation-path}

Usa este flujo de trabajo cuando el renderizado del correo electrónico HTML o el comportamiento del editor no coincida con lo que esperas. Empieza en el paso 1.

1. Valida tu marcado HTML en el editor o en un validador externo.
2. Envía un [correo electrónico de prueba]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) y anota qué clientes de correo electrónico o navegadores muestran el problema.
3. Previsualiza con [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision#inbox-vision) para comparar el renderizado en distintos clientes.
4. Descarta [conflictos de extensiones del navegador](#extension-conflicts) si el propio editor se comporta de forma incorrecta.
5. Si el problema persiste, abre un [ticket de soporte]({{site.baseurl}}/braze_support) con capturas de pantalla de Inbox Vision y de los clientes afectados.

## El HTML se renderiza incorrectamente en los correos electrónicos de prueba {#html-renders-incorrectly-in-test-emails}

**Síntoma:** Un [correo electrónico de prueba]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) no se ve como esperas desde el editor.

Revisa primero tu configuración HTML y después consulta [conflictos de extensiones](#extension-conflicts), [renderizado de correo electrónico](#email-rendering), [inlining de CSS](#css-inlining) y [espacio en blanco debajo de las imágenes](#white-space-under-images).

### Conflictos de extensiones {#extension-conflicts}

Ciertas extensiones del navegador pueden causar problemas con el editor de correo electrónico. Un ejemplo es [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en) cuando se usa con Google Chrome. Si estás usando una de estas extensiones, deberías:

- Editar los correos electrónicos de Braze en un navegador que no tenga Grammarly como extensión del navegador.
- Ponerte en contacto con tu director de cuentas de Braze y solicitar cambiar tus editores de correo electrónico a solo HTML o texto plano.

La vista de texto plano elimina tu editor `WYSIWYG` (lo que ves es lo que obtienes), así que primero deberías confirmar que todos los miembros del equipo se sienten cómodos con HTML antes de hacer esta solicitud.

### Renderizado de correo electrónico {#email-rendering}

Los correos electrónicos se renderizan de forma diferente según los navegadores y los clientes de correo electrónico, así que toma nota de con qué navegadores y clientes de correo electrónico estás experimentando problemas.

- Previsualiza tus correos electrónicos usando [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision#inbox-vision) para ver cómo se ven en diferentes navegadores y clientes de correo electrónico.
- Una vez que hayas identificado qué navegadores o clientes de correo electrónico están causando problemas, informa a tu equipo de desarrolladores de que necesitarán modificar su HTML y hacer ajustes para adaptarse a esos navegadores o clientes de correo electrónico.

### Inlining de CSS {#css-inlining}

Hay ocasiones en las que las vistas previas en Inbox Vision aún no coinciden con lo que se envía con Braze. Esto puede deberse a la diferencia en el inlining de CSS realizado por Braze y por otras herramientas. Si sospechas que este es el caso, desactiva el inlining de CSS.

### Espacio en blanco debajo de las imágenes {#white-space-under-images}

**Síntoma:** Aparecen espacios en blanco o líneas después de las imágenes en los correos electrónicos de prueba.

Si notas espacios en blanco o líneas que aparecen después de las imágenes en tus correos electrónicos de prueba, esto suele deberse a cómo los clientes de correo electrónico renderizan los elementos de nivel inline. Las imágenes son de nivel inline de forma predeterminada y se alinean con la línea base, lo que permite a los navegadores acomodar los descendentes (la parte de letras como "g" o "y" que se extiende por debajo de la línea base). Esto crea un pequeño espacio que aparece como espacio en blanco.

Para solucionarlo, añade `display: block;` al CSS de tu imagen:

```html
<style>
  img {
    display: block;
  }
</style>
```

Alternativamente, aplica el estilo directamente a imágenes específicas:

```html
<img src="https://example.com/image.jpg" style="display: block;" alt="Image description" />
```
