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

Avant de lancer un Canvas, vous pouvez vérifier plusieurs détails pour vous assurer que vos messages et vos heures d'envoi correspondent aux préférences de votre audience. Les éléments à prendre en compte incluent les variations de fuseaux horaires, les paramètres d'entrée, et bien d'autres. Utilisez cette liste de vérification comme guide pour affiner ces aspects en fonction de votre cas d'usage et contribuer au succès de votre Canvas.

### Vérifier les paramètres de fuseau horaire {#review-time-zone-settings}

Si vous faites entrer les utilisateurs en fonction de leur fuseau horaire local à l'aide d'une planification d'entrée programmée, vous devez lancer votre Canvas au moins 24 heures avant le moment où vous souhaitez que les utilisateurs y entrent. Par exemple, voici un Canvas qui n'a pas laissé suffisamment de temps entre le lancement et l'heure d'entrée programmée. Dans ce scénario, certains utilisateurs pourraient ne pas entrer dans votre Canvas car l'heure d'entrée programmée est déjà passée dans certains fuseaux horaires.

{% alert tip %}
Vous verrez une alerte si vous n'avez pas programmé un délai suffisant. Une solution rapide consiste à ajuster l'heure d'envoi pour garantir que les utilisateurs puissent rester dans le segment ciblé pendant 24 heures complètes.
{% endalert %}

![Un Canvas programmé pour faire entrer les utilisateurs à une heure donnée à partir de 10 h le 30 avril 2025, dans leur fuseau horaire local.]({% image_buster /assets/img_archive/canvas_checklist1.png %}){: style="max-width:75%;"}

### Envisager l'utilisation d'expressions régulières pour les filtres d'audience {#consider-using-regular-expressions-for-audience-filters}

Après avoir configuré les détails préliminaires du moment où vos utilisateurs doivent entrer dans un Canvas, il est recommandé de vérifier vos segments ou filtres dans l'étape **Target Audience** de la création d'un Canvas. Dans cette étape, vous pouvez également consulter le résumé **Target Population** pour voir comment votre audience cible a été configurée.

Ici, envisagez d'utiliser une expression régulière pour les segments ou filtres dans les étapes de parcours d'audience, ainsi que pour les paramètres de validation de distribution dans les étapes Message et arbre décisionnel. Une [expression régulière]({{site.baseurl}}/user_guide/audience/segments/regex) (également appelée regex) est une chaîne de caractères, ce qui signifie qu'elle reconnaît des motifs et prend en compte les caractères, plutôt que des éléments comme la casse. Cela signifie que si vous utilisez « Equals / Does Not Equal », vous pourriez limiter la taille de votre audience en raison de simples erreurs de syntaxe.

Si vous remarquez que votre audience cible est plus petite que prévu, essayez d'utiliser « Matches Regex » ou « Does Not Match Regex » au lieu de « Equals » ou « Does Not Equal ». Cela peut prendre en compte les utilisateurs manquants et cibler une audience plus large.

### Identifier les paramètres d'entrée et les conditions de concurrence {#identify-entry-settings-and-race-conditions}

Une condition de concurrence peut se produire lorsque vous avez utilisé les mêmes critères d'entrée dans vos paramètres **Entry Schedule** et **Target Audience**.

Si vous utilisez une entrée basée sur une action, vérifiez que vous n'avez pas utilisé la même action de déclenchement ici que dans votre audience cible. Une condition de concurrence peut se produire lorsque l'utilisateur ne fait pas partie de l'audience au moment où il effectue l'événement déclencheur, ce qui signifie qu'il n'entrera pas dans le Canvas.

{% alert tip %}
Consultez les [bonnes pratiques]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions#scenario-3-matching-action-based-triggers-and-audience-filters) pour éviter cette condition de concurrence lors de la configuration d'un Canvas basé sur une action avec le même déclencheur que le filtre d'audience.
{% endalert %}

### Vérifier les propriétés d'entrée Canvas et les propriétés d'événement {#check-canvas-entry-properties-and-event-properties}

Bien que leurs noms soient similaires, les [propriétés d'entrée Canvas et les propriétés d'événement]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) fonctionnent différemment au sein de vos flux Canvas. Les propriétés d'entrée Canvas sont liées à vos paramètres d'entrée et peuvent être référencées dans n'importe quel composant de message tout au long de votre Canvas. Les propriétés d'entrée Canvas sont les propriétés de l'événement ou de l'appel API qui déclenche l'entrée d'un utilisateur dans un Canvas, en utilisant des paramètres d'entrée basés sur une action ou déclenchés par API.

Les propriétés d'événement, quant à elles, ne peuvent être référencées que dans la première étape Message suivant une étape de parcours d'action. Les propriétés d'événement sont les propriétés d'un événement personnalisé ou d'un événement d'achat que l'utilisateur a effectué pendant la fenêtre d'évaluation d'une étape de parcours d'action, et qui déclenche sa progression le long de l'un des parcours d'action définis.

Vérifiez l'aperçu de votre message pour toutes les étapes Message référençant des propriétés d'entrée Canvas ou des propriétés d'événement.

### Vérifier l'avancement des utilisateurs dans les étapes Message {#review-message-steps-for-user-advancement}

Par défaut, les utilisateurs progressent à travers toutes les étapes Message, qu'ils aient reçu le message ou non. Si vous souhaitez faire avancer uniquement les utilisateurs qui reçoivent un message particulier, vous pouvez le faire en ajoutant une étape d'arbre décisionnel directement après votre composant Message. Ajoutez le filtre « Received Message from Canvas Step » comme filtre supplémentaire, puis sélectionnez le Canvas et l'étape Message.

