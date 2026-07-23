1. Dans le portail Azure, accédez au centre d'administration Microsoft Entra, puis à **App Registrations**.
2. Sélectionnez **+ New registration** sous **Identity > Applications > App registrations**.
3. Saisissez un nom et sélectionnez `Accounts in this organizational directory only` comme type de compte pris en charge. Ensuite, sélectionnez **Register**.
4. Sélectionnez l'application (principal de service) que vous venez de créer, puis accédez à **Certificates & secrets > + New client secret**.
5. Saisissez une description pour le secret et définissez une période d'expiration. Ensuite, sélectionnez **Add**.
6. Notez le secret client créé afin de l'utiliser lors de la configuration de Braze.