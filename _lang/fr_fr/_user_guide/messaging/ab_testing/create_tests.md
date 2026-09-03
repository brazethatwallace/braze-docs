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

1. Allez dans **Messaging** > **Campaigns**.
2. Sélectionnez **Create campaign** et un canal pour la campagne dans la section qui permet les tests multivariés et A/B. Pour une documentation détaillée sur chaque canal de communication, consultez [Créer une campagne]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign).

## Étape 2 : Composez vos variantes {#step-2-compose-your-variants}

Vous pouvez créer jusqu'à huit variantes de votre message, en variant les titres, le contenu, les images, et plus encore. Le nombre de différences entre les messages détermine s'il s'agit d'un test multivariable ou d'un test A/B. Un test A/B examine l'effet de la modification d'une seule variable, tandis qu'un test multivariable en examine deux ou plus.

Pour des idées sur la façon de commencer à différencier vos variantes, consultez [Conseils pour les différents canaux](#tips-different-channels).

![Sélection de « Ajouter une variante » pour une campagne.]({% image_buster /assets/img/ab_create_2.png %})

## Étape 3 : Planifier votre Campaign {#step-3-schedule-your-campaign}

La planification de votre Campaign multivariée fonctionne de la même manière que celle de toute autre Campaign Braze. Tous les [types de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) standard sont disponibles.

Une fois qu'un test multivarié a commencé, vous ne pouvez plus apporter de modifications à la Campaign. Si vous modifiez les paramètres, tels que la ligne d'objet ou le corps HTML, Braze considère que l'expérience est compromise et la désactive immédiatement.

Pour optimiser automatiquement vos variantes, consultez la section [Optimiser les tests A/B avec BrazeAI]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection). Les Campaigns à envoi unique et à envois multiples utilisent des méthodes et des exigences d'optimisation différentes.

## Étape 4 : Choisir un Segment et répartir vos utilisateurs entre les variantes {#step-4-choose-a-segment-and-distribute-your-users-across-variants}

Sélectionnez les Segments à cibler, puis répartissez les membres entre les variantes sélectionnées et le [groupe de contrôle](#including-a-control-group) optionnel. Pour les bonnes pratiques concernant le choix d'un Segment pour vos tests, consultez [Choisir un Segment](#choosing-a-segment).

Pour les Campaigns prises en charge, activez **Optimiser avec BrazeAI<sup>TM</sup>** pour optimiser automatiquement la répartition de vos variantes. Pour une Campaign à envoi unique, Braze réserve une partie de l'audience pour un second envoi optimisé. Pour une Campaign à envois multiples, BrazeAI<sup>TM</sup> ajuste la répartition au fil du temps.

### Groupe de contrôle {#including-a-control-group}

Vous pouvez réserver un pourcentage de votre audience cible pour un groupe de contrôle randomisé. Les utilisateurs du groupe de contrôle ne reçoivent pas le test, mais Braze surveille leur taux de conversion pendant toute la durée de la Campaign.

Lorsque vous consultez vos résultats, vous pouvez comparer les taux de conversion de vos variantes par rapport à un taux de conversion de référence fourni par votre groupe de contrôle. Cela vous permet de comparer à la fois les effets de vos variantes et les effets de vos variantes par rapport au taux de conversion qui résulterait si vous n'envoyiez aucun message.

![Panneau de test A/B montrant la répartition en pourcentage du groupe de contrôle, de la variante 1, de la variante 2 et de la variante 3 avec 25 % pour chaque groupe.]({% image_buster /assets/img/ab_create_4.png %})

{% alert important %}
L'utilisation d'un groupe de contrôle pour déterminer un gagnant par les _ouvertures_ ou les _clics_ n'est pas recommandée. Étant donné que le groupe de contrôle ne reçoit pas le message, ces utilisateurs ne peuvent effectuer aucune ouverture ni aucun clic. Par conséquent, le taux de conversion de ce groupe est de 0 % par définition et ne constitue pas une comparaison pertinente avec les variantes.
{% endalert %}

#### Groupes de contrôle et tests A/B {#control-groups-and-ab-testing}

Lorsque vous utilisez la limitation du débit avec un test A/B, la limite de débit n'est pas appliquée au groupe de contrôle de la même manière qu'au groupe test, ce qui constitue une source potentielle de biais temporel. Utilisez des fenêtres de conversion appropriées pour éviter ce biais.

#### Groupes de contrôle avec Optimiser avec BrazeAI<sup>TM</sup> {#control-groups-with-optimize-with-brazeai}

Pour une Campaign à envois multiples avec [Optimiser avec BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection), la taille initiale du groupe de contrôle dépend du nombre de variantes. Si chaque variante reçoit plus de 20 % des utilisateurs, le groupe de contrôle commence à 20 %, et les variantes se partagent les 80 % restants de manière égale. Avec davantage de variantes, le groupe de contrôle commence plus petit. Au fur et à mesure que BrazeAI<sup>TM</sup> analyse les performances, le groupe de contrôle peut augmenter ou diminuer.

## Étape 5 : Désigner un événement de conversion (facultatif) {#step-5-designate-a-conversion-event-optional}

Définir un événement de conversion pour une Campaign vous permet de voir combien de destinataires de cette Campaign ont effectué une action particulière après l'avoir reçue.

Cela n'affecte le test que si vous avez choisi **Primary Conversion Rate** dans les étapes précédentes. Pour plus d'informations, consultez [Événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events).

## Étape 6 : Vérifier et lancer {#step-6-review-and-launch}

Sur la page de confirmation, vérifiez les détails de votre campagne multivariée et lancez le test ! Ensuite, découvrez comment [comprendre les résultats de votre test]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics).

## Ce qu'il faut savoir {#things-to-know}

Si votre expérience a déjà commencé à envoyer des messages et que vous modifiez le message, l'expérience est invalidée et tous les résultats de l'expérience sont supprimés.

- Pour éviter toute interférence avec le comportement attendu de l'expérience, nous recommandons d'éviter les modifications de message dans l'heure qui suit le lancement de la Campaign d'expérience.
- Si votre expérience est terminée et que vous modifiez le message après l'envoi, les résultats de l'expérience restent disponibles dans l'analyse de votre tableau de bord. Cependant, si vous relancez la Campaign, les résultats de l'expérience sont supprimés.

### Conseils pour différents canaux {#tips-different-channels}

Selon le canal que vous sélectionnez, vous pouvez tester différents composants de votre message. Par exemple, vous pouvez essayer de composer des variantes en ayant une idée de ce que vous souhaitez tester et de ce que vous espérez prouver. Quels leviers pouvez-vous actionner et quels sont les effets souhaités ? Bien qu'il existe des millions de possibilités à explorer en utilisant un test multivariable et A/B, voici quelques suggestions pour vous aider à démarrer :

| Canal | Aspects du message que vous pouvez modifier | Résultats à rechercher |
| ---------------------| --------------- | ------------- |
| Notification push | Texte <br> Utilisation d'images et d'émojis <br> Deep links  <br> Présentation des nombres (par exemple, « tripler » versus « augmenter de 200 % »)  <br> Présentation du temps (par exemple, « se termine à minuit » versus « se termine dans 6 heures ») | Ouvertures  <br> Taux de conversion |
| E-mail | Ligne d'objet <br> Nom d'affichage <br> Formule de salutation <br> Corps du texte <br> Utilisation d'images et d'émojis <br> Présentation des nombres (par exemple, « tripler » versus « augmenter de 200 % ») <br> Présentation du temps (par exemple, « se termine à minuit » versus « se termine dans 6 heures ») | Ouvertures  <br> Taux de conversion |
| Message in-app | Aspects listés pour « notification push » <br> [Spécifications d'image des messages in-app]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#image-specifications) | Clics <br> Taux de conversion |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Conseils pour différents canaux" }

{% alert tip %}
Lorsque vous exécutez des tests A/B, n'oubliez pas de générer des [rapports d'entonnoir]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports) qui vous permettent de comprendre comment chaque variante a impacté votre tunnel de conversion, en particulier si la « conversion » pour votre entreprise implique de réaliser plusieurs étapes ou actions.
{% endalert %}

De plus, la durée idéale de votre test peut également varier en fonction du canal. Gardez à l'esprit le temps moyen dont la plupart des utilisateurs peuvent avoir besoin pour interagir avec chaque canal.

Par exemple, si vous testez une notification push, vous pouvez obtenir des résultats significatifs plus rapidement que lors du test d'un e-mail, car les utilisateurs voient les notifications push immédiatement, mais il peut s'écouler plusieurs jours avant qu'ils ne voient ou n'ouvrent un e-mail. Si vous testez des messages in-app, gardez à l'esprit que les utilisateurs doivent ouvrir l'application pour voir la Campaign, vous devriez donc attendre plus longtemps pour collecter les résultats provenant à la fois de vos utilisateurs les plus actifs et de vos utilisateurs plus typiques.

