---
nav_title: Créer des tests
article_title: Créer des tests
page_order: 1
page_type: reference
description: "Cet article explique comment créer des tests multivariés et des tests A/B avec Braze."

local_redirect: #optimizations
  optimizations: '/docs/user_guide/messaging/ab_testing/optimizations'
---

# Créer des tests multivariés et des tests A/B {#creating-tests}

> Vous pouvez créer un test multivarié ou un test A/B pour toute campagne ciblant un seul canal. Par exemple, si vous souhaitez utiliser un test multivarié ou un test A/B pour une campagne push, vous pouvez cibler les appareils iOS et Android dans la même campagne.

![Le menu déroulant qui s'affiche lorsque vous sélectionnez le bouton « Créer une campagne » pour choisir entre multicanal et canal unique.]({% image_buster /assets/img/ab_create_1.png %}){: style="max-width:25%;float:right;margin-left:15px;" }

## Étape 1 : Créer votre campagne {#step-1-create-your-campaign}

1. Accédez à **Messaging** > **Campaigns**.
2. Sélectionnez **Create Campaign** et choisissez un canal pour la campagne dans la section qui permet les tests multivariés et A/B. Pour une documentation détaillée sur chaque canal de communication, consultez [Créer une campagne]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/).

## Étape 2 : Rédiger vos variantes {#step-2-compose-your-variants}

Vous pouvez créer jusqu'à huit variantes de votre message, en différenciant les titres, le contenu, les images, et plus encore. Le nombre de différences entre les messages détermine s'il s'agit d'un test multivarié ou d'un test A/B. Un test A/B examine l'effet de la modification d'une seule variable, tandis qu'un test multivarié en examine deux ou plus.

Pour des idées sur la façon de différencier vos variantes, consultez [Conseils pour les différents canaux](#tips-different-channels).

![Sélection de « Ajouter une variante » pour une campagne.]({% image_buster /assets/img/ab_create_2.png %})

## Étape 3 : Planifier votre campagne {#step-3-schedule-your-campaign}

La planification de votre campagne multivariée fonctionne de la même manière que pour toute autre campagne Braze. Tous les [types de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/) standard sont disponibles.

Une fois qu'un test multivarié a commencé, vous ne pouvez plus modifier la campagne. Si vous changez les paramètres, comme la ligne d'objet ou le corps HTML, Braze considère l'expérience comme compromise et la désactive immédiatement.

{% alert important %}
Pour utiliser une [optimisation]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations/) (disponible pour certains canaux), planifiez votre campagne pour un envoi unique. Les optimisations ne sont pas disponibles pour les campagnes récurrentes ou celles pour lesquelles la rééligibilité est activée.
{% endalert %}

## Étape 4 : Choisir un segment et répartir vos utilisateurs entre les variantes {#step-4-choose-a-segment-and-distribute-your-users-across-variants}

Sélectionnez les segments à cibler, puis répartissez les membres entre vos variantes sélectionnées et le [groupe de contrôle](#including-a-control-group) facultatif. Pour les bonnes pratiques concernant le choix d'un segment pour vos tests, consultez [Choisir un segment](#choosing-a-segment).

Pour les campagnes push, e-mail et webhook planifiées pour un envoi unique, vous pouvez également utiliser une [optimisation]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations/). Une optimisation réserve une partie de votre audience cible en dehors du test A/B et la conserve pour un second envoi optimisé basé sur les résultats du premier test.

### Groupe de contrôle {#including-a-control-group}

Vous pouvez réserver un pourcentage de votre audience cible pour un groupe de contrôle aléatoire. Les utilisateurs du groupe de contrôle ne reçoivent pas le test, mais Braze surveille leur taux de conversion pendant toute la durée de la campagne.

Lorsque vous consultez vos résultats, vous pouvez comparer les taux de conversion de vos variantes avec un taux de conversion de référence fourni par votre groupe de contrôle. Cela vous permet de comparer à la fois les effets de vos variantes et les effets de vos variantes par rapport au taux de conversion qui aurait résulté de l'absence totale d'envoi de message.

![Panneau de test A/B montrant la répartition en pourcentage du groupe de contrôle, de la variante 1, de la variante 2 et de la variante 3, avec 25 % pour chaque groupe.]({% image_buster /assets/img/ab_create_4.png %})

{% alert important %}
L'utilisation d'un groupe de contrôle pour déterminer un gagnant par les *ouvertures* ou les *clics* n'est pas recommandée. Étant donné que le groupe de contrôle ne reçoit pas le message, ces utilisateurs ne peuvent effectuer aucune ouverture ni aucun clic. Par conséquent, le taux de conversion de ce groupe est de 0 % par définition et ne constitue pas une comparaison pertinente avec les variantes.
{% endalert %}

