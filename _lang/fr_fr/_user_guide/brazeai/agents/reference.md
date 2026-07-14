---
nav_title: Article de référence
article_title: Référence des agents
description: "Retrouvez les détails clés sur les agents de Braze."
page_order: 3
---

# Référence des agents {#reference-for-agents}

> Lorsque vous créez des agents personnalisés, reportez-vous à cet article pour en savoir plus sur les paramètres clés, tels que les instructions et les schémas de sortie. Pour une configuration étape par étape, consultez [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents). Pour une introduction, consultez [Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents) et la [Foire aux questions]({{site.baseurl}}/user_guide/brazeai/agents/faq).

## Modèles {#models}

Lorsque vous configurez un agent, vous pouvez choisir le modèle qu'il utilise pour générer des réponses. Deux possibilités s'offrent à vous : utiliser un modèle fourni par Braze ou apporter votre propre clé API.

{% alert important %}
Le modèle **Auto** fourni par Braze est optimisé pour les modèles dont les capacités de raisonnement sont suffisantes pour effectuer des tâches telles que la recherche dans un catalogue et la vérification d'appartenance à un Segment. Si vous utilisez d'autres modèles, nous vous recommandons de les tester pour confirmer qu'ils sont adaptés à votre cas d'usage. Vous devrez peut-être ajuster vos [instructions](#writing-instructions) pour fournir différents niveaux de détails ou de raisonnement étape par étape selon la vitesse et les capacités du modèle choisi.
{% endalert %}

### Option 1 : utiliser un modèle fourni par Braze {#option-1-use-a-braze-powered-model}

C'est l'option la plus simple : aucune configuration supplémentaire n'est nécessaire. Braze donne accès directement à des grands modèles de langage (LLM). Pour utiliser cette option, sélectionnez **Auto**, qui s'appuie sur les modèles Gemini.

{% alert important %}
Si vous ne voyez pas **Braze Auto** dans le menu déroulant **Model** lors de la création d'un agent, contactez votre gestionnaire du succès des clients pour savoir comment devenir éligible à l'utilisation du modèle Braze Auto.
{% endalert %}

### Option 2 : apporter votre propre clé API {#option-2-bring-your-own-api-key}

Cette option vous permet de connecter votre compte Braze à des fournisseurs tels qu'OpenAI, Anthropic ou Google Gemini. Si vous apportez votre propre clé API d'un fournisseur de LLM, les coûts liés aux jetons sont facturés directement par votre fournisseur, et non par Braze.

Nous vous recommandons de tester régulièrement les modèles les plus récents, car les anciens modèles peuvent être abandonnés ou rendus obsolètes au bout de quelques mois. Assurez-vous de disposer de crédits suffisants auprès de votre fournisseur pour exécuter vos agents à grande échelle. Vous pouvez également vous inscrire aux notifications de la Console des agents dans les [Préférences de notification]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) pour être alerté lorsque Braze détecte qu'un modèle n'est plus disponible ou rencontre des problèmes de facturation avec votre fournisseur de LLM.

Pour configurer cette option :

1. Allez dans **Intégrations partenaires** > **Partenaires technologiques** et trouvez votre fournisseur.
2. Saisissez votre clé API fournie par le fournisseur.
3. Sélectionnez **Enregistrer**.

Vous pouvez ensuite retourner à votre agent et sélectionner votre modèle.

Lorsque vous utilisez un LLM fourni par Braze, les fournisseurs de ce modèle agissent en tant que sous-traitants secondaires de Braze, conformément aux conditions de l'addendum relatif au traitement des données (DPA) conclu entre vous et Braze. Si vous choisissez d'apporter votre propre clé API, le fournisseur de votre abonnement LLM est considéré comme un fournisseur tiers dans le cadre du contrat entre vous et Braze.

#### Niveaux de réflexion {#thinking-levels}

Certains fournisseurs de LLM vous permettent d'ajuster le niveau de réflexion d'un modèle sélectionné. Les niveaux de réflexion définissent l'étendue du raisonnement que le modèle effectue avant de répondre, allant de réponses rapides et directes à des chaînes de raisonnement plus longues. Cela affecte la qualité des réponses, la latence et la consommation de jetons.

