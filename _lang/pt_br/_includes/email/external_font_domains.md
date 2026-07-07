### Domínios de fontes externas {#external-font-domains}

Ao criar páginas personalizadas de {{ include.page_type }}, a Braze sanitiza as entradas HTML para prevenir ataques de cross-site scripting (XSS). Como parte dessa medida de segurança, URLs de recursos externos — incluindo URLs de fontes — são removidas, a menos que pertençam a um dos seguintes domínios permitidos:

- `assets.appboycdn.com`
- `braze-images.com`
- `cdn.braze.com`
- `cdn.braze.eu`
- `fonts.googleapis.com`
- `fonts.gstatic.com`

Se você precisar usar fontes personalizadas na sua página de {{ include.page_type }}, referencie fontes de um desses domínios ou use [fontes web-safe](https://www.w3schools.com/cssref/css_websafe_fonts.php).

Para práticas recomendadas de gerenciamento de lista de e-mails, consulte [Inscrições de e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions).