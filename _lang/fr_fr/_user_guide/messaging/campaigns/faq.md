---
nav_title: FAQ
article_title: FAQ sur les campagnes
page_order: 10
page_type: FAQ
description: "Cette page répond aux questions fréquemment posées sur les campagnes."
tool: Campaigns

---

# Questions fréquemment posées

> Cet article répond à certaines questions fréquemment posées sur les campagnes.

### Comment créer une campagne multicanale ?

Pour créer une campagne multicanale, sélectionnez **Envoi de messages** > **Campagnes**. Ensuite, sélectionnez **Créer une campagne** > **Multicanale**. Vous pouvez alors choisir parmi les canaux de communication suivants : Cartes de contenu, e-mail, LINE, notifications push, SMS/MMS/RCS, webhook ou WhatsApp.

### Puis-je ajouter un groupe de contrôle à ma campagne multicanale ?

Non, les groupes de contrôle dans les campagnes sont conçus pour les communications monocanales, comme E-mail A versus E-mail B. Comme alternative, essayez d'utiliser [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/) pour tester différents canaux, contenus de messages et délais de livraison.

### Quels sont les moyens de commencer à tester et optimiser les campagnes ?

Les campagnes multivariées et l'exécution de Canvas avec plusieurs variantes sont un excellent point de départ ! Par exemple, vous pouvez lancer une [campagne multivariée]({{site.baseurl}}/user_guide/messaging/ab_testing/) pour tester un message avec différentes rédactions ou lignes d'objet. Les Canvas avec plusieurs variantes permettent de tester des workflows entiers.

### Pourquoi le taux d'ouverture de ma campagne a-t-il diminué ?

Un faible taux d'ouverture n'est pas toujours lié à un problème technique. Il peut y avoir des problèmes de troncature d'e-mail, ce qui entraîne l'absence du pixel de suivi. Cependant, il est aussi possible que moins d'utilisateurs ouvrent leurs e-mails en raison du contenu ou de changements dans la taille de l'audience.

### Comment les audiences des campagnes sont-elles évaluées ?

Par défaut, les campagnes vérifient les filtres d'audience au moment de l'entrée. Pour les campagnes à livraison par événement avec un délai, il existe une option pour réévaluer les critères de segment au moment de l'envoi afin de s'assurer que les utilisateurs font toujours partie de l'audience cible lorsque le message est envoyé.

### Pourquoi y a-t-il une différence entre le nombre de destinataires uniques et le nombre d'envois pour une campagne ou un Canvas donné ?

Une explication possible est que la campagne ou le Canvas a la rééligibilité activée, ce qui signifie que les utilisateurs qui remplissent les critères du segment et les paramètres de livraison peuvent recevoir le message plus d'une fois. Si la rééligibilité n'est pas activée, la différence entre les envois et les destinataires uniques peut s'expliquer par le fait que les utilisateurs possèdent plusieurs appareils, sur différentes plateformes, associés à leurs profils.

Par exemple, si vous avez un Canvas qui comprend à la fois des notifications push iOS et web, un utilisateur donné possédant un appareil mobile et un ordinateur de bureau peut recevoir plus d'un message.

### Pourquoi le nombre de conversions peut-il dépasser le nombre d'utilisateurs uniques pour les campagnes multicanales ?

Pour les campagnes multicanales, Braze comptabilise les conversions par canal, et non par utilisateur. Lorsqu'un utilisateur effectue une seule action de conversion dans la fenêtre de conversion, Braze attribue cette conversion à chaque canal par lequel l'utilisateur a reçu un message. Cela signifie que si un utilisateur reçoit des messages sur plusieurs canaux (par exemple, e-mail et push) et convertit, Braze comptabilise plusieurs conversions, une pour chaque canal. Par conséquent, le nombre total de conversions peut dépasser le nombre d'utilisateurs uniques ayant converti.

Par exemple, si une campagne multicanale envoie à la fois un e-mail et une notification push à un utilisateur, et que cet utilisateur effectue une action de conversion après avoir reçu les deux messages et dans la fenêtre de conversion, Braze comptabilise cela comme deux conversions, une attribuée à l'e-mail et une attribuée au push, même s'il s'agit d'une seule action du même utilisateur.

### Pourquoi ma campagne a-t-elle une base d'utilisateurs atteignables plus petite que le segment que j'utilise pour la campagne ?

