---
nav_title: メール到達性用語集
article_title: メール到達性用語集
layout: glossary_page
glossary_top_header: "メール到達性用語集"
glossary_top_text: "この用語集では、Brazeを通じてメールを送信する際に遭遇する可能性のある、一般的なメール到達性およびメールインフラに関する用語を定義しています。"
page_order: 1
page_type: glossary
description: "この用語集では、Brazeを通じてメールを送信する際に遭遇する可能性のある、一般的なメール到達性およびメールインフラに関する用語を定義しています。"
channel:
  - email

glossaries:
  - name: Allowlist
    description: ユーザーがメールの受信を許可し、ゴミ箱やスパムフォルダーにフィルタリングまたは振り分けられるべきではないと判断した連絡先のリストです。
  - name: Block
    description: ブロックバウンスは、メールボックスプロバイダーによってメールの配信が受け入れられなかった結果です。多くのメールボックスプロバイダーは、スパムやウイルスを送信していると報告されたIPアドレスやドメイン、またはメールポリシーやスパムフィルターに違反するコンテンツを含むメールをブロックします。SendGridでは「ブロック」を、一般的にソフトバウンスと呼ばれるものを指すために使用しています。SendGridにおけるブロックは、技術的または一時的な理由によりメールの配信が受け入れられなかった場合に発生します。
  - name: Blocklist
    description: スパムの既知の発信元として報告およびリストされたIPアドレスのリストです。パブリックブロックリストとプライベートブロックリストがあります。パブリックブロックリストは公開され、一般に利用可能です。多くの場合は無料サービスとして、場合によっては有料で提供されています。
  - name: Bounce
    description: ハードバウンスとも呼ばれ、バウンスしたアドレスは恒久的に配信不能であり、以降の送信から除外されます。Brazeにおけるバウンスの詳細については、メール分析用語集の<a href="/docs/user_guide/channels/email/reporting/analytics_glossary#bounces">バウンス</a> を参照してください。
  - name: Bulk folder
    description: 一部のメールクライアントでは、迷惑メールフォルダーまたはスパムフォルダーとも呼ばれます。
  - name: CAN-SPAM Act
    description: "商業メールを規制する米国の法律です（正式名称：Controlling the Assault of Non-Solicited Pornography and Marketing Act of 2003）。"
  - name: Click rate
    description: 受信者がメッセージ内のリンクをクリックした割合です。詳細については、メール分析用語集の<a href="/docs/user_guide/channels/email/reporting/analytics_glossary#unique-clicks">ユニーククリック</a> を参照してください。
  - name: Content filters
    description: メール本文内のテキスト、単語、フレーズ、またはヘッダー情報に基づいてメールをブロックするソフトウェアフィルターです。
  - name: Deferred
    description: メッセージが最初の試行で配信できなかった場合、そのメッセージは遅延とみなされます。遅延されたメールのほとんどは最終的に配信されます。
  - name: Deliverability
    description: 到達性コミュニティにおいて、到達性は主に受信トレイに到達する能力に焦点を当てています。この率はBrazeが直接トラッキングできるものではないため、受信トレイへの配置を推測するために他の利用可能なデータを使用する必要があります。
  - name: Delivery rate
    description: 受信トレイへの配置やメールが開封されたかどうかに関係なく、配信が成功した割合です。詳細については、メール分析用語集の<a href="/docs/user_guide/channels/email/reporting/analytics_glossary#deliveries">配信率 %</a> を参照してください。
  - name: DKIM
    description: DomainKeys Identified Mailは、メッセージの転送中に組織がそのメッセージに対する責任を持つことを可能にします。その組織は、メッセージの発信者または仲介者として、メッセージのハンドラーです。その組織の評判が、メッセージの配信を信頼するかどうかを評価する基準となります。
  - name: DMARC
    description: Domain-based Message Authentication, Reporting & Conformanceは、メールフィッシングや詐欺を減らすために組織によって作成された技術仕様です。現在、Google、Yahoo、Microsoftを含むすべての主要なメールボックスプロバイダーで使用されています。
  - name: Drop
    description: SendGridは、各ユーザーのバウンス、スパムレポート、購読解除をトラッキングするためのメールリストを保持しています。ユーザーがアカウント内のこれらのリストに存在するメールアドレスにメッセージを送信した場合、SendGridは自動的にそのメッセージをドロップします（つまり、そのアドレスには送信しません）。
  - name: ESP (email service provider)
    description: メールマーケターにメール送信および転送機能を提供する企業です。今日の多くのマーケティング、CRM、カスタマーエンゲージメントプラットフォームにはメール送信コンポーネントが含まれており、メール送信機能に関してESPと呼ばれることが一般的です。例としては、ConstantContact、MailChimp、Emarsys、Salesforce Marketing Cloud、Cheetah Digital、Sailthruなどがあります。
  - name: Feedback loop (FBL)
    description: 送信者がスパムレポートの通知を受け取り、スパムレポート率を計算して、今後の送信からそのアドレスを削除できるようにするメカニズムです。
  - name: Hard bounce
    description: 無効、閉鎖済み、または存在しないメールアカウントに送信されたメッセージです。通常、ハードバウンスしたメールは500番台のSMTP応答コードで識別できます。詳細については、メール分析用語集の<a href="/docs/user_guide/channels/email/reporting/analytics_glossary#hard-bounce">ハードバウンス</a> を参照してください。
  - name: IP
    description: インターネットに接続された各デバイスに割り当てられる一意の番号です。
  - name: ISP (Internet Service Provider)
    description: AT&T、British Telecom、Comcast（Xfinity）、Cox、Orange、Sky、Spectrum、Tiscali、TalkTalk、Virginなど、消費者にインターネットサービスを提供する企業です。Gmail、Yahoo、Microsoftなどのメールボックスプロバイダーも口語的に含まれます。
  - name: List hygiene
    description: ハードバウンスや購読解除された名前をメーリングリストから削除し、リストを維持管理する行為です。
  - name: List-Unsubscribe
    description: List-Unsubscribeヘッダーは、メッセージのヘッダー部分に含めることができるテキストで、受信者が今後のメッセージを自動的に停止するために選択できる購読解除ボタンを表示できるようにします。
  - name: Mailbox provider (MBP)
    description: Gmail、Yahoo、Microsoftなど、受信者にメールアクセスを提供するプロバイダーです。
  - name: MX record
    description: MXレコードは、ドメインネームシステム（DNS）におけるリソースレコードの一種で、Simple Mail Transfer Protocol（SMTP）を使用してインターネットメールをどのようにルーティングするかを指定します。
  - name: NDR (non-delivery report)
    description: メール受信者がメールの配信を受け入れないことを選択した場合のフィードバックで、SMTP応答の形式で提供されます。NDRはバウンスと呼ばれることが多いです。
  - name: Opens unique rate
    description: 開封トラッキングピクセルが読み込まれた割合で、ユニーク受信者のみをカウントします（重複なし）。詳細については、メール分析用語集の<a href="/docs/user_guide/channels/email/reporting/analytics_glossary#unique-opens">ユニーク開封</a> を参照してください。
  - name: Phishing
    description: 詐欺師が本物に見えるメールを使用して、受信者からクレジットカードや銀行口座番号、社会保障番号、その他の個人を特定できる情報（PII）などの機密個人情報を騙し取る、なりすまし詐欺の一形態です。
  - name: Re-engagement campaign
    description: 非アクティブまたは無反応のユーザーに送信されるメールキャンペーンで、開封、クリック、コンバージョンの形でメールへの再エンゲージメントを促すことを目的としています。再エンゲージメントキャンペーンは、単独のキャンペーンとして、または一連のキャンペーンとして非アクティブユーザーに送信できます。
  - name: Reverse DNS (rDNS)
    description: ドメイン名がIPアドレスに一致するのではなく、IPアドレスがドメイン名に正しく一致するプロセスです。スパムフィルターやプログラムがIPアドレスをドメイン名に一致させることができない場合、メールを拒否する可能性があります。
  - name: Smart Network Data Services (SNDS)
    description: Windows Live Hotmailが提供するSNDSは、Hotmail購読者に実際に送信されたメールに基づいて送信者にデータを提供します。報告される指標には、苦情、SmartScreenフィルターの結果、スパムトラップへのヒットが含まれます。
  - name: Soft bounce
    description: 「メールボックスがいっぱい」「ユーザーの容量超過」「スパムのような特性によりメールがブロックされた」「組織のポリシーに違反しているためメッセージが拒否された」「サーバーが一時的に利用不可」など、一時的または過渡的な問題によるバウンスです。SendGridではこれらを「ブロック」と呼んでいます。<br><br>一時的な問題と考えられるソフトバウンス（通常はSMTP 4xxコードのもの）への配信は、メッセージが配信されるか72時間が経過するまで再試行されます。ソフトバウンスしたメッセージが72時間後に配信できない場合、それ以上の配信試行は停止され、配信失敗はバウンスとしてカウントされます。詳細については、メール分析用語集の<a href="/docs/user_guide/channels/email/reporting/analytics_glossary#soft-bounce">ソフトバウンス</a> を参照してください。
  - name: Spam
    description: 不要なメールです。指標においては、ユーザーがこれらのメールをスパムとしてマークする必要があります（メールはまず配信される必要があるため、このカウントは配信数に含まれます）。詳細については、メール分析用語集の<a href="/docs/user_guide/channels/email/reporting/analytics_glossary#spam">スパム</a> を参照してください。
  - name: SpamCop
    description: ブロックリストおよびIPアドレスデータベースで、以前は個人所有でしたが、現在はメールベンダーIronportの一部です。多くのメールボックスプロバイダーは、受信メールのIPアドレスをSpamCopの記録と照合し、そのアドレスがスパム苦情によりブロックリストに登録されているかどうかを確認します。
  - name: Spam rate
    description: 受信者がメッセージを閲覧中にスパムとしてマークした割合です。この率には、スパムフォルダーに振り分けられたメールは含まれません。また、GmailやiCloudなどフィードバックループを持たないメールボックスプロバイダーからの苦情も含まれません。詳細については、メール分析用語集の<a href="/docs/user_guide/channels/email/reporting/analytics_glossary#spam">スパム</a> を参照してください。
  - name: Spam trap
    description: ISPやアンチスパム組織がスパムを収集・検出するために使用するメールアドレスです。スパムトラップとも呼ばれます。詳細については、<a href="/docs/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps">到達性の落とし穴とスパムトラップ</a> を参照してください。
  - name: Suppression list
    description: Brazeには抑制リストはありませんが、<a href="/docs/user_guide/channels/email/best_practices/sunset_policies">サンセットポリシー</a> に記載されているとおり、サンセットポリシーを作成できます。メール購読の管理の詳細については、<a href="/docs/user_guide/channels/email/subscriptions">購読</a> を参照してください。
  - name: Throttling
    description: 送信者が一度に1つのメールボックスプロバイダーまたはメールサーバーに送信するメールメッセージの数を制限する手法です。一部のメールボックスプロバイダーは、メッセージを過剰に受信した場合にメールをバウンスします。
  - name: Transactional mail
    description: トランザクションメッセージは、CAN-SPAM法の下で「以前に合意された取引を促進、完了、または確認する」メールとして定義されています。商業メッセージとは異なり、トランザクションメッセージには米国郵便サービスの住所や購読解除リンクは必要ありません。

---