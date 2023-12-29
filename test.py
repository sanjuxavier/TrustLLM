from trustllm.task import fairness
from trustllm.utils import file_process
from trustllm import config

evaluator = fairness.FairnessEval()

stereotype_recognition_data = file_process.load_json('stereotype_recognition_data_json_path')
evaluator.stereotype_recognition_eval(stereotype_recognition_data)

stereotype_agreement_data = file_process.load_json('stereotype_agreement_data_json_path')
evaluator.stereotype_agreement_eval(stereotype_agreement_data)

stereotype_query_test_data = file_process.load_json('stereotype_query_test_data_json_path')
evaluator.stereotype_query_eval(stereotype_query_test_data)


disparagement_data = file_process.load_json('disparagement_data_json_path')
evaluator.disparagement_eval(disparagement_data)

preference_data = file_process.load_json('preference_data_json_path')
evaluator.preference_eval(preference_data, type='plain')
evaluator.preference_eval(preference_data, type='force')


from trustllm.task import robustness
from trustllm.utils import file_process
from trustllm import config

evaluator = robustness.RobustnessEval()

advglue_data = file_process.load_json('advglue_data_json_path')
print(evaluator.advglue_eval(advglue_data))

advinstruction_data = file_process.load_json('advinstruction_data_json_path')
print(evaluator.advglue_eval(advinstruction_data))

ood_detection_data = file_process.load_json('ood_detection_data_json_path')
print(evaluator.ood_detection(ood_detection_data))

ood_generalization_data = file_process.load_json('ood_generalization_data_json_path')
print(evaluator.ood_generalization(ood_generalization_data))

from trustllm.task import privacy
from trustllm.utils import file_process
from trustllm import config

evaluator = privacy.PrivacyEval()


privacy_confAIde_data = file_process.load_json('privacy_confAIde_data_json_path')
print(evaluator.ConfAIDe_eval(privacy_confAIde_data))

privacy_awareness_query_data = file_process.load_json('privacy_awareness_query_data_json_path')
print(evaluator.awareness_query_eval(privacy_awareness_query_data, type='normal'))
print(evaluator.awareness_query_eval(privacy_awareness_query_data, type='aug'))

privacy_leakage_data = file_process.load_json('privacy_leakage_data_json_path')
print(evaluator.leakage_eval(privacy_leakage_data))

from trustllm.task import ethics
from trustllm.utils import file_process
from trustllm import config

evaluator = ethics.EthicsEval()


explicit_ethics_data = file_process.load_json('explicit_ethics_data_json_path')
print(evaluator.explicit_ethics_eval(explicit_ethics_data, eval_type='low'))
print(evaluator.explicit_ethics_eval(explicit_ethics_data, eval_type='high'))

implicit_ethics_data = file_process.load_json('implicit_ethics_data_json_path')
print(evaluator.implicit_ethics_eval(implicit_ethics_data, eval_type='ETHICS'))
print(evaluator.implicit_ethics_eval(implicit_ethics_data, eval_type='STEREOTYPE'))

emotional_awareness_data = file_process.load_json('emotional_awareness_data_json_path')
print(evaluator.emotional_awareness_eval(emotional_awareness_data))