Si vous avez configuré un [Groupe de contrôle global]({{site.baseurl}}/user_guide/audience/global_control_group/), cela empêchera un pourcentage de votre audience atteignable de recevoir des campagnes. Cela signifie que le nombre d'utilisateurs atteignables pour votre segment peut parfois être supérieur au nombre d'utilisateurs atteignables pour votre campagne, même si la campagne utilise ce même segment.

### Qu'offre la livraison en fuseau horaire local ?

La livraison en fuseau horaire local vous permet de distribuer des campagnes de communication à un segment en fonction du fuseau horaire individuel de chaque utilisateur. Sans la livraison en fuseau horaire local, les campagnes seront planifiées en fonction des paramètres de fuseau horaire de votre entreprise dans Braze.

Par exemple, une entreprise basée à Londres qui envoie une campagne à 12 h atteindra les utilisateurs de la côte ouest des États-Unis à 4 h du matin. Si votre application n'est disponible que dans certains pays, cela peut ne pas poser de problème. Sinon, nous recommandons fortement d'éviter d'envoyer des notifications push tôt le matin à votre base d'utilisateurs.

### Comment Braze reconnaît-il le fuseau horaire d'un utilisateur ?

Braze détermine automatiquement le fuseau horaire d'un utilisateur à partir de son appareil. Cela garantit la précision du fuseau horaire et une couverture complète de vos utilisateurs. Les utilisateurs créés via l'API utilisateur ou sans fuseau horaire défini auront le fuseau horaire de votre entreprise comme fuseau horaire par défaut jusqu'à ce qu'ils soient reconnus dans votre application par le SDK.