Si vous n'êtes pas sûr de la durée pendant laquelle votre test devrait s'exécuter, [Optimiser avec BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) peut automatiquement configurer et exécuter l'optimisation.

### Choisir un Segment {#choosing-a-segment}

Étant donné que différents Segments de vos utilisateurs peuvent réagir différemment aux messages, le succès d'un message particulier en dit long à la fois sur le message lui-même et sur son Segment cible. Par conséquent, essayez de concevoir un test en gardant votre Segment cible à l'esprit.

Par exemple, bien que les utilisateurs actifs puissent avoir des taux de réponse égaux à « Cette offre expire demain ! » et « Cette offre expire dans 24 heures ! », les utilisateurs qui n'ont pas ouvert l'application depuis une semaine pourraient être plus réceptifs à la seconde formulation, car elle crée un plus grand sentiment d'urgence.

De plus, lorsque vous choisissez le Segment sur lequel exécuter votre test, assurez-vous de considérer si la taille de ce Segment est suffisamment grande pour votre test. En général, les tests multivariables et A/B avec plus de variantes nécessitent un groupe de test plus important pour obtenir des résultats statistiquement significatifs. Cela s'explique par le fait que davantage de variantes entraînent moins d'utilisateurs voyant chaque variante individuelle.

{% alert tip %}
En règle générale, vous avez probablement besoin d'environ 15 000 utilisateurs par variante (y compris le groupe de contrôle) pour atteindre un niveau de confiance de 95 % dans les résultats de votre test. Cependant, le nombre exact d'utilisateurs dont vous avez besoin pourrait être supérieur ou inférieur, en fonction de votre cas particulier. Pour des indications plus précises sur les tailles d'échantillon par variante, envisagez de consulter un [calculateur de taille d'échantillon](https://www.calculator.net/sample-size-calculator.html).
{% endalert %}

### Biais et randomisation {#bias-and-randomization}

Une question fréquente concernant les affectations aux groupes de contrôle et de test est de savoir si elles peuvent introduire un biais dans vos tests. D'autres se demandent parfois comment nous savons si ces affectations sont véritablement aléatoires.

Les utilisateurs sont affectés aux variantes de message, aux variantes de Canvas ou à leurs groupes de contrôle respectifs en concaténant leur ID utilisateur (généré aléatoirement) avec l'ID de Campaign ou de Canvas (généré aléatoirement), en prenant le modulo de cette valeur par 100, puis en ordonnant les utilisateurs dans des tranches qui correspondent aux pourcentages d'affectation pour les variantes et le groupe de contrôle optionnel choisis dans le tableau de bord. Il n'y a donc aucun moyen pratique que les comportements des utilisateurs avant la création d'une Campaign ou d'un Canvas particulier varient systématiquement entre les variantes et le groupe de contrôle. Il n'est pas non plus pratique d'être plus aléatoire (ou plus précisément, pseudo-aléatoire) que cette implémentation.

#### Erreurs à éviter {#mistakes-to-avoid}

Il existe quelques erreurs courantes à éviter pour ne pas créer l'apparence de différences basées sur le canal de communication si les audiences ne sont pas filtrées correctement.

Par exemple, si vous envoyez une notification push à une audience large avec un groupe de contrôle, le groupe de test envoie des messages uniquement aux utilisateurs disposant d'un jeton de notification push. Cependant, le groupe de contrôle inclut à la fois les utilisateurs qui disposent d'un jeton de notification push et ceux qui n'en ont pas. Dans ce cas, votre audience initiale pour la Campaign ou le Canvas doit être filtrée pour disposer d'un jeton de notification push (`Foreground Push Enabled` est `true`). La même chose doit être faite pour l'éligibilité à recevoir des messages sur d'autres canaux : avoir donné son consentement, disposer d'un jeton de notification push ou être abonné.

Notez que si une variante de contrôle ne comporte aucune étape de Canvas, les événements de critères de sortie ne sont pas enregistrés pour les utilisateurs de la variante de contrôle.

{% alert note %}
Si vous utilisez manuellement des numéros de compartiment aléatoires pour les groupes de contrôle, consultez les [points à surveiller]({{site.baseurl}}/user_guide/audience/global_control_group#things-to-watch-for) dans vos groupes de contrôle.
{% endalert %}