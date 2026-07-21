---
nav_title: Configurer votre agent
article_title: Configurer votre agent Decisioning Studio Go
page_order: 0
page_type: reference
description: "Cet article décrit le flux de configuration de Decisioning Studio Go pour paramétrer l'audience, la planification, les créatifs, les contraintes et lancer votre agent."
toc_headers: h2
---

# Configurer votre agent Decisioning Studio Go {#set-up-your-decisioning-studio-go-agent}

> Cet article décrit comment configurer un agent Decisioning Studio Go à l'aide du flux de configuration en libre-service dans le tableau de bord de Braze.

Pour un aperçu du fonctionnement de Decisioning Studio Go, consultez [BrazeAI Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go). Pour vérifier que votre programme est adapté avant de configurer un agent, consultez [Exemples pour Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples).

## Conditions préalables {#prerequisites}

Vérifiez que vous disposez des éléments suivants :

- Un [segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) pour votre audience d'entrée qui n'est pas activement utilisé dans un autre Canvas ou une autre Campaign
- Au moins un modèle d'e-mail
- Le contenu des variantes que vous souhaitez tester, comme des lignes d'objet alternatives, des CTA et des images principales. Vous pouvez créer des variantes pendant la configuration, mais les avoir prêtes accélère le processus
- Un accès à l'espace de travail avec les autorisations nécessaires pour configurer des agents AI Decisioning

Si votre espace de travail n'a pas été provisionné pour Decisioning Studio Go, vous ne verrez pas l'option de configuration d'agent dans l'onglet **AI Decisioning**. Contactez votre gestionnaire du succès des clients pour obtenir l'accès.

## Étape 1 : Configurer votre agent {#step-1-set-up-your-agent}

1. Dans le tableau de bord de Braze, accédez à l'onglet **AI Decisioning**.
2. Sélectionnez **Create Agent**.
3. Donnez à votre agent un nom qui le distingue des autres dans votre espace de travail. Par exemple, « Membres fidélité — Engagement hebdomadaire » plutôt que « Agent e-mail ».
4. (Facultatif) Ajoutez une description pour fournir un contexte dont vous ou un collègue pourriez avoir besoin ultérieurement. Cela peut inclure l'objectif de l'agent, le segment qu'il cible et ce à quoi ressemble le succès.


L'agent optimise vos créatifs e-mail pour maximiser l'engagement authentique, mesuré par l'activité de clics significatifs par utilisateur. Les clics passent par plusieurs filtres de validation indépendants qui éliminent l'activité automatisée et les clics liés aux désinscriptions, de sorte que le signal reflète un intérêt réel des clients plutôt qu'un volume brut de clics.

## Étape 2 : Sélectionner l'audience cible {#step-2-select-the-target-audience}

Sélectionnez le segment Braze auquel votre agent envoie des messages. Les utilisateurs de ce segment sont automatiquement répartis en deux groupes :

- **Groupe Decisioning Studio :** reçoit du contenu e-mail optimisé par l'IA. L'agent choisit la meilleure combinaison de variantes pour chaque utilisateur.
- **Groupe de contrôle aléatoire :** minimum 5 % du segment. Reçoit des combinaisons sélectionnées aléatoirement des mêmes options, à des jours sélectionnés aléatoirement. Ce groupe est obligatoire.

![Un segment sélectionné avec 1 100 utilisateurs estimés.]({% image_buster /assets/img/decisioning_studio_go/audience_details.png %})

### Pourquoi un segment dédié est important {#why-a-dedicated-segment-matters}

Si les utilisateurs de votre segment sélectionné reçoivent également des messages d'autres Canvas ou Campaigns, l'engagement observé par l'agent est affecté par ces autres messages. L'agent ne peut pas déterminer si un utilisateur a cliqué en raison de ses décisions ou à cause d'autre chose. Un avertissement s'affiche si votre segment sélectionné est utilisé ailleurs ; vous pouvez continuer, mais attendez-vous à des résultats plus bruités.

### Recherche d'utilisateurs {#user-lookup}

Utilisez **User Lookup** pour vérifier si des utilisateurs spécifiques répondent aux critères de votre segment. Cela est utile pour valider la définition de votre segment.

