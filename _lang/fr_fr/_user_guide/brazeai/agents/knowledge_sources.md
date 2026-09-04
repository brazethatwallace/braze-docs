---
nav_title: Sources de connaissances
article_title: Sources de connaissances
description: "Cet article de référence explique comment créer et gérer des sources de connaissances pour vos agents BrazeAI."
page_type: reference
page_order: 3.5
---

# Sources de connaissances {#knowledge-sources}

> Les sources de connaissances aident vos agents IA à interpréter les données du catalogue et à récupérer les informations pertinentes pour atteindre vos objectifs. Pour une introduction aux agents Braze, consultez [Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents). Pour ajouter des connaissances à un agent, consultez [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#add-resources).

{% alert important %}
Les sources de connaissances pour la Console des agents sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

## Comment ça fonctionne {#how-it-works}

Les sources de connaissances sont un type de contexte d'agent. Un agent IA peut référencer une source de connaissances pour récupérer des données du catalogue de manière plus précise que si le catalogue était directement référencé dans les instructions de l'agent.

Imaginons que vous créez un agent pour recommander des restaurants à New York en fonction de la cuisine préférée d'un utilisateur, qui est un attribut personnalisé. Cet agent référence la source de connaissances du catalogue « nyc_restaurants ». Lorsque vous créez cette source de connaissances, vous n'incluez que les champs dont l'agent a besoin, tels que le nom du restaurant, l'emplacement et le type de cuisine, et vous excluez les autres colonnes du catalogue qui ne sont pas utiles aux recommandations.

Les instructions de l'agent décrivent clairement son rôle et ses contraintes :

{% raw %}
```
You are a restaurant recommendation agent. Use your knowledge to help find restaurants for the user. Only include filters in your knowledge source query. Don't ask any followup questions. The user's favorite cuisine is {{custom_attribute.${favorite_cuisine}}}
```
{% endraw %}

Si la cuisine préférée d'un utilisateur est la pizza, l'agent peut renvoyer la réponse suivante en se basant sur la source de connaissances :

```
Here are some pizza recommendations for you:
- Dale's Pizza (Greenwich Village, Manhattan): Dale's Pizza invites you to savor the taste of authentic New York. Nestled in the heart of Manhattan, this iconic pizzeria offers a warm and inviting atmosphere perfect for any occasion.
- Pizza Palace (Carroll Gardens, Brooklyn): Pizza Palace is a highly-rated culinary gem renowned for its exquisite pizza. This inviting spot offers a warm and modern dining experience.
```

## Créer une source de connaissances {#create-a-knowledge-source}

Pour créer une source de connaissances :

1. Accédez à **Console des agents** > **Sources de connaissances**.
2. Sélectionnez **Ajouter une source de connaissances**. Dans le menu déroulant, sélectionnez **Catalogue**.
3. Sélectionnez le catalogue dans le menu déroulant.
4. Passez en revue les champs du catalogue et désélectionnez ceux qui ne s'appliquent pas au cas d'usage de votre agent. Nous recommandons d'exclure les champs du catalogue qui ne sont pas utiles pour la récupération ou la génération — limitez la source de connaissances aux seuls champs dont votre agent a besoin.
5. (facultatif) Ajoutez une description pour décrire le contenu de la source de connaissances.
6. Sélectionnez **Ajouter une source de connaissances**.

Inclure tous les champs du catalogue peut ajouter un contexte inutile et réduire la qualité des résultats. Désélectionner les champs qui ne sont pas pertinents pour votre cas d'usage aide l'agent à se concentrer sur les données qui comptent.

![Une source de connaissances « nyc_restaurants » qui référence le catalogue « nyc_restaurants ».]({% image_buster /assets/img/ai_agent/knowledge_source_example.png %})

Vous pouvez également créer une source de connaissances pendant la création d'un agent en accédant à la section **Instructions** de votre agent. Sélectionnez **Ajouter des connaissances** > **Créer une source de connaissances**.

## Utiliser une source de connaissances dans votre agent IA {#use-a-knowledge-source-in-your-ai-agent}

Vous pouvez gérer les sources de connaissances depuis la section **Sources de connaissances**. Vous y trouverez des détails tels que les sources de connaissances actives et la date de leur dernière synchronisation. Notez que le nom de la source de connaissances correspond au nom du catalogue utilisé comme source.

Pour utiliser une source de connaissances dans votre agent IA :

1. Accédez à la section **Instructions** de votre agent.
2. Sélectionnez **+ Contexte de l'agent** > **Ajouter des connaissances**.
3. Dans le menu déroulant, sélectionnez la source de connaissances.

Votre agent peut désormais référencer la source de connaissances et récupérer les données pertinentes du catalogue.

## Questions fréquentes {#frequently-asked-questions}

### Comment fonctionnent les sources de connaissances ? {#how-do-knowledge-sources-work}

Convertir un catalogue en source de connaissances aide les agents Braze à comprendre le véritable sens des mots et des expressions du catalogue, afin qu'ils puissent trouver plus efficacement des données pertinentes pour produire de meilleurs résultats.

### Quand dois-je créer une source de connaissances ? {#when-should-i-create-a-knowledge-source}

Créez une source de connaissances lorsque vous configurez un agent personnalisé (agent d'étape Canvas ou agent de catalogue) qui a besoin de données de catalogue comme contexte. Les sources de connaissances aident les agents à récupérer les données du catalogue de manière plus précise que si le catalogue était directement référencé dans les instructions de l'agent.

### Si un agent dispose d'une source de connaissances comme contexte, dois-je également lui attribuer le catalogue d'origine comme contexte ? {#if-an-agent-has-been-given-a-knowledge-source-as-context-do-i-also-need-to-assign-the-original-catalog-as-context}

Non. La source de connaissances remplace le catalogue en tant que contexte de l'agent — vous n'avez pas besoin d'attacher les deux. Lorsque vous créez la source de connaissances, n'incluez que les champs du catalogue dont votre agent a besoin.

### Comment évaluer l'efficacité d'une source de connaissances ? {#how-should-i-evaluate-the-effectiveness-of-a-knowledge-source}

Dupliquez un agent existant qui référence un catalogue standard, puis remplacez-le par la source de connaissances équivalente. Exécutez quelques invocations de test dans la Console des agents pour vérifier la précision, puis envisagez soit de remplacer l'agent existant là où il est déployé, soit de réaliser un test A/B entre l'ancien agent et le nouveau (en utilisant le chemin d'expérience) pour évaluer l'impact sur les performances.