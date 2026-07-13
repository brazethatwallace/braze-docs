---
nav_title: Modifier votre campagne après le lancement
article_title: Modifier votre campagne après le lancement
page_order: 1
tool: Campaigns
page_type: reference
description: "Cet article de référence donne un aperçu des conséquences de la modification de certains aspects d'une campagne après son lancement, y compris la manière dont les changements se propagent pour les campagnes de messages in-app."

---

# Modifier votre campagne après le lancement {#edit-your-campaign-after-launch}

> Cet article donne un aperçu des conséquences de la modification de certains aspects d'une campagne après son lancement.

## Pourquoi arrêter une campagne avant de la modifier {#risks-of-editing-live}

{% alert important %}
Braze recommande d'arrêter une campagne avant d'y apporter des modifications, plutôt que de la modifier pendant qu'elle est en cours. Modifier une campagne en cours sans l'arrêter au préalable peut entraîner un comportement inattendu, y compris le fait que des utilisateurs reçoivent le message deux fois.
{% endalert %}

Lorsqu'une campagne est lancée, tous les utilisateurs éligibles sont mis en file d'attente pour recevoir le message. Cependant, un utilisateur n'est marqué comme ayant reçu la campagne que lorsque le message est effectivement distribué, et non lorsqu'il est mis en file d'attente. Si vous modifiez une campagne en cours sans l'arrêter au préalable, Braze remet en file d'attente les utilisateurs éligibles pour la version mise à jour alors que la file d'attente d'origine est encore en cours de traitement. Les utilisateurs qui n'ont pas encore reçu le message d'origine se retrouveront dans les deux files d'attente, ce qui peut entraîner :

