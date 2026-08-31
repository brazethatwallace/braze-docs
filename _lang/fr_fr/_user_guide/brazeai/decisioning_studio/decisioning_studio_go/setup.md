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

Confirmez que vous disposez des éléments suivants :

- Un [segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) pour votre audience d'entrée qui n'est pas activement utilisé dans un autre Canvas ou une autre Campaign
- Au moins un modèle d'e-mail
- Le contenu des variantes que vous souhaitez tester, comme des lignes d'objet alternatives, des CTA et des images principales. Vous pouvez créer des variantes lors de la configuration, mais les avoir prêtes accélère le processus
- Un accès à l'espace de travail avec les autorisations nécessaires pour configurer des agents IA Decisioning

Si votre espace de travail n'a pas été provisionné pour Decisioning Studio Go, vous ne verrez pas l'option de configuration de l'agent dans l'onglet **AI Decisioning**. Contactez votre gestionnaire du succès des clients pour obtenir l'accès.

## Étape 1 : Configurer votre agent {#step-1-set-up-your-agent}

1. Dans le tableau de bord de Braze, accédez à l'onglet **AI Decisioning**.
2. Sélectionnez **Create Agent**.
3. Donnez à votre agent un nom qui le distingue des autres agents de votre espace de travail. Par exemple, préférez « Membres fidélité — Engagement hebdomadaire » plutôt que « Agent e-mail ».
4. (Facultatif) Ajoutez une description pour fournir un contexte dont vous ou un collègue pourriez avoir besoin ultérieurement. Celle-ci peut inclure l'objectif de l'agent, le Segment qu'il cible et ce qui définit le succès.


L'agent optimise le contenu créatif de vos e-mails afin de maximiser l'engagement réel, mesuré par l'activité de clics significatifs par utilisateur. Les clics passent par plusieurs filtres de validation indépendants qui éliminent l'activité automatisée et les clics liés aux désinscriptions, de sorte que le signal reflète un véritable intérêt client plutôt qu'un simple volume de clics brut.

## Étape 2 : Sélectionner l'audience cible {#step-2-select-the-target-audience}

Sélectionnez le Segment Braze auquel votre agent envoie des messages. Les utilisateurs de ce Segment sont automatiquement répartis en deux groupes :

- **Groupe Decisioning Studio :** Reçoit le contenu d'e-mail optimisé par l'IA. L'agent choisit la meilleure combinaison de variantes pour chaque utilisateur.
- **Groupe de contrôle aléatoire :** Minimum 5 % du Segment. Reçoit des combinaisons sélectionnées aléatoirement des mêmes options, à des jours choisis aléatoirement. Ce groupe est obligatoire.

![Un Segment sélectionné avec 1 100 utilisateurs estimés.]({% image_buster /assets/img/decisioning_studio_go/audience_details.png %})

### Pourquoi un Segment dédié est important {#why-a-dedicated-segment-matters}

Si les utilisateurs de votre Segment sélectionné reçoivent également des messages provenant d'autres Canvas ou Campaigns, l'engagement observé par l'agent est affecté par ces autres messages. L'agent ne peut pas déterminer si un utilisateur a cliqué en raison de ses décisions ou à cause d'autre chose. Un avertissement s'affiche si votre Segment sélectionné est utilisé ailleurs ; vous pouvez poursuivre, mais attendez-vous à des résultats plus bruités.

### Recherche d'utilisateur {#user-lookup}

Utilisez **User Lookup** pour vérifier si des utilisateurs spécifiques répondent à vos critères de Segment. Cette fonctionnalité est utile pour valider la définition de votre Segment.

### Filtres d'audience {#audience-filters}

Les filtres d'audience ne sont pas pris en charge dans cette version. Si vous avez besoin de critères de ciblage supplémentaires, [créez un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) en appliquant ces filtres, puis sélectionnez ce Segment comme audience d'entrée.

### Intégrer avec des Canvas existants {#integrate-with-existing-canvases}

Pour utiliser Decisioning Studio Go au sein d'un parcours plus large :

