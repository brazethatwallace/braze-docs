---
nav_title: Timing intelligent
article_title: Timing intelligent
page_order: 1.3
description: "Cet article propose un aperçu du timing intelligent (appelé auparavant Livraison intelligente) et explique comment tirer parti de cette fonctionnalité dans vos campagnes."
toc_headers: h2
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Timing intelligent {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomintelligent-timing-stylefloatrightwidth120pxborder0-classnoimgborderintelligent-timing}

> Utilisez le timing intelligent pour transmettre votre message à chaque utilisateur au moment où Braze détermine l'heure d'envoi optimale, c'est-à-dire lorsque l'utilisateur est le plus susceptible d'interagir (ouvrir ou cliquer). Cela vous permet de vérifier plus facilement que vous envoyez vos messages à vos utilisateurs à l'heure qui leur convient le mieux, ce qui peut entraîner un engagement accru.

## À propos du timing intelligent {#about-intelligent-timing}

Braze calcule le moment d'envoi optimal en se basant sur une analyse statistique des interactions passées de vos utilisateurs avec votre application et avec chaque canal de communication. Les données d'interaction suivantes sont utilisées :

- Heures de session
- Ouvertures directes des notifications push
- Ouvertures influencées par les notifications push
- Clics sur les e-mails
- Ouvertures des e-mails (à l'exclusion des [ouvertures automatiques]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens))
- Clics sur les SMS (uniquement si le [raccourcissement de liens]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) et le suivi avancé sont activés)

Par exemple, Sam ouvre régulièrement vos e-mails le matin, mais elle ouvre votre application et interagit avec les notifications le soir. Cela signifie que Sam recevrait une Campaign par e-mail avec le timing intelligent le matin, tandis qu'elle recevrait des Campaigns avec des notifications push le soir, au moment où elle est plus susceptible d'interagir.

Si un utilisateur ne dispose pas de suffisamment de données d'engagement pertinentes pour que Braze puisse calculer le moment d'envoi optimal, vous pouvez spécifier une heure de repli.

## Exemples {#examples}

- Envoyer des Campaigns récurrentes qui ne sont pas sensibles au facteur temps
- Automatiser des Campaigns avec des utilisateurs de plusieurs fuseaux horaires
- Lors de l'envoi de messages à vos utilisateurs les plus engagés (ils disposeront du plus grand volume de données d'engagement)

## Utiliser le timing intelligent {#using-intelligent-timing}

Cette section décrit comment configurer le timing intelligent pour vos Campaigns et Canvas.

{% tabs local %}
{% tab Campaign %}
### Étape 1 : Ajouter le timing intelligent {#step-1-add-intelligent-timing}

