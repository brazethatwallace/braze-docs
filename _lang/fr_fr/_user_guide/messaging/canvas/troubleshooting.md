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
Les journaux de l'**historique des messages** et du **diagnostic des messages** sont disponibles pendant **30 jours** à compter de l'événement. Contactez l'[assistance Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) dans ce délai si vous avez besoin d'aide pour investiguer un incident spécifique.
{% endalert %}

## Commencez ici : identifiez votre symptôme {#start-here-match-your-symptom}

| Symptôme | Aller à |
| --- | --- |
| Un utilisateur n'est pas entré dans le Canvas | [L'utilisateur n'est pas entré dans le Canvas](#user-didnt-enter-the-canvas) |
| Un utilisateur est entré mais n'a pas reçu de message ou d'étape | [L'utilisateur n'a pas reçu de message ou d'étape du Canvas](#user-didnt-receive-a-canvas-message-or-step) |
| Personne ou moins d'utilisateurs que prévu ne sont entrés | [Entrées Canvas faibles ou nulles](#low-or-zero-canvas-entries) |
| Les envois ou distributions sont inférieurs à l'audience estimée | [Envois inférieurs aux prévisions](#lower-sends-than-expected) |
| Les analyses du Canvas semblent incorrectes (groupe de contrôle, conversions, zéro envoi) | [Incohérences dans les analyses du Canvas](#canvas-analytics-mismatches) |
| Les analyses affichent bien plus d'envois que d'entrées ou plus de sorties que d'entrées | [Le filtrage par plage de dates peut afficher des chiffres inattendus](#date-range-filtering-can-show-unexpected-numbers) |
| Le Canvas ne s'enregistre pas ou l'éditeur se fige | [Problèmes d'éditeur et d'enregistrement](#editor-and-save-issues) |
| Impossible de supprimer une variante du Canvas | [Impossible de supprimer une variante du Canvas en raison d'un Segment archivé](#cant-delete-a-canvas-variant-because-of-an-archived-segment) |
| J'ai arrêté le Canvas mais des messages ont quand même été envoyés | [Comportement d'un Canvas arrêté](#stopped-canvas-behavior) |
| Erreur « Too many Canvas branches » au lancement | [Erreur « Too many Canvas branches »](#too-many-canvas-branches-error) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptôme Canvas" }

## Parcours d'investigation standard {#standard-investigation-path}

Utilisez ce flux de travail pour investiguer un utilisateur spécifique ou un problème d'envoi agrégé. Commencez à l'étape 1 pour chaque incident.

1. Confirmez que le Canvas est actif (ni brouillon, ni arrêté, ni archivé).
2. Confirmez que la planification d'entrée (fenêtre planifiée, fuseau horaire, déclencheur par événement ou entrée déclenchée par API) correspond au moment où vous attendez l'entrée des utilisateurs.
3. Vérifiez l'historique de communication d'un utilisateur en accédant à **Audience** > **Rechercher des utilisateurs**, en ouvrant le profil, puis en sélectionnant **Historique des messages** (30 derniers jours).
   - Si aucun enregistrement n'existe pour l'heure d'envoi attendue, le problème concerne l'entrée, pas le message. Accédez à [L'utilisateur n'est pas entré dans le Canvas](#user-didnt-enter-the-canvas).
4. Consultez le **journal des modifications** du Canvas ainsi que les journaux des modifications de tous les Segments utilisés dans le ciblage. Confirmez que l'audience, les étapes ou les paramètres d'envoi n'ont pas été modifiés pendant l'incident.
5. Vérifiez les résultats agrégés sur la page d'analyse du Canvas en ouvrant le [tableau de bord de diagnostic des messages]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) et en examinant les raisons d'abandon et de rejet.
   - Si vous voyez un résultat que vous ne reconnaissez pas, consultez [Résultats d'abandon]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes) dans la documentation de diagnostic.
   - Si une étape affiche zéro entrée (et non zéro envoi), vérifiez le type d'étape précédente ([Parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), [Délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) ou [Arbre décisionnel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)).
6. Si le problème persiste, contactez l'[assistance Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) dans les 30 jours en fournissant l'ID du Canvas, les ID des utilisateurs concernés, les horodatages (avec le fuseau horaire) et des captures d'écran de l'historique des messages ou du diagnostic des messages.

Avant le lancement, utilisez [Envoyer des Canvas de test]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) et [Prévisualiser les parcours utilisateurs]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) pour valider votre configuration.

## L'utilisateur n'est pas entré dans le Canvas {#user-didnt-enter-the-canvas}

**Symptôme :** un utilisateur n'est pas entré dans le Canvas alors que vous vous y attendiez, ou moins d'utilisateurs sont entrés que ne le suggèrent vos événements déclencheurs.

Les utilisateurs doivent correspondre à l'**audience cible** avant que Braze n'évalue le déclencheur d'entrée (sauf pour les déclencheurs de [changement d'attribut]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Un déclencheur seul ne garantit pas l'entrée si l'utilisateur ne faisait pas partie de l'audience au moment de l'évaluation.

La rééligibilité et la réentrée sont des contrôles distincts dans [Sélection des contrôles d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) :

- **Rééligibilité :** détermine si un utilisateur est autorisé à entrer de nouveau dans le Canvas après en être sorti (fenêtre temporelle et paramètre **Autoriser les utilisateurs à réentrer dans le Canvas**).
- **Réentrée :** détermine si un utilisateur actuellement dans le Canvas peut emprunter un parcours simultané.

Un utilisateur peut être rééligible mais bloqué parce qu'il se trouve encore dans le Canvas, ou bien avoir quitté le Canvas tout en étant encore en dehors de la fenêtre de rééligibilité. Vérifiez les deux paramètres lorsqu'un utilisateur ne réintègre pas un Canvas.

Vérifiez les éléments suivants :

- **Planification de l'entrée et fuseau horaire :** confirmez que le Canvas était actif et que l'utilisateur a déclenché l'événement pendant la [fenêtre d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule).
- **Audience cible au moment de l'évaluation :** examinez les journaux de modifications des Segments et des filtres. [User Lookup]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) peut afficher un faux positif pour certains types de filtres (par exemple, les attributs de date au format chaîne de caractères).
- **Limites d'entrée :** le [nombre maximum d'entrées]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) ou les plafonds d'audience ont peut-être été atteints.
- **Groupe de contrôle global :** les utilisateurs du [groupe de contrôle global]({{site.baseurl}}/user_guide/audience/global_control_group) n'entrent pas dans les Canvas de communication.
- **Groupe de contrôle du Canvas :** les utilisateurs assignés au groupe de contrôle du Canvas lors de l'entrée ne reçoivent pas les messages de variante. L'attribution des variantes se fait à l'entrée, pas via les filtres de Segment. Voir [Incohérences dans les analyses Canvas](#canvas-analytics-mismatches).
- **Critères de sortie :** l'utilisateur a peut-être correspondu aux [critères de sortie]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) avant ou pendant l'entrée. Si l'entrée et la sortie utilisent le même événement, consultez [Correspondance des critères d'entrée et de sortie]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria).
- **Entrée déclenchée par API :** confirmez que l'utilisateur a été ajouté via l'[endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases). Vous pouvez [créer un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) avec un filtre d'entrée Canvas et exporter les utilisateurs via [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