1. Créez un Segment dédié pour les utilisateurs qui doivent être inclus dans l'agent.
2. Dans votre [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas), utilisez une étape de mise à jour utilisateur pour ajouter l'utilisateur à ce Segment au bon moment du parcours.
3. Confirmez que les utilisateurs sortent du Canvas afin que l'agent (et non le Canvas) gère l'envoi d'e-mails pour tous les utilisateurs du Segment à partir de ce point.

## Étape 3 : Configurer la planification {#step-3-configure-the-schedule}

Déterminez quand l'agent est autorisé à envoyer des messages.

### Étape 3.1 : Déterminer la fréquence d'envoi {#step-31-determine-the-send-frequency}

Sélectionnez la fréquence à laquelle les utilisateurs reçoivent des e-mails de cet agent, par exemple trois fois par semaine. Il s'agit d'une sélection unique. L'agent n'optimise pas entre différentes fréquences ; il choisit les jours et les heures en fonction de la fréquence que vous avez définie.

### Étape 3.2 : Sélectionner les jours de la semaine {#step-32-select-the-days-of-the-week}

Choisissez les jours auxquels l'agent peut envoyer des messages. Vous devez sélectionner au moins autant de jours que votre fréquence l'exige (si l'agent envoie trois fois par semaine, sélectionnez au moins trois jours ; sélectionner davantage de jours offre plus de flexibilité à l'agent). L'agent optimise au sein de cet ensemble en choisissant les meilleurs jours pour chaque utilisateur. Pour une flexibilité maximale, sélectionnez les sept jours.

### Étape 3.3 : Définir les heures calmes {#step-33-set-quiet-hours}

Spécifiez les périodes pendant lesquelles l'agent ne doit pas envoyer de messages. Les heures calmes utilisent le fuseau horaire local de l'utilisateur. L'utilisation la plus courante consiste à bloquer les envois tard dans la nuit et très tôt le matin. En dehors des heures calmes, l'agent planifie les envois aux moments les plus susceptibles de générer des clics pour chaque utilisateur.

### Étape 3.4 : Définir les règles de limite de fréquence {#step-34-set-frequency-capping-rules}

Vos règles de limite de fréquence peuvent être appliquées au niveau de l'agent :

- **Appliquer la limite de fréquence :** Empêche l'agent d'envoyer des messages à un utilisateur une fois sa limite de fréquence atteinte. En fonction de la configuration de vos règles, cette limite peut s'appliquer au niveau de l'utilisateur individuel ou au niveau global du compte. Dans les deux cas, les messages ne sont pas envoyés à cet utilisateur tant que la limite est atteinte.
- **Comptabiliser dans la limite :** Choisissez si les envois de cet agent sont comptabilisés dans la limite globale de l'utilisateur.

{% alert tip %}
Si votre limite de fréquence protège l'expérience utilisateur, les envois de l'agent sont déjà ciblés et vous n'avez peut-être pas besoin de les comptabiliser dans la limite. Si votre limite contrôle le volume global d'envois ou les dépenses, vous souhaitez probablement qu'ils soient comptabilisés. Votre gestionnaire du succès des clients ou votre consultant en solutions peut vous aider à déterminer la bonne approche pour votre espace de travail.
{% endalert %}

## Étape 4 : Ajouter du contenu et des modèles {#step-4-add-content-and-templates}

Définissez les éléments avec lesquels l'agent doit travailler :

- **Créations de base :** Les modèles d'e-mail complets. L'agent choisit d'abord quelle création de base envoyer à un utilisateur donné.
- **Composants créatifs :** Les éléments spécifiques au sein d'une création de base — ligne d'objet, CTA et image principale — que l'agent personnalise pour chaque utilisateur.

Vous pouvez créer des créations de base en :

- Utilisant le compositeur d'e-mail standard de Braze.
- Importent un e-mail depuis un Canvas ou une Campaign existante.

