---
nav_title: FAQ
article_title: FAQ sur les e-mails
page_order: 30
description: "Cette page fournit des réponses aux questions fréquemment posées sur l'envoi de messages par e-mail."
channel: email

---

# Questions fréquemment posées {#frequently-asked-questions}

> Cet article fournit des réponses à certaines questions fréquemment posées sur les e-mails.

## Que se passe-t-il lorsqu'un e-mail est envoyé et que plusieurs profils partagent la même adresse e-mail ? {#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address}

Si plusieurs utilisateurs partageant la même adresse e-mail se trouvent dans un segment devant recevoir une Campaign, un seul profil utilisateur possédant cette adresse est sélectionné au moment de l'envoi. Ainsi, l'e-mail n'est envoyé qu'une seule fois grâce à la déduplication, évitant que la même adresse ne reçoive le message plusieurs fois.

**Adresses e-mail uniques :** Braze n'impose pas l'unicité des adresses e-mail entre les profils. Si vous comptez sur une relation univoque entre une adresse e-mail et un profil, surveillez les doublons en interne lors de la création des utilisateurs.

**Déduplication avant Liquid :** Pour les envois où Braze déduplique par adresse e-mail au sein d'un même dispatch (par exemple, les Campaigns planifiées où plusieurs membres du segment partageant la même adresse sont traités ensemble), cette déduplication a lieu avant l'exécution de Liquid pour le profil choisi pour représenter cette adresse. Si Liquid interrompt le traitement pour ce profil (par exemple avec [`abort_message()`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)), cette adresse ne reçoit pas le message lors de ce dispatch, y compris les profils déjà ignorés par la déduplication. Les envois déclenchés n'appliquent pas cette même déduplication par adresse au sein d'un dispatch ; plusieurs profils partageant une adresse peuvent tous rester éligibles dans un même lot, de sorte que ce comportement d'interruption ne s'applique pas de la même manière (voir le paragraphe suivant).

Si plusieurs profils partagent une adresse e-mail et qu'un profil se désabonne, Braze met à jour les autres profils (jusqu'à 100) ayant cette adresse avec le même statut d'abonnement. Cela s'applique aux désabonnements et autres modifications telles que le statut d'abonnement global et les statuts individuels des groupes d'abonnement.

**Groupes initiateurs :** Pour les Campaigns avec des [groupes initiateurs]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups), Braze sélectionne un profil pour la distribution principale lorsque plusieurs profils partagent une adresse. Ce destinataire principal peut ne pas faire partie de votre groupe initiateur, même si un autre profil ayant la même adresse en fait partie.

Les scénarios suivants peuvent donner l'impression qu'un utilisateur a reçu un e-mail deux fois :

- **Listes initiateurs ou destinataires de test :** Les adresses initiateurs et les destinataires de test internes peuvent recevoir un envoi en plus de votre audience principale, ce qui peut ressembler à un doublon lorsqu'une boîte de réception correspond à la fois à un profil et à une entrée initiateur.
- **Une erreur s'est produite lors de la création de la Campaign ou du Canvas :** L'utilisateur peut ne pas recevoir le même envoi deux fois, mais peut recevoir deux e-mails distincts avec la même ligne d'objet. Lorsqu'une Campaign ou un Canvas est dupliqué, vérifiez les détails de configuration de l'e-mail tels que les images ou les lignes d'objet. Vous pouvez également consulter les journaux des modifications pour voir si la Campaign ou le Canvas a été modifié après le lancement : un doublon peut partager la même ligne d'objet que l'original au moment où l'utilisateur l'a reçu.
- **Plusieurs profils utilisateur ont un transfert d'e-mails :** Si un utilisateur possède plusieurs comptes dans une application donnée mais qu'un compte transfère les e-mails, l'utilisateur reçoit la Campaign une seule fois par boîte de réception ; le message peut apparaître deux fois dans la boîte où les messages sont transférés. Seuls certains fournisseurs indiquent quand un e-mail a été transféré depuis un autre compte.
- **Configuration de l'e-mail côté destinataire :** Certains clients fusionnent les boîtes de réception (« boîte de réception universelle »). Si la même Campaign cible plusieurs comptes partageant une boîte de réception, il peut sembler qu'une personne a reçu la Campaign deux fois alors que deux profils distincts ont effectivement reçu le message. Le destinataire peut confirmer si plusieurs comptes sont combinés dans une seule boîte de réception.

Cette déduplication s'applique lorsque les utilisateurs ciblés se trouvent dans le même dispatch. La rééligibilité est évaluée par profil, non par adresse e-mail.

La rééligibilité des Campaigns et des étapes Canvas utilise le profil de chaque utilisateur, et non la boîte de réception. Plusieurs profils peuvent donc être éligibles à des envois distincts tout en respectant cette logique. Combiné avec des déclencheurs, cela peut entraîner la distribution de plus d'un message à la même boîte de réception, même lorsque vous essayez de respecter une seule période d'inéligibilité au niveau de l'adresse. Les Campaigns déclenchées (à l'exception des Campaigns déclenchées par API) et les Canvas peuvent également envoyer deux fois à une même adresse lorsque des profils différents partageant la même adresse e-mail répondent au déclencheur à des moments différents, par exemple si l'utilisateur A et l'utilisateur B partagent `johndoe@example.com` mais se trouvent dans des fuseaux horaires différents alors que la distribution utilise les fuseaux horaires locaux.

Les utilisateurs ne sont pas dédupliqués par e-mail à l'entrée du Canvas, de sorte qu'ils peuvent ne pas être dédupliqués au-delà de la première étape d'un Canvas s'ils progressent à des moments légèrement différents en raison d'une entrée limitée par le débit. Lorsqu'un utilisateur associé à une adresse e-mail donnée ouvre ou clique sur un e-mail, tous les profils utilisateur partageant cette adresse sont marqués comme ayant ouvert ou cliqué la Campaign.

### Exception : Campaigns déclenchées par API {#exception-api-triggered-campaigns}

Les Campaigns déclenchées par API dédupliquent ou envoient des doublons en fonction de l'endroit où l'audience est définie. Les e-mails en double doivent être ciblés séparément dans l'appel API en utilisant des `user_ids` distincts pour recevoir plusieurs distributions. Voici trois scénarios possibles pour les Campaigns déclenchées par API :

- **Scénario 1 : E-mails en double dans le segment cible :** Si le même e-mail apparaît dans plusieurs profils utilisateur regroupés dans les filtres d'audience du tableau de bord pour une Campaign déclenchée par API, un seul des profils reçoit l'e-mail.
- **Scénario 2 : E-mails en double dans différents `user_ids` au sein de l'objet recipients :** Si le même e-mail apparaît dans plusieurs valeurs `external_user_id` référencées par l'objet `recipients`, l'e-mail est envoyé deux fois.
- **Scénario 3 : E-mails en double en raison de `user_ids` dupliqués dans l'objet recipients :** Si vous essayez d'ajouter le même profil utilisateur deux fois, un seul des profils reçoit l'e-mail.

