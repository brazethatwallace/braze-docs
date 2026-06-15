---
title: Ketch
nav_title: Ketch
description: "Cet article de référence est consacré à l'intégration de Braze et de Ketch. Ketch permet de simplifier les opérations de confidentialité et d'assurer un contrôle complet et dynamique des données, ainsi que des informations qui en sont extraites."
alias: /partners/ketch
page_type: partner
search_tag: Ketch
---

# Ketch

> [Ketch](https://www.ketch.com) permet aux entreprises d'être des gestionnaires responsables de leurs données. Ketch simplifie les opérations de confidentialité et offre un contrôle et un traitement complet et dynamique des données.

_Cette intégration est maintenue par Ketch._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Ketch vous permet de contrôler les préférences de communication des clients dans le centre de préférences de Ketch et de propager automatiquement ces changements dans Braze.

{% alert note %}
Vous souhaitez obtenir des conseils sur la création de groupes d'abonnement ? Consultez nos articles sur les <a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/'>groupes d'abonnement SMS</a> et les <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/'>groupes d'abonnement e-mail</a>.
{% endalert %}

## Conditions préalables {#prerequisites}

| Exigences | Description |
|---|---|
| Compte Ketch | Un compte [Ketch](https://www.ketch.com) avec des privilèges d'administrateur est requis pour activer cette intégration. |
| Clé API de Braze | Une clé API REST de Braze avec les autorisations `users.track`, `subscription.status.get`, `subscription.status.set`, `users.delete`, `users.alias.new`, `users.export.ids`, `email.unsubscribe` et `email.blacklist`. <br><br> Cette clé peut être créée dans le tableau de bord de Braze (**Console de développement** > **Clé API REST** > **Créer une nouvelle clé API**). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration {#integration}

### Étape 1 : Établir la connexion Braze {#step-1-set-up-the-braze-connection}

1. Dans votre [instance Ketch](https://app.ketch.com), accédez à **Data Systems** et sélectionnez **Braze**. Cliquez ensuite sur **New Connection**.
2. Donnez à votre connexion Braze un nom identifiable, qui sera utilisé pour faire référence à cette connexion dans les processus basés sur l'API. Notez qu'un code sera également créé pour cette connexion. Ce code doit être unique pour l'ensemble des connexions.
3. Confirmez le mappage de l'identité de vos utilisateurs. Par défaut, Ketch mappe les identités des utilisateurs en fonction de leur adresse e-mail ou de leur `external_id` dans Braze.
4. Ajoutez la clé API de Braze et indiquez l'endpoint de l'API. Notez que cet [endpoint API]({{site.baseurl}}/api/basics/#endpoints) dépend de l'instance de Braze utilisée par votre organisation.

### Étape 2 : Configurer les préférences d'abonnement {#step-2-configure-subscription-preferences}

1. Accédez à **Policy Center** > **Subscriptions**. Si vous ne voyez pas l'onglet des abonnements sous **Policy Center**, assurez-vous que vous avez accès au centre de préférences marketing et vérifiez que vous disposez des autorisations de compte nécessaires pour accéder à cette partie du produit.
2. Cliquez sur **Create New Subscription** pour créer un nouveau sujet. Chaque abonnement aura un nom et un code.
3. Ajoutez les canaux pour l'envoi de vos sujets d'abonnement. Chaque canal s'affichera dans le centre de préférences marketing de vos utilisateurs. Vous pouvez également préciser la manière dont vous souhaitez que le centre de préférences Ketch orchestre un signal d'abonnement ou de désabonnement particulier.
4. Sélectionnez la connexion Braze que vous souhaitez utiliser pour orchestrer les signaux d'abonnement et de désabonnement.
5. Saisissez le `subscription_group_id` de Braze correspondant au groupe d'abonnement auquel vous souhaitez envoyer les préférences utilisateur de Ketch.

![ID de groupe d'abonnement Braze.]({% image_buster /assets/img/ketch/ketch1.png %})

{% alert note %}
Afin de collecter et d'orchestrer les signaux d'abonnement et de désabonnement des utilisateurs, les identités doivent être correctement configurées. Ketch recommande de configurer l'e-mail comme identifiant pour orchestrer les signaux de préférence des utilisateurs pour cette intégration.
{% endalert %}


### Étape 3 : Configurer les identités {#step-3-configure-identities}

Un utilisateur ne peut voir le centre de préférences marketing que lorsque Ketch peut confirmer son identité en matière de préférences marketing. Si Ketch ne parvient pas à capturer correctement l'identité de l'utilisateur, la page des préférences marketing n'apparaît pas, car Ketch n'est pas en mesure de gérer ses préférences.

1. Pour configurer l'identité des préférences marketing, accédez à la page **Settings** dans Ketch, puis cliquez sur **Identity space**. Vous devrez soit créer un nouvel espace d'identité, soit modifier un espace d'identité existant pour l'assigner comme identité de préférence marketing. Vérifiez que l'étiquette Ketch déployée sur la propriété capture correctement cet espace d'identité.
2. Accédez à **Experience Server** > **Properties** et modifiez la propriété souhaitée. Sous la couche de données de cette propriété, veillez à activer l'espace d'identité personnalisé. Ensuite, configurez la manière dont l'identité de préférence marketing est capturée sur ce site.
3. Une fois l'espace d'identité configuré, vérifiez que le centre de préférences apparaît en l'ouvrant sur le site web où l'étiquette Ketch a été déployée.