Utilisez une seule création de base ou plusieurs. Avec une seule création de base, l'agent personnalise uniquement les composants qu'elle contient. Avec plusieurs créations de base — par exemple, une décontractée, une formelle et une promotionnelle — l'agent choisit également quelle création de base convient le mieux à chaque utilisateur. L'agent peut aussi choisir parmi plusieurs créations de base sans composants créatifs supplémentaires.

### Étape 4.1 : Marquer les points de personnalisation avec des étiquettes Liquid {#step-41-mark-personalization-points-with-liquid-tags}

Pour chaque composant que vous souhaitez que l'agent personnalise, remplacez le contenu statique dans votre création de base par une étiquette Liquid du menu de personnalisation. Fournissez ensuite les options de variantes dans la section **Composants créatifs**.

Les composants pris en charge dans cette version sont :

- **Ligne d'objet :** Remplacez la ligne d'objet dans les **Paramètres d'envoi** par l'étiquette Liquid pour la ligne d'objet.
- **CTA :** Remplacez le texte du bouton dans le corps de l'e-mail par l'étiquette Liquid pour le CTA.
- **Image :** Remplacez l'URL de l'image principale par l'étiquette Liquid pour l'image.

{% alert note %}
Les [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) ne sont pas pris en charge comme points de substitution pour les composants personnalisés. Placez votre ligne d'objet personnalisée, votre CTA et votre image directement dans le corps de l'e-mail plutôt qu'à l'intérieur d'un bloc de contenu.
{% endalert %}

### Étape 4.2 : Ajouter des variantes {#step-42-add-variants}

Dans la section **Composants créatifs**, ajoutez les options de variantes pour chaque point de personnalisation :

- Plusieurs options de ligne d'objet
- Plusieurs options de texte CTA
- Plusieurs URL d'images

