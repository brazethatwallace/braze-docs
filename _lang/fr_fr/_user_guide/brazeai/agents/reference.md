---
nav_title: Article de référence
article_title: Référence des agents
description: "Retrouvez les détails clés sur les agents de Braze."
page_order: 3
---

# Référence des agents {#reference-for-agents}

> Lorsque vous créez des agents personnalisés, reportez-vous à cet article pour en savoir plus sur les paramètres clés, tels que les instructions et les schémas de sortie. Pour une configuration étape par étape, consultez [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents). Pour une introduction, consultez [Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents) et la [Foire aux questions]({{site.baseurl}}/user_guide/brazeai/agents/faq).

## Modèles {#models}

Lorsque vous configurez un agent, vous pouvez choisir le modèle qu'il utilise pour générer des réponses. Vous avez deux options : utiliser un modèle fourni par Braze ou apporter votre propre clé API.

{% alert important %}
Le modèle **Auto** fourni par Braze est optimisé pour les modèles dont les capacités de raisonnement sont suffisantes pour effectuer des tâches telles que la recherche dans les catalogues et l'appartenance à un Segment. Lorsque vous utilisez d'autres modèles, nous vous recommandons de tester pour confirmer que votre modèle fonctionne bien pour votre cas d'usage. Vous devrez peut-être ajuster vos [instructions](#writing-instructions) pour fournir différents niveaux de détail ou de raisonnement étape par étape aux modèles ayant différentes vitesses et capacités.
{% endalert %}

### Option 1 : Utiliser un modèle fourni par Braze {#option-1-use-a-braze-powered-model}

C'est l'option la plus simple, sans configuration supplémentaire requise. Braze fournit un accès direct aux grands modèles de langage (LLM). Pour utiliser cette option, sélectionnez **Auto**, qui utilise les modèles Gemini.

{% alert important %}
Si vous ne voyez pas **Braze Auto** comme option dans le menu déroulant **Model** lors de la création d'un agent, contactez votre gestionnaire du succès des clients pour savoir comment devenir éligible à l'utilisation du modèle Braze Auto.
{% endalert %}

### Option 2 : Apporter votre propre clé API {#option-2-bring-your-own-api-key}

Avec cette option, vous pouvez connecter votre compte Braze à des fournisseurs tels qu'OpenAI, Anthropic ou Google Gemini. Si vous apportez votre propre clé API d'un fournisseur de LLM, les coûts des jetons sont facturés directement par votre fournisseur, et non par Braze.

Nous vous recommandons de tester régulièrement les modèles les plus récents, car les modèles anciens peuvent être abandonnés ou dépréciés après quelques mois. Assurez-vous de disposer de crédits suffisants auprès de votre fournisseur pour exécuter vos agents à grande échelle. Vous pouvez également vous inscrire aux notifications de l'Agent Console dans les [Préférences de notification]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) pour être alerté lorsque Braze détecte qu'un modèle n'est plus disponible ou rencontre des problèmes de facturation avec votre fournisseur de LLM.

Pour configurer cela :

1. Allez dans **Partner Integrations** > **Technology Partners** et trouvez votre fournisseur.
2. Saisissez votre clé API du fournisseur.
3. Sélectionnez **Enregistrer**.

Ensuite, vous pouvez revenir à votre agent et sélectionner votre modèle.

Lorsque vous utilisez un LLM fourni par Braze, les fournisseurs de ce modèle agissent en tant que sous-traitants de Braze, soumis aux conditions de l'Addendum sur le traitement des données (DPA) entre vous et Braze. Si vous choisissez d'apporter votre propre clé API, le fournisseur de votre abonnement LLM est considéré comme un fournisseur tiers dans le cadre du contrat entre vous et Braze.

#### Niveaux de raisonnement {#thinking-levels}

Certains fournisseurs de LLM peuvent vous permettre d'ajuster le niveau de raisonnement d'un modèle sélectionné. Les niveaux de raisonnement définissent l'étendue de la réflexion que le modèle utilise avant de répondre — des réponses rapides et directes aux chaînes de raisonnement plus longues. Cela affecte la qualité des réponses, la latence et l'utilisation des jetons.

