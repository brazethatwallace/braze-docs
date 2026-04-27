---
nav_title: FAQ
article_title: FAQ Canvas
page_order: 8
alias: "/canvas_v2_101/"
description: "Cet article répond aux questions fréquemment posées sur Canvas."
tool: Canvas
toc_headers: h2 

---

# Questions fréquemment posées

> Cet article répond à certaines questions fréquemment posées sur Canvas.

## Création et modification de Canvas

### Combien d'étapes puis-je inclure dans un Canvas ?

Vous pouvez ajouter jusqu'à 200 étapes dans un Canvas.

### Quelle est la différence entre un composant et une étape ?

Un [composant]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/) est un élément individuel de votre Canvas que vous pouvez utiliser pour déterminer l'efficacité de votre Canvas. Les composants peuvent inclure des actions telles que la division du parcours utilisateur, l'ajout d'un délai, ou encore le test de plusieurs chemins Canvas. Une étape dans Canvas fait référence au parcours utilisateur personnalisé dans les branches de votre Canvas. Essentiellement, votre Canvas est composé de composants individuels qui créent des étapes pour le parcours de vos utilisateurs.

### Puis-je lancer un Canvas avec des étapes déconnectées ?

Oui. Vous pouvez également enregistrer des Canvas après leur lancement avec des étapes déconnectées. 

### Où vont les utilisateurs lorsqu'ils atteignent une étape déconnectée ?

Si un utilisateur se trouve dans une étape déconnectée de votre workflow Canvas, il passera à l'étape suivante s'il y en a une, et les paramètres de l'étape détermineront comment l'utilisateur doit avancer. Cela permet aux utilisateurs d'apporter des modifications aux étapes sans avoir à les connecter directement au reste du Canvas. Cela vous laisse également une marge pour tester avant de passer en production immédiatement, ce qui permet en pratique d'enregistrer un brouillon.

Nous vous recommandons de vérifier la vue analytique pour les utilisateurs en attente dans une étape Canvas avant de déconnecter une étape.

### Que se passe-t-il si l'audience et l'heure d'envoi sont identiques pour un Canvas qui a une variante, mais plusieurs branches ?

Nous mettons en file d'attente une tâche pour chaque étape — elles s'exécutent à peu près en même temps, et l'une d'entre elles « l'emporte ». En pratique, la répartition peut être relativement équilibrée, mais il y aura probablement au moins un léger biais en faveur de l'étape créée en premier. 

De plus, nous ne pouvons pas garantir exactement à quoi ressemblera cette répartition. Si vous souhaitez une répartition égale, ajoutez un filtre [Numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/).

### Comment les audiences Canvas sont-elles évaluées ?

Par défaut, les filtres et segments pour les étapes complètes du Canvas sont vérifiés au moment de l'envoi. L'étape Arbre décisionnel effectue une évaluation juste après la réception d'une étape précédente (ou avant un délai).

### Quand un événement d'exception se déclenche-t-il ?

Les événements d'exception ne se déclenchent que lorsque l'utilisateur attend de recevoir le composant Canvas auquel il est associé. Si un utilisateur effectue une action en avance, l'événement d'exception ne se déclenchera pas. Si vous souhaitez exclure les utilisateurs ayant déjà effectué un certain événement, utilisez plutôt des [filtres]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/).

### Comment la modification d'un Canvas affecte-t-elle les utilisateurs déjà dans le Canvas ?

Si vous modifiez certaines étapes d'un Canvas multi-étapes, les utilisateurs qui faisaient déjà partie de l'audience mais n'ont pas encore reçu les étapes recevront la version mise à jour du message. Notez que cela ne se produira que s'ils n'ont pas encore été évalués pour l'étape en question.

Pour plus d'informations sur ce que vous pouvez modifier après le lancement, consultez [Modifier votre Canvas après le lancement]({{site.baseurl}}/post-launch_edits/).

### Que se passe-t-il lorsque vous arrêtez un Canvas ?

Lorsque vous arrêtez un Canvas, les règles suivantes s'appliquent :

- Les utilisateurs ne pourront plus entrer dans le Canvas.
- Aucun message supplémentaire ne sera envoyé, quel que soit l'endroit où se trouve l'utilisateur dans le flux.
- **Exception :** les Canvas contenant des e-mails ne s'arrêteront pas immédiatement. Une fois les demandes d'envoi transmises à SendGrid, il n'est plus possible d'empêcher leur distribution à l'utilisateur.

### Dois-je créer un seul Canvas ou des Canvas séparés par cycle de vie utilisateur ?

Selon ce que vous souhaitez accomplir avec votre Canvas, vous pourriez avoir besoin d'approches différentes pour construire votre parcours utilisateur. La flexibilité de Canvas vous permet de cartographier les parcours utilisateurs pour n'importe quelle étape du cycle de vie. Consultez nos [modèles de Canvas Braze]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) pour plusieurs exemples d'approches simplifiées pour créer des parcours utilisateurs efficaces.

## Messages et distribution

### Quand les messages in-app dans Canvas sont-ils envoyés ?

Les messages in-app sont envoyés au prochain démarrage de session. Cela signifie que si l'utilisateur entre dans l'étape Canvas avant l'arrêt du Canvas, il recevra quand même le message in-app lors de son prochain démarrage de session, tant que le message in-app n'a pas encore expiré.

Il est possible qu'un utilisateur démarre une session avant l'arrêt du Canvas, mais que le message in-app ne lui soit pas affiché immédiatement. Cela peut se produire si le message in-app est déclenché par un événement personnalisé ou est différé. Cela signifie qu'il est possible qu'un utilisateur enregistre une impression de message in-app et « reçoive » le message in-app après l'arrêt du Canvas. Cependant, l'utilisateur aurait dû démarrer la session avant l'arrêt du Canvas, mais **après** avoir reçu l'étape Canvas.

{% alert note %}
L'arrêt d'un Canvas ne fera pas sortir du parcours utilisateur les utilisateurs qui attendent de recevoir des messages. Si vous réactivez le Canvas et que des utilisateurs attendent toujours le message, ils le recevront (sauf si le moment où le message aurait dû être envoyé est déjà passé, auquel cas ils ne le recevront pas).
{% endalert %}

### Pourquoi un Canvas peut-il afficher zéro envoi alors que des impressions sont enregistrées ?

Si les _Messages envoyés_ sont toujours à zéro pour un Canvas contenant une étape de message in-app, c'est parce que la distribution des messages in-app fonctionne différemment des autres canaux de communication.

Les messages in-app sont « récupérés » par le SDK, plutôt qu'« envoyés » par Braze. Les messages in-app pour les utilisateurs éligibles sont distribués automatiquement au démarrage de la session et « attendent » l'événement déclencheur avant de s'afficher. Comme les utilisateurs éligibles reçoivent le message lorsqu'ils démarrent une session, Braze ne signale pas cela comme un événement d'envoi. Lorsque les utilisateurs effectuent l'événement déclencheur, le message s'affiche et Braze enregistre une impression et marque l'étape Canvas (ou la campagne) comme reçue sur le profil utilisateur. Par conséquent, le total des _Envois_ sera de zéro pour les messages in-app.

### Puis-je planifier des heures d'envoi différentes pour chaque variante dans la même étape Message Canvas ou le même envoi multivarié ?

Non. Les variantes d'une même configuration multivariée ou étape Message partagent un seul calendrier de distribution. Vous ne pouvez pas attribuer à une variante un envoi à 18 h et à une autre un envoi à 19 h pour le même envoi planifié.

Pour échelonner les envois ou utiliser des horaires différents par chemin, essayez les méthodes suivantes :

- Des étapes Message séparées avec des étapes de délai entre elles, afin que chaque message ait sa propre planification.
- Des branches ou une étape [Chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) pour que les utilisateurs suivent des chemins avec des horaires différents.
- Des campagnes séparées si le cas d'usage n'a pas besoin de rester dans un seul Canvas.

Pour les concepts de tests multivariés et A/B dans les campagnes, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

## Analyses et conversions

### Comment les conversions des utilisateurs sont-elles suivies dans un Canvas ?