### Le nombre d'événements déclencheurs est supérieur aux entrées dans le Canvas {#trigger-event-count-is-higher-than-canvas-entries}

**Symptôme :** le volume d'événements déclencheurs est supérieur au nombre d'entrées dans le Canvas.

Braze déduplique les tentatives d'entrée multiples qui se produisent au même instant ; vous pouvez donc observer moins d'entrées dans le Canvas que d'événements déclencheurs. Pour tester des entrées multiples, espacez les événements déclencheurs d'au moins une seconde.

Si un utilisateur déclenche le même événement plusieurs fois en une seconde, Braze ne traite qu'une seule entrée. Consultez les diagnostics de messagerie pour des résultats tels que **Utilisateur non rééligible** lorsque des règles de réentrée ou de rééligibilité s'appliquent.

{% details Heure d'été et Canvas planifiés quotidiennement %}

Les jours de changement d'heure (heure d'été), les Canvas planifiés quotidiennement peuvent s'exécuter jusqu'à une heure plus tôt ou plus tard que d'habitude. Si vos critères d'entrée reposent sur des attributs personnalisés ou des événements dont les horodatages se situent dans l'heure précédant l'heure d'entrée planifiée, les utilisateurs peuvent ne pas encore être éligibles le jour du changement d'heure, car l'attribut ou l'événement n'a pas encore été enregistré.

