---
nav_title: Délai
article_title: Délai
alias: "/delay_step/"
page_order: 8
page_type: reference
description: "Cet article de référence explique comment ajouter un délai à votre Canvas sans avoir besoin d'ajouter un message associé."
tool: Canvas

---

# Délai

> Les composants Délai vous permettent d'ajouter un délai autonome à un Canvas. Vous pouvez ajouter un délai à votre Canvas sans avoir besoin d'ajouter un message associé.

Les délais peuvent rendre votre Canvas plus lisible. Vous pouvez également utiliser ce composant pour retarder une étape différente jusqu'à une date exacte, un jour spécifique ou un jour spécifique de la semaine. Un composant Délai peut être connecté à une seule étape suivante au maximum. <br> ![Une étape Délai avec un délai d'un jour comme première étape d'un Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Créer un délai

Pour créer un délai, ajoutez une étape à votre Canvas. Glissez-déposez le composant Délai depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape, puis choisissez **Délai**.

#### Délais prolongés

Vous pouvez prolonger les étapes Délai jusqu'à deux ans (730 jours). Par exemple, si vous effectuez l'onboarding de nouveaux utilisateurs pour votre application, vous pouvez ajouter un délai prolongé de deux mois avant d'envoyer une étape Message pour inciter les utilisateurs qui n'ont pas démarré de session.

## Types de délais

Vous pouvez choisir le type de délai avant le prochain message dans votre Canvas. Vous pouvez soit définir un délai pour que vos utilisateurs attendent une période déterminée, soit les retarder jusqu'à une date et une heure spécifiques.

