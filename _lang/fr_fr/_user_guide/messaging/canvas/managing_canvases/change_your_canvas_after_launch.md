---
nav_title: Modifier les Canvas après le lancement
article_title: Modifier les Canvas après le lancement
page_order: 0
description: "Cet article de référence présente les différents aspects d'un Canvas qui peuvent être modifiés après le lancement initial."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Modifier les Canvas après le lancement {#edit-canvases-after-launch}

> Cet article de référence présente ce qui peut être modifié dans un Canvas après le lancement initial.

Vous pouvez modifier vos Canvas après le lancement en :

* Insérant de nouvelles étapes du Canvas dans le parcours utilisateur
* Ajoutant de nouvelles variantes et connexions
* Ajustant la distribution des variantes
* Arrêtant ou reprenant toutes les étapes du Canvas

{% alert note %}
La distribution de la variante de contrôle ne peut être que diminuée après le lancement.
{% endalert %}

Vous pouvez supprimer les éléments suivants dans votre parcours utilisateur :

- [Étapes du Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about)
- Variantes du Canvas
- Connexions entre les étapes du Canvas

Si vous souhaitez modifier ou ajouter des étapes supplémentaires à votre parcours utilisateur Canvas, les détails suivants s'appliquent :

- Les utilisateurs qui ne sont pas encore entrés dans le Canvas sont éligibles à toutes les étapes nouvellement créées.
- Si vos paramètres d'entrée du Canvas permettent aux utilisateurs de réintégrer les étapes, les utilisateurs qui ont déjà dépassé les étapes nouvellement créées sont éligibles à la réintégration.
- Les utilisateurs qui se trouvent actuellement dans un Canvas lancé, mais qui n'ont pas encore atteint les points du parcours utilisateur où de nouvelles étapes ont été ajoutées, sont éligibles pour recevoir ces étapes nouvellement ajoutées.

Si vous supprimez une étape [Délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) ou [Parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), vous pouvez éventuellement rediriger les utilisateurs qui attendent actuellement dans l'étape vers une autre étape du Canvas. Pour les délais, les utilisateurs restent dans l'étape jusqu'à la fin de la période de délai. Pour les parcours d'action, les utilisateurs restent dans l'étape jusqu'à la fin de la fenêtre d'évaluation.

Notez que lorsque vous lancez un Canvas initialement, Braze met en file d'attente les utilisateurs pour l'étape de message à laquelle ils se trouvent, et non tous les messages suivants dans le Canvas. Si vous apportez une modification au Canvas après le lancement, certains utilisateurs peuvent déjà être en file d'attente et ne pas prendre en compte les changements. Si vous arrêtez le Canvas, le dupliquez, puis le modifiez et lancez cette nouvelle version, le Canvas réévalue tous les utilisateurs, et pas seulement ceux qui n'ont pas encore été mis en file d'attente.

Consultez la section [Bonnes pratiques](#best-practices) pour des cas d'usage spécifiques de modification. De manière générale, il est recommandé d'éviter de modifier les Canvas en production, car cela peut entraîner des comportements inattendus.

{% details Développer pour les détails de l'éditeur Canvas d'origine %}

Gardez à l'esprit les modifications post-lancement autorisées suivantes pour un Canvas, en fonction du workflow avec lequel votre Canvas a été créé. Si votre Canvas utilise le workflow Canvas d'origine, vous devrez d'abord le cloner vers Canvas Flow pour effectuer des modifications post-lancement.

Vous ne pouvez pas modifier ou supprimer des connexions existantes, et vous ne pouvez pas insérer une étape entre des étapes déjà connectées. Si vous souhaitez modifier ou ajouter des étapes supplémentaires à votre parcours utilisateur Canvas, les détails suivants s'appliquent :

- Les utilisateurs qui ne sont pas encore entrés dans le Canvas sont éligibles à toutes les étapes nouvellement créées.
- Si vos paramètres d'entrée du Canvas permettent aux utilisateurs de réintégrer les étapes, les utilisateurs qui ont déjà dépassé les étapes nouvellement créées sont éligibles à la réintégration.
- Les utilisateurs qui se trouvent actuellement dans un Canvas lancé, mais qui n'ont pas encore atteint les étapes nouvellement ajoutées dans le parcours utilisateur, sont éligibles pour recevoir ces étapes nouvellement ajoutées.
- Si une étape de délai est la dernière étape du Canvas, les utilisateurs qui atteignent cette étape sont automatiquement sortis du Canvas et ne recevront aucune étape nouvellement créée.

{% alert important %}
Si vous mettez à jour les paramètres de **Délai** ou de **Fenêtre** d'une étape du Canvas, les utilisateurs qui se trouvent actuellement dans cette étape au moment de la mise à jour respectent le délai qui leur a été attribué lors de leur entrée initiale. Seuls les nouveaux utilisateurs entrant dans le Canvas et ceux qui n'ont pas encore été mis en file d'attente pour cette étape reçoivent le message à l'heure mise à jour.
{% endalert %}

L'arrêt d'un Canvas ne fait pas sortir les utilisateurs qui attendent de recevoir un message. Si vous réactivez le Canvas et que des utilisateurs attendent toujours le message, ils le reçoivent (sauf si l'heure à laquelle le message aurait dû être envoyé est passée, auquel cas ils ne le reçoivent pas).

{% enddetails %}

## Détails du Canvas {#canvas-details}

Vous pouvez modifier les paramètres et détails suivants après le lancement d'un Canvas :

- Nom et description du Canvas
- Teams
- Tags
  - L'ajout d'une étiquette après le lancement vous permet de recibler des utilisateurs dans des Segments à l'aide de filtres tels que `Received Message from Campaign or Canvas with Tag`.
- Type d'entrée, planification et contrôles
- Statut d'abonnement
- Limitation du débit
- Limite de fréquence
- Heures calmes
- Audience cible

Après le lancement d'un Canvas :

- Les événements de conversion ne peuvent pas être modifiés.
- Les étapes suivantes ne peuvent pas être ajoutées ni supprimées, et ne peuvent pas être réorganisées pour ajuster le classement : [parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), [parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) et [chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step).
  - **Solution 1 :** Créez un nouveau parcours d'audience, parcours d'action ou chemin d'expérience et reconfigurez les parcours vers cette nouvelle étape.
  - **Solution 2 :** Dupliquez le Canvas pour effectuer vos modifications.

### Étapes individuelles {#individual-steps}

Pour les étapes individuelles d'un Canvas, vous pouvez modifier les détails suivants après le lancement :

* Nom
* Contenu du message
* Déclencheurs
* Audience
* Événements d'exception
* Délais (uniquement pour les étapes de délai)

Cependant, le type de planification de l'étape et les pourcentages de contrôle ne sont pas modifiables après le lancement. Pour les étapes de parcours d'action et de parcours d'audience, les classements et les fenêtres d'évaluation ne sont pas modifiables après le lancement.

#### Étape Envoyer à la destination {#send-to-destination-step}

Lors de la modification de l'étape [Envoyer à la destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) sur un Canvas en direct or en ligne/en production/instantané, les comportements suivants s'appliquent :

- **Changement du Canvas de destination :** La modification de l'étape Envoyer à la destination pour pointer vers un Canvas de destination différent suit les mêmes règles générales de modification post-lancement. Les changements n'affectent que les utilisateurs qui n'ont pas encore atteint l'étape Envoyer à la destination.
  - Les utilisateurs qui sont déjà passés par l'étape restent dans le Canvas de destination d'origine — ils ne sont pas redirigés.
  - Les utilisateurs actuellement en file d'attente dans des étapes antérieures (par exemple, en attente dans une étape de délai avant l'étape Envoyer à la destination) sont évalués par rapport aux critères d'entrée et d'audience du nouveau Canvas de destination lorsqu'ils atteignent l'étape. Les utilisateurs éligibles sont envoyés vers le nouveau Canvas de destination.
- **Canvas de destination arrêté :** Si le Canvas de destination est arrêté alors que votre Canvas source est encore actif, les utilisateurs qui atteignent l'étape Envoyer à la destination ne sont pas envoyés vers le Canvas de destination. Cela provoque une perte d'utilisateurs lors du transfert, et non une pause pendant l'arrêt de la destination.
  - Les utilisateurs qui ne peuvent pas entrer dans le Canvas de destination arrêté continuent dans le Canvas source si d'autres étapes suivent l'étape Envoyer à la destination. Pour en savoir plus sur le comportement d'avancement, consultez [Envoyer à la destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination#how-does-advancement-behavior-work-for-send-to-destination-steps).
  - Vous ne pouvez pas lancer un Canvas source avec une étape Envoyer à la destination qui pointe vers une destination arrêtée. Ce comportement s'applique lorsqu'un Canvas de destination est arrêté après que le Canvas source est déjà en direct or en ligne/en production/instantané.

### Pourcentages des variantes du Canvas {#canvas-variant-percentages}

Après le lancement d'un Canvas, vous pouvez uniquement diminuer les pourcentages de la variante de contrôle. Si un pourcentage de variante est modifié dans le Canvas, vous constaterez que vos utilisateurs peuvent être redistribués vers d'autres variantes.

Au départ, ces utilisateurs se voient attribuer aléatoirement une variante particulière avant de recevoir une Campaign pour la première fois. À partir de ce moment, chaque fois que la Campaign est reçue par la suite (ou que l'utilisateur entre à nouveau dans une variante du Canvas), il reçoit la même variante, sauf si les pourcentages de variantes sont modifiés.

Si les pourcentages de variantes changent, les utilisateurs peuvent être redistribués vers d'autres variantes. Les utilisateurs restent dans ces variantes jusqu'à ce que les pourcentages soient à nouveau modifiés. Notez que pour les Canvas utilisant des branches avec des filtres `NOT` et des numéros de compartiment aléatoire, les utilisateurs peuvent ne pas recevoir la même branche à chaque fois dans leur parcours utilisateur lorsqu'ils entrent à nouveau dans le Canvas.

#### Groupes de contrôle {#control-groups}

Les groupes de contrôle restent cohérents si le pourcentage de variante est inchangé. Si le pourcentage d'un groupe de contrôle est diminué ou augmenté, les utilisateurs qui avaient précédemment reçu des messages ne pourraient pas entrer dans le groupe de contrôle lors d'un envoi ultérieur, et aucun utilisateur du groupe de contrôle ne recevrait jamais de message.

### Heure d'envoi locale {#local-send-time}

Les Canvas programmés pour être lancés à une heure d'envoi locale peuvent être modifiés jusqu'à 24 heures avant l'heure d'envoi prévue. Cette fenêtre est appelée la « zone de sécurité ».

{% alert tip %}
Si vous prévoyez d'apporter des modifications plus importantes nécessitant la création d'une copie entièrement nouvelle du Canvas, pensez à exclure les utilisateurs qui ont reçu le premier Canvas et à réajuster les horaires de planification du Canvas pour tenir compte de l'envoi par fuseau horaire.
{% endalert %}

Lorsqu'un calendrier d'entrée est configuré pour faire entrer les utilisateurs immédiatement au lancement, le Canvas se lance à l'heure la plus proche par incréments de 5 minutes. Par exemple, si vous mettez à jour un Canvas pour faire entrer les utilisateurs immédiatement à 8 h 31 PST, l'heure de lancement est fixée à 8 h 30 PST et dans le fuseau horaire de l'entreprise.

### Suppression de variantes {#deleting-variants}

Lorsque des variantes sont supprimées d'un Canvas, les événements suivants se produisent :

- Les étapes au sein de la variante (y compris celles partagées par d'autres variantes) sont supprimées.
- Les analyses de l'étape et les analyses de niveau supérieur du Canvas, telles que _Total des entrées_, _Total des sorties_ et _Taux de conversion_, sont supprimées.
- Les utilisateurs dans les variantes supprimées sortent des étapes, et les messages suivants ne sont pas envoyés.

### Propriétés d'entrée du Canvas {#canvas-entry-properties}

Les propriétés d'entrée du Canvas ne sont pas intégrées dans les étapes lors de l'envoi. Cela signifie que lorsque les propriétés d'entrée du Canvas sont modifiées après le lancement d'un Canvas, ces changements ne s'appliquent qu'aux nouveaux utilisateurs qui entrent dans le Canvas. Si votre Canvas permet aux utilisateurs d'entrer à nouveau dans le Canvas, les utilisateurs qui entrent à nouveau sont déterminés par les propriétés d'entrée du Canvas mises à jour.

## Bonnes pratiques {#best-practices}

Consultez ces bonnes pratiques à garder à l'esprit lorsque vous modifiez ou ajoutez des éléments à votre Canvas après son lancement.

{% alert important %}
De manière générale, évitez d'apporter des modifications lorsque le Canvas est actif et que des utilisateurs sont en file d'attente.
{% endalert %}

### Étapes déconnectées {#disconnected-steps}

Vous pouvez lancer votre Canvas avec des étapes déconnectées et également enregistrer ces Canvas après le lancement. Avant de déconnecter une étape de votre workflow, nous vous recommandons de vérifier la vue analytique des étapes pour les utilisateurs en attente.

Imaginons qu'un utilisateur se trouve dans une étape déconnectée de votre workflow Canvas. Cet utilisateur avance vers l'étape suivante s'il y en a une. Les paramètres de l'étape déterminent comment l'utilisateur doit avancer.

En créant ou en modifiant des étapes déconnectées, vous pouvez apporter des modifications à ces étapes indépendantes sans avoir à les connecter directement au reste de votre Canvas. Cela vous aide à tester vos étapes avant de relancer votre Canvas.

### Étape des chemins d'expérience {#experiment-path-step}

Si votre Canvas comporte une expérience de chemin gagnant active ou en cours et que vous mettez à jour le Canvas actif, l'expérience prend fin. Cela s'applique même si vous ne mettez pas à jour l'étape des chemins d'expérience. Pour relancer l'expérience, déconnectez le chemin d'expérience existant et lancez-en un nouveau, ou dupliquez le Canvas et lancez le duplicata. Sinon, les utilisateurs passent par le chemin d'expérience sans optimisation.

Les étapes des chemins d'expérience existantes qui utilisent des chemins personnalisés continuent de fonctionner. La mise à jour d'un Canvas actif met également fin à une expérience de chemins personnalisés en cours.

### Délais {#time-delays}

La modification de Canvas avec des délais peut être un peu délicate. Gardez donc à l'esprit les détails suivants lorsque vous apportez des modifications à vos Canvas :

- Si vous mettez à jour le délai dans une étape de délai, seuls les nouveaux utilisateurs entrant dans le Canvas et les utilisateurs qui n'ont pas encore été mis en file d'attente pour cette étape reçoivent le message avec le délai mis à jour.
- Si vous supprimez une étape avec un délai (comme les étapes de délai ou les parcours d'action) et décidez de rediriger ces utilisateurs vers une autre étape du Canvas, les utilisateurs ne sont redirigés qu'après l'expiration du délai de l'étape. Par exemple, supposons que vous supprimez une étape de délai avec un délai d'un jour et que vous redirigez ces utilisateurs vers une étape de message. Dans ce cas, les utilisateurs ne sont redirigés qu'après l'expiration du délai d'un jour.
- Si votre Canvas comporte une ou plusieurs étapes de chemins d'expérience, la suppression d'étapes pourrait invalider les résultats de cette étape.

### Arrêt des Canvas {#stopping-canvases}

L'arrêt d'un Canvas ne fait pas sortir les utilisateurs qui attendent dans une étape. Si vous réactivez le Canvas et que les utilisateurs sont toujours en attente, ils terminent l'étape et passent à l'étape suivante. Cependant, si le moment où l'utilisateur aurait dû passer à l'étape suivante est déjà passé, il sort du Canvas.

Par exemple, supposons que vous ayez un Canvas créé avec le workflow Canvas Flow, programmé pour se lancer à 14 h avec une variante comportant deux étapes : une étape de délai avec un délai d'une heure suivie d'une étape de message.

Un utilisateur entre dans ce Canvas à 14 h 01 et entre dans l'étape de délai au même moment. Cela signifie que l'utilisateur est programmé pour passer à l'étape suivante du parcours utilisateur (l'étape de message) à 15 h 01. Si vous arrêtez le Canvas à 14 h 30 et le réactivez à 15 h 30, l'utilisateur sort du Canvas puisqu'il est après 15 h 01. Cependant, si vous réactivez le Canvas à 14 h 40, l'utilisateur passe à l'étape de message comme prévu à 15 h 01.

## Ce qu'il faut savoir {#things-to-know}

Les problèmes courants suivants peuvent être déclenchés par la modification ou l'ajout de composants à tout autre composant d'un Canvas après son lancement.

{% alert important %}
Les problèmes suivants sont évitables. Si vous devez apporter des modifications à un Canvas après son lancement, nous vous recommandons d'abord de confirmer que tous les utilisateurs qui sont déjà entrés dans le Canvas ont terminé leur parcours utilisateur. De plus, nous vous suggérons de ne pas supprimer les étapes qui ont déjà été traitées par au moins un utilisateur.
{% endalert %}

- Données de reporting manquantes (lorsque des variantes de message sont supprimées puis rajoutées)
- Les utilisateurs ne suivent pas le parcours attendu
- Les messages sont envoyés à des moments inattendus
- Les modifications n'écrasent pas les données Currents, vous pouvez donc remarquer des écarts entre les étapes du Canvas (comme des `canvas_step_ids` qui n'existent plus dans le Canvas en raison d'une suppression)
- Les utilisateurs peuvent recevoir le même message deux fois
- Les utilisateurs ne recevront pas de messages en raison de la limitation du débit existante
  - Lorsque vous mettez à jour la limitation du débit sur un Canvas actif, la nouvelle limitation du débit s'applique uniquement aux utilisateurs qui passent par l'étape Message après la modification de la limitation du débit. Les utilisateurs qui sont déjà en file d'attente pour une étape Message conservent la limitation du débit d'origine qui était en vigueur lorsqu'ils ont été mis en file d'attente. Pour appliquer une nouvelle limitation du débit à tous les utilisateurs, arrêtez le Canvas, dupliquez-le avec la limitation du débit mise à jour et lancez le nouveau Canvas. Utilisez un filtre pour empêcher les utilisateurs ayant reçu des messages du Canvas d'origine d'entrer dans le doublon.
- Lorsqu'un Canvas est [automatiquement arrêté]({{site.baseurl}}/user_guide/messaging/governance/statuses#available-statuses), les brouillons post-lancement du Canvas sont également supprimés.