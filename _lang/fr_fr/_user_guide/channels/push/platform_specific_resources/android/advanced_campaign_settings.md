---
nav_title: "Paramètres avancés des campagnes push"
article_title: "Paramètres avancés des campagnes push"
page_order: 5
page_layout: reference
description: "Cet article de référence présente les paramètres avancés des campagnes push Android, tels que la priorité, les URI personnalisées, les options de distribution, et bien plus encore."
platform: Android
channel:
  - push
tool:
  - Campaigns

---

# Paramètres avancés des campagnes push {#advanced-push-campaign-settings}

> De nombreux paramètres avancés sont disponibles pour les notifications push Android et Fire OS envoyées via le tableau de bord de Braze. Cet article décrit ces fonctionnalités et explique comment les utiliser efficacement.

## ID de notification {#notification-id}

Un ID de notification est un identifiant unique pour une catégorie de messages de votre choix qui indique au service d'envoi de messages de ne prendre en compte que le message le plus récent portant cet ID. Définir un ID de notification vous permet d'envoyer uniquement le message le plus récent et le plus pertinent, plutôt qu'un empilement de messages obsolètes et non pertinents.

Pour attribuer un ID de notification, accédez à la page de composition du push que vous souhaitez mettre à jour, sélectionnez l'onglet **Settings**, puis saisissez un nombre entier dans la section **Notification ID**. Pour mettre à jour cette notification après l'avoir émise, envoyez une autre notification avec le même ID que celui utilisé précédemment.

![Champ Notification ID.]({% image_buster /assets/img_archive/notification_ids.png %}){: style="max-width:60%;" }

## Durée de vie (TTL) {#ttl}

Le champ **Time to en direct or en ligne/en production/instantané** vous permet de définir une durée personnalisée de stockage des messages auprès du service d'envoi de messages push. Si l'appareil reste hors ligne au-delà du TTL, le message expirera et ne sera pas distribué.

Pour modifier la durée de vie de votre notification push Android, accédez au composeur et sélectionnez l'onglet **Settings**. Trouvez le champ **Time to en direct or en ligne/en production/instantané** et saisissez une valeur en jours, heures ou secondes.

Les valeurs par défaut de la durée de vie sont définies par votre administrateur sur la page [Paramètres de notifications push]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings). Par défaut, Braze définit le TTL des notifications push à la valeur maximale pour chaque service d'envoi de messages push. Bien que les paramètres TTL par défaut s'appliquent globalement, vous pouvez les remplacer au niveau du message lors de la création d'une campagne. Cela est utile lorsque différentes campagnes nécessitent des niveaux d'urgence ou des fenêtres de distribution différents.

Par exemple, imaginons que votre application héberge un concours de quiz hebdomadaire. Vous envoyez une notification push une heure avant le début. En définissant le TTL à 1 heure, vous vous assurez que les utilisateurs qui ouvrent l'application après le début du concours ne recevront pas de notification concernant un événement déjà commencé.

{% details Bonnes pratiques %}

### Quand utiliser un TTL plus court {#when-to-use-shorter-ttl}

Des TTL plus courts garantissent que les utilisateurs reçoivent des notifications pertinentes pour des événements ou des promotions qui perdent rapidement de leur intérêt. Par exemple :

- **Commerce de détail :** Envoi d'une notification push pour une vente flash qui se termine dans 2 heures (TTL : 1 à 2 heures)
- **Livraison de repas :** Notification aux utilisateurs lorsque leur commande est à proximité (TTL : 10 à 15 minutes)
- **Applications de transport :** Partage de mises à jour sur l'arrivée d'un véhicule (TTL : quelques minutes)
- **Rappels d'événements :** Notification aux utilisateurs lorsqu'un webinaire va bientôt commencer (TTL : moins d'1 heure)

### Quand éviter un TTL plus court {#when-to-avoid-shorter-ttl}

- Si le message de votre campagne reste pertinent pendant plusieurs jours ou semaines, comme les rappels de renouvellement d'abonnement ou les promotions en cours.
- Lorsque maximiser la portée est plus important que l'urgence, comme pour les annonces de mise à jour d'application ou les promotions de fonctionnalités.

{% enddetails %}

## Priorité de distribution Firebase Messaging {#fcm-priority}

Le champ **Firebase Messaging Delivery Priority** vous permet de contrôler si une notification push est envoyée avec une priorité « normale » ou « élevée » à Firebase Cloud Messaging. Ce paramètre détermine la rapidité de distribution des messages et leur impact sur l'autonomie de la batterie de l'appareil.

| Priorité | Description | Idéal pour |
|---------|-------------|----------|
| Normale | Distribution optimisée pour la batterie, pouvant être retardée pour économiser l'énergie | Contenu non urgent, offres promotionnelles, mises à jour d'actualités |
| Élevée | Distribution immédiate avec une consommation de batterie plus importante | Notifications urgentes, alertes critiques, mises à jour d'événements en direct or en ligne/en production/instantané, alertes de compte, actualités de dernière minute ou rappels urgents |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Priorité de distribution Firebase Messaging" }

### Considérations {#considerations}

- **Paramètre par défaut** : vous pouvez définir une priorité FCM par défaut pour toutes les campagnes Android dans vos [Paramètres de notifications push]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings). Ce paramètre au niveau de la campagne remplacera la valeur par défaut si nécessaire.
- **Dépriorisation** : si FCM détecte que votre application envoie fréquemment des messages à haute priorité qui ne génèrent pas de notifications visibles par l'utilisateur ou d'engagement, ces messages peuvent être automatiquement dépriorisés en priorité normale.
- **Impact sur la batterie** : les messages à haute priorité réveillent les appareils en veille de manière plus agressive et consomment davantage de batterie. Utilisez cette priorité avec discernement.

