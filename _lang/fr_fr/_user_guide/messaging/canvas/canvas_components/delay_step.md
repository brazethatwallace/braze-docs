---
nav_title: Délai
article_title: Délai
alias: "/delay_step/"
page_order: 8
page_type: reference
description: "Cet article de référence explique comment ajouter un délai à votre Canvas sans avoir besoin d'ajouter un message associé."
tool: Canvas

---

# Délai {#delay}

> Les composants Délai vous permettent d'ajouter un délai autonome à un Canvas. Vous pouvez ajouter un délai à votre Canvas sans avoir besoin d'ajouter un message associé.

Les délais peuvent rendre votre Canvas plus lisible. Vous pouvez également utiliser ce composant pour retarder une étape différente jusqu'à une date exacte, un jour spécifique ou un jour spécifique de la semaine. Un composant Délai peut être connecté à une seule étape suivante au maximum. <br> ![Une étape Délai avec un délai d'un jour comme première étape d'un Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Créer un délai {#create-a-delay}

Pour créer un délai, ajoutez une étape à votre Canvas. Glissez-déposez le composant Délai depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape, puis choisissez **Delay**.

### Délais prolongés {#extended-delays}

Vous pouvez prolonger les étapes de délai jusqu'à deux ans (730 jours). Par exemple, si vous effectuez l'onboarding de nouveaux utilisateurs pour votre application, vous pouvez ajouter un délai prolongé de deux mois avant d'envoyer une étape de message pour relancer les utilisateurs qui n'ont pas démarré de session.

## Types de délai {#time-delay-types}

Vous pouvez choisir le type de délai avant le prochain message dans votre Canvas. Vous pouvez soit définir un délai pour que vos utilisateurs attendent pendant une période déterminée, soit les retenir jusqu'à une date et une heure spécifiques.

S'il y a un délai, il est normal que certains utilisateurs ne passent à l'étape suivante du Canvas qu'après ce délai. Les utilisateurs en attente ne seront pas comptabilisés dans l'indicateur _Proceeded to Next Step_. Pour plus d'informations, consultez [Analyse des délais](#delay-analytics).

{% tabs %}
{% tab Durée %}

Sélectionner **Durée** vous permet de retenir les utilisateurs pendant un nombre défini de secondes, minutes, heures, jours ou semaines, et à une heure spécifique. Par exemple, vous pouvez retenir les utilisateurs pendant quatre heures ou pendant un jour.

Notez la différence entre le calcul des « jours » et des « jours calendaires ».

- Un « jour » correspond à 24 heures et est calculé à partir du moment où l'utilisateur entre dans l'étape de délai.
- Un « jour calendaire » définit le temps d'attente jusqu'à la prochaine heure spécifiée, qui peut être inférieur à 24 heures. Vous pouvez choisir de retenir selon l'heure de l'entreprise ou l'heure locale de l'utilisateur. Si aucune heure n'est spécifiée, l'utilisateur est retenu jusqu'à minuit le jour suivant, selon l'heure de l'entreprise.

### Comportement du délai : « jours calendaires » à une heure spécifique versus « jours » {#delay-behavior-calendar-days-at-a-specific-time-versus-days}

Lorsque vous sélectionnez **jours calendaires** comme unité et activez **À une heure spécifique** (par exemple, **1 jour calendaire à 9 h**), Canvas calcule d'abord la date calendaire cible, puis applique l'heure planifiée. Par exemple, si une étape Canvas envoie à 21 h le lundi et que l'étape de délai est définie sur **1 jour calendaire à 9 h**, l'étape suivante envoie à 9 h le mardi. Canvas calcule lundi + 1 jour calendaire = mardi, puis applique l'heure de 9 h.

En revanche, lorsque vous sélectionnez **jours** comme unité sans **À une heure spécifique** (par exemple, **Après 1 jour**), Canvas attend une période complète de 24 heures à partir du moment où l'utilisateur entre dans l'étape de délai. Par exemple, si une étape envoie à 9 h 35 le 13 octobre et que l'étape de délai est **Après 1 jour**, l'étape suivante envoie à 9 h 35 le 14 octobre.

