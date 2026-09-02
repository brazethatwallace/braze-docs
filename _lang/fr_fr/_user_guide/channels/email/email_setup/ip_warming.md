---
nav_title: IP warming
article_title: IP warming
page_order: 1
page_type: reference
description: "Cet article de référence traite de l'IP warming et des bonnes pratiques."
channel: email
local_redirect:
  automated-ip-warming: '/docs/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming'
---

# IP warming {#ip-warming}

> L'IP warming consiste à habituer les fournisseurs de boîtes de réception à recevoir des messages provenant de vos adresses IP dédiées. Il s'agit d'une étape essentielle de l'envoi d'e-mails avec n'importe quel fournisseur de services d'e-mail marketing (fournisseur de services d'e-mailing) et d'une pratique courante chez Braze pour garantir que vos messages atteignent leur boîte de réception à un taux élevé et constant. Si vous utilisez l'[IP warming automatisé]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming), consultez la [FAQ sur l'IP warming automatisé]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/faq).

L'IP warming est conçu pour vous aider à établir une réputation positive auprès des fournisseurs de services Internet (ISP). Chaque fois qu'une nouvelle adresse IP est utilisée pour envoyer un e-mail, les ISP surveillent ces e-mails de manière programmatique afin de vérifier qu'ils ne sont pas utilisés pour envoyer des courriers indésirables aux utilisateurs. Considérez la réputation de votre IP et de votre domaine comme un score de crédit : les ISP s'appuient sur cette réputation pour déterminer si votre courrier arrive dans la boîte de réception ou dans le dossier spam. Tout comme un score de crédit, il faut du temps pour bâtir une réputation positive, et encore plus pour en reconstruire une mauvaise.

## Réception des e-mails et livrabilité {#email-delivery-and-deliverability}

La **réception** correspond à la part d'e-mails acceptés et n'ayant pas subi d'échec d'envoi définitif. La **livrabilité** indique si le courrier atteint la boîte de réception plutôt que le dossier de courrier indésirable — les fournisseurs de boîtes de réception n'exposent pas cette information sous la forme d'un indicateur unique.

Un taux de réception sain se situe souvent autour de 99 % avec un taux de rebond ne dépassant pas environ 1 %. Les taux peuvent sembler bons sur le papier tout en masquant des problèmes (par exemple, de nombreux rebonds provenant d'un seul domaine, ou des e-mails distribués mais filtrés comme courrier indésirable). Surveillez les ouvertures et les clics, pas uniquement la réception. Même un faible taux de signalement de courrier indésirable peut justifier un examen plus approfondi.

### Recommandations avant l'IP warming {#recommendations-before-ip-warming}

Avant de commencer l'IP warming :

1. Dans **Paramètres** > **Préférences e-mail**, définissez votre domaine d'envoi par défaut, ajoutez un lien de désabonnement valide dans votre [pied de page personnalisé]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer), activez l'[en-tête list-unsubscribe]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) et envisagez des pages personnalisées de désabonnement/abonnement si nécessaire.
2. Configurez la [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) pour les e-mails.
3. Créez vos modèles requis en accédant à **Contenu** > **E-mail**.

## Que se passe-t-il si je n'ai pas le temps de réchauffer mes IP ? {#what-if-i-dont-have-time-to-warm-ips}

**L'IP warming est obligatoire.** Si vous ne réchauffez pas vos IP correctement et que le schéma de vos e-mails éveille le moindre soupçon, la vitesse de distribution de vos e-mails pourrait être considérablement limitée ou ralentie. Votre domaine ou votre IP pourrait également être bloqué par les fournisseurs de services Internet, ce qui peut entraîner l'envoi de vos e-mails directement dans le dossier spam de la boîte de réception de vos utilisateurs. C'est pourquoi il est important de réchauffer vos IP correctement.

Les fournisseurs de services Internet limitent la distribution des e-mails lorsqu'un soupçon de spam apparaît, afin de protéger leurs utilisateurs. Par exemple, si vous envoyez un e-mail à 100 000 utilisateurs, le fournisseur de services Internet pourrait ne distribuer l'e-mail qu'à 5 000 de ces utilisateurs au cours de la première heure. Ensuite, il surveille les indicateurs d'engagement tels que les taux d'ouverture, les taux de clics, les désabonnements et les signalements de courrier indésirable. Ainsi, si un nombre significatif de signalements de spam se produit, il pourrait choisir de reléguer le reste de cet envoi dans le dossier spam plutôt que de le distribuer dans la boîte de réception de l'utilisateur.

Si l'engagement est modéré, il peut continuer à limiter vos e-mails afin de collecter davantage de données d'engagement pour déterminer avec plus de certitude si l'e-mail est du spam ou non. Si l'e-mail présente des indicateurs d'engagement très élevés, il peut cesser complètement de limiter cet e-mail. Ces données sont utilisées pour créer une réputation d'e-mail qui détermine si vos e-mails sont automatiquement filtrés comme spam.

Si votre domaine ou votre IP est bloqué par un fournisseur de services Internet, les journaux de messages dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) contiendront des informations sur les sites web à consulter pour faire appel auprès de ces fournisseurs et être retiré de ces listes.

