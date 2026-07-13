---
nav_title: Campaign Connector
article_title: Campaign Connector
page_order: 2
tool: Campaigns
page_type: tutorial
description: "Cet article pratique explique ce qu'est Campaign Connector et comment l'utiliser pour diffuser du contenu ciblé et pertinent au bon moment."

---
# Campaign Connector

> Campaign Connector vous permet de créer des campagnes qui se déclenchent lorsque les utilisateurs interagissent avec des campagnes actives. Vous pouvez ainsi diffuser du contenu ciblé et pertinent au bon moment.

## Fonctionnement {#how-it-works}

Cette fonctionnalité vous permet de cibler les utilisateurs qui effectuent les interactions suivantes avec des campagnes actives :

- Voir un message in-app
- Cliquer sur un message in-app
- Cliquer sur les boutons d'un message in-app
- Cliquer sur un e-mail
- Cliquer sur un alias dans un e-mail
- Ouvrir un e-mail
- Ouvrir directement une notification push
- Cliquer sur un bouton de notification push
- Cliquer sur une page Push Stories
- Effectuer un événement de conversion
- Recevoir un e-mail
- Recevoir un SMS
- Cliquer sur un lien SMS raccourci
- Recevoir une notification push
- Recevoir un webhook
- Être inscrit dans un groupe de contrôle
- Voir une carte de contenu
- Cliquer sur une carte de contenu
- Rejeter une carte de contenu

{% alert important %}
Les déclencheurs Campaign Connector ne peuvent pas être utilisés pour déclencher des campagnes de messages in-app. Les messages in-app ne peuvent être déclenchés que par des événements du SDK, tels que des événements personnalisés ou le démarrage d'une session. Pour en savoir plus, consultez [Créer un message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).
{% endalert %}

### Règles de distribution {#delivery-rules}

Notez que vous ne pouvez pas utiliser Campaign Connector pour envoyer un message à un utilisateur après qu'il a effectué une interaction avec une campagne. Par exemple, si vous menez une campagne marketing pendant neuf semaines et que vous configurez une campagne de suivi utilisant Campaign Connector au début de la quatrième semaine, la campagne de suivi ne distribuera des messages qu'aux utilisateurs ayant interagi avec la campagne marketing après la publication de la campagne de suivi (semaines 4 à 9). Par conséquent, pour vous assurer que vos campagnes de suivi atteignent chaque utilisateur ciblé, vous devez :

- Configurer votre campagne d'origine en tant que brouillon
- Configurer et publier votre campagne de suivi
- Publier la campagne d'origine

Ces règles de distribution sont particulièrement importantes si vous ciblez des utilisateurs inscrits dans un groupe de contrôle, qui reçoivent un e-mail ou une notification push. Étant donné que les utilisateurs seront inscrits dans le groupe de contrôle dès la publication de la campagne d'origine, vous devez publier la campagne de suivi avant de publier la campagne d'origine. De même, si vous publiez la campagne d'origine avant la campagne de suivi, de nombreux utilisateurs risquent de recevoir votre e-mail et/ou votre notification push avant la publication de la campagne de suivi.

## Utiliser Campaign Connector avec vos campagnes {#using-campaign-connector-with-your-campaigns}

### Étape 1 : Créer une nouvelle campagne {#step-1-create-a-new-campaign}

Rédigez les messages que vous souhaitez envoyer à vos utilisateurs. Vous pouvez sélectionner une campagne monocanal ou multicanal, selon votre cas d'utilisation.

### Étape 2 : Sélectionner l'interaction et la campagne cible {#step-2-select-interaction-and-target-campaign}

1. Sélectionnez [Livraison par événement]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) et ajoutez le déclencheur « Interagir avec une campagne » pour cibler les utilisateurs qui interagissent avec une campagne active.
2. Choisissez l'interaction de déclenchement.
3. Ensuite, sélectionnez la campagne active que vous souhaitez cibler.

![Sélection de la campagne active que vous souhaitez cibler.]({% image_buster /assets/img_archive/Campaign_Connector1.png %})

### Étape 3 : Définir un délai de planification et ajouter des exceptions (facultatif) {#step-3-set-schedule-delay-and-add-exceptions-optional}

Si vous choisissez de définir un délai de planification, vous pouvez ajouter une exception à l'action de déclenchement. Par exemple, vous pourriez vouloir renvoyer une campagne e-mail aux utilisateurs qui n'ont pas ouvert l'e-mail d'origine. Dans ce scénario, vous pouvez choisir « E-mail reçu » comme déclencheur et définir un délai de planification d'une semaine. Ensuite, vous pouvez ajouter « Ouvrir un e-mail » comme exception. Vous renverrez ainsi l'e-mail aux utilisateurs qui n'ont pas ouvert l'e-mail d'origine dans la semaine suivant sa réception.

![Exemple de configuration d'un délai de planification avec une exception à l'action de déclenchement pour renvoyer un e-mail aux utilisateurs qui n'ont pas ouvert l'e-mail d'origine dans la semaine suivant sa réception.]({% image_buster /assets/img_archive/Campaign_Connector3.png %})

Les événements d'exception ne se déclenchent que lorsqu'un utilisateur est en attente de recevoir le message associé. Si un utilisateur effectue l'action avant d'être en attente du message, l'événement d'exception ne se déclenchera pas.

### Étape 4 : Poursuivre la création de la campagne {#step-4-proceed-with-campaign-creation}

Continuez à créer votre campagne comme vous le feriez habituellement. Notez que si vous souhaitez vous assurer d'envoyer un message à chaque utilisateur susceptible d'interagir avec une campagne spécifique, il est préférable de cibler un segment contenant tous les utilisateurs de votre application.

## Cas d'utilisation {#use-cases}

Vous pouvez utiliser Campaign Connector pour cibler les utilisateurs qui interagissent ou n'interagissent pas avec des campagnes actives.

Par exemple, vous pourriez choisir de cibler les utilisateurs ayant cliqué sur une notification push promotionnelle annonçant la livraison gratuite, afin de leur envoyer une notification push promotionnelle offrant 15 % de réduction sur un achat.

Campaign Connector peut également cibler les utilisateurs qui reçoivent une notification push leur rappelant qu'ils ont abandonné leur panier. Par exemple, vous pourriez vouloir renvoyer la notification aux utilisateurs qui ne l'ont pas ouverte directement. Cependant, vous souhaiterez probablement exclure les utilisateurs ayant effectué un achat depuis l'envoi de la notification d'origine, même s'ils ne l'ont pas ouverte directement. Vous pouvez réaliser ce cas d'utilisation en ajoutant un déclencheur « Notification push reçue » pour la campagne « Panier abandonné », en définissant un délai de planification et en ajoutant « Effectue un achat » et « A ouvert directement la notification push » comme exceptions.