Pour les étapes Message avec des messages in-app, vous pouvez utiliser un composant de parcours d'action au lieu du composant d'arbre décisionnel. Cela vous permettra de faire avancer les utilisateurs en fonction de leur visualisation ou non de votre message in-app. Définissez un groupe d'actions en ajoutant le filtre « Interact with Step » et sélectionnez **View in app message**. Ensuite, définissez la fenêtre d'évaluation de l'étape sur la fenêtre d'expiration du message in-app.

Pour un composant Message en communication multicanale, nous recommandons ce qui suit :
* Incluez une étape de délai entre vos étapes Message et arbre décisionnel, et définissez le délai à au moins cinq secondes.
* Si le composant inclut le timing intelligent, définissez le délai à 24 heures.
* Si le composant inclut une limitation du débit, divisez vos messages en plusieurs étapes Message monocanales et connectez-les ensemble. Ensuite, connectez l'étape d'arbre décisionnel directement après la dernière étape Message pour vérifier si un utilisateur a reçu l'un des messages. Vous pouvez également utiliser cette méthode comme alternative à une étape Message multicanale avec timing intelligent.

## Éléments à prendre en compte après le lancement {#things-to-consider-after-launch}

Vous avez lancé votre Canvas ! Et maintenant ? Utilisez cette liste de vérification pour savoir comment examiner et ajuster votre Canvas en cas de divergences après le lancement, en fonction de ces scénarios.

### Beaucoup d'entrées, mais peu d'envois {#many-entries-but-few-sends}

Par exemple, imaginons que vous avez constaté un écart entre le nombre de messages envoyés et le total des entrées. Vous pouvez identifier et découvrir les points à ajuster dans votre Canvas en vérifiant ces éléments clés.

#### Audience d'entrée {#entry-audience}

Si vous utilisez une campagne à envoi planifié, vérifiez bien votre audience cible en examinant votre population cible. Comment se présentent les chiffres selon les canaux, et quel est le rapport avec les canaux que vous avez utilisés dans votre Canvas ? Si les chiffres les plus bas correspondent aux canaux que vous avez utilisés dans votre Canvas, vous avez peut-être trouvé le problème.

#### Premier composant du Canvas {#first-component-of-the-canvas}

Examinez les filtres d'audience, les déclencheurs d'action ou les Segments utilisés dans les premiers composants de votre Canvas. Y a-t-il des fautes de frappe ou des conditions trop strictes qui empêchent votre Canvas de bien démarrer ? Utilisez-vous « Equals » alors que vous devriez utiliser « Matches Regex » ?

#### Groupe de contrôle du Canvas {#canvas-control-group}

Examinez la répartition des utilisateurs entre vos variantes et votre groupe de contrôle. Le groupe de contrôle est-il plus grand que prévu ? Si c'est le cas, vous pouvez modifier ce paramètre. Si **Optimiser avec BrazeAI<sup>TM</sup>** est activé et que le groupe de contrôle l'emporte, envisagez d'arrêter votre Canvas et d'essayer une nouvelle approche.

### Une audience totale vide {#an-empty-total-audience}

Si vous ne voyez aucune donnée d'entrée pour votre Canvas, la raison pour laquelle les utilisateurs n'entrent peut-être pas dans votre Canvas peut être liée à des conditions de concurrence et à des filtres de segmentation d'audience trop restrictifs.

Si vous utilisez une entrée basée sur une action dans votre planification d'entrée, vérifiez que vous n'avez pas utilisé la même action de déclenchement ici et dans votre **Audience cible**. Une condition de concurrence peut se produire lorsque l'utilisateur ne fait pas partie de l'audience au moment où il effectue l'événement déclencheur, ce qui signifie qu'il n'entrera pas dans le Canvas.

De plus, vérifiez que le Segment sélectionné contient bien des utilisateurs en examinant le tableau **Population cible** dans les paramètres de l'**Audience cible**. Si ce nombre est faible, voyez comment vous pouvez ajuster vos paramètres d'entrée ou examinez vos Segments ou filtres sélectionnés pour détecter d'éventuelles erreurs.

### Baisse inattendue entre les étapes {#unexpected-drop-off-between-steps}

Un autre moyen évident d'identifier des points d'ajustement pour votre Canvas est de constater une baisse importante d'une étape du Canvas à la suivante. Dans ce cas, vérifiez que vos filtres d'audience et vos événements d'exception ne contiennent pas de fautes de frappe ou d'erreurs de casse. Et comme toujours, vérifiez que vos filtres d'audience ne sont pas trop stricts au point d'exclure la majorité de vos utilisateurs de l'entrée dans le Canvas.

Ensuite, il est important d'identifier les paramètres qui peuvent affecter le moment et les conditions d'envoi des messages à vos utilisateurs :
- [Timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)
- [Heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)
- Validations de distribution

De manière générale, choisissez soit le timing intelligent, soit les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) pour votre Canvas, mais pas les deux. La même recommandation s'applique : utilisez soit le timing intelligent, soit la [limitation du débit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping), mais pas les deux. Pour en savoir plus sur la meilleure façon d'utiliser l'Intelligence Suite, consultez nos [cas d'usage de l'Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence_suite#use-cases).

### Volumes d'envoi suspects entre les parcours {#suspicious-send-volumes-between-paths}

Lorsque le volume d'envois entre deux ou plusieurs parcours (qu'il s'agisse de parcours d'audience ou de parcours d'action) ne correspond pas à ce que vous attendez, c'est l'occasion de vérifier vos Segments, filtres ou actions de déclenchement. Veillez également à identifier et supprimer tout filtre redondant.