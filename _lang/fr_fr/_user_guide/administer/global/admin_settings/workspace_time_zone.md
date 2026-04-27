---
nav_title: "Fuseaux horaires de l'espace de travail"
article_title: "Fuseaux horaires de l'espace de travail pour l'envoi de messages"
alias: /workspace_time_zones/
page_order: 3
description: "Cet article de référence explique comment configurer différents fuseaux horaires pour vos espaces de travail Braze, ce qui permet aux équipes opérant dans différentes localisations géographiques de mieux contrôler la planification des campagnes et des Canvas."
---

# Fuseaux horaires de l'espace de travail pour l'envoi de messages

> Les fuseaux horaires des espaces de travail permettent aux administrateurs de définir des fuseaux horaires spécifiques pour chaque espace de travail. Cela permet aux campagnes planifiées et aux Canvas (qui n'utilisent pas l'heure locale ou le timing intelligent) d'être envoyés selon le fuseau horaire désigné de l'espace de travail, plutôt que selon le fuseau horaire global de l'entreprise.

{% multi_lang_include early_access_beta_alert.md feature='Workspace time zones' %}

Par défaut, un nouvel espace de travail hérite du fuseau horaire défini pour votre entreprise. Les administrateurs peuvent remplacer cette valeur par défaut pour un ou plusieurs espaces de travail en utilisant les fuseaux horaires des espaces de travail. Lorsque le fuseau horaire d'un espace de travail est défini, les campagnes planifiées et les Canvas au sein de cet espace de travail se réfèrent à ce nouveau fuseau horaire pour leurs heures d'envoi.

Par exemple, si le fuseau horaire d'un espace de travail est défini sur PST et qu'une campagne dans cet espace de travail est planifiée pour être envoyée à 15 h PST, elle sera livrée à 15 h PST. Cela s'applique même si le fuseau horaire global de votre entreprise est différent (par exemple, EST, où 15 h PST correspond à 18 h EST).

## Gestion des fuseaux horaires de l'espace de travail

Si vous êtes administrateur, vous pouvez accéder aux fuseaux horaires des espaces de travail et les gérer en allant dans **Paramètres** > **Paramètres d'administration** > **Fuseaux horaires de l'espace de travail**.

Ici, vous pouvez consulter la liste de tous vos espaces de travail, leur fuseau horaire défini et la dernière modification du fuseau horaire. Utilisez la barre de recherche pour trouver des espaces de travail spécifiques par nom.

![Page « Fuseaux horaires de l'espace de travail » avec une liste d'espaces de travail, leurs fuseaux horaires respectifs et la date de dernière modification des fuseaux horaires.]({% image_buster /assets/img/workspaces/time_zones/workspace_time_zones_page.png %})

### Définir un fuseau horaire

{% alert note %}
La prise en compte des mises à jour de fuseau horaire peut prendre quelques minutes.
{% endalert %}

{% tabs %}
{% tab Espace de travail unique %}
1. Localisez l'espace de travail souhaité dans la liste.
2. Sélectionnez l'icône **Modifier** à côté du nom de l'espace de travail.

![Bouton « Modifier » à côté du nom d'un espace de travail.]({% image_buster /assets/img/workspaces/time_zones/single_edit_icon.png %})

{: start="3"}
3. Dans le menu déroulant, sélectionnez le fuseau horaire souhaité pour cet espace de travail.
4. Sélectionnez **Enregistrer**.

![Menu déroulant avec le fuseau horaire GMT sélectionné.]({% image_buster /assets/img/workspaces/time_zones/edit_single_workspace.png %})
{% endtab %}
{% tab Plusieurs espaces de travail %}

Vous pouvez appliquer un fuseau horaire spécifique à plusieurs espaces de travail en même temps en procédant comme suit :

1. Cochez les cases à côté de tous les espaces de travail que vous souhaitez mettre à jour.
2. Sélectionnez **Modifier le fuseau horaire**.
3. Dans le menu déroulant, sélectionnez un fuseau horaire à appliquer à tous les espaces de travail sélectionnés.

![Page « Fuseaux horaires de l'espace de travail » avec plusieurs espaces de travail sélectionnés et un bouton « Modifier le fuseau horaire ».]({% image_buster /assets/img/workspaces/time_zones/bulk_edit_workspace_time_zone.png %})

{: start="4"}
4. Sélectionnez **Enregistrer**.

{% endtab %}
{% endtabs %}

## Impact sur les campagnes et les Canvas

{% alert important %}
Informez les équipes et les parties prenantes concernées au sein de chaque espace de travail de tout changement de fuseau horaire afin d'éviter toute confusion sur les planifications de campagnes.
{% endalert %}

- **Campagnes en heure locale et timing intelligent :** les campagnes et les Canvas qui utilisent l'heure locale de l'utilisateur ou le [timing intelligent]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery/#option-3-intelligent-timing) pour la distribution continueront de fonctionner comme avant et ne seront pas affectés par les fuseaux horaires des espaces de travail.
- **Campagnes et Canvas planifiés :** toute campagne ou tout Canvas planifié qui n'utilise pas l'heure locale de l'utilisateur ou le timing intelligent pour la distribution sera désormais envoyé en fonction du fuseau horaire sélectionné pour l'espace de travail.
- **Campagnes planifiées avant un changement de fuseau horaire :** si vous avez planifié une campagne ou un Canvas avant de modifier le fuseau horaire de l'espace de travail, Braze conserve l'heure d'envoi d'origine et ne la replanifie pas. Par exemple, si une campagne est configurée pour être envoyée à 19 h PST et que le fuseau horaire de l'espace de travail est modifié en EST, la campagne sera toujours envoyée à 19 h PST (ce qui correspond désormais à 22 h EST). Le système continuera de se référer à l'heure d'origine, mais l'interprétera selon le nouveau fuseau horaire de l'espace de travail.

## Impact sur les filtres d'audience basés sur la date

Lorsqu'un fuseau horaire d'espace de travail est mis à jour, les filtres d'audience qui utilisent des critères basés uniquement sur la date (sans heure spécifique) sont réévalués en fonction des limites du nouveau fuseau horaire.

Pour les filtres tels que « A effectué l'événement personnalisé X pour la dernière fois après », Braze utilise le fuseau horaire de l'espace de travail pour déterminer le début et la fin de la journée calendaire. La modification de ce paramètre déplace le point de coupure de 23 h 59 pour cette date spécifique.

### Exemple

Un espace de travail met à jour son fuseau horaire de l'heure de l'Est (EST) à l'heure du Pacifique (PST).

- **Heure de coupure précédente :** 23 h 59 EST
- **Nouvelle heure de coupure :** 23 h 59 PST (soit 2 h 59 EST le jour suivant)

Suite à ce changement, un utilisateur qui effectue l'événement personnalisé à 22 h PST le 6 mars 2026 (soit 1 h EST le 7 mars 2026) est désormais inclus dans l'audience, car il se situe dans les limites du jour calendaire PST pour cette date.

## Écarts dans les rapports

Les fuseaux horaires des espaces de travail offrent un contrôle précis sur l'envoi des campagnes, mais vous devez être conscient des écarts potentiels dans les rapports tant que cette fonctionnalité est en accès anticipé. Recoupez les points de données et tenez compte du fuseau horaire lors de l'analyse des rapports pour les espaces de travail avec des remplacements de fuseau horaire spécifiques.