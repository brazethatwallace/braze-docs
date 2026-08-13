Si vous voyez deux entrées de données personnalisées avec le même nom visible, l'une des entrées peut contenir un espace invisible au début ou à la fin.

Pour résoudre ce problème :

1. Accédez à **Data Settings** > **Custom Attributes** ou **Custom Events**, puis localisez les deux entrées qui semblent avoir le même nom.
2. Vérifiez si l'un des noms contient un espace masqué :
    1. Faites un clic droit sur chaque nom et sélectionnez **Inspecter**.
    2. Vérifiez la valeur textuelle HTML dans les outils de développement de votre navigateur.
    3. Comparez les valeurs (par exemple, `email` par rapport à ` email`).
    4. Si nécessaire, consultez [Inspecter et modifier les pages et les styles avec Chrome DevTools](https://developer.chrome.com/docs/devtools/inspect-mode).
3. Décidez quel nom doit rester comme clé canonique, et standardisez l'orthographe et la casse exactes.
4. Si une entrée contient des espaces au début ou à la fin et a été créée directement dans le tableau de bord, cessez d'utiliser cette entrée et passez à la clé canonique :
    - Mettez à jour tous les workflows du tableau de bord, les imports CSV et les runbooks internes pour utiliser la clé canonique.
    - [Bloquez les données personnalisées]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data) pour l'entrée incorrecte lorsque vous êtes prêt à la retirer.
5. Vérifiez vos chemins d'ingestion :
    - Les payloads API et SDK suppriment automatiquement les espaces au début et à la fin.
    - Les noms créés dans le tableau de bord ne sont pas automatiquement nettoyés ; une saisie manuelle et une gouvernance sont donc nécessaires.