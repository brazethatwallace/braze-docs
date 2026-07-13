---
nav_title: E-mail transactionnel
article_title: E-mail transactionnel
page_order: 4
page_type: landing
channel:
  - email
search_rank: 3
description: "Envoyez des e-mails transactionnels pour des notifications critiques et urgentes déclenchées par des appels API dans Braze."
---

# E-mail transactionnel {#transactional-email}

> Les e-mails transactionnels sont spécialement conçus pour envoyer des messages automatisés et non promotionnels afin de faciliter une transaction convenue entre vous et vos clients. Utilisez les campagnes d'e-mails transactionnels dans Braze pour envoyer des notifications critiques et urgentes déclenchées par des appels API, telles que des confirmations de commande, des réinitialisations de mot de passe et des mises à jour d'expédition.

## Conditions préalables {#prerequisites}

L'e-mail transactionnel n'est disponible que dans le cadre de certains forfaits Braze. Contactez votre gestionnaire de la satisfaction client Braze ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support) pour plus de détails.

Avant de commencer, assurez-vous de disposer des éléments suivants :

- La [configuration de l'e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup) terminée, y compris la configuration des adresses IP et du domaine, l'authentification et le réchauffement d'adresses IP
- Une **clé REST API Braze** avec la permission `transactional.send`

## Cas d'utilisation {#use-cases}

L'e-mail transactionnel est conçu pour envoyer des messages non promotionnels déclenchés par un service. Les cas d'utilisation courants sont les suivants :

| Cas d'utilisation | Explication |
| --- | --- |
| Confirmations de commande | Confirmer que l'achat d'un client a été reçu et est en cours de traitement. |
| Réinitialisations de mot de passe | Envoyer des liens sécurisés et urgents permettant aux clients de réinitialiser les identifiants de leur compte. |
| Notifications d'expédition | Informer les clients lorsque leur commande a été expédiée, y compris les informations de suivi et les dates de livraison estimées. |
| Alertes de compte | Envoyer des notifications critiques liées au compte, telles que des échecs de paiement, des modifications d'abonnement ou des alertes de sécurité. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'utilisation" }

## Différences entre l'e-mail transactionnel et l'e-mail marketing {#how-transactional-email-differs-from-marketing-email}

Les e-mails transactionnels sont envoyés via une [API HTTP transactionnelle]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) Braze dédiée, optimisée pour la rapidité et la fiabilité. Contrairement aux e-mails marketing, les e-mails transactionnels :

- Ne nécessitent pas que l'utilisateur ait donné son consentement aux communications marketing
- Sont déclenchés par des appels API plutôt que par des planifications ou des déclencheurs basés sur des actions
- Prennent en charge une distribution quasi instantanée pour les contenus urgents

## Étapes suivantes {#next-steps}

- [Créer un e-mail transactionnel]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email)
- [Configurer le suivi]({{site.baseurl}}/user_guide/channels/transactional_email/tracking)