Chaque variante peut être associée à des créations de base spécifiques, ou rendue disponible pour toutes les créations de base. Par exemple, si vous avez une création de base promouvant des soldes et une autre promouvant les nouveautés, vous pouvez restreindre votre ligne d'objet `Don't miss our biggest savings of the year` à la création soldes uniquement, tout en rendant votre CTA `Just dropped` disponible pour les deux.

Les images doivent être sélectionnées depuis la bibliothèque multimédia de Braze. Si vous souhaitez utiliser une image, commencez par la télécharger dans la bibliothèque multimédia.

### Étape 4.3 : Prévisualiser et tester {#step-43-preview-and-test}

Au fur et à mesure que vous ajoutez du contenu, prévisualisez et testez votre message à l'aide de l'aperçu dynamique qui montre le rendu des différentes combinaisons de variantes. Cela est utile pour repérer et résoudre les problèmes de rendu avant le lancement. Une fois vos créations de base et vos variantes configurées, vous pouvez consulter la liste complète de toutes les combinaisons que l'agent est autorisé à envoyer.

Vous pouvez également envoyer un message test à vous-même ou à un coéquipier. Les envois tests affichent la combinaison de variantes spécifique que vous sélectionnez, et non ce que l'agent choisirait pour un utilisateur particulier.

## Étape 5 : Définir les contraintes {#step-5-define-constraints}

Les contraintes empêchent l'agent d'envoyer du contenu répétitif au même utilisateur. Les niveaux suivants sont disponibles :

- **Niveau de base créative :** Empêche l'envoi d'une même base créative à un utilisateur plus d'une fois dans une fenêtre que vous définissez. Utile lorsque chaque base créative est suffisamment distincte pour qu'une répétition dans, par exemple, une semaine paraisse redondante.
- **Niveau de ligne d'objet :** Empêche l'envoi d'une même ligne d'objet à un utilisateur plus d'une fois dans une fenêtre que vous définissez. Utile lorsque les lignes d'objet constituent le signal de répétition le plus visible.

Les contraintes au niveau des variantes sur des images ou des CTA spécifiques ne sont pas prises en charge dans cette version.

## Étape 6 : Réviser et lancer {#step-6-review-and-launch}

L'écran **Révision** affiche l'intégralité de votre configuration : audience et répartition du groupe de contrôle aléatoire, planification, créations de base, nombre de variantes et contraintes actives. Passez en revue et résolvez les avertissements de validation (par exemple, chevauchement de Segment avec une autre Campaign) qui s'affichent dans cette section.

Sélectionnez **Lancer** pour activer l'agent. Il passe du statut **Brouillon** à **Actif** et commence l'envoi le prochain jour éligible.

## Après le lancement {#after-launch}

### Période d'apprentissage {#training-period}

Lorsque votre agent est lancé, il entre dans une période d'apprentissage. Un indicateur d'apprentissage s'affiche dans l'interface de reporting. Les performances peuvent fluctuer au cours des premiers jours, pendant que l'agent explore les combinaisons. Les e-mails continuent d'être envoyés pendant qu'il apprend. Il n'y a pas de délai d'attente.

Des changements significatifs dans les performances apparaissent après que l'agent a terminé son apprentissage et entre dans la phase de personnalisation active. Le reporting indique quand cette transition se produit, afin que vous sachiez toujours à quelle étape se trouve votre agent.

### Vues de reporting {#reporting-views}

L'interface de reporting propose trois vues principales :

| Vue | Description |
|---|---|
| **Performance** | Taux de clics, indicateurs d'engagement et gain du groupe Decisioning Studio par rapport au groupe de contrôle aléatoire. |
| **Configuration** | Les paramètres actuels de l'agent, utiles pour confirmer ce qui est en cours d'exécution. |
| **Préférences de l'agent** | Le nombre de fois où chaque variante a été choisie par l'agent, montrant vers quoi l'agent tend pour votre audience. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vues de reporting" }

Les analyses au niveau des éléments montrent comment les lignes d'objet, les CTA et les images individuels performent à travers toutes les combinaisons.

### Modifier un agent actif {#edit-an-active-agent}

Accédez à la vue **Configuration** pour modifier l'audience, la planification, les créations ou les contraintes après le lancement. La vue Configuration affiche un résumé des modifications. Validez les modifications avant qu'elles ne prennent effet. L'ajout de nouvelles variantes ne réinitialise pas l'apprentissage de l'agent sur les variantes existantes ; cela ajoute simplement de nouvelles options au répertoire de l'agent.

### Mettre en pause ou arrêter {#pause-or-stop}

Le cycle de vie d'un agent est **Brouillon** > **Actif** > **Arrêté**. Sélectionnez **Arrêter** à tout moment pour interrompre un agent ; il cesse d'envoyer et reprend lorsque vous le réactivez.

## Référence {#reference}

Le tableau suivant résume les domaines de Decisioning Studio Go et les détails associés.

| Domaine | Détails |
|---|---|
| **Canal** | E-mail uniquement |
| **Indicateur de conversion** | Clics uniquement (clics uniques quotidiens par utilisateur) |
| **Points de personnalisation** | Ligne d'objet, CTA, image principale (par création de base) |
| **Audience** | Un Segment Braze, avec un groupe de contrôle aléatoire obligatoire (minimum 5 %) |
| **Fréquence** | Sélection unique (pas de décision de fréquence) |
| **Envois de test** | Via le compositeur Braze |
| **Rapports** | Vues Performance, Configuration et Préférences de l'agent, ainsi que les répartitions au niveau des éléments |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Périmètre de Decisioning Studio Go" }

### Considérations {#considerations}

- Les Content Blocks ne sont pas pris en charge comme points de substitution de personnalisation.
- Les URL des images doivent être ajoutées manuellement. Actuellement, l'intégration avec la bibliothèque multimédia n'est pas prise en charge.
- Les filtres d'audience ne sont pas pris en charge au-delà de la sélection de Segment.
- La personnalisation du corps du texte, de l'accroche et de l'en-tête n'est pas encore disponible.

## Résolution des problèmes {#troubleshooting}

Contactez votre gestionnaire du succès des clients ou votre consultant en solutions pour obtenir de l'aide sur la configuration des agents, l'examen des performances ou la conception de programmes.

Pour les questions fréquentes, consultez la [FAQ de Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq).