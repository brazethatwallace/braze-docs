---
nav_title: FAQ
article_title: FAQ Canvas
page_order: 8
alias: "/canvas_v2_101/"
description: "Cet article répond aux questions fréquemment posées sur Canvas."
tool: Canvas
toc_headers: h2

---

# Questions fréquemment posées {#frequently-asked-questions}

> Cet article répond à certaines questions fréquemment posées sur Canvas.

## Création et modification de Canvas {#building-and-editing-canvas}

### Combien d'étapes puis-je inclure dans un Canvas ? {#how-many-steps-i-can-include-in-a-canvas}

Vous pouvez ajouter jusqu'à 200 étapes dans un Canvas.

### Existe-t-il des limites de taille pour les propriétés d'entrée Canvas ? {#are-there-size-limits-for-canvas-entry-properties}

Oui. L'[objet de contexte Canvas]({{site.baseurl}}/api/objects_filters/context_object) (propriétés d'entrée Canvas) a une taille maximale de 50&nbsp;Ko. Gardez les payloads aussi petits que possible dans cette limite. Pour comprendre comment les propriétés d'entrée et d'événement fonctionnent dans Canvas, consultez [Propriétés de contexte et d'événement]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties).

### Pourquoi l'erreur « Too many Canvas branches » s'affiche-t-elle ? {#why-do-i-see-a-too-many-canvas-branches-error}

Cette erreur apparaît lorsque la combinaison de branchements d'étapes et de la taille de l'audience d'entrée peut créer des problèmes de performance de cluster empêchant l'envoi des messages. Pour les étapes de résolution — y compris l'utilisation des [parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), la réduction des branchements ou de la taille de l'audience, et la reconstruction dans Canvas Flow — consultez [Erreur « Too many Canvas branches »]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#too-many-canvas-branches-error).

### Puis-je utiliser la sélection intelligente avec la rééligibilité dans un Canvas ? {#can-i-use-intelligent-selection-with-re-eligibility-in-a-canvas}

Oui. Les Canvas peuvent utiliser la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) lorsque la rééligibilité est activée, tandis que les Campaigns nécessitent une fenêtre de rééligibilité de 24 heures ou plus lorsque la sélection intelligente est activée. Braze ne peut pas garantir la même variante lors d'une nouvelle entrée, car l'allocation évolue au fil du temps.

### Quelle est la différence entre un composant et une étape ? {#whats-the-difference-between-a-component-and-a-step}

Un [composant]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about) est un élément individuel de votre Canvas que vous pouvez utiliser pour déterminer l'efficacité de votre Canvas. Les composants peuvent inclure des actions telles que la division de votre parcours utilisateur, l'ajout d'un délai, et même le test de plusieurs chemins Canvas. Une étape dans Canvas fait référence au parcours utilisateur personnalisé dans vos branches Canvas. Essentiellement, votre Canvas est constitué de composants individuels qui créent des étapes pour votre parcours utilisateur.

### Puis-je lancer un Canvas avec des étapes déconnectées ? {#can-i-launch-a-canvas-with-disconnected-steps}

Oui. Vous pouvez également enregistrer des Canvas après le lancement avec des étapes déconnectées.

### Où vont les utilisateurs lorsqu'ils atteignent une étape déconnectée ? {#where-do-users-go-when-theyve-reached-a-disconnected-step}

Si un utilisateur se trouve dans une étape déconnectée de votre workflow Canvas, il passera à l'étape suivante s'il y en a une, et les paramètres de l'étape détermineront comment l'utilisateur doit avancer. Cette fonctionnalité permet aux utilisateurs d'apporter des modifications aux étapes sans avoir à les connecter directement au reste du Canvas. Cela vous donne également une marge de manœuvre pour tester avant de passer en production immédiatement, permettant ainsi d'enregistrer un brouillon.

Nous recommandons de vérifier la vue analytique des utilisateurs en attente dans une étape Canvas avant de déconnecter une étape.

### Que se passe-t-il si l'audience et l'heure d'envoi sont identiques pour un Canvas qui a une variante, mais plusieurs branches ? {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

Nous mettons en file d'attente une tâche pour chaque étape — elles s'exécutent à peu près au même moment, et l'une d'entre elles « l'emporte ». En pratique, la répartition peut être quelque peu uniforme, mais il est probable qu'il y ait au moins un léger biais en faveur de l'étape créée en premier.

De plus, nous ne pouvons faire aucune garantie quant à la distribution exacte. Si vous souhaitez une répartition égale, ajoutez un filtre [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers).

### Comment les audiences Canvas sont-elles évaluées ? {#how-are-canvas-audiences-evaluated}

Par défaut, les filtres et Segments pour les étapes complètes du Canvas sont vérifiés au moment de l'envoi. L'étape de l'arbre décisionnel effectue une évaluation juste après la réception d'une étape précédente (ou avant un délai).

### Quand un événement d'exception se déclenche-t-il ? {#when-does-an-exception-event-trigger}

Les événements d'exception ne se déclenchent que lorsque l'utilisateur attend de recevoir le composant Canvas auquel ils sont associés. Si un utilisateur effectue une action à l'avance, l'événement d'exception ne se déclenchera pas. Si vous souhaitez exclure les utilisateurs ayant déjà effectué un certain événement, utilisez plutôt des [filtres]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

### Comment la modification d'un Canvas affecte-t-elle les utilisateurs déjà dans le Canvas ? {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

Si vous modifiez certaines étapes d'un Canvas à plusieurs étapes, les utilisateurs qui faisaient déjà partie de l'audience mais n'ont pas encore reçu les étapes recevront la version mise à jour du message. Notez que cela ne se produira que s'ils n'ont pas encore été évalués pour l'étape.

Pour plus d'informations sur ce que vous pouvez modifier après le lancement, consultez [Modifier votre Canvas après le lancement]({{site.baseurl}}/post-launch_edits).

### Que se passe-t-il lorsque vous arrêtez un Canvas ? {#what-happens-when-you-stop-a-canvas}

Lorsque vous arrêtez un Canvas, les règles suivantes s'appliquent :

- Les utilisateurs ne pourront plus entrer dans le Canvas.
- Aucun autre message ne sera envoyé, quel que soit l'endroit où se trouve un utilisateur dans le flux.
- **Exception :** les Canvas contenant des e-mails ne s'arrêteront pas immédiatement. Une fois que les demandes d'envoi ont été transmises à SendGrid, il n'est plus possible d'empêcher leur distribution à l'utilisateur.

