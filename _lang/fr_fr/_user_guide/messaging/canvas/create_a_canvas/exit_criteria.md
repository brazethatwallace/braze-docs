---
nav_title: Critères de sortie
article_title: Critères de sortie
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "Cet article de référence traite des critères de sortie et de la manière dont les utilisateurs peuvent quitter votre Canvas en fonction des critères sélectionnés."
tool: Canvas
---

# Critères de sortie {#exit-criteria}

> En ajoutant des événements d'exception directement à vos règles d'entrée de Canvas, vous pouvez retirer des utilisateurs du parcours lorsqu'ils effectuent une action spécifique.
> Braze enregistre la sortie dès que l'événement se produit.
> La rapidité avec laquelle un utilisateur quitte complètement le Canvas dépend de l'étape dans laquelle il se trouve, en particulier pour les étapes de délai.
> Pour en savoir plus, consultez [Comment les utilisateurs sortent](#how-users-exit).

## Comment les utilisateurs sortent {#how-users-exit}

Lorsqu'un utilisateur effectue l'événement de sortie, Braze le marque immédiatement pour sortir du Canvas. Après cela, il ne progresse vers aucune étape ultérieure.

S'il se trouve dans une étape de délai, il y reste jusqu'à la fin de la période de délai. Il ne passe à aucune des étapes suivantes lorsque le délai se termine : il quitte entièrement le Canvas à la place. Selon l'endroit où vous consultez les données du Canvas, vous pouvez observer une activité liée à la sortie au moment où l'événement de sortie se produit, puis à nouveau lorsque l'étape de délai se termine et que l'utilisateur quitte complètement le Canvas.

Par exemple, si un utilisateur se trouve dans une étape de délai de 30 jours et qu'il effectue l'événement de sortie le premier jour de l'étape de délai, il est marqué pour sortir immédiatement, mais il ne quitte pas complètement le Canvas avant la fin de l'étape de délai (29 jours plus tard).

Prenons un autre exemple avec des critères de sortie basés sur le temps. Un utilisateur entre dans une étape de délai définie à 24 heures le 1er juillet à minuit. Pendant cette période de délai, il effectue l'événement de sortie « A passé une dernière commande il y a moins d'une heure » à 3 h du matin. Cet utilisateur sera évalué selon les critères de sortie le 2 juillet à minuit, c'est-à-dire à la fin de la durée de l'étape de délai. Étant donné que 21 heures se sont écoulées depuis sa commande du 1er juillet à 3 h du matin, il ne sortira pas du Canvas, car il n'a pas passé de commande dans l'heure précédant la fin de l'étape de délai le 2 juillet. Cela a un impact sur le « Total Exits by Exit Criteria » dans l'analyse de votre Canvas, qui n'est mis à jour qu'après qu'un utilisateur a complètement quitté le Canvas.

## Configurer les critères de sortie {#setting-up-exit-criteria}

Dans l'étape **Target Audience** du générateur de Canvas, vous pouvez configurer des critères de sortie pour identifier les utilisateurs que vous souhaitez faire sortir de votre Canvas.

Les critères de sortie incluent un événement d'exception, qui est l'action spécifique pouvant amener les utilisateurs à sortir du Canvas.

![Les critères de sortie configurés pour ré-engager les utilisateurs qui ont consulté des produits mais ne les ont pas encore ajoutés à leur panier ou n'ont pas encore passé de commande.]({% image_buster /assets/img/exit_criteria.png %}){: style="max-width:90%;"}

### Sélection des événements d'exception {#exception-events}

Lorsqu'un utilisateur effectue l'événement d'exception, Braze le marque pour sortie conformément à la section [Comment les utilisateurs sortent](#how-users-exit). Les événements d'exception s'appliquent pendant que l'utilisateur est dans le Canvas, y compris lorsqu'il attend dans une étape telle qu'une étape de délai.

Supposons que vous ayez un Canvas configuré pour promouvoir un nouveau produit. Dans ce cas, la commande du produit serait l'événement d'exception. Ainsi, après qu'un utilisateur a passé la commande, il ne recevra plus de messages concernant un produit qu'il a déjà acheté. Les événements d'exception permettent de garder votre communication pertinente et personnalisée.

Les événements d'exception supplémentaires incluent :

- Passer une commande
- Démarrer une session
- Effectuer un événement personnalisé
- Effectuer un événement de conversion
- Ajouter une adresse e-mail
- Modifier la valeur d'un attribut personnalisé
- Mettre à jour un statut d'abonnement
- Mettre à jour un statut du groupe d'abonnement
- Interagir avec une Campaign
- Entrer dans un emplacement
- Déclencher un géorepérage
- Envoyer un message SMS entrant
- Envoyer un message WhatsApp entrant
- Envoyer un message LINE entrant
- Effectuer un événement de mise à jour du panier

#### Étapes planifiées {#scheduled-steps}

Pour les étapes de Canvas qui ne maintiennent pas l'utilisateur dans une étape de délai jusqu'à un moment futur, l'utilisateur quitte généralement le Canvas dès que l'étape en cours est terminée. Cette complétion se produit souvent immédiatement après l'événement d'exception, car il n'y a pas de minuteur de délai restant sur cette étape. Cela diffère d'une étape de délai, où l'utilisateur reste jusqu'à la fin du délai même après avoir été marqué pour sortie (voir [Comment les utilisateurs sortent](#how-users-exit)).

#### Étapes déclenchées {#triggered-steps}

Si une étape de Canvas est déclenchée par un événement, le dernier envoi planifié mis en file d'attente à partir de ce déclencheur sera annulé, mais l'utilisateur restera dans le Canvas pendant toute la durée de la fenêtre. Cela signifie que l'utilisateur peut toujours recevoir l'étape s'il effectue à nouveau l'événement déclencheur dans la fenêtre. Une fois la fenêtre passée, l'utilisateur sortira alors du Canvas.

### Utilisation de Segments et de filtres {#using-segments-and-filters}

Vous pouvez également ajouter des Segments et des filtres dans les critères de sortie. Cela signifie que les utilisateurs correspondant au Segment et au filtre sortiront du Canvas et ne recevront plus aucun message supplémentaire.

Par exemple, si la première étape d'un Canvas est une étape de délai avec un délai de cinq jours, les critères de sortie sont évalués à la fin de cette étape. Si un utilisateur remplit les critères de sortie alors qu'il se trouve dans l'étape de délai, il est marqué pour sortie immédiatement, mais il quitte définitivement le Canvas à la fin des cinq jours (et il ne progresse vers aucune étape après le délai).

{% alert note %}
Les attributs de type tableau ne sont actuellement pas pris en charge comme critères de sortie pour les événements d'exception.
{% endalert %}

### Avoir le même événement de sortie et événement de conversion {#having-the-same-exit-event-and-conversion-event}

Lorsque l'événement de sortie et l'événement de conversion sont identiques, les deux événements (conversion et sortie) seront comptabilisés. Par exemple, si un Canvas comporte une étape de délai et qu'un utilisateur remplit les critères de sortie pendant cette étape de délai, l'événement de sortie sera incrémenté dès que l'utilisateur quitte l'étape de délai. La conversion sera également incrémentée dès que l'événement est enregistré dans le profil utilisateur.

Les conversions sont suivies même après la fin du Canvas, mais les sorties ne sont plus suivies une fois que l'utilisateur a quitté le Canvas. La fenêtre de conversion s'étend jusqu'à trois jours au-delà de la durée maximale du Canvas. Cela signifie que les conversions continueront d'être suivies après que le suivi des sorties aura cessé.

La durée minimale d'une fenêtre de conversion est de cinq minutes. Définissez les fenêtres de conversion sur cinq minutes pour vos événements de conversion afin de vous rapprocher le plus possible de la parité avec les événements de sortie. Nous recommandons également de définir la fenêtre de conversion pour qu'elle corresponde au moins au chemin le plus long dans le Canvas.

Considérons l'exemple suivant illustrant comment les analyses sont calculées :

1. Dix utilisateurs passent par le Canvas.
2. Trois utilisateurs effectuent l'événement de conversion dans les cinq minutes (le nombre d'événements de sortie est de trois et le nombre d'événements de conversion est de trois).
3. Cinq autres utilisateurs sortent du Canvas après cinq minutes mais effectuent l'événement de conversion après deux jours (le nombre d'événements de sortie reste identique, mais le nombre d'événements de conversion passe à huit).
4. Les deux derniers utilisateurs sortent du Canvas après cinq minutes mais n'effectuent pas l'événement de conversion, ou l'effectuent après trois jours et cinq minutes (ils ne sont comptabilisés ni dans les indicateurs d'événements de sortie ni dans ceux d'événements de conversion).

## Exemple {#example}

Imaginons que nous souhaitons cibler les utilisateurs qui n'ont pas encore passé de commande dans notre entreprise de fourniture de sacs à dos. Pour configurer les critères de sortie, nous devons :

1. Sélectionner **Place an Order** comme événement d'exception.
2. Sélectionner **Add Trigger**.
3. Pour **Segments**, sélectionner **Used in last day** afin que, lors du lancement de notre Canvas, l'audience exclue les utilisateurs ayant effectué des achats.
4. Pour **Filters**, sélectionner **Purchase behavior** > **Number of purchases** > **Purchased product**.
5. Définir le groupe de filtres sur `backpack-example exactly 1`. Cela signifie que les utilisateurs ayant acheté notre produit sac à dos sortiraient du Canvas.

![Paramètres des critères de sortie avec « Makes Any Purchase » comme événement d'exception : si un utilisateur effectue un achat, il sortira de ce Canvas.]({% image_buster /assets/img_archive/exit_criteria_example.png %}){: style="max-width:80%;"}

{% alert tip %}
Pour configurer des critères de sortie qui comparent les propriétés d'événement aux propriétés d'entrée du Canvas (par exemple, sortir uniquement lorsqu'un utilisateur achète l'article spécifique qu'il a abandonné), consultez [Faire correspondre les critères de sortie aux événements d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria).
{% endalert %}