### Filtres d'audience {#audience-filters}

Les filtres d'audience ne sont pas pris en charge dans cette version. Si vous avez besoin de critères de ciblage supplémentaires, [créez un segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) avec ces filtres appliqués, puis sélectionnez ce segment comme audience d'entrée.

### Intégration avec des Canvas existants {#integrate-with-existing-canvases}

Pour utiliser Decisioning Studio Go dans un parcours plus large :

1. Créez un segment dédié pour les utilisateurs qui doivent être dans l'agent.
2. Dans votre [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas), utilisez une étape de mise à jour utilisateur pour ajouter l'utilisateur à ce segment au bon moment du parcours.
3. Confirmez que les utilisateurs quittent le Canvas afin que l'agent (et non le Canvas) gère l'envoi d'e-mails pour tous les utilisateurs du segment à partir de ce point.

## Étape 3 : Configurer la planification {#step-3-configure-the-schedule}

Déterminez quand l'agent est autorisé à envoyer.

### Étape 3.1 : Déterminer la fréquence d'envoi {#step-31-determine-the-send-frequency}

Sélectionnez la fréquence à laquelle les utilisateurs reçoivent des e-mails de cet agent, par exemple trois fois par semaine. Il s'agit d'une sélection unique. L'agent n'optimise pas entre différentes fréquences ; il choisit les jours et les heures dans la fréquence que vous définissez.

### Étape 3.2 : Sélectionner les jours de la semaine {#step-32-select-the-days-of-the-week}

Choisissez les jours où l'agent peut envoyer. Vous devez sélectionner au moins autant de jours que votre fréquence l'exige (si l'agent envoie trois fois par semaine, sélectionnez au moins trois jours ; sélectionner plus de jours donne à l'agent plus de flexibilité). L'agent optimise au sein de cet ensemble, en choisissant les meilleurs jours pour chaque utilisateur. Pour une flexibilité maximale, sélectionnez les sept jours.

### Étape 3.3 : Définir les heures calmes {#step-33-set-quiet-hours}

Spécifiez les périodes pendant lesquelles l'agent ne doit pas envoyer. Les heures calmes utilisent le fuseau horaire local de l'utilisateur. L'utilisation la plus courante est de bloquer les envois tard le soir et très tôt le matin. En dehors des heures calmes, l'agent planifie les envois aux moments les plus susceptibles de générer des clics pour chaque utilisateur.

### Étape 3.4 : Définir les règles de limite de fréquence {#step-34-set-frequency-capping-rules}

Vos règles de limite de fréquence peuvent être appliquées au niveau de l'agent :

- **Appliquer la limite de fréquence :** empêche l'agent d'envoyer à un utilisateur une fois que sa limite de fréquence a été atteinte. Selon la configuration de vos règles, cette limite peut s'appliquer au niveau de l'utilisateur individuel ou au niveau global du compte. Dans les deux cas, les messages ne sont pas envoyés à cet utilisateur tant que la limite est atteinte.
- **Compter dans la limite :** choisissez si les envois de cet agent comptent dans la limite globale de l'utilisateur.

{% alert tip %}
Si votre limite de fréquence protège l'expérience utilisateur, les envois de l'agent sont déjà ciblés et vous n'avez peut-être pas besoin de les compter dans la limite. Si votre limite contrôle le volume global d'envois ou les dépenses, vous souhaiterez probablement qu'ils soient comptés. Votre gestionnaire du succès des clients ou consultant en solutions peut vous aider à confirmer la bonne approche pour votre espace de travail.
{% endalert %}

## Étape 4 : Ajouter du contenu et des modèles {#step-4-add-content-and-templates}

Définissez les éléments avec lesquels l'agent travaille :

- **Créatifs de base :** les modèles d'e-mail complets. L'agent choisit d'abord quel créatif de base envoyer à un utilisateur donné.
- **Composants créatifs :** les éléments spécifiques au sein d'un créatif de base — ligne d'objet, CTA et image principale — que l'agent personnalise par utilisateur.

Vous pouvez créer des créatifs de base en :

