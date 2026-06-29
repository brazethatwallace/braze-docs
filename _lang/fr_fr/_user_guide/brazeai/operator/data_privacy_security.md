---
nav_title: Confidentialité et sécurité des données
article_title: Confidentialité et sécurité des données pour BrazeAI Operator
page_order: 5
page_type: reference
description: "Cet article de référence explique comment BrazeAI Operator gère les données, y compris la conformité HIPAA, la conservation des données, la minimisation des informations personnelles identifiables et la gouvernance."
---

# Confidentialité et sécurité des données pour BrazeAI Operator {#data-privacy-and-security-for-brazeai-operator}

> BrazeAI Operator<sup>TM</sup> s'intègre à OpenAI pour fournir une assistance alimentée par l'intelligence artificielle. Cet article explique comment Operator gère les données, quelles informations sont partagées avec OpenAI, et comment minimiser l'exposition des informations personnelles identifiables (PII) et contrôler les accès.

## Comment Operator accède aux données {#how-operator-accesses-data}

L'accès d'Operator aux données client est strictement événementiel et limité à la portée de chaque invocation, et non persistant. Chaque message utilisateur ou événement de navigation lorsqu'Operator est ouvert déclenche une requête HTTP distincte vers OpenAI. Il n'y a pas de connexion permanente ni de flux de données persistant.

OpenAI n'a pas d'accès direct aux magasins de données Braze ni à la table utilisateur complète. Le LLM ne reçoit que le payload spécifique associé à la requête active.

### Quelles données sont incluses dans chaque requête {#what-data-is-included-in-each-request}

Chaque payload de requête envoyé à OpenAI peut inclure les éléments suivants :

- **Métadonnées système :** prompts système rédigés par Braze et schémas d'outils (définitions des outils que le LLM peut invoquer).
- **Message de l'utilisateur du tableau de bord :** la saisie textuelle de l'utilisateur du tableau de bord.
- **Résultats des outils :** résultats de recherche contenant des noms, des ID et des données associées.
- **Contenu de la page scrapé :** contenu de la page active du tableau de bord, tronqué à environ 4 000 caractères.
- **Chaînes de contexte de la page :** chaînes contextuelles provenant de la page active du tableau de bord.

## Sous-traitants de données {#data-sub-processors}

### Fournisseurs de modèles en tant que sous-traitants ou fournisseurs tiers {#model-providers-as-sub-processors-or-third-party-providers}

Lorsque vous utilisez une intégration avec un fournisseur de LLM fourni par Braze via les services Braze (« LLM fourni par Braze »), les fournisseurs de ce LLM agissent en tant que sous-traitants de Braze, conformément aux termes de l'addendum relatif au traitement des données (DPA) entre vous et Braze. BrazeAI Operator<sup>TM</sup> s'intègre à OpenAI.

### Comment les données sont utilisées avec OpenAI {#how-data-is-used-with-openai}

