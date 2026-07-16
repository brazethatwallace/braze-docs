---
nav_title: Créer un message
article_title: Créer un message SMS, MMS ou RCS
page_order: 1
description: "Cet article explique comment créer et envoyer un message SMS, MMS ou RCS dans Braze."
page_type: reference
alias: /create_sms_mms_rcs_message/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
search_rank: 1
---

# Créer un message SMS, MMS ou RCS {#create-an-sms-mms-or-rcs-message}

> Les campagnes SMS, MMS et RCS sont idéales pour atteindre directement vos clients et converser avec eux de manière programmatique. Vous pouvez utiliser Liquid et d'autres contenus dynamiques pour créer une expérience personnalisée avec vos utilisateurs et favoriser un environnement qui enrichit une expérience utilisateur discrète avec votre marque.

## Étape 1 : Choisir où créer votre message {#step-1-choose-where-to-build-your-message}

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont plus adaptées aux communications ciblées et ponctuelles, tandis que les Canvas sont plus adaptés aux parcours utilisateur en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

1. Accédez à **Messaging** > **Campaigns** et sélectionnez **Create Campaign**.
2. Sélectionnez **SMS/MMS/RCS** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multichannel**.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) et des [étiquettes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) si nécessaire.
   * Les étiquettes facilitent la recherche de vos campagnes et la création de rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder), vous pouvez filtrer par étiquettes spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différentes plateformes, types de messages et dispositions pour chacune de vos variantes. Pour en savoir plus sur ce sujet, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).
   * Braze vous permet d'inclure des variantes SMS et RCS au sein d'une même campagne, afin de comparer les performances de chacune.

