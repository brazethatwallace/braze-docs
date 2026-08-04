---
nav_title: Limite de débit et limite de fréquence
article_title: Limite de débit et limite de fréquence
page_order: 6
tool: Campaigns
page_type: reference
description: "Cet article de référence aborde les concepts de limite de débit et de limite de fréquence dans les campagnes, et comment vous pouvez gérer la pression marketing pour améliorer l'expérience utilisateur."

---

# Limite de débit et limite de fréquence {#rate-limiting-and-frequency-capping}

> La limite de débit et la limite de fréquence peuvent être utilisées conjointement pour vous assurer que vos utilisateurs reçoivent les messages dont ils ont besoin.

## À propos de la limitation du débit {#about-rate-limiting}

Braze vous permet de contrôler la pression marketing en limitant le débit de vos Campaigns, en régulant le volume de trafic sortant de votre plateforme. Vous pouvez mettre en œuvre deux types différents de limitation du débit pour vos Campaigns :

1. [Limitation du débit centrée sur l'utilisateur :](#user-centric-rate-limiting) se concentre sur la meilleure expérience possible pour l'utilisateur.
2. [Limitation du débit de vitesse de livraison :](#delivery-speed-rate-limiting) prend en compte la bande passante de vos serveurs.

Braze ne prend pas en charge une limitation du débit à la seconde. Braze essaie de répartir uniformément les envois de messages tout au long de la minute, mais ne peut pas le garantir. Par exemple, si vous avez une Campaign avec une limite de débit de 5 000 messages par minute, nous essayons de répartir les 5 000 requêtes uniformément sur la minute (environ 84 messages par seconde), mais il peut y avoir des variations dans le débit à la seconde.

### Limitation du débit centrée sur l'utilisateur {#user-centric-rate-limiting}

À mesure que vous créez davantage de Segments, il y aura des cas où les membres de ces Segments se chevauchent. Si vous envoyez des Campaigns à ces Segments, vous voulez vous assurer de ne pas envoyer trop souvent des messages à vos utilisateurs. Si un utilisateur reçoit trop de messages dans un court laps de temps, il se sentira submergé et désactivera les notifications push ou désinstallera votre application.

#### Filtres de Segment pertinents {#relevant-segment-filters}

Braze fournit les filtres suivants pour vous aider à limiter le débit auquel vos utilisateurs reçoivent des messages :

- Last Engaged With Message
- Last Received Any Message
- Last Received Push
- Last Received Email
- Last Received SMS

#### Mise en œuvre des filtres {#implementing-filters}

Supposons que nous ayons créé un Segment nommé « Retargeting Filter Showcase » avec un filtre « Dernière utilisation de l'application il y a plus de 7 jours » pour cibler les utilisateurs. Il s'agirait d'un Segment de réengagement standard.

Si vous avez d'autres Segments plus ciblés qui ont récemment reçu des notifications, vous ne souhaitez peut-être pas que vos utilisateurs soient ciblés par des Campaigns plus génériques dirigées vers ce Segment. En ajoutant le filtre « Last Received Push » à ce Segment, l'utilisateur s'est assuré que s'il a reçu une autre notification au cours des dernières 24 heures, il sortira de ce Segment pour les 24 heures suivantes. S'il répond toujours aux autres critères du Segment 24 heures plus tard et n'a reçu aucune autre notification, il réintégrera le Segment.

![Un Segment nommé « Retargeting Filter Showcase » avec le groupe de filtres « Dernière utilisation de l'application il y a plus de 7 jours ».]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"}

L'ajout de ce filtre à tous les Segments ciblés par des Campaigns ferait en sorte que vos utilisateurs reçoivent un maximum d'une notification push toutes les 24 heures. Vous pourriez alors prioriser vos messages en vous assurant que vos messages les plus importants sont envoyés avant les messages moins importants.

#### Définir un plafond maximum d'utilisateurs {#setting-a-maximum-user-cap}

Dans l'étape **Target Audiences** de votre compositeur de Campaign, vous pouvez également limiter le nombre total d'utilisateurs qui recevront votre message. Cela sert de vérification indépendante de vos filtres de Campaign.

![Résumé de l'audience avec une case cochée pour limiter le nombre de personnes qui reçoivent la Campaign.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"}

En sélectionnant la limite maximale d'utilisateurs, vous pouvez limiter le volume de messages envoyés par canal ou globalement pour tous les types de messages. Braze n'envoie pas de messages aux utilisateurs assignés aux groupes de contrôle, ils ne comptent donc pas dans la limite.

{% alert note %}
Le plafond maximum d'utilisateurs limite le nombre d'utilisateurs auxquels les messages sont envoyés, et non le nombre de messages effectivement délivrés. Comme les messages abandonnés comptent dans ce plafond, le nombre réel de messages envoyés peut être inférieur à la limite configurée. Par exemple, si vous définissez un plafond de 10 000 et que 2 000 messages sont abandonnés en raison de la logique Liquid ou d'autres conditions, seuls 8 000 messages sont envoyés.
{% endalert %}

##### Plafond maximum d'utilisateurs pour les Campaigns multicanal {#maximum-user-cap-for-multichannel-campaigns}

Pour les Campaigns multicanal, Braze sélectionne d'abord une audience jusqu'à votre plafond maximum d'utilisateurs configuré. Braze évalue ensuite chaque utilisateur de cette audience plafonnée pour chaque canal de la Campaign.

En conséquence, la taille de l'audience plafonnée reste la même, mais les envois par canal peuvent différer en fonction de l'éligibilité au canal. Par exemple, si vous définissez un plafond maximum d'utilisateurs de 500 000 et qu'un utilisateur n'est éligible que pour les notifications push et les Content Cards, cet utilisateur reçoit ces canaux mais pas l'e-mail.

Si vous répartissez ces canaux dans des Campaigns distinctes qui ciblent chacune le même Segment et ont chacune leur propre plafond maximum d'utilisateurs, chaque Campaign évalue et plafonne les utilisateurs indépendamment. Braze ne garantit pas que chaque Campaign sélectionne exactement le même sous-ensemble d'utilisateurs.

Si vous avez besoin de Campaigns de suivi pour cibler les utilisateurs auxquels une Campaign précédente a été envoyée, créez un Segment en utilisant le filtre **Received Campaign**, puis utilisez ce Segment pour les Campaigns de suivi.

##### Plafond maximum d'utilisateurs avec optimisations {#maximum-user-cap-with-optimizations}

Si vous utilisez une optimisation comme la variante gagnante ou la variante personnalisée, la Campaign consistera en deux envois : l'expérience initiale et l'envoi final.

Pour configurer un plafond maximum d'utilisateurs dans ce scénario, sélectionnez **Limit the number of people who will receive this campaign**, puis sélectionnez **In total this campaign should**, et entrez une limite d'audience. Votre limite d'audience sera répartie selon les pourcentages affichés dans le panneau **A/B Testing**.

Si vous sélectionnez **Every time the campaign is scheduled**, ces deux phases seront limitées séparément au nombre défini. Ce n'est généralement pas souhaitable.

#### Définir un plafond maximum d'impressions pour les Campaigns {#setting-a-maximum-impression-cap-on-campaigns}

Pour les messages in-app, vous pouvez contrôler la pression marketing en définissant un nombre maximum d'impressions qui seront affichées à votre base d'utilisateurs, après quoi Braze n'enverra plus de messages à vos utilisateurs. Cependant, il est important de noter que ce plafond n'est pas exact.

Les règles des messages in-app sont envoyées à une application au démarrage de la session, ce qui signifie que Braze peut envoyer un message à l'utilisateur avant que le plafond ne soit atteint, mais au moment où l'utilisateur déclenche le message, le plafond a été atteint. Dans cette situation, l'appareil affichera quand même le message.

Par exemple, supposons que vous ayez un jeu avec un message in-app qui se déclenche lorsqu'un utilisateur termine un niveau, et que vous le plafonniez à 100 impressions. Il y a eu 99 impressions jusqu'à présent. Alice et Bob ouvrent tous les deux le jeu, et Braze indique à leurs appareils qu'ils sont éligibles pour recevoir le message lorsqu'ils terminent un niveau. Alice termine un niveau en premier et reçoit le message. Bob termine le niveau ensuite, mais comme son appareil n'a pas communiqué avec les serveurs Braze depuis le début de sa session, son appareil ne sait pas que le message a atteint son plafond, et il reçoit également le message. Cependant, lorsqu'un plafond d'impressions a été atteint, la prochaine fois qu'un appareil demande la liste des messages in-app éligibles, le système n'envoie pas ce message et le supprime de cet appareil.

### Limitation du débit et tests A/B {#rate-limiting-and-ab-testing}

Lors de l'utilisation de la limitation du débit avec un test A/B, la limite de débit n'est pas appliquée au groupe de contrôle de la même manière qu'au groupe de test, ce qui est une source potentielle de biais temporel. Pour éviter ce biais, utilisez des fenêtres de conversion appropriées.

### Limitation du débit de vitesse de livraison {#delivery-speed-rate-limiting}

Si vous anticipez que de grandes Campaigns provoqueront un pic d'activité des utilisateurs et surchargeront vos serveurs, vous pouvez spécifier une limite de débit par minute pour l'envoi de messages, ce qui signifie que Braze n'envoie pas plus que votre paramètre de limite de débit dans une minute.

Lors du ciblage des utilisateurs pendant la création d'une Campaign, vous pouvez naviguer vers **Target Audiences** (pour les Campaigns) ou **Send Settings** (pour Canvas) pour sélectionner une limite de débit (par incréments variés allant de 10 à 500 000 messages par minute).

Notez que les Campaigns sans limitation du débit peuvent dépasser ces limites de livraison. Cependant, sachez que les messages seront abandonnés s'ils sont retardés de 72 heures ou plus en raison d'une limite de débit trop basse. Si la limite de débit est trop basse, le créateur de la Campaign recevra des alertes dans le tableau de bord et par e-mail.

{% alert tip %}
Définissez une [limite de débit de messagerie au niveau du workspace]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) pour appliquer une limite de débit à l'ensemble d'un workspace.
{% endalert %}

#### Exemple {#example}

Si vous essayez d'envoyer 75 000 messages avec une limite de débit de 10 000 par minute, la livraison sera répartie sur huit minutes. Votre Campaign n'enverra pas plus de 10 000 messages pour chacune des sept premières minutes, et 5 000 au cours de la dernière minute.

#### Nombre d'envois {#number-of-sends}

Notez que les messages soumis à une limitation du débit peuvent ne pas être envoyés uniformément au cours de chaque minute. En reprenant l'exemple d'une limite de débit de 10 000 par minute, cela signifie que Braze s'assure que pas plus de 10 000 messages ne sont envoyés par minute. Cela pourrait signifier qu'un pourcentage plus élevé des 10 000 messages est envoyé dans la première moitié de la minute par rapport à la seconde moitié.

La limite de débit est appliquée au début de la tentative d'envoi du message. Lorsqu'il y a des fluctuations dans le temps nécessaire pour compléter l'envoi, le nombre d'envois complétés peut légèrement dépasser la limite de débit pendant quelques minutes. Au fil du temps, le nombre d'envois par minute se stabilisera pour ne pas dépasser la limite de débit.

{% alert important %}
Soyez prudent lorsque vous retardez des messages urgents avec cette forme de limitation du débit par rapport au nombre total d'utilisateurs dans un Segment. Par exemple, si le Segment contient 30 millions d'utilisateurs mais que nous définissons la limite de débit à 10 000 par minute, une grande partie de votre base d'utilisateurs ne recevra pas le message avant le lendemain.
{% endalert %}

#### Campaigns multicanal et Canvas {#multichannel-campaigns-and-canvases}

Lors de la définition d'une limite de débit de vitesse de livraison pour une Campaign multicanal ou un Canvas, vous pouvez choisir de définir soit une limite de débit partagée, soit une limite par canal.

Lorsqu'une Campaign multicanal ou un Canvas utilise une limite de débit partagée, cela signifie que le nombre total de messages envoyés par minute depuis la Campaign ou le Canvas ne dépasse pas la limite de débit. Par exemple, si votre Canvas a une limite de débit de 500 000 par minute et contient des étapes de messages e-mail et SMS, Braze envoie un total de 500 000 messages par minute entre l'e-mail et le SMS.

![L'option pour limiter le débit auquel la Campaign envoie, sélectionnée avec 500 000 messages par minute.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"}

Lorsqu'une Campaign multicanal ou un Canvas utilise une limitation du débit par canal, la limite de débit s'appliquera à chacun de vos canaux sélectionnés. Par exemple, vous pouvez configurer votre Campaign ou Canvas pour envoyer un maximum de 5 000 webhooks et 2 500 messages SMS par minute à travers la Campaign ou le Canvas.

![Limites de débit distinctes pour deux canaux, webhook et SMS/MMS/RCS, avec respectivement 5 000 et 2 500 messages par minute.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Notifications push {#push-notifications}

Pour les Campaigns ou Canvas avec des plateformes push (comme Android, iOS, Web Push ou Kindle), vous pouvez sélectionner **Push notifications** pour appliquer une limite de débit partagée entre toutes les plateformes push de votre Campaign ou Canvas.

![Le menu déroulant des canaux avec les options pour les plateformes push et les notifications push.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"}

Si vous sélectionnez une limite pour les notifications push, vous ne pouvez pas définir de limites de débit individuelles par canal push. De même, si vous sélectionnez des limites pour des canaux push individuels, vous ne pouvez pas définir de limites partagées pour les notifications push.

{% alert important %}
**Mises à jour de l'interface de limitation du débit**<br>
Braze a mis à jour l'interface de limitation du débit pour offrir plus de transparence et de contrôle sur la façon dont les limites de débit s'appliquent aux Campaigns multicanal et aux Canvas.<br><br>

- **Campaigns et Canvas existants :** toutes les Campaigns et Canvas existants ont été migrés vers cette interface. Leur comportement de livraison reste le même. Le tableau de bord indique si la Campaign utilise une logique partagée ou par canal.<br>
- **Nouvelles Campaigns et nouveaux Canvas :** pour toutes les nouvelles Campaigns et tous les nouveaux Canvas, il y a un basculement manuel pour choisir votre logique de limite de débit préférée. Assurez-vous de sélectionner le comportement de limitation du débit qui correspond à votre intention lors de la définition ou de la mise à jour d'une limite de débit de Campaign ou de Canvas.
{% endalert %}

##### Considérations relatives à la limitation du débit {#rate-limiting-considerations}

Quelques points à garder à l'esprit lors de la configuration des limites de débit et le comportement auquel vous devez vous attendre :

- Les envois SMS sont soumis à une limite de débit de 50 000 par groupe d'abonnement. Certains fournisseurs SMS peuvent imposer d'autres limites.
- Les messages suivants ne seront pas limités par la limite de débit et ne seront pas comptabilisés dans celle-ci :
    - Envois de test
    - Groupes initiateurs
    - Content Cards configurées pour être créées « à la première impression » (cela sera contrôlé par le taux d'impressions de l'application. Consultez [Création de carte]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences) pour plus d'informations sur les différences entre les options de création de carte.)
- Les limites de débit de vitesse de livraison ne sont pas prises en charge pour les éléments suivants :
    - Réponses automatiques SMS
    - Messages garantis par un SLA (comme les [e-mails transactionnels]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email))
    - Messages in-app
    - Feature flags
    - Banners

#### Limitation du débit et nouvelles tentatives de contenu connecté {#rate-limiting-and-connected-content-retries}

Lorsque la [nouvelle tentative de contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries) est activée, Braze réessaiera les appels échoués tout en respectant la limite de débit que vous avez définie pour chaque renvoi. Considérons le scénario d'envoi de 75 000 messages avec une limite de débit de 10 000 par minute. Imaginez que dans la première minute, l'appel échoue ou est lent et n'envoie que 4 000 messages.

Au lieu d'essayer de rattraper le retard et d'envoyer les 6 000 messages restants dans la deuxième minute ou de les ajouter aux 10 000 déjà prévus pour l'envoi, Braze déplacera ces 6 000 messages à la « fin de la file d'attente » et ajoutera une minute, si nécessaire, au nombre total de minutes nécessaires pour envoyer votre message.

| Minute | Sans échec | 6 000 échecs à la minute 1 |
|--------|------------|---------------------------|
| 1      | 10 000     | 4 000                     |
| 2      | 10 000     | 10 000                    |
| 3      | 10 000     | 10 000                    |
| 4      | 10 000     | 10 000                    |
| 5      | 10 000     | 10 000                    |
| 6      | 10 000     | 10 000                    |
| 7      | 10 000     | 10 000                    |
| 8      | 5 000      | 10 000                    |
| 9      | 0          | 6 000                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Limitation du débit et nouvelles tentatives de contenu connecté" }

Les requêtes de contenu connecté ne sont pas limitées indépendamment et suivront la limite de débit des webhooks. Cela signifie que s'il y a un appel de contenu connecté vers un endpoint unique par webhook, vous pouvez vous attendre à 5 000 webhooks et également 5 000 appels de contenu connecté par minute. Notez que la mise en cache peut affecter cela et réduire le nombre d'appels de contenu connecté. De plus, les nouvelles tentatives peuvent augmenter les appels de contenu connecté, nous vous recommandons donc de vérifier que l'endpoint de contenu connecté peut gérer certaines fluctuations.

{% alert note %}
**Les limites de débit sont des limites de vitesse et ne définissent pas une vitesse d'envoi exacte.** En général, les messages sont répartis uniformément au cours d'une minute donnée, et dans la grande majorité des cas, ils sont envoyés au niveau ou très près de la limite configurée. Ce n'est pas toujours le cas — par exemple, lorsque les messages sont très volumineux (comme les e-mails avec de nombreux Content Blocks, des tags de contenu connecté ou des tags d'éléments de catalogue), ou lorsqu'il y a de nombreux abandons Liquid (les messages abandonnés consomment quand même un créneau et peuvent réduire les taux d'envoi effectifs).<br><br>
En pratique, le taux d'envoi soutenu (messages complétés par minute) peut être inférieur à la limite de débit configurée en raison des nouvelles tentatives, de la variabilité du réseau, de la latence des endpoints en aval et du lissage par minute. Si vous constatez régulièrement un débit nettement inférieur à celui attendu, vérifiez les temps de réponse du contenu connecté, les taux d'erreur (comme `429`) et le comportement des nouvelles tentatives.
{% endalert %}

## À propos des limites de fréquence {#about-frequency-capping}

À mesure que votre base d'utilisateurs continue de croître et que vos communications s'étendent pour inclure des Campaigns de cycle de vie, déclenchées, transactionnelles et de conversion, il est important d'éviter que vos notifications ne paraissent « spammy » ou intrusives. En offrant un meilleur contrôle sur l'expérience de vos utilisateurs, les limites de fréquence vous permettent de créer les Campaigns que vous souhaitez sans submerger votre audience.

### Utiliser la limitation du débit et les limites de fréquence ensemble {#use-rate-limiting-and-frequency-capping-together}

Lorsque vous activez à la fois la limitation du débit et les limites de fréquence sur une Campaign, Braze les applique dans l'ordre suivant :

1. **La limitation du débit** est appliquée en premier pour sélectionner le groupe initial d'utilisateurs pouvant recevoir des messages.
2. **La limite de fréquence** est appliquée ensuite pour filtrer les utilisateurs de ce groupe.
3. **Les messages sont envoyés** aux utilisateurs restants.

{% alert important %}
Si de nombreux utilisateurs de votre groupe soumis à la limitation du débit sont également soumis à la limite de fréquence, vous pourriez envoyer moins de messages que la valeur de votre limitation du débit. Braze ne remplace pas les utilisateurs supplémentaires à partir de la limitation du débit une fois que la limite de fréquence a retiré des utilisateurs du groupe d'envoi.
{% endalert %}

#### Exemple

Avec une limitation du débit de 500 utilisateurs et les limites de fréquence activées, si 200 de ces 500 utilisateurs soumis à la limitation du débit sont également soumis à la limite de fréquence, seuls 300 messages sont envoyés, et non 500.

#### Recommandations {#recommendations}

Si vous devez atteindre un nombre spécifique d'utilisateurs lorsque vous utilisez les deux fonctionnalités ensemble, envisagez les approches suivantes :

- **Augmentez votre limitation du débit :** pour tenir compte des utilisateurs soumis à la limite de fréquence. Par exemple, si vous souhaitez atteindre 500 utilisateurs mais que vous vous attendez à ce que certains soient soumis à la limite de fréquence, définissez votre limitation du débit plus élevée (par exemple, 1 000 utilisateurs).
- **Utilisez la limitation du débit seule :** si votre objectif est de contrôler le volume de messages envoyés par Campaign.
- **Contactez votre gestionnaire du succès des clients :** pour obtenir de l'aide dans la conception d'une stratégie de communication robuste qui équilibre les besoins métier et les considérations techniques.

### Aperçu de la fonctionnalité {#freq-cap-feat-over}

Les limites de fréquence sont appliquées au niveau de l'envoi d'une Campaign ou d'un composant Canvas et peuvent être configurées pour chaque espace de travail depuis **Paramètres** > **Règles de limite de fréquence**.

Par défaut, les limites de fréquence sont activées lors de la création de nouvelles Campaigns. À partir de là, vous pouvez choisir les éléments suivants :

- Le canal de communication que vous souhaitez limiter : notification push, e-mail, SMS, webhook, WhatsApp, LINE, ou l'un de ces canaux.
- Le nombre de fois que chaque utilisateur doit recevoir une Campaign ou un composant Canvas envoyé depuis un canal dans un certain laps de temps.
- Le nombre de fois que chaque utilisateur doit recevoir une Campaign ou un composant Canvas envoyé par [tag](#frequency-capping-by-tag) dans un certain laps de temps.

Ce laps de temps peut être mesuré en minutes, jours ou semaines (sept jours), avec une durée maximale de 30 jours.

Chaque ligne de limites de fréquence est connectée à l'aide de l'opérateur `AND`, et vous pouvez ajouter jusqu'à 10 règles par espace de travail. Vous pouvez inclure plusieurs limites pour les mêmes types de messages. Par exemple, vous pouvez limiter les utilisateurs à une seule notification push par jour et à trois notifications push maximum par semaine. Notez que les messages abandonnés ne sont pas comptabilisés dans les limites de fréquence.

![Section des limites de fréquence avec des listes de Campaigns et de Canvas auxquels les règles s'appliqueront ou non.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"}

#### Comportement lorsque les utilisateurs sont soumis à la limite de fréquence ou qu'un message est abandonné sur une étape Canvas {#behavior-when-users-are-frequency-capped-or-a-message-is-aborted-on-a-canvas-step}

La limite de fréquence globale seule ne fait pas sortir les utilisateurs d'un Canvas. Sur les [étapes Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step), les utilisateurs continuent d'avancer lorsqu'un message n'est pas envoyé en raison de la limite de fréquence globale, conformément à la façon dont [les utilisateurs avancent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance) dans l'étape. Il en va de même lorsqu'un message est abandonné (par exemple, par une condition d'abandon Liquid) : l'utilisateur continue à travers le Canvas comme si le message avait été envoyé.

Cela est distinct des **validations de réception** sur une étape Message. Si un utilisateur ne remplit pas vos critères de validation de réception au moment de l'envoi, il peut sortir du Canvas à cette étape.

### Règles de réception {#delivery-rules}

Il peut y avoir certaines Campaigns, comme les messages transactionnels, que vous souhaitez toujours faire parvenir à l'utilisateur, même s'il a déjà atteint sa limite de fréquence. Par exemple, une application de livraison peut souhaiter envoyer un e-mail ou une notification push lorsqu'un article est livré, quel que soit le nombre de Campaigns que l'utilisateur a reçues.

Si vous souhaitez qu'une Campaign particulière ignore les règles de limite de fréquence, vous pouvez configurer cela dans le tableau de bord de Braze lors de la planification de la réception de cette Campaign en basculant **Limite de fréquence** sur **OFF**.

Après cela, il vous sera demandé si vous souhaitez toujours que cette Campaign soit comptabilisée dans votre limite de fréquence. Les messages qui sont comptabilisés dans la limite de fréquence sont inclus dans les calculs du filtre Canal intelligent.

Lors de l'envoi de [Campaigns API]({{site.baseurl}}/developer_guide/rest_api/messaging#messaging), qui sont souvent transactionnelles, vous aurez la possibilité de spécifier qu'une Campaign doit ignorer les règles de limite de fréquence en définissant `override_frequency_capping` sur `true` dans la requête API.

Par défaut, les nouvelles Campaigns et les nouveaux Canvas qui ne respectent pas les limites de fréquence ne seront pas non plus comptabilisés dans celles-ci. Cela est configurable pour chaque Campaign et Canvas.

{% alert note %}
Ce comportement modifie le comportement par défaut lorsque vous désactivez les limites de fréquence pour une Campaign ou un Canvas. Les modifications sont rétrocompatibles et n'affectent pas les messages actuellement en cours.
{% endalert %}

![Section des contrôles de réception avec la limite de fréquence activée.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"}

#### Comment les envois sont comptabilisés dans les limites {#how-sends-count-toward-caps}

Les limites de fréquence s'appliquent par envoi : chaque fois que Braze envoie une Campaign ou un composant Canvas à un utilisateur, cela est comptabilisé dans vos limites, et non chaque variante de message ou plateforme au sein de cet envoi. Par exemple, si les utilisateurs sont limités à cinq Campaigns de notification push par semaine, ils ne reçoivent plus de Campaigns de notification push après le cinquième envoi jusqu'à la réinitialisation de la limite.

##### Envois multicanaux {#multichannel-sends}

Lorsqu'un seul envoi utilise plusieurs canaux, cet envoi est comptabilisé au maximum une fois par règle de limite de fréquence applicable. Par exemple, si vous créez une Campaign multicanal qui envoie un e-mail, une notification push iOS et une notification push Android en une seule réception, et que votre espace de travail a des règles pour les notifications push et les e-mails, ainsi qu'une règle qui s'applique à tous les canaux, cette réception est comptabilisée une fois pour la règle de notification push, une fois pour la règle d'e-mail et une fois pour la règle tous canaux — elle n'est pas comptabilisée une fois par plateforme de notification push ou par message au sein de l'envoi. Si les utilisateurs sont limités à une notification push et une Campaign d'e-mail par jour et qu'ils reçoivent cette Campaign multicanal, ils ne sont pas éligibles pour des Campaigns de notification push ou d'e-mail supplémentaires pour le reste de la journée, sauf si une Campaign ignore les règles de limite de fréquence.

Les In-App Messages et les Content Cards ne sont pas comptabilisés comme des limites ni dans les limites des Campaigns ou des composants Canvas de quelque type que ce soit.

##### Notifications push avec plusieurs appareils {#push-notifications-with-multiple-devices}

Pour les Campaigns de notification push, les limites de fréquence sont comptabilisées au niveau de la Campaign ou du composant Canvas, et non par appareil individuel. Si un profil utilisateur a plusieurs appareils enregistrés pour les notifications push (par exemple, un iPhone et un iPad), une limite de fréquence au niveau de la Campaign compte cela comme un seul envoi, quel que soit le nombre d'appareils recevant la notification. Cela est similaire à la façon dont une Campaign récurrente avec une cadence quotidienne est comptabilisée comme un seul envoi par jour, même si elle se répète plusieurs fois au cours de la semaine.

{% alert important %}
La limite de fréquence globale est planifiée en fonction du fuseau horaire de l'utilisateur et est calculée par jours calendaires, et non par périodes de 24 heures. Par exemple, si vous configurez une règle de limite de fréquence pour n'envoyer pas plus d'une Campaign par jour, un utilisateur peut recevoir un message à 23 h dans son fuseau horaire local, et il serait éligible pour recevoir un autre message une heure plus tard.
{% endalert %}

#### Cas d'usage {#use-cases}

{% tabs %}
{% tab Cas d'usage 1 %}

Supposons que vous définissiez une règle de limite de fréquence pour que vos utilisateurs ne reçoivent pas plus de trois Campaigns de notification push ou étapes Canvas par semaine de l'ensemble des Campaigns ou étapes Canvas.

Si votre utilisateur doit recevoir trois notifications push, deux In-App Messages et une Content Card cette semaine, il recevra tous ces messages.

{% endtab %}
{% tab Cas d'usage 2 %}

Ce scénario utilise une règle de limite de fréquence pour que les utilisateurs ne reçoivent pas plus de deux Campaigns de notification push ou étapes Canvas par semaine de l'ensemble des Campaigns ou étapes Canvas.

**Lorsque le scénario suivant se produit :**

- Un utilisateur déclenche la même Campaign `Campaign ABC` trois fois au cours d'une semaine.
- Cet utilisateur déclenche `Campaign ABC` une fois le lundi, une fois le mercredi et une fois le jeudi.

![Section des limites de fréquence avec la règle d'envoyer pas plus de 2 Campaigns de notification push ou étapes Canvas de l'ensemble des Campaigns ou étapes Canvas à un utilisateur chaque semaine.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Alors, le comportement attendu est le suivant :**

- Cet utilisateur recevra les envois de Campaign déclenchés le lundi et le mercredi.
- Cet utilisateur ne recevra pas le troisième envoi de Campaign le jeudi car il a déjà reçu deux envois de Campaigns de notification push cette semaine.

{% endtab %}
{% endtabs %}

### Limites de fréquence par tag {#frequency-capping-by-tag}

Les [règles de limite de fréquence](#delivery-rules) peuvent être appliquées aux espaces de travail en utilisant des tags spécifiques que vous avez appliqués à vos Campaigns et Canvas, vous permettant essentiellement de baser vos limites de fréquence sur des groupes nommés personnalisés.

Avec les limites de fréquence par tag, les règles peuvent être définies sur les tags principaux et imbriqués, de sorte que Braze prendra en compte tous les tags. Par exemple, si vous avez choisi d'utiliser le tag principal A comme limite de fréquence, nous inclurons également les informations de tous les tags imbriqués (par exemple, les tags B et C) lors de la détermination de la limite.

Vous pouvez également combiner les limites de fréquence classiques avec les limites de fréquence par tags. Considérez les règles suivantes :

1. Pas plus de trois Campaigns de notification push ou composants Canvas par semaine de l'ensemble des Campaigns et étapes Canvas. <br>**ET**
2. Pas plus de deux Campaigns de notification push ou composants Canvas par semaine avec le tag `promotional`.

![Section des limites de fréquence avec deux règles limitant le nombre de Campaigns de notification push ou Canvas pouvant être envoyés à un utilisateur chaque semaine.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

En conséquence, vos utilisateurs ne recevront pas plus de trois envois de Campaign par semaine sur l'ensemble des Campaigns et étapes Canvas, et pas plus de deux Campaigns de notification push ou composants Canvas avec le tag `promotional`.

{% alert important %}
Les Canvas sont tagués au niveau du Canvas, par opposition au tagging par composant. Ainsi, chaque composant Canvas héritera de tous les tags au niveau du Canvas.
{% endalert %}

#### Règles en conflit {#conflicting-rules}

Lorsque des règles sont en conflit, la règle de limite de fréquence la plus restrictive et applicable est appliquée à vos utilisateurs. Par exemple, supposons que vous ayez les règles suivantes :

1. Pas plus d'une Campaign de notification push ou d'un composant Canvas par semaine de l'ensemble des Campaigns et composants Canvas. <br>**ET**
2. Pas plus de trois Campaigns de notification push ou composants Canvas par semaine avec le tag `promotional`.

![Section des limites de fréquence avec des règles en conflit pour limiter le nombre de Campaigns de notification push ou étapes Canvas envoyés à un utilisateur chaque semaine.]({% image_buster /assets/img/global_rules.png %} "global rules")

Dans cet exemple, votre utilisateur ne recevra pas plus d'une Campaign de notification push ou d'un composant Canvas avec le tag « promotional » au cours d'une semaine donnée, car vous avez spécifié que les utilisateurs ne doivent pas recevoir plus d'une Campaign de notification push ou d'un composant Canvas de l'ensemble des Campaigns et composants Canvas. En d'autres termes, la règle de fréquence applicable la plus restrictive est celle qui sera appliquée à un utilisateur donné.

#### Comptage des tags {#tag-count}

Les règles de limite de fréquence par tag sont calculées au moment de l'envoi d'un message. Cela signifie que les limites de fréquence par tag ne comptent que les tags actuellement présents sur les Campaigns ou Canvas qu'un utilisateur a reçus dans le passé. Elles ne comptent pas les tags qui étaient sur les Campaigns ou Canvas au moment de leur envoi, mais qui ont depuis été supprimés. Elles comptent si un tag est ajouté ultérieurement à un message qu'un utilisateur a reçu dans le passé, mais avant que le nouveau message tagué ne soit envoyé.

##### Cas d'usage {#use-case}

Considérez les Campaigns et la règle de limite de fréquence par tag suivantes :

**Campaigns** :

- **Campaign A** est une Campaign de notification push taguée comme `promotional`. Elle est prévue pour être envoyée à 9 h le lundi.
- **Campaign B** est une Campaign de notification push taguée comme `promotional`. Elle est prévue pour être envoyée à 9 h le mercredi.

**Règle de limite de fréquence par tag :**

- Votre utilisateur ne doit pas recevoir plus d'une Campaign de notification push par semaine avec le tag `promotional`.<br><br>

| Action | Résultat |
|---|---|
| Le tag `promotional` est supprimé de **Campaign A** après que votre utilisateur a reçu le message, mais avant que **Campaign B n'ait été envoyée.** | Votre utilisateur reçoit **Campaign B**. |
| Le tag `promotional` est supprimé par erreur de **Campaign A** après que votre utilisateur a reçu le message. <br> Le tag est rajouté à **Campaign A** le mardi, avant que **Campaign B** ne soit envoyée. | Votre utilisateur ne reçoit pas **Campaign B**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'usage" }

#### Envoi à grande échelle {#sending-at-large-scales}

Les règles de limite de fréquence par tag peuvent ne pas être correctement appliquées à grande échelle, par exemple 100 messages par canal provenant de Campaigns ou de composants Canvas.

Par exemple, si votre règle de limite de fréquence par tag est :

> Pas plus de deux Campaigns d'e-mail ou composants Canvas avec le tag `Promotional` à un utilisateur chaque semaine.

Et que vous envoyez à l'utilisateur plus de 100 e-mails provenant de Campaigns et d'étapes Canvas avec les limites de fréquence activées au cours d'une semaine, plus de deux e-mails peuvent être envoyés à l'utilisateur.

Étant donné que 100 messages par canal représentent plus de messages que la plupart des marques n'en envoient à leurs utilisateurs, il est peu probable que vous soyez affecté par cette limitation. Pour éviter cette limitation, vous pouvez définir un plafond pour le nombre maximum d'e-mails que vous souhaitez que vos utilisateurs reçoivent au cours d'une semaine.

Par exemple, vous pourriez configurer la règle suivante :

> Pas plus de trois Campaigns d'e-mail ou composants Canvas par semaine de l'ensemble des Campaigns et étapes Canvas.

Cette règle garantit qu'aucun utilisateur ne reçoit plus de 100 e-mails par semaine car, au maximum, les utilisateurs reçoivent trois e-mails par semaine provenant de Campaigns ou de composants Canvas avec les limites de fréquence activées.

## Questions fréquemment posées {#frequently-asked-questions}

### Si je modifie la limitation d'envoi d'un Canvas actif, cela affecte-t-il les utilisateurs déjà dans le Canvas ? {#if-i-change-a-send-throttle-on-an-active-canvas-does-it-affect-users-already-in-the-canvas}

Oui, lorsque vous augmentez ou diminuez une limite de débit d'un Canvas, la limite mise à jour prend effet pour les nouveaux messages dans un délai d'environ 30 secondes après la modification en raison de la mise en cache.

### La limite de fréquence entraîne-t-elle la sortie des utilisateurs d'un Canvas ? {#does-frequency-capping-cause-users-to-exit-a-canvas}

Non. Si un utilisateur d'un Canvas est soumis à une limite de fréquence en raison des paramètres de limite de fréquence globale, l'utilisateur avance immédiatement à l'étape suivante du Canvas. L'utilisateur ne sort **pas** du Canvas en raison de la limite de fréquence.

### Comment puis-je identifier les utilisateurs qui ont été soumis à une limite de fréquence dans un Canvas ? {#how-can-i-identify-users-who-were-frequency-capped-in-a-canvas}

Les utilisateurs soumis à une limite de fréquence ne génèrent pas d'événement d'envoi pour cette étape. Pour identifier ces utilisateurs, vous pouvez utiliser [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) pour suivre les événements de messages limités en fréquence. Vous pouvez également créer une [Segment Extension]({{site.baseurl}}/user_guide/audience/segments/segment_extension) pour analyser les utilisateurs qui sont entrés dans le Canvas mais n'ont pas reçu le message attendu.

### Pourquoi le tableau de bord affiche-t-il une erreur de limite de débit pour ma campagne ? {#why-does-the-dashboard-show-a-rate-limit-error-for-my-campaign}

Cela signifie généralement que la [limite de débit de la vitesse de distribution](#delivery-speed-rate-limiting) de la campagne est définie trop bas pour la taille de l'audience, de sorte que l'envoi complet prendrait plus de temps que la fenêtre autorisée et Braze affiche un avertissement. Augmentez la limite de débit de la vitesse de distribution, réduisez l'audience ou utilisez **Limit send volume** pour que chaque occurrence planifiée se termine dans la fenêtre d'envoi autorisée. Vous pouvez également définir une [limite de débit de communication au niveau de l'espace de travail]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) pour appliquer un plafond à l'ensemble des campagnes.

**Limit send volume** contrôle le nombre d'utilisateurs éligibles à un envoi, et non le nombre de messages que Braze envoie par minute. Seule une limite de débit de la vitesse de distribution définit le débit par minute.

### Que signifie « Envoyé » pour la limite de fréquence ? {#what-does-sent-mean-for-frequency-capping}

Dans les analyses et la limite de fréquence, _Envoyé_ fait référence au moment où Braze expédie le message (l'envoi est enregistré), et non à la distribution finale garantie vers l'appareil ou la boîte de réception. La limite de fréquence et le décompte des envois utilisent ces événements d'envoi enregistrés, qui peuvent différer des indicateurs « distribué » en aval.

### Pourquoi est-ce que je constate des rebonds ou des reports d'e-mails ? {#why-am-i-seeing-email-bounces-or-deferrals}

Les messages de rebond et de report d'e-mails utilisent de nombreux codes différents et des textes spécifiques aux fournisseurs. Ne considérez pas un code particulier comme le signe d'un problème de limitation de débit, car la cause dépend de votre contexte d'envoi et des retours du fournisseur de messagerie.

Si les messages sont temporairement reportés, envoyer moins peut aider à court terme. Utilisez une [limite de débit de la vitesse de distribution](#delivery-speed-rate-limiting), **Limit send volume**, ou les deux.

Pour une solution à long terme, travaillez avec un expert en livrabilité pour examiner vos données de rebond et de report.