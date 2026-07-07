---
nav_title: Checklist pré et post-lancement
article_title: Checklist pré et post-lancement
page_order: 2
description: "Cet article fournit des recommandations sur les éléments à vérifier avant et après le lancement d'un Canvas."
tool: Canvas

---

# Checklist pré et post-lancement {#pre-and-post-launch-checklist}

> Cet article fournit des recommandations sur les éléments à vérifier avant et après le lancement d'un Canvas.

## Éléments à vérifier avant le lancement {#things-to-consider-before-launch}

Avant de lancer un Canvas, plusieurs détails méritent d'être vérifiés pour vous assurer que vos messages et vos horaires d'envoi correspondent aux préférences de votre audience. Parmi les points à considérer : les variations de fuseaux horaires, les paramètres d'entrée, et bien d'autres. Utilisez cette checklist comme guide pour affiner ces aspects en fonction de votre cas d'utilisation et contribuer au succès de votre Canvas.

### Vérifier les paramètres de fuseau horaire {#review-time-zone-settings}

Si vous faites entrer les utilisateurs en fonction de leur fuseau horaire local avec une planification d'entrée programmée, vous devez lancer votre Canvas au moins 24 heures avant l'heure à laquelle vous souhaitez que les utilisateurs y entrent. Par exemple, voici un Canvas qui ne laisse pas suffisamment de temps entre le lancement et l'heure d'entrée programmée. Dans ce scénario, certains utilisateurs pourraient ne pas entrer dans votre Canvas car l'heure d'entrée programmée est déjà passée dans certains fuseaux horaires.

{% alert tip %}
Une alerte s'affichera si vous n'avez pas prévu un délai suffisant. Une solution rapide consiste à ajuster l'heure d'envoi pour que les utilisateurs puissent rester dans le segment ciblé pendant 24 heures complètes.
{% endalert %}

![Un Canvas programmé pour faire entrer les utilisateurs à une heure précise, à partir de 10 h le 30 avril 2025, dans leur fuseau horaire local.]({% image_buster /assets/img_archive/canvas_checklist1.png %}){: style="max-width:75%;"}

### Envisager l'utilisation d'expressions régulières pour les filtres d'audience {#consider-using-regular-expressions-for-audience-filters}

Après avoir configuré les détails préliminaires concernant le moment où vos utilisateurs doivent entrer dans un Canvas, il est recommandé de vérifier vos segments ou filtres dans l'étape **Audience cible** de la création du Canvas. Dans cette étape, vous pouvez également consulter le résumé de la **Population cible** pour voir comment votre audience cible a été configurée.

Envisagez ici d'utiliser une expression régulière pour les segments ou filtres dans les étapes de Parcours d'audience, ainsi que pour les paramètres de validation de la réception dans les étapes Message et Arbre décisionnel. Une [expression régulière]({{site.baseurl}}/user_guide/audience/segments/regex) (aussi appelée regex) est une chaîne de caractères qui reconnaît des motifs et prend en compte les caractères, plutôt que des éléments comme la casse. Cela signifie que si vous utilisez « Est égal à / N'est pas égal à », vous pourriez limiter la taille de votre audience à cause de simples erreurs de syntaxe.

Si vous constatez que votre audience cible est plus petite que prévu, essayez d'utiliser « Correspond à l'expression régulière » ou « Ne correspond pas à l'expression régulière » au lieu de « Est égal à » ou « N'est pas égal à ». Cela pourrait inclure les utilisateurs manquants et cibler une audience plus large.

### Identifier les paramètres d'entrée et les conditions de concurrence {#identify-entry-settings-and-race-conditions}

Une condition de concurrence peut survenir lorsque vous utilisez les mêmes critères d'entrée dans vos paramètres de **Planification d'entrée** et d'**Audience cible**.

