---
nav_title: Bloc Gérer les abonnements
article_title: Bloc Gérer les abonnements
description: "Cet article explique comment ajouter et configurer le bloc de formulaire Gérer les abonnements sur une page de destination Braze, afin que les consommateurs puissent s'abonner et gérer leurs groupes d'abonnement e-mail, SMS ou WhatsApp."
page_order: 5
---

# Bloc Gérer les abonnements {#manage-subscriptions-block}

> Ajoutez un bloc **Gérer les abonnements** à une page de destination pour que les utilisateurs puissent consulter, s'abonner à et mettre à jour leurs groupes d'abonnement e-mail, SMS ou WhatsApp.

Le bloc **Gérer les abonnements** prend en charge deux cas d'usage principaux :

- **[Gérer les abonnements existants](#update-existing-subscriptions) :** Partagez l'[étiquette Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) de la page de destination dans un e-mail, un SMS, un message WhatsApp ou sur un autre canal. Lorsqu'un utilisateur identifié ouvre la page, le bloc pré-remplit automatiquement la case à cocher de chaque groupe d'abonnement avec son état d'abonnement actuel, afin qu'il puisse consulter et mettre à jour ses préférences.
- **[Capturer de nouveaux abonnements](#capture-new-subscribers) :** Ajoutez le bloc à une page de destination de génération de prospects, accompagné d'un bloc **Capture d'e-mail** ou **Capture de téléphone**, afin que les nouveaux visiteurs puissent choisir les groupes d'abonnement auxquels s'inscrire lors de l'envoi du formulaire.

{% alert important %}
Chaque bloc **Gérer les abonnements** est dédié à un seul canal : [e-mail]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups), [SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states) ou [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states). Pour collecter les préférences de plusieurs canaux, ajoutez un bloc pour chacun d'entre eux. Pour le consentement RCS, utilisez plutôt un bloc [Capture de téléphone]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).
{% endalert %}

## Prérequis {#prerequisites}

| Exigences | Description |
| --- | --- |
| Groupes d'abonnement e-mail, SMS ou WhatsApp | Au moins un [groupe d'abonnement e-mail]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups), un [groupe d'abonnement SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states) ou un [groupe d'abonnement WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states) pour le canal que vous ajoutez au bloc. Créez des groupes e-mail depuis le tableau de bord ou via les [endpoints de groupes d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups). Les groupes SMS sont provisionnés lors de la [configuration SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#enable-subscription-groups). Les groupes WhatsApp sont créés lorsque vous [intégrez WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) à votre espace de travail. |
| Autorisations pour les pages de destination | Les mêmes [autorisations]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites) requises pour créer et modifier toute page de destination. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Étape 1 : Ajouter le bloc Gérer les abonnements {#step-1-add-the-manage-subscriptions-block}

Dans l'éditeur de page de destination par glisser-déposer, accédez à la section **Créer** et sélectionnez **Blocs de formulaire**. Faites glisser **Gérer les abonnements** dans une ligne de votre page ; il s'ajuste automatiquement à la largeur de la colonne.

Le bloc est vide tant que vous n'y avez pas ajouté de groupes d'abonnement. Pour afficher les groupes de plusieurs canaux, ajoutez un bloc **Gérer les abonnements** pour chaque canal.

## Étape 2 : Sélectionner le canal et les groupes d'abonnement {#step-2-select-the-channel-and-subscription-groups}

Avec le bloc **Manage Subscriptions** sélectionné, cliquez sur **+ Add subscription groups** dans le panneau **Block properties** à droite. La fenêtre modale **Add subscription groups** s'ouvre.

1. Dans **Select channel**, choisissez **Email**, **SMS** ou **WhatsApp**. Chaque bloc prend en charge un seul canal. Si un canal possède déjà un bloc **Manage Subscriptions** sur la page, la carte correspondante est désactivée et porte le libellé **Added**.
2. Dans **Select subscription groups**, sélectionnez les groupes à inclure. L'intitulé de la liste correspond au canal (**Email subscription groups**, **SMS subscription groups** ou **WhatsApp subscription groups**).
3. Sélectionnez **Add selected**.

Chaque groupe d'abonnement apparaît sous la forme d'une case à cocher sélectionnable sur la page de destination.

Si vous sélectionnez **SMS** et que votre espace de travail ne dispose pas encore de groupes d'abonnement SMS, la fenêtre modale affiche **No SMS subscription groups yet**. Effectuez la [configuration du groupe d'abonnement SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states), puis revenez au bloc.

Si vous sélectionnez **WhatsApp** et que votre espace de travail ne dispose pas encore de groupes d'abonnement WhatsApp, la fenêtre modale affiche **No WhatsApp subscription groups yet**. Effectuez la [configuration du groupe d'abonnement WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states), puis revenez au bloc.

