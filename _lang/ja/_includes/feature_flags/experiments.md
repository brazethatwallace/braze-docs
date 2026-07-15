# フィーチャーフラグ実験 {#feature-flag-experiments}

> フィーチャーフラグ実験では、コンバージョン率を最適化するためにアプリケーションの変更をA/Bテストできます。マーケターはフィーチャーフラグを使って、新機能がコンバージョン率にプラスまたはマイナスの影響を与えるかどうか、あるいはどのフィーチャーフラグプロパティのセットが最適かを判断できます。

## 前提条件 {#prerequisites}

実験でユーザーデータを追跡する前に、ユーザーがフィーチャーフラグを操作したタイミングをアプリで記録する必要があります。これをフィーチャーフラグインプレッションと呼びます。ユーザーがテスト中の機能を見たとき、あるいは見た可能性があるときは、コントロールグループであっても、必ずフィーチャーフラグのインプレッションを記録してください。

フィーチャーフラグのインプレッションを記録する方法については、[フィーチャーフラグを作成する]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#impressions)を参照してください。

{% tabs %}
{% tab Web %}

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewFeature();
} else {
  return new ExistingFeature();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("my-new-feature")
braze.logFeatureFlagImpression("my-new-feature")
if (featureFlag?.enabled == true) {
  return NewFeature()
} else {
  return ExistingFeature()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## フィーチャーフラグ実験を作成する {#creating-a-feature-flag-experiment}

### ステップ1: 実験を作成する {#step-1-create-an-experiment}

1. **メッセージング** > **キャンペーン**に移動し、**+ キャンペーンを作成**を選択します。
2. **フィーチャーフラグ実験**を選択します。
3. キャンペーンに明確で意味のある名前を付けます。

### ステップ2: 実験のバリアントを追加する {#step-2-add-experiment-variants}

次に、バリエーションを作成します。それぞれのバリアントについて、オンまたはオフにしたいフィーチャーフラグを選択し、割り当てられたプロパティを確認します。

機能のインパクトをテストするには、バリアントを使ってトラフィックを2つ以上のグループに分けます。1つのグループを「My control group」と名付け、そのフィーチャーフラグをオフにします。

フィーチャーフラグ実験では、合計9つのグループ（1つのコントロールグループと最大8つのバリアント）をサポートしています。

### ステップ3: プロパティを上書きする（オプション） {#step-3-overwrite-properties-optional}

特定のキャンペーンバリアントを受け取るユーザーに対して最初に設定したデフォルトのプロパティを上書きできます。

追加のデフォルトプロパティを編集、追加、削除するには、**メッセージング** > **フィーチャーフラグ**からフィーチャーフラグ自体を編集します。バリアントが無効になっている場合、SDKは指定されたフィーチャーフラグの空のプロパティオブジェクトを返します。

![「実験のバリアント」セクションにおいて、「link」変数キーが「/sales」で上書きされている様子]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

### ステップ4: ターゲットとするユーザーを選択する {#step-4-choose-users-to-target}

セグメントまたはフィルターのいずれかを使用して、[ターゲットユーザー]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users)を選択します。例えば、**Received Feature Flag Variant**フィルターを使用して、すでにA/Bテストを受けたユーザーをリターゲティングできます。

![フィルターグループ検索バーで「Received Feature Flag Variant」が強調表示された、フィーチャーフラグ実験の「ターゲット」ページ]({% image_buster /assets/img/feature_flags/variant-filter-dropdown.png %}){: style="max-width:70%"}

{% alert note %}
セグメントメンバーシップは、指定されたユーザーのフィーチャーフラグが更新されたときに計算されます。変更は、アプリがフィーチャーフラグをリフレッシュした後、または新しいセッションが開始されたときに利用可能になります。
{% endalert %}

### ステップ5: バリアントを配布する {#step-5-distribute-variants}

実験に使用するパーセンテージ分布を選択します。ベストプラクティスとして、実験開始後に配布を変更すべきではありません。

### ステップ6: コンバージョンを割り当てる {#step-6-assign-conversions}

Brazeでは、キャンペーンを受け取った後にユーザーが特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events)）を実行する頻度を追跡できます。ユーザーが指定されたアクションを取った場合にコンバージョンがカウントされる最大30日間のウィンドウを指定します。

### ステップ7: レビューして開始する {#step-7-review-and-launch}

最後の実験の構築が完了したら、その詳細を確認し、**実験を開始**を選択します。

## 結果を確認する {#reviewing-the-results}

フィーチャーフラグ実験が終了したら、実験のインプレッションデータを確認できます。**メッセージング** > **キャンペーン**に移動し、フィーチャーフラグ実験を含むキャンペーンを選択します。

### キャンペーン分析 {#campaign-analytics}

**キャンペーン分析**は、次のような実験のパフォーマンスの概要を提供します。

- インプレッションの総数
- ユニークインプレッション数
- 1次コンバージョン率
- メッセージによって生み出された総収益
- 推定オーディエンス

また、配信、オーディエンス、およびコンバージョンに関する実験の設定を表示することもできます。

### フィーチャーフラグ実験のパフォーマンス {#feature-flag-experiment-performance}

**フィーチャーフラグ実験パフォーマンス**は、メッセージがさまざまな次元でどの程度のパフォーマンスを示したかを表示します。表示される具体的な指標は、選択したメッセージングチャネルや、多変量テストを実施しているかどうかによって異なります。各バリアントに関連するフィーチャーフラグの値を確認するには、**プレビュー**を選択します。