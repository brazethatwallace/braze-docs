---
nav_title: Exemples
article_title: Exemples pour Decisioning Studio Go
page_order: 5
page_type: reference
description: "Passez en revue les types de programmes e-mail courants pour déterminer si Decisioning Studio Go est adapté à votre scénario."
---

# Exemples pour Decisioning Studio Go {#examples-for-decisioning-studio-go}

> Decisioning Studio Go fonctionne le mieux pour les programmes e-mail récurrents où l'agent a le temps d'apprendre à partir de l'engagement et où votre contenu inclut suffisamment d'options de variantes pour une personnalisation significative. Cette page regroupe les cas d'usage courants d'e-mail par niveau d'adéquation, avec des exemples et des recommandations pour chacun.

Pour un aperçu du fonctionnement de Decisioning Studio Go, consultez [BrazeAI Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go).

Chaque exemple de ce guide est associé à l'un des niveaux d'adéquation suivants :

| Niveau d'adéquation | Description |
|---|---|
| **Idéal** | L'agent dispose de suffisamment de temps pour apprendre, votre audience est assez stable pour montrer une amélioration, et la personnalisation peut avoir un impact significatif sur l'engagement. Commencez ici. |
| **Compatible** | L'exemple peut bien fonctionner, mais le succès dépend du calendrier, de la taille de l'audience ou du séquençage. Examinez les considérations avant de vous engager. |
| **Non recommandé** | L'exemple entre en conflit avec la façon dont l'agent apprend. Choisissez un autre type de programme, ou échangez avec votre gestionnaire du succès des clients ou votre consultant en solutions pour envisager une configuration différente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Niveaux d'adéquation" }

{% alert note %}
Quel que soit le niveau d'adéquation, l'agent apprend mieux lorsque votre audience génère suffisamment de signaux d'engagement pour que l'algorithme détecte des tendances. En règle générale, visez des audiences cibles de plusieurs dizaines de milliers d'utilisateurs ou plus, avec un volume d'envoi hebdomadaire régulier. L'agent peut fonctionner avec des audiences plus petites, mais attendez-vous à une période d'apprentissage plus longue et à une amélioration moins fiable. Votre gestionnaire du succès des clients ou votre consultant en solutions peut vous aider à confirmer si une audience donnée est dimensionnée de manière appropriée.
{% endalert %}

## Idéal {#best-fit}

### Campaigns calendaires permanentes {#always-on-calendared-campaigns}

| Sujet | Détails |
|---|---|
| À quoi cela ressemble | Un calendrier marketing qui s'étend sur plusieurs mois ou plus, avec du contenu ajouté et retiré au fil du temps — par exemple, un calendrier pour les membres d'un programme de fidélité, un planning de diffusion de contenu, ou un calendrier lifestyle ou d'inspiration. |
| Pourquoi c'est adapté | Les programmes de longue durée donnent à l'agent le temps d'apprendre ce qui fonctionne pour différents utilisateurs. L'audience est stable, le contenu est actualisé régulièrement, et les clics sont généralement un indicateur significatif d'engagement. |
| Ce qu'il faut préparer | Plusieurs créations de base ou ensembles de variantes que vous êtes à l'aise de faire tourner. L'agent sélectionne la version qui fonctionne pour chaque utilisateur, mais il a besoin de suffisamment de variété dans les options que vous fournissez. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaigns calendaires permanentes" }

### Programmes permanents {#evergreen-programs}

| Sujet | Détails |
|---|---|
| À quoi cela ressemble | Des Campaigns continues qui ne sont pas liées à des dates ou événements spécifiques — réactivation, programmes de réengagement, relances de comptes inactifs ou célébrations de jalons. |
| Pourquoi c'est adapté | Comme les Campaigns calendaires, l'audience est dynamique mais le programme fonctionne indéfiniment. L'agent a le temps d'apprendre, le contenu est flexible, et les clics sont un indicateur avancé que l'agent peut optimiser. |
| Ce qu'il faut préparer | Des options de variantes pour la ligne d'objet et le CTA qui présentent le message sous différents angles de motivation. Les variantes d'images sont utiles si vous en disposez. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Programmes permanents" }

## Cas d'usage compatibles {#supported-use-cases}

### Promotions multi-e-mails {#multi-email-promotions}

| Sujet | Détails |
|---|---|
| À quoi cela ressemble | Un ensemble d'e-mails envoyés sur plusieurs semaines sous le même thème promotionnel — par exemple, une série de rentrée scolaire ou une promotion multi-semaines par catégorie. |
| Pourquoi ça fonctionne | Si la promotion dure suffisamment longtemps — au moins plusieurs semaines — l'agent a le temps d'apprendre au sein de la promotion. Le taux de clics est généralement un indicateur avancé solide de l'engagement promotionnel. |
| Considérations | Pour les promotions plus courtes, l'agent peut ne pas disposer de suffisamment de jours de données pour apprendre avant la fin du programme. En règle générale, l'agent a besoin d'au moins 10 jours de Campaign pour développer des recommandations solides. Si votre promotion est plus courte, demandez-vous si un programme permanent pourrait porter l'apprentissage à la place, puis appliquez ce que vous avez appris à la prochaine promotion. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Promotions multi-e-mails" }

### Parcours déclenchés par une action ou un événement {#action-or-event-driven-journeys}