## Planifications d'IP warming {#ip-warming-schedules}

Nous vous recommandons vivement de respecter strictement une planification d'IP warming pour favoriser la livrabilité. Il est également important de ne pas sauter de jours, car une montée en charge régulière améliore les indicateurs de distribution. Choisissez une planification en fonction de votre historique d'envoi d'e-mails existant et de vos indicateurs de livrabilité.

{% alert tip %}
Si vous souhaitez bénéficier d'une ressource dédiée à la livrabilité au sein de votre équipe de compte, contactez votre gestionnaire de compte Braze pour plus d'informations.
{% endalert %}

{% tabs local %}
{% tab Conservateur %}

La planification conservatrice est une approche plus lente et plus prudente qui aide à établir une solide réputation d'expéditeur en partant de zéro. Elle est recommandée si vous débutez dans l'envoi d'e-mails, si vous migrez depuis une IP partagée, ou si vous avez rencontré des problèmes de livrabilité tels que la limitation de débit ou le blocage par un fournisseur de boîtes de réception.

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
22+ | Doubler tous les 3 jours jusqu'au volume souhaité

{% endtab %}
{% tab Modéré %}

La planification modérée est une approche équilibrée qui augmente le volume d'envoi à un rythme régulier. Elle est recommandée pour la plupart des expéditeurs, y compris ceux qui disposent d'un certain historique d'envoi d'e-mails et qui effectuent une transition vers une nouvelle IP.

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
22+ | Doubler tous les 2 jours jusqu'au volume souhaité

{% endtab %}
{% tab Agressif %}

{% alert important %}
La planification agressive est l'approche la plus rapide et n'est recommandée que pour les expéditeurs disposant d'un historique d'envoi établi et positif, ainsi que d'indicateurs de livrabilité conformes aux bonnes pratiques, notamment des taux d'ouverture élevés, des taux de clics élevés et des taux de rebond faibles. Utiliser cette planification sans un historique éprouvé peut nuire à votre réputation d'expéditeur.
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
21+ | Doubler quotidiennement jusqu'au volume souhaité

{% endtab %}
{% endtabs %}

