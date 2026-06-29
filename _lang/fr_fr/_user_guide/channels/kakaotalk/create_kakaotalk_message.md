---
nav_title: Créer un message KakaoTalk
article_title: Créer un message KakaoTalk
description: "Cet article de référence explique comment créer un message KakaoTalk."
page_order: 1
alias: /create_kakaotalk_message/
channel:
  - KakaoTalk
---

# Créer un message KakaoTalk {#create-a-kakaotalk-message}

> Utilisez le [canal de communication KakaoTalk]({{site.baseurl}}/kakaotalk/) pour atteindre directement les utilisateurs via la plateforme KakaoTalk. Créez une expérience utilisateur personnalisée en utilisant Liquid et d'autres contenus dynamiques pour construire un environnement qui favorise et enrichit une expérience utilisateur de qualité avec votre marque.<br><br>Pour configurer votre canal de communication KakaoTalk, consultez [Configurer KakaoTalk]({{site.baseurl}}/kakaotalk_setup/).

## Étape 1 : Choisir où créer votre message {#step-1-choose-where-to-build-your-message}

KakaoTalk est pris en charge dans les Campaigns et les Canvas. Les Campaigns sont idéales pour les envois de messages uniques, tandis que les Canvas vous permettent d'orchestrer des parcours utilisateur multi-étapes et multicanaux.

{% tabs local %}
{% tab Campaign %}

1. Accédez à **Messaging** > **Campaigns** et sélectionnez **Create Campaign**.
2. Sélectionnez **KakaoTalk** pour une campagne monocanal, ou **Multichannel Campaign** pour une campagne multicanal.

![Panneau avec les options de sélection du canal de communication.]({% image_buster /assets/img/kakaotalk/kakaotalk_campaign.png %}){: style="max-width:30%" }

3. Vous pouvez ajouter des variantes supplémentaires à votre campagne, ce qui vous permet de choisir différents types de messages et dispositions. Pour en savoir plus, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% endtab %}
{% tab Canvas %}

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/).
2. Ajoutez une étape Message dans le générateur Canvas et sélectionnez **KakaoTalk**.

![Sélections de canaux de communication dans Canvas.]({% image_buster /assets/img/kakaotalk/kakaotalk_canvas.png %})

{% endtab %}
{% endtabs %}

## Étape 2 : Rédiger votre message KakaoTalk {#step-2-compose-your-kakaotalk-message}

1. Sélectionnez le menu déroulant **KakaoTalk channel**, qui affiche la liste des canaux KakaoTalk que vous avez configurés via la page Partenaires technologiques, puis sélectionnez le canal KakaoTalk à utiliser pour envoyer le message.
2. Sélectionnez le type de message à envoyer :
- Texte
- Image
- Élément de liste
    - Étroit
    - Large

![Section des variantes KakaoTalk avec trois types de messages à sélectionner.]({% image_buster /assets/img/kakaotalk/kakaotalk_variants.png %})

{% tabs local %}
{% tab Texte %}

Un message texte KakaoTalk est la forme de communication la plus simple : un message texte standard.

### Spécifications {#specifications}

| Zone | Spécifications |
| --- | --- |
| Contenu | Contenu textuel, y compris les emojis et la personnalisation Liquid |
| Capacité de texte | Jusqu'à 1 000 caractères |
| Boutons | Jusqu'à 5 boutons facultatifs. Actuellement, ils ne peuvent être utilisés que pour ouvrir une URL au clic. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spécifications" }

