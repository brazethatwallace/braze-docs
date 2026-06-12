---
nav_title: ワークスペースの作成と管理
article_title: ワークスペースの作成と管理
page_order: 0
layout: dev_guide
guide_top_header: "ワークスペースの作成と管理"
guide_top_text: "この記事では、ワークスペースの作成、設定、管理方法について説明します。"
page_type: reference
description: "この記事では、ワークスペースの作成、設定、管理方法について説明します。"

guide_featured_title: "セクション記事"
guide_featured_list:
- name: ワークスペース間のデータ移行
  link: /docs/user_guide/administer/global/create_and_manage_workspaces/migrate_workspace_data
  image: /assets/img/braze_icons/switch-horizontal-01.svg
---

<br>

# ワークスペースの作成と管理 {#create-and-manage-workspaces}

> この記事では、ワークスペースの作成、設定、管理方法について説明します。

## ワークスペースとは {#what-is-a-workspace}

Braze で行うすべての操作はワークスペース内で行われます。ワークスペースは、関連するモバイルアプリや Web サイトのエンゲージメントを追跡・管理するための共有環境です。ワークスペースは、同じまたは非常に類似したアプリをグループ化します。たとえば、モバイルアプリの Android 版と iOS 版などです。

## ワークスペースの作成 {#creating-a-workspace}

### ステップ 1:計画を立てる {#step-1-have-a-plan}

開始する前に、チームと Braze のオンボーディングマネージャーと協力して、ユースケースに最適なワークスペース構成を決定してください。Braze でのワークスペース計画の詳細については、[はじめに: ワークスペース]({{site.baseurl}}/user_guide/get_started/workspaces/)ガイドをご覧ください。

### ステップ 2:ワークスペースを追加する {#step-2-add-your-workspace}

グローバルヘッダーのワークスペースドロップダウンから、新しいワークスペースを作成したり、既存のワークスペースを切り替えたりできます。

1. ワークスペースドロップダウンを選択し、<i class="fa-solid fa-square-plus" style="color: #0b8294;"></i> **Create workspace**を選択します。

![「Create workspace」ボタンが表示されたワークスペースドロップダウン。]({% image_buster /assets/img/workspaces/workspace_create.png %}){: style="max-width:60%;"}

{:start="2"}
2. ワークスペースに名前を付けます。

{% alert tip %}
社内の他のメンバーがワークスペースを簡単に見つけられるように、命名規則を採用することをお勧めします。たとえば、「Upon Voyage US – Production」や「Upon Voyage US – Staging」などです。
{% endalert %}

{:start="3"}
3. **Create**を選択します。Braze がワークスペースを作成するまで数秒かかる場合があります。

![「Upon Voyage US - Staging」という名前が入力された「Create Workspace」モーダル。]({% image_buster /assets/img/workspaces/workspace_name.png %}){: style="max-width:60%" }

**App Settings**ページに移動し、アプリインスタンスの追加を開始できます。このページには、**Settings** > **App Settings**からいつでもアクセスできます。

![アプリを追加するボタンが表示された Upon Voyage US - Staging ワークスペースの「App Settings」ページ。]({% image_buster /assets/img/workspaces/workspace_empty_state.png %})

### ステップ 3:アプリインスタンスを追加する {#step-3-add-your-app-instances}

ワークスペース内に収集されるさまざまなサイトやアプリを「アプリインスタンス」と呼びます。

1. **App Settings**ページから、**+ Add app**を選択します。
2. アプリインスタンスに名前を付け、このアプリインスタンスが対応するプラットフォームを選択します。複数のプラットフォームを選択すると、Braze は各プラットフォームに対して1つのアプリインスタンスを作成します。

![アプリの詳細を選択するオプションが表示された「Add New App to Upon Voyage US - Staging」モーダル。]({% image_buster /assets/img/workspaces/workspace_add_app.png %}){: style="max-width:60%" }

{:start="3"}
3. **Add app**を選択して確認します。

#### アプリ API キー {#app-api-keys}

アプリインスタンスを追加すると、その API キーにアクセスできるようになります。API キーは、アプリインスタンスと Braze API 間のリクエストに使用されます。API キーは、Braze SDKをアプリや Web サイトに統合する際にも重要です。

