---
nav_title: Envoi de SMS
article_title: Envoi de SMS
page_order: 4
alias: /sms_message_sending/
description: "Cet article de référence couvre les bases et les bonnes pratiques de l'envoi de SMS."
page_type: reference
channel:
  - SMS

---

# Envoi de messages SMS {#sms-message-sending}

> L'envoi de messages peut sembler complexe, mais ce n'est pas une fatalité. Les sections suivantes présentent les fondamentaux de l'envoi de messages SMS avec Braze, notamment l'importance des groupes d'abonnement, les exigences relatives aux segments de message et au corps des messages, ainsi que les options de personnalisation avancées disponibles.

## Les bases de l'envoi de SMS {#sms-sending-basics}

### Sélectionner votre groupe d'abonnement {#select-your-subscription-group}

Les messages SMS doivent être envoyés depuis un [groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups/). Un groupe d'abonnement est un ensemble de numéros de téléphone d'envoi (tels que des codes courts, des codes longs et/ou des identifiants d'expéditeur alphanumériques) utilisés pour un type spécifique d'envoi de messages. Vous devez désigner un groupe d'abonnement pour vous assurer que seuls les utilisateurs abonnés sont ciblés. Certains clients peuvent avoir plusieurs groupes d'abonnement pour différents cas d'utilisation, comme l'envoi de SMS transactionnels et l'envoi de SMS promotionnels.<br><br>

### Saisir le corps du message {#input-message-body}

Le corps d'un message SMS accepte jusqu'à 1 600 caractères, y compris les emojis, le Liquid et le Contenu connecté. Un seul envoi de Campaign peut générer l'envoi de plusieurs segments de message. Les corps de messages SMS Braze peuvent être composés selon les normes d'encodage [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) ou [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set). Si un caractère UCS-2 (par exemple, un emoji) est utilisé, le corps du message sera automatiquement formaté selon cette norme d'encodage.<br><br>

### Comprendre les segments de message et les limites de caractères {#understand-message-segments-and-character-limits}

Les segments de message SMS correspondent à la manière dont l'industrie du SMS comptabilise les messages. Un segment de message est un regroupement d'un nombre défini de caractères (160 pour l'encodage GSM-7 ; 67 pour l'encodage UCS-2) qui sera envoyé en un seul envoi SMS. Si vous envoyez un SMS de 161 caractères en encodage GSM-7, vous constaterez que deux (2) segments de message ont été envoyés. L'envoi de plusieurs segments de message peut entraîner des frais supplémentaires.<br><br>

### Personnalisation des mots-clés (facultatif) {#keyword-customization-optional}

La réglementation exige des réponses à toutes les réponses par mots-clés SMS d'abonnement (Opt-In), de désabonnement (Opt-Out) et d'aide/information (Help/Info). Avec Braze, vous pouvez définir vos propres mots-clés pour déclencher les réponses d'abonnement, de désabonnement et d'aide, gérer vos propres réponses envoyées aux utilisateurs, et définir des ensembles de mots-clés pour différentes langues. Pour en savoir plus, consultez notre collection sur le [traitement des mots-clés]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/).

{% alert tip %}
Vous souhaitez apprendre à créer une campagne SMS ? Consultez notre guide étape par étape sur la [création d'un message SMS, MMS ou RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/).
{% endalert %}

Pour les bonnes pratiques d'envoi, y compris les recommandations pour l'envoi multi-pays et à haut volume, consultez les [bonnes pratiques pour les SMS, MMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/best_practices/).