#### Groupes de contrôle avec les tests A/B {#control-groups-with-ab-testing}

Lorsque vous utilisez une limite de débit avec un test A/B, la limite de débit n'est pas appliquée au groupe de contrôle de la même manière qu'au groupe de test, ce qui constitue une source potentielle de biais temporel. Utilisez des fenêtres de conversion appropriées pour éviter ce biais.

#### Groupes de contrôle avec la Sélection intelligente {#control-groups-with-intelligent-selection}

La taille du groupe de contrôle pour une campagne avec la [Sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/) est basée sur le nombre de variantes. Si chaque variante est envoyée à plus de 20 % des utilisateurs, le groupe de contrôle représente 20 % et les variantes sont réparties équitablement sur les 80 % restants. Cependant, si vous avez suffisamment de variantes pour que chacune soit envoyée à moins de 20 % des utilisateurs, le groupe de contrôle doit être réduit. Lorsque la Sélection intelligente commence à analyser les performances de votre test, le groupe de contrôle augmente ou diminue en fonction des résultats.

## Étape 5 : Définir un événement de conversion (facultatif) {#step-5-designate-a-conversion-event-optional}

Définir un événement de conversion pour une campagne vous permet de voir combien de destinataires de cette campagne ont effectué une action particulière après l'avoir reçue.

Cela n'affecte le test que si vous avez choisi **Primary Conversion Rate** dans les étapes précédentes. Pour plus d'informations, consultez [Événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/).

## Étape 6 : Vérifier et lancer {#step-6-review-and-launch}

Sur la page de confirmation, vérifiez les détails de votre campagne multivariée et lancez le test ! Ensuite, découvrez comment [comprendre les résultats de votre test]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/).

## Bon à savoir {#things-to-know}

Si votre expérience a déjà commencé l'envoi et que vous modifiez le message, l'expérience est invalidée et tous les résultats de l'expérience sont supprimés.

- Pour éviter toute interférence avec le comportement attendu de l'expérience, nous recommandons de ne pas modifier les messages dans l'heure qui suit le lancement de la campagne d'expérience.
- Si votre expérience est terminée et que vous modifiez le message après l'envoi, les résultats de l'expérience restent disponibles dans l'analytique de votre tableau de bord. Cependant, si vous relancez la campagne, les résultats de l'expérience sont supprimés.

### Conseils pour les différents canaux {#tips-different-channels}

Selon le canal que vous sélectionnez, vous pouvez tester différents composants de votre message. Par exemple, essayez de rédiger des variantes en ayant une idée de ce que vous souhaitez tester et de ce que vous espérez prouver. Quels leviers pouvez-vous actionner et quels sont les effets souhaités ? Bien qu'il existe des millions de possibilités à explorer avec un test multivarié ou A/B, voici quelques suggestions pour vous lancer :

| Canal | Aspects du message que vous pouvez modifier | Résultats à observer |
| ---------------------| --------------- | ------------- |
| Push | Texte <br> Utilisation d'images et d'emojis <br> Liens profonds <br> Présentation des chiffres (par exemple, « triple » versus « augmentation de 200 % ») <br> Présentation du temps (par exemple, « se termine à minuit » versus « se termine dans 6 heures ») | Ouvertures <br> Taux de conversion |
| E-mail | Objet <br> Nom d'affichage <br> Formule de salutation <br> Corps du texte <br> Utilisation d'images et d'emojis <br> Présentation des chiffres (par exemple, « triple » versus « augmentation de 200 % ») <br> Présentation du temps (par exemple, « se termine à minuit » versus « se termine dans 6 heures ») | Ouvertures <br> Taux de conversion |
| Message in-app | Aspects listés pour « push » <br> [Spécifications des images de messages in-app]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/#in-app-messages) | Clics <br> Taux de conversion |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Conseils pour les différents canaux" }

{% alert tip %}
Lorsque vous effectuez des tests A/B, n'oubliez pas de générer des [rapports d'entonnoir]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/) qui vous permettent de comprendre comment chaque variante a impacté votre tunnel de conversion, surtout si la « conversion » pour votre entreprise implique plusieurs étapes ou actions.
{% endalert %}

De plus, la durée idéale de votre test peut varier selon le canal. Gardez à l'esprit le temps moyen dont la plupart des utilisateurs ont besoin pour interagir avec chaque canal.

