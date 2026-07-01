---
nav_title: Rééligibilité
article_title: Rééligibilité
page_order: 10
page_type: reference
description: "Cet article de référence définit la rééligibilité pour les Campaigns et les Canvas."
tool:
    - Campaigns
    - Canvas
toc_headers: h2
---

# Rééligibilité pour les Campaigns et Canvas {#re-eligibility-for-campaigns-and-canvas}

> Lorsque vous planifiez une Campaign ou un Canvas récurrent(e) ou déclenché(e), vous avez la possibilité de permettre aux utilisateurs de redevenir éligibles. La rééligibilité signifie que les utilisateurs peuvent entrer dans la Campaign ou le Canvas plusieurs fois en fonction du déclencheur.

## Fonctionnement {#how-it-works}

Par défaut, Braze n'envoie un message à un utilisateur qu'une seule fois, même s'il se requalifie plusieurs fois, car la rééligibilité doit être activée séparément. Une fois activée, les membres qualifiés pourront recevoir à nouveau des messages après avoir reçu la première instance de la Campaign ou du Canvas. Vous pouvez définir le délai au bout duquel les utilisateurs redeviennent éligibles.

## Activer la rééligibilité {#turning-on-re-eligibility}

{% tabs local %}
{% tab campaign %}
Pour activer la rééligibilité pour une Campaign, cochez la case **Allow users to become re-eligible to receive campaign** dans la section **Delivery Controls**. Le délai maximum de rééligibilité pour une Campaign est de 720 jours.

