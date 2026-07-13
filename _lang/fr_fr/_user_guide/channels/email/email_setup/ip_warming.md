---
nav_title: Réchauffement d'adresses IP
article_title: Réchauffement d'adresses IP
page_order: 1
page_type: reference
description: "Cet article de référence traite du réchauffement d'adresses IP et des bonnes pratiques."
channel: email
local_redirect:
  automated-ip-warming: '/docs/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming'
---

# Réchauffement d'adresses IP {#ip-warming}

> Le réchauffement d'adresses IP consiste à habituer les fournisseurs de boîtes de réception à recevoir des messages provenant de vos adresses IP dédiées. Il s'agit d'une étape essentielle de l'envoi d'e-mails avec n'importe quel fournisseur de services d'e-mailing (ESP) et d'une pratique courante chez Braze pour garantir que vos messages atteignent leur boîte de réception à un taux élevé et constant.

Le réchauffement d'adresses IP est conçu pour vous aider à établir une réputation positive auprès des fournisseurs de services Internet (ISP). Chaque fois qu'une nouvelle adresse IP est utilisée pour envoyer un e-mail, les ISP surveillent ces e-mails de manière programmatique afin de vérifier qu'ils ne sont pas utilisés pour envoyer des courriers indésirables aux utilisateurs. Considérez la réputation de votre IP et de votre domaine comme un score de crédit : les ISP s'appuient sur cette réputation pour déterminer si votre courrier arrive dans la boîte de réception ou dans le dossier spam. Tout comme un score de crédit, il faut du temps pour bâtir une réputation positive, et encore plus pour en reconstruire une mauvaise.

## Distribution et livrabilité des e-mails {#email-delivery-and-deliverability}

La **distribution** correspond à la part d'e-mails qui ont été acceptés et n'ont pas subi d'échec d'envoi définitif. La **livrabilité** indique si le courrier atteint la boîte de réception plutôt que le dossier spam — les fournisseurs de messagerie n'exposent pas cette information sous la forme d'un indicateur unique.

Un taux de distribution sain se situe généralement autour de 99 % avec un taux de rebond ne dépassant pas environ 1 %. Les taux peuvent sembler bons sur le papier tout en masquant des problèmes (par exemple, de nombreux rebonds provenant d'un seul domaine, ou des e-mails distribués mais filtrés comme spam). Surveillez les ouvertures et les clics, pas uniquement la distribution. Même un faible taux de signalement de courrier indésirable peut justifier un examen approfondi.

### Recommandations avant le réchauffement d'adresses IP {#recommendations-before-ip-warming}

Avant de commencer le réchauffement d'adresses IP :

1. Dans **Paramètres** > **Préférences des e-mails**, définissez votre domaine d'envoi par défaut, ajoutez un lien de désabonnement valide dans votre [pied de page personnalisé]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer), activez l'[en-tête list-unsubscribe]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) et envisagez des pages de désabonnement/abonnement personnalisées si nécessaire.
2. Configurez la [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) pour les e-mails.
3. Créez vos modèles requis en accédant à **Contenu** > **E-mail**.

## Que faire si je n'ai pas le temps de réchauffer les adresses IP ? {#what-if-i-dont-have-time-to-warm-ips}

**Le réchauffement d'adresses IP est requis.** Si vous ne réchauffez pas les adresses IP de manière appropriée et que le schéma de vos envois d'e-mails éveille des soupçons, la vitesse de distribution de vos e-mails pourrait être considérablement ralentie. Votre domaine ou votre adresse IP pourrait également être bloqué par les ISP, ce qui peut entraîner l'envoi direct de vos e-mails dans le dossier spam de la boîte de réception de vos utilisateurs. C'est pourquoi il est important de réchauffer correctement vos adresses IP.

Les ISP limitent la distribution des e-mails lorsqu'ils soupçonnent du spam afin de protéger leurs utilisateurs. Par exemple, si vous envoyez un e-mail à 100 000 utilisateurs, l'ISP pourrait ne distribuer l'e-mail qu'à 5 000 de ces utilisateurs au cours de la première heure. Ensuite, il surveille les indicateurs d'engagement tels que les taux d'ouverture, les taux de clics, les désabonnements et les signalements de courrier indésirable. Si un nombre significatif de signalements de spam se produit, il peut choisir de reléguer le reste de cet envoi dans le dossier spam plutôt que de le distribuer dans la boîte de réception de l'utilisateur.

