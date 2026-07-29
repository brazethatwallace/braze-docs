---
nav_title: Configurer l'orchestration
article_title: Configurer l'orchestration
page_order: 4
page_type: reference
description: "Cet article explique comment configurer l'orchestration pour BrazeAI Decisioning Studio, notamment le choix de votre CEP, la collecte des identifiants requis et la configuration de votre intégration."
toc_headers: h2
---

# Configurer l'orchestration {#set-up-orchestration}

> Les agents de décision doivent se connecter à une plateforme d'engagement client (CEP) pour orchestrer les communications une fois qu'ils ont ingéré les données client et personnalisé au niveau 1:1. Cet article couvre ce que vous devez préparer et comment configurer l'intégration pour chaque CEP prise en charge.

## Qu'est-ce que l'orchestration ? {#what-is-orchestration}

L'orchestration est la connexion entre Decisioning Studio et votre plateforme d'engagement client (CEP). Une fois que votre agent de décision a déterminé l'action optimale pour chaque client, l'orchestration exécute ces décisions en déclenchant des communications personnalisées via votre CEP.

Voyez les choses ainsi :

- **Decisioning Studio** décide *quoi* envoyer et *quand* l'envoyer
- **Votre CEP** gère *comment* l'envoyer

## Choisir votre CEP {#choose-your-cep}

La première étape consiste à choisir quel CEP utiliser avec Decisioning Studio. Votre choix affecte la complexité de la configuration et les fonctionnalités disponibles.

### CEP pris en charge {#supported-ceps}

| CEP | Type d'intégration | Complexité de la configuration |
|-----|-----------------|------------------|
| **Braze** | Intégration API native (recommandée) | Faible |
| **Salesforce Marketing Cloud** | Événements API + Journey Builder | Moyenne |
| **Autres CEP** | Personnalisée (fichier de recommandation) | Élevée |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CEP pris en charge" }

{% alert tip %}
Si vous utilisez déjà Braze comme CEP, nous vous recommandons d'utiliser l'intégration native Braze pour une expérience de configuration optimale.
{% endalert %}

## Prérequis {#prerequisites}

Avant de configurer l'orchestration, rassemblez les éléments suivants en fonction de la plateforme d'engagement client (CEP) choisie.

{% tabs %}
{% tab Braze %}

| Exigence | Description |
|------|-------------|
| **Clé API REST** | Une nouvelle clé API avec des permissions pour les données utilisateur, les messages, les Campaigns, Canvas, les Segments et les modèles. |
| **URL du tableau de bord de Braze** | L'URL de votre instance Braze (par exemple, `https://dashboard-01.braze.com`). |
| **ID de l'application** | La clé API associée à l'application que vous souhaitez suivre (disponible dans **Paramètres** > **Paramètres de l'application**). |
| **Nom d'affichage et adresse e-mail** | Les informations d'expéditeur à utiliser pour vos Campaigns (disponibles dans **Paramètres** > **Préférences e-mail**). |
| **Modèles de base** | Les modèles de messages que votre agent utilise pour l'orchestration. Vous créez des Campaigns déclenchées par API pour chaque modèle. |
| **ID d'utilisateur test** | Un ID utilisateur pour tester l'intégration avant le lancement. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| Exigence | Description |
|------|-------------|
| **Identifiants du package d'application** | Client ID, Client Secret, Authentication Base URI, REST Base URI et SOAP Base URI provenant d'un package installé avec une intégration API serveur à serveur. |
| **Permissions API** | Portées pour les canaux, les ressources, les automatisations, les parcours, les contacts, les extensions de données et les événements de suivi. |
| **Extensions de données** | Vous avez besoin d'extensions de données pour les données d'abonnés, les données d'engagement et les recommandations. |
| **Modèles d'e-mail** | Les modèles que vous souhaitez que Decisioning Studio utilise, avec les ID de modèle pour chacun. |
| **Accès à Journey Builder** | Accès pour créer et activer des parcours multi-étapes avec des sources d'entrée par événement API. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

{% endtab %}
{% tab Autres CEP %}

Si vous utilisez une CEP autre que Braze ou Salesforce Marketing Cloud, Decisioning Studio peut s'intégrer via une approche par fichier de recommandations :

| Élément | Description |
|------|-------------|
| **Capacité d'ingestion de données** | Votre CEP doit être capable d'ingérer des fichiers de recommandations (généralement CSV ou JSON) contenant des décisions personnalisées pour chaque client. |
| **Prise en charge du contenu dynamique** | Vos Campaigns doivent prendre en charge le remplissage dynamique des champs en fonction des données de recommandation. |
| **Ressources d'ingénierie personnalisées** | Votre équipe doit construire l'intégration pour lire les fichiers de recommandations et déclencher les communications. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

{% endtab %}
{% endtabs %}

## Planifier vos campagnes {#plan-your-campaigns}

Avant de configurer l'orchestration, tenez compte des détails suivants :

### Modèles de base {#base-templates}

Un modèle de base est tout modèle de message que votre agent de décision pourrait utiliser. Considérez les points suivants :

- **Combien de modèles ?** Votre agent peut fonctionner avec un seul modèle ou plusieurs. S'il y en a plusieurs, l'agent peut personnaliser le modèle que chaque client reçoit.
- **Quels canaux ?** E-mail, notification push, SMS ou une combinaison. Chaque canal peut nécessiter des modèles et des Campaigns distincts.
- **Quels éléments dynamiques ?** Identifiez les parties de votre message que l'agent personnalise (lignes d'objet, CTA, offres, timing, etc.). Ceux-ci deviennent des propriétés de déclenchement API ou des marques substitutives dynamiques.

