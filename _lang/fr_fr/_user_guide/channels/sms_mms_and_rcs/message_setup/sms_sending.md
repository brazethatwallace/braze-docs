---
nav_title: Envoi de SMS
article_title: Envoi de SMS
page_order: 4
alias: /sms_message_sending/
description: "Consultez les groupes d'abonnement, la facturation des messages et les fondamentaux des mots-clés pour l'envoi de messages SMS."
page_type: reference
channel:
  - SMS

---

# Envoi de messages SMS {#sms-message-sending}

> Consultez les fondamentaux relatifs aux abonnements, à la facturation et aux mots-clés qui s'appliquent lorsque vous envoyez des messages SMS avec Braze.

## Principes de base de l'envoi de SMS {#sms-sending-basics}

### Sélectionner votre groupe d'abonnement {#select-your-subscription-group}

Envoyez des messages SMS à partir d'un [groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups). Un groupe d'abonnement contient des numéros de téléphone d'envoi, tels que des codes courts, des codes longs et des identifiants d'expéditeur alphanumériques, pour un objectif de communication spécifique. Utilisez des groupes d'abonnement distincts pour des cas d'usage tels que la communication transactionnelle et promotionnelle.

### Composer le message {#compose-the-message}

Pour les champs de message, les limites de caractères, la personnalisation, les médias et le raccourcissement de liens, consultez [Créer un message SMS, MMS ou RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create#sms-and-mms-fields-and-settings).

### Comprendre les segments de message et les limites de caractères {#understand-message-segments-and-character-limits}

Les messages SMS utilisent l'encodage GSM-7 ou UCS-2 et sont facturés par segment de message. Pour les règles d'encodage, les tailles de segment et le calculateur de segments, consultez [Calculateurs de facturation SMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).

### Personnalisation des mots-clés (facultatif) {#keyword-customization-optional}

La réglementation exige des réponses aux mots-clés d'abonnement, de désabonnement et d'aide ou d'information. Définissez les mots-clés, les réponses et les ensembles de mots-clés spécifiques à chaque langue via le [traitement des mots-clés]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing).

Pour les bonnes pratiques d'envoi, y compris les recommandations pour l'envoi multi-pays et à haut volume, consultez [Bonnes pratiques pour les SMS, MMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/best_practices).