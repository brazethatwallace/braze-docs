---
nav_title: Arbre décisionnel
article_title: Arbre décisionnel
alias: /decision_split/
page_order: 7
page_type: reference
description: "Cet article de référence explique comment créer et utiliser des arbres décisionnels dans votre Canvas."
tool: Canvas

---

# Arbre décisionnel {#decision-split}

> Le composant d'arbre décisionnel dans Canvas vous permet d'offrir des expériences personnalisées en temps réel à vos utilisateurs.

![Une étape d'arbre décisionnel intitulée « Push activé ? » pour les utilisateurs dont les notifications push ne sont pas activées et ceux dont elles le sont.]({% image_buster /assets/img/decision-split-1.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

Ce composant peut être utilisé pour créer des branches dans un Canvas selon qu'un utilisateur correspond ou non à une requête.

## Créer un arbre décisionnel {#create-a-decision-split}

Pour créer un arbre décisionnel dans votre workflow, ajoutez une étape à votre Canvas. Ensuite, glissez-déposez le composant depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape et sélectionnez **Decision Split**.

### Définir votre répartition {#define-your-split}

Comment souhaitez-vous répartir vos utilisateurs ? Vous pouvez utiliser des [segments]({{site.baseurl}}/user_guide/audience/segments) et des filtres pour tracer la ligne. Concrètement, vous créez une requête `true` ou `false` qui évalue vos utilisateurs, puis les oriente vers une étape ou une autre. Vous devez utiliser au moins un segment ou un filtre. Il n'est pas nécessaire d'utiliser à la fois un segment et un filtre.

![Une étape d'arbre décisionnel avec le filtre « Foreground Push Enabled is true » sélectionné.]({% image_buster /assets/img/define-split-2.png %})

{% alert note %}
Par défaut, les segments et les filtres d'une étape de l'arbre décisionnel sont vérifiés juste après la réception de l'étape précédente, sauf si vous ajoutez un délai.
{% endalert %}

## Utiliser votre répartition {#use-your-split}

L'arbre décisionnel vous aide à distinguer les parcours de vos utilisateurs en fonction de leur segment, de leurs attributs, ou même de leur utilisation de certains canaux de communication pour recevoir vos messages.

Imaginons que vous créez un flux d'onboarding. Vous pourriez commencer par un e-mail de bienvenue lors de l'inscription. Puis, deux jours plus tard, vous souhaitez envoyer une notification push, mais uniquement aux utilisateurs dont les notifications push sont activées. Ensuite, tous les utilisateurs reçoivent un autre e-mail trois jours après leur inscription. Vous pourriez également utiliser votre arbre décisionnel pour envoyer un message in-app aux utilisateurs qui n'ont pas activé les notifications push afin de les encourager à le faire.

S'il n'y a pas d'étape après l'un des parcours, les utilisateurs qui empruntent ce parcours quitteront le Canvas.

![Une étape d'arbre décisionnel intitulée « Push activé ? » pour les utilisateurs dont les notifications push ne sont pas activées et ceux dont elles le sont. Pour les utilisateurs sans notifications push, un délai de 3 jours est appliqué, puis ils reçoivent un e-mail. Pour les utilisateurs avec notifications push activées, un délai d'1 jour est appliqué, ils reçoivent une notification push suivie d'un délai de 2 jours, puis ils reçoivent le même e-mail que les utilisateurs sans notifications push.]({% image_buster /assets/img/use-split-onboarding-3.png %}){: style="max-width:60%"}

## Analytique {#analytics}

Consultez le tableau suivant pour les descriptions des indicateurs analytiques de cette étape :

| Indicateur | Description |
|---|---|
| _Entrées_ | Le nombre total de fois où l'étape a été atteinte. Si votre Canvas autorise la rééligibilité et qu'un utilisateur entre deux fois dans une étape de l'arbre décisionnel, deux entrées seront enregistrées. |
| _Oui_ | Le nombre d'entrées qui ont rempli les critères spécifiés et ont emprunté le parcours « oui ». |
| _Non_ | Le nombre d'entrées qui n'ont pas rempli les critères spécifiés et ont emprunté le parcours « non ». |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytique" }