Dans la plupart des cas, montez en charge jusqu'à votre volume d'envoi quotidien moyen plutôt que votre volume de pointe. Les fournisseurs de services Internet évaluent principalement le comportement d'envoi des dernières semaines pour déterminer votre réputation. Ainsi, si vous n'atteignez votre volume de pointe que tous les quelques mois (par exemple, 7 millions lors d'une période saisonnière), vous pouvez monter en charge vers ce pic plus près de la date d'envoi. En revanche, si vous atteignez votre volume de pointe toutes les une à deux semaines, montez en charge jusqu'à ce pic dès le départ.

Une fois l'IP warming terminé et le volume quotidien souhaité atteint, vous devez vous efforcer de maintenir ce volume quotidiennement. Certaines fluctuations sont normales, mais atteindre le volume souhaité puis n'effectuer qu'un envoi massif une fois par semaine peut avoir un impact négatif sur vos indicateurs de distribution et votre réputation d'expéditeur.

{% alert important %}
La plupart des fournisseurs de services Internet ne conservent les données de réputation que pendant 30 jours. Si vous passez un mois sans envoyer de messages, vous devez recommencer le processus d'IP warming.
{% endalert %}

### Adresses IP {#ip-addresses}

Après trois mois de non-utilisation, Braze peut recycler et réattribuer des adresses IP. Quel que soit l'historique antérieur d'une adresse IP, un IP warming complet est recommandé pour toutes les IP nouvellement attribuées, car la plupart des fournisseurs de services Internet ne conservent les données de réputation que pendant 30 jours. Pour la plupart des fournisseurs, cela signifie qu'une période d'inactivité de trois mois réinitialise effectivement la réputation. Si vous avez d'autres questions sur l'historique d'une adresse IP spécifique, contactez l'[assistance Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Comment limiter les envois pendant le warming {#how-to-limit-sends-during-warming}

Notre fonctionnalité intégrée de limitation des utilisateurs est un outil utile pour vous aider dans le warming de votre adresse IP. Après avoir choisi les Segments de communication souhaités lors de la création de la campagne, à l'étape [Utilisateurs cibles]({{site.baseurl}}/user_guide/channels/email/html_editor#step-4-build-the-remainder-of-your-campaign-or-canvas), sélectionnez le menu déroulant **Advanced Options** pour limiter vos utilisateurs. Au fur et à mesure que votre calendrier de warming progresse, vous pouvez augmenter progressivement cette limite pour accroître le volume d'e-mails que vous envoyez.

![La fonctionnalité intégrée de limitation des utilisateurs est un outil utile pour vous aider dans le warming de votre adresse IP. Après avoir choisi les Segments de communication souhaités lors de la création de la campagne, à l'étape Utilisateurs cibles, sélectionnez le menu déroulant Advanced Options pour limiter vos utilisateurs. Au fur et à mesure que votre calendrier de warming progresse, vous pouvez augmenter progressivement cette limite pour accroître le volume d'e-mails que vous envoyez.]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentation par sous-domaine {#subdomain-segmentation}

De nombreux fournisseurs de services Internet et fournisseurs d'accès aux e-mails ne filtrent plus uniquement en fonction de la réputation de l'adresse IP. Ces technologies de filtrage prennent désormais également en compte la réputation basée sur le domaine. Cela signifie que les filtres examinent toutes les données associées au domaine de l'expéditeur et ne se limitent plus à l'adresse IP seule. C'est pourquoi, en plus du warming de votre adresse IP d'envoi d'e-mails, nous recommandons également d'utiliser des domaines ou sous-domaines distincts pour les e-mails marketing, transactionnels et professionnels.

{% alert important %}
La segmentation par sous-domaine est particulièrement importante pour les expéditeurs à fort volume. Ces expéditeurs doivent collaborer avec un conseiller Braze lors de la configuration de leur compte afin de s'assurer qu'ils respectent cette pratique.
{% endalert %}

Nous recommandons de segmenter vos domaines de manière à ce que les e-mails professionnels soient envoyés via votre domaine de premier niveau, tandis que les e-mails marketing et transactionnels soient envoyés via des domaines ou sous-domaines différents.

## Bonnes pratiques {#best-practices}

Vous pouvez éviter toutes les conséquences d'un IP warming insuffisant en suivant ces bonnes pratiques :

### Commencer par de petits volumes d'envoi d'e-mails {#start-with-small-sending-volumes-of-email}

Augmentez la quantité d'e-mails envoyés chaque jour aussi progressivement que possible. Les campagnes d'e-mails soudaines et à fort volume sont celles qui suscitent le plus de méfiance de la part des fournisseurs de services Internet. Par conséquent, commencez par envoyer de petites quantités d'e-mails et augmentez progressivement vers le volume que vous souhaitez atteindre à terme. Gardez à l'esprit que vous réchauffez votre IP auprès de chaque fournisseur de services Internet individuellement : les fournisseurs ne partagent pas les données de réputation entre eux. Lorsque vous planifiez vos volumes de warming, assurez-vous de ne pas augmenter le volume trop rapidement auprès d'un seul fournisseur. Quel que soit le volume, nous vous recommandons de réchauffer votre IP par précaution. Consultez les [plannings d'IP warming](#ip-warming-schedules).

### Proposer un contenu d'introduction engageant {#have-engaging-introductory-content}

Vérifiez que votre premier contenu est très engageant et maximise la probabilité que les utilisateurs cliquent, ouvrent et interagissent avec vos e-mails. Privilégiez toujours des e-mails bien ciblés plutôt que des envois massifs indifférenciés lors du réchauffement de vos IP.

### Définir une cadence d'envoi régulière {#set-a-consistent-sending-cadence}

Une fois l'IP warming terminé, établissez une cadence d'envoi en veillant également à répartir vos e-mails sur une journée ou plusieurs jours. En créant un planning aussi régulier que possible, vous pouvez éviter un refroidissement de l'IP, qui peut survenir si le volume d'envoi s'arrête ou diminue significativement pendant plus de quelques jours.

Consultez notre [planning d'IP warming](#ip-warming-schedules) pour répartir vos envois sur une période plus longue, plutôt que d'envoyer un envoi massif à un moment précis.

### Nettoyer vos listes d'e-mails {#clean-your-email-lists}

Vérifiez que votre liste d'e-mails est propre et ne contient pas d'adresses anciennes ou non vérifiées. L'idéal est de vous assurer que vous êtes [conforme aux réglementations CASL et CAN-SPAM]({{site.baseurl}}/user_guide/administer/global/privacy/spam_regulations).

### Surveiller votre réputation d'expéditeur {#monitor-your-sender-reputation}

Lors du processus d'IP warming, veillez à surveiller attentivement votre réputation d'expéditeur. Ces indicateurs spécifiques sont importants à suivre :
- **Taux de rebond :** si une campagne présente un taux de rebond supérieur à 3-5 %, vous devriez évaluer la propreté de votre liste en suivant les recommandations de notre article [Keep It Clean: The Importance of Email List Hygiene](https://www.braze.com/blog/email-list-hygiene/). De plus, vous devriez envisager de mettre en place une [politique de temporisation]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies) pour cesser d'envoyer des e-mails aux adresses inactives ou dormantes.
- **Signalements de courrier indésirable :** si une campagne est signalée comme courrier indésirable à un taux supérieur à 0,08 %, vous devriez réévaluer le contenu que vous envoyez, vérifier qu'il est ciblé vers une audience intéressée et vous assurer que vos e-mails sont formulés de manière à susciter l'intérêt.
- **Taux d'ouverture :** les taux d'ouverture sont un indicateur utile du placement en boîte de réception. Si vos taux d'ouverture uniques dépassent 25 %, vous bénéficiez probablement d'un bon placement en boîte de réception, ce qui indique une réputation d'expéditeur positive.

{% alert tip %}
Braze déconseille d'utiliser le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) pour réchauffer vos IP. Étant donné que les campagnes d'IP warming font partie des premières campagnes que vous envoyez, Braze ne dispose pas encore de suffisamment d'informations sur vos utilisateurs pour calculer un moment d'envoi optimal. Dans ce cas, tous les messages avec le timing intelligent seraient envoyés à l'heure de repli par défaut, donc au même moment.
{% endalert %}

{% alert tip %}
Il est normal que des e-mails soient envoyés dans le dossier de courrier indésirable pendant l'IP warming, car votre domaine et votre IP n'ont pas encore établi de réputation positive. Si des e-mails arrivent dans votre dossier de courrier indésirable, votre administrateur de messagerie devra peut-être ajouter votre domaine d'envoi Braze et votre IP à la liste d'autorisation de votre entreprise.
{% endalert %}