---
nav_title: Créer des agents
article_title: Créer des agents personnalisés
description: "Découvrez comment créer des agents, ce qu'il convient de préparer avant de commencer et comment les mettre en œuvre dans les domaines de la communication, de la prise de décision et de la gestion des données."
page_order: 1
alias: /creating-agents/
---

# Créer des agents personnalisés {#create-custom-agents}

> Découvrez comment créer des agents personnalisés, ce qu'il convient de préparer avant de commencer et comment les mettre en œuvre dans les domaines de la communication, de la prise de décision et de la gestion des données. Pour des informations plus générales, consultez [Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents).

## Prérequis {#prerequisites}

Avant de commencer, vous aurez besoin des éléments suivants :

- L'[autorisation]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) d'accéder à la **Console d'agents** dans votre espace de travail. Vérifiez auprès de vos administrateurs Braze si vous ne voyez pas cette option.
- L'autorisation de créer et de modifier des agents IA personnalisés.
- Une idée de ce que vous souhaitez que l'agent accomplisse. Les Braze Agents peuvent prendre en charge les actions suivantes :
   - **Communication personnalisée :** générer des lignes d'objet, des titres, du contenu intégré au produit ou d'autres contenus.
   - **Routage des utilisateurs :** orienter les utilisateurs dans Canvas en fonction de leur comportement, de leurs préférences ou de leurs attributs personnalisés.
   - **Gestion des données :** calculer des valeurs, enrichir les entrées de catalogue ou actualiser les champs de profil.

## Comment ça fonctionne {#how-it-works}

Lorsque vous créez un agent, vous définissez son objectif et établissez des garde-fous pour encadrer son comportement. Une fois en direct or en ligne/en production/instantané, l'agent peut être déployé dans Braze pour générer du contenu personnalisé, prendre des décisions en temps réel ou mettre à jour des champs de catalogue. Pendant la création de votre agent, vous pouvez l'enregistrer en tant que brouillon, et vous pouvez mettre en pause ou mettre à jour un agent à tout moment depuis le tableau de bord. Chaque enregistrement crée une nouvelle version que vous pouvez consulter dans l'onglet [Historique des versions]({{site.baseurl}}/user_guide/brazeai/agents/reference#version-history).

Les cas d'usage suivants illustrent quelques façons de tirer parti des agents personnalisés.

| Cas d'usage | Description |
| --- | --- |
| Gestion des retours clients | Transmettez les retours des utilisateurs à un agent pour analyser le sentiment et générer des messages de suivi empathiques. Pour les utilisateurs à forte valeur, l'agent peut escalader la réponse ou inclure des avantages. |
| Localisation de contenu | Traduisez le texte d'un catalogue dans une autre langue pour des campagnes internationales, ou ajustez le ton et la longueur pour des canaux spécifiques à une région. Par exemple, traduisez « Classic Clubmaster Sunglasses » en espagnol par « Gafas de sol Classic Clubmaster », ou raccourcissez les descriptions pour les campagnes SMS. |
| Résumé d'avis ou de retours | Résumez le sentiment ou les retours dans un nouveau champ, par exemple en attribuant des scores de sentiment tels que Positif, Neutre ou Négatif, ou en créant un court résumé textuel comme « La plupart des clients mentionnent un excellent ajustement, mais signalent une livraison lente. » |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comment ça fonctionne" }

## Créer un agent {#create-an-agent}

### Étape 1 : Choisir un type d'agent {#step-1-choose-an-agent-type}

Pour créer un agent, commencez par choisir votre type d'agent :

1. Accédez à **Agent Console**.
2. Choisissez **Canvas Step Agents** ou **Catalog Agents**.

### Étape 2 : Choisir comment créer un agent {#step-2-choose-how-to-build-an-agent}

Sélectionnez **Create agent**, puis choisissez l'une des options suivantes :

- **Custom agent** pour créer un agent à partir de zéro
- Une option dans **Create an agent with Operator** pour utiliser [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) afin d'appliquer un [modèle de départ](#agent-templates-built-with-operator)

Si vous utilisez Operator, examinez et approuvez ses modifications dans le chat avant de passer à l'étape suivante.

### Étape 3 : Configurer les détails {#step-3-set-up-details}

Ensuite, configurez les détails de votre agent :