Vous pouvez également sélectionner **À une heure spécifique** pour définir quand les utilisateurs avancent dans le Canvas. Cette option prend en compte l'heure à laquelle l'utilisateur est entré dans l'étape de délai. Si cette heure dépasse l'heure configurée dans les paramètres, Braze ajoute des heures supplémentaires au délai.

Par exemple, supposons que nous sommes le 11 décembre et que notre étape de délai est définie sur une **Durée** d'une semaine à 8 h UTC. Si un utilisateur entre dans l'étape de délai le 4 décembre, il est libéré de l'étape de délai pour poursuivre son parcours aujourd'hui s'il est entré initialement dans l'étape de délai avant 8 h UTC. S'il est entré dans l'étape de délai après cette heure, l'utilisateur est retenu jusqu'au jour suivant (la prochaine occurrence de cette heure).

{% endtab %}
{% tab Date calendaire %}

Sélectionner **Date calendaire** vous permet de retenir les utilisateurs dans l'étape jusqu'à une date et une heure spécifiques.

### Considérations {#considerations}

#### Les utilisateurs ne recevront pas les étapes ou messages dont la date est passée {#users-wont-receive-past-dated-steps-or-messages}

Si la date et l'heure sélectionnées sont déjà passées au moment où les utilisateurs atteignent l'étape de délai, ils quittent le Canvas. Il peut y avoir jusqu'à 31 jours entre le début du Canvas et les dates choisies pour les étapes « attendre jusqu'à un jour précis ».

{% alert important %}
Si vous participez à l'[accès anticipé Canvas Context]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context), vous pouvez définir des délais allant jusqu'à 2 ans.
{% endalert %}

Par exemple, les utilisateurs ne recevront pas les étapes ou messages dans ces scénarios :

- Un message est planifié pour être envoyé le 3 mai à 21 h, mais l'étape de délai expire le 3 mai à 9 h.
- Une étape Canvas retient jusqu'à une heure spécifique dans le fuseau horaire local de l'utilisateur, mais les utilisateurs n'ont pas de fuseau horaire défini dans leur profil utilisateur. Le délai utilise alors par défaut le fuseau horaire de l'entreprise pour ces utilisateurs, et l'heure spécifiée est déjà passée.

#### Les utilisateurs quittent le Canvas si une étape de délai ultérieure se situe dans la période d'une étape de délai précédente {#users-exit-if-a-subsequent-delay-step-is-within-a-prior-delay-steps-timeline}

Si le Canvas comporte deux étapes de délai mais que la première est plus longue que la seconde, les utilisateurs quittent également le Canvas.

Par exemple, supposons qu'un Canvas comporte ces étapes :
- Étape 1 : étape de message
- Étape 2 : étape de délai jusqu'au 13 décembre à 22 h
- Étape 3 : étape de message
- Étape 4 : étape de délai jusqu'au 13 décembre à 19 h
- Étape 5 : étape de message

Les utilisateurs qui entrent dans l'étape 4 quittent le Canvas avant de recevoir l'étape 5, car le délai de l'étape 4 fait partie de la période de l'étape 2.

{% endtab %}
{% tab Jour de la semaine %}

Sélectionner **Jour de la semaine** vous permet de retenir les utilisateurs dans l'étape jusqu'à un jour spécifique de la semaine, à une heure spécifique. Par exemple, vous pouvez retenir les utilisateurs jusqu'au prochain jeudi à 16 h dans le fuseau horaire de l'entreprise.

Pour configurer correctement cette option, vous devez également sélectionner ce qui se passe si l'utilisateur entre dans le Canvas le jour de la semaine sélectionné (par exemple, jeudi), mais après l'heure spécifiée. Vous pouvez choisir de faire avancer l'utilisateur le même jour ou de le retenir jusqu'à la semaine suivante.
{% endtab %}
{% endtabs %}

### Mises à jour du profil pendant les délais {#profile-updates-during-delays}

