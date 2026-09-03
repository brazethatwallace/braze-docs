---
nav_title: Fuseaux horaires de l'espace de travail
article_title: Fuseaux horaires de l'espace de travail
alias: /workspace_time_zones/
page_order: 3
description: "Cet article de référence explique comment configurer différents fuseaux horaires pour vos espaces de travail Braze, ce qui permet aux équipes opérant dans différentes localisations géographiques de mieux contrôler la planification des Campaigns et des Canvas."
toc_headers: h2
---

# Fuseaux horaires de l'espace de travail {#workspace-time-zones}

> Les fuseaux horaires des espaces de travail permettent aux administrateurs de définir des fuseaux horaires spécifiques pour chaque espace de travail. Cela permet aux Campaigns planifiées et aux Canvas (qui n'utilisent pas l'heure locale ou le timing intelligent) d'être envoyés selon le fuseau horaire désigné de l'espace de travail, plutôt que selon le fuseau horaire global de l'entreprise.

{% alert important %}
Les fuseaux horaires des espaces de travail pour l'envoi de messages sont déployés progressivement. Il est possible que ces paramètres ne soient pas encore visibles dans votre tableau de bord.
{% endalert %}

Par défaut, un nouvel espace de travail hérite du fuseau horaire défini pour votre entreprise. Les administrateurs peuvent remplacer cette valeur par défaut pour un ou plusieurs espaces de travail en utilisant les fuseaux horaires des espaces de travail. Lorsqu'un fuseau horaire d'espace de travail est défini, les Campaigns planifiées et les Canvas au sein de cet espace de travail se réfèrent à ce nouveau fuseau horaire pour leurs heures d'envoi.

Par exemple, si le fuseau horaire d'un espace de travail est défini sur PST et qu'une Campaign dans cet espace de travail est planifiée pour être envoyée à 15 h PST, elle sera livrée à 15 h PST. Cela s'applique même si le fuseau horaire global de votre entreprise est différent (par exemple, EST, où 15 h PST correspond à 18 h EST).

## Gérer les fuseaux horaires des espaces de travail {#manage-workspace-time-zones}

Si vous êtes administrateur, vous pouvez accéder aux fuseaux horaires des espaces de travail et les gérer en accédant à **Paramètres** > **Paramètres d'administration** > **Fuseaux horaires des espaces de travail**.

Ici, vous pouvez consulter la liste de tous vos espaces de travail, leur fuseau horaire défini et la dernière modification du fuseau horaire. Utilisez la barre de recherche pour trouver des espaces de travail spécifiques par nom.

### Définir un fuseau horaire {#setting-a-time-zone}

{% alert note %}
La prise en compte des mises à jour de fuseau horaire peut prendre quelques minutes.
{% endalert %}

{% tabs %}
{% tab Espace de travail unique %}
1. Localisez l'espace de travail souhaité dans la liste.
2. Sélectionnez l'icône **Modifier** à côté du nom de l'espace de travail.

![Page « Fuseaux horaires des espaces de travail » avec l'icône « Modifier » à côté du nom d'un espace de travail.]({% image_buster /assets/img/workspaces/time_zones/single_edit_icon.png %})

{: start="3"}
3. Dans le menu déroulant, sélectionnez le fuseau horaire souhaité pour cet espace de travail.
4. Sélectionnez **Enregistrer**.

{% endtab %}
{% tab Plusieurs espaces de travail %}

Vous pouvez appliquer un fuseau horaire spécifique à plusieurs espaces de travail en même temps en procédant comme suit :

1. Cochez les cases à côté de tous les espaces de travail que vous souhaitez mettre à jour.
2. Sélectionnez **Modifier le fuseau horaire**.
3. Dans le menu déroulant, sélectionnez un fuseau horaire à appliquer à tous les espaces de travail sélectionnés.

![Page « Fuseaux horaires des espaces de travail » avec plusieurs espaces de travail sélectionnés et le menu déroulant « Modifier le fuseau horaire » ouvert.]({% image_buster /assets/img/workspaces/time_zones/bulk_edit_workspace_time_zone.png %})

{: start="4"}
4. Sélectionnez **Enregistrer**.

