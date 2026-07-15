### Domaines de polices externes {#external-font-domains}

Lors de la création de pages {{ include.page_type }} personnalisées, Braze assainit les entrées HTML pour prévenir les attaques de type cross-site scripting (XSS). Dans le cadre de cette mesure de sécurité, les URL de ressources externes, y compris les URL de polices, sont supprimées à moins qu'elles ne proviennent des domaines autorisés suivants :

- `assets.appboycdn.com`
- `braze-images.com`
- `cdn.braze.com`
- `cdn.braze.eu`
- `fonts.googleapis.com`
- `fonts.gstatic.com`

Si vous devez utiliser des polices personnalisées dans votre page {{ include.page_type }}, référencez des polices provenant de l'un de ces domaines ou utilisez des [polices web-safe](https://www.w3schools.com/cssref/css_websafe_fonts.php) à la place.

Pour les bonnes pratiques de gestion des listes d'e-mails, consultez [Abonnements e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions).