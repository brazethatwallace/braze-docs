---
nav_title: WhatsApp
article_title: WhatsApp
page_order: 10
page_type: landing
channel:
  - WhatsApp
search_rank: 3
description: "Atteignez vos clients avec des messages WhatsApp personnalisés pour l'assistance, les notifications et les campagnes promotionnelles via Braze."
alias: /whatsapp/
---

# WhatsApp

> WhatsApp est une plateforme de messagerie pair-à-pair utilisée dans le monde entier pour la messagerie conversationnelle des entreprises. Avec le canal WhatsApp dans Braze, vous pouvez envoyer des messages d'assistance, des notifications et des campagnes promotionnelles dans des conversations en fil que les utilisateurs utilisent déjà au quotidien. Ce hub couvre la configuration de WhatsApp, les types de messages, les modèles, la gestion des abonnements et le reporting. Commencez par la [configuration de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) pour connecter vos comptes Meta Business et WhatsApp Business, puis créez votre premier message basé sur un modèle. Consultez [Abonnements et désabonnements]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) avant d'envoyer des messages promotionnels à de nouveaux utilisateurs.

## Conditions préalables {#prerequisites}

La disponibilité de WhatsApp dépend de votre offre Braze. Contactez votre gestionnaire de compte ou votre gestionnaire de la satisfaction client pour commencer.

Avant de commencer, assurez-vous de disposer des éléments suivants :

- Un compte Meta Business Manager et un compte WhatsApp Business
- Un numéro de téléphone WhatsApp qui respecte les exigences de l'[API Cloud](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)

Pour une présentation complète, consultez la [configuration de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup).

## Cas d'usage {#use-cases}

| Cas d'usage | Explication |
| --- | --- |
| Support client | Permettez des conversations bidirectionnelles en temps réel pour traiter les demandes, résoudre les problèmes et fournir une assistance personnalisée. |
| Notifications de commande | Envoyez des confirmations de commande, des mises à jour d'expédition et des notifications de livraison directement aux clients sur WhatsApp. |
| Rappels de rendez-vous | Réduisez les absences grâce à des rappels de rendez-vous envoyés en temps opportun et permettez aux clients de confirmer ou de reprogrammer. |
| Campaigns promotionnelles | Contactez les clients avec des promotions ciblées, des lancements de produits et des offres personnalisées grâce à des messages multimédias enrichis. |
| Conversations bidirectionnelles | Développez des relations plus profondes grâce à une communication interactive qui permet aux clients de répondre, de poser des questions et de donner leur avis. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'usage" }

## Questions fréquemment posées {#frequently-asked-questions}

### Comment connecter WhatsApp à Braze ? {#how-do-i-connect-whatsapp-to-braze}

Créez un compte Meta Business Manager et un compte WhatsApp Business, puis suivez les étapes décrites dans [Configuration de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup).

### Quels types de messages puis-je envoyer sur WhatsApp ? {#what-message-types-can-i-send-on-whatsapp}

Utilisez des modèles approuvés pour les messages sortants et les messages de session pris en charge pour les conversations bidirectionnelles. Consultez [Créer un message WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message) pour connaître les types de messages pris en charge.

### Les utilisateurs doivent-ils donner leur consentement pour recevoir des messages WhatsApp ? {#do-users-need-to-opt-in-to-whatsapp-messages}

Oui. Les utilisateurs doivent donner leur consentement avant que vous n'envoyiez des messages promotionnels ou récurrents sur WhatsApp. Consultez [Abonnements et désabonnements]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) pour la gestion des abonnements.

## Prochaines étapes {#next-steps}

{% article_tiles %}
- name: Configuration de WhatsApp
  link: /docs/user_guide/channels/whatsapp/whatsapp_setup
- name: Créer un message WhatsApp
  link: /docs/user_guide/channels/whatsapp/create_a_whatsapp_message
{% endarticle_tiles %}