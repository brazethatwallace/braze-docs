1. In the Azure portal, navigate to the Microsoft Entra admin center, and then **App Registrations**.
2. Select **+ New registration** under **Identity > Applications > App registrations**
3. Enter a name, and select `Accounts in this organizational directory only` as the supported account type. Then, select **Register**.
4. Select the application (service principal) you just created, then navigate to **Certificates & secrets > + New client secret**
5. Enter a description for the secret, and set an expiry period for the secret. Then, select **Add**.
6. Note the client secret created to use in the Braze setup.