{% alert important %}
Si vous envoyez une Campaign API via un appel API (à l'exclusion des Campaigns déclenchées par API), et que plusieurs utilisateurs sont spécifiés dans l'audience du segment avec la même adresse e-mail, l'envoi se fait autant de fois que l'adresse est listée dans l'appel. En effet, les appels API sont considérés comme intentionnellement construits.
{% endalert %}

#### Tests A/B avec des adresses e-mail en double {#ab-testing-with-duplicate-email-addresses}

Évitez les [tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) sur les e-mails lorsque plusieurs profils peuvent partager la même adresse e-mail. Les variantes sont attribuées par profil, ce qui peut produire plus d'un message dans la même boîte de réception. Si vous devez tester dans cette situation, ne combinez pas une étape de **variante gagnante** avec la [distribution en fuseau horaire local]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) d'une manière qui retarde la sélection du gagnant : ces options combinées peuvent augmenter le risque d'envois en double.

#### Canvas et adresses e-mail en double {#canvas-and-duplicate-email-addresses}

Pour les parcours Canvas, la possibilité que des adresses e-mail en double reçoivent un seul envoi ou plusieurs peut dépendre du traitement par lots à l'entrée, du timing des étapes et d'autres facteurs. Considérez ce comportement comme indéfini jusqu'à ce que vous le validiez pour votre parcours. Dans la mesure du possible, fusionnez ou consolidez les profils en double. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="deterministic deduplication for duplicate email addresses in Canvas" %}

### Que se passe-t-il pour le statut d'abonnement lorsque l'adresse e-mail d'un utilisateur est remplacée par une adresse partagée avec un autre utilisateur ? {#what-happens-to-the-subscription-state-when-a-users-email-address-changes-to-one-shared-by-another-user}

Si vous définissez ou mettez à jour l'adresse e-mail de l'utilisateur A avec une autre adresse e-mail partagée par un utilisateur B existant, l'utilisateur A hérite du statut d'abonnement déjà existant de l'utilisateur B, sauf si le paramètre **Réabonner les utilisateurs lorsqu'ils mettent à jour leur e-mail** est activé.

### Les mises à jour de mes paramètres d'e-mail sortant s'appliqueront-elles rétroactivement ? {#will-updates-to-my-outbound-email-settings-apply-retroactively}

Non. Les mises à jour apportées aux paramètres d'e-mail sortant n'affectent pas rétroactivement les envois existants. Par exemple, modifier le nom d'affichage par défaut dans les paramètres d'e-mail ne remplacera pas automatiquement le nom d'affichage par défaut existant dans vos Campaigns ou Canvas actifs.

### Qu'est-ce qu'un « bon » taux de distribution d'e-mails ? {#what-is-a-good-email-delivery-rate}

En général, le « nombre magique » se situe autour de 98 % de messages distribués avec un taux de rebond ne dépassant pas 3 %. Si moins de 98 % des messages sont distribués, il y a généralement lieu de s'inquiéter.

Cependant, un taux de distribution de 98 % ou plus peut encore présenter des problèmes de livrabilité. Par exemple, si tous vos rebonds proviennent d'un seul domaine, c'est un signal clair d'un problème de réputation avec ce fournisseur.

De plus, les messages peuvent être distribués mais finir dans les spams, ce qui indique des problèmes de réputation potentiellement sérieux. Il est important de surveiller non seulement le nombre de messages distribués, mais aussi les taux d'ouverture et de clics pour déterminer si les utilisateurs voient réellement les messages dans leur boîte de réception. Étant donné que les fournisseurs ne signalent généralement pas chaque instance de spam, un taux de spam même de 1 % peut être préoccupant et nécessiter une analyse approfondie.

Enfin, votre activité et les types d'e-mails que vous envoyez peuvent également affecter la distribution. Par exemple, quelqu'un envoyant principalement des [e-mails transactionnels]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email) devrait s'attendre à un meilleur taux que quelqu'un envoyant de nombreux messages marketing.

### Pourquoi mes indicateurs de distribution d'e-mails ne totalisent-ils pas 100 % ? {#why-are-my-email-delivery-metrics-not-adding-up-to-100}

Les indicateurs de distribution d'e-mails (distributions, rebonds et taux de spam) peuvent ne pas totaliser 100 % en raison des e-mails ayant subi un échec provisoire d'envoi et n'ayant pas été distribués après la période de réessai pouvant aller jusqu'à 72 heures.

Les échecs provisoires d'envoi sont des e-mails qui rebondissent en raison d'un problème temporaire ou transitoire, tel qu'une « boîte aux lettres pleine », un « serveur temporairement indisponible », etc. Si un e-mail ayant subi un échec provisoire d'envoi n'est toujours pas distribué après 72 heures, cet e-mail ne sera pas pris en compte dans les indicateurs de distribution de la Campaign.

### Qu'est-ce qu'une boucle de rétroaction e-mail ? {#what-is-an-email-feedback-loop}

