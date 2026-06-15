---
nav_title: "SMS, MMS et RCS"
article_title: "SMS, MMS et RCS"
page_order: 8
page_type: landing
channel:
  - SMS
  - MMS
  - RCS
search_rank: 3
description: "Cette page d'accueil est dédiée aux SMS (Short Messaging Service), MMS (Multimedia Messaging Service) et RCS (Rich Communication Services). Ces services offrent un moyen plus direct d'atteindre vos utilisateurs que la plupart des autres canaux de communication, car ils utilisent leur numéro de téléphone, ce qui vous permet de les joindre en temps réel."
---

# SMS, MMS et RCS {#sms-mms-and-rcs}

> Les SMS (Short Messaging Service), MMS (Multimedia Messaging Service) et RCS (Rich Communication Services) offrent un moyen plus direct d'atteindre vos utilisateurs que la plupart des autres canaux de communication, car ils utilisent les numéros de téléphone pour une portée en temps réel.

Le SMS reste l'un des canaux les plus utilisés au monde — des milliards de messages texte sont envoyés chaque jour — car il est rapide, direct et familier pour les clients.

## Conditions préalables {#prerequisites}

La disponibilité des SMS, MMS et RCS dépend de votre offre Braze. Contactez votre gestionnaire de compte ou votre gestionnaire de la satisfaction client pour commencer.

Avant de commencer, assurez-vous de disposer des éléments suivants :

- Des codes courts, des codes longs ou des identifiants d'expéditeur alphanumériques configurés. Pour en savoir plus, consultez [Configuration de l'expéditeur]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/).
- Une connaissance des lois et réglementations relatives aux SMS, y compris le TCPA et les exigences des opérateurs. Pour en savoir plus, consultez [Lois et réglementations]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/).
- Un consentement explicite d'abonnement recueilli auprès des utilisateurs. Pour en savoir plus, consultez [Collecte des abonnements des utilisateurs]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins/).

## Cas d'utilisation {#use-cases}

| Cas d'utilisation | Explication |
| --- | --- |
| Rappels de rendez-vous | Envoyez des rappels en temps opportun avant les rendez-vous planifiés, réduisant les absences et tenant les clients informés. |
| Mises à jour de commande | Informez les clients des confirmations de commande, de l'état d'expédition et des mises à jour de livraison en temps réel. |
| Authentification à deux facteurs | Envoyez des codes de vérification à usage unique pour la connexion au compte et la confirmation de transaction. |
| Offres promotionnelles | Atteignez les clients avec des promotions à durée limitée, des ventes flash et des remises personnalisées directement sur leur téléphone. |
| Assistance client | Activez des conversations bidirectionnelles pour résoudre les demandes des clients, recueillir des retours ou confirmer des demandes de service. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Use cases" }

## Comparaison des SMS, MMS et RCS {#sms-mms-and-rcs-compared}

- Le **SMS** envoie des messages texte uniquement, jusqu'à 160 caractères (ou 70 caractères avec Unicode). Il est universellement pris en charge sur tous les appareils mobiles et par tous les opérateurs.
- Le **MMS** étend le SMS avec la prise en charge de contenu multimédia, y compris les images, les GIF et l'audio. Le MMS nécessite la prise en charge par l'opérateur et l'appareil.
- Le **RCS** est la prochaine génération de l'envoi de messages professionnels, offrant des fonctionnalités riches telles que des profils d'expéditeur de marque, des réponses suggérées, des carrousels et des accusés de lecture. La disponibilité du RCS dépend de la prise en charge par l'opérateur et l'appareil.

### Pourquoi utiliser le RCS ? {#why-use-rcs}

Le RCS (Rich Communication Services) s'appuie sur le SMS pour offrir une expérience plus riche, semblable à une application, dans l'application de messagerie par défaut des appareils compatibles. Les marques utilisent le RCS pour :

- Envoyer des images et des vidéos en haute résolution au lieu de simples textes.
- Ajouter des réponses et des actions suggérées pour que les clients puissent répondre en un seul appui.
- Afficher un profil d'expéditeur vérifié avec l'image de marque pour que les messages inspirent confiance.
- Prendre en charge les accusés de lecture et les indicateurs de saisie lorsque les opérateurs le permettent.

Le RCS est adapté à des cas d'utilisation tels que les mises à jour transactionnelles (expédition, rendez-vous), les promotions avec du contenu riche, l'assistance client avec des parcours de réponse rapide, et l'onboarding ou les tutoriels qui bénéficient de médias et d'actions structurées. Pour la configuration et la migration depuis le SMS, consultez [Configuration du RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup/).

## Étapes suivantes {#next-steps}

- [Configuration des messages]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/)
- [Créer un message]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/)