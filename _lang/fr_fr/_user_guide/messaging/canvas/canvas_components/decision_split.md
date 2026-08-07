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

### Définir votre arbre décisionnel {#define-your-split}

Comment souhaitez-vous répartir vos utilisateurs ? Vous pouvez utiliser des [Segments]({{site.baseurl}}/user_guide/audience/segments) et des filtres pour tracer la ligne. Essentiellement, vous créez une requête `true` ou `false` qui évaluera vos utilisateurs et les orientera ensuite vers une étape ou une autre. Vous devez utiliser au moins un Segment ou un filtre. Il n'est pas nécessaire d'utiliser à la fois un Segment et un filtre.

![Une étape d'arbre décisionnel avec le filtre « Foreground Push Enabled is true » sélectionné.]({% image_buster /assets/img/define-split-2.png %})

{% alert note %}
Par défaut, les Segments et les filtres d'une étape d'arbre décisionnel sont vérifiés juste après la réception de l'étape précédente, sauf si vous ajoutez un délai.
{% endalert %}

#### Filtres de reciblage dans les Canvas avec réentrée {#retargeting-filters-in-canvases-with-re-entry}

Les filtres de reciblage dans une étape d'arbre décisionnel, tels que `Clicked/Opened Step In This Canvas`, évaluent l'engagement sur l'ensemble des entrées dans le Canvas pour un utilisateur, y compris les entrées précédentes. Par exemple, si un utilisateur a interagi avec une étape lors d'une entrée précédente, l'arbre décisionnel reconnaît cette interaction lorsqu'il réintègre le Canvas.

Pour les Canvas avec réentrée activée, utilisez une étape [Parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) avec le déclencheur **Interact with Step** lorsque vous devez évaluer l'engagement uniquement pendant l'entrée en cours dans le Canvas et dans une fenêtre temporelle donnée. Les parcours d'action ne comptent que les interactions qui se produisent pendant la fenêtre d'évaluation de l'étape.

## Utiliser votre arbre décisionnel {#use-your-split}

L'utilisation d'un arbre décisionnel peut vous aider à distinguer les parcours de vos utilisateurs en fonction de leur Segment ou de leurs attributs, et même selon qu'ils utilisent certains canaux de communication pour recevoir vos messages !

Imaginons que vous créez un flux d'onboarding. Vous pourriez commencer par un e-mail de bienvenue lors de l'inscription. Puis, deux jours plus tard, vous souhaitez envoyer une notification push, mais uniquement aux utilisateurs qui ont activé les notifications push. Ensuite, tous les utilisateurs reçoivent un autre e-mail trois jours après leur inscription. Vous pourriez également utiliser votre arbre décisionnel pour envoyer un message in-app aux utilisateurs qui n'ont pas activé les notifications push afin de les encourager à le faire.

S'il n'y a pas d'étape après l'un des parcours, les utilisateurs qui empruntent ce parcours quitteront le Canvas.

![Une étape d'arbre décisionnel intitulée « Push activé ? » pour les utilisateurs qui n'ont pas activé les notifications push et ceux qui les ont activées. Pour les utilisateurs qui n'ont pas activé les notifications push, ils subissent un délai de 3 jours puis reçoivent un e-mail. Pour les utilisateurs qui ont activé les notifications push, ils subissent un délai d'1 jour, reçoivent une notification push suivie d'un délai de 2 jours, puis reçoivent le même e-mail que les utilisateurs qui n'ont pas activé les notifications push.]({% image_buster /assets/img/use-split-onboarding-3.png %}){: style="max-width:60%"}

## Analyse {#analytics}

Consultez le tableau suivant pour obtenir les descriptions des analyses de cette étape :

| Indicateur | Description |
|---|---|
| _Entrées_ | Le nombre total de fois où l'étape a été atteinte. Si votre Canvas autorise la rééligibilité et qu'un utilisateur entre deux fois dans une étape d'arbre décisionnel, deux entrées seront enregistrées. |
| _Oui_ | Le nombre d'entrées qui ont rempli les critères spécifiés et ont emprunté le parcours « oui ». |
| _Non_ | Le nombre d'entrées qui n'ont pas rempli les critères spécifiés et ont emprunté le parcours « non ». |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analyse" }