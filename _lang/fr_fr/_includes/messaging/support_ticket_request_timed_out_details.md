- **Enregistrement d'écran :** Un enregistrement des étapes que vous avez suivies avant de voir l'erreur, y compris les transitions de page.
- **Horodatage et fuseau horaire :** L'heure exacte à laquelle l'erreur s'est produite et votre fuseau horaire.
- **Navigateur et version :** Le navigateur que vous utilisez (par exemple, Chrome 120, Safari 17) et si vous avez essayé de reproduire l'erreur dans un autre navigateur.
{% if include.context == 'canvas' -%}
- **Étapes pour reproduire :** Une description claire des actions qui déclenchent l'erreur, y compris les étapes du Canvas ou les configurations spécifiques impliquées.
{% elsif include.context == 'campaign' -%}
- **Étapes pour reproduire :** Une description claire des actions qui déclenchent l'erreur, y compris les paramètres spécifiques de Campaign ou de Canvas impliqués.
{% endif -%}
- **Journaux réseau (facultatif) :** Ouvrez les outils de développement de votre navigateur (onglet **Network**), reproduisez l'erreur et exportez le journal réseau sous forme de fichier journal HTTP Archive (HAR). Cela aide l'équipe d'assistance à identifier quel appel API est en dépassement de délai.