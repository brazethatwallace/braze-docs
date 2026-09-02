---
nav_title: "Comptes professionnels multiples"
article_title: "Comptes professionnels multiples"
page_order: 5
description: "Cet article de référence couvre les étapes pour ajouter des comptes WhatsApp Business et des numéros de téléphone."
page_type: reference
channel:
  - WhatsApp
---

# Comptes WhatsApp Business et numéros de téléphone multiples {#multiple-whatsapp-business-accounts-and-phone-numbers}

> Vous pouvez ajouter plusieurs comptes WhatsApp Business et groupes d'abonnement (ainsi que des numéros de téléphone) à chaque espace de travail. <br><br>Chaque groupe d'abonnement est connecté à un numéro de téléphone unique, ce qui signifie que vous ne pouvez pas connecter le même numéro de téléphone à plusieurs groupes d'abonnement, ni connecter plusieurs numéros de téléphone à un même groupe d'abonnement.

## Comptes WhatsApp Business multiples {#multiple-whatsapp-business-accounts}

Disposer de plusieurs comptes WhatsApp Business est utile si vous souhaitez envoyer des messages WhatsApp aux utilisateurs dans un espace de travail Braze qui comporte plusieurs marques. En effet, chaque compte professionnel fonctionne de manière indépendante au sein de WhatsApp et possède son propre numéro de téléphone, ses propres modèles de messages et sa propre évaluation de qualité.

Les comptes professionnels imbriqués dans le même Meta Business gestionnaire partagent également la gestion des autorisations d'accès des utilisateurs et les catalogues (pas encore pris en charge sur Braze).

![Diagramme de l'écosystème Braze et WhatsApp, montrant comment les espaces de travail et les comptes WhatsApp Business se connectent entre eux : vous pouvez connecter un groupe d'abonnement à un numéro de téléphone, plusieurs comptes WhatsApp Business à un espace de travail, et un espace de travail à plusieurs Meta Business Portfolios.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

### Ajouter un compte WhatsApp Business {#adding-a-whatsapp-business-account}

Vous pouvez ajouter jusqu'à 10 comptes WhatsApp Business par espace de travail. Les comptes professionnels peuvent être imbriqués dans différents Meta Business Managers. Pour ajouter un compte :

1. Accédez à **Partenaires technologiques** > **WhatsApp** et sélectionnez **Ajouter un compte WhatsApp Business**.

![Section d'intégration de l'envoi de messages WhatsApp avec des options pour ajouter un compte professionnel ou ajouter un groupe d'abonnement et un numéro.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2. Suivez le processus d'inscription. Pour un guide détaillé étape par étape, consultez [Inscription intégrée WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup).

{% alert important %}
Votre numéro de téléphone doit respecter toutes les exigences applicables à tout numéro de téléphone WhatsApp, y compris ne pas être enregistré sur d'autres comptes WhatsApp.
{% endalert %}

## Groupes d'abonnement et numéros de téléphone multiples {#multiple-subscription-groups-and-phone-numbers}

Les modèles de messages sont partagés entre tous les numéros de téléphone d'un même compte WhatsApp Business. Pour plus de détails sur les groupes d'abonnement WhatsApp, consultez [Groupes d'abonnement]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).

Chaque numéro de téléphone WhatsApp apparaîtra comme une conversation WhatsApp distincte pour les utilisateurs. Chaque numéro de téléphone au sein d'un compte WhatsApp Business fonctionne indépendamment des autres, ce qui signifie qu'ils peuvent avoir les mêmes valeurs ou des valeurs différentes pour les éléments suivants :
- Nom d'affichage
- État
- Évaluation de qualité
- Limite d'envoi de messages

### Ajouter un groupe d'abonnement et un numéro de téléphone {#adding-a-subscription-group-and-phone-number}

Vous pouvez ajouter jusqu'à 20 groupes d'abonnement (et numéros de téléphone d'envoi) par compte WhatsApp Business. Pour ajouter un groupe d'abonnement et un numéro de téléphone :

1. Accédez à **Partenaires technologiques** > **WhatsApp** et sélectionnez **Ajouter un groupe d'abonnement et un numéro**.

![Section d'intégration de l'envoi de messages WhatsApp avec des options pour ajouter un compte professionnel ou ajouter un groupe d'abonnement et un numéro.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2. Suivez le processus d'inscription. <br><br> À l'étape **Sélectionner votre compte WhatsApp Business**, sélectionnez votre compte WhatsApp Business existant et ajoutez un nouveau numéro de téléphone. Ce numéro doit respecter toutes les exigences applicables à tout numéro de téléphone WhatsApp, y compris ne pas être enregistré sur d'autres comptes WhatsApp.

### Supprimer un groupe d'abonnement et un numéro de téléphone {#removing-a-subscription-group-and-phone-number}

1. Accédez à **Audience** > **Abonnements** et archivez le groupe d'abonnement.
2. Accédez à votre Meta Business gestionnaire et supprimez le numéro de téléphone.