Vous pouvez vérifier le fuseau horaire de votre entreprise dans les [paramètres de l'entreprise]({{site.baseurl}}/user_guide/administer/global/admin_settings/) sur le tableau de bord.

### Quand Braze évalue-t-il les utilisateurs pour la livraison en fuseau horaire local ?

Braze évalue l'éligibilité des utilisateurs à l'entrée aux moments suivants :

- Heure des Samoa (UTC+13) ou UTC+14 pendant l'heure d'été
- L'heure locale du jour planifié

Pour qu'un utilisateur soit éligible à l'entrée, il doit être éligible aux deux vérifications. Par exemple, si un Canvas est planifié pour être lancé le 7 août 2021 à 14 h en fuseau horaire local, le ciblage d'un utilisateur situé à New York nécessiterait les vérifications d'éligibilité suivantes :

- New York le 6 août 2021 à 21 h
- New York le 7 août 2021 à 14 h

L'utilisateur doit être dans le segment pendant 24 heures avant le lancement. Si l'utilisateur n'est pas éligible lors de la première vérification, Braze ne tente pas la seconde.

#### Exemples

Par exemple, si une campagne est planifiée pour être livrée à 19 h UTC, nous commençons à mettre en file d'attente les envois de la campagne dès qu'un fuseau horaire est identifié (comme les Samoa). Cela signifie que nous préparons l'envoi du message, pas que nous envoyons la campagne. Si les utilisateurs ne correspondent à aucun filtre lors de la vérification d'éligibilité, ils ne feront pas partie de l'audience cible.

Autre exemple : supposons que vous souhaitiez créer deux campagnes planifiées pour être envoyées le même jour — une le matin et une le soir — et ajouter un filtre pour que les utilisateurs ne puissent recevoir la seconde campagne que s'ils ont déjà reçu la première. Avec la livraison en fuseau horaire local, certains utilisateurs pourraient ne pas recevoir la seconde campagne. En effet, nous vérifions l'éligibilité lorsque le fuseau horaire de l'utilisateur est identifié, et si l'heure planifiée n'est pas encore arrivée dans leur fuseau horaire, ils n'ont pas reçu la première campagne, ce qui signifie qu'ils ne seront pas éligibles pour la seconde.

Pour une représentation visuelle de la façon dont un utilisateur peut être dans un segment lors de la première vérification mais pas lors de la seconde, consultez cette chronologie :

![Chronologie d'un utilisateur entrant dans le segment avant la première vérification, puis le quittant avant la seconde.]({% image_buster /assets/img/local_time_zone_diagram.png %})

{% details Description de la chronologie %}

1. L'utilisateur A entre dans le segment à 6 h 59 PST (4 h 59 heure des Samoa).
2. Braze vérifie l'appartenance au segment à 7 h heure des Samoa pour déterminer quels utilisateurs sont éligibles pour recevoir la campagne dans les 24 prochaines heures. L'utilisateur A est dans le segment à ce moment.
3. Le segment a une fenêtre de 24 heures, donc l'utilisateur A quitte le segment 24 heures après y être entré : 6 h 59 PST (4 h 59 heure des Samoa).
4. La campagne en heure locale s'envoie à 7 h PST, mais l'utilisateur A a déjà quitté le segment.

{% enddetails %}

### Comment planifier une campagne en fuseau horaire local ?

Lors de la planification d'une campagne, choisissez de l'envoyer à une heure désignée, puis sélectionnez **Envoyer la campagne aux utilisateurs dans leur fuseau horaire local**.

Braze recommande fortement de planifier toutes les campagnes en fuseau horaire local 24 heures à l'avance. Comme une telle campagne doit être envoyée sur une journée entière, la planifier 24 heures à l'avance garantit que votre message atteindra l'ensemble de votre segment. Cependant, vous pouvez planifier ces campagnes moins de 24 heures à l'avance si nécessaire. Gardez à l'esprit que Braze n'enverra pas de messages aux utilisateurs qui ont manqué l'heure d'envoi de plus d'une heure.

Par exemple, s'il est 13 h et que vous planifiez une campagne en fuseau horaire local pour 15 h, la campagne sera immédiatement envoyée à tous les utilisateurs dont l'heure locale est entre 15 h et 16 h, mais pas aux utilisateurs dont l'heure locale est 17 h. De plus, l'heure d'envoi que vous choisissez pour votre campagne ne doit pas encore être passée dans le fuseau horaire de votre entreprise.

La modification d'une campagne en fuseau horaire local planifiée moins de 24 heures à l'avance ne modifiera pas la planification du message. Si vous décidez de modifier une campagne en fuseau horaire local pour l'envoyer à une heure ultérieure (par exemple, 19 h au lieu de 18 h), les utilisateurs qui faisaient partie du segment ciblé lorsque l'heure d'envoi originale a été choisie recevront toujours le message à l'heure originale (18 h). Si vous modifiez un fuseau horaire local pour envoyer à une heure antérieure (par exemple, 16 h au lieu de 17 h), la campagne sera tout de même envoyée à tous les membres du segment à l'heure originale (17 h).

{% alert note %}
Pour les composants Canvas, les utilisateurs n'ont pas besoin d'être dans le composant pendant 24 heures pour recevoir le composant suivant du parcours utilisateur pour la livraison en fuseau horaire local.
{% endalert %}

Si vous avez autorisé les utilisateurs à redevenir éligibles pour la campagne, ils la recevront à nouveau à l'heure originale (17 h). Cependant, pour toutes les occurrences suivantes de votre campagne, vos messages ne seront envoyés qu'à l'heure mise à jour.

### Quand les modifications apportées aux campagnes en fuseau horaire local prennent-elles effet ?

Les segments cibles pour les campagnes en fuseau horaire local doivent inclure une fenêtre d'au moins 48 heures pour tout filtre basé sur le temps afin de garantir la livraison à l'ensemble du segment. Par exemple, considérez un segment ciblant les utilisateurs à leur deuxième jour avec les filtres suivants :

- Première utilisation de l'application il y a plus d'un jour
- Première utilisation de l'application il y a moins de deux jours

La livraison en fuseau horaire local peut manquer des utilisateurs dans ce segment en fonction de l'heure de livraison et du fuseau horaire local des utilisateurs. En effet, un utilisateur peut quitter le segment au moment où son fuseau horaire déclenche la livraison.

### Quelles modifications puis-je apporter aux campagnes planifiées avant le lancement ?

Lorsque la campagne est planifiée, vous devez effectuer les modifications sur tout élément autre que la composition du message avant que nous mettions les messages en file d'attente pour l'envoi. Comme pour toutes les campagnes, vous ne pouvez pas modifier les événements de conversion après le lancement.

### J'ai mis à jour ma campagne planifiée. Pourquoi ne s'est-elle pas lancée ?

Cela peut se produire lorsqu'une campagne est planifiée pour se lancer exactement à l'heure à laquelle elle a été mise à jour. Par exemple, s'il est actuellement 15 h 10 et que vous avez modifié la campagne pour se lancer à 15 h 10 et sélectionné **Mettre à jour la campagne**, il est maintenant passé 15 h 10, ce qui signifie que l'heure planifiée pour le lancement est dépassée. Au lieu de planifier la campagne pour la même heure, sélectionnez **Envoyer dès le lancement de la campagne**.

### Quelle est la « zone de sécurité » avant que les messages d'une campagne planifiée ne soient mis en file d'attente ?

Nous recommandons d'apporter des modifications aux messages dans les délais suivants :

- **Campagnes planifiées ponctuelles :** Modifiez jusqu'à l'heure d'envoi planifiée.
- **Campagnes planifiées récurrentes :** Modifiez jusqu'à l'heure d'envoi planifiée.
- **Campagnes en heure locale :** Modifiez jusqu'à 24 heures avant l'heure d'envoi planifiée.
- **Campagnes à heure d'envoi optimale :** Modifiez jusqu'à 24 heures avant le jour où la campagne est planifiée pour être envoyée.

Si vous apportez des modifications en dehors de ces recommandations, les mises à jour pourraient ne pas être reflétées dans le message envoyé. Par exemple, si vous modifiez l'heure d'envoi trois heures avant qu'une campagne ne soit planifiée pour être envoyée à 12 h en heure locale, les situations suivantes peuvent se produire :

- Braze n'envoie pas de messages aux utilisateurs qui ont manqué l'heure d'envoi de plus d'une heure.
- Les messages déjà mis en file d'attente peuvent toujours être envoyés à l'heure initialement prévue, plutôt qu'à l'heure ajustée.

Si vous devez apporter des modifications, nous recommandons d'arrêter la campagne en cours (cela annule tous les messages en file d'attente). Vous pouvez ensuite dupliquer la campagne, effectuer les modifications nécessaires et lancer la nouvelle campagne. Vous devrez peut-être exclure de cette campagne les utilisateurs qui ont déjà reçu la première campagne. Assurez-vous de réajuster les horaires de planification de la campagne pour tenir compte de l'envoi par fuseau horaire.

### Pourquoi aucun utilisateur n'est-il entré dans ma campagne planifiée quotidienne le jour du changement d'heure ?

Lors des jours de transition vers l'heure d'été ou d'hiver, les campagnes planifiées quotidiennement peuvent s'exécuter jusqu'à une heure plus tôt ou plus tard que d'habitude, selon que les horloges avancent ou reculent. Si votre segment repose sur des attributs personnalisés ou des événements avec des horodatages qui tombent dans l'heure précédant l'heure d'envoi planifiée, ces utilisateurs pourraient ne pas encore être éligibles lorsque la campagne évalue l'éligibilité le jour du changement d'heure.

Par exemple, supposons que les utilisateurs reçoivent généralement une mise à jour d'attribut personnalisé à 15 h UTC, et que votre campagne s'exécute quotidiennement à 10 h 30 à New York (heure de l'Est). Lorsque New York est à l'heure standard (UTC-5), 10 h 30 ET correspond à 15 h 30 UTC, donc la campagne s'exécute après l'enregistrement de l'attribut. Lorsque New York passe à l'heure d'été (UTC-4), 10 h 30 ET correspond à 14 h 30 UTC, donc le jour du passage à l'heure d'été, la campagne peut s'exécuter avant la mise à jour de l'attribut à 15 h UTC. Comme l'attribut qualifiant n'existe pas encore, ces utilisateurs sont filtrés. Si la rééligibilité est désactivée, les utilisateurs qui sont entrés les jours précédents ne peuvent pas réentrer, ce qui entraîne zéro entrée pour ce jour.

Pour éviter cela, assurez-vous que vos mises à jour d'attributs personnalisés ou d'événements se produisent plus d'une heure avant l'heure d'envoi planifiée de la campagne.

### Pourquoi le nombre d'utilisateurs entrant dans une campagne ne correspond-il pas au nombre attendu ?

Le nombre d'utilisateurs entrant dans une campagne peut différer du nombre attendu en raison de la façon dont les audiences et les déclencheurs sont évalués. Dans Braze, une audience est évaluée avant le déclencheur (sauf lors de l'utilisation d'un déclencheur de [changement d'attribut]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Cela entraîne l'exclusion des utilisateurs de la campagne s'ils ne font pas initialement partie de votre audience sélectionnée avant l'évaluation des actions de déclenchement.

{% alert tip %}
Pour obtenir une assistance supplémentaire sur la résolution des problèmes de campagne, assurez-vous de contacter l'assistance Braze dans les 30 jours suivant la survenue de votre problème, car nous ne disposons que des 30 derniers jours de journaux de diagnostic.
{% endalert %}

### Quelle est la différence entre les options Exporter les données utilisateur en CSV et Exporter les adresses e-mail en CSV sur ma page d'analyse de campagne ?

L'option **Exporter les adresses e-mail en CSV** télécharge uniquement les données des utilisateurs ayant des adresses e-mail. Par exemple, si vous avez un segment de 100 000 utilisateurs, mais que seulement 50 000 d'entre eux ont des adresses e-mail, et que vous cliquez sur **Exporter les adresses e-mail en CSV**, l'export ne contiendra que 50 000 lignes de données. En comparaison, l'option **Exporter les données utilisateur en CSV** exporte toutes les données utilisateur.

### Puis-je rechercher une campagne par son identifiant API ?

Oui, utilisez le filtre `api_id:YOUR_API_ID` sur la page **Campagnes** pour rechercher une campagne par son identifiant API. Consultez [rechercher des campagnes]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/search_campaigns/) pour en savoir plus.

