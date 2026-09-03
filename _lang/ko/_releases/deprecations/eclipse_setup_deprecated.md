---
nav_title: Eclipse를 사용한 초기 SDK 설정
page_order: 1
page_type: update
noindex: true
description: "이 보관된 문서에서는 Eclipse를 사용하여 초기 SDK 설정을 수행하는 방법을 설명합니다. Braze는 Eclipse IDE에 대한 지원을 중단했습니다."
---

# Eclipse를 사용한 초기 SDK 설정 {#initial-sdk-setup-with-eclipse}

{% alert update %}
[Google이 Eclipse Android 개발자 도구 플러그인에 대한 지원을 서비스 종료함](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html)에 따라 Braze는 Eclipse IDE에 대한 지원을 중단했습니다. 마이그레이션 전에 Eclipse 통합에 대한 도움이 필요한 경우 [고객지원팀에 이메일을 보내]({{site.baseurl}}/support_contact/) 도움을 요청하세요.
{% endalert %}

## 1단계 {#step-1}
명령줄에서 [Braze Android GitHub 리포지토리](https://github.com/braze-inc/braze-android-sdk)를 복제합니다.

```bash
$ git clone git@github.com:braze-inc/braze-android-sdk.git
```

## 2단계 {#step-2}
Braze 프로젝트를 로컬 워크스페이스로 가져옵니다.

Eclipse에서:

  - **File** > **Import**로 이동합니다.

    ![파일 가져오기]({{site.baseurl}}/assets/img_archive/file_import.png)
  - **Android** > **Existing Android Code into Workspace**를 선택합니다.

    ![Android 가져오기]({{site.baseurl}}/assets/img_archive/android_import.png)
  - "Browse"를 클릭합니다.

    ![찾아보기]({{site.baseurl}}/assets/img_archive/click_browse.png)
  - Braze UI 프로젝트 폴더를 선택하고 "copy project into workspace"를 체크한 다음 "Finish"를 클릭합니다.

    ![Android UI 프로젝트 선택]({{site.baseurl}}/assets/img_archive/select_project_android.png)

## 3단계 {#step-3}
자신의 프로젝트에서 Braze를 참조합니다.
Eclipse에서:

  - 프로젝트를 마우스 오른쪽 버튼으로 클릭하고 "Properties"를 선택합니다.

    ![속성 클릭]({{site.baseurl}}/assets/img_archive/click_properties.png)
  - "Android"의 Library 섹션에서 "Add..."를 클릭하고 android-sdk-ui를 앱의 라이브러리로 추가합니다.

    ![Braze 추가]({{site.baseurl}}/assets/img_archive/add_appboy_ui.png)

## 4단계 {#step-4}
종속성 오류를 해결하고 빌드 대상을 수정합니다.

이때 Braze 코드에 오류가 표시될 수 있는데, 이는 종속성이 채워지지 않았거나 빌드 대상이 잘못되었을 가능성이 있기 때문입니다.

   - Braze UI 프로젝트를 마우스 오른쪽 버튼으로 클릭하고 **Properties** > **Android**를 선택하여 빌드 대상이 Braze의 현재 빌드 도구 버전으로 설정되어 있는지 확인합니다.

      ![빌드 대상]({{site.baseurl}}/assets/img_archive/build_target.png)
   - Braze UI 프로젝트를 마우스 오른쪽 버튼으로 클릭하고 **Properties** > **Java Build Path** > **Add JARs…**를 선택한 다음 기본 애플리케이션에서 'android-support-v4.jar'를 라이브러리로 추가합니다.

      ![지원 라이브러리]({{site.baseurl}}/assets/img_archive/android_support_v4.png)

## 5단계 {#step-5}

마지막 구성 요소를 추가합니다.

  - SDK 버전 1.10.0 이상의 경우 AndroidManifest.xml에
  `<service android:name="com.appboy.services.AppboyDataSyncService" />`
  를 추가해야 합니다. Eclipse는 매니페스트 병합을 지원하지 않기 때문입니다.

  - SDK 버전 1.7.0 이상의 경우, 라이브러리 프로젝트에서 "assets/fontawesome-webfont.ttf"를 애플리케이션에 복사해야 합니다. Eclipse는 라이브러리의 자산 폴더를 자동으로 포함하지 않습니다.