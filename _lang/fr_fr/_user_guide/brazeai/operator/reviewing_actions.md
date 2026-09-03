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

Lorsqu'Operator propose des modifications dans le tableau de bord (comme remplir des champs de formulaire, mettre à jour des paramètres ou générer des images), il présente chaque modification sous forme de carte d'action à examiner.

1. **Operator résume le plan :** Operator explique ce qu'il prévoit de faire avant d'afficher les cartes d'action.
2. **Les cartes d'action individuelles apparaissent :** Chaque modification proposée est présentée sous forme de carte distincte indiquant ce qu'Operator souhaite modifier ou effectuer dans le tableau de bord. Pour les modifications de valeurs existantes, la valeur précédente et la valeur proposée sont affichées côte à côte pour comparaison.
3. **Examiner et approuver :** Examinez chaque carte et approuvez-la ou refusez-la.
4. **L'action s'exécute :** Les actions approuvées sont exécutées dans Braze. Les actions refusées ne sont pas appliquées.

Si une action échoue après approbation, Operator vous en informe avec des détails sur l'échec.

### Disponibilité {#availability}

Operator peut proposer des cartes d'action sur les pages prises en charge du tableau de bord, y compris les éditeurs de messages, les pages de listes et d'aperçu, les paramètres et d'autres surfaces sur lesquelles il peut agir. Pour une couverture représentative, consultez [Ce que vous pouvez faire avec Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities). Pour les canaux de messages et éditeurs pris en charge, consultez [Générer des messages]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages).

La couverture s'étend régulièrement. Si Operator ne peut pas agir sur la page où vous vous trouvez, il fournit une liste d'étapes à suivre dans l'interface utilisateur.

## Modifier un plan {#modify-a-plan}

Pour modifier le plan d'Operator, approuvez ou rejetez d'abord les actions en attente. Décrivez ensuite le changement souhaité dans un nouveau message de chat.

Les actions approuvées ne peuvent pas être annulées via Operator. Décrivez le nouveau changement à Operator ou effectuez les modifications manuellement dans le tableau de bord.

## Actions à approbation automatique {#auto-approve-actions}

Le bouton **Actions à approbation automatique** se trouve dans le panneau de chat d'Operator.

- **Activé :** les actions suggérées par Operator s'exécutent immédiatement sans nécessiter d'approbation manuelle, y compris la [navigation vers une autre page]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard) pour répondre à votre demande. Certaines actions nécessitent toujours une approbation explicite pour des raisons de sécurité, comme la génération d'images ou la modification de paramètres au niveau de l'espace de travail.
- **Désactivé (par défaut) :** toutes les actions proposées suivent le processus de vérification manuelle décrit, y compris la navigation entre les pages. Operator propose le déplacement et attend votre approbation avant de vous y conduire.

![Le bouton d'approbation automatique et la fenêtre modale de confirmation dans le panneau de chat d'Operator.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

L'approbation automatique se réinitialise lorsque vous actualisez la page, ouvrez un nouvel onglet, ou vous déconnectez puis vous reconnectez. Naviguer entre les pages du tableau de bord ne la réinitialise pas. L'approbation automatique peut être désactivée à tout moment.

Pour en savoir plus sur la restriction de l'accès à Operator et l'audit de l'utilisation par l'équipe, consultez [Confidentialité des données et sécurité]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security).