{% endtab %}
{% endtabs %}

## Impact sur les Campaigns et les Canvas {#impact-on-campaigns-and-canvases}

{% alert important %}
Informez les équipes et les parties prenantes concernées au sein de chaque espace de travail de tout changement de fuseau horaire afin d'éviter toute confusion concernant les planifications de Campaigns.
{% endalert %}

- **Campaigns et Canvas avec heure locale et timing intelligent :** Les Campaigns et les Canvas qui utilisent l'heure locale de l'utilisateur ou le [timing intelligent]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#option-3-intelligent-timing) pour la distribution continuent de fonctionner comme avant et ne sont pas affectés par les fuseaux horaires de l'espace de travail.
- **Campaigns et Canvas planifiés :** Toute Campaign ou tout Canvas planifié qui n'utilise pas l'heure locale de l'utilisateur ni le timing intelligent pour la distribution envoie les messages en fonction du fuseau horaire sélectionné pour l'espace de travail.
- **Campaigns planifiées avant un changement de fuseau horaire :** Si vous avez planifié une Campaign ou un Canvas avant de modifier le fuseau horaire de l'espace de travail, Braze conserve l'heure d'envoi d'origine et ne la replanifie pas. Par exemple, si une Campaign est configurée pour être envoyée à 19 h PST et que le fuseau horaire de l'espace de travail est modifié en EST, la Campaign est toujours envoyée à 19 h PST (ce qui correspond désormais à 22 h EST). Le système continue de référencer l'heure d'origine, mais l'interprète selon le nouveau fuseau horaire de l'espace de travail.

## Impact sur les filtres d'audience basés sur les dates {#impact-on-date-based-audience-filters}

Lorsque le fuseau horaire d'un espace de travail est mis à jour, les filtres d'audience qui utilisent des critères basés uniquement sur la date (sans heure spécifique) sont réévalués en fonction des limites du nouveau fuseau horaire.

Pour les filtres tels que « A effectué l'événement personnalisé X pour la dernière fois après », Braze utilise le fuseau horaire de l'espace de travail pour déterminer le début et la fin de la journée calendaire. La modification de ce paramètre décale le point de coupure de 23 h 59 pour cette date spécifique.

### Exemple {#example}

Un espace de travail met à jour son fuseau horaire de l'heure de l'Est (EST) à l'heure du Pacifique (PST).

- **Heure de coupure précédente :** 23 h 59 EST
- **Nouvelle heure de coupure :** 23 h 59 PST (soit 2 h 59 EST le jour suivant)

Suite à ce changement, un utilisateur qui effectue l'événement personnalisé à 22 h PST le 6 mars 2026 (soit 1 h EST le 7 mars 2026) est désormais inclus dans l'audience, car il se trouvait dans les limites du jour calendaire PST pour cette date.

## Impact sur les données de performance {#impact-on-performance-data}

La mise à jour du fuseau horaire de votre espace de travail affecte la manière dont les données de performance sont agrégées et affichées dans votre tableau de bord. Étant donné que les analyses de données telles que les *utilisateurs actifs quotidiens* (DAU) s'appuient sur le fuseau horaire de l'espace de travail pour définir le début et la fin d'une journée de 24 heures, une modification de ce paramètre décale ces fenêtres de reporting.

Lorsque vous modifiez le fuseau horaire, vous pouvez constater des fluctuations ou des « décalages » dans vos données historiques. Cela se produit parce que la fenêtre de 00 h 00 à 23 h 59 s'est déplacée par rapport à l'UTC.

Prenons l'exemple suivant pour un espace de travail dont le fuseau horaire passe d'UTC à PST (UTC-8) :

- **Avant le changement :** une « journée » de reporting est mesurée de 00 h 00 UTC à 23 h 59 UTC.
- **Après le changement :** une « journée » de reporting est désormais mesurée de 00 h 00 PST à 23 h 59 PST.

Par conséquent, un événement survenu à 01 h 00 UTC le 1er janvier aurait été comptabilisé dans les statistiques du 1er janvier. Après le passage au PST, ce même événement (survenu à 17 h 00 PST le 31 décembre) serait attribué aux indicateurs de la veille dans le rapport mis à jour.