| Niveau | Quand l'utiliser |
|--------|-----------------|
| **Minimal** | Tâches simples et bien définies (comme la recherche dans un catalogue ou la classification directe). Réponses les plus rapides et coût le plus bas. |
| **Faible** | Tâches qui bénéficient d'un peu plus de raisonnement sans nécessiter d'analyse approfondie. |
| **Moyen** | Tâches à plusieurs étapes ou nuancées (comme l'analyse de plusieurs entrées pour recommander une action). |
| **Élevé** | Raisonnement complexe, cas particuliers, ou situations où le modèle doit réfléchir aux étapes avant de répondre. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Niveaux de réflexion" }

Nous vous recommandons de commencer par **Minimal** et de tester les réponses de votre agent. Vous pouvez ensuite passer au niveau **Faible** ou **Moyen** si l'agent a du mal à fournir des réponses précises. Dans de rares cas, un niveau **Élevé** peut être nécessaire, mais sachez que ce niveau peut entraîner des coûts de jetons élevés, des temps de réponse plus longs ou un risque accru d'erreurs de délai d'attente. Si votre agent peine à concilier un raisonnement à plusieurs étapes avec des temps de réponse raisonnables, envisagez de diviser votre cas d'usage en plusieurs agents capables de collaborer dans un Canvas ou un catalogue.

Braze utilise les mêmes plages d'adresses IP pour les appels LLM sortants que pour le contenu connecté. Ces plages sont répertoriées dans la [liste d'autorisation IP du contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting). Si votre fournisseur prend en charge la liste d'autorisation IP, vous pouvez restreindre la clé à ces plages afin que seul Braze puisse l'utiliser.

{% alert important %}
Lorsque vous utilisez un LLM fourni par Braze, les fournisseurs de ce modèle agissent en tant que sous-traitants secondaires de Braze, conformément aux conditions de l'addendum relatif au traitement des données (DPA) conclu entre vous et Braze. Si vous choisissez d'apporter votre propre clé API, le fournisseur de votre abonnement LLM est considéré comme un fournisseur tiers dans le cadre du contrat entre vous et Braze.
{% endalert %}

#### Déterminer le modèle à utiliser {#determine-which-model-to-use}

Chaque fournisseur de LLM propose un mélange légèrement différent de capacités, de coûts et de niveaux de réflexion. Voici quelques recommandations générales et bonnes pratiques :

- Pour optimiser les coûts, privilégiez les modèles à faible coût en jetons avant de passer à des modèles plus coûteux. N'augmentez le coût que si les modèles moins chers peinent avec votre cas d'usage ou produisent des résultats incohérents ou inexacts.
- Pour optimiser la vitesse et les performances, privilégiez les niveaux de réflexion les plus bas avant de passer à des niveaux supérieurs. N'augmentez le niveau de réflexion que si les niveaux inférieurs peinent avec votre cas d'usage ou produisent des résultats incohérents ou inexacts.
- Si les modèles ou niveaux de réflexion les moins coûteux peinent avec votre cas d'usage ou produisent des résultats incohérents ou inexacts, envisagez de passer à des modèles plus coûteux ou à des niveaux de réflexion supérieurs.
- Pendant les tests, veillez à trouver le bon équilibre entre fiabilité et précision d'une part, et consommation de jetons et durée d'invocation d'autre part.
- Chaque cas d'usage peut avoir un modèle et un niveau de réflexion optimaux différents. Nous vous recommandons de tester minutieusement pour vérifier la qualité constante sans dépassements de délai.

### Contrôles du flux d'invocation {#invocation-flow-controls}

Les contrôles du flux d'invocation suivants s'appliquent par espace de travail :

- **Modèle fourni par Braze :** 5 000 invocations par minute
- **Clé API personnelle :** 5 000 invocations par minute

Lorsque de nombreux utilisateurs entrent simultanément dans une étape Agent, Braze met les invocations en file d'attente selon ces limites, de sorte que le traitement peut prendre plus de temps lors d'envois à fort volume.

### Limites quotidiennes d'invocations et de crédits {#daily-invocation-and-credit-limits}

