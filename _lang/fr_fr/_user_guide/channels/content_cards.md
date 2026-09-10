---
nav_title: Content Cards
article_title: Content Cards
page_order: 2
page_type: landing
description: "Envoyez un flux dynamique de contenu enrichi à vos utilisateurs grâce aux Content Cards, intégrées directement dans votre application ou votre site web."
channel:
  - content cards
search_rank: 5
---

# Content Cards {#content-cards}

> Les Content Cards vous permettent d'envoyer un flux de contenu enrichi, hautement ciblé et dynamique, à vos clients au sein des applications qu'ils utilisent, sans interrompre leur expérience. Les Content Cards sont intégrées directement dans votre application ou votre site web, ce qui vous permet de créer des boîtes de réception de messages et des interfaces personnalisées qui étendent la portée d'autres canaux tels que l'e-mail ou les notifications push.

## Prérequis {#prerequisites}

La disponibilité des Content Cards dépend de votre forfait Braze. Contactez votre gestionnaire de compte ou votre gestionnaire de la satisfaction client pour commencer.

Avant de pouvoir utiliser les Content Cards, vous devez intégrer le [SDK Braze]({{site.baseurl}}/developer_guide/content_cards) dans votre application ou votre site web. Aucune configuration supplémentaire n'est requise. Pour créer votre propre interface utilisateur, consultez le [guide de personnalisation des Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards).

## Avantages de l'utilisation des Content Cards {#benefits-of-using-content-cards}

Voici quelques avantages de l'utilisation des Content Cards par rapport au développement de contenu directement dans votre application par vos développeurs :

- **Segmentation et personnalisation simplifiées :** Vos données utilisateur sont hébergées dans Braze, ce qui facilite la définition de votre audience et la personnalisation de vos messages avec les Content Cards.
- **Rapports centralisés :** L'analytique des Content Cards est suivie dans Braze, ce qui vous donne une visibilité sur l'ensemble de vos Campaigns depuis un seul endroit.
- **Parcours client cohérents :** Vous pouvez combiner les Content Cards avec d'autres canaux dans Braze pour créer des expériences client harmonieuses. Un cas d'usage courant consiste à envoyer une notification push, puis à enregistrer cette notification en tant que Content Card dans votre application pour tous ceux qui n'ont pas interagi avec le push. Si le contenu est intégré directement dans votre application par vos développeurs, il est alors isolé du reste de vos communications.
- **Aucun abonnement requis :** Tout comme les In-App Messages, les Content Cards ne nécessitent ni abonnement ni autorisation de la part de vos utilisateurs. Mais alors que les In-App Messages sont sans autorisation et éphémères, les Content Cards sont sans autorisation et permanentes. Cela signifie que les stratégies de communication qui associent les In-App Messages et les Content Cards offrent un excellent équilibre.
- **Plus de contrôle sur l'expérience de communication :** Bien que vous ayez encore besoin de vos développeurs pour la configuration initiale des Content Cards, vous pourrez ensuite gérer le message, les destinataires, le calendrier et bien plus encore directement depuis votre tableau de bord Braze.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## Les Content Cards en chiffres {#content-cards-by-the-numbers}

Lorsque vous créez des Content Cards dans Braze, vous pouvez mettre à jour vos messages et mesurer leur impact sans avoir à refondre votre application ou votre site web. Voici les points clés issus des recherches de Braze :

- Les Content Cards sont **38 fois** plus efficaces que l'e-mail pour stimuler les ventes sur une fenêtre de 72 heures.[^1]
- L'utilisation des Content Cards dans les Campaigns d'inscription à un programme de fidélité multiplie les conversions par **5**.[^1]
- La communication via les notifications push, les In-App Messages et les Content Cards génère **6,9 fois** plus de sessions que les notifications push seules.[^2]
- La communication via l'e-mail, les In-App Messages et les Content Cards multiplie par **3,6** la durée de vie moyenne des utilisateurs par rapport à l'e-mail seul.[^2]

## Cas d'usage {#use-cases}

Consultez cette section pour découvrir quelques cas d'usage courants pour les Content Cards.

{% alert tip %}
Pour plus d'inspiration, consultez le [guide d'inspiration Content Cards](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), qui comprend plus de 20 campagnes personnalisables, notamment des programmes de recommandation, des lancements de produits et des renouvellements d'abonnement.
{% endalert %}

{% tabs %}
{% tab Onboarding et prochaines étapes %}

Lorsque de nouveaux utilisateurs explorent votre application et votre site web, guidez-les à travers les valeurs et avantages de ce que vous proposez grâce à des Content Cards placées de manière stratégique. Encouragez les utilisateurs à s'abonner à d'autres canaux de communication avec une Content Card sur votre page d'accueil, et enregistrez les tâches d'onboarding restantes dans un onglet dédié alimenté par les Content Cards. N'oubliez pas de supprimer une carte une fois que l'utilisateur a accompli la tâche souhaitée !

![Exemple de cas d'usage d'onboarding avec les Content Cards.]({% image_buster /assets/img_archive/cc_usecase_onboarding.png %})

{% endtab %}
{% tab Participation à des événements %}

Mettez en avant des Content Cards en haut de la page d'accueil d'un utilisateur pour encourager la participation à des événements, en utilisant le ciblage par localisation pour toucher les utilisateurs potentiels là où ils se trouvent. Inviter les utilisateurs à des événements physiques pertinents les fait se sentir spéciaux, surtout avec des messages personnalisés qui exploitent leur activité antérieure avec votre marque.

![Exemple de cas d'usage de participation à des événements avec les Content Cards.]({% image_buster /assets/img_archive/cc_usecase_event.png %})

{% endtab %}
{% tab Recommandations %}

Utilisez les données dont vous disposez sur les comportements et préférences des utilisateurs pour afficher du contenu pertinent en temps réel à partir de Content Cards sur la page d'accueil ou dans la boîte de réception, et incitez-les à revenir vers votre offre de produits.

![Exemple de cas d'usage de recommandations avec les Content Cards.]({% image_buster /assets/img_archive/cc_usecase_recommendation.png %})

{% endtab %}
{% tab Ventes et promotions %}

Tirez parti des Content Cards pour mettre en avant des messages promotionnels et des offres non réclamées directement sur votre page d'accueil ou dans une boîte de réception promotionnelle dédiée. Intégrez du contenu pertinent basé sur les achats précédents de chaque client pour proposer des promotions personnalisées et percutantes.

![Exemple de cas d'usage de ventes et promotions avec les Content Cards.]({% image_buster /assets/img_archive/cc_usecase_promo.png %})

{% endtab %}
{% endtabs %}

### Autres cas d'usage {#other-use-cases}

En dehors de ces principaux cas d'usage, les clients utilisent les Content Cards de nombreuses manières différentes. La force des Content Cards réside dans leur flexibilité. Si le cas d'usage que vous souhaitez n'est pas présenté ici, vous pouvez configurer des [paires clé-valeur]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) et envoyer les payloads à votre application ou site web.

Pour un aperçu de la mise en œuvre des emplacements de Content Cards dans votre application ou votre site web, consultez [Créer des Content Cards personnalisées]({{site.baseurl}}/developer_guide/content_cards/creating_cards).

## Prochaines étapes {#next-steps}

{% article_tiles %}
- name: Créer une carte de contenu
  link: /docs/user_guide/channels/content_cards/create_a_content_card
- name: Détails créatifs
  link: /docs/user_guide/channels/content_cards/creative_details
{% endarticle_tiles %}

[^1]: [8 conseils pour tirer le meilleur parti de vos campagnes de rétention client](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Rapport : la différence du marketing cross-canal](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)