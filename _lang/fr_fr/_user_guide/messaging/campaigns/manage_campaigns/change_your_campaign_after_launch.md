---
nav_title: Modifier votre campagne après le lancement
article_title: Modifier votre campagne après le lancement
page_order: 1
tool: Campaigns
page_type: reference
description: "Cet article de référence donne un aperçu des conséquences de la modification de certains aspects d'une campagne après son lancement."

---

# Modifier votre campagne après le lancement {#edit-your-campaign-after-launch}

> Cet article donne un aperçu des conséquences de la modification de certains aspects d'une campagne après son lancement.

## Arrêter votre campagne {#stopping-your-campaign}

Pour arrêter une campagne, ouvrez la page **Détails de la campagne** et sélectionnez **Arrêter la campagne**. Lorsqu'une campagne est arrêtée :

- Les messages dont l'envoi est planifié seront annulés.
- Les tests A/B dont le test initial a déjà été envoyé seront définitivement annulés.
- Les événements liés aux messages déjà envoyés (par exemple, les clics d'ouverture) continueront d'être suivis.

Pour relancer votre campagne, sélectionnez **Reprendre**. Votre campagne reprendra l'envoi des messages et des tests A/B, mais les messages manqués ne seront ni renvoyés ni replanifiés.

### Arrêter votre campagne pendant l'envoi {#stopping-your-campaign-during-sending}

Pour les campagnes avec une audience plus large et des limites de débit, Braze partitionne et planifie des lots de messages à envoyer à différents moments. Lorsqu'une campagne est arrêtée, les envois ne sont pas annulés immédiatement. Ils sont annulés lorsqu'ils commencent à s'exécuter et détectent que la campagne a été arrêtée.

Par exemple, si vous lancez une campagne e-mail avec limite de débit, que vous la mettez en pause pendant quelques heures, puis que vous la reprenez, tous les messages qui étaient planifiés pour être envoyés pendant les heures de pause sont annulés et ne seront jamais envoyés. Les messages restants planifiés après la reprise de la campagne continuent d'être envoyés. Si la rééligibilité est activée pour la campagne, les utilisateurs peuvent redevenir éligibles pour recevoir la campagne en plus des messages qui étaient déjà en file d'attente avant l'arrêt de la campagne.

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

- **Timing intelligent :** Braze commence à calculer l'heure d'envoi optimale à minuit, heure de Samoa. Si cette heure est déjà passée, le traitement du message aura déjà commencé. Pour en savoir plus, consultez la section [Timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/).
- **Distribution selon le fuseau horaire local :** La modification d'une campagne en fuseau horaire local planifiée moins de 24 heures à l'avance ne modifiera pas la planification du message. Pour en savoir plus, consultez la section [Comment planifier une campagne en fuseau horaire local ?]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign).

### Débit d'envoi {#send-rate}

Lorsque vous utilisez une limite de débit, Braze « planifie » vos messages par tranches d'une minute. Si vous souhaitez modifier le débit d'envoi des messages, suivez le processus ci-dessous pour effectuer des changements immédiats.

#### Mettre en pause des campagnes avec limitation du débit de distribution {#pausing-campaigns-with-delivery-speed-rate-limiting}

Lorsque vous mettez en pause une campagne qui utilise la [limitation du débit de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-speed-rate-limiting), Braze répartit les envois sur des créneaux d'une minute. **Reprendre** ne renvoie pas les messages des créneaux qui ont été annulés pendant la pause de la campagne.

Les messages soumis à une limite de débit ne sont annulés que si la campagne est toujours en pause au moment de leur envoi planifié. Qu'un message soit envoyé ou non après la reprise dépend du moment où vous avez mis la campagne en pause et de la durée de cette pause.

Par exemple :

1. Vous mettez la campagne en pause à 13 h.
2. Un message soumis à une limite de débit est planifié pour être envoyé à 13 h 05.
   - Si vous reprenez avant 13 h 05, le message est envoyé.
   - Si vous reprenez après 13 h 05, le message est annulé pendant la pause et n'est pas envoyé.

Si certains utilisateurs n'ont pas reçu de messages parce que la campagne était en pause pendant leur créneau d'envoi planifié, dupliquez la campagne et ciblez uniquement ces utilisateurs plutôt que de compter sur **Reprendre** pour distribuer les messages manqués.

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