| Sujet | Détails |
|---|---|
| À quoi cela ressemble | Un e-mail unique ou une séquence déclenchée par une action client — abandon de panier, abandon de navigation ou suivi post-achat. |
| Pourquoi ça fonctionne | Les déclencheurs créent un point d'entrée clair. Si le parcours est récurrent et que le volume d'audience est régulier, l'agent peut apprendre quel contenu fonctionne pour quels utilisateurs. |
| Considérations | Le timing est important. Si l'e-mail doit être envoyé dans les minutes suivant l'événement déclencheur, travaillez avec votre gestionnaire du succès des clients ou votre consultant en solutions pour confirmer que le calendrier d'envoi de l'agent est compatible. Si les utilisateurs doivent recevoir les e-mails dans un ordre spécifique (e-mail A avant e-mail B), vous devez orchestrer les mouvements d'audience vous-même — l'agent ne séquence pas les envois pour un même utilisateur au sein d'un parcours multi-e-mails. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Parcours déclenchés par une action ou un événement" }

## Non recommandé {#not-recommended}

### Séquences de drip {#drip-sequences}

| Sujet | Détails |
|---|---|
| À quoi cela ressemble | Une séquence multi-e-mails — par exemple, un tutoriel d'onboarding — où les utilisateurs doivent recevoir l'e-mail A, puis l'e-mail B, puis l'e-mail C dans l'ordre. |
| Pourquoi ce n'est pas adapté | L'agent sélectionne ce qu'il envoie à chaque utilisateur en fonction de ce qui est le plus susceptible de générer un clic pour cet utilisateur. Il ne modélise pas les exigences de séquençage. Si vous devez imposer un ordre spécifique, vous devez orchestrer l'audience vous-même (en déplaçant les utilisateurs de Segment en Segment après chaque e-mail), ce qui réduit la plupart des avantages de l'utilisation de l'agent. L'agent ne peut pas non plus confirmer de manière indépendante que l'e-mail A a réussi avant d'envoyer l'e-mail B. |
| Que faire à la place | Utilisez [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) pour orchestrer le drip. Si vous souhaitez une optimisation par IA au sein d'un drip, échangez avec votre gestionnaire du succès des clients ou votre consultant en solutions pour savoir si [Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/get_started) est plus adapté. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Séquences de drip" }

### Envois e-mail ponctuels {#one-time-email-blasts}

| Sujet | Détails |
|---|---|
| À quoi cela ressemble | Un e-mail unique envoyé en une seule fois — une annonce Black Friday, un lancement de nouveau produit ou une communication d'entreprise ponctuelle. |
| Pourquoi ce n'est pas adapté | L'agent a besoin de temps pour apprendre. Un envoi unique ne lui donne aucune possibilité d'améliorer ses décisions avant la fin de la Campaign. Le temps qu'il accumule suffisamment de signaux d'engagement pour faire de meilleurs choix, le programme est terminé. |
| Que faire à la place | Si vous avez un programme permanent avec un contenu similaire — par exemple, un programme d'annonces de produits tout au long de l'année — utilisez Decisioning Studio Go pour celui-ci et appliquez ce que vous apprenez aux envois ponctuels. Pour un envoi véritablement ponctuel, le [test A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) ou la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) sont plus adaptés. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Envois e-mail ponctuels" }

## En un coup d'œil {#at-a-glance}

| Scénario | Adéquation | Considération clé |
|---|---|---|
| Campaigns calendaires permanentes | Idéal | Fournissez plusieurs créations de base ou ensembles de variantes à actualiser au fil du temps. |
| Programmes permanents (réactivation, réengagement) | Idéal | Fournissez des options de variantes qui présentent le même message sous différents angles de motivation. |
| Promotions multi-e-mails | Compatible | Visez au moins 10 jours de Campaign ; les promotions plus courtes limitent l'apprentissage. |
| Parcours déclenchés par une action ou un événement | Compatible | Confirmez les exigences de timing d'envoi ; vous êtes responsable de l'application du séquençage. |
| Séquences de drip (tutoriels d'onboarding) | Non recommandé | Utilisez Canvas pour le séquençage ; envisagez Decisioning Studio Pro pour l'optimisation au sein du drip. |
| Envois e-mail ponctuels | Non recommandé | Utilisez le test A/B ou la sélection intelligente à la place. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tableau récapitulatif des exemples" }

## Prochaines étapes {#next-steps}

Contactez votre gestionnaire du succès des clients ou votre consultant en solutions Braze si vous n'êtes pas sûr que votre programme soit adapté. Les signaux forts incluent :

- L'audience reçoit des e-mails régulièrement — au moins chaque semaine — sur une période d'un mois ou plus.
- L'audience est suffisamment large pour générer un signal d'engagement régulier (plusieurs dizaines de milliers d'utilisateurs est un objectif de départ utile).
- Vous disposez d'au moins deux ou trois options de variantes significatives à proposer (lignes d'objet, CTA ou images qui présentent le message différemment).
- Les clics sont un indicateur avancé de la valeur commerciale pour ce programme, pas simplement une métrique de vanité.
- Le Segment n'est pas activement utilisé par un autre Canvas ou une autre Campaign qui serait en concurrence pour l'engagement des mêmes utilisateurs.