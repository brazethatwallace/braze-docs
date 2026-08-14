---
nav_title: Heures calmes de l'espace de travail
article_title: Heures calmes de l'espace de travail
page_order: 4
page_type: reference
description: "Cet article de référence couvre les heures calmes de l'espace de travail, la manière dont Braze gère les messages pendant la période calme et l'interaction entre les heures calmes et le timing intelligent."
---

# Heures calmes de l'espace de travail {#workspace-quiet-hours}

> Les heures calmes de l'espace de travail vous permettent de définir une fenêtre d'heures calmes par défaut pour un canal de communication à l'échelle de votre espace de travail. Chaque campagne et Canvas envoyé sur ce canal respecte automatiquement cette fenêtre, ce qui vous évite de configurer les heures calmes sur chaque campagne ou Canvas individuellement.

Les heures calmes de l'espace de travail sont distinctes des heures calmes au niveau des campagnes et des Canvas, qui s'appliquent toujours lorsque vous les configurez. Utilisez les heures calmes de l'espace de travail pour le cas par défaut (par exemple, une exigence de conformité pour tous les envois SMS). Conservez les heures calmes au niveau des campagnes et des Canvas pour les exceptions.

{% alert important %}
Les heures calmes de l'espace de travail sont actuellement disponibles en accès anticipé. Les options de configuration peuvent changer avant la disponibilité générale. Contactez votre équipe de compte Braze pour demander l'accès.
{% endalert %}

## Fonctionnement {#how-it-works}

