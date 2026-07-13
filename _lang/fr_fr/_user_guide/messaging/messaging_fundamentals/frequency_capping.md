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

## À propos de la limite de débit {#about-rate-limiting}

Braze vous permet de contrôler la pression marketing en limitant le débit de vos campagnes, régulant ainsi le volume de trafic sortant de votre plateforme. Vous pouvez mettre en œuvre deux types différents de limite de débit pour vos campagnes :

1. [Limite de débit centrée sur l'utilisateur :](#user-centric-rate-limiting) se concentre sur la meilleure expérience possible pour l'utilisateur.
2. [Limite de débit de vitesse d'envoi :](#delivery-speed-rate-limiting) prend en compte la bande passante de vos serveurs.

Braze ne prend pas en charge une limite de débit par seconde. Braze essaie de répartir uniformément les envois de messages tout au long de la minute, mais ne peut pas le garantir. Par exemple, si vous avez une campagne avec une limite de débit de 5 000 messages par minute, nous essayons de répartir les 5 000 requêtes uniformément sur la minute (environ 84 messages par seconde), mais il peut y avoir des variations dans le débit par seconde.

### Limite de débit centrée sur l'utilisateur {#user-centric-rate-limiting}

Au fur et à mesure que vous créez des segments, il y aura des cas où l'appartenance à ces segments se chevauche. Si vous envoyez des campagnes à ces segments, vous voulez vous assurer de ne pas envoyer trop souvent des messages à vos utilisateurs. Si un utilisateur reçoit trop de messages dans un court laps de temps, il se sentira submergé et désactivera les notifications push ou désinstallera votre application.

#### Filtres de segment pertinents {#relevant-segment-filters}

Braze fournit les filtres suivants pour vous aider à limiter le débit auquel vos utilisateurs reçoivent des messages :

- Dernière interaction avec un message
- Dernier message reçu
- Dernière notification push reçue
- Dernier e-mail reçu
- Dernier SMS reçu

#### Mise en œuvre des filtres {#implementing-filters}

Imaginons que nous ayons créé un segment nommé « Vitrine de filtres de reciblage » avec un filtre « Dernière utilisation de l'application il y a plus de 7 jours » pour cibler les utilisateurs. Il s'agirait d'un segment de réengagement standard.

Si vous avez d'autres segments plus ciblés qui ont reçu des notifications récemment, vous ne souhaitez peut-être pas que vos utilisateurs soient ciblés par des campagnes plus génériques destinées à ce segment. En ajoutant le filtre « Dernière notification push reçue » à ce segment, l'utilisateur s'est assuré que s'il a reçu une autre notification au cours des dernières 24 heures, il sortira de ce segment pour les 24 heures suivantes. S'il répond toujours aux autres critères du segment 24 heures plus tard et n'a reçu aucune autre notification, il réintégrera le segment.

![Un segment nommé « Vitrine de filtres de reciblage » avec le groupe de filtres « Dernière utilisation de l'application il y a plus de 7 jours ».]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"}

L'ajout de ce filtre à tous les segments ciblés par des campagnes ferait en sorte que vos utilisateurs reçoivent un maximum d'une notification push toutes les 24 heures. Vous pourriez alors prioriser vos messages en vous assurant que vos messages les plus importants sont envoyés avant les messages moins importants.

#### Définir un plafond maximum d'utilisateurs {#setting-a-maximum-user-cap}

À l'étape **Audience cible** du compositeur de votre campagne, vous pouvez également limiter le nombre total d'utilisateurs qui recevront votre message. Cela sert de vérification indépendante de vos filtres de campagne.

![Résumé de l'audience avec une case cochée pour limiter le nombre de personnes qui reçoivent la campagne.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"}

En sélectionnant la limite maximale d'utilisateurs, vous pouvez limiter le volume de messages envoyés par canal ou globalement pour tous les types de messages. Braze n'envoie pas de messages aux utilisateurs affectés aux groupes de contrôle, ils ne comptent donc pas dans la limite.

{% alert note %}
Le plafond maximum d'utilisateurs limite le nombre d'utilisateurs ciblés, pas le nombre de messages envoyés avec succès. Comme les messages abandonnés comptent dans ce plafond, le nombre réel de messages envoyés peut être inférieur à la limite configurée. Par exemple, si vous définissez un plafond de 10 000 et que 2 000 messages sont abandonnés en raison de la logique Liquid ou d'autres conditions, seuls 8 000 messages sont envoyés.
{% endalert %}

##### Plafond maximum d'utilisateurs avec optimisations {#maximum-user-cap-with-optimizations}

Si vous utilisez une optimisation comme la variante gagnante ou la variante personnalisée, la campagne sera composée de deux envois : l'expérience initiale et l'envoi final.

Pour configurer un plafond maximum d'utilisateurs dans ce scénario, sélectionnez **Limiter le nombre de personnes qui recevront cette campagne**, puis sélectionnez **Au total, cette campagne doit**, et saisissez une limite d'audience. Votre limite d'audience sera répartie selon les pourcentages affichés dans le panneau **A/B Testing**.

Si vous sélectionnez **À chaque planification de la campagne**, ces deux phases seront limitées séparément au nombre défini. Ce n'est généralement pas souhaitable.

#### Définir un plafond maximum d'impressions sur les campagnes {#setting-a-maximum-impression-cap-on-campaigns}

Pour les messages in-app, vous pouvez contrôler la pression marketing en définissant un nombre maximum d'impressions qui seront affichées à votre base d'utilisateurs, après quoi Braze n'enverra plus de messages à vos utilisateurs. Cependant, il est important de noter que ce plafond n'est pas exact.

Les règles de messages in-app sont envoyées à une application au démarrage de la session, ce qui signifie que Braze peut envoyer un message à l'utilisateur avant que le plafond ne soit atteint, mais au moment où l'utilisateur déclenche le message, le plafond a été atteint. Dans cette situation, l'appareil affichera quand même le message.

Par exemple, imaginons que vous ayez un jeu avec un message in-app qui se déclenche lorsqu'un utilisateur termine un niveau, et que vous le plafonniez à 100 impressions. Il y a eu 99 impressions jusqu'à présent. Alice et Bob ouvrent tous les deux le jeu, et Braze indique à leurs appareils qu'ils sont éligibles pour recevoir le message lorsqu'ils terminent un niveau. Alice termine un niveau en premier et reçoit le message. Bob termine le niveau ensuite, mais comme son appareil n'a pas communiqué avec les serveurs Braze depuis le début de sa session, son appareil ne sait pas que le message a atteint son plafond, et il reçoit également le message. Cependant, lorsqu'un plafond d'impressions a été atteint, la prochaine fois qu'un appareil demande la liste des messages in-app éligibles, le système n'envoie pas ce message et le supprime de cet appareil.

### Limite de débit et tests A/B {#rate-limiting-and-ab-testing}

Lors de l'utilisation de la limite de débit avec un test A/B, la limite de débit n'est pas appliquée au groupe de contrôle de la même manière qu'au groupe de test, ce qui est une source potentielle de biais temporel. Pour éviter ce biais, utilisez des fenêtres de conversion appropriées.

### Limite de débit de vitesse d'envoi {#delivery-speed-rate-limiting}

Si vous anticipez que de grandes campagnes provoqueront un pic d'activité utilisateur et surchargeront vos serveurs, vous pouvez spécifier une limite de débit par minute pour l'envoi de messages, ce qui signifie que Braze n'envoie pas plus que votre paramètre de limite de débit dans une minute.

Lors du ciblage des utilisateurs pendant la création de la campagne, vous pouvez naviguer vers **Audience cible** (pour les campagnes) ou **Paramètres d'envoi** (pour Canvas) pour sélectionner une limite de débit (par incréments variés allant de 10 à 500 000 messages par minute).

Notez que les campagnes sans limite de débit peuvent dépasser ces limites d'envoi. Cependant, sachez que les messages seront abandonnés s'ils sont retardés de 72 heures ou plus en raison d'une limite de débit trop basse. Si la limite de débit est trop basse, le créateur de la campagne recevra des alertes dans le tableau de bord et par e-mail.

{% alert tip %}
Définissez une [limite de débit de messagerie de l'espace de travail]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) pour appliquer une limite de débit à l'ensemble d'un espace de travail.
{% endalert %}

#### Exemple {#example}

Si vous essayez d'envoyer 75 000 messages avec une limite de débit de 10 000 par minute, l'envoi sera réparti sur huit minutes. Votre campagne n'enverra pas plus de 10 000 messages pour chacune des sept premières minutes, et 5 000 au cours de la dernière minute.

#### Nombre d'envois {#number-of-sends}

Notez que les messages avec limite de débit peuvent ne pas être envoyés uniformément au cours de chaque minute. En reprenant l'exemple d'une limite de débit de 10 000 par minute, cela signifie que Braze s'assure que pas plus de 10 000 messages ne sont envoyés par minute. Cela pourrait signifier qu'un pourcentage plus élevé des 10 000 messages est envoyé dans la première moitié de la minute par rapport à la seconde moitié.

La limite de débit est appliquée au début de la tentative d'envoi du message. Lorsqu'il y a des fluctuations dans le temps nécessaire pour terminer l'envoi, le nombre d'envois terminés peut légèrement dépasser la limite de débit pendant quelques minutes. Au fil du temps, le nombre d'envois par minute se stabilisera pour ne pas dépasser la limite de débit.

{% alert important %}
Soyez prudent lorsque vous retardez des messages urgents avec cette forme de limite de débit par rapport au nombre total d'utilisateurs dans un segment. Par exemple, si le segment contient 30 millions d'utilisateurs mais que nous fixons la limite de débit à 10 000 par minute, une grande partie de votre base d'utilisateurs ne recevra pas le message avant le lendemain.
{% endalert %}

#### Campagnes multicanal et Canvas {#multichannel-campaigns-and-canvases}

Lors de la définition d'une limite de débit de vitesse d'envoi pour une campagne multicanal ou un Canvas, vous pouvez choisir de définir soit une limite de débit partagée, soit une limite par canal.

Lorsqu'une campagne multicanal ou un Canvas utilise une limite de débit partagée, cela signifie que le nombre total de messages envoyés par minute depuis la campagne ou le Canvas ne dépasse pas la limite de débit. Par exemple, si votre Canvas a une limite de débit de 500 000 par minute et contient des étapes de messages e-mail et SMS, Braze envoie un total de 500 000 messages par minute entre les e-mails et les SMS.

![L'option pour limiter le débit auquel la campagne envoie, sélectionnée avec 500 000 messages par minute.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"}

Lorsqu'une campagne multicanal ou un Canvas utilise une limite de débit par canal, la limite de débit s'appliquera à chacun de vos canaux sélectionnés. Par exemple, vous pouvez configurer votre campagne ou Canvas pour envoyer un maximum de 5 000 webhooks et 2 500 messages SMS par minute à travers la campagne ou le Canvas.

![Limites de débit séparées pour deux canaux, webhook et SMS/MMS/RCS, avec respectivement 5 000 et 2 500 messages par minute.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Notifications push {#push-notifications}

Pour les campagnes ou Canvas avec des plateformes push (comme Android, iOS, notification push Web ou Kindle), vous pouvez sélectionner **Notifications push** pour appliquer une limite de débit partagée entre toutes les plateformes push de votre campagne ou Canvas.

![Le menu déroulant des canaux avec les options pour les plateformes push et les notifications push.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"}

Si vous sélectionnez une limite pour les notifications push, vous ne pouvez pas définir de limites de débit individuelles par canal push. De même, si vous sélectionnez des limites pour des canaux push individuels, vous ne pouvez pas définir de limites partagées pour les notifications push.

{% alert important %}
**Mises à jour de l'interface de limite de débit**<br>
Braze a mis à jour l'interface de limite de débit pour offrir plus de transparence et de contrôle sur la façon dont les limites de débit s'appliquent aux campagnes multicanal et aux Canvas.<br><br>

- **Campagnes et Canvas existants :** toutes les campagnes et tous les Canvas existants ont été migrés vers cette interface. Leur comportement d'envoi reste le même. Le tableau de bord indique si la campagne utilise une logique partagée ou par canal.<br>
- **Nouvelles campagnes et nouveaux Canvas :** pour toutes les nouvelles campagnes et tous les nouveaux Canvas, il y a un bouton bascule manuel pour choisir votre logique de limite de débit préférée. Assurez-vous de sélectionner le comportement de limite de débit qui correspond à votre intention lors de la configuration ou de la mise à jour d'une limite de débit de campagne ou de Canvas.
{% endalert %}

##### Considérations relatives à la limite de débit {#rate-limiting-considerations}

Quelques points à garder à l'esprit lors de la configuration des limites de débit et le comportement auquel vous devez vous attendre :

- Les envois SMS sont soumis à une limite de débit de 50 000 par groupe d'abonnement. Certains fournisseurs SMS peuvent imposer d'autres limites.
- Les messages suivants ne seront pas limités par la limite de débit et ne seront pas comptabilisés dans celle-ci :
    - Envois de test
    - Groupes initiateurs
    - Content Cards configurées pour être créées « à la première impression » (cela sera contrôlé par le taux d'impressions de l'application. Consultez [Création de carte]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences) pour plus d'informations sur les différences entre les options de création de carte.)
- Les limites de débit de vitesse d'envoi ne sont pas prises en charge pour les éléments suivants :
    - Réponses automatiques SMS
    - Messages avec SLA garanti (comme les [e-mails transactionnels]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email))
    - Messages in-app
    - Feature flags
    - Bannières

#### Limite de débit et nouvelles tentatives de contenu connecté {#rate-limiting-and-connected-content-retries}

Lorsque la [nouvelle tentative de contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries) est activée, Braze réessaiera les appels échoués tout en respectant la limite de débit que vous avez définie pour chaque renvoi. Considérons le scénario d'envoi de 75 000 messages avec une limite de débit de 10 000 par minute. Imaginons que dans la première minute, l'appel échoue ou est lent et n'envoie que 4 000 messages.

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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Limite de débit et nouvelles tentatives de contenu connecté" }

Les requêtes de contenu connecté ne sont pas limitées indépendamment et suivront la limite de débit des webhooks. Cela signifie que s'il y a un appel de contenu connecté vers un endpoint unique par webhook, vous pouvez vous attendre à 5 000 webhooks et également 5 000 appels de contenu connecté par minute. Notez que la mise en cache peut affecter cela et réduire le nombre d'appels de contenu connecté. De plus, les nouvelles tentatives peuvent augmenter les appels de contenu connecté, nous vous recommandons donc de vérifier que l'endpoint de contenu connecté peut gérer certaines fluctuations.

{% alert note %}
**Les limites de débit sont des limites de vitesse et ne définissent pas une vitesse d'envoi exacte.** Généralement, les messages sont répartis uniformément au cours d'une minute donnée, et dans la grande majorité des cas, ils sont envoyés au niveau ou très proche de la limite configurée. Ce n'est pas toujours le cas, par exemple lorsque les messages sont très volumineux (comme les e-mails avec de nombreux Content Blocks, des balises de contenu connecté ou des balises d'éléments de catalogue), ou lorsqu'il y a de nombreux abandons Liquid (les messages abandonnés consomment quand même un créneau et peuvent réduire les taux d'envoi effectifs).<br><br>
En pratique, le taux d'envoi soutenu (messages terminés par minute) peut être inférieur à la limite de débit configurée en raison des nouvelles tentatives, de la variabilité du réseau, de la latence des endpoints en aval et du lissage par minute. Si vous constatez régulièrement un débit significativement inférieur à celui attendu, vérifiez les temps de réponse du contenu connecté, les taux d'erreur (comme `429`) et le comportement des nouvelles tentatives.
{% endalert %}

## À propos de la limite de fréquence {#about-frequency-capping}

Au fur et à mesure que votre base d'utilisateurs continue de croître et que vos messages s'étendent pour inclure des campagnes de cycle de vie, déclenchées, transactionnelles et de conversion, il est important d'empêcher vos notifications de paraître « spammy » ou intrusives. En offrant un meilleur contrôle sur l'expérience de vos utilisateurs, la limite de fréquence vous permet de créer les campagnes que vous souhaitez sans submerger votre audience.

### Utiliser la limite de débit et la limite de fréquence ensemble {#use-rate-limiting-and-frequency-capping-together}

Lorsque vous activez à la fois la limite de débit et la limite de fréquence sur une campagne, Braze les applique dans l'ordre suivant :

1. **La limite de débit** est appliquée en premier pour sélectionner le groupe initial d'utilisateurs pouvant recevoir des messages.
2. **La limite de fréquence** est appliquée ensuite pour filtrer les utilisateurs de ce groupe.
3. **Les messages sont envoyés** aux utilisateurs restants.

{% alert important %}
Si de nombreux utilisateurs dans votre groupe limité en débit sont plafonnés en fréquence, vous pouvez envoyer moins de messages que la valeur de votre limite de débit. Braze ne complète pas avec des utilisateurs supplémentaires à partir de la limite de débit une fois que la limite de fréquence a retiré des utilisateurs du groupe d'envoi.
{% endalert %}

#### Exemple

Avec une limite de débit de 500 utilisateurs et la limite de fréquence activée, si 200 de ces 500 utilisateurs limités en débit sont plafonnés en fréquence, seuls 300 messages sont envoyés — pas 500.

#### Recommandations {#recommendations}

Si vous devez atteindre un nombre spécifique d'utilisateurs lorsque vous utilisez les deux fonctionnalités ensemble, envisagez les approches suivantes :

- **Augmentez votre limite de débit :** pour tenir compte des utilisateurs qui sont plafonnés en fréquence. Par exemple, si vous souhaitez atteindre 500 utilisateurs mais que vous vous attendez à ce que certains soient plafonnés en fréquence, définissez votre limite de débit plus haut (par exemple, 1 000 utilisateurs).
- **Utilisez la limite de débit seule :** si votre objectif est de contrôler le volume de messages envoyés par campagne.
- **Contactez votre gestionnaire de la satisfaction client :** pour obtenir de l'aide dans la conception d'une stratégie de communication robuste qui équilibre les besoins métier et les considérations techniques.

### Aperçu de la fonctionnalité {#freq-cap-feat-over}

La limite de fréquence est appliquée au niveau de l'envoi de la campagne ou du composant Canvas et peut être configurée pour chaque espace de travail depuis **Paramètres** > **Règles de limite de fréquence**.

Par défaut, la limite de fréquence est activée lors de la création de nouvelles campagnes. À partir de là, vous pouvez choisir les éléments suivants :

- Le canal de communication que vous souhaitez plafonner : push, e-mail, SMS, webhook, WhatsApp, LINE, ou l'un de ces canaux.
- Combien de fois chaque utilisateur doit recevoir une campagne ou un composant Canvas envoyé depuis un canal dans un certain laps de temps.
- Combien de fois chaque utilisateur doit recevoir une campagne ou un composant Canvas envoyé par [étiquette](#frequency-capping-by-tag) dans un certain laps de temps.

Ce laps de temps peut être mesuré en minutes, jours ou semaines (sept jours), avec une durée maximale de 30 jours.

Chaque ligne de limites de fréquence est connectée à l'aide de l'opérateur `AND`, et vous pouvez ajouter jusqu'à 10 règles par espace de travail. Vous pouvez inclure plusieurs plafonds pour les mêmes types de messages. Par exemple, vous pouvez plafonner les utilisateurs à pas plus d'une notification push par jour et pas plus de trois notifications push par semaine. Notez que les messages abandonnés ne comptent pas dans la limite de fréquence.

![Section de limite de fréquence avec des listes de campagnes et de Canvas auxquels les règles s'appliqueront et ne s'appliqueront pas.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"}

#### Comportement lorsque les utilisateurs sont plafonnés en fréquence ou qu'un message est abandonné sur une étape Canvas {#behavior-when-users-are-frequency-capped-or-a-message-is-aborted-on-a-canvas-step}

La limite de fréquence globale seule ne fait pas sortir les utilisateurs d'un Canvas. Sur les [étapes de message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step), les utilisateurs continuent d'avancer lorsqu'un message n'est pas envoyé en raison de la limite de fréquence globale, conformément à la [façon dont les utilisateurs avancent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance) dans l'étape. Il en va de même lorsqu'un message est abandonné (par exemple, par une condition d'abandon Liquid) : l'utilisateur continue à travers le Canvas comme si le message avait été envoyé.

Cela est distinct des **validations d'envoi** sur une étape de message. Si un utilisateur ne remplit pas vos critères de validation d'envoi au moment de l'envoi, il peut sortir du Canvas à cette étape.

### Règles d'envoi {#delivery-rules}

Il peut y avoir certaines campagnes, comme les messages transactionnels, que vous souhaitez toujours faire parvenir à l'utilisateur, même s'il a déjà atteint sa limite de fréquence. Par exemple, une application de livraison peut souhaiter envoyer un e-mail ou une notification push lorsqu'un article est livré, quel que soit le nombre de campagnes que l'utilisateur a reçues.

Si vous souhaitez qu'une campagne particulière ignore les règles de limite de fréquence, vous pouvez configurer cela dans le tableau de bord de Braze lors de la planification de l'envoi de cette campagne en basculant **Limite de fréquence** sur **OFF**.

Après cela, il vous sera demandé si vous souhaitez toujours que cette campagne soit comptabilisée dans votre limite de fréquence. Les messages qui comptent dans la limite de fréquence sont inclus dans les calculs du filtre de canal intelligent.

Lors de l'envoi de [campagnes API]({{site.baseurl}}/developer_guide/rest_api/messaging#messaging), qui sont souvent transactionnelles, vous aurez la possibilité de spécifier qu'une campagne doit ignorer les règles de limite de fréquence en définissant `override_frequency_capping` sur `true` dans la requête API.

Par défaut, les nouvelles campagnes et les nouveaux Canvas qui n'obéissent pas aux limites de fréquence ne seront pas non plus comptabilisés dans celles-ci. Ceci est configurable pour chaque campagne et Canvas.

{% alert note %}
Ce comportement modifie le comportement par défaut lorsque vous désactivez la limite de fréquence pour une campagne ou un Canvas. Les modifications sont rétrocompatibles et n'affectent pas les messages actuellement en cours.
{% endalert %}

![Section des contrôles d'envoi avec la limite de fréquence activée.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"}

#### Comment les envois sont comptabilisés dans les plafonds {#how-sends-count-toward-caps}

La limite de fréquence s'applique par envoi : chaque fois que Braze envoie une campagne ou un composant Canvas à un utilisateur, cela compte dans vos plafonds — pas chaque variante de message ou plateforme au sein de cet envoi. Par exemple, si les utilisateurs sont plafonnés à cinq campagnes push par semaine, ils ne reçoivent plus aucune campagne push après le cinquième envoi jusqu'à la réinitialisation du plafond.

##### Envois multicanal {#multichannel-sends}

Lorsqu'un seul envoi utilise plusieurs canaux, cet envoi compte au maximum une fois par règle de limite de fréquence applicable. Par exemple, si vous créez une campagne multicanal qui envoie un e-mail, une notification push iOS et une notification push Android en un seul envoi, et que votre espace de travail a des règles pour les notifications push et les e-mails, ainsi qu'une règle qui s'applique à tous les canaux, cet envoi compte une fois dans la règle push, une fois dans la règle e-mail et une fois dans la règle tous canaux — il ne compte pas une fois par plateforme push ou par message au sein de l'envoi. Si les utilisateurs sont plafonnés à une notification push et une campagne e-mail par jour et qu'ils reçoivent cette campagne multicanal, ils ne sont plus éligibles pour des campagnes push ou e-mail supplémentaires pour le reste de la journée, sauf si une campagne ignore les règles de limite de fréquence.

Les messages in-app et les Content Cards ne sont pas comptabilisés comme ou dans les plafonds des campagnes ou composants Canvas de tout type.

##### Notifications push avec plusieurs appareils {#push-notifications-with-multiple-devices}

Pour les campagnes push, la limite de fréquence est comptabilisée au niveau de la campagne ou du composant Canvas, et non par appareil individuel. Si un profil utilisateur a plusieurs appareils enregistrés pour les notifications push (par exemple, un iPhone et un iPad), un plafond de fréquence au niveau de la campagne compte cela comme un seul envoi, quel que soit le nombre d'appareils qui reçoivent la notification. Cela est similaire à la façon dont une campagne récurrente avec une cadence quotidienne compte comme un envoi par jour, même si elle se répète plusieurs fois au cours de la semaine.

{% alert important %}
La limite de fréquence globale est planifiée en fonction du fuseau horaire de l'utilisateur et est calculée par jours calendaires, et non par périodes de 24 heures. Par exemple, si vous configurez une règle de limite de fréquence pour n'envoyer pas plus d'une campagne par jour, un utilisateur peut recevoir un message à 23 h dans son fuseau horaire local, et il serait éligible pour recevoir un autre message une heure plus tard.
{% endalert %}

#### Cas d'usage {#use-cases}

{% tabs %}
{% tab Cas d'usage 1 %}

Imaginons que vous définissiez une règle de limite de fréquence pour que vos utilisateurs ne reçoivent pas plus de trois campagnes de notifications push ou étapes Canvas par semaine de toutes les campagnes ou étapes Canvas.

Si votre utilisateur est prévu pour recevoir trois notifications push, deux messages in-app et une Content Card cette semaine, il recevra tous ces messages.

{% endtab %}
{% tab Cas d'usage 2 %}

Ce scénario utilise une règle de limite de fréquence pour que les utilisateurs ne reçoivent pas plus de deux campagnes de notifications push ou étapes Canvas par semaine de toutes les campagnes ou étapes Canvas.

**Lorsque le scénario suivant se produit :**

- Un utilisateur déclenche la même campagne `Campaign ABC` trois fois au cours d'une semaine.
- Cet utilisateur déclenche `Campaign ABC` une fois le lundi, une fois le mercredi et une fois le jeudi.

![Section de limite de fréquence avec la règle d'envoyer pas plus de 2 campagnes de notifications push/étapes Canvas de toutes les campagnes/étapes Canvas à un utilisateur chaque semaine.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Alors, le comportement attendu est que :**

- Cet utilisateur recevra les envois de campagne déclenchés le lundi et le mercredi.
- Cet utilisateur ne recevra pas le troisième envoi de campagne le jeudi car il a déjà reçu deux envois de campagne push cette semaine.

{% endtab %}
{% endtabs %}

### Limite de fréquence par étiquette {#frequency-capping-by-tag}

Les [règles de limite de fréquence](#delivery-rules) peuvent être appliquées aux espaces de travail en utilisant des étiquettes spécifiques que vous avez appliquées à vos campagnes et Canvas, vous permettant essentiellement de baser votre limite de fréquence sur des groupes nommés personnalisés.

Avec la limite de fréquence par étiquette, les règles peuvent être définies sur les étiquettes principales et imbriquées, de sorte que Braze prendra en compte toutes les étiquettes. Par exemple, si vous avez choisi d'utiliser l'étiquette principale A comme limite de fréquence, nous inclurons également les informations de toutes les étiquettes imbriquées (par exemple, les étiquettes B et C) lors de la détermination de la limite.

Vous pouvez également combiner la limite de fréquence standard avec la limite de fréquence par étiquettes. Considérez les règles suivantes :

1. Pas plus de trois campagnes de notifications push ou composants Canvas par semaine de toutes les campagnes et étapes Canvas. <br>**ET**
2. Pas plus de deux campagnes de notifications push ou composants Canvas par semaine avec l'étiquette `promotional`.

![Section de limite de fréquence avec deux règles limitant le nombre de campagnes de notifications push/Canvas pouvant être envoyées à un utilisateur chaque semaine.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

En conséquence, vos utilisateurs ne recevront pas plus de trois envois de campagne par semaine sur toutes les campagnes et étapes Canvas et pas plus de deux campagnes de notifications push ou composants Canvas avec l'étiquette `promotional`.

{% alert important %}
Les Canvas sont étiquetés au niveau du Canvas, par opposition à l'étiquetage par composant. Ainsi, chaque composant Canvas héritera de toutes les étiquettes au niveau du Canvas.
{% endalert %}

#### Règles en conflit {#conflicting-rules}

Lorsque des règles sont en conflit, la règle de limite de fréquence la plus restrictive et applicable est appliquée à vos utilisateurs. Par exemple, imaginons que vous ayez les règles suivantes :

1. Pas plus d'une campagne de notifications push ou composant Canvas par semaine de toutes les campagnes et composants Canvas. <br>**ET**
2. Pas plus de trois campagnes de notifications push ou composants Canvas par semaine avec l'étiquette `promotional`.

![Section de limite de fréquence avec des règles en conflit pour limiter le nombre de campagnes de notifications push/étapes Canvas envoyées à un utilisateur chaque semaine.]({% image_buster /assets/img/global_rules.png %} "global rules")

Dans cet exemple, votre utilisateur ne recevra pas plus d'une campagne de notifications push ou composant Canvas avec l'étiquette « promotional » au cours d'une semaine donnée, car vous avez spécifié que les utilisateurs ne doivent pas recevoir plus d'une campagne de notifications push ou composant Canvas de toutes les campagnes et composants Canvas. En d'autres termes, la règle de fréquence applicable la plus restrictive est celle qui sera appliquée à un utilisateur donné.

#### Comptage des étiquettes {#tag-count}

Les règles de limite de fréquence par étiquette sont calculées au moment de l'envoi d'un message. Cela signifie que la limite de fréquence par étiquette ne compte que les étiquettes actuellement présentes sur les campagnes ou Canvas qu'un utilisateur a reçus dans le passé. Elle ne compte pas les étiquettes qui étaient sur les campagnes ou Canvas au moment de leur envoi, mais qui ont depuis été supprimées. Elle compte si une étiquette est ajoutée ultérieurement à un message qu'un utilisateur a reçu dans le passé, mais avant que le nouveau message étiqueté ne soit envoyé.

##### Cas d'usage {#use-case}

Considérez les campagnes et la règle de limite de fréquence par étiquette suivantes :

**Campagnes** :

- **Campaign A** est une campagne push étiquetée `promotional`. Elle est prévue pour être envoyée à 9 h le lundi.
- **Campaign B** est une campagne push étiquetée `promotional`. Elle est prévue pour être envoyée à 9 h le mercredi.

**Règle de limite de fréquence par étiquette :**

- Votre utilisateur ne doit pas recevoir plus d'une campagne de notifications push par semaine avec l'étiquette `promotional`.<br><br>

| Action | Résultat |
|---|---|
| L'étiquette `promotional` est supprimée de **Campaign A** après que votre utilisateur a reçu le message, mais avant que **Campaign B** ne soit envoyée. | Votre utilisateur reçoit **Campaign B**. |
| L'étiquette `promotional` est supprimée par erreur de **Campaign A** après que votre utilisateur a reçu le message. <br> L'étiquette est rajoutée à **Campaign A** le mardi, avant que **Campaign B** ne soit envoyée. | Votre utilisateur ne reçoit pas **Campaign B**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'usage" }

#### Envoi à grande échelle {#sending-at-large-scales}

Les règles de limite de fréquence par étiquette peuvent ne pas être correctement appliquées à grande échelle, comme 100 messages par canal provenant de campagnes ou composants Canvas.

Par exemple, si votre règle de limite de fréquence par étiquette est :

> Pas plus de deux campagnes e-mail ou composants Canvas avec l'étiquette `Promotional` à un utilisateur chaque semaine.

Et que vous envoyez à l'utilisateur plus de 100 e-mails provenant de campagnes et d'étapes Canvas avec la limite de fréquence activée au cours d'une semaine, plus de deux e-mails peuvent être envoyés à l'utilisateur.

Étant donné que 100 messages par canal représentent plus de messages que la plupart des marques n'en envoient à leurs utilisateurs, il est peu probable que vous soyez affecté par cette limitation. Pour éviter cette limitation, vous pouvez définir un plafond pour le nombre maximum d'e-mails que vous souhaitez que vos utilisateurs reçoivent au cours d'une semaine.

Par exemple, vous pourriez configurer la règle suivante :

> Pas plus de trois campagnes e-mail ou composants Canvas par semaine de toutes les campagnes et étapes Canvas.

Cette règle garantit qu'aucun utilisateur ne reçoit plus de 100 e-mails par semaine car, au maximum, les utilisateurs reçoivent trois e-mails par semaine provenant de campagnes ou composants Canvas avec la limite de fréquence activée.

## Questions fréquemment posées {#frequently-asked-questions}

### Si je modifie la limitation d'envoi d'un Canvas actif, cela affecte-t-il les utilisateurs déjà dans le Canvas ? {#if-i-change-a-send-throttle-on-an-active-canvas-does-it-affect-users-already-in-the-canvas}

Oui, lorsque vous augmentez ou diminuez une limite de débit d'un Canvas, la limite mise à jour prend effet pour les nouveaux messages dans un délai d'environ 30 secondes après la modification en raison de la mise en cache.

### La limite de fréquence fait-elle sortir les utilisateurs d'un Canvas ? {#does-frequency-capping-cause-users-to-exit-a-canvas}

Non. Si un utilisateur Canvas est plafonné en fréquence en raison des paramètres de limite de fréquence globale, l'utilisateur avance immédiatement à l'étape Canvas suivante. L'utilisateur ne sort **pas** du Canvas en raison de la limite de fréquence.

### Comment puis-je identifier les utilisateurs qui ont été plafonnés en fréquence dans un Canvas ? {#how-can-i-identify-users-who-were-frequency-capped-in-a-canvas}

Les utilisateurs plafonnés en fréquence ne génèrent pas d'événement d'envoi pour cette étape. Pour identifier ces utilisateurs, vous pouvez utiliser [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) pour suivre les événements de plafonnement de fréquence des messages. Vous pouvez également créer une [extension de segment]({{site.baseurl}}/user_guide/audience/segments/segment_extension) pour analyser les utilisateurs qui sont entrés dans le Canvas mais n'ont pas reçu le message attendu.

### Pourquoi le tableau de bord affiche-t-il une erreur de limite de débit pour ma campagne ? {#why-does-the-dashboard-show-a-rate-limit-error-for-my-campaign}

Cela signifie généralement que la [limite de débit de vitesse d'envoi](#delivery-speed-rate-limiting) de la campagne est définie à un niveau trop bas pour la taille de l'audience, de sorte que terminer l'envoi prendrait plus de temps que la fenêtre autorisée et Braze affiche un avertissement. Augmentez la limite de débit de vitesse d'envoi, réduisez l'audience, ou utilisez **Limiter le volume d'envoi** pour que chaque occurrence planifiée se termine dans la fenêtre d'envoi autorisée. Vous pouvez également définir une [limite de débit de messagerie de l'espace de travail]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) pour appliquer un plafond à l'ensemble des campagnes.

**Limiter le volume d'envoi** contrôle le nombre d'utilisateurs éligibles pour un envoi, pas le nombre de messages que Braze envoie par minute. Seule une limite de débit de vitesse d'envoi définit le débit par minute.

### Que signifie « Envoyé » pour la limite de fréquence ? {#what-does-sent-mean-for-frequency-capping}

Dans les analyses et la limite de fréquence, _Envoyé_ fait référence au moment où Braze envoie le message (l'envoi est enregistré), et non à la livraison finale garantie à l'appareil ou à la boîte de réception. La limite de fréquence et le comptage des envois utilisent ces événements d'envoi enregistrés, qui peuvent différer des indicateurs « livré » en aval.

### Pourquoi est-ce que je vois des rebonds ou des reports d'e-mails ? {#why-am-i-seeing-email-bounces-or-deferrals}

Les messages de rebond et de report d'e-mails utilisent de nombreux codes différents et des textes spécifiques aux fournisseurs. Ne considérez pas un code particulier comme le signe d'un problème de limite de débit, car la cause dépend de votre contexte d'envoi et des retours du fournisseur de boîtes aux lettres.

Si les messages sont temporairement reportés, envoyer moins peut aider à court terme. Utilisez une [limite de débit de vitesse d'envoi](#delivery-speed-rate-limiting), **Limiter le volume d'envoi**, ou les deux.

Pour une solution à long terme, travaillez avec un expert en livrabilité pour examiner vos données de rebonds et de reports.