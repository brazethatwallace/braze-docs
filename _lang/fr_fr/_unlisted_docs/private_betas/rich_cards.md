---
nav_title: "Créer un message RCS"
article_title: "Créer un message RCS"
permalink: /create_rcs_message/
description: "Cet article explique comment créer un message RCS."
hidden: true
---

# Créer un message RCS {#creating-an-rcs-message}

> Les campagnes RCS sont idéales pour atteindre directement vos clients et converser avec eux de manière programmatique. Vous pouvez utiliser Liquid et d'autres contenus dynamiques pour créer une expérience personnalisée avec vos utilisateurs et favoriser une expérience utilisateur discrète et enrichissante avec votre marque.

## Créer un message RCS

### Étape 1 : Choisir où créer votre message {#step-1-choose-where-to-build-your-message}

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont plus adaptées aux envois de messages simples et ponctuels, tandis que les Canvas sont plus adaptés aux parcours utilisateur en plusieurs étapes.

{% tabs %}
{% tab Campaign %}
1. Accédez à **Envoi de messages** > **Campaigns** et sélectionnez **Créer une campagne**.
2. Sélectionnez **SMS/MMS/RCS** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multicanal**.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [équipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [étiquettes]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) selon vos besoins.
   * Les étiquettes facilitent la recherche de vos campagnes et la création de rapports. Par exemple, lorsque vous utilisez le [Générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer par étiquettes spécifiques.

{: start="5"}
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différentes plateformes, types de messages et dispositions pour chacune de vos variantes ajoutées. Pour en savoir plus, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- **Test de variantes SMS et RCS** : Braze vous permet d'inclure des variantes SMS et RCS au sein d'une même campagne, ce qui vous permet de comparer les performances de chacune. Vous pouvez ajouter des variantes SMS et RCS lors de la première étape de la composition du message.

{: start="6"}
6. Sélectionnez un [groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups/) compatible RCS. Lors de la sélection d'un groupe d'abonnement, Braze ajoutera automatiquement un filtre de segmentation, garantissant que seuls les utilisateurs abonnés recevront la campagne. Seuls les codes longs et codes courts appartenant à ce groupe d'abonnement seront utilisés pour envoyer des SMS aux utilisateurs ciblés.
- **Repli SMS** : Braze recommande fortement que chaque groupe d'abonnement contenant un expéditeur RCS inclue également au moins un code SMS pour le repli. Cela est important pour la livrabilité dans les cas où les messages RCS ne parviennent pas à être livrés. Les raisons possibles incluent l'incompatibilité de l'appareil de l'utilisateur et une couverture opérateur incomplète dans un pays ou une région donnée. En activant le repli SMS, votre message sera tout de même livré à votre utilisateur et vous ne manquerez jamais cette opportunité de communiquer avec lui.

{: start="7"}
7. Choisissez entre SMS et RCS. Avant de composer des messages RCS, choisissez le canal d'envoi. Nous recommandons généralement d'utiliser RCS dans la mesure du possible, car les avantages en termes d'engagement utilisateur sont significatifs par rapport au SMS ; cependant, nous offrons toujours la possibilité d'envoyer par SMS afin que vous disposiez d'une flexibilité et d'un contrôle maximaux.

![Options pour sélectionner un type de message RCS ou SMS/MMS.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier depuis la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Créez votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape de message **SMS/MMS/RCS** dans le générateur de Canvas.
3. Donnez à votre étape un nom clair et significatif.
4. Sélectionnez un [groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups/) compatible RCS. Lors de la sélection d'un groupe d'abonnement, Braze ajoutera automatiquement un filtre de segmentation, garantissant que seuls les utilisateurs abonnés recevront la campagne. Seuls les codes longs et codes courts appartenant à ce groupe d'abonnement seront utilisés pour cibler les utilisateurs.
- **Repli SMS** : Braze recommande fortement que chaque groupe d'abonnement contenant un expéditeur RCS inclue également au moins un code SMS pour le repli. Cela est important pour la livrabilité dans les cas où les messages RCS ne parviennent pas à être livrés. Les raisons possibles incluent l'incompatibilité de l'appareil de l'utilisateur et une couverture opérateur incomplète dans un pays ou une région donnée. En activant le repli SMS, votre message sera tout de même livré à votre utilisateur et vous ne manquerez jamais cette opportunité de communiquer avec lui.

{: start="5"}
5. Choisissez entre SMS et RCS. Avant de composer des messages RCS, choisissez le canal d'envoi. Nous recommandons généralement d'utiliser RCS dans la mesure du possible, car les avantages en termes d'engagement utilisateur sont significatifs par rapport au SMS ; cependant, nous offrons toujours la possibilité d'envoyer par SMS afin que vous disposiez d'une flexibilité et d'un contrôle maximaux.

![Options pour sélectionner un type de message RCS ou SMS/MMS.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Étape 2 : Sélectionner votre type de message RCS {#step-2-select-your-rcs-message-type}

Lors de la création d'une campagne ou d'un Canvas, choisissez parmi trois types de messages RCS (Texte, Média, Carte enrichie) pour configurer les messages les mieux adaptés à vos objectifs.

![Options pour sélectionner un type de message Texte, Média ou Carte.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs local %}
{% tab Texte %}
Comme son nom l'indique, les messages texte RCS se concentrent sur le texte comme support. Si vous saisissez jusqu'à 160 caractères, le message RCS est facturé comme un message texte uniquement (ou « basique »). Si vous dépassez 160 caractères ou utilisez un élément enrichi, le message est facturé comme un message RCS enrichi (ou « unique ») et la limite de caractères passe à 3 072 caractères.

#### Fonctionnalités {#features}

- Les types de messages texte incluent toutes les fonctionnalités SMS. Seul le suivi avancé est possible pour le suivi des clics sur les URL, ce qui vous offre une granularité de reporting au niveau de l'utilisateur.
- De plus, vous avez désormais la possibilité d'inclure des boutons **Réponses suggérées** et **Actions suggérées** qui favorisent des actions utilisateur à fort engagement, comme visiter une page d'accueil ou passer une commande.
    - Les **Réponses suggérées** sont des boutons contenant des réponses suggérées sur lesquelles les utilisateurs peuvent cliquer et qui sont pré-remplies dans leur champ de saisie, supprimant la friction de devoir réfléchir à une réponse en leur fournissant un ensemble limité de choix.
    - Les **Actions suggérées** sont des boutons qui déclenchent une action sur l'appareil de l'utilisateur. Elles consistent généralement en un ou deux mots descriptifs et une icône visuelle pour aider l'utilisateur à comprendre ce que fait le bouton. Braze prend actuellement en charge les actions suggérées OpenURL. Cela fonctionne de manière similaire à une URL : les utilisateurs qui sélectionnent le bouton sont redirigés vers une page web ou un autre emplacement identifié par URL.

![Un GIF de trois actions suggérées pour un message RCS promouvant des styles de mode tendance : « Fairytale royalty », « Edgy academia » et « Show me your other styles ».]({% image_buster /assets/unlisted_docs/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Considérations {#considerations}

- Pour les limites de caractères, vous pouvez écrire jusqu'à 160 caractères pour un message RCS texte uniquement (basique) ou jusqu'à 3 072 pour un message RCS enrichi (unique).
- Pour les limites de boutons, vous pouvez ajouter jusqu'à cinq boutons par message. Ces boutons peuvent être des actions suggérées ou des réponses suggérées.
- Les blocs de texte longs et un trop grand nombre de boutons peuvent frustrer les utilisateurs ; dans la mesure du possible, nous recommandons de privilégier la simplicité.
- Dans certains cas, il peut être plus rentable d'envoyer des messages texte plus longs via RCS qu'avec SMS. En effet, les messages SMS plus longs sont divisés en plusieurs segments, chacun étant facturable, tandis que les messages RCS sont facturés par message. Contactez votre gestionnaire de compte Braze pour plus de détails et de conseils.
{% endtab %}

{% tab Média %}
Les messages média RCS vous permettent d'utiliser des formats média engageants qui ne sont pas possibles avec le SMS. Ceux-ci incluent des fichiers image, vidéo et document. Ces options média existent pour vous aider à engager votre audience encore plus profondément et permettre des cas d'utilisation entièrement nouveaux. Pour le moment, seul le téléchargement d'images est pris en charge via la [Bibliothèque multimédia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/).

#### Fonctionnalités

- Les types de messages média prennent en charge tout ce qui est disponible dans les types de messages texte, y compris le texte, les réponses suggérées et les actions suggérées.
- Prise en charge des fichiers image, y compris les formats JPEG et PNG. Les fichiers image sont disponibles via le téléchargement depuis la Bibliothèque multimédia.
- Prise en charge des fichiers vidéo, y compris les formats MP4, MPEG et MV4. Les fichiers vidéo peuvent être ajoutés par URL directement dans le compositeur de messages.
- Prise en charge des fichiers document au format PDF. Les fichiers document peuvent être ajoutés via l'URL directement dans le compositeur de messages.

![Compositeur RCS avec une option pour télécharger un fichier média.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_media_type.png %})

#### Spécifications des fichiers {#file-specifications}

| Type de fichier | Spécifications |
| --- | --- |
| Tous | - La taille du fichier est limitée à 100 Mo <br><br>- L'URL du fichier peut contenir jusqu'à 2 048 caractères |
| Fichiers image | Les formats de fichiers pris en charge incluent JPG, JPEG et GIF |
| Fichiers vidéo | Les formats de fichiers pris en charge incluent H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Fichiers document | Formats de fichiers pris en charge : PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Considérations

L'expérience utilisateur lors de la réception de messages RCS peut varier légèrement en fonction de plusieurs facteurs, notamment la couverture opérateur dans le pays de destination, le matériel de l'appareil mobile et le système d'exploitation de l'appareil mobile.

De manière générale, le RCS s'intègre plus naturellement avec les appareils Android (cette méthode a été largement mise en œuvre par Google, et la messagerie RCS pair-à-pair est largement adoptée au sein de la communauté Android). Différents appareils peuvent offrir l'expérience à des vitesses et qualités différentes.
{% endtab %}

{% tab Carte enrichie %}

{% alert important %}
Les cartes enrichies sont en accès anticipé. Contactez votre gestionnaire de la satisfaction client Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

Une carte enrichie combine média, texte et boutons en un seul message, créant une expérience plus intuitive et engageante pour vos clients. Vous pouvez créer deux sous-types de cartes enrichies : Texte et Média.

{% subtabs %}
{% subtab Texte %}
Une carte enrichie Texte est un message concis axé sur le texte. Elle doit inclure les éléments suivants :

- **Titre :** Jusqu'à 200 caractères. Peut être personnalisé avec Liquid.
- **Description :** Jusqu'à 2 000 caractères. Peut être personnalisée avec Liquid.
- **Boutons :** Au moins un bouton est requis. Vous pouvez ajouter jusqu'à quatre boutons avec des actions **Réponse suggérée** ou **Ouvrir une URL web**.

{% endsubtab %}
{% subtab Média %}

Une carte enrichie Média est un message visuel contenant une image ou une vidéo. Elle doit inclure les éléments suivants :

- **Média :** Une image, un GIF ou une vidéo.
    - Les miniatures vidéo personnalisées ne sont pas prises en charge dans l'accès anticipé. L'accès anticipé ne prend en charge qu'une disposition verticale avec une hauteur de média élevée pour les fichiers image et vidéo.
- **Boutons :** Au moins un bouton est requis. Vous pouvez ajouter jusqu'à quatre boutons avec des actions **Réponse suggérée** ou **Ouvrir une URL web**.

{% endsubtab %}
{% endsubtabs %}

### Fonctionnalités
- **Boutons de carte** et **Suggestions :** Vous pouvez ajouter jusqu'à quatre boutons et cinq suggestions (jusqu'à 25 caractères chacune) en bas de la carte enrichie (boutons) ou en bas de l'écran de message (suggestions). Un utilisateur peut sélectionner ces options pour envoyer une réponse spécifique ou effectuer une action spécifique.
- **Personnalisation :** Vous pouvez utiliser Liquid pour personnaliser tous les éléments de la carte enrichie, y compris le titre, la description, le média et les boutons.
- **Facturation :** Les cartes enrichies sont facturées comme un seul message RCS enrichi (ou « unique »).
- **Recommandations pour les URL :** Les URL saisies en texte brut dans le titre ou la description ne seront pas cliquables. Vous devez utiliser un bouton **OpenURL** pour diriger les utilisateurs vers un site web.

![Panneau avec des options pour sélectionner une carte enrichie Média ou Texte.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_media_text.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Étape 3 : Composer votre message RCS {#step-3-compose-your-rcs-message}

Rédigez votre message en utilisant les langues et la personnalisation ([Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) et emojis) selon vos besoins. Veillez à respecter nos limites de texte pour réduire vos risques de frais de dépassement.

{% alert important %}
Avant de continuer, lisez nos [recommandations sur les limites de messages RCS](#step-2-select-your-rcs-message-type). Les messages RCS sont [facturés par message]({{site.baseurl}}/sms_rcs_billing_calculators/), il est donc judicieux de comprendre les nuances de ce qui peut être inclus dans chaque type de message RCS.
{% endalert %}

### Étape 4 : Prévisualiser et tester votre message {#step-4-preview-and-test-your-message}

Braze recommande toujours de prévisualiser et de tester votre message avant de l'envoyer. Accédez à l'onglet **Test** pour envoyer un RCS de test à des groupes de test de contenu ou à des utilisateurs individuels, ou prévisualisez le message en tant qu'utilisateur directement dans Braze.

### Étape 5 : Construire le reste de votre campagne ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

Ensuite, construisez le reste de votre campagne ou Canvas. Consultez les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des messages RCS.

#### Étape 5.1 : Choisir la planification ou le déclencheur de livraison {#step-51-choose-delivery-schedule-or-trigger}

Les messages RCS peuvent être livrés selon un horaire planifié, une action ou un déclencheur API. Pour en savoir plus, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Pour la livraison par événement, vous pouvez également définir la durée de la campagne et les heures calmes.

Spécifiez vos contrôles de livraison, comme permettre aux utilisateurs de redevenir éligibles pour recevoir la campagne ou activer les règles de limite de fréquence.

#### Étape 5.2 : Choisir les utilisateurs à cibler {#step-52-choose-users-to-target}

Ciblez les utilisateurs en choisissant des segments ou des filtres pour affiner votre audience. Vous devriez avoir déjà sélectionné le groupe d'abonnement, qui restreint les utilisateurs selon le niveau ou la catégorie de communication qu'ils souhaitent avoir avec vous.

{% multi_lang_include target_audiences.md %}

Ensuite, vous sélectionnerez l'audience plus large parmi vos segments et affinerez ce segment davantage avec des [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) optionnels. Vous obtiendrez automatiquement un aperçu de ce à quoi ressemble approximativement la population de ce segment en ce moment. Gardez à l'esprit que l'appartenance exacte au segment est toujours calculée juste avant l'envoi du message.

{% alert tip %}
Vous souhaitez utiliser le reciblage RCS pour cibler les utilisateurs en fonction de leurs interactions SMS et RCS ? Consultez [Reciblage]({{site.baseurl}}/sms_mms_rcs_user_retargeting/).
{% endalert %}

#### Étape 5.3 : Choisir les événements de conversion {#step-53-choose-conversion-events}

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, ou événements de conversion, après avoir reçu une campagne. Vous pouvez autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

Les événements de conversion vous aident à mesurer le succès de votre campagne. Par exemple :
- Si vous utilisez le géociblage pour déclencher un message RCS dont l'objectif final est que l'utilisateur effectue un achat, définissez l'événement de conversion sur **Achat**.
- Si vous essayez d'amener l'utilisateur vers votre application, définissez l'événement de conversion sur **Démarre une session**.

Vous pouvez également définir des événements de conversion personnalisés en fonction de votre cas d'utilisation spécifique. Soyez créatif dans la façon dont vous souhaitez véritablement mesurer le succès de votre campagne.

### Étape 6 : Vérifier et déployer {#step-6-review-and-deploy}

Après avoir terminé la création de votre campagne ou Canvas, vérifiez ses détails, testez-la, puis envoyez-la !

Ensuite, consultez [Reporting pour SMS, MMS et RCS]({{site.baseurl}}/sms_mms_rcs_reporting/) pour découvrir comment accéder aux résultats de vos campagnes RCS.

## Analyse et reporting {#analytics-and-reporting}

Les analyses de votre campagne ou Canvas incluent :

- Les statistiques de _Total des clics_ qui incluent toutes les interactions avec la carte enrichie, comme les clics sur les boutons et les réponses ou actions suggérées.
- Un tableau de répartition qui fournit une vue plus détaillée de ces interactions.

{% alert note %}
L'accès anticipé n'inclut pas le suivi des clics au niveau de l'utilisateur. Le _Total des clics_ s'incrémentera à chaque clic sur un bouton. Par exemple, si un utilisateur clique trois fois sur le même bouton, le nombre de clics augmentera de trois.
{% endalert %}

## Conseils {#tips}

### Utiliser Liquid pour la personnalisation des messages {#using-liquid-for-message-personalization}

Si vous prévoyez d'utiliser Liquid, assurez-vous d'inclure une valeur par défaut pour la personnalisation choisie afin que, si le profil utilisateur du destinataire est incomplet, il ne reçoive pas une marque substitutive vide `Hi, !` au lieu de son nom ou d'une phrase cohérente.

### Générer du texte avec l'IA {#generating-ai-copy}

Besoin d'aide pour créer un texte engageant ? Essayez d'utiliser l'[assistant de rédaction IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities/#generate-copy). Saisissez un nom ou une description de produit, et l'IA générera un texte marketing semblable à celui d'un humain pour l'utiliser dans vos messages.

![Compositeur de messages avec une icône pour ouvrir l'assistant de rédaction IA.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

## Questions fréquemment posées {#frequently-asked-questions}

### Puis-je envoyer des messages vocaux pré-enregistrés avec RCS ? {#can-i-send-pre-recorded-voicemails-with-rcs}

Oui, vous pouvez utiliser les messages média pour prendre en charge les fichiers audio.