### Dois-je créer un seul Canvas ou des Canvas séparés par cycle de vie utilisateur ? {#should-i-build-one-canvas-or-separate-canvases-per-user-lifecycle}

Selon ce que vous souhaitez accomplir avec votre Canvas, vous pourriez avoir besoin d'approches différentes pour construire votre parcours utilisateur. La flexibilité de Canvas vous permet de cartographier les parcours utilisateurs pour n'importe quelle étape du cycle de vie de l'utilisateur. Consultez nos [modèles Canvas de Braze]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) pour plusieurs exemples d'approches simplifiées pour créer des parcours utilisateurs efficaces.

## Messages et distribution {#messages-and-delivery}

### Quand les messages in-app dans Canvas sont-ils envoyés ? {#when-are-in-app-messages-in-canvas-sent}

Les messages in-app sont envoyés au prochain démarrage de session. Cela signifie que si l'utilisateur entre dans l'étape du Canvas avant que le Canvas ne soit arrêté, il recevra toujours le message in-app lors de son prochain démarrage de session, tant que le message in-app n'a pas encore expiré.

Il est possible qu'un utilisateur démarre une session avant l'arrêt du Canvas, mais que le message in-app ne lui soit pas affiché immédiatement. Cela peut se produire si le message in-app est déclenché par un événement personnalisé ou s'il est retardé. Il est donc possible qu'un utilisateur enregistre une impression de message in-app et « reçoive » le message in-app après l'arrêt du Canvas. Cependant, l'utilisateur aurait dû démarrer la session avant l'arrêt du Canvas, mais **après** avoir reçu l'étape du Canvas.

{% alert note %}
Arrêter un Canvas n'entraîne pas la sortie des utilisateurs qui attendent de recevoir des messages du parcours utilisateur. Si vous réactivez le Canvas et que des utilisateurs attendent toujours le message, ils le recevront (sauf si le moment auquel le message aurait dû être envoyé est passé, auquel cas ils ne le recevront pas).
{% endalert %}

### Pourquoi un Canvas peut-il afficher zéro envoi même si des impressions sont enregistrées ? {#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged}

Si les _Messages envoyés_ sont toujours à zéro pour un Canvas contenant une étape de message in-app, c'est parce que la distribution des messages in-app fonctionne différemment des autres canaux de communication.

Les messages in-app sont « récupérés » par le SDK, plutôt que « poussés » depuis Braze. Les messages in-app pour les utilisateurs éligibles sont distribués automatiquement au démarrage de la session et « attendent » l'événement déclencheur avant de s'afficher. Comme les utilisateurs éligibles reçoivent le message lorsqu'ils démarrent une session, Braze ne le signale pas comme un événement d'envoi. Lorsque les utilisateurs effectuent l'événement déclencheur, le message s'affiche et Braze enregistre une impression et marque l'étape du Canvas (ou la Campaign) comme reçue sur le profil utilisateur. Par conséquent, le total des _Envois_ est à zéro pour les messages in-app.

### Pourquoi les utilisateurs n'ont-ils pas reçu mon message in-app après un long délai ou une branche ? {#why-didnt-users-receive-my-in-app-message-after-a-long-delay-or-branch}

Une fois les étapes de [Délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) en amont et les vérifications d'audience terminées, les utilisateurs ne deviennent éligibles à un message in-app que lorsqu'ils atteignent l'étape Message. Si le message expire à une date calendaire ou dans une courte fenêtre de **durée après que l'étape est disponible**, les utilisateurs sur des branches plus lentes peuvent arriver après l'expiration et ne jamais voir le message. Alignez l'expiration avec les délais de parcours les plus longs réalistes. Pour plus d'informations et d'exemples, consultez [Expiration des messages in-app]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#in-app-message-expiration).

### Pourquoi vois-je « Canvas Entry Properties may not be used in In-App Messages. » ? {#why-do-i-see-canvas-entry-properties-may-not-be-used-in-in-app-messages}

Ce message apparaît lorsque la personnalisation fait référence à des champs que les messages in-app ne peuvent pas résoudre dans Canvas. Utilisez l'objet `context` comme décrit dans [Propriétés de contexte et d'événement]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) et [Étape Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step). L'espace de noms Liquid hérité `canvas_entry_properties` a des contraintes différentes de `context`. Si vous avez besoin que des valeurs persistent à travers plusieurs étapes, consultez les [propriétés persistantes dans l'éditeur Canvas d'origine]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties) avec votre équipe Braze. Les valeurs stockées sont effacées lorsqu'un utilisateur quitte le Canvas avant que l'appareil ne télécharge le payload in-app.

### Où puis-je trouver les clics sur les boutons pour les messages in-app par glisser-déposer dans Canvas ? {#where-can-i-find-button-clicks-for-drag-and-drop-in-app-messages-in-canvas}

