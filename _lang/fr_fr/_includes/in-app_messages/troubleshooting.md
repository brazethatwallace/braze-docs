### Résolution des problèmes d'affichage {#troubleshooting-in-app-message-display}

Si votre application demande et reçoit des messages in-app mais qu'ils ne s'affichent pas, il se peut que la logique côté appareil empêche l'affichage :

1. L'événement déclencheur se déclenche-t-il comme prévu ? Pour le vérifier, configurez le message pour qu'il se déclenche à l'aide d'une action différente (comme le démarrage d'une session) et vérifiez s'il s'affiche.
{% if include.sdk == "iOS" %}
2. Les messages in-app déclenchés sont soumis à une limitation de débit basée sur l'[intervalle de temps minimum entre les déclenchements]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=swift#overriding-the-default-rate-limit), qui est de 30 secondes par défaut.
{% elsif include.sdk == "Android" %}
2. Les messages in-app déclenchés sont soumis à une limitation de débit basée sur l'[intervalle de temps minimum entre les déclenchements]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=android#overriding-the-default-rate-limit), qui est de 30 secondes par défaut.
{% elsif include.sdk == "Web" %}
2. Les messages in-app déclenchés sont soumis à une limitation de débit basée sur l'[intervalle de temps minimum entre les déclenchements]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web#overriding-the-default-rate-limit), qui est de 30 secondes par défaut.
{% endif %}
3. Les échecs de téléchargement d'images empêchent l'affichage des messages in-app contenant des images. Vérifiez les journaux de votre appareil pour détecter d'éventuels échecs de téléchargement. Essayez de supprimer temporairement l'image pour voir si le message s'affiche.
{% case include.sdk %}
  {% when "iOS" %}
4. Si vous avez défini un délégué pour personnaliser la gestion des messages in-app, vérifiez qu'il ne bloque pas l'affichage. Consultez [Personnalisation]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift).
  {% when "Android" %}
4. Si vous avez défini un délégué pour personnaliser la gestion des messages in-app, vérifiez qu'il ne bloque pas l'affichage. Consultez [Personnalisation]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).
  {% when "Web" %}
4. Si vous utilisez une gestion personnalisée des messages in-app via [`braze.subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage), vérifiez que le rappel ne bloque pas l'affichage. Consultez [Personnalisation]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=web).
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
5. Si l'orientation de l'appareil ne correspond pas au paramètre du message in-app, celui-ci ne s'affichera pas.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
6. Selon les conditions réseau, les images peuvent être téléchargées avant l'affichage. Sur les connexions lentes ou les appareils peu performants, prévoyez un délai supplémentaire ou optimisez la taille des ressources.
{% endcase %}

{% if include.sdk == "iOS" %}
### Les impressions et les clics ne sont pas enregistrés {#impressions-and-clicks-arent-being-logged}

Si vous avez défini un délégué de message in-app pour gérer manuellement l'affichage du message ou les actions de clic, vous devez enregistrer manuellement les [clics](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) et les [impressions](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:)) sur le message in-app.
{% elsif include.sdk == "Android" %}
### Les impressions et les clics ne sont pas enregistrés

Si vous avez défini un délégué de message in-app pour gérer manuellement l'affichage du message ou les actions de clic, vous devez enregistrer manuellement les clics et les impressions sur le message in-app.
{% endif %}