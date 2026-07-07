# Questions fréquemment posées {#frequently-asked-questions}

> Voici les réponses aux questions fréquemment posées sur les bannières dans Braze. Pour des informations plus générales, consultez [À propos des bannières]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}/).

## Quand les mises à jour des bannières apparaissent-elles pour les utilisateurs ? {#when-do-banner-updates-appear-for-users}

Les bannières sont actualisées avec leurs dernières données chaque fois que vous appelez la méthode d'actualisation&#8212;il n'est pas nécessaire de renvoyer ou de mettre à jour votre campagne de bannières.

## Combien d'emplacements puis-je demander au cours d'une session ? {#how-many-placements-can-i-request-in-a-session}

Dans une seule requête d'actualisation, vous pouvez demander un maximum de 10 emplacements. Pour chacun d'entre eux, Braze renverra la bannière ayant la priorité la plus élevée à laquelle l'utilisateur est éligible. Toute demande supplémentaire renverra une erreur.

Pour plus d'informations, consultez [Demandes d'emplacement]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## Combien de campagnes de bannières peuvent être actives simultanément ? {#how-many-banner-campaigns-can-be-active-simultaneously}

Chaque espace de travail peut prendre en charge jusqu'à 200 campagnes de bannières actives. Si cette limite est atteinte, vous devrez [archiver ou désactiver]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) une campagne existante avant d'en créer une nouvelle.

## Pour les campagnes partageant un emplacement, quelle bannière est affichée en premier ? {#for-campaigns-sharing-a-placement-which-banner-is-displayed-first}

Si un utilisateur est éligible à plusieurs campagnes de bannières partageant le même emplacement, la bannière ayant la priorité la plus élevée sera affichée. Pour plus d'informations, consultez [Priorité des bannières]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## Puis-je utiliser des bannières dans mon flux de Content Cards existant ? {#can-i-use-banners-in-my-existing-content-card-feed}

Les bannières sont différentes des Content Cards, ce qui signifie que vous ne pouvez pas utiliser des bannières et des Content Cards dans le même flux. Pour remplacer les flux de Content Cards existants par des bannières, vous devrez [créer des emplacements dans votre application ou votre site web]({{site.baseurl}}/developer_guide/banners/placements/).

## Les bannières peuvent-elles inclure de la vidéo ? {#can-banners-include-video}

Le compositeur de bannières standard prend en charge les images, le texte et les boutons. Pour inclure une vidéo dans une bannière, vous pouvez utiliser un bloc **Custom Code** et afficher une vidéo ou un lecteur intégré dans votre application ou votre site web.

## Puis-je déclencher une bannière en fonction des actions de l'utilisateur ? {#can-i-trigger-a-banner-based-on-user-actions}

Bien que les bannières ne prennent pas en charge la [livraison par événement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/), vous pouvez cibler les utilisateurs en fonction de leurs actions passées à l'aide de la segmentation et de la priorité.

Par exemple, pour afficher une bannière spéciale uniquement aux utilisateurs ayant effectué un événement `purchase` :
1. **Ciblage :** dans votre campagne, ciblez un segment d'utilisateurs ayant effectué l'événement personnalisé `purchase` au moins une fois.
2. **Priorité :** si vous disposez d'une bannière générale pour tous les utilisateurs et d'une bannière spécifique pour les acheteurs ciblant le même emplacement, définissez la priorité de la bannière spécifique sur **High** et celle de la bannière générale sur **Medium** ou **Low**.

Lorsque l'utilisateur démarre une nouvelle session ou actualise les bannières après avoir effectué l'action, Braze évalue son éligibilité. S'il correspond au segment « Achat », la bannière à priorité élevée sera affichée.


## Les utilisateurs peuvent-ils fermer une bannière ? {#can-users-dismiss-a-banner}