Une boucle de rétroaction e-mail (FBL) permet aux expéditeurs de surveiller leur réputation en identifiant les Campaigns qui génèrent un volume élevé de plaintes. Pour les étapes de mise en œuvre d'une boucle de rétroaction Gmail, consultez l'article [Boucle de rétroaction de Google](https://support.google.com/a/answer/6254652).

### Que sont les pixels de suivi d'ouverture ? {#what-are-open-tracking-pixels}

Les [pixels de suivi d'ouverture]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement) utilisent le domaine de suivi des clics de l'expéditeur pour suivre les événements d'ouverture d'e-mails. Le pixel est une balise image ajoutée au HTML de l'e-mail. C'est le plus souvent le dernier élément HTML dans la balise body. Lorsqu'un utilisateur charge son e-mail, une requête est effectuée pour afficher l'image depuis le domaine de suivi personnalisé, ce qui enregistre un événement d'ouverture.

### Puis-je suivre les ouvertures pour les e-mails affichés en texte brut ? {#can-i-track-opens-for-emails-rendered-in-plain-text}

Non. Braze suit les ouvertures d'e-mails à l'aide d'un [pixel de suivi d'ouverture]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#open-tracking-pixel) intégré dans le HTML de l'e-mail. Lorsque le client de messagerie du destinataire charge l'e-mail, il demande cette image, et Braze enregistre un événement d'ouverture.

Étant donné que les e-mails en texte brut ne peuvent pas contenir d'images, le pixel de suivi d'ouverture n'est pas inclus, et les ouvertures ne peuvent donc pas être suivies pour les e-mails affichés en texte brut. Les clics peuvent toujours être suivis, car les hyperliens restent fonctionnels en texte brut.

C'est un comportement attendu. Pour une précision optimale du taux d'ouverture, concevez vos e-mails en HTML et gardez à l'esprit que les ouvertures ne seront pas comptabilisées lorsque les destinataires consultent la version en texte brut.

### Comment fonctionne le suivi des e-mails lorsque les destinataires transfèrent des e-mails ? {#how-does-email-tracking-work-when-recipients-forward-emails}

Lorsqu'un destinataire transfère un e-mail, l'e-mail transféré contient le même pixel de suivi d'ouverture et les mêmes liens de suivi des clics que l'original. Cela signifie :

- Si une personne qui ne faisait pas partie de l'audience originale de votre Campaign reçoit un e-mail transféré et l'ouvre, Braze enregistre un événement d'ouverture.
- Si cette personne clique sur un lien dans l'e-mail transféré, Braze enregistre un événement de clic.
- Ces événements sont attribués au profil du destinataire original, et non à la personne qui a reçu l'e-mail transféré, car le pixel de suivi et les liens sont liés au destinataire original.

Braze ne peut pas distinguer les ouvertures et les clics du destinataire original de ceux des personnes qui ont reçu une copie transférée. Il s'agit d'un comportement standard pour les pixels de suivi d'e-mails qui affecte tous les fournisseurs de services d'e-mailing.

Lors de l'analyse des indicateurs d'e-mails, gardez à l'esprit que l'activité de transfert peut contribuer aux compteurs d'ouvertures et de clics. Si vous constatez des taux d'engagement inhabituellement élevés ou une activité répétée provenant du même profil au fil du temps, le transfert peut être un facteur.

### Que se passe-t-il lorsqu'une Campaign ou un Canvas e-mail est arrêté ? {#what-happens-when-an-email-campaign-or-canvas-is-stopped}

Les utilisateurs ne peuvent plus entrer dans le Canvas, et aucun autre message n'est envoyé.

Pour les Campaigns et Canvas e-mail, le bouton d'arrêt n'interrompt pas immédiatement l'envoi. Lorsque les demandes d'envoi sont transmises, elles ne peuvent pas être empêchées d'atteindre l'utilisateur, ce qui peut se produire après un certain délai.

Bien que Braze n'envoie plus de demandes supplémentaires une fois la Campaign ou le Canvas arrêté, les analyses peuvent encore augmenter pendant que le fournisseur de services d'e-mailing termine le traitement des demandes déjà en cours.

### Pourquoi est-ce que je vois plus de _Clics totaux_ que d'_Ouvertures totales_ dans mes analyses d'e-mails ? {#why-am-i-seeing-more-_total-clicks_-than-_total-opens_-in-my-email-analytics}

_Ouvertures totales_ correspond au nombre de fois où l'e-mail a été ouvert par les utilisateurs, tandis que _Clics totaux_ correspond au nombre de fois où les utilisateurs ont cliqué dans l'e-mail distribué, y compris tout type de clics tels que les clics sur les liens. Vous pouvez voir plus de clics que d'ouvertures pour l'une des raisons suivantes :

- Les utilisateurs effectuent plusieurs clics dans le corps de l'e-mail au cours d'une seule ouverture.
- Les utilisateurs cliquent sur certains liens de l'e-mail dans le volet d'aperçu de leur téléphone. Dans ce cas, Braze enregistre cet e-mail comme cliqué mais non ouvert.
- Les utilisateurs rouvrent un e-mail qu'ils avaient précédemment prévisualisé.

### Pourquoi mes compteurs de clics sont-ils plus élevés que mon segment d'utilisateurs ayant cliqué ? {#why-are-my-click-counts-higher-than-my-segment-of-users-who-clicked}

Les analyses de Campaign affichent le nombre total d'événements de clics, tandis que les Segments renvoient le nombre d'utilisateurs uniques ayant effectué ces clics. Comme chaque utilisateur peut cliquer plusieurs fois, le total des clics dans les analyses est souvent supérieur au nombre d'utilisateurs ayant cliqué lorsque vous créez un Segment.

Par exemple, si 100 utilisateurs cliquent chacun sur un lien 3 fois, les analyses de Campaign affichent 300 clics totaux, mais un Segment filtré par « A cliqué sur l'e-mail » pour cette Campaign renvoie 100 utilisateurs.

### Pourquoi est-ce que je ne vois aucune ouverture ni aucun clic d'e-mail ? {#why-am-i-seeing-zero-email-opens-and-clicks}

Vous pouvez ne voir aucune ouverture ni aucun clic d'e-mail s'il y a une mauvaise configuration de votre domaine de suivi. Cela peut être dû à l'une des raisons suivantes :
- Il y a un problème SSL où les URL de suivi sont en `http` au lieu de `https`.
- Il y a un problème avec votre CDN où la chaîne user agent sur les événements d'ouverture, les événements de clic, ou les deux ne se renseignent pas.

### Pourquoi est-ce que je constate un comportement inhabituel d'ouverture ou de clic d'e-mail ? {#why-am-i-seeing-unusual-email-open-or-click-behavior}

Si vous remarquez des schémas inattendus dans vos indicateurs d'ouverture ou de clic d'e-mails, comme un seul utilisateur semblant cliquer sur chaque lien immédiatement, ou des ouvertures qui ne s'enregistrent pas comme prévu, examinez les causes courantes suivantes :

#### Le rognage de l'e-mail supprime le pixel de suivi {#email-clipping-removes-the-tracking-pixel}

Lorsqu'un e-mail est rogné par le fournisseur de messagerie du destinataire (par exemple, Gmail rogne les messages dépassant environ 102 Ko), le contenu en bas de l'e-mail peut être tronqué. Comme le pixel de suivi d'ouverture est généralement inséré en bas de l'e-mail, le rognage peut empêcher le suivi d'ouverture de fonctionner.

**Comment identifier :** Vérifiez si l'e-mail affiche un lien « Afficher le message en entier » ou similaire en bas. Vous pouvez utiliser [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) pour prévisualiser l'e-mail complet avec défilement et vérifier si le message est rogné.

**Comment résoudre :** Vous pouvez configurer Braze pour placer le pixel de suivi en haut de l'e-mail plutôt qu'en bas. Le déplacement du pixel de suivi peut affecter la façon dont certains clients de messagerie affichent votre HTML, donc testez vos e-mails dans Inbox Vision après avoir effectué ce changement. Notez que si le destinataire a désactivé les images, les ouvertures ne peuvent pas être suivies quel que soit l'emplacement du pixel.

#### Le pixel de suivi crée un espace blanc en haut de l'e-mail {#tracking-pixel-causes-white-gap-at-top-of-email}

Lorsque le pixel de suivi d'ouverture est positionné en haut d'un e-mail, une ligne blanche ou un espace visible peut apparaître en haut du corps de l'e-mail, en particulier sur les appareils mobiles.

**Comment identifier :** Dans Braze, allez dans **Paramètres** > **Préférences e-mail** et sélectionnez la section **Pixel de suivi d'ouverture**. Si **Déplacer pour SendGrid**, **Déplacer pour SparkPost** ou **Déplacer pour Amazon SES** est activé pour votre fournisseur d'envoi, le pixel est positionné en haut de votre HTML d'e-mail. Si vous remarquez un espace blanc ou une ligne en haut de votre e-mail rendu, ce paramètre peut en être la cause.

**Comment résoudre :** Désactivez le toggle **Déplacer pour SendGrid**, **Déplacer pour SparkPost** ou **Déplacer pour Amazon SES** approprié dans la section **Pixel de suivi d'ouverture** pour votre fournisseur d'envoi. Le pixel de suivi est généralement moins visible en bas d'un e-mail. Testez vos e-mails dans [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) après avoir modifié l'emplacement. Pour plus d'informations, consultez [Mettre à jour l'emplacement]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement).

