import json
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
from datasets import Dataset

# Load the dataset
with open("./t5_train/training_data.json", "r") as f:
    data = json.load(f)

# Prepare the dataset
inputs = [item["input"] for item in data]
outputs = [json.dumps(item["output"]) for item in data]

# Tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

# Tokenize the inputs and outputs
train_encodings = tokenizer(inputs, truncation=True, padding=True, max_length=512)
with tokenizer.as_target_tokenizer():
    labels = tokenizer(outputs, truncation=True, padding=True, max_length=512)

# Convert to torch tensors
train_encodings = {key: torch.tensor(val) for key, val in train_encodings.items()}
labels = {key: torch.tensor(val) for key, val in labels.items()}

# Create a dataset
class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: val[idx] for key, val in self.encodings.items()}
        item['labels'] = self.labels['input_ids'][idx]
        return item

    def __len__(self):
        return len(self.labels['input_ids'])

train_dataset = CustomDataset(train_encodings, labels)

# Training arguments
training_args = TrainingArguments(
    output_dir='./t5_train/results',
    num_train_epochs=3,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./t5_train/logs',
    logging_steps=10,
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
)

# Train the model
trainer.train()

# Save the model
model.save_pretrained("./t5_train/trained_model")
tokenizer.save_pretrained("./t5_train/trained_model")