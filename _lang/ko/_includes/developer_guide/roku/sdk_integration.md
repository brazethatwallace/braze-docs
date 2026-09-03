## Roku SDK 통합하기 {#integrating-the-roku-sdk}

### 1단계: 파일 추가 {#step-1-add-files}

Braze SDK 파일은 [Braze Roku SDK 리포지토리](https://github.com/braze-inc/braze-roku-sdk)의 `sdk_files` 디렉토리에서 찾을 수 있습니다.

1. `BrazeSDK.brs`를 앱의 `source` 디렉토리에 추가합니다.
2. `BrazeTask.brs`와 `BrazeTask.xml`을 앱의 `components` 디렉토리에 추가합니다.

### 2단계: 참조 추가 {#step-2-add-references}

다음 `script` 요소를 사용하여 메인 씬에 `BrazeSDK.brs`에 대한 참조를 추가합니다:

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### 3단계: 구성 {#step-3-configure}

`main.brs` 내에서 글로벌 노드에 Braze 구성을 설정합니다:

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

[SDK 엔드포인트]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)와 API 키는 Braze 대시보드에서 확인할 수 있습니다.

### 4단계: Braze 초기화 {#step-4-initialize-braze}

Braze 인스턴스를 초기화합니다:

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## 선택적 구성 {#optional-configurations}

### 로깅 {#logging}

Braze 통합을 디버깅하려면 Roku 디버그 콘솔에서 Braze 로그를 확인할 수 있습니다. 자세한 내용은 Roku 개발자 문서의 [코드 디버깅](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md)을 참조하세요.