Chaque agent dispose d'une limite quotidienne d'invocations (250 000 par défaut ; 1 000 000 maximum, sauf si votre contrat autorise davantage). Chaque invocation, y compris les aperçus dans la Console des agents et les exécutions de Canvas de test utilisant **Simuler la réponse**, est comptabilisée dans cette limite.

Dans la Console des agents, la **limite quotidienne de coût en crédits d'action** estime le nombre maximal de crédits qu'un agent peut consommer par jour. Braze multiplie le **ratio de crédits** par invocation de votre espace de travail pour le modèle sélectionné par la limite quotidienne d'invocations.

### Surveiller la consommation de crédits {#monitor-credit-usage}

Allez dans **Paramètres** > **Facturation** > **Utilisation des crédits** > **Console des agents** pour consulter la consommation de crédits, le nombre d'invocations et les ratios de crédits par agent.

Les ratios de crédits proviennent de votre contrat et apparaissent dans le tableau de bord [Utilisation des crédits]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage) (onglet **Ratios de crédits** et onglet **Console des agents**). L'estimation se met à jour lorsque vous modifiez le modèle ou la limite d'invocations.

Pour maîtriser les dépenses, réduisez la limite quotidienne d'invocations. Pour les modèles [avec votre propre clé (BYO)](#option-2-bring-your-own-api-key), vous pouvez également choisir un modèle moins coûteux ou réduire le [niveau de réflexion](#thinking-levels) pour diminuer les coûts de jetons du fournisseur. **Braze Auto** ne permet pas d'ajuster le niveau de réflexion.

### Erreurs de limite de débit {#rate-limit-errors}

Si le fournisseur de LLM renvoie une erreur de limite de débit lors d'une étape Agent dans Canvas ou d'une invocation d'agent de catalogue, Braze relance continuellement la requête en utilisant des délais exponentiels jusqu'à ce que l'appel aboutisse ou que Braze détermine qu'il ne peut pas être complété.

Lorsque les tentatives de relance dans Canvas ou pour le catalogue sont épuisées, le panneau de détails des **Logs** affiche **Error** et le message du fournisseur (tel que `Rate limit exceeded`) dans **Output**. Les tentatives de relance sont visibles dans les logs, y compris la toute première invocation, quel que soit son résultat final. Pour un utilisateur donné, s'il faut quatre tentatives de relance pour obtenir un succès, vous pouvez rechercher l'ID utilisateur et voir les cinq entrées (l'originale plus quatre relances) dans les **Logs**, et l'originale ainsi que les trois premières relances afficheront **Error** avec `Rate limit exceeded`.

![Détails du log de la Console des agents montrant une erreur de dépassement de limite de débit dans le champ Output.]({% image_buster /assets/img/ai_agent/rate_limit_error_log.png %}){: style="max-width:75%;"}

## Rédaction des instructions {#writing-instructions}

Les instructions sont les règles ou directives que vous donnez à l'agent (prompt système). Elles définissent le comportement de l'agent à chaque exécution. Les instructions système peuvent contenir jusqu'à 25 Ko.

Si vous avez créé votre agent avec [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) en utilisant un [modèle de départ]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator), passez en revue les instructions préremplies et modifiez-les si nécessaire.

Voici quelques bonnes pratiques générales pour vous aider à démarrer avec la rédaction de prompts :

1. Commencez par la fin. Énoncez d'abord l'objectif.
2. Donnez au modèle un rôle ou un personnage (« Vous êtes un ... »).
3. Définissez clairement le contexte et les contraintes (audience, longueur, ton, format).
4. Demandez une structure (« Retournez du JSON/une liste à puces/un tableau... »).
5. Montrez plutôt que de décrire. Incluez quelques exemples de qualité.
6. Décomposez les tâches complexes en étapes ordonnées (« Étape 1... Étape 2... »).
7. Encouragez le raisonnement (« Réfléchissez en interne aux différentes étapes, puis donnez une réponse finale concise » ou « expliquez brièvement votre décision »).
8. Testez, inspectez et itérez. De petits ajustements peuvent produire des gains de qualité importants.
9. Traitez les cas particuliers, ajoutez des garde-fous et des instructions de refus.
10. Mesurez et documentez ce qui fonctionne en interne pour faciliter la réutilisation et la montée en charge.

