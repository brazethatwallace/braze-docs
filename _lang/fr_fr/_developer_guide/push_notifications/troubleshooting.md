---
page_order: 10.9
nav_title: Résolution des problèmes
article_title: Résolution des problèmes des notifications push pour le SDK Braze
description: "Diagnostiquez les problèmes de distribution et d'affichage des notifications push à l'aide d'un index de symptômes, d'un parcours d'investigation standard et de vérifications spécifiques au SDK par plateforme."
channel:
  - push notifications
---

# Résolution des problèmes des notifications push {#troubleshoot-push-notifications}

> Utilisez cette page pour diagnostiquer les problèmes de distribution et d'affichage des notifications push sur un appareil. Pour les vérifications de distribution côté tableau de bord (statut d'abonnement, segments, plafonds), consultez [Résolution des problèmes des notifications push]({{site.baseurl}}/user_guide/channels/push/troubleshooting).

Avant de déboguer, ajoutez-vous en tant qu'[utilisateur test]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users) et consultez [Envoi de messages de test]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages).

## Commencez ici : identifiez votre symptôme {#start-here-match-your-symptom}

Trouvez le comportement que vous observez dans le tableau, puis suivez les étapes de la section correspondante. Si vous ne savez pas quelle section s'applique, utilisez le [parcours d'investigation standard](#standard-investigation-path).

| Symptôme | Aller à |
| --- | --- |
| Notification push non reçue sur une plateforme | Sélectionnez l'onglet de votre SDK dans [Résolution des problèmes spécifiques à la plateforme](#platform-specific-troubleshooting) |
| Les sauts de ligne autour des étiquettes Liquid semblent incorrects lors de l'enregistrement | [Sauts de ligne dans les notifications push](#push-linebreaks) |
| Vérifications de distribution dans le tableau de bord (abonnement, segment, plafonds) | [Résolution des problèmes des notifications push]({{site.baseurl}}/user_guide/channels/push/troubleshooting) |
| Le deep link d'une notification push ne s'ouvre pas correctement | [Résolution des problèmes de deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting) |
| Codes d'erreur courants des notifications push | [Messages d'erreur courants des notifications push]({{site.baseurl}}/user_guide/channels/push/push_error_codes) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptôme du SDK push" }

## Parcours d'investigation standard {#standard-investigation-path}

Utilisez ce flux de travail pour chaque incident de notification push. Commencez à l'étape 1.

1. Confirmez que l'appareil dispose d'un jeton push valide et que l'autorisation push est accordée dans les paramètres de l'appareil.
2. Dans le tableau de bord, confirmez que l'utilisateur test correspond au [Segment]({{site.baseurl}}/user_guide/channels/push/troubleshooting#segment) de la Campaign ou du Canvas et qu'il ne fait pas partie du [groupe de contrôle]({{site.baseurl}}/user_guide/channels/push/troubleshooting#control-group-status).
3. Envoyez une [notification push de test]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages) à l'appareil de test.
4. [Activez la journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduisez le problème et consultez les conseils spécifiques à la plateforme dans votre [onglet SDK](#platform-specific-troubleshooting).
5. Si le problème persiste, contactez l'[Assistance Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) en fournissant les journaux détaillés, la plateforme, la version du SDK et l'ID de la Campaign ou du Canvas.

## Les clics push ne sont pas enregistrés {#push-clicks-not-logged}

- Assurez-vous d'avoir suivi les [étapes d'intégration push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling).
- Braze ne gère pas les notifications push reçues silencieusement au premier plan (comportement push au premier plan par défaut avant le framework `UserNotifications`). Cela signifie que les liens ne seront pas ouverts et que les clics push ne seront pas enregistrés. Si votre application n'a pas encore intégré le framework `UserNotifications`, Braze ne gérera pas les notifications push lorsque l'état de l'application est `UIApplicationStateActive`. Assurez-vous que votre application ne retarde pas les appels aux [méthodes de gestion push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling) ; sinon, le SDK Swift pourrait traiter les notifications push comme des événements push silencieux au premier plan et ne pas les gérer.

## Sauts de ligne dans les notifications push {#push-linebreaks}

Lors de la rédaction de notifications push avec des étiquettes Liquid, les sauts de ligne adjacents aux étiquettes Liquid sont automatiquement supprimés avant l'envoi du message. Dans le [compositeur de notifications push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message), ces sauts de ligne sont réajoutés afin que votre message reste lisible pendant la modification. Si vous remarquez des sauts de ligne autour des étiquettes Liquid lors de l'enregistrement de votre message, il s'agit d'un comportement attendu.