#! /bin/bash

export WORLD_SIZE=2
export CUDA_VISIBLE_DEVICES=0,1



torchrun --nproc_per_node=2 finetune.py \
--base_model "decapoda-research/llama-7b-hf" \
--output_dir "./lora-alpaca-7b-8bit" \
--wandb_project "alpaca" \
--wandb_run_name "7-8bit"

torchrun --nproc_per_node=2 finetune.py \
--base_model "decapoda-research/llama-13b-hf" \
--output_dir "./lora-alpaca-13b-8bit" \
--wandb_project "alpaca" \
--wandb_run_name "13-8bit"