# Foire aux questions

> Voici les réponses aux questions fréquemment posées sur les bannières dans Braze. Pour des informations plus générales, consultez [À propos des bannières]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}).

## Quand les mises à jour des bannières apparaissent-elles pour les utilisateurs ?

Les bannières sont actualisées avec leurs dernières données chaque fois que vous appelez la méthode d'actualisation. Il n'est pas nécessaire de renvoyer ou de mettre à jour votre campagne de bannières.

## Combien d'emplacements puis-je demander au cours d'une session ?

Dans une seule requête d'actualisation, vous pouvez demander un maximum de 10 emplacements. Pour chacun d'entre eux, Braze renverra la bannière ayant la priorité la plus élevée à laquelle l'utilisateur est éligible. Toute demande supplémentaire renverra une erreur.

Pour plus d'informations, consultez [Demandes d'emplacement]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## Combien de campagnes de bannières peuvent être actives simultanément ?

Chaque espace de travail peut prendre en charge jusqu'à 200 campagnes de bannières actives. Si cette limite est atteinte, vous devrez [archiver ou désactiver]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) une campagne existante avant d'en créer une nouvelle.

## Pour les campagnes partageant un emplacement, quelle bannière est affichée en premier ?

Si un utilisateur est éligible à plusieurs campagnes de bannières partageant le même emplacement, la bannière ayant la priorité la plus élevée sera affichée. Pour plus d'informations, consultez [Priorité des bannières]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## Puis-je utiliser des bannières dans mon flux de Cartes de contenu existant ?

Les bannières sont différentes des Cartes de contenu, ce qui signifie que vous ne pouvez pas utiliser des bannières et des Cartes de contenu dans le même flux. Pour remplacer les flux de Cartes de contenu existants par des bannières, vous devrez [créer des emplacements dans votre application ou votre site web]({{site.baseurl}}/developer_guide/banners/placements/).

## Les bannières peuvent-elles inclure de la vidéo ?

Le compositeur de bannières standard prend en charge les images, le texte et les boutons. Pour inclure une vidéo dans une bannière, vous pouvez utiliser un bloc **Custom Code** et afficher une vidéo ou un lecteur intégré dans votre application ou votre site web.

## Puis-je déclencher une bannière en fonction des actions de l'utilisateur ?

Bien que les bannières ne prennent pas en charge la [livraison par événement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery), vous pouvez cibler les utilisateurs en fonction de leurs actions passées à l'aide de la segmentation et de la priorité.

Par exemple, pour afficher une bannière spéciale uniquement aux utilisateurs ayant effectué un événement `purchase` :
1. **Ciblage :** Dans votre campagne, ciblez un segment d'utilisateurs ayant effectué l'événement personnalisé `purchase` au moins une fois.
2. **Priorité :** Si vous disposez d'une bannière générale pour tous les utilisateurs et d'une bannière spécifique pour les acheteurs ciblant le même emplacement, définissez la priorité de la bannière spécifique sur **Élevée** et celle de la bannière générale sur **Moyenne** ou **Faible**.

Lorsque l'utilisateur démarre une nouvelle session ou actualise les bannières après avoir effectué l'action, Braze évalue son éligibilité. S'il correspond au segment « Achat », la bannière à priorité élevée sera affichée.


## Les utilisateurs peuvent-ils fermer manuellement une bannière ?

{% alert important %}
La possibilité pour les utilisateurs de fermer manuellement une bannière est en accès anticipé. Consultez [Configurer le comportement de fermeture]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#dismiss-behavior) pour plus de détails. Si vous souhaitez participer à l'accès anticipé, contactez votre gestionnaire de la satisfaction client.
{% endalert %}

Les utilisateurs peuvent fermer manuellement les bannières uniquement si le comportement de fermeture est activé et si votre espace de travail participe à l'accès anticipé. Si la fermeture n'est pas activée ou disponible pour votre espace de travail, vous pouvez contrôler la visibilité des bannières en gérant l'éligibilité des segments d'utilisateurs. Lorsqu'un utilisateur ne répond plus aux critères de ciblage d'une campagne de bannières, il ne la verra plus lors de sa prochaine session.

Par exemple, si vous affichez une bannière promotionnelle jusqu'à ce qu'un utilisateur effectue un achat, l'enregistrement d'un événement tel que `purchase_completed` peut retirer cet utilisateur du segment ciblé, masquant ainsi la bannière lors des sessions suivantes.

## Puis-je exporter les analyses des campagnes de bannières à l'aide de l'API Braze ?

Oui. Vous pouvez utiliser l'[endpoint `/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) pour obtenir des données sur le nombre de campagnes de bannières consultées, cliquées ou converties.

## Quand la segmentation des utilisateurs est-elle effectuée ?

Les utilisateurs sont segmentés au début de la session. Si les segments ciblés d'une campagne dépendent d'attributs personnalisés, d'événements personnalisés ou d'autres attributs de ciblage, ceux-ci doivent être présents sur le profil de l'utilisateur au début de la session.

## Comment composer mes bannières pour garantir la latence la plus faible ?

Plus le contenu de votre bannière est simple, plus son rendu sera rapide. Il est recommandé de tester votre campagne de bannières en fonction de la latence attendue pour votre cas d'utilisation. Par exemple, pensez à tester les attributs Liquid tels que `catalog_items`.

## Toutes les étiquettes Liquid sont-elles prises en charge ?

Non. Cependant, la plupart des étiquettes Liquid sont prises en charge pour les messages de bannières, à l'exception de `catalog_items` qui sont re-rendus à l'aide de l'[étiquette `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid).

## Puis-je capturer les événements de clic ?

Oui. La manière dont les événements de clic sont capturés dépend de la façon dont votre bannière est rendue :

- **Composants standard de l'éditeur :** Si votre bannière utilise des composants d'éditeur standard (images, boutons, texte), les clics sont automatiquement suivis lorsque vous utilisez les méthodes d'insertion du SDK.
- **Blocs de code personnalisés :** Si vous souhaitez suivre les clics sur les éléments d'un bloc éditeur de code personnalisé, vous devez appeler `brazeBridge.logClick()` depuis votre HTML personnalisé pour enregistrer les clics. Cela s'applique également lorsque vous utilisez les méthodes du SDK pour insérer et afficher la bannière. Pour la référence complète, consultez [Code personnalisé et pont JavaScript pour les bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners/custom_code/#javascript-bridge).
- **Interface utilisateur personnalisée (headless) :** Si vous créez une interface utilisateur entièrement personnalisée en utilisant les propriétés personnalisées de la bannière au lieu de rendre le HTML de la bannière, appelez `logClick()` sur l'objet Banner depuis le code de votre application.

Pour plus d'informations, consultez [Enregistrement des clics]({{site.baseurl}}/developer_guide/banners/placements/#logging-clicks).