- **Une fenêtre par canal :** chaque canal prend en charge une seule fenêtre d'heures calmes de l'espace de travail, définie par une heure de début et une heure de fin.
- **Fuseau horaire local :** comme les heures calmes au niveau des campagnes et des Canvas, les heures calmes de l'espace de travail s'appliquent dans le fuseau horaire local de chaque destinataire, et non dans celui de votre entreprise.
- **Rétention pour envoi ultérieur :** un message qui serait normalement envoyé pendant la fenêtre est retenu et envoyé plus tard, ou abandonné, selon le type de campagne. Voir [Que se passe-t-il pour un message retenu](#what-happens-to-a-held-message). Les heures calmes ne modifient jamais le contenu du message. Elles n'affectent que le timing.
- **Durée maximale de la fenêtre :** une fenêtre d'heures calmes ne peut pas dépasser 20 heures. Cette limite existe pour éviter de suspendre accidentellement tous les envois sur un canal (par exemple, en définissant la même valeur pour l'heure de début et l'heure de fin).

### Canaux pris en charge {#supported-channels}

Vous pouvez définir une fenêtre d'heures calmes de l'espace de travail pour l'un des canaux suivants :

- Content Cards
- E-mail
- KakaoTalk
- LINE
- Notification push
   - Cela couvre toutes les plateformes push de votre espace de travail. Il n'est pas possible de définir des heures calmes différentes pour des plateformes individuelles (par exemple, iOS vs. Android).
- SMS/MMS/RCS
- Webhook
- WhatsApp

## Prérequis {#prerequisites}

Pour créer ou mettre à jour les heures calmes de l'espace de travail, vous avez besoin de la permission « Edit Quiet Hours ».

| Permission | Accès |
|---|---|
| Edit Quiet Hours | Créer et mettre à jour les heures calmes de l'espace de travail. |
| View Quiet Hours | Consulter la configuration des heures calmes de l'espace de travail sans la modifier. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permissions des heures calmes" }

Les permissions existantes de modification des campagnes et des Canvas ne sont pas affectées. Les utilisateurs disposant de ces permissions peuvent toujours modifier les heures calmes au niveau des campagnes ou des Canvas.

## Configurer les heures calmes de l'espace de travail {#set-up-workspace-quiet-hours}

### Configurer la fenêtre de l'espace de travail {#configure-the-workspace-window}

1. Accédez à **Paramètres** > **Heures calmes**.
2. Sélectionnez **Ajouter des heures calmes**.
3. Sélectionnez un canal, puis saisissez une heure de début et une heure de fin. Un canal ne peut avoir qu'une seule fenêtre d'heures calmes de l'espace de travail à la fois.
4. (Facultatif) Pour ajouter un autre canal, sélectionnez à nouveau **Ajouter des heures calmes**.
5. Enregistrez vos modifications.

![La page de paramètres des heures calmes de l'espace de travail avec des fenêtres d'heures calmes pour SMS et e-mail, chacune avec une heure de début et une heure de fin, et une option Ajouter des heures calmes.]({% image_buster /assets/img/quiet_hours/workspace_quiet_hours_settings.png %}){: style="max-width:90%;"}

Les mises à jour des heures calmes de l'espace de travail sont enregistrées dans un journal des modifications, incluant l'auteur de la modification et la date, car ce paramètre affecte chaque campagne et Canvas sur le canal.

### Appliquer ou remplacer dans une campagne ou un Canvas {#apply-or-override-in-a-campaign-or-canvas}

Après l'enregistrement, la fenêtre d'heures calmes de l'espace de travail apparaît dans l'éditeur de campagne et de Canvas pour chaque canal disposant d'une fenêtre. Vous pouvez conserver la valeur par défaut de l'espace de travail, ou la désactiver et appliquer une fenêtre spécifique à la campagne ou au Canvas, de la même manière que vous désactivez une limite de fréquence au niveau de l'espace de travail.

1. Sélectionnez **Appliquer les heures calmes pour cette campagne** (ou l'équivalent Canvas).
2. Sélectionnez **Utiliser les heures calmes de l'espace de travail** pour appliquer la valeur par défaut de l'espace de travail, ou sélectionnez **Utiliser des heures calmes personnalisées** pour définir une fenêtre spécifique à la campagne ou au Canvas.
3. Pour consulter la fenêtre de l'espace de travail pour les canaux utilisés, sélectionnez **Voir les heures calmes**.

![La section Heures calmes d'une campagne avec l'option Appliquer les heures calmes pour cette campagne sélectionnée, Utiliser les heures calmes de l'espace de travail sélectionné, et la fenêtre e-mail de l'espace de travail de 20h00 à 8h00 développée.]({% image_buster /assets/img/quiet_hours/campaign_workspace_quiet_hours.png %}){: style="max-width:70%;"}

## Priorité : espace de travail versus heures calmes de campagne ou Canvas {#precedence-workspace-versus-campaign-or-canvas-quiet-hours}

Pour toute campagne ou Canvas donné, un seul paramètre d'heures calmes est actif à la fois (heures calmes de l'espace de travail, fenêtre spécifique à la campagne ou au Canvas, ou aucun). Une fenêtre d'heures calmes au niveau de la campagne ou du Canvas prend toujours le pas sur la valeur par défaut de l'espace de travail.

La manière dont les heures calmes s'appliquent dépend également du moment où la campagne ou le Canvas a été créé :

- **Campagnes et Canvas existants** (créés avant l'activation des heures calmes de l'espace de travail) : si la campagne ou le Canvas ne dispose pas de sa propre fenêtre d'heures calmes, la fenêtre d'heures calmes de l'espace de travail pour ce canal s'applique automatiquement. S'il dispose déjà d'une fenêtre au niveau de la campagne ou du Canvas, cette fenêtre continue de s'appliquer.
- **Nouvelles campagnes et nouveaux Canvas :** lorsque vous créez une campagne ou un Canvas, vous pouvez utiliser la valeur par défaut des heures calmes de l'espace de travail, définir une fenêtre personnalisée au niveau de la campagne ou du Canvas, ou désactiver entièrement les heures calmes.

| Configuration présente | Heures calmes appliquées |
|---|---|
| La campagne ou le Canvas dispose de sa propre fenêtre d'heures calmes | La fenêtre au niveau de la campagne ou du Canvas s'applique. Les heures calmes de l'espace de travail sont ignorées pour cette campagne ou ce Canvas. |
| La campagne ou le Canvas ne dispose pas de sa propre fenêtre d'heures calmes, et une fenêtre d'heures calmes de l'espace de travail existe pour le canal utilisé | La fenêtre d'heures calmes de l'espace de travail s'applique automatiquement. Cela inclut les campagnes et Canvas existants qui n'ont jamais configuré d'heures calmes. |
| La campagne ou le Canvas a désactivé les heures calmes | Aucune heure calme ne s'applique. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Priorité des heures calmes" }

### Que se passe-t-il pour un message retenu {#what-happens-to-a-held-message}

Ce qui arrive à un message tombant dans une fenêtre d'heures calmes dépend du type de réception de la campagne ou du Canvas :

- **Campagnes et Canvas déclenchés par une action :** le comportement de repli peut être soit **Abandonner le message**, soit **Envoyer au prochain créneau disponible**, les mêmes options que pour les heures calmes au niveau des campagnes et des Canvas.
- **Campagnes planifiées avec une heure d'envoi fixe :** le comportement de repli est **Abandonner le message**. Braze ne retarde pas un envoi à heure fixe jusqu'au prochain créneau disponible, car cela pourrait concentrer un grand volume de messages dans une fenêtre d'envoi compressée une fois les heures calmes terminées.
- **Campagnes utilisant le timing intelligent :** aucun comportement de repli séparé n'est nécessaire. Braze intègre déjà la fenêtre d'heures calmes de l'espace de travail dans le calcul de l'heure d'envoi optimale pour chaque utilisateur, de sorte que les messages ne sont pas planifiés à l'intérieur de la fenêtre.
- **Campagnes déclenchées par API et campagnes API :** le comportement de repli est **Abandonner le message** par défaut.

### Campagnes déclenchées par API et campagnes API {#api-triggered-and-api-campaigns}

Les heures calmes fonctionnent différemment pour les campagnes déclenchées par API et les campagnes API.

#### Campagnes déclenchées par API {#api-triggered-campaigns}

Les campagnes déclenchées par API suivent les mêmes options d'heures calmes que les autres campagnes dans le tableau de bord. Vous pouvez utiliser la valeur par défaut des heures calmes de l'espace de travail, définir une fenêtre personnalisée au niveau de la campagne, ou désactiver les heures calmes dans la configuration de la campagne. Il n'existe pas de paramètre API `ignore_workspace_quiet_hours` pour les envois déclenchés par API.

Pour les envois planifiés déclenchés par API utilisant `at_optimal_time`, les heures calmes de l'espace de travail sont déjà intégrées dans le calcul de l'heure d'envoi optimale, de manière similaire au [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing).

#### Campagnes API {#api-campaigns}

Les campagnes API ne peuvent pas utiliser les heures calmes au niveau de la campagne. Seule la fenêtre d'heures calmes de l'espace de travail s'applique. Pour envoyer pendant cette fenêtre, incluez le paramètre optionnel `ignore_workspace_quiet_hours` dans votre requête API.

### Exclusions {#exclusions}

Les éléments suivants ne sont jamais retenus par les heures calmes de l'espace de travail, quel que soit le canal :

- Messages transactionnels et messages couverts par un SLA
- Réponses automatiques SMS (par exemple, les réponses aux mots-clés `STOP` ou `HELP`)
- Envois de test et envois de groupe initiateur

## Autres considérations {#other-considerations}

- **Envois planifiés dans le fuseau horaire de l'entreprise :** les heures calmes de l'espace de travail sont basées sur le fuseau horaire local de chaque destinataire, mais l'heure d'envoi d'une campagne planifiée peut être définie dans le fuseau horaire de votre entreprise. Ce décalage signifie qu'une heure d'envoi qui semble correcte dans le fuseau horaire de l'entreprise pourrait tout de même tomber dans les heures calmes pour certains destinataires. Vérifiez les détails des heures calmes de l'espace de travail affichés dans l'éditeur de campagne avant l'envoi.
- **Réception après la fin des heures calmes :** si une large audience a été retenue pendant la fenêtre, ces messages peuvent devenir éligibles à l'envoi simultanément à la fermeture de la fenêtre. Anticipez cette situation lorsqu'un canal a une audience large et une longue fenêtre d'heures calmes.
- **Indépendance par rapport à la limite de fréquence et à la limitation du débit :** les heures calmes de l'espace de travail s'appliquent indépendamment de la limite de fréquence et de la limitation du débit. Un message qui passe ces contrôles peut tout de même être retenu par les heures calmes, et un message retenu par les heures calmes est toujours évalué par rapport aux limites de débit une fois qu'il est prêt à être envoyé.
- **Le timing intelligent prend le pas sur les heures calmes de l'espace de travail pour les campagnes multicanales déclenchées par une action. Pour limiter les heures d'envoi, définissez plutôt des heures calmes personnalisées.

## Paramètres associés {#related-settings}

- [Heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) : la version existante de cette fonctionnalité, par campagne et par Canvas. Les heures calmes de l'espace de travail ne la remplacent pas ; elles définissent la valeur par défaut qui s'applique lorsqu'une campagne ou un Canvas ne configure pas sa propre fenêtre.
- [Timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) : calcule une heure d'envoi optimale par utilisateur. Lorsqu'il est activé en parallèle des heures calmes de l'espace de travail, les heures calmes sont intégrées dans ce calcul.
- [Limitation du débit et limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) : contrôles de réception distincts qui s'appliquent indépendamment des heures calmes.