![API キーと SDK エンドポイントのフィールドが表示された Upon Voyage iOS アプリの設定ページ。]({% image_buster /assets/img/workspaces/app_api_key.png %})

{% alert note %}
各プラットフォームのアプリの各バージョンに対して、個別のアプリインスタンスを作成する必要があります。たとえば、iOS と Android の両方で Free 版と Pro 版のアプリがある場合、ワークスペース内に4つのアプリインスタンス（Free iOS アプリ、Free Android アプリ、Pro iOS アプリ、Pro Android アプリ）を作成します。これにより、各アプリインスタンスに1つずつ、合計4つの API キーが使用できるようになります。
{% endalert %}

#### ライブ SDK バージョン {#live-sdk-version}

特定のアプリのアプリ設定ページに表示されるライブ SDK バージョンは、1日の合計セッション数の5%以上を占め、かつ過去1日間に500セッション以上あるアプリバージョンのうち、最も高いバージョンです。

このフィールドは、Braze SDKをアプリまたは Web サイトに統合した後に表示されます。お使いのプラットフォームで Braze SDKの新しいバージョンが利用可能な場合、「Newer Version Available」というタグとともにここに表示されます。

![フィールド値が「5.4.0」で、新しいバージョンが利用可能であることを示すアイコンが表示された「Live SDK Version」セクション。]({% image_buster /assets/img/workspaces/app_live_sdk_version.png %})

### ステップ 4:必要に応じて繰り返す {#step-4-repeat-as-needed}

プランに必要な数のワークスペースを設定するために、ステップ 2 と 3 を繰り返します。ベストプラクティスとして、統合テストやCampaignテスト用のテストワークスペースを作成することをお勧めします。

{% alert tip %}
**テストワークスペースを追加する**<br>特定のユーザーを本番インスタンスから完全にサンドボックス化することで、アプリテストを実行できます。新しいワークスペースを作成し、アプリケーションを公開する際に、Braze が使用する API キーをテストワークスペースではなく本番ワークスペースのものに変更してください。
{% endalert %}

## ワークスペースの管理 {#managing-workspaces}

### お気に入りの追加 {#adding-favorites}

お気に入りのワークスペースを追加して、最もよく使用するワークスペースにさらに素早くアクセスできます。

![「お気に入りのワークスペース」タブが表示されたワークスペースドロップダウン。]({% image_buster /assets/img/workspaces/workspace_favorites.png %}){: style="max-width:50%;"}

お気に入りのワークスペースを追加するには:

1. プロファイルドロップダウンを選択し、**Manage your account**を選択します。
2. **Account Profile**セクションで、**Favorite workspaces**フィールドを見つけます。
3. リストからワークスペースを選択します。
4. **Save Changes**を選択します。

お気に入りに追加できるワークスペースの数に制限はありませんが、利便性のためにリストを短くしておくことをお勧めします。

### ワークスペースの名前変更 {#renaming-workspaces}

ワークスペースの名前を変更するには:

1. **Settings** > **App Settings**に移動します。
2. ワークスペース名にカーソルを合わせ、<i class="fa-solid fa-pencil" style="color: #0b8294;"></i>を選択します。
3. ワークスペースに新しい名前を付け、<i class="fa-solid fa-square-check" style="color: #0b8294;"></i> **Save**を選択します。

![ワークスペース名の横に表示される鉛筆アイコン。]({% image_buster /assets/img/workspaces/workspace_rename.gif %}){: style="max-width:50%;"}

### ワークスペースとアプリインスタンスの削除 {#deleting-workspaces-and-app-instances}

ワークスペースまたはアプリインスタンスを削除するには:

1. **Settings** > **App Settings**に移動します。
2. **Delete workspace**を選択して該当するワークスペースを削除するか、該当するアプリインスタンスの横にあるゴミ箱アイコンを選択します。

現在ユーザーのターゲティングに使用されているアプリインスタンスやワークスペース、または1,000人以上のユーザーがいるものは削除できません。削除しようとすると、エラーメッセージが表示されます。削除を進めるには、ダッシュボードリンクと削除するアプリインスタンスまたはワークスペースの名前を含む[サポートケースを作成]({{site.baseurl}}/user_guide/administer/personal/braze_support/)してください。

{% alert warning %}
ワークスペースの削除には注意してください！ワークスペースを削除すると、復元できません。
{% endalert %}

