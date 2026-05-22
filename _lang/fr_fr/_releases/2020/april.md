---
nav_title: avril
page_order: 9
noindex: true
page_type: update
description: "Cet article contient les notes de version d'avril 2020."
---
# Avril 2020 {#april-2020}

## Partenariat avec Movable Ink {#movable-ink-partnership}

Movable Ink permet aux clients de Braze d'utiliser des fonctionnalités créatives intelligentes telles que des comptes à rebours, des sondages et des surfaces à gratter dans leurs campagnes de notification push, de messages in-app et de cartes de contenu. L'intégration entre Movable Ink et Braze permet une approche plus complète pour les messages dynamiques axés sur les données, en offrant aux utilisateurs des éléments en temps réel sur les sujets qui comptent.

Commencez à [intégrer Movable Ink]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/) dans vos campagnes !

## Timing intelligent {#intelligent-timing}

Lors de la planification d'une campagne, vous pouvez utiliser le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/) (anciennement Intelligent Delivery) pour envoyer votre message à chaque utilisateur au moment où Braze estime qu'il est le plus susceptible de s'engager.

Les mises à jour de cette fonctionnalité comprennent :
- **Clarification des heures calmes** : la fonctionnalité des heures calmes reste inchangée, mais l'interface utilisateur a été modifiée pour plus de clarté.
- **Ajout du graphique de prévisualisation** : vous pouvez maintenant générer un graphique pour voir combien d'utilisateurs recevront des messages à chaque heure de la journée avec le timing intelligent, ainsi que la proportion d'utilisateurs ayant suffisamment de données pour calculer un moment d'envoi optimal.
- **Ajout d'un repli personnalisé** : vous pouvez maintenant choisir l'heure locale à laquelle envoyer un message aux utilisateurs lorsqu'ils ne disposent pas de suffisamment de données d'engagement pour calculer un moment d'envoi optimal.

## Exportation d'audience Facebook {#facebook-audience-export}

Braze permet d'exporter manuellement vos utilisateurs à partir de la page Segments de Braze pour créer des audiences personnalisées Facebook. Il s'agit d'une exportation d'audience unique et statique qui ne créera que de nouvelles [audiences personnalisées Facebook]({{site.baseurl}}/partners/facebook/).

Disponible pour tous les clusters, un nouveau processus d'exportation d'audience Facebook de Braze simplifie le flux de travail grâce à des étapes d'intégration claires. Vous n'avez plus besoin de mettre sur liste blanche les URI de redirection OAuth pour envoyer des audiences personnalisées ni d'ajuster les paramètres de l'application Facebook pour l'intégration.

{% alert important %}
Notez que tous les clients utilisant actuellement Facebook Custom Audiences doivent réintégrer leurs Segments Braze avec ces nouvelles étapes.
{% endalert%}


## Mises à jour API du bloc de contenu et du modèle d'e-mail {#content-block-and-email-template-api-updates}

Les endpoints [template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) et [content_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) ont été mis à jour pour inclure un nouveau champ `tags`. Ce champ s'affichera sous forme de tableau listant toutes les étiquettes qui s'appliquent au bloc de contenu ou au modèle d'e-mail concerné.

## Adresse d'expéditeur personnalisée {#personalized-from-address}

Lors de la création d'un e-mail dans Braze, vous pouvez désormais personnaliser l'adresse de l'expéditeur du message dans la section **Sending Info** de la composition de l'e-mail. Vous pouvez utiliser n'importe lequel de nos [tags de personnalisation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/) pris en charge.

![Adresse d'expéditeur personnalisée]({% image_buster /assets/img/personalized-from-name.png %}){: style="max-width:80%"}