Si un utilisateur entre dans un Canvas et ajoute une adresse e-mail valide pendant l'étape de délai avant qu'elle ne se termine, il recevra l'e-mail à l'étape suivante. Cela s'applique également aux autres mises à jour du profil. Toute modification des attributs utilisateur ou des informations de contact pendant le délai est prise en compte lorsque l'utilisateur passe aux étapes suivantes.

## Utiliser les étapes de délai {#using-delay-steps}

Imaginons que nous sommes le 10 juin. Le 11 juin, vous souhaitez que les utilisateurs entrent dans le Canvas et reçoivent un message concernant une promotion à venir. Ensuite, vous voulez maintenir les utilisateurs dans le Canvas jusqu'au 17 juin à 15 h, heure locale. À 15 h, heure locale, le 17 juin, vous souhaitez envoyer aux utilisateurs un message de rappel concernant la promotion.

La séquence d'étapes du Canvas pourrait ressembler à ce qui suit :

1. Commencez par ajouter une étape Message qui s'envoie immédiatement après que les utilisateurs entrent dans le Canvas le 11 juin.
2. Créez une étape de délai qui maintient les utilisateurs jusqu'à 13 h, heure locale, le 17 juin.
3. Reliez l'étape de délai à une autre étape Message qui envoie son message immédiatement.

### Composants de délai à la fin d'un Canvas {#delay-as-last-step}

Si vous ajoutez un composant de délai à votre Canvas et qu'il n'y a pas d'étapes suivantes, tout utilisateur qui atteint la dernière étape est automatiquement sorti du Canvas. Cela est vrai même si le temps de l'étape de délai n'a pas encore été atteint. Cela signifie que les utilisateurs qui ont déjà atteint l'étape de délai ne recevront pas les messages que vous ajoutez après cette étape. Cependant, si un utilisateur n'a pas encore atteint l'étape de délai et qu'un message est ajouté, il recevra ce message.

### Délais personnalisés {#personalized-delays}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The personalized delays and extended delays feature' %}

Sélectionnez le bouton **Personnaliser le délai** pour configurer un délai personnalisé pour vos utilisateurs. Vous pouvez l'utiliser avec une [étape de contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) pour sélectionner la variable de contexte selon laquelle appliquer le délai. Cela remplace l'heure de la journée définie dans l'attribut ou la propriété sélectionnée. C'est utile lorsque vous appliquez un décalage en jours ou en semaines et que vous souhaitez que les utilisateurs avancent à une heure précise. Le fuseau horaire provient de l'attribut ou de la propriété, ou utilise le fuseau horaire de secours si aucun n'est disponible.

#### Comportement du fuseau horaire pour « à une heure précise » {#time-zone-behavior-for-at-specific-time}

Lors de la configuration de délais personnalisés avec l'option **à une heure précise**, le comportement du fuseau horaire dépend du type de données de votre attribut ou variable de contexte :

- **Type de données chaîne de caractères avec fuseau horaire :** si l'attribut ou la variable de contexte est un type de données chaîne de caractères qui inclut des informations de fuseau horaire, il se conforme au fuseau horaire spécifié dans la chaîne. Par exemple, `2025-06-10T10:00:00-08:00` utilise UTC-8.
- **Type de données chaîne de caractères sans fuseau horaire :** si l'attribut ou la variable de contexte est un type de données chaîne de caractères sans informations de fuseau horaire, il se conforme au fuseau horaire de secours. Par exemple, `2025-06-10` utilise le fuseau horaire de secours.
- **Type de données temporel :** si l'attribut ou la variable de contexte est un type de données temporel, il se conforme à UTC. En effet, le type de données temporel est toujours converti en UTC lors de l'enregistrement dans la base de données, donc « à une heure précise » fait toujours référence à UTC lorsque la variable est définie sur le type de données temporel. Par exemple, `2025-06-10T10:00:00-08:00` utilise UTC+0.

{% alert note %}
Il est possible qu'un attribut personnalisé ou une variable de contexte n'ait ni heure précise ni fuseau horaire s'il s'agit d'un type de données chaîne de caractères. S'il s'agit d'un type de données temporel, vous devrez spécifier l'heure et le fuseau horaire. Cependant, si l'attribut personnalisé ou la variable de contexte est une chaîne « non pertinente » (comme « product_name »), l'utilisateur sort du Canvas.
{% endalert %}

