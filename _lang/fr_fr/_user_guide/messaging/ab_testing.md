---
nav_title: Test A/B
article_title: "Tests A/B"
page_order: 6
layout: dev_guide
guide_top_header: "Tests A/B"
guide_top_text: "Menez des expériences pour optimiser vos messages. Un test A/B compare les réponses des utilisateurs à plusieurs versions d'une même **Campaign**, tandis qu'un test multivarié étend ce principe à deux variables ou plus. Dans Braze, les deux termes sont utilisés de manière interchangeable, car le processus de configuration est identique. Associez les tests A/B à la <a href='/docs/user_guide/brazeai/intelligence_suite/intelligent_selection'>Sélection intelligente</a> pour optimiser automatiquement vos résultats."

page_type: landing
description: "Configurez et analysez des tests A/B et des expériences multivariées dans Braze."

guide_featured_title: "Articles de la section"
guide_featured_list:
  - name: Concepts
    link: /docs/user_guide/messaging/ab_testing/concepts
    image: /assets/img/braze_icons/lightbulb-02.svg
  - name: Créer des tests
    link: /docs/user_guide/messaging/ab_testing/create_tests
    image: /assets/img/braze_icons/plus-circle.svg
  - name: Optimisations
    link: /docs/user_guide/messaging/ab_testing/optimizations
    image: /assets/img/braze_icons/settings-01.svg
  - name: Analyse
    link: /docs/user_guide/messaging/ab_testing/analytics
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: FAQ
    link: /docs/user_guide/messaging/ab_testing/faq
    image: /assets/img/braze_icons/annotation-question.svg
---

## Quand utiliser les tests A/B {#when-to-use-ab-tests}

- **Essayer un nouveau type de message :** Expérimentez et découvrez ce qui parle à vos utilisateurs.
- **Campaigns d'onboarding ou envois récurrents :** Assurez-vous que vos **Campaigns** à fort trafic sont aussi efficaces que possible.
- **Plusieurs idées de messages :** Lancez un test et prenez une décision fondée sur les données.
- **Remettre en question les hypothèses :** Vérifiez si les tactiques marketing classiques fonctionnent réellement pour votre audience spécifique.

## Conseils pour mener des tests efficaces {#tips-for-running-effective-tests}

- **Utilisez des échantillons de grande taille** pour vous assurer que les résultats reflètent votre utilisateur moyen et ne sont pas faussés par des valeurs aberrantes.
- **Randomisez les groupes de test** afin que les différences de taux de réponse reflètent des différences de messages, et non des différences d'échantillons.
- **Sachez ce que vous testez.** Isoler un seul changement permet d'identifier l'élément ayant eu le plus d'impact ; tester plusieurs différences à la fois permet de comparer des approches plus globales.
- **Définissez la durée du test à l'avance** et ne l'interrompez pas prématurément, même si les premiers résultats semblent prometteurs.
- **Ajoutez les tests avant le lancement.** Ajouter un test à une **Campaign** déjà en cours produit des résultats inexacts. Clonez la **Campaign**, arrêtez l'originale, puis ajoutez le test au clone.
- **Incluez un [groupe de contrôle]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/#including-a-control-group)** pour mesurer l'impact par rapport à l'absence totale de message.