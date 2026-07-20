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

### Quels sont les avantages du modèle Auto par rapport au modèle BYO (bring-your-own) ? {#what-are-the-benefits-of-using-auto-model-versus-bring-your-own-byo-model}

Les avantages du modèle Auto de Braze incluent :

- Aucune récupération ni saisie de clés API ou configuration d'intégration requise
- Routage automatique de chaque invocation vers le modèle le plus efficace pour accomplir la tâche

### Où puis-je consulter mon utilisation actuelle des agents ? {#where-can-i-find-my-current-agent-usage}

Accédez à **Paramètres** > **Facturation** > **Utilisation des crédits** > **Console des agents** pour consulter la consommation de crédits, le nombre d'invocations et les ratios de crédits par agent. Consultez [Limites quotidiennes d'invocations et de crédits]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits) pour plus de détails.

### Puis-je utiliser des instructions Liquid conditionnelles dans les instructions de l'agent ? {#can-i-use-conditional-liquid-statements-in-agent-instructions}

Non, tenter d'écrire des blocs Liquid comme les instructions {% raw %}`{% if %}`{% endraw %} peut entraîner une erreur de validation. Les agents peuvent gérer différents scénarios grâce à des descriptions en langage naturel dans le prompt.

### Les agents peuvent-ils accéder aux données utilisateur au-delà des attributs Liquid spécifiques ou du contexte Canvas que je leur transmets ? {#can-agents-access-user-data-beyond-the-specific-liquid-attributes-or-canvas-context-that-i-pass-to-them}

