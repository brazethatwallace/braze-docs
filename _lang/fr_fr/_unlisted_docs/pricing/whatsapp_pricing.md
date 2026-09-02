---
nav_title: Mises à jour de la tarification WhatsApp
permalink: "/whatsapp_pricing_updates/"
hidden: true
noindex: true
hide_toc: true
---

# Mises à jour de la tarification WhatsApp {#whatsapp-pricing-updates}

## Modifications tarifaires supplémentaires pour WhatsApp en octobre 2025 {#additional-whatsapp-pricing-changes-in-october-2025}
*Dernière mise à jour le 3 septembre 2025*

### Modifications tarifaires dans certaines régions {#pricing-changes-in-some-regions}

À compter du **1er octobre**, Meta met à jour les tarifs dans des marchés spécifiques.

- **Pour les messages utilitaires et d'authentification :** Les tarifs sont réduits en Argentine, en Égypte, au Mexique et en Amérique du Nord afin de garantir que la tarification reste attractive.
- **Pour les messages marketing :** Les tarifs sont réduits au Mexique afin de garantir que la tarification continue de favoriser l'adoption et de soutenir un écosystème de communication sain.

| Pays et type de message | % de variation |
| --- | --- |
| Argentine - Authentification                | -10,04 %  |
| Argentine - Utilitaire                      | -10,04 %  |
| Égypte - Authentification                   | -30,43 %  |
| Égypte - Authentification - International   | -0,58 %   |
| Égypte - Utilitaire                         | -30,43 %  |
| Mexique - Marketing                         | -30,08 %  |
| Amérique du Nord - Authentification         | -70,39 %  |
| Arabie saoudite - Authentification          | -6,89 %   |
| Arabie saoudite - Utilitaire               | -6,89 %   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Modifications tarifaires supplémentaires pour WhatsApp en juillet 2025 {#additional-whatsapp-pricing-changes-in-july-2025}
*Dernière mise à jour le 12 juin 2025*

En plus des mises à jour tarifaires de juillet annoncées précédemment, Meta déploie quelques modifications supplémentaires qui prendront également effet le 1er juillet 2025.

Voici un bref résumé des changements précédemment annoncés :
- La tarification WhatsApp passera à un modèle « par message » au lieu d'un modèle « par conversation ». **Les tarifs « par message » seront identiques aux tarifs actuels « par conversation ».**
- Les modèles utilitaires envoyés en réponse aux messages des utilisateurs (donc dans une [fenêtre de service client](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows) ouverte) seront gratuits.

*Pour plus de détails sur ces changements, consultez la publication précédente datée du 12 mars, plus loin dans cet article.*

Changements supplémentaires du 1er juillet (annoncés par Meta le 15 mai) :
- Meta met à jour les tarifs des messages utilitaires et d'authentification sur plusieurs marchés, dans le cadre d'efforts continus visant à garantir que les prix restent comparables à ceux des canaux alternatifs.
    - Les tarifs pour les messages utilitaires et d'authentification diminuent sur tous les marchés, à l'exception de l'Indonésie. En Indonésie, les tarifs utilitaires augmentent tandis que les tarifs d'authentification diminuent.
- Meta affine sa définition de la catégorie utilitaire, en se basant sur l'engagement et le ressenti des utilisateurs, ce qui entraîne le déplacement de certains cas d'usage vers ou depuis la catégorie utilitaire. Consultez la nouvelle [définition des modèles utilitaires](https://developers.facebook.com/docs/whatsapp/pricing/updates-to-pricing#updates-to-template-category-guidelines) de Meta.

Pour la plupart des clients, ces mises à jour prendront effet automatiquement le 1er juillet.

## Prochaines modifications tarifaires de WhatsApp en juillet 2025 {#upcoming-whatsapp-pricing-changes-in-july-2025}

*Dernière mise à jour le 12 mars 2025 (Publié initialement le 13 décembre 2024)*

WhatsApp apporte deux nouvelles modifications à sa tarification à compter du 1er juillet 2025. Braze mettra à jour ses tarifs pour refléter ces changements à la même date. Un résumé des modifications et des bonnes pratiques pour les prendre en compte est présenté dans la section suivante.

### Mise à jour 1 : la tarification WhatsApp passera à un modèle « par message » au lieu d'un modèle « par conversation ». {#update-1-whatsapp-pricing-will-shift-to-a-per-message-model-instead-of-a-per-conversation-model}

**Les tarifs « par message » seront identiques aux tarifs actuels « par conversation ».**

#### Pourquoi ce changement ? {#why-are-they-making-this-change}

Meta passe à un modèle « par message » pour aider les marques à simplifier les calculs de ROI or retour sur investissement or retour sur investissement (ROI or retour sur investissement). Ce changement permettra également aux marques de comparer plus facilement le ROI or retour sur investissement avec d'autres canaux tarifés au message.

#### Quel impact cela aura-t-il sur mon utilisation actuelle de WhatsApp ? {#how-will-this-affect-my-current-whatsapp-usage}

- Les conversations actuelles envoyées avec un seul modèle de message dans la fenêtre de 24 heures ne seront pas affectées.
- **Les conversations actuelles envoyées avec deux modèles de message ou plus du _même type_ dans la fenêtre de 24 heures verront leur coût augmenter.** Par exemple, envoyer deux modèles marketing dans la période de 24 heures coûtera deux fois plus, car la facturation se fera par modèle de message.

| Exemple de scénario | Tarification avant avril 2025 | Tarification après avril 2025 |
| --- | --- | --- |
| La marque envoie un modèle de message marketing dans la fenêtre de 24 heures | Facturation pour une conversation marketing | Facturation pour un message marketing |
| La marque envoie deux modèles de messages marketing dans la fenêtre de 24 heures | Facturation pour une conversation marketing | Facturation pour deux messages marketing |
| La marque envoie un modèle de message utilitaire dans la fenêtre de 24 heures | Facturation pour une conversation utilitaire | Facturation pour un message utilitaire |
| La marque envoie deux modèles de messages utilitaires dans la fenêtre de 24 heures | Facturation pour une conversation utilitaire | Facturation pour deux messages utilitaires |
| La marque envoie un modèle de message marketing et un modèle de message utilitaire dans la fenêtre de 24 heures | Facturation pour une conversation marketing et une conversation utilitaire | Facturation pour un message marketing et un message utilitaire |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Cette mise à jour s'applique aux modèles marketing, utilitaires et d'authentification. Les conversations de service sont gratuites depuis le 1er novembre 2024.

*Remarque : cette mise à jour était initialement prévue pour le 1er avril, puis le 1er mai, et désormais le **1er juillet**.*

### Mise à jour 2 : les modèles utilitaires envoyés pendant une fenêtre de service client de 24 heures seront gratuits. {#update-2-utility-templates-sent-during-a-24-hour-customer-service-window-will-be-free-of-charge}

#### Comment cela fonctionne-t-il ? {#how-does-this-work}

Une [fenêtre de service client de 24 heures](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows) est créée lorsqu'un utilisateur final envoie un message à une marque. Si votre marque répond avec un modèle utilitaire, celui-ci sera gratuit.

Les modèles utilitaires envoyés en dehors d'une fenêtre de service client de 24 heures (par exemple, les modèles utilitaires envoyés de manière proactive par une marque pour des rappels de compte ou des mises à jour de statut de la commande) seront toujours facturés.

Nous recommandons les bonnes pratiques suivantes pour prendre en compte ces changements et optimiser votre budget marketing WhatsApp :

- Limitez l'envoi de plusieurs modèles de messages du même type (sans réponse de l'utilisateur) dans la période de 24 heures. Vous ne serez pas facturé plus que ce que vous payiez auparavant avec le modèle « par conversation ». C'est également une bonne pratique pour offrir des expériences de qualité à vos clients et limiter la fatigue liée aux messages.
- Utilisez la [messagerie de réponse]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages) lorsque vous répondez aux messages des utilisateurs finaux. La messagerie de réponse est gratuite.

