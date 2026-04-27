Vous pouvez utiliser ce modèle pour créer n'importe quelle page ou section de la documentation Braze. Pour la configuration de l'environnement, les prévisualisations et les types de contenu, les contributeurs ayant accès au dépôt doivent suivre le guide disponible sous `docs/contributing/` (par exemple `generating_a_preview.md` et `content_types.md`). Tous les autres peuvent utiliser [Documentation feedback]({{site.baseurl}}/feedback/) pour contacter l'équipe de documentation.

{% details Afficher le modèle %}
{% raw %}
`````markdown
---
nav_title: NAV_TITLE
article_title: ARTICLE_TITLE
description: "SHORT_DESCRIPTION."
alias: /OPTIONAL_SHORT_ARTICLE_TITLE/
page_type: reference
layout: OPTIONAL_LAYOUT_FILE
---

<!-- Le titre de votre page, utilisé pour afficher le titre dans la page. -->
# ARTICLE_TITLE

<!-- L'aperçu commence par un caractère '>' et décrit ce qui sera abordé. Dans un paragraphe suivant facultatif, contextualisez le sujet à un niveau général dans une introduction. -->
> DESCRIPTION.

INTRODUCTION.

<!-- Les conditions préalables pour cette tâche. Si aucune condition préalable n'est requise, vous pouvez supprimer cette section. -->
## Conditions préalables

Avant de commencer, vous devez effectuer les actions suivantes :

- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE

<!-- Une explication facultative et brève du fonctionnement de la fonctionnalité. -->
## Fonctionnement

CONTENU.

<!-- Guidez l'utilisateur dans l'intégration et l'activation de la fonctionnalité. -->
 ## Intégration
CONTENU.

<!-- Un guide pratique avec des étapes imbriquées. -->
## TASK_TO_COMPLETE

<!-- Aperçu facultatif de la tâche. -->
CONTENU.

<!-- En-tête orienté action qui décrit l'objectif de l'étape. -->
### Étape 1 : ACTION_TO_COMPLETE

<!-- Utilisez des puces numérotées ou des paragraphes pour décrire comment effectuer cette action. -->
CONTENU.

### Étape 2 : ACTION_TO_COMPLETE

CONTENU.
<!-- Références facultatives, telles que les types de données pris en charge, les champs, les définitions et autres éléments similaires. -->
### REFERENCE_TO_ASSIST_WITH_ACTION

CONTENU.

<!-- Pour les étapes facultatives, ajoutez « (facultatif) » à la fin de l'en-tête. -->
### Étape 3 : OPTIONAL_ACTION_TO_COMPLETE (facultatif)

CONTENU.
<!-- Une section facultative pour ce qui est pris en charge. Ajoutez des en-têtes imbriqués pour plus de précision. -->
## Types de données pris en charge / Attributs pris en charge / Événements pris en charge / ETC. pris en charge
CONTENU.
<!-- Une section facultative avec des considérations importantes que les utilisateurs doivent examiner avant d'utiliser la fonctionnalité. -->
## Considérations

CONTENU.

<!-- Une section facultative guidant les utilisateurs dans la résolution des problèmes courants. -->
## Résolution des problèmes

### ISSUE_TO_TROUBLESHOOT
CONTENU.

`````
{% endraw %}
{% enddetails %}