Les indicateurs au niveau des boutons pour les messages in-app par glisser-déposer apparaissent sur la fiche d'analyse de l'étape **Message** dans **Détails du Canvas**, et pas uniquement dans le résumé de haut niveau du Canvas. Ouvrez le Canvas, sélectionnez l'étape Message et consultez l'engagement in-app à cet endroit. Pour les concepts de reporting, consultez [Mesurer et tester avec l'analyse Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).

### Puis-je planifier des heures d'envoi différentes pour chaque variante dans la même étape Message du Canvas ou le même envoi multivarié ? {#can-i-schedule-different-send-times-for-each-variant-in-the-same-canvas-message-step-or-multivariate-send}

Non. Les variantes dans la même configuration multivariée ou étape Message partagent une seule planification de distribution. Vous ne pouvez pas assigner une variante à un envoi à 18 h et une autre à 19 h pour ce même envoi planifié.

Pour échelonner les envois ou utiliser des heures différentes par parcours, essayez les méthodes suivantes :

- Des étapes Message séparées avec des étapes de Délai entre elles afin que chaque message ait sa propre planification.
- Des branches ou une étape [Chemin d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) pour que les utilisateurs suivent des parcours avec des timings différents.
- Des Campaigns séparées si le cas d'usage ne nécessite pas de rester dans un seul Canvas.

Pour les concepts de tests multivariés et A/B dans les Campaigns, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

### Que se passe-t-il si un utilisateur atteint la limite de fréquence globale à une étape Message du Canvas ? {#what-happens-if-a-user-is-global-frequency-capped-at-a-canvas-message-step}

Il ne reçoit pas cet envoi pour le canal limité, mais les étapes Message font tout de même avancer les utilisateurs lorsqu'un message n'est pas envoyé en raison de la limite de fréquence globale. Pour les cas d'avancement étape par étape, consultez [Comment les utilisateurs avancent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance). La limite de fréquence globale seule ne fait pas sortir les utilisateurs d'un Canvas ; ce comportement est distinct des **Validations de distribution** sur une étape Message. Pour plus de détails, consultez [Limitation du débit et limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Pourquoi les envois sont-ils inférieurs à la taille de l'audience estimée ? {#why-are-sends-lower-than-the-estimated-audience-size}

Les envois peuvent être inférieurs à l'**Audience estimée** pour bon nombre des mêmes raisons que pour les [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size), notamment les limites de fréquence, les filtres stricts d'appareil ou de navigateur, les fenêtres de rééligibilité, la limitation du débit et les exclusions au niveau du canal (par exemple, la joignabilité push ou les vérifications d'abonnement et de livrabilité e-mail).

Des facteurs spécifiques à Canvas s'appliquent également :

- **Entrée par événement ou déclenchée par API :** les utilisateurs n'entrent (et ne reçoivent les étapes) qu'après avoir effectué le comportement d'entrée, de sorte que les envois réalisés sont en retard par rapport à l'estimation initiale jusqu'à ce que ces actions se produisent.
- **Parcours d'audience :** les utilisateurs sont dirigés vers la branche de plus haute priorité pour laquelle ils sont éligibles, de sorte que les branches en aval peuvent recevoir moins d'utilisateurs que ne le suggère un simple décompte de Segment.
- **Vérifications d'audience et d'heure d'envoi :** les étapes complètes réévaluent les filtres au moment de l'envoi, sauf configuration contraire. Les utilisateurs qui étaient éligibles lors de la création du Canvas peuvent être exclus avant l'envoi d'un message.
- **Groupes de contrôle :** les groupes de contrôle globaux ou de Canvas retiennent une part des entrants hors de la communication.
- **Heures calmes et délais :** les messages peuvent être retenus ou replanifiés, décalant les envois hors de la fenêtre de reporting que vous consultez.
- **Plafonds d'entrée ou d'audience maximum :** les plafonds d'entrée ou d'envoi arrêtent les utilisateurs supplémentaires même lorsque le Segment sous-jacent est plus grand.
- **Fenêtre de reporting :** la plage d'analyse peut ne pas inclure tous les envois que vous comparez à l'estimation.

### Pourquoi l'audience estimée et le nombre d'utilisateurs du Canvas ne correspondent-ils pas ? {#why-dont-estimated-audience-and-canvas-user-counts-match}

L'**Audience estimée** reflète les utilisateurs qui correspondent à votre Segment et aux filtres d'entrée au moment où l'estimation est exécutée. Après ce moment, les entrées différées ou par événement, la rééligibilité, les déclenchements par API ou le routage des branches peuvent augmenter le nombre de profils qui touchent le parcours par rapport à l'instantané. Les utilisateurs peuvent également être exclus lorsque les filtres au moment de l'envoi échouent, ce qui réduit les entrées ou les envois réalisés. Comparez le timing, les plafonds et les paramètres d'évaluation en parallèle de [Pourquoi les envois sont-ils inférieurs à la taille de l'audience estimée ?](#why-are-sends-lower-than-the-estimated-audience-size).

### Pourquoi le nombre de _Destinataires uniques_ est-il supérieur au nombre d'utilisateurs ciblés ? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

Le nombre de _Destinataires uniques_ peut être supérieur à l'audience attendue car Braze suit les **destinataires uniques quotidiens** pour le reporting de Canvas et de Campaign. Cela permet une attribution de conversion précise à chaque fois qu'un utilisateur reçoit un message dans le parcours.

Par exemple, si un utilisateur reçoit une étape de Canvas le lundi et à nouveau le vendredi et convertit après chaque envoi, Braze peut compter deux lignes de destinataires et deux conversions dans le périmètre. Avec des entrées récurrentes ou la rééligibilité, le même petit ensemble de profils peut produire plusieurs _Destinataires uniques_ sur plusieurs jours.

### Pourquoi mon Canvas connaît-il des taux d'envoi en baisse ? {#why-is-my-canvas-experiencing-lower-send-rates}

Si vous constatez que votre Canvas planifié quotidiennement envoie à moins d'utilisateurs au fil du temps, vérifiez les points suivants :

- **Vérifiez si la rééligibilité est activée :** sans rééligibilité, Braze ne fait entrer chaque utilisateur dans le Canvas qu'une seule fois. Pour les Canvas planifiés quotidiennement, seuls les utilisateurs qui correspondent à l'audience et qui ne sont pas encore entrés dans le Canvas sont éligibles à chaque entrée. À mesure que davantage d'utilisateurs entrent, chaque entrée ultérieure dispose de moins d'utilisateurs éligibles, ce qui entraîne une baisse du volume d'entrée.
- **Vérifiez si l'audience a une composition fixe :** les audiences construites à partir d'une liste fixe d'utilisateurs (comme un [import CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) utilisé comme filtre de Segment) n'acquièrent pas automatiquement de nouveaux membres. Sans nouveaux entrants, le volume d'entrée ne peut pas se rétablir à mesure que les utilisateurs entrent dans le Canvas.

Pour les [limites de débit de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) et les autres facteurs qui réduisent les envois pour une occurrence unique, consultez [Pourquoi les envois sont-ils inférieurs à la taille de l'audience estimée ?](#why-are-sends-lower-than-the-estimated-audience-size).

### Pourquoi un petit Segment de groupe de contrôle affiche-t-il des changements dans l'historique de composition ? {#why-does-a-small-control-group-segment-show-changes-in-historical-membership}

Les graphiques d'historique de composition utilisent des échantillons estimés, de sorte que les petits Segments — y compris les Segments de [groupe de contrôle global]({{site.baseurl}}/user_guide/audience/global_control_group) — peuvent afficher des variations au jour le jour même lorsque l'audience sous-jacente est stable. Pour comprendre le fonctionnement des estimations et pourquoi les graphiques peuvent fluctuer, consultez [Consulter la taille historique de la composition d'un Segment]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#viewing-historical-segment-membership-size).

## Analyses et conversions {#analytics-and-conversions}

### Comment le tableau de bord des conversions attribue-t-il les conversions Canvas ? {#how-does-the-conversions-dashboard-attribute-canvas-conversions}

Le [tableau de bord des conversions]({{site.baseurl}}/user_guide/analytics/dashboards/conversions) attribue les conversions Canvas en fonction de la [méthode d'attribution]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#attribution-methods) que vous sélectionnez (par exemple, **Upon Receipt**, **Upon Send**, **Upon Open** ou **Upon Click**). Pour qu'un utilisateur apparaisse dans le rapport, il doit entrer dans le Canvas ou la Campaign, enregistrer la méthode d'attribution sélectionnée et effectuer l'événement de conversion dans les paramètres de votre rapport.

Pour les règles de conversion au niveau des étapes et des variantes dans les analyses Canvas, consultez [Comment les conversions des utilisateurs sont-elles suivies dans un Canvas ?](#how-are-user-conversions-tracked-in-a-canvas).

### Comment les conversions des utilisateurs sont-elles suivies dans un Canvas ? {#how-are-user-conversions-tracked-in-a-canvas}

Un utilisateur ne peut convertir qu'une seule fois par entrée dans un Canvas. Les conversions sont attribuées au dernier message reçu par l'utilisateur pour cette entrée. Le bloc récapitulatif au début d'un Canvas reflète toutes les conversions effectuées par les utilisateurs dans ce parcours, qu'ils aient reçu ou non un message. Chaque étape suivante n'affiche que les conversions qui se sont produites lorsque cette étape était la dernière reçue par l'utilisateur.

{% alert note %}
Lorsqu'un utilisateur entre à nouveau dans un Canvas, les événements de conversion ne sont suivis que pour l'entrée la plus récente. Les événements de conversion ne sont pas enregistrés pour les entrées précédentes, même si l'événement de conversion est renseigné rétroactivement.
{% endalert %}

{% details Développer pour voir les exemples %}

**Exemple 1**

Un parcours Canvas comporte 10 notifications push et l'événement de conversion est « démarrage de session » (« Ouvre l'application ») :

- L'utilisateur A ouvre l'application après être entré dans le Canvas mais avant de recevoir le premier message.
- L'utilisateur B ouvre l'application après chaque notification push.

**Résultat :** le récapitulatif affichera deux conversions, tandis que les étapes individuelles afficheront une conversion de un à la première étape et zéro pour toutes les étapes suivantes.

{% alert note %}
Si les heures calmes sont actives lorsque l'événement de conversion se produit, les mêmes règles s'appliquent.
{% endalert %}

**Exemple 2**

Un Canvas à une seule étape avec les heures calmes activées :

1. L'utilisateur entre dans le Canvas.
2. La première étape n'a pas de délai, mais se trouve dans la plage des heures calmes configurées, le message est donc supprimé.
3. L'utilisateur effectue l'événement de conversion.

**Résultat :** l'utilisateur sera compté comme converti dans la variante globale du Canvas, mais pas dans l'étape, car il n'a pas reçu l'étape.

{% enddetails %}

### Quelle est la différence entre les différents types de taux de conversion ? {#whats-the-difference-between-the-different-conversion-rate-types}

- Le total des conversions du Canvas reflète le nombre d'utilisateurs uniques ayant effectué un événement de conversion, et non le nombre de conversions que chacun a effectuées.
- Le taux de conversion de la variante ou le bloc récapitulatif au début d'un Canvas reflète toutes les conversions effectuées par les utilisateurs dans ce parcours, qu'ils aient reçu ou non un message, sous forme de total agrégé.
- Le taux de conversion de l'étape reflète le nombre d'individus ayant reçu cette étape de message et effectué l'un des événements de conversion définis.

### Pourquoi le taux de conversion de mon étape Canvas n'est-il pas égal au taux de conversion total de ma variante Canvas ? {#why-is-my-canvas-step-conversion-rate-not-equal-to-my-canvas-variant-total-conversion-rate}

Il est courant que le total des conversions d'une variante Canvas soit supérieur à la somme des totaux de ses étapes. Cela se produit parce qu'un utilisateur peut effectuer un événement de conversion pour une variante dès qu'il entre dans celle-ci. Cependant, ce même événement de conversion n'est pas comptabilisé pour une étape Canvas. Ainsi, tout utilisateur qui entre dans le Canvas et effectue l'événement de conversion avant de recevoir la première étape du Canvas est comptabilisé dans le total de conversion de la variante, mais pas dans le total de l'étape. Il en va de même pour un utilisateur qui entre dans le Canvas mais en sort avant de recevoir une étape.

Notez qu'il est également possible qu'un utilisateur entre dans une variante, ne reçoive aucun message d'une étape, puis convertisse. Dans ce cas, aucune conversion n'est enregistrée au niveau de l'étape. Cependant, comme l'utilisateur a techniquement converti, une conversion est enregistrée au niveau du Canvas.

### Comment puis-je confirmer si mes utilisateurs ont reçu un Canvas déclenché par API ? {#how-can-i-confirm-if-my-users-received-an-api-triggered-canvas}

Vous pouvez [créer un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) en utilisant un filtre Canvas pour confirmer si les utilisateurs sont entrés dans le Canvas ou ont reçu une étape Canvas spécifique. Par exemple, utilisez un filtre d'entrée Canvas si vous souhaitez confirmer que les utilisateurs sont entrés dans le Canvas déclenché par API, ou un filtre d'étape reçue si vous souhaitez confirmer qu'ils ont reçu un message du Canvas. Ensuite, utilisez l'[endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) pour exporter les utilisateurs de ce Segment.

### Puis-je supprimer un Canvas ? {#can-i-delete-a-canvas}

Non, mais vous pouvez [archiver un Canvas]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Comment reprendre un Canvas ou une Campaign archivé(e) ? {#how-do-i-resume-an-archived-canvas-or-campaign}

Les messages archivés ne sont pas envoyés tant que vous ne les ramenez pas dans un état modifiable. [Désarchivez]({{site.baseurl}}/user_guide/messaging/governance/archiving#unarchiving) la Campaign ou le Canvas, configurez le calendrier d'entrée ou l'heure d'envoi sur une fenêtre future (ou dupliquez le parcours si vous avez besoin d'une copie vierge), puis sélectionnez **Reprendre** ou lancez selon les besoins. Consultez [Archiver des Campaigns et des Canvas]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Pourquoi mon Canvas ne s'enregistre-t-il pas alors qu'aucune erreur n'apparaît ? {#why-doesnt-my-canvas-save-when-no-error-appears}

Des filtres **Attribut personnalisé** vides dans les filtres d'audience ou au niveau des étapes peuvent bloquer l'enregistrement sans message de validation détaillé. Ouvrez chaque carte de filtre, supprimez les règles d'attribut personnalisé incomplètes ou saisissez à la fois le nom et la valeur de l'attribut, puis sélectionnez **Enregistrer** à nouveau.

### Pourquoi une étiquette a-t-elle disparu de mon Canvas ou de ma Campaign ? {#why-did-a-tag-disappear-from-my-canvas-or-campaign}

Lorsqu'une [étiquette]({{site.baseurl}}/user_guide/messaging/governance/tags) est supprimée de votre espace de travail, Braze la retire de chaque Campaign et Canvas qui la référençait. Ce nettoyage ne génère pas toujours sa propre ligne dans le journal des modifications d'un Canvas.

### Comment puis-je consulter les analyses de chacun de mes composants Canvas ? {#how-can-i-view-analytics-for-each-of-my-canvas-components}

Pour consulter les analyses d'un composant Canvas, accédez à votre Canvas et faites défiler la page **Canvas Details**. Vous pouvez y voir les analyses de chaque composant. Consultez [Analyses Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics) pour plus de détails.

### Quand l'engagement d'une étape Canvas est-il visible sur un profil utilisateur ? {#when-is-engagement-from-a-canvas-step-visible-on-a-user-profile}

Les filtres tels que `Received Message from Canvas Step` se mettent à jour après que Braze enregistre l'événement d'envoi, de réception ou d'engagement correspondant pour cette étape. Les messages in-app peuvent enregistrer les impressions séparément des indicateurs de type envoi. Consultez [Pourquoi un Canvas peut-il afficher zéro envoi alors que des impressions sont enregistrées ?](#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged). Ces mêmes événements apparaissent dans les indicateurs de l'étape sur **Canvas Details**.

### En ce qui concerne le nombre d'utilisateurs uniques, les analyses Canvas ou le segmenteur sont-ils plus précis ? {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

Le segmenteur fournit des statistiques plus précises pour les données d'utilisateurs uniques que les statistiques Canvas ou Campaign. En effet, les statistiques Canvas et Campaign sont des nombres que Braze incrémente lorsqu'un événement se produit, ce qui signifie que des variables pourraient entraîner un écart entre ce nombre et celui du segmenteur. Par exemple, les utilisateurs peuvent convertir plus d'une fois pour un Canvas ou une Campaign.

### Pourquoi le nombre d'utilisateurs entrant dans un Canvas ne correspond-il pas au nombre attendu ? {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

Le nombre d'utilisateurs entrant dans un Canvas peut différer du nombre attendu en raison de la manière dont les audiences et les déclencheurs sont évalués. Dans Braze, une audience est évaluée avant le déclencheur (sauf en cas d'utilisation d'un déclencheur de [changement d'attribut]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Les utilisateurs seront donc exclus du Canvas s'ils ne font pas partie de l'audience sélectionnée avant l'évaluation des actions de déclenchement.

### Que se passe-t-il avec les utilisateurs anonymes pendant leur parcours Canvas ? {#what-happens-to-anonymous-users-during-their-canvas-journey}

Bien que les utilisateurs anonymes puissent entrer et sortir des Canvas, leurs actions ne sont pas associées à un profil utilisateur spécifique tant qu'ils ne sont pas identifiés, de sorte que leurs interactions peuvent ne pas être entièrement suivies dans vos analyses. Vous pouvez utiliser le [générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder) pour générer un rapport de ces indicateurs.

{% alert tip %}
Pour obtenir une aide supplémentaire sur la résolution des problèmes Canvas, contactez le support Braze dans les 30 jours suivant la survenue de votre problème, car nous ne conservons que les 30 derniers jours de journaux de diagnostic.
{% endalert %}

### Puis-je exclure les utilisateurs actuellement dans un parcours Canvas d'une Campaign ou d'un Segment ? {#can-i-exclude-users-who-are-currently-in-a-canvas-journey-from-a-campaign-or-segment}

Utilisez des [filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) tels que `Entered Canvas Variation`, `In Canvas Control Group` ou `Received Message from Canvas Step` pour cibler les utilisateurs en fonction de l'entrée dans le Canvas, de l'affectation à une variante ou de l'engagement avec une étape. Ces filtres évaluent l'historique des entrées et les interactions — ils n'indiquent pas si un utilisateur progresse encore dans un parcours actif.

Pour inclure ou exclure des utilisateurs en fonction de leur participation active à un Canvas, ajoutez des étapes [Mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) à l'entrée et à la sortie du Canvas pour définir et effacer des attributs personnalisés, puis filtrez sur ces attributs dans les Campaigns ou les Segments.

## Segmentation {#segmentation}

### Quelle est la différence entre « N'est pas entré dans la variante du Canvas » et « N'est pas dans le groupe de contrôle du Canvas » ? {#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group}

Consultez les [filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) pour obtenir les définitions complètes des filtres.

#### N'est pas entré dans la variante du Canvas {#has-not-entered-canvas-variation}

L'utilisateur n'est jamais entré dans un parcours de variante d'un Canvas spécifique. Tous les utilisateurs qui ne font pas partie du groupe de contrôle sont inclus, qu'ils soient ou non entrés dans le Canvas. Cela comprend les utilisateurs qui sont entrés dans une autre variante et ceux qui ne sont entrés dans aucune variante.

#### N'est pas dans le groupe de contrôle du Canvas {#is-not-in-canvas-control-group}

L'utilisateur est entré dans le Canvas, mais ne fait pas partie du groupe de contrôle et a par conséquent reçu une variante. Seuls les utilisateurs qui sont entrés dans le Canvas sont inclus.

Notez que l'attribution de la variante se fait à l'entrée dans le Canvas. Si un utilisateur n'est pas entré dans un Canvas, aucune variante ne lui sera attribuée. Autrement dit, il ne fera partie ni du groupe de contrôle, ni d'une variante.

## Éditeur Canvas d'origine {#original-canvas-editor}

{% details Développer pour les FAQ de l'éditeur Canvas d'origine %}

### Comment convertir un Canvas existant de l'éditeur d'origine vers l'éditeur actuel ? {#how-do-i-convert-an-existing-canvas-from-the-original-editor-to-the-current-editor}

Vous pouvez [cloner votre Canvas]({{site.baseurl}}/cloning_canvases). Cela crée une copie de votre Canvas d'origine dans le flux de travail Canvas le plus récent.

### Quelles sont les principales différences entre les éditeurs Canvas actuel et d'origine ? {#what-are-the-main-differences-between-the-current-and-original-canvas-editors}

#### Barre d'outils des composants Canvas {#canvas-component-toolbar}

Auparavant, avec l'éditeur Canvas d'origine, une étape complète était ajoutée par défaut chaque fois que vous créiez une étape dans votre parcours utilisateur. Ces étapes complètes sont remplacées par différents composants Canvas, ce qui vous offre l'avantage d'une visibilité accrue et d'une personnalisation améliorée pour votre expérience d'édition. Vous pouvez immédiatement voir tous vos composants Canvas depuis la barre d'outils des étapes Canvas.

#### Comportement des étapes {#step-behavior}

Auparavant, chaque étape complète incluait des informations telles que les paramètres de délai et de planification, les événements d'exception, les filtres d'audience, la configuration des messages et les options d'avancement des messages, le tout dans un seul composant. Ces paramètres sont séparés dans l'éditeur actuel pour rendre votre expérience de création de Canvas plus personnalisable et introduisent quelques différences de fonctionnalité.

#### Avancement du composant Message {#message-component-advancement}

Les [composants Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) font avancer tous les utilisateurs qui entrent dans l'étape. Il n'est pas nécessaire de spécifier le comportement d'avancement des messages, ce qui simplifie la configuration globale de l'étape. Si vous souhaitez implémenter l'option **Avancer lorsque le message est envoyé**, ajoutez un parcours d'audience séparé pour filtrer les utilisateurs qui n'ont pas reçu l'étape précédente.

#### Comportement du délai « dans » {#delay-in-behavior}

Les [composants Délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) attendront la totalité du temps de délai avant de passer à l'étape suivante.

Supposons que le 12 avril, nous avons un composant Délai dont le délai est configuré pour envoyer votre utilisateur à l'étape suivante dans un jour à 14 h. Un utilisateur entre dans le composant à 14 h 01 le 13 avril.
- Pour le flux de travail d'origine, l'utilisateur passerait à l'étape suivante à 14 h le 14 avril, soit moins d'un jour après l'heure d'entrée.
- Dans l'éditeur actuel, l'utilisateur passerait à l'étape suivante à 14 h le 15 avril. Notez que c'est la même heure, mais plus d'un jour après l'heure d'entrée.

#### Comportement du timing intelligent {#intelligent-timing-behavior}

Comme le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) est stocké dans le composant Message, les délais seront appliqués avant les calculs du timing intelligent. Cela signifie que, selon le moment où un utilisateur entre dans le composant, il peut recevoir le message plus tard qu'il ne le recevrait dans un Canvas construit avec le flux de travail Canvas d'origine.

Supposons que votre délai est configuré sur 2 jours, que le timing intelligent est activé et qu'il a déterminé que le meilleur moment pour envoyer votre message est 14 h. Un utilisateur entre dans l'étape Délai à 14 h 01.
- **Flux de travail actuel :** Il faudra 48 heures pour que le délai s'écoule, donc l'utilisateur reçoit le message le troisième jour à 14 h.
- **Flux de travail d'origine :** L'utilisateur reçoit le message le deuxième jour à 14 h.

Notez que si le timing intelligent est activé, le message sera envoyé dans les 24 heures suivant l'entrée de l'utilisateur dans le composant Message à l'heure intelligente identifiée (même si aucun composant Délai n'est impliqué).

#### Événements d'exception {#exception-events}

##### Heures calmes {#quiet-hours}

L'événement d'exception est appliqué à l'aide des parcours d'action, qui sont séparés des étapes Message. Les heures calmes sont appliquées dans le composant Message. Cela signifie que si un utilisateur a déjà passé le parcours d'action (et n'a pas été exclu par l'événement d'exception), puis rencontre les heures calmes lorsqu'il arrive au composant Message, et que son Canvas est configuré de sorte que le message soit renvoyé après la période d'heures calmes, l'événement d'exception ne sera plus appliqué. Notez que ce cas d'usage n'est pas courant.

Pour les segments et les filtres, l'étape Message dispose de validations de distribution qui permettent aux utilisateurs de configurer des segments et filtres supplémentaires qui sont validés au moment de l'envoi. Cela empêche le cas limite mentionné ci-dessus concernant les heures calmes.

##### Paramètre de planification « dans » ou « au prochain » {#in-or-on-the-next-schedule-setting}

Les événements d'exception sont créés à l'aide des parcours d'action. Les parcours d'action ne prennent en charge que « après une fenêtre temporelle de X » et non « dans X temps » ou « au prochain X temps ».

{% enddetails %}

### Que dois-je inclure lors de la soumission d'un ticket d'assistance pour une erreur « Request Timed Out » ? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Si vous rencontrez une erreur « Request Timed Out » lors de la modification d'un Canvas et que vous devez contacter l'[assistance Braze]({{site.baseurl}}/braze_support), incluez les informations suivantes pour accélérer la résolution :

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='canvas' %}

## Réception Canvas et résolution des problèmes {#canvas-delivery-and-troubleshooting}

### Les utilisateurs orphelins sont-ils éligibles pour recevoir des messages Canvas ? {#are-orphaned-users-eligible-to-receive-canvas-messages}

Non. Les [utilisateurs orphelins]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users) ne sont pas éligibles pour recevoir des messages. Si un profil devient orphelin alors qu'un utilisateur se trouve dans un parcours Canvas, il quitte silencieusement le flux. L'analyse ne montre pas toujours un événement **Exited** pour cette sortie, et le résumé du workflow peut inclure un `partial_update_token` sans `exited_date` ni `exit_reason`.

Pour plus d'informations sur les fusions et les profils orphelins, consultez [Fusionner les utilisateurs en double]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

### Si j'arrête un Canvas ou une Campaign actifs, les messages déjà envoyés au fournisseur de services d'e-mailing sont-ils quand même distribués ? {#if-i-stop-an-active-canvas-or-campaign-do-messages-already-sent-to-the-esp-still-deliver}

Oui. Après que Braze a envoyé une requête à votre fournisseur de services d'e-mailing (ESP), Braze ne peut pas rappeler cet envoi. L'arrêt d'un Canvas ou d'une Campaign empêche de nouvelles requêtes d'envoi, mais les messages déjà transmis à l'ESP peuvent encore être distribués et peuvent encore incrémenter les compteurs d'envois au fur et à mesure que l'ESP les traite.

Il s'agit du même comportement décrit pour [l'arrêt d'un Canvas](#what-happens-when-you-stop-a-canvas) : les envois d'e-mails en cours ne sont pas immédiatement interrompus.

### Comment puis-je confirmer qu'une étape webhook Canvas s'est déclenchée sans contenu visible pour l'utilisateur ? {#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content}

Braze suit les **envois** de webhooks et les résultats de distribution associés pour les étapes [Webhook]({{site.baseurl}}/user_guide/channels/webhooks) dans les Campaigns et les Canvas. Utilisez l'analyse des étapes, les [rapports de webhooks]({{site.baseurl}}/user_guide/channels/webhooks/reporting) ou les événements webhooks [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) pour confirmer que l'étape a été exécutée. Les journaux de requêtes de votre endpoint fournissent une confirmation supplémentaire lorsque vous avez besoin d'une preuve de réception côté serveur.

Braze n'inclut pas de pixel de suivi invisible intégré pour les étapes webhook. Appuyez-vous sur les indicateurs webhook de Braze et sur la journalisation de votre endpoint plutôt que sur des requêtes d'images d'un pixel personnalisées.

### Pourquoi mon étape webhook n'a-t-elle pas de champ de corps de requête ? {#why-does-my-webhook-step-have-no-body-field}

Les étapes webhook utilisent un corps de requête pour `POST`, `PUT`, `PATCH` et `DELETE`. Si vous changez la méthode en `GET`, Braze supprime le champ de corps car les requêtes GET ne prennent pas en charge un corps de requête. Repassez à une méthode prenant en charge un corps si vous devez envoyer du JSON ou des données de formulaire. Pour plus de détails sur les méthodes, consultez [Créer un webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#http-method).

### Comment utiliser spacer.gif dans une étape webhook ? {#how-do-i-use-spacergif-in-a-webhook-step}

Braze héberge une image de remplacement `spacer.gif` sur `cdn.braze.com` et `braze-images.com`. Certaines équipes pointent l'URL d'un webhook vers cette image lorsqu'une étape doit se déclencher sans appeler un endpoint externe. Les étapes webhook standard doivent appeler un véritable endpoint. Utilisez les [rapports de webhooks]({{site.baseurl}}/user_guide/channels/webhooks/reporting) et les journaux de votre endpoint pour confirmer la distribution, comme décrit dans [Comment puis-je confirmer qu'une étape webhook Canvas s'est déclenchée sans contenu visible pour l'utilisateur ?](#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content).

### Pourquoi mon Canvas ne se charge-t-il pas avec une erreur « invalid next-step-id » ? {#why-wont-my-canvas-load-with-an-invalid-next-step-id-error}

Cette erreur de console signifie qu'au moins une étape pointe vers une étape suivante manquante ou invalide, par exemple après une suppression partielle, un clonage ou un import. Ouvrez le Canvas dans l'éditeur, reconnectez les étapes orphelines ou supprimez les étapes qui n'ont plus de chemin valide en aval. Si le Canvas ne se charge toujours pas, contactez le [support Braze]({{site.baseurl}}/braze_support) avec l'ID du Canvas et une capture d'écran de l'erreur de console.

### Pourquoi un horodatage de conversion Canvas dans Currents diffère-t-il de mon analyse Canvas ? {#why-does-a-canvas-conversion-timestamp-in-currents-differ-from-my-canvas-analytics}

Currents enregistre les conversions Canvas sous forme d'événements [`users.canvas.Conversion`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-conversion-events). Le champ `time` de l'événement correspond au moment où l'événement de conversion s'est produit. Le champ `conversion_behavior` de cet événement décrit la définition de la conversion (type et fenêtre). L'analyse Canvas peut également agréger les conversions par rapport à l'entrée dans le Canvas dans la fenêtre de conversion. Lors du rapprochement des exportations, comparez le `time` Currents à l'horodatage de l'événement de conversion et aux paramètres de votre fenêtre de conversion Canvas.

### Pourquoi `canvas_step_name` est-il nul dans Currents ? {#why-is-canvas_step_name-null-in-currents}

Les champs de nom de Campaign et de Canvas tels que `canvas_step_name` peuvent être `null` lorsqu'un événement Currents est envoyé avant que Braze n'ait fini de propager les métadonnées de l'étape, par exemple après la création ou le renommage d'une étape. Pour plus de détails, consultez [Pourquoi le nom de la Campaign ou de l'étape Canvas est-il `NULL` dans mes données Currents ?]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data).

### Pourquoi mon tableau ne se met-il pas à jour dans une étape de mise à jour de l'utilisateur ? {#why-isnt-my-array-updating-in-a-user-update-step}

Vérifiez le JSON dans votre étape [Mise à jour de l'utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Les mises à jour de tableaux et d'attributs imbriqués nécessitent des chemins et des valeurs valides pour l'attribut que vous modifiez. N'incluez pas les champs que l'étape fournit automatiquement, comme l'ID utilisateur externe. Utilisez l'onglet **Aperçu et test** de l'étape pour confirmer le payload avant le lancement.

### Puis-je envoyer des messages Canvas à des utilisateurs sans `external_id` ? {#can-i-send-canvas-messages-to-users-without-an-external_id}

Oui, si un profil utilisateur Braze existe déjà. Les utilisateurs sans `external_id` sont des [utilisateurs anonymes]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles) et peuvent être référencés avec un `braze_id` ou un [alias d'utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases). Créez ou mettez à jour le profil avec l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ou votre SDK avant l'entrée dans le Canvas, puis utilisez une [entrée par événement ou déclenchée par API]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule). Le ciblage Canvas standard nécessite toujours un profil utilisateur Braze — vous ne pouvez pas envoyer de messages Canvas à une adresse e-mail seule sans profil.

### Pourquoi un utilisateur est-il entré dans un Canvas moins de fois qu'il n'a déclenché l'événement ? {#why-did-a-user-enter-a-canvas-fewer-times-than-they-performed-the-trigger-event}

Pour les Canvas par événement et déclenchés par API, Braze déduplique les événements déclencheurs de sorte qu'un utilisateur puisse entrer au maximum environ **une fois par seconde** pour le même Canvas. Si un utilisateur déclenche le même événement plusieurs fois en une seconde, une seule entrée est traitée.

Pour permettre plusieurs entrées dans la même seconde, espacez les événements déclencheurs d'au moins 1,1 seconde (par exemple, lorsque vous contrôlez la synchronisation des événements depuis votre serveur). Pour un comportement de type Campaign permettant plusieurs déclenchements dans la même seconde, comparez votre cas d'usage aux [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns) avec des paramètres de planification et de rééligibilité appropriés.

### Quand les utilisateurs sont-ils dédupliqués dans les Canvas déclenchés par API ? {#when-are-users-de-duplicated-in-api-triggered-canvases}

Si un utilisateur entre à nouveau dans un Canvas déclenché par API et atteint une étape de délai où il est déjà en file d'attente depuis une entrée précédente pour un message identique, Braze déduplique l'utilisateur pour éviter les envois en double. La deuxième instance du Canvas se termine, de sorte que le nombre d'entrées peut dépasser le nombre d'envois.

### Pourquoi une notification push de test arrive-t-elle dans la mauvaise application, alors que les envois réels semblent corrects ? {#why-does-a-test-push-go-to-the-wrong-app-but-live-sends-look-correct}

La fonctionnalité **Test push** sur un profil utilisateur envoie la notification à tous les appareils activés pour les push de ce profil. Lorsque plusieurs applications sont installées sur un appareil, le système d'exploitation distribue généralement la notification de test à la première application disponible, qui peut ne pas être celle que vous souhaitez valider.

Pour confirmer le ciblage spécifique à une application, envoyez un message en conditions réelles ou de test via une Campaign ou un Canvas avec une audience restreinte (par exemple, filtrez par `external_id`) au lieu de vous fier uniquement à **Test push** sur le profil.

Pour les étapes Message du **Canvas** avec plusieurs applications, activez **Valider l'audience au moment de l'envoi du message** sur l'étape Message afin que les vérifications de Segment et de filtres s'exécutent au moment de l'envoi. Pour plus d'informations, consultez [Étape Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

Pour le comportement général du test push, consultez [Envoi de messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) et [FAQ Push]({{site.baseurl}}/user_guide/channels/push/faqs).

### Comment déboguer les Push Stories sur iOS et Android ? {#how-do-i-debug-push-stories-on-ios-and-android}

Commencez par [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories) pour la configuration et les exigences créatives. Pour l'implémentation et la gestion des notifications enrichies, consultez [Notifications enrichies]({{site.baseurl}}/developer_guide/push_notifications/rich) et [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories) dans le guide développeur.

### Qui reçoit l'e-mail « Canvas Messages Delayed 24+ Hours » ? {#who-receives-the-canvas-messages-delayed-24-hours-email}

Braze envoie cette notification lorsque des messages Canvas sont retardés de 24 heures ou plus en raison de la limitation du débit. L'e-mail est envoyé aux utilisateurs du tableau de bord qui ont précédemment apporté des modifications au Canvas concerné (en se basant sur les journaux de modifications du Canvas). Si Braze ne peut pas déterminer ces destinataires, l'e-mail est envoyé aux **administrateurs de l'entreprise** de l'espace de travail.

### Quand un utilisateur cesse-t-il de recevoir des messages après un événement d'exception ? {#when-does-a-user-stop-receiving-messages-after-an-exception-event}

Braze enregistre la sortie dès que l'événement d'exception se produit, mais les utilisateurs peuvent rester dans une étape jusqu'à ce que les minuteries se terminent — c'est particulièrement visible dans les étapes de délai. Le comportement diffère également entre les étapes planifiées et les étapes déclenchées par événement. Pour les chronologies, les exemples et les nuances d'analyse, consultez [Critères de sortie]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria).

### Pourquoi mon étape de parcours d'action affiche-t-elle une erreur lorsque je sélectionne une interaction d'alias de lien ? {#why-does-my-action-paths-step-show-an-error-when-i-select-a-link-alias-interaction}

Les groupes d'actions qui utilisent des déclencheurs d'interactivité e-mail (par exemple, **Clic sur un alias dans l'e-mail** ou **A cliqué sur un alias dans n'importe quelle Campaign ou étape Canvas**) nécessitent une étape Message qui a déjà envoyé le message contenant ce lien. Ajoutez ou réorganisez les étapes pour que l'e-mail soit envoyé avant que l'étape de parcours d'action n'évalue le clic, ou choisissez une interaction correspondant à un message que l'utilisateur a déjà reçu dans ce Canvas. Pour la liste complète des déclencheurs d'interaction, consultez [Livraison par événement]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

### Comment les horodatages historiques des événements personnalisés affectent-ils les Canvas et les Campaigns par événement ? {#how-do-historical-custom-event-timestamps-affect-action-based-canvases-and-campaigns}

Braze évalue les parcours par événement lorsque les événements qualifiants sont ingérés et que l'utilisateur remplit vos critères d'audience. Si un événement arrive sur le profil en dehors de la fenêtre pendant laquelle votre Canvas ou votre Campaign était actif, ou avant que l'utilisateur ne corresponde à votre audience, l'entrée ou les envois en aval peuvent ne pas se produire comme prévu. Comparez les horodatages des événements aux moments de mise en production et à l'appartenance au Segment en utilisant le journal d'activité du profil utilisateur et les étapes de résolution des problèmes décrites dans [Résolution des problèmes liés aux événements personnalisés]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#troubleshooting-custom-events). Si le comportement ne correspond toujours pas à vos attentes, contactez le [support Braze]({{site.baseurl}}/braze_support).