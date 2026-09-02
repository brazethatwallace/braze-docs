---
nav_title: ワークスペース間の移行
article_title: ワークスペース間での電話番号と購読グループの移行
page_order: 3
description: "このリファレンス記事では、WhatsAppの電話番号と購読グループをワークスペース間で移行する方法について説明します。"
page_type: reference
channel:
  - WhatsApp
---

# WhatsAppの電話番号と購読グループをワークスペース間で移行する {#transfer-whatsapp-phone-numbers-and-subscription-groups-between-workspaces}

> このページでは、WhatsApp Businessアカウント（WABA）の電話番号とそれに関連する購読グループを、Braze内のあるワークスペースから別のワークスペースに移動する方法について説明します。このプロセスにより、BrazeでWhatsAppを使用する際の操作が効率化され、エンジニアリングの支援が不要になります。

## 前提条件 {#prerequisites}

- 元のワークスペースと新しいワークスペースの両方で、[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)「Manage Subscription Groups」があることを確認してください。
- WABAは複数の[Brazeクラスター]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)にまたがることはできません。1つの会社内で作業している場合、これが発生する可能性は低いです。

## 電話番号と購読グループの移行 {#transferring-a-phone-number-and-subscription-group}

### ステップ 1:購読グループをアーカイブする {#step-1-archive-the-subscription-group}

WhatsApp購読グループをアーカイブするには、以下のステップに従ってください。

1. 購読グループが現在存在するワークスペースに移動します。
2. **オーディエンス** > **購読グループ管理**に移動し、移動したいWhatsApp電話番号に関連付けられた購読グループを見つけます。
3. 購読グループのステータスにカーソルを合わせ、<i class="fa-solid fa-box-archive" aria-label="アーカイブ"></i> **アーカイブ**を選択します。これにより購読グループは非アクティブとしてマークされますが、削除はされません。

![購読グループの「アクティブ」ステータスにカーソルを合わせると表示される「アーカイブ」ボタン。]({% image_buster /assets/img/whatsapp/archive_subscription_group.png %}){: style="max-width:70%;"}

### ステップ 2:WhatsApp電話番号を新しいワークスペースに統合する {#step-2-integrate-the-whatsapp-phone-number-into-the-new-workspace}

1. WhatsApp電話番号を移動したいワークスペースに移動します。
2. **パートナー連携** > **テクノロジーパートナー** > **WhatsApp**に移動し、**WhatsApp Messaging Integration**セクションまでスクロールします。
3. **新規購読グループと電話番号を作成**オプションを選択します。
4. 統合プロセスを開始します。このプロセス中に、アーカイブされた購読グループから電話番号を選択できます。

### ステップ 3:統合を確認する {#step-3-verify-the-integration}

1. 統合が完了したら、WhatsApp電話番号が新しいワークスペースの購読グループに関連付けられていることを確認します。
2. そのWhatsApp電話番号を通じてメッセージの送受信ができることをテストして確認します。

## 考慮事項 {#considerations}

- WhatsApp電話番号を元のワークスペースに戻す必要がある場合は、同じステップを繰り返してください。移行先のワークスペースで購読グループをアーカイブし、元のワークスペースに統合します。
- 移行中にMeta Business マネージャーからWhatsApp電話番号を削除する必要はありません。