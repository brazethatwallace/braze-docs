## Braze APIでのデータ記録（推奨） {#logging-data-with-the-braze-api-recommended}

Braze API [`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用して、分析をリアルタイムで記録できます。分析を記録するには、キーと値のペアフィールドに`braze_id`値を送信して（以下のスクリーンショットを参照）、更新するユーザープロファイルを識別します。

![キーと値のペアが3セットあるプッシュメッセージ。1.「Braze_id」がBraze IDを取得するためのLiquidコールとして設定されている。2.「cert_title」が「Braze Marketer Certification」に設定されている。3.「Cert_description」が「Certified Braze marketers drive...」に設定されている。]({% image_buster /assets/img/push_implementation_guide/push18.png %}){: style="max-width:80%;"}

## データの手動記録 {#logging-data-manually}

手動で記録するには、まずXcode内でワークスペースを設定してから、分析を作成、保存、および取得する必要があります。これには、開発者側でのカスタム作業が必要になります。以下に示すコードスニペットがこの対応に役立ちます。

分析はモバイルアプリケーションがその後起動されるまでBrazeに送信されないことに注意してください。つまり、解除設定に応じて、プッシュ通知が解除されてからモバイルアプリが起動し分析が取得されるまでに不確定な期間が存在することがよくあります。この時間バッファーがすべてのユースケースに影響するとは限りませんが、この影響を考慮し、必要に応じてアプリケーションを開くことでこの問題に対処するようにユーザージャーニーを調整してください。

![Brazeで分析が処理される方法を説明するグラフィック。1.分析データが作成される。2.分析データが保存される。3.プッシュ通知が解除される。4.プッシュ通知が解除されてからモバイルアプリが起動するまでの不確定な期間。5.モバイルアプリが起動する。6.分析データが受信される。7.分析データがBrazeに送信される。]({% image_buster /assets/img/push_implementation_guide/push13.png %})

### ステップ1:Xcode内でアプリグループを設定する {#step-1-configure-app-groups-within-xcode}

Xcodeで`App Groups`機能を追加します。アプリにワークスペースがない場合は、メインアプリターゲットの機能に移動し、`App Groups`をオンにして、**+** 追加ボタンをクリックします。次に、アプリのバンドルIDを使用してワークスペースを作成します。たとえば、アプリのバンドルIDが`com.company.appname`の場合、ワークスペースの名前を`group.com.company.appname.xyz`にすることができます。メインアプリターゲットとコンテンツ拡張ターゲットの両方で`App Groups`がオンになっていることを確認してください。

![メインアプリと拡張ターゲットでApp Groupsが有効になっているXcodeの署名と機能画面。]({% image_buster /assets/img/swift/push_story/add_app_groups.png %})

### ステップ2:コードスニペットの統合 {#step-2-integrate-code-snippets}

以下のコードスニペットは、カスタムイベント、カスタム属性、およびユーザー属性を保存・送信する方法についての参考情報です。このガイドでは`UserDefaults`の用語で説明しますが、コードの表現はヘルパーファイル`RemoteStorage`の形式になります。また、ユーザー属性の送信と保存に使用される追加のヘルパーファイル`UserAttributes`と`EventName Dictionary`もあります。

{% tabs local %}
{% tab Custom Events %}

#### カスタムイベントの保存 {#saving-custom-events}

カスタムイベントを保存するには、分析をゼロから作成する必要があります。これは、辞書を作成し、メタデータを入力し、ヘルパーファイルを使用してデータを保存することで行います。

1. イベントメタデータで辞書を初期化します
2. イベントデータを取得して保存するために`userDefaults`を初期化します
3. 既存の配列がある場合は、既存の配列に新しいデータを追加して保存します
4. 既存の配列がない場合は、新しい配列を`userDefaults`に保存します

{% subtabs global %}
{% subtab Swift %}
``` swift
func saveCustomEvent(with properties: [String: Any]? = nil) {
  // 1
  let customEventDictionary = Dictionary(eventName: "YOUR-EVENT-NAME", properties: properties)

  // 2
  let remoteStorage = RemoteStorage(storageType: .suite)

  // 3
  if var pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] {
    pendingEvents.append(contentsOf: [customEventDictionary])
    remoteStorage.store(pendingEvents, forKey: .pendingCustomEvents)
  } else {
  // 4
    remoteStorage.store([customEventDictionary], forKey: .pendingCustomEvents)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveCustomEvent:(NSDictionary<NSString *, id> *)properties {
  // 1
  NSDictionary<NSString *, id> *customEventDictionary = [[NSDictionary alloc] initWithEventName:@"YOUR-EVENT-NAME" properties:properties];

  // 2
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingEvents = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents] mutableCopy];

  // 3
  if (pendingEvents) {
    [pendingEvents addObject:customEventDictionary];
    [remoteStorage store:pendingEvents forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
  // 4
    [remoteStorage store:@[ customEventDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

#### カスタムイベントのBrazeへの送信 {#sending-custom-events-to-braze}

通知コンテンツアプリ拡張機能から保存された分析を記録するのに最適なタイミングは、SDKの初期化直後です。これは、保留中のイベントをループして「Event Name」キーをチェックし、Brazeに適切な値を設定し、次回この機能が必要なときのためにストレージをクリアすることで実行できます。

1. 保留中のイベントの配列をループします
2. `pendingEvents`辞書の各キーと値のペアをループします
3. 「Event Name」のキーを明示的にチェックし、それに応じて値を設定します
4. その他すべてのキーと値が`properties`辞書に追加されます
5. 個別のカスタムイベントを記録します
6. すべての保留中のイベントをストレージから削除します

{% subtabs global %}
{% subtab Swift %}
``` swift
func logPendingCustomEventsIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] else { return }

  // 1
  for event in pendingEvents {
    var eventName: String?
    var properties: [AnyHashable: Any] = [:]

  // 2
    for (key, value) in event {
      if key == PushNotificationKey.eventName.rawValue {
  // 3
        if let eventNameValue = value as? String {
          eventName = eventNameValue
        } else {
          print("Invalid type for event_name key")
        }
      } else {
  // 4
        properties[key] = value
      }
    }
  // 5
    if let eventName = eventName {
      AppDelegate.braze?.logCustomEvent(eventName, properties: properties)
    }
  }

  // 6
  remoteStorage.removeObject(forKey: .pendingCustomEvents)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingEventsIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingEvents = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents];

  // 1
  for (NSDictionary<NSString *, id> *event in pendingEvents) {
    NSString *eventName = nil;
    NSMutableDictionary *properties = [NSMutableDictionary dictionary];

  // 2
    for (NSString* key in event) {
      if ([key isEqualToString:@"event_name"]) {
  // 3
        if ([[event objectForKey:key] isKindOfClass:[NSString class]]) {
          eventName = [event objectForKey:key];
        } else {
          NSLog(@"Invalid type for event_name key");
        }
      } else {
  // 4
        properties[key] = event[key];
      }
    }
  // 5
    if (eventName != nil) {
      [AppDelegate.braze logCustomEvent:eventName properties:properties];
    }
  }

  // 6
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomEvents];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Custom Attributes %}

#### カスタム属性の保存 {#saving-custom-attributes}

カスタム属性を保存するには、分析をゼロから作成する必要があります。これは、辞書を作成し、メタデータを入力し、ヘルパーファイルを使用してデータを保存することで行います。

1. 属性メタデータで辞書を初期化します
2. 属性データを取得して保存するために`userDefaults`を初期化します
3. 既存の配列がある場合は、既存の配列に新しいデータを追加して保存します
4. 既存の配列がない場合は、新しい配列を`userDefaults`に保存します

{% subtabs global %}
{% subtab Swift %}
``` swift
func saveCustomAttribute() {
  // 1
  let customAttributeDictionary: [String: Any] = ["YOUR-CUSTOM-ATTRIBUTE-KEY": "YOUR-CUSTOM-ATTRIBUTE-VALUE"]

  // 2
  let remoteStorage = RemoteStorage(storageType: .suite)

  // 3
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] {
    pendingAttributes.append(contentsOf: [customAttributeDictionary])
    remoteStorage.store(pendingAttributes, forKey: .pendingCustomAttributes)
  } else {
  // 4
    remoteStorage.store([customAttributeDictionary], forKey: .pendingCustomAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
``` objc
- (void)saveCustomAttribute {
  // 1
  NSDictionary<NSString *, id> *customAttributeDictionary = @{ @"YOUR-CUSTOM-ATTRIBUTE-KEY": @"YOUR-CUSTOM-ATTRIBUTE-VALUE" };

  // 2
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes] mutableCopy];

  // 3
  if (pendingAttributes) {
    [pendingAttributes addObject:customAttributeDictionary];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
  // 4
    [remoteStorage store:@[ customAttributeDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

#### カスタム属性のBrazeへの送信 {#sending-custom-attributes-to-braze}

通知コンテンツアプリ拡張機能から保存された分析を記録するのに最適なタイミングは、SDKの初期化直後です。これは、保留中の属性をループし、Brazeで適切なカスタム属性を設定し、次回この関数が必要になったときに備えてストレージをクリアすることで実行できます。

1. 保留中の属性の配列をループします
2. `pendingAttributes`辞書の各キーと値のペアをループします
3. 対応するキーと値で個々のカスタム属性を記録します
4. ストレージからすべての保留中の属性を削除します

{% subtabs global %}
{% subtab Swift %}
``` swift
func logPendingCustomAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] else { return }

  // 1
  pendingAttributes.forEach { setCustomAttributesWith(keysAndValues: $0) }

  // 4
  remoteStorage.removeObject(forKey: .pendingCustomAttributes)
}

func setCustomAttributesWith(keysAndValues: [String: Any]) {
  // 2
  for (key, value) in keysAndValues {
  // 3
    if let value = value as? [String] {
      setCustomAttributeArrayWithKey(key, andValue: value)
    } else {
      setCustomAttributeWithKey(key, andValue: value)
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingCustomAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes];

  // 1
  for (NSDictionary<NSString*, id> *attribute in pendingAttributes) {
    [self setCustomAttributeWith:attribute];
  }

  // 4
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomAttributes];
}

- (void)setCustomAttributeWith:(NSDictionary<NSString *, id> *)keysAndValues {
  // 2
  for (NSString *key in keysAndValues) {
  // 3
    [self setCustomAttributeWith:key andValue:[keysAndValues objectForKey:key]];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab User Attributes %}

#### ユーザー属性の保存 {#saving-user-attributes}

ユーザー属性を保存する際には、どのタイプの属性が更新されているか（`email`、`first_name`、`phone_number`など）を判別するためにカスタムオブジェクトを作成することをお勧めします。オブジェクトは、`UserDefaults`からの保存・取得に対応している必要があります。これを行う方法の一例については、`UserAttribute`ヘルパーファイルを参照してください。

1. エンコードされた`UserAttribute`オブジェクトを対応する型で初期化します
2. イベントデータを取得して保存するために`userDefaults`を初期化します
3. 既存の配列がある場合は、既存の配列に新しいデータを追加して保存します
4. 既存の配列がない場合は、新しい配列を`userDefaults`に保存します

{% subtabs global %}
{% subtab Swift %}
``` swift
func saveUserAttribute() {
  // 1
  guard let data = try? PropertyListEncoder().encode(UserAttribute.userAttributeType("USER-ATTRIBUTE-VALUE")) else { return }

  // 2
  let remoteStorage = RemoteStorage(storageType: .suite)

  // 3
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] {
    pendingAttributes.append(contentsOf: [data])
    remoteStorage.store(pendingAttributes, forKey: .pendingUserAttributes)
  } else {
  // 4
    remoteStorage.store([data], forKey: .pendingUserAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveUserAttribute {
  // 1
  UserAttribute *userAttribute = [[UserAttribute alloc] initWithUserField:@"USER-ATTRIBUTE-VALUE" attributeType:UserAttributeTypeEmail];

  NSError *error;
  NSData *data = [NSKeyedArchiver archivedDataWithRootObject:userAttribute requiringSecureCoding:YES error:&error];

  if (error != nil) {
    // log error
  }
  // 2
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes] mutableCopy];

  // 3
  if (pendingAttributes) {
    [pendingAttributes addObject:data];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingUserAttributes];
  } else {
  // 4
    [remoteStorage store:@[data] forKey:RemoteStorageKeyPendingUserAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

#### ユーザー属性のBrazeへの送信 {#sending-user-attributes-to-braze}

通知コンテンツアプリ拡張機能から保存された分析を記録するのに最適なタイミングは、SDKの初期化直後です。これは、保留中の属性をループし、Brazeで適切なカスタム属性を設定し、次回この関数が必要になったときに備えてストレージをクリアすることで実行できます。

1. `pendingAttributes`データの配列をループします
2. 属性データからエンコードされた`UserAttribute`オブジェクトを初期化します
3. ユーザー属性タイプ（メール）に基づいて特定のユーザーフィールドを設定します
4. ストレージからすべての保留中のユーザー属性を削除します

{% subtabs global %}
{% subtab Swift %}
``` swift
func logPendingUserAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] else { return }

  // 1
  for attributeData in pendingAttributes {
  // 2
    guard let userAttribute = try? PropertyListDecoder().decode(UserAttribute.self, from: attributeData) else { continue }

  // 3
    switch userAttribute {
    case .email(let email):
      user?.email = email
    }
  }
  // 4
  remoteStorage.removeObject(forKey: .pendingUserAttributes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingUserAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes];

  // 1
  for (NSData *attributeData in pendingAttributes) {
    NSError *error;

  // 2
    UserAttribute *userAttribute = [NSKeyedUnarchiver unarchivedObjectOfClass:[UserAttribute class] fromData:attributeData error:&error];

    if (error != nil) {
      // log error
    }

  // 3
    if (userAttribute) {
      switch (userAttribute.attributeType) {
        case UserAttributeTypeEmail:
          [self user].email = userAttribute.userField;
          break;
      }
    }
  }
  // 4
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingUserAttributes];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Helper Files %}

#### ヘルパーファイル {#helper-files}

{% details RemoteStorage Helper File %}
{% subtabs global %}
{% subtab Swift %}
```swift
enum RemoteStorageKey: String, CaseIterable {

  // MARK: - Notification Content Extension Analytics
  case pendingCustomEvents = "pending_custom_events"
  case pendingCustomAttributes = "pending_custom_attributes"
  case pendingUserAttributes = "pending_user_attributes"
}

enum RemoteStorageType {
  case standard
  case suite
}

class RemoteStorage: NSObject {
  private var storageType: RemoteStorageType = .standard
  private lazy var defaults: UserDefaults = {
    switch storageType {
    case .standard:
      return .standard
    case .suite:
      return UserDefaults(suiteName: "YOUR-DOMAIN-IDENTIFIER")!
    }
  }()

  init(storageType: RemoteStorageType = .standard) {
    self.storageType = storageType
  }

  func store(_ value: Any, forKey key: RemoteStorageKey) {
    defaults.set(value, forKey: key.rawValue)
  }

  func retrieve(forKey key: RemoteStorageKey) -> Any? {
    return defaults.object(forKey: key.rawValue)
  }

  func removeObject(forKey key: RemoteStorageKey) {
    defaults.removeObject(forKey: key.rawValue)
  }

  func resetStorageKeys() {
    for key in RemoteStorageKey.allCases {
      defaults.removeObject(forKey: key.rawValue)
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@interface RemoteStorage ()

@property (nonatomic) StorageType storageType;
@property (nonatomic, strong) NSUserDefaults *defaults;

@end

@implementation RemoteStorage

- (id)initWithStorageType:(StorageType)storageType {
  if (self = [super init]) {
    self.storageType = storageType;
  }
  return self;
}

- (void)store:(id)value forKey:(RemoteStorageKey)key {
  [[self defaults] setValue:value forKey:[self rawValueForKey:key]];
}

- (id)retrieveForKey:(RemoteStorageKey)key {
  return [[self defaults] objectForKey:[self rawValueForKey:key]];
}

- (void)removeObjectForKey:(RemoteStorageKey)key {
  [[self defaults] removeObjectForKey:[self rawValueForKey:key]];
}

- (void)resetStorageKeys {
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingCustomEvents]];
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingCustomAttributes]];
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingUserAttributes]];
}

- (NSUserDefaults *)defaults {
  if (!self.defaults) {
    switch (self.storageType) {
      case StorageTypeStandard:
        return [NSUserDefaults standardUserDefaults];
        break;
      case StorageTypeSuite:
        return [[NSUserDefaults alloc] initWithSuiteName:@"YOUR-DOMAIN-IDENTIFIER"];
    }
  } else {
    return self.defaults;
  }
}

- (NSString*)rawValueForKey:(RemoteStorageKey)remoteStorageKey {
    switch(remoteStorageKey) {
    case RemoteStorageKeyPendingCustomEvents:
      return @"pending_custom_events";
    case RemoteStorageKeyPendingCustomAttributes:
      return @"pending_custom_attributes";
    case RemoteStorageKeyPendingUserAttributes:
      return @"pending_user_attributes";
    default:
      [NSException raise:NSGenericException format:@"Unexpected FormatType."];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
{% details UserAttribute Helper File %}
{% subtabs global %}
{% subtab Swift %}
```swift
enum UserAttribute: Hashable {
  case email(String?)
}

// MARK: - Codable
extension UserAttribute: Codable {
  private enum CodingKeys: String, CodingKey {
    case email
  }

  func encode(to encoder: Encoder) throws {
    var values = encoder.container(keyedBy: CodingKeys.self)

    switch self {
    case .email(let email):
      try values.encode(email, forKey: .email)
    }
  }

  init(from decoder: Decoder) throws {
    let values = try decoder.container(keyedBy: CodingKeys.self)

    let email = try values.decode(String.self, forKey: .email)
    self = .email(email)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation UserAttribute

- (id)initWithUserField:(NSString *)userField attributeType:(UserAttributeType)attributeType {
  if (self = [super init]) {
    self.userField = userField;
    self.attributeType = attributeType;
  }
  return self;
}

- (void)encodeWithCoder:(NSCoder *)encoder {
  [encoder encodeObject:self.userField forKey:@"userField"];
  [encoder encodeInteger:self.attributeType forKey:@"attributeType"];
}

- (id)initWithCoder:(NSCoder *)decoder {
  if (self = [super init]) {
    self.userField = [decoder decodeObjectForKey:@"userField"];

    NSInteger attributeRawValue = [decoder decodeIntegerForKey:@"attributeType"];
    self.attributeType = (UserAttributeType) attributeRawValue;
  }
  return self;
}

@end
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
{% details EventName Dictionary Helper File %}
{% subtabs global %}
{% subtab Swift %}
```swift
extension Dictionary where Key == String, Value == Any {
  init(eventName: String, properties: [String: Any]? = nil) {
    self.init()
    self[PushNotificationKey.eventName.rawValue] = eventName

    if let properties = properties {
      for (key, value) in properties {
        self[key] = value
      }
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation NSDictionary (Helper)

- (id)initWithEventName:(NSString *)eventName properties:(NSDictionary *)properties {
  self = [self init];
  if (self) {
    dict[@"event_name"] = eventName;

    for(id key in properties) {
      dict[key] = properties[key];
    }
  }
  return self;
}

@end
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
<br>
{% endtab %}
{% endtabs %}