Pour les Campaigns déclenchées avec la rééligibilité activée, les utilisateurs qui [n'ont pas réellement reçu le message de la Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#why-did-a-user-not-receive-my-triggered-campaign) (bien qu'ils aient effectué l'événement déclencheur) se qualifieront automatiquement pour le message la prochaine fois qu'ils effectueront l'événement déclencheur. En effet, la rééligibilité est basée sur la réception du message et non sur l'entrée dans la Campaign. En rendant les utilisateurs rééligibles pour une Campaign déclenchée, vous leur permettez de réellement recevoir (et pas simplement déclencher) le message plus d'une fois.

{% alert note %}
La « réception » inclut l'attribution via des identifiants de canal partagés : lorsqu'un message est distribué, ouvert ou cliqué, Braze met à jour les données de tous les profils partageant la même adresse e-mail ou le même numéro de téléphone. Ainsi, un utilisateur à qui le message n'a jamais été directement envoyé peut être marqué comme l'ayant reçu et peut ne pas redevenir éligible.
{% endalert %}

De plus, si vous essayez d'envoyer un message immédiatement avec une rééligibilité de zéro minute, nous tenterons toujours de le planifier immédiatement, quel que soit le nombre de versions précédentes de la Campaign ou du Canvas que l'utilisateur a reçues.

### Rééligibilité avec les Campaigns déclenchées par API {#re-eligibility-with-api-triggered-campaigns}

Le nombre de fois qu'un utilisateur reçoit une Campaign déclenchée par API peut être limité à l'aide des paramètres de rééligibilité. Cela signifie que l'utilisateur ne recevra la Campaign qu'une seule fois ou une fois dans une fenêtre donnée, quel que soit le nombre de fois où le déclencheur API est activé.

Par exemple, supposons que vous utilisiez une Campaign déclenchée par API pour envoyer à l'utilisateur un message concernant un article qu'il a récemment consulté. Dans ce cas, vous pouvez limiter la Campaign à l'envoi d'un message maximum par jour, quel que soit le nombre d'articles consultés, tout en activant le déclencheur API pour chaque article. En revanche, si votre Campaign déclenchée par API est transactionnelle, vous voudrez vous assurer que l'utilisateur reçoit la Campaign à chaque transaction en définissant le délai à zéro minute.
{% endtab %}

{% tab canvas %}

Pour activer la rééligibilité pour un Canvas, sélectionnez **Allow users to re-enter this Canvas** dans la section **Entry Controls**. Vous pouvez choisir entre permettre aux utilisateurs de réentrer après la durée maximale du Canvas ou après une fenêtre spécifiée.

La rééligibilité pour les variantes de Canvas est liée à l'entrée dans le Canvas plutôt qu'à la réception du message. Les utilisateurs qui entrent dans un Canvas et ne reçoivent aucun message ne pourront pas réentrer dans le Canvas à moins que la rééligibilité ne soit activée.

Notez qu'un utilisateur n'a pas besoin de quitter un Canvas avant d'y réentrer si la rééligibilité est définie à zéro seconde, ce qui signifie qu'un utilisateur peut entrer à nouveau dans le même Canvas. Autre exemple : si la durée du Canvas est définie à 7 jours et la période de rééligibilité à 3 jours, un utilisateur peut réentrer dans le Canvas avant d'avoir terminé son premier parcours.

Vous pouvez ajouter des filtres supplémentaires pour empêcher les utilisateurs de recevoir la même étape ou le même message plusieurs fois. Cependant, lorsqu'un utilisateur réentre dans un Canvas pour la deuxième fois, les étapes précédemment reçues lors de son premier passage dans le Canvas ne sont pas visibles pour l'utilisateur. Cela signifie que l'utilisateur peut toujours recevoir le même message à nouveau. Pour éviter cela, vous pouvez configurer le Canvas pour empêcher la réentrée ou définir la rééligibilité sur la durée maximale du Canvas.

Vous pouvez également utiliser une [étape de mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) pour que l'utilisateur recevant l'étape enregistre cela comme un attribut personnalisé, qui peut ensuite être utilisé pour filtrer les utilisateurs ayant déjà reçu l'étape au cours de leur parcours Canvas.

### Exemple {#example}

Par exemple, supposons qu'un utilisateur sans adresse e-mail entre dans un Canvas récurrent quotidien contenant une seule étape dans le parcours utilisateur. Cette étape ne contient qu'un message e-mail, donc l'utilisateur ne reçoit pas l'engagement. Cet utilisateur ne pourra pas réentrer dans le Canvas à moins que la rééligibilité ne soit activée.

Si vous avez un Canvas récurrent ou déclenché actif sans rééligibilité et que vous souhaitez que les utilisateurs réentrent dans le Canvas jusqu'à ce qu'ils reçoivent un message, vous pouvez envisager de permettre aux utilisateurs d'être rééligibles à l'entrée en ajoutant un filtre aux critères d'entrée qui exclut les clients ayant déjà reçu un message du Canvas.

Si la rééligibilité d'un Canvas est définie sur une durée plus courte que celle du Canvas, il est possible que les utilisateurs entrent dans le Canvas plus d'une fois, ce qui peut entraîner un comportement trompeur pour les Canvas utilisant des messages in-app avec des délais particulièrement longs. Étant donné que plusieurs messages in-app de Canvas pourraient être déclenchés par le même démarrage de session, l'utilisateur pourrait potentiellement recevoir le même message de manière répétée si un composant spécifique s'affiche plus rapidement que les autres.
{% endtab %}
{% endtabs %}

## Calculs du délai de rééligibilité {#re-eligibility-delay-calculations}

La rééligibilité pour les Campaigns et les Canvas est calculée en secondes, et non en jours calendaires. Cela signifie qu'un jour compte comme 24 heures (soit 86 400 secondes) à partir du moment où un utilisateur reçoit le message, et non le jour calendaire suivant à minuit. De même, un mois compte exactement 2 592 000 secondes, soit environ 30 jours.

### Exemple

Considérez le scénario suivant :

* Une Campaign est configurée pour être envoyée mensuellement le 15 avec une rééligibilité définie à 30 jours.
* Il y a moins de 30 jours entre le 15 février et le 15 mars.

Cela signifie que les utilisateurs ayant reçu la Campaign le 15 février ne sont pas éligibles pour la Campaign envoyée le 15 mars. (Un utilisateur peut être marqué comme ayant « reçu » la Campaign en raison d'identifiants de canal partagés — par exemple, s'il partage une adresse e-mail ou un numéro de téléphone avec quelqu'un qui a reçu, ouvert ou cliqué le message.) Si la Campaign est configurée pour être envoyée quotidiennement à 8 h avec une rééligibilité d'un jour, et qu'il y a une latence dans l'envoi du message, les utilisateurs ayant reçu la Campaign à 8 h 30 ne sont pas encore rééligibles le lendemain à 8 h.

## Rééligibilité pour les Content Cards {#re-eligibility-for-content-cards}

Lorsque la rééligibilité est activée pour des Campaigns ou des étapes de Canvas de Content Cards, un utilisateur peut recevoir une autre carte alors qu'une carte précédente de la même Campaign est encore présente dans son flux, ce qui peut ressembler à des cartes en double. Pour réduire les doublons, désactivez la rééligibilité ou allongez la fenêtre de rééligibilité afin que la première carte [expire du flux]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#the-30-day-expiration-and-re-eligibility) avant que l'utilisateur ne se qualifie pour un nouvel envoi.

## Rééligibilité pour les bannières {#re-eligibility-for-banners}

Lorsque la rééligibilité est activée pour des Campaigns de bannières, les utilisateurs qui ferment une bannière peuvent redevenir éligibles après une fenêtre de temporisation configurable qui commence au moment de la fermeture. Si la rééligibilité n'est pas activée, les utilisateurs ayant fermé la bannière restent inéligibles. Pour configurer la rééligibilité, consultez [Configurer la rééligibilité]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility). Notez que les étapes de bannière dans Canvas utilisent les paramètres de réentrée du Canvas à la place.

## Test multivarié {#multivariate-testing}

Pour les tests multivariés, Braze détermine la rééligibilité des variantes pour toutes les Campaigns, les messages in-app déclenchés et les Canvas en utilisant les règles suivantes :

- Lorsque les pourcentages de variantes ne sont pas modifiés, chaque utilisateur entrera toujours dans la même variante d'une Campaign, d'un message in-app déclenché ou d'un Canvas à chaque fois qu'il est rééligible.
- Si les pourcentages de variantes changent, les utilisateurs peuvent être redistribués vers d'autres variantes.
- Les groupes de contrôle resteront cohérents si le pourcentage de variante est inchangé, et aucun utilisateur ayant précédemment reçu des messages n'entrera jamais dans le groupe de contrôle lors d'un envoi ultérieur, tout comme aucun utilisateur du groupe de contrôle ne recevra jamais de message.