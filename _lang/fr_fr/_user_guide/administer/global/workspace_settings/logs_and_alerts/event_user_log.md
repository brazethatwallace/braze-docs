---
nav_title: Journal des événements utilisateurs
article_title: Journal des événements utilisateur
page_order: 1
page_type: reference
description: "Cet article de référence couvre le journal des événements utilisateurs, qui peut vous aider à déboguer ou résoudre les problèmes liés à votre intégration Braze."

---

# Journal des événements utilisateur

> Le journal des événements utilisateur peut vous aider à analyser, déboguer ou résoudre les problèmes liés à votre intégration Braze. Cet onglet vous fournit un journal des erreurs qui détaille le type d'erreur, l'application à laquelle elle est associée, le moment où elle s'est produite, et offre souvent la possibilité de consulter les données brutes associées.

{% alert tip %}
En complément de cet article, nous vous recommandons également de consulter notre cours d'apprentissage Braze Learning [Outils d'assurance qualité et de débogage](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), qui explique comment utiliser le journal des événements utilisateurs pour effectuer vos propres opérations de résolution des problèmes et de débogage.
{% endalert %}

Pour accéder au journal, allez dans **Paramètres** > **Journal des événements utilisateur**.

Pour trouver facilement vos journaux, vous pouvez filtrer en fonction de :

* SDK ou API
* Noms d'applications
* Période
* Utilisateur

Chaque journal est divisé en plusieurs sections, qui peuvent inclure :

* Attributs de l'appareil
* Attributs utilisateur
* Événements
* Événements de Campaign
* Données de réponse

Sélectionnez l'icône **Développer les données** pour afficher les données JSON brutes de ce journal spécifique.

![L'icône « Développer les données » à côté d'un journal spécifique.]({% image_buster /assets/img_archive/expand_data.png %})

Les journaux des événements utilisateurs restent disponibles dans le tableau de bord pendant 30 jours après leur enregistrement.

![Journaux bruts pour les événements]({% image_buster /assets/img_archive/rawlogs.png %}){: style="max-width:60%;"}

## Résolution des problèmes

### Journaux SDK manquants pour les utilisateurs test

Si vous avez ajouté un utilisateur à un groupe interne, mais qu'il n'affiche aucun journal SDK dans le journal des événements utilisateurs, cela peut être dû à une option de configuration manquante. Pour capturer les journaux SDK, assurez-vous de sélectionner **Enregistrer les événements utilisateur pour les membres du groupe** dans les **Paramètres du groupe interne** pour ce [groupe interne]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/).

### Délai dans la mise à jour des journaux

Il s'agit potentiellement d'une lenteur normale de notre API.

Lorsque vous appelez des méthodes du SDK, celui-ci met généralement ces événements en cache localement et les envoie au serveur toutes les 10 secondes. L'ingestion des événements par notre file d'attente de traitement peut prendre de quelques secondes à quelques minutes, selon la charge globale à ce moment-là.

Si vous souhaitez que les événements arrivent le plus rapidement possible, essayez d'appeler la fonction `requestImmediateDataFlush()`.

### Échecs d'impression des messages in-app

Si un message in-app ne s'affiche pas, vous pouvez trouver la raison dans le journal des événements utilisateurs en développant les données JSON brutes de la requête SDK concernée et en recherchant le champ `error_code` dans la réponse. Le `error_code` identifie la raison spécifique de l'échec de l'impression (par exemple, une valeur de couleur invalide ou un problème de rendu). Partagez ce code d'erreur avec l'[assistance Braze]({{site.baseurl}}/braze_support/) si une investigation plus approfondie est nécessaire.

### La fin de session et le début de session ont des horodatages similaires (iOS)

Le journal des événements utilisateurs affiche l'horodatage du moment où Braze a été notifié de la fin de la session, ce qui sera quelques millisecondes avant le début de la session suivante. Braze ne peut pas savoir que la session s'est terminée avant que l'application ne soit rouverte, car iOS interrompt de manière agressive l'exécution des threads lorsque l'application est en arrière-plan — aucune donnée ne peut donc être envoyée à Braze tant que l'application n'est pas rouverte.

Bien que l'heure de fin de session soit indiquée comme étant quelques secondes avant le début de la session, lorsque l'événement est envoyé, la durée de session est transmise séparément et est correcte — reflétant le temps pendant lequel l'application était ouverte. Par conséquent, ce comportement n'a pas d'impact sur le filtre `Median Session Duration`.

En ce qui concerne les sessions utilisateur, vous pouvez utiliser Braze pour surveiller des données telles que :

- Le nombre de sessions d'un utilisateur
- La dernière fois qu'un utilisateur a démarré une session
- Si l'utilisateur démarre une session après avoir reçu une campagne
- La durée médiane des sessions de l'utilisateur

Ces comportements ne sont pas impactés par l'envoi de l'événement de fin de session lors de la session suivante.