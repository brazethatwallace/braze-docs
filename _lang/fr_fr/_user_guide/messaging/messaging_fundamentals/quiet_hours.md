---
nav_title: Heures calmes
article_title: Heures calmes
page_order: 4
page_type: reference
description: "Cet article de référence explique ce que sont les heures calmes, comment Braze gère les messages pendant cette période, et comment les heures calmes interagissent avec le timing intelligent."
---

# Heures calmes {#quiet-hours}

> Les heures calmes empêchent l'envoi de messages pendant une fenêtre de temps définie. Vous pouvez les utiliser pour éviter de contacter les utilisateurs à des moments inopportuns (comme la nuit ou tôt le matin) tout en envoyant les messages à un moment optimal en dehors de cette fenêtre.

Les heures calmes sont configurées au niveau de la Campaign ou du Canvas. Vous pouvez également définir des [heures calmes au niveau du workspace]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours) comme valeur par défaut pour un canal de communication à l'échelle de votre workspace (accès anticipé).

## Fonctionnement des heures calmes {#how-quiet-hours-work}

Lorsque les heures calmes sont activées et qu'un message devrait normalement être envoyé pendant la fenêtre restreinte, Braze retient le message et le distribue au prochain créneau disponible après la fin des heures calmes.

Par exemple, si les heures calmes s'étendent de 22 h à 6 h et qu'un message est planifié pour 5 h 30, Braze le distribue à 6 h à la place.

{% alert note %}
Les heures calmes s'appliquent dans le fuseau horaire local de chaque utilisateur.
{% endalert %}

## Heures calmes et timing intelligent {#quiet-hours-and-intelligent-timing}

Les heures calmes et le timing intelligent fonctionnent indépendamment. Activer les heures calmes ne nécessite pas que le timing intelligent soit activé, et inversement. De manière générale, nous recommandons de choisir l'un ou l'autre plutôt que d'utiliser les deux ensemble, sauf si des exigences de politique, de conformité ou autres rendent les heures calmes nécessaires en complément du timing intelligent.

- **Sans timing intelligent :** les heures calmes agissent comme une fenêtre de non-envoi pour votre heure d'envoi planifiée. Si l'heure planifiée tombe dans les heures calmes, le message est retenu et envoyé à la fermeture de la fenêtre.
- **Avec le timing intelligent :** Braze calcule toujours l'heure d'envoi optimale de chaque utilisateur. Si cette heure tombe dans les heures calmes, le message est retenu et distribué au bord le plus proche de la fenêtre calme.

Pour plus d'informations sur la configuration des heures calmes au sein d'une campagne avec timing intelligent, consultez [Timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing).

## Considérations {#considerations}

- **Les messages sont envoyés en même temps à la fin des heures calmes.** Si une large audience a des messages retenus pendant les heures calmes, tous ces messages sont envoyés en même temps à la fermeture de la fenêtre. Pour les campagnes sensibles au temps, tenez compte de l'impact sur le timing de réception.
- **Les heures calmes ne sont pas la même chose que l'abandon d'un message.** L'abandon d'un message le supprime entièrement. Les heures calmes retiennent le message et le distribuent plus tard.
- **Les heures calmes ne réévaluent pas l'appartenance au Segment pour un envoi retenu.** Braze vérifie l'appartenance au Segment au moment où le message est déclenché. Si l'utilisateur est éligible à ce moment-là, Braze retient le message et l'envoie à la fin des heures calmes. Cela est distinct de la [réévaluation de l'appartenance au Segment au moment de l'envoi]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#audience-criteria-evaluation) ou des [validations de distribution]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) de Canvas.
- **Les heures calmes sont distinctes de la limite de fréquence et de la limitation du débit.** Chacun de ces contrôles de distribution s'applique indépendamment. Un message qui respecte les limites de fréquence et de débit peut tout de même être retenu par les heures calmes, et un message retenu par les heures calmes est évalué par rapport aux limites de débit au moment de son envoi effectif. Pour en savoir plus, consultez [Limitation du débit et limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

## Articles connexes {#related-articles}

- [Heures calmes de l'espace de travail]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours)