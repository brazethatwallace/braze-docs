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

> Utilisez le [canal de communication KakaoTalk]({{site.baseurl}}/kakaotalk) pour atteindre directement les utilisateurs via la plateforme KakaoTalk. Créez une expérience utilisateur personnalisée en utilisant Liquid et d'autres contenus dynamiques pour construire un environnement qui favorise et enrichit une expérience utilisateur de qualité avec votre marque.<br><br>Pour configurer votre canal de communication KakaoTalk, consultez [Configurer KakaoTalk]({{site.baseurl}}/kakaotalk_setup).

## Étape 1 : Choisir où créer votre message {#step-1-choose-where-to-build-your-message}

KakaoTalk est pris en charge à la fois dans les Campaigns et dans Canvas. Les Campaigns sont idéales pour les campagnes de communication ponctuelles, tandis que Canvas vous permet d'orchestrer des parcours utilisateurs multi-étapes et multicanaux.

{% tabs local %}
{% tab Campaign %}

1. Allez dans **Messaging** > **Campaigns** et sélectionnez **Create Campaign**.
2. Sélectionnez **KakaoTalk** pour une campagne monocanal, ou **Multichannel Campaign** pour une campagne multicanal.

![Panneau avec les options de sélection du canal de communication.]({% image_buster /assets/img/kakaotalk/kakaotalk_campaign.png %}){: style="max-width:30%" }

3. Vous pouvez ajouter des variantes supplémentaires à votre campagne, ce qui vous permet de choisir différents types de messages et mises en page. Pour en savoir plus, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% endtab %}
{% tab Canvas %}

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).
2. Ajoutez une étape Message dans le générateur Canvas et sélectionnez **KakaoTalk**.

![Sélection des canaux de communication dans Canvas.]({% image_buster /assets/img/kakaotalk/kakaotalk_canvas.png %})

{% endtab %}
{% endtabs %}

## Étape 2 : Composer votre message KakaoTalk {#step-2-compose-your-kakaotalk-message}

1. Sélectionnez le menu déroulant **Canal KakaoTalk**, qui affiche la liste des canaux KakaoTalk que vous avez configurés via la page Partenaires technologiques, puis sélectionnez le canal KakaoTalk à utiliser pour envoyer le message.
2. Sélectionnez le type de message à envoyer :
   - Texte
   - Image
       - Étroite
       - Large
   - Élément de liste
   - Carrousel

{% tabs local %}
{% tab Texte %}

Un message texte KakaoTalk est la forme de communication la plus simple : un message texte standard.

### Spécifications {#specifications}

| Zone | Spécifications |
| --- | --- |
| Contenu | Contenu textuel, y compris les emojis et la personnalisation Liquid |
| Capacité de texte | Jusqu'à 1 000 caractères |
| Boutons | Jusqu'à 5 boutons optionnels. Actuellement, ils ne peuvent être utilisés que pour ouvrir une URL au clic. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spécifications" }