Si vous utilisez une entrée basée sur une action, vérifiez que vous n'avez pas utilisé la même action de déclenchement ici et dans votre audience cible. Une condition de concurrence peut se produire lorsque l'utilisateur ne fait pas partie de l'audience au moment où il effectue l'événement déclencheur, ce qui l'empêche d'entrer dans le Canvas.

{% alert tip %}
Consultez les [bonnes pratiques]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions#scenario-3-matching-action-based-triggers-and-audience-filters) pour éviter cette condition de concurrence lors de la configuration d'un Canvas basé sur une action avec le même déclencheur que le filtre d'audience.
{% endalert %}

### Vérifier les propriétés d'entrée du Canvas et les propriétés d'événement {#check-canvas-entry-properties-and-event-properties}

Bien que leurs noms soient similaires, les [propriétés d'entrée du Canvas et les propriétés d'événement]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) fonctionnent différemment dans vos workflows Canvas. Les propriétés d'entrée du Canvas sont liées à vos paramètres d'entrée et peuvent être référencées dans n'importe quel composant de message tout au long de votre Canvas. Les propriétés d'entrée du Canvas sont les propriétés de l'événement ou de l'appel API qui déclenche l'entrée d'un utilisateur dans un Canvas, via des paramètres d'entrée basés sur une action ou déclenchés par API.

Les propriétés d'événement, en revanche, ne peuvent être référencées que dans la première étape Message suivant une étape de Parcours d'actions. Les propriétés d'événement sont les propriétés d'un événement personnalisé ou d'un événement d'achat que l'utilisateur a effectué pendant la fenêtre d'évaluation d'une étape de Parcours d'actions, et qui déclenche sa progression le long de l'un des parcours d'action définis.

Vérifiez l'aperçu de votre message pour toutes les étapes Message qui référencent des propriétés d'entrée du Canvas ou des propriétés d'événement.

### Vérifier l'avancement des utilisateurs dans les étapes Message {#review-message-steps-for-user-advancement}

Par défaut, les utilisateurs progressent à travers toutes les étapes Message, qu'ils aient reçu le message ou non. Si vous souhaitez ne faire avancer que les utilisateurs qui ont reçu un message particulier, vous pouvez ajouter une étape Arbre décisionnel directement après votre composant Message. Ajoutez le filtre « A reçu un message de l'étape du Canvas » comme filtre supplémentaire, puis sélectionnez le Canvas et l'étape Message.

Pour les étapes Message contenant des messages in-app, vous pouvez utiliser un composant Parcours d'actions au lieu du composant Arbre décisionnel. Cela vous permettra de faire avancer les utilisateurs selon qu'ils ont vu ou non votre message in-app. Définissez un groupe d'actions en ajoutant le filtre « Interagir avec l'étape » et sélectionnez **Voir le message in-app**. Ensuite, définissez la fenêtre d'évaluation de l'étape sur la fenêtre d'expiration du message in-app.

Pour un composant Message dans un envoi de messages multicanal, nous recommandons ce qui suit :
* Incluez une étape de délai entre vos étapes Message et Arbre décisionnel, et définissez le délai à au moins cinq secondes.
* Si le composant inclut le timing intelligent, définissez le délai à 24 heures.
* Si le composant inclut une limite de débit, divisez vos messages en plusieurs étapes Message monocanal et connectez-les ensemble. Ensuite, connectez l'étape Arbre décisionnel directement après la dernière étape Message pour vérifier si un utilisateur a reçu l'un des messages. Vous pouvez également utiliser cette méthode comme alternative à une étape Message multicanal avec le timing intelligent.

## Éléments à vérifier après le lancement {#things-to-consider-after-launch}

Votre Canvas est lancé ! Et maintenant ? Utilisez cette checklist pour voir comment vérifier et ajuster votre Canvas en cas d'écarts après le lancement, en fonction des scénarios suivants.

### Beaucoup d'entrées, mais peu d'envois {#many-entries-but-few-sends}

