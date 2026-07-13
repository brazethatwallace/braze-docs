Brazeを使ってiOSプッシュ通知を送信する前に、[Appleの開発者向けドキュメント](https://developer.apple.com/documentation/usernotifications/establishing-a-token-based-connection-to-apns)に記載されているように、`.p8` プッシュ通知ファイルをアップロードする必要があります。

1. Apple開発者アカウントで、[**Certificates, Identifiers & Profiles**](https://developer.apple.com/account/ios/certificate)にアクセスします。
2. **Keys**で**All**を選択し、ページ上部の追加ボタン（+）をクリックします。
3. **Key Description**で、署名キーの一意の名前を入力します。
4. **Key Services**で**Apple Push Notification service (APNs)**チェックボックスをオンにし、**Continue**をクリックします。**Confirm**をクリックします。
5. キーIDをメモしておきます。**Download**をクリックして、キーを生成してダウンロードします。ダウンロードしたファイルは安全な場所に保存してください。このファイルは一度しかダウンロードできません。
6. Brazeで、**設定** > **アプリ設定**に移動し、**Apple Push Certificate**で`.p8`ファイルをアップロードします。開発用または本番用のプッシュ証明書のいずれかをアップロードできます。アプリがApp Storeで公開された後にプッシュ通知をテストするには、アプリの開発バージョン用に別のワークスペースを設定することをお勧めします。
7. プロンプトが表示されたら、アプリの[バンドルID](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier)、[キーID](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/)、[チームID](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id)を入力します。また、アプリの開発環境と本番環境のどちらに通知を送信するかを指定する必要があります。これはプロビジョニングプロファイルによって定義されます。
8. 完了したら、**保存**を選択します。