Si l'engagement est modéré, le fournisseur peut continuer à limiter le débit de vos e-mails pour collecter davantage de données d'engagement afin de déterminer avec plus de certitude si l'e-mail est du spam ou non. Si l'e-mail présente des indicateurs d'engagement très élevés, il peut cesser complètement de limiter le débit. Ces données sont utilisées pour construire une réputation d'expéditeur qui déterminera à terme si vos e-mails sont automatiquement filtrés comme spam.

Si votre domaine ou votre adresse IP est bloqué par un ISP, les journaux de messages dans le [Journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) contiendront des informations sur les sites web à consulter pour faire appel auprès de ces fournisseurs et être retiré de ces listes.

## Calendriers de réchauffement d'adresses IP {#ip-warming-schedules}

Nous recommandons vivement de suivre strictement un calendrier de réchauffement d'adresses IP pour favoriser la livrabilité. Il est également important de ne pas sauter de jours, car une montée en charge régulière améliore les indicateurs de distribution. Choisissez un calendrier en fonction de votre historique d'envoi d'e-mails existant et de vos indicateurs de livrabilité.

{% alert tip %}
Si vous souhaitez bénéficier d'une ressource dédiée à la livrabilité au sein de votre équipe de compte, contactez votre gestionnaire de compte Braze pour en savoir plus.
{% endalert %}

{% tabs local %}
{% tab Conservateur %}

Le calendrier conservateur est une approche plus lente et plus prudente qui aide à établir une solide réputation d'envoi à partir de zéro. Il est recommandé si vous débutez dans l'envoi d'e-mails, si vous migrez depuis une adresse IP partagée, ou si vous avez rencontré des problèmes de livrabilité tels que la limitation de débit ou le blocage par un fournisseur de messagerie.

Jour | Nombre d'e-mails à envoyer
----|---------------------
1 | 50
2 | 50
3 | 50
4 | 100
5 | 100
6 | 100
7 | 500
8 | 500
9 | 500
10 | 1 000
11 | 1 000
12 | 1 000
13 | 2 000
14 | 2 000
15 | 2 000
16 | 4 000
17 | 4 000
18 | 4 000
19 | 8 000
20 | 8 000
21 | 8 000
22+ | Doublez tous les 3 jours jusqu'au volume souhaité

{% endtab %}
{% tab Modéré %}

Le calendrier modéré est une approche équilibrée qui augmente le volume d'envoi à un rythme régulier. Il est recommandé pour la plupart des expéditeurs, y compris ceux qui disposent d'un certain historique d'envoi d'e-mails et qui passent à une nouvelle adresse IP.

Jour | Nombre d'e-mails à envoyer
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1 000
5 | 2 000
6 | 4 000
7 | 8 000
8 | 16 000
9 | 25 000
10 | 35 000
11 | 50 000
12 | 75 000
13 | 100 000
14 | 150 000
15 | 200 000
16 | 275 000
17 | 375 000
18 | 500 000
19 | 650 000
20 | 825 000
21 | 1 000 000
22+ | Doublez tous les 2 jours jusqu'au volume souhaité

{% endtab %}
{% tab Agressif %}

{% alert important %}
Le calendrier agressif est l'approche la plus rapide et n'est recommandé que pour les expéditeurs disposant d'un historique d'envoi positif et établi, ainsi que d'indicateurs de livrabilité conformes aux bonnes pratiques, notamment des taux d'ouverture élevés, des taux de clics élevés et des taux de rebond faibles. Utiliser ce calendrier sans un historique éprouvé peut nuire à votre réputation d'expéditeur.
{% endalert %}

Jour | Nombre d'e-mails à envoyer
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1 000
5 | 2 500
6 | 5 000
7 | 9 000
8 | 16 000
9 | 29 000
10 | 52 000
11 | 98 000
12 | 160 000
13 | 225 000
14 | 315 000
15 | 450 000
16 | 615 000
17 | 875 000
18 | 1 200 000
19 | 1 750 000
20 | 2 750 000
21+ | Doublez chaque jour jusqu'au volume souhaité

{% endtab %}
{% endtabs %}

