# 字段说明

每行为一个 JSON 对象，字段如下：

- `sample_id` (string)：样本唯一编号。
- `source_text` (string)：原文片段。
- `correct_translation` (string)：参考译文片段。
- `incorrect_translation` (string)：含错译文片段。
- `error_location` (object)：`text`（错误片段文本）、`start`/`end`（字符级位置，左闭右开）。
- `error_type` (object)：`level_1`（Accuracy、Terminology、Style、Audience appropriateness）、`level_2`（13 类细类）。
- `error_severity` (string)：`major` 或 `minor`。
- `judge_comment` (string)：专家评析原文。
- `error_provenance` (object)：`competition`、`year`、`source_file`、`translation_file`、`line_number`。
- `language_direction` (object)：`source_language`、`target_language`。