1. Créez une Campaign et composez votre message.
2. Sélectionnez **Scheduled Delivery** comme type de réception.
3. Sous **Time-Based Scheduling Options**, sélectionnez **Intelligent Timing**.
4. Définissez la fréquence d'envoi. Pour les envois ponctuels, sélectionnez **Once** et choisissez une date d'envoi. Pour les envois récurrents, sélectionnez **Daily**, **Weekly** ou **Monthly** et configurez les options de récurrence. Consultez les [considérations](#considerations) pour plus de détails.
5. Vous pouvez également configurer les [heures calmes](#quiet-hours).
6. Spécifiez un [horaire de secours](#campaign-fallback). Il s'agit de l'heure à laquelle le message est envoyé si le profil d'un utilisateur ne contient pas d'événements pertinents pour calculer un moment optimal.

![Écran de planification de Campaign affichant le timing intelligent avec l'horaire de secours et les paramètres d'heures calmes]({% image_buster /assets/img/intelligent_timing/campaign_scheduling.png %})

#### Heures calmes {#quiet-hours}

Utilisez les heures calmes pour empêcher l'envoi de messages pendant des heures spécifiques. Cela est utile lorsque vous souhaitez éviter d'envoyer des messages tôt le matin ou pendant la nuit, tout en permettant au timing intelligent de déterminer la meilleure fenêtre de réception.

{% alert note %}
Les heures calmes ont remplacé le paramètre **Only send within specific hours**. Au lieu de choisir quand les messages peuvent être envoyés, vous choisissez désormais quand ils ne doivent pas être envoyés. Par exemple, pour envoyer des messages entre 16 h et 18 h, définissez les heures calmes de 18 h à 16 h le lendemain.
{% endalert %}

1. Sélectionnez **Enable Quiet Hours**.
2. Sélectionnez l'heure de début et de fin pendant laquelle les messages ne doivent **pas** être envoyés.

![Basculement des heures calmes activé avec une heure de début et de fin définie pour bloquer la réception des messages pendant la nuit]({% image_buster /assets/img/intelligent_timing/quiet_hours.png %})

Lorsque les heures calmes sont activées, Braze n'envoie pas de messages pendant la période calme, même si ce moment correspond à l'heure d'envoi optimale d'un utilisateur. Si l'heure optimale d'un utilisateur tombe dans la fenêtre calme, le message sera envoyé au bord le plus proche de la fenêtre.

Par exemple, si les heures calmes sont définies de 22 h à 6 h et que l'heure optimale d'un utilisateur est 5 h 30, Braze retiendra le message et le remettra à 6 h, l'heure la plus proche en dehors de la fenêtre calme.

Pour en savoir plus, consultez [Heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

#### Aperçu des heures de réception {#preview-delivery-times}

Pour afficher une estimation du nombre d'utilisateurs qui recevront le message à chaque heure de la journée, utilisez le graphique d'aperçu (Campaigns uniquement).

1. Ajoutez des Segments ou des filtres dans l'étape Target Audiences.
2. Dans la section **Preview Delivery Times for** (qui apparaît dans les étapes Target Audiences et Schedule Delivery), sélectionnez votre canal.
3. Cliquez sur **Refresh Data**.

![Graphique d'aperçu de réception pour Android Push montrant un pic d'engagement entre 12 h et 14 h, et l'heure la plus populaire de l'application étant 14 h.]({% image_buster /assets/img/intel-timing-preview.png %})

### Étape 2 : Choisir une date d'envoi {#step-2-choose-a-send-date}

Ensuite, sélectionnez une date d'envoi pour votre Campaign. Gardez les points suivants à l'esprit lors de la planification de Campaigns avec le timing intelligent :

#### Lancer la Campaign 48 heures à l'avance {#launch-campaign-48-hours-in-advance}

Lancez votre Campaign au moins 48 heures avant la date d'envoi prévue. Cela s'explique par les variations de fuseaux horaires. Braze calcule l'heure optimale à minuit heure des Samoa (UTC+13), l'un des premiers fuseaux horaires au monde. Une seule journée s'étend sur environ 48 heures à travers le globe, ce qui signifie que si vous lancez une Campaign dans cette période tampon de 48 heures, il est possible que l'heure optimale d'un utilisateur soit déjà passée dans son fuseau horaire, et le message ne sera pas envoyé.

{% alert important %}
Si une Campaign est lancée et que l'heure optimale d'un utilisateur date de moins d'une heure, le message est envoyé immédiatement. Si l'heure optimale date de plus d'une heure, le message n'est pas envoyé du tout.
{% endalert %}

#### Fenêtre de 3 jours pour les filtres de Segment {#3-day-window-for-segment-filters}

Si vous ciblez une audience ayant effectué une action pendant une certaine période, prévoyez une fenêtre d'au moins 3 jours dans vos filtres de Segment. Par exemple, au lieu de `First used app more than 1 day ago` et `First used app less than 3 days ago`, utilisez 1 jour et 4 jours.

![Filtres pour l'audience cible où la Campaign cible les utilisateurs ayant utilisé l'application pour la première fois entre 1 et 4 jours.]({% image_buster /assets/img/intelligent_timing/first_used_app.png %})

Cela s'explique également par les fuseaux horaires : sélectionner une période de moins de 3 jours peut entraîner la sortie de certains utilisateurs du Segment avant que leur heure d'envoi optimale ne soit atteinte.

Pour en savoir plus, consultez la [FAQ : timing intelligent](#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

#### Planifier les variantes gagnantes 2 jours après le test A/B {#schedule-winning-variants-2-days-after-ab-test}

Si vous tirez parti d'un [test A/B avec optimisation]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations), comme l'envoi automatique de la **variante gagnante** ou l'utilisation d'une **variante personnalisée**, le timing intelligent peut affecter la durée et le calendrier de votre Campaign.

Lors de l'utilisation du timing intelligent, nous recommandons de planifier l'envoi de la variante gagnante au moins **2 jours après** le début du test A/B. Par exemple, si votre test A/B commence le 16 avril à 16 h, planifiez l'envoi de la variante gagnante au plus tôt le 18 avril à 16 h. Cela donne à Braze suffisamment de temps pour évaluer le comportement des utilisateurs et envoyer les messages au moment optimal.

![Sections de test A/B montrant un test A/B avec la variante gagnante sélectionnée, avec les critères de victoire, la date d'envoi et l'heure d'envoi locale sélectionnés]({% image_buster /assets/img/intelligent_timing/ab_testing_intelligent_timing.png %})

### Étape 3 : Configurer les heures calmes (facultatif) {#step-3-configure-quiet-hours-optional}

Vous pouvez éventuellement choisir de limiter la fenêtre de réception. Cela peut être utile si votre Campaign concerne un événement, une vente ou une promotion spécifique, mais n'est généralement pas recommandé lors de l'utilisation du timing intelligent. Pour en savoir plus, consultez les [considérations](#considerations).

Les heures calmes agissent comme une fenêtre de non-envoi. Le timing intelligent détermine toujours l'heure d'envoi optimale de chaque utilisateur, mais si cette heure tombe dans les heures calmes, Braze retarde le message jusqu'au prochain moment disponible en dehors de la période d'heures calmes.

Pour configurer les heures calmes :

1. Lors de la configuration du timing intelligent, sélectionnez **Enable Quiet Hours**.
2. Saisissez l'heure de début et de fin de la fenêtre d'heures calmes.

### Étape 4 : Choisir un horaire de secours {#campaign-fallback}

Choisissez un horaire de secours à utiliser si le profil d'un utilisateur ne contient aucun événement pertinent pour calculer une heure de réception optimale.

![Planification d'une Campaign avec le timing intelligent]({% image_buster /assets/img/intelligent_timing_1.png %})

{% multi_lang_include brazeai/intelligent_suite/fallback_time.md type="campaign" %}

### Étape 5 : Aperçu des heures de réception {#step-5-preview-delivery-times}

Pour afficher une estimation du nombre d'utilisateurs qui reçoivent le message à chaque heure de la journée, utilisez le graphique d'aperçu :

1. Ajoutez des Segments ou des filtres dans l'étape **Target Audiences**.
2. Dans la section **Preview Delivery Times for** (qui apparaît dans les étapes **Target Audiences** et **Schedule Delivery**), sélectionnez votre canal.
3. Sélectionnez **Refresh Data**.

Le graphique d'aperçu affiche chaque heure de la journée selon votre heure locale. Les libellés ne sont pas définis sur un fuseau horaire global unique.

![Exemple d'aperçu des heures de réception pour Android Push.]({% image_buster /assets/img/intel-timing-preview.png %})

Chaque fois que vous modifiez des paramètres liés au timing intelligent ou à l'audience de votre Campaign, actualisez les données pour afficher un graphique mis à jour.

Le graphique affiche en bleu les utilisateurs qui avaient des événements pertinents pour calculer une heure optimale et en rouge les utilisateurs qui utiliseront l'horaire de secours. Utilisez les filtres de calcul pour ajuster la vue d'aperçu et obtenir un aperçu plus détaillé de chaque groupe d'utilisateurs.
{% endtab %}

{% tab Canvas %}

### Étape 1 : Ajouter le timing intelligent

Dans votre Canvas, ajoutez une [étape Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step), puis accédez à **Delivery Settings** et sélectionnez **Using Intelligent Timing**.

Les messages seront envoyés aux utilisateurs ayant accédé à l'étape ce jour-là à leur heure locale optimale. Cependant, si leur heure optimale est déjà passée ce jour-là, le message sera remis à l'heure optimale le jour suivant. Les étapes Message ciblant plusieurs canaux peuvent envoyer ou tenter d'envoyer des messages à des heures différentes selon les canaux. Lorsque le premier message d'une étape Message tente d'être envoyé, tous les utilisateurs sont automatiquement avancés.

### Étape 2 : Choisir un horaire de secours {#step-2-choose-a-fallback-time}

Choisissez un horaire de secours pour l'envoi du message aux utilisateurs de votre audience qui ne disposent pas de données d'engagement pertinentes permettant à Braze de calculer une heure d'envoi optimale. {% multi_lang_include brazeai/intelligent_suite/fallback_time.md %}

### Étape 4 : Ajouter une étape de délai {#step-4-add-a-delay-step}

Contrairement aux Campaigns, vous n'avez pas besoin de lancer votre Canvas 48 heures avant la date d'envoi, car le timing intelligent est défini au niveau de l'étape, et non au niveau du Canvas.

Ajoutez plutôt une [étape de délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) d'au moins deux jours calendaires entre l'entrée de l'utilisateur dans le Canvas et le moment où il reçoit l'étape de timing intelligent.

#### Jours calendaires vs jours de 24 heures {#calendar-vs-24-hour-days}

Lors de l'utilisation du timing intelligent après une étape de délai, la date de réception peut varier en fonction de la manière dont vous calculez votre délai. Cela s'applique uniquement lorsque votre délai est défini sur **After a duration**, car il existe une différence entre le calcul des « jours » et des « jours calendaires ».

- **Jours :** 1 jour correspond à 24 heures, calculé à partir du moment où l'utilisateur entre dans l'étape de délai.
- **Jours calendaires :** 1 jour correspond à la période entre l'entrée de l'utilisateur dans l'étape de délai et minuit dans son fuseau horaire. Cela signifie qu'un jour calendaire peut ne durer que quelques minutes.

Lors de l'utilisation du timing intelligent, nous recommandons d'utiliser les jours calendaires pour les délais plutôt que les jours de 24 heures. En effet, avec les jours calendaires, le message sera envoyé le dernier jour du délai, à l'heure optimale. Avec un jour de 24 heures, il est possible que l'heure optimale de l'utilisateur soit antérieure à son entrée dans l'étape, ce qui signifie qu'un jour supplémentaire sera ajouté à son délai.

Par exemple, supposons que l'heure optimale de Luka est 14 h. Il entre dans l'étape de délai à 14 h 01 le 1er mars, et le délai est défini à 2 jours.

- Le jour 1 se termine le 2 mars à 14 h 01
- Le jour 2 se termine le 3 mars à 14 h 01

Cependant, le timing intelligent est configuré pour envoyer à 14 h, heure déjà passée. Luka ne recevra donc le message que le jour suivant : le 4 mars à 14 h.

![Graphique illustrant la différence entre les jours et les jours calendaires : si l'heure optimale d'un utilisateur est 14 h mais qu'il entre dans l'étape de délai à 14 h 01 avec un délai de 2 jours, le calcul en jours remet le message 3 jours plus tard car l'utilisateur est entré dans l'étape après son heure optimale, tandis que le calcul en jours calendaires remet le message 2 jours plus tard, le dernier jour du délai.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}
{% endtab %}
{% endtabs %}

## Considérations {#considerations}

- Les messages in-app et les webhooks sont envoyés immédiatement et ne bénéficient pas de moments optimaux.
- Le timing intelligent n'est pas disponible pour les Campaigns déclenchées par une action ou par l'API.
- Le timing intelligent ne doit pas être utilisé dans les scénarios suivants :
    - **Limitation du débit :** si la limitation du débit et le timing intelligent sont utilisés conjointement, il n'y a aucune garantie quant au moment où le message sera distribué. Les Campaigns récurrentes quotidiennes avec le timing intelligent ne prennent pas en charge de manière fiable un plafond total d'envoi de messages.
    - **Campaigns d'IP warming :** certains comportements du timing intelligent peuvent compliquer l'atteinte des volumes quotidiens nécessaires lorsque vous commencez à réchauffer votre IP. Cela s'explique par le fait que le timing intelligent évalue les Segments deux fois : une première fois lors de la création initiale de la Campaign ou du Canvas, puis une seconde fois avant l'envoi aux utilisateurs pour vérifier qu'ils font toujours partie de ce Segment. Cela peut entraîner des modifications et des variations dans les Segments, et certains utilisateurs peuvent en sortir lors de la seconde évaluation. Ces utilisateurs ne sont pas remplacés, ce qui impacte votre capacité à atteindre le plafond maximum d'utilisateurs.

## Résolution des problèmes {#troubleshooting}

### Le graphique d'aperçu affiche peu d'utilisateurs avec des horaires optimaux {#preview-chart-showing-few-users-with-optimal-times}

S'il n'existe pas d'événements pertinents pour un utilisateur (par exemple, les nouveaux utilisateurs avec peu ou pas d'engagement), Braze utilise le paramètre de secours configuré, soit votre heure de secours personnalisée, soit l'heure la plus populaire d'utilisation de l'application parmi tous les utilisateurs.

### Impact du fuseau horaire sur la distribution avec le timing intelligent {#impact-of-time-zone-on-intelligent-timing-delivery}

Le timing intelligent utilise le fuseau horaire local de chaque utilisateur et les jours calendaires pour déterminer le moment optimal de distribution. De ce fait, les utilisateurs situés dans des fuseaux horaires en avance ou en retard par rapport au fuseau horaire de référence de votre campagne peuvent recevoir des messages un jour calendaire différent de celui attendu.

Par exemple, si une campagne est planifiée pour le 15 mars et que l'heure optimale d'un utilisateur est calculée pour cette date, un utilisateur dans un fuseau horaire en avance par rapport au point de référence de la campagne peut recevoir le message tard le 14 mars dans le fuseau horaire de référence, tandis qu'un utilisateur dans un fuseau horaire en retard par rapport au point de référence peut le recevoir le 16 mars.

Si les utilisateurs ne reçoivent pas les messages comme prévu, vérifiez que le champ du fuseau horaire dans leur profil est correctement renseigné. Si le champ du fuseau horaire est vide, l'utilisateur peut recevoir des messages alignés sur le fuseau horaire de l'entreprise plutôt que sur son fuseau local.

### Envoi au-delà de la date planifiée {#sending-past-the-scheduled-date}

Votre campagne avec timing intelligent peut envoyer des messages au-delà de la date planifiée si vous utilisez un [test A/B avec une optimisation]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations). Les Campaigns utilisant des optimisations de test A/B peuvent automatiquement envoyer la variante gagnante une fois le test initial terminé, prolongeant ainsi la durée de la campagne. Par défaut, les Campaigns avec une optimisation envoient la variante gagnante aux utilisateurs restants le jour suivant le test initial, mais vous pouvez modifier cette date d'envoi.

Si vous utilisez le timing intelligent, nous vous recommandons de laisser plus de temps au test A/B pour se terminer et de planifier l'envoi de la variante gagnante 2 jours après le test initial au lieu d'1 jour.

## Foire aux questions (FAQ) {#faq}

### Généralités {#general}

#### Que prédit le timing intelligent ? {#what-does-intelligent-timing-predict}

Le timing intelligent se concentre sur la prédiction du moment où un utilisateur est le plus susceptible d'ouvrir ou de cliquer sur vos messages, afin de s'assurer que vos messages atteignent les utilisateurs à des moments d'engagement optimaux.

#### Le timing intelligent est-il calculé séparément pour chaque jour de la semaine ? {#is-intelligent-timing-calculated-separately-for-each-day-of-the-week}

Non, le timing intelligent n'est pas lié à des jours spécifiques. Il personnalise les heures d'envoi en fonction des habitudes d'engagement propres à chaque utilisateur et du canal que vous utilisez, comme l'e-mail ou les notifications push. Ainsi, vos messages parviennent aux utilisateurs au moment où ils sont le plus réceptifs.

### Calculs {#calculations}

#### Quelles données sont utilisées pour calculer l'heure optimale pour chaque utilisateur ? {#what-data-is-used-to-calculate-the-optimal-time-for-each-user}

Pour calculer l'heure optimale, le timing intelligent :

1. Analyse les données d'interaction de chaque utilisateur enregistrées par le SDK de Braze. Cela inclut :
  - Horaires des sessions
  - Ouvertures directes de notification push
  - Ouvertures influencées de notification push
  - Clics sur des e-mails
  - Ouvertures d'e-mail (à l'exclusion des ouvertures de machines)
2. Regroupe ces événements par heure, en identifiant l'heure d'envoi optimale pour chaque utilisateur.

#### Les ouvertures de machines sont-elles prises en compte dans le calcul du moment optimal ? {#are-machine-opens-included-when-calculating-optimal-time}

Non, les [ouvertures de machines]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) sont exclues des calculs du moment optimal. Cela signifie que les heures d'envoi sont basées uniquement sur l'engagement réel des utilisateurs, offrant un timing plus précis pour vos campagnes.

#### Quelle est la précision du moment optimal ? {#how-precise-is-the-optimal-time}

Le timing intelligent planifie les messages pendant l'« heure la plus engagée » de l'utilisateur, en fonction de ses débuts de session et des événements d'ouverture de messages. Au cours de cette heure, l'heure du message est arrondie aux cinq minutes les plus proches. Par exemple, si l'heure optimale d'un utilisateur est calculée à 16 h 58, le message sera planifié pour 17 h 00. Il peut y avoir de légers retards de réception/distribution en raison de l'activité du système pendant les périodes d'affluence.

#### Quels sont les calculs de secours s'il n'y a pas d'événements pertinents ? {#what-are-the-fallback-calculations-if-there-are-no-relevant-events}

Si aucun événement pertinent n'est disponible pour un utilisateur, le timing intelligent utilise le paramètre de secours configuré dans vos paramètres de message, soit une heure de secours personnalisée, soit l'heure la plus populaire pour utiliser l'application parmi tous les utilisateurs.

### Campagnes {#campaigns}

#### Combien de temps à l'avance dois-je lancer une campagne de timing intelligent pour la livrer avec succès à tous les utilisateurs de tous les fuseaux horaires ? {#how-far-in-advance-should-i-launch-an-intelligent-timing-campaign-to-successfully-deliver-it-to-all-users-in-all-time-zones}

Braze calcule le moment optimal à minuit, heure des Samoa, l'un des premiers fuseaux horaires du monde. Un seul jour couvre environ 48 heures. Par exemple, une personne dont le moment optimal est 0 h 01 et qui vit en Australie a déjà dépassé cette heure optimale, et il est donc « trop tard » pour lui envoyer la campagne. Pour ces raisons, vous devez planifier 48 heures à l'avance pour réussir à livrer le message à toutes les personnes qui utilisent votre application dans le monde.

#### Pourquoi ma campagne de timing intelligent affiche-t-elle peu ou pas d'envois ? {#why-is-my-intelligent-timing-campaign-showing-little-to-no-sends}

Si aucun événement d'engagement pertinent n'est détecté pour un utilisateur (par exemple, les nouveaux utilisateurs qui cliquent ou ouvrent rarement ou jamais), le timing intelligent utilise le paramètre de secours configuré, soit votre heure de secours personnalisée, soit l'heure la plus populaire pour utiliser l'application parmi tous les utilisateurs.

#### Pourquoi ma campagne de timing intelligent est-elle envoyée après la date planifiée ? {#why-is-my-intelligent-timing-campaign-sending-past-the-scheduled-date}

Votre campagne de timing intelligent peut être envoyée après la date planifiée parce que vous utilisez des tests A/B. Les campagnes utilisant les tests A/B peuvent envoyer automatiquement la variante gagnante une fois le test A/B terminé, ce qui augmente la durée d'envoi de la campagne. Par défaut, les campagnes de timing intelligent sont planifiées pour envoyer la variante gagnante aux utilisateurs restants le lendemain, mais vous pouvez modifier cette date d'envoi.

Nous vous recommandons, si vous avez des campagnes avec le timing intelligent, de laisser plus de temps pour que le test A/B se termine et de planifier l'envoi de la variante gagnante deux jours après au lieu d'un.

### Fonctionnalité {#functionality}

#### Quand Braze vérifie-t-il les critères d'éligibilité pour les segments et les filtres d'audience ? {#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters}

Braze effectue deux vérifications lorsqu'une campagne est lancée :

1. **Vérification initiale :** À minuit dans le premier fuseau horaire le jour de l'envoi.
2. **Vérification à l'heure planifiée :** Juste avant l'envoi, à l'heure sélectionnée par le timing intelligent pour l'utilisateur.

Soyez prudent lorsque vous filtrez sur la base d'autres envois de campagne afin d'éviter de cibler des segments inéligibles. Par exemple, si vous envoyez deux campagnes le même jour à des heures différentes et que vous ajoutez un filtre qui n'autorise les utilisateurs à recevoir la deuxième campagne que s'ils ont reçu la première, les utilisateurs ne recevront pas la deuxième campagne. En effet, personne n'était éligible lorsque la campagne a été créée et que les segments ont été formés.

#### Puis-je utiliser les heures calmes dans ma campagne de timing intelligent ? {#can-i-use-quiet-hours-in-my-intelligent-timing-campaign}

Les heures calmes peuvent être utilisées dans le cadre d'une campagne utilisant le timing intelligent. L'algorithme de timing intelligent évitera les heures calmes afin d'envoyer le message à tous les utilisateurs éligibles. Cela dit, nous vous recommandons de désactiver les heures calmes, à moins qu'il n'y ait des implications en termes de politique, de conformité ou d'autres implications juridiques quant au moment où les messages peuvent ou ne peuvent pas être envoyés.

#### Que se passe-t-il si le moment optimal pour un utilisateur se situe pendant les heures calmes ? {#what-happens-if-the-optimal-time-for-a-user-is-within-the-quiet-hours}

Si l'heure optimale déterminée tombe pendant les heures calmes, Braze trouve le bord le plus proche des heures calmes et planifie le message pour la prochaine heure autorisée avant ou après les heures calmes. Le message est mis en file d'attente pour être envoyé à la limite la plus proche des heures calmes par rapport à l'heure optimale.

#### Puis-je utiliser le timing intelligent et la limitation du débit ? {#can-i-use-intelligent-timing-and-rate-limiting}

La limitation du débit peut être utilisée dans le cadre d'une campagne utilisant le timing intelligent. Cependant, la nature même de la limitation du débit implique que certains utilisateurs peuvent recevoir leur message à un moment moins qu'optimal, en particulier si un nombre important d'utilisateurs par rapport à la taille de la limite de débit sont planifiés à l'heure de secours parce qu'ils n'ont pas d'événements pertinents.

Nous vous recommandons de n'utiliser la limitation du débit sur une campagne de timing intelligent que lorsque des exigences techniques doivent être respectées.

#### Puis-je utiliser le timing intelligent pendant l'IP warming ? {#can-i-use-intelligent-timing-while-ip-warming}

Braze ne recommande pas l'utilisation du timing intelligent lors du premier réchauffement d'adresses IP, car certains de ses comportements peuvent entraîner des difficultés à atteindre les volumes quotidiens. Cela est dû au fait que le timing intelligent évalue les segments de campagne deux fois : une première fois lors de la création de la campagne, et une seconde fois avant l'envoi aux utilisateurs pour vérifier qu'ils font toujours partie du segment.

Cela peut entraîner des modifications de segments, provoquant souvent la sortie de certains utilisateurs du segment lors de la deuxième évaluation. Ces utilisateurs ne sont pas remplacés, ce qui a un impact sur votre capacité à atteindre le plafond utilisateur maximal.

#### Comment l'heure la plus populaire pour l'application est-elle déterminée ? {#how-is-the-most-popular-app-time-determined}

L'heure la plus populaire pour l'application est déterminée par l'heure moyenne de début de session pour l'espace de travail (en heure locale). Cet indicateur se trouve dans le tableau de bord lors de la prévisualisation des horaires pour une campagne, affiché en rouge.

#### Le timing intelligent tient-il compte des ouvertures de machines ? {#does-intelligent-timing-account-for-machine-opens}

Oui, les ouvertures de machines sont filtrées par le timing intelligent, de sorte qu'elles n'influencent pas ses résultats.

#### Comment puis-je m'assurer que le timing intelligent fonctionne le mieux possible ? {#how-can-i-make-sure-intelligent-timing-works-as-well-as-possible}

Le timing intelligent utilise l'historique individuel d'engagement de chaque utilisateur avec les messages, quelle que soit l'heure à laquelle il les a reçus. Avant d'utiliser le timing intelligent, assurez-vous d'avoir envoyé aux utilisateurs des messages à différents moments de la journée. De cette manière, vous pouvez « échantillonner » le moment le plus propice pour chaque utilisateur. Un échantillonnage inadéquat des différents moments de la journée peut conduire le timing intelligent à choisir une heure d'envoi non optimale pour un utilisateur.

#### Comment activer le timing intelligent sur une étape Canvas ? {#how-do-i-enable-intelligent-timing-on-a-canvas-step}

Dans Canvas, ajoutez ou ouvrez une [étape Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step), allez dans **Delivery Settings** et sélectionnez **Using Intelligent Timing**. Conformément aux instructions de configuration de Canvas dans cet article, incluez une [étape de délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) d'au moins deux jours calendaires entre l'entrée dans le Canvas et cette étape de message, afin que le timing intelligent dispose d'un historique d'engagement suffisant pour son évaluation.