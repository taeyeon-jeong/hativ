# hativ


## UI 요소 식별을 위한 속성

### **안정성 우선순위**

UI 요소를 식별하는 데 있어 안정성을 기준으로 우선순위를 나열하면 아래와 같습니다:

1. **`resource-id`**
2. **`accessibility id`** (또는 `content-description`)
3. **`xpath`**
4. **`instance`**
5. **`index`**

---

### **1. `resource-id`**

- **특징**:
    - Android에서 UI 요소에 부여된 **고유 식별자**입니다.
    - XML에서 정의된 요소에 대해 명확하게 고유한 값을 가지며, 앱이 변하지 않는 한 값이 바뀌지 않음.
    - 일반적으로 `com.example.app:id/button1`와 같은 형태로 표시됩니다.
- **장점**:
    - 가장 안정적이고 빠름.
    - 계층 구조나 요소의 순서에 영향을 받지 않음.
    - 유지 보수와 테스트 자동화에서 가장 선호되는 방법.
- **단점**:
    - 모든 UI 요소에 `resource-id`가 정의되어 있지는 않을 수 있음.
    - 개발자가 ID를 설정하지 않았다면 사용할 수 없음.
- **적합한 상황**:
    - **가장 우선적으로 사용**해야 함. `resource-id`가 존재한다면 이를 사용하는 것이 최선.

**예제**:

```python
element = driver.find_element_by_id("com.example.app:id/button1")
```

---

### **2. `accessibility id` (또는 `content-description`)**

- **특징**:
    - Android의 **`content-description`** 속성을 기반으로 한 식별자.
    - 주로 접근성을 위해 사용되며, Appium에서는 **`accessibility id`*라는 이름으로 호출됨.
    - 사람이 읽을 수 있는 이름(예: "Submit Button")으로 지정됩니다.
- **장점**:
    - 비교적 안정적이며, UI 변경에도 영향을 덜 받음.
    - 사람이 읽을 수 있는 값으로 유지 보수가 용이.
    - 계층 구조와 순서에 의존하지 않음.
- **단점**:
    - 모든 UI 요소에 정의되어 있지 않을 수 있음.
    - 개발자가 의미 있는 `content-description`을 설정하지 않았다면 사용할 수 없음.
- **적합한 상황**:
    - `resource-id`가 없는 경우 가장 안정적인 대안.

**예제**:

```python
element = driver.find_element_by_accessibility_id("Submit Button")
```

---

### **3. `xpath`**

- **특징**:
    - UI 요소의 계층 구조(Tree)와 속성을 기반으로 요소를 탐색.
    - 복잡한 조건(텍스트, 클래스 이름, 속성 등)을 결합하여 요소를 찾을 수 있음.
- **장점**:
    - 유연하며, 거의 모든 상황에서 요소를 찾을 수 있음.
    - `resource-id`나 `accessibility id`가 없는 요소도 검색 가능.
- **단점**:
    - UI 계층 구조가 변경되면 XPath를 수정해야 함.
    - 긴 XPath는 읽기 어려우며, 유지 보수가 어려움.
    - 검색 속도가 느림.
- **적합한 상황**:
    - 요소에 고유한 ID나 접근성 속성이 없고, 특정 조건으로 요소를 구분해야 할 때.

**예제**:

```python
element = driver.find_element_by_xpath("//android.widget.Button[@text='Submit']")
```

---

### **4. `instance`**

- **특징**:
    - 동일한 클래스 이름을 가진 UI 요소를 구분하기 위해 Appium에서 자동으로 할당한 **순번(0부터 시작)**.
    - 요소가 화면에 표시된 순서대로 번호를 매김.
- **장점**:
    - 같은 클래스의 요소가 여러 개 있는 경우, 빠르게 특정 요소를 선택 가능.
- **단점**:
    - UI 상태(동적 UI)나 계층 구조가 변경되면 `instance` 값이 달라질 수 있음.
    - 요소의 고유성이 보장되지 않음.
- **적합한 상황**:
    - 요소 식별이 제한적이고, UI가 고정적일 때만 사용.

**예제**:

```python
element = driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button").instance(0)')
```

---

### **5. `index`**

- **특징**:
    - 요소가 부모 요소 아래에서 몇 번째인지 나타냅니다.
    - UI 계층 구조(Tree)의 고정적인 위치를 기반으로 식별.
- **장점**:
    - 간단하고 빠르게 사용할 수 있음.
- **단점**:
    - UI 구조가 조금이라도 바뀌면 `index` 값이 변경되므로 매우 불안정.
    - 같은 부모 아래 동일한 클래스가 여러 개 있는 경우 식별이 어려움.
- **적합한 상황**:
    - 고정된 UI에서만 제한적으로 사용 가능.

**예제**:

```python
element = driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button").index(1)')
```

---

### **종합 평가**

- 가장 안정적인 방법은 **`resource-id`** > **`accessibility id`** > **`xpath`** > **`instance`** > **`index`** 순입니다.
- *`resource-id`*와 **`accessibility id`*는 UI 요소가 고유성을 가지며 변경 가능성이 낮아 **우선적으로 사용**해야 합니다.
- *`xpath`*는 유연하지만, UI 구조가 변하기 쉬운 경우에는 유지 보수가 어려우므로 최후의 수단으로 사용하는 것이 좋습니다.
- *`instance`*와 **`index`*는 UI 변경에 민감하므로 안정적인 테스트를 위해 **가능하면 피하는 것이 좋습니다**.

---

### **추천 전략**

1. **`resource-id`**: 항상 최우선으로 사용.
2. **`accessibility id`**: `resource-id`가 없을 경우 사용.
3. **`xpath`**: 조건 기반으로 복잡한 요소를 탐색해야 할 때 사용.
4. *`instance`*와 **`index`**: UI 구조가 절대 변경되지 않는다는 확신이 있을 때만 사용.
