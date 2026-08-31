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

## Bases des tests {#testing-basics}

### Quelle est la différence entre le test A/B et le test multivarié ? {#what-is-the-difference-between-ab-testing-and-multivariate-testing}

#### Test A/B {#ab-testing}

Dans un test A/B, le marketeur expérimente une seule variable au sein de la Campaign (comme la ligne d'objet de l'e-mail ou l'heure d'envoi du message). Cela consiste à diviser aléatoirement un sous-ensemble de l'audience en deux groupes ou plus, à présenter à chaque groupe une variante différente, puis à observer quelle variante affiche le taux de conversion le plus élevé. En général, la variante la plus performante est ensuite envoyée au reste de l'audience.

#### Test multivarié {#multivariate-testing}

Le test multivarié est une extension du test A/B, qui permet au marketeur de tester plusieurs variables simultanément afin de déterminer la combinaison la plus efficace. Par exemple, vous pourriez tester la ligne d'objet de votre e-mail, l'image accompagnant votre texte et la couleur du bouton d'appel à l'action. Ce type de test vous permet d'explorer davantage de variables et de combinaisons de variantes au sein d'une seule expérience, et d'obtenir des informations plus rapidement et de manière plus complète qu'avec un test A/B. Cependant, tester plus de variables et de combinaisons au sein d'une seule expérience nécessite une audience plus large pour atteindre une signification statistique.

### Comment les résultats du test A/B sont-ils calculés ? {#how-are-ab-test-results-calculated}

Braze teste toutes les variantes les unes par rapport aux autres à l'aide du test du khi-deux de Pearson, qui mesure si une variante surpasse statistiquement toutes les autres à un niveau de signification de p < 0,05, soit ce que nous appelons une signification de 95 %. Parmi toutes les variantes dépassant ce seuil de signification, la variante la plus performante est désignée comme la « gagnante ».

Il s'agit d'un test distinct du score de confiance, qui ne décrit que la performance d'une variante par rapport au groupe de contrôle sous la forme d'une valeur numérique comprise entre 0 et 100 %. Plus précisément, il représente notre confiance dans le fait que la différence standardisée du taux de conversion entre la variante et le groupe de contrôle est significativement supérieure au hasard.

### Pourquoi la distribution des variantes n'est-elle pas uniforme ? {#why-isnt-the-variant-distribution-even}

L'attribution des variantes est aléatoire à chaque envoi, de sorte que la répartition réelle peut ne pas correspondre exactement aux pourcentages que vous avez configurés, en particulier avec des échantillons de petite taille. Pour en savoir plus, consultez la section [Distribution des variantes]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/variant_distribution).

## Exécution et conclusion des tests {#running-and-concluding-tests}

### Quand le test initial est-il terminé ? {#when-is-the-initial-test-over}

Pour une Campaign à envoi unique utilisant **Optimiser avec BrazeAI<sup>TM</sup>**, le test initial se termine après la durée d'expérience configurée. BrazeAI<sup>TM</sup> envoie ensuite la variante la plus performante à l'audience restante.

Pour les Campaigns récurrentes, déclenchées par action et déclenchées par API qui envoient plusieurs fois, **Optimiser avec BrazeAI<sup>TM</sup>** suit en continu les performances des variantes et redirige le trafic de la Campaign vers les variantes les plus performantes.

### Comment Braze gère-t-il les utilisateurs qui ont reçu une variante de message dans une Campaign récurrente ou une étape d'entrée Canvas ? {#how-does-braze-handle-users-who-received-a-message-variant-in-a-recurring-campaign-or-canvas-entry-step}

