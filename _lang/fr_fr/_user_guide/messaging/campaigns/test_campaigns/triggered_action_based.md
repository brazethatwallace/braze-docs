---
nav_title: Campagnes déclenchées par API et par action
article_title: Tester les campagnes déclenchées par API et par action
page_order: 2
page_type: reference
description: "Cet article de référence explique comment tester les campagnes déclenchées par API et par action."

---

# Campagnes déclenchées par API et par action {#api-triggered-and-action-based-campaigns}

> Lors de la configuration de campagnes, il est toujours recommandé de tester vos messages avant de les lancer. Cet article de référence explique comment créer un segment d'essai qui vous permettra d'inspecter les requêtes API, les payloads et de consulter les journaux de livrabilité.

## Étape 1 : Créer un segment d'essai {#step-1-create-a-test-user-segment}

La seule façon de tester le déclenchement d'une campagne via l'API ou un événement personnalisé est de mettre la campagne en production. Lors du déploiement d'une nouvelle campagne, nous recommandons vivement d'ajouter un segment d'essai pour vérifier la livrabilité. Cela constitue un filet de sécurité : même si une campagne est envoyée accidentellement, elle ne sera adressée qu'aux utilisateurs internes.

1. **Importer des utilisateurs test**<br>Les utilisateurs test peuvent être importés dans Braze via un fichier CSV ou une requête ponctuelle par lot via [Postman]({{site.baseurl}}/api/postman_collection). Lors de l'importation de ces utilisateurs, nous recommandons de définir un attribut personnalisé sur leur profil (par exemple `internal_test_user: true`) qui pourra être utilisé pour créer un segment de test. <br><br>
2. **Ajouter les utilisateurs test en tant qu'utilisateurs test reconnus par Braze**<br>[Marquer vos utilisateurs test comme utilisateurs test reconnus par Braze]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups) dans le tableau de bord vous donne accès à une journalisation détaillée pour chaque utilisateur, vous permettant d'inspecter les requêtes API, leurs payloads et de consulter les journaux de livrabilité. Ces journaux peuvent vous aider à déterminer s'il y a eu des problèmes lors de la livraison des campagnes aux utilisateurs finaux. <br><br>
3. **Créer un segment**<br>Pour créer un segment d'essai, créez un segment d'utilisateurs dont l'attribut personnalisé `internal_test_user` est défini sur `true`. Ce segment pourra être supprimé une fois la campagne mise en production.

## Étape 2 : Tester les envois {#step-2-testing-sends}

Ensuite, vous pouvez effectuer un envoi test depuis le tableau de bord de Braze ou utiliser Inbox Vision (e-mail uniquement) pour prévisualiser la disposition pendant que la campagne est encore en mode brouillon. Vous pouvez ensuite envoyer la campagne à votre segment d'essai pour vérifier qu'elle se comporte comme prévu. Que la campagne soit déclenchée par API ou par action, utilisez Postman pour envoyer une requête ponctuelle à l'API Braze afin de déclencher la campagne.

## Étape 3 : Utiliser les journaux Braze pour inspecter les résultats entrants {#step-3-use-braze-logging-to-inspect-inbound-results}

Utilisez les journaux Braze pour résoudre les problèmes de déclenchement, d'envoi et d'événements.
- Le [journal des événements utilisateur]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) affiche le payload brut de la requête de déclenchement API, l'événement personnalisé déclenchant la campagne, ainsi que toutes les propriétés de déclencheur ou d'événement associées.
- Le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) consigne les erreurs et vous aide à comprendre pourquoi un message particulier n'a peut-être pas été livré.

## Étape 4 : Supprimer le segment d'essai et déployer la campagne {#step-4-remove-the-test-segment-and-roll-out-the-campaign}

Une fois que le message se déclenche et s'affiche correctement, avec tous les liens cliqués correctement enregistrés, vous pouvez supprimer le segment et mettre à jour la campagne. Si vous préférez repartir de zéro afin que les quelques impressions des utilisateurs test ne soient pas comptabilisées, vous pouvez dupliquer la campagne et la relancer sans le segment d'essai.