### Exemples {#examples}

Pour des configurations de départ dans la Console des agents, consultez [Modèles d'agents créés avec Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).

Pour des exemples complets d'instructions que vous pouvez copier ou adapter, consultez la [bibliothèque de cas d'usage des agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/examples).

| Exemple | Catégorie | Type d'agent | Ce qu'il fait |
| --- | --- | --- | --- |
| [Rédiger des messages personnalisés en fonction du contexte d'un utilisateur]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-personalized-messaging-based-on-a-users-context) | Génération de contenu | Agent d'étape Canvas | Génère un objet et une accroche d'e-mail coordonnés ainsi qu'un titre et un corps de notification push pour les utilisateurs ayant effectué une recherche sans réserver. |
| [Analyser les retours utilisateur pour déterminer les prochaines étapes]({{site.baseurl}}/user_guide/brazeai/agents/examples#analyze-user-feedback-to-determine-next-steps) | Standardisation des données | Agent d'étape Canvas | Classifie le sentiment et le sujet d'une enquête post-voyage, puis recommande une prochaine action CRM. |
| [Catégoriser les utilisateurs en compartiments d'intérêt à partir d'attributs existants]({{site.baseurl}}/user_guide/brazeai/agents/examples#categorize-users-into-interest-buckets-from-existing-attributes) | Agent d'affinité | Agent d'étape Canvas | Classifie les utilisateurs en compartiments d'intérêt à partir d'attributs et de signaux d'intention forte, puis recommande la meilleure expérience ou le meilleur article suivant. |
| [Orienter les utilisateurs vers le chemin Canvas le plus pertinent en fonction de leur comportement récent]({{site.baseurl}}/user_guide/brazeai/agents/examples#route-users-to-the-most-relevant-canvas-path-from-recent-behavior) | Agent d'affinité | Agent d'étape Canvas | Déduit la motivation à partir du comportement récent et renvoie la clé de route optimale pour la prochaine étape Canvas de l'utilisateur. |
| [Attribuer des catégories d'intérêt aux utilisateurs à partir d'actions à forte intention en temps réel]({{site.baseurl}}/user_guide/brazeai/agents/examples#assign-users-to-interest-categories-from-real-time-high-intent-actions) | Agent d'affinité | Agent d'étape Canvas | Attribue des catégories d'intérêt à partir d'actions à forte intention et recommande la meilleure expérience ou le meilleur article suivant. |
| [Classifier les messages entrants pour détecter une intention de désinscription]({{site.baseurl}}/user_guide/brazeai/agents/examples#classify-inbound-messages-for-opt-out-intent) | Classification et routage | Agent d'étape Canvas | Renvoie un booléen strict indiquant si un message est une demande de désinscription. |
| [Standardiser les messages entrants en données structurées pour l'automatisation]({{site.baseurl}}/user_guide/brazeai/agents/examples#standardize-inbound-messages-into-structured-data-for-automation) | Standardisation des données | Agent d'étape Canvas | Normalise les SMS ou chats entrants en intention structurée, entités et indicateurs de conformité pour l'automatisation en aval. |
| [Rédiger des descriptions à fort taux de conversion conformes aux directives de marque]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-high-converting-descriptions-that-align-with-brand-guidelines) | Génération de contenu | Agent de catalogue | Génère des descriptions courtes et conformes à la marque pour chaque ligne du catalogue. |
| [Fournir des traductions en fonction de la langue utilisée par région]({{site.baseurl}}/user_guide/brazeai/agents/examples#provide-translations-based-on-language-used-by-region) | Enrichissement de catalogue | Agent de catalogue | Localise les chaînes d'interface et de marketing par locale et limite de caractères. |
| [Enrichir les éléments du catalogue avec des descriptions, des catégories et des étiquettes]({{site.baseurl}}/user_guide/brazeai/agents/examples#enrich-catalog-items-with-descriptions-categories-and-tags) | Enrichissement de catalogue | Agent de catalogue | Génère des descriptions enrichies, des catégories et des étiquettes à partir des données existantes des éléments du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Résumé des exemples" }

### Utilisation de Liquid {#using-liquid}

Inclure du [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) dans les instructions de votre agent permet d'ajouter une couche supplémentaire de personnalisation à ses réponses. Vous pouvez spécifier la variable Liquid exacte que l'agent reçoit et l'intégrer dans le contexte de votre prompt. Par exemple, au lieu d'écrire explicitement « prénom », vous pouvez utiliser l'extrait de code Liquid {% raw %}`{{${first_name}}}`{% endraw %} :

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

Dans la section **Logs** de la **Console des agents**, vous pouvez examiner les détails des entrées et sorties de l'agent pour comprendre quelle valeur est rendue par Liquid.

### Quelles données les agents reçoivent {#what-data-agents-receive}

Le contexte d'un agent n'est pas une mémoire conversationnelle ouverte. Contrairement à un assistant de chat, un agent ne voit que les données que vous lui transmettez explicitement au moment de l'invocation : il ne parcourt pas les profils utilisateur, ne déduit pas les champs manquants et ne vous signale pas l'absence d'informations requises.

Concevez chaque agent comme un pipeline délibéré d'entrée vers sortie. Transmettez chaque point de donnée dont l'agent a besoin en utilisant un ou plusieurs des moyens suivants :

1. **Liquid dans les instructions :** intégrez des attributs utilisateur ({% raw %}`{{${first_name}}}`{% endraw %}) et des [variables de contexte Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) ({% raw %}`{{context.${variable_name}}}`{% endraw %}) directement dans le prompt de l'agent.
2. **+ Contexte de l'agent :** sélectionnez des catalogues, l'appartenance à un Segment, des directives de marque, **Tout le contexte Canvas** ou des données d'interaction utilisateur dans la Console des agents.
3. [Étapes de contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) : définissez ou mettez à jour des variables `context.*` en amont dans le Canvas avant l'exécution d'une étape Agent.
4. **Contexte supplémentaire sur l'étape Agent :** transmettez toute valeur supplémentaire modélisée en Liquid qui n'est pas déjà spécifiée par les autres méthodes à l'agent au moment de l'envoi depuis la configuration de l'étape.

Veillez à intégrer ces variables de contexte dans les instructions de l'agent via Liquid ou à sélectionner **Ajouter tout le contexte Canvas**. Si une valeur n'est pas transmise par l'un de ces canaux, l'agent ne la reçoit pas. Listez les entrées requises dans vos instructions ou dans les [prérequis du cas d'usage]({{site.baseurl}}/user_guide/brazeai/agents/use_cases), et vérifiez les entrées dans **Console des agents** > **Logs** après les tests.

![Détails d'un agent qui utilise Liquid dans ses instructions.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

Pour les agents de catalogue, utilisez les **Champs** dans la section **Sortie** plutôt que le schéma JSON ; vous pouvez toutefois rédiger des instructions qui demandent au modèle de produire une sortie clé-valeur correspondant à ces noms de champs.

Pour plus de détails sur les bonnes pratiques en matière de prompts, consultez les guides des fournisseurs de modèles suivants :

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## Sorties {#outputs}

Si vous avez créé votre agent avec [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) en utilisant un [modèle de départ]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator), passez en revue le schéma de sortie prérempli et modifiez-le si nécessaire.

### Schémas de base {#basic-schemas}

Les schémas de base constituent une sortie simple renvoyée par un agent. Il peut s'agir d'une chaîne de caractères, d'un nombre, d'une valeur booléenne, d'un tableau de chaînes de caractères ou d'un tableau de nombres.

Par exemple, si vous souhaitez collecter des scores de sentiment utilisateur à partir d'une enquête de satisfaction simple pour déterminer le niveau de satisfaction de vos clients après réception d'un produit, vous pouvez sélectionner **Number** comme schéma de base pour structurer le format de sortie.

{% alert important %}
Les tableaux ne sont disponibles que pour les agents Canvas, pas pour les agents de catalogue.
{% endalert %}

![Console des agents avec le nombre sélectionné comme schéma de base.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

### Schémas avancés {#advanced-schemas}

Les options de schéma avancé incluent la structuration manuelle de champs ou l'utilisation de JSON.

- **Champs :** une méthode sans code pour imposer un format de sortie d'agent que vous pouvez utiliser de manière cohérente.
- **JSON :** une approche par code pour créer un format de sortie précis, où vous pouvez imbriquer des variables et des objets dans le schéma JSON. Disponible uniquement pour les agents Canvas, pas pour les agents de catalogue.

Nous recommandons d'utiliser les schémas avancés lorsque vous souhaitez que l'agent renvoie une structure de données comportant plusieurs valeurs définies de manière structurée, plutôt qu'une sortie à valeur unique. Cela permet de mieux formater la sortie en tant que variable de contexte cohérente.

### Sortie de secours {#fallback-output}

Les valeurs de secours ne sont disponibles que pour les **agents d'étape Canvas**. Dans la section **Sortie** de la Console des agents pour un agent Canvas, vous pouvez définir les valeurs que Braze utilise lorsqu'une invocation échoue.

Pour les schémas **JSON**, Braze lit le schéma et génère un champ de saisie pour chaque propriété afin que vous puissiez définir une valeur de secours par clé. Pour les schémas **Champs**, vous saisissez une valeur de secours pour chaque champ. Pour les schémas de base, vous saisissez une seule valeur de secours. Les agents Canvas prennent en charge Liquid dans les valeurs de secours.

Pour les étapes de configuration, consultez [Configurer les valeurs de secours]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values). Pour le comportement à l'exécution dans Canvas, consultez [Gestion des erreurs et comportement de secours]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior).

Par exemple, vous pouvez utiliser un format de sortie au sein d'un agent destiné à créer un exemple d'itinéraire de voyage pour un utilisateur à partir d'un formulaire qu'il a soumis. Le format de sortie vous permet de définir que chaque réponse de l'agent doit contenir des valeurs pour `tripStartDate`, `tripEndDate` et `destination`. Chacune de ces valeurs peut être extraite des variables de contexte et placée dans une étape Message pour la personnalisation via Liquid.

{% tabs %}
{% tab Champs %}

Si vous souhaitez formater les réponses à une enquête de satisfaction simple pour déterminer la probabilité que les répondants recommandent la nouvelle saveur de glace de votre restaurant, vous pouvez configurer les champs suivants pour structurer le format de sortie :

| Nom du champ | Valeur |
| --- | --- |
| **likelihood_score** | Nombre |
| **explanation** | Chaîne de caractères |
| **confidence_score** | Nombre |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schémas avancés" }

![Console des agents affichant trois champs de sortie pour le score de probabilité, l'explication et le score de confiance.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab Schéma JSON %}

Si vous souhaitez collecter les retours utilisateur sur leur dernière expérience culinaire dans votre chaîne de restaurants, vous pouvez sélectionner **JSON Schema** comme format de sortie et insérer le JSON suivant pour renvoyer un objet de données incluant une variable de sentiment et une variable de raisonnement.

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

Choisissez des catalogues spécifiques auxquels un agent peut se référer pour lui donner le contexte nécessaire à la compréhension de vos produits et d'autres données non liées aux utilisateurs, le cas échéant. Les agents utilisent des outils pour trouver uniquement les éléments pertinents et les envoient au LLM afin de minimiser la consommation de jetons. Pour une meilleure récupération des données du catalogue, créez une [source de connaissances]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) et ajoutez-la comme contexte de l'agent au lieu d'attacher le catalogue directement.

![Le catalogue « restaurants » et la colonne « Loyalty_Program » sélectionnés pour la recherche de l'agent.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

Lorsque vous déployez un agent de catalogue sur un champ de catalogue, activez le contrôle d'entrée requise et choisissez quelles colonnes sélectionnées sont **requises pour l'exécution** avant que l'agent ne s'invoque. L'agent ignore une ligne uniquement lorsqu'une de ces colonnes requises est vide ou manquante, par exemple un champ `gender` qui n'a pas encore été renseigné. Les colonnes sélectionnées sont requises par défaut, mais vous pouvez retirer des colonnes susceptibles d'être vides sans bloquer l'exécution. Cela évite de gaspiller des jetons sur des données incomplètes.

Les agents de catalogue respectent également l'ordre des colonnes lorsque les champs d'entrée dépendent les uns des autres. Si la colonne D doit être générée à partir des colonnes B et C, l'agent ne s'exécute pas sur la colonne D tant que B et C ne contiennent pas de valeurs pour cette ligne.

Pour les scénarios de déploiement et des exemples, consultez [Utiliser les agents de catalogue]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#use-catalog-agents) et [Bonnes pratiques pour les agents de catalogue]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

## Contexte d'appartenance à un Segment {#segment-membership-context}

Vous pouvez sélectionner jusqu'à cinq Segments pour que l'agent puisse croiser l'appartenance de chaque utilisateur à ces Segments lorsqu'il est utilisé dans un Canvas. Supposons que votre agent ait accès à l'appartenance au Segment « Utilisateurs fidèles » et qu'il soit utilisé dans un Canvas. Lorsque des utilisateurs entrent dans une étape Agent, celui-ci peut vérifier si chaque utilisateur est membre de chaque Segment que vous avez spécifié dans la Console des agents, et utiliser l'appartenance (ou la non-appartenance) de chaque utilisateur comme contexte pour le LLM.

![Le Segment « Utilisateurs fidèles » sélectionné pour l'accès à l'appartenance de l'agent.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## Directives de marque {#brand-guidelines}

Vous pouvez sélectionner des [directives de marque]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) que votre agent devra respecter dans ses réponses. Par exemple, si vous souhaitez que votre agent génère un texte SMS pour encourager les utilisateurs à s'inscrire à une salle de sport, vous pouvez utiliser ce champ pour faire référence à votre directive prédéfinie, audacieuse et motivante.

## Historique d'interaction spécifique à l'utilisateur {#user-history}

Les données d'interaction d'un utilisateur incluent ses ouvertures, clics et données de conversion récents pour les Campaign et Canvas. Par exemple, vous pouvez inclure ce contexte pour qu'un agent le prenne en compte lorsqu'il est évalué dans un Canvas. L'historique d'interaction spécifique à l'utilisateur peut également influencer un agent dont le rôle est de rédiger des messages personnalisés.

## Historique des versions {#version-history}

La Console des agents enregistre une nouvelle version chaque fois que vous enregistrez des modifications apportées à l'agent. L'onglet **Historique des versions** répertorie chaque version enregistrée et les modifications entre les enregistrements.

1. Ouvrez l'agent dans la Console des agents.
2. Sélectionnez l'onglet **Historique des versions**.
3. Sélectionnez une version pour examiner sa configuration.

Pour inspecter les modifications d'une version, sélectionnez **Voir**. Braze affiche un diff en ligne de style code qui met en évidence les ajouts et les suppressions. Le contenu supprimé apparaît avec un style barré en rouge.

Si vous devez restaurer les instructions d'une version précédente, ouvrez **Voir** pour cette version, copiez le texte des instructions et collez-le dans votre champ **Instructions** actuel.

{% alert tip %}
Dans la vue du diff en ligne, appuyez sur <kbd>⌘</kbd> + <kbd>A</kbd> (macOS) ou <kbd>Ctrl</kbd> + <kbd>A</kbd> (Windows) pour sélectionner toutes les instructions sans le balisage de suppression en rouge, afin de pouvoir copier et restaurer le texte propre.
{% endalert %}

## Dupliquer des agents {#duplicate-agents}

Dupliquez un agent pour tester des améliorations ou des itérations côte à côte avec l'original. Utilisez l'[historique des versions](#version-history) pour examiner ou restaurer des configurations antérieures. Pour dupliquer un agent :

1. Survolez la ligne de l'agent et sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i>.
2. Sélectionnez **Dupliquer**.

## Archiver des agents {#archive-agents}

Au fur et à mesure que vous créez des agents personnalisés, vous pouvez organiser la page **Gestion des agents** en archivant les agents qui ne sont pas activement utilisés. Pour archiver un agent :

1. Survolez la ligne de l'agent et sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i>.
2. Sélectionnez **Archiver**.