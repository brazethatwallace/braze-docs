---
article_title: Limites de débit pour les Campaigns push et les Canvas multicanaux
permalink: /rate_limiting_v3/
page_type: reference
description: "Cet article décrit les limites de débit de vitesse de distribution pour les Campaigns push et les Canvas multicanaux."
---

# Limites de débit pour les Campaigns push et les Canvas multicanaux {#rate-limiting-for-push-campaigns-and-multichannel-canvases}

> Cette page couvre les limites de débit pour les Campaigns push et les Canvas multicanaux, y compris les points à garder à l'esprit lorsque vous réglez vos messages.

Lorsque vous définissez les limites de débit de vitesse de distribution pour les Campaigns push et les Canvas multicanaux, vous pouvez désormais choisir entre :

- Des limites de débit par canal
- Une limite de débit globale partagée entre tous les canaux de messages.

{% alert important %}
Les limites de débit pour les Campaigns push et les Canvas multicanaux sont en accès anticipé. Contactez le gestionnaire de votre compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

Les fonctionnalités suivantes **ne sont pas** incluses dans cet accès anticipé :

- Définir des limites de débit par canal sur les Campaigns multicanaux de tout type et les Canvas déclenchés par API
- Définir une limite de débit globale
- Définir des limites de débit par étape de message dans Canvas

## Considérations {#considerations}

- Cette mise à jour des limites de débit ne vous empêche pas de définir une limite de débit très basse. Cela signifie que sans cette protection en place, vous pourriez définir une limite de débit qui, en fonction de la taille de l'audience, pourrait entraîner l'envoi de vos messages à un rythme extrêmement lent.
- Les résumés des **Paramètres d'envoi** pour les Campaigns et les Canvas peuvent contenir des descriptions inexactes pour les limites de débit définies : <br><br>![Paramètres d'envoi pour les Campaigns où il n'y a aucune limitation sur le débit auquel les utilisateurs recevront des messages.]({% image_buster /assets/unlisted_docs/img/send_settings_example.png %}){: style="max-width:65%"}<br><br>
- Les limites de débit pour les Campaigns multicanaux (pas les Canvas ni les Campaigns push) refléteront le [comportement de limitation de débit des Campaigns multicanaux non mis à jour]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting). Nous vous recommandons d'éviter de créer des Campaigns multicanaux avec limite de débit pendant cette phase d'accès anticipé.