1. Navigieren Sie im Azure-Portal zum Microsoft Entra Admin Center und dann zu **App Registrations**.
2. Wählen Sie **+ New registration** unter **Identity > Applications > App registrations** aus.
3. Geben Sie einen Namen ein und wählen Sie `Accounts in this organizational directory only` als unterstützten Kontotyp aus. Wählen Sie dann **Register** aus.
4. Wählen Sie die soeben erstellte Anwendung (Dienstprinzipal) aus und navigieren Sie dann zu **Certificates & secrets > + New client secret**.
5. Geben Sie eine Beschreibung für das Secret ein und legen Sie einen Ablaufzeitraum für das Secret fest. Wählen Sie dann **Add** aus.
6. Notieren Sie sich das erstellte Client-Secret, um es bei der Braze-Einrichtung zu verwenden.