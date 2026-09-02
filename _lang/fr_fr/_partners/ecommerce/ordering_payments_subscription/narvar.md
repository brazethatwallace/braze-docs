---
nav_title: Narvar
article_title: Narvar
description: "Découvrez comment intégrer Narvar à Braze."
alias: /partners/narvar/
page_type: partner
search_tag: Partner
---

# Narvar

> Narvar est une plateforme post-achat qui renforce la fidélité des clients grâce au suivi des commandes, aux mises à jour des livraisons et à la gestion des retours. L'intégration de Braze et Narvar permet aux marques d'exploiter les événements de notification de Narvar pour déclencher des messages directement depuis Braze, en tenant les clients informés grâce à des mises à jour opportunes.

## Conditions préalables {#prerequisites}

| Condition | Description |
|-----------------------|-----------------------------------------------------------------------------------------------|
| Compte Narvar | Un compte Narvar est nécessaire pour bénéficier de ce partenariat. |
| Clé d'API REST Braze | Une clé d'API REST Braze avec l'autorisation `messages.send`. Elle peut être créée dans le tableau de bord de Braze depuis **Settings** > **API Keys**. |
| Endpoint REST Braze | L'[URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), qui dépend de l'URL de votre instance Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Fonctionnalités prises en charge {#supported-features}

| Type | Fonctionnalités prises en charge |
|-------|----------|
| Notifications | - Anticipation de la livraison<br>- Retard du transporteur<br>- Livraison standard effectuée |
| Canaux | Notifications push |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fonctionnalités prises en charge" }

{% alert note %}
Si vous êtes intéressé par d'autres types de notifications ou canaux, veuillez contacter votre CSM or gestionnaire de la satisfaction client or gestionnaire du succès des clients Braze et Narvar.
{% endalert %}

## Détails de l'intégration {#integration-details}

Pour chaque événement de notification, Narvar envoie une requête à l'endpoint Braze [`/messaging/send`]({{site.baseurl}}/api/endpoints/messaging/) afin de transmettre un message push à chaque consommateur abonné.

Narvar est responsable de la configuration des payloads de notification push pour chaque message. Actuellement, Narvar ne dispose pas d'une interface de conception intégrée pour les notifications push. Son équipe collaborera donc avec la vôtre pour déterminer et définir les exigences en matière de payload. Ces payloads peuvent être personnalisés dans la même mesure que ceux envoyés par votre propre système, y compris la prise en charge de marqueurs substitutifs à contenu variable, tels que les données relatives aux commandes et les détails concernant les consommateurs.

## Démarrer avec l'intégration Braze-Narvar {#getting-started-with-the-braze-narvar-integration}

1. **Contactez votre CSM or gestionnaire de la satisfaction client or gestionnaire du succès des clients Narvar** pour exprimer votre intérêt pour l'intégration.
2. **Désignez des environnements Braze** pour la pré-production et la production.
3. **Générez une clé d'API** dans Braze pour l'usage de Narvar.
4. **Générez des clés de Campaign** dans Braze si nécessaire.
5. **Fournissez les clés d'API et de Campaign** à Narvar par le biais d'un lien unique sécurisé.
6. **Partagez les détails du payload de notification push** pour finaliser la configuration.