Dans la plupart des cas, montez en charge jusqu'à votre volume d'envoi quotidien moyen plutôt que votre volume de pointe. Les ISP examinent principalement les quelques semaines précédentes de comportement d'envoi pour évaluer votre réputation. Ainsi, si vous n'atteignez votre volume de pointe que tous les quelques mois (par exemple, 7 millions pendant une période saisonnière), vous pouvez monter en charge vers ce pic plus près de la date d'envoi. En revanche, si vous atteignez votre volume de pointe toutes les une à deux semaines, montez en charge jusqu'à ce pic dès le départ.

Une fois le réchauffement d'adresses IP terminé et le volume quotidien souhaité atteint, vous devez vous efforcer de maintenir ce volume quotidiennement. Certaines fluctuations sont normales, mais atteindre le volume souhaité puis n'effectuer qu'un envoi massif une fois par semaine peut avoir un impact négatif sur vos indicateurs de distribution et votre réputation d'expéditeur.

{% alert important %}
La plupart des ISP ne conservent les données de réputation que pendant 30 jours. Si vous passez un mois sans envoyer de messages, vous devez recommencer le processus de réchauffement d'adresses IP.
{% endalert %}

### Adresses IP {#ip-addresses}

Après trois mois de non-utilisation, Braze peut recycler et réattribuer des adresses IP. Quel que soit l'historique antérieur d'une adresse IP, un réchauffement complet est recommandé pour toutes les adresses IP nouvellement attribuées, car la plupart des ISP ne conservent les données de réputation que pendant 30 jours. Pour la plupart d'entre eux, cela signifie qu'une période d'inactivité de trois mois réinitialise effectivement la réputation. Si vous avez d'autres questions sur l'historique d'une adresse IP spécifique, contactez l'[Assistance Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Comment limiter les envois pendant le réchauffement {#how-to-limit-sends-during-warming}

