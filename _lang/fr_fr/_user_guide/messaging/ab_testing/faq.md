---
nav_title: FAQ
article_title: FAQ sur les tests multivariés et A/B
page_order: 21
page_type: reference
toc_headers: h2
description: "Cet article répond aux questions fréquemment posées sur les tests multivariés et A/B avec Braze."
---

# FAQ sur les tests multivariés et A/B {#multivariate-and-ab-test-faq}

> Cet article répond aux questions fréquemment posées sur les tests multivariés et A/B avec Braze.

## Principes de base des tests {#testing-basics}

### Quelle est la différence entre un test A/B et un test multivarié ? {#what-is-the-difference-between-ab-testing-and-multivariate-testing}

#### Test A/B {#ab-testing}

Dans un test A/B, le marketeur expérimente une seule variable au sein de la campagne (comme la ligne d'objet d'un e-mail ou l'heure d'envoi du message). Cela consiste à diviser aléatoirement un sous-ensemble de l'audience en deux groupes ou plus, à présenter à chaque groupe une variante différente, puis à observer laquelle affiche le taux de conversion le plus élevé. En général, la variante la plus performante est ensuite envoyée au reste de l'audience.

#### Test multivarié {#multivariate-testing}

Le test multivarié est une extension du test A/B qui permet au marketeur de tester plusieurs variables simultanément afin de déterminer la combinaison la plus efficace. Par exemple, vous pourriez tester la ligne d'objet de votre e-mail, l'image qui accompagne votre texte et la couleur du bouton d'appel à l'action. Ce type de test vous permet d'explorer davantage de variables et de combinaisons de variantes au sein d'une seule expérience, et d'obtenir des informations plus rapidement et de manière plus complète qu'avec un test A/B. Cependant, tester plus de variables et de combinaisons au sein d'une seule expérience nécessite une audience plus large pour atteindre une significativité statistique.

### Comment les résultats d'un test A/B sont-ils calculés ? {#how-are-ab-test-results-calculated}

Braze compare toutes les variantes entre elles à l'aide du test du khi-deux de Pearson, qui mesure si une variante surpasse statistiquement toutes les autres à un niveau de significativité de p < 0,05, soit ce que nous appelons une significativité de 95 %. Parmi toutes les variantes qui dépassent ce seuil de significativité, la variante la plus performante est désignée comme « gagnante ».

Il s'agit d'un test distinct du score de confiance, qui décrit uniquement la performance d'une variante par rapport au contrôle sous la forme d'une valeur numérique comprise entre 0 et 100 %. Plus précisément, il représente notre confiance dans le fait que la différence standardisée du taux de conversion entre la variante et le contrôle est significativement supérieure au hasard.

### Pourquoi la distribution des variantes n'est-elle pas uniforme ? {#why-isnt-the-variant-distribution-even}

L'affectation des variantes est aléatoire à chaque envoi, de sorte que la répartition réelle peut ne pas correspondre exactement aux pourcentages que vous avez configurés, en particulier avec des échantillons de petite taille. Pour en savoir plus, consultez [Distribution des variantes]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/variant_distribution/).

## Exécution et conclusion des tests {#running-and-concluding-tests}

### Quand le test initial est-il terminé ? {#when-is-the-initial-test-over}

Lorsque vous utilisez la variante gagnante pour des campagnes à envoi unique, le test se termine lorsque l'heure d'envoi de la variante gagnante arrive. Braze désigne une variante comme gagnante si elle affiche le taux de conversion le plus élevé avec une marge statistiquement significative.

Pour les campagnes récurrentes, déclenchées par une action ou déclenchées par l'API, vous pouvez utiliser la Sélection intelligente pour suivre en continu les données de performance de chaque variante et optimiser en permanence le trafic de la campagne vers les variantes les plus performantes. Avec la Sélection intelligente, plutôt que de définir explicitement un groupe d'expérience où les utilisateurs reçoivent des variantes aléatoires, l'algorithme de Braze affine continuellement son estimation de la variante la plus performante, ce qui permet potentiellement une sélection plus rapide de la meilleure variante.

### Comment Braze gère-t-il les utilisateurs qui ont reçu une variante de message dans une campagne récurrente ou une étape d'entrée de Canvas ? {#how-does-braze-handle-users-who-received-a-message-variant-in-a-recurring-campaign-or-canvas-entry-step}

