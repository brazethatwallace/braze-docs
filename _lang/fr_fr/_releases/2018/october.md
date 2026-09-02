---
nav_title: octobre
page_order: 4
noindex: true
page_type: update
description: "Cet article contient les notes de version d’octobre 2018."
---
# Octobre 2018 {#october-2018}

{% comment %}
  À ajouter ultérieurement...
  Activation/Désactivation du groupe de contrôle selon une sélection intelligente
  La boîte de sélection intelligente comporte désormais une case à cocher qui vous permet de [basculer l'utilisation d'un groupe de contrôle]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing#including-a-control-group). Si activé, le groupe de contrôle fera 20 % de la taille de l'audience et évoluera pendant que la sélection intelligente optimise ainsi les tailles d'audience en fonction des variantes.
  Assistant de paramètres de Canvas Entry (Bêta)
  L’interface utilisateur de Canvas sera simplifiée pour éviter les tâches manquées et les erreurs résultantes. Les configurations de canvas, en particulier, seront désormais affichées dans un assistant, similaire à la conception de l'assistant de campagnes. Ce n’est pas reflété dans notre documentation actuellement, car c’est déployé progressivement. Revenez bientôt pour en savoir plus !
  API Groupe d’abonnement (masqué)
  Braze a mis à disposition un nouvel appel GET pour vous permettre de faire des requêtes basées sur un identifiant externe ou une adresse électronique. Vous recevrez ensuite tous les groupes d’abonnement associés à cet utilisateur.
{% endcomment %}

## Calculer les statistiques exactes d'audience pour les Campaigns {#calculate-exact-audience-stats-for-campaigns}

Vous pouvez désormais accéder à **Campaign Analytics** et calculer les statistiques exactes de votre audience. Cliquez sur **Calculate Exact Stats** dans le pied de la section **Target Audiences**, et les statistiques exactes d'audience s'afficheront. Vous devrez enregistrer la Campaign avant de procéder au calcul (les Campaigns en brouillon seront enregistrées comme brouillons).

## Dépréciation de Windows 8 {#windows-8-deprecation}

Braze ne prend plus en charge Windows 8 depuis le 10 octobre 2018.

## Hub de partenariats {#partnerships-hub}

Vous pouvez désormais trouver une liste de vos intégrations sur la plateforme Braze sous **Intégrations**, ainsi que les clés d'intégration et les instructions.

## Calculs des analyses e-mail {#email-analytics-calculations}

Braze calcule désormais toutes les analyses e-mail en utilisant les données d'événements de notre partenaire d'envoi d'e-mails (ESP) afin d'améliorer considérablement la précision de nos analyses e-mail. Cette solution utilise Postgres, une solution de base de données open source, pour garantir l'intégrité des données.

{% alert important %}
Les ouvertures uniques et les clics uniques dépendent actuellement encore des données agrégées fournies par nos partenaires d'envoi d'e-mails. Un travail est en cours pour calculer ces statistiques d'unicité en utilisant la même infrastructure introduite dans cette version.
{% endalert %}

## Commandes du panneau de composition {#composer-panel-controls}

Les commandes du composeur de messages ont été actualisées pour inclure un libellé associé aux icônes afin d'améliorer la convivialité et la navigation.

## Azure pour Currents {#azure-for-currents}

Les clients Braze utilisant Currents peuvent désormais voir [Azure]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents) comme une intégration potentielle.

## Extensions des champs de saisie {#input-field-expansions}

Vous pouvez désormais agrandir les zones de saisie pour les lignes d'objet des e-mails et les titres des notifications push.