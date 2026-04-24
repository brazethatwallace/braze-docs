Vous pouvez utiliser ce modèle pour créer n'importe quelle page ou section de la documentation Braze. Pour la configuration de l'environnement, les prévisualisations et les types de contenu, les contributeurs ayant accès au dépôt doivent suivre le guide disponible sous `docs/contributing/` (par exemple `generating_a_preview.md` et `content_types.md`). Tous les autres peuvent utiliser [Documentation feedback]({{site.baseurl}}/feedback/) pour contacter l'équipe de documentation.

{% details Show template %}
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

<!-- The title of your page, used to render the in-page title. -->
# ARTICLE_TITLE

<!-- The overview starts with a '>' character and discusses what will be covered. In an optional following paragraph, contextualize the topic at a high-level in an introduction. -->
> DESCRIPTION.

INTRODUCTION.

<!-- The prerequisites for this task. If no prerequisites are required, you can remove this section. -->
## Conditions préalables

Avant de commencer, vous devez effectuer les actions suivantes :

- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE

<!-- An optional, brief explanation of how the feature workflow looks. -->
## Fonctionnement

CONTENU.

<!-- Walk a user through integrating and turning on the feature. -->
 ## Intégration
CONTENU.

<!-- A how-to guide with nested steps. -->
## TASK_TO_COMPLETE

<!-- Optional overview of the task. -->
CONTENU.

<!-- Action-oriented header that describes the step's goal. -->
### Étape 1 : ACTION_TO_COMPLETE

<!-- Use number bullets or paragraphs to describe how to complete this action -->
CONTENU.

### Étape 2 : ACTION_TO_COMPLETE

CONTENU.
<!-- Optional references, such as supported data types, fields, definitions, and similar. -->
### REFERENCE_TO_ASSIST_WITH_ACTION

CONTENU.

<!-- For optional steps, add "(optional)" to the end of the header. -->
### Étape 3 : OPTIONAL_ACTION_TO_COMPLETE (facultatif)

CONTENU.
<!-- An optional section for what is supported. Add nested headers to be more specific. -->
## Types de données pris en charge / Attributs pris en charge / Événements pris en charge / ETC. pris en charge
CONTENU.
<!-- An optional section with important considerations for users to review before using the feature. -->
## Considérations

CONTENU.

<!-- An optional section guiding users through troubleshooting common issues. -->
## Résolution des problèmes

### ISSUE_TO_TROUBLESHOOT
CONTENU.

`````
{% endraw %}
{% enddetails %}