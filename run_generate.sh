#! /bin/bash

export CUDA_VISIBLE_DEVICES=0

python generate.py \
--load_8bit \
--base_model 'decapoda-research/llama-7b-hf' \
--lora_weights 'tloen/alpaca-lora-7b'