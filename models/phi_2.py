from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch
import gc

def query_response(query):

        try:
                device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
                print("Using device: ",torch.cuda.get_device_name(0))

                tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2")
                tokenizer.pad_token = tokenizer.eos_token
                print('Tokenizer loaded successfully.')

                model = AutoModelForCausalLM.from_pretrained(
                "microsoft/phi-2",
                low_cpu_mem_usage=True,  
                device_map="auto",  
                torch_dtype=torch.float16,  
                quantization_config=BitsAndBytesConfig(load_in_4bit=True,bnb_4bit_compute_dtype=torch.float16)
                )
                
                print("Model loaded successfully.")

        except Exception as e:
                print(f"Error loading model: {e}")
                return None


        #input_text = "Write a short story about an alien."
        input = tokenizer(query, return_tensors="pt", padding=True)
        input = {key: value.to(device) for key, value in input.items()}

        output = model.generate(**input, max_length=80)

        #print(output,len(output))
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

        print("Successfully used Phi-2 LLM to generate response. Deleting model.")
        del model
        gc.collect()
        torch.cuda.empty_cache()

        return generated_text