Les utilisateurs sont affectés aléatoirement à une variante particulière avant de recevoir la campagne pour la première fois. Chaque fois que la campagne est reçue par la suite (ou que l'utilisateur entre à nouveau dans une variante de Canvas), ils reçoivent la même variante, sauf si les pourcentages de variantes sont modifiés. Si les pourcentages de variantes changent, les utilisateurs peuvent être redistribués vers d'autres variantes. Les utilisateurs restent dans ces variantes jusqu'à ce que les pourcentages soient à nouveau modifiés. Les utilisateurs ne sont redistribués que pour les variantes qui ont été modifiées.

Par exemple, supposons que nous ayons une campagne ou un Canvas avec trois variantes. Si seules la variante A et la variante B sont modifiées ou mises à jour, les utilisateurs de la variante C ne seront pas redistribués car le pourcentage de la variante C n'a pas changé. Les groupes de contrôle restent cohérents si le pourcentage de la variante est inchangé. Les utilisateurs qui ont précédemment reçu des messages ne peuvent pas entrer dans le groupe de contrôle lors d'un envoi ultérieur, et aucun utilisateur du groupe de contrôle ne peut jamais recevoir de message.

{% alert note %}
Un utilisateur peut être marqué comme ayant « reçu » un message s'il partage un identifiant de canal (comme une adresse e-mail ou un numéro de téléphone) avec quelqu'un qui a reçu, ouvert ou cliqué sur le message.
{% endalert %}

#### Qu'en est-il des Chemins d'expérience ? {#what-about-experiment-paths}

Le même principe s'applique, car les chemins de Canvas qui suivent une expérience sont également des variantes.

#### Puis-je effectuer des actions pour redistribuer les utilisateurs dans les campagnes et les Canvas ? {#can-i-take-actions-to-redistribute-users-in-campaigns-and-canvases}

La seule façon de redistribuer les utilisateurs dans les Canvas est d'utiliser les [chemins aléatoires dans les Chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/#step-1-choose-the-number-of-paths-and-audience-distribution), qui randomisent toujours l'affectation des chemins lorsque les utilisateurs entrent à nouveau dans le Canvas. Cependant, il ne s'agit pas d'une expérience standard et cela pourrait invalider les résultats de l'expérience, car le groupe de contrôle peut être contaminé par des utilisateurs du groupe de traitement.

## Confiance et biais {#confidence-and-bias}

### La confiance augmente-t-elle avec le temps ? {#does-confidence-increase-over-time}

La confiance augmente avec le temps si toutes les autres conditions restent constantes. Cela signifie qu'il n'y a pas d'autres facteurs marketing susceptibles d'influencer les variantes, comme par exemple une variante A qui mentionne une promotion de 25 % de réduction se terminant en cours de test.

La confiance mesure le degré de certitude de Braze quant au fait que la variante est différente du contrôle. À mesure que davantage de messages sont envoyés, la puissance statistique du test augmente, ce qui renforce la confiance dans le fait que les différences de performance mesurées ne sont pas dues au hasard. En général, un échantillon plus large augmente notre confiance dans l'identification de petites différences de performance entre les variantes et le contrôle.

### L'affectation aux groupes de contrôle et de test peut-elle introduire un biais dans les tests ? {#can-control-and-test-group-assignments-introduce-bias-to-testing}

Il n'existe aucun moyen pratique pour que les attributs ou comportements d'un utilisateur avant la création d'une campagne ou d'un Canvas particulier varient systématiquement entre les variantes et le contrôle.

Pour affecter les utilisateurs aux variantes de message, aux variantes de Canvas ou à leurs groupes de contrôle respectifs, nous commençons par associer leur ID utilisateur généré aléatoirement à l'ID de campagne ou de Canvas généré aléatoirement. Ensuite, nous appliquons un algorithme de hachage sha256 et divisons le résultat par 100, en conservant le reste (également appelé modulo 100). Enfin, nous classons les utilisateurs dans des tranches correspondant aux pourcentages d'affectation des variantes (et du contrôle facultatif) définis dans le tableau de bord.

### Pourquoi ne puis-je pas utiliser la limite de débit avec un groupe de contrôle ? {#why-cant-i-use-rate-limiting-with-a-control-group}

Braze ne prend actuellement pas en charge la limite de débit avec les tests A/B comportant un groupe de contrôle. En effet, la limite de débit ne s'applique pas au groupe de contrôle de la même manière qu'aux variantes, ce qui introduit un biais. Envisagez plutôt d'utiliser la [Sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/), qui ajuste automatiquement le pourcentage d'utilisateurs recevant chaque variante en fonction des analyses et de la performance de la campagne.