Un utilisateur ne peut convertir qu'une seule fois par entrée dans le Canvas. Les conversions sont attribuées au dernier message reçu par l'utilisateur pour cette entrée. Le bloc récapitulatif au début d'un Canvas reflète toutes les conversions effectuées par les utilisateurs dans ce chemin, qu'ils aient reçu un message ou non. Chaque étape suivante n'affichera que les conversions survenues lorsque cette étape était la dernière reçue par l'utilisateur.

{% alert note %}
Lorsqu'un utilisateur entre à nouveau dans un Canvas, les événements de conversion ne sont suivis que pour l'entrée la plus récente. Les événements de conversion ne sont pas enregistrés pour les entrées précédentes, même si l'événement de conversion est renseigné rétroactivement.
{% endalert %}

{% details Développer pour voir des exemples %}

**Exemple 1**

Il y a un chemin Canvas avec 10 notifications push et l'événement de conversion est « démarrage de session » (« Ouvre l'application ») :

- L'utilisateur A ouvre l'application après être entré mais avant de recevoir le premier message.
- L'utilisateur B ouvre l'application après chaque notification push.

**Résultat :** Le récapitulatif affichera deux conversions tandis que les étapes individuelles afficheront une conversion de un à la première étape et zéro pour toutes les étapes suivantes.

{% alert note %}
Si les heures calmes sont actives lorsque l'événement de conversion se produit, les mêmes règles s'appliquent.
{% endalert %}

**Exemple 2**

Il y a un Canvas à une seule étape avec les heures calmes activées :

1. L'utilisateur entre dans le Canvas.
2. La première étape n'a pas de délai, mais se situe dans les heures calmes définies, donc le message est supprimé.
3. L'utilisateur effectue l'événement de conversion.

**Résultat :** L'utilisateur sera comptabilisé comme converti dans la variante globale du Canvas, mais pas dans l'étape puisqu'il n'a pas reçu l'étape.

{% enddetails %}

### Quelle est la différence entre les différents types de taux de conversion ?

- Le total des conversions Canvas reflète le nombre d'utilisateurs uniques ayant effectué un événement de conversion, et non le nombre de conversions effectuées par chacun. 
- Le taux de conversion de la variante ou le bloc récapitulatif au début d'un Canvas reflète toutes les conversions effectuées par les utilisateurs dans ce chemin, qu'ils aient reçu un message ou non, sous forme de total agrégé. 
- Le taux de conversion de l'étape reflète le nombre de personnes ayant reçu cette étape de message et ayant effectué l'un des événements de conversion définis.

### Pourquoi le taux de conversion de mon étape Canvas n'est-il pas égal au taux de conversion total de ma variante Canvas ?

Il est courant que le total des conversions d'une variante Canvas soit supérieur à la somme des totaux de ses étapes. Cela se produit parce qu'un utilisateur peut effectuer un événement de conversion pour une variante dès qu'il entre dans la variante. Cependant, ce même événement de conversion ne compte pas pour une étape Canvas. Ainsi, tout utilisateur qui entre dans le Canvas et effectue l'événement de conversion avant de recevoir la première étape Canvas sera comptabilisé dans le total de conversion de la variante, mais pas dans le total de l'étape. Il en va de même pour un utilisateur qui entre dans le Canvas mais en sort avant de recevoir une étape.

### Comment puis-je consulter les analyses de chacun de mes composants Canvas ?

Pour consulter les analyses d'un composant Canvas, accédez à votre Canvas et faites défiler la page **Détails du Canvas**. Vous pouvez y voir les analyses de chaque composant. Consultez [Analyses Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) pour plus de détails.

### En ce qui concerne le nombre d'utilisateurs uniques, les analyses Canvas ou le segmenteur sont-ils plus précis ?

Le segmenteur fournit une statistique plus précise pour les données d'utilisateurs uniques par rapport aux statistiques Canvas ou de campagne. En effet, les statistiques Canvas et de campagne sont des nombres que Braze incrémente lorsqu'un événement se produit, ce qui signifie que des variables peuvent entraîner des différences par rapport au segmenteur. Par exemple, les utilisateurs peuvent convertir plus d'une fois pour un Canvas ou une campagne.

### Pourquoi le nombre d'utilisateurs entrant dans un Canvas ne correspond-il pas au nombre attendu ?

