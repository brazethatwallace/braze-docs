---
nav_title: "Canaux de notification"
article_title: Canaux de notification push
page_order: 4
page_type: reference
description: "Cet article de référence couvre les sujets relatifs aux canaux de notification push Android, tels que la transition vers Android O, l'ajout d'un canal à Braze, la configuration d'un canal de secours, et plus encore."
platform: Android
channel:
  - push

---

# Canaux de notification {#notification-channels}

> Les [canaux de notification](https://www.braze.com/blog/android-o-push-notifications-channels/) sont un moyen d'organiser les notifications push, introduits avec Android O. À partir d'Android O, toutes les notifications push doivent disposer d'un canal de notification indiquant le type de message (par exemple, « notifications de chat » ou « notifications d'abonnement »). Vos utilisateurs peuvent ensuite contrôler certains aspects de leurs notifications (par exemple, la mise en veille, les paramètres de son/vibration, ou la désinscription, etc.) en fonction de chaque canal.

## Transition vers Android O {#transitioning-to-android-o}

Les canaux de notification ne peuvent être créés que dans le code de votre application et ne peuvent pas être créés de manière programmatique dans le tableau de bord de Braze. Nous recommandons que votre équipe d'ingénierie travaille avec vos marketeurs pour s'assurer que les canaux de notification souhaités sont correctement ajoutés au tableau de bord.

À partir d'Android O, les notifications push nécessitent un canal valide pour s'afficher. Si votre application cible Android O ou une version ultérieure, vous devez utiliser la version 2.1.0 ou ultérieure du SDK Braze. Votre équipe de développement doit définir les canaux que vous souhaitez utiliser ainsi que les paramètres de notification suggérés (par exemple, importance, son, voyants lumineux) pour chaque canal dans le code de votre application. Vous pouvez consulter la documentation développeur d'Android [ici](https://developer.android.com/preview/features/notification-channels.html) et la documentation développeur de Braze [ici.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels)

{% alert note %}
Android prend en charge la localisation des noms de canaux, de sorte que dans le code de votre application, vous pouvez associer un identifiant de canal à plusieurs traductions d'un nom de canal.
{% endalert %}

Une fois ces canaux créés, vos ingénieurs devront transmettre les identifiants de canal associés à votre équipe marketing. Votre équipe devra saisir les noms et identifiants de vos canaux dans le tableau de bord de Braze pour les utiliser dans vos campagnes et Canvas.

Pour ajouter un canal au tableau de bord de Braze, accédez au composeur de notification push Android, sélectionnez le champ des canaux de notification, puis sélectionnez « gérer les canaux ».
{% alert important %}
Seuls les utilisateurs disposant d'autorisations incluant « gérer les applications » pourront gérer les canaux.
{% endalert %}

## Canal par défaut du SDK {#sdk-default-channel}

Android nécessite un canal valide pour afficher les notifications push au niveau d'API 26 (Android O) ou ultérieur. Le SDK Android de Braze version 2.1.0 inclut un canal par défaut appelé « General », qui sera créé et utilisé si vous ne spécifiez pas de canaux supplémentaires dans le tableau de bord ou si vous tentez d'envoyer vers un canal invalide. Vous pouvez renommer ce libellé dans le SDK et fournir une description du canal. Nous vous recommandons d'y réfléchir afin d'offrir une meilleure expérience utilisateur.

Une fois qu'un canal est ajouté à votre application, vous pouvez choisir de le supprimer. Cependant, les consommateurs pourront toujours voir le nombre de canaux que vous avez [supprimés][3]. Le tableau de bord de Braze ne prend pas en charge la création programmatique de canaux : les canaux doivent être créés et définis dans le code de votre application pour garantir une expérience fluide.

Encore une fois, nous vous recommandons de vous coordonner avec votre équipe d'ingénierie pour assurer une transition fluide vers le ciblage d'Android O.

## Canal de secours du tableau de bord {#dashboard-fallback-channel}

Braze vous permet de spécifier un canal de secours dans le tableau de bord. L'objectif du canal de secours du tableau de bord est de fournir un identifiant de canal pour les messages push hérités sans sélection explicite de canal. Nous définissons une sélection de canal comme le choix d'un canal dans notre composeur de notification push Android.

Les messages pour lesquels aucun canal n'a été sélectionné seront envoyés avec l'identifiant du canal de secours du tableau de bord. Lorsque vous modifiez votre canal de secours du tableau de bord, tout message pour lequel aucun canal n'a été explicitement sélectionné sera envoyé avec l'identifiant du nouveau canal de secours.

Voici un exemple du comportement attendu du canal de secours du tableau de bord :

Votre canal de secours du tableau de bord s'appelle « Marketing » et vous avez 10 messages push Android pour lesquels vous n'avez jamais sélectionné de canal. Ces campagnes sont envoyées via le canal « Marketing » car le canal « Marketing » est le canal de secours du tableau de bord.

De plus, vous avez 15 messages que vous avez choisi d'envoyer via le canal « Social Notifications » et cinq messages que vous avez choisi d'envoyer via le canal « Marketing ».

Vous décidez ensuite de changer votre canal par défaut du tableau de bord de « Marketing » à « Updates ».

Dans cette situation, les 10 campagnes sans sélection de canal qui étaient précédemment envoyées via le canal « Marketing » seront désormais envoyées via le canal « Updates » car ces messages sont envoyés via le canal de secours. Les 15 messages qui étaient envoyés via le canal « Social Notifications » continueront d'être envoyés via le canal « Social Notifications ». Les cinq messages qui étaient envoyés via le canal « Marketing » continueront d'être envoyés via le canal « Marketing ».

Dans le cas où un identifiant de canal invalide est fourni à Braze (par exemple, si vous fournissez un identifiant de canal que vos développeurs n'ont pas créé dans le SDK), nous livrerons la notification via votre canal par défaut du SDK. Par conséquent, nous vous encourageons vivement à tester vos canaux de notification via le tableau de bord de Braze pendant le développement.

Pour mieux comprendre le comportement attendu des canaux, consultez le tableau suivant :

| Scénario | Résultat |
| ---|-------------
| **Société ABC** met à jour vers un SDK prenant en charge Android O<br>**Société ABC** n'ajoute aucun canal au tableau de bord de Braze<br>**Société ABC** ne renomme pas son canal par défaut du SDK | Les notifications push envoyées aux appareils Android O créeront un canal appelé « General » et les notifications seront envoyées via le canal « General »
| **Société XYZ** met à jour vers un SDK prenant en charge Android O <br>**Société XYZ** n'ajoute aucun canal au tableau de bord de Braze<br>**Société XYZ** renomme son canal par défaut du SDK en « Marketing » | Les notifications push envoyées aux appareils Android O créeront un canal appelé « Marketing » et les notifications seront envoyées via le canal « Marketing »
| **Société LMN** met à jour vers un SDK prenant en charge Android O <br>**Société LMN** définit deux canaux dans le code de son application, « Promotions » et « Order Updates » <br>**Société LMN** ajoute les identifiants de canal pour « Promotions » et « Order Updates » au tableau de bord de Braze <br>**Société LMN** désigne « Promotions » comme canal de secours du tableau de bord<br>**Société LMN** renomme son canal par défaut du SDK en « Marketing » | Les notifications push envoyées aux appareils Android O ne créeront pas de canal<br><br>À moins que le marketeur ne spécifie explicitement que les notifications doivent être envoyées via le canal « Order Updates » ou « Marketing », toutes les notifications créées avant l'ajout des canaux au tableau de bord seront envoyées via le canal « Promotions »<br><br>Le canal par défaut du SDK, « Marketing », n'est créé et utilisé que si la société tente d'envoyer une notification via un identifiant de canal invalide ou s'il est explicitement sélectionné
| **Société HIJ** met à jour vers Android O mais ne met pas à jour le SDK Android de Braze vers la version 2.1.0 ou ultérieure | Les notifications envoyées aux utilisateurs exécutant Android O ou une version ultérieure n'apparaissent pas |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dashboard fallback channel" }

## Ajouter des canaux au tableau de bord de Braze {#adding-channels-to-the-braze-dashboard}

1. Ouvrez n'importe quelle campagne ou Canvas incluant une notification push Android et cliquez sur **Edit Campaign**.
2. Accédez au composeur de messages push Android.
3. Cliquez sur **Manage Notification Channels**. Tous les canaux ajoutés ici seront disponibles globalement pour toutes les campagnes et tous les Canvas. Vous devez disposer des [autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#limited-and-team-role-permissions) « Manage Apps » pour votre espace de travail afin de gérer les canaux.

Lorsque vous appliquez un canal de notification à une campagne ou une étape du Canvas spécifique, le nombre d'**utilisateurs pouvant être atteints** (situé dans l'étape Audience cible) pour la notification push Android ne semblera pas changer. Cependant, seuls les utilisateurs abonnés au canal de notification sélectionné verront le message, et les analyses de votre campagne (comme les clics) seront mesurées en fonction de cette audience.

![]({% image_buster /assets/img_archive/Click_Here.png %})

{:start="4"}
4. Cliquez sur **Add Notification Channel**.
5. Saisissez le nom et l'identifiant du canal de notification que vous souhaitez ajouter.<br><br>![]({% image_buster /assets/img_archive/Enter_Channel.png %})<br><br>
6. Répétez les étapes 4 et 5 pour chaque canal de notification que vous souhaitez ajouter.
7. Appuyez sur **Save** pour enregistrer vos modifications.

## Spécifier votre canal de secours {#specifying-your-fallback-channel}

Votre canal de secours est le canal via lequel Braze tentera d'envoyer votre message Android si vous n'avez pas sélectionné de canal pour le message. Les seules campagnes et Canvas qui auront des messages Android sans sélection de canal sont les campagnes et Canvas créés avant que votre équipe n'ajoute des canaux au tableau de bord de Braze. Si vous modifiez votre canal de secours, le changement sera appliqué globalement à toutes les campagnes et tous les Canvas sans sélection explicite de canal.

1. Ouvrez n'importe quelle campagne ou Canvas existant.
2. Accédez au composeur de notification push Android.
3. Sélectionnez **Manage Notification Channels** après avoir développé les options de canal de notification. <br><br>![]({% image_buster /assets/img_archive/Change_Fallback.png %}){: style="max-width:80%;"}<br><br>
4. Ajoutez le canal au tableau de bord (s'il n'a pas déjà été ajouté).
5. Sélectionnez le bouton radio à côté du canal que vous souhaitez désigner comme canal de secours.
6. Enregistrez vos modifications. Vos modifications seront appliquées globalement.

## Ajouter des canaux à vos messages push Android {#adding-channels-to-your-android-push-messages}

1. Accédez au composeur de notification push Android sur n'importe quelle campagne ou Canvas.
2. Sélectionnez le canal que vous souhaitez utiliser dans le menu déroulant. Si vous ne disposez pas d'un menu déroulant mais plutôt de la vue suivante, vous devrez ajouter des canaux avant de les sélectionner pour vos campagnes.

![]({% image_buster /assets/img_archive/No_Select.png %})

[3]: https://developer.android.com/preview/features/notification-channels.html#DeletingChannels