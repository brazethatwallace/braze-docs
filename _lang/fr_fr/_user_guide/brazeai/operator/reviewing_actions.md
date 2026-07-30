---
nav_title: Vérifier les actions
article_title: Examen des actions de BrazeAI Operator<sup>TM</sup>
page_order: 2
description: "Découvrez comment examiner et approuver les actions lorsque BrazeAI Operator propose des modifications dans le tableau de bord."
---

# Examen des actions de BrazeAI Operator {#reviewing-brazeai-operator-actions}

> Découvrez comment examiner et approuver les actions lorsque BrazeAI Operator<sup>TM</sup> propose des modifications dans le tableau de bord.

![Operator présente les cartes d'action suggérées pour examen.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## Fonctionnement des cartes d'action {#how-action-cards-work}

Lorsqu'Operator propose des modifications dans le tableau de bord (telles que remplir des champs de formulaire, mettre à jour des paramètres ou générer des images), il présente chaque modification sous forme de carte d'action à examiner.

1. **Operator résume le plan :** Operator explique ce qu'il prévoit de faire avant d'afficher les cartes d'action.
2. **Les cartes d'action individuelles apparaissent :** Chaque modification proposée est présentée sous forme de carte distincte qui indique ce qu'Operator souhaite modifier ou effectuer dans le tableau de bord. Pour les modifications apportées à des valeurs existantes, la valeur précédente et la valeur proposée sont affichées côte à côte pour comparaison.
3. **Examinez et approuvez :** Passez en revue chaque carte, puis approuvez-la ou refusez-la.
4. **L'action est exécutée :** Les actions approuvées sont exécutées dans Braze. Les actions refusées ne sont pas appliquées.

Si une action échoue après approbation, Operator vous en informe avec les détails de l'échec.

### Disponibilité {#availability}

Les cartes d'action sont prises en charge pour le contenu des messages dans les mêmes canaux et éditeurs où Operator peut générer des messages, ainsi que sur la page [Créer un agent personnalisé]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents). Pour connaître les canaux et éditeurs pris en charge, consultez [Générer des messages]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages).

Sur les autres pages, Operator fournit une liste d'étapes à suivre dans l'interface utilisateur au lieu d'agir lui-même. Les fonctionnalités d'Operator sont régulièrement améliorées, et une couverture élargie des outils de création est prévue.

## Modifier un plan {#modify-a-plan}

Pour modifier le plan d'Operator, commencez par approuver ou rejeter les actions en attente. Décrivez ensuite le changement souhaité dans un nouveau message.

Les actions approuvées ne peuvent pas être annulées via Operator. Décrivez la nouvelle modification à Operator ou effectuez les changements manuellement dans le tableau de bord.

## Approbation automatique des actions {#auto-approve-actions}

Le bouton **Approbation automatique des actions** se trouve dans le panneau de discussion d'Operator.

- **Activé :** Les actions suggérées par Operator sont exécutées immédiatement sans nécessiter d'approbation manuelle. Certaines actions nécessitent toujours une approbation explicite pour des raisons de sécurité, comme la génération d'images ou la modification de paramètres au niveau de l'espace de travail.
- **Désactivé (par défaut) :** Toutes les actions proposées suivent le processus de vérification manuelle décrit ci-dessus.

![Le bouton d'approbation automatique et la boîte de dialogue modale de confirmation dans le panneau de discussion d'Operator.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

L'approbation automatique se réinitialise lorsque vous actualisez la page, ouvrez un nouvel onglet ou vous déconnectez puis vous reconnectez. Naviguer entre les pages du tableau de bord ne la réinitialise pas. L'approbation automatique peut être désactivée à tout moment.

Pour en savoir plus sur la restriction de l'accès à Operator et l'audit de l'utilisation par votre équipe, consultez [Confidentialité des données et sécurité]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security).