1. Saisissez un nom et une description pour aider votre équipe à comprendre son objectif.
2. (facultatif) Ajoutez des tags pour filtrer votre agent.
3. Choisissez le [modèle]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) que votre agent utilisera.
4. Si vous n'utilisez pas le modèle **Braze Auto**, sélectionnez le [niveau de réflexion]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels) du modèle. Vous pouvez choisir entre minimal, faible, moyen ou élevé. Nous recommandons de commencer par **Minimal** et de tester les réponses de votre agent, puis d'ajuster ce paramètre si nécessaire.
5. Définissez une limite d'invocations quotidiennes. Par défaut, cette valeur est fixée à 250 000, mais elle peut être augmentée jusqu'à 1 000 000. Si vous souhaitez augmenter la limite au-delà de 1 000 000, contactez votre gestionnaire du succès des clients pour en savoir plus. Définissez la limite suffisamment haute pour la taille d'audience prévue après les tests. Une limite trop basse provoque des échecs de limite quotidienne (qui ne consomment pas de crédits mais appliquent des valeurs de repli ou laissent la sortie `null`).

Le champ **Daily action credit cost limit** spécifie le nombre maximum de crédits que cet agent peut consommer par jour. Braze le calcule à partir du ratio de crédits par invocation de votre espace de travail pour le modèle sélectionné (issu de votre contrat, affiché sur la page [Credit Ratios]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage)) multiplié par la limite d'invocations quotidiennes. L'estimation se met à jour lorsque vous modifiez le modèle ou la limite d'invocations.

Pour gérer les coûts, réduisez la limite d'invocations quotidiennes. Pour les modèles [BYO (bring-your-own)]({{site.baseurl}}/user_guide/brazeai/agents/reference#option-2-bring-your-own-api-key), vous pouvez également passer à un modèle moins coûteux ou réduire le [niveau de réflexion]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels). **Braze Auto** ne prend pas en charge l'ajustement du niveau de réflexion. Suivez l'utilisation réelle dans **Settings** > **Billing** > **Credits Usage** > **Agent Console**.