| Niveau | Quand l'utiliser |
|--------|------------------|
| **Faible** | Tâches simples et bien définies (comme la recherche dans un catalogue, la classification simple). Réponses les plus rapides et coût le plus bas. |
| **Faible** | Tâches qui bénéficient d'un peu plus de raisonnement mais ne nécessitent pas d'analyse approfondie. |
| **Moyen** | Tâches à plusieurs étapes ou nuancées (comme l'analyse de plusieurs entrées pour recommander une action). |
| **Élevé** | Raisonnement complexe, cas particuliers, ou lorsque vous avez besoin que le modèle détaille ses étapes avant de répondre. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Niveaux de raisonnement" }

Nous vous recommandons de commencer avec le niveau **Faible** et de tester les réponses de votre agent. Ensuite, vous pouvez ajuster le niveau de raisonnement à **Faible** ou **Moyen** si vous constatez que l'agent a du mal à fournir des réponses précises. Dans de rares cas, un niveau de raisonnement **Élevé** peut être nécessaire, bien que l'utilisation de ce niveau puisse entraîner des coûts élevés en jetons et des temps de réponse plus longs ou un risque accru d'[erreurs de dépassement de délai]({{site.baseurl}}/user_guide/brazeai/agents/faq#what-might-cause-a-custom-agent-to-frequently-time-out). Si votre agent peine à équilibrer le raisonnement à plusieurs étapes avec des temps de réponse raisonnables, envisagez de diviser votre cas d'usage en plusieurs agents pouvant travailler ensemble dans un Canvas ou un catalogue.

Braze utilise les mêmes plages d'adresses IP pour les appels LLM sortants que pour le contenu connecté. Les plages sont répertoriées dans la [liste d'autorisation des adresses IP du contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting). Si votre fournisseur prend en charge l'autorisation par adresse IP, vous pouvez restreindre la clé à ces plages afin que seul Braze puisse l'utiliser.

{% alert important %}
Lorsque vous utilisez un LLM fourni par Braze, les fournisseurs de ce modèle agissent en tant que sous-traitants de Braze, soumis aux conditions de l'Addendum sur le traitement des données (DPA) entre vous et Braze. Si vous choisissez d'apporter votre propre clé API, le fournisseur de votre abonnement LLM est considéré comme un fournisseur tiers dans le cadre du contrat entre vous et Braze.
{% endalert %}

#### Déterminer quel modèle utiliser {#determine-which-model-to-use}

Chaque fournisseur de LLM propose une combinaison légèrement différente de capacités de modèle, de coûts et de niveaux de raisonnement. Voici quelques lignes directrices générales et bonnes pratiques :

- Pour l'efficacité des coûts, privilégiez le test de modèles à faible coût en jetons par rapport aux modèles plus coûteux. N'ajustez vers des modèles plus coûteux que si les modèles moins coûteux peinent avec le cas d'usage ou génèrent des résultats incohérents ou imprécis.
- Pour l'efficacité de la vitesse et des performances, privilégiez le test de niveaux de raisonnement plus faibles par rapport aux niveaux plus élevés. N'ajustez vers des niveaux de raisonnement plus élevés que si les niveaux plus faibles peinent avec le cas d'usage ou génèrent des résultats incohérents ou imprécis.
- Si les modèles ou niveaux de raisonnement moins coûteux peinent avec le cas d'usage ou génèrent des résultats incohérents ou imprécis, envisagez de passer à des modèles ou niveaux de raisonnement plus coûteux.
- Pendant les tests, assurez-vous d'équilibrer la fiabilité et la précision avec l'utilisation des jetons et la durée d'invocation.
- Chaque cas d'usage peut avoir un modèle et un niveau de raisonnement optimaux différents. Nous vous recommandons de tester minutieusement pour vérifier une qualité constante sans dépassement de délai.

### Contrôles du flux d'invocation {#invocation-flow-controls}

Les contrôles de flux d'invocation suivants s'appliquent par espace de travail :

- **Modèle fourni par Braze :** 5 000 invocations par minute
- **Apport de votre propre clé API :** 5 000 invocations par minute

Lorsque de nombreux utilisateurs entrent dans une étape Agent simultanément, Braze met les invocations en file d'attente selon ces limites, de sorte que le traitement peut prendre plus de temps lors d'envois à fort volume.

### Limites quotidiennes d'invocations et de crédits {#daily-invocation-and-credit-limits}

