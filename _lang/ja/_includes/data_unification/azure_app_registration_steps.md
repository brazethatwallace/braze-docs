1. Azureポータルで、Microsoft Entra管理センターに移動し、**App Registrations**を選択します。
2. **Identity > Applications > App registrations**の下にある**+ New registration**を選択します。
3. 名前を入力し、サポートされるアカウントの種類として`Accounts in this organizational directory only`を選択します。次に、**Register**を選択します。
4. 作成したアプリケーション（サービスプリンシパル）を選択し、**Certificates & secrets > + New client secret**に移動します。
5. シークレットの説明を入力し、シークレットの有効期限を設定します。次に、**Add**を選択します。
6. 作成されたクライアントシークレットをメモしておき、Brazeの設定で使用します。