#### Statistiques retardées ou clics sans ouvertures {#delayed-stats-or-clicks-without-opens}

Le suivi d'ouverture repose sur le fait que le destinataire charge l'e-mail avec les images activées. Dans certains cas, les statistiques peuvent sembler retardées ou des clics peuvent être enregistrés sans ouvertures correspondantes en raison de :

- Le destinataire consultait l'e-mail dans un volet d'aperçu sans l'ouvrir complètement, puis cliquant sur des liens directement depuis l'aperçu.
- Le client de messagerie ne chargeant pas les images (et donc le pixel de suivi) tant que le destinataire n'a pas interagi avec les liens.

#### Les logiciels de sécurité simulent des clics sur les liens {#security-software-simulates-link-clicks}

Certains outils de sécurité de messagerie d'entreprise (tels que Barracuda, Proofpoint et services similaires) analysent les e-mails entrants en cliquant automatiquement sur tous les liens du message pour vérifier qu'ils sont sûrs. Cela peut entraîner des événements de clic apparaissant en quelques secondes après l'envoi, souvent avec chaque lien de l'e-mail cliqué en succession rapide.

Ce comportement est plus courant avec les domaines de messagerie institutionnels (tels que les lycées, universités et environnements d'entreprise) et est plus probable lorsque votre domaine d'envoi diffère significativement de votre domaine de suivi. La configuration d'un [domaine de suivi personnalisé]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) peut réduire la fréquence de ces clics automatisés.

**Comment identifier :** Recherchez l'adresse IP de l'événement de clic (disponible dans les données Currents) dans un moteur de recherche. Si l'IP est associée à un fournisseur de sécurité connu (tel que Barracuda Networks), les clics sont probablement automatisés. Vous pouvez également voir un en-tête User-Agent cohérent à travers plusieurs clics automatisés.

Pour plus de contexte sur la façon dont l'analyse de sécurité affecte les indicateurs d'e-mails, consultez [Gérer les augmentations des taux de clics]({{site.baseurl}}/user_guide/channels/email/reporting).

### Quels sont les risques potentiels de déclencher des clics serveur ? {#what-are-the-potential-risks-of-triggering-server-clicks}

Certains éléments d'un e-mail, tels que des messages trop longs ou un nombre excessif de points d'exclamation, peuvent déclencher des réponses de sécurité des services de messagerie. Ces réponses peuvent affecter les rapports et la réputation IP et inciter les utilisateurs à se désabonner.

Pour les bonnes pratiques sur la gestion de ces réponses, consultez [Gérer les augmentations des taux de clics]({{site.baseurl}}/user_guide/channels/email/reporting).

### Braze peut-il suivre les liens de désabonnement comptabilisés dans l'indicateur « Désabonnements » ? {#can-braze-track-unsubscribe-links-counted-toward-the-unsubscribe-metric}

Braze suit les liens de désabonnement si le Liquid suivant est utilisé dans les e-mails : {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Pourquoi est-ce que je vois un nombre de désabonnements différent du nombre de clics sur mon lien de désabonnement ? {#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link}

S'il y a plus de _Désabonnements_ que d'utilisateurs ayant cliqué sur le lien de désabonnement dans le corps de l'e-mail, le [**List-unsubscribe**]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) explique souvent l'écart. Le list-unsubscribe est un chemin de désabonnement supplémentaire dans l'en-tête de l'e-mail (pas le lien dans le corps de votre message). Lorsqu'un utilisateur se désabonne de cette manière, cela est comptabilisé dans les _Désabonnements_ mais ne compte pas comme un clic sur l'URL de désabonnement suivie dans le corps.

Si le nombre total de clics sur le lien de désabonnement dans le corps est supérieur au nombre de _Désabonnements_, les utilisateurs peuvent avoir cliqué sur le lien plus d'une fois — par exemple, s'ils se désabonnent, se réabonnent, puis se désabonnent à nouveau, les analyses d'e-mails peuvent enregistrer plusieurs clics dans la répartition des clics.

Si un utilisateur clique sur le lien de désabonnement deux fois (par exemple, s'il s'est désabonné, s'est réabonné, puis s'est désabonné à nouveau), cela compte deux fois dans les analyses d'e-mails.

### Puis-je ajouter un lien « voir cet e-mail dans un navigateur » à mes e-mails ? {#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails}

Non. Braze n'offre pas cette fonctionnalité. En effet, une majorité croissante d'e-mails est ouverte sur des appareils mobiles et dans des clients de messagerie modernes, qui affichent les images et le contenu sans problème.

**Solution de contournement :** Pour obtenir le même résultat, vous pouvez héberger le contenu de votre e-mail sur une page de destination externe (telle que votre site web), qui peut ensuite être liée depuis la Campaign e-mail que vous créez en utilisant l'outil **Lien** lors de la modification du corps de l'e-mail.

### Braze convertit-il automatiquement les URL en texte brut ou les textes « www. » en liens ? {#does-braze-automatically-turn-plain-text-urls-or-www-text-into-links}

Non. Braze n'analyse pas votre message pour convertir le texte brut, tel que du texte commençant par `www.` ou ressemblant à une URL, en hyperliens. Seuls les liens que vous définissez avec des balises d'ancrage HTML (`<a href="...">`) sont traités via le rendu normal et les fonctionnalités de liens dans Braze.

Si un destinataire voit du texte brut affiché comme un lien cliquable, ce comportement provient généralement de son client de messagerie (par exemple, Gmail, Outlook ou Apple Mail). De nombreux clients détectent les chaînes ressemblant à des URL après la distribution du message et les transforment en liens sur l'appareil du destinataire. Braze ne contrôle pas ce comportement et ne peut pas le désactiver pour le destinataire.

Pour une apparence, un suivi et un style de lien prévisibles, utilisez des balises `<a href>` explicites plutôt que des URL en texte brut.

### Puis-je contrôler l'attribut `target` sur les liens des e-mails ? {#can-i-control-the-target-attribute-on-email-links}

Bien que vous puissiez définir l'attribut `target` (tel que `target="_blank"` ou `target="_top"`) sur les liens dans le HTML de votre e-mail, la plupart des clients de messagerie ignorent ou remplacent cet attribut. Par exemple, Gmail force effectivement un comportement similaire à `_blank` quel que soit ce que vous spécifiez.

Étant donné que le comportement des clients de messagerie varie, l'attribut `target` ne doit pas être utilisé de manière fiable pour contrôler comment les liens s'ouvrent. Pour des détails sur les clients de messagerie qui prennent en charge l'attribut `target`, consultez [caniemail.com](https://www.caniemail.com/features/html-target/).

### Pourquoi le signe plus `+` dans mon lien e-mail se transforme-t-il en espace ? {#why-does-a-plus-sign-in-my-email-link-turn-into-a-space}

Certains analyseurs de requêtes traitent un signe plus non encodé `+` comme un espace. Si votre URL de destination nécessite un signe plus dans un paramètre de requête, encodez-le en pourcentage comme `%2B` avant d'ajouter le lien à votre e-mail.

### Pourquoi mes utilisateurs sont-ils automatiquement désabonnés par un logiciel de sécurité d'e-mail ? {#why-are-my-users-being-auto-unsubscribed-by-email-security-software}

Certains outils de sécurité de messagerie d'entreprise (tels que Barracuda, Proofpoint et services similaires) pré-chargent ou analysent toutes les URL des e-mails entrants, y compris les liens de désabonnement. Cela peut provoquer des désabonnements involontaires lorsque l'outil de sécurité suit le lien de désabonnement en un clic (list-unsubscribe).

Pour atténuer ce problème :

- **Recommandez aux destinataires d'ajouter votre domaine d'envoi à la liste d'autorisation :** Travaillez avec les équipes informatiques des destinataires concernés pour ajouter votre domaine d'envoi et les domaines de suivi Braze à la liste d'autorisation de leur service de sécurité de messagerie.
- **Utilisez un centre de préférences :** Au lieu d'un lien de désabonnement direct, utilisez un [centre de préférences]({{site.baseurl}}/user_guide/channels/email/subscriptions) qui nécessite une interaction de l'utilisateur pour confirmer l'action de désabonnement. Les scanners de sécurité ne complètent généralement pas les formulaires à plusieurs étapes.
- **Examinez les journaux de désabonnement :** Vérifiez l'en-tête `User-Agent` et l'adresse IP dans les données d'événements de désabonnement de Currents pour identifier des schémas cohérents avec une analyse automatisée (tels que des en-têtes `User-Agent` cohérents à travers plusieurs désabonnements).

Pour plus de détails sur la façon dont l'analyse côté serveur peut affecter les indicateurs d'e-mails, consultez [Gérer les augmentations des taux de clics]({{site.baseurl}}/user_guide/channels/email/reporting).

### Pourquoi mon taux d'ouverture automatique a-t-il changé de manière inattendue ? {#why-has-my-machine-open-rate-changed-unexpectedly}

Les [ouvertures automatiques]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) sont déclenchées par des fonctionnalités de sécurité de messagerie telles que la protection de la confidentialité dans Apple Mail (MPP), qui pré-charge le contenu de l'e-mail (y compris le pixel de suivi) sans que l'utilisateur n'ouvre physiquement l'e-mail. Les taux d'ouverture automatique peuvent fluctuer en fonction de :

- Les changements dans la proportion de votre audience utilisant Apple Mail ou d'autres clients de messagerie avec des fonctionnalités de confidentialité activées.
- Les mises à jour des fonctionnalités de confidentialité des fournisseurs de messagerie ou des comportements de détection de bots.
- Les changements dans votre segmentation ou ciblage d'audience.

Les pourcentages d'ouverture automatique ne sont pas une mesure fiable de l'engagement réel. Pour une vue plus précise de la performance des e-mails, concentrez-vous sur les *Autres ouvertures* (ouvertures non automatiques) et les *Clics uniques*. Vous pouvez également comparer ces indicateurs dans le temps à l'aide du [tableau de bord des performances e-mail]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance).

### Pourquoi mes deep links ne fonctionnent-ils pas dans Gmail ? {#why-are-my-deep-links-not-working-in-gmail}

Gmail supprime tous les liens non HTTP/HTTPS des e-mails. Si votre deep link utilise un schéma personnalisé (tel que `myapp://path/to/content`), Gmail le supprimera et le lien ne fonctionnera pas pour les destinataires lisant l'e-mail dans Gmail. Il s'agit d'une limitation de Gmail, pas de Braze.

Pour contourner ce problème :

- **Utilisez les Universal Links (iOS) ou les App Links (Android).** Ceux-ci utilisent des URL standard `https://` qui ouvrent votre application lorsqu'elle est installée et renvoient vers une page web dans le cas contraire. Consultez [Universal Links et App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links) pour les instructions de configuration.
- **Utilisez un fournisseur de deep linking.** Des services comme [Branch](https://www.branch.io/) génèrent des deep links au format HTTP compatibles avec les clients de messagerie, y compris Gmail.
- **Configurez un endpoint de redirection.** Hébergez un endpoint `https://` sur votre serveur qui redirige vers l'URL au schéma personnalisé de votre application. Les clients de messagerie conserveront le lien `https://`, et la redirection se chargera d'ouvrir l'application.

### L'indicateur *Ouvertures uniques* inclut-il les *Ouvertures automatiques* ? {#does-the-unique-opens-metric-include-machine-opens}

Oui. *Ouvertures uniques* inclut les *Ouvertures automatiques*. Vous pouvez consulter les deux indicateurs dans la vue **Analyses de Campaign** et le **Générateur de rapports**.

Pour savoir comment cela affecte l'attribution dans le **Tableau de bord des conversions**, consultez [Pourquoi les totaux d'ouvertures d'e-mails ne correspondent-ils pas aux analyses de Campaign ?]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#why-dont-email-open-totals-match-campaign-analytics) dans [Résolution des problèmes]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#troubleshooting) sur la page du tableau de bord des conversions.

### Pourquoi mon volume de distribution d'e-mails ne correspond-il pas à mon volume d'envoi ? {#why-does-my-email-delivery-volume-not-match-my-send-volume}

Après l'envoi d'un e-mail, la boîte de réception du destinataire décide quand il est distribué. Les messages peuvent être reportés pendant des heures ou des jours en raison d'une boîte aux lettres pleine, d'un throttling du fournisseur de services d'e-mailing depuis une IP donnée, et de raisons similaires.

Lorsque des messages reportés sont distribués un jour calendaire différent du jour d'envoi, les _Distributions_ peuvent dépasser les _Envois_ pour la même période. Lorsque de nombreux reports aboutissent le même jour, les _Envois_ peuvent dépasser les _Distributions_ pour cette période.

### Pourquoi est-ce que je vois un avertissement m'invitant à inclure un lien de désabonnement alors que mon e-mail en contient déjà un ? {#why-am-i-seeing-a-warning-to-include-an-unsubscribe-link-when-my-email-already-has-one}

Cet avertissement peut persister pour les Campaigns dupliquées à partir d'une Campaign qui ne comportait pas de lien de désabonnement. Pour le supprimer :

- Pour les e-mails HTML, allez dans l'onglet **Texte brut**, puis sélectionnez **Régénérer à partir du HTML**.
- Après la duplication, dupliquez la variante, puis supprimez la variante originale. **Ne sélectionnez pas** la variante originale, sinon l'avertissement peut se reporter.

### Pourquoi un utilisateur a-t-il reçu un e-mail qu'il n'aurait pas dû recevoir ? {#why-did-a-user-receive-an-email-they-shouldnt-have}

La distribution peut sembler incorrecte même lorsque Braze s'est comporté conformément à la configuration. Examinez les points suivants :

- **Profils en double** partageant une boîte de réception (voir [Que se passe-t-il lorsqu'un e-mail est envoyé et que plusieurs profils partagent la même adresse e-mail ?](#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address)).
- **Listes initiateurs, destinataires de test ou adresses internes** inclus dans l'audience ou dans un envoi en CC/CCI.
- **Timing du Segment ou du Canvas :** l'utilisateur correspondait à l'audience ou à l'étape du Canvas au moment où Braze a évalué l'éligibilité, puis les attributs ou le statut d'abonnement ont changé avant qu'il ne lise le message.
- **Groupes d'abonnement :** l'utilisateur est resté abonné à un groupe ciblé par votre message même si son statut d'abonnement global suggérait le contraire.
- **Imports API ou fichier** qui ont mis à jour l'utilisateur après la segmentation mais avant que vous ne vous attendiez à ce que le changement s'applique.

Consultez le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), les journaux de modifications de la Campaign ou du Canvas, et la définition du Segment. Si vous ne parvenez toujours pas à expliquer l'envoi, contactez le support Braze avec les identifiants utilisateur, le `dispatch_id` (si disponible) et les horodatages.

### Pourquoi un utilisateur n'a-t-il pas reçu mon e-mail ? {#why-hasnt-a-user-received-my-email-message}

Il existe plusieurs raisons pour lesquelles un utilisateur ne reçoit pas un e-mail que vous vous attendiez à ce qu'il reçoive, notamment :

- Il n'était pas éligible pour recevoir l'e-mail.
- Son adresse e-mail est invalide ou n'existe pas.
- Il a peut-être manqué ou supprimé le message.
- Le message est peut-être dans son dossier spam.

{% alert tip %}
Un événement de distribution dans Braze signifie que l'e-mail a été accepté par le serveur du fournisseur de boîte de réception. Cependant, cela ne garantit pas que le message apparaisse dans la boîte de réception de l'utilisateur. Le fournisseur de boîte de réception peut diriger le message vers les spams ou, dans de rares cas, empêcher silencieusement l'affichage du message.
{% endalert %}

Utilisez les tableaux suivants pour cerner la cause.

#### L'e-mail n'a pas été envoyé {#the-email-wasnt-sent}

| Cause possible | Que vérifier |
|---|---|
| L'utilisateur n'était pas éligible pour la Campaign ou le Canvas | Vérifiez les paramètres **Target Audiences** (pour les Campaigns) ou **Target Audience** (pour les Canvas) dans les [paramètres]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) pour confirmer que l'utilisateur remplissait tous les filtres d'audience, critères de Segment et règles de distribution au moment de l'envoi. |
| Le message a été interrompu | Vérifiez le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) pour les raisons d'interruption, telles que les erreurs Liquid ou les champs requis manquants. |
| L'adresse e-mail de l'utilisateur était invalide ou manquante | Dans **Recherche d'utilisateurs**, vérifiez le profil de l'utilisateur pour confirmer qu'une adresse e-mail valide était enregistrée au moment de l'envoi. |
| L'adresse e-mail de l'utilisateur a précédemment subi un échec d'envoi définitif | Un échec d'envoi définitif marque l'adresse e-mail comme invalide et empêche les futurs envois à cette adresse. De même, si un destinataire marque votre e-mail comme spam, Braze n'envoie que des e-mails transactionnels à cet utilisateur, pas les Campaigns standard. Vérifiez l'onglet **Engagement** dans le profil de l'utilisateur. Pour plus d'informations, consultez [Adresses e-mail désabonnées]({{site.baseurl}}/user_guide/channels/email/subscriptions#unsubscribed-email-addresses) et [Rebonds et e-mails invalides]({{site.baseurl}}/user_guide/channels/email/subscriptions#bounces-and-invalid-emails). |
| L'utilisateur est désabonné de l'e-mail | Vérifiez le statut d'abonnement de l'utilisateur sous **Paramètres de contact** dans l'onglet **Engagement**. Braze n'envoie pas d'e-mails aux utilisateurs désabonnés. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cause de la non-expédition de l'e-mail" }

#### L'e-mail a été envoyé, mais n'est pas arrivé dans la boîte de réception {#the-email-was-sent-but-didnt-arrive-in-their-inbox}

| Cause possible | Que vérifier |
|---|---|
| Le fournisseur de boîte de réception (MBP) était injoignable | Un problème temporaire a empêché l'e-mail d'atteindre le MBP du destinataire. Cela se résout généralement avec les réessais. Les fournisseurs de services d'e-mailing réessaient les échecs provisoires d'envoi pendant un maximum de 72 heures. |
| Le MBP a rejeté l'e-mail | Le serveur de messagerie du destinataire a rejeté l'e-mail. Consultez le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) pour les détails du rebond. |
| Le MBP a silencieusement supprimé l'e-mail | Le MBP a accepté l'e-mail mais ne l'a pas affiché à l'utilisateur et n'a pas renvoyé de rebond. Ceci échappe au contrôle de Braze et ne peut pas être détecté dans les journaux Braze. |
| L'e-mail est allé dans le dossier spam | Le MBP a identifié le message comme spam et l'a dirigé vers le dossier spam ou courrier indésirable de l'utilisateur. Demandez à l'utilisateur de vérifier son dossier spam. |
| Le destinataire a un filtrage de messagerie personnalisé | L'utilisateur ou son administrateur informatique peut avoir configuré des règles de boîte de réception qui filtrent, redirigent ou suppriment les messages entrants. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cause de l'absence de l'e-mail dans la boîte de réception" }

### Comment puis-je retirer une adresse e-mail de la liste de rebonds ? {#how-can-i-remove-an-email-address-from-the-bounce-list}

Si une adresse e-mail valide apparaît comme invalide dans Braze (généralement après un échec d'envoi définitif de votre fournisseur de services d'e-mailing), utilisez l'endpoint [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces). Cela supprime l'adresse de votre liste de rebonds Braze et de la liste de rebonds maintenue par votre fournisseur d'e-mail. Braze reprend ensuite l'envoi à cette adresse.

Si l'adresse a été marquée comme spam plutôt qu'ayant subi un échec d'envoi définitif, utilisez plutôt l'endpoint [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam).

Pour plus d'informations, consultez [Rebonds et e-mails invalides]({{site.baseurl}}/user_guide/channels/email/subscriptions#bounces-and-invalid-emails) et [Supprimer une adresse e-mail de votre liste de rebonds ou de spam]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps#remove-an-email-address-from-your-bounce-or-spam-list).

### Comment résoudre les problèmes de livrabilité des e-mails ? {#how-do-i-troubleshoot-email-deliverability-issues}

Si vos e-mails sont retardés, reportés ou rejetés, consultez le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) pour les détails des rebonds et reports, puis identifiez où le problème se situe dans la chaîne de distribution. Les problèmes de livrabilité courants se répartissent en quatre catégories :