Pour générer des résultats d'intelligence artificielle via les fonctionnalités BrazeAI qui exploitent OpenAI (« Output »), Braze enverra certaines informations (« Input ») à OpenAI. L'Input se compose de vos prompts, du contenu affiché dans le tableau de bord et des données de l'espace de travail pertinentes pour vos requêtes. Conformément aux [engagements de la plateforme API d'OpenAI](https://openai.com/enterprise-privacy/), les données envoyées à l'API d'OpenAI via Braze ne sont pas utilisées pour entraîner ou améliorer les modèles OpenAI. Entre vous et Braze, l'Output est votre propriété intellectuelle. Braze ne revendiquera aucun droit d'auteur sur cet Output. Braze ne fournit aucune garantie de quelque nature que ce soit concernant tout contenu généré par l'intelligence artificielle, y compris l'Output.

## Conformité HIPAA et conservation des données {#hipaa-compliance-and-data-retention}

### Conformité HIPAA {#hipaa-compliance}

Si vous utilisez le cluster US-02 de Braze, Operator est couvert par l'accord de partenariat commercial (BAA) de Braze, et les informations de santé protégées (PHI) peuvent être soumises à la fonctionnalité conformément aux exigences HIPAA. Ne soumettez pas de PHI soumises à la réglementation HIPAA lorsque vous utilisez Operator dans d'autres clusters Braze.

### Suppression des PII {#pii-redaction}

Il n'existe pas de couche automatisée de suppression des PII dans le pipeline de requêtes d'Operator. Les données sont envoyées entièrement brutes et ne sont pas anonymisées avant leur transmission à OpenAI. L'accès est limité à la page active du tableau de bord ou à la saisie de l'utilisateur du tableau de bord, mais aucun filtrage de contenu n'est appliqué avant la transmission.

### Conservation des données par OpenAI {#openai-data-retention}

La durée de conservation des données envoyées via Operator par OpenAI dépend de votre cluster :

| Cluster | Conservation |
| --- | --- |
| US-02 (clients HIPAA) | Zéro conservation des données (ZDR). Les données ne sont pas stockées par OpenAI après le traitement. |
| Tous les autres clusters | 30 jours pour la surveillance des abus. Il s'agit d'une période de conservation standard du secteur imposée par OpenAI. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conservation des données OpenAI par cluster" }

### Entraînement des modèles {#model-training}

Les données envoyées à l'API d'OpenAI via Braze ne sont pas utilisées pour entraîner ou améliorer les modèles OpenAI. Cela est régi par des accords contractuels entre Braze et OpenAI ainsi que par les engagements de la plateforme API d'OpenAI. OpenAI agit en tant que sous-traitant de Braze, et toutes les données personnelles sont soumises au DPA entre Braze et ses clients.

### Routage des données dans l'UE {#eu-data-routing}

Le routage des données dans l'UE n'est pas actuellement implémenté pour Operator, et aucun plan n'est prévu pour le mettre en œuvre.

## Minimiser l'exposition des PII {#minimize-pii-exposure}

Vous pouvez prendre plusieurs mesures pour limiter l'exposition des PII lorsque vous utilisez Operator :

- **Désactivez le paramètre Afficher les PII** pour tous les utilisateurs qui utilisent Operator. Si un utilisateur ne peut pas voir les PII, Operator ne peut pas y accéder non plus.
- **N'ouvrez pas Operator sur une page de profil utilisateur.** Le contenu de la page est scrapé et inclus dans chaque requête envoyée à OpenAI.
- **Lors des tests, utilisez un profil utilisateur personnalisé** plutôt que de sélectionner un profil existant. C'est le comportement par défaut d'Operator.
- **Ne saisissez pas et ne collez pas de PII** directement dans le prompt d'Operator.
- **Désactivez l'approbation automatique des actions** pour garder le contrôle sur ce qu'Operator peut accéder et exécuter.
- **Ne demandez pas à Operator d'afficher les valeurs de prévisualisation des attributs** lors de la création d'un segment ou de l'écriture de Liquid.

## Gouvernance et contrôle d'accès {#governance-and-access-control}

### Restreindre l'accès à Operator {#restrict-access-to-operator}

L'accès à Operator est géré au niveau de l'espace de travail via les [autorisations granulaires des utilisateurs]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/). Les administrateurs peuvent accorder ou révoquer l'autorisation **Use BrazeAI Operator** pour des utilisateurs individuels, garantissant que seul le personnel autorisé peut interagir avec l'outil. Sans ces autorisations spécifiques, l'interface d'Operator est entièrement masquée et les endpoints backend restent sécurisés.

### Modèle avec intervention humaine {#human-in-the-loop-model}

Par défaut, Operator nécessite une approbation explicite avant de valider toute modification. Les modifications proposées sont présentées sous forme de [cartes d'action]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/) pour vérification. Si un utilisateur rejette une proposition, aucune modification n'est effectuée. Si un utilisateur accepte une proposition, le tableau de bord est mis à jour, mais les modifications restent en attente et doivent être enregistrées ou lancées manuellement pour devenir persistantes.

Les utilisateurs peuvent activer **l'approbation automatique des actions** dans le panneau de chat d'Operator, ce qui entraîne l'exécution immédiate des actions suggérées sans vérification manuelle. Même avec l'approbation automatique activée, certaines actions nécessitent toujours une approbation explicite pour des raisons de sécurité, notamment la génération d'images et la modification des paramètres au niveau de l'espace de travail.

### Héritage des autorisations utilisateur {#user-permission-inheritance}

Operator hérite intégralement du profil d'autorisations de l'utilisateur connecté. Il ne peut pas consulter des données ni exécuter des actions, telles que des modifications de Campaign, que l'utilisateur n'est pas déjà autorisé à effectuer de manière indépendante.

### Auditer l'utilisation de l'équipe {#audit-team-usage}

Téléchargez le [rapport d'événements de sécurité]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#security-event-report) de Braze pour surveiller l'utilisation de l'équipe. L'événement « Requested BrazeAI Operator Response » fournit une piste d'audit complète, vous permettant de vérifier les entrées exactes fournies à Operator.