### Pourquoi les espaces s'affichent-ils différemment dans les champs de saisie et dans le texte affiché ?

La gestion des espaces diffère entre les champs de saisie et les composants de texte affiché en raison du style CSS. Dans les composants de texte avec le CSS par défaut `white-space: normal`, plusieurs espaces consécutifs sont réduits à un seul espace lors de l'affichage. C'est le comportement HTML standard pour le texte rendu.

Les champs de saisie préservent les espaces multiples exactement tels que vous les saisissez, car vous devez voir et modifier l'espacement exact pour une saisie de données précise. Cela signifie que du texte avec plusieurs espaces peut apparaître différemment lorsqu'il est affiché dans un champ de saisie (où tous les espaces sont préservés) par rapport à son affichage dans d'autres parties du tableau de bord (où le CSS peut réduire les espaces multiples).

Par exemple, si vous saisissez un nom de campagne ou un paramètre UTM avec plusieurs espaces dans un champ de saisie, vous verrez tous les espaces préservés. Cependant, lorsque ce même texte apparaît dans les résultats de recherche, les listes de campagnes ou d'autres composants de texte, les espaces multiples peuvent apparaître comme un seul espace en raison de la gestion des espaces par le CSS.

### Quelle est la différence entre les campagnes API et les campagnes déclenchées par API ?

