---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes liés aux Canvas
page_order: 7
page_type: reference
description: "Diagnostiquez les problèmes d'entrée, d'envoi et d'analyse des Canvas à l'aide d'un parcours d'investigation standard, d'un index des symptômes et de liens vers l'historique des messages et le tableau de bord de diagnostic des messages."
tool: Canvas
---

# Résolution des problèmes liés aux Canvas {#troubleshoot-canvases}

> Utilisez cette page pour diagnostiquer les problèmes d'entrée, d'envoi et d'analyse des Canvas. Pour les définitions et les approfondissements, consultez la [FAQ Canvas]({{site.baseurl}}/user_guide/messaging/canvas/faqs).

{% alert note %}
Les journaux de l'**historique des messages** et du **diagnostic des messages** sont disponibles pendant **30 jours** à compter de l'événement. Contactez l'[Assistance Braze]({{site.baseurl}}/braze_support) dans ce délai si vous avez besoin d'aide pour investiguer un incident spécifique.
{% endalert %}

## Commencez ici : identifiez votre symptôme {#start-here-match-your-symptom}

| Symptôme | Aller à |
| --- | --- |
| Un utilisateur n'est pas entré dans le Canvas | [L'utilisateur n'est pas entré dans le Canvas](#user-didnt-enter-the-canvas) |
| Un utilisateur est entré mais n'a pas reçu de message ou d'étape | [L'utilisateur n'a pas reçu de message ou d'étape Canvas](#user-didnt-receive-a-canvas-message-or-step) |
| Personne ou moins d'utilisateurs que prévu ne sont entrés | [Entrées Canvas faibles ou nulles](#low-or-zero-canvas-entries) |
| Les envois ou distributions sont inférieurs à l'audience estimée | [Envois inférieurs aux attentes](#lower-sends-than-expected) |
| Les analyses du Canvas semblent incorrectes (groupe de contrôle, conversions, zéro envoi) | [Incohérences dans les analyses Canvas](#canvas-analytics-mismatches) |
| Le Canvas ne s'enregistre pas ou l'éditeur se fige | [Problèmes d'éditeur et d'enregistrement](#editor-and-save-issues) |
| J'ai arrêté le Canvas mais des messages ont quand même été envoyés | [Comportement d'un Canvas arrêté](#stopped-canvas-behavior) |
| Erreur « Too many Canvas branches » au lancement | [Erreur « Too many Canvas branches »](#too-many-canvas-branches-error) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptôme Canvas" }

## Parcours d'investigation standard {#standard-investigation-path}

Utilisez ce flux de travail pour investiguer un problème concernant un utilisateur spécifique ou un envoi agrégé. Commencez à l'étape 1 pour chaque incident.

1. Confirmez que le Canvas est actif (ni brouillon, ni arrêté, ni archivé).
2. Confirmez que la planification d'entrée (fenêtre planifiée, fuseau horaire, déclencheur par événement ou entrée déclenchée par API) correspond au moment où vous attendez l'entrée des utilisateurs.
3. Vérifiez l'historique des messages d'un utilisateur en accédant à **Audience** > **Rechercher des utilisateurs**, en ouvrant le profil et en sélectionnant **Historique des messages** (30 derniers jours).
   - Si aucun enregistrement n'existe pour l'heure d'envoi attendue, le problème concerne l'entrée, pas le message. Consultez [L'utilisateur n'est pas entré dans le Canvas](#user-didnt-enter-the-canvas).
4. Vérifiez le **journal des modifications** du Canvas et les journaux des modifications de tous les segments utilisés dans le ciblage. Confirmez que l'audience, les étapes ou les paramètres d'envoi n'ont pas été modifiés pendant l'incident.
5. Vérifiez les résultats agrégés sur la page d'analyse du Canvas en ouvrant le [tableau de bord de diagnostic des messages]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) et en examinant les raisons d'abandon et de rejet.
   - Si vous voyez un résultat que vous ne reconnaissez pas, consultez [Résultats d'abandon]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes) dans la documentation de diagnostic.
   - Si une étape affiche zéro entrée (et non zéro envoi), vérifiez le type d'étape précédente ([Parcours d'actions]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), [Délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) ou [Arbre décisionnel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)).
6. Si vous êtes toujours bloqué, contactez l'[Assistance Braze]({{site.baseurl}}/braze_support) dans les 30 jours avec l'ID du Canvas, les ID des utilisateurs concernés, les horodatages (avec fuseau horaire) et les captures d'écran de l'historique des messages ou du diagnostic des messages.

Avant le lancement, utilisez [Envoyer des Canvas de test]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) et [Prévisualiser les parcours utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) pour valider votre configuration.

## L'utilisateur n'est pas entré dans le Canvas {#user-didnt-enter-the-canvas}

**Symptôme :** Un utilisateur n'est pas entré dans le Canvas au moment attendu, ou moins d'utilisateurs sont entrés que ne le suggèrent vos événements déclencheurs.

Les utilisateurs doivent correspondre à l'**audience cible** avant que Braze n'évalue le déclencheur d'entrée (sauf pour les déclencheurs de [changement d'attribut]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Un déclencheur seul ne garantit pas l'entrée si l'utilisateur ne faisait pas partie de l'audience au moment de l'évaluation.

La rééligibilité et la réentrée sont des contrôles distincts dans [Sélection des contrôles d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) :

- **Rééligibilité :** Détermine si un utilisateur est autorisé à entrer à nouveau dans le Canvas après en être sorti (fenêtre temporelle et paramètre **Autoriser les utilisateurs à entrer à nouveau dans le Canvas**).
- **Réentrée :** Détermine si un utilisateur actuellement dans le Canvas peut entrer dans un parcours concurrent.

Un utilisateur peut être rééligible mais bloqué parce qu'il est encore dans le Canvas, ou peut en être sorti mais se trouver encore en dehors de la fenêtre de rééligibilité. Vérifiez les deux paramètres lorsqu'un utilisateur ne parvient pas à entrer à nouveau dans un Canvas.

Vérifiez les points suivants :

- **Planification d'entrée et fuseau horaire :** Confirmez que le Canvas était actif et que l'utilisateur a effectué le déclencheur pendant la [fenêtre d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule).
- **Audience cible au moment de l'évaluation :** Consultez les journaux des modifications des segments et des filtres. La [recherche d'utilisateurs]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) peut afficher un faux positif pour certains types de filtres (par exemple, les attributs de date au format chaîne de caractères).
- **Plafonds d'entrée :** Les [entrées maximales]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) ou les plafonds d'audience peuvent avoir été atteints.
- **Groupe de contrôle global :** Les utilisateurs du [groupe de contrôle global]({{site.baseurl}}/user_guide/audience/global_control_group) n'entrent pas dans les Canvas d'envoi de messages.
- **Groupe de contrôle du Canvas :** Les utilisateurs affectés au groupe de contrôle du Canvas à l'entrée ne reçoivent pas les messages de variante. L'affectation à la variante se fait à l'entrée, pas via les filtres de segment. Consultez [Incohérences dans les analyses Canvas](#canvas-analytics-mismatches).
- **Critères de sortie :** L'utilisateur peut avoir correspondu aux [critères de sortie]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) avant ou pendant l'entrée. Si l'entrée et la sortie utilisent le même événement, consultez [Correspondance des critères d'entrée et de sortie]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria).
- **Entrée déclenchée par API :** Confirmez que l'utilisateur a été ajouté avec l'[endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases). Vous pouvez [créer un segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) avec un filtre d'entrée Canvas et exporter les utilisateurs avec [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

