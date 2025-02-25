from transformers import T5Tokenizer, T5ForConditionalGeneration

# 加载训练好的模型和分词器
model = T5ForConditionalGeneration.from_pretrained('./t5_train/trained_model')
tokenizer = T5Tokenizer.from_pretrained('./t5_train/trained_model')

# 数据预处理函数
def preprocess_input(input_text):
    return tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)

# 生成JSON格式输出的函数
def generate_json(input_text):
    inputs = preprocess_input(input_text)
    outputs = model.generate(**inputs, max_length=512, num_beams=5, early_stopping=True)
    decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded_output

# 示例输入
input_text = "Generate Test: Before closing the window. paste Shortcut from #Task Manager#"
json_output = generate_json(input_text)
print(json_output)

# 更多测试示例
test_inputs = [
    "Generate Test: Before proceeding to the next step. open Historian Viewer to $default path$ from #Notification Area#",
    "Generate Test: After saving the current settings. click Button from #Control Panel#",
    "Generate Test: Wait for the confirmation message. set $example text$ to Textbox from #Mainwindow#"
]

for test_input in test_inputs:
    print(f"Input: {test_input}")
    print(f"Output: {generate_json(test_input)}")
    print()