Pour des informations plus détaillées sur le traitement des messages et la dépriorisation, consultez la [documentation FCM](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) et [Traitement des messages et dépriorisation sur Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority#deprioritize).

## Texte récapitulatif {#summary-text}

Le texte récapitulatif vous permet de définir du texte supplémentaire dans la vue étendue de la notification. Il sert également de légende pour les notifications contenant des images.

![Un message Android avec le titre « Ceci est le titre de la notification. » et le texte récapitulatif « Ceci est le texte récapitulatif de la notification. »]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

Le texte récapitulatif s'affiche sous le corps du message dans la vue étendue.

![Un message Android avec le titre « Ceci est le titre de la notification. » et le texte récapitulatif « Ceci est le texte récapitulatif de la notification. »]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Pour les notifications push contenant des images, le texte du message s'affiche dans la vue réduite, tandis que le texte récapitulatif s'affiche comme légende de l'image lorsque la notification est étendue.

## URI personnalisées {#custom-uris}

La fonctionnalité **Custom URI** vous permet de spécifier une URL Web ou une ressource Android vers laquelle naviguer lorsque la notification est cliquée. Si aucune URI personnalisée n'est spécifiée, cliquer sur la notification amène les utilisateurs dans votre application. Vous pouvez utiliser l'URI personnalisée pour créer des liens profonds à l'intérieur de votre application ainsi que pour diriger les utilisateurs vers des ressources extérieures à votre application. Cela peut être spécifié via notre [API d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging) ou dans l'onglet **Compose** du composeur push.

![Champ Custom URI.]({% image_buster /assets/img_archive/deep_link.png %}){: style="max-width:60%;"}

## Priorité d'affichage des notifications {#notification-display-priority}

{% multi_lang_include alerts/important_alerts.md alert='Android notification priority' %}

Le niveau de priorité d'une notification push affecte la façon dont votre notification est affichée dans le tiroir de notifications par rapport aux autres notifications. Il peut également affecter la vitesse et le mode de distribution, car les messages de priorité normale et inférieure peuvent être envoyés avec une latence légèrement plus élevée ou regroupés pour préserver l'autonomie de la batterie, tandis que les messages de haute priorité sont toujours envoyés immédiatement.

Cette fonctionnalité est utile pour différencier vos messages en fonction de leur caractère critique ou urgent. Par exemple, une notification concernant des conditions routières dangereuses serait un bon candidat pour recevoir une priorité élevée, tandis qu'une notification concernant une vente en cours devrait recevoir une priorité plus basse. Vous devriez vous demander si l'utilisation d'une priorité intrusive est réellement nécessaire pour la notification que vous envoyez, car occuper constamment la première place dans la boîte de réception de vos utilisateurs ou interrompre leurs autres activités peut avoir un impact négatif.

Sous Android O, la priorité des notifications est devenue une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir la priorité d'un canal lors de sa configuration, puis utiliser le tableau de bord pour sélectionner le canal approprié lors de l'envoi de vos notifications. Pour les appareils exécutant des versions d'Android antérieures à O, il est possible de spécifier un niveau de priorité pour les notifications Android et Fire OS via le tableau de bord de Braze et l'API d'envoi de messages.

Pour envoyer un message à l'ensemble de votre base d'utilisateurs avec une priorité spécifique, nous recommandons de spécifier indirectement la priorité via la [configuration des canaux de notification](https://developer.android.com/training/notify-user/channels#importance) (pour cibler les appareils O+) et d'envoyer la priorité individuelle depuis le tableau de bord (pour cibler les appareils &#60;O).

Consultez le tableau suivant pour les niveaux de priorité que vous pouvez définir sur les notifications push Android ou Fire OS :

| Priorité | Description | Valeur `priority` (pour les messages API) |
|------|-----------|----------------------------|
| Max | Messages urgents ou critiques en termes de temps. | `2` |
| Élevée | Communication importante, comme un nouveau message d'un ami. | `1` |
| Par défaut | La plupart des notifications. À utiliser si votre message ne relève explicitement d'aucun des autres types de priorité. | `0` |
| Basse | Information que vous souhaitez porter à la connaissance des utilisateurs mais qui ne nécessite pas d'action immédiate. | `-1`|
| Min | Information contextuelle ou de fond. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Priorité d'affichage des notifications" }

Pour plus d'informations, consultez la documentation de Google sur les [notifications Android](http://developer.android.com/design/patterns/notifications.html).

## Catégorie push {#push-category}

Les notifications push Android offrent la possibilité de spécifier si votre notification appartient à une catégorie prédéfinie. L'interface système Android peut utiliser cette catégorie pour prendre des décisions de classement ou de filtrage concernant l'emplacement de la notification dans le tiroir de notifications de l'utilisateur.

![Onglet Paramètres avec la catégorie définie sur None, qui est le paramètre par défaut.]({% image_buster /assets/img_archive/braze_category.png %}){: style="max-width:60%;"}

| Catégorie | Description |
|---|-------|
| None | Option par défaut. |
| Alarm | Alarme ou minuteur. |
| Call | Appel entrant (vocal ou vidéo) ou demande de communication synchrone similaire. |
| Email | Message en masse asynchrone (e-mail). |
| Error | Erreur dans une opération en arrière-plan ou un état d'authentification. |
| Event | Événement de calendrier. |
| Message | Message direct entrant (SMS, message instantané, etc.). |
| Progress | Progression d'une opération en arrière-plan de longue durée. |
| Promotion | Promotion ou publicité. |
| Recommendation | Recommandation spécifique et opportune pour un élément unique. |
| Reminder | Rappel planifié par l'utilisateur. |
| Service | Indication d'un service en arrière-plan en cours d'exécution. |
| Social | Mise à jour de réseau social ou de partage. |
| Status | Information continue sur l'appareil ou l'état contextuel. |
| System | Mise à jour du système ou de l'état de l'appareil. Réservé à l'utilisation système. |
| Transport | Contrôle de transport multimédia pour la lecture. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Catégorie push" }

## Visibilité push {#push-visibility}

Les notifications push Android fournissent un champ facultatif pour déterminer comment une notification apparaît sur l'écran de verrouillage de l'utilisateur. Consultez le tableau suivant pour les options de visibilité et leurs descriptions.

| Visibilité | Description |
|---|-----|
| Public | La notification apparaît sur l'écran de verrouillage |
| Private | La notification s'affiche avec « Contenu masqué » comme message |
| Secret | La notification n'apparaît pas sur l'écran de verrouillage |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Visibilité push" }

De plus, les utilisateurs Android peuvent remplacer la façon dont les notifications push apparaissent sur leur écran de verrouillage en modifiant le paramètre de confidentialité des notifications sur leur appareil. Ce paramètre remplacera la visibilité définie dans la notification push.

![Emplacement de la priorité push dans le tableau de bord avec Set Visibility activé et défini sur Private.]({% image_buster /assets/img_archive/braze_visibility.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Quelle que soit la visibilité, toutes les notifications seront affichées sur l'écran de verrouillage de l'utilisateur si le paramètre de confidentialité des notifications de son appareil est défini sur **Show all content** (paramètre par défaut). De même, les notifications ne seront pas affichées sur l'écran de verrouillage si la confidentialité des notifications est définie sur **Do not show notifications**. La visibilité n'a d'effet que si la confidentialité des notifications est définie sur **Hide sensitive content**.

La visibilité n'a aucun effet sur les appareils antérieurs à Android Lollipop 5.0.0, ce qui signifie que toutes les notifications seront affichées sur ces appareils.

Consultez notre [documentation Android](https://developer.android.com/guide/topics/ui/notifiers/notifications) pour plus d'informations.

## Sons de notification {#notification-sounds}

Sous Android O, les sons de notification sont devenus une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir le son d'un canal lors de sa configuration, puis utiliser le tableau de bord pour sélectionner le canal approprié lors de l'envoi de vos notifications.

Pour les appareils exécutant des versions d'Android antérieures à Android O, Braze vous permet de définir le son d'un message push individuel via le composeur du tableau de bord. Vous pouvez le faire en spécifiant une ressource sonore locale sur l'appareil (par exemple, `android.resource://com.mycompany.myapp/raw/mysound`).

Sélectionner **Default** dans ce champ jouera le son de notification par défaut de l'appareil. Cela peut être spécifié via notre [API d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging) ou dans les **Settings** du composeur push.

![Le champ « Sound ».]({% image_buster /assets/img_archive/sound_android.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Ensuite, saisissez l'URI complète de la ressource sonore (par exemple, `android.resource://com.mycompany.myapp/raw/mysound`) dans le champ du tableau de bord.

Pour envoyer un message à l'ensemble de votre base d'utilisateurs avec un son spécifique, nous recommandons de spécifier indirectement le son via la [configuration des canaux de notification](https://developer.android.com/training/notify-user/channels) (pour cibler les appareils O+) et d'envoyer le son individuel depuis le tableau de bord (pour cibler les appareils &#60;O).