Par exemple, si vous testez une notification push, vous pouvez obtenir des résultats significatifs plus rapidement qu'avec un test par e-mail, car les utilisateurs voient les notifications push immédiatement, alors qu'il peut s'écouler plusieurs jours avant qu'ils ne voient ou n'ouvrent un e-mail. Si vous testez des messages in-app, gardez à l'esprit que les utilisateurs doivent ouvrir l'application pour voir la campagne. Vous devriez donc attendre plus longtemps pour collecter les résultats, aussi bien de vos utilisateurs les plus actifs que de vos utilisateurs plus occasionnels.

Si vous n'êtes pas sûr de la durée idéale de votre test, la fonctionnalité [Sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/) peut être utile pour identifier efficacement une variante gagnante.

### Choisir un segment {#choosing-a-segment}

Étant donné que différents segments de vos utilisateurs peuvent réagir différemment aux messages, le succès d'un message particulier en dit long à la fois sur le message lui-même et sur son segment cible. Essayez donc de concevoir un test en gardant votre segment cible à l'esprit.

Par exemple, les utilisateurs actifs peuvent réagir de manière similaire à « Cette offre expire demain ! » et « Cette offre expire dans 24 heures ! », mais les utilisateurs qui n'ont pas ouvert l'application depuis une semaine pourraient être plus réceptifs à la seconde formulation, car elle crée un plus grand sentiment d'urgence.

De plus, lorsque vous choisissez le segment sur lequel effectuer votre test, assurez-vous que la taille de ce segment est suffisamment grande. En général, les tests multivariés et A/B comportant davantage de variantes nécessitent un groupe de test plus important pour obtenir des résultats statistiquement significatifs. En effet, plus il y a de variantes, moins d'utilisateurs voient chaque variante individuelle.

{% alert tip %}
À titre indicatif, vous avez probablement besoin d'environ 15 000 utilisateurs par variante (y compris le groupe de contrôle) pour atteindre un niveau de confiance de 95 % dans les résultats de votre test. Cependant, le nombre exact d'utilisateurs nécessaires peut être supérieur ou inférieur, selon votre cas particulier. Pour des indications plus précises sur la taille des échantillons par variante, envisagez d'utiliser un [calculateur de taille d'échantillon](https://www.calculator.net/sample-size-calculator.html).
{% endalert %}

### Biais et randomisation {#bias-and-randomization}

Une question fréquente concernant l'affectation aux groupes de contrôle et de test est de savoir si cela peut introduire un biais dans vos tests. D'autres se demandent parfois comment nous savons si ces affectations sont véritablement aléatoires.

Les utilisateurs sont affectés aux variantes de message, aux variantes de Canvas ou à leurs groupes de contrôle respectifs en concaténant leur ID utilisateur (généré aléatoirement) avec l'ID de la campagne ou du Canvas (également généré aléatoirement), en prenant le modulo 100 de cette valeur, puis en classant les utilisateurs dans des tranches correspondant aux pourcentages d'affectation des variantes et du groupe de contrôle facultatif définis dans le tableau de bord. Il n'y a donc aucun moyen pratique pour que les comportements des utilisateurs avant la création d'une campagne ou d'un Canvas particulier varient systématiquement entre les variantes et le groupe de contrôle. Il n'est pas non plus possible d'être plus aléatoire (ou plus précisément, pseudo-aléatoire) que cette implémentation.

#### Erreurs à éviter {#mistakes-to-avoid}

Il existe certaines erreurs courantes qui peuvent créer l'apparence de différences basées sur le canal de communication si les audiences ne sont pas correctement filtrées.

Par exemple, si vous envoyez une notification push à une large audience avec un groupe de contrôle, le groupe de test envoie des messages uniquement aux utilisateurs disposant d'un jeton de notification push. Cependant, le groupe de contrôle inclut à la fois les utilisateurs qui disposent d'un jeton de notification push et ceux qui n'en ont pas. Dans ce cas, votre audience initiale pour la campagne ou le Canvas doit filtrer sur la possession d'un jeton de notification push (`Foreground Push Enabled` est `true`). La même logique doit être appliquée pour l'éligibilité à recevoir des messages sur d'autres canaux : avoir donné son consentement, disposer d'un jeton de notification push ou être abonné.

Notez que si une variante de contrôle ne contient aucune étape de Canvas, les événements de critères de sortie ne sont pas enregistrés pour les utilisateurs de la variante de contrôle.

{% alert note %}
Si vous utilisez manuellement des numéros de compartiment aléatoires pour les groupes de contrôle, consultez les [points de vigilance]({{site.baseurl}}/user_guide/audience/global_control_group/#things-to-watch-for) concernant vos groupes de contrôle.
{% endalert %}