La fonctionnalité intégrée de limitation du nombre d'utilisateurs est un outil utile pour vous aider à réchauffer votre adresse IP. Après avoir choisi les segments de messagerie souhaités lors de la création de la campagne, à l'étape [Utilisateurs cibles]({{site.baseurl}}/user_guide/channels/email/html_editor#step-4-build-the-remainder-of-your-campaign-or-canvas), sélectionnez le menu déroulant **Options avancées** pour limiter le nombre d'utilisateurs. Au fur et à mesure de votre calendrier de réchauffement, vous pouvez augmenter progressivement cette limite pour accroître le volume d'e-mails envoyés.

![La fonctionnalité intégrée de limitation du nombre d'utilisateurs est un outil utile pour vous aider à réchauffer votre adresse IP. Après avoir choisi les segments de messagerie souhaités lors de la création de la campagne, à l'étape Utilisateurs cibles, sélectionnez le menu déroulant Options avancées pour limiter le nombre d'utilisateurs. Au fur et à mesure de votre calendrier de réchauffement, vous pouvez augmenter progressivement cette limite pour accroître le volume d'e-mails envoyés.]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentation par sous-domaine {#subdomain-segmentation}

De nombreux ISP et fournisseurs d'accès à la messagerie ne filtrent plus uniquement en fonction de la réputation de l'adresse IP. Ces technologies de filtrage prennent désormais également en compte la réputation basée sur le domaine. Cela signifie que les filtres examinent toutes les données associées au domaine de l'expéditeur et ne se limitent pas à l'adresse IP seule. C'est pourquoi, en plus de réchauffer votre adresse IP, nous recommandons également d'utiliser des domaines ou sous-domaines distincts pour le courrier marketing, transactionnel et professionnel.

{% alert important %}
La segmentation par sous-domaine est particulièrement importante pour les expéditeurs à fort volume. Ces expéditeurs doivent travailler avec un conseiller Braze lors de la configuration de leur compte pour s'assurer qu'ils respectent cette pratique.
{% endalert %}

Nous recommandons de segmenter vos domaines de sorte que le courrier professionnel soit envoyé via votre domaine de premier niveau, et que le courrier marketing et transactionnel soit envoyé par des domaines ou sous-domaines différents.

## Bonnes pratiques {#best-practices}

Vous pouvez éviter toutes les conséquences d'un réchauffement d'adresses IP insuffisant en suivant ces bonnes pratiques :

### Commencez par de petits volumes d'envoi d'e-mails {#start-with-small-sending-volumes-of-email}

Augmentez la quantité envoyée chaque jour aussi progressivement que possible. Les campagnes d'e-mails soudaines et à fort volume sont celles qui éveillent le plus de suspicion chez les ISP. Par conséquent, commencez par envoyer de petites quantités d'e-mails et montez progressivement en charge vers le volume que vous souhaitez atteindre. Gardez à l'esprit que vous réchauffez votre adresse IP auprès de chaque ISP individuellement — ils ne partagent pas les données de réputation entre eux. Lorsque vous planifiez vos volumes de réchauffement, assurez-vous de ne pas augmenter le volume trop rapidement auprès d'un seul fournisseur. Quel que soit le volume, nous recommandons de réchauffer votre adresse IP par mesure de sécurité. Consultez les [calendriers de réchauffement d'adresses IP](#ip-warming-schedules).

### Proposez un contenu d'introduction engageant {#have-engaging-introductory-content}

Assurez-vous que votre premier contenu est très engageant et maximise la probabilité que les utilisateurs cliquent, ouvrent et interagissent avec votre e-mail. Privilégiez toujours des e-mails bien ciblés plutôt que des envois massifs indifférenciés lors du réchauffement d'adresses IP.

### Établissez une cadence d'envoi régulière {#set-a-consistent-sending-cadence}

Une fois le réchauffement d'adresses IP terminé, établissez une cadence d'envoi en veillant également à répartir vos e-mails sur une journée ou plusieurs jours. En créant un calendrier aussi régulier que possible, vous pouvez éviter un refroidissement de l'adresse IP, qui peut survenir si le volume d'envoi s'arrête ou diminue significativement pendant plus de quelques jours.

Consultez notre [calendrier de réchauffement d'adresses IP](#ip-warming-schedules) pour répartir vos envois sur une période plus longue, plutôt que d'effectuer un envoi massif à un moment précis.

### Nettoyez vos listes d'e-mails {#clean-your-email-lists}

Assurez-vous que votre liste d'e-mails est propre et ne contient pas d'adresses anciennes ou non vérifiées. L'idéal est de vérifier que vous êtes conforme aux réglementations [CASL et CAN-SPAM]({{site.baseurl}}/user_guide/administer/global/privacy/spam_regulations).

### Surveillez votre réputation d'expéditeur {#monitor-your-sender-reputation}

Lors du processus de réchauffement d'adresses IP, veillez à surveiller attentivement votre réputation d'expéditeur. Les indicateurs suivants sont particulièrement importants à observer :
- **Taux de rebond :** Si une campagne présente un taux de rebond supérieur à 3-5 %, vous devez évaluer la propreté de votre liste en suivant les recommandations de notre article [Keep It Clean: The Importance of Email List Hygiene](https://www.braze.com/blog/email-list-hygiene/). De plus, vous devriez envisager de mettre en place une [politique de désengagement]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies) pour cesser d'envoyer des e-mails aux adresses inactives ou dormantes.
- **Signalements de courrier indésirable :** Si une campagne est signalée comme spam à un taux supérieur à 0,08 %, vous devez réévaluer le contenu que vous envoyez, vérifier qu'il est ciblé vers une audience intéressée et vous assurer que vos e-mails sont formulés de manière à susciter l'intérêt.
- **Taux d'ouverture :** Les taux d'ouverture sont un indicateur utile du placement en boîte de réception. Si vos taux d'ouverture uniques dépassent 25 %, vous bénéficiez probablement d'un bon placement en boîte de réception, ce qui indique une réputation d'expéditeur positive.

{% alert tip %}
Braze déconseille l'utilisation du [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) pour réchauffer vos adresses IP. Les campagnes de réchauffement d'adresses IP étant parmi les premières que vous envoyez, Braze ne dispose pas encore de suffisamment d'informations sur vos utilisateurs pour calculer un moment d'envoi optimal. Dans ce cas, tous les messages avec le timing intelligent utiliseraient par défaut l'heure de repli et seraient envoyés au même moment.
{% endalert %}

{% alert tip %}
Il est normal que des e-mails soient envoyés dans le dossier spam pendant le réchauffement d'adresses IP, car votre domaine et votre adresse IP n'ont pas encore établi de réputation positive. Si des e-mails arrivent dans votre dossier spam, votre administrateur de messagerie devra peut-être ajouter votre domaine d'envoi Braze et votre adresse IP à la liste d'autorisation de votre entreprise.
{% endalert %}