#!/bin/bash

source .env

docker run --runtime nvidia --gpus all \
	--name mx_vllm \
	-v ~/.cache/huggingface:/root/.cache/huggingface \
	--env "HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN" \
	-p 9000:8000 \
	--ipc=host \
	vllm/vllm-openai:latest \
	--model google/gemma-3-12b-it