![Interface Agent Console pour la création d'un agent personnalisé dans Braze. L'écran affiche des champs pour saisir le nom et la description de l'agent, sélectionner un modèle et définir une limite d'invocations quotidiennes.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### Étape 4 : Rédiger les instructions {#agent-instructions}

Donnez des instructions à l'agent. Si vous avez utilisé un modèle Operator, examinez les instructions pré-remplies et modifiez-les si nécessaire.

Incluez des instructions sur ce que l'agent doit faire dans des scénarios inattendus ou ambigus. Cela minimise le risque que la confusion de l'agent entraîne des erreurs. Par exemple, plutôt que de demander à l'agent uniquement des valeurs de sentiment « positif » ou « négatif », demandez-lui de renvoyer « incertain » s'il ne peut pas se décider.

Consultez la section [Rédiger des instructions]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions) pour les bonnes pratiques et les [Exemples]({{site.baseurl}}/user_guide/brazeai/agents/reference#examples) pour vous inspirer dans la formulation des consignes de votre agent.

#### Ajouter du contexte {#add-resources}

{% alert important %}
Les agents ne reçoivent que les données que vous leur transmettez explicitement — ils ne parcourent pas les profils utilisateur et ne vous avertissent pas lorsque des données requises sont manquantes. Utilisez Liquid dans vos instructions, sélectionnez **+ Agent context**, ajoutez des [étapes de contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) en amont dans Canvas, ou transmettez du contexte supplémentaire sur l'étape Agent. Pour une liste complète des sources de données et des conseils de conception, consultez [Quelles données les agents reçoivent]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).
{% endalert %}

Sélectionnez **+ Agent context** pour choisir ce que votre agent peut référencer. Cela inclut :

- [Champs de catalogue]({{site.baseurl}}/user_guide/brazeai/agents/reference#catalogs-and-fields) : donnez à l'agent accès aux données de votre catalogue pour des réponses plus précises.
- [Sources de connaissances]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) : donnez à l'agent accès aux données de catalogue via une source de connaissances pour une récupération plus précise que l'attachement direct d'un catalogue.
- [Appartenance à un Segment]({{site.baseurl}}/user_guide/brazeai/agents/reference#segment-membership-context) : permettez à l'agent de personnaliser les réponses en fonction des Segments auxquels un utilisateur appartient. Vous pouvez sélectionner jusqu'à cinq Segments.
- [Directives de marque]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) : référencez les directives de voix et de style de marque que l'agent doit suivre. Par exemple, si vous souhaitez que votre agent génère du contenu SMS pour encourager les utilisateurs à s'inscrire à un abonnement de salle de sport, vous pouvez utiliser ce champ pour référencer vos directives prédéfinies audacieuses et motivantes.
- [Tout le contexte Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) : analysez toutes les données de contexte Canvas d'un utilisateur lorsque cet agent est invoqué, y compris les variables qui ne sont pas référencées dans la section **Instructions**.
- [Données d'interaction utilisateur]({{site.baseurl}}/user_guide/brazeai/agents/reference#user-history) : fournissez à l'agent les données récentes d'ouvertures, de clics et de conversions des Campaigns et Canvas de chaque utilisateur.

{% alert tip %}
Pour les agents Canvas, vous pouvez utiliser Liquid dans vos instructions pour référencer des attributs utilisateur, tels que leur prénom et nom, ou des attributs personnalisés. Toute variable Liquid dans les instructions de l'agent est automatiquement transmise à l'étape Agent lorsqu'un utilisateur entre dans l'étape. Consultez [Quelles données les agents reçoivent]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive) pour savoir comment transmettre délibérément le contexte Canvas et les données de profil.
{% endalert %}

### Étape 5 : Sélectionner la sortie {#select-output}

Dans la section **Output**, vous pouvez organiser et définir la [sortie]({{site.baseurl}}/user_guide/brazeai/agents/reference#outputs) de l'agent à l'aide de schémas basiques ou de schémas avancés. Si vous avez utilisé un modèle Operator, examinez le schéma de sortie pré-rempli et modifiez-le si nécessaire.

Pour de meilleurs résultats, assurez-vous que ce que vous spécifiez dans la section **Output** correspond aux instructions de l'agent que vous avez saisies à l'[étape 4](#agent-instructions). Par exemple, si vous avez mentionné dans les instructions de l'agent que vous souhaitez un objet avec deux chaînes de caractères, assurez-vous de spécifier un objet avec deux chaînes de caractères dans la section **Output**. Si les instructions de votre agent ne correspondent pas à la sortie spécifiée, l'agent peut être confus, expirer ou générer des sorties indésirables.

{% alert tip %}
Lorsque vous utilisez un [schéma de sortie avancé]({{site.baseurl}}/user_guide/brazeai/agents/reference#advanced-schemas), ajoutez un champ de type chaîne de caractères nommé `explanation` si vous souhaitez que l'agent renvoie son raisonnement en plus de ses autres sorties. Indiquez à l'agent dans vos [instructions](#agent-instructions) de remplir `explanation` lorsque cela vous aide à examiner ou déboguer les réponses.
{% endalert %}

#### Configurer les valeurs de repli {#configure-fallback-values}

Les valeurs de repli sont disponibles uniquement pour les Canvas Step Agents. Dans la section **Output** d'un Canvas Step Agent, vous pouvez définir les valeurs que Braze utilise lorsqu'une invocation d'agent échoue, par exemple lorsque le LLM expire ou renvoie une erreur de clé API invalide. Les valeurs de repli fonctionnent comme des valeurs par défaut de personnalisation. Vous pouvez définir une ligne d'objet statique ou un court message qui fournit tout de même une sortie utile aux utilisateurs lorsque l'agent ne peut pas s'exécuter.

Les Catalog Agents ne prennent pas en charge la configuration des valeurs de repli dans Agent Console.

![Configuration de la sortie dans Agent Console montrant le champ de sortie de repli pour un schéma de type nombre.]({% image_buster /assets/img/ai_agent/fallback_output.png %}){: style="max-width:75%;"}

Pour les agents Canvas, les valeurs de repli prennent en charge le templating [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) afin que vous puissiez référencer des attributs utilisateur ou des variables de contexte dans le texte de repli.

Les champs de repli s'adaptent au format de sortie de votre Canvas Step Agent :

| Format de sortie | Configuration du repli |
| --- | --- |
| Chaîne de caractères, nombre ou booléen | Saisissez une seule valeur de repli (Liquid pris en charge). |
| Champs (schéma avancé) | Saisissez une valeur de repli pour chaque champ défini dans la sortie de l'agent. |
| Schéma JSON (schéma avancé) | Braze lit votre schéma JSON et génère un champ de saisie pour chaque propriété afin que vous puissiez définir une valeur de repli par clé. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurer les valeurs de repli" }

Lorsqu'un Canvas Step Agent avec des valeurs de repli s'exécute dans une [étape Agent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step), Braze rend le repli par utilisateur et le stocke dans la variable de sortie au lieu de `null`. Si vous ne configurez pas de valeurs de repli, les invocations échouées laissent la sortie Canvas non définie (`null`).

Pour le comportement à l'exécution, consultez [Gestion des erreurs et comportement de repli]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior).

### Étape 6 : Tester l'agent {#step-6-test-the-agent}

Le volet **Preview** est une instance de l'agent qui s'affiche sous forme de panneau côte à côte dans l'expérience de configuration. Vous pouvez utiliser cette section pour tester l'agent pendant que vous le créez ou le mettez à jour, afin de l'expérimenter de manière similaire aux utilisateurs finaux. Cette étape vous aide à confirmer qu'il se comporte comme prévu et vous donne l'occasion de peaufiner les réglages avant la mise en production.

1. Dans le champ **Test your agent**, saisissez des données client ou des réponses client d'exemple — tout ce qui reflète des scénarios réels que votre agent devra gérer.
2. Prévisualisez la réponse de l'agent pour un utilisateur aléatoire, un utilisateur existant ou un utilisateur personnalisé.
3. Sélectionnez **Simulate response**. L'agent s'exécutera en fonction de votre configuration et affichera sa réponse.

{% alert note %}
Les exécutions de test sont comptabilisées dans votre limite d'invocations quotidiennes.
{% endalert %}

![Agent Console montrant le volet Preview pour tester un agent personnalisé. L'interface affiche un champ d'entrées d'exemple avec des données client, un bouton d'exécution du test et une zone de réponse où la sortie de l'agent apparaît.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Examinez la sortie avec un regard critique. Posez-vous les questions suivantes :

- Le contenu est-il conforme à l'image de marque ?
- La logique de décision oriente-t-elle les clients comme prévu ?
- Les valeurs calculées sont-elles exactes ?

Si quelque chose ne semble pas correct, mettez à jour la configuration de l'agent et testez à nouveau. Exécutez plusieurs entrées différentes pour voir comment l'agent s'adapte à différents scénarios, en particulier les cas limites comme l'absence de données ou les réponses invalides.

{% alert tip %}
Évitez de dire à l'agent exactement ce que vous ne voulez pas qu'il fasse. Les LLM peuvent tout de même générer ce contenu si vous le mentionnez dans les instructions.
{% endalert %}

### Étape 7 : Utiliser votre agent {#step-7-use-your-agent}

Votre agent est maintenant prêt à être utilisé ! Pour plus de détails, consultez [Déployer des agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents).

## Modèles d'agents créés avec Operator {#agent-templates-built-with-operator}

Operator peut préconfigurer les instructions, les champs de sortie et le contexte pour les modèles de départ suivants de la Console des agents. Choisissez un modèle dans Operator ou demandez à Operator d'en appliquer un par son nom.

### Modèles d'agents d'étape Canvas {#canvas-step-agent-templates}

| Modèle | Description | Exemple de sortie |
| --- | --- | --- |
| Rédacteur personnalisé | Génère du contenu spécifique au canal à partir des attributs utilisateur, du contexte Canvas et des directives de marque | Ligne d'objet et accroche d'e-mail ; titre et corps de notification push |
| Analyste de commentaires | Analyse les commentaires ouverts issus d'enquêtes ou du support en champs structurés pour le branchement Canvas | Sentiment, sujet, prochaine action recommandée |
| Routeur de parcours | Dirige chaque utilisateur vers le chemin Canvas le plus pertinent en fonction de son profil et du contexte du parcours | Nom du chemin ou valeur booléenne pour les étapes d'arbre décisionnel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Modèles d'agents d'étape Canvas" }

### Modèles d'agents de catalogue {#catalog-agent-templates}

| Modèle | Description | Exemple de sortie |
| --- | --- | --- |
| Rédacteur de descriptions | Rédige de courtes descriptions marketing à partir des colonnes existantes du catalogue | Description de produit ou de destination |
| Catégoriseur d'articles | Attribue des catégories ou des étiquettes à partir des données de la ligne | Libellés de catégorie pour le filtrage et les recommandations |
| Traducteur de localisation | Traduit les chaînes de caractères du catalogue dans les langues cibles en respectant les limites de caractères | Texte localisé par langue |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Modèles d'agents de catalogue" }

## Ressources associées {#related-resources}

- [Référence pour les agents]({{site.baseurl}}/user_guide/brazeai/agents/reference)
- [Questions fréquentes]({{site.baseurl}}/user_guide/brazeai/agents/faq)
- [Webinaire Braze sur l'IA en action : 3 nouveaux cas d'usage pour la personnalisation 1:1](https://www.braze.com/resources/webinars-and-events/ai-in-action-use-cases)