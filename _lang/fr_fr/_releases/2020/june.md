---
nav_title: juin
page_order: 7
noindex: true
page_type: update
description: "Cet article contient les notes de version de juin 2020."
---
# Juin 2020 {#june-2020}

## Rapports de rétention {#retention-reports}

Les rapports de rétention offrent désormais la rétention par plage pour les [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/test_campaigns/retention_reports/) et les [Canvas]({{site.baseurl}}/user_guide/analytics/reports/retention_reports/). La rétention par plage mesure le nombre d'utilisateurs qui reviennent et effectuent un événement de rétention sélectionné pendant des intervalles de temps spécifiques.

## Mises à jour de l'API de suivi des utilisateurs {#user-track-api-updates}

L'[endpoint `users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) dispose désormais d'un taux par défaut de 50 000 requêtes API par minute pour les entreprises créées sur le tableau de bord après le 2 juin 2020. Les entreprises existantes créées avant cette date et leurs espaces de travail continueront de bénéficier d'un nombre illimité de requêtes API vers l'endpoint `users/track`.

 Braze impose cette valeur par défaut sur notre endpoint client le plus utilisé, dans le cadre de nos objectifs de stabilité et de fiabilité pour notre API et notre infrastructure. La limite imposée est très généreuse et n'affectera que très peu d'entreprises et leurs opérations courantes. Si vous avez besoin d'une augmentation de cette limite, contactez votre gestionnaire de la satisfaction client ou notre équipe d'assistance pour en faire la demande.