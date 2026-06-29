---
nav_title: Principes généraux
article_title: Principes généraux relatifs aux données pour Decisioning Studio
page_order: 1
page_type: reference
description: "Cet article de référence présente les principes généraux relatifs aux données qui s'appliquent à toutes les ressources de données utilisées par BrazeAI Decisioning Studio."
---

# Principes généraux {#general-principles}

> Des données bien structurées constituent le fondement d'un agent Decisioning Studio efficace. Avant d'examiner les exigences propres à chaque ressource, il est utile de comprendre les quatre principes fondamentaux qui s'appliquent à l'ensemble des données que vous envoyez à Decisioning Studio. Le non-respect de l'un de ces principes figure parmi les causes les plus fréquentes de dégradation des performances du modèle.

## Un identifiant client cohérent dans toutes les ressources {#one-consistent-customer-identifier-across-all-assets}

Chaque ressource de données (profils clients, activations, engagements, conversions) doit faire référence au même identifiant client. Il doit exister exactement un identifiant principal qui identifie de manière unique et cohérente chaque client dans toutes les ressources.

| Exigence | Conséquence en cas de non-respect |
|-------------|------------------------|
| Un identifiant client unique doit être présent dans chaque ressource | Si différentes ressources utilisent des systèmes d'ID différents (par exemple, un ID d'entrepôt de données pour les caractéristiques et un ID de plateforme pour les activations), le moteur de Decisioning Studio ne peut pas les joindre de manière fiable. Cela rompt la boucle de rétroaction et dégrade à la fois l'entraînement du modèle et la précision des rapports. Si le mappage entre les deux systèmes d'ID s'avère être de type plusieurs-à-plusieurs plutôt que un-à-plusieurs, les problèmes d'intégrité des données qui en résultent peuvent être graves. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Un identifiant client cohérent dans toutes les ressources" }

Consultez [Utiliser l'ID externe Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/braze_external_id) pour savoir quel identifiant utiliser.

## Les données d'événements doivent être transmises sous forme de flux incrémental, et non sous forme de snapshot {#event-data-must-be-passed-as-an-incremental-stream-not-as-a-snapshot}

Les événements, tels que les conversions, les engagements et les activations, représentent des actions discrètes survenues à un moment précis. Ils doivent être transmis à Decisioning Studio sous forme de flux incrémental (en ajout uniquement) d'enregistrements individuels, et non sous forme de snapshot agrégé.

| Exigence | Conséquence en cas de non-respect |
|-------------|------------------------|
| Les données d'événements doivent être structurées sous forme d'enregistrements individuels horodatés et transmises de manière incrémentale | Lorsque les données d'événements sont agrégées dans un snapshot (par exemple, en stockant un attribut « heure du dernier envoi » plutôt que des enregistrements d'envoi individuels), vous perdez le timing précis de chaque événement. Il devient alors impossible d'attribuer correctement les résultats à des décisions spécifiques, ce qui rompt la boucle de rétroaction dont le modèle a besoin pour apprendre. Sans horodatages précis des événements, vous ne pouvez pas savoir exactement quand une conversion a eu lieu ni quelle recommandation l'a déclenchée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Les données d'événements doivent être transmises sous forme de flux incrémental, et non sous forme de snapshot" }

Consultez [Snapshots et flux d'événements]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams) pour une explication complète de la distinction ainsi que des exemples de schémas corrects et incorrects.

## Les données de snapshot doivent être mises à jour selon un calendrier régulier {#snapshot-data-must-be-updated-on-a-regular-time-driven-schedule}

Les données de snapshot (telles que les profils et caractéristiques des clients) représentent l'état actuel d'un client à un moment donné. Les mises à jour des données de snapshot doivent être pilotées par un calendrier régulier (par exemple, quotidien), et non par des déclencheurs d'événements.

| Exigence | Conséquence en cas de non-respect |
|-------------|------------------------|
| Les snapshots doivent être mis à jour pour tous les clients selon un calendrier régulier, qu'un client ait eu ou non un événement ce jour-là | Si les mises à jour de snapshot ne sont déclenchées que lorsqu'un événement survient, les caractéristiques qui dépendent de l'écoulement du temps (telles que « jours depuis le dernier achat » ou « jours depuis l'inscription ») deviennent obsolètes pour les clients n'ayant pas eu d'événement récent. Le modèle s'entraîne alors sur des valeurs de caractéristiques périmées, ce qui réduit sa capacité à formuler des recommandations précises et opportunes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Les données de snapshot doivent être mises à jour selon un calendrier régulier" }

## Toutes les ressources doivent respecter des exigences minimales de qualité et d'intégrité des données {#all-assets-must-meet-minimum-data-quality-and-integrity-requirements}

Au-delà de la structure, les données elles-mêmes doivent être cohérentes en interne et suffisamment complètes pour être exploitables.

| Exigence | Conséquence en cas de non-respect |
|-------------|------------------------|
| Chaque ressource doit contenir les champs nécessaires pour établir une clé primaire et, le cas échéant, des clés de jointure vers d'autres ressources. Les enregistrements en double doivent être supprimés ou dédupliqués avant l'ingestion. | Les enregistrements en double ou non appariables ajoutent du bruit à l'entraînement du modèle et peuvent entraîner une attribution incorrecte. Les clés manquantes empêchent le moteur de relier les événements tout au long du parcours client, de la recommandation jusqu'à la conversion. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Toutes les ressources doivent respecter des exigences minimales de qualité et d'intégrité des données" }

Pour les données de flux d'événements en particulier, chaque enregistrement doit inclure au minimum :

**Champs requis :**
- Identifiant client
- Horodatage du moment où l'événement s'est produit (et non du moment où l'enregistrement a été créé dans votre système ; ces deux valeurs sont différentes ; consultez [Snapshots et flux d'événements]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams) pour comprendre pourquoi c'est important)
- Horodatage du moment où l'enregistrement a été créé dans votre système (utilisé pour découper de manière fiable les exports incrémentaux)
- Type d'événement
- Champs suffisants pour filtrer les événements spécifiques qui vous intéressent

**Champs recommandés :**
- Métadonnées d'événement supplémentaires permettant un appariement fiable entre les types d'événements (par exemple, relier un événement de conversion à l'activation spécifique qui l'a précédé)