### Paramètres de rééligibilité {#re-eligibility-settings}

Vos Campaigns doivent permettre aux utilisateurs de recevoir des messages plusieurs fois :

- Pour les tests, vous envoyez la même Campaign au même utilisateur de manière répétée
- En production, l'agent peut déterminer que la même Campaign est optimale pour un utilisateur sur des jours consécutifs

{% alert note %}
Bien que vous configuriez la rééligibilité pour les tests, les agents Decisioning Studio sont conçus pour respecter les limites de fréquence et n'envoient pas la même Campaign à un utilisateur plus d'une fois par jour en production.
{% endalert %}

### Propriétés de déclenchement API {#api-trigger-properties}

Pour les intégrations Braze, planifiez les dimensions que votre agent optimise. Celles-ci deviennent des propriétés de déclenchement API qui transmettent des valeurs dynamiques dans vos Campaigns :

| Exemple de dimension | Propriété de déclenchement API |
|-------------------|---------------------|
| Ligne d'objet | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| Appel à l'action | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| Offre | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| Montant de la remise | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Propriétés de déclenchement API" }

## Configuration de l'intégration {#integration-setup}

Sélectionnez votre plateforme d'engagement client dans cette liste pour commencer la configuration de l'intégration.

{% tabs %}
{% tab Braze %}

## Configurer l'intégration Braze {#set-up-braze-integration}

Suivez ces étapes pour intégrer un agent Decisioning Studio avec les capacités d'orchestration de Braze (l'équipe de services Braze est disponible pour vous aider) :

### Étape 1 : Créer une clé API {#step-1-create-an-api-key}

Accédez à **Paramètres** > **Clés API**, puis créez une nouvelle clé avec les permissions suivantes :

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### Étape 2 : Configurer des campaigns déclenchées par API {#step-2-set-up-api-triggered-campaigns}

Configurez une Campaign déclenchée par API pour chaque modèle de base avec des propriétés de déclenchement API pour toutes les dimensions optimisées.

Un modèle de base est tout modèle que l'agent Decisioning peut utiliser pour orchestrer des messages. Un agent Decisioning peut avoir 1 modèle de base ou plusieurs, auquel cas le choix du bon modèle de base pour chaque client est l'une des décisions que l'agent personnalise.

### Étape 3 : Configurer la rééligibilité {#step-3-configure-re-eligibility}

Assurez-vous que toutes les Campaigns déclenchées par API permettent aux utilisateurs de redevenir éligibles dans un délai de 15 minutes.