![Un message texte KakaoTalk dans le composeur.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

{% endtab %}
{% tab Image %}

Une image est un message qui combine un élément visuel avec du texte d'accompagnement. Braze gère automatiquement le téléchargement de l'image vers les serveurs KakaoTalk.

### Spécifications générales {#general-specifications}

| Zone | Spécifications |
| --- | --- |
| Contenu | Une image et du texte d'accompagnement |
| Formats de fichier acceptés | JPEG ou PNG |
| Largeur recommandée | 500px |
| Taille du fichier | Jusqu'à 500 ko |
| Rapport hauteur/largeur | Doit être compris entre 2:1 (large) et 3:4 (haut) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spécifications générales" }

Les messages image étroits et larges ont chacun des limites de caractères et des options de boutons différentes.

{% subtabs %}
{% subtab Image étroite %}

#### Image étroite {#narrow-image}

Un message avec image étroite présente une image légèrement plus haute et étroite, avec des options de texte et de boutons plus étendues.

##### Spécifications

| Zone | Spécifications |
| --- | --- |
| Contenu | Une image et du texte d'accompagnement |
| Capacité de texte | Jusqu'à 500 caractères |
| Boutons | Jusqu'à 5 boutons optionnels |
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
| Boutons | Jusqu'à 2 boutons optionnels |
| Source de l'image | Les images peuvent être ajoutées via la bibliothèque multimédia Braze ou une URL directe |
| Personnalisation | Vous pouvez spécifier le comportement au clic de l'image |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spécifications" }

![Un message KakaoTalk avec image large.]({% image_buster /assets/img/kakaotalk/wide_image.png %})

{% endsubtab %}
{% endsubtabs %}

### Ajouter des images {#add-images}

Vous pouvez ajouter des images via la bibliothèque multimédia Braze ou en collant une URL hébergeant un fichier JPEG ou PNG. Vous pouvez également spécifier le comportement au clic de l'image pour rediriger les utilisateurs qui cliquent dessus vers une URL spécifique.

Braze gère automatiquement toutes les exigences de téléchargement d'images de KakaoTalk, ce qui signifie que vous n'avez pas besoin de télécharger les images vers les fournisseurs KakaoTalk avant d'envoyer des messages. Il vous suffit de télécharger les images et d'envoyer le message directement depuis Braze !

![Section avec des icônes sélectionnées pour ajouter une image étroite.]({% image_buster /assets/img/kakaotalk/add_image.png %})

{% endtab %}
{% tab Élément de liste %}


Un message de type liste d'éléments KakaoTalk est conçu pour présenter une liste d'éléments de contenu dans un format vertical clair.

Les messages de type liste d'éléments se composent d'un en-tête, d'une section de liste d'éléments et d'une zone de boutons optionnelle.

#### Spécifications

| Zone | Spécifications |
| --- | --- |
| Nombre d'éléments | Nécessite au moins 2 ou 3 éléments |
| En-tête | Jusqu'à 250 caractères |
| Titre de l'élément | Jusqu'à 25 caractères |
| URL du site web (par élément, appui sur la ligne) | Obligatoire. Jusqu'à 250 caractères. S'ouvre lorsqu'un utilisateur appuie sur l'image ou le titre de cet élément. |
| Boutons (au niveau du message) | Jusqu'à 5 boutons optionnels avec leurs propres URL ou actions |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spécifications" }

![Un message de type liste d'éléments KakaoTalk.]({% image_buster /assets/img/kakaotalk/item_list.png %})

{% endtab %}
{% tab Carrousel %}

Un message carrousel KakaoTalk comprend jusqu'à six cartes défilantes. Chaque carte possède une image, un en-tête, un message, une **URL du site web** optionnelle et au moins un bouton.

La carte et ses boutons utilisent tous deux un champ intitulé **URL du site web** dans le composeur, mais ils s'appliquent à des cibles d'appui différentes :

- **URL du site web de la carte :** (Optionnel) S'ouvre lorsqu'un utilisateur appuie sur l'image de la carte. Si vous laissez ce champ vide, l'image n'est pas cliquable.
- **URL du site web du bouton :** S'ouvre lorsqu'un utilisateur appuie sur ce bouton. Chaque bouton web nécessite sa propre URL et peut pointer vers une destination différente de celle de l'image de la carte.

Les URL des cartes et des boutons sont raccourcies et suivies indépendamment lorsque le suivi des clics est activé.

Braze télécharge automatiquement les images des cartes vers les serveurs KakaoTalk lorsque vous envoyez le message, de manière similaire aux messages image.

{% alert note %}
Le type de message **Carrousel** peut ne pas apparaître dans votre espace de travail tant qu'il n'a pas été activé pour votre compte.
{% endalert %}

### Spécifications

| Zone | Spécifications |
| --- | --- |
| Cartes | 2 à 6 cartes défilantes |
| En-tête (par carte) | Jusqu'à 20 caractères |
| Message (par carte) | Jusqu'à 180 caractères |
| Image (par carte) | Obligatoire |
| Formats de fichier acceptés | JPG ou PNG |
| Largeur minimale | 500px |
| Rapport hauteur/largeur | 2:1, 16:10, 3:2, 4:3, 1:1 ou 3:4 |
| URL du site web (par carte, appui sur l'image) | (Optionnel) Jusqu'à 250 caractères. S'ouvre lorsqu'un utilisateur appuie sur l'image de la carte. |
| Boutons (par carte) | Au moins 1, jusqu'à 2 |
| Texte du bouton (par carte) | Jusqu'à 8 caractères |
| Types de boutons | Ouvrir une URL web, lien d'application ou réponse textuelle |
| URL du site web du bouton (par bouton **Ouvrir une URL web**) | Obligatoire. Jusqu'à 500 caractères. S'ouvre lorsqu'un utilisateur appuie sur ce bouton. |
| Personnalisation | Liquid pris en charge dans les champs des cartes et les URL |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spécifications" }

![Un message carrousel KakaoTalk.]({% image_buster /assets/img/kakaotalk/carousel_message.png %})

{% endtab %}
{% endtabs %}

## Étape 3 : Configurer le suivi des clics {#step-3-set-up-click-tracking}

Lorsque le suivi des clics KakaoTalk est activé, Braze raccourcit automatiquement vos URL, ajoute des mécanismes de suivi et enregistre les clics en temps réel. Ces données vous permettent de créer des stratégies de segmentation et de reciblage plus ciblées, comme segmenter les utilisateurs en fonction de leur comportement de clic et déclencher des messages en réponse à des clics spécifiques.

Le suivi des clics est pris en charge pour les messages texte, image, élément de liste et carrousel. Il prend en charge les liens dans les boutons et les actions au clic sur les images. Vous pouvez également personnaliser les URL à l'aide de Liquid et de domaines personnalisés.

Pour activer le suivi des clics, cochez **Click Tracking** dans la section **Link options** du composeur. Les URL sont raccourcies à l'aide du domaine Braze par défaut (`https://brz.ai`) ou du domaine personnalisé spécifié pour le groupe d'abonnement, et personnalisées pour l'utilisateur.

Pour tous les détails sur le suivi des clics, les domaines personnalisés, la personnalisation Liquid dans les URL, le reporting et le reciblage, consultez [Suivi des clics KakaoTalk]({{site.baseurl}}/kakaotalk_click_tracking).

### Recibler les utilisateurs {#retargeting-users}

Vous pouvez recibler les utilisateurs qui ont cliqué sur une URL dans un message KakaoTalk en utilisant les filtres de segmentation et déclencheurs suivants :

- Déclencheurs par événement
    - Interact with Campaign
    - Interact with Step

- Filtres de segmentation
    - Clicked/Opened Campaign
    - Clicked/Opened Campaign or Canvas with Tag
    - Clicked/Opened Step

## Étape 4 : Prévisualiser et tester votre message KakaoTalk {#step-4-preview-and-test-your-kakaotalk-message}

L'aperçu du message se met automatiquement à jour au fur et à mesure que vous composez votre message KakaoTalk. Lorsque vous êtes prêt à tester, accédez à l'onglet **Test** pour envoyer un message test à des groupes de test de contenu ou à des utilisateurs individuels, ou pour prévisualiser le message en tant qu'utilisateur existant ou personnalisé directement dans Braze.

Après avoir sélectionné vos utilisateurs test, sélectionnez **Send Test**. Une notification indiquera les résultats de votre envoi test. Pour CJ OliveNetworks, vous recevrez une réponse « C100 ». Si vous voyez une erreur différente, consultez la [documentation utilisateur CJ KakaoTalk](https://developers.kakao.com/docs/latest/en/index).

![Fenêtre d'aperçu d'un message KakaoTalk.]({% image_buster /assets/img/kakaotalk/preview_message.png %})

{% alert note %}
Pour prévisualiser et envoyer un message test à un utilisateur existant, vous devez disposer des permissions « View PII ». Vous pouvez prévisualiser et envoyer un message test à un utilisateur personnalisé sans ces permissions.
{% endalert %}

Pour consulter les résultats d'un envoi ou résoudre des problèmes, accédez à **Paramètres** > **Journal d'activité des messages**. Pour plus d'informations, consultez [Journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log).

## Étape 5 : Créer le reste de votre campagne ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

Consultez les sections suivantes pour savoir comment utiliser au mieux nos outils pour créer des messages KakaoTalk.

### Choisir la planification de la livraison ou le déclencheur {#choose-delivery-schedule-or-trigger}

Les messages KakaoTalk peuvent être envoyés selon un horaire planifié, une action ou un déclencheur API. Pour en savoir plus sur les options de planification et de déclenchement, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign) ou [Types de planification d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#entry-schedule-types) (pour votre Canvas).

Vous pouvez spécifier des contrôles de livraison, comme autoriser les utilisateurs à redevenir éligibles pour recevoir la campagne, ou activer des règles de limite de fréquence. Pour la livraison par événement, vous pouvez également définir la durée de la campagne et les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

{% alert important %}
KakaoTalk applique des heures calmes d'environ 20h50 à 08h00, heure standard de Corée (KST). Les messages planifiés pendant cette fenêtre ne sont pas envoyés tant que les heures calmes ne sont pas terminées. Cette restriction est appliquée par les fournisseurs de livraison KakaoTalk (CJ OliveNetworks et Infobip) et s'applique à tous les types de messages KakaoTalk, indépendamment du paramètre optionnel d'heures calmes de Braze.
{% endalert %}

### Choisir les utilisateurs à cibler {#choose-users-to-target}

Ciblez les utilisateurs en sélectionnant des Segments ou des filtres pour affiner votre audience. Pour l'instant, KakaoTalk ne peut envoyer des messages qu'aux amis du canal. Nous vous recommandons de définir un attribut personnalisé pour identifier les amis du canal, afin de pouvoir segmenter correctement vos utilisateurs et éviter d'envoyer des messages KakaoTalk à des utilisateurs qui ne peuvent pas les recevoir.

### Choisir les événements de conversion {#choose-conversion-events}

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, les événements de conversion, après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion est comptabilisée si l'utilisateur effectue l'action spécifiée.

Les événements de conversion vous aident à mesurer le succès de votre campagne. Par exemple, si vous essayez d'inciter les utilisateurs à utiliser votre application, définissez l'événement de conversion sur **Starts Session**.

Vous pouvez également définir des événements de conversion personnalisés en fonction de votre cas d'usage spécifique. Faites preuve de créativité et réfléchissez à la manière dont vous souhaitez mesurer le succès de votre campagne.

## Étape 6 : Vérifier et déployer {#step-6-review-and-deploy}

Après avoir terminé la création de votre dernière campagne ou Canvas, vérifiez ses détails, testez-la et envoyez-la !