Par exemple, supposons que les utilisateurs reçoivent habituellement une mise à jour d'attribut personnalisé à 15 h dans le fuseau horaire de votre Canvas et que votre Canvas s'exécute quotidiennement à 15 h 30 dans ce même fuseau. Lors d'un passage à l'heure d'été (avancée), le Canvas peut évaluer les utilisateurs jusqu'à une heure plus tôt que d'habitude par rapport à cette mise à jour d'attribut — avant que l'attribut n'ait été enregistré. Si la rééligibilité est désactivée, les utilisateurs qui sont entrés les jours précédents ne peuvent pas réentrer, ce qui entraîne zéro entrée pour cette journée.

Pour éviter cela, assurez-vous que les mises à jour de vos attributs personnalisés ou événements surviennent plus d'une heure avant l'heure d'entrée planifiée du Canvas.

{% enddetails %}

## L'utilisateur n'a pas reçu de message ou d'étape du Canvas {#user-didnt-receive-a-canvas-message-or-step}

**Symptôme :** Un utilisateur est entré dans le Canvas mais n'a pas reçu le message ou l'étape attendu(e).

Vérifiez l'[**historique des messages**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab) de l'utilisateur pour l'étape du Canvas et l'horodatage. Si aucun enregistrement n'existe, revenez à [L'utilisateur n'est pas entré dans le Canvas](#user-didnt-enter-the-canvas).

Vérifiez ensuite les éléments suivants selon le type de déclencheur ou d'étape :

- **Déclencheurs d'événement personnalisé ou d'achat :** Confirmez que l'événement apparaît dans **Analytics** > **Rapport d'événements personnalisés** (ou **Revenus** pour les achats). Comparez l'horodatage de l'événement avec le moment où le Canvas est devenu actif et avec tout délai planifié sur l'étape.
- **Entrée déclenchée par API :** Confirmez l'entrée avec un filtre de Segment Canvas et un export, comme décrit dans [L'utilisateur n'est pas entré dans le Canvas](#user-didnt-enter-the-canvas).
- **Parcours d'action ou déclencheurs d'étape Message :** Confirmez que l'utilisateur a effectué l'événement prérequis et que les [propriétés d'événement]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#event-properties) sont disponibles sur l'étape.
- **Étapes de message in-app :** Les messages in-app sont envoyés au prochain démarrage de session après que l'utilisateur entre dans l'étape, et uniquement à partir d'événements SDK (pas de la REST API). Consultez [Quand les messages in-app dans Canvas sont-ils envoyés ?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent) dans la FAQ Canvas.
- **Groupe de contrôle du Canvas :** Vérifiez que l'utilisateur n'a pas été affecté au groupe de contrôle du Canvas à l'entrée.
- **Éligibilité du canal et paramètres d'envoi :** Confirmez le statut d'abonnement, l'état d'activation des notifications push et les [paramètres d'envoi]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings) par étape (par exemple, **Paramètres d'abonnement** définis uniquement pour les utilisateurs ayant opté). N'ajoutez pas de filtres monocanal dans **Audience cible** sur des Canvas multicanaux.
- **Validations de distribution :** Si vous avez activé **Valider l'audience au moment de l'envoi du message** sur une étape Message, les utilisateurs qui ne correspondent plus aux filtres au moment de l'envoi ne reçoivent pas le message. Consultez [Validations de distribution]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).
- **Heures calmes, timing intelligent, plafonnement de fréquence et limitation du débit :** Ces fonctionnalités peuvent différer, supprimer ou annuler les envois. Les utilisateurs peuvent rester dans le Canvas après une annulation liée aux heures calmes.
- **Conditions de concurrence :** Si l'utilisateur a déclenché plusieurs actions simultanément, consultez [Conditions de concurrence]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions).

{% alert important %}
Lorsqu'une étape Message d'un Canvas annule un envoi, l'utilisateur avance tout de même vers l'étape suivante. Le Canvas progresse en cas d'annulation afin que les étapes de délai et de parcours d'action ultérieures ne soient pas bloquées de manière permanente. Consultez [Comment les utilisateurs avancent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance) et [Résultats des annulations]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes).
{% endalert %}

