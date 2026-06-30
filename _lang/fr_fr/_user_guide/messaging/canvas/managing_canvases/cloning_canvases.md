---
nav_title: Cloner des Canvas
article_title: Cloner des Canvas
page_order: 3
alias: "/cloning_canvases/"
description: "Cet article de référence décrit comment cloner un Canvas de l'éditeur Canvas d'origine vers le workflow Canvas Flow."
tool: Canvas
---

# Cloner des Canvas vers Canvas Flow {#clone-canvases-to-canvas-flow}

> Si vous disposez d'un Canvas existant créé dans l'éditeur d'origine, vous pouvez le cloner pour en créer une copie dans Canvas Flow. En passant au workflow Canvas actuel, vous accédez à des [composants Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components) légers, aux [propriétés d'entrée persistantes]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#canvas-entry-properties) et à l'[édition post-lancement]({{site.baseurl}}/post-launch_edits). Votre Canvas d'origine ne sera ni modifié ni supprimé.

{% alert important %}
Vous ne pouvez plus créer ni dupliquer de Canvas à l'aide de l'expérience Canvas d'origine. Braze recommande aux utilisateurs de l'expérience Canvas d'origine de passer à Canvas Flow, l'expérience Canvas actuelle.
{% endalert %}

Pour cloner votre Canvas, procédez comme suit :

1. Accédez au tableau de bord Canvas.
2. Identifiez le Canvas dont vous souhaitez créer une copie dans le workflow Canvas Flow. Vous pouvez cloner des Canvas ayant l'état **Brouillon**, **Actif** ou **Arrêté**.
3. Cliquez sur <i class="fas fa-ellipsis-vertical"></i> **Plus d'actions** et sélectionnez **Cloner vers Canvas Flow**.

![Diagramme de flux du processus décrit.]({% image_buster /assets/img_archive/clone_to_v2_workflow.png %}){: style="max-width:25%;"}

{: start="4"}
4. Saisissez le nom de votre nouveau Canvas et cliquez sur **Cloner vers Canvas Flow**.

![Exemple de placement d'une fenêtre modale de carte de contenu.]({% image_buster /assets/img_archive/clone_to_v2_modal.png %}){: style="max-width:70%;"}

Vous disposez désormais de deux versions de votre Canvas : le Canvas d'origine et la version Canvas Flow. Votre Canvas d'origine conserve son état initial, et le Canvas cloné a l'état **Brouillon**. Vous pouvez toujours accéder au Canvas d'origine, mais Braze recommande d'utiliser le workflow Canvas Flow pour continuer à créer vos Canvas.

Auparavant, certains Canvas comportant des embranchements ne pouvaient pas être clonés. Désormais, vous pouvez cloner des Canvas avec des embranchements. Notez que le clonage de Canvas avec des embranchements peut entraîner des étapes déconnectées. Résolvez ces étapes déconnectées (c'est-à-dire les étapes qui ne sont reliées à aucune étape précédente) pour vous assurer que le parcours de votre Canvas est correctement configuré.

{% alert note %}
Si vous clonez un Canvas actif, Braze continuera d'envoyer les utilisateurs à travers le Canvas d'origine. Nous vous recommandons d'arrêter un Canvas avant de le cloner afin d'éviter d'envoyer des messages en double aux utilisateurs depuis les deux Canvas.
{% endalert %}

![Tableau de bord Canvas avec deux Canvas listés : Copie V2 de Canvas V1 et Canvas V1. La Copie V2 de Canvas V1 comporte une icône indiquant qu'elle utilise le workflow Canvas Flow.]({% image_buster /assets/img_archive/clone_to_v2_dashboard.png %})

Le clonage de votre Canvas vers le workflow Canvas Flow est terminé. Vous pouvez maintenant continuer à créer vos Canvas dans cette expérience mise à jour !

## Recommandations {#recommendations}

Pour permettre aux utilisateurs existants de poursuivre leur parcours après avoir cloné votre Canvas d'origine vers Canvas Flow, vous pouvez ajouter des filtres à votre Canvas existant afin d'empêcher les nouveaux utilisateurs d'entrer dans le nouveau Canvas.

Si la rééligibilité est désactivée, ajoutez le filtre « Entered Canvas Variation ». Si la rééligibilité est activée, voici les méthodes possibles pour vous assurer que les utilisateurs n'entrent pas deux fois dans le même Canvas :
- Mettez à jour le Canvas existant pour y inclure une étiquette unique. Pour le nouveau Canvas, ajoutez un filtre « Last Received Message from Campaign or Canvas with Tag ». Cela empêche les utilisateurs d'entrer dans le Canvas une seconde fois après une date d'entrée spécifique (nombre total de jours après l'envoi du dernier message du Canvas d'origine, plus la fenêtre de conversion).
- **La méthode suivante consommera des points de donnée.** Mettez à jour le Canvas d'origine pour y inclure un webhook Braze-à-Braze qui déclenche un horodatage d'attribut personnalisé lors de l'entrée. Cet attribut peut ensuite être utilisé pour empêcher les utilisateurs d'entrer dans le nouveau Canvas après la date spécifiée (nombre total de jours après l'envoi du dernier message du Canvas d'origine, plus la fenêtre de conversion).

Pour les Canvas déclenchés par API, coordonnez-vous avec votre équipe technique pour vous assurer que ces Canvas utilisent le nouvel ID de Canvas lorsque les nouveaux Canvas sont prêts à être lancés.

Pour en savoir plus sur les différences entre l'éditeur Canvas d'origine et l'expérience Canvas Flow, consultez la [FAQ Canvas]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor).