---
nav_title: Bloc Gérer les abonnements
article_title: Bloc Gérer les abonnements
description: "Cet article explique comment ajouter et configurer le bloc de formulaire Gérer les abonnements sur une page de destination Braze, afin que les consommateurs puissent s'abonner à leurs groupes d'abonnement e-mail et les gérer."
page_order: 5
---

# Bloc Gérer les abonnements {#manage-subscriptions-block}

> Ajoutez un bloc **Gérer les abonnements** à une page de destination pour que les utilisateurs puissent consulter, s'abonner à et mettre à jour leurs groupes d'abonnement e-mail.

Le bloc **Gérer les abonnements** prend en charge deux cas d'usage principaux :

- **[Gérer les abonnements existants](#update-existing-subscriptions) :** Partagez l'[étiquette Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) de la page de destination dans un e-mail ou un message sur un autre canal. Lorsqu'un utilisateur identifié ouvre la page, le bloc pré-remplit automatiquement la case à cocher de chaque groupe d'abonnement avec son état d'abonnement actuel, afin qu'il puisse consulter et mettre à jour ses préférences.
- **[Capturer de nouveaux abonnements](#capture-new-subscribers) :** Ajoutez le bloc à une page de destination de génération de prospects, accompagné d'un bloc **Capture d'e-mail**, afin que les nouveaux visiteurs puissent choisir les groupes d'abonnement auxquels s'inscrire lors de l'envoi du formulaire.

{% alert important %}
Le bloc **Gérer les abonnements** ne prend en charge que les [groupes d'abonnement e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups). Il ne prend pas en charge les groupes d'abonnement SMS, RCS ou WhatsApp.
{% endalert %}

## Prérequis {#prerequisites}

| Exigences | Description |
| --- | --- |
| Groupes d'abonnement e-mail | Au moins un [groupe d'abonnement e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups), [créé depuis le tableau de bord]({{site.baseurl}}/user_guide/channels/email/subscriptions#creating-a-subscription-group) ou via les [endpoints de groupes d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups). |
| Autorisations de page de destination | Les mêmes [autorisations]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites) requises pour créer et modifier n'importe quelle page de destination. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Étape 1 : Ajouter le bloc Gérer les abonnements {#step-1-add-the-manage-subscriptions-block}

Dans l'éditeur de page de destination par glisser-déposer, accédez à la section **Build** et sélectionnez **Form Blocks**. Faites glisser **Manage Subscriptions** dans une ligne de votre page ; le bloc s'ajuste automatiquement à la largeur de la colonne.

Le bloc est vide tant que vous n'y avez pas ajouté de groupes d'abonnement.

## Étape 2 : Sélectionner les groupes d'abonnement {#step-2-select-the-subscription-groups}

Avec le bloc **Manage Subscriptions** sélectionné, cliquez sur **+ Add subscription groups** dans le panneau **Block properties** à droite. Une liste des [groupes d'abonnement par e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups) disponibles dans votre espace de travail s'affiche.

Cochez la case à côté de chaque groupe d'abonnement que vous souhaitez inclure, puis confirmez votre sélection pour les ajouter au bloc. Chaque groupe d'abonnement apparaît sous la forme d'une case à cocher sélectionnable sur la page de destination.

{% alert note %}
Le bloc **Manage Subscriptions** affiche uniquement les groupes que vous ajoutez explicitement. L'ajout d'un groupe d'abonnement au bloc n'abonne pas automatiquement les visiteurs à ce groupe : un visiteur doit cocher la case du groupe et soumettre le formulaire.
{% endalert %}

## Étape 3 : Configurer les paramètres du bloc {#step-3-configure-the-block-settings}

Utilisez le panneau **Block properties** pour ajuster le comportement et l'apparence du bloc.

### Groupes d'abonnement {#subscription-groups}

- **Réorganiser les groupes :** Faites glisser un groupe d'abonnement par sa poignée pour modifier l'ordre dans lequel il apparaît dans le bloc.
- **Ajouter ou supprimer des groupes :** Sélectionnez **+ Add subscription groups** pour inclure davantage de groupes, ou sélectionnez l'icône de suppression à côté d'un groupe pour le retirer du bloc.

### Inclure des descriptions {#include-descriptions}

Activez **Include descriptions** pour afficher le texte descriptif de chaque groupe d'abonnement à côté de son nom, offrant ainsi aux visiteurs plus de contexte sur ce à quoi ils s'abonnent.

### Case à cocher « S'abonner à tous » {#subscribe-to-all-checkbox}

Activez le paramètre **"Subscribe to all" checkbox** pour ajouter une case à cocher supplémentaire au bloc. Lorsqu'un visiteur la sélectionne, toutes les cases à cocher des groupes d'abonnement du bloc sont cochées — pratique pour un abonnement rapide à tous les groupes répertoriés.

## Mettre à jour les abonnements existants {#update-existing-subscriptions}

Pour permettre aux utilisateurs existants de consulter et mettre à jour leurs abonnements e-mail, partagez la page de destination en utilisant son [étiquette Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) dans un e-mail, une étape du Canvas ou un autre message. Lorsqu'un utilisateur ouvre la page via ce lien, Braze l'identifie et pré-remplit automatiquement chaque case à cocher de groupe d'abonnement dans le bloc **Manage Subscriptions** pour correspondre à son état d'abonnement actuel, de manière similaire à un [centre de préférences e-mail]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

L'utilisateur peut cocher ou décocher les cases pour mettre à jour ses abonnements, puis soumettre le formulaire pour enregistrer ses modifications.

{% alert note %}
Le pré-remplissage de l'état d'abonnement actuel d'un utilisateur dans le bloc **Manage Subscriptions** est inclus par défaut et ne nécessite pas le [niveau Landing Pages Pro]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers). Cela diffère du [pré-remplissage basé sur Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#pre-fill-form-fields) pour les autres champs de formulaire, qui nécessite Landing Pages Pro.
{% endalert %}

## Capturer de nouveaux abonnés {#capture-new-subscribers}

Pour collecter de nouveaux abonnés, par exemple sur une page de destination de génération de leads, associez le bloc **Manage Subscriptions** à un [bloc Email Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) afin que la page capture l'adresse e-mail du consommateur en même temps que ses sélections de groupes d'abonnement.

Si le consommateur n'est pas identifié (par exemple, s'il arrive sans étiquette Liquid de page de destination), les cases à cocher ne sont pas sélectionnées par défaut. Lorsqu'il soumet le formulaire, il est abonné aux groupes d'abonnement qu'il a sélectionnés.

## Ce qu'il faut savoir {#things-to-know}

- **Consentement SMS, RCS et WhatsApp :** pour recueillir le consentement pour ces canaux sur une page de destination plutôt que par e-mail, utilisez un [bloc Capture de téléphone]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).
- **Expérience de confirmation :** les pages de destination comportant des blocs de formulaire, y compris **Gérer les abonnements**, nécessitent une expérience de confirmation après la soumission. [Créez une page de confirmation]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional) et associez-la à votre bouton **Submit**.
- **Référence des blocs éditeur :** pour une référence complète de chaque bloc de page de destination et de ses propriétés, consultez [Blocs éditeur (pages de destination)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).