![ワークスペースを削除するボタンとアプリを削除するゴミ箱アイコンが表示されたアプリ設定ページ。]({% image_buster /assets/img/workspaces/workspace_delete.png %})

## よくある質問 {#frequently-asked-questions}

### アプリを更新する際に新しいワークスペースを作成すべきですか {#should-i-create-a-new-workspace-when-im-releasing-an-updated-app}

これは、アプリを更新するのか、まったく新しいアプリを作成するのかによって異なります。

#### アプリの更新 {#updating-your-app}

アプリを更新する場合は、同じワークスペース内に新しいアプリインスタンスを作成して、旧バージョンと新バージョンを分離する必要があります。これにより、セグメンテーション時にそのアプリを選択することで、新バージョンのユーザーを効果的にターゲットできます。旧バージョンのユーザーにメッセージを送信したい場合は、フィルターを使用して[以前のアプリバージョンをターゲット]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)できます。

新しいワークスペースを作成すると、ユーザーは旧ワークスペースと新ワークスペースの2か所に存在することになります。また、同じプッシュトークンを持つ可能性もあります。これにより、すでにアップグレード済みのユーザーが、旧ワークスペースのユーザーのみを対象としたマーケティングメッセージを受信してしまう可能性があります。

#### 新しいアプリのリリース {#releasing-a-new-app}

まったく新しいアプリをアプリストアにリリースする場合は、新しいワークスペースを作成する必要があります。新しいワークスペースを作成することで、古いアプリバージョンのすべての履歴データとユーザープロファイルはこの新しいワークスペースには存在しません。そのため、既存のユーザーが新しいアプリバージョンにアップグレードすると、古いアプリの行動データなしで新しいプロファイルが作成されます。

### 1つのワークスペースに複数のアプリインスタンスがあります。メッセージで単一のアプリのみをターゲットにするにはどうすればよいですか {#singular-app}

メッセージが特定のアプリのみをターゲットにするようにするには、選択したアプリインスタンスのユーザーのみをターゲットにするSegmentを追加します。これは、ユーザーが同じワークスペース内の異なるアプリインスタンスに対して2つのプッシュトークンを持っている可能性がある場合に特に重要です。このシナリオでは、ユーザーが現在使用しているアプリとは異なるアプリの通知を受信する可能性があります。理想的な体験とは言えません！

デフォルトでは、Segmentはワークスペース内のすべてのアプリと Web サイトをターゲットにします。1つのアプリまたは Web サイトのみをターゲットにするSegmentを設定するには:

1. 意味のある名前でSegmentを作成します。Braze では「All Users ({名前} {プラットフォーム})」という形式を使用しています。たとえば、「All Users (Upon Voyage iOS)」です。
2. **Apps and websites targeted**で、**Users from specific apps**を選択します。
3. **Specific apps**ドロップダウンで、アプリまたはサイトを選択します。

![特定のアプリのユーザーをターゲットにしているSegment。]({% image_buster /assets/img/workspaces/users_from_specific_apps_filter.png %})

このSegmentをメッセージに追加し、必要に応じて追加のSegmentやフィルターでオーディエンスをさらに絞り込むことができます。

#### Campaigns

Campaignsの場合は、コンポーザーの**Target Audiences**ステップにSegmentを追加します。

#### Canvas

Canvasでは、**Delivery Validations**セクションのメッセージステップにSegmentを追加します。配信バリデーションは、メッセージ送信時にオーディエンスが配信基準を満たしているかを再確認します。正しいアプリに配信されるように、各メッセージステップに配信バリデーションを指定することを忘れないでください。エントリレベルでのセグメンテーションは不要です。

{% details 元のCanvasワークフローの手順を展開 %}

元のCanvasワークフローでは、**Audience**セクションのCanvasコンポーネントレベルにSegmentを追加します。エントリレベルでのセグメンテーションは不要です。

{% enddetails %}

## 次のステップ {#next-steps}

ワークスペースを作成したら、設定を行います:

- [ワークスペース設定]({{site.baseurl}}/user_guide/administer/global/workspace_settings/)で、API キー、メール設定、プッシュ設定などを設定します。
- [会社ユーザーの管理]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/)で、このワークスペースにユーザーを追加し、権限を割り当てます。