Les utilisateurs sont assignés aléatoirement à une variante particulière avant de recevoir la Campaign pour la première fois. À chaque réception successive de la Campaign (ou lorsque l'utilisateur entre à nouveau dans une variante Canvas), il reçoit la même variante, sauf si les pourcentages de variantes sont modifiés. Si les pourcentages de variantes changent, les utilisateurs peuvent être redistribués vers d'autres variantes. Les utilisateurs restent dans ces variantes jusqu'à ce que les pourcentages soient de nouveau modifiés. Les utilisateurs ne sont redistribués que pour les variantes qui ont été modifiées.

Par exemple, imaginons que nous avons une Campaign ou un Canvas avec trois variantes. Si seules les variantes A et B sont modifiées ou mises à jour, les utilisateurs de la variante C ne seront pas redistribués, car le pourcentage de la variante C n'a pas changé. Les groupes de contrôle restent cohérents si le pourcentage de variante est inchangé. Les utilisateurs qui ont déjà reçu des messages ne peuvent pas intégrer le groupe de contrôle lors d'un envoi ultérieur, et aucun utilisateur du groupe de contrôle ne peut recevoir un message.

{% alert note %}
Un utilisateur peut être marqué comme ayant « reçu » un message s'il partage un identifiant de canal (tel qu'une adresse e-mail ou un numéro de téléphone) avec quelqu'un qui a reçu, ouvert ou cliqué le message.
{% endalert %}

#### Qu'en est-il des chemins d'expérience ? {#what-about-experiment-paths}

Le même principe s'applique, car les chemins Canvas suivant une expérience sont également des variantes.

#### Puis-je effectuer des actions pour redistribuer les utilisateurs dans les Campaigns et les Canvas ? {#can-i-take-actions-to-redistribute-users-in-campaigns-and-canvases}

La seule façon de redistribuer les utilisateurs dans les Canvas est d'utiliser les [chemins aléatoires dans les chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#step-1-choose-the-number-of-paths-and-audience-distribution), qui randomisent toujours les attributions de chemin lorsque les utilisateurs entrent à nouveau dans le Canvas. Cependant, il ne s'agit pas d'une expérience standard et cela pourrait invalider les résultats de l'expérience, car le groupe de contrôle peut être contaminé par des utilisateurs soumis au traitement.

## Confiance et biais {#confidence-and-bias}

### La confiance augmente-t-elle au fil du temps ? {#does-confidence-increase-over-time}

La confiance augmente au fil du temps si toutes les autres conditions restent constantes. Cela signifie qu'aucun autre facteur marketing ne vient influencer les variantes, comme par exemple une variante A évoquant une promotion de 25 % qui se terminerait en cours de test.

La confiance est une mesure du degré de certitude de Braze quant au fait qu'une variante diffère du groupe de contrôle. À mesure que davantage de messages sont envoyés, la puissance statistique du test augmente, ce qui accroît la confiance dans le fait que les différences de performance mesurées ne sont pas dues au hasard. En général, un échantillon plus grand renforce la capacité à identifier de faibles écarts de performance entre les variantes et le groupe de contrôle.

Cependant, si les taux de conversion entre les variantes et le groupe de contrôle convergent (se rapprochent) à mesure que davantage de messages sont envoyés, la confiance peut diminuer, car l'écart mesuré qui vous intéresse se réduit, ce qui peut contrebalancer l'avantage d'un échantillon plus large.

### L'affectation aux groupes de contrôle et de test peut-elle introduire un biais dans les tests ? {#can-control-and-test-group-assignments-introduce-bias-to-testing}

Il n'existe aucun moyen pratique pour que les attributs ou les comportements d'un utilisateur antérieurs à la création d'une Campaign ou d'un Canvas particulier varient systématiquement entre les variantes et le groupe de contrôle.

Pour affecter les utilisateurs aux variantes de message, aux variantes de Canvas ou à leurs groupes de contrôle respectifs, nous commençons par associer leur identifiant utilisateur généré aléatoirement à l'identifiant de Campaign ou de Canvas généré aléatoirement. Nous appliquons ensuite un algorithme de hachage sha256, divisons le résultat par 100 et conservons le reste (également appelé modulo 100). Enfin, nous répartissons les utilisateurs en tranches correspondant aux pourcentages d'affectation des variantes (et du groupe de contrôle optionnel) définis dans le tableau de bord.

### Pourquoi ne puis-je pas utiliser la limitation du débit avec un groupe de contrôle ? {#why-cant-i-use-rate-limiting-with-a-control-group}

Braze ne prend actuellement pas en charge la limitation du débit avec les tests A/B comportant un groupe de contrôle. La limitation du débit ne s'applique pas au groupe de contrôle de la même manière qu'aux variantes, ce qui introduit un biais. Envisagez plutôt d'utiliser l'option [Optimiser avec BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection), qui ajuste automatiquement le pourcentage d'utilisateurs recevant chaque variante en fonction des performances de la Campaign.