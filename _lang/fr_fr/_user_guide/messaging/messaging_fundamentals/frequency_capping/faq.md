---
nav_title: FAQ
article_title: FAQ sur les limites de débit et les limites de fréquence
page_order: 0
page_type: FAQ
description: "Cet article fournit des réponses aux questions fréquemment posées sur les limites de débit et les limites de fréquence."
tool: Campaigns

---

# Questions fréquemment posées {#frequently-asked-questions}

> Cet article fournit des réponses aux questions fréquemment posées sur les limites de débit et les limites de fréquence.

### Si je modifie la limitation d'envoi d'un Canvas actif, cela affecte-t-il les utilisateurs déjà dans le Canvas ? {#if-i-change-a-send-throttle-on-an-active-canvas-does-it-affect-users-already-in-the-canvas}

Oui, lorsque vous augmentez ou diminuez une limite de débit d'un Canvas, la limite mise à jour s'applique aux nouveaux messages. Il peut y avoir un bref délai avant que la mise à jour ne soit reflétée dans l'ensemble du Canvas.

### Que se passe-t-il si un utilisateur atteint une étape Message d'un Canvas mais dépasse la limite de fréquence globale ? {#what-happens-if-a-user-reaches-a-canvas-message-step-but-is-over-the-global-frequency-cap}

L'utilisateur ne reçoit pas cet envoi pour le canal limité, mais il suit toujours les règles d'avancement de votre étape Message. Les étapes Message font avancer les utilisateurs lorsqu'un message n'est pas envoyé en raison de la limite de fréquence globale, de sorte qu'ils passent à l'étape suivante du Canvas. Pour la liste complète des cas d'avancement, consultez [Comment les utilisateurs avancent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#how-users-advance).

### Comment puis-je identifier les utilisateurs qui ont été limités par la fréquence dans un Canvas ? {#how-can-i-identify-users-who-were-frequency-capped-in-a-canvas}

Les utilisateurs limités par la fréquence ne génèrent pas d'événement d'envoi pour cette étape. Pour identifier ces utilisateurs, vous pouvez utiliser [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) pour suivre les événements de messages abandonnés où `abort_type` est `frequency_capped`. Vous pouvez également créer une [Segment Extension]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) pour analyser les utilisateurs qui sont entrés dans le Canvas mais n'ont pas reçu le message attendu.

### Comment les jours calendaires et les fuseaux horaires sont-ils utilisés pour les limites de fréquence globales « par jour » ? {#how-are-calendar-days-and-time-zones-used-for-per-day-global-frequency-caps}

La limite de fréquence globale utilise le fuseau horaire de l'utilisateur et compte par jour calendaire, et non par périodes glissantes de 24 heures. Pour un exemple, consultez [Règles de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-rules).

### La limite de fréquence globale s'applique-t-elle aux messages in-app déclenchés ? {#does-global-frequency-capping-apply-to-triggered-in-app-messages}

Non, la limite de fréquence globale s'applique uniquement aux messages push, e-mail, SMS, webhook, WhatsApp et LINE.

### La limite de fréquence s'applique-t-elle aux campagnes reçues ou aux messages individuels au sein d'un envoi ? {#does-frequency-capping-limit-campaigns-received-or-individual-messages-inside-a-send}

La limite de fréquence s'applique par envoi : chaque envoi de campagne ou d'étape du Canvas compte dans vos limites, et non chaque variante ou plateforme au sein d'un envoi. Pour plus d'informations, consultez [Règles de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-rules).

### Si plusieurs messages sont éligibles en même temps et que seuls certains respectent la limite, quels messages sont envoyés ? {#if-several-messages-are-eligible-at-the-same-time-and-only-some-fit-under-the-cap-which-messages-send}

Braze envoie jusqu'à la limite. Lorsque plusieurs envois sont en concurrence dans la même fenêtre, les messages traités en premier sont ceux qui comptent dans la limite. Les envois restants dans cette fenêtre sont limités.

### Les webhooks échoués comptent-ils dans la limite de fréquence globale ? {#do-failed-webhooks-count-toward-the-global-frequency-cap}

Non. Un webhook compte dans la limite lorsque Braze enregistre une distribution réussie. Les réponses de webhook non réussies (par exemple, les codes d'état `4xx` ou `5xx`) ne comptent pas dans la limite.