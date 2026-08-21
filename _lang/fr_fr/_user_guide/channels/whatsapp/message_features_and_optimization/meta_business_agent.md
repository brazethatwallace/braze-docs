---
nav_title: Meta Business Agent
article_title: Meta Business Agent et Braze WhatsApp
page_order: 8
description: "Ce guide explique comment Meta Business Agent interagit avec un numéro de téléphone WhatsApp Business connecté à Braze, et à quoi vous attendre si vous l'activez."
page_type: reference
channel:
  - WhatsApp
alias: /meta_business_agent/
hidden: true
noindex: true
---

# Meta Business Agent et Braze WhatsApp {#meta-business-agent-and-braze-whatsapp}

> Meta Business Agent peut répondre aux messages WhatsApp entrants sur un numéro également connecté à Braze. Cet article explique comment ces deux systèmes partagent la visibilité des messages, comment activer l'agent dans les outils de Meta, et comment la facturation est répartie. Il reflète les fonctionnalités et la documentation du produit Meta Business Agent en date d'août 2026.

Meta continue de développer activement Meta Business Agent, certains détails peuvent donc évoluer ; consultez la [documentation de Meta Business Agent](https://developers.facebook.com/documentation/meta-business-agent/overview) pour les informations les plus récentes.

## Qu'est-ce que Meta Business Agent ? {#what-is-meta-business-agent}

Meta Business Agent est un répondeur alimenté par l'IA que Meta exploite directement sur un numéro de téléphone WhatsApp Business. Lorsqu'il est activé pour un numéro éligible, il peut répondre aux messages entrants des utilisateurs au nom de l'entreprise, en s'appuyant sur des connaissances (informations sur l'entreprise, FAQ, fichiers, contenu du site web) et des connecteurs configurés dans les outils de Meta.

L'activation de Meta Business Agent se fait entièrement dans WhatsApp Manager et Meta Business Suite, indépendamment de votre espace de travail Braze. Braze n'est pas nécessaire pour la configuration, et il n'existe actuellement aucun contrôle dans le tableau de bord de Braze pour cela.

## Comment il interagit avec votre numéro connecté à Braze {#how-it-interacts-with-your-braze-connected-number}

Meta Business Agent et Braze peuvent coexister sur le même numéro de téléphone WhatsApp Business, mais ne partagent pas aujourd'hui la visibilité sur chaque message.

- **Les messages sortants initiés par Braze ne sont pas affectés.** Braze continue d'envoyer des messages modèles WhatsApp et des messages de réponse via les Campaigns et les Canvas exactement comme aujourd'hui, que Meta Business Agent soit activé ou non.
- **Les messages entrants sont routés par Meta Business Agent.** Pour chaque message entrant d'un utilisateur, Meta Business Agent décide s'il le transmet à Braze ou s'il le traite lui-même.
  - **Si Meta route le message vers Braze :** il est traité de la même manière que tout message WhatsApp entrant aujourd'hui. Les déclencheurs basés sur les actions des Campaigns et Canvas existants ainsi que les parcours d'action se déclenchent selon la logique que vous avez déjà mise en place.
  - **Si Meta Business Agent traite le message lui-même :** Braze ne traite pas actuellement le canal séparé (messages en attente et échos de messages) qui porterait cette activité. Les messages entrants que l'agent décide de traiter, ainsi que ses propres réponses à ces messages, ne sont actuellement visibles dans aucune interface de Braze.

| Flux de messages | Ce qui se passe aujourd'hui |
| --- | --- |
| Messages modèles WhatsApp et messages de réponse envoyés via des Campaigns ou des étapes Canvas | Non affecté ; Braze continue d'envoyer selon la configuration |
| Message entrant que Meta route vers Braze | Traité normalement ; les déclencheurs et parcours d'action existants s'appliquent |
| Message entrant que Meta Business Agent traite lui-même | Non visible actuellement par Braze ; les déclencheurs et parcours d'action existants pour les messages entrants ne se déclenchent pas |
| Message sortant envoyé par Meta Business Agent | Non visible actuellement par Braze |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Flux de messages" }

## Activer Meta Business Agent {#enable-meta-business-agent}

Meta Business Agent s'active par numéro de téléphone dans les outils de Meta, pas dans Braze :

1. Vérifiez l'éligibilité et activez-le pour un numéro de téléphone dans [WhatsApp Manager](https://business.facebook.com/wa/manage/home/), en acceptant les conditions d'utilisation de Meta Business Agent.
2. Configurez les connaissances et les compétences de l'agent (informations sur l'entreprise, FAQ, fichiers, connecteurs) via les [API de configuration de l'agent](https://developers.facebook.com/documentation/meta-business-agent/reference/configure/agent-skills) de Meta.
3. Activez l'agent via les [paramètres de l'agent](https://developers.facebook.com/documentation/meta-business-agent/reference/onboard/agent-settings).

## Points à considérer avant l'activation {#things-to-weigh-before-enabling-it}

- **Pas de contrôle côté Braze :** l'activation, la configuration et la désactivation de Meta Business Agent se font entièrement dans les outils de Meta ; il n'y a rien à activer ou désactiver dans Braze.
- **Facturation :** avec l'introduction de Meta Business Agent, les messages non modélisés sont désormais classés dans l'une des deux catégories suivantes : Service (catégorie existante) ou Meta Business Agent (nouvelle catégorie).
  - Les réponses non modélisées traitées par Braze sont facturées en tant que messages de service à partir du 1er octobre 2026.
    - Si vous répondez à un message entrant avec un modèle marketing, utilitaire ou d'authentification, il est facturé en tant que tel.
  - Les messages Meta Business Agent sont facturés directement par Meta à partir du 1er août 2026. Consultez leur tarification pour plus de détails.
  - Les messages sont classés dans une seule catégorie, vous n'êtes donc jamais facturé deux fois pour le même message.