Chaque agent dispose d'une limite quotidienne d'invocations (250 000 par défaut ; 1 000 000 maximum sauf si votre contrat permet davantage). Chaque invocation (y compris les aperçus de l'Agent Console et les exécutions de Canvas de test utilisant **Simulate response**) est comptabilisée dans cette limite.

Dans l'Agent Console, la **Daily action credit cost limit** estime le maximum de crédits qu'un agent peut consommer par jour. Braze multiplie le ratio de crédits par invocation de votre espace de travail pour le modèle sélectionné par la limite quotidienne d'invocations.

### Quand les crédits sont consommés {#when-credits-are-consumed}

Braze ne facture des crédits que pour les invocations qui terminent leur traitement. Les crédits ne sont pas consommés lorsqu'une invocation échoue en raison de :

- Une [erreur de limitation du débit](#rate-limit-errors) du fournisseur de LLM (y compris les tentatives qui échouent finalement)
- L'indisponibilité du modèle sélectionné
- L'atteinte par l'agent de sa limite quotidienne d'invocations

Les crédits sont consommés lorsqu'une invocation expire, même si l'agent ne renvoie pas de résultat exploitable.

### Surveiller l'utilisation des crédits {#monitor-credit-usage}

Allez dans **Settings** > **Billing** > **Credits Usage** > **Agent Console** pour consulter la consommation de crédits, le nombre d'invocations et les ratios de crédits par agent.

Les ratios de crédits proviennent de votre contrat et apparaissent sur le tableau de bord [Credits Usage]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage) (onglet **Credit Ratios** et onglet **Agent Console**). L'estimation se met à jour lorsque vous modifiez le modèle ou la limite d'invocations.

Pour gérer les dépenses, réduisez la limite quotidienne d'invocations. Pour les modèles [BYO (apport de votre propre clé)](#option-2-bring-your-own-api-key), vous pouvez également choisir un modèle moins coûteux ou réduire le [niveau de raisonnement](#thinking-levels) pour diminuer les coûts en jetons du fournisseur. Braze Auto ne prend pas en charge l'ajustement du niveau de raisonnement.

### Erreurs de limitation du débit {#rate-limit-errors}

Si le fournisseur de LLM renvoie une erreur de limitation du débit lors d'une invocation d'Agent Canvas Step ou d'Agent Catalog, Braze retente continuellement la requête en utilisant des délais exponentiels jusqu'à ce que l'appel réussisse ou que Braze détermine qu'il ne peut pas être complété.

Lorsque les tentatives de Canvas ou de catalogue sont épuisées, le panneau de détails des **Logs** affiche **Error** et le message du fournisseur (tel que `Rate limit exceeded`) dans **Output**. Les tentatives sont visibles dans les journaux, y compris la toute première invocation indépendamment de son succès ou échec final. Pour un utilisateur donné, s'il faut quatre tentatives pour finalement obtenir un succès, vous pouvez rechercher l'ID utilisateur et voir les cinq entrées (l'originale plus les quatre tentatives) dans les **Logs**, et l'originale plus les trois premières tentatives afficheront **Error** avec `Rate limit exceeded`.

Les erreurs de limitation du débit ne consomment pas de crédits Braze, y compris les tentatives échouées affichées dans les **Logs**.

![Détails du journal de l'Agent Console montrant une erreur de dépassement de limite du débit dans le champ Output.]({% image_buster /assets/img/ai_agent/rate_limit_error_log.png %}){: style="max-width:75%;"}

## Instructions de rédaction {#writing-instructions}

Les instructions sont les règles ou directives que vous donnez à l'agent (prompt système). Elles définissent comment l'agent doit se comporter à chaque exécution. Les instructions système peuvent atteindre 25 Ko.

Si vous avez créé votre agent avec [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) à l'aide d'un [modèle de départ]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator), passez en revue les instructions pré-remplies et modifiez-les selon vos besoins.

Voici quelques bonnes pratiques générales pour vous aider à démarrer avec la rédaction de prompts :

1. Commencez par la fin en tête. Énoncez d'abord l'objectif.
2. Donnez au modèle un rôle ou un persona (« Vous êtes un… »).
3. Définissez un contexte et des contraintes clairs (audience, longueur, ton, format).
4. Demandez une structure (« Renvoyez du JSON/une liste à puces/un tableau… »).
5. Montrez, ne dites pas. Incluez quelques exemples de haute qualité.
6. Décomposez les tâches complexes en étapes ordonnées (« Étape 1… Étape 2… »).
7. Encouragez le raisonnement (« Réfléchissez aux étapes en interne, puis fournissez une réponse finale concise » ou « expliquez brièvement votre décision »).
8. Testez, inspectez et itérez. De petits ajustements peuvent entraîner de grands gains de qualité.
9. Gérez les cas limites, ajoutez des garde-fous et des instructions de refus.
10. Mesurez et documentez ce qui fonctionne en interne pour la réutilisation et la mise à l'échelle.

### Exemples {#examples}

Pour les configurations de départ dans Agent Console, consultez [Modèles d'agents créés avec Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).

Pour des exemples complets d'instructions que vous pouvez copier ou adapter, consultez la [bibliothèque de cas d'usage pour les Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/examples).

| Exemple | Catégorie | Type d'agent | Ce qu'il fait |
| --- | --- | --- | --- |
| [Rédiger des messages personnalisés en fonction du contexte d'un utilisateur]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-personalized-messaging-based-on-a-users-context) | Génération de contenu | Canvas Step Agent | Génère un objet/accroche d'e-mail et un titre/corps de notification push coordonnés pour les utilisateurs qui ont effectué une recherche sans réserver. |
| [Analyser les retours utilisateurs pour déterminer les prochaines étapes]({{site.baseurl}}/user_guide/brazeai/agents/examples#analyze-user-feedback-to-determine-next-steps) | Standardisation des données | Canvas Step Agent | Classifie le sentiment et le sujet d'une enquête post-voyage, puis recommande une prochaine étape CRM. |
| [Catégoriser les utilisateurs en compartiments d'intérêt à partir des attributs existants]({{site.baseurl}}/user_guide/brazeai/agents/examples#categorize-users-into-interest-buckets-from-existing-attributes) | Agent d'affinité | Canvas Step Agent | Classifie les utilisateurs en compartiments d'intérêt à partir des attributs et des signaux de forte intention, puis recommande la meilleure prochaine expérience ou le meilleur élément. |
| [Orienter les utilisateurs vers le chemin Canvas le plus pertinent à partir du comportement récent]({{site.baseurl}}/user_guide/brazeai/agents/examples#route-users-to-the-most-relevant-canvas-path-from-recent-behavior) | Agent d'affinité | Canvas Step Agent | Déduit la motivation à partir du comportement récent et renvoie la meilleure clé de route pour la prochaine étape Canvas de l'utilisateur. |
| [Attribuer des catégories d'intérêt aux utilisateurs à partir d'actions récentes de forte intention]({{site.baseurl}}/user_guide/brazeai/agents/examples#assign-users-to-interest-categories-from-real-time-high-intent-actions) | Agent d'affinité | Canvas Step Agent | Attribue des catégories d'intérêt à partir d'actions de forte intention et recommande la meilleure prochaine expérience ou le meilleur élément. |
| [Classifier les messages entrants pour détecter une intention de désabonnement]({{site.baseurl}}/user_guide/brazeai/agents/examples#classify-inbound-messages-for-opt-out-intent) | Classification et routage | Canvas Step Agent | Renvoie un booléen strict indiquant si un message est une demande de désabonnement. |
| [Standardiser les messages entrants en données structurées pour l'automatisation]({{site.baseurl}}/user_guide/brazeai/agents/examples#standardize-inbound-messages-into-structured-data-for-automation) | Standardisation des données | Canvas Step Agent | Normalise les SMS ou chats entrants en intention structurée, entités et indicateurs de conformité pour l'automatisation en aval. |
| [Rédiger des descriptions à fort taux de conversion conformes aux directives de marque]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-high-converting-descriptions-that-align-with-brand-guidelines) | Génération de contenu | Catalog Agent | Génère des descriptions courtes et conformes à la marque pour chaque ligne du catalogue. |
| [Fournir des traductions basées sur la langue utilisée par région]({{site.baseurl}}/user_guide/brazeai/agents/examples#provide-translations-based-on-language-used-by-region) | Enrichissement de catalogue | Catalog Agent | Localise les chaînes d'interface et de marketing par locale et limite de caractères. |
| [Enrichir les éléments de catalogue avec des descriptions, des catégories et des tags]({{site.baseurl}}/user_guide/brazeai/agents/examples#enrich-catalog-items-with-descriptions-categories-and-tags) | Enrichissement de catalogue | Catalog Agent | Génère des descriptions améliorées, des catégories et des tags à partir des données existantes des éléments de catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Résumé des exemples" }

### Utiliser Liquid {#using-liquid}

Inclure du [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) dans les instructions de votre agent peut ajouter un niveau supplémentaire de personnalisation dans sa réponse. Vous pouvez spécifier la variable Liquid exacte que l'agent reçoit et l'inclure dans le contexte de votre prompt. Par exemple, au lieu d'écrire explicitement « prénom », vous pouvez utiliser l'extrait Liquid {% raw %}`{{${first_name}}}`{% endraw %} :

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

Dans la section **Logs** de l'**Agent Console**, vous pouvez consulter les détails des entrées et sorties de l'agent pour comprendre quelle valeur est rendue à partir du Liquid.

### Quelles données les agents reçoivent {#what-data-agents-receive}

Le contexte d'un agent n'est pas une mémoire conversationnelle ouverte. Contrairement à un assistant de chat, un agent ne voit que les données que vous lui transmettez explicitement au moment de l'invocation — il ne parcourt pas les profils utilisateur, ne déduit pas les champs manquants et ne vous signale pas l'absence d'informations requises.

Concevez chaque agent comme un pipeline délibéré d'entrée vers sortie. Connectez chaque point de données dont l'agent a besoin en utilisant une ou plusieurs des méthodes suivantes :

1. **Liquid dans les instructions :** Intégrez les attributs utilisateur ({% raw %}`{{${first_name}}}`{% endraw %}) et les [variables de contexte Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) ({% raw %}`{{context.${variable_name}}}`{% endraw %}) directement dans le prompt de l'agent.
2. **+ Agent context :** Sélectionnez des catalogues, l'appartenance à un Segment, les directives de marque, **All Canvas Context** ou les données d'interaction utilisateur dans Agent Console.
3. [Étapes de contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) : Définissez ou mettez à jour les variables `context.*` en amont dans le Canvas avant l'exécution d'une étape Agent.
4. **Contexte supplémentaire sur l'étape Agent :** Transmettez toute valeur supplémentaire modélisée avec Liquid non encore spécifiée par les autres méthodes à l'agent au moment de l'envoi depuis la configuration de l'étape.

Assurez-vous soit d'intégrer ces variables de contexte via un modèle Liquid dans les instructions de l'agent, soit de sélectionner **Add All Canvas Context**. Si une valeur n'est pas transmise par l'un de ces canaux, l'agent ne la reçoit pas. Listez les entrées requises dans vos instructions ou dans les [prérequis des cas d'usage]({{site.baseurl}}/user_guide/brazeai/agents/examples), et vérifiez les entrées dans **Agent Console** > **Logs** après les tests.

![Les détails d'un agent dont les instructions contiennent du Liquid.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

Pour les Catalog Agents, utilisez les **Fields** dans la section **Output** plutôt qu'un schéma JSON ; vous pouvez toujours rédiger des instructions demandant au modèle une sortie clé-valeur correspondant à ces noms de champs.

Pour plus de détails sur les bonnes pratiques de prompting, consultez les guides des fournisseurs de modèles suivants :

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## Sorties {#outputs}

Si vous avez créé votre agent avec [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) à l'aide d'un [modèle de départ]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator), vérifiez le schéma de sortie prérempli et modifiez-le si nécessaire.

### Schémas de base {#basic-schemas}

Les schémas de base sont une sortie simple qu'un agent renvoie. Il peut s'agir d'une chaîne de caractères, d'un nombre, d'un booléen, d'un tableau de chaînes de caractères ou d'un tableau de nombres.

Par exemple, si vous souhaitez recueillir des scores de satisfaction utilisateur à partir d'une enquête de feedback simple pour déterminer le niveau de satisfaction de vos clients après avoir reçu un produit, vous pouvez sélectionner **Number** comme schéma de base pour structurer le format de sortie.

{% alert important %}
Les tableaux sont uniquement disponibles pour les agents d'étapes Canvas, et non pour les agents de catalogue.
{% endalert %}

![Console de l'agent avec le type number sélectionné comme schéma de base.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

### Schémas avancés {#advanced-schemas}

Les options de schéma avancé comprennent la structuration manuelle des champs ou l'utilisation de JSON.

- **Fields :** Une approche sans code pour imposer un format de sortie d'agent que vous pouvez utiliser de manière cohérente.
- **JSON :** Une approche basée sur le code pour créer un format de sortie précis, où vous pouvez imbriquer des variables et des objets dans le schéma JSON. Uniquement disponible pour les agents d'étapes Canvas, et non pour les agents de catalogue.

Nous recommandons d'utiliser les schémas avancés lorsque vous souhaitez que l'agent renvoie une structure de données avec plusieurs valeurs définies de manière structurée, plutôt qu'une sortie à valeur unique. Cela permet de mieux formater la sortie en tant que variable de contexte cohérente.

### Sortie de secours {#fallback-output}

Les valeurs de secours sont disponibles uniquement pour les agents d'étapes Canvas. Dans la section **Output** de la console de l'agent pour un agent d'étape Canvas, vous pouvez définir les valeurs que Braze utilise lorsqu'une invocation échoue.

Pour les schémas **JSON**, Braze lit le schéma et génère un champ de saisie pour chaque propriété afin que vous puissiez définir une valeur de secours par clé. Pour les schémas **Fields**, vous saisissez une valeur de secours pour chaque champ. Pour les schémas de base, vous saisissez une seule valeur de secours. Les agents d'étapes Canvas prennent en charge Liquid dans les valeurs de secours.

Pour les étapes de configuration, consultez [Configurer les valeurs de secours]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values). Pour le comportement à l'exécution dans Canvas, consultez [Gestion des erreurs et comportement de secours]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior).

Par exemple, vous pouvez utiliser un format de sortie au sein d'un agent destiné à créer un exemple d'itinéraire de voyage pour un utilisateur en fonction d'un formulaire qu'il a soumis. Le format de sortie vous permet de définir que chaque réponse de l'agent doit inclure des valeurs pour `tripStartDate`, `tripEndDate` et `destination`. Chacune de ces valeurs peut être extraite des variables de contexte et placée dans une étape Message pour la personnalisation à l'aide de Liquid.

{% tabs %}
{% tab Fields %}

Si vous souhaitez formater les réponses d'une enquête de feedback simple pour déterminer la probabilité que les répondants recommandent la nouvelle saveur de glace de votre restaurant, vous pouvez configurer les champs suivants pour structurer le format de sortie :

| Nom du champ | Valeur |
| --- | --- |
| **likelihood_score** | Number |
| **explanation** | String |
| **confidence_score** | Number |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schémas avancés" }

![Console de l'agent affichant trois champs de sortie pour le score de probabilité, l'explication et le score de confiance.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON schema %}

Si vous souhaitez recueillir les commentaires des utilisateurs sur leur expérience gastronomique la plus récente dans votre chaîne de restaurants, vous pouvez sélectionner **JSON Schema** comme format de sortie et insérer le JSON suivant pour renvoyer un objet de données incluant une variable de sentiment et une variable de raisonnement.

```json
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "sentiment",
    "reasoning"
  ]
}
```

{% endtab %}
{% endtabs %}

## Catalogues et champs {#catalogs-and-fields}

Choisissez des catalogues spécifiques qu'un agent pourra consulter et fournissez-lui le contexte nécessaire pour comprendre vos produits et autres données non liées aux utilisateurs, le cas échéant. Les agents utilisent des outils pour trouver uniquement les éléments pertinents et les envoient au LLM afin de minimiser l'utilisation de jetons. Pour une meilleure récupération des données de catalogue, créez une [source de connaissances]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) et ajoutez-la comme contexte d'agent au lieu de rattacher directement le catalogue.

![Le catalogue « restaurants » et la colonne « Loyalty_Program » sélectionnés pour la recherche par l'agent.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

Lorsque vous déployez un agent de catalogue sur un champ de catalogue, activez le contrôle d'entrée obligatoire et choisissez les colonnes sélectionnées qui doivent être renseignées avant que l'agent ne s'exécute. L'agent ignore une ligne uniquement lorsque l'une de ces colonnes obligatoires est vide ou manquante — par exemple, un champ `gender` qui n'a pas encore été rempli. Les colonnes sélectionnées sont obligatoires par défaut, mais vous pouvez retirer celles qui peuvent être vides sans bloquer l'exécution. Cela évite de gaspiller des jetons sur des données incomplètes.

Les agents de catalogue respectent également l'ordre des colonnes lorsque les champs d'entrée dépendent les uns des autres. Si la colonne D doit être générée à partir des colonnes B et C, l'agent ne s'exécute pas sur la colonne D tant que B et C ne contiennent pas de valeurs pour cette ligne.

Pour les scénarios de déploiement et des exemples, consultez [Utiliser les agents de catalogue]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#use-catalog-agents) et [Bonnes pratiques pour les agents de catalogue]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

## Contexte d'appartenance à un Segment {#segment-membership-context}

Vous pouvez sélectionner jusqu'à cinq Segments que l'agent pourra croiser avec l'appartenance de chaque utilisateur lorsqu'il est utilisé dans un Canvas. Imaginons que votre agent dispose d'une appartenance au Segment « Loyalty Users » et qu'il est utilisé dans un Canvas. Lorsque les utilisateurs entrent dans une étape Agent, l'agent peut vérifier si chaque utilisateur est membre de chacun des Segments que vous avez spécifiés dans la console de l'agent, et utiliser l'appartenance (ou la non-appartenance) de chaque utilisateur comme contexte pour le LLM.

![Le Segment « Loyalty Users » sélectionné pour l'accès à l'appartenance de l'agent.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## Directives de marque {#brand-guidelines}

Vous pouvez sélectionner des [directives de marque]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) que votre agent devra respecter dans ses réponses. Par exemple, si vous souhaitez que votre agent génère du contenu SMS pour encourager les utilisateurs à s'inscrire à un abonnement en salle de sport, vous pouvez utiliser ce champ pour faire référence à vos directives prédéfinies au ton percutant et motivant.

## Historique d'interaction spécifique à l'utilisateur {#user-history}

Les données d'interaction d'un utilisateur incluent ses ouvertures, clics et données de conversion récents pour les Campaign et Canvas. Par exemple, vous pouvez inclure ce contexte pour qu'un agent le prenne en compte lorsqu'il est évalué dans un Canvas. L'historique d'interaction spécifique à l'utilisateur peut également influencer un agent dont le rôle est de rédiger des messages personnalisés.

## Historique des versions {#version-history}

La Console des agents enregistre une nouvelle version chaque fois que vous enregistrez des modifications apportées à l'agent. L'onglet **Historique des versions** répertorie chaque version enregistrée et les modifications entre les enregistrements.

1. Ouvrez l'agent dans la Console des agents.
2. Sélectionnez l'onglet **Historique des versions**.
3. Sélectionnez une version pour examiner sa configuration.

Pour inspecter les modifications d'une version, sélectionnez **Voir**. Braze affiche un diff en ligne de style code qui met en évidence les ajouts et les suppressions. Le contenu supprimé apparaît avec un style barré en rouge.

![Historique des versions de la Console des agents avec le panneau des différences par rapport à la version précédente ouvert, montrant les ajouts en vert et les suppressions en rouge dans les instructions de l'agent.]({% image_buster /assets/img/ai_agent/instruction_differences.png %}){: style="max-width:75%;"}

Si vous devez restaurer les instructions d'une version précédente, ouvrez **Voir** pour cette version, copiez le texte des instructions et collez-le dans votre champ **Instructions** actuel.

{% alert tip %}
Dans la vue du diff en ligne, appuyez sur <kbd>⌘</kbd> + <kbd>A</kbd> (macOS) ou <kbd>Ctrl</kbd> + <kbd>A</kbd> (Windows) pour sélectionner toutes les instructions sans le balisage de suppression en rouge, afin de pouvoir copier et restaurer le texte propre.
{% endalert %}

## Dupliquer des agents {#duplicate-agents}

Dupliquez un agent pour tester des améliorations ou des itérations côte à côte avec l'original. Utilisez l'[historique des versions](#version-history) pour consulter ou restaurer des configurations antérieures. Pour dupliquer un agent :

1. Survolez la ligne de l'agent et sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i>.
2. Sélectionnez **Dupliquer**.

## Archiver des agents {#archive-agents}

Au fur et à mesure que vous créez des agents personnalisés, vous pouvez organiser la page **Agent Management** en archivant les agents qui ne sont pas activement utilisés. Pour archiver un agent :

1. Survolez la ligne de l'agent et sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i>.
2. Sélectionnez **Archiver**.