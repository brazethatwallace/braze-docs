{% if include.section == "Differing audience size" %}

La taille de la population cible affichée dans une campagne ou un Canvas peut différer de la [taille de l'audience atteignable pour un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/#segment-membership-calculation), même si vous ajoutez directement ce segment dans votre campagne ou votre Canvas sans filtre supplémentaire.
Cela peut se produire pour plusieurs raisons :

- Lorsqu'un Groupe de contrôle global s'applique à une campagne ou à un Canvas, les utilisateurs de ce Groupe de contrôle global sont exclus du décompte des utilisateurs pouvant être atteints.
- La taille de la population cible d'une campagne ou d'un Canvas exclut les utilisateurs qui ne sont pas joignables via les différents canaux de messages ; le comportement diffère d'un canal à l'autre. Par exemple, l'audience atteignable pour une campagne ou un Canvas exclut les utilisateurs qui sont désabonnés, marqués comme spam (pour les e-mails) ou qui ont fait l'objet d'un échec d'envoi définitif (pour les e-mails). Le segment lui-même, en revanche, n'exclut que les désinscriptions lorsqu'il affiche le nombre estimé d'utilisateurs atteignables par e-mail.
- Braze n'envoie des messages SMS qu'aux utilisateurs faisant partie du groupe d'abonnement sélectionné. Par conséquent, la population cible SMS d'une campagne ou d'un Canvas exclura également tous les utilisateurs qui ne font pas partie du groupe d'abonnement sélectionné.

{% endif %}

{% if include.section == "Refresh settings" %}

Si vous n'avez pas besoin que votre extension soit actualisée à intervalles réguliers, vous pouvez l'enregistrer sans utiliser les paramètres d'actualisation, et Braze générera par défaut votre extension de segments en fonction de l'appartenance des utilisateurs à ce moment-là. Utilisez le comportement par défaut si vous souhaitez générer l'audience une seule fois, puis la cibler avec une campagne ponctuelle.

Votre segment commencera toujours à être traité après l'enregistrement initial. À chaque actualisation de votre segment, Braze réexécute le segment et met à jour l'appartenance au segment pour refléter les utilisateurs présents dans votre segment au moment de l'actualisation. Cela peut aider vos campagnes récurrentes à atteindre les utilisateurs les plus pertinents.

#### Mise en place d'une actualisation récurrente {#setting-up-a-recurring-refresh}

Pour établir une planification récurrente en définissant des paramètres d'actualisation, sélectionnez **Activer l'actualisation**. L'option de définition des paramètres d'actualisation est disponible pour tous les types d'extensions de segments, y compris les segments SQL, les extensions de segments CDI et les extensions de segments basées sur des formulaires simples.

{% alert important %}
Pour optimiser la gestion de vos données, les paramètres d'actualisation sont automatiquement désactivés pour les extensions de segments non utilisées. Les extensions de segments sont considérées comme non utilisées lorsqu'elles :

- Ne sont utilisées dans aucune campagne, aucun Canvas ni aucun segment actif ou inactif (brouillon, arrêté, archivé) ; ou
- N'ont pas été modifiées depuis plus de 7 jours

Braze informera le contact de la société et le créateur de l'extension si ce paramètre est désactivé. L'option de régénération quotidienne des extensions peut être réactivée à tout moment.
{% endalert %}

#### Sélectionner vos paramètres d'actualisation {#selecting-your-refresh-settings}

![Paramètres d'intervalle d'actualisation avec une fréquence d'actualisation hebdomadaire, une heure de début à 10 h et le lundi sélectionné comme jour.]({% image_buster /assets/img/segment/segment_interval_settings.png %}){: style="max-width:50%;"}

Dans le panneau **Paramètres d'intervalle d'actualisation**, vous pouvez sélectionner la fréquence à laquelle cette extension de segments sera actualisée : toutes les heures, tous les jours, toutes les semaines ou tous les mois. Vous devrez également sélectionner l'heure précise (dans le fuseau horaire de votre société) à laquelle l'actualisation doit avoir lieu, par exemple :

- Si vous avez une campagne d'e-mail envoyée tous les lundis à 11 h, heure de la société, et que vous souhaitez vous assurer que votre segment est actualisé juste avant l'envoi, vous devriez choisir une planification d'actualisation hebdomadaire à 10 h les lundis.
- Si vous souhaitez que votre segment soit actualisé tous les jours, sélectionnez la fréquence d'actualisation quotidienne, puis choisissez l'heure de l'actualisation.

{% alert note %}
La possibilité de définir une planification d'actualisation horaire n'est pas disponible pour les extensions de segments basées sur des formulaires (mais vous pouvez définir des planifications quotidiennes, hebdomadaires ou mensuelles).
{% endalert %}

#### Consommation de crédits et coûts supplémentaires {#credit-consumption-and-additional-costs}

Étant donné que les actualisations réexécutent la requête de votre segment, chaque actualisation pour les segments SQL consommera des crédits de segment SQL, et chaque actualisation pour les extensions de segments CDI entraînera un coût au sein de votre entrepôt de données third-party.

{% alert note %}
L'actualisation des segments peut prendre jusqu'à 60 minutes en raison des temps de traitement des données. Les segments en cours d'actualisation auront un état « En cours de traitement » dans votre liste d'extensions de segments. Cela a plusieurs implications :

- Pour terminer le traitement de votre segment avant une heure précise, choisissez une heure d'actualisation située 60 minutes plus tôt.
- Il ne peut y avoir qu'une seule actualisation à la fois pour une extension de segments donnée. En cas de conflit où une nouvelle actualisation est lancée alors qu'une actualisation existante a déjà commencé à être traitée, Braze annulera la nouvelle demande d'actualisation et poursuivra le traitement en cours.
{% endalert %}

#### Critères de désactivation automatique des extensions périmées {#criteria-to-automatically-disable-stale-extensions}

Les actualisations planifiées sont automatiquement désactivées lorsqu'une extension de segments est périmée. Une extension de segments est périmée si elle répond aux critères suivants :

- Non utilisée dans des campagnes ou des Canvas actifs
- Non utilisée dans un segment faisant partie d'une campagne ou d'un Canvas actif
- Non utilisée dans un segment où le [suivi analytique]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/#segment-analytics-tracking) est activé
- Non modifiée depuis plus de sept jours
- Non ajoutée à une campagne, un Canvas (y compris les brouillons) ou un segment depuis plus de sept jours

Si l'actualisation planifiée est désactivée pour une extension de segments, une notification l'indique pour cette extension.

![Une notification indiquant « Les actualisations planifiées ont été désactivées pour cette extension car elle n'est utilisée dans aucune campagne, aucun Canvas ni aucun segment actif. L'extension de segments a été désactivée le 23 février 2025 à 0 h 00. »]({% image_buster /assets/img/segment/segment_extension_disabled.png %})

Lorsque vous êtes prêt à utiliser une extension de segments périmée, passez en revue les paramètres d'actualisation, sélectionnez la planification d'actualisation qui correspond à votre cas d'utilisation, puis enregistrez les modifications.

{% endif %}

{% if include.section == "same channel identifier" %}

Lorsqu'un message est reçu, ouvert ou cliqué, Braze met à jour les données de tous les profils partageant le même identifiant de canal que le profil ayant enregistré l'interaction (par exemple, la même adresse e-mail pour les e-mails, ou le même numéro de téléphone pour les SMS ou WhatsApp). Les utilisateurs qui partagent un identifiant avec une personne ayant reçu, ouvert ou cliqué le message peuvent correspondre à ce filtre même s'ils ne faisaient pas partie de la campagne à l'origine ou n'ont pas reçu le message directement.

{% endif %}