S'il y a un délai, il est normal que certains utilisateurs ne passent à l'étape suivante du Canvas qu'après le délai. Les utilisateurs en attente ne seront pas comptabilisés dans l'indicateur _Passés à l'étape suivante_. Pour plus d'informations, consultez [Analyse des délais](#delay-analytics).

{% tabs %}
{% tab Durée %}

Sélectionner **Durée** vous permet de retarder les utilisateurs pendant un nombre défini de secondes, minutes, heures, jours ou semaines, et à une heure spécifique. Par exemple, vous pouvez retarder les utilisateurs de quatre heures ou d'un jour.

Notez la différence entre le calcul des « jours » et des « jours calendaires ».

- Un « jour » correspond à 24 heures et est calculé à partir du moment où l'utilisateur entre dans l'étape Délai.
- Un « jour calendaire » définit le temps d'attente jusqu'à la prochaine heure spécifiée, qui peut être inférieur à 24 heures. Vous pouvez choisir de retarder selon l'heure de l'entreprise ou l'heure locale de l'utilisateur. Si aucune heure n'est spécifiée, l'utilisateur sera retardé jusqu'à minuit le jour suivant, selon l'heure de l'entreprise.

Vous pouvez également sélectionner **À une heure spécifique** pour indiquer quand les utilisateurs avanceront dans le Canvas. Cette option prend en compte l'heure à laquelle l'utilisateur est entré dans l'étape Délai. Si cette heure dépasse l'heure configurée dans les paramètres, des heures supplémentaires seront ajoutées au délai.

Par exemple, supposons que nous sommes le 11 décembre et que notre étape Délai est configurée avec une **Durée** d'une semaine à 8 h UTC. Si un utilisateur entre dans l'étape Délai le 4 décembre, il sera libéré de l'étape Délai pour poursuivre son parcours aujourd'hui s'il est entré dans l'étape Délai avant 8 h UTC. S'il est entré dans l'étape Délai après cette heure, l'utilisateur sera retardé jusqu'au jour suivant (la prochaine occurrence de cette heure).

{% endtab %}
{% tab Date calendaire %}

Sélectionner **Date calendaire** vous permet de retenir les utilisateurs dans l'étape jusqu'à une date et une heure spécifiques.

#### Considérations

##### Les utilisateurs ne recevront pas les étapes ou messages dont la date est passée

Si la date et l'heure sélectionnées sont déjà passées au moment où les utilisateurs arrivent à l'étape Délai, ils quitteront le Canvas. Il peut y avoir jusqu'à 31 jours entre le début du Canvas et les dates choisies pour les étapes « attendre jusqu'à un jour exact ».

{% alert important %}
Si vous participez à l'[accès anticipé de Canvas Context]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/), vous pouvez définir des délais allant jusqu'à 2 ans.
{% endalert %}

Par exemple, les utilisateurs ne recevront pas les étapes ou messages dans ces scénarios :

- Un message est planifié pour être envoyé le 3 mai à 21 h, mais l'étape Délai expire le 3 mai à 9 h.
- Une étape du Canvas est retardée jusqu'à une heure spécifique dans le fuseau horaire local de l'utilisateur, mais les utilisateurs n'ont pas de fuseau horaire défini dans leur profil utilisateur. Le délai utilise alors par défaut le fuseau horaire de l'entreprise pour ces utilisateurs, et l'heure spécifiée est déjà passée.

##### Les utilisateurs quitteront le Canvas si une étape Délai suivante se situe dans la période d'une étape Délai précédente

Si le Canvas comporte deux étapes Délai mais que la première étape Délai est plus longue que la seconde, les utilisateurs quitteront également le Canvas.

Par exemple, supposons qu'un Canvas comporte ces étapes :
- Étape 1 : étape Message
- Étape 2 : étape Délai jusqu'au 13 décembre à 22 h
- Étape 3 : étape Message
- Étape 4 : étape Délai jusqu'au 13 décembre à 19 h
- Étape 5 : étape Message

Les utilisateurs qui entrent dans l'étape 4 quitteront le Canvas avant de recevoir l'étape 5, car le délai de l'étape 4 se situe dans la période de l'étape 2.

{% endtab %}
{% tab Jour de la semaine %}

Sélectionner **Jour de la semaine** vous permet de retenir les utilisateurs dans l'étape jusqu'à un jour spécifique de la semaine, à une heure spécifique. Par exemple, vous pouvez retarder les utilisateurs jusqu'au prochain jeudi à 16 h dans le fuseau horaire de l'entreprise.

Pour configurer correctement cette option, vous devrez également sélectionner ce qui se passe si l'utilisateur entre dans le Canvas le jour de la semaine sélectionné (par exemple, jeudi), mais après l'heure spécifiée. Vous pouvez choisir de faire avancer l'utilisateur le même jour ou de le retenir jusqu'à la semaine suivante.
{% endtab %}
{% endtabs %}

## Utiliser les étapes Délai

Supposons que nous sommes le 10 juin. Le 11 juin, vous souhaitez que les utilisateurs entrent dans le Canvas et reçoivent un message concernant une promotion à venir. Ensuite, vous voulez retenir les utilisateurs dans le Canvas jusqu'au 17 juin à 15 h, heure locale. À 15 h, heure locale, le 17 juin, vous souhaitez envoyer aux utilisateurs un message de rappel concernant la promotion.

La séquence des étapes du Canvas pourrait ressembler à ceci :

1. Commencez par ajouter une étape Message qui s'envoie immédiatement après que les utilisateurs entrent dans le Canvas le 11 juin.
2. Créez une étape Délai qui retient les utilisateurs jusqu'à 15 h, heure locale, le 17 juin.
3. Reliez l'étape Délai à une autre étape Message qui envoie son message immédiatement.

### Composants Délai à la fin d'un Canvas {#delay-as-last-step}

Si vous ajoutez un composant Délai à votre Canvas et qu'il n'y a pas d'étapes suivantes, tout utilisateur qui atteint la dernière étape sera automatiquement sorti du Canvas. Cela est vrai même si le délai de l'étape Délai n'a pas encore été atteint. Cela signifie que les utilisateurs qui ont déjà atteint l'étape Délai ne recevront aucun message que vous ajoutez après cette étape. Cependant, si un utilisateur n'a pas encore atteint l'étape Délai et qu'un message est ajouté, il recevra ce message.

### Délais personnalisés

{% multi_lang_include alerts/early_access_beta_alert.md feature='The personalized delays and extended delays feature' %}

Activez le bouton **Personnaliser le délai** pour configurer un délai personnalisé pour vos utilisateurs. Vous pouvez l'utiliser avec une [étape Context]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) pour sélectionner la variable de contexte sur laquelle baser le délai. Cela remplacera l'heure de la journée définie dans l'attribut ou la propriété sélectionnée. C'est utile lorsque vous appliquez un décalage en jours ou en semaines et que vous souhaitez que les utilisateurs avancent à une heure spécifique. Le fuseau horaire provient de l'attribut ou de la propriété, ou utilise le fuseau horaire de secours si aucun n'est disponible.

#### Comportement du fuseau horaire pour « à une heure spécifique »

Lors de la configuration de délais personnalisés avec l'option **à une heure spécifique**, le comportement du fuseau horaire dépend du type de données de votre attribut ou variable de contexte :

- **Type de données chaîne de caractères avec fuseau horaire :** si l'attribut ou la variable de contexte est de type chaîne de caractères et inclut des informations de fuseau horaire, le fuseau horaire spécifié dans la chaîne est utilisé. Par exemple, `2025-06-10T10:00:00-08:00` utilise UTC-8.
- **Type de données chaîne de caractères sans fuseau horaire :** si l'attribut ou la variable de contexte est de type chaîne de caractères sans information de fuseau horaire, le fuseau horaire de secours est utilisé. Par exemple, `2025-06-10` utilise le fuseau horaire de secours.
- **Type de données temporel :** si l'attribut ou la variable de contexte est de type temporel, le fuseau UTC est utilisé. En effet, le type de données temporel est toujours converti en UTC lors de l'enregistrement dans la base de données, donc « à une heure spécifique » fera toujours référence à UTC lorsque la variable est de type temporel. Par exemple, `2025-06-10T10:00:00-08:00` utilise UTC+0.

{% alert note %}
Il est possible qu'un attribut personnalisé ou une variable de contexte n'ait ni heure spécifique ni fuseau horaire s'il s'agit d'un type de données chaîne de caractères. S'il s'agit d'un type de données temporel, vous devrez spécifier l'heure et le fuseau horaire. Cependant, si l'attribut personnalisé ou la variable de contexte est une chaîne « non pertinente » (comme « product_name »), l'utilisateur quittera le Canvas.
{% endalert %}

#### Cas d'utilisation

Supposons que vous souhaitez rappeler à vos clients d'acheter du dentifrice dans 30 jours. En combinant une étape Context et une étape Délai, vous pouvez sélectionner cette variable de contexte pour baser le délai. Dans ce cas, votre étape Context aurait les champs suivants :

- **Nom de la variable de contexte :** product_reminder_interval
- **Type de données :** Time
- **Valeur :** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![La variable « product_reminder_interval » et sa valeur.]({% image_buster /assets/img/context_step1.png %})

Ensuite, parce que vous souhaitez rappeler vos clients dans 30 jours, vous sélectionnerez **Jusqu'à un jour spécifique** comme option de délai et sélectionnerez **Personnaliser le délai** pour utiliser les informations de votre étape Context. Vos utilisateurs seront ainsi retardés jusqu'à la variable de contexte sélectionnée.

## Analyse des délais {#delay-analytics}

Les composants Délai disposent des indicateurs suivants dans la vue d'analyse d'un Canvas actif ou précédemment actif.

| Indicateur | Description |
|---|---|
| _Entrées_ | Reflète le nombre de fois où l'étape a été atteinte. Si votre Canvas autorise la rééligibilité et qu'un utilisateur entre deux fois dans une étape Délai, deux entrées seront enregistrées. |
| _Passés à l'étape suivante_ | Reflète le nombre d'entrées qui sont passées à l'étape suivante dans le Canvas. |
| _Sortis du Canvas_ | Reflète le nombre d'entrées qui ont quitté le Canvas et ne sont pas passées à l'étape suivante. |
| _Échec de la personnalisation_ | Reflète le nombre de fois où un message ou contenu personnalisé destiné à un utilisateur n'a pas pu être délivré en raison des éléments suivants :<br> {::nomarkdown}<ul><li>La valeur du délai est dans le passé</li><li>La valeur du délai est à plus de 2 ans dans le futur</li><li>La valeur <b>Après une durée</b> n'est pas un nombre</li><li>La valeur <b>Jusqu'à un jour spécifique</b> n'est pas une date ou une chaîne au format date</li></ul>{:/} <br>Consultez [Erreurs d'échec de personnalisation](#personaliztion-failed-errors) pour plus de détails. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analyse des délais" }

Les séries temporelles de ces analyses sont disponibles dans la vue détaillée du composant.

## Résolution des problèmes

### Erreurs d'échec de personnalisation {#personaliztion-failed-errors}

Si les utilisateurs ne déclenchent pas un délai personnalisé, cela peut être dû au fait que l'étape Context que vous avez configurée pour les qualifier pour l'étape Délai ne fonctionne pas comme prévu. Lorsqu'une [variable de contexte est invalide]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/#troubleshooting), un utilisateur continuera à travers votre Canvas sans que son contexte soit défini par l'étape Context. Cela peut l'empêcher de se qualifier pour des étapes ultérieures de votre Canvas, comme les délais personnalisés.

### Utilisateurs dans une étape Délai lorsqu'un Canvas est arrêté

Lorsque vous [arrêtez un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch/#stopping-canvases), les utilisateurs qui attendent déjà dans une étape Délai ne sont pas immédiatement sortis. Braze planifie toujours la fin du délai, mais **aucun message supplémentaire n'est envoyé** tant que le Canvas est arrêté.

Si vous réactivez le Canvas avant que le délai d'un utilisateur ne soit écoulé, celui-ci peut avancer à l'étape suivante comme prévu. Si la fenêtre de délai est déjà passée pendant que le Canvas était arrêté, ces utilisateurs quittent le Canvas au lieu de recevoir l'étape suivante. Pour des exemples, consultez [Que se passe-t-il lorsque vous arrêtez un Canvas ?]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#what-happens-when-you-stop-a-canvas) et [Arrêter des Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch/#stopping-canvases).