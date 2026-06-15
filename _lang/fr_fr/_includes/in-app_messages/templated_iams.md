Les messages in-app sont délivrés sous forme de messages in-app modélisés lorsque l'option **Réévaluer l'éligibilité de la campagne avant l'affichage** est sélectionnée ou si l'une des étiquettes Liquid suivantes est présente dans le message :

- `canvas_entry_properties`
- `connected_content`
- Les variables SMS telles que {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Cela signifie qu'au démarrage de la session, l'appareil recevra uniquement le déclencheur de ce message in-app, et non le message complet. Lorsque l'utilisateur déclenche le message in-app, son appareil effectue une requête réseau pour récupérer le message réel.

{% alert note %}
Le message ne sera pas délivré si l'appareil n'a pas accès à Internet. Il est également possible que le message ne soit pas délivré si la logique Liquid met trop de temps à être résolue.
{% endalert %}