Imaginons par exemple que vous avez remarqué un écart entre le nombre de messages envoyés et le total des entrées. Vous pouvez identifier les zones à ajuster dans votre Canvas en vérifiant ces points clés.

#### Audience d'entrée {#entry-audience}

Si vous utilisez une campagne à envoi programmé, vérifiez votre audience cible en examinant votre population cible. Comment se présentent les chiffres par canal, et quel est le rapport avec les canaux que vous avez utilisés dans votre Canvas ? Si les chiffres les plus bas correspondent aux canaux utilisés dans votre Canvas, vous avez peut-être trouvé le problème.

#### Premier composant du Canvas {#first-component-of-the-canvas}

Examinez les filtres d'audience, les déclencheurs d'action ou les segments utilisés dans les premiers composants de votre Canvas. Y a-t-il des fautes de frappe ou des conditions trop restrictives qui empêchent votre Canvas de bien démarrer ? Utilisez-vous « Est égal à » alors que vous devriez utiliser « Correspond à l'expression régulière » ?

#### Groupe de contrôle du Canvas {#canvas-control-group}

Vérifiez la répartition des utilisateurs entre vos variantes et votre groupe de contrôle. Le groupe de contrôle est-il plus important que prévu ? Si c'est le cas, vous pouvez modifier ce paramètre. Si la **Sélection intelligente** est activée et que le groupe de contrôle l'emporte, envisagez d'arrêter votre Canvas et d'essayer une nouvelle approche.

### Une audience totale vide {#an-empty-total-audience}

Si vous ne voyez aucune donnée d'entrée pour votre Canvas, les raisons pour lesquelles les utilisateurs n'entrent pas dans votre Canvas peuvent être liées à des conditions de concurrence et à des filtres de segmentation d'audience trop restrictifs.

Si vous utilisez une entrée basée sur une action dans votre planification d'entrée, vérifiez que vous n'avez pas utilisé la même action de déclenchement ici et dans votre **Audience cible**. Une condition de concurrence peut se produire lorsque l'utilisateur ne fait pas partie de l'audience au moment où il effectue l'événement déclencheur, ce qui l'empêche d'entrer dans le Canvas.

De plus, vérifiez que le segment sélectionné contient des utilisateurs en consultant le tableau **Population cible** dans les paramètres de l'**Audience cible**. Si ce nombre est faible, voyez comment ajuster vos paramètres d'entrée ou examinez vos segments ou filtres sélectionnés pour détecter d'éventuelles erreurs.

### Baisse inattendue entre les étapes {#unexpected-drop-off-between-steps}

Un autre moyen évident d'identifier des zones d'ajustement pour votre Canvas est de constater une forte baisse d'une étape du Canvas à la suivante. Dans ce cas, vérifiez que vos filtres d'audience et événements d'exception ne contiennent pas de fautes de frappe ou d'erreurs de casse. Et comme toujours, assurez-vous que vos filtres d'audience ne sont pas si stricts qu'ils excluent la majorité de vos utilisateurs de l'entrée dans le Canvas.

Ensuite, il est important d'identifier les paramètres qui peuvent affecter le moment et la possibilité d'envoi des messages à vos utilisateurs :
- [Timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)
- [Heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)
- Validations de réception

En général, choisissez soit le timing intelligent, soit les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) pour votre Canvas, mais pas les deux. La même recommandation s'applique : utilisez soit le timing intelligent, soit la [limite de débit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping), mais pas les deux. Pour en savoir plus sur la meilleure façon d'utiliser l'Intelligence Suite, consultez nos [cas d'utilisation de l'Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence_suite#use-cases).

### Volumes d'envoi suspects entre les parcours {#suspicious-send-volumes-between-paths}

Lorsque le volume d'envois entre deux ou plusieurs parcours (Parcours d'audience ou Parcours d'actions) ne correspond pas à vos attentes, c'est l'occasion de vérifier vos segments, filtres ou actions de déclenchement. Assurez-vous également d'identifier et de supprimer tout filtre redondant.