| Exemple de scénario | Tarification avant avril 2025 | Tarification après avril 2025 |
| --- | --- | --- |
| - La marque envoie un modèle marketing <br>- L'utilisateur répond <br>- La marque répond avec un message de réponse | Facturation pour une conversation marketing | Facturation pour un message marketing |
| - L'utilisateur envoie un message à la marque <br>- La marque répond avec un message de réponse | Gratuit <br> _Classé comme conversation de service_ | Gratuit <br> _Classé comme conversation de service_ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Nous recommandons les bonnes pratiques suivantes pour prendre en compte ces changements et optimiser votre budget marketing WhatsApp :

- Limitez l'envoi de plusieurs modèles de messages du même type (sans réponse de l'utilisateur) dans la période de 24 heures. Cela vous évite d'être facturé plus que ce que vous payiez auparavant avec le modèle « par conversation ». C'est également une bonne pratique pour offrir des expériences de qualité à vos clients et limiter la fatigue liée aux messages.
- Utilisez la [messagerie de réponse]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages) lorsque vous répondez aux messages des utilisateurs finaux. La messagerie de réponse est gratuite.

*Remarque : cette mise à jour était initialement prévue pour le 1er avril et désormais le **1er juillet**.*

## Changements de tarification WhatsApp d'août 2024 à novembre 2024 {#whatsapp-pricing-changes-from-august-2024-november-2024}

*Dernière mise à jour le 29 octobre 2024*

### Conversations utilitaires {#utility-conversations}

Le 1er août 2024, Meta a abaissé les tarifs des conversations utilitaires pour encourager les marques à faciliter davantage de parcours clients post-achat sur la plateforme. Nous avons répercuté ces réductions de coûts sur vos allocations de crédits de messages ou de crédits WhatsApp dans des proportions équivalentes. Cette mise à jour est entrée en vigueur le même jour que celle de Meta (1er août).

#### Que sont les conversations utilitaires ? {#what-are-utility-conversations}

