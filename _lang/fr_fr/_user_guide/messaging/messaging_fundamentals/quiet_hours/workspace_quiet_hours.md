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

- **Une fenêtre par canal :** Chaque canal prend en charge une seule fenêtre d'heures calmes au niveau de l'espace de travail, définie par une heure de début et une heure de fin.
- **Fuseau horaire local :** Comme les heures calmes au niveau des Campaigns et des Canvas, les heures calmes de l'espace de travail s'appliquent dans le fuseau horaire local de chaque destinataire, et non dans celui de votre entreprise.
- **Rétention pour distribution ultérieure :** Un message qui serait normalement envoyé pendant la fenêtre est retenu et distribué plus tard, ou abandonné, selon le type de Campaign. Consultez [Ce qui arrive à un message retenu](#what-happens-to-a-held-message). Les heures calmes ne modifient jamais le contenu des messages. Elles n'affectent que le timing.
- **Durée maximale de la fenêtre :** Une fenêtre d'heures calmes ne peut pas dépasser 20 heures. Cette limite existe pour éviter de suspendre accidentellement tous les envois sur un canal (par exemple, en définissant la même valeur pour l'heure de début et l'heure de fin).

### Canaux pris en charge {#supported-channels}

Vous pouvez définir une fenêtre d'heures calmes au niveau de l'espace de travail pour n'importe lequel des canaux suivants :

- Content Cards
- E-mail
- KakaoTalk
- LINE
- Notification push
   - Cela couvre toutes les plateformes push de votre espace de travail. Il n'est pas possible de définir des heures calmes différentes pour chaque plateforme (par exemple, iOS vs. Android).
- SMS/MMS/RCS
- Webhook
- WhatsApp

## Prérequis {#prerequisites}

Pour créer ou mettre à jour les heures calmes d'un espace de travail, vous devez disposer de la permission « Edit Quiet Hours ».

| Permission | Accès |
|---|---|
| Edit Quiet Hours | Créer et mettre à jour les heures calmes de l'espace de travail. |
| View Quiet Hours | Consulter la configuration des heures calmes de l'espace de travail sans la modifier. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permissions relatives aux heures calmes" }

Les permissions existantes de modification des Campaigns et des Canvas ne sont pas affectées. Les utilisateurs disposant de ces permissions peuvent toujours modifier les heures calmes au niveau d'une Campaign ou d'un Canvas.

## Configurer les heures calmes de l'espace de travail {#set-up-workspace-quiet-hours}

### Configurer la fenêtre de l'espace de travail {#configure-the-workspace-window}

1. Accédez à **Paramètres** > **Heures calmes**.
2. Sélectionnez **Ajouter des heures calmes**.
3. Sélectionnez un canal, puis saisissez une heure de début et une heure de fin. Un canal ne peut avoir qu'une seule fenêtre d'heures calmes d'espace de travail à la fois.
4. (Facultatif) Pour ajouter un autre canal, sélectionnez à nouveau **Ajouter des heures calmes**.
5. Enregistrez vos modifications.

![La page des paramètres d'heures calmes de l'espace de travail avec des fenêtres d'heures calmes pour SMS et e-mail, chacune avec une heure de début et une heure de fin, ainsi qu'une option Ajouter des heures calmes.]({% image_buster /assets/img/quiet_hours/workspace_quiet_hours_settings.png %}){: style="max-width:90%;"}

Les mises à jour des heures calmes de l'espace de travail sont enregistrées dans un journal des modifications, indiquant qui a effectué la modification et quand, car ce paramètre affecte chaque Campaign et Canvas sur le canal.

### Appliquer ou remplacer dans une Campaign ou un Canvas {#apply-or-override-in-a-campaign-or-canvas}

Après l'enregistrement, la fenêtre d'heures calmes de l'espace de travail apparaît dans l'éditeur de Campaign et de Canvas pour chaque canal disposant d'une fenêtre. Vous pouvez conserver la valeur par défaut de l'espace de travail, ou la désactiver et appliquer une fenêtre spécifique à la Campaign ou au Canvas, de la même manière que vous désactivez une limite de fréquence au niveau de l'espace de travail.

1. Sélectionnez **Appliquer les heures calmes pour cette campagne** (ou l'équivalent Canvas).
2. Sélectionnez **Utiliser les heures calmes de l'espace de travail** pour appliquer la valeur par défaut de l'espace de travail, ou sélectionnez **Utiliser des heures calmes personnalisées** pour définir une fenêtre spécifique à la Campaign ou au Canvas.
3. Pour consulter la fenêtre de l'espace de travail pour les canaux utilisés, sélectionnez **Afficher les heures calmes**.

![La section Heures calmes d'une Campaign avec l'option Appliquer les heures calmes pour cette campagne sélectionnée, Utiliser les heures calmes de l'espace de travail sélectionné, et la fenêtre d'espace de travail e-mail de 20 h 00 à 8 h 00 développée.]({% image_buster /assets/img/quiet_hours/campaign_workspace_quiet_hours.png %}){: style="max-width:70%;"}

## Priorité : heures calmes de l'espace de travail versus heures calmes d'une Campaign ou d'un Canvas {#precedence-workspace-versus-campaign-or-canvas-quiet-hours}

Pour toute Campaign ou tout Canvas donné, un seul paramètre d'heures calmes est actif à la fois (heures calmes de l'espace de travail, fenêtre spécifique à la Campaign ou au Canvas, ou aucune). Une fenêtre d'heures calmes au niveau de la Campaign ou du Canvas prend toujours le pas sur la valeur par défaut de l'espace de travail.

La façon dont les heures calmes s'appliquent dépend également du moment où la Campaign ou le Canvas a été créé :

- **Campaigns et Canvas existants** (créés avant l'activation des heures calmes de l'espace de travail) : si la Campaign ou le Canvas ne possède pas sa propre fenêtre d'heures calmes, la fenêtre d'heures calmes de l'espace de travail pour ce canal s'applique automatiquement. S'il possède déjà une fenêtre au niveau de la Campaign ou du Canvas, cette fenêtre continue de s'appliquer.
- **Nouvelles Campaigns et nouveaux Canvas :** lorsque vous créez une Campaign ou un Canvas, vous pouvez utiliser la valeur par défaut des heures calmes de l'espace de travail, définir une fenêtre personnalisée au niveau de la Campaign ou du Canvas, ou désactiver entièrement les heures calmes.

| Configuration présente | Heures calmes appliquées |
|---|---|
| La Campaign ou le Canvas possède sa propre fenêtre d'heures calmes | La fenêtre au niveau de la Campaign ou du Canvas s'applique. Les heures calmes de l'espace de travail sont ignorées pour cette Campaign ou ce Canvas. |
| La Campaign ou le Canvas ne possède pas de fenêtre d'heures calmes propre, et une fenêtre d'heures calmes de l'espace de travail existe pour le canal utilisé | La fenêtre d'heures calmes de l'espace de travail s'applique automatiquement. Cela inclut les Campaigns et Canvas existants qui n'ont jamais configuré d'heures calmes. |
| La Campaign ou le Canvas a été exclu des heures calmes | Aucune heure calme ne s'applique. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Priorité des heures calmes" }

### Ce qui arrive à un message retenu {#what-happens-to-a-held-message}

Ce qui arrive à un message tombant dans une fenêtre d'heures calmes dépend du type de distribution de la Campaign ou du Canvas :

- **Campaigns et Canvas déclenchés par une action :** le comportement de repli peut être **Abandonner le message** ou **Envoyer au prochain créneau disponible**, les mêmes options que pour les heures calmes au niveau de la Campaign ou du Canvas.
- **Campaigns planifiées avec une heure d'envoi fixe :** le comportement de repli est **Abandonner le message**. Braze ne retarde pas un envoi à heure fixe jusqu'au prochain créneau disponible, car cela pourrait concentrer un grand volume de messages dans une fenêtre d'envoi compressée une fois les heures calmes terminées.
- **Campaigns utilisant le timing intelligent :** aucun comportement de repli distinct n'est nécessaire. Braze intègre déjà la fenêtre d'heures calmes de l'espace de travail dans le calcul de l'heure d'envoi optimale pour chaque utilisateur, de sorte que les messages ne sont pas planifiés à l'intérieur de la fenêtre.
- **Campaigns déclenchées par API et Campaigns API :** le comportement de repli est **Abandonner le message** par défaut.

### Campaigns déclenchées par API et Campaigns API {#api-triggered-and-api-campaigns}

Les heures calmes fonctionnent différemment pour les Campaigns déclenchées par API et les Campaigns API.

#### Campaigns déclenchées par API {#api-triggered-campaigns}

Les Campaigns déclenchées par API suivent les mêmes options d'heures calmes que les autres Campaigns dans le tableau de bord. Vous pouvez utiliser la valeur par défaut des heures calmes de l'espace de travail, définir une fenêtre personnalisée au niveau de la Campaign, ou désactiver les heures calmes dans la configuration de la Campaign. Il n'existe pas de paramètre API `ignore_workspace_quiet_hours` pour les envois déclenchés par API.

Pour les envois déclenchés par API planifiés avec `at_optimal_time`, les heures calmes de l'espace de travail sont déjà intégrées dans le calcul de l'heure d'envoi optimale, de manière similaire au [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing).

#### Campaigns API {#api-campaigns}

Les Campaigns API ne peuvent pas utiliser les heures calmes au niveau de la Campaign. Seule la fenêtre d'heures calmes de l'espace de travail s'applique. Pour envoyer pendant cette fenêtre, incluez le paramètre optionnel `ignore_workspace_quiet_hours` dans votre requête API.

### Exclusions {#exclusions}

Les éléments suivants ne sont jamais retenus par les heures calmes de l'espace de travail, quel que soit le canal :

- Messages e-mail transactionnels
- Réponses automatiques SMS (par exemple, les réponses aux mots-clés `STOP` ou `HELP`)
- Envois de test et envois de groupe initiateur

## Autres considérations {#other-considerations}

- **Envois planifiés selon le fuseau horaire de l'entreprise :** les heures calmes de l'espace de travail sont basées sur le fuseau horaire local de chaque destinataire, mais l'heure d'envoi d'une campagne planifiée peut être définie selon le fuseau horaire de votre entreprise. Ce décalage signifie qu'une heure d'envoi qui semble correcte dans le fuseau de l'entreprise pourrait tout de même tomber pendant les heures calmes pour certains destinataires. Vérifiez les détails des heures calmes de l'espace de travail affichés dans l'éditeur de campagne avant l'envoi.
- **Distribution après la fin des heures calmes :** si une large audience a été mise en attente pendant la fenêtre, ces messages peuvent tous devenir éligibles à l'envoi en même temps à la fermeture de la fenêtre. Anticipez cette situation lorsqu'un canal a une audience étendue et une longue fenêtre d'heures calmes.
- **Indépendant de la limite de fréquence et de la limitation du débit :** les heures calmes de l'espace de travail s'appliquent indépendamment de la limite de fréquence et de la limitation du débit. Un message qui passe ces contrôles peut tout de même être retenu par les heures calmes, et un message retenu par les heures calmes est toujours évalué par rapport aux limites de débit une fois qu'il est prêt à être envoyé.
- **Le timing intelligent remplace les heures calmes de l'espace de travail pour les Campaigns multicanales déclenchées par une action. Pour limiter les heures d'envoi, définissez plutôt des heures calmes personnalisées.

## Paramètres associés {#related-settings}

- [Heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) : la version existante de cette fonctionnalité, configurée par Campaign et par Canvas. Les heures calmes de l'espace de travail ne la remplacent pas ; elles définissent la valeur par défaut qui s'applique lorsqu'une Campaign ou un Canvas ne configure pas sa propre fenêtre.
- [Timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) : calcule un horaire d'envoi optimal par utilisateur. Lorsqu'il est activé en parallèle des heures calmes de l'espace de travail, celles-ci sont prises en compte dans le calcul.
- [Limitation du débit et limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) : contrôles de distribution distincts qui s'appliquent indépendamment des heures calmes.