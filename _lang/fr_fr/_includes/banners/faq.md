# Questions fréquemment posées {#frequently-asked-questions}

> Voici les réponses aux questions fréquemment posées sur les bannières dans Braze. Pour des informations plus générales, consultez [À propos des bannières]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}).

## Quand les mises à jour des bannières apparaissent-elles pour les utilisateurs ? {#when-do-banner-updates-appear-for-users}

Les bannières sont actualisées avec leurs dernières données chaque fois que vous appelez la méthode d'actualisation — il n'est pas nécessaire de renvoyer ou de mettre à jour votre Campaign de bannières.

## Combien de placements puis-je demander au cours d'une session ? {#how-many-placements-can-i-request-in-a-session}

Dans une seule requête d'actualisation, vous pouvez demander un maximum de 10 placements. Pour chacun d'entre eux, Braze renvoie la bannière de priorité la plus élevée à laquelle l'utilisateur est éligible. Les requêtes supplémentaires renvoient une erreur.

Pour plus d'informations, consultez [Requêtes de placement]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## Combien de Campaigns de bannières peuvent être actives simultanément ? {#how-many-banner-campaigns-can-be-active-simultaneously}

Chaque espace de travail peut prendre en charge jusqu'à 200 Campaigns de bannières actives. Si cette limite est atteinte, vous devrez [archiver ou désactiver]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses#changing-the-status) une Campaign existante avant d'en créer une nouvelle.

## Pour les Campaigns partageant un emplacement, quelle bannière est affichée en premier ? {#for-campaigns-sharing-a-placement-which-banner-is-displayed-first}

Si un utilisateur est éligible à plusieurs Campaigns de bannières partageant le même emplacement, la bannière ayant la priorité la plus élevée est affichée. Pour plus d'informations, consultez [Priorité des bannières]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## Puis-je utiliser les bannières dans mon flux Content Cards existant ? {#can-i-use-banners-in-my-existing-content-card-feed}

Les bannières sont différentes des Content Cards, ce qui signifie que vous ne pouvez pas utiliser les bannières et les Content Cards dans le même flux. Pour remplacer les flux Content Cards existants par des bannières, vous devrez [créer des placements dans votre application ou site web]({{site.baseurl}}/developer_guide/banners/placements).

## En quoi les bannières diffèrent-elles des messages in-app ? {#how-are-banners-different-from-in-app-messages}

Les bannières et les [messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages) atteignent tous deux les utilisateurs au sein de votre application ou de votre site web, mais ils utilisent des modèles de distribution différents. Si vous comparez les bannières à une configuration existante de messages in-app, attendez-vous à des différences au niveau des déclencheurs, du rythme d'actualisation et des tests, et non à une correspondance exacte.

| Sujet | Bannières | Messages in-app |
| --- | --- | --- |
| Où les messages apparaissent | En ligne aux [emplacements]({{site.baseurl}}/developer_guide/banners/placements) que vous définissez dans votre application ou votre site | Superpositions plein écran, modales ou glissantes gérées par le SDK |
| Quand le contenu se met à jour | Lorsque votre application ou votre site appelle une actualisation de bannière (par exemple au démarrage de session ou en cours de session) | Les messages modélisés évaluent le Liquid lorsque le message in-app est déclenché (par exemple lors d'un événement personnalisé ou au démarrage de session), après la mise en cache du payload sur l'appareil |
| Déclencheurs basés sur les actions | Pas de [livraison par événement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery) ; utilisez plutôt les Segments, la priorité et le rythme d'actualisation | Prend en charge la livraison par événement et la livraison déclenchée par API |
| Tests | Prévisualisez un utilisateur, puis confirmez que l'actualisation de l'emplacement dans votre application ou votre site affiche la bannière attendue | Utilisez **Test Send** ou les flux de prévisualisation in-app pour l'affichage basé sur les déclencheurs |
| Rapports | Les vues et les clics de bannière suivent l'analytique des bannières | Les impressions et les clics in-app suivent l'analytique des messages in-app |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="En quoi les bannières diffèrent-elles des messages in-app ?" }

## Les bannières peuvent-elles inclure de la vidéo ? {#can-banners-include-video}

Le générateur de bannières standard prend en charge les images, le texte et les boutons. Pour inclure une vidéo dans une bannière, vous pouvez utiliser un bloc **Custom Code** dans le générateur, ou créer l'intégralité de la bannière avec l'éditeur HTML et intégrer un lecteur vidéo directement dans votre code HTML.

## Puis-je déclencher une bannière en fonction des actions de l'utilisateur ? {#can-i-trigger-a-banner-based-on-user-actions}

Bien que les bannières ne prennent pas en charge la [livraison par événement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery), vous pouvez cibler les utilisateurs en fonction de leurs actions passées à l'aide de la segmentation et de la priorité.

Par exemple, pour afficher une bannière spéciale uniquement aux utilisateurs ayant effectué un événement `purchase` :
1. **Ciblage :** Dans votre Campaign, ciblez un Segment d'utilisateurs ayant effectué l'événement personnalisé `purchase` au moins une fois.
2. **Priorité :** Si vous avez une bannière générale pour tous les utilisateurs et cette bannière spécifique pour les acheteurs ciblant le même emplacement, définissez la priorité de la bannière spécifique sur **High** et celle de la bannière générale sur **Medium** ou **Low**.

