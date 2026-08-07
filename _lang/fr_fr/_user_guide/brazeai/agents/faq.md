---
nav_title: FAQ
article_title: FAQ sur les agents
description: "Cet article répond aux questions fréquemment posées sur les agents Braze."
page_order: 10
toc_headers: h2
---

# Questions fréquemment posées sur les agents {#agents-frequently-asked-questions}

> Cet article répond aux questions fréquemment posées sur les agents Braze.

## Général {#general}

### Quelle est la différence entre les agents d'étape Canvas et les agents de catalogue ? {#what-is-the-difference-between-canvas-step-agents-and-catalog-agents}

Lorsque vous créez un agent, vous indiquez si vous souhaitez créer un agent d'étape Canvas ou un agent de catalogue. Ce choix détermine les types d'instructions et d'options que l'agent peut prendre en charge. Les agents d'étape Canvas traitent les utilisateurs en temps réel au sein des parcours, tandis que les agents de catalogue enrichissent les données du catalogue en ajoutant ou en mettant à jour des colonnes avec des informations traitées.

### Quels sont les avantages du modèle automatique par rapport au modèle personnalisé (BYO) ? {#what-are-the-benefits-of-using-auto-model-versus-bring-your-own-byo-model}

Les avantages du modèle automatique de Braze comprennent :

- Aucune récupération ni saisie de clés API ou de configuration d'intégration requise
- Routage automatique de chaque invocation vers le modèle le plus efficace pour la tâche

### Où puis-je consulter mon utilisation actuelle des agents ? {#where-can-i-find-my-current-agent-usage}

Accédez à **Paramètres** > **Facturation** > **Utilisation des crédits** > **Agent Console** pour consulter la consommation de crédits, le nombre d'invocations et les ratios de crédits par agent. Consultez [Limites quotidiennes d'invocations et de crédits]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits) pour plus de détails.

### Puis-je utiliser des instructions Liquid conditionnelles dans les instructions de l'agent ? {#can-i-use-conditional-liquid-statements-in-agent-instructions}

Non, tenter d'écrire des blocs Liquid comme des instructions {% raw %}`{% if %}{% endraw %}` peut entraîner une erreur de validation. Les agents peuvent gérer différents scénarios grâce à des descriptions en langage naturel dans le prompt.

### Les agents peuvent-ils accéder aux données utilisateur au-delà des attributs Liquid spécifiques ou du contexte Canvas que je leur transmets ? {#can-agents-access-user-data-beyond-the-specific-liquid-attributes-or-canvas-context-that-i-pass-to-them}

Non. Les agents ne reçoivent que les points de données utilisateur spécifiques qui leur sont transmis via Liquid dans les instructions, les sélections [+ Contexte de l'agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#add-resources), les [étapes de contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) en amont dans Canvas, ou le contexte supplémentaire sur l'étape Agent. Les agents ne peuvent pas rechercher dans les profils utilisateur des attributs que vous ne les avez pas configurés pour recevoir.

Les agents ne peuvent pas non plus vous avertir lorsque des données requises sont manquantes : ils poursuivent avec ce qui se trouve dans le prompt. Considérez la configuration de l'agent comme une conception délibérée entrée-sortie : transmettez chaque champ dont l'agent a besoin et vérifiez les entrées dans **Agent Console** > **Logs**. Pour des conseils, consultez [Quelles données les agents reçoivent]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

## Résolution des problèmes {#troubleshooting}

### Pourquoi mon agent n'a-t-il pas suivi mes instructions ou mes règles ? {#why-did-my-agent-not-follow-my-instructions-or-rules}

Envisagez d'utiliser [Operator]({{site.baseurl}}/user_guide/brazeai/operator) pour comprendre pourquoi votre agent ne suit pas vos instructions. Operator peut fournir des instructions étape par étape et des explications détaillées.

### Pourquoi mon agent de catalogue a-t-il ignoré certaines lignes ? {#why-did-my-catalog-agent-skip-some-rows}

Les agents de catalogue ignorent une ligne lorsqu'une colonne que vous avez marquée comme **obligatoire pour l'exécution** est vide ou manquante — par exemple, un champ `gender` qui n'a pas été renseigné. Après avoir sélectionné les colonnes d'entrée, activez le contrôle d'entrée obligatoire pour le champ du catalogue et choisissez les colonnes qui doivent contenir des valeurs avant que l'agent ne s'exécute ; les colonnes sélectionnées sont obligatoires par défaut, mais vous pouvez retirer les colonnes qui peuvent rester vides sans bloquer l'invocation. Cela évite de gaspiller des jetons sur des données incomplètes.

L'agent respecte également les dépendances entre colonnes. Si une colonne de sortie dépend d'autres colonnes (par exemple, la colonne D nécessite des valeurs dans les colonnes B et C), l'agent ne s'exécute pas tant que ces colonnes en amont ne sont pas renseignées pour cette ligne.

Pour plus de détails, consultez les [bonnes pratiques pour les agents de catalogue]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

### Les invocations d'agent échouées consomment-elles des crédits ? {#do-failed-agent-invocations-consume-credits}

Cela dépend du type d'échec :

| Échec | Consomme des crédits ? |
| --- | --- |
| Erreur de limitation du débit | Non |
| Modèle indisponible | Non |
| Limite d'invocations quotidiennes atteinte | Non |
| Expiration du délai | Oui |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Les invocations d'agent échouées consomment-elles des crédits ?" }

Consultez [Quand les crédits sont consommés]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed) pour plus de détails.