#### Lire les réponses de limitation de débit du fournisseur de services d'e-mailing {#reading-esp-rate-limit-responses}

Votre fournisseur de services d'e-mailing (ESP), tel qu'Amazon SES, SparkPost ou SendGrid, renvoie des codes de réponse SMTP lors de l'acceptation ou du report de messages. Les réponses de limitation de débit utilisent généralement des codes 4xx, qui indiquent des échecs temporaires :

- **421 :** Service temporairement indisponible, souvent en raison d'un volume élevé, de limites de connexion ou de contraintes de ressources serveur. Le message reste en file d'attente et votre ESP réessaie automatiquement la distribution.
- **429 :** Limite de débit API dépassée. Vous avez envoyé trop de requêtes dans la fenêtre de temps autorisée.
- **450 / 451 :** Report temporaire dû au volume ou aux connexions. Le serveur destinataire vous demande de ralentir.

Lorsque vous voyez ces codes dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) ou le tableau de bord de votre ESP, réduisez le volume d'envoi vers le domaine concerné et utilisez des intervalles de réessai progressivement plus longs. Continuer à plein volume lorsque le débit est limité peut transformer des reports temporaires en rejets permanents.

#### Limites de débit des fournisseurs de boîte de réception {#mailbox-provider-rate-limits}

