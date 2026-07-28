1. No portal do Azure, navegue até o centro de administração do Microsoft Entra e, em seguida, **App Registrations**.
2. Selecione **+ New registration** em **Identity > Applications > App registrations**
3. Insira um nome e selecione `Accounts in this organizational directory only` como o tipo de conta compatível. Em seguida, selecione **Register**.
4. Selecione o app (service principal) que você acabou de criar e navegue até **Certificates & secrets > + New client secret**
5. Insira uma descrição para o segredo e defina um período de vencimento para o segredo. Em seguida, selecione **Add**.
6. Anote o segredo do cliente criado para usar na configuração da Braze.