Lorsque l'utilisateur démarre une nouvelle session ou actualise les bannières après avoir effectué l'action, Braze évalue son éligibilité. S'il correspond au Segment « Purchase », la bannière à haute priorité est affichée.

## Les utilisateurs peuvent-ils fermer une bannière ? {#can-users-dismiss-a-banner}

Oui. Vous pouvez permettre aux utilisateurs de fermer manuellement une bannière. Consultez [Configurer le comportement de fermeture]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#dismiss-behavior) pour savoir comment configurer la fermeture dans le générateur et dans l'éditeur HTML.

Les utilisateurs ne peuvent fermer manuellement les bannières que si le comportement de fermeture est activé. Si la fermeture n'est pas activée, vous pouvez contrôler la visibilité de la bannière en gérant l'éligibilité du Segment de l'utilisateur. Lorsqu'un utilisateur ne remplit plus les critères de ciblage d'une Campaign de bannière, il ne la verra plus lors de sa prochaine session.

Lorsqu'un utilisateur ferme une bannière, il n'est plus éligible pour cette Campaign par défaut. Pour permettre aux utilisateurs ayant fermé la bannière de la revoir, [configurez la rééligibilité]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility) dans l'étape **Delivery Controls** de la Campaign. Les étapes de bannière Canvas utilisent les paramètres de réentrée Canvas pour contrôler la rééligibilité à la place.

Par exemple, si vous affichez une bannière promotionnelle jusqu'à ce qu'un utilisateur effectue un achat, l'enregistrement d'un événement tel que `purchase_completed` peut retirer cet utilisateur du Segment ciblé, masquant ainsi la bannière lors des sessions suivantes.

## Puis-je exporter les analyses de Campaigns de bannières à l'aide de l'API Braze ? {#can-i-export-banners-campaign-analytics-using-the-braze-api}

Oui. Vous pouvez utiliser l'[endpoint `/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) pour obtenir des données sur le nombre de Campaigns de bannières qui ont été vues, cliquées ou converties.

## Quand les utilisateurs sont-ils segmentés ? {#when-are-users-segmented}

Les utilisateurs sont segmentés au début de la session. Si les Segments ciblés d'une Campaign dépendent d'attributs personnalisés, d'événements personnalisés ou d'autres attributs de ciblage, ceux-ci doivent être présents sur l'utilisateur au début de la session.

## Comment composer des bannières pour garantir la latence la plus faible ? {#how-can-i-compose-banners-to-ensure-the-lowest-latency}

Plus le contenu de votre bannière est simple, plus elle s'affiche rapidement. Il est préférable de tester votre Campaign de bannière par rapport à la latence attendue pour votre cas d'usage. Par exemple, assurez-vous de tester les attributs Liquid comme `catalog_items`.

Si vous utilisez le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) (en accès anticipé), sachez que chaque appel est décompté d'un budget de rendu partagé d'environ deux secondes pour l'ensemble des emplacements lors d'une seule actualisation. Si le budget est dépassé ou qu'un appel expire, le résultat du contenu connecté est traité comme nul, et les bannières ne réessaient pas. Pour minimiser la latence :

- Gardez vos endpoints rapides et [mettez les réponses en cache]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) autant que possible.
- Limitez le nombre d'URL de contenu connecté uniques parmi les emplacements qui s'affichent ensemble.
- Évitez de chaîner les appels lorsqu'une réponse de contenu connecté détermine l'URL de l'appel suivant.
- Utilisez des instructions de garde Liquid ou le [filtre `default`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) pour gérer les résultats nuls et éviter les bannières vides.

## Toutes les étiquettes Liquid sont-elles prises en charge ? {#are-all-liquid-tags-supported}

Non. Cependant, la plupart des étiquettes Liquid sont prises en charge pour les messages de type bannière, à l'exception de `catalog_items` qui sont re-rendus à l'aide de [l'étiquette `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs#using-liquid).

## Puis-je capturer les événements de clic ? {#can-i-capture-click-events}

Oui. La manière dont les événements de clic sont capturés dépend de la façon dont votre bannière est rendue :

- **Générateur — composants standard :** Si votre bannière utilise des composants standard de l'éditeur (images, boutons, texte), les clics sont suivis automatiquement lorsque vous utilisez les méthodes d'insertion du SDK.
- **Générateur — blocs de code personnalisé :** Si vous souhaitez suivre les clics pour des éléments au sein d'un bloc de l'éditeur de code personnalisé, vous devez appeler `brazeBridge.logClick()` depuis votre HTML personnalisé. Cela s'applique même lorsque vous utilisez les méthodes du SDK pour insérer et afficher la bannière.
- **Éditeur HTML :** Le suivi des clics n'est pas automatique. Vous devez appeler `brazeBridge.logClick()` pour chaque élément cliquable que vous souhaitez suivre. Pour la référence complète, consultez [Code personnalisé et pont JavaScript pour les bannières]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).
- **Interface personnalisée (headless) :** Si vous créez une interface entièrement personnalisée en utilisant les propriétés personnalisées de la bannière au lieu d'afficher le HTML de la bannière, appelez `logClick()` sur l'objet bannière depuis le code de votre application.

Pour plus d'informations, consultez [Enregistrement des clics]({{site.baseurl}}/developer_guide/banners/placements#logging-clicks).