Les fournisseurs de boîte de réception appliquent leurs propres limites de débit sur le courrier entrant, séparément des contrôles d'envoi de Braze. Ces limites peuvent être strictes et échappent à votre contrôle direct :

- Virgin Media / NTL (Royaume-Uni) : utilise une limitation de débit horaire qui déclenche des erreurs `421 4.1.1 MXIN503 Hourly ratelimit for your IP exceeded`. Ces limites peuvent affecter même les expéditeurs à faible volume. Elles sont appliquées au niveau de l'IP pour tous les expéditeurs partageant cette IP.
- Gmail, Yahoo, iCloud, Microsoft : chaque fournisseur a des seuils de throttling propriétaires basés sur votre réputation d'expéditeur, votre volume et vos schémas d'engagement.

Si vous rencontrez une limitation de débit spécifique à un fournisseur, envisagez de répartir vos envois sur une période plus longue ou de segmenter par fournisseur de boîte de réception pour étaler le volume de manière plus progressive. Vérifiez si votre liste de destinataires est concentrée chez un seul fournisseur — si la plupart des destinataires utilisent un seul domaine, échelonnez la distribution.

#### Retards d'e-mails d'entreprise dus à l'analyse antivirus {#corporate-email-delays-from-antivirus-scanning}

Les adresses e-mail professionnelles passent souvent par des passerelles de sécurité d'entreprise qui analysent les messages avant la distribution. Cela peut retarder les e-mails de 15 à 20 minutes ou plus, en particulier pour les messages avec :

