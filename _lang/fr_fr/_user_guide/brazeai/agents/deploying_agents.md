---
nav_title: Déployer des agents
article_title: Déployer des agents personnalisés
description: "Découvrez comment utiliser les agents personnalisés dans Braze après les avoir créés."
alias: /deploying-agents/
page_order: 2
---

# Déployer des agents personnalisés {#deploy-custom-agents}

> Après avoir [créé un agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/), utilisez cette page pour savoir où et comment le déployer dans Braze. Le type d'agent que vous choisissez lors de la création — agent Canvas ou agent de catalogue — détermine l'endroit où l'agent peut s'exécuter. Pour une introduction, consultez [Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/).

## Types d'agents personnalisés {#types-of-custom-agents}

Les agents personnalisés se déploient dans différentes parties de Braze selon leur type. Utilisez le tableau ci-dessous pour trouver le bon chemin de déploiement pour votre agent.

| Type d'agent | Déployé dans | S'exécute quand | Section |
| --- | --- | --- | --- |
| Agent d'étape Canvas | [Étape Agent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/) dans Canvas | Un utilisateur entre dans l'étape | [Utiliser les agents d'étape Canvas](#use-canvas-step-agents) |
| Agent de catalogue | Champ de catalogue | Une ligne de catalogue est créée ou mise à jour | [Utiliser les agents de catalogue](#use-catalog-agents) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Types d'agents personnalisés" }

Vous sélectionnez le type d'agent dans la **Console des agents** lorsque vous créez l'agent. Pour les étapes de configuration, consultez [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#step-1-choose-an-agent-type).

## Bonnes pratiques {#best-practices}

Ciblez les cas d'utilisation à forte valeur ajoutée où les agents peuvent générer le meilleur retour sur investissement (ROI), et choisissez des audiences susceptibles de répondre. Une audience plus restreinte mais à fort potentiel surpasse souvent une audience large avec peu d'opportunités.

Pour les agents Canvas, commencez par les utilisateurs qui présentent des signaux forts — comme des recherches récentes, un engagement élevé ou des données de profil riches — avant d'élargir à des segments plus larges. Pour les agents de catalogue, privilégiez les lignes où les colonnes d'entrée dont vous avez besoin sont déjà renseignées, afin que chaque invocation dispose de suffisamment de contexte pour produire un résultat utile.

Pour tester le ROI à petite échelle avant de déployer un agent à grande échelle, utilisez une étape [Chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) afin que seule une partie de votre audience entre dans la branche contenant votre étape Agent.

## Utiliser les agents d'étape Canvas {#use-canvas-step-agents}

Après avoir créé un agent Canvas, ajoutez-le à un Canvas en tant qu'étape Agent pour personnaliser les messages ou guider la prise de décision en temps réel.

### Fonctionnement {#how-it-works}

Lorsqu'un utilisateur atteint une étape Agent dans un Canvas, Braze envoie les données d'entrée que vous avez configurées à votre agent. L'agent traite l'entrée à l'aide de son modèle et de ses instructions, puis renvoie un résultat stocké dans la variable de sortie que vous avez définie dans l'étape. Vous pouvez utiliser ce résultat pour la prise de décision, la personnalisation ou le traitement en aval.

Les étapes Agent utilisent les [variables de contexte Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/) pour ingérer le contexte pertinent et produire une variable utilisable dans le Canvas. Pour les conditions préalables et une référence complète, consultez [Étape Agent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/).

### Ajouter une étape Agent {#add-an-agent-step}

Pour ajouter un agent à votre Canvas :

1. Glissez-déposez le composant **Agent** depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape et sélectionnez **Agent**.
2. Sélectionnez l'agent qui traite les données dans cette étape.
3. Définissez le nom de la variable de sortie. Le type de données de sortie est défini dans la [Console des agents]({{site.baseurl}}/user_guide/brazeai/agents/).
4. (Facultatif) Ajoutez des valeurs de contexte supplémentaires que l'agent pourra consulter lors de son exécution. Cela peut inclure des variables Liquid supplémentaires ou du contexte Canvas que vous n'avez pas encore lié dans la configuration de l'agent — par exemple, des valeurs que vous souhaitez transmettre uniquement au moment de l'envoi depuis cette étape.
5. Testez et prévisualisez le résultat de l'agent dans l'aperçu de l'étape.

Pour les types de données de sortie, le templating Liquid et les captures d'écran, consultez [Étape Agent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/).

### Cas d'utilisation {#use-cases}

| Cas d'utilisation | Description |
| --- | --- |
| Évaluation et qualification des prospects | Utilisez une étape Agent pour évaluer les prospects entrants sur une échelle (par exemple, de 1 à 10). Dirigez les utilisateurs dont le score dépasse un seuil vers des parcours de fidélisation, tout en écartant les prospects peu adaptés. |
| Personnalisation dynamique des messages | Demandez à un agent de générer des lignes d'objet, des recommandations produits ou du contenu de message en fonction des attributs utilisateur ou de leurs comportements récents. La réponse peut être insérée directement dans une étape Message. |
| Gestion des commentaires clients | Transmettez les commentaires des clients à un agent pour analyser le sentiment et générer des messages de suivi empathiques. Pour les utilisateurs à forte valeur, l'agent peut escalader la réponse ou inclure des avantages. |
| Routage intelligent | Utilisez les résultats de l'agent (booléens ou numériques) pour répartir les utilisateurs dans différents chemins Canvas. Par exemple, classez les utilisateurs comme « à risque » ou « en bonne santé » et ajustez la fréquence d'envoi des messages en conséquence. |
| Interprétation des enquêtes ou des réponses | Permettez à un agent d'analyser les réponses ouvertes d'un sondage ou les champs de texte libre, en renvoyant des valeurs structurées (par exemple, en catégorisant l'intention ou le besoin) qui déterminent les chemins en aval. |
| Raisonnement en plusieurs étapes | Configurez un agent pour combiner des champs contextuels et prendre des décisions complexes, comme recommander la meilleure action à entreprendre (e-mail, SMS ou intervention humaine) en fonction de plusieurs attributs utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'utilisation" }

### Utiliser le résultat de l'agent {#use-the-agent-output}

Après l'exécution de l'agent, utilisez la variable de sortie dans votre Canvas :

- **Routage du parcours :** Dirigez les utilisateurs vers différents chemins Canvas en fonction de la réponse de l'agent. Utilisez les [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) ou les [Arbres décisionnels]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) avec des résultats numériques, booléens ou structurés.
- **Personnalisation :** Insérez la réponse de l'agent directement dans une étape Message à l'aide de Liquid.
- **Traitement des données utilisateur :** Analysez et standardisez les données utilisateur, puis stockez-les dans le profil utilisateur (par exemple, avec une étape [Mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/)) ou envoyez-les via un webhook.

Pour des exemples, consultez [Fonctionnement]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/#how-it-works) dans Étape Agent.

### Gestion des erreurs et comportement de repli {#fallback-behavior}

Ce qui suit s'applique aux **agents d'étape Canvas** dans une [Étape Agent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/).

- Si le modèle connecté renvoie une [erreur de limite de débit]({{site.baseurl}}/user_guide/brazeai/agents/reference/#rate-limit-errors) du fournisseur LLM, Braze relance continuellement la requête en utilisant des délais exponentiels jusqu'à ce que l'appel aboutisse ou que Braze détermine qu'il ne peut pas être complété ; les utilisateurs passent ensuite à l'étape Canvas suivante.
- Pour les autres échecs (comme un délai d'attente dépassé ou une clé API invalide), la variable de sortie est définie sur `null` sauf si l'agent dispose de [valeurs de repli configurées]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#configure-fallback-values) dans la Console des agents.
- Si un agent atteint sa limite d'invocations quotidiennes, Braze applique également les valeurs de repli configurées lorsqu'elles sont présentes ; sinon, la variable de sortie est définie sur `null`.

Lorsque des valeurs de repli sont configurées, Braze les applique pour les erreurs non réessayables et pour les dépassements de limite quotidienne. Braze effectue le rendu du repli avec Liquid par utilisateur et stocke le résultat dans la variable de sortie de l'étape Agent. Sans valeurs de repli, ces échecs définissent la variable de sortie sur `null`. Si vous préférez configurer des valeurs par défaut spécifiques à l'étape dans les étapes Message plutôt que des replis dans la Console des agents, vous pouvez toujours utiliser les [valeurs Liquid par défaut]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/) en aval. Pour cela, laissez les replis vides dans la section **Output** de la configuration de l'agent afin que les valeurs par défaut Liquid puissent s'appliquer lorsque l'agent renvoie null.

- Les réponses sont mises en cache pour des entrées identiques et peuvent être réutilisées pour des invocations identiques répétées dans un délai de quelques minutes. Les réponses mises en cache comptent toujours dans le total des invocations quotidiennes.
- Les étapes Agent peuvent prendre du temps pour traiter un grand lot d'utilisateurs. Braze met les invocations en file d'attente conformément aux [contrôles de flux d'invocation]({{site.baseurl}}/user_guide/brazeai/agents/reference/#invocation-flow-controls), de sorte que les utilisateurs peuvent rester en attente lors d'envois à fort volume.

Pour la configuration de l'étape Agent et les détails d'exécution, consultez [Gestion des erreurs]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/#error-handling) dans Étape Agent. Pour plus de détails, consultez [Gestion des erreurs]({{site.baseurl}}/user_guide/brazeai/agents/#error-handling) dans Agents Braze.

## Utiliser les agents de catalogue {#use-catalog-agents}

Après avoir créé un agent de catalogue, appliquez-le à un champ de catalogue pour générer ou calculer automatiquement des valeurs pour chaque ligne. L'agent s'exécute également sur les nouvelles lignes ajoutées au catalogue à l'avenir.

### Fonctionnement

Après le lancement, l'agent s'exécute et évalue chaque ligne en intégrant les colonnes sélectionnées dans son contexte pour produire un résultat. Les agents s'exécutent sur toutes les nouvelles lignes ajoutées après le déploiement de l'agent. Si vous avez sélectionné **Recalculate when catalog rows update**, toutes les valeurs de ce champ sont mises à jour lorsque les champs source existants changent.

Lorsque vous configurez les colonnes d'entrée pour un agent de catalogue, activez le contrôle intégré au produit qui indique quelles colonnes sélectionnées sont **requises pour l'exécution** avant que l'agent ne s'invoque (les libellés peuvent varier légèrement selon l'espace de travail). Avec ce contrôle activé, choisissez le sous-ensemble de colonnes qui doivent contenir des valeurs — les colonnes sélectionnées sont requises par défaut, mais vous pouvez retirer les colonnes autorisées à rester vides sans bloquer l'agent. L'agent ignore une ligne uniquement lorsqu'une colonne que vous avez laissée comme requise est vide ou manquante — par exemple, un champ `gender` qui n'a pas été renseigné. Exécuter l'agent sans le contexte requis gaspille des jetons et peut produire des résultats de faible qualité.

Les agents de catalogue respectent également les dépendances entre colonnes. Si la colonne D est générée à partir des colonnes B et C, l'agent ne s'exécute pas sur la colonne D pour une ligne tant que B et C ne contiennent pas de valeurs pour cette ligne.

Vous pouvez actualiser et modifier les champs de votre catalogue qui utilisent des agents. Pour supprimer un agent d'une colonne, désélectionnez **Apply AI agent**. La colonne redevient alors une colonne non agentique, et les champs conservent les dernières valeurs appliquées par l'agent lors de sa dernière exécution sur le catalogue.

Les références circulaires dans les catalogues ne sont pas prises en charge, ce qui signifie que le scénario suivant ne peut pas se produire :

- La colonne agentique 1 utilise la colonne agentique 2 comme entrée
- La colonne agentique 2 utilise la colonne agentique 1 comme entrée

### Ajouter un agent à un champ de catalogue {#add-an-agent-to-a-catalog-field}

![Une étape Agent dans un champ de catalogue.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Pour ajouter un agent à votre champ de catalogue :

1. Dans votre catalogue, ajoutez un nouveau champ.
2. Sélectionnez **Apply AI agent**.
3. Affectez un agent à ce champ.
4. Sélectionnez les colonnes à transmettre en entrée. Si aucune n'est sélectionnée, l'agent aura accès à toutes les colonnes du catalogue.
5. (Facultatif) Activez **Only run when required columns have values** pour ignorer les lignes où une ou plusieurs colonnes d'entrée sélectionnées sont vides. Lorsque cette option est activée, sélectionnez lesquelles des colonnes d'entrée doivent être renseignées pour que l'agent s'exécute — toutes les colonnes sélectionnées sont requises par défaut, mais vous pouvez retirer celles qui sont autorisées à rester vides sans bloquer l'exécution.
6. Décidez si l'agent doit recalculer les champs lorsque les lignes du catalogue sont mises à jour. Si vous ne sélectionnez pas cette option, l'agent ne s'exécute qu'une seule fois par ligne.
7. Sélectionnez **Add fields** pour déployer l'agent et consulter les estimations de coûts. La fenêtre modale **Cost estimation** indique le nombre de fois que l'agent s'exécutera sur ce catalogue, soit approximativement le nombre total de lignes. Pour continuer, sélectionnez **Confirm**.

### Bonnes pratiques pour les agents de catalogue {#catalog-agent-best-practices}

Planifiez les colonnes dont l'agent a besoin avant de l'appliquer à un champ de catalogue. Après avoir activé les contrôles d'entrée requise pour le champ, sélectionnez les colonnes contenant les données que votre agent doit lire, puis décochez toute colonne susceptible de rester vide sans bloquer l'exécution. L'agent ignore une ligne uniquement lorsqu'une colonne que vous avez laissée marquée comme requise est vide.

Ne laissez pas une colonne marquée comme requise si vous vous attendez à ce qu'elle reste vide pour certaines lignes tout en souhaitant que l'agent s'exécute — retirez-la plutôt de l'ensemble requis. Ignorer les lignes incomplètes évite une utilisation incorrecte des jetons et maintient une qualité de résultat élevée.

| Scénario | Ce qui se passe |
| --- | --- |
| Lignes préremplies avec des marques substitutives | Si vous ajoutez des lignes de catalogue avec uniquement un ID et un nom de fonds, puis renseignez les autres colonnes ultérieurement, l'agent ignore ces lignes jusqu'à ce que les colonnes d'entrée requises aient des valeurs. |
| Agent appliqué après l'existence de lignes | Lorsque vous appliquez un agent à un champ d'un catalogue qui contient déjà des lignes, l'agent évalue chaque ligne mais ne s'exécute que là où les colonnes d'entrée requises sont renseignées. |
| Catalogue partiellement complet | Par exemple, un catalogue de 100 lignes où `leader` est renseigné pour les entrées 2026 mais les autres lignes ne contiennent qu'un ID et un nom de fonds avec des champs vides ailleurs. L'agent s'exécute sur les lignes ayant une valeur `leader` et ignore les lignes sans cette valeur lorsque `leader` reste requis. |
| Colonnes dépendantes | Si la colonne 3 dépend des colonnes 1 et 2, l'agent n'écrit pas dans la colonne 3 tant que les colonnes 1 et 2 n'ont pas de valeurs pour cette ligne. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bonnes pratiques pour les agents de catalogue" }

### Cas d'utilisation

| Cas d'utilisation | Description |
| --- | --- |
| Générer des descriptions de produits | Créez automatiquement des textes marketing courts pour les nouvelles entrées du catalogue, par exemple en générant une description accrocheuse à partir de données produit structurées comme le nom, la catégorie et les fonctionnalités. |
| Enrichir les attributs des produits | Complétez les valeurs manquantes telles que la famille de couleurs, le style ou la saison en vous basant sur le nom et les détails du produit. Par exemple, si le nom d'un produit est « Lunettes de soleil polarisées Laguna », l'agent pourrait attribuer le style « sport » et la famille de couleurs « bleu ». |
| Calculer les champs dérivés | Utilisez les champs existants pour générer de nouvelles données, comme un « score d'adéquation » basé sur les attributs ou une « étiquette de popularité » à partir des ventes et du nombre d'avis. |
| Catégoriser ou étiqueter les éléments | Attribuez des étiquettes pour la logique de recommandation afin que les modèles de personnalisation puissent segmenter les produits plus efficacement. Par exemple, étiquetez les produits comme « extérieur », « festival » ou « premium ». |
| Localiser le contenu | Traduisez le texte du catalogue dans une autre langue pour les campagnes internationales, ou ajustez le ton et la longueur pour les canaux spécifiques à chaque région. Par exemple, traduisez « Classic Clubmaster Sunglasses » en espagnol par « Gafas de sol Classic Clubmaster », ou raccourcissez les descriptions pour les campagnes SMS. |
| Résumer les avis ou les commentaires | Résumez le sentiment ou les commentaires dans un nouveau champ, par exemple en attribuant des scores de sentiment comme Positif, Neutre ou Négatif, ou en créant un bref résumé tel que « La plupart des clients mentionnent un excellent ajustement, mais signalent une livraison lente ». |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'utilisation" }

### Définir les champs de réponse {#define-response-fields}

Si votre agent utilise des [champs]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/?tab=fields#advanced-schemas) comme format de sortie, vous pouvez sélectionner le champ correspondant de l'agent pour **Response Field** afin de l'utiliser dans le champ du catalogue.

Supposons que vous disposiez d'un agent qui ajoute des descriptions de produits à un catalogue avec les champs suivants pour structurer le format de sortie :

| Nom du champ | Valeur |
| --- | --- |
| **description** | Texte |
| **confidence_score_out_of_ten** | Nombre |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Définir les champs de réponse" }

Vous pouvez ajouter un champ nommé **product_description** à un catalogue et sélectionner **description** comme **Response Field** pour remplir la colonne avec les descriptions de l'agent.

![Un champ « product_description » avec l'agent « Descriptor » appliqué. La sortie « description » est sélectionnée comme champ de réponse.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

Vous pouvez également remplacer manuellement la cellule générée par l'agent en sélectionnant **Edit Item** et en modifiant la description générée. Pour revenir à la description générée par l'agent, sélectionnez le symbole d'actualisation dans la cellule.

### Gestion des erreurs {#error-handling}

- Les invocations de catalogue ayant échoué ne font pas l'objet d'une nouvelle tentative, y compris lorsque le fournisseur LLM renvoie une [erreur de limite de débit]({{site.baseurl}}/user_guide/brazeai/agents/reference/#rate-limit-errors).
- Si l'appel API vers le fournisseur de modèle fondamental renvoie une autre erreur, comme une erreur de clé API invalide, la valeur du champ n'est pas mise à jour. Les agents de catalogue ne prennent pas en charge la configuration de valeurs de repli dans la Console des agents.
- Vous pouvez consulter les journaux de l'agent pour obtenir des détails sur les exécutions ayant échoué.
- Les agents de catalogue sont limités au traitement de valeurs d'entrée de 25 Ko maximum par ligne.

## Surveiller votre agent {#monitor-your-agent}

La surveillance fonctionne de la même manière, que votre agent s'exécute dans Canvas ou dans les catalogues.

Dans la section **Utilisation** de votre agent, vous pouvez consulter et accéder aux endroits où l'agent est activement utilisé dans les catalogues et les Canvas.

![Section Utilisation de l'agent affichant deux agents actifs et un agent inactif pour les Canvas.]({% image_buster /assets/img/ai_agent/agent_usage.png %})

Dans la section **Journaux** de votre agent, vous pouvez surveiller les appels réels de l'agent dans vos Canvas et catalogues. Vous pouvez filtrer par informations telles que la période, le résultat (réussite ou échec) ou l'emplacement de l'appel. Vous pouvez également sélectionner **Exporter en CSV** pour exporter uniquement les journaux affichés sur la page actuelle.

{% alert tip %}
Vous pouvez également surveiller les erreurs de limite d'invocations quotidiennes dans le [Journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/).
{% endalert %}

![Journaux pour un agent AI Sentiment Score.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

Sélectionnez **Voir** pour un appel d'agent spécifique afin de consulter l'entrée, la sortie et l'ID utilisateur.

![Le panneau de détails d'un agent Random Sports Assignment affichant l'invite d'entrée, la réponse de sortie et l'ID utilisateur associé.]({% image_buster /assets/img/ai_agent/agent_logs_view.png %})

### Utiliser Currents {#use-currents}

Vous pouvez également utiliser ces événements Currents pour accéder aux schémas d'enregistrement Kafka :

- Événements d'exécution de l'agent
- Événements d'invocation d'outils

Consultez le [glossaire des événements d'engagement liés aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) pour plus de détails.

## Articles connexes {#related-articles}

- [Étape Agent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/)
- [Article de référence pour les agents]({{site.baseurl}}/user_guide/brazeai/agents/reference/)
- [Foire aux questions]({{site.baseurl}}/user_guide/brazeai/agents/faq/)