### Le nombre d'événements déclencheurs est supérieur aux entrées Canvas {#trigger-event-count-is-higher-than-canvas-entries}

**Symptôme :** Le volume d'événements déclencheurs est supérieur au nombre d'entrées Canvas.

Braze déduplique les tentatives d'entrée multiples qui se produisent au même instant, ce qui peut entraîner moins d'entrées Canvas que d'événements déclencheurs. Pour tester des entrées multiples, espacez les événements déclencheurs d'au moins une seconde.

Si un utilisateur effectue le même déclencheur plusieurs fois en une seconde, Braze ne traite qu'une seule entrée. Consultez le diagnostic des messages pour les résultats tels que **Utilisateur non rééligible** lorsque les règles de réentrée ou de rééligibilité s'appliquent.

{% details Heure d'été et Canvas planifiés quotidiennement %}

Lors des jours de transition vers l'heure d'été ou d'hiver, les Canvas planifiés quotidiennement peuvent s'exécuter jusqu'à une heure plus tôt ou plus tard que d'habitude. Si vos critères d'entrée reposent sur des attributs personnalisés ou des événements avec des horodatages situés dans l'heure précédant l'heure d'entrée planifiée, les utilisateurs peuvent ne pas encore être éligibles le jour du changement d'heure, car l'attribut ou l'événement n'a pas encore été enregistré.

Par exemple, supposons que les utilisateurs reçoivent généralement une mise à jour d'attribut personnalisé à 15 h 00 dans le fuseau horaire de votre Canvas et que votre Canvas s'exécute quotidiennement à 15 h 30 dans ce même fuseau horaire. Lors d'un passage à l'heure d'été (avance d'une heure), le Canvas peut évaluer les utilisateurs jusqu'à une heure plus tôt que d'habitude par rapport à cette mise à jour d'attribut, c'est-à-dire avant que l'attribut n'ait été enregistré. Si la rééligibilité est désactivée, les utilisateurs qui sont entrés les jours précédents ne peuvent pas entrer à nouveau, ce qui entraîne zéro entrée pour cette journée.

