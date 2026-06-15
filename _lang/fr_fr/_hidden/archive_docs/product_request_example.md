---
nav_title: Exemple de demande de produit
hidden: true
alias: /product_request/

page_type: reference
description: "Cet article de référence présente un exemple de demande de produit."
---

# Exemple de demande de produit {#product-request-example}

Voici un exemple de demande de produit pertinente soumise par un client. Elle définit clairement la demande et détaille le cas d'utilisation de la fonctionnalité.

## Exemple de demande de la part de Skyscanner {#example-request-from-skyscanner}

### Quel problème essayez-vous de résoudre ? {#what-problem-are-you-trying-to-solve}
Skyscanner aimerait pouvoir indiquer la priorité de certaines étiquettes par rapport à d'autres, dans le contexte de la limite de fréquence.

### Quels sont les cas d'utilisation spécifiques ? {#what-are-some-specific-use-cases}
_C'est là que les liens vers les Campaigns et Canvas peuvent aider, ainsi qu'une description_

Comme nous allons déployer de plus en plus de Campaigns déclenchées, basées sur le comportement des utilisateurs, il est possible que certains e-mails se télescopent, et que ceux dont l'envoi est prévu en début de journée aient la priorité sur ceux de l'après-midi, puisque nous nous limitons à un e-mail par jour. Ce n'est pas idéal : par exemple, les e-mails concernant la partie inférieure de l'entonnoir (reciblage) génèrent plus de résultats que leurs homologues TOFU (par exemple la newsletter), et nous aimerions pouvoir les hiérarchiser.

Par exemple, nous aimerions pouvoir définir que la limite de fréquence est au maximum d'un jour, mais que toutes les Campaigns et tous les Canvas étiquetés avec un reciblage de redirection sont P0, toutes les inspirations sont P3, tous les reciblages pour les recherches seraient P2, Xsell pourrait être P1, etc.

À titre d'illustration, le résultat serait alors de définir des étiquettes par ordre de priorité.

### Avez-vous des informations supplémentaires ? {#do-you-have-any-additional-insight}
_En quoi cela vous avantagerait-il, vous et vos équipes, au-delà de « voici ce que nous pourrions faire »._

Cela nous aiderait à créer nos e-mails et nos Campaigns en tant qu'écosystème, et à les intégrer dans une expérience globale pour les utilisateurs, en supprimant le casse-tête des horaires d'envoi pour nous assurer que le TOFU ne prend pas le dessus.