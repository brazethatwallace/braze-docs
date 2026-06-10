---
nav_title: Déployer des agents
article_title: Déployer des agents personnalisés
description: "Découvrez comment utiliser les agents personnalisés dans Braze après les avoir créés."
alias: /deploying-agents/
page_order: 2
---

# Déployer des agents personnalisés {#deploy-custom-agents}

> Découvrez comment utiliser les agents personnalisés dans les étapes du Canvas ou les champs du catalogue après les avoir créés. Pour une introduction, consultez [Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/).

## Agents dans Canvas {#agents-in-canvas}

Vous pouvez utiliser des agents comme étapes d'un parcours pour personnaliser les messages ou guider la prise de décision en temps réel. Pour des instructions détaillées sur la configuration, consultez [Étape Agent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/).

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

## Agents dans les catalogues {#agents-in-catalogs}

Vous pouvez appliquer un agent aux champs du catalogue afin qu'il génère ou calcule automatiquement des valeurs pour chaque ligne. L'agent s'exécutera également sur les nouvelles lignes ajoutées au catalogue à l'avenir.

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

### Étapes {#steps}

![Une étape Agent dans un champ de catalogue.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Pour ajouter un agent à votre champ de catalogue :

1. Dans votre catalogue, ajoutez un nouveau champ.
2. Sélectionnez **Apply AI agent**.
3. Affectez un agent à ce champ.
4. Sélectionnez les colonnes à transmettre en entrée. Si aucune n'est sélectionnée, l'agent aura accès à toutes les colonnes du catalogue.
5. Décidez si l'agent doit recalculer les champs lorsque les lignes du catalogue sont mises à jour. Si vous ne sélectionnez pas cette option, l'agent ne s'exécutera qu'une seule fois par ligne.
6. Sélectionnez **Add fields** pour déployer l'agent et consulter les estimations de coûts. La fenêtre modale **Cost estimation** indique le nombre de fois que l'agent s'exécutera sur ce catalogue, soit approximativement le nombre total de lignes. Pour continuer, sélectionnez **Confirm**.

### Fonctionnement des agents de catalogue {#how-catalog-agents-run}

Après le lancement, l'agent s'exécute et évalue chaque ligne en intégrant les colonnes sélectionnées dans son contexte pour produire un résultat. Les agents s'exécutent sur toutes les nouvelles lignes ajoutées après le déploiement de l'agent. Si vous avez sélectionné **Recalculate when catalog rows update**, toutes les valeurs de ce champ sont mises à jour lorsque les champs source existants changent.

Vous pouvez actualiser et modifier les champs de votre catalogue qui utilisent des agents. Pour supprimer un agent d'une colonne, désélectionnez **Apply AI agent**. La colonne redevient alors une colonne non agentique, et les champs conservent les dernières valeurs appliquées par l'agent lors de sa dernière exécution sur le catalogue.

Les références circulaires dans les catalogues ne sont pas prises en charge, ce qui signifie que le scénario suivant ne peut pas se produire :

- La colonne agentique 1 utilise la colonne agentique 2 comme entrée
- La colonne agentique 2 utilise la colonne agentique 1 comme entrée

![L'option permettant de sélectionner « Apply AI agent » pour un champ du catalogue.]({% image_buster /assets/img/ai_agent/edit_agent_column.png %}){: style="max-width:80%;"}

{% alert note %}
Les agents de catalogue sont limités au traitement de valeurs d'entrée de 25 Ko maximum par ligne.
{% endalert %}

#### Définir les champs de réponse {#define-response-fields}

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

### Gestion des erreurs dans les catalogues {#error-handling-in-catalogs}

- Les invocations de catalogue ayant échoué ne font pas l'objet d'une nouvelle tentative, y compris en cas d'[erreurs de limite de débit]({{site.baseurl}}/user_guide/brazeai/agents/reference/#rate-limit-errors) du fournisseur LLM.
- Si l'appel API vers le fournisseur de modèle fondamental renvoie une autre erreur, comme une erreur de clé API invalide, la valeur du champ n'est pas mise à jour.
- Vous pouvez consulter les journaux de l'agent pour obtenir des détails sur les exécutions ayant échoué.

## Surveiller votre agent {#monitor-your-agent}

Dans la section **Usage** de votre agent, vous pouvez consulter et accéder aux endroits où l'agent est activement utilisé dans les catalogues et les Canvas.

![Section Usage de l'agent affichant deux agents actifs et un agent inactif pour les Canvas.]({% image_buster /assets/img/ai_agent/agent_usage.png %})

Dans la section **Logs** de votre agent, vous pouvez surveiller les appels réels de l'agent dans vos Canvas et catalogues. Vous pouvez filtrer par informations telles que la période, le résultat (réussite ou échec) ou l'emplacement de l'appel. Vous pouvez également sélectionner **Export CSV** pour exporter uniquement les journaux affichés sur la page actuelle.

{% alert tip %}
Vous pouvez également surveiller les erreurs de limite d'invocations quotidiennes dans le [Journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/).
{% endalert %}

![Journaux pour un agent AI Sentiment Score.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

Sélectionnez **View** pour un appel d'agent spécifique afin de consulter l'entrée, la sortie et l'ID utilisateur.

![Le panneau de détails d'un agent Random Sports Assignment affichant l'invite d'entrée, la réponse de sortie et l'ID utilisateur associé.]({% image_buster /assets/img/ai_agent/agent_logs_view.png %})

### Utiliser Currents {#use-currents}

Vous pouvez également utiliser ces événements Currents pour accéder aux schémas d'enregistrement Kafka :

- Événements d'exécution de l'agent
- Événements d'invocation d'outils

Consultez le [glossaire des événements d'engagement liés aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) pour plus de détails.

## Articles connexes {#related-articles}

- [Article de référence pour les agents]({{site.baseurl}}/user_guide/brazeai/agents/reference/)
- [Foire aux questions]({{site.baseurl}}/user_guide/brazeai/agents/faq/)