![Diagramme de limitation de fréquence Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Bien que l'agent Decisioning Studio n'envoie jamais la même Campaign plus d'une fois par jour, vous souhaitez pouvoir envoyer les mêmes Campaigns plusieurs fois par jour à des fins de test.
{% endalert %}

### Étape 4 : Ajouter des marques substitutives dynamiques {#step-4-add-dynamic-placeholders}

Celles-ci servent de marques substitutives dynamiques pour les décisions que l'agent Decisioning Studio optimise.

#### Exemple 1 : Campaign e-mail {#example-1-email-campaign}

Supposons que l'agent Decisioning Studio optimise une Campaign e-mail. La configuration pourrait ressembler à ceci :

![Exemple de Campaign e-mail Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

En supposant que l'agent optimise le choix des modèles et le message d'appel à l'action (CTA), une Campaign déclenchée par API devrait être créée pour chaque modèle, et la section CTA d'un modèle pourrait ressembler à :

![Exemple de section CTA d'une Campaign e-mail Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### Exemple 2 : Campaign de notification push {#example-2-push-campaign}

Supposons qu'un agent Decisioning Studio optimise le message d'une Campaign de notification push. La configuration pourrait ressembler à ceci :

![Exemple de Campaign de notification push Decisioning Studio - configuration]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Exemple de Campaign de notification push Decisioning Studio - contenu]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

Ce qui donne le message suivant :

![Exemple de Campaign de notification push Decisioning Studio - résultat]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### Exemple 3 : Campaign SMS {#example-3-sms-campaign}

Supposons que l'agent Decisioning Studio optimise les champs d'une Campaign SMS. La configuration pourrait ressembler à ceci :

![Exemple de Campaign SMS Decisioning Studio - configuration]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Exemple de Campaign SMS Decisioning Studio - contenu]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

Ce qui donne le message suivant :

![Exemple de Campaign SMS Decisioning Studio - résultat]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Configurer l'intégration SFMC {#set-up-sfmc-integration}

Decisioning Studio prend en charge l'intégration native avec Salesforce Marketing Cloud. Decisioning Studio déclenche des événements API dans un parcours avec les données nécessaires pour remplir les éléments dynamiques.

{% alert important %}
Lors de la configuration des cas d'usage, **les ID API doivent être saisis en majuscules**. Cela inclut les ID de parcours, les ID de Campaign et tout autre identifiant. Si les ID API sont saisis en minuscules alors que vos données SFMC contiennent des UUID en majuscules, les filtres d'événements ne correspondront pas et les indicateurs de reporting ne se rempliront pas correctement.
{% endalert %}

{% endtab %}
{% tab Autres plateformes %}

## Configurer d'autres intégrations de plateformes d'engagement client {#set-up-other-cep-integrations}

Decisioning Studio peut s'intégrer à n'importe quelle plateforme d'engagement client. Cependant, cela peut nécessiter un travail d'ingénierie personnalisé de la part de votre équipe, car Decisioning Studio ne peut pas déclencher de communications directement.

Dans ce scénario, l'agent fournit un « fichier de recommandations ». Ce fichier contient des lignes pour chaque client, avec des colonnes indiquant toutes les décisions personnalisées pour ce client.

Par exemple, le fichier de recommandations suivant :

![Exemple de fichier de recommandations Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

Pourrait être utilisé pour optimiser une Campaign e-mail qui ressemble à ceci :

![Exemple de Campaign e-mail optimisée par Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## Bonnes pratiques {#best-practices}

Gardez ces bonnes pratiques à l'esprit lorsque vous préparez l'orchestration :

1. **Commencez avec un périmètre restreint :** Utilisez un seul canal et un ou deux modèles au départ. Vous pourrez élargir par la suite en fonction de ce qui fonctionne.
2. **Testez minutieusement :** Avant le lancement, testez votre intégration avec un petit groupe d'utilisateurs pour vérifier que le contenu dynamique s'affiche correctement.
3. **Documentez votre configuration :** Gardez une trace des identifiants de Campaign, des identifiants de modèles, des clés API et des autres identifiants. Vous en aurez besoin pour les référencer dans le portail Decisioning Studio.
4. **Coordonnez-vous avec votre équipe :** La mise en place de l'orchestration peut impliquer les équipes marketing, techniques et data. Assurez-vous que chacun comprend son rôle dans le processus.
5. **Anticipez les données de retour :** L'orchestration envoie des messages et collecte les données d'engagement et de conversion qui aident votre agent à apprendre. Consultez [Préparer vos données]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data) pour plus de détails.

## Étapes suivantes {#next-steps}

Après avoir configuré l'orchestration, passez à la conception de votre agent :

- [Concevoir des agents de décision]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/design_agents)