Le nombre d'utilisateurs entrant dans un Canvas peut différer du nombre attendu en raison de la façon dont les audiences et les déclencheurs sont évalués. Dans Braze, une audience est évaluée avant le déclencheur (sauf lors de l'utilisation d'un déclencheur de [changement d'attribut]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Cela entraînera la sortie des utilisateurs du Canvas s'ils ne font pas partie de votre audience sélectionnée avant l'évaluation des actions de déclenchement.

### Que se passe-t-il pour les utilisateurs anonymes pendant leur parcours Canvas ?

Bien que les utilisateurs anonymes puissent entrer et sortir des Canvas, leurs actions ne sont pas associées à un profil utilisateur spécifique tant qu'ils ne sont pas identifiés, de sorte que leurs interactions peuvent ne pas être entièrement suivies dans vos analyses. Vous pouvez utiliser le [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder/) pour générer un rapport de ces indicateurs.

{% alert tip %}
Pour obtenir une assistance supplémentaire concernant la résolution des problèmes Canvas, contactez l'assistance Braze dans les 30 jours suivant la survenue de votre problème, car nous ne disposons que des 30 derniers jours de journaux de diagnostic.
{% endalert %}

## Segmentation

### Quelle est la différence entre « N'est pas entré dans la variante Canvas » et « N'est pas dans le groupe de contrôle Canvas » ?

Consultez les [Filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/) pour les définitions complètes des filtres.

#### N'est pas entré dans la variante Canvas

L'utilisateur n'est jamais entré dans un chemin de variante d'un Canvas spécifique. Tous les utilisateurs qui ne sont pas dans le groupe de contrôle sont inclus, qu'ils soient entrés ou non dans le Canvas. Cela inclut les utilisateurs qui sont entrés dans une autre variante et les utilisateurs qui ne sont entrés dans aucune variante. 

#### N'est pas dans le groupe de contrôle Canvas

L'utilisateur est entré dans le Canvas, mais n'est pas dans le groupe de contrôle et a par conséquent reçu une variante. Cela inclut uniquement les utilisateurs qui sont entrés dans le Canvas.

Notez que l'attribution de la variante se fait à l'entrée dans le Canvas. Si un utilisateur n'est pas entré dans un Canvas, aucune variante ne lui sera attribuée. En d'autres termes, il ne sera ni dans le groupe de contrôle ni dans une variante.

## Éditeur Canvas d'origine

{% details Développer pour voir les FAQ de l'éditeur Canvas d'origine %}

### Comment convertir un Canvas existant de l'éditeur d'origine vers l'éditeur actuel ?

Vous pouvez [cloner votre Canvas]({{site.baseurl}}/cloning_canvases/). Cela crée une copie de votre Canvas d'origine dans le workflow Canvas le plus récent.

### Quelles sont les principales différences entre les éditeurs Canvas actuel et d'origine ?

#### Barre d'outils des composants Canvas

Auparavant, avec l'éditeur Canvas d'origine, une étape complète était ajoutée par défaut chaque fois que vous créiez une étape dans votre parcours utilisateur. Ces étapes complètes sont remplacées par différents composants Canvas, ce qui vous offre une meilleure visibilité et une personnalisation accrue de votre expérience d'édition. Vous pouvez voir immédiatement tous vos composants Canvas depuis la barre d'outils des étapes Canvas.

#### Comportement des étapes

Auparavant, chaque étape complète incluait des informations telles que les paramètres de délai et de planification, les événements d'exception, les filtres d'audience, la configuration des messages et les options d'avancement des messages, le tout dans un seul composant. Ce sont des paramètres séparés dans l'éditeur actuel pour rendre votre expérience de création Canvas plus personnalisable, et cela introduit quelques différences de fonctionnement.

#### Avancement du composant Message

Les [composants Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) font avancer tous les utilisateurs qui entrent dans l'étape. Il n'est pas nécessaire de spécifier le comportement d'avancement des messages, ce qui simplifie la configuration globale de l'étape. Si vous souhaitez implémenter l'option **Avancer lorsque le message est envoyé**, ajoutez un Parcours d'audience séparé pour filtrer les utilisateurs qui n'ont pas reçu l'étape précédente.  

