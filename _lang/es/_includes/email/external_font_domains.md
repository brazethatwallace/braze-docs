### Dominios de fuentes externas {#external-font-domains}

Al crear páginas de {{ include.page_type }} personalizadas, Braze sanea las entradas HTML para prevenir ataques de cross-site scripting (XSS). Como parte de esta medida de seguridad, las URL de recursos externos, incluidas las URL de fuentes, se eliminan a menos que provengan de los siguientes dominios permitidos:

- `assets.appboycdn.com`
- `braze-images.com`
- `cdn.braze.com`
- `cdn.braze.eu`
- `fonts.googleapis.com`
- `fonts.gstatic.com`

Si necesitas usar fuentes personalizadas en tu página de {{ include.page_type }}, haz referencia a fuentes de uno de estos dominios o usa [fuentes web seguras](https://www.w3schools.com/cssref/css_websafe_fonts.php) en su lugar.

Para conocer las mejores prácticas de gestión de listas de correo electrónico, consulta [Suscripciones de correo electrónico]({{site.baseurl}}/user_guide/channels/email/subscriptions).