Pour éviter cela, assurez-vous que les mises à jour de vos attributs personnalisés ou événements se produisent plus d'une heure avant l'heure d'entrée planifiée du Canvas.

{% enddetails %}

## L'utilisateur n'a pas reçu de message ou d'étape Canvas {#user-didnt-receive-a-canvas-message-or-step}

**Symptôme :** Un utilisateur est entré dans le Canvas mais n'a pas reçu le message ou l'étape attendu(e).

Vérifiez l'[**historique des messages**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab) de l'utilisateur pour l'étape et l'horodatage du Canvas. Si aucun enregistrement n'existe, retournez à [L'utilisateur n'est pas entré dans le Canvas](#user-didnt-enter-the-canvas).

Ensuite, vérifiez les points suivants selon le type de déclencheur ou d'étape :

- **Déclencheurs d'événement personnalisé ou d'achat :** Confirmez que l'événement apparaît dans **Analytics** > **Rapport d'événements personnalisés** (ou **Chiffre d'affaires** pour les achats). Comparez l'horodatage de l'événement avec le moment où le Canvas est passé en production et avec tout délai planifié sur l'étape.
- **Entrée déclenchée par API :** Confirmez l'entrée avec un filtre de segment Canvas et un export, comme décrit dans [L'utilisateur n'est pas entré dans le Canvas](#user-didnt-enter-the-canvas).
- **Parcours d'actions ou déclencheurs d'étape de message :** Confirmez que l'utilisateur a effectué l'événement prérequis et que les [propriétés d'événement]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#event-properties) sont disponibles sur l'étape.
- **Étapes de message in-app :** Les messages in-app sont envoyés au prochain démarrage de session après que l'utilisateur entre dans l'étape, et uniquement à partir d'événements SDK (pas de la REST API). Consultez [Quand les messages in-app dans Canvas sont-ils envoyés ?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent) dans la FAQ Canvas.
- **Groupe de contrôle du Canvas :** Vérifiez que l'utilisateur n'a pas été affecté au groupe de contrôle du Canvas à l'entrée.
- **Éligibilité au canal et paramètres d'envoi :** Confirmez le statut d'abonnement, l'état d'activation des notifications push et les [Paramètres d'envoi]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings) par étape (par exemple, **Paramètres d'abonnement** définis sur les utilisateurs ayant donné leur consentement uniquement). N'ajoutez pas de filtres monocanal à l'**audience cible** sur les Canvas multicanaux.
- **Validations de distribution :** Si vous avez activé **Valider l'audience au moment de l'envoi du message** sur une étape de message, les utilisateurs qui ne correspondent plus aux filtres au moment de l'envoi ne reçoivent pas le message. Consultez [Validations de distribution]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).
- **Heures calmes, timing intelligent, plafonds de fréquence et limites de débit :** Ces paramètres peuvent reporter, supprimer ou abandonner des envois. Les utilisateurs peuvent rester dans le Canvas après un abandon dû aux heures calmes.
- **Conditions de concurrence :** Si l'utilisateur a déclenché plusieurs actions simultanément, consultez [Conditions de concurrence]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions).

{% alert important %}
Lorsqu'une étape de message Canvas abandonne un envoi, l'utilisateur avance tout de même à l'étape suivante. Canvas avance en cas d'abandon afin que les étapes de délai et de parcours d'actions ultérieures ne soient pas bloquées de façon permanente. Consultez [Comment les utilisateurs avancent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance) et [Résultats d'abandon]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes).
{% endalert %}

