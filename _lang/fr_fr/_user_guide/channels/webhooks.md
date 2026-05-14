---
nav_title: Webhooks
article_title: Webhooks
page_order: 9
page_type: landing
alias: /about_webhooks/
description: "Connectez vos systèmes avec des webhooks dans Braze, déclenchés par des événements personnalisés pour envoyer des données et des messages programmatiques vers des endpoints externes."
channel:
  - webhooks
search_rank: 3
---

# Webhooks

> Un webhook est un message automatisé envoyé d'un système à un autre lorsque certains critères sont remplis. Dans Braze, ce critère est généralement le déclenchement d'un événement personnalisé. Les webhooks offrent un accès dynamique et flexible aux données et aux fonctionnalités programmatiques, et vous permettent de mettre en place des parcours clients qui rationalisent vos processus.

## Conditions préalables {#prerequisites}

La disponibilité des webhooks dépend de votre offre Braze. Contactez votre gestionnaire de compte ou votre gestionnaire de la satisfaction client pour commencer.

## Cas d'utilisation {#use-cases}

Les webhooks sont un excellent moyen de connecter vos systèmes entre eux — après tout, les webhooks sont le mode de communication des applications. Voici quelques scénarios généraux où les webhooks peuvent être particulièrement utiles :

- Envoyer des données vers et depuis Braze
- Envoyer des messages à vos clients via des canaux non directement pris en charge par Braze
- Publier vers les API de Braze

Voici quelques cas d'utilisation plus spécifiques :

- Créer un [workflow de scoring de prospects]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring/) en utilisant des webhooks et Canvas pour qualifier et acheminer les prospects.
- Si un utilisateur se désabonne des e-mails, vous pourriez utiliser un webhook pour mettre à jour votre base de données analytique ou votre CRM avec cette même information, garantissant ainsi une vue globale du comportement de cet utilisateur.
- Envoyer des [messages transactionnels]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) aux utilisateurs via Facebook Messenger ou Line.
- Envoyer du publipostage aux clients en réponse à leur activité in-app et web en utilisant des webhooks pour communiquer avec des services tiers comme [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/).
- Si un joueur atteint un certain niveau ou accumule un certain nombre de points, utilisez des webhooks et votre configuration API existante pour envoyer une amélioration de personnage ou des pièces directement sur son compte. Si vous envoyez le webhook dans le cadre d'une campagne de communication multicanale, vous pouvez envoyer une notification push ou un autre message pour informer le joueur de la récompense en même temps.
- Si vous êtes une compagnie aérienne, vous pouvez utiliser des webhooks et votre configuration API existante pour créditer le compte d'un client avec une réduction après qu'il a réservé un certain nombre de vols.
- Des recettes « If This Then That » ([IFTTT](https://ifttt.com/about)) infinies — par exemple, si un client se connecte à l'application via e-mail, cette adresse peut être automatiquement configurée dans Salesforce.

## Gestion des erreurs et limite de débit des webhooks {#webhook-error-handling-and-rate-limiting}

Braze ne retente la distribution des webhooks que pour certaines réponses HTTP (par exemple, `408`, `429` et `5XX`). La plupart des autres réponses, y compris `401 Unauthorized` et les autres erreurs `4XX`, ne font pas l'objet d'une nouvelle tentative. Les en-têtes de réponse tels que `Retry-After` et `X-Rate-Limit-*` peuvent influencer le délai d'attente **lorsqu'une réponse est déjà éligible à une nouvelle tentative** ; ils n'amènent pas Braze à retenter les erreurs qui ne font pas partie de l'ensemble des erreurs pouvant être retentées.

Pour le tableau complet des codes de réponse, les limites de nouvelles tentatives et le comportement en cas de délai d'attente, consultez [Codes de réponse et logique de nouvelle tentative]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/#response-codes-and-retry-logic).

Si la majorité des requêtes webhook vers un hôte spécifique échouent, Braze reporte temporairement toutes les tentatives d'envoi vers cet hôte. L'envoi reprend après une période de refroidissement définie, permettant à votre système de récupérer.

## Utiliser les webhooks avec les partenaires Braze {#utilizing-webhooks}

Il existe de nombreuses façons d'utiliser les webhooks, et avec nos partenaires technologiques (Alloys), vous pouvez les exploiter pour améliorer votre communication directement avec vos clients et utilisateurs.

Découvrez :
* [Messenger]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/instant_chat/messenger/)
* [Remerge]({{site.baseurl}}/partners/remerge/)
* [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/)
* Et bien d'autres de nos [partenaires technologiques]({{site.baseurl}}/partners/home/) !

## Étapes suivantes {#next-steps}

- [Créer un webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)
- [Créer un webhook Braze-à-Braze]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook/)