- Utilisant le compositeur d'e-mails standard de Braze.
- Important un e-mail depuis un Canvas ou une Campaign existant(e).

Utilisez un seul créatif de base ou plusieurs. Avec un seul créatif de base, l'agent personnalise uniquement les composants qu'il contient. Avec plusieurs créatifs de base — par exemple, un décontracté, un formel et un promotionnel — l'agent choisit également quel créatif de base convient le mieux à chaque utilisateur. L'agent peut aussi choisir parmi plusieurs créatifs de base sans composants créatifs supplémentaires.

### Étape 4.1 : Marquer les points de personnalisation avec des étiquettes Liquid {#step-41-mark-personalization-points-with-liquid-tags}

Pour chaque composant que vous souhaitez que l'agent personnalise, remplacez le contenu statique dans votre créatif de base par une étiquette Liquid du menu de personnalisation. Fournissez ensuite les options de variantes dans la section **Creative Components**.

Les composants pris en charge dans cette version sont :

- **Ligne d'objet :** remplacez la ligne d'objet dans **Sending Settings** par l'étiquette Liquid pour la ligne d'objet.
- **CTA :** remplacez le texte du bouton dans le corps de l'e-mail par l'étiquette Liquid pour le CTA.
- **Image :** remplacez l'URL de l'image principale par l'étiquette Liquid pour l'image.

{% alert note %}
Les [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) ne sont pas pris en charge comme points de substitution pour les composants personnalisés. Placez votre ligne d'objet, votre CTA et votre image personnalisés directement dans le corps de l'e-mail plutôt que dans un Content Block.
{% endalert %}

### Étape 4.2 : Ajouter des variantes {#step-42-add-variants}

Dans la section **Creative Components**, ajoutez les options de variantes pour chaque point de personnalisation :

- Plusieurs options de lignes d'objet
- Plusieurs options de texte CTA
- Plusieurs URL d'images