### Mon agent a du mal avec une tâche complexe. Comment puis-je améliorer ses performances ? {#subagent-approach}

Si vous constatez que l'agent a du mal avec les tâches que vous lui demandez d'effectuer, envisagez une approche par sous-agents. Par exemple, vous pourriez utiliser trois agents pour effectuer les opérations suivantes :

- L'agent 1 standardise et transforme les données de contexte Canvas non structurées entrantes.
- L'agent 2 consulte un catalogue de détails d'articles et identifie les articles potentiellement pertinents.
- L'agent 3 consulte un catalogue différent contenant diverses descriptions possibles pour chaque article et identifie la description d'article la plus pertinente pour l'utilisateur afin de l'insérer dans un e-mail.

### Qu'est-ce qui pourrait provoquer des expirations de délai fréquentes pour un agent personnalisé ? {#what-might-cause-a-custom-agent-to-frequently-time-out}

Un agent personnalisé peut expirer si :

- Les instructions de l'agent sont incomplètes ou contradictoires
- Les instructions de l'agent ne couvrent pas tous les scénarios ou n'incluent pas de condition de repli (comme « Si toutes les entrées sont vides, renvoyer 'Impossible de personnaliser' »)
- Les instructions de l'agent demandent un format de sortie différent de celui spécifié dans l'onglet **Output** (par exemple, si les instructions demandent une chaîne de caractères, mais que dans l'onglet **Output** la sortie est définie comme un nombre)
- La tâche de l'agent est trop complexe et bénéficierait d'une [approche par sous-agents](#subagent-approach)

#### Comment réduire les expirations de délai {#how-to-reduce-timeouts}

Si votre agent expire souvent, essayez les solutions suivantes avant de contacter votre gestionnaire de compte pour demander une limite de délai plus élevée :

- **Choisissez un modèle plus simple ou moins coûteux :** les modèles plus rapides terminent généralement dans la fenêtre de délai par défaut. Consultez [Déterminer quel modèle utiliser]({{site.baseurl}}/user_guide/brazeai/agents/reference#determine-which-model-to-use).
- **Réduisez le niveau de réflexion (modèles BYO uniquement) :** commencez à **Faible** et augmentez uniquement si la qualité de la sortie en souffre. Consultez [Niveaux de réflexion]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels).
- **Simplifiez le prompt :** supprimez les instructions redondantes, raccourcissez les exemples et réduisez le schéma de sortie. Utilisez [Operator]({{site.baseurl}}/user_guide/brazeai/operator) pour examiner et affiner vos instructions.
- **Divisez les workflows complexes en plusieurs agents :** si le cas d'usage comporte plusieurs sous-étapes (par exemple, classifier l'intention, puis générer le texte), utilisez des agents distincts en séquence dans Canvas ou dans le catalogue au lieu d'un seul agent qui fait tout. Consultez l'[approche par sous-agents](#subagent-approach).

{% alert note %}
Les expirations de délai consomment des crédits Braze même lorsque l'agent ne renvoie aucune sortie exploitable. Consultez [Quand les crédits sont consommés]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed).
{% endalert %}

Pour les agents d'étape Canvas, configurez des [valeurs de repli]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) dans la console d'agent afin que les utilisateurs reçoivent tout de même une sortie lorsqu'une invocation échoue.

### Pourquoi mon agent a-t-il bien fonctionné en test mais ne reçoit-il aucune donnée spécifique à l'utilisateur lorsque je le lance dans un Canvas ? {#why-did-my-agent-do-fine-in-testing-but-isnt-getting-any-user-specific-data-when-i-launch-it-in-a-canvas}

Si votre agent fonctionne correctement pendant les tests mais ne reçoit pas de données spécifiques à l'utilisateur dans un Canvas en direct, essayez les étapes de résolution suivantes :

- Assurez-vous que les données spécifiques à l'utilisateur que vous souhaitez transmettre à l'agent sont saisies sous forme de variables Liquid dans les instructions de l'agent.
- Si vous avez des données importantes dans le contexte Canvas, utilisez l'option **Add all Canvas context** dans la configuration de l'agent pour vous assurer que l'agent reçoit l'intégralité du contexte Canvas.
- Assurez-vous que tout contexte Canvas auquel vous souhaitez que l'agent accède est stocké en tant que contexte Canvas. Utilisez une étape de contexte avant l'étape de l'agent pour stocker ces données.

## Conformité {#compliance}

### Agent Console est-il conforme au RGPD/CCPA ? {#is-agent-console-gdprccpa-compliant}

Oui. Lorsqu'un client utilise le modèle Braze Auto (propulsé par Gemini), Google agit en tant que sous-traitant de Braze, soumis aux conditions de l'accord de traitement des données (DPA) entre le client et Braze.

### Agent Console est-il conforme à la HIPAA ? {#is-agent-console-hipaa-compliant}

Oui. Lors de l'utilisation du modèle Braze Auto, nous disposons d'un accord HIPAA spécifique, le Business Associate Addendum (BAA), avec Google couvrant Gemini, qui alimente notre modèle Auto.

Notre BAA s'applique uniquement aux clients utilisant le modèle Braze Auto. Si les clients utilisent leur propre clé LLM, Braze n'envoie pas d'informations de santé protégées (PHI) soumises à la HIPAA à un LLM en leur nom ; les clients les envoient directement. Dans ce cas, le BAA entre Braze et Google ne s'applique pas. Le traitement des données via leur propre clé LLM est régi par le contrat du client et tout BAA qu'il a conclu directement avec son fournisseur de LLM.