![Un message texte KakaoTalk dans le compositeur.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

{% endtab %}
{% tab Image %}

Une image est un message qui combine un élément visuel avec du texte d'accompagnement. Braze gère automatiquement le téléchargement de l'image vers les serveurs KakaoTalk.

### Spécifications générales {#general-specifications}

| Zone | Spécifications |
| --- | --- |
| Contenu | Une image et du texte d'accompagnement |
| Formats de fichier acceptés | JPEG ou PNG |
| Largeur recommandée | 500 px |
| Taille du fichier | Jusqu'à 500 ko |
| Rapport hauteur/largeur | Doit être compris entre 2:1 (large) et 3:4 (haut) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spécifications générales" }

Les messages image étroits et larges ont chacun des limites de caractères et des considérations de boutons différentes.

{% subtabs %}
{% subtab Image étroite %}

#### Image étroite {#narrow-image}

Un message avec image étroite présente une image légèrement plus haute et étroite, avec des options de texte et de boutons plus étendues.

##### Spécifications

| Zone | Spécifications |
| --- | --- |
| Contenu | Une image et du texte d'accompagnement |
| Capacité de texte | Jusqu'à 500 caractères |
| Boutons | Jusqu'à 5 boutons facultatifs |
| Source de l'image | Les images peuvent être ajoutées via la bibliothèque multimédia Braze ou une URL directe |
| Personnalisation | Vous pouvez spécifier le comportement au clic de l'image |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spécifications" }

![Un message KakaoTalk avec image étroite.]({% image_buster /assets/img/kakaotalk/narrow_image.png %})

{% endsubtab %}
{% subtab Image large %}

#### Image large {#wide-image}

Un message avec image large présente une image large proéminente, adaptée à une communication visuelle à fort impact, avec un texte d'accompagnement minimal.

##### Spécifications

| Zone | Spécifications |
| --- | --- |
| Contenu | Une image et du texte d'accompagnement |
| Capacité de texte | Jusqu'à 76 caractères |
| Boutons | Jusqu'à 2 boutons facultatifs |
| Source de l'image | Les images peuvent être ajoutées via la bibliothèque multimédia Braze ou une URL directe |
| Personnalisation | Vous pouvez spécifier le comportement au clic de l'image |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spécifications" }

![Un message KakaoTalk avec image large.]({% image_buster /assets/img/kakaotalk/wide_image.png %})

{% endsubtab %}
{% endsubtabs %}

### Ajouter des images {#add-images}

Vous pouvez ajouter des images via la bibliothèque multimédia Braze ou en collant une URL hébergeant un fichier JPEG ou PNG. Vous pouvez également spécifier le comportement au clic de l'image pour rediriger les utilisateurs qui cliquent dessus vers une URL spécifique.

Braze gère automatiquement toutes les exigences de téléchargement d'images de KakaoTalk, ce qui signifie que vous n'avez **pas besoin** de télécharger les images vers les fournisseurs KakaoTalk avant d'envoyer des messages. Il vous suffit de télécharger les images et d'envoyer le message directement depuis Braze !

![Section avec les icônes sélectionnées pour ajouter une image étroite.]({% image_buster /assets/img/kakaotalk/add_image.png %})

{% endtab %}
{% tab Élément de liste %}


Un message de type liste d'éléments KakaoTalk est conçu pour présenter une liste d'éléments de contenu dans un format vertical clair.

Les messages de type liste d'éléments se composent d'un en-tête, d'une section de liste d'éléments et d'une zone de boutons facultative.

#### Spécifications

| Zone | Spécifications |
| --- | --- |
| Nombre d'éléments | Nécessite au moins 2 ou 3 éléments |
| Boutons | Jusqu'à 5 boutons facultatifs |
| En-tête | Jusqu'à 250 caractères |
| Titre de l'élément | Jusqu'à 25 caractères |
| URL du site web (par élément) | Jusqu'à 250 caractères |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spécifications" }

![Un message de type liste d'éléments KakaoTalk.]({% image_buster /assets/img/kakaotalk/item_list.png %})

{% endtab %}
{% endtabs %}


## Étape 3 : Configurer le suivi des clics {#step-3-set-up-click-tracking}

Lorsque le suivi des clics KakaoTalk est activé, Braze raccourcit automatiquement vos URL, ajoute des mécanismes de suivi et enregistre les clics en temps réel. Ces données vous permettent de créer des stratégies de segmentation et de reciblage plus ciblées, comme segmenter les utilisateurs en fonction de leur comportement de clic et déclencher des messages en réponse à des clics spécifiques.

Le suivi des clics est pris en charge pour les messages texte, image et liste d'éléments. Il prend en charge les liens dans les boutons et les actions au clic sur les images. Vous pouvez également personnaliser les URL en utilisant Liquid et des domaines personnalisés.

Pour activer le suivi des clics, cochez **Click Tracking** dans la section **Link options** du compositeur. Les URL seront raccourcies en utilisant le domaine Braze par défaut (`https://brz.ai`) ou le domaine personnalisé spécifié pour le groupe d'abonnement, et personnalisées pour l'utilisateur.

Pour tous les détails sur le suivi des clics, les domaines personnalisés, la personnalisation Liquid dans les URL, le reporting et le reciblage, consultez [Suivi des clics KakaoTalk]({{site.baseurl}}/kakaotalk_click_tracking/).

### Recibler les utilisateurs {#retargeting-users}

Vous pouvez recibler les utilisateurs qui ont cliqué sur une URL dans un message KakaoTalk en utilisant les filtres de segmentation et déclencheurs suivants :

- Déclencheurs basés sur les actions
    - Interact with Campaign
    - Interact with Step

- Filtres de segmentation
    - Clicked/Opened Campaign
    - Clicked/Opened Campaign or Canvas with Tag
    - Clicked/Opened Step

## Étape 4 : Prévisualiser et tester votre message KakaoTalk {#step-4-preview-and-test-your-kakaotalk-message}

La prévisualisation du message se met automatiquement à jour au fur et à mesure que vous rédigez votre message KakaoTalk. Lorsque vous êtes prêt à tester, accédez à l'onglet **Test** pour envoyer un message test à des groupes de test de contenu ou à des utilisateurs individuels, ou pour prévisualiser le message en tant qu'utilisateur existant ou personnalisé directement dans Braze.

Après avoir sélectionné vos utilisateurs test, sélectionnez **Send Test**. Une notification indiquera les résultats de votre envoi test. Pour CJ OliveNetworks, vous recevrez une réponse « C100 ». Si vous voyez une erreur différente, consultez la [documentation utilisateur CJ KakaoTalk](https://developers.kakao.com/docs/latest/en/index).

![Fenêtre de prévisualisation d'un message KakaoTalk.]({% image_buster /assets/img/kakaotalk/preview_message.png %})

{% alert note %}
Pour prévisualiser et envoyer un message test à un utilisateur existant, vous devez disposer des autorisations « View PII ». Vous pouvez prévisualiser et envoyer un message test à un utilisateur personnalisé sans ces autorisations.
{% endalert %}

Pour consulter les résultats d'un envoi ou résoudre des problèmes, accédez à **Paramètres** > **Journal d'activité des messages**. Pour en savoir plus, consultez [Journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/).

## Étape 5 : Construire le reste de votre campagne ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

Consultez les sections suivantes pour savoir comment utiliser au mieux nos outils pour créer des messages KakaoTalk.

### Choisir une planification d'envoi ou un déclencheur {#choose-delivery-schedule-or-trigger}

Les messages KakaoTalk peuvent être envoyés selon une planification horaire, une action ou un déclencheur API. Pour en savoir plus sur les options de planification et de déclenchement, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/) ou [Types de planification d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#entry-schedule-types) (pour votre Canvas).

Vous pouvez spécifier des contrôles d'envoi, comme permettre aux utilisateurs de redevenir éligibles pour recevoir la campagne, ou activer des règles de limite de fréquence. Pour la livraison par événement, vous pouvez également définir la durée de la campagne et les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/).

### Choisir les utilisateurs à cibler {#choose-users-to-target}

Ciblez les utilisateurs en sélectionnant des segments ou des filtres pour affiner votre audience. Pour l'instant, KakaoTalk ne peut envoyer des messages qu'aux amis du canal. Nous recommandons de définir un attribut personnalisé pour identifier les amis du canal, afin de segmenter correctement vos utilisateurs et d'éviter d'envoyer des messages KakaoTalk à des utilisateurs qui ne peuvent pas les recevoir.

### Choisir les événements de conversion {#choose-conversion-events}

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, les événements de conversion, après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion est comptabilisée si l'utilisateur effectue l'action spécifiée.

Les événements de conversion vous aident à mesurer le succès de votre campagne. Par exemple, si vous essayez d'inciter les utilisateurs à utiliser votre application, définissez l'événement de conversion sur **Starts Session**.

Vous pouvez également définir des événements de conversion personnalisés en fonction de votre cas d'utilisation spécifique. Soyez créatif et réfléchissez à la manière dont vous souhaitez mesurer le succès de votre campagne.

## Étape 6 : Vérifier et déployer {#step-6-review-and-deploy}

Une fois que vous avez terminé de construire votre campagne ou Canvas, vérifiez ses détails, testez-le et envoyez-le !