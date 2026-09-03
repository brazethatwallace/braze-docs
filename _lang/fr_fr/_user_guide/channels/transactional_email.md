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

## Prérequis {#prerequisites}

L'e-mail transactionnel est uniquement disponible dans le cadre de certains forfaits Braze. Contactez votre gestionnaire de la satisfaction client Braze ou ouvrez un [ticket d'assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support) pour plus de détails.

Avant de commencer, assurez-vous de disposer des éléments suivants :

- [Configuration de l'e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup) terminée, y compris la configuration de l'IP et du domaine, l'authentification et l'IP warming
- Une **clé REST API Braze** avec la permission `transactional.send`

## Cas d'usage {#use-cases}

L'e-mail transactionnel est conçu pour l'envoi de messages non promotionnels déclenchés par un service. Les cas d'usage courants incluent les suivants :

| Cas d'usage | Explication |
| --- | --- |
| Confirmations de commande | Confirmer que l'achat d'un client a bien été reçu et est en cours de traitement. |
| Réinitialisations de mot de passe | Distribuer des liens sécurisés et sensibles au facteur temps permettant aux clients de réinitialiser les identifiants de leur compte. |
| Notifications d'expédition | Notifier les clients lorsque leur commande a été expédiée, y compris les informations de suivi et les dates de livraison estimées. |
| Alertes de compte | Envoyer des notifications critiques liées au compte, telles que les échecs de paiement, les modifications d'abonnement ou les alertes de sécurité. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'usage" }

## Différences entre les e-mails transactionnels et les e-mails marketing {#how-transactional-email-differs-from-marketing-email}

Les e-mails transactionnels sont envoyés via une [API HTTP transactionnelle]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email) dédiée de Braze, optimisée pour la rapidité et la fiabilité. Contrairement aux e-mails marketing, les e-mails transactionnels :

- Ne nécessitent pas que l'utilisateur ait consenti à recevoir des communications marketing
- Sont déclenchés par des appels API plutôt que par des déclencheurs planifiés ou basés sur des actions
- Prennent en charge une distribution quasi instantanée pour les contenus urgents

## Étapes suivantes {#next-steps}

- [Créer un e-mail transactionnel]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email)
- [Suivi]({{site.baseurl}}/user_guide/channels/transactional_email/tracking)