Les conversations utilitaires vous permettent d'assurer le suivi d'actions ou de demandes spécifiques des clients. Les exemples incluent la confirmation d'abonnement, les mises à jour et confirmations de commandes, les mises à jour ou alertes de compte (par exemple, les rappels de paiement) ou les enquêtes de satisfaction.

#### Comment tirer parti de cette mise à jour ? {#how-can-you-benefit-from-this-update}

Nous vous encourageons à profiter de cette mise à jour en utilisant WhatsApp pour la communication transactionnelle. Vous pouvez également envisager de transférer certains de vos messages SMS transactionnels vers WhatsApp si cela convient à votre marque (en fonction de la portée de votre audience et de l'engagement sur chaque canal). Par exemple, cela peut être une bonne option pour les clients en Asie, en Amérique latine et en Europe, où WhatsApp est un canal très utilisé.

### Conversations marketing {#marketing-conversations}

Le 1er octobre 2024, Meta a réduit de 25 % les tarifs des conversations marketing au Royaume-Uni pour refléter la demande actuelle. Nous avons répercuté ces réductions de coûts sur vos allocations de crédits de messages ou de crédits WhatsApp dans des proportions équivalentes. Cette mise à jour est entrée en vigueur le même jour que celle de Meta (1er octobre).

#### Que sont les conversations marketing ? {#what-are-marketing-conversations}

Les conversations marketing vous permettent d'atteindre un large éventail d'objectifs, de la visibilité à la stimulation des ventes en passant par le reciblage des clients. Les exemples incluent les annonces de nouveaux produits, les promotions/offres ciblées et les Campaigns d'abandon de panier.

### Conversations de service {#service-conversations}

À compter du 1er novembre 2024, toutes les conversations de service sont gratuites. Les conversations de service ne consommeront plus d'allocations de crédits de messages ou de crédits WhatsApp. Ce changement est entré en vigueur le même jour que celui de Meta (1er novembre).

#### Que sont les conversations de service ? {#what-are-service-conversations}

Les conversations de service vous permettent de répondre aux demandes des clients. Cela inclut les conversations initiées par un utilisateur final auxquelles la marque répond avec un [message de réponse]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages) plutôt qu'un message modèle.

#### Comment tirer parti de cette mise à jour ?

Certaines conversations qui étaient auparavant facturées en tant que « service » sont désormais gratuites. Cela inclut :

- Les [Campaigns de réponse non reconnue]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages) où un utilisateur final envoie un message qui n'est pas reconnu et la marque répond avec un message générique en utilisant la [communication par réponse]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages). Par exemple, un utilisateur final envoie un message sans mot-clé et la marque répond avec « Nous ne reconnaissons pas votre message, veuillez contacter le support client. »
- Les conversations qui commencent lorsqu'un utilisateur final envoie à la marque un mot-clé promu et que la marque répond en utilisant un [message de réponse]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages). Les exemples courants sont l'abonnement à la communication WhatsApp ou la participation à une promotion spécifique.

<br>

Les informations détaillées sur la réduction des conversations utilitaires se trouvent dans la section suivante :

| Région de facturation                      | Pourcentage de réduction utilitaire |
|--------------------------------------------|-------------------------------------|
| Argentine                                  | 16,7 %                             |
| Brésil                                     | 77,1 %                             |
| Chili                                      | 65,9 %                             |
| Colombie                                   | 97,6 %                             |
| Égypte                                     | 92,4 %                             |
| France                                     | 60,9 %                             |
| Allemagne                                  | 35,5 %                             |
| Inde                                       | 66,7 %                             |
| Indonésie                                  | 0,0 %                              |
| Israël                                     | 71,8 %                             |
| Italie                                     | 28,6 %                             |
| Malaisie                                   | 30,0 %                             |
| Mexique                                    | 62,4 %                             |
| Pays-Bas                                   | 37,5 %                             |
| Nigeria                                    | 79,0 %                             |
| Amérique du Nord                           | 73,3 %                             |
| Autre                                      | 77,2 %                             |
| Pakistan                                   | 78,7 %                             |
| Pérou                                      | 52,3 %                             |
| Reste de l'Afrique                         | 61,9 %                             |
| Reste de l'Asie-Pacifique                  | 66,7 %                             |
| Reste de l'Europe centrale et orientale    | 43,0 %                             |
| Reste de l'Amérique latine                 | 77,1 %                             |
| Reste du Moyen-Orient                      | 20,7 %                             |
| Reste de l'Europe occidentale              | 28,6 %                             |
| Russie                                     | 16,1 %                             |
| Arabie saoudite                            | 54,4 %                             |
| Afrique du Sud                             | 62,0 %                             |
| Espagne                                    | 47,4 %                             |
| Turquie                                    | 43,0 %                             |
| Émirats arabes unis                        | 20,7 %                             |
| Royaume-Uni                                | 44,7 %                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour mieux comprendre comment tirer parti de ces mises à jour, contactez votre gestionnaire du succès des clients.