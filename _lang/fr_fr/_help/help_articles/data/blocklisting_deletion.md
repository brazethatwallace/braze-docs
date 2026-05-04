---
nav_title: Différence entre la liste d'exclusion et la suppression
article_title: Différence entre la liste d'exclusion et la suppression
page_order: 2

page_type: solution
description: "Cet article d'aide vous explique la différence entre la mise en liste d'exclusion et la suppression d'attributs."
---

# Différence entre la liste d'exclusion et la suppression {#difference-between-blocklisting-and-deleting}

Pour comprendre la différence entre placer des données personnalisées dans une liste d'exclusion et les supprimer dans Braze, examinez les résultats de chaque action :

- **Liste d'exclusion :** Si des attributs personnalisés, des événements ou des achats sont placés en liste d'exclusion, ils restent sur les profils utilisateur, mais Braze ne traite plus les nouvelles données pour ces objets.
- **Suppression :** Si des attributs personnalisés, des événements ou des achats sont supprimés, Braze retire ces données des profils utilisateur. Les attributs personnalisés et événements supprimés sont déplacés dans la `Corbeille` pendant sept jours, durant lesquels vous pouvez les restaurer. Après sept jours, Braze les supprime définitivement. La suppression n'empêche pas non plus la réception de nouvelles données entrantes ; assurez-vous donc que les données ne sont plus envoyées via votre SDK, votre API ou vos imports CSV avant de procéder à la suppression.

## Que dois-je faire ? {#which-should-i-do}

Pour mettre des données en liste d'exclusion, Braze doit envoyer les informations de mise en liste d'exclusion à l'appareil de chaque utilisateur. Il s'agit d'une opération gourmande en données, ce que nous essayons idéalement d'éviter. De plus, si la liste est trop importante (> 100 attributs, événements ou achats), votre application peut commencer à ralentir.

Si vous ne prévoyez plus d'envoyer des attributs à Braze, la suppression est l'approche recommandée.

Quel que soit votre choix, les attributs personnalisés, les événements et les achats que vous supprimez n'apparaissent plus sur la page **Manage Workspace**, ce qui les retire des filtres de segment. Si vous supprimez des données personnalisées, Braze retire ces données au niveau utilisateur des profils.