- Des pièces jointes volumineuses
- Des liens vers des domaines inconnus
- Un contenu ressemblant à des schémas d'hameçonnage

Ces retards surviennent parce que les systèmes de sécurité mettent les messages en file d'attente pour une analyse comportementale dans des environnements sandbox isolés. Si un grand volume de courrier arrive simultanément, les messages s'accumulent en file d'attente pour l'analyse et le retard s'allonge. C'est un comportement normal de la sécurité de messagerie d'entreprise et il ne peut pas être contourné. Lors de l'envoi de messages urgents à des destinataires professionnels, tenez compte de cette fenêtre de traitement dans votre chronologie de communication.

#### Résolution des erreurs de limitation de débit Google 421 4.7.28 {#troubleshooting-google-421-4728-rate-limit-errors}

Gmail renvoie une erreur `421-4.7.28` lorsqu'il détecte un taux inhabituel d'e-mails non sollicités provenant de votre adresse IP, plage d'IP d'envoi, domaine SPF, domaine DKIM ou domaine d'URL. Il s'agit d'un throttle temporaire, pas d'un blocage permanent, mais cela signale que votre volume, votre vélocité ou votre réputation d'envoi ne répondent pas aux attentes actuelles de Gmail.

Si vous recevez cette erreur :

1. Suspendez immédiatement les envois non essentiels pendant 24 à 48 heures. Continuer à envoyer pendant un throttling aggrave le problème et peut conduire à des rejets permanents 550.
2. Confirmez que SPF, DKIM et DMARC sont correctement configurés et que votre en-tête From: est aligné avec votre authentification.
3. Consultez [Google Postmaster Tools](https://postmaster.google.com/) et le [Centre de livrabilité]({{site.baseurl}}/user_guide/analytics/dashboards/deliverability_center) de Braze (après avoir connecté Google Postmaster) pour le statut de conformité de votre domaine et les taux de plaintes spam. Votre taux de spam signalé par les utilisateurs doit rester en dessous de 0,1 % (le plafond absolu est de 0,3 %).
4. Après la pause, reprenez l'envoi à 10 à 20 % du volume précédent uniquement vers vos destinataires les plus engagés. Augmentez le volume lentement sur plusieurs semaines uniquement si aucune autre erreur 4xx ne survient.

Pour des conseils supplémentaires, consultez les [Lignes directrices de Google pour les expéditeurs en masse](https://support.google.com/mail/answer/81126).

### Comment optimiser les images dans Outlook ? {#how-can-i-optimize-images-in-outlook}

Outlook utilise souvent le moteur de rendu de Microsoft Word plutôt que le rendu standard du navigateur, ce qui peut provoquer un affichage incorrect des images ou ajouter des bordures autour des images. Ce même rendu spécifique au client affecte également [la façon dont le texte alternatif s'affiche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text) dans les différents clients de messagerie.

Si les images s'affichent plus larges que leur largeur attendue dans Outlook, ajoutez le CSS suivant à l'image :

```css
max-width: 100%;
```

Par exemple :

```html
<img src="your-image.png" style="max-width: 100%;" alt="Description">
```

Vous pouvez également encapsuler du contenu pour le masquer dans Outlook desktop en utilisant des commentaires conditionnels :

```html
<!--[if !mso]><!-- -->
<span>Content hidden in Outlook desktop</span>
<!--<![endif]-->
```

### Puis-je utiliser des images SVG ou WebP dans mes e-mails ? {#can-i-use-svg-or-webp-images-in-my-email-messages}

Les images SVG ne sont pas recommandées pour les e-mails en raison de la prise en charge limitée par les clients de messagerie. Gmail et plusieurs autres fournisseurs de messagerie majeurs n'affichent pas les images SVG, ce qui peut entraîner des images cassées ou manquantes pour les destinataires. Le WebP n'est pas pris en charge de manière cohérente par tous les clients.

Utilisez plutôt des formats largement pris en charge tels que PNG ou JPEG pour que les images s'affichent de manière fiable.

### Puis-je intégrer des vidéos dans les e-mails ? {#can-i-embed-videos-in-emails}

Les vidéos intégrées ne sont pas nativement prises en charge par de nombreux clients de messagerie populaires tels que Gmail, Outlook et Yahoo. En conséquence, les éléments vidéo intégrés peuvent ne pas s'afficher comme prévu ou ne pas apparaître du tout. De plus, intégrer une vidéo directement dans un e-mail peut augmenter significativement la taille de l'e-mail, ce qui augmente la probabilité que le message soit marqué comme spam.

À la place, vous pouvez créer un GIF ou une image statique qui ressemble à une vidéo dans un lecteur vidéo, puis lier cette image à votre vidéo. Lorsque les utilisateurs cliquent sur l'image, ils sont dirigés vers la vidéo hébergée sur votre site web ou une plateforme vidéo. Braze prend également en charge l'intégration avec [Playable]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/playable), qui fournit du contenu vidéo optimisé avec lecture automatique dans les clients de messagerie pris en charge.

### Les variables Liquid assignées dans une partie du compositeur de messages peuvent-elles être utilisées dans une autre ? {#can-liquid-variables-assigned-in-one-part-of-the-message-composer-be-used-in-another}

Non. Chaque partie de l'e-mail (objet, corps, en-têtes, boutons, etc.) est générée séparément, de sorte que le Liquid assigné dans un champ n'est pas disponible dans un autre. Assignez les variables dans chaque champ qui en a besoin.

### Mon modèle d'e-mail est manquant. Où est-il ? {#my-email-template-is-missing-where-is-it}

Tout d'abord, confirmez que vous disposez des [permissions utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) nécessaires pour voir les modèles. Pour consulter les modèles d'e-mails enregistrés, allez dans **Contenu** > **E-mail**. Vous pouvez filtrer les modèles par statut et type (HTML ou glisser-déposer).

### Dois-je enregistrer des domaines pour les e-mails de relais ou masqués ? {#do-i-need-to-register-domains-for-relay-or-masked-emails}

Le [relais d'e-mail privé d'Apple]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/email_private_relay_apple_SSO) vous demande d'enregistrer vos domaines d'envoi dans le portail développeur Apple pour éviter les rebonds. Le service Shielded Email de Google ne nécessite pas de processus d'enregistrement ou d'ajout à la liste d'autorisation de domaine manuel.

### Puis-je ajouter des hyperliens dans les lignes d'objet ou les accroches d'e-mails ? {#can-i-add-hyperlinks-in-email-subject-lines-or-preheaders}

Non. L'ajout d'hyperliens dans les lignes d'objet d'e-mails n'est pas pris en charge par les fournisseurs de boîte de réception. Bien que certains fournisseurs analysent automatiquement les lignes d'objet et convertissent les adresses physiques, les dates ou les heures en liens cliquables, cela se fait automatiquement sur l'appareil du destinataire et échappe au contrôle de Braze (ou de tout autre fournisseur de services d'e-mailing).