{% alert tip %}
Si tous les messages de votre campagne sont similaires ou ont le même contenu, rédigez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier depuis la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) à l'aide du compositeur Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape de message **SMS/MMS/RCS** dans le générateur Canvas.
3. Donnez à votre étape un nom clair et significatif.
4. Choisissez une [planification d'étape]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) et spécifiez un délai si nécessaire.
5. Filtrez votre audience pour cette étape si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d'audience seront vérifiées après le délai, au moment de l'envoi des messages.
6. Choisissez votre [comportement d'avancement]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases).
7. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Sélectionner un groupe d'abonnement {#step-2-select-a-subscription-group}

Sélectionnez un [groupe d'abonnement]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) pour vous assurer d'envoyer votre message aux bons utilisateurs. Lors de la sélection d'un groupe d'abonnement, Braze ajoutera automatiquement un filtre de segmentation, garantissant que seuls les utilisateurs abonnés recevront la campagne.

Le groupe d'abonnement que vous sélectionnez détermine les types de messages disponibles dans le compositeur :

| Type de groupe d'abonnement | Types de messages disponibles |
| --- | --- |
| SMS uniquement | SMS |
| SMS avec numéros compatibles MMS | SMS et MMS |
| Compatible RCS (avec expéditeur vérifié RCS) | SMS, MMS (si activé) et RCS |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Sélectionner un groupe d'abonnement" }

{% alert tip %}
Braze recommande vivement que chaque groupe d'abonnement contenant un expéditeur RCS inclue également au moins un code SMS de secours. Cela garantit que si un message RCS ne parvient pas à être livré (par exemple, en raison d'une incompatibilité d'appareil ou d'une couverture opérateur incomplète), le message atteindra tout de même votre utilisateur via SMS.
{% endalert %}

Après avoir sélectionné votre groupe d'abonnement, choisissez le type de message que vous souhaitez rédiger. Si votre groupe d'abonnement prend en charge plusieurs types, vous verrez des options pour choisir entre eux.

![Options pour sélectionner un type de message RCS ou SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

## Étape 3 : Rédiger votre message {#step-3-compose-your-message}

L'expérience de rédaction change en fonction du type de message que vous avez sélectionné. Sélectionnez l'onglet correspondant à votre type de message.

{% tabs local %}
{% tab SMS %}

Rédigez votre message en utilisant les langues et la personnalisation (Liquid, contenu connecté et emojis) selon vos besoins. Veillez à respecter nos limites de texte pour réduire vos risques de frais supplémentaires.

{% alert important %}
Avant de continuer, lisez les directives sur les [segments de messages SMS et les limites de texte]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator). Les segments de messages SMS sont les lots de caractères que les opérateurs téléphoniques utilisent pour mesurer les messages texte. Les messages sont facturés par segment de message, il est donc judicieux de comprendre les nuances de la façon dont les messages seront découpés.
{% endalert %}

![Compositeur SMS dans Braze avec le message « Bonjour first_name, nous apprécions votre soutien ! Pourquoi ne pas passer dans l'un de nos magasins et montrer ce SMS pour une remise exclusive ? Répondez STOP pour ne plus recevoir de messages de notre part. »]({% image_buster /assets/img/sms_campaign_compose.png %})

### Ajouter une carte de contact {#adding-a-contact-card}

Vous pouvez ajouter une carte de contact à votre message SMS afin que les clients puissent ajouter les informations de votre entreprise et vos coordonnées à leurs contacts. Vous pouvez attribuer des propriétés telles que le nom de l'entreprise, le numéro de téléphone, l'adresse, l'e-mail et une petite photo. Consultez [Cartes de contact]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card) pour plus de détails.

{% endtab %}
{% tab MMS %}

Pour envoyer un message MMS, votre groupe d'abonnement doit contenir au moins un numéro de téléphone compatible MMS. Cela est indiqué par une étiquette **MMS** à côté du groupe d'abonnement dans le compositeur.

Saisissez le corps de votre message, puis téléchargez une image PNG, JPEG ou GIF depuis la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) ou spécifiez une URL d'image. Une seule image est prise en charge par message.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

![L'onglet de rédaction pour écrire un message MMS.]({% image_buster /assets/img/sms/mms_composer.png %}){: style="max-width:80%;"}

### Spécifications des images {#image-specifications}

| Propriété | Recommandation |
| --- | --- |
| Taille | Jusqu'à 600&nbsp;Ko |
| Types de fichiers | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spécifications des images" }

### Cartes de contact {#contact-cards}

Vous pouvez également inclure une [carte de contact]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card) (vCard) à la place d'une image.

### Comportement des opérateurs {#carrier-behavior}

Les messages MMS sont facturés à un tarif différent de celui des SMS texte uniquement. Tous les opérateurs ne peuvent pas accepter les MMS. Dans ces cas, le MMS est automatiquement converti en un lien image que l'utilisateur peut sélectionner.

{% alert note %}
Évitez d'envoyer des MMS à des numéros Google Voice. Google Voice offre une prise en charge limitée des MMS, ce qui entraîne une livraison de messages peu fiable.
{% endalert %}

### MMS entrants et personnalisation {#inbound-mms-and-personalization}

Lorsqu'un client envoie un message entrant contenant un média, Braze expose le média dans les [événements entrants SMS de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) et dans Liquid sous la forme {% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %} (par exemple dans les messages de reciblage ou de suivi). Pour en savoir plus sur l'utilisation des propriétés SMS entrantes dans Canvas, consultez [Étape de message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

{% endtab %}
{% tab RCS %}

Regardez cette présentation rapide pour voir comment créer un message texte ou média RCS.

{% multi_lang_include video.html id="3y0iiqqygw" source="wistia" %}

Choisissez entre un type de message **Texte** ou **Média**.

![Options pour sélectionner un type de message Texte ou Média.]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% subtabs %}
{% subtab Texte %}

Les messages texte RCS se concentrent sur le texte comme support. Si votre message fait jusqu'à 160 caractères sans éléments enrichis, il est facturé comme un message RCS basique. Si vous dépassez 160 caractères ou utilisez un élément enrichi, il est facturé comme un message RCS enrichi (unique) avec une limite de 3 072 caractères.

**Fonctionnalités :**

- Toutes les fonctionnalités SMS sont incluses, avec un suivi avancé disponible pour le suivi des clics sur les URL.
- **Réponses suggérées** : boutons contenant des réponses suggérées que les utilisateurs peuvent sélectionner pour les pré-remplir dans leur champ de saisie.
- **Actions suggérées** : boutons qui déclenchent une action sur l'appareil de l'utilisateur. Braze prend actuellement en charge les actions suggérées OpenURL, qui redirigent les utilisateurs vers une page web ou un autre emplacement identifié par URL.

![Trois actions suggérées pour un message RCS faisant la promotion de styles de mode tendance.]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

**Considérations :**

- Android et iOS peuvent tronquer différemment : Android affiche le texte complet du message enrichi, tandis qu'iOS tronque après la troisième ligne.
- Vous pouvez ajouter jusqu'à cinq boutons par message. Il peut s'agir d'actions suggérées ou de réponses suggérées.
- Les blocs de texte longs et les nombreux boutons peuvent submerger les destinataires ; privilégiez la simplicité lorsque c'est possible.
- Dans certains cas, il peut être plus rentable d'envoyer des messages texte longs via RCS plutôt que par SMS, car les messages SMS longs sont découpés en plusieurs segments facturables, tandis que les messages RCS sont facturés par message.

{% endsubtab %}
{% subtab Média %}

Les messages média RCS vous permettent d'utiliser des formats média attrayants qui ne sont pas possibles avec les SMS, notamment les fichiers image, vidéo et document.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

**Fonctionnalités :**

- Prend en charge tout ce qui est disponible dans les types de messages texte, y compris le texte, les réponses suggérées et les actions suggérées.
- Fichiers image (JPEG, PNG) téléchargés depuis la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library).
- Fichiers vidéo (MP4, MPEG, MV4) ajoutés par URL dans le compositeur de messages.
- Fichiers document (PDF) ajoutés par URL dans le compositeur de messages.

![Compositeur RCS avec une option pour télécharger un fichier média.]({% image_buster /assets/img/rcs/rcs_media_type.png %})

**Spécifications des fichiers :**

| Type de fichier | Spécifications |
| --- | --- |
| Tous | Taille de fichier limitée à 100 Mo. L'URL du fichier peut contenir jusqu'à 2 048 caractères. |
| Image | Formats pris en charge : JPG, JPEG, GIF |
| Vidéo | Formats pris en charge : H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Document | Format pris en charge : PDF |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spécifications des fichiers" }

**Considérations :**

L'expérience utilisateur lors de la réception de messages RCS peut varier en fonction de la couverture de l'opérateur, du matériel de l'appareil mobile et du système d'exploitation. Le RCS s'intègre plus naturellement aux appareils Android, et différents appareils peuvent restituer l'expérience à des vitesses et qualités différentes.

{% endsubtab %}
{% endsubtabs %}

Rédigez votre message en utilisant les langues et la personnalisation ([Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) et emojis) selon vos besoins. Veillez à respecter les limites de texte pour réduire vos risques de frais supplémentaires.

{% alert important %}
Avant de continuer, lisez les [directives sur les types de messages RCS](#step-3-compose-your-message) plus haut dans cette section. Les messages RCS sont [facturés par message]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator), il est donc judicieux de comprendre ce qui peut être inclus dans chaque type.
{% endalert %}

{% endtab %}
{% endtabs %}

### Conseils {#tips}

#### Utiliser Liquid {#using-liquid}

{% raw %}
Si vous prévoyez d'utiliser Liquid, veillez à inclure une valeur par défaut pour la personnalisation choisie afin que, dans le cas où le profil de votre utilisateur serait incomplet, il ne reçoive pas une marque substitutive vide `Hi, !` au lieu de son nom ou d'une phrase cohérente.
{% endraw %}

#### Générer du texte avec l'IA {#generating-ai-copy}

Essayez d'utiliser l'[assistant de rédaction IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Saisissez un nom ou une description de produit, et l'IA générera un texte marketing de qualité humaine à utiliser dans vos messages.

![Bouton Lancer le rédacteur IA, situé dans le champ Message du compositeur SMS.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### Créer des messages de droite à gauche {#creating-right-to-left-messages}

L'apparence finale des messages de droite à gauche dépend en grande partie de la façon dont les fournisseurs de services les restituent. Pour les bonnes pratiques de rédaction de messages de droite à gauche qui s'affichent aussi fidèlement que possible, consultez [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Créer des flux de messages conversationnels (RCS) {#create-conversational-message-workflows-rcs}

Les flux de messages conversationnels vous permettent de répondre dynamiquement aux utilisateurs, créant une expérience de messagerie interactive. Pour créer un flux, créez un Canvas puis combinez les réponses suggérées avec les [parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) pour diriger votre flux en fonction de la réponse sélectionnée par l'utilisateur.

1. Dans le générateur Canvas, créez une étape de message RCS avec plusieurs réponses suggérées.

![Compositeur de messages RCS avec des réponses suggérées.]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. Connectez ce message à un parcours d'action avec un groupe d'actions pour chaque réponse suggérée.
3. Pour chaque groupe d'actions :
   - Sélectionnez le déclencheur **Send an SMS inbound message**.
   - Définissez le corps du message pour qu'il soit identique à la réponse suggérée correspondante.

![Étape de parcours d'action configurée avec trois groupes d'actions, un pour chaque réponse suggérée.]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. Connectez chaque groupe d'actions à une étape de message RCS, puis ajoutez du contenu en fonction de la réponse suggérée associée.
5. Poursuivez le flux conversationnel en ajoutant des réponses suggérées à tous les messages de suivi.
6. Répétez les étapes 2 à 4 jusqu'à ce que le flux soit terminé.

![Canvas montrant un flux conversationnel avec deux parcours d'action.]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

## Étape 4 : Prévisualiser et tester votre message {#step-4-preview-and-test-your-message}

Braze recommande toujours de prévisualiser et de tester votre message avant de l'envoyer. Passez à l'onglet **Test** pour envoyer un SMS, MMS ou RCS de test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou à des utilisateurs individuels, ou prévisualisez le message en tant qu'utilisateur directement dans Braze.

{% alert tip %}
Si vous souhaitez tester en combien de segments votre SMS pourrait être découpé, testez la longueur de votre texte avec le [calculateur de segments SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator).
{% endalert %}

![Prévisualisation du texte SMS depuis l'onglet Test du compositeur. Dans la section profil, le champ Prénom est défini sur « James ». Dans la section de prévisualisation, le SMS affiche désormais « Bonjour James, nous apprécions votre soutien ! »]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert note %}
Pour les MMS, l'ordre des ressources (image et corps du message) ne peut pas être personnalisé. L'ordre dépend du téléphone qui reçoit le message.
{% endalert %}

{% alert note %}
Étant donné que le rendu RCS est contrôlé par le système d'exploitation de l'utilisateur, le fabricant de l'appareil, l'opérateur et l'application de messagerie (par exemple, Google Messages vs. Apple Messages), l'apparence du message peut varier. La prévisualisation affichée dans Braze peut ne pas correspondre exactement à ce que l'utilisateur final reçoit. Validez le rendu final sur de vrais appareils dans la mesure du possible. Pour plus de détails sur le rendu RCS sur les appareils iOS, consultez [Pourquoi mon message RCS ne s'affiche-t-il pas correctement sur les appareils iOS ?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-doesnt-my-rcs-message-render-accurately-on-ios-devices).
{% endalert %}

Pour plus d'informations, consultez [Envoyer des messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=sms%2Fmms%20and%20rcs).

## Étape 5 : Construire le reste de votre campagne ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Ensuite, construisez le reste de votre campagne. Consultez les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer votre message.

### Choisir la planification ou le déclencheur de livraison {#choose-delivery-schedule-or-trigger}

Les messages peuvent être livrés en fonction d'une heure planifiée, d'une action ou d'un déclencheur API. Pour en savoir plus, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Pour la livraison par événement, vous pouvez également définir la durée de la campagne et les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

C'est également à cette étape que vous pouvez spécifier les contrôles de livraison, comme permettre aux utilisateurs de devenir [rééligibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) pour recevoir la campagne, ou activer les règles de [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping).

### Choisir les utilisateurs à cibler {#choose-users-to-target}

Ensuite, [ciblez les utilisateurs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) en choisissant des segments ou des filtres pour affiner votre audience. Vous devriez avoir déjà choisi le groupe d'abonnement, qui restreint les utilisateurs selon le niveau ou la catégorie de communication qu'ils souhaitent avoir avec vous.

{% multi_lang_include audience/target_audiences.md %}

Sélectionnez l'audience la plus large parmi vos segments, puis affinez ce segment davantage avec des filtres optionnels. Vous obtenez automatiquement un aperçu de la population approximative de ce segment. Gardez à l'esprit que l'appartenance exacte au segment est toujours calculée avant l'envoi du message.

{% alert tip %}
Intéressé par le reciblage ? Consultez [Reciblage des utilisateurs]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting) pour en savoir plus.
{% endalert %}

### Choisir les événements de conversion {#choose-conversion-events}

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

Les événements de conversion vous aident à mesurer le succès de votre campagne. Par exemple :

- Si vous utilisez le géociblage pour déclencher un message dont l'objectif final est que l'utilisateur effectue un achat, définissez l'événement de conversion sur `Purchase`.
- Si vous essayez d'inciter l'utilisateur à ouvrir votre application, définissez l'événement de conversion sur `Starts Session`.

Vous pouvez également définir des événements de conversion personnalisés en fonction de votre cas d'usage spécifique.

{% endtab %}
{% tab Canvas %}

Si ce n'est pas déjà fait, complétez les sections restantes de votre composant Canvas. Pour plus de détails sur la façon de construire le reste de votre Canvas, d'implémenter les tests multivariés et la sélection intelligente, et plus encore, consultez l'étape [Construire votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) de notre documentation Canvas.

{% endtab %}
{% endtabs %}

## Étape 6 : Vérifier et déployer {#step-6-review-and-deploy}

Après avoir terminé la construction de votre campagne ou Canvas, vérifiez ses détails, testez-le, puis envoyez-le !

Ensuite, consultez [Rapports SMS, MMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting) pour découvrir comment accéder aux résultats de vos campagnes.

## Questions fréquemment posées {#frequently-asked-questions}

### Puis-je envoyer des messages vocaux préenregistrés avec RCS ? {#can-i-send-pre-recorded-voicemails-with-rcs}

Oui, vous pouvez utiliser les messages média pour prendre en charge les fichiers audio.