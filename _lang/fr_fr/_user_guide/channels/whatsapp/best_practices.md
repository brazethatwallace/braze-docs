---
nav_title: Bonnes pratiques
article_title: Bonnes pratiques
page_order: 22
description: "Cet article présente les bonnes pratiques recommandées lors de l'utilisation du canal de communication WhatsApp, notamment comment maintenir une note de qualité téléphonique élevée et éviter un taux élevé de blocages et de signalements."
page_type: reference
channel:
  - WhatsApp


---
# Bonnes pratiques pour WhatsApp {#whatsapp-best-practices}

> Avant d'envoyer vos messages WhatsApp, consultez ces bonnes pratiques recommandées pour maintenir une note de qualité téléphonique élevée, éviter les blocages et les signalements, et gérer l'abonnement et le désabonnement des utilisateurs.

## Maintenir une note de qualité téléphonique élevée {#maintain-a-high-phone-quality-rating}

WhatsApp base sa [note de qualité téléphonique](https://www.facebook.com/business/help/896873687365001) sur les actions effectuées par les utilisateurs qui reçoivent vos messages, comme le blocage ou le signalement de votre entreprise. Il est important de maintenir une note de qualité élevée, car si elle est basse et ne s'améliore pas au bout d'un certain temps, votre limite d'envoi de messages peut diminuer.

La première fois que vous envoyez un message à un utilisateur sur WhatsApp, ces options s'affichent dans le fil de conversation.

![Fil de conversation WhatsApp avec des options pour bloquer ou signaler une entreprise]({% image_buster /assets/img/whatsapp/whatsapp_block_report.png %}){: style="max-width:30%;"}

{% alert note %}
Pour consulter les indicateurs relatifs à vos blocages et signalements, assurez-vous que l'[onglet Insights](https://www.facebook.com/business/help/683499390267496) est activé dans votre WhatsApp Manager.
{% endalert %}

Pour éviter un nombre élevé de blocages et de signalements, Braze recommande les bonnes pratiques suivantes afin de maintenir une note de qualité téléphonique élevée et des limites d'envoi de messages stables.

### Respecter les exigences et les directives d'abonnement de WhatsApp {#follow-whatsapp-opt-in-requirements-and-guidelines}

Assurez-vous que tous les utilisateurs ont activement consenti à recevoir des messages WhatsApp avant de commencer à communiquer avec eux sur WhatsApp. Lorsque vous demandez aux utilisateurs de s'abonner, ils doivent être informés qu'ils acceptent spécifiquement de recevoir des messages de votre entreprise via WhatsApp.

{% alert note %}
Pour plus d'informations sur les exigences d'abonnement et des conseils utiles, consultez [Get Opt-in for WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/).
{% endalert %}

### Suivre les bonnes pratiques d'envoi de messages {#follow-messaging-best-practices}

- Faites en sorte que le nom de votre canal reflète votre marque afin que les utilisateurs reconnaissent que le message provient de vous et non d'un spam.
- Envoyez un message de confirmation aux utilisateurs après avoir recueilli leur consentement d'abonnement.
- Envoyez vos messages à des horaires appropriés.

### Offrir aux clients la possibilité de se désabonner {#give-customers-the-option-to-opt-out}

Les désinscriptions n'ont pas d'impact sur votre note de qualité téléphonique. Il est donc préférable qu'un utilisateur se désabonne des communications WhatsApp plutôt qu'il vous bloque ou vous signale.

Une bonne pratique recommandée consiste à fournir des instructions sur la manière de se désabonner dans le pied de page du premier message que vous envoyez aux utilisateurs. Par exemple, vous pourriez indiquer que les utilisateurs peuvent se désabonner de votre canal WhatsApp en répondant avec votre mot-clé de désinscription. Vous pouvez également inclure régulièrement le pied de page de désinscription dans vos futures Campaigns. Pour savoir comment configurer cela, consultez [Abonnement et désinscription]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs).

![Message WhatsApp avec un pied de page indiquant de répondre STOP pour se désabonner du canal]({% image_buster /assets/img/whatsapp/whatsapp_unsubscribe.png %}){: style="max-width:35%;"}

### Minimiser la latence de réponse pour les flux bidirectionnels {#minimize-response-latency-for-two-way-flows}

Pour les flux Canvas interactifs qui répondent avec des [messages de réponse]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats#response-messages) :

- Placez l'étape de message de réponse immédiatement après le déclencheur entrant ou l'évaluation du parcours d'action.
- Utilisez des [webhooks]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) au lieu d'étapes de mise à jour utilisateur lorsque des modifications d'abonnement ne sont pas nécessaires avant la réponse.
- Évitez les longs délais ou les attentes de plusieurs jours entre les messages entrants et les envois de réponse ; la fenêtre de service client WhatsApp est de 24 heures par message entrant.