Chaque variante peut être associée à des créatifs de base spécifiques, ou rendue disponible pour tous les créatifs de base. Par exemple, si vous avez un créatif de base promouvant une vente et un autre promouvant les nouveautés, vous pouvez restreindre votre ligne d'objet `Don't miss our biggest savings of the year` au créatif de vente uniquement, tout en gardant votre CTA `Just dropped` disponible pour les deux.

Les images doivent être sélectionnées depuis la bibliothèque multimédia de Braze. Si vous souhaitez utiliser une image, téléchargez-la d'abord dans la bibliothèque multimédia.

### Étape 4.3 : Prévisualiser et tester {#step-43-preview-and-test}

Au fur et à mesure que vous ajoutez du contenu, prévisualisez et testez votre message à l'aide de l'aperçu dynamique qui montre comment les différentes combinaisons de variantes s'affichent. Cela est utile pour repérer et résoudre les problèmes de rendu avant le lancement. Une fois vos créatifs de base et vos variantes configurés, vous pouvez voir la liste complète de toutes les combinaisons que l'agent est autorisé à envoyer.

Vous pouvez également envoyer un test à vous-même ou à un collègue. Les envois de test affichent la combinaison de variantes spécifique que vous sélectionnez, et non ce que l'agent choisirait pour un utilisateur particulier.

## Étape 5 : Définir les contraintes {#step-5-define-constraints}

Les contraintes empêchent l'agent d'envoyer du contenu répétitif au même utilisateur. Les niveaux suivants sont disponibles :

- **Niveau créatif de base :** empêche l'envoi du même créatif de base à un utilisateur plus d'une fois dans une fenêtre que vous définissez. Utile lorsque chaque créatif de base est suffisamment distinct pour que le répéter dans, par exemple, une semaine semblerait redondant.
- **Niveau ligne d'objet :** empêche l'envoi de la même ligne d'objet à un utilisateur plus d'une fois dans une fenêtre que vous définissez. Utile lorsque les lignes d'objet sont le signal de répétition le plus visible.

Les contraintes au niveau des variantes sur des images ou des CTA spécifiques ne sont pas prises en charge dans cette version.

## Étape 6 : Vérifier et lancer {#step-6-review-and-launch}

L'écran **Review** affiche votre configuration complète : audience et répartition du groupe de contrôle aléatoire, planification, créatifs de base, nombre de variantes et contraintes actives. Vérifiez et résolvez tous les avertissements de validation (par exemple, chevauchement de segment avec une autre Campaign) qui s'affichent dans cette section.

Sélectionnez **Launch** pour activer l'agent. Il passe de **Draft** à **Live** et commence à envoyer le prochain jour éligible.

## Après le lancement {#after-launch}

### Période d'apprentissage {#training-period}

Lorsque votre agent est lancé, il entre dans une période d'apprentissage. Un indicateur d'apprentissage s'affiche dans l'interface de reporting. Les performances peuvent fluctuer dans les premiers jours pendant que l'agent explore les combinaisons. Les e-mails continuent d'être envoyés pendant qu'il apprend. Il n'y a pas de période d'attente.

Des changements significatifs de performance apparaissent après que l'agent sort de la phase d'apprentissage et entre dans la personnalisation active. Le reporting indique quand cette transition se produit, afin que vous sachiez toujours à quelle étape se trouve votre agent.

### Vues de reporting {#reporting-views}

L'interface de reporting propose trois vues principales :

| Vue | Description |
|---|---|
| **Performance** | Taux de clics, indicateurs d'engagement et amélioration du groupe Decisioning Studio par rapport au groupe de contrôle aléatoire. |
| **Configuration** | Les paramètres actuels de l'agent — utile pour confirmer ce qui est en cours d'exécution. |
| **Préférences de l'agent** | Nombre de fois où chaque variante a été choisie par l'agent, montrant vers quoi l'agent tend pour votre audience. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vues de reporting" }

Les ventilations au niveau des éléments montrent comment les lignes d'objet, les CTA et les images individuels performent à travers toutes les combinaisons.

### Modifier un agent en cours d'exécution {#edit-a-live-agent}

Accédez à la vue **Configuration** pour modifier l'audience, la planification, les créatifs ou les contraintes après le lancement. La vue Configuration affiche un résumé des modifications. Validez les modifications avant qu'elles ne prennent effet. L'ajout de nouvelles variantes ne réinitialise pas l'apprentissage de l'agent sur les variantes existantes ; cela ajoute de nouvelles options au menu de l'agent.

### Mettre en pause ou arrêter {#pause-or-stop}

Le cycle de vie d'un agent est **Draft** > **Live** > **Stopped**. Sélectionnez **Stop** à tout moment pour arrêter un agent ; il cesse d'envoyer et reprend lorsque vous le réactivez.

## Référence {#reference}

Le tableau suivant résume les domaines de Decisioning Studio Go et les détails associés.

| Domaine | Détails |
|---|---|
| **Canal** | E-mail uniquement |
| **Indicateur de conversion** | Clics uniquement (clics quotidiens uniques par utilisateur) |
| **Points de personnalisation** | Ligne d'objet, CTA, image principale (par créatif de base) |
| **Audience** | Un segment Braze, avec groupe de contrôle aléatoire obligatoire (minimum 5 %) |
| **Fréquence** | Sélection unique (pas de décision sur la fréquence) |
| **Envois de test** | Via le compositeur Braze |
| **Reporting** | Vues Performance, Configuration et Préférences de l'agent, plus ventilations au niveau des éléments |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Périmètre de Decisioning Studio Go" }

### Considérations {#considerations}

- Les Content Blocks ne sont pas pris en charge comme points de substitution pour la personnalisation.
- Les URL d'images doivent être ajoutées manuellement. Actuellement, l'intégration avec la bibliothèque multimédia n'est pas prise en charge.
- Les filtres d'audience ne sont pas pris en charge au-delà de la sélection de segment.
- La personnalisation du corps du texte, de l'accroche et de l'en-tête n'est pas encore disponible.

## Résolution des problèmes {#troubleshooting}

Contactez votre gestionnaire du succès des clients ou consultant en solutions pour obtenir de l'aide sur la configuration de l'agent, l'examen des performances ou la conception du programme.

Pour les questions courantes, consultez la [FAQ de Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq).