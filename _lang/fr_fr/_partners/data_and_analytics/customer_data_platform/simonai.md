---
nav_title: Simon AI
article_title: Simon AI
description: "Utilisez l'intégration de Braze et Simon AI pour créer et synchroniser des audiences sophistiquées vers Braze pour l'orchestration, en temps réel et sans code."
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Simon AI

> La plateforme de marketing agentique [Simon AI][1] aide les équipes marketing à atteindre une véritable personnalisation individuelle. Elle combine un CDP composable avec des agents d'intelligence artificielle qui opèrent directement dans le Snowflake AI Data Cloud pour agir en tant qu'équipe de données et d'exécution du marketeur.

Utilisez l'intégration de Braze et Simon AI pour créer et synchroniser des audiences avancées vers Braze pour une orchestration en temps réel et sans code. Grâce à cette intégration, vous pouvez tirer parti de la résolution d'identité, de l'unification des données client et de la segmentation pilotée par l'IA de Simon AI pour alimenter des campagnes Braze plus personnalisées et plus percutantes en aval.

## Conditions préalables {#prerequisites}

Pour commencer, vous devez authentifier votre compte Braze dans votre compte Simon AI.

| Condition | Description |
| --------- | ----------- |
| Simon AI | Vous devez disposer d'un compte Simon AI existant pour exploiter l'intégration Braze depuis Simon AI. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track`, `campaigns.trigger.schedule.create` et `campaigns.trigger.send`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| URL du tableau de bord de Braze | [L'URL de votre endpoint REST][3]. Votre endpoint dépendra de l'URL Braze de votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'usage {#use-cases}

- Déclencher un Canvas ou un e-mail Braze
- Transmettre et maintenir les propriétés de segment
- Synchroniser les traits et les propriétés de contact

{% alert note %}
Lors de l'utilisation de l'intégration Simon et Braze, Simon n'envoie que les deltas à chaque synchronisation vers Braze, évitant ainsi les coûts liés aux données non pertinentes. Consultez [Synchroniser les traits et les propriétés de contact](#sync-traits-and-contact-properties) pour en savoir plus.
{% endalert %}

## Intégration {#integration}

### Authentifier votre compte Braze dans Simon AI {#authenticate-your-braze-account-in-simon-ai}

Pour utiliser l'intégration Braze, authentifiez d'abord votre compte Braze dans Simon :

1. Dans le menu de navigation, cliquez sur **Integrations**, puis faites défiler jusqu'à Braze.
2. Saisissez votre [clé API REST][2] Braze et votre [URL du tableau de bord][3].
3. Cliquez sur **Save Changes**.

Une connexion réussie affiche **Connected** dans la fenêtre.

![Écran d'intégration dans Simon AI][8]{: style="max-width:70%"}

### Ajouter des actions Braze aux Flows ou Journeys dans Simon AI {#add-braze-actions-to-flows-or-journeys-in-simon-ai}

Après avoir authentifié votre compte Braze dans Simon AI, vous pouvez ajouter des actions Braze aux [Flows][4] et aux [Journeys][5].

Trois actions sont disponibles :

- **Sync Simon segment attribute** : synchronisez les détails de votre segment avec un attribut personnalisé nouveau ou existant dans Braze.
- **Trigger a Braze Canvas** : déclenchez un Canvas Braze qui exploite les données de votre segment Simon.
- **Send a Braze campaign** : lancez une campagne Braze complète depuis Simon.

![Liste déroulante affichant les actions Braze disponibles dans Simon AI.][9]{: style="max-width:60%"}

Certaines actions ne sont disponibles que pour des types de Flows spécifiques ou uniquement pour les Journeys. Pour en savoir plus, consultez [docs.simondata.com][6].

### Synchroniser les traits et les propriétés de contact {#sync-traits-and-contact-properties}

Pour minimiser la consommation de données, vous pouvez choisir des traits spécifiques à synchroniser par défaut, plutôt que de mettre à jour chaque champ pour tous les clients d'un segment.

{% alert note %}
Pour commencer avec la synchronisation des traits, soumettez une demande dans le [centre d'assistance Simon](https://docs.simondata.com/docs/support-center). Votre gestionnaire de compte vous informera lorsque vous pourrez procéder aux étapes suivantes.
{% endalert %}

Une fois que les traits de contact ont été activés par votre gestionnaire de compte :

1. Dans Simon, développez **Admin Center** dans la navigation de gauche et sélectionnez **Sync Contact Traits**.
2. Choisissez **Braze**. Les propriétés de contact sont affichées ici, organisées par jeu de données.
3. Sélectionnez les champs que vous souhaitez synchroniser lorsque vous utilisez l'intégration Simon et Braze :
   1. **Number of traits** indique le nombre de traits disponibles dans ce jeu de données. Vous pouvez tous les sélectionner ou développer la ligne pour choisir des champs individuels.
   2. Modifiez le **Downstream name** si vous souhaitez que les noms de champs apparaissent différemment lorsqu'ils arrivent dans Braze.
   3. Si c'est la première fois que vous intégrez Braze depuis Simon, cliquez sur **Backfill all contacts**. Le remplissage envoie tous les points de donnée à Braze la première fois que vous utilisez une action dans un Flow ou un Journey pour vous assurer que toutes vos données sont entièrement synchronisées. Ensuite, lors des synchronisations suivantes, seuls les traits que vous choisissez sur cet écran sont envoyés à Braze. Cela permet de vous assurer que vous n'êtes facturé que pour les données dont vous avez besoin.

![Sélection des traits à synchroniser dans Simon AI.][10]

[1]: https://www.simon.ai/
[2]: {{site.baseurl}}/api/basics#creating-rest-api-keys
[3]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
[4]: https://docs.simondata.com/docs/campaigns-flows
[5]: https://docs.simondata.com/docs/campaigns-journeys-two
[6]: https://docs.simondata.com
[7]: https://docs.simondata.com/docs/support-center
[8]: {% image_buster /assets/img/simon_data/ConnecttoBraze.png %}
[9]: {% image_buster /assets/img/simon_data/BrazeActions.png %}
[10]: {% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %}