# ComfyUI Easy Math 节点开发计划

## 1. 项目概述
创建一个名为 `ComfyUI_Easy_Math` 的自定义节点插件，提供一个集成的数学运算节点 `EasyMath`。该节点允许用户通过下拉菜单选择 11 种不同的数学运算方式。

## 2. 节点设计 (EasyMath)

### 2.1 输入 (Input)
节点将包含以下输入参数：

*   **`op` (Required)**: 下拉菜单，用于选择运算模式。
    *   选项:
        *   `Add` (加)
        *   `Subtract` (减)
        *   `Multiply` (乘)
        *   `Divide` (除)
        *   `Multiply Add` (乘后加)
        *   `Power` (幂)
        *   `Logarithm` (对数)
        *   `Square Root` (平方根)
        *   `Inverse Square Root` (平方根倒数)
        *   `Absolute` (绝对值)
        *   `Exponent` (指数)
*   **`a` (Required)**: `FLOAT` 类型，第一个操作数 (默认值: 0.0)。
*   **`b` (Required)**: `FLOAT` 类型，第二个操作数 (默认值: 0.0)。
    *   *注：在 Square Root, Inverse Square Root, Absolute, Exponent 模式下被忽略。*
*   **`c` (Optional)**: `FLOAT` 类型，第三个操作数 (默认值: 0.0)。
    *   *注：仅在 Multiply Add (A * B + C) 模式下使用。*

### 2.2 输出 (Output)
*   **`FLOAT`**: 运算结果（浮点数）。
*   **`INT`**: 运算结果（整数，向下取整或四舍五入，方便连接到需要整数的节点）。

### 2.3 运算逻辑与边界处理
| 运算模式 | 公式 | 边界/特殊情况处理 |
| :--- | :--- | :--- |
| Add | `a + b` | 无 |
| Subtract | `a - b` | 无 |
| Multiply | `a * b` | 无 |
| Divide | `a / b` | 若 `b == 0`，返回 `0.0` (防止崩溃) |
| Multiply Add | `a * b + c` | 无 |
| Power | `a ** b` | 若结果为复数或溢出，捕获异常并返回 `0.0` |
| Logarithm | `log(a, b)` | 若 `a <= 0` 或 `b <= 0` 或 `b == 1`，返回 `0.0` |
| Square Root | `sqrt(a)` | 若 `a < 0`，返回 `0.0` |
| Inverse Square Root | `1 / sqrt(a)` | 若 `a <= 0`，返回 `0.0` |
| Absolute | `abs(a)` | 无 |
| Exponent | `exp(a)` | 若溢出，返回最大浮点数或 `0.0` |

## 3. 文件结构
```
ComfyUI_Easy_Math/
├── __init__.py       # 插件入口，注册节点
├── nodes.py          # 节点逻辑实现
└── README.md         # 说明文档
```

## 4. 开发步骤
1.  **创建 `nodes.py`**: 实现 `EasyMath` 类，定义 `INPUT_TYPES`, `RETURN_TYPES`, `FUNCTION` 和具体的运算逻辑 `op`。
2.  **创建 `__init__.py`**: 导入 `EasyMath` 类并导出 `NODE_CLASS_MAPPINGS` 和 `NODE_DISPLAY_NAME_MAPPINGS`。
3.  **更新 `README.md`**: 添加节点说明、安装方法和功能列表。
