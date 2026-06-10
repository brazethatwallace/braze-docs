---
nav_title: Parcours d'actions
article_title: Parcours d'actions
alias: /action_paths/
page_order: 1
page_type: reference
description: "Cet article de référence explique comment utiliser les Parcours d'actions, un composant qui permet de trier les utilisateurs en fonction de leurs actions."
tool: Canvas
---

# Parcours d'actions {#action-paths}

> Les Parcours d'actions dans Canvas vous permettent de trier vos utilisateurs en fonction de leurs actions.

![Une étape Parcours d'actions dans un parcours utilisateur Canvas.]({% image_buster /assets/img/canvas_actionpath.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Grâce aux Parcours d'actions, vous pouvez :

* Personnaliser les parcours utilisateur en fonction d'une action spécifique, y compris les événements d'engagement et les événements personnalisés
* Retenir les utilisateurs pendant une durée donnée afin de prioriser leur prochain parcours en fonction de leurs actions au cours de cette période d'évaluation

## Créer un parcours d'action {#creating-an-action-path}

Pour créer un parcours d'action, ajoutez un composant à votre Canvas. Glissez-déposez le composant depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape et sélectionnez **Parcours d'actions**.

### Paramètres d'action {#action-settings}

Dans les **Paramètres d'action**, définissez la **Fenêtre d'évaluation** pour déterminer combien de temps les utilisateurs sont retenus dans l'étape. Par défaut, les utilisateurs sont évalués sur une journée, mais vous pouvez ajuster cette fenêtre en secondes, minutes, heures, jours et semaines selon votre Canvas. La fenêtre d'évaluation maximale pour un parcours d'action est de 31 jours.

Dans les **Paramètres d'action**, vous pouvez également activer l'ordre de classement pour vos composants en activant le bouton **Faire avancer les utilisateurs selon l'ordre de classement**.

![Les Paramètres d'action avec une fenêtre d'évaluation de 1 jour.]({% image_buster /assets/img/actionpath_settings.png %})

Par défaut, le **Classement** est désactivé. Lorsqu'un utilisateur entre dans le parcours d'action et effectue l'événement déclencheur associé à un groupe d'actions, il avance immédiatement dans le groupe d'actions correspondant en fonction de la **première action qualifiante** qu'il effectue après être entré dans l'étape. Si un utilisateur effectue une deuxième action correspondant à un autre groupe d'actions, il ne change pas de parcours — c'est la première action qui détermine son itinéraire. Si un utilisateur n'effectue aucun événement déclencheur, il avance dans le groupe par défaut **Tous les autres** à la fin de la période d'évaluation.

Lorsque l'option **Faire avancer les utilisateurs selon l'ordre de classement** est activée, le **Classement** est actif. Tous les utilisateurs sont alors retenus jusqu'à la fin de la fenêtre d'évaluation. À la fin de la période d'évaluation, les utilisateurs avancent dans le groupe d'actions de plus haute priorité pour lequel ils sont éligibles à la fin de la fenêtre d'évaluation. Les utilisateurs qui n'effectuent aucune des actions pendant la fenêtre d'évaluation avancent dans le groupe par défaut **Tous les autres**.

{% alert tip %}
Pour orienter les utilisateurs en fonction de leurs attributs actuels ou de leur appartenance à un segment plutôt que des actions qu'ils effectuent, utilisez plutôt les [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/).
{% endalert %}

Notez que vous pouvez déclencher un parcours d'action lorsqu'un objet d'attribut personnalisé imbriqué change, mais pas pour les tableaux d'attributs personnalisés imbriqués ni pour les modifications de types de données de tableau d'objets.

#### Messages in-app {#in-app-messages}

Notez que lorsque le déclencheur du groupe d'actions est le démarrage d'une session et que l'étape suivante est un message in-app, l'utilisateur doit effectuer deux démarrages de session pour recevoir le message in-app. La première session assigne l'utilisateur au groupe d'actions dans le parcours d'action, et la seconde session déclenche le message in-app.

#### Exemple de statut de classement {#ranking-status-example}

Supposons que vous ayez un parcours d'action avec une période d'évaluation d'un jour et deux groupes d'actions : Groupe 1 et Groupe 2. Le Groupe 1 a pour événement déclencheur « Démarrer une session » et le Groupe 2 « Effectuer un achat ». Si le **Classement** est activé, tous les utilisateurs du parcours d'action sont « retenus » pendant un jour. À la fin de la journée, si un utilisateur a démarré une session et effectué un achat, il avance dans le parcours de rang le plus élevé. Dans ce cas, l'utilisateur avancerait dans le Groupe 1.

Dans l'exemple précédent, si le **Classement** est désactivé et qu'un utilisateur effectue l'un des événements déclencheurs (« Démarrer une session » ou « Effectuer un achat »), cet utilisateur avance dans le groupe d'actions correspondant en fonction de l'action de déclenchement.

Notez que les propriétés d'entrée Canvas diffèrent des propriétés d'événement. Les propriétés d'entrée Canvas sont les propriétés de l'événement qui a déclenché le Canvas. Ces propriétés ne peuvent être utilisées que dans la première étape complète d'un Canvas lorsque vous utilisez le workflow Canvas d'origine. Avec Canvas, les propriétés d'entrée persistantes sont activées et permettent de réutiliser les propriétés d'entrée tout au long du Canvas. À l'inverse, les propriétés d'événement proviennent d'un événement ou d'une action qui se produit au fil du parcours de l'utilisateur.

### Groupes d'actions {#action-groups}

Ajoutez un ou plusieurs déclencheurs pour définir vos groupes d'actions. Vous pouvez sélectionner une variété de déclencheurs, par exemple si les utilisateurs :

- Effectuent un achat
- Démarrent une session
- Effectuent un [événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)
- Effectuent un événement de conversion
- Ajoutent une adresse e-mail
- Modifient la valeur d'un attribut personnalisé.
  - Cela inclut l'ajout d'un nouvel attribut avec une valeur à un profil utilisateur pour la première fois (lorsque l'attribut n'était pas présent auparavant).
  - Les déclencheurs d'attribut ne sont pas disponibles pour les attributs de type tableau.
- Mettent à jour leur statut d'abonnement ou leur statut du groupe d'abonnement
- Interagissent avec une Campaign ou une carte de contenu
- Entrent dans un emplacement
- Déclenchent un géorepérage
- Envoient un message entrant SMS ou WhatsApp

![Un groupe d'actions nommé « Groupe 1 » pour les utilisateurs qui effectuent un achat quelconque.]({% image_buster /assets/img/actionpath_group.png %})

Dans les paramètres de chaque groupe d'actions, vous avez également la possibilité de cocher la case **Je souhaite que ce groupe quitte le Canvas**, ce qui signifie que les utilisateurs de ce groupe quitteront le Canvas à la fin de la période d'évaluation.

### Canvas avec rééligibilité {#canvases-with-re-eligibility}

Si des utilisateurs entrent dans un parcours d'action plusieurs fois et ont plusieurs entrées simultanées dans le parcours d'action, le comportement attendu varie en fonction du statut du **Classement**.

| Statut du classement | Comportement du parcours d'action |
|---|--------------|
| **Désactivé** | Un utilisateur peut entrer dans un parcours d'action plus d'une fois. Ces entrées sont retenues dans le parcours d'action jusqu'à ce qu'une action ou un événement déclencheur soit enregistré. Si l'événement déclencheur ne satisfait pas les filtres de propriétés d'une entrée (par exemple, une [variable de contexte]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_variables/) ne correspond pas aux filtres de propriétés du déclencheur), l'entrée reste dans le parcours d'action. <br><br>Si l'événement déclencheur satisfait plus d'une entrée, Braze déduplique uniquement ces entrées et fait immédiatement avancer l'entrée correspondante la plus ancienne dans le groupe d'actions approprié. |
| **Activé** | Toutes les entrées avancent à la fin de la fenêtre d'évaluation correspondante. Aucune déduplication n'est effectuée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas avec rééligibilité" }

Notez que les classements ne sont pas [modifiables après le lancement]({{site.baseurl}}/post-launch_edits/).