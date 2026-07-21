---
nav_title: Prévisualisation des chemins utilisateur
article_title: Prévisualisation des chemins utilisateur
page_order: 0.3
alias: /preview_user_paths/
description: "Cette page explique comment prévisualiser les parcours des utilisateurs dans Canvas."
tool:
  - Canvas
---

# Prévisualiser les parcours des utilisateurs dans Canvas {#preview-user-paths-in-canvas}

> Découvrez l'expérience Canvas que vous avez créée pour vos utilisateurs. Cela inclut la prévisualisation du timing et des messages que vos utilisateurs reçoivent. Ces tests permettent de s'assurer que vos messages sont envoyés à la bonne audience, et ce avant l'envoi de votre Canvas.

## Création d'un test {#creating-a-test-run}

Procédez comme suit pour prévisualiser votre parcours utilisateur :

1. Accédez à votre générateur de Canvas. Enregistrez les modifications non sauvegardées et résolvez les éventuelles erreurs.
2. Sélectionnez **Test Canvas** dans le pied de page.
3. Sélectionnez un utilisateur test.
4. (Facultatif) Sélectionnez un destinataire pour le test.
5. Sélectionnez **Run Test**.

Vous pouvez lancer une prévisualisation même si vous n'avez pas la permission de modifier un Canvas, mais cette prévisualisation s'exécute avec les modifications non enregistrées s'il y en a.

### Étapes prises en charge {#supported-steps}

Les étapes suivantes sont prises en charge :
- Message
- Parcours d'audience
- Arbre décisionnel
- Délai
- Parcours d'action
- Chemin d'expérience
- Agent
- Mise à jour utilisateur (uniquement dans l'éditeur d'interface, ce qui signifie que les étapes utilisant l'éditeur JSON sont ignorées)

Si le test rencontre un type d'étape qui n'est pas listé dans cette section, l'étape non prise en charge est ignorée et l'utilisateur test continue vers l'étape prise en charge suivante.

### Étapes Agent {#agent-steps}

Lorsqu'un test atteint une [étape Agent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step), Braze met en pause et demande **Voulez-vous exécuter l'agent « {agentName} » ?** Choisissez comment continuer :

- **Oui :** Ajoutez éventuellement du contexte dans le champ de texte (en plus du profil de l'utilisateur test et de tout contexte Canvas déjà présent dans le parcours), puis sélectionnez **Simulate response** pour invoquer l'agent. Vous pouvez saisir des valeurs d'exemple en langage naturel — par exemple, en décrivant le contenu d'un panier ou le texte d'un message entrant — pour reproduire le contexte d'exécution que l'agent recevrait en production.
- **Non :** Braze n'invoque pas l'agent. L'étape utilise la **sortie de secours** configurée pour l'agent dans la section **Output** de la [console Agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values).

Lorsque vous sélectionnez **Oui** puis **Simulate response**, l'agent s'exécute pour l'utilisateur de prévisualisation, stocke sa sortie dans la variable de sortie de l'étape Agent, et le test continue le long du parcours. Les invocations issues de **Simulate response** sont comptabilisées dans la limite d'invocations quotidiennes de l'agent et apparaissent dans **Agent Console** > **Logs**.

Pour tester une étape Agent de manière isolée (sans exécuter l'intégralité du parcours Canvas), utilisez la prévisualisation intégrée à l'étape dans le générateur de Canvas. Pour les détails de configuration, consultez [Tester l'agent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#step-5-test-the-agent) dans Étape Agent.

Si votre étape Agent dépend de données provenant d'une [étape de contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) en amont, exécutez **Test Canvas** afin que les variables de contexte soient renseignées le long du parcours. Les groupes initiateurs n'évaluent pas les étapes de contexte ni les variables de contexte pour les destinataires initiateurs.

### Détails des étapes du Canvas {#canvas-step-details}

Pour afficher plus de détails sur les critères d'entrée, sélectionnez **See more**. Les étapes avec segmentation affichent les critères remplis ou non remplis. Les messages affichent également ces informations pour les validations de réception/distribution et l'éligibilité des canaux. Les étapes de message indiquent quels canaux ont été envoyés et lesquels ne l'ont pas été.

### Liquid

Braze traite la logique Liquid pendant un test, même si vous n'envoyez pas de message test réel. Cela signifie que la [logique d'abandon de message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) et les autres logiques Liquid sont prises en compte et peuvent impacter le parcours utilisateur dans le Canvas.

Si votre prévisualisation envoie la dernière étape de votre parcours utilisateur au lieu d'abandonner, la prévisualisation utilise peut-être l'heure actuelle comme heure testée pour l'évaluation Liquid, et non l'heure réelle à laquelle l'utilisateur se trouverait dans l'étape en fonction de l'heure d'entrée dans le Canvas.

## Prévisualisations du timing {#previews-for-timing}

Pour les Canvas planifiés, l'utilisateur test entre à la prochaine heure d'entrée planifiée. Pour les Canvas basés sur une action avec des dates de début, l'utilisateur test entre à la date et l'heure de début.

Bien que les heures de début par défaut s'appliquent toujours, l'heure d'entrée est configurable dans tous les cas, ce qui vous permet de simuler une date passée ou future. Cependant, vous ne pouvez pas tester avant la date de début ni après la date de fin du Canvas.

Les étapes de message et de délai affichent l'heure à laquelle un utilisateur progresserait ou recevrait le message sans avoir besoin de reconfigurer les délais. Notez que bien que les étapes indiquent si le timing intelligent est utilisé, cette prévisualisation du parcours utilisateur ne calcule pas d'estimation pour un utilisateur test.

Pour les Canvas avec un déclencheur d'action comme « changement de valeur d'attribut personnalisé », Braze tente de simuler le changement en définissant temporairement l'attribut de l'utilisateur dans le déclencheur comme vide **uniquement pour le test du Canvas** (cela n'affecte pas le profil utilisateur). L'objectif est de tester que l'attribut change par rapport à sa valeur actuelle.

## Quand les utilisateurs entrent et sortent {#when-users-enter-and-exit}

Les utilisateurs test entrent dans la prévisualisation même s'ils ne sont pas éligibles en conditions réelles. S'ils ne sont pas éligibles, vous pouvez voir pourquoi ils n'ont pas rempli les critères. Lorsqu'un utilisateur test entre dans la prévisualisation, nous supposons qu'il a rempli les critères d'audience cible et effectué les critères de déclencheur d'action. Par exemple, pour un Canvas qui utilise des événements personnalisés dans les critères d'entrée, l'utilisateur test est supposé avoir effectué l'événement personnalisé tel qu'attendu dans les critères d'entrée. Cependant, si le même événement personnalisé est utilisé ailleurs dans le Canvas (comme dans les critères de sortie), tenez compte de l'impact potentiel sur votre parcours utilisateur.

Les événements, déclencheurs API, attributs personnalisés et propriétés d'entrée du Canvas qui sont supposés permettre à un utilisateur test d'entrer dans le Canvas ne sont pas mis à jour dans le profil utilisateur réel et ne persistent pas au-delà du test. Par exemple, pendant le test, lorsqu'un attribut personnalisé est utilisé comme déclencheur de Canvas, les critères de déclencheur sont appliqués à la prévisualisation de l'utilisateur **comme si** celui-ci avait déclenché le changement d'attribut personnalisé.

### Point important {#consideration}

Si vous testez un parcours d'action avec des actions qui correspondent aux critères de sortie (y compris les propriétés d'événement), les critères de sortie sont déclenchés et le test se termine. Si vous testez une étape de message qui correspond aux critères de sortie, les critères de sortie sont déclenchés et le test se termine.

À ce stade, vous ne pouvez pas sélectionner un événement ou une propriété spécifique au sein d'un parcours d'action pour déclencher les critères de sortie (uniquement le parcours dans son ensemble). Si un utilisateur peut potentiellement remplir plusieurs critères de sortie, le premier qui est traité et qu'il remplit est affiché comme résultat.

## Chemins d'expérience et variantes du Canvas {#experiment-paths-and-canvas-variants}

- Pour les Canvas avec des variantes de niveau supérieur, sélectionnez une variante au début du test.
- Pour les chemins d'expérience, sélectionnez la variante dans laquelle l'utilisateur progresse lorsque l'utilisateur test rencontre l'étape.
- Pour les chemins d'expérience utilisant un chemin personnalisé ou une variante gagnante, bien qu'il y ait une période de délai pendant laquelle l'utilisateur test attend dans une étape de message, ce délai n'est pas pris en compte car Braze suppose que l'utilisateur a progressé immédiatement dans la variante sélectionnée.

## Envois de test {#test-sends}

Vous pouvez choisir d'envoyer des messages test à un groupe de test interne ou à un utilisateur individuel au fur et à mesure que le test se déroule. Cela signifie que seuls les messages que l'utilisateur rencontre le long du parcours de test sont envoyés. Les destinataires reçoivent les messages avec leurs propres attributs par défaut, mais vous pouvez les remplacer par les attributs de l'utilisateur test.

Pour envoyer tous les messages test d'un Canvas en une seule fois, quel que soit le parcours, et sans prévisualiser le parcours, vous pouvez sélectionner **Send All Test Messages** dans l'onglet **Test Sends**.

## Réactivité {#responsiveness}

Les étapes du Canvas réagissent au timing lors de la prévisualisation des parcours utilisateur. Les mises à jour effectuées via l'étape Mise à jour utilisateur sont reflétées dans les étapes suivantes du flux, mais ne sont pas appliquées au profil utilisateur réel. Les effets de l'entrée d'un utilisateur dans une variante sont reflétés dans les étapes suivantes de la prévisualisation.

De même, les filtres reconnaissent les actions qui se sont produites à la suite de l'interaction de l'utilisateur test avec d'autres étapes du Canvas. Par exemple, ce mode de prévisualisation reconnaît qu'un utilisateur a rencontré une étape de message qui a été « envoyée » plus tôt dans le Canvas, et il reconnaît que l'utilisateur test a « effectué une action » pour progresser dans un parcours d'action.

Consultez [Critères de sortie]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) pour plus de détails sur le comportement réactif.

## Contenu connecté {#connected-content}

Le contenu connecté est exécuté s'il est inclus dans le Canvas. Cela signifie que si vous testez un Canvas contenant des appels de contenu connecté ou des Content Blocks qui contiennent du contenu connecté, le Canvas peut envoyer les appels de contenu connecté, ce qui modifierait les données référencées dans d'autres Campaigns ou Canvas.

Lors de la prévisualisation des parcours utilisateur, envisagez de supprimer le contenu connecté qui modifie les profils utilisateur ou les données référencées dans d'autres Canvas ou Campaigns.

## Webhooks {#webhooks}

Les webhooks s'exécutent lorsque des messages test sont envoyés, mais pas pendant le test. Comme pour le contenu connecté, envisagez de supprimer les webhooks qui modifient les profils utilisateur ou les données référencées dans d'autres Canvas ou Campaigns.

## Variables de contexte et groupes initiateurs {#context-variables-and-seed-groups}

Pour une étape de message avec l'e-mail comme canal de communication, les groupes initiateurs envoient des copies initiatrices des e-mails lorsqu'un utilisateur atteint cette étape dans le Canvas. Ces copies initiatrices ne sont pas envoyées dans le cadre des propres parcours Canvas des destinataires du groupe initiateur, donc Braze n'exécute pas les [étapes de contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) et n'évalue pas les variables de contexte pour ces destinataires. Si le contenu de votre e-mail fait référence à des variables de contexte, les destinataires du groupe initiateur reçoivent une copie initiatrice sans ces données renseignées. Pour tester des messages qui reposent sur des données de variables de contexte, utilisez la prévisualisation **Test Canvas** avec des envois de test au lieu des groupes initiateurs.

## Cas d'usage {#use-case}

Dans ce scénario, le Canvas est configuré pour cibler les utilisateurs qui n'ont pas eu de session dans une application. Ce parcours comprend une étape de message avec un e-mail de bienvenue, une étape de délai définie sur un jour et une étape de parcours d'audience qui se divise en deux chemins : les utilisateurs ayant au moins une session et tous les autres. Selon le parcours d'audience dans lequel un utilisateur se trouve, l'étape de message suivante est envoyée.

![Un exemple de Canvas avec une étape de message, une étape de délai, une étape de parcours d'audience et deux étapes de message.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

Comme notre utilisateur test remplit les critères d'entrée du Canvas, il peut entrer dans le Canvas et parcourir le parcours utilisateur. Cependant, comme notre utilisateur test n'a pas ouvert l'application au cours du dernier jour calendaire, il continue sur le chemin « Tous les autres » et reçoit une notification push indiquant : « Dernière chance ! Terminez votre première tâche pour un bonus exclusif. »

![La section « Test Results » montre que l'utilisateur test a rempli les critères d'entrée et fournit un résumé de son parcours, y compris les étapes qui lui ont été envoyées.]({% image_buster /assets/img/preview_user_path_results_example.png %})