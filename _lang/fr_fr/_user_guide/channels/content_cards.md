---
nav_title: Cartes de contenu
article_title: Cartes de contenu
page_order: 2
page_type: landing
description: "Envoyez un flux dynamique de contenu enrichi à vos utilisateurs grâce aux Cartes de contenu, intégrées directement dans votre application ou votre site web."
channel:
  - content cards
search_rank: 5
---

# Cartes de contenu

> Les Cartes de contenu vous permettent d'envoyer un flux de contenu enrichi, hautement ciblé et dynamique, à vos clients au sein des applications qu'ils utilisent, sans interrompre leur expérience. Les Cartes de contenu sont intégrées directement dans votre application ou votre site web, ce qui vous permet de créer des boîtes de réception de messages et des interfaces personnalisées qui étendent la portée d'autres canaux tels que l'e-mail ou les notifications push.

## Conditions préalables

La disponibilité des Cartes de contenu dépend de votre offre Braze. Contactez votre gestionnaire de compte ou votre gestionnaire de la satisfaction client pour commencer.

Avant de pouvoir utiliser les Cartes de contenu, vous devez intégrer le [SDK Braze]({{site.baseurl}}/developer_guide/content_cards/) dans votre application ou votre site web. Aucune configuration supplémentaire n'est requise. Pour créer votre propre interface utilisateur, consultez le [guide de personnalisation des Cartes de contenu]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/).

## Avantages des Cartes de contenu

Voici quelques avantages des Cartes de contenu par rapport à un contenu intégré directement dans votre application par vos développeurs :

- **Segmentation et personnalisation simplifiées :** Vos données utilisateur sont stockées dans Braze, ce qui facilite la définition de votre audience et la personnalisation de vos messages avec Content Cards.
- **Reporting centralisé :** L'analyse des Cartes de contenu est suivie dans Braze, ce qui vous donne une visibilité sur l'ensemble de vos Campaigns en un seul endroit.
- **Parcours client cohérents :** Vous pouvez combiner Content Cards avec d'autres canaux dans Braze pour créer des expériences client homogènes. Un cas d'utilisation courant consiste à envoyer une notification push, puis à enregistrer cette notification sous forme de Content Card dans votre application pour les utilisateurs qui n'ont pas interagi avec le push. Si le contenu est intégré directement dans votre application par vos développeurs, il reste isolé du reste de vos communications.
- **Aucun abonnement requis :** Comme In-App Messages, Content Cards ne nécessitent ni abonnement ni autorisation de la part de vos utilisateurs. Cependant, alors que In-App Messages ne nécessitent pas d'autorisation et sont éphémères, Content Cards ne nécessitent pas d'autorisation et sont permanentes. Les stratégies de communication qui associent In-App Messages et Content Cards offrent ainsi un excellent équilibre.
- **Plus de contrôle sur l'expérience de communication :** Même si vous aurez besoin de vos développeurs pour la configuration initiale de Content Cards, vous pourrez ensuite contrôler le message, les destinataires, le timing et bien plus encore directement depuis votre tableau de bord de Braze.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## Les Cartes de contenu en chiffres

Lorsque vous créez des Cartes de contenu dans Braze, vous pouvez mettre à jour vos messages et mesurer leur impact sans avoir à refondre votre application ou votre site web. Voici quelques résultats clés issus des recherches de Braze :

- Les Content Cards sont **38 fois** plus efficaces que l'e-mail pour stimuler les ventes sur une période de 72 heures.[^1]
- L'utilisation de Content Cards dans les campagnes d'inscription aux programmes de fidélité multiplie les conversions par **5**.[^1]
- La communication via les notifications push, In-App Messages et Content Cards génère **6,9 fois** plus de sessions que les notifications push seules.[^2]
- La communication via l'e-mail, In-App Messages et Content Cards multiplie par **3,6** la durée de vie moyenne des utilisateurs par rapport à l'e-mail seul.[^2]

[^1]: [8 conseils pour tirer le meilleur parti de vos campagnes de fidélisation client](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Rapport : la différence en matière de marketing multicanal](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)

## Cas d'utilisation

Consultez cette section pour découvrir quelques cas d'utilisation courants des Cartes de contenu.

{% alert tip %}
Pour plus d'inspiration, consultez le [Guide d'inspiration pour les Cartes de contenu](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), qui comprend plus de 20 campagnes personnalisables, notamment des programmes de recommandation, des lancements de nouveaux produits et des renouvellements d'abonnement.
{% endalert %}

{% tabs %}
{% tab Onboarding et étapes suivantes %}

Lorsque de nouveaux utilisateurs explorent votre application et votre site web, guidez-les à travers les avantages de votre offre grâce à des Cartes de contenu placées de manière stratégique. Encouragez les utilisateurs à s'abonner à d'autres canaux de communication avec une carte de contenu sur votre page d'accueil, et enregistrez les tâches d'onboarding restantes dans un onglet dédié alimenté par les Cartes de contenu. N'oubliez pas de supprimer une carte une fois que l'utilisateur a accompli la tâche souhaitée !

![Exemple de cas d'utilisation d'onboarding avec les Cartes de contenu.]({% image_buster /assets/img_archive/cc_usecase_onboarding.png %})

{% endtab %}
{% tab Participation aux événements %}

Affichez des Cartes de contenu en haut de la page d'accueil d'un utilisateur pour encourager la participation aux événements, en utilisant le ciblage par localisation pour atteindre les utilisateurs potentiels là où ils se trouvent. Inviter les utilisateurs à des événements physiques pertinents leur donne un sentiment d'exclusivité, surtout avec des messages personnalisés qui exploitent leur activité précédente avec votre marque.

![Exemple de cas d'utilisation de participation aux événements avec les Cartes de contenu.]({% image_buster /assets/img_archive/cc_usecase_event.png %})

{% endtab %}
{% tab Recommandations %}

Exploitez les données dont vous disposez sur les comportements et les préférences des utilisateurs pour afficher du contenu pertinent en temps réel via des Cartes de contenu sur la page d'accueil ou dans la boîte de réception, et ramenez-les vers votre offre produit.

![Exemple de cas d'utilisation de recommandations avec les Cartes de contenu.]({% image_buster /assets/img_archive/cc_usecase_recommendation.png %})

{% endtab %}
{% tab Ventes et promotions %}

Tirez parti des Cartes de contenu pour mettre en avant des messages promotionnels et des offres non réclamées directement sur votre page d'accueil ou dans une boîte de réception promotionnelle dédiée. Affichez du contenu pertinent basé sur les achats précédents de chaque client pour proposer des promotions personnalisées qui captent l'attention.

![Exemple de cas d'utilisation de ventes et promotions avec les Cartes de contenu.]({% image_buster /assets/img_archive/cc_usecase_promo.png %})

{% endtab %}
{% endtabs %}

### Autres cas d'utilisation

Au-delà de ces principaux cas d'utilisation, les clients utilisent les Cartes de contenu de nombreuses façons différentes. La force des Cartes de contenu réside dans leur flexibilité. Si le cas d'utilisation que vous recherchez n'est pas présenté ici, vous pouvez configurer des [paires clé-valeur]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/) et envoyer les payloads à votre application ou votre site web.

Pour un aperçu de la mise en œuvre des emplacements de Cartes de contenu dans votre application ou votre site web, consultez [Créer des Cartes de contenu personnalisées]({{site.baseurl}}/developer_guide/content_cards/creating_cards/).

## Étapes suivantes

- [Créer une carte de contenu]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/)
- [Détails créatifs]({{site.baseurl}}/user_guide/channels/content_cards/creative_details/)