Oui. Vous pouvez permettre aux utilisateurs de fermer manuellement une bannière en activant le comportement de fermeture dans le compositeur de bannières. Consultez [Configurer le comportement de fermeture]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#dismiss-behavior) pour plus de détails sur l'activation de la fermeture et la personnalisation du bouton de fermeture.

Les utilisateurs peuvent fermer manuellement les bannières uniquement si le comportement de fermeture est activé. Si la fermeture n'est pas activée, vous pouvez contrôler la visibilité des bannières en gérant l'éligibilité des segments d'utilisateurs. Lorsqu'un utilisateur ne répond plus aux critères de ciblage d'une campagne de bannières, il ne la verra plus lors de sa prochaine session.

Lorsqu'un utilisateur ferme une bannière, il n'est plus éligible à cette campagne par défaut. Pour permettre aux utilisateurs ayant fermé la bannière de la revoir, [configurez la rééligibilité]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#re-eligibility) dans l'étape **Contrôles de l'envoi** de la campagne. Les étapes de bannière Canvas utilisent les paramètres de réentrée Canvas pour contrôler la rééligibilité.

Par exemple, si vous affichez une bannière promotionnelle jusqu'à ce qu'un utilisateur effectue un achat, l'enregistrement d'un événement tel que `purchase_completed` peut retirer cet utilisateur du segment ciblé, masquant ainsi la bannière lors des sessions suivantes.

## Puis-je exporter les analyses des campagnes de bannières à l'aide de l'API Braze ? {#can-i-export-banners-campaign-analytics-using-the-braze-api}

Oui. Vous pouvez utiliser l'[endpoint `/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) pour obtenir des données sur le nombre de campagnes de bannières consultées, cliquées ou converties.

## Quand la segmentation des utilisateurs est-elle effectuée ? {#when-are-users-segmented}

Les utilisateurs sont segmentés au début de la session. Si les segments ciblés d'une campagne dépendent d'attributs personnalisés, d'événements personnalisés ou d'autres attributs de ciblage, ceux-ci doivent être présents sur le profil de l'utilisateur au début de la session.

## Comment composer mes bannières pour garantir la latence la plus faible ? {#how-can-i-compose-banners-to-ensure-the-lowest-latency}

Plus le contenu de votre bannière est simple, plus son rendu sera rapide. Il est recommandé de tester votre campagne de bannières en fonction de la latence attendue pour votre cas d'utilisation. Par exemple, pensez à tester les attributs Liquid tels que `catalog_items`.

## Toutes les étiquettes Liquid sont-elles prises en charge ? {#are-all-liquid-tags-supported}

Non. Cependant, la plupart des étiquettes Liquid sont prises en charge pour les messages de bannières, à l'exception de `catalog_items` qui sont re-rendus à l'aide de l'[étiquette `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid).

## Puis-je capturer les événements de clic ? {#can-i-capture-click-events}

Oui. La manière dont les événements de clic sont capturés dépend de la façon dont votre bannière est rendue :

- **Composants standard de l'éditeur :** si votre bannière utilise des composants d'éditeur standard (images, boutons, texte), les clics sont automatiquement suivis lorsque vous utilisez les méthodes d'insertion du SDK.
- **Blocs de code personnalisés :** si vous souhaitez suivre les clics sur les éléments d'un bloc éditeur de code personnalisé, vous devez appeler `brazeBridge.logClick()` depuis votre HTML personnalisé pour enregistrer les clics. Cela s'applique également lorsque vous utilisez les méthodes du SDK pour insérer et afficher la bannière. Pour la référence complète, consultez [Code personnalisé et pont JavaScript pour les bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners/custom_code/#javascript-bridge).
- **Interface utilisateur personnalisée (headless) :** si vous créez une interface utilisateur entièrement personnalisée en utilisant les propriétés personnalisées de la bannière au lieu d'afficher le HTML de la bannière, appelez `logClick()` sur l'objet Banner depuis le code de votre application.

Pour plus d'informations, consultez [Enregistrement des clics]({{site.baseurl}}/developer_guide/banners/placements/#logging-clicks).