- Des utilisateurs recevant la campagne deux fois (la version d'origine et la version mise à jour), même si la rééligibilité est désactivée.
- La version d'origine de la campagne étant toujours distribuée aux utilisateurs de la première file d'attente.
- Des comptages d'audience inattendus dans les analyses de la campagne.

Cela est plus susceptible de se produire avec des campagnes ciblant une large audience et planifiées pour un envoi immédiat, car une grande file d'attente d'utilisateurs est traitée en même temps. Pour les campagnes à livraison par événement avec des déclencheurs progressifs (comme les événements d'inscription), le risque est plus faible car seul un petit nombre d'utilisateurs est généralement en file d'attente à un moment donné.

Pour effectuer des modifications en toute sécurité, arrêtez d'abord la campagne, puis modifiez la campagne arrêtée ou [dupliquez-la](#making-immediate-changes) avec vos modifications.

## Arrêter votre campagne {#stopping-your-campaign}

Pour arrêter une campagne, ouvrez la page **Détails de la campagne** et sélectionnez **Arrêter la campagne**. Lorsqu'une campagne est arrêtée :

- Les messages dont l'envoi est planifié seront annulés.
- Les tests A/B dont le test initial a déjà été envoyé seront définitivement annulés.
- Les événements liés aux messages déjà envoyés (par exemple, les clics d'ouverture) continueront d'être suivis.

Pour relancer votre campagne, sélectionnez **Reprendre**. Votre campagne reprendra l'envoi des messages et des tests A/B, mais les messages manqués ne seront ni renvoyés ni replanifiés.

### Arrêter votre campagne pendant l'envoi {#stopping-your-campaign-during-sending}

Pour les campagnes avec une audience plus large et des limites de débit, Braze partitionne et planifie des lots de messages à envoyer à différents moments. Lorsqu'une campagne est arrêtée, les envois ne sont pas annulés immédiatement. Ils sont annulés lorsqu'ils commencent à s'exécuter et détectent que la campagne a été arrêtée.

Par exemple, si vous lancez une campagne e-mail avec limite de débit, que vous la mettez en pause pendant quelques heures, puis que vous la reprenez, tous les messages qui étaient planifiés pour être envoyés pendant les heures de pause sont annulés et ne seront jamais envoyés. Les messages restants planifiés après la reprise de la campagne continuent d'être envoyés. Si la rééligibilité est activée pour la campagne, les utilisateurs peuvent redevenir éligibles pour recevoir la campagne en plus des messages qui étaient déjà en file d'attente avant l'arrêt de la campagne.

## Campagnes de messages in-app {#in-app-message-campaigns}

Contrairement aux notifications push ou aux e-mails, les messages in-app sont distribués aux appareils au début de la session et mis en cache localement jusqu'à ce que le déclencheur se déclenche. Lorsque vous modifiez une campagne de messages in-app en cours — par exemple en l'arrêtant, en définissant une [date de fin]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/create#choose-a-trigger), en activant **Réévaluer l'éligibilité de la campagne avant l'affichage**, en mettant à jour le contenu, en changeant le déclencheur du message ou en modifiant l'audience cible — la configuration mise à jour se propage lorsque les appareils récupèrent les déclencheurs au début de leur prochaine session.

Voici ce à quoi vous pouvez vous attendre :

- Les appareils qui n'ont pas démarré de nouvelle session depuis votre modification peuvent continuer à utiliser la configuration précédente jusqu'à ce qu'ils synchronisent à nouveau les déclencheurs.
- Les appareils qui démarrent une session après votre modification reçoivent la dernière configuration.

### Arrêter un lancement erroné {#stop-a-mistaken-launch}

Si vous avez lancé la mauvaise campagne de messages in-app, sélectionnez **Arrêter la campagne** sur la page **Détails de la campagne**. C'est le moyen le plus rapide d'empêcher les nouvelles sessions de télécharger le message. Les utilisateurs qui ont déjà mis en cache le payload avant l'arrêt de la campagne peuvent encore le voir lorsqu'ils remplissent les conditions du déclencheur, jusqu'à ce que leur appareil synchronise les déclencheurs mis à jour lors d'une session ultérieure.

[L'archivage]({{site.baseurl}}/user_guide/messaging/governance/archiving) et les dates de fin suivent les mêmes règles de propagation : ils arrêtent la distribution pour les synchronisations futures mais ne suppriment pas les messages déjà mis en cache sur les appareils. Si vous devez examiner, dupliquer ou modifier la campagne, arrêtez-la d'abord et archivez-la plus tard lorsque vous avez terminé.

### Limiter les distributions obsolètes {#limit-stale-deliveries}

Sélectionnez **Réévaluer l'éligibilité de la campagne avant l'affichage** dans les paramètres de distribution de votre campagne afin que Braze confirme l'appartenance à l'audience et le statut de la campagne juste avant chaque affichage. Cela permet d'éviter les impressions après l'arrêt, l'archivage ou le dépassement de la date de fin d'une campagne. Vous pouvez activer ou désactiver ce paramètre après le lancement, mais il suit les mêmes règles de propagation que les autres modifications : les appareils ne reçoivent la configuration mise à jour qu'à leur prochaine synchronisation des déclencheurs.

Pour en savoir plus, consultez [Choisir les utilisateurs à cibler]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/create#choose-users-to-target) et [Pourquoi ma campagne de messages in-app archivée continue-t-elle à générer des impressions de messages in-app ?]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#why-is-my-archived-in-app-message-campaign-still-delivering-in-app-message-impressions).

## Campagnes déclenchées {#triggered-campaigns}

Toutes les modifications apportées aux campagnes à livraison par événement et aux campagnes déclenchées par API prennent effet immédiatement pour les envois à venir.

Si ces campagnes ont été déclenchées mais pas encore envoyées (par exemple, une campagne à livraison par événement avec un délai d'un jour est modifiée pendant cette période de délai), consultez les recommandations suivantes pour les campagnes planifiées.

### Campagnes planifiées {#scheduled-campaigns}

Si vous devez apporter des modifications à une campagne après son lancement, prenez note des éléments suivants lors de la modification de votre campagne afin de vérifier que vos changements produisent les effets souhaités.

### Contenu du message {#message-content}

Toute modification du contenu du message (y compris les titres, les corps de texte et les images) prend effet immédiatement après l'enregistrement pour tous les envois de messages à venir. Il n'est pas possible de modifier le contenu des messages qui ont déjà été envoyés.

### Planification et audience {#scheduling-and-audience}

Si vous modifiez l'heure d'envoi planifiée ou l'audience de votre campagne, ces changements sont immédiatement reflétés dans la campagne.

#### Considérations {#considerations}

Si votre campagne utilise le timing intelligent ou la distribution selon le fuseau horaire local, les modifications de l'heure d'envoi planifiée ne seront pas prises en compte si la modification est effectuée moins de 24 heures avant l'heure d'envoi initiale. Voici pourquoi :

- **Timing intelligent :** Braze commence à calculer l'heure d'envoi optimale à minuit, heure de Samoa. Si cette heure est déjà passée, le traitement du message aura déjà commencé. Pour en savoir plus, consultez la section [Timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing).
- **Distribution selon le fuseau horaire local :** La modification d'une campagne en fuseau horaire local planifiée moins de 24 heures à l'avance ne modifiera pas la planification du message. Pour en savoir plus, consultez la section [Comment planifier une campagne en fuseau horaire local ?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign).

### Débit d'envoi {#send-rate}

Lorsque vous utilisez une limite de débit, Braze « planifie » vos messages par tranches d'une minute. Si vous souhaitez modifier le débit d'envoi des messages, suivez le processus ci-dessous pour effectuer des changements immédiats.

#### Mettre en pause des campagnes avec limitation du débit de distribution {#pausing-campaigns-with-delivery-speed-rate-limiting}

Lorsque vous mettez en pause une campagne qui utilise la [limitation du débit de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting), Braze répartit les envois sur des créneaux d'une minute. **Reprendre** ne renvoie pas les messages des créneaux qui ont été annulés pendant la pause de la campagne, et tous les messages ne sont pas nécessairement envoyés lorsque la campagne est reprise.

Si certains utilisateurs n'ont pas reçu de messages parce que la campagne était en pause, dupliquez la campagne et ciblez uniquement ces utilisateurs plutôt que de compter sur **Reprendre** pour distribuer les messages manqués.

## Effectuer des changements immédiats {#making-immediate-changes}

Si vous avez besoin que les changements prennent effet immédiatement, procédez comme suit :

1. Arrêtez la campagne concernée.
2. Dupliquez la campagne.
3. Apportez vos modifications à la campagne dupliquée.

{% alert important %}
Cela réinitialise l'éligibilité des personnes qui ont déjà reçu la campagne d'origine. Vous devrez donc peut-être filtrer la campagne dupliquée pour cibler uniquement les personnes qui n'ont pas reçu la campagne d'origine.
{% endalert %}

## Enregistrer des brouillons de campagnes actives {#campaign-drafts}

Les brouillons sont idéaux pour apporter des modifications à grande échelle à des campagnes actives. En créant un brouillon, vous pouvez tester les changements prévus avant votre prochain lancement.

{% alert note %}
Une campagne ne peut avoir qu'un seul brouillon à la fois. De plus, les analyses ne sont pas disponibles tant que les modifications du brouillon n'ont pas été lancées.
{% endalert %}

Pour créer un brouillon, procédez comme suit :

1. Accédez à votre campagne active.
2. Apportez vos modifications.
3. Sélectionnez **Enregistrer en tant que brouillon**. Notez qu'après avoir créé un brouillon, vous ne pouvez pas modifier la campagne active tant que vous n'avez pas lancé ou supprimé votre brouillon.

![Un brouillon d'une campagne active avec une option pour afficher la campagne active.]({% image_buster /assets/img/campaign_draft.png %})

Pendant que vous modifiez le brouillon, vous pouvez également consulter la campagne active depuis l'en-tête du brouillon de campagne ou le pied de page des analyses de la campagne.

Pour revenir à une campagne active, sélectionnez **Modifier le brouillon** depuis la vue des analyses ou la vue de la campagne active.

### Priorisation des messages in-app {#in-app-message-prioritization}

La priorité des messages in-app sera mise à jour immédiatement (avant le lancement du brouillon) lorsque vous sélectionnez **Définir la priorité exacte** et que vous spécifiez la priorité par rapport à d'autres campagnes ou Canvas.