{% alert note %}
Le bloc **Manage Subscriptions** n'affiche que les groupes que vous ajoutez explicitement. Ajouter un groupe d'abonnement au bloc n'abonne pas automatiquement les visiteurs à celui-ci : un visiteur doit cocher la case du groupe et soumettre le formulaire.
{% endalert %}

## Étape 3 : Configurer les paramètres du bloc {#step-3-configure-the-block-settings}

Utilisez le panneau **Propriétés du bloc** pour ajuster le comportement et l'apparence du bloc.

### Groupes d'abonnement {#subscription-groups}

- **Réorganiser les groupes :** Faites glisser un groupe d'abonnement par sa poignée pour modifier l'ordre dans lequel il apparaît dans le bloc.
- **Ajouter ou supprimer des groupes :** Sélectionnez **+ Ajouter des groupes d'abonnement** pour inclure davantage de groupes, ou sélectionnez l'icône de suppression à côté d'un groupe pour le retirer du bloc.

### Inclure les descriptions {#include-descriptions}

Activez **Inclure les descriptions** pour afficher le texte de description de chaque groupe d'abonnement à côté de son nom, offrant ainsi aux visiteurs plus de contexte sur ce à quoi ils s'abonnent. Les groupes e-mail peuvent inclure une description dans la gestion des abonnements. Les groupes SMS et WhatsApp de ce bloc n'affichent pas de texte de description.

### Case à cocher « S'abonner à tout » {#subscribe-to-all-checkbox}

Activez le paramètre **Case à cocher « S'abonner à tout »** pour ajouter une case à cocher supplémentaire au bloc. Lorsqu'un visiteur la sélectionne, toutes les cases à cocher des groupes d'abonnement du bloc sont cochées, ce qui est pratique pour un abonnement rapide à tous les groupes répertoriés.

## Mettre à jour les abonnements existants {#update-existing-subscriptions}

Pour permettre aux utilisateurs existants de consulter et de mettre à jour leurs abonnements e-mail, SMS ou WhatsApp, partagez la page de destination en utilisant son [étiquette Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) dans un e-mail, un SMS, un WhatsApp, une étape du Canvas ou un autre message. Lorsqu'un utilisateur ouvre la page via ce lien, Braze l'identifie et pré-remplit automatiquement chaque case à cocher de groupe d'abonnement dans le bloc **Manage Subscriptions** pour correspondre à son état d'abonnement actuel, de manière similaire à un [centre de préférences e-mail]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

L'utilisateur peut cocher ou décocher les cases pour mettre à jour ses abonnements, puis soumettre le formulaire pour enregistrer ses modifications.

{% alert note %}
Le pré-remplissage de l'état d'abonnement actuel d'un utilisateur dans le bloc **Manage Subscriptions** est inclus par défaut et ne nécessite pas le [niveau Landing Pages Pro]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers). Cela diffère du [pré-remplissage basé sur Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#pre-fill-form-fields) pour les autres champs de formulaire, qui nécessite Landing Pages Pro.
{% endalert %}

## Capturer de nouveaux abonnés {#capture-new-subscribers}

Pour collecter de nouveaux abonnés, associez le bloc **Manage Subscriptions** à un champ de capture pour ce canal :

- **E-mail :** Ajoutez un bloc [Email Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) afin que la page capture l'adresse e-mail du visiteur en même temps que ses sélections de groupes d'abonnement e-mail.
- **SMS ou WhatsApp :** Ajoutez un bloc [Phone Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) afin que la page capture le numéro de téléphone du visiteur en même temps que ses sélections de groupes d'abonnement SMS ou WhatsApp.

Si le visiteur n'est pas identifié (par exemple, s'il arrive sans étiquette Liquid de page de destination), les cases à cocher commencent désélectionnées. Lorsqu'il soumet le formulaire, il est abonné aux groupes d'abonnement qu'il a sélectionnés.

## Ce qu'il faut savoir {#things-to-know}

- **Un canal par bloc :** vous pouvez ajouter un bloc **Manage Subscriptions** par canal sur une page (un pour l'e-mail, un pour le SMS et un pour WhatsApp).
- **RCS :** ce bloc ne répertorie pas les subscription groups RCS. Pour recueillir le consentement pour le RCS, utilisez un bloc [Phone Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).
- **Expérience de confirmation :** les pages de destination avec des blocs de formulaire, y compris **Manage Subscriptions**, nécessitent une expérience de confirmation après la soumission. [Créez une page de confirmation]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional) et reliez-la à votre bouton **Submit**.
- **Référence des blocs éditeur :** pour une référence complète de chaque bloc de page de destination et de ses propriétés, consultez [Blocs éditeur (pages de destination)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).