#### Comportement du délai « dans »

Les [composants de délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/) attendront la totalité du temps de délai avant de passer à l'étape suivante. 

Supposons que le 12 avril, nous ayons un composant de délai configuré pour envoyer votre utilisateur à l'étape suivante dans un jour à 14 h. Un utilisateur entre dans le composant à 14 h 01 le 13 avril. 
- Pour le workflow d'origine, l'utilisateur passerait à l'étape suivante à 14 h le 14 avril, soit moins d'un jour après l'heure d'entrée. 
- Dans l'éditeur actuel, l'utilisateur passerait à l'étape suivante à 14 h le 15 avril. Notez que c'est la même heure, mais plus d'un jour après l'heure d'entrée. 

#### Comportement du timing intelligent

Puisque le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/) est stocké dans le composant Message, les délais seront appliqués avant les calculs du timing intelligent. Cela signifie que, selon le moment où un utilisateur entre dans le composant, il peut recevoir le message plus tard que dans un Canvas construit avec le workflow Canvas d'origine.

Supposons que votre délai est fixé à 2 jours, que le timing intelligent est activé et qu'il a déterminé que le meilleur moment pour envoyer votre message est 14 h. Un utilisateur entre dans l'étape de délai à 14 h 01.
- **Workflow actuel :** Il faudra 48 heures pour que le délai s'écoule, donc l'utilisateur recevra le message le troisième jour à 14 h.
- **Workflow d'origine :** L'utilisateur reçoit le message le deuxième jour à 14 h.

Notez que si le timing intelligent est activé, le message sera envoyé dans les 24 heures suivant l'entrée de l'utilisateur dans le composant Message, à l'heure intelligente identifiée (même si aucun composant de délai n'est impliqué).

#### Événements d'exception

##### Heures calmes

L'événement d'exception est appliqué à l'aide des Parcours d'actions, qui sont séparés des étapes Message. Les heures calmes sont appliquées dans le composant Message. Cela signifie que si un utilisateur a déjà passé le Parcours d'actions (et n'a pas été exclu par l'événement d'exception), puis rencontre les heures calmes lorsqu'il arrive au composant Message, et que son Canvas est configuré pour renvoyer le message après la période d'heures calmes, l'événement d'exception ne sera plus appliqué. Notez que ce cas d'usage n'est pas courant.

Pour les segments et les filtres, l'étape Message dispose de validations de distribution qui permettent aux utilisateurs de configurer des segments et filtres supplémentaires qui sont validés au moment de l'envoi. Cela évite le cas limite mentionné ci-dessus concernant les heures calmes.

##### Paramètre de planification « dans » ou « au prochain »

Les événements d'exception sont créés à l'aide des Parcours d'actions. Les Parcours d'actions ne prennent en charge que « après une fenêtre de temps X » et non « dans X temps » ou « au prochain X temps ».

{% enddetails %}

### Que dois-je inclure lors de la soumission d'un ticket d'assistance pour une erreur « Request Timed Out » ?

Si vous rencontrez une erreur « Request Timed Out » lors de la modification d'un Canvas et que vous devez contacter l'[assistance Braze]({{site.baseurl}}/braze_support/), incluez les informations suivantes pour accélérer la résolution :

- **Enregistrement d'écran :** Un enregistrement des étapes que vous avez effectuées avant de voir l'erreur, y compris les transitions de page.
- **Horodatage et fuseau horaire :** L'heure exacte à laquelle l'erreur s'est produite et votre fuseau horaire.
- **Navigateur et version :** Le navigateur que vous utilisez (par exemple, Chrome 120, Safari 17) et si vous avez essayé de reproduire l'erreur dans un autre navigateur.
- **Étapes de reproduction :** Une description claire des actions qui déclenchent l'erreur, y compris les étapes Canvas ou configurations spécifiques impliquées.
- **Journaux réseau (facultatif) :** Ouvrez les outils de développement de votre navigateur (onglet **Réseau**), reproduisez l'erreur et exportez le journal réseau sous forme de fichier journal HTTP Archive (HAR). Cela aide l'équipe d'assistance à identifier quel appel API expire.