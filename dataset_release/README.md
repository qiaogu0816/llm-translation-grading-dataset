# 大语言模型辅助翻译批改研究：数据集

本仓库为硕士学位论文《大语言模型辅助翻译批改研究——基于错误识别的实证分析》的配套数据集。

## 内容

- `data/正式数据集.jsonl`：3 287 对含错样本，每行一个 JSON 对象。
- `schema.md`：字段说明。
- `scripts/load_dataset.py`：读取与基本统计示例。
- `model_results/`：10 个大语言模型的原始输出。因体积较大（约 308 MB），不放入 Git 仓库，将以 GitHub Release 附件形式发布。

## 样本字段

| 字段 | 说明 |
|---|---|
| `sample_id` | 样本编号，含赛事、年份、方向、题目、错误序号与版本号 |
| `source_text` | 原文片段 |
| `correct_translation` | 参考译文片段 |
| `incorrect_translation` | 含错译文片段 |
| `error_location` | 错误位置：`text`、`start`、`end`（字符级，左闭右开） |
| `error_type` | 错误类型：`level_1`（Accuracy / Terminology / Style / Audience appropriateness）与 `level_2`（13 类细类） |
| `error_severity` | 严重程度：`major` / `minor` |
| `judge_comment` | 专家评析原文（错误判定的依据） |
| `error_provenance` | 语料出处：赛事、年份、原文/参考译文文件、行号 |
| `language_direction` | 翻译方向：`en-zh` / `zh-en` |

## 使用说明

- 本数据集仅用于学术研究与教学，不得用于商业用途。
- 竞赛原文、参考译文与专家评析的著作权归原赛事、期刊与作者所有；引用与再分发请遵守相应版权规定。
- 模型输出中的模型名称已按论文编号（0—9）匿名化，映射见论文第三章。

## 引用

如使用本数据集，请引用：

> 作者. 大语言模型辅助翻译批改研究——基于错误识别的实证分析[D]. 硕士学位论文, 2026.

## 仓库地址

https://github.com/qiaogu0816/llm-translation-grading-dataset