De même, l'ajout d'hyperliens dans l'accroche n'est pas pris en charge dans le secteur de l'e-mail.

Si vous avez besoin d'une fonctionnalité similaire à du contenu cliquable dans la ligne d'objet ou la zone d'accroche, envisagez d'utiliser les [promotions Gmail]({{site.baseurl}}/user_guide/channels/email/html_editor/gmail_promotions_tab) pour ajouter des annotations interactives à vos e-mails pour les utilisateurs Gmail.

### Que signifie la raison de rebond `unable to get mx info` ou `failed to get IPs from PTR record` ? {#what-does-the-bounce-reason-unable-to-get-mx-info-or-failed-to-get-ips-from-ptr-record-mean}

Dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), une raison de rebond similaire à ce qui suit indique un problème de résolution de la configuration de messagerie du domaine destinataire (le domaine après le `@` dans l'adresse), et non un problème lié à la composition du message Braze :

Les causes habituelles incluent :

- Des **enregistrements MX** manquants, incorrects ou inaccessibles pour ce domaine
- Des noms d'hôte de messagerie entrants qui ne se résolvent pas ou qui échouent aux vérifications **PTR (DNS inversé)** attendues par l'infrastructure de réception
- Des domaines invalides ou mal saisis dans l'adresse e-mail

**Prochaines étapes :**

- Confirmez l'orthographe de l'adresse et du domaine.
- Si l'adresse est correcte, contactez le propriétaire de la boîte aux lettres ou l'équipe informatique de ce domaine.
- Demandez-leur d'auditer les enregistrements MX et les enregistrements DNS associés, y compris les enregistrements PTR de leurs serveurs de messagerie, auprès de leur fournisseur DNS.

Les autres destinataires ne sont généralement pas affectés. Pour savoir comment les échecs provisoires d'envoi apparaissent dans les rapports, consultez [Échec provisoire d'envoi]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce).

### Pourquoi est-ce que je reçois une alerte de spam lorsque j'envoie un e-mail depuis Braze à moi-même ? {#why-do-i-get-a-spam-alert-when-sending-an-email-from-braze-to-myself}

Si vous envoyez un e-mail de test depuis Braze à votre propre adresse e-mail et voyez un avertissement de spam ou d'hameçonnage, tel que « le domaine d'envoi est similaire au domaine de votre entreprise, mais nous ne le reconnaissons pas », il s'agit d'une fonctionnalité de sécurité anti-hameçonnage courante, et non d'une erreur de configuration Braze.

Cette alerte apparaît généralement lorsque le domaine d'envoi de l'e-mail correspond au domaine du destinataire (par exemple, les deux sont `@votreentreprise.com`). Les systèmes de sécurité de messagerie signalent ceci parce que les fraudeurs usurpent souvent des domaines qui ressemblent au domaine de l'entreprise du destinataire.

Pour vérifier que votre e-mail est correctement configuré :

1. Affichez le message original (en-têtes bruts de l'e-mail) dans votre client de messagerie.
2. Vérifiez que les authentifications SPF, DKIM et DMARC passent toutes avec succès.
3. Si les trois passent, votre envoi d'e-mail Braze est correctement configuré.

Pour empêcher cette alerte d'apparaître :

Demandez à votre équipe informatique d'ajouter votre domaine d'envoi Braze et vos adresses IP à la liste d'autorisation dans les services de sécurité de messagerie ou la passerelle de messagerie de votre entreprise. Cela indique à votre système de sécurité de faire confiance aux e-mails provenant de votre infrastructure d'envoi Braze.