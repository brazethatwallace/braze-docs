{% multi_lang_include developer_guide/prerequisites/roku.md %}

## 이전에 저장된 데이터 삭제 {#wiping-previously-stored-data}

Roku SDK에는 `wipeData` 메서드가 포함되어 있지 않습니다. 다른 Braze SDK의 `wipeData()`와 기능적으로 동일한 초기 상태를 만들려면 네 개의 Braze 레지스트리 섹션을 지운 다음 SDK를 다시 초기화하세요.

Braze Roku SDK는 다음 레지스트리 섹션에 데이터를 유지합니다:

| 섹션 | 내용 |
|---------|----------|
| `braze.section.device_id` | Braze에서 이 기기를 식별하는 데 사용되는 기기 UUID입니다. |
| `braze.section.user_id` | 설정된 경우 외부 사용자 ID입니다. |
| `braze.section.session` | 활성 세션 UUID, 시작 시간 및 종료 시간입니다. |
| `braze.section.config` | 캐시된 SDK 구성 및 피처 플래그 데이터입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Wiping previously-stored data" }

### 1단계: 레지스트리 섹션 지우기 {#step-1-clear-the-registry-sections}

[`roRegistry.Delete()`](https://developer.roku.com/docs/references/brightscript/components/roregistry.md)를 사용하여 각 Braze 섹션을 삭제한 다음 `Flush()`를 호출하여 변경 사항을 유지합니다:

```brightscript
sub WipeBrazeData()
    registry = CreateObject("roRegistry")
    registry.Delete("braze.section.device_id")
    registry.Delete("braze.section.user_id")
    registry.Delete("braze.section.session")
    registry.Delete("braze.section.config")
    registry.Flush()
end sub
```

### 2단계: Braze SDK 다시 초기화 {#step-2-re-initialize-the-braze-sdk}

[Braze SDK를 초기화]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku)하면 SDK가 누락된 레지스트리 데이터를 정상적으로 처리합니다:

- 기기 ID 섹션이 비어 있으므로 SDK가 새 UUID를 생성하고 기기를 익명으로 처리합니다.
- 사용자 ID 섹션이 비어 있으므로 SDK가 익명 사용자(빈 문자열 `""`)로 기본 설정됩니다.
- 세션 섹션이 비어 있으므로 SDK가 새 세션을 시작합니다.
- 구성 섹션이 비어 있으므로 SDK가 서버에서 구성을 다시 가져옵니다.

{% alert note %}
Roku SDK는 레지스트리를 지울 때 서버 측 삭제 요청을 생성하지 않습니다. Braze에서 사용자를 제거해야 하는 경우 사용자의 `external_id` 또는 `braze_id`를 사용하여 [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)에 요청을 보내세요.
{% endalert %}