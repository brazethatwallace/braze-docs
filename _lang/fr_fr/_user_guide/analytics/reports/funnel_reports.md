---
nav_title: Rapports d'entonnoir
article_title: Rapports d'entonnoir pour les campagnes et les Canvas
page_order: 8
page_type: reference
description: "Cette page présente les avantages des rapports d'entonnoir, comment les configurer et comment interpréter votre rapport."
tool: Reports
---

# Rapports d'entonnoir {#funnel-reports}

> La page **Rapport d'entonnoir** propose un rapport visuel qui vous permet d'analyser les parcours de vos clients après la réception d'une campagne ou d'un Canvas, y compris les différentes actions effectuées sur le chemin de la conversion et les points d'abandon. ![Capture d'écran de la page Rapport d'entonnoir montrant un tunnel de conversion pour les performances d'une campagne ou d'un Canvas]({% image_buster /assets/img/funnel_report/funnel_report2.png %}){: style="float:right;max-width:15%;margin-bottom:15px; border: 0"}

Si votre campagne ou Canvas utilise un groupe de contrôle ou plusieurs variantes, vous pouvez comprendre comment les différentes variantes ont influencé le tunnel de conversion à un niveau plus granulaire et optimiser en fonction de ces données.

![Rapport d'entonnoir 1]({% image_buster /assets/img/funnel_report/funnel_report1.jpg %}){: style="max-width:80%;"}

## Cas d'utilisation {#use-cases}

Les rapports d'entonnoir peuvent répondre à des questions telles que :

- **Onboarding :** après l'envoi d'un Canvas « Bienvenue, nouveau venu ! », combien d'utilisateurs ont complété chaque étape du parcours d'onboarding ?
- **Finalisation d'achat :** où les abandons d'achat se sont-ils produits pour une promotion saisonnière ?
- **Conversions personnalisées :** quelle proportion d'utilisateurs a démarré une session, écouté un titre et créé une playlist après un push « Nouvelle sortie » ?
- **Abandons d'upsell :** dans un Canvas d'upsell, à quel moment les utilisateurs ont-ils quitté le parcours avant de s'abonner ?
- **Comportements post-engagement :** quelle variante d'e-mail a généré le plus d'achats après ouverture ?
- **Fréquence de conversion :** quel pourcentage d'utilisateurs a parrainé un ami au moins trois fois après avoir reçu une campagne ?

## Configurer les rapports d'entonnoir {#setting-up-funnel-reports}

![Rapport d'entonnoir 5]({% image_buster /assets/img/funnel_report/canvas_campaign.png %}){: style="float:right;max-width:40%;border:0;margin-left:15px;"}

Vous pouvez exécuter des rapports d'entonnoir pour les campagnes et Canvas actifs existants. Ces rapports affichent une série d'événements par lesquels un destinataire de campagne progresse sur une période de 1 à 30 jours à partir de la date d'entrée dans le Canvas ou la campagne. Un utilisateur est considéré comme converti à une étape de l'entonnoir s'il effectue l'événement dans l'ordre spécifié.

Les rapports d'entonnoir sont disponibles aux emplacements suivants dans le tableau de bord :

- La page **Campaign Analytics** pour une campagne spécifique
- La page **Canvas Details** pour un Canvas spécifique, en sélectionnant le bouton **Analyze Variants**

{% alert important %}
Les rapports d'entonnoir ne sont pas disponibles pour les [campagnes API]({{site.baseurl}}/api/api_campaigns).
{% endalert %}

### Étape 1 : Sélectionner une plage de dates {#step-1-select-a-date-range}

Vous pouvez sélectionner une période pour votre rapport (au cours des six derniers mois) et affiner les données pour voir les utilisateurs qui, en entrant dans la campagne ou le Canvas, ont complété les événements de l'entonnoir dans une fenêtre définie (maximum 30 jours). Dans l'exemple suivant, votre entonnoir rechercherait les utilisateurs ayant reçu cette campagne ou ce Canvas au cours des sept derniers jours et ayant complété l'entonnoir en trois jours.

{% alert note %}
Si vous définissez la fenêtre de complétion de l'entonnoir à un jour, l'événement de l'entonnoir doit se produire dans les 24 heures suivant la réception du message. Cependant, si vous sélectionnez plusieurs jours, la fenêtre de temps est comptée en jours calendaires dans le fuseau horaire de l'entreprise.
{% endalert %}

![Rapport d'entonnoir pour un Canvas avec « 7 derniers jours » sélectionné dans le menu déroulant de la période.]({% image_buster /assets/img/funnel_report/funnel_report5.png %}){: style="max-width:90%;"}

### Étape 2 : Sélectionner les événements pour les étapes de l'entonnoir {#step-2-select-events-for-funnel-steps}

Pour chaque rapport d'entonnoir, le premier événement est la réception du message par l'utilisateur. À partir de là, les événements suivants que vous choisissez filtrent le nombre d'utilisateurs ayant effectué ces événements, ainsi que les événements précédents.

#### Événements disponibles pour les rapports d'entonnoir {#available-funnel-report-events}

| Campaign | Démarrage de session, Achat effectué, Événement personnalisé effectué, Événement d'engagement lié aux messages |
| Canvas | Démarrage de session, Achat effectué, Événement personnalisé effectué, Étape du Canvas reçue, Interaction avec l'étape |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Événements disponibles pour les rapports d'entonnoir" }

{% alert note %}
L'événement de rapport **Interaction avec l'étape** ne peut être utilisé qu'avec les étapes du Canvas qui utilisent les canaux e-mail ou push.
{% endalert %}

![Rapport d'entonnoir pour un Canvas avec un menu déroulant des événements de rapport disponibles.]({% image_buster /assets/img/funnel_report/funnel_report3.png %}){: style="max-width:80%;"}

Les rapports d'entonnoir vous permettent de comparer le succès de vos messages au-delà des événements de conversion ou des événements d'engagement que vous avez initialement configurés. Ainsi, si vous n'avez pas ajouté un événement de conversion au départ, vous pouvez tout de même suivre les conversions pour cet événement à l'aide d'un entonnoir.

Par exemple, si vous sélectionnez une fenêtre de rapport de 14 jours, suivie des événements `Added to cart` et `Made purchase`, vous verrez à la fois le nombre d'utilisateurs ayant ajouté au panier dans les 14 jours suivant la réception du message et le nombre d'utilisateurs ayant ajouté au panier puis effectué un achat dans les 14 jours suivant la réception de la campagne.

Autre exemple : vous souhaitez peut-être connaître le pourcentage d'utilisateurs ayant converti sur un e-mail après avoir cliqué dessus. Pour calculer cela, vous pourriez créer un rapport où le deuxième événement est le clic sur votre e-mail et le troisième événement est l'exécution de votre événement de conversion.

Après avoir sélectionné **Build Report**, le rapport d'entonnoir peut prendre plusieurs minutes à se générer. Pendant ce temps, vous pouvez naviguer vers d'autres pages du tableau de bord. Vous recevrez une notification dans le tableau de bord lorsque votre rapport sera prêt.

## Interpréter votre rapport d'entonnoir {#interpreting-your-funnel-report}

Dans votre rapport d'entonnoir, vous pouvez comparer directement le groupe de contrôle avec les variantes que vous avez configurées. Chaque événement consécutif indique le pourcentage des utilisateurs précédents ayant effectué cette action et converti à travers l'entonnoir.

### Composants du rapport d'entonnoir {#funnel-report-components}

- **Axe horizontal** : affiche le pourcentage de destinataires du message ayant effectué ces actions.
- **Graphique** : affiche le nombre de messages reçus, le nombre d'utilisateurs ayant effectué les actions précédentes ainsi que l'action choisie, le taux de conversion et la variation en pourcentage par rapport au groupe de contrôle.
- **Option de régénération** : vous permet de régénérer votre rapport et indique la date de dernière génération du rapport actuel.
- **Variantes** : représentées par des colonnes colorées, les rapports d'entonnoir permettent jusqu'à 8 variantes et un groupe de contrôle. Par défaut, le **graphique** n'affiche que trois variantes. Pour en voir davantage, vous pouvez sélectionner manuellement les autres variantes.

![Graphique du rapport d'entonnoir.]({% image_buster /assets/img/funnel_report/funnel_report4.jpg %})

**Pour les campagnes avec plusieurs variantes** : Braze affichera un tableau avec les indicateurs pour chaque événement et variante, ainsi que la variation en pourcentage par rapport au groupe de contrôle. Le taux de conversion correspond au nombre d'utilisateurs ayant effectué l'événement (et les suivants) par destinataire du message.

**Pour les campagnes avec rééligibilité** : si un utilisateur reçoit la campagne plus d'une fois dans la fenêtre de rapport, Braze déterminera si l'utilisateur doit être inclus dans l'entonnoir en fonction des actions effectuées après la première réception de la campagne dans la fenêtre de temps.
- Notez qu'il peut y avoir un écart entre les valeurs de conversion de l'entonnoir et les valeurs de conversion standard, car les utilisateurs peuvent convertir plus d'une fois avec la rééligibilité, mais les rapports d'entonnoir comptabilisent au maximum une conversion même si un utilisateur effectue l'événement plus d'une fois.

**Pour les campagnes multivariantes avec rééligibilité** : si un utilisateur reçoit plusieurs variantes de la campagne pendant la fenêtre de rapport, Braze déterminera s'il doit être inclus dans l'entonnoir de la variante en fonction des actions effectuées après la première réception de la variante de campagne. Cela signifie qu'un même utilisateur pourrait être comptabilisé dans plusieurs variantes différentes s'il a reçu plusieurs variantes pendant la fenêtre de temps de l'entonnoir.

{% alert important %}
Les utilisateurs orphelins ne sont pas suivis dans les rapports d'entonnoir. Lorsqu'un utilisateur anonyme entre dans un Canvas ou une campagne et devient ensuite identifié via la méthode `changeUser()`, son identifiant Braze change. Les rapports d'entonnoir ne suivent que les événements ultérieurs correspondant à l'identifiant utilisateur au moment de l'entrée et ne tiennent pas compte des événements effectués par l'utilisateur après le changement d'identifiant. Cela signifie que les événements de conversion effectués par l'utilisateur après son identification ne seront pas inclus dans le rapport d'entonnoir.
{% endalert %}

## Questions fréquentes {#frequently-asked-questions}

### Un utilisateur sort-il du rapport s'il saute un événement ? {#does-a-user-fall-out-of-the-report-if-they-skip-an-event}

Oui. Un utilisateur quitte l'entonnoir à la première étape où il n'effectue pas l'événement suivant dans la séquence exacte que vous avez configurée.

### Combien d'événements puis-je inclure dans un rapport d'entonnoir ? {#how-many-events-can-i-include-in-a-funnel-report}

Il n'y a pas de limite stricte, mais quatre à six événements couvrent la plupart des cas d'utilisation. Les entonnoirs très longs peuvent être lents ou expirer.

### Quels canaux prennent en charge l'événement d'entonnoir **Interaction avec l'étape** ? {#what-channels-support-the-interacted-with-step-funnel-event}

**Interaction avec l'étape** est disponible pour les étapes du Canvas qui utilisent les canaux **e-mail** ou **push**.

### Pourquoi mon rapport d'entonnoir met-il longtemps à charger ? {#why-is-my-funnel-report-taking-a-long-time-to-load}

Les requêtes volumineuses peuvent expirer. Essayez une fenêtre de rapport plus courte, moins d'étapes d'entonnoir, ou les deux.

### Pourquoi les analyses du Canvas diffèrent-elles du rapport d'entonnoir ? {#why-are-the-analytics-on-the-canvas-different-from-the-funnel-report}

Les analyses des étapes du Canvas peuvent afficher des chiffres plus élevés que l'entonnoir pour les mêmes dates calendaires, car les analyses des étapes incluent un engagement et des conversions plus larges, tandis que l'entonnoir impose un ordre des événements et des règles de temporalité.

#### Analyses du Canvas (Analyze Variants) {#canvas-analytics-analyze-variants}

La plage de dates filtre les événements par **date de survenue**. Si vous sélectionnez du 1er au 7 janvier, vous verrez toutes les entrées et tous les événements de conversion survenus pendant cette fenêtre, indépendamment de la date d'entrée de l'utilisateur dans le Canvas. Un utilisateur entré le 1er janvier mais ayant converti le 8 janvier afficherait une entrée et zéro conversion, car la conversion est survenue en dehors des dates sélectionnées. La fenêtre de conversion configurée sur l'étape du Canvas peut s'étendre au-delà de la fenêtre de suivi maximale de l'entonnoir, de sorte que les analyses au niveau de l'étape peuvent capturer des conversions sur un horizon plus long.

#### Rapports d'entonnoir

La plage de dates filtre les utilisateurs par **date d'entrée** dans le Canvas. Si vous sélectionnez du 1er au 7 janvier, le rapport inclut chaque utilisateur entré pendant cette fenêtre, puis suit ses actions pendant la fenêtre de complétion de l'entonnoir que vous configurez (jusqu'à 30 jours après l'entrée). Le même utilisateur entré le 1er janvier et ayant converti le 8 janvier afficherait une entrée et une conversion, car la conversion s'est produite dans la fenêtre post-entrée.

De plus, les rapports d'entonnoir exigent que les événements se produisent dans l'ordre spécifié et comptabilisent chaque utilisateur au maximum une fois, tandis que les analyses du Canvas comptent toutes les conversions et l'engagement sans contrainte d'ordre.