Pour les filtres au niveau des étapes, les conflits entre branches et le comportement de branchement des messages in-app, consultez [Lancer avec Canvas Flow — Résolution des problèmes]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#troubleshooting) et la [FAQ Canvas]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery).

{% alert important %}
Si votre Canvas basé sur des actions envoie des messages plus tôt que prévu, vérifiez que l'horodatage de votre événement personnalisé utilise l'heure actuelle et non une heure antérieure. Braze évalue les délais à partir de l'horodatage envoyé avec l'événement. Consultez [Livraison par événement]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule).
{% endalert %}

## Entrées Canvas faibles ou nulles {#low-or-zero-canvas-entries}

**Symptôme :** Personne ou moins d'utilisateurs que prévu ne sont entrés dans le Canvas.

Commencez par la [liste de vérification de lancement Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#launch-checklist), puis confirmez :

- Le Canvas est actif et l'heure actuelle se situe dans la fenêtre d'entrée planifiée.
- Les [paramètres d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) (rééligibilité, entrées maximales et plafonds d'entrée) autorisent les utilisateurs que vous attendez.
- L'audience cible et les filtres de segment correspondent toujours aux utilisateurs attendus après le lancement.
- Les pourcentages du groupe de contrôle global et du groupe de contrôle Canvas indiquent quelle part des utilisateurs entre dans chaque parcours par rapport à ceux qui reçoivent des messages.
- Les limites de débit de l'espace de travail ou les files d'attente d'entrée sont susceptibles d'ajouter des délais entre le moment où les utilisateurs sont éligibles et celui où ils entrent ou avancent dans une étape.

Pour un utilisateur individuel, suivez le [parcours d'investigation standard](#standard-investigation-path). Pour les entrées nulles liées au changement d'heure, consultez la section dépliable sous [L'utilisateur n'est pas entré dans le Canvas](#user-didnt-enter-the-canvas).

## Envois inférieurs aux attentes {#lower-sends-than-expected}

**Symptôme :** Les envois ou distributions sont inférieurs à l'audience estimée sur une étape Canvas.

Les causes courantes incluent la réévaluation de l'audience au moment de l'envoi, l'éligibilité au canal, les groupes de contrôle, les heures calmes, le timing intelligent, les limites de débit et le comportement de distribution des messages in-app (zéro _envoi_ avec des impressions est un comportement attendu pour les messages in-app).

Pour une liste détaillée, consultez [Pourquoi les envois sont-ils inférieurs à la taille estimée de l'audience ?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#why-are-sends-lower-than-the-estimated-audience-size) dans la FAQ Canvas et [Pourquoi les envois sont-ils inférieurs à la taille estimée de l'audience ?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size) pour les Campaigns.

Utilisez le [tableau de bord de diagnostic des messages]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) pour voir les raisons d'abandon et de rejet au niveau de l'étape.

## Incohérences dans les analyses Canvas {#canvas-analytics-mismatches}

**Symptôme :** Les analyses du Canvas semblent incorrectes (répartition du groupe de contrôle, conversions ou zéro envoi).

L'affectation au groupe de contrôle et à la variante se fait à l'entrée du Canvas en fonction des pourcentages que vous avez définis dans le générateur, et non via des filtres de segment. Les utilisateurs qui ne peuvent pas recevoir un canal spécifique peuvent tout de même entrer dans une variante ; utilisez les [Paramètres d'envoi]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings) par étape pour limiter qui reçoit chaque type de message au lieu de restreindre l'**audience cible** avec des filtres de canal.

Distinguez le groupe de contrôle du Canvas du [groupe de contrôle global]({{site.baseurl}}/user_guide/audience/global_control_group). Pour les définitions des filtres, consultez [Quelle est la différence entre « N'est pas entré dans la variante Canvas » et « N'est pas dans le groupe de contrôle Canvas » ?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group) dans la FAQ Canvas.

{% details Pourquoi les envois d'une variante peuvent être inférieurs au pourcentage de la variante %}

Imaginons le scénario suivant :

- Un Canvas possède une seule variante et un groupe de contrôle.
- La première étape de la variante est une notification push.
- 90 % des utilisateurs ont été sélectionnés pour entrer dans la variante, et 10 % pour entrer dans le groupe de contrôle.

![Exemple de Canvas avec 90 % pour la variante et 10 % pour le groupe de contrôle.]({% image_buster /assets/img_archive/trouble15.png %})

Dans ce scénario, 90 % des utilisateurs qui entrent dans le Canvas entrent dans la variante.

Si nous examinons le segment des utilisateurs actifs, nous pouvons constater que même s'il contient 29,8 k utilisateurs, seuls 64 % d'entre eux ont les notifications push activées :

![Segment avec le filtre « Push Enabled » défini sur « true » et une estimation de 29,8 k utilisateurs.]({% image_buster /assets/img_archive/trouble16.png %})

Cela signifie que même si vous avez spécifié que 90 % des utilisateurs devaient entrer dans la variante, tous ces utilisateurs ne sont pas en mesure de recevoir une notification push. Les utilisateurs qui ne peuvent pas recevoir de notification push entrent tout de même dans la variante : le nombre d'envois reflète l'éligibilité au canal au niveau de l'étape, pas l'affectation à la variante à l'entrée.

{% enddetails %}

Pour les définitions des taux de conversion et les analyses au niveau des étapes, consultez [Analyses et conversions]({{site.baseurl}}/user_guide/messaging/canvas/faqs#analytics-and-conversions) dans la FAQ Canvas.

## Problèmes d'éditeur et d'enregistrement {#editor-and-save-issues}

**Symptôme :** L'éditeur de Canvas ne se charge pas, se fige ou n'enregistre pas vos modifications.

| Symptôme | Cause la plus probable |
| --- | --- |
| Le bouton d'enregistrement tourne indéfiniment sans erreur | Filtre d'attribut personnalisé vide ou incomplet dans l'audience du Canvas ou un filtre d'étape — supprimez le filtre ou sélectionnez un attribut valide |
| Erreur « Request Timed Out » lors de la modification | Interférence d'une extension de navigateur, d'un bloqueur de publicités ou d'une session expirée — essayez une fenêtre de navigation privée ou un autre navigateur |
| Impossible d'enregistrer après l'archivage d'une variante | Une variante archivée est encore référencée en aval ; vérifiez les connexions des étapes et restaurez ou remplacez la variante |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptôme de l'éditeur" }

Si l'éditeur se fige sur un Canvas volumineux ou complexe, essayez les solutions suivantes :

- Videz le cache et les cookies de votre navigateur, puis rechargez la page. Les bloqueurs de publicités d'entreprise ou les extensions de navigateur peuvent interférer avec la plateforme Braze.
- Utilisez les commandes de zoom du Canvas pour réduire la vue à 25 % ou 10 % afin de diminuer la quantité d'interface que le navigateur doit afficher.
- Essayez un autre navigateur web.

Si le Canvas ne se charge pas et ne progresse pas, une version précédente ne s'est pas enregistrée correctement et peut contenir des étapes invalides. Dupliquez le Canvas depuis le tableau de bord. Si le problème persiste, ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support).

Pour les tickets d'assistance « Request Timed Out », incluez un enregistrement d'écran, l'horodatage et le fuseau horaire, le navigateur et sa version, les étapes pour reproduire le problème, et éventuellement un journal HAR depuis les outils de développement de votre navigateur. Consultez [Que dois-je inclure lors de la soumission d'un ticket d'assistance pour une erreur « Request Timed Out » ?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error) dans la FAQ Canvas.

## Comportement d'un Canvas arrêté {#stopped-canvas-behavior}

**Symptôme :** Vous avez arrêté le Canvas mais des utilisateurs ont quand même reçu des messages.

Lorsque vous arrêtez un Canvas, les utilisateurs ne peuvent plus y entrer et aucun autre message n'est envoyé depuis le flux Canvas. Les envois d'e-mails déjà transmis à votre fournisseur de services d'e-mailing ne peuvent pas être rappelés.

Les utilisateurs en attente sur une étape de délai ou de parcours d'actions ne sont pas automatiquement retirés du parcours lorsque vous arrêtez le Canvas. Si vous réactivez le Canvas avant que leur heure d'envoi planifiée ne soit passée, ils peuvent encore recevoir les étapes en attente.

Pour tous les détails, consultez [Que se passe-t-il lorsque vous arrêtez un Canvas ?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas) dans la FAQ Canvas.

## Erreur « Too many Canvas branches » {#too-many-canvas-branches-error}

**Symptôme :** Vous voyez une erreur « Too many Canvas branches » lors du lancement d'un Canvas planifié.

Cette erreur apparaît lorsque la combinaison de la ramification des étapes et de la taille de l'audience d'entrée peut créer des problèmes de performance du cluster qui empêchent l'envoi des messages. Braze affiche ce message lorsque vous lancez un Canvas avec une entrée planifiée — il n'apparaît pas lorsque vous enregistrez un brouillon.

Pour résoudre ce problème :

- Réduisez la ramification des étapes dans le Canvas.
- Réduisez la taille de l'audience d'entrée.
- Utilisez les [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) pour consolider la ramification au lieu de nombreux parcours parallèles.
- Si votre Canvas utilise l'éditeur d'origine, [clonez-le vers Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases) et reconstruisez-le avec les composants Canvas.

Si vous devez tout de même lancer le Canvas sans modifications et que vous ne pouvez pas passer à Canvas Flow, contactez l'[Assistance]({{site.baseurl}}/support_contact).

## Quand contacter l'Assistance {#when-to-contact-support}

Contactez l'[Assistance Braze]({{site.baseurl}}/braze_support) dans les 30 jours suivant le problème si vous avez suivi le [parcours d'investigation standard](#standard-investigation-path) et que vous avez toujours besoin d'aide.

Incluez :

- L'ID du Canvas et les ID des utilisateurs concernés (ID externe ou ID Braze)
- Les horodatages avec le fuseau horaire
- Les captures d'écran ou exports de l'**historique des messages** ou du **diagnostic des messages**
- Pour les erreurs « Request Timed Out » de l'éditeur, les détails listés dans [Problèmes d'éditeur et d'enregistrement](#editor-and-save-issues)