Pour les filtres au niveau des étapes, les conflits entre branches et le comportement de branchement des messages in-app, consultez [Lancer avec Canvas Flow — Résolution des problèmes]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#troubleshooting) et la [FAQ Canvas]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery).

{% alert important %}
Si votre Canvas basé sur les actions envoie des messages plus tôt que prévu, vérifiez que l'horodatage de votre événement personnalisé utilise l'heure actuelle et non une heure antérieure. Braze évalue les délais à partir de l'horodatage envoyé avec l'événement. Consultez [Livraison par événement]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule).
{% endalert %}

## Entrées Canvas faibles ou nulles {#low-or-zero-canvas-entries}

**Symptôme :** Aucun utilisateur ou moins d'utilisateurs que prévu n'est entré dans le Canvas.

Commencez par la [checklist de lancement avec Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#launch-checklist), puis vérifiez les points suivants :

- Le Canvas est actif et l'heure actuelle se situe dans la fenêtre d'entrée planifiée.
- Les [paramètres d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) (rééligibilité, nombre maximum d'entrées et plafonds d'entrée) autorisent les utilisateurs que vous attendez à entrer.
- L'audience cible et les filtres de Segment correspondent toujours aux utilisateurs attendus après le lancement.
- Les pourcentages du groupe de contrôle global et du groupe de contrôle Canvas indiquent quelle part d'utilisateurs entre dans chaque parcours par rapport à ceux qui reçoivent des messages.
- Les limites de débit de l'espace de travail ou les files d'attente d'entrée sont susceptibles d'ajouter des délais entre le moment où les utilisateurs se qualifient et celui où ils entrent ou avancent dans une étape.

Pour un utilisateur unique, suivez le [parcours d'investigation standard](#standard-investigation-path). Pour les entrées nulles liées au changement d'heure (DST), consultez la section dépliable sous [L'utilisateur n'est pas entré dans le Canvas](#user-didnt-enter-the-canvas).

## Envois inférieurs aux prévisions {#lower-sends-than-expected}

**Symptôme :** Les envois ou les distributions sont inférieurs à l'audience estimée sur une étape du Canvas.

Les causes courantes incluent la réévaluation de l'audience au moment de l'envoi, l'éligibilité au canal, les groupes de contrôle, les heures calmes, le timing intelligent, les limites de débit et le comportement de distribution des messages in-app (zéro _Envois_ avec des impressions est normal pour les messages in-app).

Si une étape Message montre que de nombreux utilisateurs sont entrés mais que peu d'envois ont eu lieu, vérifiez si `abort_message()` dans Liquid a annulé l'envoi. Pour les vérifications du journal d'activité des messages, les attributs manquants et les envois de test, consultez [Résolution des problèmes de taux d'abandon élevés]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages#troubleshooting-high-abort-rates).

Pour une liste détaillée, consultez [Pourquoi les envois sont-ils inférieurs à la taille estimée de l'audience ?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#why-are-sends-lower-than-the-estimated-audience-size) dans la FAQ Canvas et [Pourquoi les envois sont-ils inférieurs à la taille estimée de l'audience ?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size) pour les Campaigns.

Utilisez le [tableau de bord de diagnostic des messages]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) pour consulter les raisons d'abandon et de rejet au niveau de l'étape.

## Incohérences dans les analyses Canvas {#canvas-analytics-mismatches}

**Symptôme :** Les analyses Canvas semblent incorrectes (répartition du groupe de contrôle, conversions ou envois à zéro).

L'attribution au groupe de contrôle et aux variantes se fait à l'entrée dans le Canvas, en fonction des pourcentages que vous avez définis dans le générateur, et non via des filtres de segment. Les utilisateurs qui ne peuvent pas recevoir un canal spécifique peuvent tout de même entrer dans une variante ; utilisez les [paramètres d'envoi]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings) au niveau de chaque étape pour limiter qui reçoit chaque type de message, au lieu de restreindre l'**audience cible** avec des filtres de canal.

Distinguez le groupe de contrôle du Canvas du [groupe de contrôle global]({{site.baseurl}}/user_guide/audience/global_control_group). Pour les définitions des filtres, consultez [Quelle est la différence entre « N'est pas entré dans une variante du Canvas » et « N'est pas dans le groupe de contrôle du Canvas » ?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group) dans la FAQ Canvas.

{% details Pourquoi les envois d'une variante peuvent être inférieurs au pourcentage de la variante %}

Imaginons le scénario suivant :

- Un Canvas comporte une seule variante et un groupe de contrôle.
- La première étape de la variante est une notification push.
- 90 % des utilisateurs ont été sélectionnés pour entrer dans la variante et 10 % pour entrer dans le groupe de contrôle.

![Exemple de Canvas avec 90 % pour la variante et 10 % pour le groupe de contrôle.]({% image_buster /assets/img_archive/trouble15.png %})

Dans ce scénario, 90 % des utilisateurs qui entrent dans le Canvas sont affectés à la variante.

Lorsque vous examinez le segment des utilisateurs actifs, vous constaterez que même s'il contient 29,8k utilisateurs, seuls 64 % d'entre eux ont les notifications push activées :

![Segment avec le filtre « Push activé » défini sur « vrai » et une estimation de 29,8k utilisateurs.]({% image_buster /assets/img_archive/trouble16.png %})

Cela signifie que même si vous avez spécifié que 90 % des utilisateurs entrent dans la variante, tous ne peuvent pas recevoir de notification push. Les utilisateurs qui ne peuvent pas recevoir de notifications push entrent tout de même dans la variante : le nombre d'envois reflète l'éligibilité au canal au niveau de l'étape, et non l'attribution de la variante à l'entrée.

{% enddetails %}

### Le filtrage par plage de dates peut afficher des chiffres inattendus {#date-range-filtering-can-show-unexpected-numbers}

**Symptôme :** Les analyses du Canvas ou d'une étape affichent des chiffres inattendus ou improbables, comme beaucoup plus d'envois que d'entrées, ou plus d'utilisateurs sortant d'une étape qu'il n'y en a qui y sont entrés.

Cela peut se produire lorsque vous utilisez le filtre calendrier de plage de dates en haut de la page d'analyse du Canvas. Si vous sélectionnez une plage de dates qui exclut certaines actions des utilisateurs, les indicateurs affichés peuvent ne montrer qu'une partie du parcours de chaque utilisateur.

Par exemple :
- Vous pouvez voir 100 entrées avec 8 000 envois si votre plage de dates commence après l'entrée de la plupart des utilisateurs mais inclut le moment où ils ont reçu les messages.
- Vous pouvez voir plus d'utilisateurs passer à l'étape suivante qu'il n'y en a qui sont entrés dans l'étape précédente, si votre plage ne capture que les sorties mais pas les entrées antérieures.

Pour résoudre ce problème, ajustez la plage de dates pour inclure toutes les dates depuis le lancement du Canvas jusqu'à aujourd'hui, ou sélectionnez une plage couvrant l'intégralité de la période pertinente pour les indicateurs dont vous avez besoin.

Pour les définitions des taux de conversion et les analyses au niveau des étapes, consultez [Analyses et conversions]({{site.baseurl}}/user_guide/messaging/canvas/faqs#analytics-and-conversions) dans la FAQ Canvas.

## Problèmes d'éditeur et de sauvegarde {#editor-and-save-issues}

**Symptôme :** L'éditeur Canvas ne se charge pas, se fige ou ne sauvegarde pas vos modifications.

| Symptôme | Cause la plus probable |
| --- | --- |
| Le bouton de sauvegarde tourne indéfiniment sans erreur | Filtre d'attribut personnalisé vide ou incomplet dans l'audience du Canvas ou dans un filtre d'étape — supprimez le filtre ou sélectionnez un attribut valide |
| Erreur « Request Timed Out » lors de la modification | Interférence d'une extension de navigateur, de bloqueurs de publicités ou d'une session expirée — essayez une fenêtre de navigation privée ou un autre navigateur |
| Impossible de sauvegarder après l'archivage d'une variante | Une variante archivée est encore référencée en aval ; vérifiez les connexions des étapes et restaurez ou remplacez la variante |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptôme de l'éditeur" }

{% alert note %}
Si le même Canvas est ouvert dans plusieurs onglets de navigateur, sauvegarder dans un onglet peut écraser les modifications effectuées dans un autre onglet obsolète. Cette condition de concurrence peut entraîner la suppression de filtres d'audience ou l'application de modifications non souhaitées. Pour éviter toute perte de données, fermez les onglets en double avant de modifier et de sauvegarder un Canvas.
{% endalert %}

Si l'éditeur se fige sur un Canvas volumineux ou complexe, essayez les étapes suivantes :

- Videz le cache et les cookies du navigateur, puis rechargez la page. Les bloqueurs de publicités d'entreprise ou les extensions de navigateur peuvent interférer avec la plateforme Braze.
- Utilisez les commandes de zoom du Canvas pour réduire la vue à 25 % ou 10 % afin de diminuer la quantité d'interface que le navigateur doit rendre.
- Essayez un autre navigateur web.

Si le Canvas ne se charge pas et ne progresse pas, une version précédente ne s'est pas enregistrée correctement et peut contenir des étapes invalides. Dupliquez le Canvas depuis le tableau de bord. Si le problème persiste, ouvrez un [ticket d'assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support).

Pour les tickets d'assistance « Request Timed Out », incluez un enregistrement d'écran, un horodatage et un fuseau horaire, le navigateur et sa version, les étapes pour reproduire le problème et, éventuellement, un journal HAR provenant des outils de développement de votre navigateur. Consultez [Que dois-je inclure lors de la soumission d'un ticket d'assistance pour une erreur « Request Timed Out » ?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error) dans la FAQ Canvas.

{% multi_lang_include audience/segments.md section='Canvas variant archived segment' %}

## Comportement d'un Canvas arrêté {#stopped-canvas-behavior}

**Symptôme :** Vous avez arrêté le Canvas mais les utilisateurs continuent de recevoir des messages.

Lorsque vous arrêtez un Canvas, les utilisateurs ne peuvent plus y entrer et aucun autre message n'est envoyé depuis le flux du Canvas. Les envois d'e-mails déjà transmis à votre fournisseur de services d'e-mailing ne peuvent pas être rappelés.

Les utilisateurs en attente sur une étape de délai ou un parcours d'action ne sont pas automatiquement retirés du parcours lorsque vous arrêtez le Canvas. Si vous réactivez le Canvas avant que leur heure d'envoi planifiée ne soit dépassée, ils peuvent encore recevoir les étapes en attente.

Pour plus de détails, consultez [Que se passe-t-il lorsque vous arrêtez un Canvas ?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas) dans la FAQ Canvas.

## Erreur « Too many Canvas branches » {#too-many-canvas-branches-error}

**Symptôme :** Vous voyez une erreur « Too many Canvas branches » lors du lancement d'un Canvas planifié.

Cette erreur apparaît lorsque la combinaison de la ramification des étapes et de la taille de l'audience d'entrée peut créer des problèmes de performance du cluster qui empêchent l'envoi des messages. Braze affiche ce message lorsque vous lancez un Canvas avec une entrée planifiée — il n'apparaîtra pas lorsque vous enregistrez un brouillon.

Pour résoudre ce problème :

- Réduisez la ramification des étapes dans le Canvas.
- Réduisez la taille de l'audience d'entrée.
- Utilisez les [parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) pour consolider la ramification au lieu de nombreux parcours parallèles.
- Si votre Canvas utilise l'éditeur d'origine, [clonez-le vers Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases) et reconstruisez-le avec les composants Canvas.

Si vous devez tout de même lancer le Canvas sans modifications et que vous ne pouvez pas passer à Canvas Flow, contactez le [support]({{site.baseurl}}/support_contact).

## Quand contacter le support {#when-to-contact-support}

Contactez le [support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) dans les 30 jours suivant le problème si vous avez suivi le [parcours d'investigation standard](#standard-investigation-path) et avez encore besoin d'aide.

Incluez :

- L'ID du Canvas et les ID des utilisateurs concernés (ID externe ou ID Braze)
- Les horodatages avec le fuseau horaire
- Des captures d'écran ou des exports depuis **Messaging History** ou **Messaging Diagnostics**
- Pour les erreurs « Request Timed Out » de l'éditeur, les détails listés dans [Problèmes d'éditeur et de sauvegarde](#editor-and-save-issues)