#### Cas d'usage {#use-case}

Imaginons que vous souhaitez rappeler à vos clients d'acheter du dentifrice dans 30 jours. En utilisant une combinaison d'une étape de contexte et d'une étape de délai, vous pouvez sélectionner cette variable de contexte pour appliquer le délai. Dans ce cas, votre étape de contexte aurait les champs suivants :

- **Nom de la variable de contexte :** product_reminder_interval
- **Type de données :** Time
- **Valeur :** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![La variable « product_reminder_interval » et sa valeur.]({% image_buster /assets/img/context_step1.png %})

Ensuite, parce que vous souhaitez rappeler à vos clients dans 30 jours, vous sélectionnerez **Jusqu'à un jour précis** comme option de délai et sélectionnerez **Personnaliser le délai** pour utiliser les informations de votre étape de contexte. Cela signifie que vos utilisateurs sont mis en attente jusqu'à la variable de contexte sélectionnée.

## Analyse des délais {#delay-analytics}

Les composants de délai disposent des indicateurs suivants dans la vue d'analyse d'un Canvas actif ou précédemment actif.

| Indicateur | Description |
|---|---|
| _Entrées_ | Reflète le nombre de fois où l'étape a été atteinte. Si votre Canvas autorise la rééligibilité et qu'un utilisateur entre deux fois dans une étape de délai, deux entrées sont enregistrées. |
| _Passés à l'étape suivante_ | Reflète le nombre d'entrées qui sont passées à l'étape suivante du Canvas. |
| _Sortis du Canvas_ | Reflète le nombre d'entrées qui sont sorties du Canvas sans passer à l'étape suivante. |
| _Échec de la personnalisation_ | Reflète le nombre de fois où un message ou un contenu personnalisé destiné à un utilisateur n'a pas pu être livré pour les raisons suivantes :<br> {::nomarkdown}<ul><li>La valeur du délai est dans le passé</li><li>La valeur du délai est à plus de 2 ans dans le futur</li><li>La valeur <b>Après une durée</b> n'est pas un nombre</li><li>La valeur <b>Jusqu'à un jour spécifique</b> n'est pas une date ou une chaîne de caractères au format date</li></ul>{:/} <br>Consultez [Erreurs d'échec de personnalisation](#personaliztion-failed-errors) pour plus de détails. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analyse des délais" }

Les séries temporelles de ces analyses sont disponibles dans la vue étendue du composant.

## Résolution des problèmes {#troubleshooting}

### Erreurs d'échec de personnalisation {#personalization-failed-errors}

Si les utilisateurs ne déclenchent pas un délai personnalisé, il se peut que l'étape de contexte que vous avez configurée pour les qualifier pour l'étape de délai ne fonctionne pas comme prévu. Lorsqu'une [variable de contexte est invalide]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#troubleshooting), un utilisateur poursuit son parcours dans votre Canvas sans que son contexte soit défini par l'étape de contexte. Cela peut l'empêcher de se qualifier pour des étapes ultérieures de votre Canvas, telles que les délais personnalisés.

## Résolution des problèmes

### Utilisateurs dans une étape de délai lorsqu'un Canvas est arrêté {#users-in-a-delay-step-when-a-canvas-is-stopped}

Lorsque vous [arrêtez un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#stopping-canvases), les utilisateurs qui attendent déjà dans une étape de délai ne sont pas immédiatement retirés. Braze planifie toujours l'achèvement du délai, mais **aucun message supplémentaire n'est envoyé** tant que le Canvas est arrêté.

Si vous réactivez le Canvas avant que le délai d'un utilisateur ne soit écoulé, celui-ci peut passer à l'étape suivante comme prévu. Si la fenêtre de délai s'est déjà écoulée pendant que le Canvas était arrêté, ces utilisateurs quittent le Canvas au lieu de recevoir l'étape suivante. Pour des exemples, consultez [Que se passe-t-il lorsque vous arrêtez un Canvas ?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas) et [Arrêter des Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#stopping-canvases).