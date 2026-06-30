---
nav_title: Gérer les modèles
article_title: Gérer les modèles
page_order: 1

page_type: reference
description: "Cet article de référence décrit comment dupliquer et archiver des modèles dans la section Modèles du tableau de bord de Braze."
tool:
  - Templates
  - Media

---

# Gérer les modèles {#manage-templates}

> Archiver ou dupliquer des modèles peut aider à mieux les organiser et les gérer. Cet article de référence explique comment archiver et dupliquer des modèles dans la section **Modèles** du tableau de bord de Braze.

## Dupliquer des modèles {#duplicating-templates}

{% tabs %}
{% tab Modèle individuel %}

![Menu déroulant avec l'option de duplication.]({% image_buster /assets/img/template_duplicate_cog.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Pour dupliquer un modèle individuel, sélectionnez <i class="fas fa-ellipsis-v"></i> **Plus d'options** pour le modèle, puis sélectionnez **Dupliquer** dans le menu déroulant.
<br><br>

{% alert note %}
Pour les modèles de [bloc de contenu]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks), un brouillon est créé. Pour tous les autres modèles, une nouvelle copie dupliquée est automatiquement créée.
{% endalert %}

{% endtab %}
{% tab Plusieurs modèles %}

{% raw %}

La duplication de plusieurs modèles s'effectue en cochant la case à côté du nom du modèle. Sélectionnez d'abord les modèles, puis sélectionnez **Dupliquer**.

Les modèles dupliqués peuvent être retrouvés en triant la colonne **Dernière modification**. Par défaut, les nouveaux modèles sont nommés `Copy of ORIGINAL_TEMPLATE_NAME`.

{% endraw %}

![Trois modèles triés par date de dernière modification, avec un modèle copié en haut de la liste.]({% image_buster /assets/img/duplicate_multiple_template.gif %})

{% endtab %}
{% endtabs %}

## Archiver des modèles {#archiving-templates}

![Menu déroulant des paramètres développé affichant trois options : « Archiver », « Dupliquer » et « Copier vers l'espace de travail », avec l'option « Archiver » mise en surbrillance.]({% image_buster /assets/img/template_archive_cog.png %}){: style="float:right;max-width:20%;margin-left:15px;"}

Pour archiver un modèle individuel, sélectionnez <i class="fas fa-ellipsis-v"></i> **Plus d'options** sur l'écran de la grille des modèles et sélectionnez **Archiver**. Lorsqu'un modèle est archivé, notez les différents scénarios suivants :

- Les campagnes actives continuent d'utiliser le modèle archivé sans interruption.
- Les brouillons de campagnes conservent le contenu du modèle archivé et peuvent être modifiés et lancés.
- Pour modifier un modèle archivé, vous devez d'abord le désarchiver. De même, pour utiliser un modèle archivé dans une campagne, vous devez d'abord désarchiver le modèle.

Pour archiver plusieurs modèles, cochez la case à côté de chaque modèle que vous souhaitez archiver. Après avoir sélectionné plusieurs modèles, sélectionnez **Archiver**. Vous pouvez retrouver vos modèles archivés en sélectionnant **Archivé** sous **Afficher** dans la grille des modèles.

![Section des modèles d'e-mail par glisser-déposer enregistrés montrant deux modèles sélectionnés et une barre d'outils avec l'option d'archivage.]({% image_buster /assets/img/archive_multiple_template.png %}){: style="max-width:60%;"}

{% alert important %}
L'archivage n'est actuellement pas disponible pour les [modèles de liens]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing#link-templates).
{% endalert %}