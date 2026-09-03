---
nav_title: Indicateur de fonctionnalité
article_title: Indicateur de fonctionnalité
page_order: 8
page_type: reference
description: "Cet article de référence explique comment les indicateurs de fonctionnalité peuvent être utilisés dans Canvas."
tool: Canvas
local_redirect:
  create-a-feature-flag: '/docs/user_guide/messaging/feature_flags/create_feature_flags'
---

# Indicateur de fonctionnalité {#feature-flag}

> Les indicateurs de fonctionnalité vous permettent d'expérimenter et de confirmer vos hypothèses autour de nouvelles fonctionnalités. Les marketeurs peuvent utiliser les indicateurs de fonctionnalité pour segmenter leur audience dans [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) et suivre l'impact du déploiement d'une fonctionnalité sur les conversions. De plus, les [chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) vous permettent d'optimiser ces conversions en testant différents messages ou chemins les uns par rapport aux autres afin de déterminer lequel est le plus efficace. Utilisez le chemin gagnant à mesure que vous déployez progressivement votre fonctionnalité auprès d'une audience plus large.

Vous souhaitez en savoir plus sur les indicateurs de fonctionnalité et leur utilisation dans Braze ? Consultez nos articles dédiés aux [indicateurs de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags).

## Créer un indicateur de fonctionnalité {#creating-a-feature-flag}

![Exemple d'une étape Indicateur de fonctionnalité pour la fonctionnalité Live Chat Button.]({% image_buster /assets/img/feature_flags/feature_flag_canvas_step.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Pour créer un composant Indicateur de fonctionnalité, commencez par ajouter une étape à votre Canvas. Glissez-déposez le composant depuis la barre latérale, ou cliquez sur le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape et sélectionnez **Indicateur de fonctionnalité**. Ensuite, sélectionnez l'indicateur de fonctionnalité dans le menu déroulant, qui contient tous les indicateurs de fonctionnalité non archivés.

## Fonctionnement de cette étape {#how-this-step-works}

Lorsqu'un Canvas est arrêté, archivé, ou qu'une étape Indicateur de fonctionnalité est supprimée, les utilisateurs qui sont passés par cette étape ne reçoivent plus l'indicateur de fonctionnalité ni ses propriétés.

Pour un indicateur de fonctionnalité sans déploiement ni expérience d'indicateur de fonctionnalité, après l'arrêt d'un Canvas contenant une étape Indicateur de fonctionnalité faisant référence à cet indicateur :

- Aucun utilisateur ne dispose de cet indicateur de fonctionnalité dans l'onglet **Feature Flags Eligibility**.
- Aucun utilisateur ne correspond au filtre de segmentation `Feature Flags` pour cet indicateur de fonctionnalité.

Si l'indicateur de fonctionnalité dispose d'un déploiement, d'une expérience d'indicateur de fonctionnalité ou d'un autre Canvas actif qui y fait référence, les utilisateurs peuvent toujours être éligibles via ces canaux.

Les propriétés d'une étape du Canvas peuvent être modifiées après le lancement, et même après qu'un utilisateur est passé par l'étape. Les utilisateurs reçoivent toujours une version dynamique et en temps réel de l'indicateur de fonctionnalité, plutôt que l'ancienne version précédemment enregistrée.

- **Deux Canvas font référence au même indicateur de fonctionnalité, et un utilisateur entre dans les deux :** l'utilisateur reçoit la valeur définie dans le Canvas dans lequel il est entré le plus récemment, et non dans le Canvas précédent. Cette valeur apparaît dans l'onglet **Feature Flags Eligibility**.
- **Un Canvas comporte deux étapes Indicateur de fonctionnalité faisant référence au même indicateur de fonctionnalité :** l'utilisateur reçoit la valeur définie dans la deuxième étape tant qu'il se trouve sur ce chemin, et cette valeur apparaît dans l'onglet **Feature Flags Eligibility**.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## Écraser les propriétés {#overwriting-properties}

Lorsque vous créez un indicateur de fonctionnalité, vous spécifiez des propriétés par défaut. Lors de la configuration d'une étape Indicateur de fonctionnalité dans Canvas, vous pouvez soit conserver les valeurs par défaut, soit écraser les valeurs pour les utilisateurs qui entrent dans cette étape.

![Un indicateur de fonctionnalité « Preference Center » avec « String » comme propriété, « url » comme clé de propriété et une valeur.]({% image_buster /assets/img/feature_flags/feature_flags_canvas_details.png %}){: style="max-width:90%"}

Accédez à **Messagerie** > **Indicateurs de fonctionnalité** pour modifier, ajouter ou supprimer des propriétés supplémentaires.

## Différences entre Canvas et le déploiement {#canvas-and-rollout-differences}

Canvas et le déploiement d'un indicateur de fonctionnalité (en faisant glisser le curseur) peuvent fonctionner indépendamment l'un de l'autre. Un point important à noter : l'entrée dans une étape du Canvas écrase toute configuration de déploiement par défaut. Cela signifie que si un utilisateur n'est pas éligible à un indicateur de fonctionnalité, une étape du Canvas peut activer la fonctionnalité pour cet utilisateur.

De même, si un utilisateur est éligible au déploiement d'un indicateur de fonctionnalité avec certaines propriétés, et qu'il entre également dans l'étape du Canvas, il recevra les valeurs écrasées de cette étape du Canvas.