Non. Les agents ne reçoivent que les points de donnée utilisateur spécifiques qui leur sont transmis via Liquid dans les instructions, les sélections [+ Contexte de l'agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#add-resources), les [étapes de contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) en amont dans Canvas, ou le contexte supplémentaire sur l'étape Agent. Les agents ne peuvent pas rechercher dans les profils utilisateur des attributs que vous ne les avez pas configurés pour recevoir.

Les agents ne peuvent pas non plus vous avertir lorsque des données requises sont manquantes — ils poursuivent avec ce qui se trouve dans le prompt. Considérez la configuration de l'agent comme une conception délibérée entrée-sortie : transmettez chaque champ dont l'agent a besoin et vérifiez les entrées dans **Console des agents** > **Logs**. Pour des conseils, consultez [Quelles données les agents reçoivent]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

## Résolution des problèmes {#troubleshooting}

### Pourquoi mon agent n'a-t-il pas suivi mes instructions ou mes règles ? {#why-did-my-agent-not-follow-my-instructions-or-rules}

Envisagez d'utiliser [Operator]({{site.baseurl}}/user_guide/brazeai/operator) pour comprendre pourquoi votre agent ne suit pas vos instructions. Operator peut fournir des instructions étape par étape et des explications détaillées.

### Pourquoi mon agent de catalogue a-t-il ignoré certaines lignes ? {#why-did-my-catalog-agent-skip-some-rows}

Les agents de catalogue ignorent une ligne lorsqu'une colonne que vous avez marquée comme **requise pour l'exécution** est vide ou manquante — par exemple, un champ `gender` qui n'a pas été renseigné. Après avoir sélectionné les colonnes d'entrée, activez le contrôle d'entrée requise pour le champ du catalogue et choisissez les colonnes qui doivent contenir des valeurs avant que l'agent ne s'exécute ; les colonnes sélectionnées sont requises par défaut, mais vous pouvez retirer les colonnes qui peuvent rester vides sans bloquer l'invocation. Cela évite de gaspiller des jetons sur des données incomplètes.

L'agent respecte également les dépendances entre colonnes. Si une colonne de sortie dépend d'autres colonnes (par exemple, la colonne D nécessite des valeurs dans les colonnes B et C), l'agent ne s'exécute pas tant que ces colonnes en amont ne sont pas renseignées pour cette ligne.

Pour plus de détails, consultez les [bonnes pratiques pour les agents de catalogue]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

### Mon agent a du mal avec une tâche complexe. Comment puis-je améliorer ses performances ? {#subagent-approach}

Si vous constatez que l'agent a du mal avec les tâches que vous lui demandez d'accomplir, envisagez une approche par sous-agents. Par exemple, vous pourriez utiliser trois agents pour effectuer les opérations suivantes :

- L'agent 1 standardise et transforme les données de contexte Canvas entrantes non structurées.
- L'agent 2 consulte un catalogue de détails d'articles et identifie les articles potentiellement pertinents.
- L'agent 3 consulte un autre catalogue contenant différentes descriptions possibles pour chaque article et identifie la description la plus pertinente pour l'utilisateur afin de l'intégrer dans un e-mail.

### Qu'est-ce qui peut provoquer des délais d'expiration fréquents pour un agent personnalisé ? {#what-might-cause-a-custom-agent-to-frequently-time-out}

Un agent personnalisé peut expirer si :

- Les instructions de l'agent sont incomplètes ou contradictoires
- Les instructions de l'agent ne couvrent pas tous les scénarios ou n'incluent pas de condition de repli (par exemple, « Si toutes les entrées sont vides, renvoyer "Could not personalize" »)
- Les instructions de l'agent demandent un format de sortie différent de celui spécifié dans l'onglet **Sortie** (par exemple, si les instructions demandent une chaîne de caractères, mais que dans l'onglet **Sortie**, la sortie est définie comme un nombre)
- La tâche de l'agent est trop complexe et gagnerait à adopter une [approche par sous-agents](#subagent-approach)

Pour les agents d'étape Canvas, configurez des [valeurs de repli]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) dans la Console des agents afin que les utilisateurs reçoivent tout de même une sortie lorsqu'une invocation échoue.

### Pourquoi mon agent fonctionnait-il bien en test mais ne reçoit-il aucune donnée utilisateur spécifique lorsque je le lance dans un Canvas ? {#why-did-my-agent-do-fine-in-testing-but-isnt-getting-any-user-specific-data-when-i-launch-it-in-a-canvas}

Si votre agent fonctionne correctement pendant les tests mais ne reçoit pas de données utilisateur spécifiques dans un Canvas en production, essayez les étapes de résolution suivantes :

- Assurez-vous que les données utilisateur spécifiques que vous souhaitez transmettre à l'agent sont saisies en tant que variables Liquid dans les instructions de l'agent.
- Si vous disposez de données importantes dans le contexte Canvas, utilisez l'option **Ajouter tout le contexte Canvas** dans la configuration de l'agent pour vous assurer que l'agent reçoit l'intégralité du contexte Canvas.
- Assurez-vous que tout contexte Canvas auquel vous souhaitez que l'agent accède est stocké en tant que contexte Canvas. Utilisez une étape de contexte avant l'étape Agent pour stocker ces données.

## Conformité {#compliance}

### La Console des agents est-elle conforme au RGPD/CCPA ? {#is-agent-console-gdprccpa-compliant}

Oui. Lorsqu'un client utilise le modèle Auto de Braze (propulsé par Gemini), Google agit en tant que sous-traitant de Braze, soumis aux conditions de l'accord de traitement des données (DPA) entre le client et Braze.

### La Console des agents est-elle conforme à la loi HIPAA ? {#is-agent-console-hipaa-compliant}

Oui. Lors de l'utilisation du modèle Auto de Braze, nous disposons d'un accord HIPAA spécifique, le Business Associate Addendum (BAA), avec Google couvrant Gemini, qui alimente notre modèle Auto.

Notre BAA s'applique uniquement aux clients utilisant le modèle Auto de Braze. Si les clients utilisent leur propre clé LLM, Braze n'envoie pas d'informations de santé protégées (PHI) soumises à la loi HIPAA à un LLM en leur nom ; les clients les envoient directement. Dans ce cas, le BAA entre Braze et Google ne s'applique pas. Le traitement des données via leur propre clé LLM est régi par le contrat du client et tout BAA qu'il a conclu directement avec son fournisseur de LLM.