Les campagnes déclenchées par API vous permettent de gérer le contenu de la campagne, les tests multivariés et les règles de rééligibilité dans le tableau de bord de Braze tout en déclenchant la livraison de ce contenu depuis vos propres serveurs et systèmes. Ces messages peuvent également inclure des données supplémentaires à intégrer dans les messages en temps réel.

Les campagnes API sont utilisées pour suivre les messages envoyés via l'API. Contrairement à la plupart des campagnes, vous ne spécifiez pas le message, les destinataires ou la planification, mais vous transmettez les identifiants dans vos appels API.

### Quelle est la différence entre les campagnes à livraison par événement et les campagnes déclenchées par API ?

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Livraison par événement

Les campagnes à livraison par événement ou déclenchées par événement sont très efficaces pour les messages transactionnels ou basés sur des accomplissements et vous permettent de les déclencher après qu'un utilisateur a effectué un certain événement.

| Avantages | Inconvénients | 
| ---- | ---- |
| • Visibilité des payloads JSON entrants dans la plateforme (si l'événement est déclenché par un utilisateur test) via le **Journal d'activité des messages**<br><br>• Les éléments de personnalisation sont inclus dans les propriétés d'événement personnalisées<br><br>• L'événement personnalisé peut être utilisé pour créer des segments d'utilisateurs éligibles au message | • Consomme des points de donnée |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Déclenchées par API

Les campagnes déclenchées par API et par serveur sont idéales pour gérer des transactions plus avancées, vous permettant de déclencher la livraison du contenu de la campagne depuis vos propres serveurs et systèmes. La requête API pour déclencher le message peut également inclure des données supplémentaires à intégrer dans le message en temps réel.

| Avantages | Points à considérer | 
| ---- | ---- |
| • Ne consomme pas de points de donnée<br><br>• Les éléments de personnalisation sont inclus dans les propriétés du payload JSON | • Ne permet pas de créer un segment d'utilisateurs éligibles au message dans les propriétés du payload JSON<br><br>• Impossible de voir les payloads JSON entrants avec le **Journal d'activité des messages** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Que dois-je inclure lors de la soumission d'un ticket d'assistance pour une erreur « Request Timed Out » ?

Si vous rencontrez une erreur « Request Timed Out » lors de la création ou de la modification d'une campagne ou d'un Canvas et que vous devez contacter l'[assistance Braze]({{site.baseurl}}/braze_support/), incluez les informations suivantes pour accélérer la résolution :

- **Enregistrement d'écran :** Un enregistrement des étapes que vous avez suivies avant de voir l'erreur, y compris les transitions de page.
- **Horodatage et fuseau horaire :** L'heure exacte à laquelle l'erreur s'est produite et votre fuseau horaire.
- **Navigateur et version :** Le navigateur que vous utilisez (par exemple, Chrome 120, Safari 17) et si vous avez essayé de reproduire l'erreur dans un autre navigateur.
- **Étapes pour reproduire :** Une description claire des actions qui déclenchent l'erreur, y compris les paramètres spécifiques de la campagne ou du Canvas concernés.
- **Journaux réseau (facultatif) :** Ouvrez les outils de développement de votre navigateur (onglet **Réseau**), reproduisez l'erreur et exportez le journal réseau sous forme de fichier HAR (HTTP Archive). Cela aide l'équipe d'assistance à identifier quel appel API expire.

### Pourquoi mes analyses d'envoi ne correspondent-elles pas à la limite maximale de destinataires que j'ai définie ?

Si vous ajoutez ou modifiez une limite maximale de destinataires sur une campagne active, la limite peut ne pas être reflétée dans vos analyses d'envoi pour les raisons suivantes :

- **Limite ajoutée après le lancement :** Si la limite maximale de destinataires n'est pas définie au lancement de la campagne, les messages déjà mis en file d'attente avant l'application de la limite sont tout de même envoyés. La limite ne prend effet que pour les envois mis en file d'attente après l'enregistrement de la modification.
- **Interaction avec la limite de débit :** Si une campagne est également soumise à une limite de débit, les messages peuvent être distribués sur une fenêtre de temps plus longue. La limite maximale de destinataires est évaluée lorsque les messages sont mis en file d'attente, pas lorsqu'ils sont livrés. Si la limite est modifiée alors que des messages sont déjà dans la file d'attente, la limite originale s'applique à ces messages.
- **Campagnes récurrentes :** Pour les campagnes récurrentes, chaque envoi planifié évalue la limite maximale de destinataires de manière indépendante. Modifier la limite entre les envois ne réajuste pas rétroactivement les comptages d'envois précédents.

Pour éviter les décalages, définissez la limite maximale de destinataires avant de lancer la campagne et évitez de la modifier pendant que des envois sont en cours.

### Pourquoi les envois sont-ils inférieurs à la taille estimée de l'audience ?

Plusieurs facteurs peuvent expliquer que le nombre d'envois soit inférieur à la taille estimée de l'audience :

- **Réévaluation du segment :** Pour les campagnes à livraison par événement ou planifiées qui réévaluent au moment de l'envoi, les utilisateurs qui étaient dans le segment lorsque la campagne a été mise en file d'attente peuvent ne plus être éligibles lorsque le message est effectivement envoyé.
- **Groupes de contrôle :** Si un [Groupe de contrôle global]({{site.baseurl}}/user_guide/audience/global_control_group/) ou un groupe de contrôle au niveau de la campagne est utilisé, une partie de l'audience est exclue de la livraison.
- **Délais et fenêtres de livraison :** Pour les campagnes en fuseau horaire local ou planifiées, les utilisateurs doivent être éligibles à la fois à l'entrée et au moment de l'envoi ; les utilisateurs dans certains fuseaux horaires peuvent se trouver en dehors de la fenêtre de livraison.
- **Limite de débit :** Si une limite de débit est appliquée, les messages sont distribués dans le temps et certains envois peuvent être différés ou ne pas encore être reflétés dans le comptage.
- **Filtres de livrabilité des e-mails :** Pour les campagnes e-mail, Braze exclut les utilisateurs qui ont subi un hard bounce, se sont désabonnés des e-mails, ont été signalés comme spam, n'ont pas d'adresse e-mail dans leur profil ou ne sont pas abonnés à un groupe d'abonnement requis. Ces vérifications sont effectuées au moment de l'envoi, de sorte qu'un utilisateur présent dans votre segment peut tout de même être exclu du comptage réel des envois.