---
nav_title: Événements personnalisés éphémères
permalink: /ephemeral_custom_events/
hidden: true
page_type: reference
---

# Événements personnalisés éphémères {#ephemeral-custom-events}

- Les événements personnalisés éphémères n'incluent pas les événements d'achat ni les événements de début et de fin de session (tels que décrits dans la documentation Braze).
- Braze ne transmet pas et ne stocke pas les événements personnalisés en tant que points de donnée dans Braze pour un maximum de 12 emplacements/noms d'événements par implémentation SDK.
- La solution d'événements éphémères est intégrée aux SDK de production iOS et Android de Braze, ainsi qu'à tout futur SDK de production Braze pour les plateformes sur lesquelles Braze a activé la solution d'événements personnalisés éphémères. Cela garantit que le client peut utiliser ces SDK de production sans être désynchronisé par rapport aux futures fonctionnalités et corrections de bugs. Cela garantit également que le client peut bénéficier des futures mises à jour du SDK sans avoir besoin d'autres processus personnalisés.
<!--
Keep this doc available on the docs site with the above permalink until 1/21/2026. This feature was built as a one-off page for a customer. Reach out to Rod Amies with questions, if needed.
-->