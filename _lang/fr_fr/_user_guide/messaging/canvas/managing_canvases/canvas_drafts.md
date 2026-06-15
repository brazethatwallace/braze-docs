---
nav_title: Enregistrer des brouillons pour Canvas
article_title: Enregistrer des brouillons pour Canvas
alias: "/save_as_draft/"
page_order: 1
description: "Cet article de référence explique comment enregistrer un brouillon pour un Canvas déjà lancé."
page_type: reference
tool: Canvas
---

# Enregistrer des brouillons pour Canvas

> Lorsque vous créez et lancez des Canvas, vous pouvez modifier un Canvas actif et l'enregistrer en tant que brouillon, ce qui vous permet de tester vos modifications avant un nouveau lancement.

Si vous avez un Canvas actif nécessitant des modifications à grande échelle, vous pouvez utiliser cette fonctionnalité pour créer, enregistrer et vérifier la qualité de vos changements **avant** de les lancer dans le Canvas actif.

Comme pour tout Canvas, un seul utilisateur peut modifier un brouillon à la fois, et un Canvas ne peut avoir qu'un seul brouillon à la fois. Ces brouillons ne disposent d'aucune analyse, car les modifications du brouillon n'ont pas encore été lancées.

![Un exemple de brouillon de Canvas avec une bannière indiquant à l'utilisateur qu'il modifie un brouillon de Canvas, avec une option pour afficher le Canvas actif. Le pied de page propose des options pour revenir à la vue analytique, enregistrer en tant que brouillon ou lancer le brouillon.]({% image_buster /assets/img_archive/canvas_draft1.png %})

## Créer un brouillon

Pour créer un brouillon :

1. Accédez à un Canvas actif.
2. Sélectionnez le bouton **Enregistrer en tant que brouillon** dans le pied de page du Canvas.

Notez que les modifications du Canvas actif ne peuvent pas être effectuées tant qu'un brouillon du Canvas existe. Vous pouvez mettre à jour le Canvas pour appliquer les modifications ou supprimer le brouillon.

## Consulter le brouillon actif

Pour consulter le Canvas actif, sélectionnez **Afficher le Canvas actif** dans le pied de page depuis la vue analytique ou dans l'en-tête du Canvas depuis le brouillon. Pour revenir à un Canvas actif, sélectionnez **Modifier le brouillon** depuis la vue analytique ou la vue du Canvas actif.

Vous ne pouvez référencer que les étapes qui ont déjà été lancées avant la création du brouillon. Cela signifie que si vous avez créé une étape ou un canal **après** la création du brouillon, il ne pourra pas être référencé dans votre brouillon.

{% alert note %}
Si un bloc de contenu est référencé dans un brouillon de Canvas, le Canvas est comptabilisé dans le nombre d'inclusions du bloc de contenu. Cependant, si le bloc de contenu est référencé dans le brouillon d'un Canvas **actif**, le Canvas ne sera pas comptabilisé dans le nombre d'inclusions du bloc de contenu.
{% endalert %}

### Priorisation des messages in-app

Pour les brouillons d'un Canvas actif, la priorité des messages in-app dans le générateur de Canvas est mise à jour immédiatement lorsqu'un utilisateur modifie la priorité. Cela signifie que la priorité des messages in-app au niveau du Canvas est appliquée au Canvas actif immédiatement, même lorsqu'un brouillon existe.

En revanche, les modifications de priorité des messages in-app au niveau des étapes sont enregistrées en tant que brouillon et appliquées lors de la mise à jour du Canvas. Par exemple, dans une étape Message, l'ordre de priorité sera mis à jour lorsqu'un utilisateur lance le brouillon, car les paramètres d'étape s'appliquent au niveau de l'étape.