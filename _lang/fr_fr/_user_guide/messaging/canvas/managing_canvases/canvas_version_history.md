---
nav_title: Historique des versions de Canvas
article_title: Historique des versions de Canvas
alias: "/canvas_version_history/"
page_order: 2
description: "Cet article de référence explique comment gérer l'historique des versions de votre Canvas."
page_type: reference
tool: Canvas
---

# Historique des versions de Canvas {#canvas-version-history}

> L'historique des versions vous permet de consulter et d'accéder aux analyses du Canvas ainsi qu'aux parcours utilisateurs de n'importe quelle version précédente de votre Canvas.

Consulter l'historique des versions de votre Canvas peut s'avérer particulièrement utile pour garder une trace de l'évolution d'un Canvas. Par exemple, si vous effectuez un changement majeur, vous pouvez vous référer aux versions précédentes du Canvas pour mieux comprendre comment vos workflows ont évolué.

{% alert tip %}
Pour obtenir la liste complète des Canvas de votre espace de travail (par exemple, dans le cadre d'un audit), utilisez l'[endpoint Exporter la liste des Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) et paginez les résultats.
{% endalert %}

## Gestion des versions {#managing-versions}

![]({% image_buster /assets/img_archive/canvas_version_history.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Pour créer une nouvelle version, cliquez sur **Update Canvas**. Cela vous permet d'apporter des modifications sans écraser la configuration précédente du Canvas. Lorsqu'une nouvelle version du Canvas est créée, les utilisateurs déjà présents dans le Canvas progresseront dans le workflow de la nouvelle version. Les utilisateurs qui entrent dans le Canvas accéderont également à la nouvelle version.

Pour accéder à l'historique des versions, rendez-vous dans les détails de votre Canvas en haut de la page et sélectionnez **# Versions**. Vous aurez alors accès au panneau latéral **Version history**. Sélectionnez l'une des versions du Canvas dans le panneau latéral pour afficher et comparer les détails du Canvas. Pour basculer entre les analyses du Canvas et la configuration du Canvas, cliquez sur **View Analytics** ou **View Canvas** dans la barre d'outils en bas de page.

{% alert note %}
Les Canvas répertoriés dans **Version history** sont en lecture seule.
{% endalert %}

Pour afficher la liste des modifications apportées à une version pendant qu'elle était active, sélectionnez **View Changes** dans le panneau latéral de l'historique des versions. Vous pouvez également consulter toutes les modifications associées à une version dans le journal des modifications du Canvas.

Notez que si vous n'avez effectué aucune modification entre le lancement d'un Canvas et la création d'une deuxième version, aucun changement n'apparaîtra dans **See Changes** pour la première version du Canvas.

Au fur et à mesure que le nombre de versions augmente, vous pouvez également renommer chaque version dans le panneau latéral pour rester organisé. Par défaut, les noms de version sont générés sous forme de numéro en fonction du nombre de versions précédemment créées. Si vous renommez une version alors qu'elle n'est plus active, cela apparaîtra dans le journal des modifications du Canvas, mais pas dans le journal des modifications de la version au sein de la vue de l'historique des versions.

![Exemple de journal des modifications du Canvas montrant que deux nouvelles versions du Canvas ont été créées.]({% image_buster /assets/img_archive/canvas_version_history_changelog.png %}){: style="max-width:85%" }

### Suppression de versions {#discarding-versions}

Vous pouvez créer jusqu'à 10 versions par Canvas. Si vous atteignez cette limite, vous pouvez supprimer une version pour libérer de l'espace pour une nouvelle. Notez que les versions sont supprimées dès que vous cliquez sur **Discard**, et non lorsque vous mettez à jour le Canvas. La suppression d'une version est reflétée dans le journal des modifications global du Canvas, et non dans le journal des modifications d'une version spécifique.

Si vous supprimez une version, la configuration du Canvas sera immédiatement perdue, mais les analyses associées à la version supprimée seront conservées.

## Consultation des analyses {#viewing-analytics}

Dans l'historique des versions, vous pouvez consulter les analyses au niveau du Canvas et au niveau des étapes. Dans la vue d'une version du Canvas, les données couvriront l'ensemble de la plage de dates, et pas uniquement la plage de dates de cette version. En revanche, au niveau des étapes, les analyses ne seront affichées que pour les étapes qui existaient pendant que cette version était active. Ces analyses sont calculées sur la base de jours calendaires correspondant au fuseau horaire de votre société, de sorte qu'elles ne seront pas spécifiques à l'heure exacte de création de la version.