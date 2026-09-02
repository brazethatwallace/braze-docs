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
description: "Découvrez les SMS, MMS et RCS dans Braze, y compris la configuration, la conformité et les bonnes pratiques pour contacter les utilisateurs par numéro de téléphone."
---

# SMS, MMS et RCS {#sms-mms-and-rcs}

> Les SMS (Short Messaging Service), MMS (Multimedia Messaging Service) et RCS (Rich Communication Services) offrent un moyen direct de contacter vos utilisateurs sur leur numéro de téléphone en temps réel. Le SMS reste l'un des canaux les plus utilisés au monde, car il est rapide, familier et efficace pour les communications urgentes. Ce hub couvre la configuration de l'expéditeur, la conformité, la collecte des abonnements, la création de messages et le reporting pour les SMS, MMS et RCS dans Braze. Consultez [Lois et réglementations]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) et [Collecter les abonnements des utilisateurs]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) avant d'envoyer votre premier message.

## Prérequis {#prerequisites}

La disponibilité des SMS, MMS et RCS dépend de votre offre Braze. Contactez votre gestionnaire de compte ou votre CSM or gestionnaire de la satisfaction client or gestionnaire du succès des clients pour commencer.

Avant de commencer, assurez-vous de disposer des éléments suivants :

- Des codes courts, des codes longs ou des identifiants d'expéditeur alphanumériques configurés. Pour plus d'informations, consultez [Configuration de l'expéditeur]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).
- Une connaissance des lois et réglementations relatives aux SMS, notamment le TCPA et les exigences des opérateurs. Pour plus d'informations, consultez [Lois et réglementations]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).
- Un consentement explicite d'abonnement recueilli auprès des utilisateurs. Pour plus d'informations, consultez [Recueil des abonnements utilisateurs]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins).

## Cas d'usage {#use-cases}

| Cas d'usage | Explication |
| --- | --- |
| Rappels de rendez-vous | Envoyez des rappels en temps utile avant les rendez-vous programmés, réduisant les absences et tenant les clients informés. |
| Mises à jour de commandes | Informez les clients des confirmations de commande, de l'état d'expédition et des mises à jour de livraison en temps réel. |
| Authentification à deux facteurs | Envoyez des codes de vérification à usage unique pour la connexion au compte et la confirmation de transactions. |
| Offres promotionnelles | Contactez les clients avec des promotions limitées dans le temps, des ventes flash et des remises personnalisées directement sur leur téléphone. |
| Support client | Activez des conversations bidirectionnelles pour résoudre les demandes des clients, recueillir des commentaires ou confirmer des demandes de service. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'usage" }

## Comparaison des SMS, MMS et RCS {#sms-mms-and-rcs-compared}

- **SMS** envoie des messages texte uniquement, jusqu'à 160 caractères (ou 70 caractères avec Unicode). Il est universellement pris en charge par tous les appareils mobiles et opérateurs.
- **MMS** étend le SMS en prenant en charge le contenu multimédia, notamment les images, les GIF et l'audio. Le MMS nécessite la prise en charge par l'opérateur et l'appareil.
- **RCS** est la nouvelle génération de la messagerie d'entreprise, offrant des fonctionnalités avancées telles que des profils d'expéditeur de marque, des réponses suggérées, des carrousels et des accusés de lecture. La disponibilité du RCS dépend de la prise en charge par l'opérateur et l'appareil.

### Pourquoi utiliser le RCS ? {#why-use-rcs}

Le RCS (Rich Communication Services) s'appuie sur le SMS pour offrir une expérience plus riche, proche d'une application, dans l'application de messagerie par défaut des appareils compatibles. Les marques utilisent le RCS pour :

- Envoyer des images haute résolution et des vidéos au lieu de simples messages texte.
- Ajouter des réponses et des actions suggérées afin que les clients puissent répondre en un seul appui.
- Afficher un profil d'expéditeur vérifié avec l'identité de marque pour que les messages inspirent confiance.
- Prendre en charge les accusés de lecture et les indicateurs de saisie lorsque les opérateurs le permettent.

Le RCS est adapté à des cas d'usage tels que les mises à jour transactionnelles (expéditions, rendez-vous), les promotions avec des créations enrichies, le support client avec des parcours de réponse rapide, ainsi que l'onboarding ou les tutoriels qui tirent parti des médias et des actions structurées. Pour la configuration et la migration depuis le SMS, consultez la section [Configuration RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup).

## Questions fréquemment posées {#frequently-asked-questions}

### Ai-je besoin du consentement d'abonnement avant d'envoyer des SMS dans Braze ? {#do-i-need-opt-in-consent-before-sending-sms-in-braze}

Oui. Recueillez le consentement explicite d'abonnement et respectez les lois applicables telles que le TCPA et les exigences des opérateurs. Consultez [Recueillir les abonnements des utilisateurs]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) et [Lois et réglementations]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

### Quelle est la différence entre SMS, MMS et RCS ? {#what-is-the-difference-between-sms-mms-and-rcs}

Le SMS envoie des messages texte uniquement, le MMS ajoute du contenu multimédia comme des images, et le RCS offre des fonctionnalités enrichies telles que des profils d'expéditeur de marque et des réponses suggérées sur les appareils compatibles. Consultez la section **Comparaison SMS, MMS et RCS** plus haut sur cette page.

### Comment configurer les numéros d'expéditeur pour les SMS ? {#how-do-i-configure-sender-numbers-for-sms}

Configurez des codes courts, des codes longs ou des identifiants d'expéditeur alphanumériques dans Braze avant de lancer des campagnes. Consultez [Configuration de l'expéditeur]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).

## Étapes suivantes {#next-steps}

- [Configuration des messages]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup)
- [Créer un message]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create)